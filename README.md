# Gestión de ObrasMTA

[![Build Status](https://travis-ci.com/maikeltoledo/IV-18-19-Proyecto.svg?branch=master)](https://travis-ci.com/maikeltoledo/IV-18-19-Proyecto)
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

Proyecto para la asignatura de Infraestructura Virtual (2018-2019)

### Descripción

Microservicio utilizado para la gestión de obras, donde nos permite:
- Altas, bajas y modificaciones de informes de obras.
- Cada informe contiene a trabajadores, gastos, material, fechas y pagos.
- Se almacenarán los informes y se pueden consultar.

### Uso
- En un futuro próximo, se usará en una empresa para llevar el control de obras.
- En este caso, se le añadirán más funcionalidades.

### Herramientas
- Base de datos: PostgreSQL
- Framework: Flask
- Sistema Log: módulo de Flask

### Test
Utilización de Pytest para realizar test en el proyecto. Los test se pasan a través de [Travis-CI](https://travis-ci.com/).
El archivo de los test se llama: test.py

### Despliegue
![Heroku](https://heroku-badge.herokuapp.com/?app=obrasmta)

He utilizado Heroku, actualmente hay una app de prueba en el siguiente enlace: [Despliegue Heroku](https://obrasmta.herokuapp.com/status)

### Documentación
La documentación la encontramos: [documentación](./doc/README.md)
