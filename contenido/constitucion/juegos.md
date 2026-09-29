# Constitución de los juegos
- slug: juegos
- documento: CONSTITUCION-GAMES.md
- orden: 4
- actualizado: 2026-09-23
- lema: Motor libre, recursos con licencia acreditada, sin compras ni anuncios, y 60 imágenes por segundo.

Amplía la constitución general para los videojuegos del catálogo.

## 1. Motor y estructura

**Qué dice.** Los juegos se hacen con un **motor de videojuegos libre** (con licencia MIT), con sus
escenas y scripts guardados en el repositorio. Cada juego tiene la misma estructura mínima: escenas,
lógica, recursos (arte, audio, fuentes), herramientas de desarrollo y textos traducibles. Las
herramientas de desarrollo **no se empaquetan** en el juego final.

**Por qué.** Un motor libre cumple la regla de licencias del catálogo; una estructura fija hace que
cualquiera sepa dónde buscar; y lo que solo sirve para desarrollar no tiene por qué ocupar sitio en
el dispositivo del jugador.

## 2. Recursos y licencias

### 2.1 Todo recurso, con licencia apta

**Qué dice.** Arte, música, efectos, fuentes y voces tienen que ser compatibles con la MIT o de uso
comercial libre, igual que el código. Sin excepciones.

**Por qué.** Un juego es tanto sus recursos como su código: una imagen con una licencia que no lo
permite impediría compartirlo igual que una biblioteca.

### 2.2 Procedencia documentada

**Qué dice.** Cada recurso lleva apuntadas su procedencia y su licencia. Si no se puede acreditar, no
entra.

**Por qué.** «Lo encontré por internet» no es una licencia.

### 2.3 Voz y audio generados

**Qué dice.** Las voces generadas se hacen con motores de voz cuya licencia permite el uso comercial.
Uno que no lo permitía quedó descartado.

**Por qué.** Es la regla 1.1 de la constitución general aplicada a la voz.

### 2.4 Recursos generados, reproducibles

**Qué dice.** Lo que produce una herramienta del propio juego se puede volver a generar: el script
que lo produce se guarda junto al resultado.

**Por qué.** Si hay que cambiarlo, se cambia el script y se regenera, en vez de retocar a mano algo
que nadie sabe cómo se hizo.

## 3. Contenido

**Qué dice.** Clasificación por edades adecuada y declarada en la tienda. Sin compras integradas, sin
anuncios y sin telemetría. El progreso se guarda **en el dispositivo**: un juego no necesita cuenta.
Si algún día hubiera partidas compartidas o marcadores, el nombre que pone el jugador saldría cifrado
como cualquier otro texto del usuario.

**Por qué.** Un juego no es una excepción a la idea del catálogo: libre, sin anuncios y sin medir a
nadie.

## 4. Interfaz

**Qué dice.** El diseño común (paleta índigo, esquinas redondeadas, modo claro y oscuro), botones con
iconos planos, y menús que se manejan con mando y con pantalla táctil, no solo con ratón.

**Por qué.** Se juega de muchas maneras, y un menú que solo funciona con ratón deja fuera a quien
juega en el móvil o con mando.

## 5. Idiomas

**Qué dice.** Castellano e inglés obligatorios, con todos los textos extraídos a ficheros de
traducción. Ningún texto escrito dentro de las escenas ni de los scripts.

**Por qué.** Como en el resto del catálogo: traducir tiene que ser rellenar una tabla.

## 6. Rendimiento

**Qué dice.** Objetivo: **60 imágenes por segundo estables** en el dispositivo de referencia. Hay un
tamaño máximo de texturas fijado para cada proyecto y aplicado antes de exportar, y antes de publicar
se mide el tiempo de carga, la memoria y la fluidez en la escena más pesada.

**Por qué.** Lo que no se mide empeora sin que nadie lo note, y las texturas demasiado grandes son la
forma más fácil de hacer un juego lento y pesado.

## 7. Publicación

**Qué dice.** Si un juego va a Google Play, se le aplica también la constitución de las aplicaciones
móviles: la misma firma, el mismo formato de versiones, la versión de Android que exija Google y una
ficha con capturas reales del juego. La compilación para Android se hace con un script.

**Por qué.** Para Google Play un juego es una aplicación más, con las mismas reglas.
