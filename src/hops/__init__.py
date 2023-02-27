from flask import Blueprint

bp = Blueprint("hops", __name__, url_prefix="/api/v1/hops")

from src.hops import hops