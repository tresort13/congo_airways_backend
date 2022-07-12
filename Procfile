web: gunicorn congo_airways_backend.wsgi
heroku ps:scale web=1
release: python manage.py makegrations --noinput
release: python manage.py migrate --noinput

