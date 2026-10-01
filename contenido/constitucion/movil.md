# Constitución de las aplicaciones móviles
- slug: movil
- documento: CONSTITUCION-MOBILE.md
- orden: 2
- actualizado: 2026-10-01
- lema: Firma, versiones, permisos, reglas de Google Play, el botón de atrás, las dos aplicaciones que usan servidor y el paso a producción.

Amplía la constitución general para las aplicaciones hechas con .NET MAUI. Cada una tiene por
objetivo **Android, Windows o los dos**, con el mismo proyecto. En Google Play están File Manager,
Hiker, Music Player, PDF Reader, QuitSmoke, SMS Forwarder, TXT Reader y sOC Uninstaller, que además
está en la Microsoft Store. Task Manager se reparte fuera de Play y es la única con cliente de
escritorio y servidor; Family Together, de localización familiar, está en desarrollo.

## 1. Estructura

**Qué dice.** Cada aplicación tiene su carpeta y su repositorio. La firma y el código común están en
una carpeta compartida a la que todas apuntan con rutas relativas, así que ninguna se puede mover de
sitio. Aparte se guardan las fichas de Google Play (textos, icono, imagen destacada, capturas) y los
vídeos de demostración que pide Google.

**Por qué.** Una sola fuente para lo común; y las fichas y los vídeos, junto al resto, para poder
rehacer una publicación sin buscarlos.

## 2. Firma

### 2.1 Todas con la misma clave que File Manager

**Qué dice.** Todas las aplicaciones se firman con **la misma clave que File Manager**, sin claves de
subida propias. Si alguna aparece firmada con otra, se corrige para que use la común, nunca al
revés. Las copias viejas de claves que quedan por ahí no valen para firmar: la única válida es la
que indica la configuración compartida.

**Por qué.** Una sola clave que custodiar, y una sola configuración que cada proyecto importa en vez
de repetirla.

### 2.2 Aplicaciones nuevas: la clave común desde el alta

**Qué dice.** Antes de subir la primera versión de una aplicación nueva, en Google Play Console se
elige usar **la misma clave de firma que otra aplicación de la cuenta: File Manager**. No se crea
ninguna clave nueva. Solo se puede hacer mientras la aplicación no tiene ninguna versión subida, y no
hay forma de hacerlo por programa: lo hace una persona en la consola.

**Por qué.** Si una aplicación nueva se deja con la clave que genera Google, Play rechaza el primer
paquete firmado con la común («esa clave ya firma otra aplicación que reciben los usuarios; crea una
distinta»), y reintentar no sirve. Pasó con sOC Credentials (tres intentos), Task Manager y TDT
Online.

### 2.3 Dos excepciones heredadas

**Qué dice.** Task Manager y TDT Online se dieron de alta con clave de subida propia antes de esta
regla, y en Play ya no se puede cambiar. Lo que suben a Play va con su clave; lo que se instala por
cable, con la común. No se repite.

**Por qué.** Se documenta para que nadie intente «arreglarlo» y se encuentre con que Play no lo
permite.

### 2.4 La clave no se puede perder

**Qué dice.** El certificado público de la clave está exportado y guardado, y la contraseña no está
en el repositorio: se da al compilar.

**Por qué.** Si se perdiera la clave habría que pedirle a Google que restableciera la clave de
subida, con la espera que eso supone; con el certificado a mano, la solicitud es inmediata.

## 3. Versiones

**Qué dice.** El número de versión interno sigue el formato **AAAAMMDDNN**: la fecha más un contador
de compilaciones del día, **siempre con dos cifras** (2026090701, no 202609071). La versión que se
ve, igual: 2026.09.07.01. El número solo sube, nunca baja: antes de compilar para la tienda se
comprueba cuál está publicado, y el del proyecto tiene que coincidir con el del paquete subido.

**Por qué.** Android solo exige que el número suba; que se lea como una fecha es comodidad nuestra.
Pero el contador a una cifra lo rompe: el día que se llega a la compilación 13 sale un número de
diez cifras, y al día siguiente la compilación 1 sale con nueve, es decir, **menor**. Android lo
rechaza como si fuera una versión anterior. Pasó con Task Manager el 7 de septiembre de 2026. Con
dos cifras caben 99 compilaciones al día, y el número sigue cabiendo en el máximo de Android hasta
el año 2099.

## 4. Permisos

**Qué dice.** Se pide **el mínimo imprescindible**, y cada permiso tiene que corresponder a una
función real y visible. Los permisos con función asociada se explican en la ficha de Play. Los
permisos restringidos (SMS, registro de llamadas, ubicación en segundo plano, instalar paquetes,
acceso a todos los ficheros) necesitan una declaración en la consola y, a menudo, un vídeo.

