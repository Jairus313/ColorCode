#!/bin/bash
gunicorn --chdir ./ wsgi:app -w 2 --threads 2 
#--bind 0.0.0.0:8000 --access-logfile=access.log