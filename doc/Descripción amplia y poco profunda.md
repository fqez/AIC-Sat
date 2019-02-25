## Descripción amplia y poco profunda

### Actores

El sistema cuenta con dos actores diferentes que interactúan con el sistema: usuarios normales y administradores.

**Usuarios**

Estos actores realizarán las tareas propias para el correcto uso del sistema en pos de obtener los resultados deseados a través de él.

**Administradores**

Los administradores podrán realizar las mismas tareas que el resto de usuarios además de algunas otras adicionales relacionadas con la administración del sistema. Se puede considerar que son usuarios con permisos especiales.

### Casos de uso

El siguiente diagrama de casos de uso muestra de forma global y superficial las tareas que pueden realizar los diferentes actores como interacción con el sistema.

<<<<<diagrama>>>>>>

A continuación se especifica detalladamente cada caso de uso y de cómo los actores interactúan con cada uno de ellos.

**Caso de uso: identificarse**

<<<< diagrama>>>>>

*Actores*: usuario.

*Descripción textual*: el usuario o administrador del sistema, a través de su navegador web, accederá a la página web del sistema donde aparecerá una ventana de bienvenida mostrándole un formulario para que introduzca credenciales de acceso al sistema. El usuario entonces introducirá sus credenciales y si son correctos será redirigido a la página principal del interfaz de web del sistema.

Diagrama de flujo de eventos:

| Usuario                                | Identificarse                           |
| :------------------------------------- | --------------------------------------- |
| 1. Ir a la página web de la aplicación |                                         |
|                                        | 2. Mostrar formulario de identificación |
| 3. Rellenar formularo                  |                                         |
| 4. Pinchar en botón de "Login"         |                                         |
|                                        | 5. Validar formulario                   |
|                                        | 6. Comprobar contra la BD               |
|                                        | 7. Redirigir a página principal         |
|                                        | **Camino alternativo**                  |
|                                        | 8. Datos de usuario incorrectos         |

**Caso de uso: subir imagen**

<<<< diagrama>>>>>

*Actores*: usuario.

*Descripción textual*: En la página principal de la aplicación se mostrará un interfaz amigable en el cual una de las opciones será "subir imagen". Cuando el usuario pulse ese botón se mostrará una ventana emergente con el sistema de ficheros de su máquina invitándole a seleccionar la imagen que quiere procesar. El usuario seleccionará la imagen deseada y seleccionará el botón correspondiente en la ventana emergente para finalizar la subida de la misma. La imagen entonces será enviada al sistema para su procesamiento.

Diagrama de flujo de eventos:

| Usuario                        | Subir imagen                                          |
| ------------------------------ | ----------------------------------------------------- |
| [Login]                        |                                                       |
| 1. Seleccionar "subir imagen"  |                                                       |
|                                | 2. Ofrecer ventana emergente de selección de archivo. |
| 4. Pinchar en botón de "Login" |                                                       |
|                                | 5. Validar formulario                                 |
|                                | 6. Comprobar contra la BD                             |
|                                | 7. Redirigir a página principal                       |
|                                | **Camino alternativo**                                |
|                                | 8. Datos de usuario incorrectos                       |

**Procesar imagen**

**Descargar imagen**

**Cambiar datos personales**

**Dar de alta usuario**

**Dar de baja usuario**

**Cambiar datos usuario** 

**Realizar respaldo BBDD**

