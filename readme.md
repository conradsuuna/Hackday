# HACKDAY

## clone repo
git clone ...

## add .env file
touch .env

copy contents from .ENVEXAMPLE and paste them in .env

## create a virtual environment
python -m venv chosen_name

## activate virtual environment
source chosen_name/bin/activate

## install dependencies 
python -m pip install -r requirements.txt

## create database in Azure data studio
CREATE DATABASE named "hackday_db"

# For local usage (models)
### flask db init
Creates a new migration repository.

### flask db migrate
Autogenerate a new revision file (Alias for 'revision...

### flask db upgrade
Then you can apply the migration to the database (Upgrade to a later version)
<!-- flask db stamp head -->

## run project
flask run
or
python server.py







<!-- $python
>>> from project import db
>>> db.create_all()
run app
$python server.py -->