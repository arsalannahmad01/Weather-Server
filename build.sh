#!/usr/bin/env bash

set -o errexit  # exit on error

pip3 install darkskylib --upgrade --no-cache- --force-reinstall
pip3 install -r requirements.txt

python3 manage.py collectstatic
python3 manage.py collectstatic --no-input
python3 manage.py migrate
