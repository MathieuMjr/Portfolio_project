from flask import Flask
from flask_restx import Api
from .extensions import db, jwt, bcrypt
from config import DevelopmentConfig
from app.api.users import api as users_ns
from app.api.login import api as login_ns
from app.api.structures import api as structures_ns
from app.api.reservations import api as reservations_ns


def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    api = Api(app, version='1.0', title='Sample API',
              description='A sample API using Flask-RESTX',
              doc='/api/')
    app.config.from_object(config_class)
    db.init_app(app)
    jwt.init_app(app)
    bcrypt.init_app(app)

    # namespaces à ajouter ici
    api.add_namespace(users_ns, path='/api/users')
    api.add_namespace(login_ns, path='/api/login')
    api.add_namespace(structures_ns, path='/api/structures')
    api.add_namespace(reservations_ns, path='/api/reservations')

    return app
