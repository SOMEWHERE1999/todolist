"""Custom error definitions."""
from __future__ import annotations

from typing import Optional

from flask import jsonify


class ApiException(Exception):
    def __init__(self, message: str, status_code: int = 400, code: int = 1):
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.code = code

    def to_response(self):
        response = jsonify({"code": self.code, "message": self.message})
        response.status_code = self.status_code
        return response


def register_error_handlers(app):
    @app.errorhandler(ApiException)
    def handle_api_error(error: ApiException):
        return error.to_response()

    @app.errorhandler(404)
    def handle_not_found(_error):
        response = jsonify({"code": 404, "message": "Resource not found"})
        response.status_code = 404
        return response

    @app.errorhandler(500)
    def handle_internal_error(_error):
        response = jsonify({"code": 500, "message": "Internal server error"})
        response.status_code = 500
        return response


__all__ = ["ApiException", "register_error_handlers"]
