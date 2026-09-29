# Anexos técnicos
- slug: anexos
- documento: constitucion.md
- orden: 6
- actualizado: 2026-09-25
- lema: El detalle técnico exhaustivo: el núcleo común de cualquier proyecto y los anexos de móvil, escritorio, servidor, código nativo y diseño.

Este es el documento técnico que está debajo de todos los demás. Nació como la norma de las
aplicaciones Android hechas con .NET MAUI y se generalizó: tiene un **núcleo común** (secciones 1 a
24) que vale para cualquier proyecto y **anexos** con el detalle de cada plataforma. Un proyecto
cumple aplicando el núcleo más los anexos de las plataformas a las que va.

Algunas partes son más antiguas que la constitución general y no siempre coinciden con ella (por
ejemplo, en las banderas del selector de idioma, en la tipografía o en las claves de firma). En ese
caso **manda la general**, que es la que se ha ido corrigiendo con cada lección. Un anexo sobre un
proyecto privado no se explica aquí.

## Núcleo común

### 1-2. Propósito y alcance

**Qué dice.** Es el documento de referencia para la arquitectura, la seguridad, la publicación y el
mantenimiento de cualquier proyecto —móvil, escritorio, servidor, web o código nativo—, desde el
diseño hasta el mantenimiento. Deja fuera las decisiones de producto y los requisitos de cada
aplicación.

**Por qué.** Separar lo común de lo particular permite que un proyecto nuevo sepa desde el primer día
qué tiene que cumplir.

### 3. Principios no negociables

**Qué dice.** Privacidad primero (y, si una aplicación comparte datos, el texto sale cifrado y la
autorización se comprueba en el servidor); mínimo privilegio; seguridad por defecto (cifrado en la
red, secretos fuera del repositorio, sin contraseñas por defecto); nada de fallos silenciosos; toda
publicación reproducible y verificable desde el código; licencia limpia; cambios pequeños y seguros;
y **estabilidad antes que mejora**.

**Por qué.** Son las ideas de las que salen todas las demás reglas: cuando una regla concreta no
cubre un caso, se decide con estos principios.

### 4. Licencia, procedencia y dependencias

**Qué dice.** Todo proyecto se publica con licencia MIT y un fichero de licencia en la raíz. No se
copia código con licencias que obligan a cambiar la del proyecto (las «copyleft», como la GPL); solo
se usan dependencias con licencias permisivas (MIT, BSD, Apache 2.0) o funciones del propio sistema
operativo. Cada dependencia se apunta en un inventario de terceros con su uso, su licencia y su
titular, y se revisa **antes** de añadirla.

**Por qué.** Una licencia copyleft «contagia» al proyecto que la incluye y le quitaría la libertad de
la MIT a quien quiera reutilizar el código. El inventario deja saber en cualquier momento qué hay
dentro y con qué permiso.

### 5. Estructura del proyecto

**Qué dice.** Cada cosa en su sitio: la lógica en servicios, nunca en la interfaz; los modelos de
datos sin lógica de presentación; las utilidades puras y sin estado; y lo de cada plataforma
encapsulado en su carpeta. Lo que comparten cliente y servidor está en un único módulo, los servicios
se reciben por inyección de dependencias, y no queda código muerto ni duplicado.

**Por qué.** La lógica fuera de la interfaz se puede probar y reutilizar; y con una sola fuente por
cada cosa, un arreglo se hace una vez y no en tres copias.

### 6. Seguridad, secretos y cumplimiento

**Qué dice.** Ninguna credencial en el repositorio; la configuración que se publica lleva los campos
sensibles vacíos, y sin credenciales no se permite el acceso. Todo lo que va por la red, cifrado, y si
atraviesa intermediarios, cifrado de extremo a extremo. Contraseñas guardadas como hash, nunca en
claro. Cada permiso y cada puerto, justificado. Si el software puede afectar a terceros (acceso
remoto, por ejemplo), aviso de uso responsable. Textos de tienda veraces, sin promesas incumplidas. Y
toda aplicación lleva un **aviso legal** visible: se entrega «tal cual», sin garantías, y su uso es
responsabilidad de quien la usa.

