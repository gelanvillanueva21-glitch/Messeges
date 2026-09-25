

from fastapi import Depends
from typing import Annotated


from sqlalchemy.ext.asyncio import AsyncSession

from app.database.database import get_database
from app.database.models.users import User


from app.utils.get_current_user import get_current_user


from app.utils.get_repositories import get_user_repo, get_msg_repo
from app.utils.get_services import get_user_service, get_msg_service


from app.service.user_service import UserService
from app.repositories.user_repo import UserRepo


from app.repositories.messsage_repo import MessageRepo
from app.service.message_service import MessageService



# Dependency variable to use so it
# avoid writing Anootated anywhere and everywhere
DatabaseDepends = Annotated[AsyncSession, Depends(get_database)]
CurrentUserDeps = Annotated[User, Depends(get_current_user)]




# Repositories Dependencies
UserRepoDeps = Annotated[UserRepo, Depends(get_user_repo)]
MsgRepoDebs = Annotated[MessageRepo, Depends(get_msg_repo)]




# Services Dependencies
UserServDeps = Annotated[UserService, Depends(get_user_service)]
MsgServDeps = Annotated[MessageService, Depends(get_msg_service)]