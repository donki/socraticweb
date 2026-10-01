# sOC AutoTask
- slug: autotask
- publicar: no (repositorio privado hasta que Josep lo dé por terminado y probado, 2026-10-01)
- plataformas: Windows 10 (versión 2004) o posterior y Windows 11, 64 bits
- lema: Graba lo que haces con el ratón y el teclado y deja que se repita solo.
- github: https://github.com/donki/AutoTask
- tiendas:
  - Microsoft Store: aún no (ficha preparada, sin enviar).
  - Google Play: no aplica (solo Windows).
- descarga_alternativa: https://github.com/donki/AutoTask/releases (última: v2026.10.01.0; ejecutable autocontenido y paquete MSIX)

## Descripción

sOC AutoTask es un grabador de macros para Windows. Pulsas Grabar, haces una vez la tarea que te aburre repetir —rellenar un formulario, ordenar unas ventanas, pulsar los mismos botones—, pulsas Parar, y a partir de ahí AutoTask la repite por ti: igual que la hiciste, más rápido o en bucle hasta que la pares.

La ventana es una barra pequeña que no estorba, y todo se maneja también con dos atajos de teclado que funcionan desde cualquier programa. Si una reproducción se desmadra, una tecla de emergencia la para al momento y suelta todas las teclas. Puedes guardar tus grabaciones, retocarlas en un editor de eventos y hasta convertirlas en un pequeño programa .exe que las reproduce en cualquier PC sin instalar nada.

No usa internet, no tiene cuenta ni anuncios, y es software libre.

## Funciones principales

- Graba movimientos y clics del ratón (los cinco botones), la rueda y el teclado, en cualquier programa.
- Atajos globales: Ctrl+Alt+Mayús+R para grabar y Ctrl+Alt+Mayús+P para reproducir, configurables.
- Parada de emergencia con Pausa, Bloq Despl o manteniendo Esc.
- Velocidad de 0,5× a 100× o la que elijas; repetir una vez, N veces o sin fin, con pausa entre vueltas.
- Guarda y abre grabaciones (.soctask), con recientes y arrastrar y soltar.
- Convierte una grabación en un .exe autónomo.
- Editor de eventos: borrar, recortar, simplificar movimientos, cambiar o insertar esperas, deshacer.
- Varios monitores y pantallas escaladas.
- Siempre encima, junto al reloj al minimizar, claro u oscuro, español e inglés.

## Guía de uso (soporte)

### Instalación

1. Descarga la última versión de https://github.com/donki/AutoTask/releases: el ejecutable `sOCAutoTask.exe` (no necesita instalación) o el paquete `.msix`.
2. Abre `sOCAutoTask.exe`. Si Windows avisa de que el editor es desconocido, pulsa «Más información» y «Ejecutar de todas formas».

Modo portátil: si pones junto al exe un fichero vacío llamado `portable.ini`, los ajustes se guardan en esa misma carpeta (por ejemplo, en un pendrive).

### Primera puesta en marcha

La primera vez se abre la **Guía de configuración**, paso a paso: atajos globales, parada de emergencia, lo que se graba, abrir grabaciones con doble clic, programas de administrador y una prueba. Cada paso dice si está hecho, pendiente u opcional, y tiene un botón que lo hace. Después se abre desde el menú **Más › Guía de configuración**.

### Flujo normal

1. Pulsa **Grabar** (o Ctrl+Alt+Mayús+R). La ventana dice «Grabando» con el tiempo y los eventos.
2. Haz la tarea con el ratón y el teclado.
3. Pulsa **Parar** (o Ctrl+Alt+Mayús+R otra vez). El atajo no queda grabado.
4. Pulsa **Reproducir** (o Ctrl+Alt+Mayús+P). Para pararla antes de tiempo, el mismo atajo, el botón o la parada de emergencia.
5. **Guardar** para conservarla como fichero `.soctask`.

### Ventana principal

