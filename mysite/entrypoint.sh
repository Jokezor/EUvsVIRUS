#!/bin/sh

if [ "$DATABASE" = "postgis" ]
then
    echo "Waiting for postgis..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.5
    done

    echo "PostgreSQL started"
fi

python manage.py flush --no-input
sleep 1
python manage.py makemigrations
sleep1
python manage.py migrate test_2
sleep 2

exec "$@"
