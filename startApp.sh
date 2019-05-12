#! /bin/bash
nohup gunicorn -b 0.0.0.0:5556 wsgi:app &
