

from typing import Annotated
from fastapi import Request, HTTPException, status, Depends
from jose import jwt, JWTError

from app.repositories.user_repo import UserRepo
from app.utils.depends import UserRepoDeps
from app.database.models.users import User
from app.config.config import settings


async def get_current_user(
    request: Request,
    repo: UserRepoDeps
) -> User:
    """
    A function that checks the cookie on
    Http only from the browser while sending
    users info
    """
    token = request.cookies.get("access_token")
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated"
        )
    
    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )
        user_id: str = payload.get("sub")
        if not user_id:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token."
            )
    except JWTError:
        raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token."
        )

    user = await repo.get_by_id(int(user_id))
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found."
        )
    return user

