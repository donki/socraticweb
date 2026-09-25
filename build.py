"""Genera la web de sOCratic a partir de contenido/apps/*.md y, con --publicar, la sube a WordPress.com.

Salidas (copia local, fuente de verdad):
  sitio/          HTML autónomo: index.html, apps/<slug>.html, soporte/index.html, soporte/<slug>.html
  wordpress/      cuerpo de cada página en bloques de WordPress, tal cual se publica

Uso:
  python build.py              genera sitio/ y wordpress/
  python build.py --publicar   además crea o actualiza las páginas en socraticweb0.wordpress.com

El token OAuth se lee de D:\\dev\\secrets\\wordpress-socraticweb0.token (fuera del repo).
"""
import html
import json
import re
import sys
import time
from pathlib import Path

import markdown

RAIZ = Path(__file__).parent
APPS = RAIZ / "contenido" / "apps"
SITIO = RAIZ / "sitio"
WP = RAIZ / "wordpress"
TOKEN = Path(r"D:\dev\secrets\wordpress-socraticweb0.token")
SITE_ID = 257589098
WP_URL = "https://socraticweb0.wordpress.com"
CONTACTO = "jsoladelarosa@gmail.com"

# Orden del catálogo: primero lo que está en tienda, luego el resto.
PUBLICADA = re.compile(r"producci[oó]n|publicada", re.I)


# ---------------------------------------------------------------- lectura

def leer_app(ruta: Path) -> dict:
    texto = ruta.read_text(encoding="utf-8")
    nombre = re.search(r"^# (.+)$", texto, re.M).group(1).strip()
    cabecera, _, cuerpo = texto.partition("\n## ")
    cuerpo = "## " + cuerpo
    campos, clave = {}, None
    for linea in cabecera.splitlines():
        m = re.match(r"^- (\w+):\s*(.*)$", linea)
        if m:
            clave = m.group(1).lower()
            campos[clave] = [m.group(2).strip()] if m.group(2).strip() else []
        elif clave and re.match(r"^\s+[-*] ", linea):
            campos[clave].append(re.sub(r"^\s+[-*] ", "", linea).strip())
    secciones = {}
    for bloque in re.split(r"^## ", cuerpo, flags=re.M)[1:]:
        titulo, _, contenido = bloque.partition("\n")
        secciones[titulo.strip().lower()] = contenido.strip()

    def uno(k):
        return (campos.get(k) or [""])[0]

    tiendas = []
    for t in campos.get("tiendas", []):
        m = re.match(r"^\s*([^(:]+?)\s*\(([^)]*)\)\s*:\s*(\S+)", t)
        if not m:
            continue
        url = m.group(3).strip("<>().,;")
        if url.startswith("http"):
            tiendas.append({"tienda": m.group(1).strip(), "estado": m.group(2).strip(),
                            "url": url, "publicada": bool(PUBLICADA.search(m.group(2)))})
    github = (uno("github").split() or [""])[0].rstrip("/").removesuffix(".git")
    github = github if github.startswith("http") else ""
    releases = (uno("descarga_alternativa").split() or [""])[0]
    releases = releases if releases.startswith("http") else (github + "/releases" if github else "")
    return {
        "nombre": nombre, "slug": uno("slug"), "plataformas": uno("plataformas"),
        "lema": uno("lema"), "github": github, "releases": releases, "tiendas": tiendas,
        "secciones": secciones,
    }


def md(texto: str) -> str:
    return markdown.markdown(texto, extensions=["tables", "sane_lists"])


# ---------------------------------------------------------------- enlaces

def enlaces(app: dict) -> list[tuple[str, str]]:
    """Botones de descarga: las tiendas donde está publicada; si no hay ninguna, GitHub."""
    botones = [(f"Descargar en {t['tienda']}", t["url"]) for t in app["tiendas"] if t["publicada"]]
    # Una tienda de extensiones solo da la extensión: la aplicación se sigue bajando de GitHub.
    solo_extension = all(re.search(r"add-ons|chrome|firefox", t, re.I) for t, _ in botones)
    if (not botones or solo_extension) and app["releases"]:
        botones.append(("Descargar desde GitHub", app["releases"]))
    return botones


