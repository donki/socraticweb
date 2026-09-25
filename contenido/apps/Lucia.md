# sOC Lucia
- slug: lucia
- publicar: no (Josep, 2026-09-25: de momento fuera de la web)
- plataformas: Windows 10 (versión 2004) o posterior y Windows 11, 64 bits; extensión opcional para Visual Studio Code
- lema: Una inteligencia artificial privada que vive en tu PC: nada de lo que escribes sale de él.
- github: https://github.com/donki/Lucia
- tiendas: ninguna. No está en la Microsoft Store (fuente: README.md del repositorio, «No está en la Microsoft Store»; la ficha de la Store está pendiente «solo si Josep quiere publicarla» según D:\sOCProjects\04-TAREAS-Lucia.md). Sin identificador de producto.
- descarga_alternativa: https://github.com/donki/Lucia/releases (última: v2026.9.22.1; ejecutable, paquete MSIX y extensión de VS Code .vsix)

## Descripción

sOC Lucia es un asistente de inteligencia artificial que funciona entero en tu ordenador. Hablas con ella desde una ventana de chat, como con los asistentes de internet, pero la IA se descarga una vez y a partir de ahí responde desde tu propio PC: tus preguntas, tus documentos y tus conversaciones no salen de él. No necesitas cuenta ni suscripción.

La aplicación analiza tu equipo y te recomienda la IA que mejor le va, entre una selección de modelos abiertos, o te deja buscar otros. Además de conversar, puede entender imágenes que le adjuntes, dibujar imágenes a partir de una descripción, tener en cuenta los documentos de una carpeta tuya, crear documentos (incluido Word), recordar cosas sobre ti y ejecutar tareas programadas, como un resumen cada mañana.

En modo agente, Lucia puede usar tu PC para resolver una tarea paso a paso: leer y escribir ficheros, ejecutar órdenes, buscar en internet o abrir programas, siempre enseñándote antes qué va a hacer y pidiéndote permiso. Y si programas, puedes usar esa misma IA desde Visual Studio Code con su extensión.

## Funciones principales

- Chat con una IA que se ejecuta en tu PC, con conversaciones guardadas en el equipo.
- Elección de la IA según tu equipo: análisis del PC, recomendación, catálogo de modelos abiertos y buscador de Hugging Face.
- Adjuntar ficheros e imágenes; la IA entiende las imágenes si el modelo tiene visión.
- Generación de imágenes en el propio PC («dibuja…»).
- Modo agente con permisos por recurso: órdenes, ficheros, internet, portapapeles y abrir cosas.
- Tus documentos: la IA consulta una carpeta tuya y genera documentos (.md, .txt, .html, .csv y .docx).
- Memoria sobre ti y tareas programadas que se ejecutan solas.
- Búsqueda en internet opcional (se puede desactivar para trabajar sin conexión).
- Integración con Visual Studio Code y otros editores de código compatibles.
- Bandeja del sistema y arranque con Windows; español e inglés; tema claro y oscuro.

## Guía de uso (soporte)

### Instalación

1. Descarga la última versión desde https://github.com/donki/Lucia/releases:
   - `sOCLucia.exe`: no necesita instalación, se abre con doble clic.
   - `sOCLucia.msix`: se instala como cualquier aplicación de Windows.
   - `soc-lucia-code-….vsix`: la extensión opcional para Visual Studio Code.
2. Abre la aplicación. Solo puede haber una abierta: si la vuelves a ejecutar, trae al frente la que ya estaba (aunque esté en la bandeja).

### Requisitos

- Windows 10 (versión 2004) o posterior, o Windows 11.
- Espacio en disco para la IA: según el modelo, de menos de 1 GB a unos 16 GB.
- Memoria: la aplicación solo te enseña las IA que caben en tu equipo. Con una tarjeta gráfica con memoria propia las respuestas son mucho más rápidas; sin ella la IA funciona en el procesador.
- Conexión a internet solo para descargar el motor y la IA la primera vez (y, si lo permites, para las búsquedas web).

### Primera puesta en marcha

1. La primera vez no hay ninguna IA instalada: la barra de estado indica «Sin IA instalada» y el chat, «Todavía no hay ninguna IA instalada. Elige una en Ajustes.»
2. Abre Ajustes (engranaje). En «La IA» verás el análisis de tu PC (procesador, memoria y gráfica) y el catálogo. Las marcadas con ★ son óptimas para tu equipo y una aparece como «Recomendada».
3. Pulsa «Instalar» en la que quieras. Antes de descargar se muestra su licencia. La descarga sigue aunque cierres Ajustes (el progreso se ve en la barra de estado) y, si cierras la aplicación a medias, continúa donde iba al volver a abrirla.
4. Al terminar, la IA queda en uso: «Instalada. La siguiente pregunta ya la usará.»
5. Escribe tu pregunta en el redactor y pulsa Intro. La primera respuesta tras abrir la aplicación tarda un poco: «Cargando la IA en memoria…».

