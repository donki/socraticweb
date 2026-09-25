# Music Player
- slug: musicplayer
- plataformas: Android / Android Auto
- lema: Tu música del móvil, por grupo o compositor, con listas y en el coche.
- github: https://github.com/donki/MusicPlayer
- tiendas:
  - Google Play (prueba cerrada): https://play.google.com/store/apps/details?id=com.socratic.musicplayer — solo en la pista de prueba cerrada (alpha 2026091401), sin producción; la página pública de Play aún no existe (devuelve 404 a 2026-09-25) (fuente: D:\sOCProjects\04-PENDIENTE-MusicPlayer.md; paquete en MusicPlayer.csproj y README.md)
  - Microsoft Store: no publicada (solo Android; no hay ficha ni ID de Store en el proyecto)
- descarga_alternativa: https://github.com/donki/MusicPlayer/releases

## Descripción
Music Player reproduce la música que ya tienes guardada en el móvil, sin cuentas, sin anuncios y sin suscripciones: solo tu biblioteca. La ordena por grupo (o por compositor, si escuchas música clásica), te deja buscar al momento y hacer tus propias listas, incluida una de favoritas.

Sigue sonando con la pantalla apagada, con los controles en la notificación, y funciona en Android Auto: en el coche tienes toda tu biblioteca organizada en grupos, listas y canciones, con los botones del volante y por voz.

Si quieres, puede buscar la foto y una reseña breve de cada grupo en Wikipedia; viene apagado y, al activarlo, lo único que sale del móvil es el nombre del grupo. También muestra la letra de la canción cuando el propio fichero la trae, e incluso va marcando la línea que suena.

## Funciones principales
- Reproduce los formatos de audio que admite Android: MP3, AAC/M4A, FLAC, OGG, Opus, WAV, MIDI y AMR.
- Biblioteca agrupada por grupo o por compositor, con búsqueda por grupo, canción o álbum.
- Listas de reproducción propias y lista de Favoritas; una canción se puede añadir a varias listas de una vez.
- Modo aleatorio y repetición de la lista o de una sola canción.
- Selección múltiple para reproducir, añadir a listas, quitar o borrar varias canciones a la vez.
- Corrección de la información de las canciones (título, artista, álbum, compositor, año, pista) e imagen personalizada.
- Ficha de la canción con la letra, sincronizada con la música cuando el fichero lo permite.
- Fotos y reseñas de los grupos (opcional, apagado por defecto).
- Android Auto con carpetas de Favoritas, Grupos, Listas y Canciones, botones de favorita, aleatorio y repetir, y control por voz.
- Al volver a abrirla, recupera la última canción que escuchabas, en pausa.

## Guía de uso (soporte)

### Primera puesta en marcha
1. Abre la aplicación. En **Biblioteca** verás el aviso **Acceso a tu música**: «Music Player necesita permiso para leer los archivos de audio guardados en este dispositivo. No se sube nada a ninguna parte.» Pulsa **Conceder acceso** y acepta el permiso de Android. Sin él no hay nada que reproducir.
2. Android también te pedirá permiso para **mostrar notificaciones**: es la notificación con los controles de reproducción, que permite que la música siga sonando con la pantalla apagada.
3. La aplicación explora el móvil («Explorando el dispositivo…») y te muestra el resumen «N canciones · N grupos».
4. Si no encuentra nada («No se ha encontrado música»), copia archivos de audio al móvil y vuelve a explorar. Si tu música está en una tarjeta o no aparece, usa **Configuración › Buscar en todo el móvil**.
5. Opcional: si quieres fotos y reseñas de los grupos, activa **Configuración › Buscar fotos y biografías de los grupos**.

### Flujo normal
- En **Biblioteca**, elige un grupo, una canción o una lista y toca una canción para que empiece a sonar.
- Controla la reproducción desde el mini reproductor de abajo, desde **Reproduciendo**, desde la notificación o desde el coche.
- Para cualquier acción sobre una canción, pulsa su botón de menú (los tres puntos); para varias a la vez, mantén pulsada una para entrar en la selección múltiple.

