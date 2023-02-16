from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_httpauth import HTTPBasicAuth

'''
API helps finding hops substitutes
'''

app = Flask(__name__)
app.config.from_object('config.DevConfig')

auth = HTTPBasicAuth()
db = SQLAlchemy(app)
migrate = Migrate(app, db)


import src.routes

if __name__ == "__main__":
    app.run(debug=True)
