"""create_products

Revision ID: d2a597b20d9f
Revises: 
Create Date: 2023-08-10 00:33:38.346168

"""
from typing import Sequence, Union

from sqlalchemy import Table, Column, Float, String, DateTime
from products_api.database import engine, metadata
from datetime import datetime


# revision identifiers, used by Alembic.
revision: str = "d2a597b20d9f"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


products = Table(
    "products",
    metadata,
    Column("id_product", String(255), primary_key=True),
    Column("name", String(255), nullable=False),
    Column("price", Float, nullable=False),
    Column("created_at", DateTime, nullable=False, default=datetime.now()),
    Column("deleted_at", DateTime, nullable=True),
)


def upgrade() -> None:
    metadata.create_all(engine)
    pass


def downgrade() -> None:
    metadata.drop_all(engine)
    pass
