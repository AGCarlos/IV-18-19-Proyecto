
## Despliegue en Heroku

He seguido el siguiente [tutorial](https://github.com/datademofun/heroku-basic-flask) para el delpliegue de la aplicación de prueba en Heroku.

-  [Aplicación en Heroku](https://obrasmta.herokuapp.com/)

-  [Ejemplo: Listar todas las obras de la BD](https://obrasmta.herokuapp.com/AllObras)

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
pymongo
```

#### Procfile

Usamos este archivo para especificar a Heroku cómo iniciar nuestra app. Este archivo se encuentra en la raíz de la app y se declara el comando que debe de ejecutarse para iniciar la aplicación, en este caso con gunicorn (un servidor web) y opciones para log. El contenido del fichero es el siguiente:

```
web: gunicorn app:app --log-file=-
```

  
### Despliegue automático
  

Se ha vinculado la cuenta de github con heroku para los despliegues automáticos.


![despliegue](https://i.imgur.com/8mbUB1w.png)

 