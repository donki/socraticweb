# Constitución general
- slug: general
- documento: CONSTITUCION-GENERAL.md
- orden: 1
- actualizado: 2026-09-30
- lema: La capa de arriba: lo que vale para todo el catálogo y lo que se ha aprendido trabajando.

La constitución general es la norma común a **todo**: aplicaciones del móvil, programas de Windows,
juegos y web. Cada categoría tiene además su propio documento, que la amplía pero nunca la
contradice. Muchas reglas llevan entre paréntesis el caso real que las hizo necesarias; aquí se
cuentan también.

## 1. Principios no negociables

### 1.1 Licencia MIT y uso comercial

**Qué dice.** Todo el código propio y **todas** las bibliotecas que se usan tienen que tener una
licencia compatible con la MIT y que permita el uso comercial. Si una biblioteca no la cumple, se
descarta y se busca otra, sin discusión.

**Por qué.** El código se publica para que cualquiera pueda leerlo, reutilizarlo o mejorarlo,
también en un proyecto comercial. Bastaría una sola dependencia con una licencia más restrictiva
para impedirlo. Pasó con un motor de síntesis de voz cuya licencia no permitía el uso comercial:
quedó fuera y se usan otros dos con licencias abiertas.

### 1.2 Sin anuncios, sin rastreadores, sin analítica

**Qué dice.** Ninguna aplicación lleva anuncios, rastreadores ni analítica. No se mide al usuario,
no se le perfila y no se vende nada de lo suyo. No hay excepción ni la habrá. Lo único que se admite
es el **servicio de avisos de Google** (Firebase Cloud Messaging), y solo esa pieza, cuando una
función necesita que un aviso llegue al momento con la aplicación cerrada: el SOS de Family
Together. Nada de los módulos de analítica o de informes de fallos, los mensajes son solo de datos,
sin texto legible, y su uso consta en la política de privacidad y en la ficha de la tienda.

**Por qué.** Las aplicaciones son de uso libre y se hacen para aprender: no hay nada que
rentabilizar con los datos de nadie, y la confianza se pierde una sola vez. La excepción está
acotada al mínimo porque un SOS no puede esperar, y aun así el servicio que lo entrega no ve qué
dice el aviso: el texto se monta en el propio móvil.

### 1.3 Privacidad primero: local por defecto

**Qué dice.** Todo se procesa en el dispositivo y las aplicaciones se usan sin cuenta. Nada sale del
dispositivo salvo lo que el usuario configure a propósito y entienda. Si un requisito choca con
esto, gana la privacidad.

**Por qué.** Lo que no sale del dispositivo no se puede filtrar, vender ni perder en un servidor
ajeno. Es la forma más sencilla de proteger los datos: no tenerlos.

### 1.4 Cuenta y servidor, solo cuando la función es esa

**Qué dice.** Una aplicación puede pedir cuenta y guardar datos en un servidor solo cuando su razón
de ser es compartir lo mismo entre varios dispositivos o entre varias personas. No se concede por
comodidad: si funcionaría igual sin cuenta, va sin cuenta. Cuando se aplica:

- Se usa una cuenta que el usuario **ya tiene** (Google o Microsoft), nunca una cuenta nuestra.
- El texto del usuario sale **cifrado** (sección 5): en el servidor nunca es legible.
- Se dice claro **qué sale y para qué** en la pantalla de entrada, en la política de privacidad y en
  la ficha de la tienda, y los tres dicen lo mismo.
- Sigue sin haber anuncios, rastreadores ni analítica.

Hoy son dos: **Task Manager**, porque sin cuenta no hay forma de saber que el móvil y el portátil son
de la misma persona, y **Family Together**, porque ver dónde está cada miembro de un grupo no existe
sin servidor.

