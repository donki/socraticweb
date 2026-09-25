"""Genera la web de sOCratic a partir de contenido/apps/*.md y, con --publicar, la sube a WordPress.com.

Salidas (copia local, fuente de verdad):
  sitio/          HTML autónomo: index.html, apps/<slug>.html, soporte/index.html, soporte/<slug>.html
  wordpress/      cuerpo de cada página en bloques de WordPress, tal cual se publica, más la cabecera
                  y el pie del tema (_cabecera.html, _pie.html)

Uso:
  python build.py              genera sitio/ y wordpress/
  python build.py --publicar   además crea o actualiza las páginas, la cabecera y el pie en
                               socraticweb0.wordpress.com

El diseño va entero en los atributos de los bloques (colores, bordes, espaciado, rejillas): el plan
gratuito de WordPress.com no admite plugins, CSS propio ni estilos globales, pero sí eso.

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
LEGAL = RAIZ / "contenido" / "legal"
SITIO = RAIZ / "sitio"
WP = RAIZ / "wordpress"
TOKEN = Path(r"D:\dev\secrets\wordpress-socraticweb0.token")
SITE_ID = 257589098
WP_URL = "https://socraticweb0.wordpress.com"
CONTACTO = "jsoladelarosa@gmail.com"
GITHUB_PERFIL = "https://github.com/donki"
TEMA = "pub/assembler"

# Paleta: la misma que la web local y el catálogo (índigo sobre pizarra).
TINTA = "#0f172a"
TEXTO = "#334155"
APAGADO = "#64748b"
LINEA = "#e2e8f0"
SUAVE = "#f8fafc"
ACENTO = "#4338ca"
ACENTO_SUAVE = "#eef2ff"
ACENTO_CLARO = "#c7d2fe"
VERDE = "#047857"
DEGRADADO = "linear-gradient(135deg,#1e1b4b 0%,#312e81 55%,#4338ca 100%)"
ANCHO = "1120px"
LECTURA = "780px"

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
    # Las fichas sangran las sublistas con 2 o 3 espacios; markdown necesita 4.
    texto = re.sub(r"^ {2,3}(?=(?:[-*]|\d+\.) )", "    ", texto, flags=re.M)
    # «<navegador>» y similares son marcadores del texto, no etiquetas: se escapan para que se vean.
    texto = re.sub(r"<(?!(?:br|strong|em|kbd|code|a|sub|sup)\b|/|https?:)([^<>\n]+)>", r"&lt;\1&gt;", texto)
    # URL sueltas → enlaces.
    texto = re.sub(r"(?<![(<\[\"'])\b(https?://[^\s)<>]+[^\s)<>.,;:])", r"<\1>", texto)
    return markdown.markdown(texto, extensions=["tables", "sane_lists", "toc"])


def etiquetas(app: dict) -> list[str]:
    """Plataformas en corto para las tarjetas. Lo que va tras «;» son requisitos, no plataformas."""
    pl = app["plataformas"]
    base = pl.split(";")[0]
    tags = []
    if re.search(r"\bandroid\b(?!\s*(tv|auto|\d))", base, re.I):
        tags.append("Android")
    if re.search(r"android tv", base, re.I):
        tags.append("Android TV")
    if re.search(r"android auto", base, re.I):
        tags.append("Android Auto")
    if re.search(r"windows", base, re.I):
        tags.append("Windows")
    if re.search(r"extensi[oó]n de navegador", pl, re.I):
        tags.append("Navegador")
    return tags


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
    return "En " + " y ".join(pub) if pub else "Descarga en GitHub"


def en_tienda(app: dict) -> bool:
    return any(t["publicada"] for t in app["tiendas"])


# ---------------------------------------------------------------- bloques de WordPress

def _attrs(d: dict) -> str:
    if not d:
        return ""
    j = json.dumps(d, ensure_ascii=False, separators=(",", ":"))
    # Igual que serialize_block_attributes(): nada que pueda cerrar el comentario.
    j = j.replace("--", "\\u002d\\u002d").replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026")
    return " " + j


def _v(valor: str) -> str:
    """«var:preset|spacing|50» → var(--wp--preset--spacing--50)."""
    if valor.startswith("var:"):
        return "var(--wp--" + valor[4:].replace("|", "--") + ")"
    return valor


def _css(style: dict | None) -> tuple[str, list[str]]:
    """Traduce el atributo style de un bloque a CSS en línea y a sus clases."""
    if not style:
        return "", []
    css, cls = [], []
    b = style.get("border", {})
    if "color" in b:
        css.append(f"border-color:{b['color']}")
        cls.append("has-border-color")
    for lado in ("top", "right", "bottom", "left"):
        if lado in b:
            css += [f"border-{lado}-color:{b[lado]['color']}", f"border-{lado}-width:{b[lado]['width']}",
                    f"border-{lado}-style:solid"]
    if "width" in b:
        css.append(f"border-width:{b['width']}")
    if "style" in b:
        css.append(f"border-style:{b['style']}")
    if "radius" in b:
        css.append(f"border-radius:{b['radius']}")
    c = style.get("color", {})
    if "text" in c:
        css.append(f"color:{c['text']}")
        cls.append("has-text-color")
    if "background" in c:
        css.append(f"background-color:{c['background']}")
        cls.append("has-background")
    if "gradient" in c:
        css.append(f"background:{c['gradient']}")
        cls.append("has-background")
    if style.get("elements", {}).get("link"):
        cls.append("has-link-color")
    d = style.get("dimensions", {})
    if "minHeight" in d:
        css.append(f"min-height:{d['minHeight']}")
    sp = style.get("spacing", {})
    for prop in ("padding", "margin"):
        for lado, valor in sp.get(prop, {}).items():
            css.append(f"{prop}-{lado}:{_v(valor)}")
    t = style.get("typography", {})
    for k, p in (("fontSize", "font-size"), ("fontStyle", "font-style"), ("fontWeight", "font-weight"),
                 ("lineHeight", "line-height"), ("letterSpacing", "letter-spacing"),
                 ("textTransform", "text-transform")):
        if k in t:
            css.append(f"{p}:{t[k]}")
    return ";".join(css), cls


def _abre(nombre: str, attrs: dict, tag: str, base: list[str], extra_cls: list[str] | None = None,
          otros: str = "") -> tuple[str, str]:
    css, cls = _css(attrs.get("style"))
    clases = base + (extra_cls or [])
    if attrs.get("className"):
        clases.append(attrs["className"])
    clases += cls
    st = f' style="{css}"' if css else ""
    return (f"<!-- wp:{nombre}{_attrs(attrs)} -->\n<{tag} class=\"{' '.join(clases)}\"{st}{otros}>",
            f"</{tag}>\n<!-- /wp:{nombre} -->")


def grupo(*hijos: str, style=None, align=None, layout=None, clase=None, tag="div") -> str:
    a = {}
    if tag != "div":
        a["tagName"] = tag
    if clase:
        a["className"] = clase
    if align:
        a["align"] = align
    if style:
        a["style"] = style
    if layout:
        a["layout"] = layout
    ini, fin = _abre("group", a, tag, ["wp-block-group"], [f"align{align}"] if align else [])
    return ini + "\n" + "\n\n".join(h for h in hijos if h) + "\n" + fin


def parrafo(h: str, style=None, size=None, clase=None) -> str:
    a = {}
    if clase:
        a["className"] = clase
    if style:
        a["style"] = style
    if size:
        a["fontSize"] = size
    extra = [f"has-{size}-font-size"] if size else []
    css, cls = _css(style)
    clases = extra + ([clase] if clase else []) + cls
    c = f' class="{" ".join(clases)}"' if clases else ""
    st = f' style="{css}"' if css else ""
    return f"<!-- wp:paragraph{_attrs(a)} -->\n<p{c}{st}>{h}</p>\n<!-- /wp:paragraph -->"


def titulo(h: str, nivel=2, style=None, size=None, ancla=None) -> str:
    a = {}
    if nivel != 2:
        a["level"] = nivel
    if ancla:
        a["anchor"] = ancla
    if style:
        a["style"] = style
    if size:
        a["fontSize"] = size
    css, cls = _css(style)
    clases = ["wp-block-heading"] + ([f"has-{size}-font-size"] if size else []) + cls
    st = f' style="{css}"' if css else ""
    idh = f' id="{ancla}"' if ancla else ""
    return f"<!-- wp:heading{_attrs(a)} -->\n<h{nivel}{idh} class=\"{' '.join(clases)}\"{st}>{h}</h{nivel}>\n<!-- /wp:heading -->"


def boton(texto: str, url: str, fondo=None, color=None, contorno=False) -> str:
    a = {}
    st = {"border": {"radius": "10px"}, "spacing": {"padding": {"top": "12px", "bottom": "12px",
                                                               "left": "22px", "right": "22px"}}}
    if color or fondo:
        st["color"] = {}
        if color:
            st["color"]["text"] = color
        if fondo:
            st["color"]["background"] = fondo
    if contorno:
        a["className"] = "is-style-outline"
        st["border"].update({"width": "1.5px", "style": "solid"})
    a["style"] = st
    css, cls = _css(st)
    externo = (' target="_blank" rel="noreferrer noopener"'
               if url.startswith("http") and not url.startswith(WP_URL) else "")
    return (f"<!-- wp:button{_attrs(a)} -->\n<div class=\"wp-block-button{' is-style-outline' if contorno else ''}\">"
            f"<a class=\"wp-block-button__link {' '.join(cls)} wp-element-button\" href=\"{html.escape(url)}\""
            f" style=\"{css}\"{externo}>{html.escape(texto)}</a></div>\n<!-- /wp:button -->")


def botones(*bs: str) -> str:
    if not bs:
        return ""
    return ("<!-- wp:buttons {\"style\":{\"spacing\":{\"blockGap\":{\"left\":\"12px\",\"top\":\"12px\"}}}} -->\n"
            "<div class=\"wp-block-buttons\">" + "\n".join(bs) + "</div>\n<!-- /wp:buttons -->")


def columnas(*cols: tuple[str, str], hueco="48px") -> str:
    partes = []
    for ancho, contenido in cols:
        partes.append(f"<!-- wp:column {{\"width\":\"{ancho}\"}} -->\n<div class=\"wp-block-column\" "
                      f"style=\"flex-basis:{ancho}\">{contenido}</div>\n<!-- /wp:column -->")
    return (f"<!-- wp:columns {{\"style\":{{\"spacing\":{{\"blockGap\":{{\"left\":\"{hueco}\",\"top\":\"32px\"}}}}}}}} -->\n"
            f"<div class=\"wp-block-columns\">" + "\n".join(partes) + "</div>\n<!-- /wp:columns -->")


def separador(color=LINEA) -> str:
    return (f"<!-- wp:separator {{\"style\":{{\"color\":{{\"background\":\"{color}\"}}}}}} -->\n"
            f"<hr class=\"wp-block-separator has-text-color has-alpha-channel-opacity has-background\" "
            f"style=\"background-color:{color};color:{color}\"/>\n<!-- /wp:separator -->")


def desplegable(pregunta: str, respuesta_html: str) -> str:
    st = {"border": {"bottom": {"color": LINEA, "width": "1px"}},
          "spacing": {"padding": {"top": "18px", "bottom": "18px"}}}
    css, _ = _css(st)
    return (f"<!-- wp:details{_attrs({'style': st})} -->\n<details class=\"wp-block-details\" style=\"{css}\">"
            f"<summary><strong>{pregunta}</strong></summary>\n{wp_html(respuesta_html)}</details>\n<!-- /wp:details -->")


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
            salida.append(separador())
        elif tag == "pre":
            trozo = trozo.replace("<pre", '<pre class="wp-block-code"', 1)
            salida.append(f"<!-- wp:code -->\n{trozo}\n<!-- /wp:code -->")
        elif tag.startswith("h"):
            nivel = max(2, int(tag[1]))
            ancla = re.search(r'\bid="([^"]+)"', trozo)
            interior = re.sub(r"^<h\d[^>]*>|</h\d>$", "", trozo)
            # Los tamaños del tema para h2/h3 son de portada; en textos largos, más contenidos.
            estilo = {"typography": {"fontWeight": "700", "lineHeight": "1.25"}, "color": {"text": TINTA},
                      "spacing": {"margin": {"top": "var:preset|spacing|50" if nivel == 2 else "var:preset|spacing|40"}}}
            if nivel >= 4:
                estilo["typography"]["fontSize"] = "1.1rem"
            salida.append(titulo(interior, nivel, ancla=ancla.group(1) if ancla else None, style=estilo,
                                 size={2: "large", 3: "medium"}.get(nivel)))
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


# ---------------------------------------------------------------- piezas del diseño

def seccion(*hijos, fondo=None, ancho=ANCHO, arriba="var:preset|spacing|70", abajo="var:preset|spacing|70",
            clase="soc-sec") -> str:
    st = {"spacing": {"padding": {"top": arriba, "bottom": abajo}, "margin": {"top": "0", "bottom": "0"}}}
    if fondo:
        st["color"] = {"background": fondo}
    return grupo(*hijos, align="full", style=st, clase=clase,
                 layout={"type": "constrained", "contentSize": ancho})


def rejilla(*hijos, minimo="18rem", hueco="24px") -> str:
    return grupo(*hijos, clase="soc-grid", style={"spacing": {"blockGap": hueco}},
                 layout={"type": "grid", "minimumColumnWidth": minimo})


def antetitulo(texto: str, color=ACENTO) -> str:
    return parrafo(html.escape(texto), style={
        "color": {"text": color},
        "typography": {"fontSize": "0.8rem", "fontWeight": "700", "letterSpacing": "0.12em",
                       "textTransform": "uppercase"}})


def cabecera_pagina(ante: str, h1: str, entrada: str, bs: list[str], extra: str = "", grande=True) -> str:
    """La franja oscura con degradado con la que empieza cada página."""
    hijos = [
        antetitulo(ante, ACENTO_CLARO),
        titulo(html.escape(h1), 1, size="x-large" if grande else "large",
               style={"typography": {"lineHeight": "1.08", "fontWeight": "700", "letterSpacing": "-0.02em"},
                      "color": {"text": "#ffffff"}}),
        parrafo(entrada, style={"color": {"text": "#e0e7ff"},
                                "typography": {"fontSize": "1.2rem", "lineHeight": "1.6"}}),
        botones(*bs),
        extra,
    ]
    return grupo(*hijos, align="full", clase="soc-hero soc-sec",
                 style={"color": {"gradient": DEGRADADO, "text": "#ffffff"},
                        "elements": {"link": {"color": {"text": "#ffffff"}}},
                        "spacing": {"padding": {"top": "var:preset|spacing|70" if not grande else "var:preset|spacing|80", "bottom": "var:preset|spacing|70" if not grande else "var:preset|spacing|80"},
                                    "margin": {"top": "0", "bottom": "0"}}},
                 layout={"type": "constrained", "contentSize": ANCHO})


def boton_claro(texto, url):
    return boton(texto, url, fondo="#ffffff", color=ACENTO)


def boton_contorno_claro(texto, url):
    return boton(texto, url, color="#ffffff", contorno=True)


def tarjeta(*hijos, fondo="#ffffff") -> str:
    return grupo(*hijos, clase="soc-card", style={
        "border": {"color": LINEA, "width": "1px", "radius": "16px"},
        "color": {"background": fondo},
        "spacing": {"padding": {"top": "28px", "bottom": "28px", "left": "28px", "right": "28px"},
                    "blockGap": "12px"}})


def tarjeta_app(app: dict, destino: str, llamada: str) -> str:
    url = f"{WP_URL}/{destino}/{app['slug']}/"
    return tarjeta(
        antetitulo(" · ".join(etiquetas(app))),
        titulo(f'<a href="{url}">{html.escape(app["nombre"])}</a>', 3, size="medium",
               style={"typography": {"fontWeight": "700", "lineHeight": "1.25"},
                      "elements": {"link": {"color": {"text": TINTA}, "typography": {"textDecoration": "none"}}}}),
        parrafo(html.escape(app["lema"]), style={"color": {"text": APAGADO}}),
        parrafo(html.escape(estado(app)), style={
            "color": {"text": VERDE if en_tienda(app) else APAGADO},
            "typography": {"fontSize": "0.85rem", "fontWeight": "600"}}),
        parrafo(f'<a href="{url}">{llamada} →</a>', style={
            "typography": {"fontWeight": "600"}, "elements": {"link": {"color": {"text": ACENTO}}}}),
    )


def encabezado_seccion(ante: str, h2: str, entrada: str = "") -> str:
    return "\n\n".join(x for x in [
        antetitulo(ante),
        titulo(html.escape(h2), 2, size="large", style={
            "typography": {"fontWeight": "700", "letterSpacing": "-0.02em", "lineHeight": "1.15"},
            "color": {"text": TINTA}}),
        parrafo(entrada, style={"color": {"text": APAGADO}, "typography": {"fontSize": "1.1rem"}}) if entrada else "",
    ] if x)


def llamada_soporte(texto_h: str, texto: str, bs: list[str], arriba=False) -> str:
    """Recuadro de ayuda al final de la página. Sin margen arriba si sigue a una sección con el suyo."""
    return seccion(
        grupo(
            titulo(texto_h, 2, size="medium", style={"typography": {"fontWeight": "700"},
                                                      "color": {"text": TINTA}}),
            parrafo(texto, style={"color": {"text": TEXTO}}),
            botones(*bs),
            clase="soc-card",
            style={"color": {"background": ACENTO_SUAVE}, "border": {"radius": "20px"},
                   "spacing": {"padding": {"top": "40px", "bottom": "40px", "left": "40px", "right": "40px"}}}),
        arriba="var:preset|spacing|70" if arriba else "0")


# ---------------------------------------------------------------- páginas

def portada_wp(apps: list[dict]) -> str:
    cifras = rejilla(*[
        grupo(parrafo(f"<strong>{n}</strong>", style={"typography": {"fontSize": "2.2rem", "lineHeight": "1"},
                                                     "color": {"text": "#ffffff"}}),
              parrafo(t, style={"color": {"text": ACENTO_CLARO}, "typography": {"fontSize": "0.95rem"}}),
              style={"spacing": {"blockGap": "6px"}})
        for n, t in [(str(len(apps)), "aplicaciones"), ("0", "anuncios"), ("0", "rastreadores"),
                     ("MIT", "licencia libre")]], minimo="9rem")
    cifras = grupo(cifras, style={"spacing": {"margin": {"top": "var:preset|spacing|60"}, "padding": {"top": "28px"}},
                                  "border": {"top": {"color": "rgba(255,255,255,0.2)", "width": "1px"}}})
    principios = [
        ("Privacidad primero", "Sin analítica, sin perfiles y sin rastreadores. Lo que escribes se queda en tu "
                               "dispositivo, y si una aplicación sincroniza, viaja cifrado."),
        ("Sin anuncios ni compras", "Las aplicaciones son gratuitas y completas. No hay versión «pro» ni "
                                    "funciones bloqueadas."),
        ("Código abierto", "Todo el código está en GitHub con licencia MIT: puedes leerlo, compilarlo y "
                           "comprobar lo que hace."),
        ("Soporte de verdad", "Cada aplicación tiene su guía, con todas sus pantallas y opciones explicadas, "
                              "y un correo al que escribir."),
    ]
    return "\n\n".join([
        cabecera_pagina(
            "Software libre para Android y Windows",
            "Aplicaciones que respetan tu privacidad",
            "Herramientas pequeñas y honestas: cada una hace una cosa y la hace bien, funciona sin conexión "
            "siempre que puede y no pide más permisos de los que necesita.",
            [boton_claro("Ver las aplicaciones", f"{WP_URL}/aplicaciones/"),
             boton_contorno_claro("Soporte", f"{WP_URL}/soporte/")],
            extra=cifras),
        seccion(
            encabezado_seccion("Catálogo", "Aplicaciones",
                               "Si una aplicación está en una tienda, el enlace te lleva allí; si no, a su "
                               "página de descargas en GitHub."),
            rejilla(*[tarjeta_app(a, "aplicaciones", "Ver aplicación") for a in apps])),
        seccion(
            encabezado_seccion("Cómo trabajamos", "Hechas para durar y para confiar en ellas"),
            rejilla(*[tarjeta(titulo(t, 3, size="medium", style={"typography": {"fontWeight": "700"},
                                                                   "color": {"text": TINTA}}),
                              parrafo(d, style={"color": {"text": APAGADO}}))
                      for t, d in principios], minimo="15rem"),
            fondo=SUAVE),
        llamada_soporte(
            "¿Necesitas ayuda con alguna aplicación?",
            f'Las guías explican cada pantalla y cada opción. Si tu duda no está, escribe a '
            f'<a href="mailto:{CONTACTO}">{CONTACTO}</a>.',
            [boton("Ir a soporte", f"{WP_URL}/soporte/", fondo=ACENTO, color="#ffffff")], arriba=True),
    ])


def indice_apps_wp(apps: list[dict]) -> str:
    return "\n\n".join([
        cabecera_pagina("Catálogo", "Aplicaciones",
                        "Todas gratuitas, sin anuncios y con el código en GitHub. Si una está en una tienda, "
                        "el enlace te lleva allí; si no, a su página de descargas.",
                        [boton_contorno_claro("Soporte", f"{WP_URL}/soporte/")], grande=False),
        seccion(rejilla(*[tarjeta_app(a, "aplicaciones", "Ver aplicación") for a in apps])),
    ])


def indice_soporte_wp(apps: list[dict]) -> str:
    return "\n\n".join([
        cabecera_pagina("Soporte", "Guías de uso",
                        "Cómo se pone en marcha cada aplicación, qué hace cada pantalla y cada opción, y las "
                        "dudas más habituales.",
                        [boton_contorno_claro(f"Escribir a {CONTACTO}", f"mailto:{CONTACTO}")], grande=False),
        seccion(rejilla(*[tarjeta_app(a, "soporte", "Ver guía") for a in apps])),
    ])


def dato(etiqueta: str, valor_html: str) -> str:
    return grupo(
        parrafo(html.escape(etiqueta), style={"color": {"text": APAGADO}, "typography": {
            "fontSize": "0.8rem", "fontWeight": "600", "textTransform": "uppercase", "letterSpacing": "0.08em"}}),
        parrafo(valor_html, style={"color": {"text": TINTA}}),
        style={"spacing": {"blockGap": "2px"}})


def pagina_app_wp(app: dict) -> str:
    s = app["secciones"]
    descarga = [boton_claro(t, u) if i == 0 else boton_contorno_claro(t, u)
                for i, (t, u) in enumerate(enlaces(app))]
    descarga.append(boton_contorno_claro("Guía de uso", f"{WP_URL}/soporte/{app['slug']}/"))
    tiendas = [f'<a href="{u}">{html.escape(t.removeprefix("Descargar en ").removeprefix("Descargar desde "))}</a>'
               for t, u in enlaces(app)]
    ficha = tarjeta(
        titulo("Ficha", 3, size="medium", style={"typography": {"fontWeight": "700"}, "color": {"text": TINTA}}),
        dato("Plataformas", html.escape(app["plataformas"])),
        dato("Descarga", " · ".join(tiendas)),
        dato("Licencia", "MIT, gratuita y sin anuncios"),
        dato("Código fuente", f'<a href="{app["github"]}">{app["github"].removeprefix("https://")}</a>')
        if app["github"] else "",
        dato("Soporte", f'<a href="{WP_URL}/soporte/{app["slug"]}/">Guía de uso</a> · '
                        f'<a href="mailto:{CONTACTO}">Correo</a>'),
        fondo=SUAVE)
    privacidad = tarjeta(
        titulo("Privacidad", 3, size="medium", style={"typography": {"fontWeight": "700"}, "color": {"text": TINTA}}),
        wp_html(md(s.get("privacidad", ""))),
        parrafo(f'<a href="{WP_URL}/privacidad/">Política de privacidad</a>',
                style={"typography": {"fontWeight": "600"}}))
    izquierda = "\n\n".join([
        titulo("Qué es", 2, size="large", style={"typography": {"fontWeight": "700"}, "color": {"text": TINTA}}),
        wp_html(md(s.get("descripción", ""))),
        titulo("Funciones principales", 2, size="large",
               style={"typography": {"fontWeight": "700"}, "color": {"text": TINTA},
                      "spacing": {"margin": {"top": "var:preset|spacing|50"}}}),
        wp_html(md(s.get("funciones principales", ""))),
    ])
    derecha = grupo(ficha, privacidad, style={"spacing": {"blockGap": "24px"}})
    return "\n\n".join([
        cabecera_pagina(" · ".join(etiquetas(app)) or "Aplicación", app["nombre"], html.escape(app["lema"]),
                        descarga, grande=False),
        seccion(columnas(("64%", izquierda), ("36%", derecha))),
        llamada_soporte(f"¿Dudas con {html.escape(app['nombre'])}?",
                        "La guía explica cómo ponerla en marcha, cada pantalla y cada opción, y las preguntas "
                        "más habituales.",
                        [boton("Abrir la guía", f"{WP_URL}/soporte/{app['slug']}/", fondo=ACENTO, color="#ffffff")]),
    ])


def preguntas(texto: str) -> list[tuple[str, str]]:
    """«**Pregunta.** Respuesta» (en la misma línea o en la siguiente) → pares."""
    pares = re.findall(r"^\*\*(.+?)\*\*[ \t]*\n?(.*?)(?=^\*\*|\Z)", texto, re.M | re.S)
    return [(p.strip(), r.strip()) for p, r in pares]


def pagina_soporte_wp(app: dict) -> str:
    s = app["secciones"]
    guia = md(s.get("guía de uso (soporte)", ""))
    indice = [(i, re.sub(r"<[^>]+>", "", t)) for i, t in re.findall(r'<h3 id="([^"]+)">(.*?)</h3>', guia)]
    faq = preguntas(s.get("preguntas frecuentes", ""))
    if faq:
        indice.append(("preguntas-frecuentes", "Preguntas frecuentes"))
    lista = "".join(f'<li><a href="#{i}">{t}</a></li>' for i, t in indice)
    contenido = [
        tarjeta(
            parrafo("<strong>En esta guía</strong>", style={"color": {"text": TINTA}}),
            f"<!-- wp:list -->\n<ul class=\"wp-block-list\">{lista}</ul>\n<!-- /wp:list -->",
            fondo=SUAVE) if indice else "",
        wp_html(guia),
    ]
    if faq:
        contenido.append(titulo("Preguntas frecuentes", 2, size="large", ancla="preguntas-frecuentes",
                                style={"typography": {"fontWeight": "700"}, "color": {"text": TINTA},
                                       "spacing": {"margin": {"top": "var:preset|spacing|70"}}}))
        contenido.append(grupo(*[desplegable(html.escape(p.rstrip()), md(r)) for p, r in faq],
                               style={"spacing": {"blockGap": "0"}}))
    ayuda = [boton("Escribir un correo", f"mailto:{CONTACTO}", fondo=ACENTO, color="#ffffff")]
    if app["github"]:
        ayuda.append(boton("Abrir una incidencia en GitHub", f"{app['github']}/issues", color=ACENTO, contorno=True))
    return "\n\n".join([
        cabecera_pagina(f"Soporte · {app['nombre']}", "Guía de uso",
                        f"Cómo funciona {html.escape(app['nombre'])}, pantalla a pantalla, y qué hace cada opción.",
                        [boton_claro("Ver la aplicación", f"{WP_URL}/aplicaciones/{app['slug']}/"),
                         boton_contorno_claro("Todas las guías", f"{WP_URL}/soporte/")], grande=False),
        seccion(*contenido, ancho=LECTURA),
        llamada_soporte("¿No encuentras lo que buscas?",
                        "Cuéntanos qué te pasa y con qué versión y dispositivo; respondemos en cuanto podemos.", ayuda),
    ])


def privacidad_wp() -> str:
    fuente = (RAIZ / "CONTENIDO-PARA-GOOGLE-SITES.md").read_text(encoding="utf-8")
    texto = fuente.split("# PÁGINA 2 — Política de privacidad", 1)[1]
    texto = texto.split("**Texto:**", 1)[1].strip()
    texto += "\n\n" + (LEGAL / "privacidad-web.md").read_text(encoding="utf-8")
    return "\n\n".join([
        cabecera_pagina("Legal", "Política de privacidad",
                        "Una sola política para todas las aplicaciones de sOCratic y para esta web: qué datos "
                        "se tocan, para qué y dónde se quedan.", [], grande=False),
        seccion(wp_html(md(texto)), ancho=LECTURA),
    ])


def pagina_legal(fichero: str, h1: str, entrada: str) -> str:
    texto = (LEGAL / fichero).read_text(encoding="utf-8")
    return "\n\n".join([
        cabecera_pagina("Legal", h1, entrada, [], grande=False),
        seccion(wp_html(md(texto)), ancho=LECTURA),
    ])


# ---------------------------------------------------------------- cabecera y pie del tema

def cabecera_tema() -> str:
    enlaces_nav = "\n".join(
        f"<!-- wp:navigation-link {{\"label\":\"{t}\",\"url\":\"{u}\",\"kind\":\"custom\",\"isTopLevelLink\":true}} /-->"
        for t, u in [("Aplicaciones", f"{WP_URL}/aplicaciones/"), ("Soporte", f"{WP_URL}/soporte/"),
                     ("Privacidad", f"{WP_URL}/privacidad/"), ("GitHub", GITHUB_PERFIL)])
    nav = ("<!-- wp:navigation {\"overlayMenu\":\"mobile\",\"style\":{\"typography\":{\"fontWeight\":\"500\"},"
           "\"spacing\":{\"blockGap\":\"28px\"}},\"layout\":{\"type\":\"flex\",\"justifyContent\":\"right\"}} -->\n"
           + enlaces_nav + "\n<!-- /wp:navigation -->")
    marca = ("<!-- wp:site-title {\"style\":{\"typography\":{\"fontWeight\":\"800\",\"letterSpacing\":\"-0.02em\"},"
             "\"elements\":{\"link\":{\"color\":{\"text\":\"" + TINTA + "\"},\"typography\":{\"textDecoration\":\"none\"}}}},"
             "\"fontSize\":\"medium\"} /-->")
    fila = grupo(marca, nav, align="wide",
                 style={"spacing": {"padding": {"top": "18px", "bottom": "18px"}}},
                 layout={"type": "flex", "flexWrap": "nowrap", "justifyContent": "space-between"})
    return grupo(fila, align="full", tag="header",
                 style={"color": {"background": "#ffffff"},
                        "border": {"bottom": {"color": LINEA, "width": "1px"}},
                        "spacing": {"margin": {"top": "0", "bottom": "0"}}},
                 layout={"type": "constrained"})


def aviso_cookies() -> str:
    """Aviso de cookies (bloque de Jetpack): va en el pie para que salga en todas las páginas.

    Su marcado copia save.jsx del bloque: <p> con el texto, el botón y <span> con los días.
    """
    st = {"color": {"text": "#ffffff", "background": TINTA},
          "elements": {"link": {"color": {"text": ACENTO_CLARO}}},
          "border": {"radius": "14px"},
          "spacing": {"padding": {"top": "1.25em", "right": "1.5em", "bottom": "1.25em", "left": "1.5em"}}}
    css, cls = _css(st)
    texto = (f'Esta web está alojada en WordPress.com, que usa cookies para sus estadísticas de visitas. '
             f'Puedes aceptarlas o ver cómo rechazarlas en la <a href="{WP_URL}/cookies/">política de cookies</a>.')
    attrs = {"render_from_template": True, "align": "wide", "consentExpiryDays": 365, "style": st}
    return (f"<!-- wp:jetpack/cookie-consent{_attrs(attrs)} -->\n"
            f"<div class=\"wp-block-jetpack-cookie-consent alignwide {' '.join(cls)}\" style=\"{css}\" "
            f"role=\"dialog\" aria-modal=\"true\"><p>{texto}</p>"
            + boton("Aceptar", "#", fondo="#ffffff", color=ACENTO)
            + "<span>365</span></div>\n<!-- /wp:jetpack/cookie-consent -->")


def pie_tema() -> str:
    claro = {"color": {"text": "#94a3b8"}, "typography": {"fontSize": "0.8rem", "fontWeight": "700",
                                                          "letterSpacing": "0.1em", "textTransform": "uppercase"}}
    lista = lambda pares: "\n".join(parrafo(f'<a href="{u}">{t}</a>', style={"spacing": {"margin": {"top": "6px"}}})
                                    for t, u in pares)
    cols = columnas(
        ("40%", "\n".join([
            parrafo("<strong>sOCratic</strong>", style={"color": {"text": "#ffffff"}, "typography": {"fontSize": "1.4rem"}}),
            parrafo("Aplicaciones libres para Android y Windows: sin anuncios, sin rastreadores y con tus datos "
                    "bajo tu control."),
        ])),
        ("20%", parrafo("Sitio", style=claro) + "\n" + lista([
            ("Aplicaciones", f"{WP_URL}/aplicaciones/"), ("Soporte", f"{WP_URL}/soporte/")])),
        ("20%", parrafo("Legal", style=claro) + "\n" + lista([
            ("Aviso legal", f"{WP_URL}/aviso-legal/"), ("Privacidad", f"{WP_URL}/privacidad/"),
            ("Cookies", f"{WP_URL}/cookies/")])),
        ("20%", parrafo("Contacto", style=claro) + "\n" + lista([
            ("Correo", f"mailto:{CONTACTO}"), ("GitHub", GITHUB_PERFIL)])),
    )
    return grupo(
        cols,
        separador("#1e293b"),
        parrafo("© 2026 sOCratic · Software libre con licencia MIT",
                style={"color": {"text": "#94a3b8"}, "typography": {"fontSize": "0.875rem"}}),
        aviso_cookies(),
        align="full", tag="footer", clase="soc-sec",
        style={"color": {"background": TINTA, "text": "#cbd5e1"},
               "elements": {"link": {"color": {"text": "#ffffff"}}},
               "spacing": {"padding": {"top": "var:preset|spacing|70", "bottom": "var:preset|spacing|50"},
                           "margin": {"top": "0", "bottom": "0"}}},
        layout={"type": "constrained", "contentSize": ANCHO})


# ---------------------------------------------------------------- HTML autónomo

def plantilla(titulo_pag: str, cuerpo: str, prof: int) -> str:
    base = "../" * prof
    return f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(titulo_pag)}</title>
<link rel="stylesheet" href="{base}estilo.css">
</head>
<body>
{cuerpo}
</body>
</html>
"""