**Por qué.** Una contraseña por defecto es una contraseña publicada. El aviso legal es lo que
acompaña a cualquier software libre: se regala tal cual es, y no se puede responder de cada uso que
se le dé.

### 7. Arquitectura de presentación

**Qué dice.** La interfaz y la lógica siempre separadas: el código de cada pantalla es delgado y
delega en servicios. Se evitan patrones pesados de presentación cuando no aportan un valor claro, y
no se mezclan dos estilos para el mismo tipo de pantalla.

**Por qué.** La solución más sencilla que separa bien es la más fácil de leer y de mantener; un patrón
pesado solo compensa cuando resuelve un problema que existe.

### 8. Idiomas

**Qué dice.** Ningún texto visible escrito en el código: todo sale de un catálogo de traducciones. Si
falta una traducción, se usa el idioma por defecto, **nunca** la clave interna. Solo se anuncian los
idiomas que están traducidos de verdad. El idioma elegido se guarda y, la primera vez, se respeta el
del sistema. Fechas y números, con el formato del usuario. Castellano e inglés siempre, también en la
ficha, la política de privacidad, las notas de versión y el aviso legal.

**Por qué.** Enseñar la clave interna de un texto o un idioma a medias hace que la aplicación parezca
rota; y respetar el idioma del sistema evita que alguien tenga que buscar cómo cambiarlo.

### 9. Datos

**Qué dice.** Los datos del usuario se guardan en su dispositivo o en un servidor bajo su control;
cada dato en el almacenamiento que le corresponde; nada de secretos en claro; los datos que faltan o
están dañados se manejan sin fallos silenciosos; y se prevé cómo migrar el formato entre versiones.
Además repite, con detalle, el cifrado del texto del usuario de la constitución general (sección 5):
qué se cifra, qué no, con qué clave, la marca de versión y la migración.

**Por qué.** Los mismos motivos que en la constitución general: lo que sale del dispositivo, sale
ilegible, y lo que la base de datos necesita entender no se cifra.

### 10. Errores y registro

**Qué dice.** Prohibido fallar en silencio. Lo que puede fallar (ficheros, red, plataforma) se
protege con mensajes claros. Las trazas de depuración solo en las compilaciones de desarrollo, sin
datos personales ni secretos en los registros, y los ficheros de registro fuera del repositorio. En
servidores, registros que rotan para no llenar el disco. Y **nunca se espera a una tarea bloqueando el
hilo de la interfaz**.

**Por qué.** Lo último se aprendió así: sOC Credentials se quedaba colgada al arrancar, con la ventana
en negro, en cuanto había una clave guardada, porque la interfaz esperaba a una tarea que a su vez
necesitaba la interfaz para terminar.

### 11. Versiones

**Qué dice.** Un solo esquema en todo el proyecto, definido en un solo sitio: la fecha más un contador
del día a dos cifras (AAAA.MM.DD.NN), o una versión semántica cuando una tienda lo pida. La versión
legible y el código interno suben a la vez, con un script, y cada versión se apunta en el registro de
cambios.

**Por qué.** Mirando la versión se sabe de qué día es; y con un solo origen no hay dos componentes
que digan versiones distintas.

### 12. Compilación y empaquetado

**Qué dice.** Scripts guardados en el repositorio compilan, empaquetan y firman, de forma que
cualquier versión se puede regenerar desde el código. Paquetes autocontenidos cuando reducen
dependencias; un solo script si el proyecto mezcla varios lenguajes; firma con el material fuera del
repositorio; y la compilación, sin errores y con los avisos en retirada.

**Por qué.** Si solo se sabe compilar en un equipo concreto y de memoria, una versión antigua no se
puede reconstruir cuando hace falta.