**Excepción registrada: Family Together entra sin cuenta.** En lugar de pedir una cuenta de Google o
Microsoft, la aplicación crea un usuario anónimo en el servidor al abrirla por primera vez, sin
pedir nada. Vincularlo a Google o Microsoft es opcional y solo sirve para recuperarlo en otro móvil.

**Por qué.** Con una cuenta que el usuario ya tiene, nosotros nunca guardamos contraseñas: no hay
nada que custodiar ni que se pueda robar. La excepción de Family Together se admite porque cada
persona usa un solo móvil y pedir una cuenta a toda la familia —niños, abuelos— frenaría
precisamente lo que la aplicación tiene que hacer. Sigue sin haber cuentas ni contraseñas nuestras.

### 1.5 Gratis y completo

**Qué dice.** No hay funciones de pago ni recortes artificiales.

**Por qué.** Una versión recortada que empuja a pagar sería lo contrario de la idea del catálogo: que
cualquiera las use libremente.

## 2. Estructura del repositorio

**Qué dice.** El trabajo se ordena en cuatro grandes carpetas —móvil, juegos, herramientas y web— más
una de material de pruebas. Las aplicaciones móviles comparten una carpeta común con la firma y el
código compartido (los diálogos propios, por ejemplo), y la referencian con rutas relativas, así que
**sacar una aplicación de su carpeta rompe la compilación**. Los ficheros de organización (tareas,
ideas) viven fuera de los repositorios.

**Por qué.** Lo común tiene una sola fuente: si cada aplicación llevara su copia de la firma o de los
diálogos, las copias acabarían siendo distintas sin que nadie lo notara.

## 3. Control de versiones

### 3.1 Commitear a menudo

**Qué dice.** Cada sesión de trabajo termina guardando los cambios en el control de versiones.

**Por qué.** El 1 de agosto de 2026 se perdieron diez horas de trabajo porque los cambios no estaban
guardados cuando falló una operación con ficheros.

### 3.2 Un repositorio por proyecto, y la constitución como submódulo

**Qué dice.** Cada proyecto tiene su repositorio, y la constitución entra en cada uno como
**submódulo** (un enlace a su repositorio), no como copia.

**Por qué.** Una copia suelta se queda vieja sin que nadie se entere; el submódulo apunta siempre a
la única versión que se edita.

### 3.3 Nunca se guardan secretos en el repositorio

**Qué dice.** Claves de firma, contraseñas y ficheros de credenciales no se suben nunca. Se excluyen
del control de versiones y se pasan al compilar o desde un fichero local.

**Por qué.** Los repositorios son públicos. Un secreto que se sube una vez queda en el historial para
siempre, aunque luego se borre.

### 3.4 Mensajes de commit en castellano, con el qué y el porqué

**Qué dice.** Los mensajes se escriben en castellano, en imperativo, y explican **qué** cambia y
**por qué**.

**Por qué.** Dentro de un año, el qué se puede leer en el código; el porqué solo queda en el mensaje.

### 3.5 Ningún asistente figura como autor

**Qué dice.** Los cambios van firmados solo por la persona que los publica. Ningún asistente de
inteligencia artificial aparece como autor ni como colaborador: ni en los commits, ni en las
descripciones, ni en los README, ni en las fichas de las tiendas.

**Por qué.** El código es del proyecto, y quien responde de él es quien lo publica. Que las
aplicaciones se hagan con ayuda de inteligencia artificial —la web lo dice abiertamente— no cambia
quién es el responsable. En septiembre de 2026 se reescribió el historial de todos los repositorios
para quitar esas menciones.

## 4. Secretos

**Qué dice.** Contraseñas y claves **nunca** van en el repositorio ni en la documentación. Las
aplicaciones móviles se firman con una clave común cuya contraseña se da en el momento de compilar,
y las credenciales para publicar en Google Play se guardan en el equipo de trabajo, fuera de los
repositorios.

**Por qué.** Con la clave de firma y su contraseña, cualquiera podría publicar una versión falsa que
los móviles aceptarían como nuestra. Con las credenciales de publicación, podría subirla a la
tienda.

