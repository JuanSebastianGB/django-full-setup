#!/bin/sh
# entrypoint.sh

# Exit immediately if a command exits with a non-zero status
set -e

# Apply database migrations
echo "Applying database migrations"
python manage.py migrate

# Start the server
echo "Starting server"
# Start the server based on the environment
if [ "$DJANGO_ENV" = "development" ]; then
  echo "Starting development server"
  exec python manage.py runserver 0.0.0.0:8000
else
  # Collect static files
  echo "Collecting static files"
  python manage.py collectstatic --noinput

  echo "Starting production server"
  exec gunicorn demo.wsgi:application --bind 0.0.0.0:8000 &
  wait
fi
