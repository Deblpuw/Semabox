apt update && install dialog nmap curl chromium shellinabox nodejs 
curl -sL https://deb.nodesource.com/setup_16.x | bash -
npm install --global fast-cli
mkdir outputs
python3 net-hc.py
crontab cron
shellinaboxd -p 4200 -m '*' -q --background=/var/run/shellinaboxd.pid -c /var/lib/shellinabox -u shellinabox -g shellinabox