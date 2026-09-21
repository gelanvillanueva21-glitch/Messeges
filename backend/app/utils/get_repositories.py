
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.database import get_database
from app.repositories.user_repo import UserRepo

from app.repositories.messsage_repo import MessageRepo


def get_user_repo(db: AsyncSession = Depends(get_database)) -> UserRepo:
    return UserRepo(db)


def get_msg_repo(db: AsyncSession = Depends(get_database)) -> MessageRepo:
    return MessageRepo(db)

