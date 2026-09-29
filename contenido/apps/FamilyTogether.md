# Family Together
- slug: familytogether
- plataformas: Android
- lema: Tu familia en el mapa, en un grupo cerrado y cifrado de extremo a extremo.
- github: https://github.com/donki/FamilyTogether
- tiendas:
  - Google Play: no publicada (todavía no está en Play; el APK de cada versión va en las releases de GitHub, según el README del repositorio a 2026-09-29)
  - Microsoft Store: no publicada (solo Android)
- descarga_alternativa: https://github.com/donki/FamilyTogether/releases (última: v2026.09.28.00, APK)

## Descripción
Family Together sirve para que las personas de un grupo cerrado —tu familia, tus amigos— vean dónde está cada una. En el mapa aparece la última posición de cada miembro con la hora y la batería de su móvil, y en el historial puedes ver por dónde ha ido cada uno en los últimos 30 días, con el recorrido ajustado a las calles y las paradas marcadas.

Podéis crear zonas (casa, colegio, trabajo) y elegir de quién queréis un aviso cuando llega o se va. Con el botón rojo mandas un SOS a tus grupos, con tu posición, aunque tengas la compartición en pausa. Y cuando quieras intimidad, pausas un grupo una hora, hasta mañana o hasta que lo reanudes.

No hace falta cuenta ni contraseña: al abrirla por primera vez solo eliges el nombre con el que te verán. Todo lo que se escribe y las coordenadas se cifran en el móvil con una clave que solo tienen los móviles del grupo, así que el servidor guarda datos que no puede leer. De uso libre, sin anuncios, sin analítica y con el código abierto.

## Funciones principales
- Mapa con la última posición de cada miembro del grupo, con la hora y el nivel de batería, o «En pausa».
- Ubicación en segundo plano cada vez que te mueves unos 25 metros, también con la aplicación cerrada; sin conexión, las posiciones se guardan y se envían después con su hora.
- Historial de recorridos de los últimos 30 días por persona y día, ajustado a calles y caminos en el propio móvil, con las paradas largas como un punto.
- Zonas del grupo con avisos al entrar y al salir, solo de las personas y zonas que tú elijas.
- SOS con cuenta atrás de 3 segundos para cancelarlo, a todos tus grupos o a los que marques, aunque estés en pausa.
- Pausa por grupo: 1 hora, 8 horas, hasta mañana, hasta una hora concreta o hasta que la reanudes.
- Grupos cerrados: invitación con código o QR que caduca a los 5 minutos y entrada aprobada por un administrador.
- Sin cuenta: usuario anónimo, con vinculación opcional de Google o Microsoft para recuperarlo en otro móvil.
- Nombres, zonas y coordenadas cifrados de extremo a extremo con la clave del grupo; borrar tu historial cuando quieras.
- En castellano e inglés, con modo claro y oscuro.

## Guía de uso (soporte)

### Primera puesta en marcha
1. Descarga el APK de la última versión desde las releases de GitHub e instálalo (Android 8 o posterior). Android te pedirá permitir la instalación de aplicaciones de origen desconocido para el navegador o el gestor de archivos con que lo abras.
2. Abre Family Together. La pantalla **Bienvenida** explica **Qué hace Family Together** y **Qué sale de tu móvil**. En **Cómo te verán** escribe **Tu nombre visible (obligatorio)** —es lo que verán los demás en el mapa; puede ser un apodo— y, si quieres, elige **Tu foto o avatar (opcional)** con **Elegir foto**. Pulsa **Continuar**.
3. Se abre la **Guía de configuración** («Prepara tu móvil»), paso a paso. Cada paso tiene un botón que lo hace o que abre la pantalla de Android donde se hace, y dice si está **Hecho** o **Pendiente**:
   - **Ubicación precisa** (**Permitir ubicación**): elige «Ubicación precisa»; con la aproximada no saldría ninguna posición.
   - **Permitir siempre** (**Permitir todo el tiempo**): Android no lo ofrece en un diálogo; se abren los ajustes y ahí eliges Permisos > Ubicación > Permitir todo el tiempo. Sin esto tu grupo solo te ve con la aplicación abierta.
   - **Notificaciones** (**Permitir notificaciones**): para los SOS, los avisos de zonas y las solicitudes para unirse. Mientras compartes, Android muestra además una notificación fija, «Compartiendo tu ubicación».
   - **Sin restricciones de batería** (**Excluir del ahorro de batería**): si Android duerme la aplicación, tu grupo deja de verte y los avisos llegan tarde.
   - **Inicio automático** (**Abrir los ajustes del fabricante**, **Opcional**): dónde permitir que la app se inicie sola si tu móvil trae su propio gestor de batería o de inicio automático.
   - **Listo**: pulsa **Terminar**. Puedes volver a la guía cuando quieras desde el menú.
