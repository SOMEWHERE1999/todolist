"""Common helper utilities."""
from __future__ import annotations

from flask import jsonify


def success_response(data=None, message: str = "success", code: int = 0):
    """Return a unified success response."""
    return jsonify({"code": code, "message": message, "data": data})


def error_response(message: str = "error", code: int = 1, http_status: int = 400):
    """Return a unified error response."""
    response = jsonify({"code": code, "message": message})
    response.status_code = http_status
    return response
