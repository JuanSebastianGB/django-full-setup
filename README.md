# Commands

```bash

# build the image
docker build -t webserver .
# run the container
docker run --rf -d -p 8080:80 --name web webserver

# List all processes
ps -C nginx -f

# Reload the configuration
nginx -s reload

# test dns resolution
nslookup ns.main.com

# Run development

docker-compose -f docker-compose.yml up --build

# Run production

docker-compose -f docker-compose.prod.yml up --build

```

URL
https://github.com/veryacademy/yt-nginx-mastery-series

For those experiencing the same error and using Ubuntu. Do the following after running docker compose build:
sudo systemctl stop systemd-resolved
sudo systemctl disable systemd-resolved

After that then run:
docker compose up

Will work.
NB. You will not be able to access the internet thus later you'll have to rollback the above commands by running :
sudo systemctl enable systemd-resolved
sudo systemctl start systemd-resolved
