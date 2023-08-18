from pydantic import BaseModel
from products_api.config import settings


class UserLogin(BaseModel):
    email: str
    password: str


class Settings(BaseModel):
    authjwt_secret_key: str = settings.server.authjwt_secret_key
