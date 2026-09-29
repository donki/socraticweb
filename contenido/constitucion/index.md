# Constitución
- lema: Las normas con las que se hacen todas las aplicaciones del catálogo, explicadas una a una: qué dice cada regla y por qué existe.
- actualizado: 2026-09-29

## Qué es la constitución

Es el conjunto de normas con las que se hacen **todas** las aplicaciones de sOCratic: las del móvil,
los programas de Windows, los juegos y esta misma web. Dice qué licencias se pueden usar, cómo se
tratan los datos de quien usa las aplicaciones, cómo tienen que ser los botones y los mensajes de
error, cómo se numeran las versiones, qué se comprueba antes de publicar y muchas cosas más.

Se llama así porque manda: una aplicación no se da por terminada si no la cumple, y cuando dos
normas chocan, gana la de más arriba.

## Un experimento de programación con IA

Todo el catálogo es un experimento de **desarrollo guiado por especificaciones**: antes de programar
se escribe qué debe hacer cada aplicación (su especificación) y con qué normas, y a partir de eso la
programan **modelos de lenguaje grandes** (LLM, por sus siglas en inglés), una forma de inteligencia
artificial. La idea es aprender qué se puede hacer así y cómo hacerlo bien.

La constitución es **la parte fija de esas especificaciones**: la que vale para todas las
aplicaciones. Cada una añade la suya —qué hace, qué pantallas tiene—, pero todas parten de estas
reglas: cómo tiene que quedar el código, qué no se puede hacer nunca y qué hay que comprobar antes de
dar algo por bueno. Quien publica cada versión, y responde de ella, es una persona.

## Por qué existe

Casi ninguna regla nació en una pizarra. La mayoría se escribió **después de un error real**: una
aplicación rechazada por una tienda, una versión que no se podía instalar, horas de trabajo
perdidas, un texto que el usuario escribió y desapareció. Cada vez que algo así pasa, se apunta la
regla que lo habría evitado, a menudo con el caso entre paréntesis. La constitución no es una lista
de buenas intenciones: es lo que costó averiguar.

## Es pública y vale para todo el catálogo

El texto completo está en GitHub, con la misma licencia MIT que el código, y cada aplicación lo
incluye dentro de su propio repositorio. Se edita en un solo sitio y llega a todas: así ninguna se
queda con una copia vieja.

Aquí está explicado para quien quiera aprender cómo se hace software cuidado. Cada página resume un
documento regla a regla, en lenguaje llano, con **qué dice** y **por qué**. Lo que es puramente
interno —rutas de trabajo, dónde se guardan las claves, identificadores de cuentas y servidores— no
se reproduce: se explica la idea. Y, como en el resto de la web, los productos que no son de
Microsoft ni de Google se describen por lo que son en vez de nombrarlos.

## Cómo se organiza

La **constitución general** es la capa de arriba y vale para todo. Cada categoría —móvil,
herramientas de Windows, juegos y web— tiene su propio documento, que **amplía** la general pero
nunca la contradice. Debajo están los **anexos técnicos**, con el detalle exhaustivo de cada
plataforma. Si alguna vez un documento contradice a la general, manda la general y se corrige el
otro.

## Cómo se mantiene al día

Cuando se aprende algo nuevo, se escribe la regla en la constitución con su porqué y se lleva a
todas las aplicaciones. Y cuando la constitución cambia, **su página de esta web cambia en el mismo
ciclo**, en castellano y en inglés. Cada página dice la fecha del texto que explica.
