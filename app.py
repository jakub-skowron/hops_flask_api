from flask import Flask
from flask_sqlalchemy import SQLAlchemy

'''
API helps finding hops substitutes
'''
#app & db

app = Flask(__name__)
'''
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
'''
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:UcoRUj5Zuw36xThWZjT4@containers-us-west-154.railway.app:6878/railway"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secret_key'

db = SQLAlchemy(app)

import routes
db.create_all()

if __name__ == "__main__":
    app.run()
