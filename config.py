"""Flask configuration."""
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))


class Config:
    """Base config."""

    SECRET_KEY = environ.get("SECRET_KEY")
    JWT_SECRET_KEY = environ.get("JWT_SECRET_KEY")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SWAGGER = {"title": "Hops API", "uiversion": 3, "version": "1.0"}


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = environ.get("PROD_DATABASE_URI")

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + path.join(basedir, 'database.db')
