from flask import jsonify

from src.error_routes import bp
from src.constants.http_responses_status_codes import (
    HTTP_404_NOT_FOUND,
    HTTP_405_METHOD_NOT_ALLOWED,
    HTTP_500_INTERNAL_SERVER_ERROR,
)


@bp.errorhandler(404)
def page_not_found(e):
    return jsonify({f"error": "page not found"}), 404


@bp.errorhandler(405)
def method_not_allowed(e):
    return jsonify({f"error": "method not allowed"}), 405


@bp.errorhandler(500)
def internal_server_error(e):
    return jsonify({f"error": "internal server error"}), 500
