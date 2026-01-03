"""Application factory for the Todo list service."""
from __future__ import annotations

from flask import Flask, render_template
from flask_cors import CORS

from config.config import Config
from controller.todolistController import todo_bp
from controller.userController import user_bp
from models import init_app as init_db
from utils.error import register_error_handlers
from utils.loggings import init_logging


def create_app():
    app = Flask(__name__, static_folder="static", template_folder="templates")
    app.config.from_object(Config)

    # Initialize extensions
    init_logging()
    init_db(app)
    CORS(app, resources={r"/api/*": {"origins": app.config.get("CORS_ORIGINS", "*")}})

    # Register blueprints
    app.register_blueprint(todo_bp, url_prefix="/api/todos")
    app.register_blueprint(user_bp, url_prefix="/api/users")

    register_error_handlers(app)

    @app.route("/")
    def index():
        return render_template("index.html")

    return app


__all__ = ["create_app"]
