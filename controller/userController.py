"""User controller handling registration and login."""
from __future__ import annotations

from flask import Blueprint, request

from models import db
from models.user import User
from utils.commons import error_response, success_response
from utils.error import ApiException

user_bp = Blueprint("user", __name__)


@user_bp.route("/register", methods=["POST"])
def register():
    payload = request.get_json() or {}
    username = payload.get("username")
    password = payload.get("password")

    if not username or not password:
        return error_response("Username and password are required", http_status=400)

    if User.query.filter_by(username=username, is_deleted=0).first():
        raise ApiException("Username already exists", status_code=409)

    user = User(username=username)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()

    return success_response(user.to_dict(), "Registration successful")


@user_bp.route("/login", methods=["POST"])
def login():
    payload = request.get_json() or {}
    username = payload.get("username")
    password = payload.get("password")

    if not username or not password:
        return error_response("Username and password are required", http_status=400)

    user = User.query.filter_by(username=username, is_deleted=0).first()
    if not user or not user.check_password(password):
        raise ApiException("Invalid credentials", status_code=401)

    return success_response(user.to_dict(), "Login successful")