def local(bloques: str, prof: int) -> str:
    """El HTML local es el mismo contenido de WordPress sin comentarios de bloque y con enlaces relativos."""
    h = re.sub(r"<!-- wp:site-title[^>]*/-->", f'<p class="soc-marca"><a href="{WP_URL}/">sOCratic</a></p>', bloques)
    h = re.sub(r"<!-- wp:navigation-link \{\"label\":\"([^\"]+)\",\"url\":\"([^\"]+)\"[^>]*/-->",
               r'<a href="\2">\1</a>', h)
    h = re.sub(r"<!-- /?wp:[^>]*-->\n?", "", h)
    base = "../" * prof

    def rel(m):
        partes = [p for p in (m.group(1) or "").split("/") if p]
        if not partes:
            return f'href="{base}index.html"'
        if partes[0] == "aplicaciones":
            partes[0] = "apps"
        if len(partes) == 1 and partes[0] in ("privacidad", "aviso-legal", "cookies"):
            return f'href="{base}{partes[0]}.html"'
        return f'href="{base}{"/".join(partes)}' + ('/index.html"' if len(partes) == 1 else '.html"')
    return re.sub(r'href="' + re.escape(WP_URL) + r'(/[^"]*)?"', rel, h)


# ---------------------------------------------------------------- publicar

