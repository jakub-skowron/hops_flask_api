from flask import Blueprint

bp = Blueprint("error_routes", __name__)

from src.error_routes import error_routes