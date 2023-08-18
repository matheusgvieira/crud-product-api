from fastapi import APIRouter
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
from products_api.models import (
    ProductsRepository,
    ProductsModelCreate,
    ProductsModelUpdate,
    ListResponse,
)
from products_api.utils.removes import remove_key_with_value_none
from products_api.utils.token import get_user_by_token
from fastapi import Depends
from starlette import status


router = APIRouter()


@router.get(
    "/",
    dependencies=[Depends(get_user_by_token)],
    responses={status.HTTP_200_OK: dict(model=ListResponse)},
)
async def list_products(page: int = 1, limit: int = 10):
    try:
        products = ProductsRepository()
        list_products = products.list(page, limit)

        if not list_products:
            return dict(error=False, data=[])

        return dict(
            error=False,
            items=list(list_products),
            limit=len(list_products),
            page=page,
            count=products.count(),
            items_removed=products.count_removed(),
        )

    except (SQLAlchemyError, ValueError) as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/{id_products}", dependencies=[Depends(get_user_by_token)])
async def show_product(id_products: str):
    try:
        products = ProductsRepository()
        product_found = products.find_by_id(id_products)

        return dict(error=False, item=product_found)

    except (SQLAlchemyError, ValueError) as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/", dependencies=[Depends(get_user_by_token)])
async def create_product(product: ProductsModelCreate):
    try:
        products = ProductsRepository()
        product_created = products.create(product)

        return dict(
            error=False, detail="Product created successfully", item=product_created
        )

    except (SQLAlchemyError, ValueError) as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/{id_products}", dependencies=[Depends(get_user_by_token)])
async def update_product(id_product: str, product: ProductsModelUpdate):
    try:
        products = ProductsRepository()
        product_updated = products.update(
            id_product, remove_key_with_value_none(product.dict())
        )

        return dict(
            error=False, detail="Product updated successfully", item=product_updated
        )

    except (SQLAlchemyError, ValueError) as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{id_products}", dependencies=[Depends(get_user_by_token)])
async def delete_product(id_product: str):
    try:
        products = ProductsRepository()
        products.delete(id_product)

        return dict(error=False, detail="Product deleted successfully")

    except (SQLAlchemyError, ValueError) as e:
        raise HTTPException(status_code=400, detail=str(e))
