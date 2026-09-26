

from datetime import datetime
from pydantic import BaseModel, ConfigDict


class Message(BaseModel):
    sender_id: int
    receiver_id: int
    message: str | None = None


class MessagesResponse(BaseModel):
    id: int
    sender_id: int
    receiver_id: int
    message: str | None = None
    image_url: str | None = None
    message_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)


class MessageData(BaseModel):
    user_id: int
    receiver_id: int
    message_id: int | None = None


