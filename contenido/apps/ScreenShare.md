# sOC ScreenShare
- slug: screenshare
- plataformas: Windows 10 (versión 2004) o posterior y Windows 11, 64 bits
- lema: Graba una pantalla, todas o una ventana con su sonido en un MP4 ligero, listo para compartir.
- github: https://github.com/donki/ScreenShare
- tiendas:
  - Microsoft Store: próximamente.
  - Google Play: no aplica (solo Windows).
- descarga_alternativa: https://github.com/donki/ScreenShare/releases (última: v2026.10.13.0; un ejecutable autocontenido)

## Descripción

sOC ScreenShare graba lo que pasa en tu pantalla en un vídeo MP4 que se puede mandar sin más: por defecto sale ligero (hasta 1080p, unos 30 MB por minuto) y se ve en cualquier móvil, navegador o programa de vídeo. Eliges qué grabar —una pantalla, todas juntas o una sola ventana—, qué sonido entra y en qué carpeta se guarda, y pulsas grabar.

Al grabar una ventana se graba solo su sonido: el de esa aplicación, no las notificaciones ni la música que suene en el resto del equipo. Si grabas una pantalla puedes elegir todo lo que suena por unos altavoces o auriculares concretos, o solo una aplicación, y sumar el micrófono si quieres hablar por encima. Cada origen tiene su volumen.

Puede empezar sola: le dices qué aplicación —y, si quieres, qué ventana de esa aplicación, por su título— y en cuanto se abre la graba con su sonido, y al cerrarse la guarda. Con dos atajos de teclado empiezas y paras sin buscar la ventana. Al terminar, la reproduces, la ves en su carpeta o copias el fichero para pegarlo en una conversación o un correo. Es software libre, sin cuenta, sin anuncios y sin rastreadores, y no se conecta a nada.

## Funciones principales

- Grabar una pantalla, todas las pantallas tal como están colocadas o una ventana; si la ventana cambia de tamaño, el vídeo no se deforma.
- Sonido de la ventana grabada, solo el suyo (también el de sus procesos auxiliares, como en los navegadores).
- Sonido de un dispositivo de salida o de una sola aplicación al grabar una pantalla, y micrófono aparte, con volumen y medidor para cada uno.
- MP4 H.264 o H.265 con audio AAC, con el codificador de la tarjeta gráfica cuando lo hay.
- Calidad «Óptima para compartir», «Alta» o personalizada: resolución, imágenes por segundo, tasa de bits, códec y audio, con los MB por minuto antes de grabar.
- Atajos de teclado globales para empezar y parar (Ctrl+Mayús+F9 y Ctrl+Mayús+F10, configurables), también con la ventana escondida.
- Grabación automática cuando se abre una aplicación o una ventana concreta de ella, y parada al cerrarse.
- Icono junto al reloj con punto rojo mientras graba; pausar y seguir.
- Al terminar: reproducir, abrir la carpeta o copiar el fichero.
- Línea de órdenes para grabar desde scripts.

## Guía de uso (soporte)

### Instalación

