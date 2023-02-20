import random

from flask import request, jsonify, Blueprint
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import jwt_required

from app import app, db
from src.hops.models import Hop
from src.constants.http_responses_status_codes import (HTTP_200_OK, HTTP_201_CREATED, HTTP_202_ACCEPTED, HTTP_409_CONFLICT, HTTP_404_NOT_FOUND)


hops = Blueprint("hops", __name__, url_prefix="/api/v1/hops")

@hops.get('/')
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
    
    return jsonify(response), HTTP_200_OK

@hops.post('/')
@jwt_required()
def add_new_hop():
    new_hop = Hop(**request.json)
    db.session.add(new_hop)
    db.session.commit()
    return jsonify(new_hop.as_dict()), HTTP_201_CREATED

@hops.put('/<int:id>/')
@jwt_required()
def update_hop(id):
    hop = Hop.query.get(id)
    
    try:
        for key, value in request.json.items():
            setattr(hop, key, value)
        db.session.commit()
        return jsonify(hop.as_dict()), HTTP_202_ACCEPTED

    except IntegrityError:
        return jsonify({"error message": f"You can't change name of this hop, beacuse {request.json['name']} already exists"}), HTTP_409_CONFLICT

@hops.delete('/<int:id>/')
@jwt_required()
def delete_hop(id):
    hop = Hop.query.get(id)
    db.session.delete(hop)
    db.session.commit()
    return jsonify({"message": "hop deleted"}), HTTP_200_OK

@hops.get('/<int:id>/')
def get_hops_description(id):
    hop = Hop.query.get(id)
    if hop:
        return jsonify(hop.as_dict()), HTTP_200_OK
    else:
        return jsonify(({"error message":"hop not found"})), HTTP_404_NOT_FOUND

@hops.get('/random/')
def get_random_hops_description():
    hops = Hop.query.all()
    output = []
    for hop in hops:
        output.append(hop.id)
    id = random.choice(output)
    hop = Hop.query.get(id)
    return jsonify(hop.as_dict()), HTTP_200_OK