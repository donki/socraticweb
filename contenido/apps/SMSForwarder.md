# SMS Forwarder
- slug: smsforwarder
- plataformas: Android
- lema: Tu app de SMS que, además, reenvía los mensajes que tú elijas a otro número.
- github: https://github.com/donki/SMSForwarder
- tiendas:
  - Google Play (producción): https://play.google.com/store/apps/details?id=com.socratic.smsforwarder — en la tienda aparece como «SMS Forwarder: Mensajes»; en producción está la 2026.09.22.2 y las 2026.09.23.8 / 2026.09.24.x están enviadas a revisión (fuente: D:\sOCProjects\TAREAS.md, entradas 2026.09.22.2 y 2026.09.24.0/.1 y apartado «SMS Forwarder no tiene fichero propio»; título comprobado en la página pública de Play el 2026-09-25; paquete en SMSForwarder.csproj)
  - Microsoft Store: no publicada (solo Android; no hay ficha ni ID de Store en el proyecto)
- descarga_alternativa: https://github.com/donki/SMSForwarder/releases

## Descripción
SMS Forwarder es una aplicación de mensajes SMS completa que puedes poner como la aplicación de mensajes de tu móvil: recibes, lees, escribes, respondes y borras tus SMS desde ella, con aviso en la barra de notificaciones cada vez que llega uno nuevo.

Su punto fuerte es el reenvío automático, que es opcional: puedes hacer que los SMS que te llegan se reenvíen solos a uno o varios números. Es perfecto para no perderte los mensajes de una segunda línea o de una SIM que no llevas encima, o para que los códigos del banco le lleguen también a otra persona. Cada número de destino decide qué recibe: todos los SMS, solo los de ciertos remitentes, solo los que contengan ciertas palabras, o una combinación.

Todo ocurre en tu teléfono: no hay cuentas, ni servidores, ni anuncios, y la aplicación ni siquiera tiene acceso a Internet. Los reenvíos salen como SMS normales por tu operador.

## Funciones principales
- Aplicación de SMS predeterminada: buzón de entrada y de enviados, notificación de cada SMS nuevo y respuesta rápida por SMS a llamadas entrantes.
- Redactar, responder y reenviar SMS a mano, eligiendo el destinatario del selector de contactos del sistema.
- Detalle de cada mensaje con el texto completo, enlaces que se pueden pulsar y botones para copiar el número o el texto.
- Borrado de mensajes uno a uno o en bloque con selección múltiple.
- Reenvío automático a uno o varios números de destino.
- Filtros por destino: todos los SMS, solo de ciertos remitentes y/o solo los que contengan ciertas palabras o frases (sin distinguir mayúsculas ni acentos).
- Configurar el reenvío de un remitente en dos toques desde el propio mensaje.
- Protección contra bucles de reenvío.
- Pantalla de diagnósticos con el estado de los permisos, ayuda para la batería y el inicio automático, y registro de actividad.
- En castellano e inglés.

## Guía de uso (soporte)

### Primera puesta en marcha
1. Abre la aplicación. Lo primero que verás es la pregunta de Android para **usar SMS Forwarder como aplicación de SMS predeterminada**. Acéptala: solo la aplicación predeterminada puede recibir los SMS, mostrarlos, borrarlos, marcarlos como leídos y reenviarlos. Siendo la predeterminada, Android le concede ya los permisos de SMS sin volver a preguntar.
2. Después te pedirá permiso para **mostrar notificaciones**, que sirve para avisarte de cada SMS que llega.
3. Si no eres la aplicación predeterminada, se te pedirán por separado los permisos de **recibir SMS** y **enviar SMS**.
4. Si quieres usar el reenvío automático, abre el menú lateral, entra en **Configuración** y añade al menos un número de destino.
5. Si tu móvil cierra las aplicaciones en segundo plano (Xiaomi, Huawei, Oppo, algunos Samsung...), entra en **Diagnósticos** y pulsa **Configurar todos los permisos**, o bien **Batería** y **Autostart**, para que el reenvío siga funcionando con la pantalla apagada y tras reiniciar.

La aplicación no pide acceso a tu agenda: cuando eliges un contacto se abre el selector del sistema, que solo le pasa el número que escoges.

### Flujo normal
- Los SMS llegan al buzón de **Mensajes** y ves una notificación con el remitente y el texto; tócala para abrir la aplicación.
- Si hay números de destino configurados, cada SMS recibido se reenvía solo a los destinos cuyas condiciones cumpla, con el formato «[SMSForwarder] De: remitente» seguido del texto.
- Para escribir un SMS, pulsa **Nuevo mensaje**; para contestar o reenviar uno concreto, tócalo en el buzón y usa los botones del detalle.

### Menú lateral
- **Mensajes**: el buzón (pantalla de inicio).
- **Configuración**: idioma y números de destino del reenvío.
- **Diagnósticos**: permisos, batería, inicio automático y registro de actividad.
- **Acerca de**: versión, contacto, idioma, privacidad, licencia y aviso legal.
- Al pie aparece la versión instalada.

