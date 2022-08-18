## Roomie Project
## roomie-flask-server

Using Flask to build a Restful API Server for Roomie.

## Project setup
### Requirement software:
* python 3.8
* pip3
* Nodejs
* IDE, VSCode recommended
Virtual environment setup
```
$ pip3 install virtualenv && virtualenv venv
$ source venv/bin/activate
```
Flask setup
```
$ export FLASK_APP=app.py
$ export FLASK_ENV=development
```
## Installation

Install with pip:

```
$ pip install -r requirements.txt
```


#### Builtin Configuration Values

DATABASE_HOST: host of database in use, i.e. localhost, 127.0.0.1

DATABASE_PORT : port of database, i.e. 27017 (Mongo default)



## Run Flask
### Run flask for develop
```
$ flask run

