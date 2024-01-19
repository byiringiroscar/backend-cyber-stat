
# Introduction

Project Cybersecurity statistics endpoint
Template is written with django 5 and python 3.9 in mind.

![Default Home View](__screenshots/home.png?raw=true "Title")

### Main features

* Separated dev and production settings

* CRUD Endpoints information

* Procfile for easy deployments

* Separated requirements files

* SQLite by default if no env variable is set

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/byiringiroscar/backend-cyber-stat.git
$ cd backend-cyber-stat.git
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd backend-cyber-stat
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/swagger/` for API documentation.
