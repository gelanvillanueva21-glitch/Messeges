

from fastapi import APIRouter, HTTPException, status, Form, File, UploadFile, Request, Query
from typing import Annotated


from app.utils.depends import CurrentUserDeps, MsgServDeps, DatabaseDepends
from app.schemas.message_schema import MessagesResponse, MessageData
from app.utils.save_image import save_file


router = APIRouter(prefix="/message", tags=['message'])


@router.post("/user/{receiver_id}")
async def message_request(
    user: CurrentUserDeps,
    service: MsgServDeps,
    receiver_id: int,
    request: Request,
    db: DatabaseDepends,
    content: Annotated[str | None, Form()] = None,
    image: Annotated[UploadFile | None, File()] = None
):
    # Support JSON request bodies when form data is not used
    if content is None and not image:
        content_type = request.headers.get("content-type", "")
        if "application/json" in content_type:
            try:
                body = await request.json()
                if isinstance(body, dict):
                    content = body.get("content") or body.get("message")
            except Exception:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Invalid JSON body."
                )

    try:
        saved_image = save_file(image)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

    try:
        result = await service.create_message(
            sender_id=user.id,
            receiver_id=receiver_id,
            content=content,
            image_url=saved_image
        )
        return {
            "status": "success",
            "data": result
        }
    except ValueError as e:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except Exception:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to send message"
        )



@router.get("/user/{receiver_id}")
async def get_messages(
    user: CurrentUserDeps,
    service: MsgServDeps,
    receiver_id: int,
    db: DatabaseDepends,
    message_id: Annotated[int | None, Query()] = None
):
    try:
        result = await service.get_messages(
            user_id=user.id,
            receiver_id=receiver_id,
            message_id=message_id
        )
        return {
            "status": "success",
            "message": result
        }
    except Exception:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch the messages."
        )



@router.get("/available")
async def get_user_available(
    user: CurrentUserDeps,
    service: MsgServDeps,
    db: DatabaseDepends
):
    try:
        result = await service.get_user_available(user.id)
        return {
            "status": "success",
            "accounts": result
        }
    except Exception:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch. Please try again later."
        )


async def search_user(
    name: Annotated[str, Query(...)],
    user: CurrentUserDeps,
    service: MsgServDeps
):
    try:
        result = await service.get_searched_user(name)
        return {
            "status": "success",
            "data": result
        }
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to search user. Please try again later."
        )
