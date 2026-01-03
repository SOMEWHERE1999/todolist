"""Database initialization module."""
from __future__ import annotations

from datetime import datetime
from typing import Any, Dict

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect

# Global database object
# It will be initialized with the Flask app inside :func:`init_app`.
db = SQLAlchemy()


class BaseModel(db.Model):
    """Base model providing a reusable ``to_dict`` helper."""

    __abstract__ = True

    def to_dict(self) -> Dict[str, Any]:
        mapper = inspect(self.__class__)
        data: Dict[str, Any] = {}
        for column in mapper.columns:
            value = getattr(self, column.key)
            if isinstance(value, datetime):
                data[column.key] = value.isoformat()
            else:
                data[column.key] = value
        return data


def init_app(app):
    """Initialize database with the given Flask application."""
    db.init_app(app)


__all__ = ["db", "init_app", "BaseModel"]
