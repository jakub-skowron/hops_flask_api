import random
from flask import request, jsonify
from app import app
from models import Hop


@app.route('/hops_list/', methods=['GET'])
def get_hops():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 20, type=int)
    name = request.args.get('name', default=None)
    used_for = request.args.get('used_for', default=None)
    beer_style = request.args.get('beer_style', default=None)
    origin = request.args.get('origin', default=None)
    result = []
    if page != 0 or per_page != 0 or len(request.args) == 0:
        hops = Hop.query.paginate(page=page,per_page=per_page)
        for hop in hops:
            result.append(hop.as_dict())
        return jsonify(result)
    else:
        params = [['name',name], ['used_for',used_for], ['typical_beer_styles',beer_style], ['origin',origin]]
        hops = Hop.query.all()
        for hop in hops:
            hop_in_list = []
            params_quant = 0
            for param in params:
                if param[1]:
                    params_quant += 1
                    hop_param_from_db = hop.as_dict()[param[0]]
                    if "_" in param[1]:
                        param[1] = param[1].replace("_", " ")
                    if param[1].lower() in hop_param_from_db.lower():
                        hop_in_list.append(hop.as_dict())
            if params_quant == len(hop_in_list) and len(hop_in_list) != 0:
                result.append(hop.as_dict())
        return jsonify(result)  
            
#hops filter by id

@app.route('/hops_list/<int:id>', methods=['GET'])
def get_hops_description(id):
    hop = Hop.query.get(id)
    if hop:
        return jsonify(hop.as_dict())
    else:
        return jsonify(({"error":"hop not found"})), 400

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

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({f"error":"page not found"}), 404

@app.errorhandler(405)
def method_not_allowed(e):
    return jsonify({f"error":"method not allowed"}), 405

@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({f"error":"internal server error"}), 404

'''
#new hops

@app.route('/hops_list/', methods=['POST'])
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
'''