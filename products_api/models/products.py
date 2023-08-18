from products_api.models.model import (
    find_by_id,
    create,
    update,
    soft_delete,
    find_all_pagination,
    count,
    count_removed,
)
from pydantic import BaseModel
from datetime import datetime
import uuid
from typing import Union


class ProductsModelCreate(BaseModel):
    name: str
    price: float


class ProductsModelUpdate(BaseModel):
    name: Union[str, None] = None
    price: Union[str, None] = None


class ProductsItemsModel(BaseModel):
    id_product: str
    name: str
    price: float
    created_at: datetime


class ProductsRepository:
    def __init__(self) -> None:
        self.data = []

    def list(self, page=1, limit=5) -> list:
        products = find_all_pagination("products", page, limit)
        list_products = list([])

        for product in products:
            list_products.append(
                dict(
                    id_product=product[0],
                    name=product[1],
                    price=product[2],
                    created_at=product[3],
                )
            )

        return list_products

    def find_by_id(self, id: str) -> dict:
        product = find_by_id("products", id)
        return dict(
            id_product=product[0],
            name=product[1],
            price=product[2],
        )

    def create(self, data: BaseModel) -> dict:
        data_dict = data.dict()
        data_dict["id_product"] = uuid.uuid4()
        data_dict["created_at"] = datetime.now()
        create("products", data_dict)
        return data_dict

    def update(self, id: str, data: dict) -> dict:
        update("products", id, data)
        return data

    def delete(self, id: str) -> None:
        soft_delete("products", id)
        return None

    def count(self) -> int:
        return count("products")

    def count_removed(self) -> int:
        return count_removed("products")
