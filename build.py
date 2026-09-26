"""Genera la web de sOCratic en castellano e inglés y, con --publicar, la sube a WordPress.com.

Fuentes:
  contenido/apps/*.md         fichas de cada aplicación en castellano (y contenido/en/apps/ en inglés)
  contenido/legal/*.md        aviso legal, cookies y privacidad de la web (y contenido/en/legal/)
  contenido/imagenes.json     de dónde salen el icono y las capturas de cada aplicación
  CONTENIDO-PARA-GOOGLE-SITES.md  la política de privacidad de las aplicaciones (castellano)

Salidas (copia local, se commitean):
  contenido/img/  imágenes reducidas
  sitio/          HTML autónomo, con sitio/en/ para el inglés
  wordpress/      cuerpo de cada página en bloques tal cual se publica, cabeceras, pies y plantillas,
                  y medios.json (qué imagen es cuál en la biblioteca de WordPress)

Uso:
  python build.py              genera todo en local
  python build.py --publicar   además sube imágenes, páginas, cabeceras, pies y plantillas

El diseño va entero en los atributos de los bloques (colores, bordes, espaciado, rejillas): el plan
gratuito de WordPress.com no admite plugins, CSS propio ni estilos globales, pero sí eso.

El token OAuth se lee de D:\\dev\\secrets\\wordpress-socraticweb0.token (fuera del repo).
"""
import hashlib
import html
import json
import re
import shutil
import sys
import time
from pathlib import Path

import markdown

RAIZ = Path(__file__).parent
CONTENIDO = RAIZ / "contenido"
SITIO = RAIZ / "sitio"
WP = RAIZ / "wordpress"
IMAGENES = CONTENIDO / "imagenes.json"
IMG = CONTENIDO / "img"
MEDIOS = WP / "medios.json"
PROYECTOS = RAIZ.parent.parent  # D:\sOCProjects
TOKEN = Path(r"D:\dev\secrets\wordpress-socraticweb0.token")
SITE_ID = 257589098
WP_URL = "https://socraticweb0.wordpress.com"
CONTACTO = "jsoladelarosa@gmail.com"
GITHUB_PERFIL = "https://github.com/donki"
TEMA = "pub/assembler"

# Paleta: índigo sobre pizarra.
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


# ---------------------------------------------------------------- idiomas

