from pydantic import BaseModel
from products_api.models.model import find, create
import uuid
from datetime import datetime


class UserLogin(BaseModel):
    email: str
    password: str


class UserRegister(BaseModel):
    name: str
    email: str
    password: str


class UserRepository:
    def __init__(self) -> None:
        self.data = []

    def find_by_email(self, email: str) -> dict:
        user = find("users", f"email = '{email}'")
        return dict(
            id_user=user[0],
            name=user[1],
            email=user[2],
            password=user[3],
            created_at=user[4],
        )

    def create(self, data: dict) -> dict:
        data["id_user"] = uuid.uuid4()
        data["created_at"] = datetime.now()
        create("users", data)
        return data
