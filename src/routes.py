import random

from flask import request, jsonify
from sqlalchemy.exc import IntegrityError

from app import app, db
from .models import Hop


@app.route('/hops/', methods=['GET'])
def get_hops():
    hops_list = []
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 20, type=int)
    
    hops = Hop.query
    
    for key, value in request.args.items():
        if key in ['page', 'per_page']:
            continue
        hops = hops.filter(getattr(Hop, key).ilike(f"%{value}%"))
    
    hops = hops.paginate(page=page, per_page=per_page, error_out=False)
    
    for item in hops.items:
        hops_list.append(item.as_dict())
    
    response = {
        "items": hops_list,
        "total_items": hops.total,
        "total_pages": hops.pages,
        "current_page": hops.page,
        "per_page": hops.per_page
    }
    
    return jsonify(response), 200

@app.route('/hops/', methods=['POST'])
def add_new_hop():
    new_hop = Hop(**request.json)
    db.session.add(new_hop)
    db.session.commit()
    return jsonify(new_hop.as_dict()), 201

@app.route('/hops/<int:id>', methods=['PUT'])
def update_hop(id):
    hop = Hop.query.get(id)
    try:
        for key, value in request.json.items():
            setattr(hop, key, value)
        db.session.commit()
        return jsonify(hop.as_dict()), 202

    except IntegrityError:
        return jsonify({"error message": f"You can't change name of this hop, beacuse {request.json['name']} already exists"})

@app.route('/hops/<int:id>', methods=['DELETE'])
def delete_hop(id):
    hop = Hop.query.get(id)
    db.session.delete(hop)
    db.session.commit()
    return jsonify({"message": "hop deleted"})

#hops filter by id

@app.route('/hops/<int:id>', methods=['GET'])
def get_hops_description(id):
    hop = Hop.query.get(id)
    if hop:
        return jsonify(hop.as_dict()), 201
    else:
        return jsonify(({"error message":"hop not found"})), 400

#random hops

@app.route('/hops/random', methods=['GET'])
def get_random_hops_description():
    hops = Hop.query.all()
    output = []
    for hop in hops:
        output.append(hop.id)
    id = random.choice(output)
    hop = Hop.query.get(id)
    return jsonify(hop.as_dict()), 201

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({f"error":"page not found"}), 404

@app.errorhandler(405)
def method_not_allowed(e):
    return jsonify({f"error":"method not allowed"}), 405

@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({f"error":"internal server error"}), 500



