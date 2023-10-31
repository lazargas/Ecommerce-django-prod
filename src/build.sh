#!/usr/bin/env bash
#exit on error
set -o errexit
c:\Python310\python.exe -m venv venv
.\venv\Scripts\activate
python -m pip install pip pip-tools rav --upgrade
pip-compile src/requirements/requirements.in -o src/requirements.txt
python -m pip install -r src/requirements.txt
npm install
python -m pip freeze
python manage.py collectstatic
python manage.py migrate