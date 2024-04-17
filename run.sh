python -m venv ./venv
source ./venv/bin/activate
pip install -r requirements.txt --upgrade
python -m webbrowser http://127.0.0.1:5000
python -m wsgi