cd ..
python --version
python3 -m venv venv
source venv/bin/activate
cd src
waitress-serve --listen=*:8000 cfehome.wsgi:application