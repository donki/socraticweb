# TXT Reader
- slug: txtreader
- plataformas: Android
- lema: Abre y lee textos, logs, JSON y código al instante, sin anuncios ni cuentas.
- github: https://github.com/donki/TXTReader
- tiendas:
  - Google Play (producción): https://play.google.com/store/apps/details?id=com.socratic.txtreader (ficha pública accesible el 2026-09-25; paquete en TXTReader.csproj y Mobile/GooglePlayConsole/TXTReader/ficha.md; la pista alpha de prueba cerrada también existe según GRUPOS-VERIFICADORES.md)
  - Microsoft Store: no publicada (no hay ficha en Mobile/MicrosoftStore ni versión para Windows)
  - Edge Add-ons / Chrome / Firefox: no aplica
- descarga_alternativa: https://github.com/donki/TXTReader/releases (última: v2026.09.14.0, APK)

## Descripción

TXT Reader es un lector de archivos de texto para Android, rápido y sin distracciones. Abre notas, listas, registros (logs), ficheros de configuración, JSON, XML, CSV o Markdown y los enseña tal cual, con una letra de ancho fijo que respeta columnas y sangrías.

Detecta sola la codificación del fichero, así que las tildes, las eñes y los caracteres especiales se ven bien aunque el archivo venga de Windows, de un servidor o de otro programa. Puedes buscar dentro del texto con resaltado al momento, ajustar el tamaño de la letra y seleccionar y copiar fragmentos.

Los archivos se abren desde la propia aplicación o desde cualquier otra con «Abrir con»: el gestor de archivos, las descargas, el correo o la nube (OneDrive, Google Drive, Dropbox). No tiene anuncios, no pide cuenta y no necesita permisos de almacenamiento.

## Funciones principales

- Abre .txt, .log, .json, .xml, .gpx, .csv, .md, .ini, .cfg, .conf y otros ficheros de texto.
- Detección automática de la codificación (UTF-8, UTF-16, UTF-32, Windows-1252, ISO-8859-1).
- Búsqueda en el texto con resaltado en amarillo mientras escribes.
- Tamaño de letra ajustable con una barra deslizante (de 8 a 32 puntos).
- Selección y copia de texto como en un navegador.
- Lista de archivos recientes para volver a abrirlos con un toque.
- Se integra con «Abrir con» y «Compartir» de otras aplicaciones y de servicios en la nube.
- Modo claro y oscuro automático; en español e inglés.
- Sin anuncios, sin cuenta y sin permisos de almacenamiento.

## Guía de uso (soporte)

### Primera puesta en marcha

1. Instala la aplicación desde Google Play (o el APK de las releases de GitHub).
2. Ábrela. No te pedirá ningún permiso: los archivos se eligen con el selector de archivos del sistema, que solo da acceso al archivo que tú escojas.
3. El idioma sigue al del teléfono (español o inglés). Puedes cambiarlo en «Acerca de» › «Idioma».
4. Si hay conexión, al arrancar comprueba si existe una versión más nueva y, si la hay, te lo dice (ver «Aviso de actualización»).

### Flujo normal

1. En la pantalla principal pulsa «Seleccionar Archivo» y elige el fichero en el selector del sistema.
2. El texto se abre en el lector con el nombre del archivo como título.
3. Escribe en la caja de búsqueda para resaltar coincidencias, mueve la barra lateral para cambiar el tamaño de letra y mantén pulsado para seleccionar y copiar.
4. Pulsa el botón Atrás de Android para volver a la pantalla principal. El archivo queda en «Archivos Recientes».

También puedes abrir un archivo desde otra aplicación con «Abrir con» › TXT Reader (o «Compartir» / «Exportar» en Google Drive y Dropbox).

### Menú lateral

Se abre con el botón de menú de la barra superior. Tiene:
- **Inicio**: vuelve a la pantalla principal.
- **Acerca de**: abre la pantalla de información y ajustes de idioma.
- Al pie del menú se ve la versión instalada.

### Pantalla principal (TXT Reader)