4. Crea un grupo o únete a uno desde **Grupos**.

### Flujo normal
- **Crear un grupo e invitar**: en **Grupos**, **Crear grupo**, escribe el nombre (por ejemplo, Familia) y pulsa **Crear**. Entra en el grupo y pulsa **Invitar**: la otra persona escanea el QR o escribe el código. Cuando lo use, te llegará su solicitud y la apruebas con **Aprobar**.
- **Unirte a un grupo**: en **Grupos**, **Unirse con un código** (8 letras y números) o **Escanear QR**. Tu solicitud queda en **Mis solicitudes** hasta que un administrador la apruebe; entonces el grupo aparece en **Mis grupos** y en el mapa.
- **Ver a los tuyos**: en **Mapa** eliges el grupo y ves a cada miembro. Para ver por dónde ha ido alguien, **Historial**.
- **Pedir ayuda**: botón rojo **SOS** del mapa.

### Menú lateral
- **Mapa**, **Grupos**, **Zonas**, **Historial**: las pantallas principales.
- **Guía de configuración**: vuelve a la guía de permisos y batería.
- **Ajustes**, **Novedades** y **Acerca de**.
- Al pie aparece la versión instalada.

### Pantalla Mapa
- **Elige un grupo**: el selector de arriba, si estás en más de uno.
- **Actualizar** (flechas, arriba a la derecha): vuelve a pedir las posiciones.
- Al abrir, el mapa se centra en tu posición: tu propia marca (tu foto o tu inicial con tu nombre) va donde está tu móvil ahora. El botón de centrar (**Ver a todos**) encuadra a todos los miembros del grupo.
- El mapa ocupa toda la pantalla. **Buscar a una persona** (la lupa, abajo a la derecha, encima del SOS) abre la lista del grupo: cada miembro con su avatar o sus iniciales y «hace N min · batería N %», **En pausa** (con la hora de fin, si la tiene) o **Sin posición todavía**. Al elegir a alguien la lista se cierra y el mapa se centra en esa persona; desde la lista también puedes **Ver a todos**. Atrás, o tocar fuera, la cierra.
- **SOS** (botón rojo): «Enviar un SOS a tus grupos».
- Avisos que pueden aparecer arriba, con su botón:
  - «No se está compartiendo tu ubicación…», «Tu grupo solo te ve con la app abierta…» o «El servicio que comparte tu ubicación está parado…»: **Abrir la guía** y completa el paso pendiente.
  - «Este móvil no tiene la clave de este grupo…»: la clave llega sola en cuanto otro miembro abra la aplicación; **Pedir la clave otra vez** la vuelve a pedir.
  - «Hay un SOS pendiente de enviar»: se reintenta solo en cuanto haya conexión.
- Sin grupos: **Aún no tienes grupos** con el botón **Ir a Grupos**.

### Pantalla SOS
1. Empieza la cuenta atrás, **Enviando SOS en** 3 segundos. «Pulsa Cancelar si ha sido sin querer»: **Cancelar** no envía nada.
2. **A estos grupos**: vienen todos marcados; desmarca los que no quieras avisar. Se envía con tu ubicación aunque estés en pausa.
3. Al terminar, **SOS enviado** («Se ha avisado a los miembros de N grupo(s) con tu posición»). Sin conexión queda **Pendiente, reintentando** y se envía solo cuando vuelva, aunque cierres la aplicación. Sin GPS en ese momento, se envía tu última posición conocida con su hora.
4. **Volver al mapa**.
- Los demás reciben «SOS de <nombre>» y, al tocarlo, le ven en el mapa.

