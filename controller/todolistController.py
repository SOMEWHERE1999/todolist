"""Todo list controller handling CRUD operations."""
from __future__ import annotations

from datetime import datetime

from flask import Blueprint, request

from models import db
from models.todolist import TodoItem
from utils.commons import error_response, success_response
from utils.error import ApiException


todo_bp = Blueprint("todo", __name__)


@todo_bp.route("/", methods=["GET"])
def list_items():
    items = (
        TodoItem.query.filter_by(is_deleted=0)
        .order_by(TodoItem.create_time.desc())
        .all()
    )
    return success_response([item.to_dict() for item in items])


@todo_bp.route("/", methods=["POST"])
def create_item():
    payload = request.get_json() or {}
    title = payload.get("title")
    status = payload.get("status", "pending")
    due_date = payload.get("due_date")

    if not title:
        return error_response("Title is required", http_status=400)

    item = TodoItem(title=title, status=status)
    if due_date:
        item.due_date = datetime.fromisoformat(due_date)

    db.session.add(item)
    db.session.commit()
    return success_response(item.to_dict(), "Item created")


@todo_bp.route("/<int:item_id>", methods=["PUT"])
def update_item(item_id: int):
    item = TodoItem.query.get(item_id)
    if not item or item.is_deleted:
        raise ApiException("Item not found", status_code=404)

    payload = request.get_json() or {}
    title = payload.get("title")
    status = payload.get("status")
    due_date = payload.get("due_date")

    if title is not None:
        item.title = title
    if status is not None:
        item.status = status
    if due_date is not None:
        item.due_date = datetime.fromisoformat(due_date) if due_date else None

    db.session.commit()
    return success_response(item.to_dict(), "Item updated")


@todo_bp.route("/<int:item_id>", methods=["DELETE"])
def delete_item(item_id: int):
    item = TodoItem.query.get(item_id)
    if not item or item.is_deleted:
        raise ApiException("Item not found", status_code=404)

    item.is_deleted = 1
    db.session.commit()
    return success_response(item.to_dict(), message="Item deleted")