## 5. Datos y bases de datos

Se aplica a toda aplicación que guarde datos del usuario en un servidor (las del principio 1.4). La
idea en una frase: **si algo tiene que salir del dispositivo, sale ilegible.**

### 5.1 El texto del usuario viaja cifrado

**Qué dice.** Todo campo de **texto libre** que sube a un servidor —títulos, notas, etiquetas,
nombres, apodos, direcciones, perfil— se cifra en el dispositivo antes de subir y se descifra al
bajar. La base de datos local se queda sin cifrar.

**Por qué.** Así, quien tenga acceso al servidor —un administrador, un fallo de seguridad— solo ve
texto ilegible. La copia local está en el dispositivo del usuario, que es suyo, y es donde las
pantallas buscan, filtran y ordenan.

### 5.2 No se cifra lo que la base de datos necesita entender

**Qué dice.** Fechas, sí/no, números, identificadores, los códigos por los que se busca y los hashes
que hay que comparar van sin cifrar.

**Por qué.** Son los que deciden qué se descarga, quién gana cuando dos dispositivos cambian lo mismo
y quién puede ver cada fila. Cifrarlos no hace la aplicación más discreta: la deja rota.

### 5.3 Con qué clave

**Qué dice.** Lo de una persona se cifra con una clave suya; lo de un grupo —sus datos, su nombre y
los apodos de sus miembros—, con una clave del grupo.

**Por qué.** Es lo que permite que los demás miembros del grupo lo lean, y solo ellos.

### 5.4 Una marca de versión delante

**Qué dice.** Todo texto cifrado empieza con una marca que dice con qué versión del cifrado se hizo.

**Por qué.** Permite convivir con lo que se subió antes sin cifrar y cambiar de algoritmo más
adelante sin perder lo anterior: la aplicación sabe cómo leer cada valor.

### 5.5 Ningún límite de longitud en el servidor sobre una columna cifrada

**Qué dice.** Las columnas que guardan texto cifrado no llevan tope de longitud.

**Por qué.** Cifrar alarga el texto (una cabecera más un tercio por la codificación), y un solo valor
que supere el tope hace que el servidor rechace el lote entero.

### 5.6 El servidor no escribe texto del usuario

**Qué dice.** Si una función del servidor rellena por su cuenta algún campo de texto del usuario, se
le quita esa parte.

**Por qué.** Reescribiría en claro lo que el dispositivo acababa de cifrar.

### 5.7 Al empezar a cifrar, se migra lo que ya estaba subido

**Qué dice.** La primera vez que se cifra, se reescribe una sola vez todo lo del usuario que ya
estaba en el servidor, se apunta que está hecho, y no se toca la fecha de modificación.

**Por qué.** Si no, lo antiguo seguiría legible. Y si se tocara la fecha, los demás dispositivos
verían un cambio que no existe y lo volverían a descargar todo.

### 5.8 Decir hasta dónde llega

**Qué dice.** Donde se implementa el cifrado se deja escrito qué protege y qué no.

**Por qué.** Por honestidad: una clave que se deriva de un dato que el servidor también conoce
protege de quien vea la tabla, pero no de quien tenga la tabla **y** ese dato. Escribirlo evita creer
que se está más protegido de lo que se está.

### 5.9 Sincronizar no puede fallar en silencio

**Qué dice.** Cuando el servidor rechaza algo, se guarda el motivo en un sitio que se pueda leer en
una versión publicada, no solo en una traza de depuración.

**Por qué.** El 1 de septiembre de 2026 la cola de subida estuvo horas atascada por un límite de
longitud del servidor, y nada lo decía.

## 6. Interfaz de usuario

### 6.1 Botones con iconos, no con palabras

**Qué dice.** Cada acción tiene un icono reconocible; el texto acompaña solo cuando el icono es
ambiguo. Vale para móvil, escritorio, juegos y web.