### 13. Distribución y publicación

**Qué dice.** Primero un canal restringido (pruebas cerradas o un despliegue parcial) y solo después
todos. Los paquetes se verifican por su huella (SHA-256) antes de instalarse. Los textos de tienda,
coherentes en todos los idiomas. Y no se mezclan en la misma publicación cambios de funcionamiento
con cambios solo de textos de ficha.

**Por qué.** Un fallo que llega a pocos se arregla sin daño; la huella garantiza que lo que se instala
es lo que se publicó; y separar los cambios deja saber qué provocó un problema.

### 14. Servidores y servicios

**Qué dice.** Con un servicio gestionado de terceros: el esquema como código en el repositorio, solo
la clave pública en el cliente, y autorización por fila en el servicio. Con servidor propio: se
instala como servicio del sistema que arranca solo, la configuración va junto al programa sin
secretos, las direcciones que se anuncian son alcanzables desde fuera, el despliegue es automático
con sus credenciales como secretos del sistema de integración, y al terminar se comprueba que responde
con la versión esperada.

**Por qué.** Lo que se hace a mano en un servidor no se puede repetir ni revisar; y anunciar una
dirección de la red de casa hace que ningún cliente de fuera pueda conectar.

### 15. Comprobación de versión y actualización

**Qué dice.** Al arrancar, la aplicación mira, sin bloquear y en silencio si no hay nada, si existe
una versión distinta. Si la hay, **se lo propone al usuario**, que decide; nunca se actualiza sin su
permiso. Se descarga de una fuente de confianza, se verifica la huella, se conserva la configuración,
y en actualizaciones automáticas se escalonan las descargas para no saturar el servidor.

**Por qué.** Quien usa la aplicación tiene que poder saber que hay una versión mejor sin que se la
impongan.

### 16. Calidad

**Qué dice.** Sin errores de compilación; pruebas unitarias y de integración cuando sea viable, y de
extremo a extremo en sistemas distribuidos; permisos y puertos justificados; cada cambio verificado
en un entorno real; README y registro de cambios al día.

**Por qué.** Compilar no es funcionar: solo probando en real se ve lo que el compilador no ve.

### 17. Flujo de publicación

**Qué dice.** Siete pasos: subir la versión, actualizar el registro de cambios (y comprobar que la
constitución está al día), compilar y firmar con el script, validar lo generado, publicar en un
canal restringido, repasar la lista de comprobación del canal y, por último, pasar a producción y
marcar la versión en el repositorio.

**Por qué.** Un orden fijo hace que no se salte ningún paso por prisa.

### 18. Plan de contingencia

**Qué dice.** Qué hacer con los errores de siempre: compilación bloqueada (cerrar procesos y limpiar),
número de versión rechazado (subirlo), idioma por defecto bloqueado, problemas de firma (comprobar
clave, contraseña y alias), fallos de credenciales al publicar y fallos al desplegar un servidor.

**Por qué.** Cuando algo falla con prisa, tener la receta escrita ahorra el rato de recordar cómo se
arregló la última vez.

### 19. Criterio de «terminado»

**Qué dice.** Una versión está lista cuando compila y se firma bien, se publica sin fallos, el icono se
ve, los textos están en todos los idiomas, los permisos están justificados, el registro de cambios y
la versión están al día, se ha probado en real, y lleva el aviso legal.

**Por qué.** Es la lista de la que salen todas las de la constitución general: sin ella, «terminado»
significa algo distinto cada día.

### 20. Colaboración en el repositorio

**Qué dice.** Un cambio lógico por commit, mensajes con el qué y el porqué, sin mezclar cambios de
funcionamiento con cambios de estilo, ramas por tarea, revisiones con descripción e impacto, y la
documentación al día.

**Por qué.** Un historial limpio deja entender, deshacer o revisar cada cambio por separado.

### 21. Mejora continua

