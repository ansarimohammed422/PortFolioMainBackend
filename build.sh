#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

# This command uses the STATIC_ROOT we just defined
python manage.py collectstatic --no-input

python manage.py migrate