### Pantalla Grupos
- **Mis grupos**: cada grupo con tu papel (**Administrador** o **Miembro**); tócalo para abrirlo.
- **Mis solicitudes**: las que esperan aprobación («Solicitud pendiente de aprobación por un administrador»).
- **Crear grupo** (+): pide el nombre, que solo ven los miembros y viaja cifrado.
- **Unirse con un código**: escribe el código de 8 caracteres que te ha dado un administrador (sin O, I, 0 ni 1) y confirma.
- **Escanear QR**: apunta la cámara al QR que enseña el administrador. Sin permiso de cámara puedes escribir el código a mano.

### Pantalla del grupo
- **Invitar** (QR, arriba): abre la pantalla **Invitar**.
- **Solicitudes pendientes** (solo administradores): «Pidió entrar hace…», con **Aprobar** o **Rechazar**.
- **Miembros**: cada uno con su papel. Un administrador puede **Hacer administrador**, **Quitar administrador** y **Expulsar** (la persona deja de ver el grupo al momento y el grupo deja de ver su posición). Siempre queda al menos un administrador.
- **Mi ubicación en este grupo**: **Compartiendo** o en pausa. **Pausar** ofrece **1 hora**, **8 horas**, **Hasta mañana a las 8:00**, **Hasta que la reanude** y **Hasta una hora…**; **Reanudar** la quita. Durante la pausa este grupo no recibe ni ve tus posiciones; tus otros grupos siguen igual.
- **Abandonar el grupo**: dejas de verlo y el grupo deja de verte; para volver hará falta una invitación nueva. Si eres el único miembro, el grupo se borra; si eres el único administrador y hay más miembros, antes tienes que nombrar a otro.

### Pantalla Invitar
- El QR y el código del grupo, con **Caduca en** y los minutos que le quedan (cada código sirve 5 minutos). Al caducar: «Caducado: pide otro código».
- **Otro código**: genera uno nuevo. **Compartir el código**: lo manda por la aplicación que elijas. **Cerrar**.
- Cuando alguien lo use, te llegará «Solicitud para unirse» para aprobarla o rechazarla.

### Pantalla Zonas (Zonas del grupo)
- Elige el grupo arriba. Cada zona muestra su nombre y **Radio: N m**, con **Editar** y **Borrar** (se borra para todo el grupo, con sus avisos).
- **Nueva zona** (+): escribe el **Nombre de la zona** (por ejemplo, Casa), toca el mapa para poner el centro y ajusta el radio con la barra (de 50 a 2000 m). **Guardar**.
- **Avisos** (campana): abre la pantalla de avisos del grupo.

### Pantalla Avisos
- Para cada persona del grupo y cada zona, dos interruptores: **Al entrar** y **Al salir**. Solo te avisará de lo que actives aquí (por ejemplo, «Ana ha llegado a Casa»).

### Pantalla Historial
- Elige el grupo, la **Persona** y el día (se guardan los últimos 30 días; lo anterior se borra solo).
- El recorrido se dibuja en el mapa con **Inicio** (verde), **Fin** (rojo) y cada **Parada** (una estancia de 10 minutos o más en el mismo sitio; al tocarla, «Parada de … a …»). Debajo, «N posiciones, de … a …».
- Si está activado el ajuste, verás «Ajustando el recorrido a calles y caminos…» y luego si se ha ajustado entero, en parte o si va en línea recta porque no se ha podido consultar el mapa.
- **Borrar mi historial** (papelera, arriba): borra tus recorridos en todos tus grupos, también los que aún no se han enviado. Tus grupos seguirán viendo tu última posición en el mapa. No se puede deshacer.

### Pantalla Ajustes
- **Idioma**: **El del sistema**, **Español** o **English**. El cambio se aplica al momento.
- **Mi nombre y avatar**: cambia tu nombre visible y tu foto (**Elegir foto**, **Quitar foto**); se actualiza en todos tus grupos.
- **Cuenta**: dice si está vinculada o no. **Vincular Google** o **Vincular Microsoft** para poder recuperarla. **Recuperar mi cuenta en este móvil**: en un móvil nuevo y sin grupos, trae tus grupos, zonas e historial; el móvil anterior deja de compartir tu ubicación.
- **Permisos y batería**: el estado de la ubicación (siempre / solo con la app abierta / sin permiso, y si está compartiendo o parado), de las notificaciones y de la batería, con **Abrir la guía**.
- **Historial**: **Ajustar recorridos a calles y caminos** (activado por defecto; apagado, no se consulta ningún mapa de calles) y **Borrar mi historial**.
- Accesos a **Novedades** y **Acerca de**.

