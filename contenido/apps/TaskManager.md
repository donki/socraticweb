# Task Manager
- slug: taskmanager
- plataformas: Android (móvil y tablet), Windows
- lema: Tus tareas en el móvil y en el ordenador, con la misma cuenta.
- github: https://github.com/donki/TaskManager
- tiendas:
  - Google Play (prueba cerrada): https://play.google.com/store/apps/details?id=com.socratic.taskmanager — solo en la pista de prueba cerrada (alpha); la página pública da 404 hasta que pase a producción, lo que exige antes 12 probadores durante 14 días (fuentes: D:\sOCProjects\06-PENDIENTE-TaskManager.md, store/google-play/ficha.md, README.md; comprobado el 2026-09-25 que la URL pública devuelve 404).
  - Microsoft Store (publicada): https://apps.microsoft.com/detail/9PHJK2391727 (enlace de Josep, 2026-09-25; ficha pública comprobada)
- descarga_alternativa: https://github.com/donki/TaskManager/releases (APK, EXE y MSIX de cada versión; última: v2026.09.23.00)

## Descripción

Task Manager es una lista de tareas que de verdad está en todos tus dispositivos: escribes una tarea en el móvil y aparece en el ordenador, y al revés. Está pensada para el día a día: se abre, se apunta lo que hay que hacer y se cierra. Cada tarea puede llevar su lista, sus etiquetas, fechas, repetición, pasos, enlaces y ficheros adjuntos, y lo que no puede esperar se ancla arriba del todo.

Además de tus listas privadas, puedes crear grupos para compartir listas con la familia, los compañeros de piso o un equipo. Para invitar a alguien basta con enseñarle un código QR: lo escanea con la propia aplicación y ya está dentro. Cuando completas una tarea, la aplicación lo celebra con una pequeña animación.

Entras con una cuenta que ya tienes, de Google o de Microsoft, y lo que escribes se cifra en tu dispositivo antes de salir. Si prefieres no usar cuenta, puedes seguir sin ella y las tareas se quedan solo en ese dispositivo. En Windows vive junto al reloj, con un panel rápido que se abre con un atajo de teclado.

## Funciones principales

- Las mismas tareas en el móvil y en el PC, sincronizadas con tu cuenta de Google o de Microsoft.
- Listas propias y grupos compartidos con otras personas, con invitación por código QR.
- Cada tarea con lista, notas, etiquetas, fecha de planificación, fecha de finalización, repetición, pasos, enlaces y ficheros adjuntos (también imágenes pegadas del portapapeles).
- Vistas de «Mis tareas», «Mis listas», «Tablero» (pendientes, en curso y hechas) y «Calendario».
- Filtros por estado y por fechas, fila de etiquetas y buscador que mira en título, notas, etiquetas, pasos y adjuntos.
- Selección múltiple para marcar hechas, anclar, etiquetar, mover o borrar varias tareas de golpe.
- Repeticiones diarias, semanales en los días que elijas, mensuales o anuales.
- Recordatorio diario de lo pendiente y aviso el día de vencimiento, con opción de repetir el aviso.
- En Windows: icono en la bandeja con el número de pendientes y panel rápido con atajo (por defecto Ctrl+Alt+T).
- Texto cifrado antes de salir del dispositivo; modo claro y oscuro; castellano e inglés.

## Guía de uso (soporte)

### Primera puesta en marcha

1. Instala la aplicación (Android desde Google Play o el APK de GitHub; Windows con el EXE o el MSIX de GitHub).
2. Se abre la pantalla **Tu cuenta** con tres opciones:
   - **Continuar con Google** / **Continuar con Microsoft** (en Windows: **Entrar con Google** / **Entrar con Microsoft**): se abre la página de tu proveedor, inicias sesión allí y vuelves a la aplicación. El nombre de tu cuenta será tu nombre en la aplicación. La cuenta es lo que permite que el móvil y el PC compartan las mismas listas y lo que hace posibles los grupos.
   - **Seguir sin cuenta**: las tareas se quedan solo en ese dispositivo, sin sincronizar y sin grupos. Si desinstalas la aplicación, se pierden. Puedes entrar con una cuenta más adelante.
