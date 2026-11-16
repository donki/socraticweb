# sOC Scanner
- slug: scanner
- plataformas: Windows 10 (versión 2004) o posterior y Windows 11, 64 bits
- lema: Escanea con un solo botón con cualquier escáner o cámara, hoja a hoja o en serie, a PDF, JPG, PNG, TIFF o BMP.
- github: https://github.com/donki/Scanner
- tiendas:
  - Microsoft Store (publicada): https://apps.microsoft.com/detail/9N9S5ZP2SG54 (Partner Center: «En Microsoft Store», 2026-11-16)
  - Google Play: no aplica (solo Windows).
- descarga_alternativa: https://github.com/donki/Scanner/releases (última: v2026.10.22.0; un ejecutable autocontenido)

## Descripción

sOC Scanner escanea con un solo botón (o con Intro) con cualquier escáner que reconozca Windows o con una cámara. Pones la hoja, pulsas y sale en la vista previa; cuando tienes todas, las guardas en un PDF de varias páginas, en TIFF, JPG, PNG o BMP.

Vale cualquier escáner o impresora multifunción, por USB o por red, del cristal o del alimentador, y también una cámara: la del portátil, una webcam o una cámara de documentos, con vista en directo. La calidad se elige con un clic (texto en blanco y negro, documento en gris, documento en color o foto) o a medida, y lo que el dispositivo no admite se ajusta solo y se explica.

Para muchas hojas seguidas está el modo **en serie**: cada hoja se guarda sola nada más escanearla, con un nombre correlativo (`Factura_0007.pdf`), sin pisar nunca un fichero. Es software libre, sin cuenta, sin anuncios y sin rastreadores, y no se conecta a internet.

## Funciones principales

- Escanear con un botón o con Intro; Esc cancela.
- Cualquier escáner o multifunción que reconozca Windows, por USB o por red, del cristal o del alimentador (todas las hojas de una vez).
- Una cámara como escáner: la del portátil, una webcam o una cámara de documentos, con vista en directo y resolución a elegir.
- Calidad a un clic (texto en blanco y negro, documento en gris, documento en color, foto) o a medida: resolución, color, tamaño de la hoja, brillo, contraste y calidad JPEG, con los megapíxeles y los MB de cada hoja a la vista.
- Lo que el dispositivo no admite se ajusta solo y se dice: el gris y el blanco y negro se sacan de una imagen en color, y el brillo y el contraste se aplican a la imagen si hace falta.
- Una a una: vista previa, girar, ordenar y quitar hojas, y guardar en PDF o TIFF de varias páginas, o en JPG, PNG o BMP.
- En serie: cada hoja se guarda sola con prefijo, número correlativo y sufijo; el contador sigue otro día.
- PDF escrito por la propia aplicación: una página por hoja, del tamaño real; el blanco y negro en 1 bit sin pérdida (una hoja de texto ocupa unas decenas de KB).
- Al terminar: abrir, enseñar en su carpeta o copiar el fichero para pegarlo en un correo o un chat.
- Los fallos se explican con la razón y qué hacer: sin papel, atasco, tapa abierta, ocupado, apagado, permiso de la cámara, fichero abierto, disco lleno…

## Guía de uso (soporte)

### Instalación

1. Instálala desde la [Microsoft Store](https://apps.microsoft.com/detail/9N9S5ZP2SG54), que la mantiene al día sola.
2. O descarga el ejecutable `sOCScanner.exe` desde la página de versiones de GitHub (https://github.com/donki/Scanner/releases) y ábrelo con doble clic: no hay que instalar nada. Si Windows avisa de que el editor es desconocido, pulsa «Más información» y «Ejecutar de todas formas».

Requisitos: Windows 10 (versión 2004) o posterior, o Windows 11, de 64 bits. El escáner tiene que estar añadido en Windows (Impresoras y escáneres) con el controlador del fabricante.

### Primera puesta en marcha

La primera vez se abre la «Guía de configuración», paso a paso (Atrás / Siguiente abajo): el escáner o la cámara en Windows (con un botón a Impresoras y escáneres), el permiso de la cámara (solo si vas a usar una), la calidad y la carpeta y los nombres de la serie. Cada paso dice si está hecho, pendiente u opcional. Se vuelve a abrir cuando quieras con el botón de ayuda (?).

### Ventana principal

- **Escáner o cámara**: la lista de dispositivos, con el botón de recargar. Debajo, lo que admite el elegido (cristal, alimentador, resoluciones) y, si tiene las dos cosas, si escanea del cristal o del alimentador.
- **Calidad**: la calidad lista para usar y, con el engranaje, el diálogo para ajustarla a medida.
- **Cómo trabajar**: Una a una o En serie, con el formato que se propone al guardar o, en serie, la carpeta, el formato y el nombre de la próxima hoja.
- **Vista previa**: la hoja elegida en grande y, debajo, todas las escaneadas, con los botones para girar, quitar y moverlas.
- **Abajo**: el botón de escanear (Intro), Guardar y Descartar, y lo que ha pasado con la última hoja.
- **Arriba a la derecha**: Guía, Novedades, Español / English y Acerca de.

### Calidad a medida

El engranaje junto a la calidad abre un diálogo: resolución (solo las que admite el dispositivo elegido), color, gris o blanco y negro, tamaño de la hoja (A4, Carta, A5 o todo el cristal), brillo, contraste y calidad JPEG (también la de las fotos dentro del PDF). Abajo se ven los megapíxeles por hoja y lo que ocupa antes de comprimir.

### En serie

Elige la carpeta, el formato y el nombre: lo que va antes y después del número, el número siguiente y sus cifras. Cada hoja se guarda sola nada más escanearla y se ve el nombre de la próxima. Si un número ya existe, se salta al siguiente libre: nunca se pisa un fichero.

## Preguntas frecuentes

**Mi escáner no sale en la lista.**
Añádelo en Windows (Configuración › Bluetooth y dispositivos › Impresoras y escáneres) con el controlador del fabricante, enciéndelo y pulsa el botón de recargar. La guía de configuración tiene un botón que abre esa página.

**La misma impresora sale dos veces.**
Una por USB y otra por red. Las dos sirven; por USB suele dar más resolución.

**¿Por qué no me deja elegir 1200 ppp?**
Solo salen las resoluciones que admite el dispositivo elegido. Si pides una calidad que no llega, se ajusta a la más alta que tiene y te lo dice.

**La cámara no se enciende.**
Windows tiene que dejar que las aplicaciones de escritorio usen la cámara: Configuración › Privacidad y seguridad › Cámara › «Permitir que las aplicaciones de escritorio accedan a la cámara». La guía lo abre.

**¿Cuánto ocupa una hoja?**
Una hoja de texto en blanco y negro, unas decenas de KB en PDF. El diálogo de calidad enseña los megapíxeles y los MB antes de escanear.

## Privacidad

Todo se queda en tu PC: lo escaneado en la carpeta que elijas, los ajustes en tu perfil y un registro de errores sin datos personales. La aplicación usa el escáner y la cámara solo al elegirlos y escanear. No se conecta a internet ni sube nada. Sin cuenta, sin anuncios, sin rastreadores, sin analítica.
