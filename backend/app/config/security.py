

from datetime import datetime, timedelta, timezone
from typing import Any


import bcrypt
from jose import jwt
from app.config.config import settings


def hash_password(plain_password: str) -> str:
    # Creating salte to inject to the hashpassword
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(
        plain_password.encode("utf-8"),
        salt
    ).decode("utf-8")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify the plain password wether it is
    the same as the hash password.
    Hashed password become plain str like before
    because it get the salt that inject to the
    password that becomes unreadable.
    """
    return bcrypt.checkpw(
        plain_password.encode("utf-8"),
        hashed_password.encode("utf-8")
    )


def create_access_token(
        data: dict[str | Any], 
        expires_delta: timedelta | None = None
) -> str:
    to_encode = data.copy()

    if expires_delta:
        expires = datetime.now(timezone.utc) + expires_delta
    else:
        # Creates a calculation expiration for cookie
        expires = datetime.now() + timedelta(hours=settings.ACCESS_TOKEN_EXPIRE_HOURS)
    to_encode.update({"exp": expires})
    return jwt.encode(
        to_encode,
        settings.SECRET_KEY,
        settings.ALGORITHM
    )

