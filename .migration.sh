#!/bin/sh

docker-compose exec django python3 manage.py makemigrations login
docker-compose exec django python3 manage.py makemigrations real
docker-compose exec django python3 manage.py migrate login
docker-compose exec django python3 manage.py migrate real
docker-compose exec django python3 manage.py migrate auth
docker-compose exec django python3 manage.py migrate --noinput
docker-compose exec django python3 manage.py collectstatic --no-input
