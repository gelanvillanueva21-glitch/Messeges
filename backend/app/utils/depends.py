

from fastapi import Depends
from typing import Annotated


from sqlalchemy.ext.asyncio import AsyncSession


from app.database.database import get_database


DatabaseDepends = Annotated[AsyncSession, Depends(get_database)]


