# sOC Uninstaller
- slug: uninstaller
- plataformas: Android / Windows
- lema: Marca varias aplicaciones y desinstálalas de una vez, en el móvil y en el PC.
- github: https://github.com/donki/Uninstaller
- tiendas:
  - Google Play (producción, con la versión 2026.08.01 y el nombre «Uninstaller»; la 2026.09.19.07 está en prueba cerrada): https://play.google.com/store/apps/details?id=com.socratic.uninstaller (ficha pública accesible el 2026-09-25; D:\sOCProjects\08-PENDIENTE-Uninstaller.md y D:\sOCProjects\01-TAREAS-Uninstaller.md: la alpha 2026091907 se publicó el 2026-09-24 y espera la revisión de Google antes de pasar a producción)
  - Microsoft Store (no publicada): sin ID todavía. El nombre «sOC Uninstaller» está por reservar en Partner Center y la ficha está preparada pero sin enviar (D:\sOCProjects\08-PENDIENTE-Uninstaller.md, puntos 6 y 7; Mobile/MicrosoftStore/Uninstaller/ficha-es-ES.md)
  - Edge Add-ons / Chrome / Firefox: no aplica
- descarga_alternativa: https://github.com/donki/Uninstaller/releases (última: v2026.09.22.02, con sOCUninstaller.exe, el zip y el MSIX de Windows; el último APK publicado ahí es el de v2026.09.19.07)

## Descripción

sOC Uninstaller es un desinstalador por lotes. En lugar de ir quitando aplicaciones una por una desde los ajustes, ves todas las que tienes instaladas en una lista, marcas las que sobran y las desinstalas seguidas. Funciona en Android y en Windows con la misma idea y el mismo aspecto.

En Android enseña cada aplicación con su icono, su fecha de instalación, su última actualización y lo que ocupa, y puedes ordenarlas o buscarlas para encontrar rápido lo que ya no usas. Cada desinstalación la confirmas tú en el diálogo del sistema: la aplicación nunca borra nada por su cuenta.

En Windows junta en una sola lista los programas clásicos y las aplicaciones de la Microsoft Store, y puede desinstalarlos sin preguntas donde el instalador lo permite. Además trae una utilidad de **Espacio en disco** para ver qué carpetas y archivos se comen el disco, encontrar duplicados y mandar a la papelera lo que sobra.

## Funciones principales

- Lista de aplicaciones instaladas con icono, nombre, fecha de instalación, última actualización y tamaño.
- Selección múltiple con casillas y «Desinstalar seleccionadas» en secuencia, con progreso («2 de 5: nombre»).
- Buscador por nombre o paquete (o editor en Windows).
- Ordenación por fecha de instalación, nombre, última actualización o tamaño.
- Mostrar u ocultar las aplicaciones del sistema.
- Windows: programas clásicos y aplicaciones de la Store en una sola lista, con modo desatendido.
- Windows: Espacio en disco con árbol de carpetas, mapa de rectángulos, archivos más grandes, reparto por tipo y antigüedad, y duplicados.
- Windows: icono en el área de notificación y arranque con Windows opcionales.
- Modo claro y oscuro; en español e inglés.

## Guía de uso (soporte)

### Primera puesta en marcha en Android

1. Instala la aplicación desde Google Play y ábrela.
2. No te pedirá ningún permiso en pantalla. Para funcionar necesita dos permisos que se conceden al instalar: ver la lista de aplicaciones instaladas (para enseñártela) y pedir desinstalaciones (para abrir el diálogo de desinstalar del sistema). También se conecta a internet solo para comprobar si hay versión nueva.
3. Verás la lista de tus aplicaciones. Por defecto solo salen las que has instalado tú; las del sistema quedan ocultas.

### Primera puesta en marcha en Windows

1. Descarga sOCUninstaller.exe (o el zip) desde las releases de GitHub. Es un único archivo: ábrelo y listo. La primera vez tarda un poco más porque se prepara en tu carpeta de usuario.
2. Si quieres tenerla a mano, ancla la ventana a la barra de tareas: el anclaje sigue valiendo tras actualizar.
3. Algunos desinstaladores pedirán permiso de administrador, como siempre en Windows.

### Flujo normal

