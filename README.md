# Localización de Viviviendas en imagen satélite

Proyecto de la asignatura Aplicaciones industriales y comerciales del [Máster de Visión Artificial](https://mastervisionartificial.es/).

Este proyecto consiste en desarrollar una aplicación web que localice casas en imágenes de satélite dadas por un usuario.

## Requisitos de ejecución

Para ejecutar el sistema es necesario disponer de un equipo con CPU relativamente moderna que soporte el conjunto de instrucciones de TensorFlow.

Además el sistema funciona bajo sistemas Linux, con distribución recomendada Ubuntu 18.04 LTS.

## Puesta en marcha

### Entorno virtual

Se recomienda trabajar dentro de un entorno virtual de Python 3.7 por seguridad y comodidad.

#### Creación del entorno

Para empezar a trabajar en un entorno virtual, se requiere tener instalado alguna versión de Python 3 (recomendado Python 3.5 o 3.7) y ejecutar:

```
python3 -m venv /ruta/al/entorno/virtual
```

con esto se generará el entorno virtual en la ruta especificada

#### Activar entorno virtual

Una vez creado el entorno virtual, para trabajar en una consola dentro de él hay que activarlo de la siguiente forma

```
source /ruta/al/entorno/virutal/bin/activate
```

Observa que el prompt cambia, lo que te indicará que ya estás dentro del entorno virtual.

### Clonar repositorio

Se recomienda trabajar dentro del directorio donde se ha creado el entorno virutal, no obstante no es obligatorio.
Clonar el repositorio de la práctica:
```
git clone https://github.com/fqez/AIVA-segmentacion-satelite AIVASat
cd AIVASat
```

### Dependencias

#### Instalar dependencias

Para instalar la dependencias ejecuta los siguientes comandos.

```
pip install -r requirements.txt
sudo apt install python3-tk
```



#### Descargar modelo

Descarga en **model** el modelo de la red de [este link](https://drive.google.com/open?id=1RFjABoLp6UUU4a0ZNF-klZRo_z1lqo5C)



### Ejecutar

#### Servidor
```
python server.py [-h] [-s HOST] [-p PORT] [-d]
```

* -h, --help            show this help message and exit
* -s HOST, --host HOST  host (default: 127.0.0.1)
* -p PORT, --port PORT  port (default: 5000)
* -d, --debug           Activate debug mode

Para ejecutar en localhost:
```
python server.py
```

Para servir en todas las ips y en el puerto 80:
```
python server.py -s 0.0.0.0 -p 80
```

#### Cliente
```
python client.py [-h] -i IN -o OUT [-s SERVER] [-p PORT]
```

* -h, --help            show this help message and exit
* -i IN, --in IN        folder with in images
* -o OUT, --out OUT     output json file
* -s SERVER, --server SERVER          server's url (default: localhost)
* PORT, --port PORT  server's port (default: 5000)

Para ejecutar en localhost:
```
python client.py -i folder -o out.json
```

Para conectarse al servidor en http://aiva.jderobot.org/:
```
python client.py -i folder -o out.json -s http://aiva.jderobot.org/ -p 80
```

### Despliegue

Para desplegar el sistema en un servidor, se ofrece una imagen de docker ya construida con todos los elementos necesarios para el funcionamiento del mismo. Para desplegar el sistema:

```
docker run -d --name nombre_imagen -p IP:PUERTO:5000 fqez/aiva:latest
```

Esta instrucción generará el contenedor y lanzará el servicio de forma automática. Para acceder a él únicamente hay que abrir un navegador web y dirigirse a la URL IP:PUERTO especificados a la hora de lanzar el contenedor de docker.

### Tests

#### Descargar los datos necesarios para los test

Ejecuta lo siguiente:

```
./scripts/prepare_test.sh
```

#### Ejecutar los test

Ejecuta lo siguiente:

```
python -m unittest discover -v -s tests
```



*Desarrollado por:*

* Francisco Perez Salgado
* Aitor Martínez Fernádez
