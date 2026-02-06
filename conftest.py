# conftest.py à la racine du projet
import sys
from pathlib import Path
import pytest
from flask import Flask
from flask_restx import Api
from app.extensions import db

sys.path.append(str(Path(__file__).resolve().parent))


@pytest.fixture
def app():
    app = Flask(__name__)
    api = Api(app, version='1.0', title='Sample API',
              description='A sample API using Flask-RESTX')
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///memory.db"
    db.init_app(app)
    # namespaces à ajouter ici
    return app


@pytest.fixture
def run():
    app = app()

    if __name__ == '__main__':
        with app.app_context():
            db.create_all()
            yield db
            db.drop_all()
        app.run(debug=True)



@pytest.fixture
def user():
    return {
        'firstname': 'Mathieu',
        'lastname': 'Mjr',
        'email': 'trulu@yopla.fr',
        'password': '123mdp!',
        'role': False
        }


@pytest.fixture
def admin():
    return {
        'firstname': 'Diana',
        'lastname': 'Boss',
        'email': 'owow@kotools.fr',
        'password': '0000lol',
        'role': False
        }
