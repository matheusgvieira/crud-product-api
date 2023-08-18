from fastapi import APIRouter
from .products import router as content_router
from .auth import router as auth_router

main_router = APIRouter()

main_router.include_router(content_router, prefix="/products", tags=["products"])
auth_router.include_router(auth_router, prefix="/auth", tags=["auth"])


@main_router.get("/")
async def root():
    return {"name": "Products API"}
