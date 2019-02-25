## Descripción amplia y poco profunda

### Actores

El sistema cuenta con dos actores diferentes que interactúan con el sistema: usuarios normales y administradores.

**Usuarios**

Estos actores realizarán las tareas propias para el correcto uso del sistema en pos de obtener los resultados deseados a través de él.

**Administradores**

Los administradores podrán realizar las mismas tareas que el resto de usuarios además de algunas otras adicionales relacionadas con la administración del sistema. Se puede considerar que son usuarios con permisos especiales.

### Casos de uso

El siguiente diagrama de casos de uso muestra de forma global y superficial las tareas que pueden realizar los diferentes actores como interacción con el sistema.

![diagrama_de_casos_de_uso](img/diagrama_de_casos_de_uso.svg)

A continuación se especifica detalladamente cada caso de uso y de cómo los actores interactúan con cada uno de ellos.

**Caso de uso: Login**

*Actores*: usuario.

*Descripción textual*: el usuario o administrador del sistema, a través de su navegador web, accederá a la página web del sistema donde aparecerá una ventana de bienvenida mostrándole un formulario para que introduzca credenciales de acceso al sistema. El usuario entonces introducirá sus credenciales y si son correctos será redirigido a la página principal del interfaz de web del sistema.

Diagrama de flujo de eventos:

| Usuario                                | Identificarse                           |
| :------------------------------------- | --------------------------------------- |
| 1. Ir a la página web de la aplicación |                                         |
|                                        | 2. Mostrar formulario de identificación |
| 3. Rellenar formulario                 |                                         |
| 4. Pinchar en botón de "Login"         |                                         |
|                                        | 5. Validar formulario                   |
|                                        | 6. Comprobar contra la BD               |
|                                        | 7. Redirigir a página principal         |
|                                        | **Camino alternativo**                  |
|                                        | 8. Datos de usuario incorrectos         |

**Caso de uso: Subir imagen**

*Actores*: usuario.

*Descripción textual*: En la página principal de la aplicación se mostrará un interfaz amigable en el cual una de las opciones será "subir imagen". Cuando el usuario pulse ese botón se mostrará una ventana emergente con el sistema de ficheros de su máquina invitándole a seleccionar la imagen que quiere procesar. El usuario seleccionará la imagen deseada y seleccionará el botón correspondiente en la ventana emergente para finalizar la subida de la misma. La imagen entonces será enviada al sistema para su procesamiento.

Diagrama de flujo de eventos:

| Usuario                                                      | Subir imagen                                                 |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [**Login**]                                                  |                                                              |
| 1. Seleccionar "subir imagen"                                |                                                              |
|                                                              | 2. Ofrecer ventana emergente de selección de archivo.        |
| 3. Seleccionar imagen a subir                                |                                                              |
| 4. Pulsar en botón correspondiente para efectuar la subida en la ventana emergente |                                                              |
|                                                              | 5. Cargar la imagen del sistema del usuario al sistema de procesamiento. |
|                                                              | 7. Redirigir a página principal                              |
|                                                              | **Camino alternativo**                                       |
|                                                              | 8. Formato de imagen incorrecto.                             |

**Caso de uso: Procesar imagen**

*Actores*: usuario.

*Descripción textual*: En la página principal de la aplicación se mostrará un interfaz amigable en el cual una de las opciones será "procesar imagen". Cuando el usuario pulse ese botón se mostrará un mensaje de procesamiento indicando que se está llevando a cabo la tarea de segmentación de la imagen. Una vez finalizado el proceso, el sistema mostrará el resultado del procesamiento en el interfaz web.

Diagrama de flujo de eventos:

| Usuario                          | Procesar imagen                                              |
| -------------------------------- | ------------------------------------------------------------ |
| [**Login**]                      |                                                              |
| 1. Seleccionar "procesar imagen" |                                                              |
|                                  | 2. Realizar el preprocesamiento y segmentación de la imagen proporcionada por el usuario. |
|                                  | 3. Obtener imagen resultante                                 |
|                                  | 4. Mostrar la imagen resultante en el interfaz web.          |
|                                  | **Camino alternativo**                                       |
|                                  | 5. Error en el procesamiento de la imagen                    |

