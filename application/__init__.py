import os
from flask import Flask
from sqlalchemy import create_engine

from config import Config
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv, find_dotenv
from sqlalchemy.ext.declarative import declarative_base

db = SQLAlchemy()
Base = declarative_base()


def create_app():
    print('start of the application')
    myApp = Flask(__name__)
    load_dotenv(find_dotenv())
    myApp.config.from_object(Config)

    global db
    db.init_app(myApp)
    engine = create_engine(Config.SQLALCHEMY_DATABASE_URI, convert_unicode=True)

    import application.models.user
    Base.metadata.create_all(engine)
    return myApp


app = create_app()
from application import routes