def publicar(paginas: list[dict], partes: dict[str, str]):
    import requests
    tok = json.loads(TOKEN.read_text(encoding="utf-8-sig"))["access_token"]
    s = requests.Session()
    s.headers["Authorization"] = f"Bearer {tok}"
    api = f"https://public-api.wordpress.com/wp/v2/sites/{SITE_ID}"
    v11 = f"https://public-api.wordpress.com/rest/v1.1/sites/{SITE_ID}"

    def post(url, datos):
        for intento in range(5):
            r = s.post(url, json=datos)
            if r.status_code < 500:
                return r
            time.sleep(3 * (intento + 1))
        return r

    for slug, contenido in partes.items():
        r = post(f"{api}/template-parts/{TEMA}//{slug}", {"content": contenido})
        print(f"parte {slug}:", r.status_code, "" if r.ok else r.text[:300])

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
                 "parent": padre, "menu_order": p["orden"], "comment_status": "closed", "ping_status": "closed"}
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
        # Sin «Me gusta» ni botones de compartir bajo el contenido.
        post(f"{v11}/posts/{ids[p['clave']]}", {"likes_enabled": False, "sharing_enabled": False})
        print(("actualizada " if pid else "creada     ") + r.json()["link"])
    # La página de ejemplo que trae WordPress sobra.
    if ("about", 0) in existentes:
        s.delete(f"{api}/pages/{existentes[('about', 0)]}", params={"force": True})
    # Portada fija y comentarios cerrados: esto solo lo aplica la API v2 (la v1.2 contesta 200 y no hace nada).
    r = post(f"{api}/settings", {
        "title": "sOCratic", "description": "Aplicaciones libres, sin anuncios y sin rastreadores",
        "show_on_front": "page", "page_on_front": ids["portada"],
        "default_comment_status": "closed", "default_ping_status": "closed"})
    print("ajustes:", r.status_code, "" if r.ok else r.text[:300])
    r = post(f"https://public-api.wordpress.com/rest/v1.2/sites/{SITE_ID}/settings", {
        "lang_id": 19, "default_likes_enabled": False, "sharing_show": []})
    print("ajustes wpcom:", r.status_code, "" if r.ok else r.text[:300])


