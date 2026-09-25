# Hiker
- slug: hiker
- plataformas: Android
- lema: Graba tus rutas con GPS, ajústalas a los caminos y vuelve a seguirlas.
- github: https://github.com/donki/Hiker
- tiendas:
  - Google Play (prueba cerrada): https://play.google.com/store/apps/details?id=com.socratic.hiker — solo en la pista de prueba cerrada (alpha 2026091202 publicada; la 2026091902 sigue en borrador), sin producción; la página pública de Play aún no existe (devuelve 404 a 2026-09-25) (fuente: D:\sOCProjects\05-PENDIENTE-Hiker.md; paquete en Hiker.csproj y GooglePlayConsole\Hiker\ficha.md)
  - Microsoft Store: no publicada (solo Android; no hay ficha ni ID de Store en el proyecto)
- descarga_alternativa: https://github.com/donki/Hiker/releases (última: v2026.09.19.02, APK)

## Descripción
Hiker es tu compañero de senderismo: graba la ruta que recorres sobre un mapa a pantalla completa, la guarda en tu móvil y te ayuda a seguirla la próxima vez, diciéndote cuánto te queda y avisándote si te sales del camino.

La grabación sigue con la pantalla apagada y en el bolsillo, y si Android cierra la aplicación en mitad de una ruta larga, al volver a abrirla te ofrece recuperar lo grabado. Al terminar, Hiker puede pegar tu recorrido a los caminos del mapa y sacarlo de dentro de los edificios, enseñándote las dos versiones para que elijas cuál guardar.

De cada ruta tienes una ficha con distancia, desniveles, altitudes, tiempos, velocidades y el perfil de desnivel dibujado. Puedes importar rutas en formato GPX. Tus rutas se quedan en tu móvil: no hay cuentas, ni anuncios, ni rastreadores.

## Funciones principales
- Mapa a pantalla completa con tu posición en tiempo real, precisión y velocidad.
- Grabación de rutas que sigue con la pantalla apagada, con notificación mientras graba.
- Recuperación de la grabación si Android cierra la aplicación a mitad de ruta.
- Ajuste de la ruta a los caminos del mapa, comparando en el mapa la versión grabada y la ajustada antes de guardar.
- Seguimiento de una ruta guardada: distancia al trazado, lo que queda y aviso en rojo si te alejas más de 50 m.
- Modo Rumbo: el mapa gira con la brújula para que lo que tienes delante quede arriba.
- Ficha de cada ruta con distancia, desnivel positivo y negativo, altitudes, duración, tiempo en movimiento, ritmo, velocidades y perfil de desnivel.
- Importación de rutas en formato GPX.
- En castellano e inglés, con modo claro y oscuro.

## Guía de uso (soporte)

### Primera puesta en marcha
1. Abre Hiker. Android te pedirá permiso de **ubicación mientras usas la aplicación**: acéptalo con ubicación precisa, porque es lo que sitúa tu posición en el mapa y graba la ruta. La aplicación no necesita la ubicación «todo el tiempo»: cuando grabas, lo hace con una notificación visible.
2. Cuando empieces a grabar, Android puede pedirte permiso de **notificaciones**: es la notificación «Grabando la ruta», que permite que la grabación siga con la pantalla apagada.
3. La primera vez, Hiker te pregunta por la **Optimización de batería** («...permite que la aplicación funcione sin restricciones de batería. ¿Deseas modificar esta configuración ahora?») y por la **Ejecución en segundo plano**. Responde **Sí** y quita las restricciones en los ajustes que se abren: así el sistema no corta la grabación en rutas largas. Cada pregunta sale una sola vez.
4. Espera a que el mapa se centre en tu posición («Obteniendo ubicación...»). Al aire libre y tras unos segundos la precisión mejora.

