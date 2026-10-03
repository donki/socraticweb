# sOC WSManager
- slug: wsmanager
- plataformas: Windows 10 (versión 2004) o posterior y Windows 11, 64 bits
- lema: Cualquier programa, como servicio de Windows: lo arranca con el equipo, lo vigila y lo vuelve a levantar si se cae.
- github: https://github.com/donki/WSManager
- tiendas:
  - Microsoft Store: no aplica (los servicios no se pueden crear desde un paquete de la Store).
  - Google Play: no aplica (solo Windows).
- descarga_alternativa: https://github.com/donki/WSManager/releases (última: v2026.10.1.0; dos ejecutables autocontenidos)

## Descripción

sOC WSManager convierte cualquier programa —un servidor, un script con su intérprete, una herramienta de consola— en un servicio de Windows de verdad: arranca con el equipo aunque nadie haya iniciado sesión, corre con la cuenta que elijas y, si se cae, se vuelve a levantar solo. Si se cae una y otra vez nada más arrancar, espera cada vez un poco más para no quemar el procesador.

Desde el icono junto al reloj ves todos tus servicios con un punto de color según su estado, y los arrancas, paras, pausas, reinicias, editas o das de baja sin abrir nada más. Si uno se para sin que nadie lo pida, te avisa. La ventana principal enseña además el proceso del servicio y el de la aplicación, y cuántas veces se ha reiniciado.

Cada servicio se configura en un editor por pestañas: el programa y sus argumentos, la cuenta, las dependencias, la prioridad y los procesadores, cómo pararlo con cuidado, qué hacer según cómo salga, a qué ficheros va su salida (con la hora en cada línea y rotación por tamaño o por antigüedad), su entorno y órdenes que se ejecutan en cada momento. Si ya tienes servicios hechos con otro gestor de servicios, los importa conservando su configuración, a mano o de forma automática, y se puede deshacer. Para scripts tiene una línea de órdenes completa. Es software libre, sin cuenta, sin anuncios y sin rastreadores, y no se conecta a nada.

## Funciones principales

- Cualquier programa como servicio de Windows, con arranque automático, retrasado, manual o deshabilitado.
- Vigilancia: si la aplicación sale, la vuelve a lanzar, con una espera creciente (de 2 a 256 segundos) si se cae en bucle; pausar el servicio cancela la espera.
- Qué hacer al salir según el código de salida: volver a lanzarla, no hacer nada, parar el servicio o dejar que actúen las acciones de recuperación de Windows.
- Parada escalonada: Ctrl+C, cerrar sus ventanas, pedir a sus hilos que acaben y, si hace falta, terminar el proceso, también los que haya lanzado.
- Salida y errores a fichero, con la hora en cada línea y rotación al arrancar, en marcha o bajo demanda.
- Cuenta del servicio: Sistema local, Servicio local, Servicio de red o una cuenta con contraseña (que va directa a Windows).
- Icono en el área de notificación con todos los servicios, su estado y sus acciones, y avisos si uno se para.
- Importación, manual o automática, de los servicios creados con otro gestor de servicios, con vuelta atrás.
- Registro de arranques, paradas, caídas y reinicios en el Visor de eventos de Windows.
- Línea de órdenes para scripts (crear, cambiar cualquier opción, arrancar, parar, volcar la configuración…).

## Guía de uso (soporte)

### Instalación

