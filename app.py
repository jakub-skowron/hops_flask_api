from flask import Flask, request, jsonify
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
    name = db.Column(db.String(32), unique=True)
    alpha = db.Column(db.String(32))
    beta = db.Column(db.String(32))
    origin = db.Column(db.String(32))
    description = db.Column(db.String(120))
    aroma = db.Column(db.String(120))
    typical_beer_styles = db.Column(db.String(120))
    used_for = db.Column(db.String(120))
    substitutions = db.Column(db.String(120))

#routes

#all hops

@app.route('/hops_list', methods=["GET"])
def get_hops_list():
    hops = Hop.query.all()
    output = []
    for hop in hops:
        output.append({        
            "id": hop.id,
            "name": hop.name,
            "alpha": hop.alpha,
            "beta": hop.beta,
            "origin": hop.origin,
            "description": hop.description,
            "aroma": hop.aroma,
            "typical_beer_styles": hop.typical_beer_styles,
            "used_for": hop.used_for,
            "substitutions": hop.substitutions
        })
    return jsonify({"hops list": output})

#special hops

@app.route('/hops_list/<int:id>', methods=['GET'])
def get_hop_description(id):
    hop = Hop.query.get_or_404(id)
    return jsonify({
        "id": hop.id,
        "name": hop.name,
        "alpha": hop.alpha,
        "beta": hop.beta,
        "origin": hop.origin,
        "description": hop.description,
        "aroma": hop.aroma,
        "typical_beer_styles": hop.typical_beer_styles,
        "used_for": hop.used_for,
        "substitutions": hop.substitutions
    })

#new hops

@app.route('/hops_list', methods=["POST"])
def add_new_hop():
    new_hop = Hop(
                name=request.json["name"].lower(), 
                alpha=request.json["alpha"].lower(), 
                beta=request.json["beta"].lower(), 
                origin=request.json["origin"].lower(), 
                description=request.json["description"].lower(), 
                aroma=request.json["aroma"].lower(), 
                typical_beer_styles=request.json["typical_beer_styles"].lower(), 
                used_for=request.json["used_for"].lower(), 
                substitutions=request.json["substitutions"].lower()
                )
    db.session.add(new_hop)
    db.session.commit()
    return jsonify({
        "id": new_hop.id,
        "name": new_hop.name,
        "alpha": new_hop.alpha,
        "beta": new_hop.beta,
        "origin": new_hop.origin,
        "description": new_hop.description,
        "aroma": new_hop.aroma,
        "typical_beer_styles": new_hop.typical_beer_styles,
        "used_for": new_hop.used_for,
        "substitutions": new_hop.substitutions
    })

#delete hops

@app.route('/hops_list/<int:id>', methods=["DELETE"])
def del_new_hop(id):
    hop_to_del = Hop.query.get_or_404(id)
    db.session.delete(hop_to_del)
    db.session.commit()
    return jsonify({"deleted": "successfully"})


if __name__ == "__main__":
    app.run(debug = True)
