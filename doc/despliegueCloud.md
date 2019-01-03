## Despliegue en Google Cloud


He seguido los siguientes enlaces:

 - [Tutorial 1](https://github.com/mitchellh/vagrant-google) 
 - [Tutorial 2](https://blog.eduonix.com/system-programming/learn-use-vagrant-cloud/)

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

    google.image_family = 'ubuntu-1604-lts'
    google.name = 'obrasmta'

    override.ssh.username = "migueltoledo"
    override.ssh.private_key_path = "~/.ssh/id_rsa"
  end

  config.vm.provision :ansible do |ansible|
      ansible.playbook = "provision/playbook.yml"
  end

end
```

#### Donde:
- PROJECT_ID: id del proyecto
- CLIENT_EMAIL: email asociado, en este caso es .....@developer.gserviceaccount.com
- JSON_KEY_LOCATION = ubicación del private.json que nos hemos descargado anteriormente.
- google.image_family: distribución que quiero usar, en este caso Ubuntu 16.04
- google.name: nombre de la máquina (obrasmta)
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
  end
```

Le indicamos la ubicación del archivo playbook.yml, este archivo es necesario para instalar las dependencias que necesita nuestra app. 

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

![puestaEnMarcha](https://i.imgur.com/v0lPzip.jpg)

Ahora tenemos que configurar una ip estática en el apartado de "Direcciones IP externas", en el apartado Tipo, cambiamos de tipo efímera (no es fija, puede cambiar) y estática para un mejor funcionamiento.

- [Tutorial para esta mejora](https://beseomyfriend.com/configurar-ip-estatica-google-cloud/)

También abrimos el puerto 80 de nuestra máquina, en el apartado de VM, configuramos "obrasmta" y permitimos el tráfico HTTP.

#### Despliegue

Para el despliegue he usado [Flightplan](https://github.com/pstadler/flightplan)  con ayuda de este [Tutorial](https://johnmunsch.com/2015/03/08/shipit-vs-flightplan-for-automated-administration/) y la web oficial para su uso y configuración.

Creamos el archivo flightplan.js para poner en marcha nuestra máquina. En este archivo vamos a definir una serie de funciones que nos permitirá ejecutar ordenes en la máquina a través de SSH. Podremos desplegar nuestra app, parar el servidor gunicorn y actualizar el servidor.

El archivo es el siguiente:
```
// Then use commands like:
// fly deploy:production
// fly stop:production
// fly upgrade:production
var  plan  =  require('flightplan');

plan.target('production', [
	{
		host:  '35.239.72.203',
		username:  'migueltoledo',
		agent:  process.env.SSH_AUTH_SOCK
	}
]);

//run the gunicorn server
plan.remote('deploy', function(remote) {
	remote.log('run the gunicorn server');
	remote.exec('cd app && sudo gunicorn app:app -b 0.0.0.0:80');
});

//stop the gunicorn server
plan.remote('stop', function(remote) {
	remote.log('stop the gunicorn server');
	remote.sudo('pkill -f gunicorn');
});

// Upgrade Ubuntu to the latest.
plan.remote('upgrade', function(remote) {
	remote.log('Fetches the list of available Ubuntu upgrades.');
	remote.sudo('apt-get update');
	// And then actually does them.
	remote.sudo('apt-get -y dist-upgrade');
});
```

- Tenemos una primera función 'production' usada para conectarnos a nuestra máquina.
- Función 'deploy' para ejecutar nuestra aplicación.
- Función 'stop' para parar el servidor gunicorn.
- Función 'upgrade' para actualizar nuestro servidor

El modo de llamar a las distintas funciones desde la línea de comandos es:
- Desplegar: fly deploy:production
- Parar gunicorn: fly stop:production
- Actualizar la máquina: fly upgrade:production

Por último ya podemos acceder a la app a través de: [DIRECCION_IP]() y en mi documentación hay un [modo de uso](https://github.com/maikeltoledo/IV-18-19-Proyecto/tree/master/doc/usoApp.md) para utilizarla.