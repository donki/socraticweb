# sOC Phone Mirror
- slug: phonemirror
- plataformas: Windows 10 (versión 2004) o posterior y Windows 11, 64 bits; maneja móviles y tablets Android 5.0 o superior
- lema: La pantalla de tu móvil Android en Windows, para manejarlo con ratón y teclado.
- github: https://github.com/donki/PhoneMirror
- tiendas:
  - Microsoft Store (en revisión): https://apps.microsoft.com/detail/9N0S24Z4DLS1 — identificador de producto 9N0S24Z4DLS1 (fuente: nota del proyecto sobre el rechazo del 2026-09-15). Rechazada el 2026-09-15 y reenviada el 2026-09-22 a la espera de certificación (fuente: D:\sOCProjects\TAREAS.md, «Josep lo reenvió a la Store el 2026-09-22 (queda esperar la certificación)»). Comprobado el 2026-09-25: el catálogo público de la Store todavía responde «producto no encontrado» para ese identificador, así que el enlace aún no funciona. El README.md del repositorio enlaza de momento a la búsqueda por nombre.
  - Google Play: no aplica (solo Windows).
- descarga_alternativa: https://github.com/donki/PhoneMirror/releases (última: v2026.9.21.0; ejecutable y paquete MSIX)

## Descripción

sOC Phone Mirror enseña la pantalla de tu móvil o tablet Android en una ventana de Windows y te deja manejarlo desde el PC: tocas con el ratón, escribes con el teclado del ordenador, copias y pegas entre los dos y arrastras ficheros para pasarlos al móvil. Es muy útil para contestar mensajes con un teclado de verdad, hacer demostraciones, grabar tutoriales o simplemente no tener que coger el teléfono mientras trabajas.

Conectas el móvil por USB y se conecta solo. La ventana se adapta al móvil: si abres un juego o un vídeo en apaisado, la ventana se pone apaisada con él. Si tienes varios móviles, puedes abrir una ventana para cada uno, y también conectarte por Wi-Fi sin cable.

Todo pasa por el cable (o por tu red local) entre el PC y el móvil: no hay cuenta, ni servidor, ni nada sale a internet. Lo que hace falta para hablar con el móvil ya va incluido en la aplicación, así que no tienes que instalar nada más. Es software libre, sin anuncios ni rastreadores.

## Funciones principales

- Pantalla del móvil en tiempo real en una ventana de Windows que se adapta a vertical y apaisado.
- Tocar, deslizar y desplazar con el ratón; botón derecho para atrás y central para inicio.
- Escribir con el teclado del PC, con tu distribución de teclado.
- Portapapeles compartido en los dos sentidos (Ctrl+C / Ctrl+V y botones).
- Botones de atrás, inicio, recientes, notificaciones, encender/apagar pantalla, girar, volumen y silencio.
- Captura de la pantalla del móvil con un clic.
- Arrastrar un APK para instalarlo, o cualquier fichero para copiarlo a la carpeta Download del móvil.
- Conexión por Wi-Fi, incluida la vinculación con código de Android 11 o posterior.
- Vive en la bandeja del sistema, puede arrancar con Windows y abrirse sola al enchufar un móvil.
- Una ventana por móvil si tienes varios conectados.

## Guía de uso (soporte)

### Instalación

1. Descarga la última versión desde https://github.com/donki/PhoneMirror/releases. Puedes elegir:
   - El ejecutable `sOCPhoneMirror.exe`: basta con él solo, no necesita instalación.
   - El paquete `.msix`, que se instala como cualquier aplicación de Windows.
2. Cuando esté publicada, también podrás instalarla desde la Microsoft Store.

La herramienta que usa para comunicarse con Android (adb) ya va incluida: la primera vez que se abre la prepara sola. Con el ejecutable suelto, además, queda disponible para las consolas nuevas de Windows («adb añadido a tu PATH…»).

### Preparar el móvil (una sola vez)

