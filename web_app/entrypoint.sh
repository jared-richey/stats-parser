#!/usr/bin/env bash

# Start the cron daemon in the background
/usr/sbin/crond &

# Start the web server and listen on port 8000 for all interfaces
python3 manage.py runserver 0.0.0.0:8000