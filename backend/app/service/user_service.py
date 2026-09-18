

from sqlalchemy.ext.asyncio import AsyncSession

from app.database.models.users import User

from app.repositories.user_repo import UserRepo
from app.schemas.user_schema import UserCreate, ChangePassword, UserLogin
from app.config.security import verify_password


class UserService:
    def __init__(
        self, 
        db: AsyncSession,
        repo: UserRepo
    ):
        self.database = db
        self.repo = repo


    async def register(
        self,
        data: UserCreate
    ) -> User:
        exist = await self.repo.get_by_username(data.username)
        if exist:
            raise ValueError()
        user = await self.repo.create(data)
        await self.database.commit()
        await self.database.refresh(user)
        return user


    async def check_account(
        self,
        data: UserLogin
    ) -> None:
        user = await self.repo.get_by_username(data.username)
        if not user or not verify_password(data.password, user.hashed_password):
            raise ValueError()
        return


