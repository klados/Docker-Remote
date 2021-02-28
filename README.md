# Docker Remote 

## Introduction

This application allows you to ...

## setup:
* Create virtual environment `python3 -m venv env`
* Activate virtual env `source env/bin/activate`
* Install dependencies: `pip3 install -r requirements.txt`
* Start mysql: ` sudo systemctl start mysql`
* `cp env-example .env`
* Create database named `dockerremote`
* Run server: `gunicorn -w 2 --reload -b localhost:5000 "main:app"`
* Create a user and update his role to superAdmin manually