
from fastapi import Depends

from app.utils.depends import DatabaseDepends, UserRepoDeps
from app.service.user_service import UserService


def get_user_service(
    db: DatabaseDepends, 
    repo: UserRepoDeps
) -> UserService:
    return UserService(db, repo)




