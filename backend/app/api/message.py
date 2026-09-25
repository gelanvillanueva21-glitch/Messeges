

from fastapi import APIRouter, HTTPException, status, Body, File, UploadFile
from typing import Annotated


from app.utils.depends import CurrentUserDeps, MsgServDeps
from app.schemas.message_schema import MessagesResponse, MessageData
from app.utils.save_image import save_file


router = APIRouter(prefix="/message", tags=['message'])


@router.post("/user/{receiver_id}")
async def message_request(
    user: CurrentUserDeps,
    service: MsgServDeps,
    receiver_id: int,
    content: Annotated[str | None, Body(...)] = None,
    image: Annotated[UploadFile | None, File(...)] = None
):
    try:
        await service.create_message(
            user.id,
            receiver_id,
            content,
            save_file(image)
        )
        return {"status": "success"}
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Failed to save image, because of file name or something occur"
        )
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to sent message"
        )



@router.get("/user/{receiver_id}")
async def get_messages(
    user: CurrentUserDeps,
    service: MsgServDeps,
    receiver_id: int
):
    try:
        result = await service.get_messages(user.id, receiver_id)
        return {
            "status": "success",
            "message": result
        }
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch the messages."
        )


@router.get("/available")
async def get_user_available(
    user: CurrentUserDeps,
    service: MsgServDeps
):
    try:
        result = await service.get_user_available(user.id)
        return {
            "status": "success",
            "accounts": result
        }
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch. Please try again later."
        )

