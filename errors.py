from werkzeug.exceptions import HTTPException
from flask import jsonify


def register_error_handlers(app):
    @app.errorhandler(HTTPException)
    def handle_http_exception(e):
        return jsonify({
            "status": e.code,
            "error": e.name,
            "message": e.description
        }), e.code

    @app.errorhandler(Exception)
    def handle_generic_exception(e):
        return jsonify({"error": "An unexpected error occurred"}), 500