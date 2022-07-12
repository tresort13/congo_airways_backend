web: gunicorn congo_airways_backend.wsgi
heroku ps:scale web=1
python manage.py migrate
