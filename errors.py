from werkzeug.exceptions import HTTPException
from flask import jsonify, Blueprint

errors_bp = Blueprint('errors', __name__)

@errors_bp.errorhandler(HTTPException)
def handle_http_exception(e):
    return jsonify({
        "status": e.code,
        "error": e.name,
        "message": e.description
    }), e.code

@errors_bp.errorhandler(Exception)
def handle_generic_exception(e):
    return jsonify({"error": "An unexpected error occurred"}), 500