IDIOMAS = {
    "es": {
        "codigo": "es", "raiz": "", "apps": "aplicaciones", "soporte": "soporte", "privacidad": "privacidad",
        "aviso": "aviso-legal", "cookies": "cookies", "otro": "en", "nombre_otro": "English",
        "nombre_propio": "Español",
        "ir_otro": "Read in English", "parte_cab": "header", "parte_pie": "footer", "plantilla": "",
        "descargar_en": "Descargar en {}", "descargar_github": "Descargar desde GitHub",
        "estado_en": "En {}", "y": " y ", "estado_github": "Descarga en GitHub", "navegador": "Navegador",
        "portada_ante": "Software libre para Android y Windows",
        "portada_h1": "Aplicaciones que respetan tu privacidad",
        "portada_entrada": "Herramientas pequeñas: cada una hace una cosa y la hace bien, funciona "
                           "sin conexión siempre que puede y no pide más permisos de los que necesita.",
        "ver_apps": "Ver las aplicaciones", "soporte_nav": "Soporte",
        "cifras": ["aplicaciones", "rastreadores", "licencia libre"],
        "catalogo_ante": "Catálogo", "catalogo_h2": "Aplicaciones",
        "catalogo_entrada": "Si una aplicación está en una tienda, el enlace te lleva allí; si no, a su página "
                            "de descargas en GitHub.",
        "trabajo_ante": "Cómo trabajamos", "trabajo_h2": "Hechas para durar y para confiar en ellas",
        "trabajo_entrada": "Dos compromisos que valen para todas las aplicaciones, hoy y en cada versión.",
        "principios": [
            ("Privacidad primero", "Sin analítica, sin perfiles y sin rastreadores. Lo que escribes se queda en "
                                   "tu dispositivo, y si una aplicación sincroniza, viaja cifrado."),
            ("Código abierto", "Todo el código está en GitHub con licencia MIT: puedes leerlo, compilarlo y "
                               "comprobar lo que hace."),
        ],
        "apps_entrada": "Todas con el código en GitHub. Si una está en una tienda, el enlace te lleva allí; si "
                        "no, a su página de descargas.",
        "soporte_h1": "Guías de uso",
        "soporte_entrada": "Cómo se pone en marcha cada aplicación, qué hace cada pantalla y cada opción, y las "
                           "dudas más habituales.",
        "ver_app": "Ver aplicación", "ver_guia": "Ver guía", "guia": "Guía de uso",
        "aplicacion": "Aplicación", "ficha": "Ficha", "plataformas": "Plataformas", "descarga": "Descarga",
        "licencia": "Licencia", "licencia_valor": "MIT, gratuita", "codigo_fuente": "Código fuente",
        "soporte_dato": "Soporte", "correo": "Correo", "privacidad_h": "Privacidad",
        "politica_privacidad": "Política de privacidad", "que_es": "Qué es",
        "funciones": "Funciones principales", "capturas_ante": "Capturas", "capturas_h2": "Así es {}",
        "en_movil": "En el móvil", "en_windows": "En Windows", "captura_de": "Captura de {}",
        "icono_de": "Icono de {}",
        "dudas_h": "¿Dudas con {}?",
        "dudas_texto": "La guía explica cómo ponerla en marcha, cada pantalla y cada opción, y las preguntas "
                       "más habituales.",
        "abrir_guia": "Abrir la guía",
        "guia_ante": "Soporte · {}", "guia_entrada": "Cómo funciona {}, pantalla a pantalla, y qué hace cada opción.",
        "ver_la_app": "Ver la aplicación", "todas_guias": "Todas las guías", "en_esta_guia": "En esta guía",
        "faq": "Preguntas frecuentes", "faq_ancla": "preguntas-frecuentes",
        "no_encuentras": "¿No encuentras lo que buscas?",
        "no_encuentras_texto": "Abre una incidencia en GitHub contando qué te pasa y con qué versión y "
                               "dispositivo.",
        "incidencia": "Abrir una incidencia en GitHub",
        "legal": "Legal",
        "privacidad_entrada": "Una sola política para todas las aplicaciones de sOCratic y para esta web: qué "
                              "datos se tocan, para qué y dónde se quedan.",
        "aviso_h1": "Aviso legal", "aviso_entrada": "Quién está detrás de esta web y en qué condiciones se usa.",
        "cookies_h1": "Política de cookies",
        "cookies_entrada": "Qué cookies hay en esta web, quién las pone y cómo rechazarlas.",
        "nav": [("apps", "Aplicaciones"), ("soporte", "Soporte"), ("privacidad", "Privacidad")],
        "pie_lema": "Aplicaciones libres para Android y Windows, con tus datos bajo tu control.",
        "sitio": "Sitio", "contacto": "Contacto", "cookies_nav": "Cookies", "aviso_nav": "Aviso legal",
        "copyright": "© 2026 sOCratic · Software libre con licencia MIT",
        "cookies_aviso": "Esta web está alojada en WordPress.com, que usa cookies para sus estadísticas de "
                         "visitas. Puedes aceptarlas o ver cómo rechazarlas en la <a href=\"{}\">política de "
                         "cookies</a>.",
        "aceptar": "Aceptar",
        "t_portada": "sOCratic", "t_apps": "Aplicaciones", "t_soporte": "Soporte",
        "t_privacidad": "Política de privacidad", "t_aviso": "Aviso legal", "t_cookies": "Política de cookies",
        "t_guia": "{}: guía de uso",
        "secciones": {},
    },
    "en": {
        "codigo": "en", "raiz": "en", "apps": "apps", "soporte": "support", "privacidad": "privacy",
        "aviso": "legal-notice", "cookies": "cookies", "otro": "es", "nombre_otro": "Español",
        "nombre_propio": "English",
        "ir_otro": "Leer en español", "parte_cab": "header-en", "parte_pie": "footer-en", "plantilla": "page-en",
        "descargar_en": "Get it on {}", "descargar_github": "Download from GitHub",
        "estado_en": "On {}", "y": " and ", "estado_github": "Download on GitHub", "navegador": "Browser",
        "portada_ante": "Open-source software for Android and Windows",
        "portada_h1": "Apps that respect your privacy",
        "portada_entrada": "Small tools: each one does one thing and does it well, works offline "
                           "whenever it can and never asks for more permissions than it needs.",
        "ver_apps": "See the apps", "soporte_nav": "Support",
        "cifras": ["apps", "trackers", "open-source license"],
        "catalogo_ante": "Catalog", "catalogo_h2": "Apps",
        "catalogo_entrada": "If an app is in a store, the link takes you there; if not, to its download page "
                            "on GitHub.",
        "trabajo_ante": "How we work", "trabajo_h2": "Built to last and to be trusted",
        "trabajo_entrada": "Two commitments that apply to every app, today and in every release.",
        "principios": [
            ("Privacy first", "No analytics, no profiling and no trackers. What you write stays on your "
                              "device, and if an app syncs, it travels encrypted."),
            ("Open source", "All the code is on GitHub under the MIT license: you can read it, build it and "
                            "check what it does."),
        ],
        "apps_entrada": "All with their code on GitHub. If an app is in a store, the link takes you there; if "
                        "not, to its download page.",
        "soporte_h1": "User guides",
        "soporte_entrada": "How to get each app up and running, what every screen and option does, and the most "
                           "common questions.",
        "ver_app": "View app", "ver_guia": "View guide", "guia": "User guide",
        "aplicacion": "App", "ficha": "Details", "plataformas": "Platforms", "descarga": "Download",
        "licencia": "License", "licencia_valor": "MIT, free", "codigo_fuente": "Source code",
        "soporte_dato": "Support", "correo": "Email", "privacidad_h": "Privacy",
        "politica_privacidad": "Privacy policy", "que_es": "What it is",
        "funciones": "Main features", "capturas_ante": "Screenshots", "capturas_h2": "A look at {}",
        "en_movil": "On mobile", "en_windows": "On Windows", "captura_de": "Screenshot of {}",
        "icono_de": "{} icon",
        "dudas_h": "Questions about {}?",
        "dudas_texto": "The guide explains how to set it up, every screen and option, and the most common "
                       "questions.",
        "abrir_guia": "Open the guide",
        "guia_ante": "Support · {}", "guia_entrada": "How {} works, screen by screen, and what every option does.",
        "ver_la_app": "View the app", "todas_guias": "All guides", "en_esta_guia": "In this guide",
        "faq": "FAQ", "faq_ancla": "faq",
        "no_encuentras": "Can't find what you need?",
        "no_encuentras_texto": "Open an issue on GitHub telling us what's happening, with which version and "
                               "device.",
        "incidencia": "Open an issue on GitHub",
        "legal": "Legal",
        "privacidad_entrada": "One policy for every sOCratic app and for this website: what data is touched, "
                              "what for and where it stays.",
        "aviso_h1": "Legal notice", "aviso_entrada": "Who is behind this website and the terms for using it.",
        "cookies_h1": "Cookie policy",
        "cookies_entrada": "Which cookies this website uses, who sets them and how to reject them.",
        "nav": [("apps", "Apps"), ("soporte", "Support"), ("privacidad", "Privacy")],
        "pie_lema": "Open-source apps for Android and Windows, with your data under your control.",
        "sitio": "Site", "contacto": "Contact", "cookies_nav": "Cookies", "aviso_nav": "Legal notice",
        "copyright": "© 2026 sOCratic · Open-source software, MIT license",
        "cookies_aviso": "This website is hosted on WordPress.com, which uses cookies for its visitor "
                         "statistics. You can accept them or see how to reject them in the <a href=\"{}\">cookie "
                         "policy</a>.",
        "aceptar": "Accept",
        "t_portada": "sOCratic (English)", "t_apps": "Apps", "t_soporte": "Support",
        "t_privacidad": "Privacy policy", "t_aviso": "Legal notice", "t_cookies": "Cookie policy",
        "t_guia": "{}: user guide",
        # Títulos de sección de las fichas en inglés → la clave castellana que usa el programa.
        "secciones": {"description": "descripción", "main features": "funciones principales",
                      "user guide (support)": "guía de uso (soporte)", "faq": "preguntas frecuentes",
                      "privacy": "privacidad"},
    },
}
L = IDIOMAS["es"]


def usar(idioma: str):
    global L
    L = IDIOMAS[idioma]


def url(clave: str | None = None, slug: str | None = None, idioma: str | None = None) -> str:
    """URL pública de una página en el idioma actual (o en el indicado)."""
    d = IDIOMAS[idioma or L["codigo"]]
    partes = [d["raiz"], d[clave] if clave else "", slug or ""]
    ruta = "/".join(p for p in partes if p)
    return f"{WP_URL}/{ruta}/" if ruta else f"{WP_URL}/"


# ---------------------------------------------------------------- lectura

def leer_app(ruta: Path, secciones_alias: dict | None = None) -> dict:
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
        titulo_s, _, contenido = bloque.partition("\n")
        t = titulo_s.strip().lower()
        secciones[(secciones_alias or {}).get(t, t)] = contenido.strip()

    def uno(k):
        return (campos.get(k) or [""])[0]

    tiendas = []
    for t in campos.get("tiendas", []):
        m = re.match(r"^\s*([^(:]+?)\s*\(([^)]*)\)\s*:\s*(\S+)", t)
        if not m:
            continue
        u = m.group(3).strip("<>().,;")
        if u.startswith("http"):
            tiendas.append({"tienda": m.group(1).strip(), "estado": m.group(2).strip(),
                            "url": u, "publicada": bool(PUBLICADA.search(m.group(2)))})
    github = (uno("github").split() or [""])[0].rstrip("/").removesuffix(".git")
    github = github if github.startswith("http") else ""
    releases = (uno("descarga_alternativa").split() or [""])[0]
    releases = releases if releases.startswith("http") else (github + "/releases" if github else "")
    return {
        "nombre": nombre, "slug": uno("slug"), "plataformas": uno("plataformas"),
        "lema": uno("lema"), "github": github, "releases": releases, "tiendas": tiendas,
        "secciones": secciones, "carpeta": ruta.stem,
        # «- publicar: no» deja la ficha en el repo sin sacarla en la web (decisión de Josep).
        "publicar": not re.match(r"no\b", uno("publicar"), re.I),
    }


