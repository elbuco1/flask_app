import os

class Config(object):
    basedir = os.path.abspath(os.path.dirname(__file__))
    evaluations_url = "http://127.0.0.1:8001"
    # evaluations_url = "http://127.0.0.1:5001"

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

