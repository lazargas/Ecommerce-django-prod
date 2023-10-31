c:\Python310\python.exe -m venv venv
.\venv\Scripts\activate
python -m pip install pip pip-tools rav --upgrade
rav run win_installs
rav run win_freeze
cd src
python manage.py collectstatic
python manage.py migrate
waitress-serve --listen=*:8000 cfehome.wsgi:application