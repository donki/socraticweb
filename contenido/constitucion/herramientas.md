# Constitución de las herramientas de Windows
- slug: herramientas
- documento: CONSTITUCION-TOOLS.md
- orden: 3
- actualizado: 2026-09-23
- lema: Utilidades internas y de escritorio: que hagan una cosa, que no rompan nada por defecto y que digan qué hicieron.

Amplía la constitución general para las herramientas: programas de apoyo, utilidades de escritorio
y generadores que se usan para hacer el resto del catálogo.

## 1. Qué es una herramienta

**Qué dice.** Es software de apoyo: scripts de automatización, utilidades de escritorio,
generadores. No se publica en tiendas ni tiene usuarios fuera del proyecto. Eso relaja lo de las
fichas y la clasificación por edades, pero **no** la licencia, la seguridad ni la privacidad.

**Por qué.** Que algo sea interno no lo hace inofensivo: una herramienta suele tener más acceso
(cuentas, dispositivos, publicación) que una aplicación normal.

## 2. Reglas

### 2.1 Una herramienta hace una cosa

**Qué dice.** Si crece hasta necesitar su propia interfaz completa y su distribución, deja de ser una
herramienta y se trata como aplicación.

**Por qué.** Así cada una se entiende de un vistazo, y lo que se convierte en producto recibe las
reglas de un producto.

### 2.2 Reproducible

**Qué dice.** Se ejecuta con una sola orden documentada en su README, con las dependencias declaradas.

**Por qué.** Si solo sabe usarla quien la escribió, el día que falta esa persona o esa memoria, no se
puede usar.

### 2.3 Sin efectos destructivos por defecto

**Qué dice.** Todo lo que borra, sobrescribe o publica pide confirmación o una opción explícita, y
siempre que tenga sentido hay un modo de ensayo que enseña qué haría sin hacerlo.

**Por qué.** Un error al ejecutar una herramienta no debería poder borrar ni publicar nada que no se
haya pedido a propósito.

### 2.4 Idempotente

**Qué dice.** Siempre que se pueda, ejecutarla dos veces no deja las cosas peor que ejecutarla una.

**Por qué.** Permite repetirla sin miedo después de un fallo a medias.

### 2.5 Salida legible

**Qué dice.** Al terminar se entiende qué hizo, qué se saltó y por qué.

**Por qué.** Una herramienta que termina en silencio no deja saber si ha funcionado.

### 2.6 Iconos planos si tiene ventana

**Qué dice.** Como en todo el catálogo: dibujo de línea de un solo color, nunca emoji.

**Por qué.** Por las mismas razones que en la constitución general (6.2).

## 3. Secretos

**Qué dice.** Los secretos nunca van dentro del código: se leen de un fichero local que no se sube al
repositorio. Las herramientas que tocan la consola de Google Play, cuentas o dispositivos dicen en su
README a qué acceden. Cualquier herramienta expuesta a la red exige autenticación robusta (token,
firma por petición, límite de peticiones y lista de permitidos), y sin token responde «no
autorizado». Y una herramienta que toca la base de datos de una aplicación deja **cifrado** lo que
está cifrado: nada de descifrarlo para verlo cómodo en un volcado, un registro o una captura.

**Por qué.** Lo que se descifra «solo para mirar» acaba en un fichero que nadie borra. Si hace falta
verlo, se ve desde la aplicación, que es de quien es la clave.

## 4. Automatización peligrosa

**Qué dice.** Las herramientas que ejecutan órdenes en el equipo o publican en tiendas tienen los
permisos justos, registran lo que hacen, y no se saltan las confirmaciones de seguridad salvo
decisión explícita y consciente.

**Por qué.** Son las que más daño pueden hacer con un error, así que son las que más vigiladas van.

## 5. Documentación

**Qué dice.** Cada herramienta tiene un README con qué hace, cómo se ejecuta, qué necesita instalado,
a qué accede y qué puede romper.

**Por qué.** Antes de ejecutar algo hay que saber qué puede pasar.
