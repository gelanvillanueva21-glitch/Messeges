

from fastapi import APIRouter, Depends, Response, HTTPException, status, Body
from typing import Annotated


from app.config.security import create_access_token, verify_password
from app.schemas.user_schema import UserResponse, UserCreate, UserLogin, ChangePassword
from app.utils.depends import UserRepoDeps, DatabaseDepends, CurrentUserDeps


route = APIRouter(prefix="/auth", tags=["auth"])


@route.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
async def register(
    data: UserCreate,
    db: DatabaseDepends,
    repo: UserRepoDeps
):
    try:
        print("hello world!")
        result = repo.create(data)
        if not result:
            raise ValueError()
        await db.commit()
        return result
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Account username already exist."
        )
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create account"
        )



@route.post("/change_password")
async def change_password(
    data: ChangePassword,
    repo: UserRepoDeps
):
    try:
        result = await repo.change_password(
            data.new_password, 
            data.id
        )
        return {"status": "success"}
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to chagne password."
        )


@route.post("/login")
async def login(
    response: Response,
    data: UserLogin,
    repo: UserRepoDeps
):
    user = await repo.get_by_username(data.username)
    if not user or not verify_password(data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect password or email."
        )
    """
    Created token then stores it through
    Http only cookies.
    """
    access_token = create_access_token(data={"sub": str(user.id3)})
    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,
        max_age=43200,
        samesite="lax",
        secure=False
    )
    return {"message": "Login successfully"}


@route.post("/logout")
async def logout(response: Response):
    response.delete_cookie(key="access_token")
    return {"status": "Logout successfuly."}


@route.get("/me", response_model=UserResponse)
async def get_me(data: CurrentUserDeps):
    return data


