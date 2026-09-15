

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING
from app.database.database import Base


if TYPE_CHECKING:
    from app.database.models.users import User



class Images(Base):
    __tablename__ = "images"

    id: Mapped[int] = mapped_column(primary_key=True)
    sender_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    image_url: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    user: Mapped["User"] = relationship("User")




