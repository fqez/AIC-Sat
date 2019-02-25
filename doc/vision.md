# 1. Documento visión.
## 1.1 Propósito
El propósito de este documento es recoger, analizar y definir las necesidades de alto nivel y las características del  sistema de localización de casas mediante imagen satélite. El documento se centra en la funcionalidad requerida por los participantes en el proyecto y los usuarios finales.
Esta funcionalidad se basa principalmente en la obtención de información residencial de una determinada región geográfica con la finalidad de obtener zonas propicias para la construcción.
Los detalles de cómo el sistema cubre los requerimientos se pueden observar en la especificación de los casos de uso y otros documentos adicionales.

## 1.2 Problema a resolver.
El sistema permitirá a los empleados de la empresa ver donde están localizadas las casas en una imagen de satélite para así poder obtener información de interés orientada al cliente en la determinación de espacios geográficos propicios para la construcción de parques infantiles.

## 1.3 Definiciones, Acrónimos, y Abreviaciones

* **RUP**: Son las siglas de Rational Unified Process. Se trata de una metodología para describir el proceso de desarrollo de software.

* **Python**: lenguaje de programación interpretado cuya filosofía hace hincapié en una sintaxis que favorezca un código legible.

* **Framework**: estructura conceptual y tecnológica de asistencia definida, normalmente, con artefactos o módulos concretos de software

* **Django**: Framework de desarrollo web desarrollado en Python.

* **Red neuronal**: modelo matemático que recibe unos datos de entrada y estima una salida en relación a ellos.

* **Red neuronal convolucional** : red neuronal basada en operaciones de convolución, cuyos datos de entrada son imágenes completas.

* **Keras**: es una biblioteca de Redes Neuronales de Código Abierto escrita en Python.

## 1.5 Definición del problema

| El problema de              | Localizar viviendas en imágenes de satélite de manera automática |
| --------------------------- | ------------------------------------------------------------ |
| afecta a                    | los empleados de la empresa                                  |
| El impacto asociado es      | se pierde mucho tiempo localizando las viviendas en las imágenes manualmente |
| Una solución adecuada sería | informatizar el proceso mediante una página web a la que subas la imagen y  te la devuelva con las casas ya marcadas |

## 1.6 Usuarios

La empresa contratadora.



## 1.7 Requisitos

### 1.7.1 Requisitos funcionales

Los requisitos funcionales más importantes son:

* **Funciones del usuario**:
  * *Subir imagen a la aplicación*: el usuario seleccionará una imagen (o un conjunto de imagenes) de su máquina y la(s) subirá a la aplicación web para su posterior procesado.
  * *Enviar imagen*: una vez subida la imagen (o el conjunto de imágenes) el usuario podrá enviar la(s) misma(s) al sistema para su procesado.
  * *Descargar imagen resultante*: una vez procesada la imagen o el conjunto de imágenes, el usuario podrá descargarla(s) a su sistema.
  * *Cambiar datos propias*
* **Funciones del administrador**: 
  * Podrá realizar todas las tareas del usuario normal además de las siguientes.
  * *Dar de alta usuarios*: añadir usuarios que puedan acceder al sistema.
  * *Dar de baja usuarios*: eliminar usuarios existentes
  * *Cambiar datos de usuarios*: cambiar datos de usuarios del sistema.
  * *Respaldar BBDD*: podrá realizar un respaldo de la base de datos cuando quiera.
* **Funciones de la aplicación web**:
  * *Procesar imagen*: una vez recibida la imagen (o conjunto de imágenes) esta se enviará directamente al sistema para su procesado.
  * *Mostrar imagen procesada*: una vez procesada la imagen por el sistema, la aplicación web la recogerá y la mostrará a través de su interfaz de usuario (el navegdor web).

### 1.7.2 Requisitos no funcionales

* **Usabilidad**
  * Dado que el sistema consta de dos botones en su interfaz de usuario, no es necesaria formación adicional del personal.
  * El sistema debe proporcionar mensajes de error que sean informativos y orientados a usuario final.
  * La aplicación web debe poseer un diseño responsivo a fin de garantizar la adecuada visualización en múltiples dispositivos (tablets, pc,smartphone).
  * Es sistema será capaz de procesar sólamente una imagen a la vez.
  * El sistema debe poseer interfaces gráficas bien formadas.
* **Seguridad**
  * Los permisos de acceso al sistema podrán ser cambiados solamente por el administrador de acceso a datos.
  * La base de datos de usuarios y configuraciones serán respaldadas automáticamente cada día.
  * Todas las comunicaciones externas entre servidores de datos, aplicación y cliente del sistema deben estar encriptadas mediante RSA.
* **Robustez**
  * El sistema debe tener una disponibilidad del 100% de las veces en que un usuario intente accederlo las 24h del día.
  * El tiempo para iniciar o reiniciar el sistema no podrá ser mayor a 2 minutos.
  * La probabilidad de fallo del sistema no podrá ser mayor a 5%.




