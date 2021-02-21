import os


class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = os.getenv('DEBUG')
    DEVELOPMENT = os.getenv('DEBUG')
    SECRET_KEY = os.getenv('SECRET_KEY')
    FLASK_SECRET = SECRET_KEY
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + os.getenv('MYSQL_DATABASE_USER') + ':' + os.getenv(
        'MYSQL_DATABASE_PASSWORD') + '@' + os.getenv('MYSQL_DATABASE_HOST') + '/' + os.getenv('MYSQL_DATABASE_DB')
