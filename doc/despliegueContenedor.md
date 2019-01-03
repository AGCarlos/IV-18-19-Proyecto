
## Despliegue con contenedor

### Docker

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
### Heroku


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