**Qué dice.** Se revisa el código de vez en cuando y se mejora a pasos pequeños, pero **nunca se
sacrifica la estabilidad por una mejora**: cada cambio deja el producto funcionando y comprobado, en
su propio commit, sin cambiar lo que ve el usuario. Lo grande se planifica como una función aparte.

**Por qué.** Una aplicación que funciona un poco peor pero funciona es mejor que una más bonita que
no arranca.

### 22. Nombres y estilo de código

**Qué dice.** Un solo idioma para código y comentarios en cada proyecto, las convenciones de nombres
habituales de cada lenguaje, estilos compartidos en vez de valores repetidos, y nombres descriptivos
en vez de abreviaturas.

**Por qué.** El código se lee muchas más veces de las que se escribe.

### 23. La constitución como submódulo

**Qué dice.** La constitución vive en su propio repositorio y cada proyecto la incluye como
submódulo, que dentro del proyecto es de solo lectura. Las mejoras se proponen en el repositorio
original; lo específico de un proyecto va en su README. Cada proyecto apunta a una versión concreta
y la actualiza a propósito, y al publicar se comprueba que no se ha quedado atrás.

**Por qué.** Una copia editada dentro de un proyecto es una divergencia, no una versión; y quedarse
anclado sin revisar hace que un proyecto incumpla reglas que ya se aprendieron.

### 24. Sistema de diseño visual

**Qué dice.** **Un valor visible, un origen**: ningún color, tamaño ni radio se escribe suelto en una
pantalla; todo sale de un color con nombre por su función («Primary», no «Azul») o de un estilo con
nombre. Cada color de fondo o de texto tiene su pareja clara y oscura. Hay un conjunto mínimo de
estilos (tarjeta, título, texto, botón principal y secundario), los controles declaran sus estados
(un botón desactivado tiene que parecerlo), las zonas táctiles miden 48 dp como mínimo, y cada
aplicación fija su escala una vez.

**Por qué.** Enumera los errores que se vieron de verdad: diccionarios de estilos que nadie cargaba,
la plantilla por defecto publicada sin tocar, el modo oscuro anulado sin querer fijando un color
claro en cada pantalla, varias paletas mezcladas por copiar pantallas de proyectos distintos. Un
color suelto es una decisión que nadie puede volver a encontrar.

## Anexo A: móvil y tiendas

### A.1 Estructura y objetivos

**Qué dice.** Carpetas fijas para pantallas, servicios, modelos y recursos, y lo de cada plataforma
en la suya. Cada aplicación declara si va a **Android, Windows o los dos**, con el mismo proyecto: lo
que depende de la plataforma queda detrás de un servicio con una implementación para cada una.
Ninguna regla se relaja por la plataforma. En Windows se entrega como EXE y MSIX y se publica en la
Microsoft Store; en Android, en Google Play.

**Por qué.** Un solo proyecto para las dos plataformas es un solo sitio donde arreglar cada fallo.

### A.2 Identificador de paquete

**Qué dice.** Todos siguen el mismo formato (com.socratic.nombre), en minúsculas.

**Por qué.** Es público y **no se puede cambiar** una vez publicado: conviene acertar a la primera.

### A.3 Permisos de Android

**Qué dice.** Se revisa el manifiesto antes de cada publicación, se justifica cada permiso, no se
piden los que las versiones modernas de Android ya no necesitan (mejor las funciones que no piden
permiso, como el selector de ficheros del sistema), se limitan a las versiones antiguas los que solo
hacen falta allí, y se quitan los que trae la plantilla del proyecto y no se usan.

**Por qué.** Un permiso heredado y sin uso incumple el mínimo privilegio igual que uno puesto a mano.

### A.4 Versiones para la tienda

**Qué dice.** La versión legible con la fecha y el código interno con el contador del día a dos
cifras, actualizados juntos en cada compilación.

