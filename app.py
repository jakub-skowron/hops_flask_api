from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from json import JSONEncoder

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

class MyEncoder(JSONEncoder):
    def default(self, obj):
        return obj.__dict__    

class Hop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    alpha = db.Column(db.String(32))
    beta = db.Column(db.String(32))
    origin = db.Column(db.String(32))
    description = db.Column(db.String(120))
    aroma = db.Column(db.String(120))
    typical_beer_styles = db.Column(db.String(120))
    used_for = db.Column(db.String(120))
    substitutions = db.Column(db.String(120))

    def as_dict(self):
        hop_dict = {
            "id": self.id,
            "name": self.name,
            "alpha": self.alpha,
            "beta": self.beta,
            "origin": self.origin,
            "description": self.description,
            "aroma": self.aroma,
            "typical_beer_styles": self.typical_beer_styles,
            "used_for": self.used_for,
            "substitutions": self.substitutions
        }
        return hop_dict
#routes

#all hops

@app.route('/hops_list', methods=["GET"])
def get_hops_list():
    hops = Hop.query.all()
    output = []
    for hop in hops:
        output.append(hop.as_dict())
    return jsonify({"hops list": output})

#hops filter by id

@app.route('/hops_list/<int:id>', methods=['GET'])
def get_hop_description(id):
    hop = Hop.query.get_or_404(id)
    return jsonify(hop.as_dict())

#new hops

@app.route('/hops_list', methods=["POST"])
def add_new_hop():
    new_hop = Hop(
                name=request.json["name"], 
                alpha=request.json["alpha"], 
                beta=request.json["beta"], 
                origin=request.json["origin"], 
                description=request.json["description"], 
                aroma=request.json["aroma"], 
                typical_beer_styles=request.json["typical_beer_styles"], 
                used_for=request.json["used_for"], 
                substitutions=request.json["substitutions"]
                )
    db.session.add(new_hop)
    db.session.commit()
    return jsonify(new_hop)

#delete hops

@app.route('/hops_list/<int:id>', methods=["DELETE"])
def del_new_hop(id):
    hop_to_del = Hop.query.get_or_404(id)
    db.session.delete(hop_to_del)
    db.session.commit()
    return jsonify({"deleted": "successfully"})


if __name__ == "__main__":
    app.run(debug = True)
