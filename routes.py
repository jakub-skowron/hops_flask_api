import random
from flask import request, jsonify
from app import app, db
from models import Hop

@app.route('/hops_list/', methods=["GET"])
def get_hops():
    name = request.args.get('name', default=None)
    used_for = request.args.get('used_for', default=None)
    beer_style = request.args.get('beer_style', default=None)
    result = []

    if len(request.args) == 0:
        hops = Hop.query.all()
        for hop in hops:
            result.append(hop.as_dict())
        return jsonify(result)
    
    else:
        params = [("name",name), ("used_for",used_for), ("typical_beer_styles",beer_style)]
        hops = Hop.query.all()
        for hop in hops:
            hop_in_list = []
            params_quant = 0
            for param in params:
                if param[1]:
                    params_quant += 1
                    if param[1] in hop.as_dict()[param[0]]:
                        hop_in_list.append(hop.as_dict())
            if params_quant == len(hop_in_list):
                result.append(hop.as_dict())
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

@app.route('/hops_list/', methods=["POST"])
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
