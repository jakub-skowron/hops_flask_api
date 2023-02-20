from flask import request, jsonify, Blueprint
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity
from flasgger import swag_from

from app import db
from src.auth.models import User
from src.constants.http_responses_status_codes import (HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED)


auth = Blueprint("auth", __name__, url_prefix="/api/v1/auth")

@auth.post('/register/')
def register():
    email = request.json.get('email')
    password = request.json.get('password')

    if email is None or password is None:
        return jsonify({'error message': 'Missing email or password'}), HTTP_400_BAD_REQUEST
    
    if User.query.filter_by(email = email).first() is not None:
        return jsonify({'error message': f'{request.json["email"]} is already register'}), HTTP_400_BAD_REQUEST
    
    user = User(email = email, password = password)
    user.hash_password(password)
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User created'}), HTTP_201_CREATED

@auth.post('/login/')
@swag_from('./docs/login.yaml')
def login():
    email = request.json.get('email', None)
    password = request.json.get('password', None)

    user = User.query.filter_by(email=email).one_or_none()
    
    if not user or not user.verify_password(password):
        return jsonify({'message': 'Wrong username or password'}), HTTP_401_UNAUTHORIZED

    access_token = create_access_token(identity=email)
    refresh_token = create_refresh_token(identity=email)

    return jsonify({
        'user': {
            'refresh': refresh_token,
            'access': access_token,
        }
    }), HTTP_200_OK

@auth.get('/token/refresh/')
@jwt_required(refresh=True)
def refresh_users_token():
    identity = get_jwt_identity()
    access = create_access_token(identity=identity)

    return jsonify({
        'access': access
    }), HTTP_200_OK