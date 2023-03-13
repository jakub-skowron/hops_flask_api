from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flasgger import Swagger
from flask_sqlalchemy import SQLAlchemy

from config import ProductionConfig, DevelopmentConfig
from src.config.swagger import swagger_config


db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

#Switch between ProductionConfig and DevelopmentConfig
def create_app(config_class=ProductionConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    Swagger(app, config=swagger_config)

    from src.blueprints.blueprints import blueprint_list
    
    for blueprint in blueprint_list:
        app.register_blueprint(blueprint)

    return app
