# sOC Credentials
- slug: credentials
- plataformas: Android, Windows, extensión de navegador para Edge, Chrome y Firefox (en Windows)
- lema: Tus contraseñas y códigos de verificación, cifrados y solo tuyos, en móvil y PC.
- github: https://github.com/donki/Credentials
- tiendas:
  - Google Play (no publicada): la app todavía no está creada en Play Console; la URL prevista sería https://play.google.com/store/apps/details?id=com.socratic.credentials, que hoy da 404 (fuentes: D:\sOCProjects\09-PENDIENTE-Credentials.md punto 8, D:\sOCProjects\03-TAREAS-Credentials.md punto 1, README.md; comprobado el 2026-09-25).
  - Microsoft Store (no publicada): ficha preparada con el nombre «sOC Credentials», pero sin identificador de producto; el README dice «en cuanto Partner Center dé el enlace» (fuentes: README.md, store/microsoft/ficha-es-ES.md). Ojo: la versión de la Store no puede usar las extensiones de navegador; para eso hace falta la versión EXE de GitHub (README.md).
  - Edge Add-ons (publicada el 2026-09-24): https://microsoftedge.microsoft.com/addons/detail/soc-credentials/pcilggpjodagihemfbimfbnnmlbfhfbk (fuentes: 09-PENDIENTE-Credentials.md punto 7, CHANGELOG.md 2026.09.24.04, README.md; la URL responde 200 el 2026-09-25).
  - Chrome Web Store (no publicada): ficha preparada, falta la cuenta de desarrollador; sin ID (fuentes: 09-PENDIENTE-Credentials.md punto 7, store/chrome/ficha-es-ES.md).
  - Firefox Add-ons (no publicada): ficha preparada, sin enviar a AMO; sin ID de tienda (fuentes: 09-PENDIENTE-Credentials.md punto 7, store/firefox/ficha-es-ES.md). Hasta entonces, en Firefox solo se puede cargar como complemento temporal.
- descarga_alternativa: https://github.com/donki/Credentials/releases (APK, EXE/ZIP y MSIX de cada versión; última: v2026.09.25.03)

## Descripción

sOC Credentials guarda tus contraseñas y tus códigos de verificación en dos pasos en una bóveda cifrada con una única contraseña maestra, que solo conoces tú. No hay servidor nuestro ni cuenta nuestra: la bóveda vive en tu dispositivo o, si lo prefieres, en la carpeta privada de la aplicación dentro de tu propio Google Drive u OneDrive, siempre cifrada. Así tienes las mismas contraseñas en el móvil y en el PC.

Además de guardar, rellena. En Android se convierte en el servicio de autocompletar del sistema y te ofrece la cuenta adecuada en cada aplicación y en el navegador, y te propone guardar las nuevas. En Windows rellena las contraseñas de los programas de escritorio y, con su extensión para Edge, Chrome y Firefox, las de las webs, incluido el código de verificación de cada sitio.

Puedes traer todo lo que ya tenías: importa desde los navegadores, desde otros gestores de contraseñas y desde aplicaciones de códigos de verificación como Google Authenticator. Y sin anuncios, sin analítica y con licencia libre.

## Funciones principales

- Bóveda cifrada con tu contraseña maestra, en el dispositivo o en tu propio Google Drive u OneDrive, sincronizada sola entre dispositivos.
- Cuatro tipos de entrada: sitio web, aplicación, código de segundo factor y nota segura, con carpetas, etiquetas, favoritas y campos extra.
- Códigos de verificación en dos pasos (TOTP) en vivo, añadidos pegando el enlace, la clave o escaneando el QR; con semilla, QR para pasarlos a otra app y códigos de respaldo.
- Generador de contraseñas y medidor de fortaleza; historial de contraseñas anteriores.
- Autocompletar de Android en aplicaciones y navegadores, con oferta de guardar lo nuevo.
- En Windows: relleno en las aplicaciones de escritorio y extensión para Edge, Chrome y Firefox.
- Importación desde Chrome, Edge, Firefox, Brave, Bitwarden, KeePass, Aegis, 2FAS y Google Authenticator; exportación cifrada o en claro.
- Desbloqueo con huella o cara en Android y opción de confiar en el dispositivo.
- Bloqueo por inactividad y vaciado automático del portapapeles.
- Guía de configuración paso a paso; castellano e inglés.

