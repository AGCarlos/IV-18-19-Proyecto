
# Gestión de ObrasMTA

[![Build Status](https://travis-ci.com/maikeltoledo/IV-18-19-Proyecto.svg?branch=master)](https://travis-ci.com/maikeltoledo/IV-18-19-Proyecto)

[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)


Proyecto para la asignatura de Infraestructura Virtual (2018-2019)


### Descripción

Microservicio utilizado para la gestión de obras, donde nos permite:

- Altas y listado de informes de obras.

- Cada informe el nombre de la obra, precio, descripción, si está activa o no, tipo de pago, materiales usados y horas de mano de obra.
- Se almacenarán los informes y se pueden consultar.

  
### Uso

- [Documentación para el uso de obrasMTA](https://github.com/maikeltoledo/IV-18-19-Proyecto/blob/master/doc/usoApp.md)

### Herramientas

- Base de datos: [MongoDB](https://www.mongodb.com/es)

- Framework de Python: [Flask](http://flask.pocoo.org/)

- Sistema Log: módulo de Flask


### Test

Utilización de Pytest para realizar test en el proyecto. Los test se pasan a través de [Travis-CI](https://travis-ci.com/).

El archivo de los test se llama: test.py

- Para pasar los test usamos: ``` $ pytest test.py  ```  
- Para usar la app: ``` $ python3 app.py   ```

### Despliegue

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://obrasmta.herokuapp.com)

He utilizado Heroku, actualmente hay una app de prueba en el siguiente enlace: [Despliegue Heroku](https://obrasmta.herokuapp.com/)

  

### Aplicación desplegada en Heroku con Docker

- Enlace a DockerHub: [App en DockerHub](https://hub.docker.com/r/migueltoledo9/iv-18-19-proyecto/)

- Contenedor: [Aplicación en Heroku](https://obrasmta-container.herokuapp.com/)

### Despliegue en Google Cloud

- Despliegue final: 35.246.89.231

### Documentación desglosada

La documentación de cada parte del proyecto la encontramos: [Glosario](./doc/README.md)