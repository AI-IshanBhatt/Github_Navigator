#!/usr/bin/env bash
#!/bin/bash

NAME="Github_Navigator"
USER=ishanbhatt
GROUP=domain
NUM_WORKERS=5
WORKERTYPE="gevent"

echo "Starting $NAME"

# Start your gunicorn
exec gunicorn runserver:app -b 0.0.0.0:5050 \
  --name $NAME \
  --workers $NUM_WORKERS \
  -k $WORKERTYPE \
  --log-file /home/ishanbhatt/CeleraOne/logs/gunicorn.log \
  --log-level INFO