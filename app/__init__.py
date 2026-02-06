from flask import Flask
from flask_restx import Api
from .extensions import db
from config import DevelopmentConfig


def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    api = Api(app, version='1.0', title='Sample API',
              description='A sample API using Flask-RESTX')
    app.config.from_object(config_class)
    db.init_app(app)
    # namespaces à ajouter ici
    return app
