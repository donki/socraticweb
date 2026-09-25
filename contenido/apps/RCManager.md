# sOC Remote Connections Manager
- slug: rcmanager
- plataformas: Windows 10 (versión 2004) o posterior y Windows 11, 64 bits
- lema: Tus escritorios remotos, terminales SSH y servidores de ficheros, en pestañas y en una sola ventana.
- github: https://github.com/donki/RCManager
- tiendas:
  - Microsoft Store (en revisión, sin publicar): enviada el 2026-09-19 con el nombre reservado «sOC Remote Connections Manager»; aún no hay identificador de producto ni enlace (fuentes: README.md del repositorio, «enviada el 2026-09-19 (enlace en cuanto Partner Center la publique)»; nota del proyecto del 2026-09-19, «falta el enlace»). No se ha encontrado el ID: no se puede dar la URL https://apps.microsoft.com/detail/…
  - Google Play: no aplica (solo Windows).
- descarga_alternativa: https://github.com/donki/RCManager/releases (última: v2026.9.23.1; ejecutable autocontenido y paquete MSIX)

## Descripción

sOC Remote Connections Manager reúne en una sola ventana todas las conexiones que usas para trabajar con servidores: escritorio remoto de Windows (RDP), terminal SSH y transferencia de ficheros por SFTP, SCP, FTP y FTPS. A la izquierda tienes un árbol con tus conexiones ordenadas en carpetas y un buscador; a la derecha, cada sesión se abre en su propia pestaña, así que puedes tener varios servidores abiertos a la vez y saltar de uno a otro.

El escritorio remoto usa el mismo cliente que trae Windows, con todas sus opciones de siempre (pantalla, recursos locales, experiencia, certificado, puerta de enlace…), y el escritorio se ajusta solo al tamaño de la pestaña. Para los ficheros tienes un explorador de dos paneles, tu PC a un lado y el servidor al otro, con el que subes y bajas carpetas enteras arrastrando, e incluso puedes editar ficheros de texto del servidor sin descargarlos.

Tus conexiones se guardan en tu PC con las contraseñas cifradas para tu usuario de Windows, o, si lo prefieres, en tu propio Google Drive u OneDrive cifradas con una frase que solo tú conoces, para tenerlas iguales en todos tus equipos. Puedes importar lo que ya tengas en Remote Desktop Manager o en ficheros .rdp. Es software libre, sin cuenta, sin anuncios y sin rastreadores.

## Funciones principales

- Conexiones RDP, SSH, SFTP/SCP y FTP/FTPS, cada sesión en su pestaña.
- Árbol de conexiones con carpetas anidadas, buscador, arrastrar y soltar, y que se conserva tal como lo dejaste.
- Escritorio remoto con todas las opciones del cliente de Windows, organizadas en las mismas pestañas que el original, resolución que sigue a la pestaña, pantalla completa en el monitor que elijas y uso de todos los monitores.
- Unidades de tu PC dentro del escritorio remoto y portapapeles compartido con texto, imágenes y ficheros.
- Terminal SSH con colores, historial, copiar y pegar, y entrada con contraseña o clave privada.
- Explorador de ficheros de dos paneles con cola de transferencias, progreso y cancelar, y cambio de permisos y propietario en servidores Linux.
- Editor de texto integrado que guarda directamente en el servidor.
- Zoom por pestaña (letra del terminal y de los paneles, escala del escritorio remoto) que se recuerda por conexión.
- Conexiones en este PC o sincronizadas cifradas en Google Drive u OneDrive.
- Importación desde Remote Desktop Manager (.rdm) y desde ficheros .rdp.

## Guía de uso (soporte)

### Instalación

