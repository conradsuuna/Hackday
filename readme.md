create a virtualenv
$virtualenv env
activate virtualenv
$source env/bin/activate
install packages 
$pip3 install -r requirements.txt
create database called "hackday_db"
run commands[
    flask db init
    flask db migrate
    flask db upgrade
]
run app
$python server.py

$python
>>> from project import db
>>> db.create_all()
run app
$python server.py