def leer_apps(idioma: str) -> list[dict]:
    """Fichas del idioma. Si falta la traducción de una, se usa la castellana."""
    es = {p.stem: p for p in sorted((CONTENIDO / "apps").glob("*.md"))}
    apps = []
    for carpeta, ruta in es.items():
        if not leer_app(ruta)["publicar"]:
            continue
        if idioma != "es":
            traducida = CONTENIDO / idioma / "apps" / f"{carpeta}.md"
            if traducida.exists():
                ruta = traducida
            else:
                print(f"aviso: falta {traducida.relative_to(RAIZ)}; va en castellano")
        apps.append(leer_app(ruta, IDIOMAS[idioma]["secciones"]))
    apps.sort(key=lambda a: (not en_tienda(a), a["nombre"].lower()))
    return apps


def md(texto: str) -> str:
    # Las fichas sangran las sublistas con 2 o 3 espacios; markdown necesita 4.
    texto = re.sub(r"^ {2,3}(?=(?:[-*]|\d+\.) )", "    ", texto, flags=re.M)
    # Una lista pegada al párrafo de arriba (sin línea en blanco) markdown la lee como texto seguido.
    texto = re.sub(r"^((?! *(?:[-*]|\d+\.) )\S.*)\n(?=(?:[-*]|\d+\.) )", r"\1\n\n", texto, flags=re.M)
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
    if re.search(r"extensi[oó]n de navegador|browser extension", pl, re.I):
        tags.append(L["navegador"])
    return tags


# ---------------------------------------------------------------- enlaces

def enlaces(app: dict) -> list[tuple[str, str]]:
    """Botones de descarga: las tiendas donde está publicada; si no hay ninguna, GitHub."""
    botones = [(L["descargar_en"].format(t["tienda"]), t["url"]) for t in app["tiendas"] if t["publicada"]]
    # Una tienda de extensiones solo da la extensión: la aplicación se sigue bajando de GitHub.
    solo_extension = all(re.search(r"add-ons|chrome|firefox", t, re.I) for t, _ in botones)
    if (not botones or solo_extension) and app["releases"]:
        botones.append((L["descargar_github"], app["releases"]))
    return botones


def estado(app: dict) -> str:
    pub = [t["tienda"] for t in app["tiendas"] if t["publicada"]]
    return L["estado_en"].format(L["y"].join(pub)) if pub else L["estado_github"]


def en_tienda(app: dict) -> bool:
    return any(t["publicada"] for t in app["tiendas"])


# ---------------------------------------------------------------- imágenes

def preparar_imagenes(apps: list[dict]):
    """Reduce los iconos y capturas de las fichas de tienda a contenido/img/<slug>/ y los apunta en cada app.

    Iconos a 192 px en PNG; capturas de móvil a 540 px y de escritorio a 1280 px de ancho, en WebP.
    """
    from PIL import Image
    mapa = json.loads(IMAGENES.read_text(encoding="utf-8"))

    def reducir(origen: str, destino: Path, ancho: int, formato: str) -> str:
        src = PROYECTOS / origen
        if not destino.exists() or destino.stat().st_mtime < src.stat().st_mtime:
            destino.parent.mkdir(parents=True, exist_ok=True)
            im = Image.open(src)
            im = im.convert("RGBA" if formato == "PNG" else "RGB")
            if im.width > ancho:
                im = im.resize((ancho, round(im.height * ancho / im.width)), Image.LANCZOS)
            im.save(destino, formato, **({"optimize": True} if formato == "PNG" else {"quality": 80, "method": 6}))
        return destino.relative_to(CONTENIDO).as_posix()

    for app in apps:
        m = mapa.get(app["slug"], {})
        base = IMG / app["slug"]
        app["icono"] = reducir(m["icono"], base / "icono.png", 192, "PNG") if m.get("icono") else ""
        app["capturas"] = [reducir(c, base / f"movil-{i + 1}.webp", 540, "WEBP")
                           for i, c in enumerate(m.get("capturas", []))]
        app["capturas_anchas"] = [reducir(c, base / f"escritorio-{i + 1}.webp", 1280, "WEBP")
                                  for i, c in enumerate(m.get("capturas_anchas", []))]


def preparar_banderas():
    """Banderas de España y de EE. UU. para cambiar de idioma: PNG dibujados aquí (nada de emoji, General §6.2;
    WordPress.com gratuito no admite SVG). 72×48 para verse nítidas a 24×16."""
    from PIL import Image, ImageDraw
    # El logo de la cabecera: el icono del perfil de desarrollador de Google Play, a 108 px (se ve a 36).
    logo = IMG / "marca" / "logo.png"
    origen = PROYECTOS / "Mobile" / "GooglePlayConsole" / "dev-profile" / "socratic_dev_icon_512.png"
    if not logo.exists() or logo.stat().st_mtime < origen.stat().st_mtime:
        logo.parent.mkdir(parents=True, exist_ok=True)
        Image.open(origen).convert("RGB").resize((108, 108), Image.LANCZOS).save(logo, "PNG", optimize=True)
    destino = IMG / "banderas"
    destino.mkdir(parents=True, exist_ok=True)
    es, us = destino / "es.png", destino / "en.png"
    if not es.exists():
        im = Image.new("RGB", (72, 48), "#AA151B")
        ImageDraw.Draw(im).rectangle((0, 12, 71, 35), fill="#F1BF00")
        im.save(es, "PNG", optimize=True)
    if not us.exists():
        escala = 4  # se dibuja grande y se reduce para suavizar las estrellas
        w, h = 72 * escala, 48 * escala
        im = Image.new("RGB", (w, h), "#FFFFFF")
        d = ImageDraw.Draw(im)
        franja = h / 13
        for i in range(0, 13, 2):
            d.rectangle((0, round(i * franja), w, round((i + 1) * franja) - 1), fill="#B22234")
        cw, ch = round(w * 0.4), round(franja * 7)
        d.rectangle((0, 0, cw, ch), fill="#3C3B6E")
        r = escala * 1.1
        for fila in range(9):
            for col in range(6 if fila % 2 == 0 else 5):
                x = cw / 12 * (2 * col + (1 if fila % 2 == 0 else 2))
                y = ch / 10 * (fila + 1)
                d.ellipse((x - r, y - r, x + r, y + r), fill="#FFFFFF")
        im.resize((72, 48), Image.LANCZOS).save(us, "PNG", optimize=True)


def medios() -> dict:
    return json.loads(MEDIOS.read_text(encoding="utf-8")) if MEDIOS.exists() else {}


def resolver_imagenes(h: str, base: str | None = None) -> str:
    """Las imágenes van como «@@img/…@@»: en WordPress, la URL de la biblioteca; en local, la ruta relativa."""
    if base is not None:
        return re.sub(r"@@(img/[^@]+)@@", lambda x: base + x.group(1), h)
    m = medios()
    return re.sub(r"@@(img/[^@]+)@@", lambda x: m.get(x.group(1), {}).get("url", x.group(1)), h)


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