**Por qué.** Un icono se entiende en cualquier idioma, ocupa menos y no se corta con la letra grande.

### 6.2 Los iconos son siempre planos

**Qué dice.** Dibujo de línea en SVG, en un lienzo de 24×24, sin relleno, con trazo fino de puntas
redondeadas y un solo color: el índigo de la paleta, blanco sobre fondos de color y rojo para borrar.
**Nunca emoji**, ni iconos de colores, degradados o sombras, y cada acción usa el mismo icono en toda
la aplicación. La única excepción con color son las banderas del selector de idioma, también planas,
al lado del nombre del idioma; nunca las letras del país («ES», «US») ni el emoji de bandera.

**Por qué.** Los emoji cambian de dibujo según el teléfono, se cortan con la letra grande y no siguen
el tema claro u oscuro. Y el emoji de bandera Windows no lo dibuja: enseña dos letras sueltas. Por
eso esta web usa banderas dibujadas como imagen.

### 6.3 Un sistema de diseño común

**Qué dice.** Paleta índigo, tipografía del sistema, esquinas redondeadas y diálogos propios en vez
de los del sistema.

**Por qué.** Todas las aplicaciones se reconocen como de la misma familia, y los diálogos propios
siguen el tema y el color de la aplicación, cosa que los del sistema no hacen.

### 6.4 Modo claro y oscuro

**Qué dice.** Todo lo que tenga interfaz funciona en los dos modos.

**Por qué.** Es una preferencia del usuario, y una pantalla que ignora el modo oscuro deslumbra de
noche o deja textos invisibles.

### 6.5 Accesibilidad

**Qué dice.** Contraste suficiente, zonas táctiles de 48 dp como mínimo y textos que se pueden
agrandar. Con la letra del sistema en grande no se puede cortar ningún texto ni icono, y se prueba en
un dispositivo real con la escala de letra que use la persona.

**Por qué.** Mucha gente usa la letra grande, y es justo donde se rompen las pantallas que solo se
probaron con la letra por defecto.

### 6.6 Toda casilla de contraseña lleva el botón del ojo

**Qué dice.** Contraseñas, frases de cifrado y códigos llevan siempre dentro de la casilla un botón
con un ojo que alterna entre puntos y texto. En Windows, el control estándar de contraseña no sabe
enseñar lo escrito, así que se usa uno propio que superpone dos casillas.

**Por qué.** Evita equivocarse al teclear una contraseña larga sin poder comprobar qué se ha escrito.

### 6.7 Toda aplicación enseña sus novedades

**Qué dice.** Hay una pantalla de **Novedades** con lo que cambió en las cinco últimas versiones,
escrito para el usuario y en los dos idiomas. Sale sola la primera vez que se abre la aplicación
tras actualizarla, y después se puede abrir desde el menú o desde «Acerca de».

**Por qué.** Una función nueva que nadie sabe que existe es como si no existiera; y un cambio que no
se explica parece un fallo.

### 6.8 Nunca se pierde lo escrito sin avisar

**Qué dice.** Lo que se escribe o se pega en una casilla se aplica al salir de ella y al guardar, no
solo al pulsar Intro. Si no es válido, se avisa y no se guarda; nunca se descarta en silencio.

**Por qué.** En sOC Credentials, el secreto de doble factor que se pegaba se perdía al pulsar
«Guardar», y el usuario creyó que la aplicación no sabía leer su código.

### 6.9 Los errores, en el idioma del usuario, con la razón y qué hacer

**Qué dice.** El usuario nunca ve un mensaje técnico ni en otro idioma. Cada error previsible tiene
su texto traducido, y un fallo que impide lo que se pidió (conectar, sincronizar, entrar) sale en un
aviso que dice en una frase la razón y qué hacer. Lo técnico va al registro.

