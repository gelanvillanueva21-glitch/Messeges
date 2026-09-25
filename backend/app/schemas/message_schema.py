

from pydantic import BaseModel, Field, ConfigDict


class Message(BaseModel):
    message: str
    sender_id: int
    receiver_id: int


class MessagesResponse(Message):
    image_url: str

    model_config = ConfigDict(from_attributes=True)


class MessageData(BaseModel):
    user_id: int
    receiver_id: int
    message_id: int | None = None

