from products_api.models.model import (
    find_by_id,
    create,
    update,
    delete,
    find_all_pagination,
)
from pydantic import BaseModel
import uuid


class ProductsModelCreate(BaseModel):
    name: str
    price: int


class Products:
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

    def create(self, data: dict) -> dict:
        data["id_product"] = uuid.uuid4()
        create("products", data)
        return data

    def update(self, id: str, data: dict) -> dict:
        update("products", id, data)
        return data

    def delete(self, id: str) -> None:
        delete("products", id)
        return None
