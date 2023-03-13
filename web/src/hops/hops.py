import random

from flask import request, jsonify
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import jwt_required
from flasgger import swag_from
from werkzeug.datastructures import ImmutableMultiDict

from src import db
from src.hops.models import Hop
from src.hops import bp
from src.constants.http_responses_status_codes import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_202_ACCEPTED,
    HTTP_409_CONFLICT,
    HTTP_404_NOT_FOUND,
)


@bp.get("/")
@swag_from("./docs/get_hops.yaml")
def get_hops():
    hops_list = []
    # changing '-' to '_' from URL
    updated_request_args = ImmutableMultiDict(
        {key.replace("-", "_"): value for key, value in request.args.items()}
    )
    page = updated_request_args.get("page", 1, type=int)
    per_page = updated_request_args.get("per_page", 20, type=int)

    hops = Hop.query

    alpha_beta_acids_keys = [
        "alpha_max_percentage",
        "alpha_min_percentage",
        "beta_max_percentage",
        "beta_min_percentage",
    ]

    for key, value in updated_request_args.items():
        if key in ["page", "per_page"]:
            continue
        if key in alpha_beta_acids_keys:
            hops = hops.filter(getattr(Hop, key).like(f"{value}"))
        else:
            hops = hops.filter(getattr(Hop, key).ilike(f"%{value}%"))

    hops = hops.paginate(page=page, per_page=per_page, error_out=False)

    for item in hops.items:
        hops_list.append(item.as_dict())

    response = {
        "items": hops_list,
        "total_items": hops.total,
        "total_pages": hops.pages,
        "current_page": hops.page,
        "per_page": hops.per_page,
    }

    return jsonify(response), HTTP_200_OK


@bp.post("/")
@jwt_required()
@swag_from("./docs/post_hops.yaml")
def add_new_hop():
    new_hop = Hop(**request.json)
    db.session.add(new_hop)
    try:
        db.session.commit()
    except IntegrityError:
        return (
            jsonify(
                {
                    "error message": f"You try to add new hop with name parameter which already exists"
                }
            ),
            HTTP_409_CONFLICT,
        )
    else:
        return jsonify(new_hop.as_dict()), HTTP_201_CREATED


@bp.put("/<int:id>/")
@jwt_required()
@swag_from("./docs/put_hop_by_id.yaml")
def update_hop(id):
    hop = Hop.query.get(id)

    for key, value in request.json.items():
        setattr(hop, key, value)
    try:
        db.session.commit()
    except IntegrityError:
        return (
            jsonify(
                {
                    "error message": f"You can't change name of this hop, beacuse {request.json['name']} already exists"
                }
            ),
            HTTP_409_CONFLICT,
        )
    else:
        return jsonify(hop.as_dict()), HTTP_202_ACCEPTED


@bp.delete("/<int:id>/")
@jwt_required()
@swag_from("./docs/delete_hop_by_id.yaml")
def delete_hop(id):
    hop = Hop.query.get(id)
    db.session.delete(hop)
    db.session.commit()
    return jsonify({"message": "hop deleted"}), HTTP_200_OK


@bp.get("/<int:id>/")
@swag_from("./docs/get_hop_by_id.yaml")
def get_hops_description(id):
    hop = Hop.query.get(id)
    if hop:
        return jsonify(hop.as_dict()), HTTP_200_OK
    else:
        return jsonify(({"error message": "hop not found"})), HTTP_404_NOT_FOUND


@bp.get("/random/")
@swag_from("./docs/get_random_hop.yaml")
def get_random_hops_description():
    hops = Hop.query.all()
    output = []
    for hop in hops:
        output.append(hop.id)
    id = random.choice(output)
    hop = Hop.query.get(id)
    return jsonify(hop.as_dict()), HTTP_200_OK