### Flujo normal
- **Grabar**: pulsa el botón rojo de grabar del mapa (o **Grabar** en el menú), camina, y al terminar pulsa **Parar**. Hiker te pregunta si quieres guardar la ruta, te ofrece ajustarla al mapa y te pide un nombre.
- **Seguir una ruta**: en **Rutas**, toca el botón de ubicación de la ruta; se dibuja en el mapa y aparece la barra de seguimiento.
- **Consultar una ruta**: en **Rutas**, toca el botón de información para ver su ficha.

### Menú lateral
- **GPS**: despliega el submenú del mapa. Junto a cada opción hay un botón de información que explica qué hace.
  - **Mapa**: muestra el mapa a pantalla completa sin iniciar ninguna grabación.
  - **Grabar**: comienza a grabar tu recorrido registrando los puntos GPS.
  - **Parar**: detiene la grabación en curso.
  - **Seguir: Sí / Seguir: No**: mantiene (o deja de mantener) el mapa centrado automáticamente en tu posición.
  - **Rumbo: Sí / Rumbo: No**: gira el mapa para que la dirección hacia la que miras apunte hacia arriba. Viene activado.
  - **Guardar**: guarda el recorrido grabado como una ruta con nombre.
  - **Borrar**: elimina del mapa el recorrido actual sin guardarlo.
- **Rutas**: tus rutas guardadas.
- **Configuración**: el idioma.
- **Acerca de**: versión, contacto, idioma, privacidad, licencia y aviso legal.
- Al pie aparece la versión instalada.

### Pantalla del mapa (GPS)
- **Cabecera de estado**: un icono con el estado (parado, grabando) y tu posición: «Lat · Lon · ±precisión en metros · velocidad en km/h».
- **Mapa**: se mueve y se amplía con los dedos; tu posición aparece como un punto y la ruta grabada o cargada como una línea.
- **Botón de ubicación**: vuelve a centrar el mapa en tu posición actual.
- **Botón de grabar** (rojo): empieza a grabar. Mientras graba aparece la barra **Grabando la ruta** con el tiempo, la distancia y los puntos registrados, y el botón **Parar**.
- **Al parar**:
  1. «Ruta grabada. Se han grabado N puntos (X km). ¿Quieres guardarla?»: **Guardar** o **Descartar** (descartar la borra del mapa).
  2. Si guardas, Hiker consulta los caminos del mapa («Ajustando la ruta… Consultando los caminos del mapa»). Si no hay conexión, avisa y guarda la ruta tal como se grabó; si ya encajaba, te lo dice y sigue.
  3. Si la ha ajustado, verás las dos versiones: en rojo la que se guardaría y en gris la otra, con el texto «En rojo: ruta ajustada — N puntos pegados a caminos y M sacados de edificios» o «En rojo: ruta grabada». El botón de **alternar** (flechas) cambia cuál está en rojo y el botón de **guardar** (disquete) se queda con la que está en rojo.
  4. Por último, **Guardar Ruta** te pide el **Nombre de la ruta** (**Guardar** / **Cancelar**) y confirma «Ruta 'nombre' guardada correctamente».
- **Barra de seguimiento** (al cargar una ruta desde Rutas): «Siguiendo la ruta» con la longitud total; en marcha muestra «En la ruta: a X del trazado» y «Quedan X», con un punto verde, o «Te has salido: a X de la ruta», con el punto en rojo, si te alejas más de 50 m. El botón **Parar** de la barra deja de seguirla.
- **Grabación interrumpida**: si Android cerró la aplicación mientras grababas, al volver a abrirla aparece «Quedó una grabación sin guardar con N puntos. ¿La recuperas?»: **Recuperar** o **Descartar**.

### Pantalla Rutas (Rutas Guardadas)
- Cada ruta muestra su nombre, **Distancia** en km y **Fecha**, con tres botones:
  - **Información**: abre la ficha de la ruta.
  - **Ubicación**: la dibuja en el mapa y empieza a seguirla.
  - **Papelera**: la borra tras preguntar «¿Eliminar la ruta 'nombre'?».
- **Cargar GPX** (icono de carpeta): elige un fichero .gpx del móvil y lo importa como ruta («Ruta 'nombre' importada.»). Si el fichero no tiene puntos, avisa.
- **Actualizar** (icono de flechas): vuelve a leer la lista.