1. En «Aplicaciones instaladas», busca u ordena para encontrar lo que quieres quitar.
2. Marca la casilla de cada aplicación (tocar la fila también la marca).
3. Pulsa **Desinstalar seleccionadas (N)** y confirma en «Desinstalar aplicaciones» con **Continuar**.
4. En Android, el sistema te pedirá confirmar cada una. En Windows, si alguna admite desinstalación silenciosa, se te preguntará antes «¿Desatendido?».
5. Al acabar verás «N de M aplicaciones desinstaladas» y la lista se refresca con lo que queda.

### Menú lateral

- **Inicio**: la lista de aplicaciones.
- **Espacio en disco**: solo en Windows.
- **Ajustes**: idioma y, en Windows, opciones de la bandeja y del arranque.
- **Acerca de**: información de la aplicación.

### Aplicaciones instaladas (Inicio)

Cabecera:
- **Contador**: «N aplicaciones instaladas · N seleccionadas · por criterio». Tocarlo abre también el menú de ordenación.
- **Ordenar por**: Fecha de instalación, Nombre (A–Z), Última actualización y Tamaño. El criterio activo sale marcado.
- **Actualizar**: vuelve a leer la lista. También puedes deslizar hacia abajo para actualizar.
- **Buscar**: muestra la caja «Buscar por nombre o paquete». El contador refleja lo que queda a la vista.
- **Seleccionar todo**: marca todo lo que se ve (si hay búsqueda, solo lo filtrado).
- **Quitar selección**: desmarca todo.
- **Mostrar apps del sistema**: enseña u oculta las aplicaciones del sistema (en Windows, los componentes de Windows). La elección se recuerda.
- **Espacio en disco** (solo Windows): abre la utilidad de espacio en disco.

Lista:
- Cada fila lleva el icono, el nombre, el paquete (en Windows, el editor) y el detalle «Inst. fecha · Act. fecha · tamaño», y la casilla de selección a la derecha.
- Lista vacía: «No hay aplicaciones para mostrar. Desliza para actualizar o activa «Mostrar apps del sistema».»

Botón inferior:
- **Desinstalar seleccionadas (N)**: lanza la desinstalación de todo lo marcado. Sin nada marcado avisa «Selecciona al menos una aplicación.».

Diálogos de desinstalación:
- **Desinstalar aplicaciones**: en Android, «Vas a desinstalar N aplicaciones. Android te pedirá confirmación para cada una.»; en Windows, explica que cada programa abre su propio desinstalador y que las apps de la Store se quitan directamente. Botones **Continuar** y **Cancelar**.
- **¿Desatendido?** (solo Windows): indica cuántos se pueden quitar sin preguntas (Windows Installer, Inno Setup, NSIS y apps de la Store). **Desatendido** los quita en silencio; **Con asistente** abre el asistente de cada uno. Los que no lo admiten abren su asistente en cualquier caso.
- **Progreso**: «Desinstalando…», barra y «n de N: nombre».

### Espacio en disco (solo Windows)

Barra de escaneo:
- **Selector de unidad**: elige una unidad (local o de red).
- **Unidad, carpeta o ruta de red (\\servidor\recurso)**: escribe una ruta y pulsa Intro.
- **Escanear** (reproducir): empieza a medir. Verás «Escaneando… carpetas, ficheros, tamaño» y el árbol va creciendo mientras tanto.
- **Parar**: detiene el escaneo y deja a la vista lo recorrido.

Vistas:
- **Árbol de carpetas**: cada carpeta con su tamaño, el porcentaje de la carpeta superior, número de ficheros y carpetas y última modificación. Se despliega por filas. Las carpetas que no se pudieron leer se marcan.
- **Mapa de rectángulos (un toque elige, dos entran en la carpeta)**: cada carpeta es un rectángulo proporcional a lo que ocupa.
- **Ficheros más grandes**: los archivos que más ocupan, con su carpeta.
- **Por tipo de fichero**: cuánto ocupa cada extensión.
- **Por antigüedad**: Modificados el último mes, De 1 a 6 meses, De 6 meses a un año, De 1 a 2 años, Más de 2 años.
- **Ficheros duplicados**: grupos de archivos con el mismo contenido de verdad, con lo que recuperarías dejando una sola copia.

