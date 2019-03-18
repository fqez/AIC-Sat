# Localización de Viviviendas en imagen satélite

Proyecto de la asignatura Aplicaciones industriales y comerciales del [Máster de Visión Artificial](https://mastervisionartificial.es/).

Este proyecto consiste en desarrollar una aplicación web que localice casas en imágenes de satélite dadas por un usuario.

## Requisitos de ejecución

Para ejecutar el sistema es necesario disponer de un equipo con CPU relativamente moderna que soporte el conjunto de instrucciones de TensorFlow.
Además el sistema funciona bajo sistemas Linux, con distribución Ubuntu 18.04 LTS.

## Entorno virtual

Se recomienda trabajar dentro de un entorno virtual de Python 3.7 por seguridad y comodidad.

### Creación del entorno

Para empezar a trabajar en un entorno virtual, se requiere tener instalado alguna versión de Python 3 (recomendado Python 3.5 o 3.7) y ejecutar:

```
python3 -m venv /ruta/al/entorno/virtual
```

con esto se generará el entorno virtual en la ruta especificada

### Activar entorno virtual

Una vez creado el entorno virtual, para trabajar en una consola dentro de él hay que activarlo de la siguiente forma

```
source /ruta/al/entorno/virutal/bin/activate
```

Observa que el prompt cambia, lo que te indicará que ya estás dentro del entorno virtual.

## Dependencias
### Instalar dependencias
Para instalar la dependencias ejecuta el siguiente comando.

```
pip install -r requirements.txt
```

### Descargar modelo
Descarga en *model* el modelo de la red de [este link](https://drive.google.com/open?id=1RFjABoLp6UUU4a0ZNF-klZRo_z1lqo5C)

## Tests
### Descargar los datos necesarios para los test
Ejecuta lo siguiente:
```
./scripts/prepare_test.sh
```

### Ejecutar los test
Ejecuta lo siguiente:
```
python -m unittest discover -v -s tests
```



 



## Desarrollado por:

* Francisco Perez Salgado
* Aitor Martínez Fernádez

