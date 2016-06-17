#!/usr/bin/env bash

python manage.py migrate --fake-initial --noinput --settings=$DJANGO_SETTINGS_MODULE


python manage.py initadmin --username=admin --password=yz2rsMcaj3UJ3daRswBd --settings=$DJANGO_SETTINGS_MODULE

python manage.py add_sites --settings=$DJANGO_SETTINGS_MODULE

# celery flower

# debugging with default server uncomment this and comment the gunicorn one
# python manage.py runserver 0.0.0.0:3000 --settings=$DJANGO_SETTINGS_MODULE


exec  gunicorn --bind=0.0.0.0:90 dockertestproject.wsgi \
        --workers=5\
        --log-level=info \
        --log-file=-\
        --access-logfile=-\
        --error-logfile=-\
        --timeout 30\
        --reload
