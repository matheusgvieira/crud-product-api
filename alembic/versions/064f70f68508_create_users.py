"""create_users

Revision ID: 064f70f68508
Revises: d2a597b20d9f
Create Date: 2023-08-15 21:04:53.818459

"""
from typing import Sequence, Union

from sqlalchemy import Table, Column, String, DateTime
from products_api.database import engine, metadata
from datetime import datetime


revision: str = "064f70f68508"
down_revision: Union[str, None] = "d2a597b20d9f"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

users = Table(
    "users",
    metadata,
    Column("id_user", String(36), primary_key=True),
    Column("email", String(255), nullable=False),
    Column("password", String(255), nullable=False),
    Column("created_at", DateTime, default=datetime.utcnow),
)


def upgrade() -> None:
    metadata.create_all(engine)
    pass


def downgrade() -> None:
    metadata.drop_all(engine)
    pass
