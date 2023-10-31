#!/usr/bin/env bash
#exit on error
set -o errexit
chmod +x build.sh
cd ..
python --version
pip install pip pip-tools rav --upgrade
src/requirements/requirements.in -o src/requirements.txt
pip install -r src/requirements.txt
npm install
-m pip freeze
cd src
python manage.py collectstatic --noinput
python manage.py migrate
