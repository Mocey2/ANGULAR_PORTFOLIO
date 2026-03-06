#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input --clear

python manage.py migrate

python manage.py load_initial_data

python manage.py createsuperuser --noinput --email "${DJANGO_SUPERUSER_EMAIL:-admin@example.com}" --username "${DJANGO_SUPERUSER_USERNAME:-admin}" 2>/dev/null || true