**Por qué.** sOC Credentials llegó a enseñar un mensaje interno en inglés de una biblioteca de
cifrado, y un error del servidor de veinte líneas dejó inservible la ventana de RC Manager. Ninguno
de los dos le decía nada útil a quien lo leía.

### 6.10 Una guía de configuración en todas las aplicaciones

**Qué dice.** Toda aplicación tiene una guía paso a paso con lo que hay que configurar para sacarle
partido: sus opciones principales y, si hace falta, ajustes del sistema (permisos, autocompletar,
aplicación por defecto, arranque con el sistema…). Cada paso explica qué hace, tiene un botón que lo
hace o abre la pantalla donde se hace, y enseña si está hecho, pendiente u opcional, comprobándolo
de nuevo al volver. Sale sola una vez y luego se abre desde el menú; los botones de avanzar van fijos
abajo.

**Por qué.** Muchas funciones dependen de un ajuste escondido en otra pantalla del sistema. Con la
guía, nadie se queda sin una función por no saber dónde se activa; y con los botones fijos,
«Siguiente» se ve aunque la letra grande haga desplazarse el texto.

### 6.11 Desbloqueo con contraseña propia

**Qué dice.** Las aplicaciones que se abren con su propia contraseña (una bóveda, por ejemplo), en
Windows se abren con esa contraseña o con la opción **«Confiar en este usuario y dispositivo»**, sin
Windows Hello. Esa confianza vale solo para ese usuario en ese dispositivo, y así se dice: otro
usuario del mismo equipo, u otro equipo, sigue necesitando la contraseña. Activarla pide
confirmación, y la ventana de la contraseña sale pequeña, abajo a la derecha.

**Por qué.** Deja claro qué se está confiando y a quién: la clave queda protegida por la cuenta del
sistema, no abierta para cualquiera que use el ordenador.

### 6.12 Un gestor global de errores en todas las aplicaciones

**Qué dice.** Un error inesperado **nunca cierra la aplicación**: se apunta en el registro con todo el
detalle, se avisa al usuario en su idioma y la aplicación sigue abierta. Se engancha al arrancar,
antes de abrir ninguna ventana, en todos los puntos por donde se puede escapar un error (el hilo de
la interfaz, las tareas en segundo plano y los propios de cada plataforma).

**Por qué.** La Microsoft Store rechazó sOC Phone Mirror en septiembre de 2026 porque «se cierra tras
arrancar»: un fallo al poner en marcha una herramienta que va dentro del paquete la tumbaba sin dejar
rastro, y no había nada que lo recogiera.

### 6.13 Nombres de productos ajenos en las aplicaciones

**Qué dice.** En los textos de las aplicaciones se pueden nombrar los productos de Microsoft y
Google, y además unos pocos más que hacen falta para que se entiendan (una aplicación de mensajería
muy extendida, un fabricante de móviles y sus marcas, y los navegadores más usados). El resto se
describe por lo que es («otros gestores de contraseñas», «el servicio de almacenamiento»…), salvo las
atribuciones que exige una licencia. En la web la regla es más estricta: solo Microsoft y Google.

**Por qué.** Evita problemas de marcas y de parecidos, y no hace falta nombrar un producto para
explicar qué hace una función.

## 7. Idiomas

**Qué dice.** Castellano e inglés como mínimo. Ningún texto va escrito dentro del código: todo pasa
por el servicio de traducciones. Un idioma nuevo se propone primero en la lista de ideas.

**Por qué.** Con los textos fuera del código, traducir es rellenar una tabla y no buscar frases por
todo el programa; y se evita anunciar un idioma a medias.

## 8. Calidad y entrega

**Qué dice.** Una tarea está **terminada** cuando:

- Compila sin avisos nuevos del compilador.
- El **banco de pruebas automatizadas** pasa entero, el cambio trae sus pruebas y la cobertura no
  baja (8.6).
