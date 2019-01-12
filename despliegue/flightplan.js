//////////////////////////////////////
// --- Comandos para su uso ---     //
//      fly ejecuta:obrasmta        //
//      fly status-mongodb:obrasmta //
//      fly actualiza:obrasmta      //
//////////////////////////////////////
var plan = require('flightplan');

plan.target('obrasmta', [
  {
    host: '35.246.89.231',
    username: 'migueltoledo',
    agent: process.env.SSH_AUTH_SOCK
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