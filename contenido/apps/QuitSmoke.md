# QuitSmoke
- slug: quitsmoke
- plataformas: Android
- lema: Reduce el tabaco poco a poco: espacia los cigarros y ahorra dinero.
- github: https://github.com/donki/QuitSmoke
- tiendas:
  - Google Play (prueba cerrada): https://play.google.com/store/apps/details?id=com.socratic.quitsmoke — solo en la pista de prueba cerrada, sin producción; la página pública de Play aún no existe (devuelve 404 a 2026-09-25) (fuente: D:\sOCProjects\03-PENDIENTE-QuitSmoke.md; paquete en QuitSmoke.csproj y GooglePlayConsole\QuitSmoke\ficha.md)
  - Microsoft Store: no publicada (solo Android; no hay ficha ni ID de Store en el proyecto)
- descarga_alternativa: https://github.com/donki/QuitSmoke/releases

## Descripción
QuitSmoke te ayuda a fumar menos de forma gradual y realista, a tu ritmo. En vez de pedirte que lo dejes de golpe, te propone un máximo de cigarros al día y reparte ese máximo a lo largo de las horas que estás despierto, para que sepas en todo momento cuánto te queda y cuándo toca el siguiente.

Registras cada cigarro con un toque, incluso desde la notificación sin abrir la aplicación, y QuitSmoke lleva la cuenta: cuántos llevas hoy, cuánto tiempo llevas sin fumar, cuánto has gastado y cuánto has ahorrado respecto a tu máximo. Cuando te sientas preparado, bajas el máximo un cigarro y sigues avanzando.

Todo se queda en tu móvil: no hay cuentas, ni anuncios, ni rastreadores. Es software libre con licencia MIT hecho por sOCratic. QuitSmoke es una herramienta de apoyo y no sustituye el consejo de un profesional sanitario.

## Funciones principales
- Máximo diario de cigarros ajustable y botón para reducirlo de uno en uno a medida que progresas.
- Cálculo automático del tiempo que conviene esperar entre cigarros según tu horario de vigilia.
- Pantalla principal con el progreso del día, el último cigarro, el próximo recomendado y el tiempo sin fumar.
- Notificación fija con el recuento del día, la hora del siguiente cigarro y un botón «Fumar» para registrarlo sin abrir la aplicación.
- Doble confirmación cuando vas a pasarte del límite diario.
- Historial de los últimos 30 días: total de cigarros, días registrados, media diaria y reducción lograda.
- Estadísticas económicas: total gastado, total ahorrado, gasto medio al día y porcentaje de ahorro, en 14 divisas.
- Consejos de salud y motivación que cambian cada vez, en castellano o inglés.
- Ajustes que se guardan solos.

## Guía de uso (soporte)

### Primera puesta en marcha
1. Instala la aplicación y ábrela. Nada más arrancar, Android te pide permiso para **mostrar notificaciones**: acéptalo, porque es lo que permite ver el recuento del día en la barra de notificaciones y registrar cigarros desde ahí con el botón «Fumar».
2. Abre el menú lateral (las tres rayas arriba a la izquierda) y entra en **Configuración**.
3. Pon tu **Cigarros máximos por día** (lo que fumas ahora mismo es un buen punto de partida).
4. Ajusta el **Horario de vigilia**: la hora a la que te levantas y la hora a la que te acuestas. Con eso y el máximo, la aplicación calcula el tiempo entre cigarros.
5. Rellena la **Configuración de Precios** (precio de la cajetilla, cigarros por cajetilla y divisa) para que las cuentas de dinero salgan bien.
6. Si usas un móvil que cierra las aplicaciones en segundo plano (Xiaomi, Huawei, Samsung con ahorro agresivo...), pulsa **Configurar Todos los Permisos** para que la notificación no desaparezca.

No hay que pulsar ningún botón de guardar: cada ajuste se guarda al cambiarlo.

### Flujo normal
- Cada vez que fumes, pulsa **Fumar Cigarro** en la pantalla principal o **Fumar** en la notificación.
- Mira en la pantalla principal o en la notificación cuándo toca el siguiente y procura esperar hasta esa hora.
- De vez en cuando, consulta el **Histórico** para ver tu reducción y el dinero ahorrado.
- Cuando te veas cómodo con tu máximo, ve a Configuración y pulsa **Reducir Máximo (Progreso gradual)**.

