"""Application configuration settings."""
from __future__ import annotations

import os


def _get_env(key: str, default: str) -> str:
    value = os.getenv(key)
    if value is None:
        return default
    return value


class Config:
    """Default configuration for the Flask application."""

    SECRET_KEY = _get_env("SECRET_KEY", "dev-secret-key")
    SQLALCHEMY_DATABASE_URI = _get_env(
        "DATABASE_URI",
        "mysql+pymysql://root:password@localhost:3306/todolist?charset=utf8mb4",
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_AS_ASCII = False
    CORS_ORIGINS = _get_env("CORS_ORIGINS", "*")


__all__ = ["Config"]
