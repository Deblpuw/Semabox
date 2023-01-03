apt update && apt install dialog nmap curl chromium shellinabox nodejs npm
curl -sL https://deb.nodesource.com/setup_16.x | bash -
npm install --global fast-cli
mkdir outputs
shellinaboxd -p 4200 -m '*' -q --background=/var/run/shellinaboxd.pid -c /var/lib/shellinabox -u shellinabox -g shellinabox
python3 NetworkHealthCheck.py &