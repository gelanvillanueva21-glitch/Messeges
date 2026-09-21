

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
    ) -> None:
        if content:
            msg_result = self.repo.message_user(data=(
                content,
                sender_id,
                receiver_id
            ))
        if image_url:
            img_result = self.repo.message_image(
                image_url,
                sender_id
            )
        await self.database.commit()


    async def get_messages(
        self,
        user_id: int,
        receiver_id: int
    ):
        result = await self.repo.get_all_messages((
            user_id,
            receiver_id
        ))
        output_list = []
        for info in result:
            if info.sender_id == user_id:
                output_list.append({})
        return output_list