### Pantalla Novedades
- Los cambios de cada versión, con la instalada marcada.

### Pantalla Acerca de
- Nombre, versión y autor (Socratic).
- **Contacto**: **Escribir al autor**.
- **Idioma**, **Novedades** (**Ver las novedades**), **Privacidad** con **Política de privacidad**, **Licencia** (MIT) y las bibliotecas de terceros, y **Aviso legal**: «Family Together no sustituye a los servicios de emergencia. En una emergencia, llama al 112.»

## Preguntas frecuentes
**¿Por qué no está en Google Play?**
Todavía no se ha publicado allí. El APK de cada versión está en las releases de GitHub; se instala a mano permitiendo las aplicaciones de origen desconocido.

**Mi grupo no me ve con la aplicación cerrada.**
Abre la **Guía de configuración** y completa los pasos pendientes: la ubicación tiene que estar en «Permitir todo el tiempo», las notificaciones activadas y la aplicación fuera del ahorro de batería. En algunas marcas también hace falta el **Inicio automático**. En **Ajustes › Permisos y batería** ves cómo está cada cosa.

**Estoy en casa y mi posición no cambia o sale aproximada.**
Dentro de casa el GPS llega mal y la ubicación por red es imprecisa. Esas lecturas solo actualizan tu última posición en el mapa; no entran en el historial ni disparan avisos de zonas. Con el móvil quieto tampoco se añade nada al historial.

**Veo el grupo como «Grupo sin clave en este móvil».**
El móvil aún no tiene la clave para descifrar ese grupo (pasa al unirte o al recuperar la cuenta). Llega sola en cuanto otro miembro abre la aplicación; puedes pulsar **Pedir la clave otra vez**.

**El código de invitación no funciona.**
Cada código caduca a los 5 minutos. Pide al administrador **Otro código**. Son 8 letras y números, sin O, I, 0 ni 1.

**He cambiado de móvil. ¿Pierdo mis grupos?**
Si vinculaste Google o Microsoft en el anterior, no: en el nuevo, antes de unirte a nada, ve a **Ajustes › Cuenta › Recuperar mi cuenta en este móvil** con la misma cuenta. Sin vincular, reinstalar es empezar como un usuario nuevo.

**El historial va en línea recta en lugar de por las calles.**
El ajuste necesita conexión para consultar el mapa de calles de la zona. Si no se ha podido, el recorrido se dibuja recto con un aviso. Comprueba también que **Ajustar recorridos a calles y caminos** está activado en **Ajustes**.

**¿Puede alguien borrar mi historial o ver lo que hago en pausa?**
No. Solo tú puedes borrar tu historial, y lo que ocurre mientras un grupo está en pausa nunca llega a ese grupo. El SOS sí se envía aunque estés en pausa.

**¿Sustituye a llamar a emergencias?**
No. La posición depende del GPS, de la red y de la batería, y puede llegar tarde o no llegar. En una emergencia, llama al 112.

## Privacidad
No hay cuenta ni contraseña: tu usuario es anónimo y solo si quieres vinculas Google o Microsoft para recuperarlo en otro móvil. Tu posición, la hora y la batería se comparten con tus grupos cuando te mueves, y tus coordenadas, tu nombre, tu avatar y los nombres de los grupos y las zonas se cifran de extremo a extremo en el móvil con la clave del grupo: el servidor guarda datos que no puede leer. El historial se borra solo a los 30 días y puedes borrar el tuyo cuando quieras. Los avisos los transporta el servicio de notificaciones de Google, con solo identificadores, nunca tu posición ni texto legible. El recorrido ajustado a las calles se calcula en el móvil: al servicio de mapas solo se le piden zonas fijas del mapa, nunca el recorrido, y se puede apagar. Sin anuncios, sin analítica y sin rastreadores. Los terceros que intervienen están en la política de privacidad.
