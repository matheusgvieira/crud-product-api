from fastapi import HTTPException, Depends
from fastapi import APIRouter
from products_api.models import UserLogin, UserRepository, UserRegister
from products_api.config import settings
from datetime import timedelta
from products_api.utils.jwt import (
    create_access_token,
    get_current_user,
    get_password_hash,
    verify_password,
)


router = APIRouter()


@router.post("/login")
def login(user: UserLogin):
    user_repository = UserRepository()

    user_found = user_repository.find_by_email(user.email)

    if not user_found:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if not verify_password(user.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token_expires = timedelta(
        minutes=settings.server.authjwt_access_token_expires
    )
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/register")
def register_user(user: UserRegister):
    user_repository = UserRepository()
    user_found = user_repository.find_by_email(user.email)

    if user_found:
        raise HTTPException(status_code=400, detail="Username already registered")

    hashed_password = get_password_hash(user.password)

    user_repository.create(
        dict(name=user.name, email=user.email, password=hashed_password)
    )

    access_token_expires = timedelta(minutes=access_token_expires)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/user")
def user(current_user: str = Depends(get_current_user)):
    return {"user": current_user}