No hay que crear cuenta ni iniciar sesión.

### Ventana principal

**Columna izquierda: Conversaciones**
- Nueva conversación. Al abrir la aplicación siempre se empieza una nueva; las anteriores siguen en la lista.
- Ajustes.
- Acerca de.
- Lista de conversaciones: clic para abrirla. En cada fila, «Renombrar» (pide el título de la conversación) y «Borrar conversación» («¿Borrar esta conversación? No se puede deshacer.»). Las que genera una tarea programada llevan un reloj.

**Barra de estado de la IA**
- Indica el estado del motor: «Descargando el motor…», «Cargando la IA en memoria…», «IA lista», «IA parada», «La IA no ha podido arrancar», y el progreso de las descargas.

**Encima del redactor**
- Preguntas / Agente (por conversación):
  - Preguntas: la IA responde; usa el PC, tus documentos o internet solo si la pregunta lo necesita (pidiendo permiso).
  - Agente: la IA resuelve la tarea con herramientas (órdenes, ficheros, internet…), paso a paso, pidiendo permiso.
- Selector de IA: «La IA que responde en la aplicación (las instaladas; más en Ajustes)». Cambia de modelo sin ir a Ajustes.
- Pensar: deja que la IA razone antes de responder. Más lento; a veces mejor en preguntas difíciles. El razonamiento sale plegado encima de la respuesta.

**Redactor**
- «Pregunta algo… (Enter envía, Mayús+Enter salto de línea)».
- Adjuntar ficheros o imágenes (clip). También puedes arrastrar ficheros al redactor o pegar con Ctrl+V una imagen o ficheros copiados. Los adjuntos aparecen encima con «Quitar». Límite: 20 MB por fichero; se admiten ficheros de texto, código, Word (.docx) e imágenes.
- Parar: detiene la respuesta en curso.
- Enviar. Puedes seguir enviando preguntas mientras responde: se contestan a continuación.

**Conversación**
- Las respuestas llegan mientras se escriben, con formato (títulos, listas, negrita y bloques de código).
- Todo el texto se puede seleccionar y copiar.
- En cada pregunta tuya: Copiar, «Editar (la copia al redactor)» y «Volver a enviar».
- En cada bloque de código: Copiar y «Guardar como fichero».
- Imágenes generadas: Abrir y «Guardar como…».
- Adjuntos y documentos generados: botón Abrir.
- Cuando la IA usa internet, cada búsqueda y página consultada se ve en la conversación.

**Ventana de permiso** (cuando la IA quiere usar un recurso)
- Título «¿Permitir esto?» con lo que quiere hacer («La IA quiere ejecutar esta orden en tu PC:», «La IA quiere leer esto:», «La IA quiere escribir este fichero:», «La IA quiere usar internet:», «La IA quiere usar el portapapeles:», «La IA quiere abrir esto:») y su motivo.
- «No volver a preguntar por esto en esta conversación».
- «Permitir siempre … (se cambia en Ajustes › Permisos)».
- Permitir (Ctrl+Enter) o Cancelar. El resultado se ve en la conversación.

**Bandeja del sistema**
- Si está activado en Ajustes, al minimizar se queda en el área de notificación: clic en el icono para volver; botón derecho, Abrir o Salir.

### Ajustes

Ajustes es una sola página con estas secciones, de arriba abajo:

