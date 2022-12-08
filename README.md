Semabox :

Interface semi-graphique, fonctionne depuis le terminal
-> démarrer l'interface automatiquement à la connecter
user semabox -> /user/semaos/semaos.sh
user root -> default

Dépendances : 
dialog nmap curl

cronjob healthcheck :
*/5 * * * * python3 /user/semaos/net-hc.py