## Guía de uso (soporte)

### Primera puesta en marcha

1. Instala la aplicación (Android: APK de GitHub; Windows: EXE de GitHub, recomendado si quieres las extensiones del navegador).
2. Pantalla **Crea tu bóveda**: escribe una **Contraseña maestra** (al menos 8 caracteres) y **Repite la contraseña maestra**, y pulsa **Crear**. Es la única llave de todo: nadie puede recuperarla, tampoco nosotros. Apúntala en un sitio seguro.
3. Tras el primer desbloqueo se abre sola la **Guía de configuración**. Cada paso tiene un botón que lo hace por ti (o te lleva a la pantalla del sistema) y se marca como **Hecho** solo; los opcionales van marcados como **Opcional**. Botones **Anterior**, **Siguiente** y **Terminar**. Puedes volver a ella desde el menú.
   - En Windows: **Siempre a mano** (arrancar con Windows y quedarse junto al reloj), **Contraseñas en las aplicaciones** (activar el relleno de escritorio), **Extensión para Edge / Chrome / Firefox** (un paso por cada navegador instalado), **Apaga el gestor del navegador** y **Tus contraseñas en todos tus dispositivos** (nube).
   - En Android: **Servicio de autocompletar**, **Servicio preferido de contraseñas** (Android 14 o posterior), **Contraseñas en <navegador>**, **Entrar con la huella** y **Tus contraseñas en todos tus dispositivos**.
4. Permisos en Android: **cámara**, solo para escanear códigos QR de segundo factor (si la niegas, puedes pegar el código); **internet**, solo si guardas la bóveda en la nube. Android pedirá además que elijas sOC Credentials como servicio de autocompletar.
5. Si quieres la bóveda en la nube: **Ajustes › Dónde vive la bóveda** y elige **Google Drive** u **OneDrive**; inicia sesión con tu cuenta y concede el acceso a la carpeta de la aplicación.
6. En otro dispositivo: crea la bóveda, entra en la misma cuenta de nube desde Ajustes y usa la misma contraseña maestra. Si la copia de la nube se creó con otra contraseña maestra, la aplicación te la pide para mezclarlas.

### Flujo normal

Abre la aplicación y desbloquéala con la contraseña maestra (o la huella). Busca la entrada y copia el usuario, la contraseña o el código, o deja que el autocompletar o la extensión los rellenen por ti. Cuando te registras en un sitio nuevo, acepta «¿Guardar en sOC Credentials?». En Windows la contraseña maestra se pide una vez por sesión y la aplicación se queda junto al reloj.

### Menú

**Bóveda** (inicio), **Ajustes**, **Guía de configuración** y **Acerca de**, con la versión al pie.

### Desbloquear

Campo **Contraseña maestra** con botón para verla, **Desbloquear** y, en Android si está activado, **Desbloquear con huella o cara**. En Windows sale como una ventana pequeña abajo a la derecha. Si la contraseña es incorrecta: «Esa no es la contraseña maestra».

### Bóveda

