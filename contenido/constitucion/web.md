# Constitución de la web
- slug: web
- documento: CONSTITUCION-WEB.md
- orden: 5
- actualizado: 2026-09-29
- lema: Esta misma web: sin rastreo, con una sola política de privacidad, bilingüe y con cada aplicación explicada pantalla a pantalla.

Amplía la constitución general para esta web y para cualquier servicio en internet del proyecto.

## 1. Principios

**Qué dice.** Seis principios para cualquier web del proyecto:

1. **Sin rastreo**: nada de analítica, cookies de terceros, píxeles de seguimiento ni fuentes cargadas
   de otros sitios.
2. **Estático por defecto**: si se puede hacer con HTML y CSS, no se añade JavaScript.
3. **Autocontenido**: nada de cargar piezas de servidores ajenos.
4. **Accesible**: HTML con significado, contraste suficiente, y que funcione sin JavaScript y con el
   teclado.
5. **Adaptable**: legible en el móvil, sin desplazamiento horizontal.
6. **Modo claro y oscuro**, según la preferencia del sistema.

**Por qué.** Cada pieza que se carga de otro sitio le cuenta a ese sitio quién visita la web. Sin
ellas, la web se puede alojar en cualquier parte y no filtra visitas; y lo sencillo funciona en más
dispositivos y se rompe menos.

## 2. La política de privacidad es parte del producto

**Qué dice.**

- Hay **una sola** política para todas las aplicaciones, y su dirección está en la ficha de Google
  Play y en la pantalla «Acerca de» de cada una. Si cambia la dirección, hay que cambiarla en todos
  esos sitios.
- Está escrita **en genérico, por casos**: las aplicaciones que funcionan enteras en el dispositivo, y
  las que sincronizan y necesitan cuenta y servidor. Cada una accede solo a lo que necesita para la
  función que anuncia; el detalle de permisos va en su ficha.
- **Excepción**: una aplicación que trata datos de otro tipo lleva su propio apartado. Hoy es Family
  Together, que comparte la ubicación dentro de un grupo; su apartado dice qué se envía y cada
  cuánto, cómo se cifra, cuánto se guarda, cómo se borra y qué terceros lo reciben, con su nombre,
  porque la ley lo exige.
- El caso «sincroniza» tiene sus condiciones por escrito: una cuenta que el usuario ya tiene, sin ver
  ni guardar contraseñas, el contenido **cifrado en el dispositivo antes de salir**, solo lo que la
  función necesita, y sin publicidad, perfiles ni analítica.
- **La política, la ficha de la tienda y la aplicación dicen lo mismo.** Si cambia lo que se guarda o
  dónde, cambian las tres en el mismo ciclo, y la política **antes** de publicar nada.
- Una copia de la política está también en Google Sites, que se actualiza a mano.
- Lleva a la vista la fecha de su última actualización.

**Por qué.** Google rechaza las fichas con la política de privacidad rota. Escribirla por casos hace
que una aplicación nueva no obligue a reescribirla. Y publicar con una política que no cuadra con lo
que hace la aplicación es declarar algo falso: hasta el 1 de septiembre de 2026 decía que no había
cuentas ni servidor, y había dejado de ser cierto.

## 3. Dónde vive la web

**Qué dice.**

- La web está alojada en un servicio de alojamiento de webs, en su plan gratuito. **La fuente de
  verdad es el repositorio**, nunca el editor del alojamiento: lo que se cambie a mano allí se pierde
  en la siguiente publicación.
- Cada aplicación tiene su ficha en un fichero de texto con una cabecera fija (nombre de la página,
  plataformas, lema, repositorio, tiendas y su estado) y las mismas secciones siempre: descripción,
  funciones, guía de uso, preguntas frecuentes y privacidad.
- Un generador produce a la vez una **copia local** navegable sin servidor y el contenido tal cual se
  publica, y las dos se guardan en el repositorio. Otra orden del mismo generador lo publica. La
  credencial para publicar vive fuera del repositorio.
- Sin complementos, widgets de terceros ni código de seguimiento. Las estadísticas propias del
  alojamiento vienen de serie en el plan gratuito: es la única excepción al principio de no rastrear,
  y afecta solo a la web alojada, no a la copia local.
- El diseño va en los propios bloques de cada página (colores, bordes, rejillas que se reordenan
  solas en el móvil), porque el plan gratuito no admite hojas de estilo propias.
- Antes de dar nada por terminado se revisa en escritorio y en móvil, con capturas de la web
  publicada: el móvil con **emulación de dispositivo**, no con una ventana estrecha. Nada puede tener
  desplazamiento horizontal.
- Comentarios cerrados en todo el sitio, sin «Me gusta» ni botones de compartir.

**Por qué.** Con el repositorio como única fuente, la web se puede regenerar entera o llevar a otro
alojamiento sin perder nada. La prueba en móvil con emulación se hizo regla porque una ventana
estrecha no baja de cierto ancho y la captura sale cortada, escondiendo justo los fallos que se
buscan.

## 3 bis. Normativa (España y Unión Europea)

**Qué dice.** La web cumple la ley de servicios de la sociedad de la información (LSSI-CE), el
Reglamento General de Protección de Datos y la ley orgánica española de protección de datos, con tres
páginas enlazadas desde el pie de todas:

- **Aviso legal**: quién es el titular, contacto, objeto, propiedad intelectual, enlaces,
  responsabilidad y ley aplicable. Hoy con nombre y correo; si la web tuviera actividad económica,
  habría que añadir NIF y domicilio.
- **Privacidad**: la de las aplicaciones más la de la web, con los derechos y cómo reclamar ante la
  Agencia Española de Protección de Datos.
