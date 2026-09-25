# PDF Reader
- slug: pdfreader
- plataformas: Android
- lema: Lee tus PDF sin anuncios ni cuentas: todo se queda en tu dispositivo.
- github: https://github.com/donki/PDFReader
- tiendas:
  - Google Play (prueba cerrada): https://play.google.com/store/apps/details?id=com.socratic.pdfreader (solo en la pista alpha de prueba cerrada, sin producción, según D:\sOCProjects\02-PENDIENTE-PDFReader.md; la ficha pública devolvía «No se ha encontrado» el 2026-09-25, así que el enlace aún no sirve al público)
  - Microsoft Store: no publicada (no hay ficha en Mobile/MicrosoftStore; la versión de Windows existe en el código pero no se distribuye)
  - Edge Add-ons / Chrome / Firefox: no aplica
- descarga_alternativa: https://github.com/donki/PDFReader/releases (última: v2026.09.15.0, APK)

## Descripción

PDF Reader es un lector de PDF sencillo y privado para Android. Abre tus documentos, te deja pasar páginas con el dedo, acercar con los dedos y saltar a la página que quieras, y recuerda por dónde ibas en cada uno.

Cada PDF que abres se guarda en una biblioteca de documentos recientes, con su número de páginas, su tamaño y cuándo lo leíste por última vez. Al volver a tocarlo, se abre por la última página que viste. En Android 15 o superior también puedes buscar texto dentro del documento y abrir PDF protegidos con contraseña.

No tiene anuncios, no pide cuenta y no necesita ningún permiso de almacenamiento: eliges los archivos con el selector del sistema o los abres desde cualquier aplicación con «Abrir con».

## Funciones principales

- Biblioteca de documentos recientes, ordenada por última lectura.
- Continúa donde lo dejaste: cada documento reabre por la última página vista.
- Pasa de página con el dedo o con los botones de anterior y siguiente.
- Zoom con pellizco, con doble toque y con botones, hasta 4 aumentos, con el texto nítido.
- Ir directamente a una página concreta.
- Búsqueda de texto dentro del documento (Android 15 o superior).
- Abre PDF protegidos con contraseña (Android 15 o superior); la contraseña no se guarda.
- Abre PDF desde otras aplicaciones con «Abrir con».
- Modo claro y oscuro automático; en español e inglés.

## Guía de uso (soporte)

### Primera puesta en marcha

1. Instala la aplicación. Mientras esté en prueba cerrada, se consigue con el enlace de invitación de probadores de Google Play o con el APK de las releases de GitHub.
2. Ábrela. No te pedirá ningún permiso: los documentos se eligen con el selector de archivos del sistema, que solo da acceso al archivo que escojas.
3. El idioma sigue al del teléfono (español si el teléfono está en español; en otro caso, inglés). Puedes cambiarlo en «Acerca de» › «Idioma».
4. Si hay conexión, al arrancar comprueba si hay una versión más nueva y te lo dice.

### Flujo normal

1. En la biblioteca pulsa «Abrir un PDF» y elige el archivo. Verás «Abriendo documento…» mientras se prepara.
2. El documento se abre en el lector. Desliza a izquierda o derecha para pasar de página, pellizca para acercar y toca el número de página para saltar a otra.
3. Vuelve atrás: el documento queda en «Documentos recientes» y la próxima vez se abrirá por la misma página.

También puedes abrir un PDF desde un gestor de archivos, el correo o el navegador con «Abrir con» › PDF Reader.

### Biblioteca

- **Cabecera**: logotipo, «PDF Reader» y el lema «Tus documentos, solo en tu dispositivo».
- **Botón de información (i)**: abre la pantalla «Acerca de».
- **Documentos recientes**: lista de los PDF que has abierto. Cada tarjeta muestra el nombre, las páginas y el tamaño, y cuándo se abrió por última vez («Hoy», «Ayer» o la fecha). Toca una tarjeta para abrirla por la última página leída.
- **Botón X de cada tarjeta (Quitar)**: pide confirmación con «Quitar documento: Se eliminará «nombre» de la biblioteca y del almacenamiento de la aplicación. El archivo original de tu dispositivo no se toca.» Botones **Quitar** y **Cancelar**.
- **Lista vacía**: si aún no hay nada, verás «Todavía no hay documentos» y la pista para abrir tu primer PDF.
- **Abrir un PDF**: botón inferior que abre el selector del sistema.

