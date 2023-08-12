from fastapi import APIRouter
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
from products_api.models import Products, ProductsModelCreate


router = APIRouter()


@router.get("/")
async def list_products(page: int = 1, limit: int = 10):
    try:
        products = Products()
        list_products = products.list(page, limit)

        if not list_products:
            return dict(error=False, data=[])

        return dict(
            error=False,
            items=list(list_products),
            total=len(list_products),
            page=page,
        )

    except (SQLAlchemyError, ValueError) as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get(
    "/{id_products}",
)
async def show_product(id_products: str):
    try:
        products = Products()
        product_found = products.find_by_id(id_products)

        return dict(error=False, item=product_found)

    except (SQLAlchemyError, ValueError) as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post(
    "/",
)
async def create_product(product: ProductsModelCreate):
    try:
        products = Products()
        print(product)
        product_created = products.create(product)

        return dict(
            error=False, detail="Product created successfully", item=product_created
        )

    except (SQLAlchemyError, ValueError) as e:
        raise HTTPException(status_code=400, detail=str(e))
