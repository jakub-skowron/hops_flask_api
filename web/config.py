from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))


class Config:
    SECRET_KEY = environ.get("SECRET_KEY", "oh_my_secret")
    JWT_SECRET_KEY = environ.get("JWT_SECRET_KEY", "oh_my_jwt_secret")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SWAGGER = {"title": "Hops API", "uiversion": 3, "version": "1.0"}


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = environ.get("DATABASE_URL", "sqlite:///database.db")


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = environ.get("DATABASE_URL")


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///test_data_base.db"
