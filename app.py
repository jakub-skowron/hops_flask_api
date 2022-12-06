from flask import Flask
from flask_sqlalchemy import SQLAlchemy

'''
API helps finding hops substitutes
'''

app = Flask(__name__)
'''
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
'''
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:luLBk2hENxANvCtoXFgM@containers-us-west-159.railway.app:6143/railway"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secret_key'

db = SQLAlchemy(app)

import routes
db.create_all()

if __name__ == "__main__":
    app.run()