- **Buscar por título, usuario, sitio o etiqueta**.
- **Ordenar por**: **Título**, **Última modificación** o **Creación**.
- **Bloquear**: cierra la bóveda al momento.
- **Nueva** (+): elige el tipo, **Sitio web**, **Aplicación**, **Código de segundo factor** o **Nota segura**.
- Filtros en fila: **Todas**, **Favoritas**, uno por tipo, uno por carpeta (con «/») y uno por etiqueta (con «#»).
- En cada entrada: **Copiar el usuario**, **Copiar la contraseña**, **Copiar el código de segundo factor** y borrar. Tocarla abre el detalle.
- Si está vacía: «Añade tu primera credencial con + o importa desde un navegador u otro gestor en Ajustes».

### Detalle de una entrada

- **Favorita** (estrella) y tipo de entrada.
- **Título** (obligatorio), **Usuario o correo** (con copiar), **Contraseña** (con **Ver** / **Ocultar**, copiar y **Generar**) y barra de fortaleza: **Muy débil**, **Débil**, **Aceptable**, **Fuerte**, **Muy fuerte**.
- **Generador de contraseñas**: **Longitud**, **Mayúsculas**, **Minúsculas**, **Números**, **Símbolos**, **Evitar caracteres que se confunden (0/O, 1/l)**, botón para generar otra y **Usar**.
- **Sitio web (URL)** con **Abrir el sitio**.
- **Código de segundo factor (TOTP)**: pega el **Enlace otpauth:// o clave secreta** o pulsa **Escanear QR**. Con el código puesto se ve en vivo con su cuenta atrás, botón de copiar, quitar y **Ver la semilla** (la clave secreta, con copiar y su QR para darlo de alta en otra app de autenticación).
- **Códigos de respaldo**: pega los que te dio el sitio, uno por línea, y pulsa **Añadir códigos**. Se ven con **Ver los códigos de respaldo**; cada uno se copia, se borra o se marca como **Usado**, y arriba se indica cuántos quedan sin usar.
- **Carpeta**, **Etiquetas, separadas por comas**, **Notas**.
- **Campos extra**: **Añadir campo** con **Nombre**, **Valor** y **Oculto**.
- **Contraseñas anteriores**: historial al cambiar la contraseña.
- Fechas de creación y modificación; botones **Borrar** (desaparece de todos tus dispositivos) y **Guardar**. Si sales con cambios, pregunta «¿Guardar los cambios antes de salir?».

### Ajustes

- **Idioma**: **Español** / **English**.
- **Dónde vive la bóveda**: **Solo en este dispositivo**, **Google Drive** u **OneDrive** (el activo se ve resaltado). Con nube: «Sesión iniciada como …», **Sincronizar ahora** y **Cerrar sesión**. La sincronización también es automática: al abrir la bóveda, al volver a la aplicación y cada cinco minutos.
- **Seguridad**:
  - **Confiar en este usuario y dispositivo**: la bóveda se abre sola, sin contraseña maestra, pero solo para tu usuario en ese dispositivo. Pide confirmación (**Confiar**); actívalo solo si nadie más usa tu usuario.
  - **Desbloquear con huella o cara** (Android): la clave solo se libera tras verificar tu huella o tu cara.
  - **Bloquear tras inactividad**: **Nunca**, 1, 2, 5, 10, 15, 30 o 60 min.
  - **Vaciar el portapapeles a los**: **Nunca**, 15, 30, 60 o 120 s.
  - **Cambiar la contraseña maestra**.
- **Importar y exportar**:
  - **Importar…**: CSV de Chrome, Edge, Firefox, Brave, Bitwarden o KeePass; JSON de Aegis, 2FAS o sOC Credentials. Las repetidas se saltan.
  - **Escanear QR de Google Authenticator**: importa todos los códigos del QR de exportación de esa app.
  - **Exportar la bóveda cifrada**.
  - **Exportar a JSON en claro (¡sin cifrar!)**: pide confirmación; guárdalo a buen recaudo y bórralo al acabar.
- **Autocompletar** (Android):
  - Estado actual y **Usar sOC Credentials para autocompletar** / **Cambiar el servicio de autocompletar** (manda en las aplicaciones).
  - **Servicio preferido de contraseñas** (Android 14+; es el que obedecen Edge y Chrome).
  - **Abrir los ajustes del navegador**, con los pasos para apagar el gestor propio del navegador.
  - **Proponerlo al desbloquear**: mientras otro gestor sea el servicio de autocompletar.
- **Rellenar en las aplicaciones de Windows** (Windows): al entrar en un campo de contraseña de un programa, aparece a su lado la lista de entradas que encajan; pulsa una para teclear usuario y contraseña.
- **Windows**:
  - **Quedarse en el área de notificación al minimizar** (clic en el icono para volver; botón derecho para **Abrir** o **Salir**).
  - **Arrancar con Windows**: pide la contraseña maestra una vez al iniciar sesión y vuelve a pedirla tras bloquear Windows (Win+L).
- **Extensiones del navegador** (Windows): estado por navegador (**Instalada** / **No instalada**) con **Instalar…**, y **Ofrecer instalarla al desbloquear**. En Edge se abre la tienda (pulsa «Obtener» y «Agregar extensión»); en Chrome, «Modo de desarrollador» y «Cargar descomprimida» con la ruta ya copiada; en Firefox, «Cargar complemento temporal…» desde about:debugging.
- **Zona peligrosa**: **Borrar esta bóveda del dispositivo** (hay que escribir BORRAR; si no está en la nube, se pierde todo).

### Extensión del navegador (Edge, Chrome, Firefox)

- Icono en la barra: enseña las entradas del sitio con **Rellenar**, **Copiar usuario**, **Copiar contraseña** y **Copiar código**, y **Buscar en la bóveda…**.
- **Generar contraseña**: **Longitud**, **Mayúsculas**, **Números**, **Símbolos**, **Generar** y **Usar en la página**.
- Sección **Navegador**: interruptor «El navegador guarda y rellena contraseñas», para apagar o volver a encender el gestor del propio navegador. La primera vez pregunta si desactivarlo (**Desactivar el del navegador** / **Dejarlo**).
- En la página: al entrar en usuario o contraseña sale una lista pegada al campo; si has escrito algo nuevo, **Guardar lo escrito en sOC Credentials**. Al enviar un formulario pregunta «¿Guardar la cuenta de … en sOC Credentials?» o «¿Actualizar la contraseña…?» con **Guardar** / **Actualizar** / **Ahora no**. Menú del botón derecho: **Rellenar con sOC Credentials**.
- Necesita la aplicación de Windows instalada; si la bóveda está cerrada, avisa «Hay que abrir la bóveda en sOC Credentials».

### Acerca de

Versión, descripción, **Contacto**, **Privacidad**, **Licencia**, **Aviso legal** y **← Volver**.

## Preguntas frecuentes

**He olvidado la contraseña maestra.** No se puede recuperar: es la única llave de la bóveda y nadie más la tiene. Si activaste **Confiar en este usuario y dispositivo** o la huella en algún dispositivo, entra por ahí, exporta la bóveda y crea una nueva.

**Lo que guardo en el PC no aparece en el móvil.** Los dos tienen que usar la misma cuenta de Google Drive u OneDrive (Ajustes › Dónde vive la bóveda) y la misma contraseña maestra. Pulsa **Sincronizar ahora**. Desde la versión 2026.09.25.03 la sincronización es automática y está arreglado el error «OneDrive: 400 Invalid request».

**En Edge o Chrome del móvil me sigue ofreciendo Google en vez de sOC Credentials.** En Android 14 y posteriores los navegadores obedecen al **Servicio preferido de contraseñas**, no al de autocompletar. En Ajustes › Autocompletar revisa los tres sitios: el servicio de autocompletar, el servicio preferido y los ajustes del propio navegador.

**La extensión dice que no puede hablar con sOC Credentials.** Abre la aplicación una vez: ella sola registra el puente con el navegador. Si acabas de actualizar, con abrirla basta. Recuerda que la versión de la Microsoft Store no admite las extensiones; usa la versión EXE.

**En Firefox la extensión desaparece al cerrar el navegador.** Hasta que se publique en la tienda de Firefox solo se puede cargar como complemento temporal y hay que volver a cargarla cada vez.

**Me sale «La copia de la nube se creó con otra contraseña maestra».** Escribe la contraseña maestra con la que se creó esa copia para mezclarla; tu contraseña actual se mantiene.

**El navegador me ofrece guardar la contraseña dos veces.** Apaga su gestor propio desde el icono de la extensión (sección **Navegador**) o desde los ajustes del navegador.

**No puedo escanear el QR.** Sin permiso de cámara no se puede escanear; pega el enlace otpauth:// o la clave secreta en su lugar.

## Privacidad

sOC Credentials no recoge ningún dato: no hay servidor propio, ni cuentas, ni telemetría, ni anuncios. La bóveda se cifra en tu dispositivo con tu contraseña maestra y solo sale de él, cifrada, si tú eliges guardarla en tu propio Google Drive u OneDrive. La extensión del navegador no se conecta a internet: solo habla con la aplicación dentro de tu ordenador.
