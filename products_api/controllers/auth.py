from fastapi import HTTPException, Depends
from fastapi_jwt_auth import AuthJWT
from fastapi import APIRouter
from products_api.models import Settings, UserLogin


router = APIRouter()


@AuthJWT.load_config
def get_config():
    return Settings()


@router.get("/login")
def login(user: UserLogin, Authorize: AuthJWT = Depends()):
    if user.email != "test" or user.password != "test":
        raise HTTPException(status_code=401, detail="Bad username or password")

    # subject identifier for who this token is for example id or username from database
    access_token = Authorize.create_access_token(subject=user.email)
    return {"access_token": access_token}


@app.get("/user")
def user(Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()

    current_user = Authorize.get_jwt_subject()
    return {"user": current_user}