**Por qué.** Cada permiso es un acceso a los datos del usuario que hay que justificar; y Google
Play lo exige como norma, no como recomendación.

## 5. Reglas de Google Play

### 5.1 SMS: solo como aplicación de mensajes por defecto

**Qué dice.** Usar el permiso de enviar SMS para reenviar mensajes es un caso **prohibido** por Google.
La única vía válida es que la aplicación sea la **aplicación de SMS por defecto**, con todo lo que eso
obliga a implementar. Y una aplicación que pide ser la predeterminada (de SMS, de teléfono, de
navegador…) pide ese papel **antes que ningún otro permiso**, y ninguna pantalla pide permisos a la
vez que ese diálogo. Se prueba quitando el papel y los permisos y abriendo la aplicación: solo debe
salir el diálogo del papel.

**Por qué.** Google Play rechazó SMS Forwarder en septiembre de 2026 por esto, con el mismo código que
había aprobado en agosto; y el primer arreglo seguía pidiendo un permiso a la vez que el papel.

### 5.2 La versión de Android objetivo es obligatoria

**Qué dice.** Ninguna aplicación se compila ni se sube con una versión de Android objetivo por debajo
de la que exige Google Play en ese momento: hoy, **Android 16**, para aplicaciones nuevas y para
cualquier actualización. Se fija en dos sitios del proyecto que tienen que coincidir, se comprueba en
el manifiesto que genera la compilación (es lo que de verdad se sube) y, antes de cada publicación,
se mira si Google ha subido la exigencia.

**Por qué.** Si se deja sin fijar, la versión depende de lo que tenga instalado el equipo que
compila: dos aplicaciones se estaban compilando para una versión anterior sin que nadie lo supiera y
se corrigieron en agosto de 2026. Mejor subirla **antes** de compilar que después del rechazo.

### 5.3 Prueba cerrada primero

**Qué dice.** Hay una pista de prueba cerrada, con los mismos grupos de probadores para todas las
aplicaciones.

**Por qué.** Lo que falla, falla primero ante unos pocos que saben que están probando.

### 5.4 Vídeo de demostración sin cortes

**Qué dice.** Cuando Google pide vídeo, se graba sin cortes y enseñando el flujo completo que
justifica los permisos.

**Por qué.** Es lo que el revisor necesita ver para aprobar un permiso sensible; un vídeo con cortes
parece que esconde algo.

### 5.5 Declaraciones de la consola que bloquean la publicación

**Qué dice.** Algunos permisos dejan subir el paquete pero no dejan cerrar la publicación hasta que
se rellena un formulario en la consola web: los **servicios en primer plano** (le pasa a Hiker, que
graba rutas así, y le pasará a Music Player por la música en segundo plano), el **permiso de leer
SMS** (lo que tiene bloqueado a SMS Forwarder) y las aplicaciones recién dadas de alta, que solo
admiten versiones en borrador.

**Por qué.** No es un fallo del programa de publicación sino una norma de Google, y el mensaje lo dice
tal cual; saberlo evita perder tiempo buscando un error que no existe.

### 5.6 Verificación de desarrollador

**Qué dice.** Para que una aplicación se pueda instalar en un Android certificado, su nombre de
paquete tiene que estar registrado a nombre de un desarrollador con la identidad verificada. Las
aplicaciones de Google Play quedan cubiertas al darlas de alta, pero se comprueba una vez en la
consola que no hay avisos. Si algún día se reparten paquetes fuera de Play firmados con la clave
propia, habrá que registrarla también.

**Por qué.** Un paquete sin registrar puede suponer la retirada de la tienda en todo el mundo, aunque
el bloqueo de instalación aún no se aplique en España.

## 6. Publicación

**Qué dice.** Orden fijo: subir la versión, compilar el paquete firmado, comprobar el número de
versión real en el manifiesto generado, subirlo a las pistas de prueba, probar en un dispositivo real
y solo entonces pasar a producción. Dos notas de la interfaz de programación de Google Play: una
opción de revisión que unas aplicaciones exigen y otras prohíben (se prueba primero sin ella), y que
actualizar la lista de probadores la **sustituye** entera, así que se lee la actual y se combina.

**Por qué.** Cada paso protege del siguiente: comprobar el número antes de subir evita un rechazo, y
probar antes de producción evita que el fallo llegue a todos. Lo de los probadores se aprendió
borrándolos sin querer.

## 7. Interfaz

### 7.1 Diseño y pantallas comunes

