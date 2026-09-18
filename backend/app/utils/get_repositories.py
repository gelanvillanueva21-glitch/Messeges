
from fastapi import Depends


from app.utils.depends import DatabaseDepends, UserRepoDeps


from app.repositories.user_repo import UserRepo


def get_user_repo(db: DatabaseDepends) -> UserRepo:
    return UserRepo(db)