def _abre(nombre: str, attrs: dict, tag: str, base: list[str], extra_cls: list[str] | None = None) -> tuple[str, str]:
    css, cls = _css(attrs.get("style"))
    clases = base + (extra_cls or [])
    if attrs.get("className"):
        clases.append(attrs["className"])
    clases += cls
    st = f' style="{css}"' if css else ""
    return (f"<!-- wp:{nombre}{_attrs(attrs)} -->\n<{tag} class=\"{' '.join(clases)}\"{st}>",
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


def boton(texto: str, destino: str, fondo=None, color=None, contorno=False) -> str:
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
               if destino.startswith("http") and not destino.startswith(WP_URL) else "")
    return (f"<!-- wp:button{_attrs(a)} -->\n<div class=\"wp-block-button{' is-style-outline' if contorno else ''}\">"
            f"<a class=\"wp-block-button__link {' '.join(cls)} wp-element-button\" href=\"{html.escape(destino)}\""
            f" style=\"{css}\"{externo}>{html.escape(texto)}</a></div>\n<!-- /wp:button -->")


def botones(*bs: str) -> str:
    if not bs:
        return ""
    return ("<!-- wp:buttons {\"style\":{\"spacing\":{\"blockGap\":{\"left\":\"12px\",\"top\":\"12px\"}}}} -->\n"
            "<div class=\"wp-block-buttons\">" + "\n".join(bs) + "</div>\n<!-- /wp:buttons -->")


def columnas(*cols: tuple[str, str], hueco="48px", centradas=False) -> str:
    partes = []
    for ancho, contenido in cols:
        partes.append(f"<!-- wp:column {{\"width\":\"{ancho}\"}} -->\n<div class=\"wp-block-column\" "
                      f"style=\"flex-basis:{ancho}\">{contenido}</div>\n<!-- /wp:column -->")
    alinear = ',"verticalAlignment":"center"' if centradas else ""
    clase = " are-vertically-aligned-center" if centradas else ""
    return (f"<!-- wp:columns {{\"style\":{{\"spacing\":{{\"blockGap\":{{\"left\":\"{hueco}\",\"top\":\"32px\"}}}}}}{alinear}}} -->\n"
            f"<div class=\"wp-block-columns{clase}\">" + "\n".join(partes) + "</div>\n<!-- /wp:columns -->")


def imagen(ruta: str, alt: str, ancho: str | None = None, radio="12px", borde=True, enlace: str | None = None) -> str:
    """Bloque de imagen. «ruta» es relativa a contenido/ (img/<slug>/…) y se resuelve al publicar."""
    st = {"border": {"radius": radio}}
    if borde:
        st["border"].update({"width": "1px", "color": LINEA})
    a = {"sizeSlug": "full", "linkDestination": "custom" if enlace else "none", "style": st}
    if ancho:
        a["width"] = ancho
    css, cls = _css(st)
    estilo_img = css + (f";width:{ancho}" if ancho else "")
    clase_img = " ".join(c for c in cls if c == "has-border-color")
    img = f'<img src="@@{ruta}@@" alt="{html.escape(alt)}" class="{clase_img}" style="{estilo_img}"/>'
    if enlace:
        img = f'<a href="{enlace}">{img}</a>'
    clases = "wp-block-image size-full has-custom-border" + (" is-resized" if ancho else "")
    return f"<!-- wp:image{_attrs(a)} -->\n<figure class=\"{clases}\">{img}</figure>\n<!-- /wp:image -->"


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


def cabecera_pagina(ante: str, h1: str, entrada: str, bs: list[str], otro: str, extra: str = "",
                    grande=True, icono: str = "") -> str:
    """La franja oscura con degradado con la que empieza cada página. «otro»: la misma página en el otro idioma."""
    # «otro» ya no se enseña (el cambio de idioma son las banderas de la cabecera); se deja el
    # parámetro para no perder qué página es la equivalente en el otro idioma.
    hijos = [
        icono,
        antetitulo(ante, ACENTO_CLARO),
        titulo(html.escape(h1), 1, size="x-large" if grande else "large",
               style={"typography": {"lineHeight": "1.08", "fontWeight": "700", "letterSpacing": "-0.02em"},
                      "color": {"text": "#ffffff"}}),
        parrafo(entrada, style={"color": {"text": "#e0e7ff"},
                                "typography": {"fontSize": "1.2rem", "lineHeight": "1.6"}}),
        botones(*bs),
        extra,
    ]
    relleno = "var:preset|spacing|80" if grande else "var:preset|spacing|70"
    return grupo(*hijos, align="full", clase="soc-hero soc-sec",
                 style={"color": {"gradient": DEGRADADO, "text": "#ffffff"},
                        "elements": {"link": {"color": {"text": "#ffffff"}}},
                        "spacing": {"padding": {"top": relleno, "bottom": relleno},
                                    "margin": {"top": "0", "bottom": "0"}}},
                 layout={"type": "constrained", "contentSize": ANCHO})


def boton_claro(texto, destino):
    return boton(texto, destino, fondo="#ffffff", color=ACENTO)


def boton_contorno_claro(texto, destino):
    return boton(texto, destino, color="#ffffff", contorno=True)


def tarjeta(*hijos, fondo="#ffffff") -> str:
    return grupo(*hijos, clase="soc-card", style={
        "border": {"color": LINEA, "width": "1px", "radius": "16px"},
        "color": {"background": fondo},
        "spacing": {"padding": {"top": "28px", "bottom": "28px", "left": "28px", "right": "28px"},
                    "blockGap": "12px"}})


def icono_app(app: dict, ancho="56px", radio="14px", enlace: str | None = None) -> str:
    if not app.get("icono"):
        return ""
    return imagen(app["icono"], L["icono_de"].format(app["nombre"]), ancho=ancho, radio=radio, borde=False,
                  enlace=enlace)


def galeria(rutas: list[str], nombre: str, minimo: str) -> str:
    return rejilla(*[imagen(r, L["captura_de"].format(nombre)) for r in rutas], minimo=minimo, hueco="20px")


