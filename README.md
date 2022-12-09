Semabox :

Interface semi-graphique, fonctionne depuis le terminal
-> démarrer l'interface automatiquement à la connecter
user semabox -> /user/semaos/semaos.sh
user root -> default

Dépendances : 
dialog nmap curl chromium && fast

cronjob healthcheck :
*/5 * * * * python3 /user/semaos/net-hc.py

SemaLynx :
start shellinaboxd 
-> shellinaboxd -p 4200 -m '*' -q --background=/var/run/shellinaboxd.pid -c /var/lib/shellinabox -u shellinabox -g shellinabox 