**Caso de uso: Descargar imagen**

*Actores*: usuario.

*Descripción textual*: En la página principal una vez realizada la segmentación de la imagen, se ofrecerá al usuario un botón para descargar la imagen resultante llamado "Descargar imagen". Una vez el usuario pulse ese botón comenzará el proceso de descarga de la misma a su sistema ofreciendo una ventana emergente para que el usuario seleccione en qué lugar de su sistema desea almacenar la imagen procesada.

Diagrama de flujo de eventos:

| Usuario                                             | Descargar imagen                                             |
| --------------------------------------------------- | ------------------------------------------------------------ |
| [**Login**]                                         |                                                              |
| 1. Seleccionar "procesar imagen"                    |                                                              |
|                                                     | 2. Ofrecer ventana emergente de selección de archivo.        |
| 3. Seleccionar directorio donde almacenar la imagen |                                                              |
| 4. Pulsar el botón guardar en la ventana emergente  |                                                              |
|                                                     | 5. Realizar proceso de descarga                              |
|                                                     | **Camino alternativo**                                       |
|                                                     | 5. Error en permisos de escritura en directorio seleccionado |

**Caso de uso: Cambiar datos propios**

*Actores*: usuario.

*Descripción textual*: En la página principal el usuario será capaz de cambiar sus datos personales como nombre de usuario y contraseña cuando el usuario pulse sobre el botón "modificar datos". Se ofrecerá otro interfaz amigable con un formulario para que el usuario cambie sus credenciales de acceso al sistema. El sistema entonces almacenará los nuevos datos en la base de datos.

Diagrama de flujo de eventos:

| Usuario                                             | Cambiar datos propios                                        |
| --------------------------------------------------- | ------------------------------------------------------------ |
| [**Login**]                                         |                                                              |
| 1. Seleccionar "cambiar datos"                      |                                                              |
|                                                     | 2. Ofrecer una ventana con los formularios de cambio de credenciales |
| 3. Rellenar el formulario de cambio de credenciales |                                                              |
| 4. Pulsar el botón guardar.                         |                                                              |
|                                                     | 5. Materializar cambio en la base de datos.                  |
|                                                     | **Camino alternativo**                                       |
|                                                     | 6. Contraseña insegura proporcionada.                        |

**Caso de uso: Dar de alta usuario**

*Actores*: administrador.

*Descripción textual*: En la página principal el administrador será capaz de dar de alta a un usuario nuevo cuando pulse sobre el botón "agregar usuario". Se ofrecerá otro interfaz amigable con un formulario para rellenar con los datos del usuario nuevo. El administrador rellenará el formulario y pulsará sobre el botón "agregar". Entonces el sistema procederá a crear una entrada en la base de datos de usuarios con los datos introducidos.

Diagrama de flujo de eventos:

| Usuario                                                      | **Dar de alta usuario**                                      |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [**Login**]                                                  |                                                              |
| 1. Seleccionar "agregar usuario"                             |                                                              |
|                                                              | 2. Ofrecer una ventana con formulario de datos para nuevo usuario. |
| 3. Rellenar el formulario.                                   |                                                              |
| 4. Pulsar sobre el botón agregar                             |                                                              |
|                                                              | 5. Mostrar ventana de confirmación                           |
| 6. Pulsar sobre el botón "Sí" en la ventana de confirmación. |                                                              |
|                                                              | 7. Materializar cambio en base de datos.                     |
|                                                              | 8. Volver a la página principal de la aplicación.            |
|                                                              | **Camino alternativo**                                       |
| 6. Pulsar sobre el botón "No" en la ventana de confirmación  |                                                              |

**Caso de uso: Dar de baja usuario**

*Actores*: administrador.

