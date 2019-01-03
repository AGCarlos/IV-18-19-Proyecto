// Then use commands like:
//   fly deploy:production
//   fly stop:production
//   fly upgrade:production
var plan = require('flightplan');

plan.target('production', [
  {
    host: '35.239.72.203',
    username: 'migueltoledo',
    agent: process.env.SSH_AUTH_SOCK
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