1. Descarga la última versión desde la página de versiones de GitHub (https://github.com/donki/ScreenShare/releases): `sOCScreenShare.exe`.
2. Ábrelo con doble clic. No hay que instalar nada. Si Windows avisa de que el editor es desconocido, pulsa «Más información» y «Ejecutar de todas formas».

Requisitos: Windows 10 (versión 2004) o posterior, o Windows 11, de 64 bits. Para grabar solo el sonido de una aplicación hace falta Windows 11 o Windows 10 compilación 20348 o posterior; en versiones anteriores la aplicación lo dice y no graba otro sonido en su lugar.

### Primera puesta en marcha

La primera vez se abre la «Guía de configuración», con cuatro pasos (Atrás / Siguiente abajo): dónde van los vídeos, el sonido del equipo (con un botón a la configuración de sonido de Windows), el micrófono (con un botón a su privacidad en Windows) y los atajos y la grabación automática (con Arrancar con Windows). Se vuelve a abrir cuando quieras con el botón de ayuda (?).

### Ventana principal

- **Qué grabar**: Una pantalla (pulsa la que quieres en el dibujo de tus pantallas), Todas las pantallas o Una ventana (de la lista de ventanas abiertas; una minimizada hay que restaurarla para grabarla).
- **Sonido**: con una pantalla, Sonido del equipo (Ninguno, Todo lo que suena por un dispositivo —elige cuál— o Solo una aplicación); con una ventana, Sonido de la ventana (solo el suyo). Micrófono, con su dispositivo. Cada uno con su barra de volumen.
- **Guardar**: carpeta de los vídeos (por defecto Vídeos\ScreenShare), con el botón para elegirla y el de abrirla; calidad (Óptima para compartir, Alta o Personalizada) con el botón «Calidad» al lado, y el tamaño estimado en MB por minuto.
- **Abajo**: Grabar, Pausar / Seguir y Parar, con su atajo debajo, y el tiempo grabado.
- **Arriba a la derecha**: Guía, Novedades, Español / English y Acerca de.
- **Última grabación**: al terminar sale arriba, con su tamaño y duración, y los botones Reproducir, Enseñar en la carpeta y Copiar el fichero.

### Calidad

El botón «Calidad» abre un diálogo aparte. Vídeo: resolución máxima (original, 2160p, 1440p, 1080p, 720p o 480p; nunca agranda), imágenes por segundo (15, 24, 30 o 60), tasa de bits automática o en Mbit/s, códec H.264 (se ve en todas partes) o H.265 (la mitad de tamaño, si tu equipo tiene codificador) y control de la tasa (variable, constante o calidad constante). Audio: 96, 128, 160 o 192 kbit/s, 44,1 o 48 kHz, mono o estéreo. Abajo se ve cómo saldrá el vídeo y cuántos MB ocupa por minuto.

### Grabación automática

En los ajustes, «Grabación automática»: añade una regla con la aplicación (de las abiertas o eligiendo su .exe) y, si quieres, un título de ventana (contiene o expresión regular) para grabar solo una pantalla concreta de esa aplicación, como la ventana de una reunión. Cada regla tiene Activa y Parar y guardar al cerrarse la ventana. Con la grabación automática encendida, cerrar la ventana deja ScreenShare junto al reloj, y puede arrancar con Windows. Si ya hay una grabación en marcha no empieza otra. Al empezar y al acabar sale un aviso junto al reloj.

### Atajos

Ctrl+Mayús+F9 empieza a grabar y Ctrl+Mayús+F10 para. Se cambian en los ajustes pulsando la combinación nueva; no admite las que usa Windows y avisa si otra aplicación ya tiene la misma.

## Preguntas frecuentes

**Grabo una ventana y no se oye nada.**
Solo entra el sonido de esa aplicación: si no estaba sonando, el vídeo sale sin sonido. Si tu Windows es anterior a la compilación 20348, la ventana lo avisa: ahí no se puede separar el sonido de una aplicación.

**¿Por qué no se ve mi ventana en la lista?**
Solo salen las ventanas visibles con título. Si está minimizada, restáurala; el botón de recargar actualiza la lista.

**El vídeo ocupa mucho.**
Usa «Óptima para compartir», baja la resolución o las imágenes por segundo, o elige H.265 si tu equipo lo tiene. El diálogo de Calidad enseña los MB por minuto antes de grabar.

**¿Sale la ventana de ScreenShare en el vídeo?**
No: mientras graba, sus ventanas se quedan fuera de la grabación.

**¿Se puede usar desde un script?**
Sí: `sOCScreenShare.exe --record <segundos>` con opciones para qué grabar, el sonido y la calidad; `--help` las enseña.

## Privacidad

Todo se queda en tu PC: los vídeos en la carpeta que elijas y los ajustes en tu perfil. La aplicación ve la imagen y el sonido solo mientras graba; la grabación automática mira qué ventanas se abren (nombre del programa y título) para compararlas con tus reglas y no guarda nada de eso. No se conecta a nada. Sin cuenta, sin anuncios, sin rastreadores, sin analítica.
