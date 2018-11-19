
  

# Documentación

  

  

### Despliegue en Heroku

  

  

He seguido el siguiente [tutorial](https://github.com/datademofun/heroku-basic-flask) para el delpliegue de la aplicación de prueba en Heroku.

  

  

-  [Aplicación en Heroku](https://obrasmta.herokuapp.com/)

  

-  [Ejemplo obras JSON](https://obrasmta.herokuapp.com/datosObras/obra1)

  
  

- Archivos necesarios para el despliegue(de prueba): requirements.txt, runtime.txt, Procfile, app.py, obras.json y status.json.

  

  

### Archivos de configuración

#### Runtime

Usamos este archivo para especificar a Heroku que estamos desplegando una aplicación en un lenguaje (python en este caso) con una versión específica. Este archivo se encuentra en la raíz de la app y contiene lo siguiente:

```

python-3.6.6

```

#### requirements.txt

Archivo necesario para decirle a Heroku qué paquetes necesitamos que sean instalados, este archivo estaba creado antes, lo que hemos añadido es: gunicorn. El archivo contiene lo siguiente:

```

pytest

FLask

gunicorn

```

#### Procfile

Usamos este archivo para especificar a Heroku cómo iniciar nuestra app. Este archivo se encuentra en la raíz de la app y se declara el comando que debe de ejecutarse para iniciar la aplicación, en este caso con gunicorn (un servidor web) y opciones para log. El contenido del fichero es el siguiente:

```

web: gunicorn app:app --log-file=-

```

### Despliegue automático

  

Se ha vinculado la cuenta de github con heroku para los despliegues automáticos.

![despliegue](https://i.imgur.com/8mbUB1w.png)

  

### El proyecto

Actualmente se pueden acceder a obras diferentes a partir de /datosObra, por ejemplo:

  

-  [/datosObra/obra1](https://obrasmta.herokuapp.com/datosObras/obra1)

-  [/datosObra/obra2](https://obrasmta.herokuapp.com/datosObras/obra2)

  

Nos devuelve un archivo JSON con los datos de esa obra. En este momento sólo hay dos obras disponibles.

  

- La próxima idea es crear una estructura de datos que genere JSON de datos leídos en la base de datos de la aplicación.

### Configuración y despliegue de Docker
#### Introducción
Docker permite encapsular todo el entorno de trabajo, consiste en virtualización basada en contenedores
para aislar las aplicaciones entre sí en un sistema operativo compartido. Esto permite que las aplicaciones
se puedan ejecutar en cualquier entorno, ya sea físico o virtual.

Para la configuración, despliegue y configuraciones, he seguido las siguientes documentaciones oficiales:

-  [Instalación de Docker](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-18-04) 
- [Configuraciones de Docker](https://docs.docker.com/get-started/part2/#dockerfile)
- [Ejecución de Docker en Heroku](https://medium.com/travis-on-docker/how-to-run-dockerized-apps-on-heroku-and-its-pretty-great-76e07e610e22)

#### Archivos y configuraciones
Tras la instalación de Docker en Ubuntu, procedemos a configurar los archivos necesarios:

- Dockerfile: utilizado para automatizar la creación de una imagen de nuestra app, que contiene todo lo necesario para que pueda ser ejecutada.
```
# Use an official Python runtime as a parent image
FROM python:2.7-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]
```
Nota: es necesario tener el archivo `requirements.txt` 
##### Construyendo la imagen
Necesitamos el siguiente comando:
```
docker build -t nameContainer .
```
Después de construir la imagen, le asignamos un tag:
```
docker tag nameContainer migueltoledo9/iv-18-19-proyecto:tag
```
En este momento, ya tenemos nuestro contenedor preparado para subirlo a DockerHub con el siguiente comando:
```
docker push migueltoledo9/iv-18-19-proyecto:tag
```
Para ejecutar la aplicación:
```
docker run -p 4000:80 nameContainer
```

##### Construyendo la imagen de forma automática
En el caso de querer hacer cambios en nuestra aplicación, tenemos que seguir los pasos anteriores. Ahora vamos a automatizar ese proceso de forma que, se suben los archivos a nuestro Github y se construye de nuevo nuestra app.

![automated-build](https://i.imgur.com/covCsq5.png)

[Link del repositorio en DockerHub](https://hub.docker.com/r/migueltoledo9/iv-18-19-proyecto/)

Para usar la imagen desde cualquier máquina (debe de tener instalado Docker), se tiene que utilizar el siguiente comando:
```
docker run -p 4000:80 migueltoledo9/iv-18-19-proyecto:despliegue
```
#### Despliegue de la imagen en Heroku
Se ha creado otra app en Heroku llamada obrasmta-container. Ahora procedemos al despliegue, donde tenemos que seguir los siguientes pasos:

1. Creamos el archivo heroku.yml para decirle a Heroku que se va tratar de un contenedor, este archivo contiene la información de cómo se debe de construir el contenedor y como ejecutarse desde el Dockerfile.
El archivo heroku.yml contiene lo siguiente:
```
build:
  docker:
    web: Dockerfile
run:
web: gunicorn app:app --log-file=-
```
2. Identificamos el contenedor en el registro de Heroku:
```
heroku container:login
```
3. Construimos el Dockerfile y hacemos push de la imagen a la app creada en heroku (obrasmta-container):
```
heroku container:push web --app obrasmta-container
```
4. Desplegamos la aplicación:
```
heroku container:release web --app obrasmta-container
```
Una vez finalizados estos pasos, podemos encontrar la aplicación en el siguiente enlace: [Docker-Heroku-APP](https://obrasmta-container.herokuapp.com/)