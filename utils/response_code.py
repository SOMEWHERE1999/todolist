"""Response status code definitions."""

class ResponseCode:
    SUCCESS = 0
    ERROR = 1
    UNAUTHORIZED = 401
    NOT_FOUND = 404
    SERVER_ERROR = 500


__all__ = ["ResponseCode"]
