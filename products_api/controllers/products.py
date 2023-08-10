from fastapi import APIRouter
from products_api.database.index import engine
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException

router = APIRouter()


@router.get(
    "/",
)
async def list_products():
    try:
        with engine.connect() as connection:
            query = text("SELECT id, name FROM items")
            result = connection.execute(query)
            items = [{"id": row["id"], "name": row["name"]} for row in result]
            return items
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))
    # return {"message": "List of products"}