3. Permisos que pide Android, y solo cuando hacen falta:
   - **Notificaciones**: para el aviso diario de lo que queda pendiente y el de las tareas que vencen. Se pide al activar «Avisarme de las tareas pendientes». Sin él, la aplicación avisa de que Android no permite mostrar avisos.
   - **Cámara**: solo para leer el código QR de una invitación a un grupo; se pide al pulsar el botón de escanear. Sin ella, el código y la clave se pueden escribir a mano.
4. Cada cuenta tiene sus propias listas en el mismo dispositivo: cambiar de Google a Microsoft cambia lo que ves, pero no borra nada de la otra.

### Flujo normal

Escribe la tarea en la caja de arriba y pulsa el botón de añadir (o Intro). Tócala para abrir su ficha y completar lo que necesite (fechas, etiquetas, pasos...). Márcala como hecha con la casilla de la fila. Usa los filtros y las etiquetas para ver lo que te interesa en cada momento.

### Menú lateral (Android)

Entradas: **Mis tareas**, **Calendario**, **Mis listas**, **Tablero**, **Mis grupos**, **Ajustes** y **Acerca de**.

### Mis tareas

- **Añadir una tarea a hoy**: caja para escribir una tarea nueva y botón de añadir. La tarea entra en la primera lista y se abre para completarla.
- **Buscar**: busca en título, notas, etiquetas, pasos y adjuntos. El aspa limpia la búsqueda.
- **Filtros**: **Pendientes**, **Ancladas**, **Acabadas**, **Todas**, **Caducadas**, **Fecha de inicio anterior a hoy**, **Fecha de inicio hoy o posterior**, **Fecha de caducidad anterior a hoy**, **Fecha de caducidad hoy o posterior**.
- **Fila de etiquetas**: **Todas las etiquetas**, **Sin etiqueta** y una por cada etiqueta con algo pendiente. A la izquierda, fijo, el botón que abre la pantalla **Etiquetas**. Pulsación larga sobre una etiqueta (botón derecho en Windows): **Borrar etiqueta**.
- En cada fila: casilla de hecha/pendiente; tocar la tarea abre su ficha. Mantén pulsada una tarea para arrastrarla y cambiarla de orden.
- **Actualizar** (arriba): vuelve a sincronizar.
- **Seleccionar varias**: activa casillas en cada fila y una barra con **Marcar hechas**, **Devolver a pendientes**, **Anclar arriba** / **Desanclar**, **Poner etiqueta** (elige una existente u «O escribe una nueva»), **Mover a una lista** y **Borrar** (pide confirmación; si alguna es repetitiva, pregunta **Solo las seleccionadas** o **Las series enteras**). El aspa o **Quitar la selección** sale del modo.
- Pie: «Se muestran X de Y pendientes · Z % hechas».

### Etiquetas

Todas las etiquetas en uso, también las que solo llevan tareas hechas, con «N sin acabar · N en total». La papelera de cada una la quita de todas sus tareas; si la llevan tareas sin acabar, pregunta antes.

### Ficha de la tarea

