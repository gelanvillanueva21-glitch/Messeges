

from sqlalchemy import select, or_
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession


from app.database.models.users import User
from app.database.models.messages import Messages
from app.database.models.images import Images
from app.schemas.message_schema import Message, MessageData



class MessageRepo:
    def __init__(self, db: AsyncSession):
        self.database = db


    def message_user(
        self,
        data: Message,
        image_url: str | None = None
    ) -> Messages:
        message = Messages(
            sender_id = data.sender_id,
            receiver_id = data.receiver_id,
            message = data.message
        )
        if image_url:
            message.image_message = Images(image_url=image_url)
        self.database.add(message)
        return message


    def message_image(
        self,
        image_url: str,
        message_id: int
    ) -> Images:
        image_message = Images(
            message_id = message_id,
            image_url = image_url
        )
        self.database.add(image_message)
        return image_message


    async def get_all_messages(
        self,
        data: MessageData
    ) -> list[Messages]:
        stmt = (
            select(Messages)
            .options(selectinload(Messages.image_message))
            .where(
                or_(
                    (Messages.sender_id == data.user_id) & (Messages.receiver_id == data.receiver_id),
                    (Messages.sender_id == data.receiver_id) & (Messages.receiver_id == data.user_id)
                )
            )
        )
        if data.message_id:
            stmt = stmt.where(
                Messages.id < data.message_id
            )
        stmt = stmt.order_by(Messages.id.desc()).limit(50)

        result = await self.database.execute(stmt)
        messages = result.scalars().all()
        return list(reversed(messages))


    async def get_all_users(self) -> list[User]:
        result = await self.database.execute(
            select(User)
        )
        return list(result.scalars().all())


    async def search(self, name: str) -> list[User]:
        result = await self.database.execute(
            select(User)
            .where(
                User.full_name.ilike(f"%{name}%")
            )
        )
        return list(result.scalars().all())

