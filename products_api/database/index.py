from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
from products_api.config import settings

# Database configuration
DATABASE_URL = settings.database.url
engine = create_engine(DATABASE_URL)