def estado(app: dict) -> str:
    pub = [t["tienda"] for t in app["tiendas"] if t["publicada"]]
    return "En " + " y ".join(pub) if pub else "Descarga desde GitHub"


# ---------------------------------------------------------------- bloques de WordPress

def wp_p(h: str) -> str:
    return f"<!-- wp:paragraph -->\n<p>{h}</p>\n<!-- /wp:paragraph -->"


def wp_h(texto: str, nivel: int = 2) -> str:
    attrs = "" if nivel == 2 else f' {{"level":{nivel}}}'
    return (f"<!-- wp:heading{attrs} -->\n<h{nivel} class=\"wp-block-heading\">{html.escape(texto)}"
            f"</h{nivel}>\n<!-- /wp:heading -->")


def wp_botones(botones: list[tuple[str, str]], secundario: bool = False) -> str:
    estilo = ' {"className":"is-style-outline"}' if secundario else ""
    clase = " is-style-outline" if secundario else ""
    items = "\n".join(
        f"<!-- wp:button{estilo} -->\n<div class=\"wp-block-button{clase}\"><a class=\"wp-block-button__link "
        f"wp-element-button\" href=\"{html.escape(u)}\">{html.escape(t)}</a></div>\n<!-- /wp:button -->"
        for t, u in botones)
    return f"<!-- wp:buttons -->\n<div class=\"wp-block-buttons\">{items}</div>\n<!-- /wp:buttons -->"


def bloques_raiz(h: str):
    """Elementos de primer nivel del HTML, respetando listas y citas anidadas."""
    pos = 0
    apertura = re.compile(r"<(h[1-6]|p|ul|ol|table|blockquote|pre|hr)\b[^>]*?(/?)>")
    while (m := apertura.search(h, pos)):
        tag = m.group(1)
        if tag == "hr":
            yield m.group(0), tag
            pos = m.end()
            continue
        nivel, i = 1, m.end()
        patron = re.compile(rf"<(/?){tag}\b[^>]*>")
        while nivel and (t := patron.search(h, i)):
            nivel += -1 if t.group(1) else 1
            i = t.end()
        yield h[m.start():i], tag
        pos = i


def wp_html(h: str) -> str:
    """Convierte el HTML de markdown en bloques nativos de WordPress."""
    salida = []
    for trozo, tag in bloques_raiz(h):
        if tag == "hr":
            salida.append(wp_separador())
        elif tag == "pre":
            trozo = trozo.replace("<pre", '<pre class="wp-block-code"', 1)
            salida.append(f"<!-- wp:code -->\n{trozo}\n<!-- /wp:code -->")
        elif tag.startswith("h"):
            nivel = int(tag[1])
            attrs = "" if nivel == 2 else f' {{"level":{nivel}}}'
            trozo = trozo.replace(f"<{tag}", f'<{tag} class="wp-block-heading"', 1)
            salida.append(f"<!-- wp:heading{attrs} -->\n{trozo}\n<!-- /wp:heading -->")
        elif tag == "p":
            salida.append(f"<!-- wp:paragraph -->\n{trozo}\n<!-- /wp:paragraph -->")
        elif tag in ("ul", "ol"):
            attrs = ' {"ordered":true}' if tag == "ol" else ""
            trozo = trozo.replace(f"<{tag}", f'<{tag} class="wp-block-list"', 1)
            salida.append(f"<!-- wp:list{attrs} -->\n{trozo}\n<!-- /wp:list -->")
        elif tag == "table":
            salida.append(f"<!-- wp:table -->\n<figure class=\"wp-block-table\">{trozo}</figure>\n<!-- /wp:table -->")
        else:
            salida.append(f"<!-- wp:quote -->\n<blockquote class=\"wp-block-quote\">{trozo[12:-13]}</blockquote>\n<!-- /wp:quote -->")
    return "\n\n".join(salida)


def wp_separador() -> str:
    return '<!-- wp:separator -->\n<hr class="wp-block-separator has-alpha-channel-opacity"/>\n<!-- /wp:separator -->'


