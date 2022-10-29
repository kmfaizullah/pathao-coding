#!/bin/sh
set -e
python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput
python3 manage.py collectstatic --noinput
python3 manage.py compilemessages
exec "$@"