### Lector

Barra inferior, de izquierda a derecha:
- **Flecha izquierda (Anterior)**: página anterior.
- **Menos (Alejar)**: reduce el zoom.
- **Número de página («3 / 20»)**: tócalo para abrir «Ir a la página: Introduce un número entre 1 y N». Escribe el número y pulsa **Ir**. Si no es válido, aparece «Página no válida».
- **Más (Acercar)**: aumenta el zoom, hasta 4 aumentos.
- **Flecha derecha (Siguiente)**: página siguiente.
- **Lupa (Buscar)**: abre la barra de búsqueda. Solo aparece en Android 15 o superior.

Gestos sobre la página:
- **Deslizar a izquierda o derecha** (sin zoom): pasa a la página siguiente o a la anterior.
- **Pellizcar**: acerca o aleja.
- **Doble toque**: acerca al doble; otro doble toque vuelve al tamaño de página completa.
- **Arrastrar** (con zoom): mueve la página ampliada.

Barra de búsqueda (Android 15 o superior):
- **Buscar en el documento**: escribe el texto y pulsa Intro. Verás «Buscando…» y después «1 de N» o «Sin resultados para «texto»». Si hay muchísimas coincidencias, se avisa con «Se muestran los primeros N resultados.».
- **Flecha arriba / flecha abajo**: coincidencia anterior / siguiente.
- **X (Cerrar la búsqueda)**: cierra la barra y borra la búsqueda.

### PDF protegido

Al abrir un PDF con contraseña aparece «PDF protegido: Introduce la contraseña de «nombre».» con una caja para la contraseña (oculta) y los botones **Cancelar** y **Abrir**. Si no es correcta, verás «La contraseña no es correcta. Inténtalo de nuevo.». La contraseña no se guarda: se pide cada vez que abres ese documento.

### Acerca de

- **Cabecera**: nombre, «Versión X», lema y Socratic.
- **Contacto**: botón con el correo; «Toca para enviar un correo electrónico» abre tu aplicación de correo con un mensaje ya preparado.
- **Idioma**: botones **Español** y **English**; «Selecciona tu idioma preferido». El cambio se aplica al momento y se recuerda.
- **Privacidad**, **Licencia** (MIT) y **Aviso Legal** con «Uso bajo su propio riesgo».
- **Volver**: regresa a la biblioteca.

### Aviso de actualización

Si hay una versión más nueva: «Actualización disponible: Hay una versión más reciente (X). Tienes la Y. ¿Quieres actualizar?», con **Actualizar** (abre la página de descarga) y **Ahora no**.

## Preguntas frecuentes

**No veo el botón de búsqueda.**
La búsqueda de texto necesita Android 15 o superior. En versiones anteriores el botón no aparece.

**Me dice «Abrir un PDF protegido con contraseña requiere Android 15 o posterior».**
Tu Android no permite descifrar PDF protegidos. Quita la contraseña del documento con otro programa o ábrelo en un teléfono con Android 15 o superior.

**«El archivo seleccionado no es un PDF válido o está dañado.»**
El archivo no es un PDF o está corrupto (por ejemplo, una descarga incompleta). Vuelve a descargarlo y ábrelo de nuevo.

**Un documento ha desaparecido de la biblioteca.**
Si borras los datos de la aplicación, la copia interna se pierde y la entrada se quita sola («El documento ya no está disponible y se ha quitado de la biblioteca.»). Tu archivo original sigue intacto: vuelve a abrirlo.

**Si quito un documento de la biblioteca, ¿se borra mi PDF?**
No. Solo se borra la copia que guarda la aplicación. El archivo original de tu teléfono no se toca.

**No encuentro la aplicación en Google Play.**
Todavía está en prueba cerrada: solo se ve con el enlace de invitación de probadores. Mientras tanto puedes instalar el APK desde las releases de GitHub.

**¿Puedo editar, firmar o anotar PDF?**
No. PDF Reader es solo un lector; esas herramientas se probaron un par de días en septiembre de 2026 y se retiraron.

## Privacidad

Los documentos se abren y se guardan solo en la carpeta privada de la aplicación dentro de tu teléfono; nada sale del dispositivo y las contraseñas de los PDF no se guardan. No hay cuentas, anuncios ni rastreadores; la única conexión a internet es para comprobar si hay una versión nueva.
