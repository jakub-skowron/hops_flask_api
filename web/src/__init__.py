from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flasgger import Swagger

from config import DevelopmentConfig
from src.config.swagger import swagger_config


db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    Swagger(app, config=swagger_config)

    from src.blueprints import blueprints
    
    for blueprint in blueprints.blueprint_list:
        app.register_blueprint(blueprint)

    return app

import src.auth.models
import src.hops.models
