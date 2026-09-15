
from typing import Annotated

from app.repositories.user_repo import UserRepo
from app.utils.depends import DatabaseDepends


def get_user_repo(db: DatabaseDepends) -> UserRepo:
    return UserRepo(db)


