ITI Project - Crowdfunding (final)

Quick start (development):
1. python -m venv venv
2. source venv/bin/activate
3. pip install -r requirements.txt
4. python manage.py makemigrations
5. python manage.py migrate
6. python manage.py createsuperuser
7. python manage.py runserver

Notes:
- Set environment variables for Facebook/Stripe/reCAPTCHA keys in production.
- Admin: add Social App for Facebook via django-allauth admin.