Acciones (sobre la fila elegida o sobre todo lo marcado con las casillas):
- **Subir un nivel**: en el mapa, vuelve a la carpeta superior.
- **Ver en el Explorador**: abre la carpeta o señala el archivo en el Explorador de Windows.
- **Copiar ruta**: copia la ruta (o las rutas, una por línea).
- **Enviar a la papelera**: pide confirmación y lo manda a la papelera, con deshacer desde Windows. Con varios marcados van todos en una sola operación. Lo que ya está dentro de la papelera se **borra definitivamente**, y se avisa de que no se podrá recuperar.
- **Exportar a CSV**: guarda la vista actual en un archivo CSV en tu carpeta Documentos.

Avisos de seguridad:
- **Carpeta del sistema**: antes de borrar algo de Windows, de Archivos de programa, de ProgramData, de un perfil de usuario o de la raíz de la unidad, explica el riesgo. El botón por defecto es Cancelar; para seguir hay que pulsar **Seguir de todos modos**.
- **Sin permisos**: si algo no se puede borrar, ofrece **Cambiar permisos y reintentar** (Windows pedirá permiso de administrador).

### Ajustes

- **Idioma**: botones **Español** y **English**; «Selecciona tu idioma preferido». El cambio se aplica al momento.
- **Windows** (solo en Windows):
  - **Quedarse en el área de notificación al minimizar** (interruptor): al minimizar, la ventana se esconde en la bandeja. Clic en el icono para volver; botón derecho para **Abrir** o **Salir**.
  - **Arrancar con Windows** (interruptor): arranca escondida en el área de notificación al iniciar sesión.

### Acerca de

- Nombre, «Versión X», «Desinstala varias apps a la vez» y Socratic.
- **Contacto**: botón con el correo; «Toca para enviar un correo electrónico».
- **Privacidad**, **Licencia** (MIT) y **Aviso Legal** con «Uso bajo su propio riesgo».
- **Volver**.

### Aviso de actualización

Si hay una versión más nueva: «Actualización disponible: Hay una versión más reciente (X). Tienes la Y. ¿Quieres actualizar?», con **Actualizar** y **Ahora no**.

## Preguntas frecuentes

**En Android tengo que confirmar cada aplicación, ¿no se pueden quitar todas de golpe?**
No. Android no permite a ninguna aplicación desinstalar otras en silencio: por seguridad, cada desinstalación la confirma el usuario. sOC Uninstaller te ahorra ir buscándolas una por una.

**No me sale la aplicación que busco.**
Puede ser una aplicación del sistema. Pulsa «Mostrar apps del sistema» o usa el buscador.

**En Google Play no veo el buscador, los ajustes ni el progreso.**
La versión de producción de Google Play es la de agosto de 2026. La nueva está en prueba cerrada y pasará a producción cuando Google la apruebe. Mientras tanto, el APK nuevo está en las releases de GitHub.

**En Windows, un programa me sigue haciendo preguntas aunque elegí «Desatendido».**
Solo los instaladores que lo admiten (Windows Installer, Inno Setup, NSIS y apps de la Store) se quitan en silencio; el resto abre su asistente. Windows puede pedir permiso de administrador igualmente.

**Espacio en disco no me deja borrar una carpeta.**
Si es por permisos, acepta «Cambiar permisos y reintentar» y concede el permiso de administrador. Si sale el aviso «Carpeta del sistema», piénsalo dos veces: borrar eso puede dejar Windows o tus programas inservibles. Para quitar un programa, desinstálalo desde Inicio.

**He mandado algo a la papelera por error.**
Recupéralo desde la Papelera de reciclaje de Windows o con Ctrl+Z en el Explorador. Lo que ya estaba dentro de la papelera y borraste desde la aplicación no se puede recuperar.

**No encuentro Espacio en disco en el móvil.**
Solo existe en Windows. En Android haría falta el permiso de acceso a todo el almacenamiento, que la aplicación no pide.

**¿Está en la Microsoft Store?**
Todavía no. Descarga la versión de Windows desde las releases de GitHub.

## Privacidad

sOC Uninstaller lee la lista de aplicaciones instaladas solo para enseñártela, y en Windows recorre las carpetas que tú le pidas para medir el espacio; nada de eso sale del dispositivo. No hay cuentas, anuncios ni rastreadores, y la única conexión a internet es para comprobar si hay una versión nueva.
