from pydantic import BaseModel
from products_api.models.model import find, create
import uuid
from datetime import datetime
from typing import Union


class UserLogin(BaseModel):
    email: str
    password: str


class UserRepository:
    def __init__(self) -> None:
        self.data = []

    def find_by_email(self, email: str) -> Union[dict, None]:
        users = find("users", f"email = '{email}'")

        if not users or len(users) == 0:
            return None

        user = users[0]
        print("user", user)
        return dict(
            id_user=user[0],
            email=user[1],
            password=user[2],
            created_at=user[3],
        )

    def create(self, data: dict) -> dict:
        data["id_user"] = uuid.uuid4()
        data["created_at"] = datetime.now()
        create("users", data)
        return data
