from fastapi import APIRouter
from .products import router as content_router

main_router = APIRouter()

main_router.include_router(content_router, prefix="/content", tags=["content"])


@main_router.get("/")
async def root():
    return {"name": "Products API"}