def pagina_app_wp(app: dict) -> str:
    s = app["secciones"]
    partes = [
        wp_p(f"<strong>{html.escape(app['lema'])}</strong>"),
        wp_p(f"Plataformas: {html.escape(app['plataformas'])} · {html.escape(estado(app))}"),
        wp_botones(enlaces(app)),
    ]
    sec = [("Código fuente en GitHub", app["github"])] if app["github"] else []
    if app["releases"] and app["releases"] not in (u for _, u in enlaces(app)):
        sec.append(("Todas las versiones (GitHub)", app["releases"]))
    sec.append(("Guía de uso y soporte", f"{WP_URL}/soporte/{app['slug']}/"))
    partes.append(wp_botones(sec, secundario=True))
    partes.append(wp_html(md(s.get("descripción", ""))))
    partes.append(wp_h("Funciones principales"))
    partes.append(wp_html(md(s.get("funciones principales", ""))))
    if s.get("privacidad"):
        partes.append(wp_h("Privacidad"))
        partes.append(wp_html(md(s["privacidad"])))
        partes.append(wp_p(f'Más detalle en la <a href="{WP_URL}/privacidad/">política de privacidad</a>, '
                           "común a todas las aplicaciones."))
    return "\n\n".join(partes)


def pagina_soporte_wp(app: dict) -> str:
    s = app["secciones"]
    partes = [
        wp_p(f'Cómo funciona <a href="{WP_URL}/aplicaciones/{app["slug"]}/">{html.escape(app["nombre"])}</a> '
             "y qué hace cada opción."),
        wp_html(md(s.get("guía de uso (soporte)", ""))),
    ]
    if s.get("preguntas frecuentes"):
        partes.append(wp_h("Preguntas frecuentes"))
        partes.append(wp_html(md(s["preguntas frecuentes"])))
    partes.append(wp_separador())
    partes.append(wp_p(f'¿No encuentras lo que buscas? Escribe a <a href="mailto:{CONTACTO}">{CONTACTO}</a>'
                       + (f' o abre una incidencia en <a href="{app["github"]}/issues">GitHub</a>.' if app["github"] else ".")))
    return "\n\n".join(partes)


def tarjetas_wp(apps: list[dict], destino: str) -> str:
    """Rejilla de tarjetas en columnas de tres."""
    filas = []
    for i in range(0, len(apps), 3):
        cols = []
        for app in apps[i:i + 3]:
            url = f"{WP_URL}/{destino}/{app['slug']}/"
            cuerpo = "\n".join([
                f"<!-- wp:heading {{\"level\":3}} -->\n<h3 class=\"wp-block-heading\"><a href=\"{url}\">"
                f"{html.escape(app['nombre'])}</a></h3>\n<!-- /wp:heading -->",
                wp_p(html.escape(app["lema"])),
                wp_p(f"<em>{html.escape(app['plataformas'])} · {html.escape(estado(app))}</em>"),
            ])
            cols.append(f"<!-- wp:column -->\n<div class=\"wp-block-column\">{cuerpo}</div>\n<!-- /wp:column -->")
        while len(cols) < 3:
            cols.append("<!-- wp:column -->\n<div class=\"wp-block-column\"></div>\n<!-- /wp:column -->")
        filas.append(f"<!-- wp:columns -->\n<div class=\"wp-block-columns\">{''.join(cols)}</div>\n<!-- /wp:columns -->")
    return "\n\n".join(filas)


def portada_wp(apps: list[dict]) -> str:
    return "\n\n".join([
        wp_p("<strong>Aplicaciones libres para Android y Windows: sin anuncios, sin rastreadores y con "
             "tus datos bajo tu control.</strong>"),
        wp_p("sOCratic es un catálogo de aplicaciones pequeñas y honestas. Cada una hace una cosa y la hace "
             "bien, funciona sin conexión siempre que puede y no pide más permisos de los que necesita. "
             "Todas son gratuitas, completas y de código abierto con licencia MIT."),
        wp_botones([("Ver las aplicaciones", f"{WP_URL}/aplicaciones/"), ("Soporte", f"{WP_URL}/soporte/")]),
        wp_separador(),
        wp_h("Aplicaciones"),
        tarjetas_wp(apps, "aplicaciones"),
        wp_separador(),
        wp_h("Cómo trabajamos"),
        wp_html(md(
            "- **Privacidad primero.** Sin analítica, sin publicidad y sin rastreadores. Lo que escribes se "
            "queda en tu dispositivo, y si una aplicación sincroniza, viaja cifrado.\n"
            "- **Sin anuncios ni compras.** Las aplicaciones son gratuitas y completas.\n"
            "- **Software libre.** Todo el código está en GitHub con licencia MIT.\n"
            "- **Soporte de verdad.** Cada aplicación tiene su guía con todas sus opciones explicadas.")),
        wp_p(f'Contacto: <a href="mailto:{CONTACTO}">{CONTACTO}</a> · '
             f'<a href="{WP_URL}/privacidad/">Política de privacidad</a>'),
    ])