**Por qué.** Con una sola cifra, el día que se pasa de nueve compilaciones el número del día
siguiente sale menor y la instalación se rechaza.

### A.5 Google Play

**Qué dice.** Canales de prueba cerrada, prueba interna y producción; siempre primero la prueba
cerrada, y a producción solo con los textos y permisos completos. Icono legible y textos coherentes
en todos los idiomas.

**Por qué.** Es lo que pide Google, y lo que evita que un fallo llegue a todos a la vez.

### A.6 Flujo de publicación en el móvil

**Qué dice.** Versión, registro de cambios, compilar y firmar, validar el paquete, publicar con el
script, comprobar en la consola (versión, canal, icono, idioma, textos) y marcar la versión en el
repositorio.

**Por qué.** El flujo general (sección 17) aplicado a Google Play.

### A.7 Paquetes con todo dentro

**Qué dice.** Todo paquete que se instala, también los de pruebas, lleva dentro todas sus piezas; nada
del despliegue rápido de desarrollo, que las deja fuera.

**Por qué.** Instalado a mano, un paquete así aborta al arrancar porque no encuentra sus piezas.

### A.8 Validación en el móvil

**Qué dice.** Para el día a día se usa un emulador de Android para PC rápido de arrancar, con un
script que instala y abre la aplicación, reglas para abrirla sin tocar nada más, comprobar que la
ventana de delante es la nuestra y que el arranque no deja ningún error en el registro. Pero ese
emulador lleva una versión antigua de Android y **no sustituye** al dispositivo real: antes de
publicar se prueba en uno real o en un emulador con la versión objetivo. Se comprueban el arranque en
frío, el tema claro y oscuro, cada idioma, y los estados vacíos y de error, siempre con **datos
inventados**, nunca personales.

**Por qué.** Una captura que «se ve bien» puede esconder un error que ya se registró; y los cambios
de las versiones nuevas de Android solo se ven en ellas.

### A.9 Diseño en .NET MAUI

**Qué dice.** La referencia es Task Manager: ante una duda, se hace como él. Los colores y estilos
están en dos ficheros que se cargan de verdad al arrancar, la plantilla de estilos por defecto se
sustituye (no se deja al lado), las tarjetas usan el control moderno y no el obsoleto, ninguna
pantalla fija su color de fondo, los botones declaran su estado desactivado, los iconos son de línea
y vectoriales (nunca emoji), y los textos salen del servicio de traducciones. Todas tienen la misma
pantalla «Acerca de» (icono, versión, contacto, idioma, privacidad, licencia y aviso legal), **sin
donaciones** en ninguna parte, y un menú lateral con, como mínimo, Inicio y Acerca de, cada opción
con su icono. Tipografía del sistema, salvo en los juegos.

**Por qué.** Comprobación barata incluida: si al renombrar un estilo la aplicación no falla, es que
ese fichero no se estaba cargando. Lo de las donaciones se aclaró tras una contradicción entre dos
secciones que explicaba por qué unas aplicaciones las tenían y otras no: manda la prohibición.

## Anexo B: escritorio

### B.1 Interfaz

**Qué dice.** Las tecnologías de ventanas de Windows (WinForms, WPF, WinUI), con el código de cada
pantalla delgado y el tema claro u oscuro del sistema cuando se pueda.

**Por qué.** Las mismas razones que la sección 7.

### B.2 Bibliotecas de controles de terceros

**Qué dice.** Se toman **controles sueltos, nunca el tema completo** de una biblioteca de terceros.
Hay una biblioteca de controles con licencia MIT admitida solo para tres controles que no existen de
serie (etiquetas, avisos dentro de la ventana y selector de hora), y se importan únicamente sus
piezas, apuntadas en el inventario de terceros.

**Por qué.** Un tema completo impone su propia identidad y reestiliza los controles de serie, así que
choca con el diseño propio; y cuando la aplicación tiene hermana en el móvil, el escritorio tiene que
parecerse a ella, no a la biblioteca.