- **Cookies**: cada cookie con quién la pone, para qué y cuánto dura, y cómo rechazarlas, con un
  aviso en todas las páginas.

Hay un **límite conocido**, escrito tal cual: el alojamiento pone sus cookies de estadísticas al
entrar, antes de que se acepte nada, y en el plan gratuito no se puede impedir. Cumplirlo al pie de
la letra exigiría un plan de pago o un alojamiento propio con la copia local. Y cuando cambian las
cookies, se vuelven a medir con el navegador y se actualiza la política.

**Por qué.** Es la ley. Y escribir el límite en vez de esconderlo es la misma honestidad que pide la
constitución general con el cifrado (5.8).

## 4. Contenido

**Qué dice.** La web tiene una **portada** (qué es sOCratic, las tarjetas de todas las aplicaciones y
la idea del catálogo), **una página por aplicación** (lema, plataformas, descripción, funciones,
privacidad, capturas y enlaces de descarga) y **una guía de soporte** por aplicación (cómo se pone en
marcha, cada pantalla con todas sus opciones y las preguntas frecuentes). Además, este apartado de
**Constitución**. Sus reglas:

- **Toda aplicación del catálogo está en la web**, salvo que su repositorio sea privado o esté a
  medias. Hoy fuera: sOC the Game (a medias), un proyecto de acceso remoto (privado) y sOC Lucia (por
  decisión propia).
- **En cada cambio de cualquier aplicación se mira si hay que actualizar la web**: su página, su guía o
  el estado de sus tiendas. Si cambia algo de cara al usuario, cambia su guía, que describe la
  versión que se descarga hoy.
- **Descarga**: la tienda si la aplicación está publicada de verdad (en prueba cerrada no tiene página
  pública, así que se enlaza a GitHub) y **siempre GitHub**, salvo si el repositorio es privado.
- Los nombres de pantallas y opciones se copian de los textos reales de la aplicación, no se inventan.
- **En castellano y en inglés**, con las mismas plantillas, menú y pie; el inglés bajo /en/, con los
  nombres de pantallas copiados de la aplicación en inglés. **Una ficha que cambia, cambia en los dos
  idiomas en el mismo ciclo.** Se cambia de idioma con las **banderas** del menú, dibujadas como imagen
  y nunca como emoji.
- **Imágenes** de cada aplicación sacadas de sus fichas de tienda, reducidas y subidas una sola vez; si
  cambian en la tienda, cambian aquí.
- **El menú de arriba se queda fijo** al desplazarse.
- **Sin correo a la vista**: el soporte va por incidencias de GitHub, y la dirección solo aparece donde
  la ley la exige (aviso legal y privacidad).
- **La idea del catálogo, en los textos generales**: las aplicaciones son de uso libre y sin anuncios,
  se hacen para aprender y para que otros aprendan, con el código abierto en GitHub. Y es **un
  experimento de programación con IA guiada por especificaciones**: primero se escribe qué debe hacer
  cada aplicación y con qué normas (esta constitución es la parte fija), y a partir de eso la
  programan modelos de lenguaje grandes (LLM). Se habla de ellos en genérico, **sin nombrar ningún
  modelo ni producto de IA concreto**, y sin promesas de producto comercial.
- **Nombres propios: solo los de Microsoft y Google.** El resto de productos y empresas se describen
  por lo que son («otros navegadores», «el servicio de mapas»…), salvo donde la ley o una licencia
  obliga a nombrarlos (privacidad, aviso legal, atribuciones), y ahí solo lo imprescindible.
- **Botones con iconos planos**, como en todo el catálogo.
- **El apartado «Constitución»** explica cada documento regla a regla, con el enlace al texto completo
  y su fecha. **Cuando cambia la constitución, cambia su página en el mismo ciclo**, en los dos
  idiomas, y el generador avisa si un documento es más nuevo que su explicación.

**Por qué.** La web es la puerta de entrada al catálogo, y solo sirve si dice la verdad del día: una
guía con un botón que ya no existe, o un enlace a una tienda donde la aplicación no está, hace más
daño que no tener guía. Sin correo a la vista se evita el correo basura, y las incidencias de GitHub
dejan las dudas y sus respuestas a la vista de todos. La regla de nombres evita problemas de marcas
y parecidos.

## 5. Servicios de servidor

**Qué dice.** Hoy el único servidor es el servicio de base de datos gestionado de Task Manager (y el
de Family Together, en desarrollo), y aunque no es nuestro, las reglas son las mismas o más estrictas:

- HTTPS obligatorio, secretos fuera del repositorio, autenticación robusta, límite de peticiones y
  registro.
- **En la aplicación solo va la clave pública** del servicio; la secreta y la de gestión no aparecen
  nunca en el código ni en nada que se distribuya.
- **La autorización se comprueba en el servidor**, con reglas por fila que dicen quién ve cada una.
  Que la aplicación no pida algo no es una protección.
- **El texto del usuario, cifrado**, y si el propio servidor rellena algún campo de texto, se le quita
  esa parte.
- **El esquema de la base de datos se guarda como código**, en ficheros numerados dentro del
  repositorio de la aplicación, que se aplican en orden y se pueden relanzar. Nada de cambios a mano
  en la consola que luego nadie sabe reproducir.
- **Si el servicio cae, la aplicación sigue funcionando** con los datos del dispositivo; lo que se
  pierde es sincronizar.

**Por qué.** Cualquiera puede leer el código de una aplicación publicada, así que todo lo que va
dentro se considera público: una clave secreta en el cliente es una clave publicada. Por eso la
autorización vive en el servidor, y el esquema versionado permite rehacer el servidor desde cero.
