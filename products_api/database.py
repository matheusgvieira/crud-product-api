from sqlalchemy import create_engine, MetaData
from .config import settings

# Database configuration
DATABASE_URL = settings.database.uri
engine = create_engine(DATABASE_URL)
metadata = MetaData()
