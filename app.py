from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import random

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

#functions
    
def convert_to_unrepeatable(dicts_list):
    change_set = set()
    unrepeatable_list = []
    for hop_dict in dicts_list:
        change_tuple = tuple(hop_dict.items())
        if change_tuple not in change_set:
            change_set.add(change_tuple)
            unrepeatable_list.append(hop_dict)
    print(unrepeatable_list)
    return unrepeatable_list

#routes

#all hops, or hops filtering by: name, useing for and typical beer styles 

@app.route('/hops_list/', methods=["GET"])
def get_hops():
    name = request.args.get('name', None)
    used_for = request.args.get('used_for', default=None)
    beer_style = request.args.get('beer_style', default=None)
    result = []
    if name is not None:
        hop = Hop.query.filter_by(name = name).first()
        result.append(hop.as_dict())
    if used_for is not None:
        hops = Hop.query.filter_by(used_for = used_for).all()
        for hop in hops:
            if hop.as_dict() in result:
                pass
            else:
                result.append(hop.as_dict())
    if beer_style is not None:
        beer_style = beer_style.lower()
        hops = Hop.query.all()
        for hop in hops:
            if hop.as_dict() in result:
                pass
            else:
                if beer_style in (hop.typical_beer_styles).lower():
                    result.append(hop.as_dict())
    if len(request.args) == 0:
        hops = Hop.query.all()
        for hop in hops:
            result.append(hop.as_dict())
    result = convert_to_unrepeatable(result)
    return jsonify(result)

#hops filter by id

@app.route('/hops_list/<int:id>', methods=['GET'])
def get_hops_description(id):
    hop = Hop.query.get(id)
    return jsonify(hop.as_dict())

#random hops

@app.route('/hops_list/random', methods=['GET'])
def get_random_hops_description():
    hops = Hop.query.all()
    output = []
    for hop in hops:
        output.append(hop.id)
    id = random.choice(output)
    hop = Hop.query.get(id)
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
    return jsonify(new_hop.as_dict())

#delete hops

@app.route('/hops_list/<int:id>', methods=["DELETE"])
def del_new_hop(id):
    hop_to_del = Hop.query.get(id)
    db.session.delete(hop_to_del)
    db.session.commit()
    return jsonify({"deleted": "successfully"})


if __name__ == "__main__":
    app.run(debug = True)
