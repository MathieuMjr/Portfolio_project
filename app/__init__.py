from flask import Flask
from flask_restx import Api
from .extensions import db


def create_app():
    app = Flask(__name__)
    api = Api(app, version='1.0', title='Sample API',
              description='A sample API using Flask-RESTX')
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
    db.init_app(app)
    # namespaces à ajouter ici
    return app
