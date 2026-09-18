
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.database import get_database
from app.repositories.user_repo import UserRepo


def get_user_repo(db: AsyncSession = Depends(get_database)) -> UserRepo:
    return UserRepo(db)


