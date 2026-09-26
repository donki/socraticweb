# File Manager
- slug: filemanager
- plataformas: Android
- lema: Explorador de archivos ligero y privado: copia, mueve, busca y comparte, sin anuncios.
- github: https://github.com/donki/FileManager
- tiendas:
  - Google Play (producción): https://play.google.com/store/apps/details?id=com.socratic.filemanager (ficha pública accesible el 2026-09-25 con el título «File Manager: sin anuncios»; D:\sOCProjects\11-PENDIENTE-FileManager.md y Mobile/GooglePlayConsole/FileManager/ficha.md)
  - Microsoft Store: no publicada (no hay ficha en Mobile/MicrosoftStore ni versión para Windows)
  - Edge Add-ons / Chrome / Firefox: no aplica
- descarga_alternativa: https://github.com/donki/FileManager/releases (última: v2026.09.14.0, APK)

## Descripción

File Manager (en español, «Gestor de Ficheros») es un explorador de archivos para Android que no te espía ni te llena de anuncios. Te enseña las carpetas y archivos de tu teléfono o tablet y te deja organizarlos: copiar, mover, renombrar, borrar, crear carpetas, abrir y compartir.

Es ligero y rápido, con lo esencial y sin ruido. Puedes buscar por nombre en la carpeta actual y en todas sus subcarpetas, filtrar por tipo (imágenes, vídeo, audio, documentos, APK, comprimidos) y ordenar por nombre, fecha o tamaño. Con una pulsación larga marcas varios elementos y actúas sobre todos a la vez.

No tiene anuncios, ni compras, ni cuenta. Todo ocurre en tu dispositivo: la aplicación solo se conecta a internet para avisarte de una versión nueva.

## Funciones principales

- Navegación por carpetas con ruta pulsable y botón Atrás que sube un nivel.
- Iconos por tipo de archivo y fecha, tamaño y número de elementos de cada entrada.
- Copiar, mover, renombrar, eliminar y crear carpetas.
- Selección múltiple con pulsación larga para copiar, mover o borrar en lote.
- Al pegar, eliges entre reemplazar o conservar ambos.
- Búsqueda por nombre en la carpeta actual y sus subcarpetas.
- Filtro por tipo y ordenación por nombre, fecha o tamaño.
- Abre cada archivo con la app adecuada (incluida la instalación de APK) y compártelo con cualquier app.
- Muestra u oculta los archivos ocultos; confirmación opcional antes de borrar.
- Modo claro y oscuro; en español e inglés.

## Guía de uso (soporte)

### Primera puesta en marcha

1. Instala la aplicación desde Google Play y ábrela.
2. Verás la pantalla «Se necesita acceso al almacenamiento». Un gestor de archivos necesita el permiso **Acceso a todos los archivos** para poder ver y ordenar tus carpetas; Android no lo concede con un diálogo normal, sino desde sus ajustes.
3. Pulsa **Conceder acceso**. Se abrirá la pantalla del sistema: activa el interruptor para File Manager y vuelve atrás. La aplicación lo detecta sola y muestra tus archivos.
4. Hay un segundo permiso que Android puede pedirte más tarde, **Instalar aplicaciones desconocidas**, solo si tocas un archivo APK y quieres instalarlo. Cada instalación la confirmas tú en el diálogo del sistema.
5. El idioma sigue al del teléfono (español o inglés; si es otro, inglés). Puedes cambiarlo en «Configuración».

### Flujo normal

1. La lista arranca en «Almacenamiento interno». Toca una carpeta para entrar y un archivo para abrirlo.
2. Para subir un nivel usa la flecha de la barra superior, el botón Atrás de Android o toca cualquier tramo de la ruta que aparece bajo la barra.
3. Para actuar sobre un elemento, pulsa sus tres puntos (⋮). Para actuar sobre varios, mantén pulsado uno y ve marcando los demás.
4. Tras «Copiar» o «Mover», navega a la carpeta de destino y pulsa **Pegar** en la barra inferior.

### Pantalla principal

Barra superior:
- **Menú (tres rayas)**: abre el menú lateral con **Inicio**, **Configuración** y **Acerca de**, y la versión de la aplicación al pie.
- **Flecha atrás**: sube a la carpeta superior (no aparece en la raíz).
- **Título**: «Almacenamiento interno» en la raíz o el nombre de la carpeta; debajo, el número de elementos.
- **Lupa (Buscar)**: muestra la caja «Buscar en esta carpeta…». Escribe y se buscan por nombre los archivos de la carpeta actual y de todas sus subcarpetas (hasta 500 resultados). Si no hay coincidencias: «Ningún fichero coincide con la búsqueda».
- **Tres puntos (Más)**: abre el menú con:
  - **Seleccionar**: entra en el modo de selección múltiple.
  - **Filtrar por tipo**: Todos los tipos, Imágenes, Vídeo, Audio, Documentos, APK, Comprimidos, Otros.
  - **Ordenar por**: Nombre (A–Z), Nombre (Z–A), Fecha (más reciente primero), Fecha (más antiguo primero), Tamaño (mayor primero), Tamaño (menor primero). Las carpetas van siempre delante.
  - **Mostrar ficheros ocultos** / **Ocultar ficheros ocultos**: enseña u oculta los que empiezan por punto.
  - **Actualizar**: vuelve a leer la carpeta.
  - **Configuración**: abre los ajustes.
  - **Acerca de**: abre la información de la aplicación.