- **Anclada**: la deja arriba del todo. **En curso**: la pasa a la columna del medio del tablero. En Windows además **Hecha**.
- **Qué hay que hacer** (título, obligatorio: si falta avisa «La tarea necesita un título»).
- **Lista**: a qué lista pertenece.
- **Notas**.
- **Etiquetas**: separadas por comas (por ejemplo «casa, urgente, trabajo»). En Windows, botón **Añadir etiqueta**.
- **Fecha de finalización** y **Planificada para** (el día en que piensas hacerla, que no tiene por qué ser el del plazo).
- **Repetición**: **No se repite**, **Cada día**, **Cada semana** (eligiendo días L M X J V S D), **Cada mes** (**Día del mes** o «El mismo día»), **Cada año** (**Mes** y día). Una tarea que se repite necesita fecha de planificación y de finalización: al guardar se crean todas las repeticiones de ese intervalo (hasta 500).
- **Enlaces y ficheros**: **Añadir enlace** (pega la dirección), **Añadir fichero**, **Pegar del portapapeles** (imagen o ficheros copiados; en Windows también Ctrl+V). Tocar un adjunto lo abre (doble clic en Windows); **Quitar** lo elimina. Hay un tamaño máximo por fichero.
- **Pasos**: escribe «Lo que dice el paso» y **Añadir paso**. Cada paso se marca, se edita (**Editar paso**), se borra (**Borrar paso**) y se arrastra para reordenar.
- Arriba: **Guardar** (marca) y **Borrar tarea** (papelera). Si la tarea se repite, pregunta **Solo esta vuelta** o **Toda la serie**.

### Calendario

El mes con las tareas en el día para el que están planificadas. Flechas **Mes anterior** / **Mes siguiente**; en Windows, **Volver a hoy**. Al elegir un día, la caja **Nueva tarea para este día** crea una tarea planificada para ese día. Tocar una tarea la abre (doble clic en Windows).

### Mis listas

Lista de tus listas con cuántas tareas quedan. El botón **+** crea una **Nueva lista**; la papelera la borra (si tiene tareas pregunta **¿Y sus tareas?**: **Moverlas** a otra lista o **Borrarlas también**). Al entrar en una lista: **Añadir una tarea**, buscador, casilla de hecha en cada tarea, botón para incluirla o quitarla de «Mi Día», y el lápiz de arriba para **Cambiar el nombre**.

### Tablero

Tres columnas: **Pendientes**, **En curso** y **Hechas**, con los mismos filtros y etiquetas que «Mis tareas». **Nueva tarea en el tablero** crea una tarea en pendientes (en Windows, el botón **Añadir en curso** la crea directamente en curso). En Windows se arrastra una tarjeta a otra columna para cambiarle el estado; en Android, se toca la tarjeta para cambiar el estado desde su ficha y la pulsación larga sirve para reordenar.

### Mis grupos

- Botones de arriba: **Nuevo grupo** (+), **Unirse a un grupo** (llave), **Escanear el QR** y **Actualizar**.
- **Nuevo grupo**: nombre (por ejemplo «Familia, Piso compartido, Proyecto...») y **Clave compartida** de al menos 6 caracteres. Se crea con una primera lista «General».
- **Unirse a un grupo**: **Código del grupo (6 caracteres)** y la clave; o **Escanear el QR** de la invitación. En Windows el QR se puede leer **De una imagen**, **Del portapapeles** o **De la pantalla**.
- En cada grupo: **Invitar a alguien** (pone una clave nueva: la invitación anterior deja de valer, a quien ya está no le afecta) y enseña el QR con **Compartir** y **Copiar código y clave** (en Windows también **Enviar por correo** y **Enviar por WhatsApp**); **Nueva lista del grupo**; y papelera, que pregunta **Salir: los demás miembros lo conservan** o **Borrarlo para todos, con sus listas y tareas** (solo quien lo creó puede borrarlo).

### Ajustes (Android)

- **Tu cuenta**: foto, nombre y correo de la cuenta y **Cerrar sesión** (sin cuenta vuelve a la pantalla de entrada; para usar otra cuenta, cierra sesión y elígela después). Sin cuenta se ve «Sin cuenta · Solo en este dispositivo».
- **Recordatorios**:
  - **Avisarme de lo que queda pendiente** (interruptor).
  - **Repetir el aviso cada**: **No repetir**, **15 minutos**, **30 minutos**, **1 hora**, **2 horas**, **4 horas**.
  - **Hora del aviso diario**: hora del resumen diario. Hay un aviso al día con lo que queda en Mi Día y otro por cada tarea con fecha de finalización (a las 9:00 de ese día).
