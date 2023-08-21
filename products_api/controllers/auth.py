from fastapi import HTTPException, Depends, Body
from fastapi import APIRouter
from products_api.models import UserLogin, UserRepository, UserLoged
from products_api.config import settings
from datetime import timedelta
from starlette import status
from products_api.utils.exceptions import LoginError, RegisterError
from products_api.utils.jwt import (
    create_access_token,
    get_current_user,
    get_password_hash,
    verify_password,
)
from products_api.utils.token import get_user_by_token, UnauthorizedMessage
from passlib.exc import UnknownHashError
from products_api.providers.logger import AppLogger

router = APIRouter()
logger = AppLogger()


@router.post(
    "/login",
    responses={
        status.HTTP_200_OK: dict(model=UserLoged),
        status.HTTP_401_UNAUTHORIZED: dict(model=UnauthorizedMessage),
    },
)
# def login(payload=Body(...)):
def login(payload: UserLogin):
    try:
        user_repository = UserRepository()

        user_found = user_repository.find_by_email(payload.email)

        if not user_found:
            raise HTTPException(status_code=401, detail="Invalid credentials")

        if not verify_password(payload.password, user_found["password"]):
            raise HTTPException(status_code=401, detail="Invalid credentials")

        access_token_expires = timedelta(
            minutes=settings.server.authjwt_access_token_expires
        )
        access_token = create_access_token(
            data=dict(
                email=user_found["email"],
                id_user=user_found["id_user"],
                created_at=user_found["created_at"].isoformat(),
            ),
            expires_delta=access_token_expires,
        )
        return {"access_token": access_token, "token_type": "Bearer"}
    except (LoginError, UnknownHashError) as error:
        logger.error(error)
        raise HTTPException(
            status_code=400, detail=f"Error ao realizar o login, tente novamente"
        )


@router.post("/register")
def register_user(user: UserLogin):
    try:
        user_repository = UserRepository()

        user_found = user_repository.find_by_email(user.email)

        if user_found is not None:
            raise HTTPException(status_code=400, detail="Username already registered")

        hashed_password = get_password_hash(user.password)

        print(hashed_password)

        user_created = user_repository.create(
            dict(email=user.email, password=hashed_password)
        )

        access_token_expires = timedelta(
            minutes=settings.server.authjwt_access_token_expires
        )

        access_token = create_access_token(
            data=dict(
                email=user_created["email"],
                id_user=str(user_created["id_user"]),
                created_at=user_created["created_at"].isoformat(),
            ),
            expires_delta=access_token_expires,
        )

        return {
            "access_token": access_token,
            "token_type": "Bearer",
            "message": "User created successfully",
        }
    except RegisterError as error:
        raise HTTPException(
            status_code=400, detail=f"Error ao realizar o registro | {error}"
        )


@router.get(
    "/user",
    responses={status.HTTP_401_UNAUTHORIZED: dict(model=UnauthorizedMessage)},
)
def get_user(user: dict = Depends(get_user_by_token)):
    return user
