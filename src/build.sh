#!/usr/bin/env bash
#exit on error
set -o errexit
sudo apt-get update
sudo apt-get install -y python3.8
cd ..
python3 -m venv venv
source venv/bin/activate
venv/bin/python -m pip install pip pip-tools rav --upgrade
venv/bin/pip-compile src/requirements/requirements.in -o src/requirements.txt
venv/bin/python -m pip install -r src/requirements.txt
npm install
venv/bin/python -m pip freeze
cd src
python manage.py collectstatic
python manage.py migrate
