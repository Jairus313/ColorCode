#!/bin/bash

# running server with 2 workers with each of 2 threads.
gunicorn --chdir ./ wsgi:app -w 2 --threads 2 

# running on specific ip and port with logs(development)
#--bind 0.0.0.0:8000 --access-logfile=access.log