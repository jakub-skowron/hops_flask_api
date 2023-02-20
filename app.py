from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flasgger import Swagger
from src.config.swagger import swagger_config


app = Flask(__name__)
app.config.from_object('config.DevConfig')

jwt = JWTManager(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from src.hops.hops import hops
from src.auth.auth import auth
from src import error_routes

app.register_blueprint(auth)
app.register_blueprint(hops)

Swagger(app, config=swagger_config)

if __name__ == "__main__":
    app.run()