1. Descarga la última versión desde la página de versiones de GitHub (https://github.com/donki/RCManager/releases). Hay dos formas:
   - El ejecutable `sOCRCManager.exe`: no necesita instalación, se abre con doble clic.
   - El paquete `.msix`: se instala como cualquier aplicación de Windows.
2. Cuando esté publicada en la Microsoft Store, también podrás instalarla desde allí.

Requisitos: Windows 10 (versión 2004) o posterior, o Windows 11. Para el escritorio remoto se usa el cliente que ya trae Windows; no hay que instalar nada más.

### Primera puesta en marcha

1. Abre la aplicación. El árbol está vacío y te indica: «Todavía no hay conexiones. Añade una con + y aparecerá aquí.»
2. Si ya tienes conexiones en Remote Desktop Manager o en ficheros .rdp, ve a Ajustes (icono de engranaje) › Importar conexiones. Si no, pulsa «Conexión nueva» (+).
3. Rellena al menos el Nombre y el Servidor, elige el Tipo y pulsa Guardar.
4. Opcional: en Ajustes elige si quieres guardar las conexiones solo en este PC o en Google Drive / OneDrive.

No hace falta crear ninguna cuenta. Solo si eliges guardar en la nube entrarás con tu cuenta de Google o de Microsoft.

### Flujo normal

- Para conectar: doble clic sobre la conexión, o selecciónala y pulsa Conectar (o Intro), o arrástrala al área de pestañas.
- Si la conexión no tiene contraseña guardada, se te pide al conectar, con la casilla «Recordarla en este PC (cifrada)».
- Cada sesión se abre en una pestaña. Pasa de una a otra con un clic, con Ctrl+Tab / Ctrl+Mayús+Tab o con el botón de sesiones abiertas de la barra inferior.
- Para editar una conexión: selecciónala y pulsa Editar, o Ctrl + doble clic.
- Para cerrar una sesión: botón «Desconectar esta pestaña» en la propia pestaña.

### Ventana principal

**Barra superior del árbol (de izquierda a derecha)**
- Conectar: abre la conexión seleccionada.
- Conexión nueva (+): abre el editor de conexión vacío.
- Carpeta nueva: pide el «Nombre de la carpeta» y la crea.
- Editar: abre el editor de la conexión seleccionada (o renombra la carpeta seleccionada).
- Duplicar: crea una copia de la conexión seleccionada.
- Borrar: pide confirmación («¿Borrar …?»). Si es una carpeta, borra también las conexiones que contiene («¿Borrar la carpeta … y las N conexiones que tiene dentro?»).
- Buscar…: filtra el árbol por nombre, servidor, usuario, carpeta o notas; solo se ven las carpetas que tienen alguna conexión que encaja.

**Árbol de conexiones**
- Doble clic: conectar. Ctrl + doble clic: editar. Intro: conectar. Supr: borrar.
- Arrastrar una conexión o una carpeta sobre otra carpeta la mueve allí (sobre una conexión, a la carpeta de esa conexión). La carpeta de destino se resalta al pasar por encima.
- Arrastrar una conexión al área de pestañas la abre.
- Al cerrar, se recuerdan las carpetas abiertas, la conexión seleccionada y el ancho del panel.

**Botones inferiores del árbol**
- Ajustes (engranaje): «Ajustes: dónde se guardan las conexiones», importación y comportamiento de la ventana.
- Abrir la carpeta del fichero de conexiones: abre en el Explorador la carpeta donde se guardan las conexiones.
- Español / English: cambia el idioma al momento.
- Acerca de: contacto con el autor, idioma, privacidad, licencia y aviso legal.

**Área de pestañas**
- Sin sesiones abiertas muestra: «Haz doble clic en una conexión, o selecciónala y pulsa Conectar. Cada sesión se abre en su pestaña.»
- Cada pestaña lleva sus botones:
  - Más pequeño / Más grande (− y +): zoom de la pestaña. En SSH cambia la letra del terminal; en ficheros, la de los paneles; en RDP, la escala del escritorio remoto (del 100 al 200 %). Se recuerda para la próxima vez que abras esa conexión.
  - Pantalla completa (F11; Ctrl+Esc para volver).
  - Desconectar esta pestaña.

**Barra de estado**
- Sesiones abiertas: menú con todas las pestañas para cambiar a cualquiera, útil cuando el escritorio remoto se queda con el teclado (atajos Ctrl+Tab / Ctrl+Mayús+Tab).
- Mensajes de estado: «Conectando con…», «Conectado con…», resultado de la sincronización con la nube, etc.

**Pantalla completa**
- RDP: usa la pantalla completa del propio cliente de Windows, con su barra de conexión arriba (se esconde sola; sus botones de minimizar y cerrar funcionan: cerrar desconecta y cierra la pestaña).
- SSH y ficheros: la ventana ocupa toda la pantalla y arriba aparece una barra que se esconde sola y vuelve al llevar el ratón al borde superior, con el nombre de la sesión, «Salir de pantalla completa (Ctrl+Esc)», sesiones abiertas y «Desconectar esta pestaña».
- La pantalla donde se abre se elige en el editor de conexión, opción «Pantalla completa en».

**Área de notificación**
- Al minimizar, la ventana se esconde y deja su icono junto al reloj (si no lo ves, está en los iconos ocultos de Windows 11). Un clic la trae de vuelta; con el botón derecho, «Abrir» y «Salir». Las sesiones abiertas siguen vivas. Se puede desactivar en Ajustes › Ventana.

### Editor de conexión

Se abre con «Conexión nueva» o «Editar». Las pestañas que aparecen dependen del tipo: RDP muestra General, Pantalla, Recursos locales, Experiencia y Avanzado; SFTP / SCP y FTP / FTPS muestran General y Transferencias; SSH solo General. Abajo, Cancelar y Guardar («El nombre y el servidor son obligatorios.»).

#### Pestaña General (todos los tipos)
- Nombre: cómo aparece en el árbol.
- Tipo: RDP, SSH, SFTP / SCP o FTP / FTPS. Al cambiarlo se propone el puerto habitual (3389 para RDP, 22 para SSH y SFTP, 21 para FTP y 990 para FTPS implícito).
- Carpeta: la carpeta del árbol donde va la conexión (se puede elegir o escribir una nueva).
- Servidor: nombre o dirección IP.
- Puerto.
- Usuario.
- Dominio (solo RDP).
- Contraseña, con botón de ojo para verla u ocultarla. «Déjala vacía para que se pida al conectar.»
- Clave privada (fichero) (SSH y SFTP), con botón «Elegir fichero»: «Fichero OpenSSH o PEM. Si se pone, la contraseña es la de la clave.»
- Cifrado (solo FTP / FTPS): «Ninguno (FTP en claro)», «FTPS explícito (AUTH TLS, puerto 21)» o «FTPS implícito (puerto 990)».
- «Transferir por SCP en vez de SFTP (la navegación va siempre por SFTP)» (solo SFTP / SCP).
- Carpeta remota al abrir y Carpeta local al abrir (SFTP y FTP): «Vacías: la carpeta que dé el servidor y tu perfil de usuario.» Si no pones carpeta remota, se empieza en la raíz del servidor (/).
- Pantalla completa en: «La pantalla donde esté la ventana» o una pantalla concreta («Pantalla N (ancho×alto)», marcando la principal).
- Notas: texto libre (también lo encuentra el buscador).

#### Pestaña Pantalla (RDP)
- Tamaño del escritorio remoto:
  - «Ajustar a la pestaña (sigue a la ventana)» (por defecto): pide al servidor la resolución que cabe en la pestaña, nítida y sin barras, y la cambia al redimensionar la ventana.
  - Tamaños fijos: 1024 × 768, 1280 × 800, 1366 × 768, 1600 × 900, 1920 × 1080, 1920 × 1200, 2560 × 1440.
  - «A medida…»: habilita Ancho y Alto (mínimo 200 píxeles cada uno). Un tamaño fijo se escala a la pestaña.
- «Usar todos los monitores en pantalla completa»: en pantalla completa el escritorio remoto tiene un monitor por cada pantalla de tu PC (la sesión se reconecta a pantalla completa para tenerlos); en la pestaña siempre es una sola pantalla. Desactivada por defecto.
- Colores: «Color de alta densidad (15 bits)», «Color de alta densidad (16 bits)», «Color verdadero (24 bits)» o «Máxima calidad (32 bits)» (por defecto).
- «Mostrar la barra de conexión en pantalla completa» (activada por defecto).

#### Pestaña Recursos locales (RDP)
- Audio remoto: «Reproducir en este PC» (por defecto), «Reproducir en el equipo remoto» o «No reproducir».
- «Grabar desde este PC (micrófono)»: usa tu micrófono en la sesión remota (desactivada por defecto).
- Combinaciones de teclas de Windows (Alt+Tab, Win…): «En este PC», «En el equipo remoto» o «En el equipo remoto solo a pantalla completa» (por defecto).
- Dispositivos y recursos locales que se usan en la sesión remota:
  - Impresoras (activada por defecto).
  - Portapapeles (texto, imágenes y ficheros) (activada por defecto).
  - Unidades de este PC (copiar y mover ficheros con el Explorador) (activada por defecto): tus discos aparecen en el equipo remoto como «C en tu PC» en Este equipo, incluidos los USB que enchufes durante la sesión.
  - Tarjetas inteligentes y Windows Hello (activada por defecto).
  - Puertos serie (desactivada por defecto).
  - Otros dispositivos Plug and Play (cámaras, reproductores…) (desactivada por defecto).

#### Pestaña Experiencia (RDP)
- Efectos visuales (desactívalos en conexiones lentas), todos activados por defecto:
  - Fondo de escritorio.
  - Suavizado de fuentes.
  - Composición del escritorio.
  - Mostrar el contenido de la ventana al arrastrarla.
  - Animación de menús y ventanas.
  - Estilos visuales.
  - Caché persistente de mapas de bits.
- Conexión: «Volver a conectar si se corta la conexión» (activada por defecto).

#### Pestaña Avanzado (RDP)
- Si falla la autenticación del servidor (certificado): «Conectar sin avisar», «Avisar» (por defecto; avisa y te deja seguir, como el cliente de Windows) o «No conectar».
- «Sesión de administración (consola, /admin)».
- Puerta de enlace de Escritorio remoto: «No usar puerta de enlace» (por defecto), «Usar siempre la puerta de enlace» o «Usar la puerta de enlace salvo para direcciones locales».
  - Servidor de puerta de enlace.
  - «Usar el mismo usuario y contraseña que el escritorio remoto» (activada por defecto). Si la quitas, aparecen Usuario, Dominio y Contraseña propios de la puerta de enlace.

#### Pestaña Transferencias (SFTP / SCP y FTP / FTPS)
- Ficheros a la vez: de 1 a 8 (por defecto 2). «Cada transferencia simultánea abre su propia conexión con el servidor. 1 es lo más seguro; 2–4 acelera muchos ficheros pequeños.»
- Reintentos si falla: de 0 a 5 (por defecto 1).
- Si el fichero ya existe en el destino: «Avisar y confirmar antes de sobrescribir» (por defecto), «Sobrescribir» o «Saltar».
- «Conservar la fecha de modificación del original» (activada por defecto).
- «Enseñar los ficheros ocultos (con punto delante) al abrir».
- Keep-alive (segundos, 0 = no): por defecto 30.
- Tiempo de espera (segundos): por defecto 20.
- Solo FTP:
  - Conexiones de datos: «Pasivo (lo normal detrás de un router)» (por defecto) o «Activo».
  - Codificación de los nombres de fichero: UTF-8 (por defecto) o Latin-1 (ISO-8859-1).

### Sesión de escritorio remoto (RDP)

- El escritorio aparece dentro de la pestaña y se ajusta a su tamaño si elegiste «Ajustar a la pestaña».
- El zoom (− y +) cambia la escala del escritorio remoto entre el 100 y el 200 %, y se recupera al volver a abrir la conexión.
- Para copiar ficheros entre tu PC y el servidor: Ctrl+C en un Explorador y Ctrl+V en el otro, o usa las unidades de tu PC que aparecen en el equipo remoto.

### Sesión SSH

- Terminal con colores, cursor y programas a pantalla completa como vim, htop o less.
- Historial: rueda del ratón o Mayús+RePág / Mayús+AvPág.
- Copiar: Ctrl+Mayús+C. Pegar: Ctrl+Mayús+V. Botón derecho: copia si hay texto seleccionado y pega si no lo hay.
- El terminal se adapta al tamaño de la ventana.

### Sesión de ficheros (SFTP / SCP y FTP / FTPS)

Mientras conecta, la pestaña muestra «Conectando con…»; al entrar aparece el explorador de dos paneles: este equipo a la izquierda y el servidor a la derecha. Cada panel tiene su barra de ruta (puedes escribir una ruta directamente) y columnas Nombre, Tamaño y Modificado (y, en servidores Linux/Unix, Permisos y Propietario).

Botones de los paneles:
- Este equipo (panel local): para cambiar de unidad.
- Subir un nivel (Retroceso).
- Actualizar.
- Nueva carpeta (F7).
- Renombrar (F2).
- Borrar (Supr): «Las carpetas se van con todo lo de dentro; no hay papelera.»
- Subir la selección al servidor / Bajar la selección a este PC (F5, o arrástrala al otro lado).
- Abrir: en local, con el programa por defecto de Windows; en remoto, una copia con el programa por defecto.
- Editar aquí (ficheros de texto).
- Copiar la ruta.
- Ver ficheros ocultos.
- Permisos y propietario (servidores Unix).
- Cancelar la transferencia (mientras hay una en curso).

Doble clic en un fichero de texto del servidor lo abre en el editor integrado; en un fichero local, lo abre con su programa de Windows. Las transferencias van en cola, con progreso («Subiendo… · N de M»).

Si un fichero ya existe y la conexión está en «Avisar y confirmar», sale «El fichero ya existe» con Sobrescribir, Saltar y la casilla «Hacer lo mismo con los demás».

**Ventana Permisos y propietario** (solo servidores Linux/Unix)
- Permisos: casillas Leer, Escribir y Ejecutar para Propietario, Grupo y Otros, con el valor Octal a la vista.
- Propietario y grupo: nombres o números; vacío = no cambiar. En SFTP, cambiar por nombre usa una orden por SSH con las mismas credenciales; la mayoría de servidores FTP no dejan cambiar el propietario.
- «Aplicar a todo lo de dentro de las carpetas».
- Aplicar.

**Editor de texto integrado**
- Guardar en el servidor (Ctrl+S), con la misma codificación y finales de línea.
- Buscar (Ctrl+F): Siguiente (Intro) y Anterior (Mayús+Intro).
- Ctrl + y Ctrl − cambian el tamaño de letra (se recuerda).
- La barra inferior indica línea y columna, y la hora del último guardado.
- Al cerrar con cambios pregunta si guardarlos en el servidor (Guardar, Descartar o Cancelar).

### Ajustes

**Dónde se guardan las conexiones**
- Este PC: las conexiones se quedan en tu perfil de usuario; nada sale del equipo.
- Google Drive: entras con Google en el navegador; el fichero va a la carpeta privada de la aplicación en tu Drive, sin acceso al resto de tus ficheros. En la pantalla de permisos de Google hay que marcar la casilla de Google Drive.
- OneDrive: entras con Microsoft; el fichero va a la carpeta de la aplicación en tu OneDrive, sin acceso al resto de tus ficheros.
- Debajo se indica con qué cuenta has entrado y la última sincronización.

**Frase de cifrado** (solo con Google Drive u OneDrive)
- Casilla de la frase, con botón de ojo para verla. Mínimo 8 caracteres.
- Guardar la frase y sincronizar.
- Sincronizar ahora.
- La frase no sale de tu PC ni se guarda en tu cuenta: usa la misma en cada equipo. Si la olvidas, la copia de la nube no se puede leer. Sin frase no se sube nada.
- Al arrancar se baja la copia de la nube si es más reciente y cada cambio se sube; si guardas desde dos equipos, gana el último.

**Importar conexiones**
- Botón «Importar de Remote Desktop Manager (.rdm) o ficheros de Escritorio remoto (.rdp)».
- De un .rdm se importan las conexiones RDP, SSH, FTP/FTPS y SFTP/SCP con sus carpetas. De los .rdp (puedes elegir varios a la vez) sale una conexión por fichero, con su nombre y sus opciones.
- Las contraseñas no se importan: se piden al conectar. Al terminar se indica cuántas se han importado, cuántas ya existían y cuántas se han dejado fuera por ser de tipos no admitidos.

**Ventana**
- «Al minimizar, al área de notificación» (activada por defecto). Desactivada, se minimiza a la barra de tareas como cualquier ventana.

Cerrar: cierra los ajustes.

### Acerca de

Contacto («Escribir al autor»), cambio de idioma, privacidad, licencia MIT y aviso legal.

### Opciones para accesos directos

Puedes crear un acceso directo que abra una conexión al arrancar: `sOCRCManager.exe --open "Nombre de la conexión"`. También `--edit "Nombre"` abre su editor y `--edit-file "Nombre" "/ruta"` abre un fichero del servidor en el editor integrado.

## Preguntas frecuentes

**No conecta a un servidor SSH, SFTP o FTP. ¿Qué pasa?**
Sale una ventana «No se ha podido conectar» con la razón: el nombre no resuelve (revisa el nombre o el DNS), el puerto está cerrado (puerto equivocado o servicio parado), no responde a tiempo (equipo apagado o cortafuegos), no hay ruta (revisa la red o la VPN), usuario o contraseña incorrectos, o el servidor no ofrece TLS. En este último caso prueba FTP sin cifrar o «FTPS implícito» en el puerto 990.

**El escritorio remoto dice que no puede continuar por el certificado.**
En el editor de conexión, pestaña Avanzado, «Si falla la autenticación del servidor (certificado)» debe estar en «Avisar» (te deja seguir tras avisar) o «Conectar sin avisar». «No conectar» bloquea los servidores con certificado propio.

**Al abrir una conexión RDP el zoom vuelve al 100 %.**
Desde la versión 2026.9.23.1 el zoom se aplica después de iniciar sesión y se reintenta unos segundos hasta que el servidor lo acepta. Actualiza a la última versión.

**He minimizado la ventana y ha desaparecido.**
Está en el área de notificación, junto al reloj (en Windows 11, quizá en los iconos ocultos, la flecha ^). Un clic la trae de vuelta. Si prefieres que se minimice a la barra de tareas, desactiva Ajustes › Ventana › «Al minimizar, al área de notificación».

**Con «Usar todos los monitores», ¿por qué la pestaña solo tiene una pantalla?**
Dentro de la pestaña el escritorio remoto siempre usa una sola pantalla. Al pulsar pantalla completa la sesión se reconecta (un par de segundos) con un monitor remoto por cada pantalla de tu PC, y al volver a la pestaña vuelve a una.

**He entrado con Google y la sincronización falla.**
Google muestra cada permiso como una casilla; si la de Google Drive se queda sin marcar, la aplicación avisa: «vuelve a entrar y marca la casilla de Google Drive». Vuelve a entrar desde Ajustes y márcala.

**En otro PC dice «El fichero de la nube está cifrado con otra frase».**
Tienes que escribir en Ajustes › Frase de cifrado exactamente la misma frase que usaste en el primer equipo. Si la has olvidado, la copia de la nube no se puede recuperar.

**He importado de Remote Desktop Manager y me pide las contraseñas.**
Es normal: las contraseñas de RDM y de los ficheros .rdp van cifradas para el usuario que las guardó y no se pueden importar. Al conectar se piden y puedes marcar «Recordarla en este PC (cifrada)».

## Privacidad

Las conexiones se guardan en tu perfil de usuario de Windows con las contraseñas cifradas para tu cuenta, y las sesiones van directamente de tu PC a tus servidores. Solo si eliges Google Drive u OneDrive, el fichero de conexiones se sube a la carpeta privada de la aplicación en tu propia cuenta, cifrado con una frase que no sale de tu PC. No hay servidor propio, ni cuenta, ni anuncios, ni rastreadores, ni analítica.