def indice_apps_wp(apps: list[dict]) -> str:
    return "\n\n".join([
        wp_p("Todas las aplicaciones de sOCratic. Si una está en una tienda, el enlace te lleva allí; si no, "
             "a su página de descargas en GitHub. El código de todas es público."),
        tarjetas_wp(apps, "aplicaciones"),
    ])


def indice_soporte_wp(apps: list[dict]) -> str:
    return "\n\n".join([
        wp_p("Guías de uso de cada aplicación: cómo se pone en marcha, qué hace cada pantalla y cada opción, "
             "y las dudas más habituales."),
        tarjetas_wp(apps, "soporte"),
        wp_separador(),
        wp_p(f'¿No está tu duda? Escribe a <a href="mailto:{CONTACTO}">{CONTACTO}</a>.'),
    ])


def privacidad_wp() -> str:
    fuente = (RAIZ / "CONTENIDO-PARA-GOOGLE-SITES.md").read_text(encoding="utf-8")
    texto = fuente.split("# PÁGINA 2 — Política de privacidad", 1)[1]
    texto = texto.split("**Texto:**", 1)[1].strip()
    return wp_html(md(texto))


# ---------------------------------------------------------------- HTML autónomo

def plantilla(titulo: str, cuerpo: str, prof: int) -> str:
    base = "../" * prof
    return f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(titulo)}</title>
