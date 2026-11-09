import os
from urllib.parse import quote_plus
from dotenv import load_dotenv
# from datetime import timedelta

load_dotenv()


class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv('SECRET_KEY')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{
        os.getenv('DB_USER')}:{
            quote_plus(os.getenv('DB_PASSWORD'))}@localhost/kotools"
    JWT_COOKIE_SECURE = True
    JWT_ACCESS_COOKIE_NAME = "access_token_cookie"
    JWT_COOKIE_SAMESITE = "None"
    JWT_TOKEN_LOCATION = ["cookies"]


class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = 'dev-key'
    JWT_SECRET_KEY = 'jwt-dev-key'
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{
        os.getenv('DB_USER')}:{
            quote_plus(os.getenv('DB_PASSWORD'))}@localhost/kotools"
    JWT_COOKIE_SECURE = False
    JWT_ACCESS_COOKIE_NAME = "access_token_cookie"
    JWT_COOKIE_SAMESITE = "Strict"
    JWT_TOKEN_LOCATION = ["cookies"]
    JWT_COOKIE_CSRF_PROTECT = True


class TestingConfig(Config):
    TESTING = True
    SECRET_KEY = 'test-key'
    JWT_SECRET_KEY = 'jwt-test-key'
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
# :memory: est une valeur spéciale qui créera une db en RAM
# les fixtures de conftest prévoient que cette db sera créée
# par l'app factory (aap_create) sur cette config et supprimé après
# chaque test

# class ProdConfig(Config):


# ressources:
# https://www.geeksforgeeks.org/python/flask-environment-specific-configurations/
# https://flask.palletsprojects.com/en/stable/config/
