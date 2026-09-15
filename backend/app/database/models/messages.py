

from datetime import datetime
from sqlalchemy import String, DateTime, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING
from app.database.database import Base


if TYPE_CHECKING:
    from app.database.models.users import User
    from app.database.models.images import Images


class Messages(Base):
    __tablename__ = "messages"

    id: Mapped[int] = mapped_column(primary_key=True)
    sender_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )
    receiver_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )
    message_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )
    message: Mapped[int] = mapped_column(
        String(10000)
    )

    message_owner: Mapped['User'] = relationship(
        "User",
        back_populates="messages"
    )
    image_sender: Mapped[list['Images']] = relationship(
        "Images",
        back_populates="images"
    )