### Menú lateral
- **Biblioteca**: grupos, canciones y listas.
- **Reproduciendo**: la canción que suena, a pantalla completa.
- **Configuración**: biblioteca, información en línea, Android Auto e idioma.
- **Acerca de**: versión, contacto, idioma, privacidad, licencia y aviso legal.
- Al pie aparece la versión instalada.

### Pantalla Biblioteca
- **Volver a explorar el dispositivo** (icono de flechas, arriba a la derecha): vuelve a leer la música del móvil.
- **Buscador** («Buscar grupo, canción o álbum»): filtra al momento. Si no hay coincidencias: «Sin resultados».
- **Pestañas** (con icono): **Grupos**, **Canciones** y **Listas**.
- **Grupos**: cada grupo (o compositor) con su foto o la carátula de su primera canción y el número de canciones. Tócalo para abrir la pantalla del grupo.
- **Canciones**: todas las canciones. Toca una para reproducirla; su botón de menú abre las acciones de la canción.
- **Listas**: la lista **Favoritas** (siempre la primera; no se puede renombrar ni borrar) y tus listas. Toca una para abrirla. El menú de cada lista ofrece **Renombrar lista** y **Eliminar** («La lista se eliminará. Las canciones seguirán en el dispositivo.»). El botón **Nueva lista** pide el **Nombre de la lista** («Mi lista»); avisa si ya existe una con ese nombre. Si no hay ninguna: «Todavía no hay listas».
- **Mini reproductor** abajo: carátula, título, grupo, barra de progreso y botones anterior / reproducir-pausa / siguiente. Tócalo para abrir **Reproduciendo**.

### Menú de una canción (botón de tres puntos)
- **Reproducir**.
- **Añadir a favoritas** / **Quitar de favoritas**.
- **Añadir a listas**: abre la pantalla para marcar varias listas a la vez.
- **Ir al grupo**.
- **Ficha y letra**: abre la ficha de la canción.
- **Editar la información**: abre la pantalla de edición.
- **Quitar de esta lista** (solo dentro de una lista).
- **Eliminar del dispositivo**: borra el fichero («No se puede deshacer»), con la confirmación de Android. La canción desaparece también de todas las listas.

### Selección múltiple
Mantén pulsada una canción en Canciones, en un grupo o en una lista. Aparece una barra con el recuento («N seleccionadas») y los botones:
- **Reproducir** la selección.
- **Añadir a listas**.
- **Seleccionar todo**.
- **Más**: **Quitar de esta lista** (dentro de una lista) y **Eliminar del dispositivo** (una sola confirmación para todas).
- **Cerrar**: sale del modo selección.

### Pantalla del grupo
- Foto del grupo, nombre y número de canciones.
- **Reseña** del grupo (si la búsqueda en línea está activada), recortada a tres líneas con un botón de tres puntos para verla entera o plegarla, y la fuente: «Imagen y texto: Wikipedia / Wikidata (CC BY-SA); grupo identificado con MusicBrainz.»
- Si la búsqueda está apagada, aviso con el botón **Activar búsqueda en línea**.
- **Actualizar información** (icono de flechas): vuelve a buscar la foto y la reseña («Información actualizada» o «No se ha encontrado nada de este grupo»).
- **Imagen** (icono de imagen): cambia la foto del grupo: **Del dispositivo**, **De una dirección** (pegas la dirección de una imagen), **Buscarla en Google** o **Quitar la personalizada**.
- **Renombrar grupo** (icono de lápiz): cambia el nombre del grupo en todas sus canciones.
- **Reproducir todo** y **Aleatorio**.
- Lista de canciones del grupo, con su menú y la selección múltiple.