### Pantalla Mensajes
- **Aviso «Hazla tu app de mensajes»**: aparece solo si SMS Forwarder no es tu aplicación de SMS predeterminada. Explica que sin serlo no puede escribir, borrar ni marcar mensajes como leídos. El botón **Usar como predeterminada** abre la pregunta de Android.
- **Entrada** / **Enviados**: pestañas para ver los SMS recibidos o los que has enviado.
- **Seleccionar** (icono de casilla): entra en el modo de selección múltiple.
- **Actualizar** (icono de flechas): vuelve a cargar la lista.
- **Lista de mensajes**: cada fila muestra el remitente o destinatario, la fecha corta (la hora si es de hoy, el día si no) y el principio del texto. Tócala para abrir el **detalle**; si el mensaje estaba sin leer, queda marcado como leído.
- **Papelera** en cada fila: borra ese mensaje del teléfono tras preguntar «¿Eliminar este mensaje del teléfono?» (**Sí** / **Cancelar**).
- **Nuevo mensaje**: abre la pantalla de redacción.
- Si no hay nada: «No hay mensajes» con la indicación «Los SMS que recibas aparecerán aquí.» (o «Los SMS que envíes aparecerán aquí.» en Enviados).

**Modo de selección múltiple**
- Cada fila enseña una casilla; tocar la fila la marca o desmarca.
- En el pie: botón para **marcar o desmarcar todos**, **Eliminar (n)** para borrar los marcados (pregunta «¿Eliminar n mensajes del teléfono?») y **Cancelar** (icono de aspa) para salir del modo.
- El botón de atrás del móvil sale del modo de selección en vez de cerrar la aplicación.
- Si alguno no se puede borrar, se borran los demás y te avisa: «Se han borrado X de Y.»

### Pantalla de detalle del mensaje (Mensaje)
- **Remitente** con un botón para **copiar el número** («El número está en el portapapeles.»).
- **Texto completo** del SMS. Los enlaces web se pueden pulsar y se abren en el navegador.
- **Copiar el texto**: copia el mensaje entero al portapapeles.
- **Reenviar**: pregunta «¿A quién le reenvías este mensaje?», ofreciendo tus números de destino configurados u **Otro destinatario…**, y abre la redacción con el texto ya puesto precedido de «De: remitente», para que lo retoques antes de enviarlo.
- **Responder**: abre la redacción con el remitente ya puesto como destinatario.
- **Reenvío automático**: deja configurado a quién se le reenvían a partir de ahora los SMS de este remitente:
  1. «¿A qué número reenviar los SMS de X?»: elige uno de tus destinos o **Otro número…** (hay que escribirlo; debe tener entre 7 y 15 dígitos).
  2. «¿Qué se le manda a Y?»: **Todos los SMS de X** o **Solo los que contengan una palabra…** (escribes la palabra o frase; no distingue mayúsculas ni acentos).
  3. Si ese destino recibía todos tus SMS, te avisa de que a partir de ahora solo recibirá los que cumplan la condición.
  4. Termina con una confirmación del tipo «Y recibirá los SMS de X» o «... que contengan “palabra”».

### Pantalla Nuevo mensaje
- **Para**: número de teléfono (por ejemplo +34 600 123 456) y botón de **contactos** para elegirlo con el selector del sistema.
- **Mensaje**: el texto, con un contador de caracteres sobre 160 (lo que cabe en un SMS).
- **Enviar**: envía el SMS («Mensaje enviado»). Avisa si el número no es válido («Introduce un número de teléfono válido (7-15 dígitos).»), si el texto está vacío o si falta el permiso de SMS.

### Pantalla Configuración
Cabecera «Configuración — Configura los números donde reenviar SMS».
- **Idioma**: botones **Español** y **English**; el activo aparece resaltado y la interfaz cambia al momento. Al instalarla usa el castellano si tu móvil está en castellano y el inglés en otro caso.
- **Campo de número** («Ej: +34 600 123 456») y botón **Agregar número**: añade un destino escrito a mano. Si no tiene entre 7 y 15 dígitos avisa «Número no válido»; si ya está, «Número duplicado».
- **Contactos**: abre el selector de contactos del sistema y añade el número elegido («Número agregado»).
- **Números configurados**: la lista de destinos. Debajo de cada número se resume qué recibe («Le llegan todos los SMS», o «Solo de N remitente(s) · con N palabra(s) o frase(s)»). Si está vacía: «No hay números configurados» y el reenvío queda desactivado.
  - Toca un número para abrir **Qué SMS recibe**.
  - **Papelera** junto a cada número: lo borra tras preguntar «¿Eliminar este número?» (**Sí, eliminar** / **Cancelar**).
- **Información**: recordatorio de que los SMS recibidos se reenvían a estos números, de que puedes añadirlos a mano o desde contactos, de que los permisos avanzados están en Diagnósticos y de que se borran con la papelera.

