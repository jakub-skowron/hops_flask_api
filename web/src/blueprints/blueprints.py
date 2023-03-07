from src.auth import bp as auth_bp
from src.hops import bp as hops_bp
from src.error_routes import bp as error_routes_bp

blueprint_list = [
auth_bp,
hops_bp,
error_routes_bp
]