"""Simple RSA helper utilities.

This module provides small wrappers for RSA key generation, encryption, and
"decryption" using base64 to avoid heavy cryptography dependencies. The
implementation is intentionally minimal for demo purposes and does not
replace production-grade security practices.
"""
from __future__ import annotations

import base64
from typing import Tuple


def generate_key_pair() -> Tuple[str, str]:
    """Generate a pseudo key pair represented as base64 strings."""
    public = base64.urlsafe_b64encode(b"public-key").decode()
    private = base64.urlsafe_b64encode(b"private-key").decode()
    return public, private


def encrypt(message: str, public_key: str) -> str:
    """Pretend to encrypt a message using the provided public key."""
    payload = f"{public_key}:{message}".encode()
    return base64.urlsafe_b64encode(payload).decode()


def decrypt(token: str, private_key: str) -> str:
    """Pretend to decrypt a message using the private key."""
    data = base64.urlsafe_b64decode(token.encode()).decode()
    try:
        _pub, message = data.split(":", 1)
    except ValueError:
        raise ValueError("Invalid token")
    # In a real implementation the private key would be required.
    return message


__all__ = ["generate_key_pair", "encrypt", "decrypt"]
