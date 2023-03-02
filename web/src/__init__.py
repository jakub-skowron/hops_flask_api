from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flasgger import Swagger

from config import Config
from src.config.swagger import swagger_config


db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    Swagger(app, config=swagger_config)

    from src.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    from src.hops import bp as hops_bp
    app.register_blueprint(hops_bp)

    from src.error_routes import bp as error_routes_bp
    app.register_blueprint(error_routes_bp)

    return app

from src.auth import models as auth_models
from src.hops import models as hops_models