<link rel="stylesheet" href="{base}estilo.css">
</head>
<body>
<div class="wrap">
<nav><a href="{base}index.html"><strong>sOCratic</strong></a>
<a href="{base}apps/index.html">Aplicaciones</a>
<a href="{base}soporte/index.html">Soporte</a>
<a href="{base}privacidad.html">Privacidad</a></nav>
<h1>{html.escape(titulo)}</h1>
{cuerpo}
<footer>sOCratic · <a href="mailto:{CONTACTO}">{CONTACTO}</a></footer>
</div>
</body>
</html>
"""


def local(bloques: str, prof: int) -> str:
    """El HTML local es el mismo contenido de WordPress sin comentarios de bloque y con enlaces relativos."""
    h = re.sub(r"<!-- /?wp:[^>]*-->\n?", "", bloques)
    base = "../" * prof

    def rel(m):
        partes = [p for p in (m.group(1) or "").split("/") if p]
        if not partes:
            return f'href="{base}index.html"'
        if partes[0] == "aplicaciones":
            partes[0] = "apps"
        if partes == ["privacidad"]:
            return f'href="{base}privacidad.html"'
        return f'href="{base}{"/".join(partes)}' + ('/index.html"' if len(partes) == 1 else '.html"')
    return re.sub(r'href="' + re.escape(WP_URL) + r'(/[^"]*)?"', rel, h)


# ---------------------------------------------------------------- publicar

def publicar(paginas: list[dict]):
    import requests
    tok = json.loads(TOKEN.read_text(encoding="utf-8-sig"))["access_token"]
    s = requests.Session()
    s.headers["Authorization"] = f"Bearer {tok}"
    api = f"https://public-api.wordpress.com/wp/v2/sites/{SITE_ID}"
    existentes = {}
    pag = 1
    while True:
        r = s.get(f"{api}/pages", params={"per_page": 100, "page": pag, "status": "publish,draft",
                                          "context": "edit"})
        r.raise_for_status()
        for p in r.json():
            existentes[(p["slug"], p["parent"])] = p["id"]
        if pag >= int(r.headers.get("X-WP-TotalPages", 1)):
            break
        pag += 1
    ids = {}
    for p in paginas:
        padre = ids.get(p["padre"], 0) if p["padre"] else 0
        datos = {"title": p["titulo"], "slug": p["slug"], "content": p["wp"], "status": "publish",
                 "parent": padre, "menu_order": p["orden"]}
        pid = existentes.get((p["slug"], padre))
        for intento in range(5):
            r = s.post(f"{api}/pages/{pid}" if pid else f"{api}/pages", json=datos)
            if r.status_code < 500:
                break
            # WordPress.com da 502 de vez en cuando aunque la página se haya guardado:
            # antes de reintentar se mira si ya existe para no duplicarla.
            time.sleep(3 * (intento + 1))
            if not pid:
                q = s.get(f"{api}/pages", params={"slug": p["slug"], "parent": padre,
                                                  "status": "publish,draft", "context": "edit"})
                if q.ok and q.json():
                    pid = q.json()[0]["id"]
        if not r.ok:
            raise SystemExit(f"{p['slug']}: {r.status_code} {r.text[:300]}")
        ids[p["clave"]] = r.json()["id"]
        print(("actualizada " if pid else "creada     ") + r.json()["link"])
    # La página de ejemplo que trae WordPress sobra.
    if ("about", 0) in existentes:
        s.delete(f"{api}/pages/{existentes[('about', 0)]}", params={"force": True})
    r = s.post(f"https://public-api.wordpress.com/rest/v1.2/sites/{SITE_ID}/settings", json={
        "blogname": "sOCratic",
        "blogdescription": "Aplicaciones libres, sin anuncios y sin rastreadores",
        "lang_id": 19,  # es
        "show_on_front": "page", "page_on_front": ids["portada"],
    })
    print("ajustes:", r.status_code, "" if r.ok else r.text[:300])


# ---------------------------------------------------------------- principal

def main():
    apps = [leer_app(p) for p in sorted(APPS.glob("*.md"))]
    apps.sort(key=lambda a: (not any(t["publicada"] for t in a["tiendas"]), a["nombre"].lower()))
    paginas = [
        {"clave": "portada", "slug": "inicio", "titulo": "sOCratic", "padre": None, "orden": 0,
         "wp": portada_wp(apps), "local": "index.html"},
        {"clave": "apps", "slug": "aplicaciones", "titulo": "Aplicaciones", "padre": None, "orden": 1,
         "wp": indice_apps_wp(apps), "local": "apps/index.html"},
        {"clave": "soporte", "slug": "soporte", "titulo": "Soporte", "padre": None, "orden": 2,
         "wp": indice_soporte_wp(apps), "local": "soporte/index.html"},
        {"clave": "privacidad", "slug": "privacidad", "titulo": "Política de privacidad", "padre": None,
         "orden": 3, "wp": privacidad_wp(), "local": "privacidad.html"},
    ]
    for i, app in enumerate(apps):
        paginas.append({"clave": f"app-{app['slug']}", "slug": app["slug"], "titulo": app["nombre"],
                        "padre": "apps", "orden": i, "wp": pagina_app_wp(app),
                        "local": f"apps/{app['slug']}.html"})
        paginas.append({"clave": f"sop-{app['slug']}", "slug": app["slug"], "titulo": f"{app['nombre']}: guía de uso",
                        "padre": "soporte", "orden": i, "wp": pagina_soporte_wp(app),
                        "local": f"soporte/{app['slug']}.html"})

    for p in paginas:
        destino = WP / (("" if not p["padre"] else ("aplicaciones" if p["padre"] == "apps" else "soporte") + "/")
                        + p["slug"] + ".html")
        destino.parent.mkdir(parents=True, exist_ok=True)
        destino.write_text(p["wp"], encoding="utf-8")
        if p["local"]:
            prof = p["local"].count("/")
            f = SITIO / p["local"]
            f.parent.mkdir(parents=True, exist_ok=True)
            f.write_text(plantilla(p["titulo"], local(p["wp"], prof), prof), encoding="utf-8")
    (SITIO / "estilo.css").write_text((RAIZ / "estilo.css").read_text(encoding="utf-8"), encoding="utf-8")
    print(f"{len(apps)} aplicaciones, {len(paginas)} páginas generadas en sitio/ y wordpress/")
    if "--publicar" in sys.argv:
        publicar(paginas)


if __name__ == "__main__":
    main()