- **Celebración**: **Vibración al completar** y **Sonido al completar** (el sonido llegará con los temas desbloqueables).
- **Identidad**: nombre visible, «Cómo te ven en los grupos».

### Acerca de (Android y Windows)

Versión, **Contacto** (**Escribir al autor**), **También disponible en** (enlace a la versión de Windows desde Android y a Google Play y a GitHub desde Windows), **Idioma** (**Español** / **English**; se aplica al momento), **Privacidad**, **Licencia** y **Aviso legal**.

### Windows: bandeja y panel rápido

- La aplicación vive junto al reloj; el icono lleva un globo rojo con las tareas pendientes de Mi Día. Clic izquierdo o el atajo (por defecto **Ctrl+Alt+T**) abre el **panel rápido** sobre cualquier ventana, incluso un juego a pantalla completa. Menú del icono: **Abrir panel rápido**, **Salir**.
- En el panel: escribir + Intro añade la tarea (**Añadir tarea (Intro)**), buscador, **Actualizar**, y botones a **Mis tareas**, **Calendario**, **Ajustes**, **Acerca de** y **Abrir la ventana principal**.
- Ventana principal con pestañas **Mis tareas**, **Mis listas**, **Tablero**, **Calendario** y **Grupos**.

### Ajustes (Windows)

- **Tu cuenta**: cuenta actual y **Cerrar sesión**. Cada cuenta tiene sus propias listas.
- **Idioma**: Español, English o idioma del sistema.
- **Atajo global (por ejemplo Ctrl+Alt+T)**: combinación que abre el panel rápido. Si otra aplicación ya lo usa, se avisa y se mantiene el anterior.
- **Iniciar con Windows y quedarse en la bandeja**.
- **Avisarme de las tareas pendientes** y **Repetir el aviso cada**.
- **Sonido al completar una tarea**.
- **Nombre visible**.
- Botones **Guardar** y **Cancelar**.

## Preguntas frecuentes

**No veo en el móvil las tareas que he creado en el PC.** Comprueba que en los dos has entrado con la misma cuenta (Google o Microsoft): cada cuenta tiene sus propias listas y «Seguir sin cuenta» no sincroniza. Pulsa **Actualizar**.

**Una tarea que se repite no me deja guardar.** Las tareas repetitivas necesitan **Planificada para** y **Fecha de finalización**: son el intervalo en el que se crean las repeticiones. Una serie se corta en 500 tareas; cuando llegues al final, pon una fecha de finalización nueva.

**He borrado una tarea repetitiva y siguen saliendo las demás.** Al borrar, elige **Toda la serie** en lugar de **Solo esta vuelta**.

**No me llegan los avisos.** Activa **Avisarme de lo que queda pendiente** en Ajustes y concede el permiso de notificaciones cuando Android lo pida (o en los ajustes de Android de la aplicación).

**El atajo de teclado no abre el panel en Windows.** Si otra aplicación ya usa esa combinación, Task Manager lo avisa. Cambia el atajo en Ajustes.

**No puedo borrar un grupo.** Solo quien lo creó puede borrarlo para todos; el resto puede **Salir** del grupo.

**He invitado a alguien y dice que la invitación no vale.** Cada **Invitación nueva** cambia la clave y anula la anterior. Envía la última.

**Quiero cambiar de cuenta.** Ajustes › **Cerrar sesión** y entra con la otra. No se pierde nada: al volver a la anterior, sus listas siguen ahí.

## Privacidad

Las tareas se guardan en tu dispositivo y, si entras con cuenta, se sincronizan con el servidor de la aplicación para que sean las mismas en todos tus dispositivos; el texto que escribes se cifra en tu dispositivo antes de subir y en el servidor no es legible. Sin cuenta, nada sale del dispositivo. No hay anuncios, rastreadores ni analítica, y la aplicación nunca ve tu contraseña de Google o Microsoft.
