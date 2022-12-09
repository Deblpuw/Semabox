Semabox :

Interface semi-graphique, fonctionne depuis le terminal
-> démarrer l'interface automatiquement à la connecter
user semabox -> /home/semabox/Semabox/semaos.sh
user root -> default

Dépendances : 
dialog nmap curl chromium shellinabox && fast

git clone https://github.com/Teth-IO/Semabox
cd Semabox
mkdir outputs

cronjob healthcheck :
*/5 * * * * python3 /home/semabox/Semabox/net-hc.py

start shellinaboxd 
-> shellinaboxd -p 4200 -m '*' -q --background=/var/run/shellinaboxd.pid -c /var/lib/shellinabox -u shellinabox -g shellinabox 
