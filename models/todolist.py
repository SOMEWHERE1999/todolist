"""Todo list model definition."""
from __future__ import annotations

from datetime import datetime

from sqlalchemy.sql import func

from . import BaseModel, db


class TodoItem(BaseModel):
    __tablename__ = "todolist"

    id = db.Column("AutoID", db.Integer, primary_key=True)
    title = db.Column("Title", db.String(200), nullable=False)
    status = db.Column("Status", db.String(32), nullable=False, default="pending")
    create_time = db.Column("CreateTime", db.DateTime, server_default=func.now())
    update_time = db.Column(
        "UpdateTime",
        db.DateTime,
        server_default=func.now(),
        onupdate=func.now(),
    )
    due_date = db.Column("DateTime", db.DateTime, nullable=True)
    is_deleted = db.Column("IsDelete", db.Integer, nullable=False, default=0)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "status": self.status,
            "create_time": self.create_time.isoformat() if self.create_time else None,
            "update_time": self.update_time.isoformat() if self.update_time else None,
            "due_date": self.due_date.isoformat() if self.due_date else None,
        }