1. En el móvil, activa las Opciones de desarrollador (normalmente, tocando siete veces «Número de compilación» en Ajustes › Información del teléfono).
2. En Ajustes › Opciones de desarrollador, activa **Depuración USB**.
3. En **Xiaomi, Redmi y POCO** activa además **«Depuración USB (ajustes de seguridad)»**: sin eso se ve la pantalla pero el ratón y el teclado no la controlan.
4. Conecta el móvil por USB. El móvil pregunta si confías en este PC: acepta en su pantalla.

### Primera puesta en marcha y flujo normal

1. Abre sOC Phone Mirror con el móvil enchufado: se conecta solo y aparece la pantalla del móvil.
2. Si no aparece, la ventana te indica qué pasa: «No hay ningún móvil conectado…» o «El móvil pregunta si confía en este PC. Acepta en su pantalla.»
3. Maneja el móvil con el ratón y el teclado (ver «Manejo con ratón y teclado»).
4. Cerrar o minimizar la ventana la esconde en la bandeja del sistema; para salir del todo, usa «Salir» en el menú del icono.

No hay que crear cuenta ni iniciar sesión.

### Ventana principal: barra superior

De izquierda a derecha:

**Conexión**
- Selector de móvil: lista los móviles detectados (modelo y número de serie).
- Volver a buscar móviles.
- Conectar por Wi-Fi: abre la ventana de conexión por red (ver más abajo).
- Conectar: empieza a espejar el móvil elegido.
- Desconectar: corta la sesión. Tras desconectar a mano, no vuelve a conectarse sola con ese móvil hasta que lo desenchufes y lo vuelvas a enchufar.

**Botones del móvil**
- Atrás.
- Inicio.
- Aplicaciones recientes.
- Notificaciones: despliega la cortina de notificaciones.
- Encender / apagar la pantalla.
- Girar.
- Bajar volumen y Subir volumen.
- Silenciar / activar el sonido del móvil (es el sonido del teléfono; esta ventana no reproduce audio).

**Herramientas**
- Guardar una captura: guarda la pantalla del móvil en la carpeta Imágenes\Phone Mirror del PC («Captura guardada en…»).
- Copiar el portapapeles del móvil al PC.
- Pegar el portapapeles del PC en el móvil.
- Siempre encima: mantiene la ventana por encima de las demás (interruptor).
- Abrir al conectar un móvil (arranca con Windows, en la bandeja): interruptor. Activado, la aplicación arranca con Windows escondida en la bandeja y se abre sola al enchufar un móvil («La aplicación arrancará con Windows y se abrirá al enchufar un móvil.»). Desactivado, ya no arranca con Windows.
- Español / English: cambia el idioma al momento.
- Acerca de.

### Zona central

- Con sesión: la pantalla del móvil, que se adapta a la ventana.
- Sin sesión: un aviso con lo que falta y el recordatorio de cómo activar la depuración USB.
- Si por algún motivo no se encontrara adb, aparecen dos botones: «Descargar las platform-tools de Android de Google (unos 7 MB)» y «Buscar adb.exe en este PC…» (la ruta elegida se recuerda).

### Barra inferior

- Estado de la conexión: «Conectando con…», el móvil conectado y su resolución, «Desconectado» o «Se ha cortado la conexión: …».
- Cuadros por segundo.

### Manejo con ratón y teclado

| Gesto | Qué hace |
|---|---|
| Clic y arrastrar | Tocar y deslizar |
| Botón derecho | Atrás (o encender la pantalla si está apagada) |
| Botón central | Inicio |
| Rueda / Mayús+rueda | Desplazar en vertical / en horizontal |
| Teclear | Escribe en el móvil (letras como texto; flechas, Intro, Retroceso, Supr, Esc, Tab, Inicio, Fin, RePág, AvPág y teclas multimedia como teclas) |
| Ctrl+V | Pega el portapapeles del PC en el móvil |
| Ctrl+C | Copia lo seleccionado en el móvil y lo trae al PC |
| Arrastrar un .apk a la ventana | Lo instala en el móvil |
| Arrastrar otro fichero | Lo copia a la carpeta Download del móvil |

### Ventana Conectar por Wi-Fi

«El móvil tiene que tener activada la depuración por red y estar en la misma red que este PC.»