def tarjeta_app(app: dict, destino: str, llamada: str) -> str:
    u = url(destino, app["slug"])
    return tarjeta(
        icono_app(app, enlace=u),
        antetitulo(" · ".join(etiquetas(app))),
        titulo(f'<a href="{u}">{html.escape(app["nombre"])}</a>', 3, size="medium",
               style={"typography": {"fontWeight": "700", "lineHeight": "1.25"},
                      "elements": {"link": {"color": {"text": TINTA}, "typography": {"textDecoration": "none"}}}}),
        parrafo(html.escape(app["lema"]), style={"color": {"text": APAGADO}}),
        parrafo(html.escape(estado(app)), style={
            "color": {"text": VERDE if en_tienda(app) else APAGADO},
            "typography": {"fontSize": "0.85rem", "fontWeight": "600"}}),
        parrafo(f'<a href="{u}">{llamada} →</a>', style={
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


def llamada(texto_h: str, texto: str, bs: list[str], arriba=False) -> str:
    """Recuadro de ayuda al final de una página. Con margen arriba si va tras una sección con fondo."""
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


def principio(numero: int, h3: str, texto: str) -> str:
    """Un compromiso de «Cómo trabajamos»: número grande en índigo y texto con filete a la izquierda."""
    return grupo(
        parrafo(f"{numero:02d}", style={"color": {"text": ACENTO},
                                         "typography": {"fontSize": "2.4rem", "fontWeight": "800", "lineHeight": "1"}}),
        titulo(html.escape(h3), 3, size="medium", style={"typography": {"fontWeight": "700"},
                                                         "color": {"text": TINTA}}),
        parrafo(html.escape(texto), style={"color": {"text": TEXTO}, "typography": {"fontSize": "1.05rem"}}),
        style={"border": {"left": {"color": ACENTO, "width": "3px"}},
               "spacing": {"padding": {"left": "28px"}, "blockGap": "10px"}})


# ---------------------------------------------------------------- páginas

def portada_wp(apps: list[dict]) -> str:
    cifras = rejilla(*[
        grupo(parrafo(f"<strong>{n}</strong>", style={"typography": {"fontSize": "2.2rem", "lineHeight": "1"},
                                                     "color": {"text": "#ffffff"}}),
              parrafo(t, style={"color": {"text": ACENTO_CLARO}, "typography": {"fontSize": "0.95rem"}}),
              style={"spacing": {"blockGap": "6px"}})
        for n, t in zip([str(len(apps)), "0", "MIT"], L["cifras"])], minimo="9rem")
    cifras = grupo(cifras, style={"spacing": {"margin": {"top": "var:preset|spacing|60"}, "padding": {"top": "28px"}},
                                  "border": {"top": {"color": "rgba(255,255,255,0.2)", "width": "1px"}}})
    # Tira de iconos de todo el catálogo en la franja de entrada.
    iconos = grupo(*[icono_app(a, ancho="52px", radio="13px", enlace=url("apps", a["slug"]))
                     for a in apps if a.get("icono")],
                   style={"spacing": {"blockGap": "14px", "margin": {"top": "var:preset|spacing|50"}}},
                   layout={"type": "flex", "flexWrap": "wrap"})
    trabajo = columnas(
        ("38%", encabezado_seccion(L["trabajo_ante"], L["trabajo_h2"], L["trabajo_entrada"])),
        ("62%", grupo(*[principio(i + 1, t, d) for i, (t, d) in enumerate(L["principios"])],
                      style={"spacing": {"blockGap": "var:preset|spacing|50"}})),
        hueco="var:preset|spacing|70")
    return "\n\n".join([
        cabecera_pagina(L["portada_ante"], L["portada_h1"], L["portada_entrada"],
                        [boton_claro(L["ver_apps"], url("apps")), boton_contorno_claro(L["soporte_nav"], url("soporte"))],
                        otro=url(idioma=L["otro"]), extra=iconos + "\n\n" + cifras),
        seccion(encabezado_seccion(L["catalogo_ante"], L["catalogo_h2"], L["catalogo_entrada"]),
                rejilla(*[tarjeta_app(a, "apps", L["ver_app"]) for a in apps])),
        seccion(trabajo, fondo=SUAVE),
    ])


def indice_apps_wp(apps: list[dict]) -> str:
    return "\n\n".join([
        cabecera_pagina(L["catalogo_ante"], L["catalogo_h2"], L["apps_entrada"],
                        [boton_contorno_claro(L["soporte_nav"], url("soporte"))],
                        otro=url("apps", idioma=L["otro"]), grande=False),
        seccion(rejilla(*[tarjeta_app(a, "apps", L["ver_app"]) for a in apps])),
    ])


def indice_soporte_wp(apps: list[dict]) -> str:
    return "\n\n".join([
        cabecera_pagina(L["soporte_nav"], L["soporte_h1"], L["soporte_entrada"], [],
                        otro=url("soporte", idioma=L["otro"]), grande=False),
        seccion(rejilla(*[tarjeta_app(a, "soporte", L["ver_guia"]) for a in apps])),
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
    descarga.append(boton_contorno_claro(L["guia"], url("soporte", app["slug"])))
    tiendas = []
    for t, u in enlaces(app):
        nombre = re.sub(r"^(Descargar en |Descargar desde |Get it on |Download from )", "", t)
        tiendas.append(f'<a href="{u}">{html.escape(nombre)}</a>')
    ficha = tarjeta(
        titulo(L["ficha"], 3, size="medium", style={"typography": {"fontWeight": "700"}, "color": {"text": TINTA}}),
        dato(L["plataformas"], html.escape(app["plataformas"])),
        dato(L["descarga"], " · ".join(tiendas)),
        dato(L["licencia"], L["licencia_valor"]),
        dato(L["codigo_fuente"], f'<a href="{app["github"]}">{app["github"].removeprefix("https://")}</a>')
        if app["github"] else "",
        dato(L["soporte_dato"], f'<a href="{url("soporte", app["slug"])}">{L["guia"]}</a>'),
        fondo=SUAVE)
    privacidad = tarjeta(
        titulo(L["privacidad_h"], 3, size="medium", style={"typography": {"fontWeight": "700"}, "color": {"text": TINTA}}),
        wp_html(md(s.get("privacidad", ""))),
        parrafo(f'<a href="{url("privacidad")}">{L["politica_privacidad"]}</a>',
                style={"typography": {"fontWeight": "600"}}))
    izquierda = "\n\n".join([
        titulo(L["que_es"], 2, size="large", style={"typography": {"fontWeight": "700"}, "color": {"text": TINTA}}),
        wp_html(md(s.get("descripción", ""))),
        titulo(L["funciones"], 2, size="large",
               style={"typography": {"fontWeight": "700"}, "color": {"text": TINTA},
                      "spacing": {"margin": {"top": "var:preset|spacing|50"}}}),
        wp_html(md(s.get("funciones principales", ""))),
    ])
    derecha = grupo(ficha, privacidad, style={"spacing": {"blockGap": "24px"}})
    capturas = []
    if app.get("capturas") or app.get("capturas_anchas"):
        capturas.append(encabezado_seccion(L["capturas_ante"], L["capturas_h2"].format(app["nombre"])))
        dos = app.get("capturas") and app.get("capturas_anchas")
        if app.get("capturas"):
            if dos:
                capturas.append(titulo(L["en_movil"], 3, size="medium", style={"color": {"text": TINTA}}))
            capturas.append(galeria(app["capturas"], app["nombre"], "11rem"))
        if app.get("capturas_anchas"):
            if dos:
                capturas.append(titulo(L["en_windows"], 3, size="medium", style={
                    "color": {"text": TINTA}, "spacing": {"margin": {"top": "var:preset|spacing|50"}}}))
            capturas.append(galeria(app["capturas_anchas"], app["nombre"], "22rem"))
    return "\n\n".join(x for x in [
        cabecera_pagina(" · ".join(etiquetas(app)) or L["aplicacion"], app["nombre"], html.escape(app["lema"]),
                        descarga, otro=url("apps", app["slug"], idioma=L["otro"]), grande=False,
                        icono=icono_app(app, ancho="88px", radio="20px")),
        seccion(columnas(("64%", izquierda), ("36%", derecha))),
        seccion(*capturas, fondo=SUAVE) if capturas else "",
        llamada(L["dudas_h"].format(html.escape(app["nombre"])), L["dudas_texto"],
                [boton(L["abrir_guia"], url("soporte", app["slug"]), fondo=ACENTO, color="#ffffff")],
                arriba=bool(capturas)),
    ] if x)


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
        indice.append((L["faq_ancla"], L["faq"]))
    lista = "".join(f'<li><a href="#{i}">{t}</a></li>' for i, t in indice)
    contenido = [
        tarjeta(
            parrafo(f"<strong>{L['en_esta_guia']}</strong>", style={"color": {"text": TINTA}}),
            f"<!-- wp:list -->\n<ul class=\"wp-block-list\">{lista}</ul>\n<!-- /wp:list -->",
            fondo=SUAVE) if indice else "",
        wp_html(guia),
    ]
    if faq:
        contenido.append(titulo(L["faq"], 2, size="large", ancla=L["faq_ancla"],
                                style={"typography": {"fontWeight": "700"}, "color": {"text": TINTA},
                                       "spacing": {"margin": {"top": "var:preset|spacing|70"}}}))
        contenido.append(grupo(*[desplegable(html.escape(p.rstrip()), md(r)) for p, r in faq],
                               style={"spacing": {"blockGap": "0"}}))
    ayuda = llamada(L["no_encuentras"], L["no_encuentras_texto"],
                    [boton(L["incidencia"], f"{app['github']}/issues", fondo=ACENTO, color="#ffffff")]
                    ) if app["github"] else ""
    # Las capturas también en la guía, justo antes del texto, para ver de qué pantallas se habla.
    capturas = app.get("capturas") or app.get("capturas_anchas")
    if capturas:
        contenido.insert(1, galeria(capturas, app["nombre"], "9rem" if app.get("capturas") else "18rem"))
    return "\n\n".join(x for x in [
        cabecera_pagina(L["guia_ante"].format(app["nombre"]), L["guia"],
                        L["guia_entrada"].format(html.escape(app["nombre"])),
                        [boton_claro(L["ver_la_app"], url("apps", app["slug"])),
                         boton_contorno_claro(L["todas_guias"], url("soporte"))],
                        otro=url("soporte", app["slug"], idioma=L["otro"]), grande=False,
                        icono=icono_app(app, ancho="64px", radio="16px")),
        seccion(*contenido, ancho=LECTURA),
        ayuda,
    ] if x)


def texto_legal(fichero: str) -> str:
    carpeta = CONTENIDO / "legal" if L["codigo"] == "es" else CONTENIDO / L["codigo"] / "legal"
    return (carpeta / fichero).read_text(encoding="utf-8")


def privacidad_wp() -> str:
    if L["codigo"] == "es":
        fuente = (RAIZ / "CONTENIDO-PARA-GOOGLE-SITES.md").read_text(encoding="utf-8")
        texto = fuente.split("# PÁGINA 2 — Política de privacidad", 1)[1].split("**Texto:**", 1)[1].strip()
    else:
        texto = texto_legal("privacidad-apps.md")
    texto += "\n\n" + texto_legal("privacidad-web.md")
    return "\n\n".join([
        cabecera_pagina(L["legal"], L["t_privacidad"], L["privacidad_entrada"], [],
                        otro=url("privacidad", idioma=L["otro"]), grande=False),
        seccion(wp_html(md(texto)), ancho=LECTURA),
    ])


def pagina_legal(clave: str, fichero: str, h1: str, entrada: str) -> str:
    return "\n\n".join([
        cabecera_pagina(L["legal"], h1, entrada, [], otro=url(clave, idioma=L["otro"]), grande=False),
        seccion(wp_html(md(texto_legal(fichero))), ancho=LECTURA),
    ])


# ---------------------------------------------------------------- cabecera, pie y plantillas del tema

def cabecera_tema() -> str:
    pares = [(t, url(c)) for c, t in L["nav"]] + [("GitHub", GITHUB_PERFIL)]
    enlaces_nav = "\n".join(
        f"<!-- wp:navigation-link {{\"label\":\"{t}\",\"url\":\"{u}\",\"kind\":\"custom\",\"isTopLevelLink\":true}} /-->"
        for t, u in pares)
    nav = ("<!-- wp:navigation {\"overlayMenu\":\"mobile\",\"style\":{\"typography\":{\"fontWeight\":\"500\"},"
           "\"spacing\":{\"blockGap\":\"28px\"}},\"layout\":{\"type\":\"flex\",\"justifyContent\":\"right\"}} -->\n"
           + enlaces_nav + "\n<!-- /wp:navigation -->")
    # Logo (el icono del perfil de desarrollador de Google Play) y nombre, a la portada del idioma
    # (el bloque site-title siempre iría a la castellana).
    marca = grupo(
        imagen("img/marca/logo.png", "sOCratic", ancho="36px", radio="9px", borde=False, enlace=url()),
        parrafo(f'<a href="{url()}"><strong>sOCratic</strong></a>', size="medium", clase="soc-marca", style={
            "typography": {"fontWeight": "800", "letterSpacing": "-0.02em"},
            "elements": {"link": {"color": {"text": TINTA}, "typography": {"textDecoration": "none"}}}}),
        style={"spacing": {"blockGap": "10px"}},
        layout={"type": "flex", "flexWrap": "nowrap", "verticalAlignment": "center"})
    # Banderas para cambiar de idioma, tras GitHub; se ven también en el móvil, junto al botón del menú.
    banderas = grupo(*[
        imagen(f"img/banderas/{i}.png", IDIOMAS[i]["nombre_propio"], ancho="24px", radio="3px",
               enlace=url(idioma=i))
        for i in ("es", "en")],
        # Altura de línea 0: si no, la imagen (en línea dentro del enlace) se queda en la línea base de
        # una caja de 26 px y sale unos 5 px más baja que el texto del menú.
        style={"spacing": {"blockGap": "10px"}, "typography": {"lineHeight": "0"}},
        layout={"type": "flex", "flexWrap": "nowrap", "verticalAlignment": "center"})
    derecha = grupo(nav, banderas, style={"spacing": {"blockGap": "24px"}},
                    layout={"type": "flex", "flexWrap": "nowrap", "verticalAlignment": "center"})
    fila = grupo(marca, derecha, align="wide",
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
    attrs = {"render_from_template": True, "align": "wide", "consentExpiryDays": 365, "style": st}
    return (f"<!-- wp:jetpack/cookie-consent{_attrs(attrs)} -->\n"
            f"<div class=\"wp-block-jetpack-cookie-consent alignwide {' '.join(cls)}\" style=\"{css}\" "
            f"role=\"dialog\" aria-modal=\"true\"><p>{L['cookies_aviso'].format(url('cookies'))}</p>"
            + boton(L["aceptar"], "#", fondo="#ffffff", color=ACENTO)
            + "<span>365</span></div>\n<!-- /wp:jetpack/cookie-consent -->")


def pie_tema() -> str:
    claro = {"color": {"text": "#94a3b8"}, "typography": {"fontSize": "0.8rem", "fontWeight": "700",
                                                          "letterSpacing": "0.1em", "textTransform": "uppercase"}}

    def lista(pares):
        return "\n".join(parrafo(f'<a href="{u}">{t}</a>', style={"spacing": {"margin": {"top": "6px"}}})
                         for t, u in pares)

    cols = columnas(
        ("40%", "\n".join([
            parrafo("<strong>sOCratic</strong>", style={"color": {"text": "#ffffff"}, "typography": {"fontSize": "1.4rem"}}),
            parrafo(L["pie_lema"]),
        ])),
        ("20%", parrafo(L["sitio"], style=claro) + "\n" + lista([
            (L["catalogo_h2"], url("apps")), (L["soporte_nav"], url("soporte")),
            (L["nombre_otro"], url(idioma=L["otro"]))])),
        ("20%", parrafo(L["legal"], style=claro) + "\n" + lista([
            (L["aviso_nav"], url("aviso")), (L["privacidad_h"], url("privacidad")),
            (L["cookies_nav"], url("cookies"))])),
        ("20%", parrafo(L["contacto"], style=claro) + "\n" + lista([("GitHub", GITHUB_PERFIL)])),
    )
    return grupo(
        cols,
        separador("#1e293b"),
        parrafo(L["copyright"], style={"color": {"text": "#94a3b8"}, "typography": {"fontSize": "0.875rem"}}),
        aviso_cookies(),
        align="full", tag="footer", clase="soc-sec",
        style={"color": {"background": TINTA, "text": "#cbd5e1"},
               "elements": {"link": {"color": {"text": "#ffffff"}}},
               "spacing": {"padding": {"top": "var:preset|spacing|70", "bottom": "var:preset|spacing|50"},
                           "margin": {"top": "0", "bottom": "0"}}},
        layout={"type": "constrained", "contentSize": ANCHO})


def plantilla_pagina() -> str:
    """Plantilla de página: la del tema, con la cabecera fija arriba al hacer scroll y las partes del idioma."""
    return (
        '<!-- wp:group {"style":{"position":{"type":"sticky","top":"0px"},"spacing":{"margin":{"top":"0","bottom":"0"}}},'
        '"layout":{"type":"default"}} -->\n<div class="wp-block-group" style="margin-top:0;margin-bottom:0">'
        f'<!-- wp:template-part {{"slug":"{L["parte_cab"]}","theme":"{TEMA}","tagName":"div"}} /--></div>\n'
        '<!-- /wp:group -->\n\n'
        '<!-- wp:group {"tagName":"main","metadata":{"name":"Main"},"style":{"spacing":{"blockGap":"0","margin":{"top":"0"}}},'
        '"layout":{"type":"default"}} -->\n<main class="wp-block-group" style="margin-top:0">'
        '<!-- wp:post-content {"layout":{"type":"constrained"}} /--></main>\n<!-- /wp:group -->\n\n'
        f'<!-- wp:template-part {{"slug":"{L["parte_pie"]}","theme":"{TEMA}","tagName":"div"}} /-->')


# ---------------------------------------------------------------- HTML autónomo

def plantilla_html(titulo_pag: str, cuerpo: str, prof: int, idioma: str) -> str:
    base = "../" * prof
    return f"""<!doctype html>
<html lang="{idioma}">
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


def local(bloques: str, prof: int, mapa: dict[str, str]) -> str:
    """El HTML local es el de WordPress sin comentarios de bloque y con enlaces relativos entre páginas."""
    h = re.sub(r"<!-- wp:navigation-link \{\"label\":\"([^\"]+)\",\"url\":\"([^\"]+)\"[^>]*/-->",
               r'<a href="\2">\1</a>', bloques)
    h = re.sub(r"<!-- /?wp:[^>]*-->\n?", "", h)
    base = "../" * prof

    def rel(m):
        destino = mapa.get(m.group(1))
        return f'href="{base}{destino}{m.group(2) or ""}"' if destino else m.group(0)
    return re.sub(r'href="(' + re.escape(WP_URL) + r'/[^"#]*)(#[^"]*)?"', rel, h)


# ---------------------------------------------------------------- publicar

def sesion():
    import requests
    tok = json.loads(TOKEN.read_text(encoding="utf-8-sig"))["access_token"]
    s = requests.Session()
    s.headers["Authorization"] = f"Bearer {tok}"
    return s


API = f"https://public-api.wordpress.com/wp/v2/sites/{SITE_ID}"


def post(s, destino, datos=None, **kw):
    """POST con reintentos: WordPress.com da 502 sueltos."""
    for intento in range(5):
        r = s.post(destino, json=datos, **kw)
        if r.status_code < 500:
            return r
        time.sleep(3 * (intento + 1))
    return r


def subir_medios():
    """Sube a la biblioteca de WordPress las imágenes de contenido/img que no estén o hayan cambiado.

    wordpress/medios.json guarda, por ruta, el id, la URL y la huella del fichero subido.
    """
    s = sesion()
    m = medios()
    tipos = {".png": "image/png", ".webp": "image/webp", ".jpg": "image/jpeg"}
    for f in sorted(IMG.rglob("*.*")):
        ruta = f.relative_to(CONTENIDO).as_posix()
        datos = f.read_bytes()
        huella = hashlib.sha256(datos).hexdigest()
        if m.get(ruta, {}).get("sha") == huella:
            continue
        nombre = ruta.removeprefix("img/").replace("/", "-")
        r = post(s, f"{API}/media", data=datos, headers={
            "Content-Type": tipos[f.suffix.lower()], "Content-Disposition": f'attachment; filename="{nombre}"'})
        if not r.ok:
            raise SystemExit(f"{ruta}: {r.status_code} {r.text[:300]}")
        viejo = m.get(ruta, {}).get("id")
        m[ruta] = {"id": r.json()["id"], "url": r.json()["source_url"], "sha": huella}
        if viejo:  # la versión anterior ya no la usa nadie
            s.delete(f"{API}/media/{viejo}", params={"force": True})
        print("imagen subida", ruta)
        WP.mkdir(exist_ok=True)
        MEDIOS.write_text(json.dumps(m, indent=1, ensure_ascii=False), encoding="utf-8")


def subir_tema(partes: dict[str, str], plantillas: dict[str, str]):
    """Partes (cabecera y pie de cada idioma) y plantillas (página castellana y page-en)."""
    s = sesion()
    for slug, contenido in partes.items():
        r = post(s, f"{API}/template-parts/{TEMA}//{slug}", {"content": contenido})
        if r.status_code == 404:  # la del inglés no existe hasta la primera vez
            area = "header" if slug.startswith("header") else "footer"
            r = post(s, f"{API}/template-parts", {"slug": slug, "title": slug, "area": area, "content": contenido})
        print(f"parte {slug}:", r.status_code, "" if r.ok else r.text[:300])
    for slug, contenido in plantillas.items():
        r = post(s, f"{API}/templates/{TEMA}//{slug}", {"content": contenido})
        if r.status_code == 404:
            r = post(s, f"{API}/templates", {"slug": slug, "title": "Page (English)", "content": contenido})
        print(f"plantilla {slug}:", r.status_code, "" if r.ok else r.text[:300])


def publicar(paginas: list[dict]):
    s = sesion()
    v11 = f"https://public-api.wordpress.com/rest/v1.1/sites/{SITE_ID}"
    existentes = {}
    pag = 1
    while True:
        r = s.get(f"{API}/pages", params={"per_page": 100, "page": pag, "status": "publish,draft",
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
                 "parent": padre, "menu_order": p["orden"], "comment_status": "closed", "ping_status": "closed",
                 "template": p["plantilla"]}
        pid = existentes.get((p["slug"], padre))
        for intento in range(5):
            r = s.post(f"{API}/pages/{pid}" if pid else f"{API}/pages", json=datos)
            if r.status_code < 500:
                break
            # WordPress.com da 502 de vez en cuando aunque la página se haya guardado:
            # antes de reintentar se mira si ya existe para no duplicarla.
            time.sleep(3 * (intento + 1))
            if not pid:
                q = s.get(f"{API}/pages", params={"slug": p["slug"], "parent": padre,
                                                  "status": "publish,draft", "context": "edit"})
                if q.ok and q.json():
                    pid = q.json()[0]["id"]
        if not r.ok:
            raise SystemExit(f"{p['slug']}: {r.status_code} {r.text[:300]}")
        ids[p["clave"]] = r.json()["id"]
        # Sin «Me gusta» ni botones de compartir bajo el contenido.
        post(s, f"{v11}/posts/{ids[p['clave']]}", {"likes_enabled": False, "sharing_enabled": False})
        print(("actualizada " if pid else "creada     ") + r.json()["link"])
    # Lo que ya no se genera sobra: la página de ejemplo de WordPress y las de apps que salen de la web.
    if ("about", 0) in existentes:
        s.delete(f"{API}/pages/{existentes[('about', 0)]}", params={"force": True})
    vivas = {(p["slug"], ids.get(p["padre"], 0) if p["padre"] else 0) for p in paginas}
    contenedores = {ids[k] for k in ("es-apps", "es-soporte", "en-apps", "en-soporte", "en-portada") if k in ids}
    for (slug, padre), pid in existentes.items():
        if padre in contenedores and (slug, padre) not in vivas:
            s.delete(f"{API}/pages/{pid}", params={"force": True})
            print("borrada    ", slug)
    # Portada fija y comentarios cerrados: esto solo lo aplica la API v2 (la v1.2 contesta 200 y no hace nada).
    r = post(s, f"{API}/settings", {
        "title": "sOCratic", "description": "Aplicaciones libres para Android y Windows",
        "show_on_front": "page", "page_on_front": ids["es-portada"],
        "default_comment_status": "closed", "default_ping_status": "closed"})
    print("ajustes:", r.status_code, "" if r.ok else r.text[:300])
    r = post(s, f"https://public-api.wordpress.com/rest/v1.2/sites/{SITE_ID}/settings", {
        "lang_id": 19, "default_likes_enabled": False, "sharing_show": []})
    print("ajustes wpcom:", r.status_code, "" if r.ok else r.text[:300])


# ---------------------------------------------------------------- principal

def paginas_idioma(idioma: str, apps: list[dict]) -> list[dict]:
    usar(idioma)
    i = idioma
    raiz = f"{i}-portada" if i != "es" else None  # en inglés todo cuelga de /en/
    carpeta = "" if i == "es" else f"{i}/"

    def pagina(clave, slug, titulo_p, padre, orden, wp, local_p, destino):
        return {"clave": f"{i}-{clave}", "slug": slug, "titulo": titulo_p, "padre": padre, "orden": orden,
                "wp": wp, "local": carpeta + local_p, "url": destino, "plantilla": L["plantilla"], "idioma": i}

    paginas = [
        pagina("portada", "inicio" if i == "es" else L["raiz"], L["t_portada"], None, 0, portada_wp(apps),
               "index.html", url()),
        pagina("apps", L["apps"], L["t_apps"], raiz, 1, indice_apps_wp(apps), "apps/index.html", url("apps")),
        pagina("soporte", L["soporte"], L["t_soporte"], raiz, 2, indice_soporte_wp(apps), "soporte/index.html",
               url("soporte")),
        pagina("privacidad", L["privacidad"], L["t_privacidad"], raiz, 3, privacidad_wp(), "privacidad.html",
               url("privacidad")),
        pagina("aviso", L["aviso"], L["t_aviso"], raiz, 4,
               pagina_legal("aviso", "aviso-legal.md", L["aviso_h1"], L["aviso_entrada"]), "aviso-legal.html",
               url("aviso")),
        pagina("cookies", L["cookies"], L["t_cookies"], raiz, 5,
               pagina_legal("cookies", "cookies.md", L["cookies_h1"], L["cookies_entrada"]), "cookies.html",
               url("cookies")),
    ]
    for n, app in enumerate(apps):
        paginas.append(pagina(f"app-{app['slug']}", app["slug"], app["nombre"], f"{i}-apps", n,
                              pagina_app_wp(app), f"apps/{app['slug']}.html", url("apps", app["slug"])))
        paginas.append(pagina(f"sop-{app['slug']}", app["slug"], L["t_guia"].format(app["nombre"]), f"{i}-soporte",
                              n, pagina_soporte_wp(app), f"soporte/{app['slug']}.html", url("soporte", app["slug"])))
    partes = {L["parte_cab"]: cabecera_tema(), L["parte_pie"]: pie_tema()}
    return paginas, partes


def main():
    publicar_ya = "--publicar" in sys.argv
    apps_es = leer_apps("es")
    apps_en = leer_apps("en")
    preparar_imagenes(apps_es)
    preparar_banderas()
    for a in apps_en:  # mismas imágenes en los dos idiomas
        b = next(x for x in apps_es if x["slug"] == a["slug"])
        a.update({k: b[k] for k in ("icono", "capturas", "capturas_anchas")})
    if publicar_ya:
        subir_medios()

    paginas, partes, plantillas = [], {}, {}
    for idioma, apps in (("es", apps_es), ("en", apps_en)):
        p, t = paginas_idioma(idioma, apps)
        paginas += p
        partes.update(t)
        plantillas[L["plantilla"] or "page"] = plantilla_pagina()
    usar("es")

    # Copia local: wordpress/ tal cual se publica y sitio/ navegable sin servidor.
    mapa = {p["url"]: p["local"] for p in paginas}
    # Se regenera todo: fuera las salidas anteriores (así no quedan páginas de apps que salen de la web).
    for viejo in [*WP.rglob("*.html"), *SITIO.rglob("*.html")]:
        viejo.unlink()
    WP.mkdir(exist_ok=True)
    partes_wp = {k: resolver_imagenes(v) for k, v in partes.items()}
    for nombre, contenido in {**{f"_parte-{k}": v for k, v in partes_wp.items()},
                              **{f"_plantilla-{k}": v for k, v in plantillas.items()}}.items():
        (WP / f"{nombre}.html").write_text(contenido, encoding="utf-8")
    for p in paginas:
        p["local_wp"] = p["wp"]
        p["wp"] = resolver_imagenes(p["wp"])
        destino = WP / (p["url"].removeprefix(WP_URL).strip("/") or "inicio")
        destino = destino.with_name(destino.name + ".html")
        destino.parent.mkdir(parents=True, exist_ok=True)
        destino.write_text(p["wp"], encoding="utf-8")
        prof = p["local"].count("/")
        f = SITIO / p["local"]
        f.parent.mkdir(parents=True, exist_ok=True)
        idioma_p = p["idioma"]
        cab = partes["header" if idioma_p == "es" else f"header-{idioma_p}"]
        pie = partes["footer" if idioma_p == "es" else f"footer-{idioma_p}"]
        cuerpo = "\n".join(local(x, prof, mapa) for x in (cab, p["local_wp"], pie))
        f.write_text(plantilla_html(p["titulo"], resolver_imagenes(cuerpo, "../" * prof), prof, idioma_p),
                     encoding="utf-8")
    (SITIO / "estilo.css").write_text((RAIZ / "estilo.css").read_text(encoding="utf-8"), encoding="utf-8")
    shutil.copytree(IMG, SITIO / "img", dirs_exist_ok=True)
    print(f"{len(apps_es)} aplicaciones, {len(paginas)} páginas en dos idiomas generadas en sitio/ y wordpress/")

    if publicar_ya:
        subir_tema(partes_wp, plantillas)
        publicar(paginas)


if __name__ == "__main__":
    main()
