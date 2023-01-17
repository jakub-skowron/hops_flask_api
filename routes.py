import random

from flask import request, jsonify
from app import app
from models import Hop


@app.route('/hops_list/', methods=['GET'])
def get_hops():

    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 20, type=int)
    allowed_filters = {'name', 'used_for', 'beer_style', 'origin'}
    result = []
    setter = True

    if not request.args:
        hops = Hop.query.paginate(page=page,per_page=per_page)
    else:
        for item in request.args.keys():
            if item not in allowed_filters:
                hops = Hop.query.paginate(page=page,per_page=per_page)
                setter = False
            else:
                for key, value in request.args.items():
                    if key in allowed_filters and setter == True:
                        if key == 'beer_style':
                            key = 'typical_beer_styles'
                        hops = Hop.query.filter(getattr(Hop, key).ilike(f"%{value}%"))
                    else:
                        return jsonify(result)
    for item in hops:
        result.append(item.as_dict())
    return jsonify(result)

#hops filter by id

@app.route('/hops_list/<int:id>', methods=['GET'])
def get_hops_description(id):
    hop = Hop.query.get(id)
    if hop:
        return jsonify(hop.as_dict()), 201
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
    return jsonify(hop.as_dict()), 202

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({f"error":"page not found"}), 404

@app.errorhandler(405)
def method_not_allowed(e):
    return jsonify({f"error":"method not allowed"}), 405

@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({f"error":"internal server error"}), 500