### Menú lateral
- **Principal**: pantalla de inicio con el estado del día.
- **Histórico**: estadísticas de los últimos 30 días.
- **Configuración**: máximo diario, horario, precios y permisos del sistema.
- **Acerca de**: versión, contacto, idioma, privacidad, licencia y aviso legal.
- Al pie del menú aparece la versión instalada.

### Pantalla Principal
- **Consejo del día**: un consejo de salud o motivación elegido al azar, con la etiqueta **Consejo Smart**. Cambia cada vez que entras o actualizas.
- **Progreso del día**: barra de progreso con **Fumados: X/Y** (los que llevas hoy frente a tu máximo) y **Restantes**.
- **Último**: hora del último cigarro registrado.
- **Próximo**: hora recomendada para el siguiente. Si todavía no has fumado hoy, es la hora a la que te levantas; si ya has llegado al máximo, aparece «--».
- **Sin fumar**: tiempo transcurrido desde el último cigarro.
- **Fumar Cigarro**: registra un cigarro con la hora actual y muestra «Cigarro registrado correctamente». Si ya has llegado al máximo, el botón cambia a **Límite alcanzado**; al pulsarlo te pregunta «Ya has fumado N cigarros hoy. ¿Quieres continuar?» (**Sí, fumar** / **No, esperar**) y después pide una **Confirmación final** («¿Estás seguro? Esto excederá tu límite diario.», **Sí, estoy seguro** / **Cancelar**). Solo si confirmas las dos veces se registra.
- **Actualizar datos**: vuelve a leer los datos y muestra otro consejo.
- **Estadísticas del día**: **Entre cigarros** (tiempo recomendado entre uno y otro) y **Horas despierto** (según tu horario de vigilia).
- Mientras la aplicación está abierta, la pantalla no se apaga sola.

### Notificación
- Título **«QuitSmoke: X/Y hoy»** con los cigarros de hoy frente al máximo.
- Texto **«Siguiente: HH:MM»**, **«Siguiente: ahora»** si ya puedes fumar, o **«Límite diario alcanzado»**.
- Botón **Fumar**: registra un cigarro sin abrir la aplicación y actualiza la notificación al momento.

### Pantalla Histórico
Muestra «Cargando historial...» mientras calcula y después:
- **Estadísticas Generales** (últimos 30 días):
  - **Total cigarros**: cigarros registrados.
  - **Días registrados**: días en los que has fumado al menos uno.
  - **Promedio/día**: media de cigarros en esos días.
  - **Reducción lograda**: porcentaje que has fumado por debajo de tu máximo, con un resumen del tipo «Reducción lograda: X% (fumados/previstos cigarros en N días)».
- **Estadísticas Económicas**:
  - **Total gastado**: lo que te han costado los cigarros fumados.
  - **Total ahorrado**: lo que has dejado de gastar frente a fumar tu máximo cada día.
  - **Promedio/día**: gasto medio diario.
  - **% de ahorro**: lo ahorrado en relación con lo gastado.
- **Actualizar datos**: recalcula las estadísticas.

### Pantalla Configuración
Cabecera «Configuración — Preferencias y permisos». Todo se guarda solo al cambiarlo.

**Tarjetas de estado**
- **Ahorro batería**: indica si la aplicación está **Excluida del ahorro** o **Optimizada (recomendado excluir)**. Aparece «Sin verificar» hasta que pulsas «Verificar Estado de Permisos».
- **Autostart**: estado del inicio automático. Como Android no permite consultarlo, tras verificar indica «Revisar en ajustes del sistema».

**Configuración de Permisos**
- **Verificar Estado de Permisos**: actualiza las dos tarjetas de estado.
- **Configurar Todos los Permisos**: pide excluir la aplicación del ahorro de batería (o abre esa pantalla del sistema) y abre también los ajustes de inicio automático y de ejecución en segundo plano del fabricante. Al terminar avisa: «Se abrieron los ajustes del sistema. Configura batería, autoinicio y segundo plano.»
- **Batería**: solo la exclusión del ahorro de batería.
- **Autostart**: abre los ajustes de inicio automático del fabricante.
- Aviso: «Para un funcionamiento óptimo, configure todos los permisos para ejecución en segundo plano.»