# ---------------------------------------------------------------- principal

def main():
    apps = [leer_app(p) for p in sorted(APPS.glob("*.md"))]
    apps.sort(key=lambda a: (not en_tienda(a), a["nombre"].lower()))
    paginas = [
        {"clave": "portada", "slug": "inicio", "titulo": "sOCratic", "padre": None, "orden": 0,
         "wp": portada_wp(apps), "local": "index.html"},
        {"clave": "apps", "slug": "aplicaciones", "titulo": "Aplicaciones", "padre": None, "orden": 1,
         "wp": indice_apps_wp(apps), "local": "apps/index.html"},
        {"clave": "soporte", "slug": "soporte", "titulo": "Soporte", "padre": None, "orden": 2,
         "wp": indice_soporte_wp(apps), "local": "soporte/index.html"},
        {"clave": "privacidad", "slug": "privacidad", "titulo": "Política de privacidad", "padre": None,
         "orden": 3, "wp": privacidad_wp(), "local": "privacidad.html"},
        {"clave": "aviso-legal", "slug": "aviso-legal", "titulo": "Aviso legal", "padre": None, "orden": 4,
         "wp": pagina_legal("aviso-legal.md", "Aviso legal",
                            "Quién está detrás de esta web y en qué condiciones se usa."),
         "local": "aviso-legal.html"},
        {"clave": "cookies", "slug": "cookies", "titulo": "Política de cookies", "padre": None, "orden": 5,
         "wp": pagina_legal("cookies.md", "Política de cookies",
                            "Qué cookies hay en esta web, quién las pone y cómo rechazarlas."),
         "local": "cookies.html"},
    ]
    for i, app in enumerate(apps):
        paginas.append({"clave": f"app-{app['slug']}", "slug": app["slug"], "titulo": app["nombre"],
                        "padre": "apps", "orden": i, "wp": pagina_app_wp(app),
                        "local": f"apps/{app['slug']}.html"})
        paginas.append({"clave": f"sop-{app['slug']}", "slug": app["slug"], "titulo": f"{app['nombre']}: guía de uso",
                        "padre": "soporte", "orden": i, "wp": pagina_soporte_wp(app),
                        "local": f"soporte/{app['slug']}.html"})
    partes = {"header": cabecera_tema(), "footer": pie_tema()}

    WP.mkdir(exist_ok=True)
    (WP / "_cabecera.html").write_text(partes["header"], encoding="utf-8")
    (WP / "_pie.html").write_text(partes["footer"], encoding="utf-8")
    for p in paginas:
        destino = WP / (("" if not p["padre"] else ("aplicaciones" if p["padre"] == "apps" else "soporte") + "/")
                        + p["slug"] + ".html")
        destino.parent.mkdir(parents=True, exist_ok=True)
        destino.write_text(p["wp"], encoding="utf-8")
        if p["local"]:
            prof = p["local"].count("/")
            f = SITIO / p["local"]
            f.parent.mkdir(parents=True, exist_ok=True)
            cuerpo = "\n".join(local(x, prof) for x in (partes["header"], p["wp"], partes["footer"]))
            f.write_text(plantilla(p["titulo"], cuerpo, prof), encoding="utf-8")
    (SITIO / "estilo.css").write_text((RAIZ / "estilo.css").read_text(encoding="utf-8"), encoding="utf-8")
    print(f"{len(apps)} aplicaciones, {len(paginas)} páginas generadas en sitio/ y wordpress/")
    if "--publicar" in sys.argv:
        publicar(paginas, partes)


if __name__ == "__main__":
    main()
