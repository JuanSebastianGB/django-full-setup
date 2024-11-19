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


# Run development

docker-compose -f docker-compose.yml up --build

# Run production

docker-compose -f docker-compose.prod.yml up --build

```