### Pantalla de una lista
- Nombre de la lista y número de canciones.
- **Reproducir todo** y **Aleatorio** (desactivados si está vacía: «Esta lista aún no tiene canciones.»).
- Canciones con su menú (incluye **Quitar de esta lista**) y selección múltiple.

### Pantalla Reproduciendo
- Carátula, título, grupo, álbum y posición en la cola («3 de 12»).
- Barra de progreso que puedes arrastrar, con el tiempo reproducido y la duración.
- **Anterior** (si la canción lleva más de 3 segundos, vuelve a su principio), **Reproducir/Pausa** y **Siguiente**.
- **Favorita** (corazón), **Aleatorio** («Reproducción aleatoria activada/desactivada») y **Repetir**, que pasa por **Sin repetición**, **Repetir todo** y **Repetir una**.
- **Información**: abre la ficha y la letra.
- **Añadir a listas** y **Eliminar** (borra la canción del dispositivo).
- Si no suena nada: «No hay nada en reproducción. Elige una canción de la biblioteca para empezar.», con un botón para ir a la **Biblioteca**.

### Pantalla Ficha de la canción
- Carátula, título, grupo, álbum, datos de la pista (**Archivo**, **Duración**...).
- **Sobre el grupo**: foto y reseña (si la búsqueda en línea está activada).
- **Letra**: la que trae el propio fichero o un fichero .lrc con el mismo nombre al lado. Si está sincronizada aparece **Sigue la música** y la línea que suena se va marcando. Si no hay: «Esta canción no trae letra... nunca la descarga.»
- Botones con icono para **editar** la información (lápiz) y **cerrar** la ficha (aspa).

### Pantalla Información de la canción (edición)
- Campos **Título** (obligatorio), **Artista**, **Artista del álbum**, **Álbum**, **Compositor**, **Pista** y **Año**.
- **Imagen**: la misma elección que en el grupo (del dispositivo, de una dirección, buscarla en Google o quitar la personalizada).
- **Buscar información en internet**: busca la canción y, si la encuentra, te propone los datos (**Usarla** rellena los campos para que los revises y guardes). Necesita la búsqueda en línea activada.
- **Deshacer la corrección**: vuelve a los datos del fichero.
- **Guardar** y **Cancelar**.
- La corrección la guarda la aplicación y, si el sistema lo permite, también el índice de medios de Android; el fichero de audio nunca se reescribe.

### Pantalla Añadir a listas
- Marca todas las listas a las que quieras añadir la canción (o las canciones seleccionadas).
- **Nueva lista** para crear una en el momento.
- **Guardar** («Añadida a N listas») o **Cancelar**.

### Pantalla Configuración
**Biblioteca**
- **Volver a explorar el dispositivo**: lee los archivos de audio que el sistema tiene indexados. Úsalo después de copiar música nueva.
- **Buscar en todo el móvil**: pide al sistema que vuelva a indexar la memoria interna y todas las tarjetas y añade lo que encuentre («N canciones nuevas»). Puede tardar unos minutos.
- **Incluir todo el audio** (interruptor): muestra también lo que el sistema no marca como música, como grabaciones, podcasts y audiolibros de 30 segundos o más.
- **Buscar carátulas**: para cada canción sin carátula, saca la imagen que lleva dentro el fichero o el cover.jpg de su carpeta («Carátulas encontradas: N»).
- **Releer etiquetas**: vuelve a leer título, grupo, álbum, compositor, año y pista de los ficheros y rellena lo que falte, respetando lo que hayas corregido a mano («Canciones completadas: N»).
- Mientras trabaja, muestra el progreso («N de M…»); si ya hay un escaneo en marcha, avisa.
- **Agrupar por compositor** (interruptor): agrupa por compositor en lugar de por intérprete. Útil para música clásica.

**Información en línea**
- **Buscar fotos y biografías de los grupos** (interruptor, apagado por defecto): al activarlo, solo se envía el nombre del grupo a MusicBrainz y Wikidata/Wikipedia para buscar una foto y una biografía breve.
- **Borrar las imágenes descargadas**: vacía las fotos guardadas («Imágenes descargadas borradas»).