**La IA**
- Instalada: la IA en uso, su licencia y su fichero.
- Análisis del PC: «Este PC: procesador (hilos), RAM, gráfica con su memoria de vídeo» (o «sin gráfica dedicada: la IA va en el procesador»). «★ = óptima para este PC: rápida y fiable. Solo se muestran las IA que caben en memoria.»
- Instaladas en este PC: cada IA descargada con «En uso», «Usar esta IA» y «Borrar esta IA» (se puede volver a descargar).
- Catálogo: Qwen3.8 27B («La más capaz. Necesita un PC con mucha memoria.»), Gemma 4 12B y Ministral 3 8B («Buenas respuestas con una descarga razonable.»), Qwen3.5 4B y Phi-4 Mini («Rápida, muchos idiomas, cabe en un PC de 8 GB.»), Qwen3.5 2B y Gemma 3 1B («Fichero pequeño, respuestas cortas.»). Cada una indica su tamaño de descarga, su licencia y cómo iría en tu PC: «★ Óptima aquí», «Funciona, pero más lenta» o «Lenta en este PC». Botón «Instalar» (o papelera si ya está instalada).
- Buscar más IA en Hugging Face: por nombre, familia (llama, mistral, gemma, qwen, deepseek…) o palabra clave (imágenes, vídeo, voz…). Pesa cada resultado y lo valora para tu PC. Casilla «Solo IA que esta aplicación puede ejecutar (modelos de texto GGUF)»; sin marcar se ven modelos de todo tipo con enlace «Abrir en huggingface.co», pero solo se instalan los de texto. Los que exigen aceptar una licencia lo avisan.
- Cancelar la descarga (durante una descarga).
- Importar un fichero GGUF…: usa un modelo que ya tengas, sin copiarlo.
- Carpeta de los modelos: «Elegir otra carpeta (los modelos se mueven allí)». Útil para llevarlos a otro disco; la IA se para mientras se mueven.

**Instrucciones fijas**
- Texto que va con cada conversación: tono, idioma, lo que la IA nunca debe hacer (por ejemplo: «responde en español, breve, y di cuándo no estás seguro»).
- «Permitir que la IA acceda a internet» (activada por defecto): puede buscar en la web y leer páginas cuando una pregunta necesita información actual. Sin marcar, trabaja sin conexión.
- Tamaño de la letra del chat: de 12 a 20 px. Solo cambia el texto de la conversación.

**Editores de código (VS Code)**
- «Activar la puerta para editores»: abre una puerta local, solo en este equipo, protegida con un token, para que un editor de código use esta IA.
- Dirección (con botón para copiarla), Token (con copiar y «Nuevo token»), Puerto (por defecto 41417) y estado («Escuchando.» / «Parada.»).
- Cómo usarla: instala la extensión «sOC Lucia Code» (.vsix de la página de versiones) y pega el token en sus ajustes; o configura otro cliente compatible con OpenAI (Continue, Cline…) con esa dirección y ese token.

**Modo agente**
- Carpeta de trabajo: donde trabaja la IA en modo agente (por defecto, Documentos). Botón «Elegir carpeta».
- Permisos: para cada recurso eliges «Preguntar» (enseña cada acción antes de hacerla), «Siempre» (no pregunta) o «Nunca» (la IA ni siquiera ve ese recurso):
  - Órdenes: ejecutar líneas de PowerShell (programas, git, python…).
  - Leer ficheros: leer ficheros, listar y buscar en carpetas.
  - Escribir ficheros: crear o sobrescribir ficheros.
  - Internet: descargar páginas o ficheros de la web (solo lectura).
  - Portapapeles: leer o sustituir el texto del portapapeles.
  - Abrir cosas: abrir un fichero, carpeta, programa o dirección web con su programa habitual.
- Abrir el registro de acciones: todo lo que ha hecho la IA queda anotado.

**Imágenes**
- Pide un dibujo en el chat («dibuja un faro al atardecer») y se genera en tu PC. Mientras se genera, la IA del chat se pausa.
- Estado: instalado (con tamaño en disco) o sin instalar (unos 1,7 GB de modelo; también se descarga la primera vez que pidas un dibujo).
- Instalar ahora, Abrir la carpeta de imágenes y Quitar.

**Tus documentos**
- Carpeta (por defecto Documentos\Lucia) con ficheros de texto, Markdown, CSV, JSON, código, HTML o Word que la IA tiene en cuenta; con cada pregunta recibe los pasajes que encajan y puede leerlos enteros. Ahí guarda también los documentos que le pidas.
- Abrir la carpeta, Elegir otra carpeta y el número de documentos en cuenta.

**Tareas programadas**
- Se crean pidiéndoselo en el chat: «cada mañana a las 9 resúmeme la carpeta de documentos», «recuérdame el viernes a las 18:00 enviar el informe», «cada 30 minutos…». Se ejecutan solas como conversación nueva mientras la aplicación está abierta (también en la bandeja), con un aviso al terminar.
- Lista de tareas con próxima y última ejecución, interruptor «Activa / parada» y «Borrar la tarea».
- Las ejecuciones desatendidas solo usan los recursos puestos en «Siempre» en Permisos.

