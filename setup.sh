# install dependencies
sudo apt -y install python3 python3-pip mongodb
sudo python3 -m pip install flask flask-cors pymongo

# sudo apt -y install nginx
sudo cp ./nginx.conf /etc/nginx/nginx.conf
sudo systemctl restart nginx

# install SSL certs by following this
# https://certbot.eff.org/lets-encrypt/ubuntufocal-nginx

# enable firewall permissions
sudo -- sh -c 'ufw --force enable; ufw status; ufw allow ssh; ufw allow http; ufw allow https;'

# set permissions on file as executable
chmod +x ./app.py

# run file in background
tmux
python3 ./app.py