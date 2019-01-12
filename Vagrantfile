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
    # Precio estimado	34,68 $/mes
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