**Lo que la IA sabe de ti**
- «Dejar que la IA recuerde cosas sobre mí»: guarda frases cortas cuando le cuentas algo duradero (nombre, trabajo, preferencias…).
- Lista de lo recordado, con «Olvidar esto» en cada frase y «Olvidarlo todo».

**Windows**
- «Quedarse en el área de notificación al minimizar».
- «Arrancar con Windows»: arranca escondida en el área de notificación al iniciar sesión.

**Idioma**
- Español o English; se aplica de inmediato.

**Diagnóstico**
- Motor en uso y aceleración (gráfica o procesador).
- Abrir el registro del motor y Abrir la carpeta de datos.

### Extensión para Visual Studio Code (opcional)

1. En la aplicación, Ajustes › Editores de código: activa la puerta y copia el token.
2. En VS Code: Extensiones › … › Instalar desde VSIX, y elige el fichero `soc-lucia-code-….vsix`.
3. En los ajustes de la extensión pega la dirección y el token.
4. El chat aparece en la barra lateral izquierda con el icono de Lucia (o con Ctrl+Alt+L). Tiene conversaciones guardadas, Preguntas/Agente, Pensar, adjuntos (el fichero abierto, uno del proyecto o del disco, la selección o imágenes pegadas), parar, copiar/editar/reenviar y, en cada bloque de código, copiar, insertar y guardar.
5. Sobre el código seleccionado (menú contextual): preguntar, explicar, mejorar y escribir tests. En modo agente puede leer y buscar en el proyecto; escribir un fichero o ejecutar una orden siempre pide confirmación.
6. Ajustes de la extensión: dirección, token, longitud máxima de respuesta, creatividad, instrucciones fijas y si la IA puede mirar y cambiar el proyecto por sí misma.

## Preguntas frecuentes

**La primera respuesta tarda mucho.**
Es normal: al abrir la aplicación la IA se carga en memoria («Cargando la IA en memoria…»). Las siguientes respuestas son más rápidas. Si tu PC va justo, elige en Ajustes una IA marcada con ★.

**Dice «La IA no ha podido arrancar» o «El motor ha terminado con el código…».**
Abre Ajustes › Diagnóstico › Abrir el registro del motor para ver la causa. Suele deberse a que la IA elegida no cabe en memoria: prueba con una más pequeña o con la recomendada.

**Al arrancar con Windows sale una ventana negra y parece colgada.**
La entrada de «Arrancar con Windows» apuntaba a una copia antigua del programa. Desde la versión 2026.9.22.0, la aplicación corrige esa entrada sola al abrirse. Si tienes un acceso directo antiguo hecho a mano, vuelve a crearlo.

**Después de dibujar una imagen, la siguiente pregunta falla con «No se ha podido responder».**
Corregido en la versión 2026.9.22.1: al generar una imagen se pausa la IA del chat y ahora se vuelve a poner en marcha sola en la siguiente pregunta. Actualiza a la última versión.

**Adjunto una imagen y la IA no la ve.**
Solo algunas IA entienden imágenes (Gemma 4 12B, Qwen3.5 4B o 2B, Ministral 3 8B, Qwen3.8 27B). Instala una de ellas; la primera vez que adjuntes una imagen te ofrecerá descargar su parte de visión (unos cientos de MB, una sola vez).

**Dibujar una imagen tarda mucho.**
La primera vez descarga el motor y el modelo de imágenes (unos 1,7 GB). Después, cada imagen tarda alrededor de un minuto con tarjeta gráfica; si la gráfica no puede, se genera en el procesador y tarda unos minutos.

**VS Code dice que falta el token o no es correcto.**
Copia el token de sOC Lucia › Ajustes › Editores de código y pégalo en los ajustes de la extensión. Si pulsaste «Nuevo token», el anterior deja de valer. La puerta debe estar activada y la aplicación abierta.

**No quiero que la IA use internet ni toque mis ficheros.**
Desmarca «Permitir que la IA acceda a internet» en Instrucciones fijas y pon en «Nunca» los recursos que quieras en Modo agente › Permisos. Con «Nunca» la IA ni siquiera sabe que existe ese recurso.

## Privacidad

Las conversaciones, tus documentos, la memoria y la propia IA se quedan en tu PC: la IA se ejecuta y responde aquí. La red solo se usa para descargar el motor y la IA que elijas, cuando lo pides, y para las búsquedas web si las permites. Sin cuenta, sin anuncios, sin rastreadores ni analítica; la puerta opcional para editores de código solo escucha en tu propio equipo y exige un token.
