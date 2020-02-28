import os

class Config(object):
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'

    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://movies:movies@localhost:3306/movies'
    # SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