**Qué dice.** El diseño índigo común, diálogos propios, botones con iconos planos (nunca emoji), una
pantalla «Acerca de» igual en todas (logo, versión, contacto, idioma, licencia) y, en las que
sincronizan, quién ha entrado y con qué cuenta, con opción de salir.

**Por qué.** Quien usa una aplicación del catálogo ya sabe moverse por las demás; y saber con qué
cuenta se está sincronizando es parte de la privacidad.

### 7.2 El botón de atrás

**Qué dice.** En cualquier pantalla que no sea la de inicio, atrás **vuelve a la anterior**, igual que
la flecha de arriba; si hay algo abierto encima (un menú, un diálogo, un buscador), primero se cierra
eso. En la pantalla de inicio, la aplicación **se oculta** sin cerrarse ni preguntar, y al volver
sigue donde estaba. Se prueba en el móvil, con el gesto y con el botón, en cada pantalla.

**Por qué.** Es lo que espera cualquiera que usa Android. Y hay dos trampas documentadas: si la
actividad principal intercepta el botón, las pantallas no se enteran; y **Android 16 activa el «atrás
predictivo»**, con el que el botón deja de llegar a las pantallas y la aplicación se cierra desde
cualquier sitio. Hasta que .NET MAUI lo soporte, se desactiva en el manifiesto. En el emulador con
una versión anterior de Android no se ve: solo en un móvil real con Android 16 (se descubrió con File
Manager en septiembre de 2026).

## 8. Task Manager: cuenta, servidor y cifrado

Es la aplicación con cuenta y servidor, y su descripción tiene que coincidir palabra por palabra con
la política de privacidad y con la ficha.

- **Entrada con una cuenta que el usuario ya tiene**, de Google o de Microsoft, con el protocolo
  estándar de inicio de sesión (OAuth 2.0 con PKCE) contra el propio proveedor. Nunca vemos la
  contraseña. La entrada con Microsoft está hecha pero oculta hasta probarla con una cuenta real.
- **Servidor:** un servicio de base de datos gestionado, alojado en Reino Unido. Es el único tercero,
  y solo como alojamiento.
- **Qué se guarda:** tareas, listas, pasos, adjuntos, perfiles, grupos y sus miembros, y apuntes de
  lo borrado (solo identificador y fecha, sin texto).
- **Qué va cifrado:** títulos, notas, etiquetas, nombres de lista y de paso, nombre y dirección de los
  adjuntos, nombre de grupo, apodos, y del perfil el nombre, el correo y la foto. Con AES-256-GCM.
- **Qué no va cifrado, a propósito:** fechas, marcas, números, identificadores, el código para unirse
  a un grupo (es por donde se busca) y el hash de su clave (hay que compararlo).
- **La autorización se comprueba en el servidor**, fila a fila. Que la aplicación no pida algo no
  protege nada.
- **Sin servidor sigue funcionando**: los datos están también en el dispositivo; lo que se pierde es
  sincronizar.
- **El aviso entre dispositivos no es inmediato**, y es una decisión: una pasada cada 30 minutos más
  el botón de refrescar.

**Por qué.** Es la aplicación del catálogo que más datos personales toca, así que su tratamiento se
escribe con detalle para poder consultarlo sin abrir el código. Un aviso instantáneo exigiría el
servicio de avisos de Google y su proyecto asociado, y para una lista de tareas no compensa.

## 9. Pruebas en dispositivo

**Qué dice.** Hay un móvil y una tableta de referencia, y el material de pruebas de cada aplicación se
guarda ordenado. Dos trampas apuntadas: algunos fabricantes, al instalar por cable, sacan un diálogo
de confirmación con una cuenta atrás de seis segundos que se deniega solo, y el error que queda
parece de permisos; y un paquete firmado en local no se puede instalar encima de la misma aplicación
instalada desde Google Play, porque la firma es distinta: hay que desinstalar primero.

**Por qué.** Son errores que despistan y que hacen perder mucho tiempo la primera vez; apuntados, la
segunda son diez segundos.

## 10. Family Together: usuario anónimo, servidor, avisos y ubicación

Family Together comparte la ubicación dentro de un grupo familiar cerrado. Sus reglas propias:

- **Usuario anónimo** creado al abrirla por primera vez: solo un nombre visible y, si se quiere, una
  imagen. Vincular Google o Microsoft es opcional y sirve para recuperar el usuario en un móvil
  nuevo; esa vinculación se verifica en el servidor, al recuperar se pasan los grupos al móvil nuevo,
  nunca se fusionan dos usuarios, y una cuenta ya vinculada a otro se rechaza con aviso.
