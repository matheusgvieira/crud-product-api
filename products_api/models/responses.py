from pydantic import BaseModel
from .products import ProductsItemsModel


class ListResponse(BaseModel):
    error: bool
    items: ProductsItemsModel
    limit: int
    page: int
    count: int
    items_removed: int
