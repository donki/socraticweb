# TDT Online
- slug: tdtonline
- plataformas: Android (móvil y tablet), Android TV
- lema: Los canales de la TDT en directo, en el móvil, la tablet y la tele.
- github: https://github.com/donki/TdtOnline
- tiendas:
  - Google Play (prueba cerrada): https://play.google.com/store/apps/details?id=com.socratic.tdtonline — solo en la pista de prueba cerrada (alpha, versión 2026091301 publicada y 2026091302 en borrador); la página pública da 404 hasta que pase a producción, lo que exige antes 12 probadores durante 14 días (fuentes: D:\sOCProjects\07-PENDIENTE-TdtOnline.md, README.md; comprobado el 2026-09-25 que la URL pública devuelve 404). En Play figura como «TDT Online: TV en directo» (Mobile\GooglePlayConsole\TdtOnline\ficha.md).
  - Microsoft Store: no aplica (solo Android).
- descarga_alternativa: https://github.com/donki/TdtOnline/releases (APK; última: v2026.09.13.2)

## Descripción

TDT Online te trae los canales de la Televisión Digital Terrestre en directo por internet, en tu móvil, tu tablet y tu televisor con Android TV. Abres la aplicación, eliges un canal y lo ves: sin registros, sin cuentas y sin anuncios.

Los canales se ordenan por categorías, con sus logotipos, un buscador y una categoría de favoritos para tener a mano los de siempre. La parrilla te enseña lo que se emite ahora y lo que viene después en cada canal, y la aplicación recuerda el último canal que viste para volver a él con un toque.

En la tele se maneja cómodamente con la cruceta del mando, y en el móvil con el dedo. La aplicación solo abre las emisiones que cada cadena publica en abierto por internet: no aloja ni reemite nada. Por eso no están las cadenas que solo se ven en sus propias plataformas con registro (como Antena 3, laSexta, Telecinco o Cuatro).

## Funciones principales

- Canales de la TDT en directo por internet (RTVE, autonómicas, temáticas e internacionales) con sus logotipos.
- Categorías en pestañas, con «Favoritos» y «Todos» al principio.
- Buscador de canales por nombre, sin importar acentos ni mayúsculas.
- Favoritos con un toque en la estrella o manteniendo pulsado OK en el mando.
- Parrilla de programación: lo que emite cada canal ahora (con barra de progreso) y lo siguiente.
- Programa en emisión en la pantalla del reproductor, con horario y descripción.
- «Último canal» para retomar lo que estabas viendo.
- Si una emisión falla, prueba sola la siguiente dirección disponible del canal.
- Listas de canales propias (JSON o M3U/M3U8) además de la lista por defecto.
- Misma interfaz en móvil, tablet y Android TV; castellano e inglés.

## Guía de uso (soporte)

### Primera puesta en marcha

1. Instala la aplicación en el móvil, la tablet o el Android TV (en la tele aparece en el lanzador con su propio banner).
2. Ábrela: no pide permisos, ni cuenta, ni configuración. Solo necesita conexión a internet. Al arrancar descarga la lista de canales («Cargando canales…») y se queda con una copia por si otro día no hay red.
3. Toca (o selecciona con la cruceta y pulsa OK) un canal para verlo.

### Flujo normal

Elige una categoría en la fila de arriba, toca un canal y se abre a pantalla completa. Vuelve atrás para regresar a la lista; el foco vuelve al canal que estabas viendo. Marca tus canales habituales como favoritos para encontrarlos siempre en la primera categoría.

### Pantalla principal

