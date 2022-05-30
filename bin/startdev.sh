#!/bin/bash
pip install -r ./requirements.txt --use-deprecated=legacy-resolver
./manage.py migrate
./manage.py runserver 0.0.0.0:8000