**Cigarros máximos por día**
- Botones **−** y **+** a los lados de la cifra, o escribe el número directamente (mínimo 1).
- Debajo, **Tiempo entre cigarros**: el intervalo recomendado resultante (horas despierto divididas entre el máximo).

**Horario de vigilia**
- **Hora de despertar**: por defecto 07:00.
- **Hora de dormir**: por defecto 23:00. Puede ser pasada la medianoche.

**Configuración de Precios**
- **Precio de cajetilla**: por defecto 5.00.
- **Cigarros por cajetilla**: por defecto 20.
- **Divisa**: Euro, Dólar Estadounidense, Libra Esterlina, Yen Japonés, Dólar Canadiense, Dólar Australiano, Franco Suizo, Yuan Chino, Peso Mexicano, Peso Argentino, Peso Chileno, Peso Colombiano, Sol Peruano y Real Brasileño.
- Debajo, **Precio por cigarrillo**: el coste de cada cigarro calculado a partir de lo anterior.

**Reducir Máximo (Progreso gradual)**
- Baja tu máximo diario en un cigarro (nunca por debajo de 1) y lo guarda. Es el botón que usas para avanzar en tu plan.

### Pantalla Acerca de
- Nombre, **Versión** instalada y autor (Socratic).
- **Contacto**: botón con la dirección de correo; al tocarlo se abre tu aplicación de correo con un mensaje «Contacto desde QuitSmoke». Si no tienes ninguna, avisa «Cliente de correo no disponible en este dispositivo».
- **Idioma**: botones **Español** y **English**; la interfaz, los consejos y la notificación cambian al momento («Idioma actualizado»). Al instalarla, la aplicación usa el castellano si el móvil está en castellano y el inglés en cualquier otro caso.
- **Privacidad**, **Licencia** (MIT) y **Aviso Legal** («Uso bajo su propio riesgo»).

### Aviso de versión nueva
Al abrir la pantalla principal, si hay una versión más reciente aparece **Actualización disponible** («Hay una versión más reciente (X). Tienes la Y. ¿Quieres actualizar?»). **Actualizar** abre la página de descargas; **Ahora no** lo cierra.

## Preguntas frecuentes
**No me sale la notificación con el botón «Fumar».**
Comprueba que diste permiso de notificaciones (Ajustes de Android › Aplicaciones › QuitSmoke › Notificaciones). La notificación aparece al abrir la aplicación y se actualiza cada vez que registras un cigarro.

**La notificación desaparece o no se actualiza con el móvil bloqueado.**
Algunos fabricantes cierran las aplicaciones en segundo plano. En Configuración pulsa **Configurar Todos los Permisos**, excluye QuitSmoke del ahorro de batería y activa el inicio automático; luego pulsa **Verificar Estado de Permisos** para comprobarlo.

**He llegado al límite y el botón dice «Límite alcanzado». ¿Ya no puedo registrar más?**
Sí puedes: pulsa el botón y confirma dos veces. Se registra igual, porque lo importante es que la cuenta sea real; la doble pregunta solo sirve para que lo pienses.

**He cambiado un ajuste y no veo el botón de guardar.**
No hace falta: los ajustes se guardan solos al cambiar cada campo o selector.

**El tiempo entre cigarros me parece raro.**
Se calcula dividiendo las horas que estás despierto (de la hora de despertar a la de dormir) entre tu máximo diario. Revisa tu Horario de vigilia en Configuración.

**El dinero ahorrado sale a cero.**
El ahorro se mide frente a fumar tu máximo cada día; si fumas justo tu máximo, no hay ahorro. Revisa también que el precio de la cajetilla y los cigarros por cajetilla estén bien puestos.

**La aplicación sale en inglés.**
Si tu móvil no está en castellano, la aplicación arranca en inglés. Cámbialo en **Acerca de › Idioma › Español**.

**La pantalla no se apaga mientras la uso.**
Es intencionado mientras QuitSmoke está en primer plano; se apaga con normalidad al salir de la aplicación.

## Privacidad
QuitSmoke guarda tu registro de cigarros, tu horario y tus precios solo en tu móvil; no hay cuentas, ni anuncios, ni rastreadores, y nada de eso sale del dispositivo. La única conexión a Internet es una comprobación de si hay una versión nueva al abrir la aplicación, que no envía ningún dato tuyo.
