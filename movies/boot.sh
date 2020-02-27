#!/bin/sh
source venv/bin/activate
flask initdb
# flask translate compile
exec gunicorn -b :5000 --access-logfile - --error-logfile - movies:application