- Dirección del móvil (IP o IP:puerto), con botón Conectar. Las direcciones que han funcionado se recuerdan (cada una con «Olvidar esta dirección») y se vuelven a conectar solas al arrancar si el móvil está encendido y en la misma red.
- **La primera vez en Android 11 o posterior**: en el móvil ve a Opciones de desarrollador › Depuración inalámbrica › Vincular dispositivo con un código. El móvil enseña una dirección con su puerto y un código de seis cifras:
  - Dirección de vinculación (IP:puerto).
  - Código de vinculación.
  - Vincular. Después conecta arriba con la dirección que sale en «Depuración inalámbrica» (es otro puerto).
- Otra forma: con el móvil enchufado una vez por cable, ejecuta «adb tcpip 5555» y aceptará conexiones a su IP hasta que se reinicie.

### Bandeja del sistema

- La aplicación vive en la bandeja: cerrar o minimizar la ventana la esconde en vez de salir. La primera vez aparece un aviso: «Sigue aquí, en el área de iconos: clic para abrir, o Salir desde el menú.»
- Clic en el icono: abre la ventana. Botón derecho: Abrir y Salir.
- Sin móvil, el icono indica «sOC Phone Mirror · esperando un móvil».

### Varias ventanas y varios móviles

- Si abres la aplicación cuando ya hay una abierta, pregunta: «Enseñar la ventana elegida» (de una lista con el móvil de cada una) o «Ventana nueva». Así puedes tener una ventana para el teléfono y otra para la tablet.
- El título de cada ventana lleva el móvil conectado.

### Acerca de

Contacto («Escribir al autor»), idioma, privacidad, licencia MIT y aviso legal.

## Preguntas frecuentes

**Veo la pantalla del móvil pero el ratón y el teclado no hacen nada (Xiaomi, Redmi, POCO).**
En esas marcas hay que activar, además de la Depuración USB, la opción «Depuración USB (ajustes de seguridad)» en las Opciones de desarrollador. Sin ella la pantalla se ve pero no se puede controlar.

**Dice «No hay ningún móvil conectado».**
Comprueba que el cable transmite datos (no solo carga), que la Depuración USB está activada y pulsa «Volver a buscar móviles». Prueba otro puerto USB si sigue sin aparecer.

**Dice «El móvil pregunta si confía en este PC».**
Desbloquea el móvil y acepta el aviso de depuración USB en su pantalla (puedes marcar que recuerde este equipo).

**He cerrado la ventana y la aplicación sigue en marcha.**
Es a propósito: vive en la bandeja del sistema para conectarse al enchufar el móvil. Para salir del todo, botón derecho en su icono (en Windows 11 puede estar en la flecha ^ de iconos ocultos) y «Salir».

**No se conecta sola al enchufar el móvil.**
Si pulsaste Desconectar, no vuelve a conectarse con ese móvil hasta que lo desenchufes y lo enchufes otra vez. Para que además se abra sola al arrancar Windows, activa el botón «Abrir al conectar un móvil».

**No consigo conectar por Wi-Fi.**
El móvil y el PC tienen que estar en la misma red. En Android 11 o posterior, primero vincula con el código de seis cifras y después conecta con la dirección que aparece en «Depuración inalámbrica», que usa un puerto distinto al de la vinculación.

**Se oye el sonido en el móvil y no en el PC.**
Es normal: la aplicación no transmite el audio. Los botones de volumen y silencio controlan el sonido del propio móvil.

**Arrastro un fichero y no sé dónde ha ido.**
Los APK se instalan; cualquier otro fichero se copia a la carpeta Download del móvil. La barra inferior confirma «… copiado a Download».

## Privacidad

Todo pasa entre tu PC y el móvil por el cable USB (o por tu red local si usas Wi-Fi): la pantalla se muestra en el PC y los toques van directos al móvil. No se guarda nada salvo las capturas que tú hagas (en Imágenes\Phone Mirror) y el texto que copies, y nada sale a internet. Sin cuenta, sin anuncios, sin rastreadores y sin analítica.