### B.3 Empaquetado

**Qué dice.** Instalador o ZIP con un script reproducible, el código nativo incluido, y la integración
con el sistema (arranque automático, bandeja) a elección del usuario.

**Por qué.** Lo que se instala tiene que poder regenerarse, y lo que se queda en el sistema lo decide
quien usa el equipo.

### B.4 Actualización

**Qué dice.** Se actualiza sustituyendo el programa y reiniciando, conservando la configuración y
verificando la huella del paquete.

**Por qué.** Actualizar no puede costarle al usuario sus ajustes.

## Anexo C: web y servidores

**Qué dice.** Un servicio con su registro de usuarios, autenticación y panel según el proyecto, y los
modelos compartidos con los clientes. Siempre por HTTPS, autenticación por token, contraseñas como
hash, cifrado de extremo a extremo si el servidor reenvía tráfico entre clientes, y solo los puertos
necesarios, abiertos en el cortafuegos del equipo y en el del proveedor. Despliegue autocontenido,
como servicio que arranca solo, automatizado y con sus credenciales como secretos; registros que
rotan y una comprobación automática al terminar cada despliegue.

**Por qué.** Un servidor está expuesto a todo internet: cada puerto abierto de más es una puerta, y un
servidor que reenvía el contenido de otros no debería poder leerlo.

## Anexo D: código nativo

**Qué dice.** El código nativo (C++) va en un módulo propio con una frontera mínima hacia el resto;
se compila con un único script y las herramientas documentadas; se enlaza con las funciones del
sistema en vez de redistribuir bibliotecas de terceros con licencias restrictivas; y gestiona sus
recursos y errores de forma explícita, sin pasar fallos silenciosos al resto de la aplicación.

**Por qué.** El código nativo es donde un error puede tumbar todo el programa: cuanto más pequeña y
clara es su frontera, más fácil es encontrarlo.

## Anexo E: componentes compartidos y diseño

### E.1 Diálogos propios

**Qué dice.** Prohibido usar los diálogos del sistema; se usa uno propio compartido (una tarjeta
redondeada sobre un velo, con el tema y el color de la aplicación) que los sustituye uno a uno.

**Por qué.** Los del sistema rompen la coherencia visual y no siguen el tema.

### E.2 Notas del autor

**Qué dice.** Existe un botón flotante para tomar notas con el contexto de la pantalla, solo en los
dispositivos del autor y **solo en las compilaciones de desarrollo**: en las que se publican está
desactivado del todo, y se comprueba antes de cada publicación.

**Por qué.** Es una herramienta de trabajo que nunca debe llegar a quien usa la aplicación.

### E.3 Barras del sistema

**Qué dice.** Desde Android 15 las aplicaciones se dibujan de borde a borde, así que el contenido se
separa de las barras de estado y de navegación y el hueco se pinta con el color de la marca; nunca
pantalla completa.

**Por qué.** Si no, las barras del sistema tapan botones y textos.

### E.4 a E.8 Paleta, icono, menú, firma y pantalla de inicio

**Qué dice.** Todas las aplicaciones comparten **exactamente la misma paleta índigo**, sin acento
propio: el rojo solo para lo destructivo o un error y el verde solo para lo positivo. El icono de
cada aplicación es un dibujo blanco sobre un degradado índigo, legible en pequeño. La cabecera del
menú lleva solo el logo y el nombre, sin frases, y el pie del menú la versión. La navegación es un
menú lateral, nunca una barra de botones abajo. La contraseña de la firma nunca va en el repositorio.
Y la pantalla de arranque es la nativa del sistema, en índigo, sin pantallas de bienvenida
artificiales que hacen esperar sin motivo.

**Por qué.** Todas se reconocen como de la misma familia sin repetir el trabajo en cada una; y una
pantalla de bienvenida con una espera inventada solo retrasa a quien quiere usar la aplicación.
