from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

'''
API helps finding hops substitutes
'''
#app & db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secret_key'

db = SQLAlchemy(app)

#models
class Hop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    alpha = db.Column(db.String(32))
    beta = db.Column(db.String(32))
    origin = db.Column(db.String(32))
    description = db.Column(db.String(120))
    aroma = db.Column(db.String(120))
    typical_beer_styles = db.Column(db.String(120))
    used_for = db.Column(db.String(120))
    substitutions = db.Column(db.String(120))

    def __repr__(self) -> str:
        return self.name


@app.route('/hops_list', methods=["GET"])
def get_hops_list():
    hops = Hop.query.all()
    output = []
    for hop in hops:
        output.append(hop)
    return {"hops list": output}
'''
@app.route('/hops_list/<int:id_hop>', methods=['GET'])
def get_hop_description(id_hop):
    result = Hop.query.
    return hops[id_hop-1]
'''

if __name__ == "__main__":
    app.run(debug = True)
