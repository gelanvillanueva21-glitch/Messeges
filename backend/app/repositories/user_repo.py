

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


from app.database.models.users import User
from app.config.security import hash_password
from app.schemas.user_schema import UserCreate


class UserRepo:
    def __init__(self, db: AsyncSession):
        self.database = db


    async def get_by_username(self, username: str) -> User:
        result = await self.database.execute(
            select(User).where(
                User.username == username
            )
        )
        return result.scalar_one_or_none();


    async def get_by_id(self, user_id: int) -> User:
        result = await self.database.execute(
            select(User).where(
                User.id == user_id
            )
        )
        return result.scalar_one_or_none()


    async def create(self, data: UserCreate) -> User:
        user = User(
            username = data.username,
            hashed_password = hash_password(data.password),
            full_name = data.full_name
        )
        self.database.add(user)
        return user


    async def change_password(
            self, 
            password: str,
            user_id: int
    ) -> None:
        user = await self.get_by_id(user_id)
        user.hashed_password = hash_password(password)