### Pantalla Qué SMS recibe (de cada número de destino)
Arriba aparece el número. Todo se guarda al momento, sin botón de guardar.
- **Todos los SMS** (interruptor): encendido, a este número le llega todo. Apagado, solo le llegan los SMS que cumplan las condiciones de abajo. Volver a encenderlo borra los remitentes y las palabras.
- **Solo de estos remitentes**: añade teléfonos escribiéndolos y pulsando **Añadir**, o con el botón de **contactos**. Vacío significa «de cualquiera»; con varios, basta con que el SMS venga de uno. El número se compara por sus últimos 9 dígitos, así que da igual que llegue con prefijo de país o sin él. Cada remitente tiene su botón para quitarlo.
- **Que contenga estas palabras o frases** («Ej: código, factura, pedido enviado»): añade palabras o frases con **Añadir**. Vacío significa «diga lo que diga»; con varias, basta con que aparezca una; no distingue mayúsculas ni acentos. Cada una tiene su botón para quitarla.
- Si rellenas las dos listas, el SMS tiene que cumplir las dos: venir de uno de esos remitentes **y** contener una de esas palabras.
- Si intentas añadir algo repetido: «Eso ya está en la lista.»

### Pantalla Diagnósticos
Cabecera «Diagnósticos — Monitoreo y estado del sistema».
- **Permisos**: estado de «Recibir SMS» y «Enviar SMS» (aparece «Granted» si está concedido y «Denied» si no).
- **Números**: cuántos destinos tienes configurados («N números configurados»).
- **Configuración de Permisos**:
  - **Verificar estado de permisos**: vuelve a comprobar los permisos.
  - **Configurar todos los permisos**: pide los permisos que falten y los ajustes de segundo plano; al terminar dice si todo quedó bien o si hay que revisar algo a mano.
  - **Batería**: comprueba si la aplicación está excluida del ahorro de batería. Si no lo está, te lo explica y ofrece abrir el ajuste del sistema.
  - **Autostart**: abre los ajustes de inicio automático del fabricante; busca «SMS Forwarder» y actívalo para que funcione tras reiniciar.
  - Aviso: configurar todos los permisos asegura que pueda recibir y reenviar SMS incluso en segundo plano.
- **Herramientas de Diagnóstico** › **Actualizar estado**: refresca los permisos, el número de destinos y el registro.
- **Registro de actividad**: lo último que ha hecho la aplicación (reenvíos, errores, números añadidos...). **Limpiar registro** lo vacía.

### Pantalla Acerca de
- Nombre, **Versión** y autor (Socratic).
- **Contacto**: botón con la dirección de correo; al tocarlo abre tu aplicación de correo.
- **Idioma**: **Español** / **English**, igual que en Configuración.
- **Privacidad**, **Licencia** (MIT) y **Aviso Legal** («Uso bajo su propio riesgo»).

## Preguntas frecuentes
**Los SMS no se reenvían.**
Comprueba en este orden: que SMS Forwarder sea tu aplicación de SMS predeterminada (si no, en Mensajes verás el aviso con el botón **Usar como predeterminada**); que haya algún número en **Configuración › Números configurados**; que el SMS cumpla las condiciones de ese destino (toca el número para verlas); y que en **Diagnósticos** los permisos salgan concedidos y la aplicación esté excluida del ahorro de batería y con inicio automático. El **Registro de actividad** te dice si el mensaje se reenvió o por qué no.

**Deja de reenviar con la pantalla apagada o después de reiniciar.**
Es el ahorro de batería del fabricante. En **Diagnósticos** pulsa **Batería** y **Autostart** (o **Configurar todos los permisos**) y activa lo que te indique.

**No puedo borrar mensajes ni se marcan como leídos.**
Android solo deja hacerlo a la aplicación de SMS predeterminada. Pulsa **Usar como predeterminada** en la pantalla Mensajes.

**El SMS reenviado llega recortado.**
El reenvío automático va en un único SMS de 160 caracteres, con la cabecera «[SMSForwarder] De: remitente»; si el texto original no cabe, se corta y termina en «...». Para mandar un mensaje largo entero, ábrelo y usa **Reenviar**, que te deja enviarlo completo.

**Un mensaje no se reenvía a un número que también me escribe.**
Es la protección contra bucles: no se reenvían los SMS que llegan desde uno de tus números de destino ni los que ya parecen un reenvío (empiezan por «[SMSForwarder]», «De:», «Reenviado:» y similares). Así se evita que dos teléfonos se reenvíen mensajes sin fin.

**¿Cuesta dinero el reenvío?**
Cada reenvío es un SMS normal que sale de tu línea, así que tiene el coste que tu operador aplique a los SMS.

**Al escribir un número me dice que no es válido.**
Tiene que tener entre 7 y 15 dígitos. Puedes ponerlo con o sin prefijo de país y con espacios.

**He deslizado un mensaje o un número para borrarlo y no pasa nada.**
Ya no se borra deslizando: usa el botón de papelera de cada fila, o el modo de selección múltiple para borrar varios mensajes a la vez.

## Privacidad
SMS Forwarder lee y envía SMS únicamente en tu teléfono; la aplicación no tiene permiso de acceso a Internet, no hay cuentas ni servidores, y sOCratic nunca recibe copia de tus mensajes. Tus números de destino y preferencias se guardan solo en el dispositivo; los únicos datos que salen de él son los SMS reenviados, que van por tu operador a los números que tú configures.
