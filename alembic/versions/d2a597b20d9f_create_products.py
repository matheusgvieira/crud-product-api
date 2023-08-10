"""create_products

Revision ID: d2a597b20d9f
Revises: 
Create Date: 2023-08-10 00:33:38.346168

"""
from typing import Sequence, Union

from sqlalchemy import Table, Column, Integer, String
from products_api.database import engine, metadata


# revision identifiers, used by Alembic.
revision: str = "d2a597b20d9f"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


products = Table(
    "products",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(255)),
    Column("price", Integer),
)


def upgrade() -> None:
    metadata.create_all(engine)
    pass


def downgrade() -> None:
    metadata.drop_all(engine)
    pass
