

from sqlalchemy import select, or_
from sqlalchemy.ext.asyncio import AsyncSession


from app.database.models.messages import Messages
from app.database.models.images import Images
from app.schemas.message_schema import Message, MessageData


class MessageRepo:
    def __init__(self, db: AsyncSession):
        self.database = db


    def message_user(
        self,
        data: Message
    ):
        message = Messages(
            sender_id = data.sender_id,
            receiver_id = data.receiver_id,
            message = data.message
        )
        self.database.add(message)
        return message


    def message_image(
        self,
        image_url: str,
        id: int
    ):
        image_message = Images(
            message_id = id,
            image_url = image_url
        )
        self.database.add(image_message)
        return image_message


    async def get_all_messages(
        self,
        data: MessageData
    ):
        result = await self.database.execute(
            select(Messages).where(
                or_(
                    (Messages.sender_id == data.user_id) & (Messages.receiver_id == data.reciever_id),
                    (Messages.sender_id == data.reciever_id) & (Messages.receiver_id == data.user_id)
                )
            ).order_by(Messages.message_at.asc())
        )
        return result.scalars().all()


