import os

class Config(object):
    basedir = os.path.abspath(os.path.dirname(__file__))
    

    # Uncomment the desired option
    # deploy = 'docker'   # deploying on docker using mysql
    # deploy = 'mysql_local' # deploying locally using mysql
    deploy = 'sqlite_local' # deploying locally using sqlite


    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'

    if deploy == 'docker':
        SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://movies:movies@db/movies'
    elif deploy == 'mysql_local':
        SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://movies:movies@localhost:32000/movies'

    SQLALCHEMY_TRACK_MODIFICATIONS = False

