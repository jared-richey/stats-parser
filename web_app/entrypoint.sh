#!/bin/bash

# Start the cron daemon in the background
/usr/sbin/crond &

# Start the django web server
python3 manage.py runserver 0.0.0.0:8000