**Android Auto**
- Solo informativo: la biblioteca está disponible en el coche sin configurar nada.

**Idioma**
- **Español** / **English**: el idioma se aplica de inmediato.

### Pantalla Acerca de
- Nombre, **Versión** y autor (Socratic), con la descripción de la aplicación.
- **Contacto**: botón para escribir un correo («Dudas, fallos e ideas son bienvenidos.»).
- **Idioma**: **Español** / **English**.
- **Privacidad**, **Licencia** (MIT) y **Aviso legal** («Uso bajo su propio riesgo»).

### Android Auto
- Conecta el móvil al coche y abre Music Player en la lista de aplicaciones de medios. Verás **Favoritas**, **Grupos**, **Listas** y **Canciones**.
- En la pantalla de reproducción del coche tienes, además de anterior / pausa / siguiente, los botones **Favorita**, **Aleatorio** y **Repetir**; cuando están activados el icono va dentro de un círculo relleno.
- Puedes pedir la música por voz con el asistente del coche.

### Aviso de versión nueva
Al arrancar, si hay una versión más reciente aparece **Actualización disponible** («Está disponible la versión X. Tienes la Y. ¿Quieres abrir la página de descarga?»): **Abrir** o **Más tarde**.

## Preguntas frecuentes
**En el coche sale «Abre Music Player en el móvil y permite el acceso a tu música».**
Aún no has dado permiso de acceso a la música. Abre la aplicación en el móvil (o pulsa **Abrir en el móvil** en el coche) y concede el acceso; la biblioteca del coche se rellena sola al momento.

**Music Player no aparece en Android Auto.**
Si instalaste la aplicación desde un archivo y no desde Google Play, Android Auto la oculta: activa las opciones de desarrollador de Android Auto y marca «Unknown sources» (orígenes desconocidos).

**No encuentra mi música o faltan canciones.**
Pulsa **Volver a explorar el dispositivo** y, si siguen faltando (por ejemplo, música en la tarjeta), **Configuración › Buscar en todo el móvil**. Si son grabaciones, podcasts o audiolibros, activa **Incluir todo el audio**.

**Mis canciones salen como «Grupo desconocido» o «Sin título», o mal agrupadas.**
Usa **Configuración › Releer etiquetas** para rellenar lo que falte desde los ficheros. Para una canción concreta, **Editar la información** desde su menú; para un grupo entero, **Renombrar grupo** en su pantalla.

**No salen las carátulas.**
Pulsa **Configuración › Buscar carátulas**: usa la imagen que lleva dentro el fichero o el cover.jpg de su carpeta. También puedes poner una imagen a mano desde **Editar la información › Imagen**.

**No veo la foto ni la reseña de los grupos.**
La búsqueda en línea viene apagada. Actívala en **Configuración › Buscar fotos y biografías de los grupos** (necesita conexión). Si un grupo no aparece, pulsa **Actualizar información** en su pantalla.

**No sale la letra.**
Music Player no descarga letras: solo muestra la que trae el propio fichero o un .lrc con el mismo nombre en la misma carpeta.

**He borrado una canción sin querer.**
«Eliminar del dispositivo» borra el fichero del móvil y no se puede deshacer. Si solo querías sacarla de una lista, usa **Quitar de esta lista**.

## Privacidad
Tu música, tus listas y tus preferencias se quedan en el móvil: no hay cuentas, ni anuncios, ni analítica. Solo hay dos conexiones a Internet: la comprobación de si hay una versión nueva al arrancar y, únicamente si la activas, la búsqueda de fotos y reseñas de grupos, que envía solo el nombre del grupo a MusicBrainz, Wikidata y Wikipedia. Si además pulsas **Buscar información en internet** al editar una canción, se consulta en MusicBrainz su título y su grupo.
