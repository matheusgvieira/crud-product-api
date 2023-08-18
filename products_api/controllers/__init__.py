from fastapi import APIRouter
from products_api.models.model import helth_check, list_tables
from .products import router as content_router
from .auth import router as auth_router

main_router = APIRouter()


@main_router.get("/", tags=["root"])
async def root():
    return {"name": "Products API"}


@main_router.get("/health", tags=["health"])
async def health_check():
    try:
        return {"status": "ok"}
    except Exception as e:
        return {"status": "error", "message": str(e)}


@main_router.get("/health/database", tags=["health"])
async def database_check():
    try:
        helth_check()
        list_tables()
        return {"status": "ok"}
    except Exception as e:
        return {"status": "error", "message": str(e)}


main_router.include_router(content_router, prefix="/products", tags=["products"])
main_router.include_router(auth_router, prefix="/auth", tags=["auth"])
