#!/usr/bin/env bash

source env/bin/activate

set -o errexit  # exit on error

pip3 install -r requirements.txt

python3 manage.py collectstatic
python3 manage.py collectstatic --no-input
python3 manage.py migrate