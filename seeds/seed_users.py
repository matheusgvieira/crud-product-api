from sqlalchemy.sql import table, column
from sqlalchemy import String, Float, create_engine, DateTime
from datetime import datetime
import random
import uuid

# Database configuration
engine = create_engine("mysql+pymysql://cpa:products@127.0.0.1:3306/crud_products_api")

user_data = [
    {
        "id_user": "a0e77311-dedb-4adb-bdf0-6a96b4f2ed60",
        "email": "sacgip@wikacih.me",
        "password": "12345678",
    },
]

# Define the product table
user_table = table(
    "users",
    column("id_user", String),
    column("email", String),
    column("password", Float),
    column("created_at", DateTime),
)


# Insert data into the product table
with engine.connect() as connection:
    for product in user_data:
        stmt = user_table.insert().values(
            id_user=product["id_user"],
            email=product["email"],
            password=product["password"],
            created_at=datetime.now(),
        )
        connection.execute(stmt)
        connection.commit()
