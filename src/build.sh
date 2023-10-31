#!/usr/bin/env bash
#exit on error
set -o errexit
cd..
python3 -m venv venv
source venv/bin/activate
venv/bin/python -m pip install pip pip-tools rav --upgrade
venv/bin/rav run installs
rav run freeze
cd src
python manage.py collectstatic
python manage.py migrate
