
## Despliegue en Google Cloud

  
  

He seguido los siguientes enlaces:

  

-  [Vagrant Google Compute Engine](https://github.com/mitchellh/vagrant-google)

-  [Tutorial](https://blog.eduonix.com/system-programming/learn-use-vagrant-cloud/)

  

para el despliegue de la aplicación de prueba en Google Cloud.

  

### Configuración de Google Cloud

  

#### Creación de cuenta y proyecto

  

Primeramente nos registramos en Google Cloud y crear un proyecto donde se instanciará nuestra máquina para que funcione la app.

  

#### Configuración para acceder a la API

  

Una vez que tenemos la cuenta habilitada, debemos crear una cuenta de servicio para el acceso a la API, se generará un archivo en formato JSON con todas las credenciales de acceso, Email, ID del proyecto, entre otros.

  

Usaremos estos datos para configurar el Vagranfile

  

#### Configuración de Vagranfile

  

Para usar vagrant, es recomendable instalarlo descargando el instalador de la [web oficial](https://www.vagrantup.com/downloads.html)

  

Una vez instalado, instalamos el plugin de google de la siguiente forma:

```

$ vagrant plugin install vagrant-google

```

  

Ahora configuramos el vagranfile de la siguiente forma:

  

```

Vagrant.configure("2") do |config|
  config.vm.box = "google/gce"

  config.vm.provider :google do |google, override|
    google.google_project_id = ENV['PROJECT_ID']
    google.google_client_email = ENV['CLIENT_EMAIL']
    google.google_json_key_location = ENV['JSON_KEY_LOCATION']

    # Última versión de la familia ubuntu-1804-lts
    google.image_family = 'ubuntu-1804-lts'
    # Nombre de la instancia
    google.name = 'obrasmta'
    # Zona: London
    google.zone = 'europe-west2-a'
    # Tipo de máquina (1 vCPU con 3,75 GB de memoria)
    # Precio estimado $31.27 $/mes
    google.machine_type = 'n1-standard-1'

    # Opciones para disco (10GB, SSD y nombre: ssd0brasmta)
    # Precio mensual del disco 0,40 $/mes
    google.disk_size = 10
    google.disk_name = 'ssd0brasmta'
    google.disk_type = 'pd-ssd'

    # Ip pública estática reservada
    google.external_ip = '35.246.89.231'
    # Permitir http en el cortafuegos
    google.tags = ['http-server']

    override.ssh.username = "migueltoledo"
    override.ssh.private_key_path = "~/.ssh/id_rsa"
  end

  config.vm.provision :ansible do |ansible|
      ansible.playbook = "provision/playbook.yml"
      # Como Ubuntu 18.04.1 incluye Python 3 (pero no Python 2), 
      # es necesario indicar a Ansible que utilice python3.
      ansible.extra_vars = {
        ansible_python_interpreter: "/usr/bin/python3",
      }
  end

end
```

  

#### Donde:

- PROJECT_ID: id del proyecto

- CLIENT_EMAIL: email asociado, en este caso es .....@developer.gserviceaccount.com

- JSON_KEY_LOCATION = ubicación del private.json que nos hemos descargado anteriormente.

##### Opciones de la instancia:

- google.image_family: última versión de la familia Ubuntu 18.04 lts 

- google.name: nombre de la instancia (obrasmta)
- google.zone: la zona por defecto es US, yo he establecido que sea Europa, en concreto la de Londres.
- google.machine_type: es el tipo de máquina, en mi caso he usado la "n1-standard-1" que tiene 1vCPU con 3,75 GB de RAM y el precio mensual es de $31.27 ( [Lista de precios por zonas](https://cloud.google.com/compute/pricing?hl=es) ).
-  google.disk_size: tamaño del disco, en mi caso he elegido 10 GB.
- google.disk_name: nombre del disco "ssd0brasmta"
- google.disk_type: tipo de disco, en mi caso SSD. Tiene un precio de 0,40 $/mes.
- google.external_ip: ip pública para asignar a la instancia (35.246.89.231)
- google.tags: opciones para la instancia, en mi caso solo le paso "http-server" para permitir http en el cortafuegos, pero se pueden configurar muchas más opciones.

- override.ssh.username: usuario para la conexión por SSH

- override.ssh.private_key_path: ubicación de las claves para la conexión por SSH

- config.vm.provision: provisionamiento con ansible, se explica a continuación

  
  

Fuente para la construcción del archivo: [Web Oficial](https://github.com/mitchellh/vagrant-google#quick-start)

  

#### Provisionamiento

  

Para el provisionamiento he usado [Ansible](https://www.ansible.com/), para su configuración me he guiado de [Vagrantup](https://www.vagrantup.com/docs/provisioning/ansible.html).

  

Se usa en el archivo Vagrantfile de la siguiente forma:

  

```

  config.vm.provision :ansible do |ansible|
      ansible.playbook = "provision/playbook.yml"
      # Como Ubuntu 18.04.1 incluye Python 3 (pero no Python 2), 
      # es necesario indicar a Ansible que utilice python3.
      ansible.extra_vars = {
        ansible_python_interpreter: "/usr/bin/python3",
      }
  end

```

  

- Le indicamos la ubicación del archivo playbook.yml, este archivo es necesario para instalar las dependencias que necesita nuestra app.
- Para que Ansible (utiliza python 2) funcione en Ubuntu 18.04, hay que decirle con la opción "ansible_python_interpreter", la ubicación de python3 para que lo use.

Tutoriales para la solución de Ansible en Ubuntu 18.04:  [Github](https://github.com/phingofficial/phing/issues/712) y [mclibre](http://www.mclibre.org/consultar/webapps/lecciones/ansible-1.html)

#### Explicando el archivo playbook.yml

  

- Ejecutamos todos los comandos como sudo, gracias a "become: yes".

- Actualizamos nuestra máquina.

- Instalamos git, python3-pip y mongodb.

- Clonamos mi repositorio de GitHub.

- Instalamos lo requisitos de la app que se encuentran en requirements.txt

  

El archivo contiene:

```
- hosts: all
remote_user: vagrant
become: yes

tasks:
	- name: Actualizar la máquina
	command: sudo apt-get update

	- name: Instalar Git, pip3 y mongodb
	command: sudo apt-get -y install git python3-pip mongodb

	- name: Clonar el repositorio de GitHub
	git: repo=https://github.com/maikeltoledo/IV-18-19-Proyecto.git dest=app/

	- name: Instalar los requisitos de la app
	command: pip3 install -r app/requirements.txt

```

  

#### Puesta en marcha

  

Llegados a este punto, podemos crear nuestra máquina definida en el archivo Vagrantfile e instalar las dependencias necesarias para ponerla en marcha. Todo esto lo hacemos con el siguiente comando:


```
vagrant up --provider=google
```

![puestaEnMarcha](https://i.imgur.com/XUEvL4Y.jpg)

  

#### Despliegue

  

Para el despliegue he usado [Flightplan](https://github.com/pstadler/flightplan) con ayuda de este [Tutorial](https://johnmunsch.com/2015/03/08/shipit-vs-flightplan-for-automated-administration/) y la web oficial para su uso y configuración.

  

Creamos el archivo flightplan.js para poner en marcha nuestra máquina. En este archivo vamos a definir una serie de funciones que nos permitirá ejecutar ordenes en la máquina a través de SSH. Podremos desplegar nuestra app, parar el servidor gunicorn y actualizar el servidor.

  

El archivo es el siguiente:

```
var plan = require('flightplan');

plan.target('obrasmta', [
{
	host:  '35.246.89.231',
	username:  'migueltoledo',
	agent:  process.env.SSH_AUTH_SOCK
}
]);

// Ejecutar el servidor gunicorn
plan.remote('ejecuta', function(remote) {
	remote.log('Ejecuta el servidor gunicorn');
	remote.exec('cd app && sudo gunicorn app:app -b 0.0.0.0:80');
});

// Estado de MongoDB
plan.remote('status-mongodb', function(remote) {
	remote.log('Estado de mongodb');
	remote.sudo('/etc/init.d/mongodb status');
});

// Actualizar Ubuntu
plan.remote('actualiza', function(remote) {
	remote.log('Buscar actualizaciones para Ubuntu');
	remote.sudo('apt-get update');
	remote.sudo('apt-get -y dist-upgrade');
});
```

  

- Tenemos una primera función 'obrasmta' usada para conectarnos a nuestra máquina en Google Cloud.

- Función 'ejecuta' para ejecutar nuestra aplicación.

- Función 'status-mongodb' para parar el estado de MondoDB.

- Función 'actualiza' para actualizar nuestro servidor Ubuntu 18.04

  

El modo de llamar a las distintas funciones desde la línea de comandos es:

- Ejecutar: fly ejecuta:obrasmta

- Estado de MongoDB: fly status-mongodb:obrasmta

- Actualizar la máquina: fly actualiza:obrasmta

  

Por último ya podemos acceder a la app a través de: [35.246.89.231](http://35.246.89.231/) y en mi documentación hay un [modo de uso](https://github.com/maikeltoledo/IV-18-19-Proyecto/tree/master/doc/usoApp.md) para utilizarla.