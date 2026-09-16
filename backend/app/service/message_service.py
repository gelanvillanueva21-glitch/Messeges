

from sqlalchemy.ext.asyncio import AsyncSession

from app.database.models.messages import Messages
from app.schemas.message_schema import Message, MessageData
from app.repositories.messsage_repo import MessageRepo


class MessageService:
    def __init__(
        self, 
        db: AsyncSession,
        msg_repo: MessageRepo
    ):
        self.database = db
        self.repo = msg_repo


    async def create_message(
        self,
        sender_id: int,
        receiver_id: int,
        content: str | None = None,
        image_url: str | None = None
    ):
        if content:
            # Block of code
            pass
        if image_url:
            # Block of code
            pass
        