- **Ruta de navegación**: cada tramo de la ruta se puede tocar para saltar a esa carpeta.

Lista:
- Cada fila muestra el icono del tipo, el nombre y, debajo, la fecha y el tamaño (o el número de elementos si es carpeta).
- **Toque**: entra en la carpeta o abre el archivo con la aplicación asociada. Un APK abre el instalador de Android.
- **Pulsación larga**: entra en el modo de selección con ese elemento marcado.
- **Tres puntos de cada fila**: menú con **Seleccionar**, **Abrir**, **Compartir** (solo archivos), **Copiar**, **Mover**, **Renombrar**, **Detalles** y **Eliminar**.
  - **Renombrar**: pide «Nuevo nombre» con **Guardar** y **Cancelar**.
  - **Detalles**: Nombre, Ruta, Tipo, Tamaño (o Contenido en carpetas) y Modificado.
  - **Eliminar**: pide confirmación si está activada en Configuración. Borrar una carpeta borra todo su contenido y no se puede deshacer.
- **Carpeta vacía**: «Esta carpeta está vacía. Crea una carpeta o pega ficheros aquí».

Botón flotante:
- **Más (+) (Nueva carpeta)**: pide «Nombre de la carpeta» y la crea en la carpeta actual.

Modo de selección (barra superior de selección):
- **X**: sale del modo selección (también con el botón Atrás).
- **Contador**: «N seleccionados».
- **Seleccionar todo**: marca todo lo que se ve.
- **Tres puntos**: **Copiar**, **Mover** o **Eliminar** los elementos marcados. Si no hay ninguno: «Selecciona algún elemento primero».
- Tocar una fila la marca o desmarca.

Barra de pegar (aparece tras Copiar o Mover):
- Indica cuántos elementos llevas y si vas a copiar o mover.
- **Pegar**: los deja en la carpeta actual. Si ya existe alguno con el mismo nombre, pregunta «El elemento ya existe» con **Reemplazar**, **Conservar ambos** o **Cancelar**.
- **Cancelar**: vacía el portapapeles.

### Configuración

- **Idioma**: botones **Español** y **English**. Aviso: «La aplicación sigue el idioma del dispositivo y usa inglés cuando no está soportado.» Al elegir uno, se aplica al momento y se recuerda.
- **Visualización**:
  - **Mostrar ficheros ocultos** (interruptor): muestra los ficheros y carpetas cuyo nombre empieza por punto.
  - **Preguntar antes de eliminar** (interruptor): muestra un diálogo de confirmación antes de eliminar nada.
- **Almacenamiento**:
  - **Acceso a todos los ficheros**: estado «Concedido» o «No concedido».
  - **Abrir ajustes**: lleva a la pantalla del sistema donde se concede o se retira el permiso.
- **Acerca de**: abre la pantalla de información.

### Acerca de

- Nombre, «Versión X», «Explora y gestiona los ficheros de tu dispositivo» y Socratic.
- **Contacto**: botón con el correo; «Toca para enviar un correo electrónico».
- **Idioma**: botones **Español** y **English**; «Selecciona tu idioma preferido».
- **Privacidad**, **Licencia** (MIT) y **Aviso Legal** con «Uso bajo su propio riesgo».
- **Volver**.

### Aviso de actualización

Si hay una versión más nueva: «Actualización disponible: Hay una versión más reciente (X). Tienes la Y. ¿Quieres actualizar?», con **Actualizar** y **Ahora no**.

## Preguntas frecuentes

**No se ve ningún archivo.**
Falta el permiso de acceso a todos los archivos. Ve a Configuración › Almacenamiento › Abrir ajustes y activa el interruptor para File Manager.

**Una carpeta sale vacía pero sé que tiene contenido.**
Probablemente es Android/data o Android/obb. Desde Android 11 el sistema las bloquea para todas las aplicaciones, incluso con acceso a todos los archivos.

**Al tocar un archivo me dice «Ninguna aplicación del dispositivo puede abrir este tipo de fichero».**
No tienes instalada ninguna app que sepa abrir ese formato. Instala una (por ejemplo, un lector de PDF o un reproductor) y vuelve a intentarlo.

**No me deja crear o renombrar: «El nombre contiene caracteres no permitidos».**
Los nombres no pueden llevar \ / : * ? " < > |. Tampoco puede haber dos elementos con el mismo nombre en la misma carpeta.

**«Una carpeta no se puede copiar dentro de sí misma.»**
Estás intentando pegar una carpeta dentro de ella misma o de una de sus subcarpetas. Elige otro destino.

**La barra de selección tapaba el primer elemento.**
Se corrigió en la versión 2026.08.28. Actualiza a la última.

**No veo mis archivos ocultos.**
Actívalos en Más › Mostrar ficheros ocultos o en Configuración › Visualización.

**Borré algo por error.**
El borrado es definitivo: no hay papelera. Activa «Preguntar antes de eliminar» en Configuración para que siempre te pida confirmación.

## Privacidad

File Manager usa el acceso a tus archivos solo para enseñártelos y hacer lo que le pidas; no los sube a ningún sitio ni recoge estadísticas. No hay cuentas, anuncios ni rastreadores, y la única conexión a internet es para comprobar si hay una versión nueva.