*Descripción textual*: En la página principal el administrador será capaz de dar de baja a un usuario existente cuando pulse sobre el botón "eliminar usuario". Se ofrecerá otro interfaz amigable con una lista de usuarios, de la cual el administrador seleccionará el usuario del que desea eliminar y acto seguido pulsará en el botón "eliminar". Se mostrará una ventana de confirmación al administrador en la que podrá decidir si finalmente elimina al usuario. En caso afirmativo automáticamente se eliminará la entrada de ese usuario en la base de datos del sistema. En caso negativo se volverá a la página del listado de usuarios.

Diagrama de flujo de eventos:

| Usuario                                                      | Dar de baja usuario                                          |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [**Login**]                                                  |                                                              |
| 1. Seleccionar "eliminar usuario"                            |                                                              |
|                                                              | 2. Ofrecer una ventana con la lista de usuarios del sistema. |
| 3. Seleccionar usuario a eliminar                            |                                                              |
| 4. Pulsar sobre el botón eliminar                            |                                                              |
|                                                              | 5. Mostrar ventana de confirmación                           |
| 6. Pulsar sobre el botón "Sí" en la ventana de confirmación. |                                                              |
|                                                              | 7. Materializar cambio en base de datos.                     |
|                                                              | 8. Volver a la página de listado de usuarios.                |
|                                                              | **Camino alternativo**                                       |
| 6. Pulsar sobre el botón "No" en la ventana de confirmación  |                                                              |

**Caso de uso: Cambiar credenciales de usuarios** 

*Actores*: administrador.

*Descripción textual*: En la página principal el administrador será capaz de cambiar sus datos personales y/o los de cualquier otro usuario registrado como nombre de usuario y contraseña cuando pulse sobre el botón "modificar datos". Se ofrecerá otro interfaz amigable con una lista de usuarios, de la cual el administrador seleccionará el usuario del que desea modificar los datos y acto seguido el interfaz web ofrecerá un formulario idéntico al requisito de "Cambiar datos personales". Al finalizar el sistema regresará a la página principal de la aplicación.

Diagrama de flujo de eventos:

| Usuario                                             | Cambiar credenciales de usuarios                             |
| --------------------------------------------------- | ------------------------------------------------------------ |
| [**Login**]                                         |                                                              |
| 1. Seleccionar "cambiar datos"                      |                                                              |
|                                                     | 2. Ofrecer una ventana con la lista de usuarios del sistema. |
| 3. Seleccionar usuario a modificar en la lista.     |                                                              |
|                                                     | 3. Ofrecer una ventana con los formularios de cambio de credenciales |
| 3. Rellenar el formulario de cambio de credenciales |                                                              |
| 4. Pulsar el botón guardar.                         |                                                              |
|                                                     | 5. Materializar cambio en la base de datos.                  |
|                                                     | **Camino alternativo**                                       |
|                                                     | 6. Contraseña insegura proporcionada.                        |

**Realizar respaldo BBDD**

*Actores*: administrador.

*Descripción textual*: En la página principal el administrador será capaz de realizar un respaldo de la base de datos cuando pulse sobre el botón "respaldar BD". Automáticamente el sistema realizará un respaldo de la base de datos mostrando un mensaje de confirmación al finalizar la tarea y devolviendo el usuario a la página principal de la aplicación.

Diagrama de flujo de eventos:

| Usuario                      | Cambiar credenciales de usuarios                             |
| ---------------------------- | ------------------------------------------------------------ |
| [**Login**]                  |                                                              |
| 1. Seleccionar "respaldo BD" |                                                              |
|                              | 2. Realizar un respaldo de la base de datos en segundo plano |
|                              | 3. Almacenar la base de datos en el directorio correspondiente de respaldos. |
|                              | 3. Mostrar un mensaje de confirmación de éxito en el respaldo. |
|                              | 4. Devolver al usuario a la página principal.                |
|                              | **Camino alternativo**                                       |
|                              | 6. Error en respaldo                                         |