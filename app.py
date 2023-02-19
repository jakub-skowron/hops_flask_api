from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_swagger_ui import get_swaggerui_blueprint

'''
API helps finding hops substitutes
'''

app = Flask(__name__)
app.config.from_object('config.DevConfig')

jwt = JWTManager(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.json'
SWAGGER_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': 'Hops API'
    }
)

app.register_blueprint(SWAGGER_BLUEPRINT, url_prefix = SWAGGER_URL)

import src.routes

if __name__ == "__main__":
    app.run(debug=True)