- **Cabecera**: título, contador «N canales» y, si ya has visto alguno, **Último canal: <nombre>** (tócalo para volver a verlo).
- Botones de la cabecera: **Ajustes** (rueda dentada), **Parrilla** (rejilla) y **Acerca de** (i).
- **Buscar canal…**: filtra entre todos los canales por el nombre. Con el mando, la tecla «Buscar» del teclado lo cierra y pasa el foco a los resultados. Si no hay coincidencias: «Ningún canal coincide con …».
- **Categorías**: **Favoritos** (siempre visible; vacía, explica cómo llenarla), **Todos** y una por categoría de la lista.
- **Rejilla de canales**: logotipo, nombre, programa actual y estrella de favorito. Tocar abre el canal; tocar la estrella o mantener pulsado el canal lo añade o lo quita de favoritos («Añadido a favoritos» / «Eliminado de favoritos»).
- Teclas del mando en Android TV: **Info** abre «Acerca de»; el **botón rojo** abre la parrilla; **Menú** o **Actualizar** vuelve a descargar la lista y la guía.

### Reproductor

- Pantalla completa con el nombre del canal, botón de **favorito** y **Ahora: <programa>** con su horario y descripción.
- **Botón amarillo** del mando: añade o quita el canal de favoritos.
- Si la emisión principal falla, aparece «Probando otra emisión…» y se prueba la siguiente; si ninguna funciona, «Este canal no se puede ver ahora mismo».

### Parrilla

Una fila por canal (favoritos delante) con el programa en curso, su barra de progreso marcada como **Ahora**, y los siguientes. Arriba, la hora. Con la cruceta se baja de canal en canal y se recorre cada fila; OK sobre el canal o sobre un programa abre el canal. Mientras se prepara, «Cargando la guía de programación…»; si no hay datos, «Ahora mismo no hay guía de programación».

### Ajustes

- **Listas de canales**: las listas que usa la aplicación. Se descargan cada vez que arranca; la primera manda en el orden de las categorías y las demás añaden canales y emisiones de repuesto. Se admiten JSON de tdt-canales, JSON de TDTChannels y M3U/M3U8. La de fábrica lleva la etiqueta **lista por defecto**.
- Papelera en cada lista: la quita («Lista quitada»).
- Campo de dirección (**https://…/lista.m3u8**) y botón **+**: añade una lista («Lista añadida»). Avisa si la dirección no es válida o si la lista ya está.
- **↻**: vuelve a descargar las listas ahora mismo.
- **↶**: restaura la lista por defecto («Lista por defecto restaurada»).
- **Cerrar**: vuelve a la pantalla principal.

### Acerca de

Versión, descripción, **Contacto**, **Idioma** (**Español** / **English**; se aplica de inmediato), **Privacidad**, **Licencia**, **Aviso legal** y **Cerrar**.

## Preguntas frecuentes

**¿Por qué no están Antena 3, laSexta, Telecinco, Cuatro y otras?** Esas cadenas (y Neox, Nova, Mega, FDF, Energy, Divinity, Be Mad o Boing) no publican su emisión en abierto: solo se ven en sus propias plataformas, con registro y protección anticopia. La aplicación solo puede ofrecer emisiones abiertas.

**Sale «No se ha podido cargar la lista de canales».** Comprueba la conexión a internet y pulsa actualizar (en la tele, el botón Menú o Actualizar del mando). Si has añadido listas propias y alguna no baja, se avisa y se sigue con las demás.

**Un canal dice «Este canal no se puede ver ahora mismo».** La cadena ha cortado o cambiado su emisión por internet. La aplicación ya ha probado las direcciones de repuesto; inténtalo más tarde.

**¿Dónde está DMAX?** Solo aparece cuando la cadena tiene su directo encendido en su web; ahora mismo lo tiene apagado, así que no sale.

**La parrilla sale vacía.** La guía tarda un momento en cargarse al arrancar («Cargando la guía de programación…»). Si sigue vacía, la fuente de la guía no está disponible en ese momento.

**¿Cómo añado un favorito con el mando?** Mantén pulsado OK sobre el canal, o pulsa el botón amarillo mientras lo ves.

**He tocado las listas y ya no salen los canales de siempre.** En Ajustes, pulsa **↶** para restaurar la lista por defecto.

## Privacidad

TDT Online no tiene cuentas, anuncios ni analítica. Solo descarga la lista de canales y la guía de programación y abre las emisiones públicas de cada cadena; los favoritos y el último canal visto se quedan en tu dispositivo.