- **Seleccionar Archivo**: abre el selector de archivos del sistema, filtrado para enseñar solo ficheros de texto (y los que Android no sabe clasificar, como .gpx, .log o .ini). Los PDF, imágenes y vídeos no aparecen.
- **Archivos Recientes**: tarjeta con los últimos 5 archivos abiertos, del más reciente al más antiguo, con su nombre y la fecha y hora en que se abrieron. Toca uno para volver a abrirlo. Si el archivo ya no existe, se quita de la lista y aparece el aviso «Archivo eliminado: El archivo ya no existe y ha sido eliminado del historial.». Si no has abierto nada aún, verás «No hay archivos recientes».
- **Acerca de**: abre la pantalla «Acerca de».

### Lector de texto

- **Título**: el nombre del archivo abierto.
- **Buscar en el texto...**: caja de búsqueda. Mientras escribes, todas las coincidencias se resaltan en amarillo. Borra el texto para quitar el resaltado.
- **Barra de tamaño (A+ / A-)**: barra vertical a la izquierda. Arrástrala hacia A+ para agrandar la letra y hacia A- para reducirla (de 8 a 32 puntos; empieza en 14).
- **Texto**: se muestra en letra de ancho fijo. Mantén pulsado para seleccionar y usa el menú del sistema para copiar.
- **Atrás** (botón del sistema): vuelve a la pantalla principal.

### Acerca de

- **Cabecera**: nombre de la app, «Versión X», «Lector de archivos de texto» y Socratic.
- **Contacto**: botón con el correo del autor. «Toca para enviar un correo electrónico» abre tu aplicación de correo.
- **Idioma**: botones **Español** y **English**. «Selecciona tu idioma preferido». El cambio se aplica al momento y se recuerda.
- **Privacidad**: resumen de qué hace la aplicación con tus datos.
- **Licencia**: «Esta aplicación es software libre distribuido bajo licencia MIT.»
- **Aviso Legal**: condiciones de uso «tal cual» y el aviso «Uso bajo su propio riesgo».
- **Volver**: regresa a la pantalla anterior.

### Aviso de actualización

Al abrir la aplicación, si hay una versión más nueva aparece «Actualización disponible: Hay una versión más reciente (X). Tienes la Y. ¿Quieres actualizar?» con dos botones:
- **Actualizar**: abre la página de descarga.
- **Ahora no**: cierra el aviso hasta la próxima vez que abras la app.

## Preguntas frecuentes

**No encuentro mi archivo en el selector o sale en gris.**
El selector solo enseña ficheros de texto. Si tu archivo tiene una extensión rara, asegúrate de tener la última versión: desde la 2026.08.01 también se admiten .gpx y otros que Android no sabe clasificar.

**Me sale «No se pudo acceder al archivo de Google Drive / Dropbox / almacenamiento en la nube».**
El archivo no está disponible sin conexión. Comprueba que tienes internet y permiso sobre el archivo; si persiste, descárgalo primero al teléfono y ábrelo desde ahí. En Dropbox, usa «Exportar» y elige TXT Reader.

**Un archivo reciente ha desaparecido de la lista.**
Al tocarlo, la aplicación comprobó que ya no existe (se borró o se movió) y lo quitó del historial. Ábrelo de nuevo con «Seleccionar Archivo» desde su nueva ubicación.

**Las tildes o las eñes se ven mal.**
La codificación se detecta automáticamente, pero ficheros muy cortos o con mezclas de codificaciones pueden confundirla. Guarda el archivo en UTF-8 desde el programa que lo creó y vuelve a abrirlo.

**El texto se ve muy pequeño o muy grande.**
Usa la barra vertical A+ / A- del lector. El tamaño vuelve a 14 puntos al abrir otro archivo.

**¿Dónde están los ajustes?**
No hay pantalla de ajustes: lo único configurable es el idioma, que está en «Acerca de».

**Solo veo 5 archivos recientes.**
Es el máximo; los más antiguos se van quitando solos.

## Privacidad

Los archivos se leen solo en tu teléfono; no se suben a ningún sitio y la lista de recientes se guarda en el propio dispositivo. La aplicación no tiene cuentas, anuncios ni rastreadores, y solo se conecta a internet para comprobar si hay una versión nueva.
