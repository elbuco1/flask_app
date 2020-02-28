from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
import logging as lg 
# from flask_migrate import Migrate
# from app.models import Movie



application = Flask(__name__)
application.config.from_object(Config)
db = SQLAlchemy(application)
# migrate = Migrate(application, db)

from app import routes, models



# flask initdb
@application.cli.command()
def initdb():
    models.init_db()

    

# uncomment to initialize database automatically for
# every run
# models.init_db()