- **Abrir**: una grabación `.soctask`, un `.rec` de otras utilidades de macros (experimental) o un exe hecho con AutoTask. También se puede arrastrar el fichero a la ventana.
- **Guardar**: en formato `.soctask`.
- **Grabar / Parar** y **Reproducir / Parar**.
- **Compilar**: crea un `.exe` que reproduce la grabación al abrirlo.
- **Editar**: abre el editor de eventos.
- **Ajustes**: velocidad, repeticiones, atajos, parada de emergencia, ventana, idioma y ficheros.
- **Más**: recientes, Guardar como, Importar .rec, abrir la carpeta de datos, guía, novedades, reiniciar como administrador, Acerca de y Salir.
- Debajo, el estado (grabando, reproduciendo con el tiempo que queda, terminado…) y la grabación cargada: nombre, eventos, duración, velocidad y repeticiones. Un asterisco indica cambios sin guardar.

### Ajustes

- **Reproducción** (se guarda con la grabación): velocidad (0,5×, 1×, 2×, 4×, 10×, 100× o personalizada de 0,1 a 1000), repetir una vez / este número de veces / sin fin, pausa entre repeticiones (segundos) y cuenta atrás antes de empezar (0 a 10 s).
- **Atajos y parada de emergencia**: haz clic en la casilla y pulsa la combinación (necesita Ctrl, Alt, Mayús o Win y otra tecla). Emergencia: Pausa/Inter, Bloq Despl y Esc mantenida durante los segundos que elijas.
- **Qué se graba**: el teclado (se puede quitar para grabar solo el ratón) y los movimientos del ratón.
- **Ventana**: siempre encima, texto bajo los iconos, al minimizar al área de notificación, tema (el de Windows, claro u oscuro) e idioma.
- **Ficheros**: abrir los `.soctask` con AutoTask con doble clic (solo para tu usuario).

### Editor de eventos

Lista con número, instante, espera, tipo y detalle de cada evento. Botones: **Borrar** (Supr), recortar **Inicio** y **Final**, **Simplificar** los movimientos del ratón (con tolerancia en píxeles, o dejando solo el último movimiento antes de cada clic), **Espera** de los elegidos, **Escalar** las esperas (porcentaje), **Insertar** una espera y **Deshacer** (Ctrl+Z). Nada cambia hasta que pulsas Aplicar.

### Compilar a .exe

Elige nombre y carpeta. El exe reproduce la grabación con su velocidad, repeticiones y cuenta atrás, y se para con las mismas teclas de emergencia. No necesita AutoTask ni instalar nada.

## Preguntas frecuentes

**El antivirus ha bloqueado el exe que he compilado.**
Algunos antivirus desconfían de los programas nuevos, sin firma, que mueven el ratón y el teclado. El exe es seguro: no usa internet, no escribe en el disco ni se instala, y solo repite lo que grabaste. Puedes añadirlo a las excepciones de tu antivirus.

**No hace nada en un programa concreto.**
Si ese programa se ejecuta como administrador, Windows no deja que otro programa normal le envíe teclas ni clics. AutoTask lo detecta y te ofrece reiniciarse como administrador (también en Más › Reiniciar como administrador). Algunos juegos no aceptan teclas ni clics simulados.

**Los clics caen en otro sitio.**
La reproducción repite las posiciones exactas de la pantalla: si las ventanas se han movido o has cambiado de monitor o de resolución, los clics caen donde estaban al grabar. Deja las ventanas igual que al grabar.

**¿Graba mis contraseñas?**
Graba todo lo que tecleas mientras está grabando, contraseñas incluidas, y queda en el fichero o en el exe. No grabes contraseñas, o quita «Grabar el teclado» en Ajustes.

**El atajo no funciona.**
Otro programa puede estar usando la misma combinación: AutoTask lo avisa y la guía lo marca como pendiente. Elige otra en Ajustes.

**¿Cómo paro una reproducción sin fin?**
Con el mismo atajo de reproducir, el botón Parar, o la parada de emergencia: Pausa, Bloq Despl o mantener Esc un segundo.

## Privacidad

sOC AutoTask no usa la red y no recoge ningún dato. Lo que grabas se queda en tu PC y solo se guarda donde tú decidas. Los ajustes y un registro de errores (sin nada de lo grabado) se guardan en tu perfil de usuario o junto al exe en modo portátil. Sin cuenta, sin anuncios, sin rastreadores, sin analítica.
