from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_limiter import Limiter,HEADERS
from flask_limiter.util import get_remote_address

'''
API helps finding hops substitutes
'''

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:0pewd52oUeMIIQhvC5bb@containers-us-west-148.railway.app:7554/railway"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secret_key'

limiter = Limiter(app=app, 
                key_func=get_remote_address, 
                default_limits=["10/minute"],
                headers_enabled=True,
                storage_uri="memory://",
                storage_options={})

db = SQLAlchemy(app)

import routes

if __name__ == "__main__":
    app.run(debug=True)