- Se ha probado en un dispositivo real, no solo en un emulador.
- Si la aplicación sincroniza, se ha probado **en dos dispositivos con la misma cuenta**.
- Los textos están en los dos idiomas.
- Está guardada en el control de versiones y su documentación está al día.
- Se ha mirado si hay que actualizar **esta web** (la página de la aplicación o su guía de soporte),
  sea el cambio grande o pequeño, y si hace falta se publica en el mismo ciclo.
- Toda aplicación está en la web, salvo que su repositorio sea privado o esté a medias.
- La versión está publicada como **release en GitHub** con sus paquetes (APK en Android; EXE y MSIX
  en Windows) y las notas del registro de cambios.
- Las aplicaciones de Windows dejan cada versión en su carpeta de OneDrive, lista para arrancar tal
  cual, con un fichero que explica qué es cada cosa.

**Por qué.** Cada punto es un fallo que ya pasó: en un solo dispositivo no se ve nada de lo que puede
fallar al sincronizar; en el emulador no se ven los cambios de las versiones nuevas de Android; y una
opción que cambia de nombre deja mal la guía de la web si nadie la mira. La release en GitHub es lo
que queda de cada versión y lo que se puede enlazar.

### 8.1 Dónde se consigue cada aplicación

**Qué dice.** El README de cada repositorio empieza con una sección «Dónde conseguirla» con los
enlaces a sus tiendas (Google Play, Microsoft Store) y a las releases de GitHub, y se actualiza en el
mismo cambio en que la aplicación entra en una tienda nueva.

**Por qué.** Quien llega al código tiene que poder instalar la aplicación sin buscar.

### 8.2 Fichas de tienda en castellano e inglés

**Qué dice.** Toda aplicación que va a la Microsoft Store, y toda extensión de navegador que va a una
tienda (la de Edge, la Chrome Web Store y la de otros navegadores), tiene sus fichas dentro del
repositorio, una en cada idioma, listas para pegar campo a campo. Cuando dos tiendas piden lo mismo,
una remite a la otra. Las capturas se hacen con el código real y **datos inventados**, nunca datos
reales ni marcas ajenas. Las dos versiones dicen lo mismo y cambian en el mismo commit que las deja
viejas.

**Por qué.** Una ficha que promete una función que ya no existe es publicidad engañosa: cuando sOC
Credentials dejó de usar Windows Hello, también tuvo que salir de sus fichas. Y un solo texto que
mantener es menos texto que se desincroniza.

### 8.3 Aplicaciones de escritorio: una sola instancia, y manda la nueva

**Qué dice.** Si una aplicación que solo admite una ventana encuentra otra abierta **de una versión
anterior**, la cierra y sigue ella. Con otra de la misma versión, le pide que se enseñe y espera su
respuesta; si no llega, arranca igual. Si dos arrancan a la vez, una espera a la otra. Y al instalar
una versión nueva se vuelve a abrir la aplicación y se comprueba que la que corre es la nueva.

**Por qué.** En sOC Credentials, tras cada actualización el navegador volvía a abrir la versión vieja
en segundo plano, y abrir la nueva le pasaba el turno a la vieja: ocurrió tres veces en un día.

### 8.4 Pruebas en el equipo del desarrollador

**Qué dice.** Cuando se prueba en el mismo equipo donde se usa la aplicación de verdad, se usa un
**modo de pruebas aislado**, solo en las compilaciones de desarrollo, con sus propios datos y sin
registrarse en nada compartido (ni con los navegadores, ni con el sistema). Una prueba nunca puede
llegar a servidores, cuentas ni datos reales, y antes de cada clic automático se comprueba qué
ventana está delante.

**Por qué.** La instancia de pruebas de sOC Credentials chocaba con la real, y el autocompletar de la
real llegó a rellenarla con la contraseña maestra. Un clic perdido en RC Manager abrió una conexión
real contra servidores de trabajo.

