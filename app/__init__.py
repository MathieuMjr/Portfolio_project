from flask import Flask
from flask_cors import CORS
from flask_restx import Api
from .extensions import db, jwt, bcrypt
from config import DevelopmentConfig, Config
from app.api.users import api as users_ns
from app.api.login import api as login_ns
from app.api.structures import api as structures_ns
from app.api.reservations import api as reservations_ns
from app.api.struct_types import api as struct_types_ns
from app.api.statuses import api as statuses_ns
from app.api.res_types import api as res_types_ns
from app.api.audience_types import api as audience_types_ns
from jwt.exceptions import ExpiredSignatureError
from flask_jwt_extended.exceptions import (InvalidHeaderError,
                                           NoAuthorizationError)


def create_app(config_class=Config):
    app = Flask(__name__)
    api = Api(app, version='1.0', title='Sample API',
              description='A sample API using Flask-RESTX',
              doc='/api/')
    app.config.from_object(config_class)
    db.init_app(app)
    jwt.init_app(app)
    bcrypt.init_app(app)

    @api.errorhandler(ExpiredSignatureError)
    def handle_expired_token(error):
        return {'error': 'Token expiré, veuillez vous reconnecter'}, 401

    @api.errorhandler(NoAuthorizationError)
    def handle_missing_token(error):
        return {'error': 'Token manquant'}, 401

    @api.errorhandler(InvalidHeaderError)
    def handle_invalid_token(error):
        return {'error': 'Token invalide'}, 401

    CORS(app, resources={r"/api/*": {"origins": "http://localhost:5500"}})

    api.add_namespace(users_ns, path='/api/users')
    api.add_namespace(login_ns, path='/api/login')
    api.add_namespace(structures_ns, path='/api/structures')
    api.add_namespace(reservations_ns, path='/api/reservations')
    api.add_namespace(struct_types_ns, path='/api/struct_types')
    api.add_namespace(statuses_ns, path='/api/statuses')
    api.add_namespace(res_types_ns, path='/api/res_types')
    api.add_namespace(audience_types_ns, path='/api/audience_types')

    return app
