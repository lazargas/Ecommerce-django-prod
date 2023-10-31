cd ..
python --version
python3 -m venv venv
source venv/bin/activate
venv/bin/python cd src
venv/bin/python waitress-serve --listen=*:8000 cfehome.wsgi:application