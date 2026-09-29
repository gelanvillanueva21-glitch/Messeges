

from sqlalchemy.ext.asyncio import AsyncSession

from app.database.models.messages import Messages
from app.schemas.message_schema import Message, MessageData, MessagesResponse
from app.repositories.messsage_repo import MessageRepo
from app.repositories.user_repo import UserRepo


class MessageService:
    def __init__(
        self, 
        db: AsyncSession,
        msg_repo: MessageRepo,
        user_repo: UserRepo | None = None
    ):
        self.database = db
        self.repo = msg_repo
        self.user_repo = user_repo or UserRepo(db)


    async def create_message(
        self,
        sender_id: int,
        receiver_id: int,
        content: str | None = None,
        image_url: str | None = None
    ) -> MessagesResponse:
        clean_content = content.strip() if content and content.strip() else None
        if not clean_content and not image_url:
            raise ValueError("Message content or image is required")

        receiver = await self.user_repo.get_by_id(receiver_id)
        if not receiver:
            await self.database.rollback()
            raise ValueError("Receiver user does not exist")


        message_data = Message(
            sender_id=sender_id,
            receiver_id=receiver_id,
            message=clean_content
        )
        msg_result = self.repo.message_user(
            data=message_data,
            image_url=image_url
        )
        await self.database.commit()
        await self.database.refresh(msg_result)

        return MessagesResponse(
            id=msg_result.id,
            sender_id=msg_result.sender_id,
            receiver_id=msg_result.receiver_id,
            message=msg_result.message,
            image_url=image_url,
            message_at=msg_result.message_at
        )


    async def get_messages(
        self,
        user_id: int,
        receiver_id: int,
        message_id: int | None = None
    ) -> list[MessagesResponse]:
        result = await self.repo.get_all_messages(
            MessageData(
                user_id=user_id,
                receiver_id=receiver_id,
                message_id=message_id
            )
        )
        return [
            MessagesResponse(
                id=msg.id,
                sender_id=msg.sender_id,
                receiver_id=msg.receiver_id,
                message=msg.message,
                image_url=msg.image_url,
                message_at=msg.message_at
            )
            for msg in result
        ]


    async def get_user_available(self, id: int):
        result = await self.repo.get_all_users()
        output = []
        for info in result:
            if id != info.id:
                output.append({
                    "full_name": info.full_name,
                    "user_id": info.id,
                    "profile_url": info.profile_url,
                    "created_at": info.created_at
                })
        return output


    async def get_searched_user(self, name: str):
        result = await self.repo.search(name)
        output = []
        for info in result:
            output.append({
                "full_name": info.full_name,
                "user_id": info.id,
                "profile_url": info.profile_url,
                "created_at": info.created_at
            })
        return output