1. Descarga la última versión desde la página de versiones de GitHub (https://github.com/donki/WSManager/releases): `sOCWSManager.exe` (la aplicación) y `sOCServiceHost.exe` (el componente de servicio). Ponlos en la misma carpeta.
2. Abre `sOCWSManager.exe`. No hay que instalar nada más. Si Windows avisa de que el editor es desconocido, pulsa «Más información» y «Ejecutar de todas formas».

Requisitos: Windows 10 (versión 2004) o posterior, o Windows 11, de 64 bits. Para crear y cambiar servicios hace falta una cuenta de administrador (Windows pide permiso en cada cambio).

### Primera puesta en marcha

La primera vez se abre la «Guía de configuración», con cuatro pasos (Anterior / Siguiente abajo):

1. **Instalar el componente de servicio**: copia `sOCServiceHost.exe` a Archivos de programa, donde solo los administradores pueden cambiarlo y Windows siempre lo puede leer. Se hace solo al crear el primer servicio.
2. **Arrancar con Windows** (opcional): deja WSManager junto al reloj para ver tus servicios y recibir avisos.
3. **Crear tu primer servicio**: botón «Servicio nuevo».
4. **Traer tus servicios de otro gestor de servicios** (opcional): botón «Importar».

La guía se vuelve a abrir cuando quieras con el botón de ayuda (?).

### Ventana principal

**Botones de la izquierda** (solo iconos; el nombre sale al pasar el ratón): Servicio nuevo (+), Editar, Arrancar o continuar, Pausar, Parar, Reiniciar, Rotar ya los ficheros de salida, Abrir la salida (stdout / stderr) y Dar de baja el servicio (en rojo, con confirmación).

**Botones de la derecha**: Importar de otro gestor de servicios, Ejecutar como administrador (escudo: una ventana aparte en la que los cambios no piden permiso uno a uno), Arrancar con Windows, Guía de configuración, Novedades, Español / English y Acerca de.

**Lista**: Estado (con su punto: verde en marcha, gris parado, ámbar en pausa o esperando para reiniciar), Servicio (nombre visible y nombre), Inicio, Cuenta, PID servicio, PID aplicación y Reinicios. Doble clic o Intro editan; Supr da de baja. Abajo, el resultado de la última acción.

### Icono del área de notificación

Un clic abre la ventana. Con el botón derecho sale un apartado por servicio, con su estado, y dentro: Arrancar, Parar, Pausar o Continuar, Reiniciar, Editar, Abrir la salida (stdout), Abrir los errores (stderr) y Dar de baja el servicio. Debajo: Servicio nuevo, Importar, Abrir la ventana y Salir. Al pasar el ratón dice cuántos servicios hay y cuántos están en marcha. Si un servicio se para sin que se haya pedido, sale un aviso «Un servicio se ha parado».

### Editor de servicio

Arriba, el **Nombre del servicio** (solo al crearlo). Abajo, Cancelar y Guardar; si algo no vale se dice en rojo y no se guarda. Si el servicio está en marcha, los cambios se aplican al reiniciarlo.

- **Aplicación**: Ruta del programa, Directorio de inicio (vacío: la carpeta del programa) y Argumentos. Las rutas pueden llevar variables como %ProgramFiles%.
- **Detalles**: Nombre visible, Descripción y Tipo de inicio (Automático, Automático (retrasado), Manual, Deshabilitado).
- **Inicio de sesión**: Sistema local (con «Permitir que el servicio interactúe con el escritorio»), Servicio local, Servicio de red o Esta cuenta (Cuenta, Contraseña y Repite la contraseña, con el ojo para verla). Sin la ventana de administrador, la contraseña se pide en la ventana de permisos al guardar. La cuenta recibe el derecho de iniciar sesión como servicio.
- **Dependencias**: Servicios de los que depende y Grupos de servicios de los que depende, uno por línea.
- **Proceso**: Prioridad (de Tiempo real a Baja), Procesadores (Todos los procesadores, o una lista como 0-1,3) y Sin ventana de consola para la aplicación.
- **Parada**: Mandar Ctrl+C, Cerrar sus ventanas (WM_CLOSE), Pedir a sus hilos que acaben (WM_QUIT) y Terminar el proceso, cada uno con su espera en milisegundos (1500 por defecto); y Parar también los procesos que haya lanzado.
- **Acciones de salida**: Tiempo mínimo en marcha para que un reinicio cuente como normal (1500 ms), Cuando la aplicación sale (Volver a lanzar la aplicación, No hacer nada, Parar el servicio, Acabar sin parar), Espera antes de reiniciar, y una lista Por código de salida (añadir y quitar).
- **E/S**: Entrada (stdin), Salida (stdout) y Errores (stderr), con qué hacer si el fichero ya existe (Añadir al final, Sustituirlo…), y Poner la fecha y la hora en cada línea.
- **Rotación**: Rotar los ficheros al arrancar el servicio; Con el servicio en marcha (No rotar, Rotar al llegar a los límites, Rotar en los límites y bajo demanda); Más viejos que (segundos) y Más grandes que (bytes).
- **Entorno**: Añadir o cambiar variables, y Sustituir todo el entorno (NOMBRE=valor, una por línea; %VARIABLE% se expande).
- **Ganchos**: una orden para cada momento (antes de lanzar la aplicación —el código 99 cancela el arranque—, después de lanzarla, antes de pararla, cuando ha salido, antes y después de rotar, al cambiar la alimentación y al volver de la suspensión).

### Importar servicios

Botón «Importar de otro gestor de servicios». La ventana tiene tres partes:

- **Servicios de otro gestor de servicios**: los que encuentra, marcados; «Importar los elegidos» pide confirmación y los pasa a WSManager conservando toda su configuración. Los que estén en marcha se paran y se vuelven a arrancar.
- **Ya importados**: cada uno con «Deshacer la importación», mientras el programa del otro gestor siga en el PC.
- **Importación automática**: «Importar automáticamente los servicios de otro gestor de servicios» (pide permiso de administrador una vez) y «Reiniciar en el acto los que estén en marcha» (si no, WSManager toma el relevo en su próximo arranque). Crea una tarea programada que se ejecuta al arrancar el PC y cada 15 minutos; cada importación sale en un aviso.

### Acerca de

Versión, Novedades, Contar un fallo o una idea, Idioma (Español / English, con sus banderas), Privacidad, Licencia y Aviso legal.

## Preguntas frecuentes

**¿Por qué me pide permiso de administrador en cada cambio?**
Crear, cambiar, arrancar o parar servicios es cosa de administradores en Windows. La aplicación corre sin privilegios y pide permiso solo para cada operación, sin dejar nada con privilegios en marcha. Si vas a hacer muchos cambios seguidos, usa el botón del escudo («Ejecutar como administrador»).

**Mi programa se cae nada más arrancar y el servicio dice «Esperando para reiniciar».**
Es la espera creciente: cada caída seguida dobla la espera, hasta 256 segundos. Mira la salida (botón de la salida) y el Visor de eventos (origen sOCWSManager) para ver por qué sale. Pausa el servicio para cancelar el reinicio pendiente.

**¿Dónde veo lo que escribe mi programa?**
Pon un fichero en la pestaña E/S (Salida y Errores pueden ser el mismo). Después, «Abrir la salida» lo abre con el programa de Windows.

**Importé un servicio en marcha con la importación automática y sigue igual.**
Por defecto, los que están en marcha pasan a WSManager en su próximo arranque (por ejemplo al reiniciar el equipo), que es el momento de menos riesgo. Si prefieres que se reinicien en el acto, marca «Reiniciar en el acto los que estén en marcha».

**¿Guarda las contraseñas de las cuentas?**
No: van directas a Windows, que es quien las guarda para el servicio.

## Privacidad

Todo se queda en tu PC: los servicios los guarda Windows, y la aplicación solo guarda su idioma y el tamaño de la ventana en tu perfil. No se conecta a nada. Sin cuenta, sin anuncios, sin rastreadores, sin analítica. Las contraseñas de las cuentas van directas a Windows y la aplicación no las guarda nunca.
