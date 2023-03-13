from flask import jsonify

from src.error_routes import bp
from src.constants.http_responses_status_codes import (
    HTTP_404_NOT_FOUND,
    HTTP_405_METHOD_NOT_ALLOWED,
    HTTP_500_INTERNAL_SERVER_ERROR,
)


@bp.app_errorhandler(404)
def page_not_found(error):
    return jsonify({"error": "page not found"}), HTTP_404_NOT_FOUND


@bp.app_errorhandler(405)
def method_not_allowed(error):
    return jsonify({"error": "method not allowed"}), HTTP_405_METHOD_NOT_ALLOWED


@bp.app_errorhandler(500)
def internal_server_error(error):
    return jsonify({"error": "internal server error"}), HTTP_500_INTERNAL_SERVER_ERROR