### Pantalla Ficha de ruta
- Nombre y fecha de la ruta.
- **Distancia**, **Desnivel positivo**, **Desnivel negativo**, **Altitud máxima**, **Altitud mínima**, **Diferencia de altitud**, **Duración**, **En movimiento**, **Ritmo** (minutos por km), **Velocidad media**, **Velocidad máxima** y **Puntos**. Los desniveles se suavizan para no sumar el ruido del GPS.
- **Perfil de desnivel**: gráfico de la altitud (m) según la distancia recorrida (km). Si la ruta no tiene altitud: «Esta ruta no lleva altitud.»
- **Ver en el mapa**: abre la ruta en el mapa para seguirla.

### Pantalla Configuración
- **Idioma**: **Español** o **English** («Selecciona tu idioma preferido»). Se guarda solo al pulsarlo y la interfaz cambia al momento. Al instalarla usa el castellano si el móvil está en castellano y el inglés en otro caso.
- No hay más ajustes: el GPS se configura solo.

### Pantalla Acerca de
- Nombre, **Versión** y autor (Socratic).
- **Contacto**: botón con la dirección de correo; abre tu aplicación de correo.
- **Idioma**: **Español** / **English**.
- **Privacidad**, **Licencia** (MIT) y **Aviso Legal** («Uso bajo su propio riesgo»).

## Preguntas frecuentes
**La ruta sale a trozos o se corta con la pantalla apagada.**
Quita a Hiker las restricciones de batería y de segundo plano (Ajustes de Android › Aplicaciones › Hiker › Batería › Sin restricciones; en Xiaomi, también «Inicio automático»). Deja activado el permiso de notificaciones: la notificación «Grabando la ruta» es lo que permite a Android seguir dando posiciones con la pantalla apagada.

**Android cerró la aplicación en mitad de la ruta. ¿He perdido lo grabado?**
No: cada punto se guarda en el móvil al momento. Al volver a abrir Hiker verás «Grabación interrumpida» y podrás pulsar **Recuperar**.

**El mapa no se centra en mi posición o sale en otro sitio.**
Comprueba que la ubicación del móvil está activada y que Hiker tiene permiso de ubicación precisa. Espera unos segundos al aire libre y pulsa el botón de ubicación. En bosques densos, cañones o entre edificios altos la señal GPS es peor.

**Al guardar dice «No se ha podido consultar el mapa».**
El ajuste a los caminos necesita conexión. Sin ella, la ruta se guarda igualmente tal como se grabó.

**El ajuste ha movido mi ruta a un camino por el que no fui.**
Antes de guardar puedes pulsar el botón de alternar para ver la ruta grabada en rojo y guardar esa en lugar de la ajustada.

**¿Puedo cargar rutas hechas en otra aplicación o en la web?**
Sí, si están en formato GPX: en **Rutas** pulsa **Cargar GPX** y elige el fichero. Para crear o editar rutas en el ordenador puedes usar herramientas web gratuitas como GPX Studio y luego pasar el fichero al móvil.

**El mapa gira solo y me mareo.**
Es el modo Rumbo. Desactívalo en el menú lateral › **GPS** › **Rumbo: No**.

**La ficha dice «Esta ruta no lleva altitud».**
Algunos ficheros GPX importados no incluyen la altitud de cada punto; sin ella no se pueden calcular los desniveles ni el perfil.

## Privacidad
Tus rutas y tu posición se guardan solo en tu móvil; no hay cuentas, ni anuncios, ni rastreadores, y Hiker no envía tus recorridos a ningún servidor. Para dibujar el mapa se descargan la biblioteca del mapa y las teselas de OpenFreeMap de la zona que ves y, solo al ajustar una ruta a los caminos, se consulta a OpenStreetMap qué caminos y edificios hay por la zona por la que pasa (sin guardar nada allí); además, al arrancar se comprueba si hay una versión nueva.