- **Servidor:** de momento, un servicio de base de datos gestionado; el destino es una instalación
  propia del mismo servidor (de código abierto) en la nube, en la Unión Europea. **Sin copia de
  seguridad diaria fuera del servidor no se pasa a producción**, solo se abre el puerto seguro de la
  web, el acceso de administración va con clave y los paneles no son públicos. Sin servidor la
  aplicación no funciona, porque su razón de ser es compartir.
- **Permisos por fila en todas las tablas**: cada persona solo ve lo de sus grupos, y unirse, aprobar,
  expulsar o recuperar solo se hace con funciones del servidor que comprueban el papel de quien lo
  pide. Una prueba con un usuario de otro grupo no debe devolver nada.
- **Cifrado:** nombre del grupo, nombres e imágenes de los miembros, nombres de las zonas **y también
  las coordenadas**, con la clave del grupo. Esa clave **nunca pasa en claro por el servidor**: va de
  móvil a móvil cifrada con un intercambio de claves (ECDH). Sin cifrar solo quedan fechas,
  identificadores, batería y el código de invitación.
- **Una posición por cada grupo** en el que se comparte, cifrada con la clave de ese grupo, y se
  guarda **30 días**; después se borra sola.
- **Avisos al momento** con el servicio de avisos de Google, solo mensajería: los mensajes llevan solo
  identificadores y el texto se monta en el móvil; los destinatarios los calcula el servidor al
  enviar; cada aviso tiene un identificador para descartar repetidos, y hay canales separados para
  SOS, zonas y solicitudes.
- **El mapa** usa una biblioteca de mapas libre **empaquetada dentro de la aplicación** y un estilo de
  mapa abierto que no pide clave. Nada de Google Maps ni de los servicios de Google Play para el mapa.
- **Ubicación en segundo plano** con un servicio en primer plano: se envía cuando uno se mueve más de
  25 metros, se descartan las lecturas imprecisas, y sin conexión se guardan en cola con su hora
  original. Hay una guía para que el ahorro de batería del fabricante no la corte.
- **Solo el último móvil que ha entrado comparte ubicación**: al recuperar el usuario en otro, el
  anterior deja de enviar.
- **Permisos** (ubicación precisa y en segundo plano, servicio en primer plano, notificaciones y
  cámara para leer el código QR), todos declarados en la consola, con vídeo y explicados en la ficha.

**Por qué.** La ubicación de una familia es de los datos más delicados que existen. Por eso se cifran
hasta las coordenadas (la base de datos no las necesita: las zonas se detectan en el móvil), la
clave del grupo nunca la ve el servidor, y guardar una posición por grupo hace que la pausa se cumpla
en origen: lo registrado mientras se estaba en pausa para un grupo nunca le llega. Los mensajes de
aviso no llevan texto para que el servicio que los entrega no sepa qué dicen, y el mapa va dentro de
la aplicación para no depender de cargarlo de fuera.

## 11. Paso a producción en Google Play: el cuestionario, preparado

**Qué dice.** Para pasar de la prueba cerrada a producción, la consola de Google Play pide un
cuestionario: cómo se reclutaron los probadores y cuánto costó, qué hicieron con la aplicación, qué
sugirieron, a quién va dirigida, qué valor aporta, cuántas instalaciones se esperan, qué se cambió
durante la prueba y por qué se da por preparada. Cada aplicación de Play lleva esas respuestas
escritas en su repositorio, en el idioma de la consola y con cada texto dentro de los **300
caracteres** del formulario (con su longitud al lado), listas para pegar; para las preguntas de
opciones, la propuesta. Los cambios salen del registro de cambios desde que la aplicación entró en
la prueba cerrada, y lo de «preparada» se apoya en el banco de pruebas automáticas, las pruebas en
un móvil real, la ausencia de fallos en la consola y la ficha y la seguridad de los datos
completas. Dos reglas: **nunca se inventa** lo que hicieron o dijeron los probadores, y lo que solo
se sabe mirando la consola (si de verdad la usaron, sus comentarios, los fallos registrados) va
marcado para comprobarlo antes de enviar. El fichero se escribe al subir una aplicación a la prueba
cerrada y se pone al día con cada versión que cambie lo que dice.

**Por qué.** Son nueve aplicaciones con el mismo cuestionario, y escribirlo a última hora en la
consola, con el límite de caracteres encima, acaba en respuestas vagas o, peor, en afirmaciones que
nadie ha comprobado. Preparado con los datos del repositorio, cada respuesta dice lo que la
aplicación hace de verdad (sus permisos, si tiene cuenta o servidor) y lo dudoso queda señalado: el
día que se cumplen los catorce días de prueba, pedir producción son unos minutos.
