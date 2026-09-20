
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.database import get_database
from app.repositories.user_repo import UserRepo
from app.utils.get_repositories import get_user_repo
from app.service.user_service import UserService


def get_user_service(
    db: AsyncSession = Depends(get_database), 
    repo: UserRepo = Depends(get_user_repo)
) -> UserService:
    return UserService(db, repo)




