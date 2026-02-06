class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'default'
    SQLALCHEMY_DATABASE_URI = "sqlite:///project.db"


class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = 'dev-key'
    SQLALCHEMY_DATABASE_URI = "sqlite:///project.db"


class TestingConfig(Config):
    TESTING = True
    SECRET_KEY = 'test-key'
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
# :memory: est une valeur spéciale qui créera une db en RAM
# les fixtures de conftest prévoient que cette db sera créée
# par l'app factory (aap_create) sur cette config et supprimé après
# chaque test

# class ProdConfig(Config):


# ressources:
# https://www.geeksforgeeks.org/python/flask-environment-specific-configurations/
# https://flask.palletsprojects.com/en/stable/config/
