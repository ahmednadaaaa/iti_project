#!/usr/bin/env bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
echo "Create superuser with: python manage.py createsuperuser"
echo "Run server with: python manage.py runserver"