### 8.5 Política de privacidad en el repositorio

**Qué dice.** Cada repositorio de una aplicación publicada lleva su política de privacidad en
castellano e inglés, que dice lo mismo que las fichas: qué datos se recogen (normalmente ninguno),
dónde se guardan y con quién se comparten.

**Por qué.** Las tiendas piden una dirección con la política desde el primer día, y así existe
aunque la aplicación aún no tenga su página en el catálogo.

### 8.6 Banco de pruebas automatizadas

**Qué dice.** Toda aplicación tiene un banco de pruebas automatizadas que se ejecuta entero con una
sola orden. Prueba la lógica —servicios, cálculos, formatos, importadores, cifrado, que las
traducciones en castellano e inglés tengan las mismas claves…—, no la interfaz; y para que la lógica
se pueda probar, se saca de las pantallas a clases propias. Son pruebas de verdad (resultados, casos
límite, errores), sin tocar datos reales, red externa ni servidores. Cada repositorio publica en su
README tres cifras con fecha: **cuántas pruebas hay** (y cuántas pasan), **qué parte del código
cubren** —también sobre toda la aplicación, que es la cifra honesta— y **cuánto tarda** el banco. La
cobertura tiende al 100 % y **nunca baja** de una versión a la siguiente sin explicarlo, y el banco
en verde es condición para dar una versión por buena. Esas cifras, junto con el **tiempo de
desarrollo con LLM** (horas aproximadas), se publican también en la ficha de cada aplicación en esta
web y en su tarjeta del catálogo, y se actualizan en el mismo ciclo que el README.

**Por qué.** Probar a mano no escala: un cambio en un sitio rompe otro que nadie volvió a mirar. Con
el banco, cada versión comprueba de nuevo todo lo anterior en segundos. Publicar las cifras obliga a
no engañarse: una cobertura que solo cuenta el código fácil de probar no dice cuánto de la
aplicación está comprobado.

### 8.7 Pruebas de interfaz automatizadas

**Qué dice.** Además de las pruebas de lógica, cada aplicación con interfaz tiene pruebas que la
manejan como lo haría una persona: la abren, recorren el menú, pulsan atrás en cada pantalla,
cambian de idioma, crean y borran un elemento de prueba y, en el móvil, comprueban que con la letra
grande ningún texto se sale de la pantalla. En Android se hacen con una herramienta libre de
automatización del móvil y en Windows con otra que usa la accesibilidad del sistema. Cada botón que
se pulsa lleva un identificador propio, para no depender del texto, que cambia con el idioma. Nunca
usan datos ni cuentas reales: en el móvil, solo en un emulador y entrando sin cuenta; en el
escritorio, con un modo aislado que no se conecta a nada. Se pasan antes de cada versión que toque
la interfaz, y su número y su tiempo se publican aparte de los de lógica.

**Por qué.** Hay fallos que solo se ven usando la aplicación: un botón de atrás que cierra la app en
vez de volver, un texto que desaparece con la letra grande, una pantalla que no se abre. Revisarlo a
mano en cada versión y en cada app es lento y se olvida; automatizado, se comprueba siempre igual.
Se probó primero en una app de móvil y otra de escritorio, y dio el mismo resultado en tres tandas
seguidas antes de hacerlo norma.

## 9. Cómo se registran las tareas

**Qué dice.** Lo pendiente se apunta en ficheros de trabajo fuera de los repositorios, uno por
aplicación, separando lo que puede hacerse desde el ordenador y lo que exige a una persona (consolas
web, el móvil, cuentas), ordenados de lo más corto a lo más largo. **Lo hecho se borra, no se
tacha**, y un fichero que se queda vacío se borra. Todos llevan la fecha de su última actualización.

**Por qué.** Una lista llena de cosas tachadas esconde lo que falta. La historia de lo hecho ya está
en el registro de cambios y en el historial de cada aplicación.
