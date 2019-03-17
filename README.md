# Localización de Viviviendas en imagen satélite

Proyecto de la asignatura Aplicaciones industriales y comerciales del [Máster de Visión Artificial](https://mastervisionartificial.es/).

Este proyecto consiste en desarrollar una aplicación web que localice casas en imágenes de satélite dadas por un usuario.

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

