from sqlalchemy.sql import table, column
from sqlalchemy import String, Float, create_engine, DateTime
from datetime import datetime
import random
import uuid

# Database configuration
engine = create_engine("mysql+pymysql://cpa:products@127.0.0.1:3306/crud_products_api")

# Seed data
items = [
    "Apples",
    "Bananas",
    "Bread",
    "Milk",
    "Eggs",
    "Cereal",
    "Chicken",
    "Rice",
    "Pasta",
    "Yogurt",
]

product_data = [
    {
        "id_product": "75a1173c-62e6-4fb7-b502-b4bc14f75046",
        "name": "Product A",
        "price": 10.99,
    },
    {
        "id_product": "246dc28c-b256-446c-b3ca-054d2bff5404",
        "name": "Product B",
        "price": 20.49,
    },
]

for item in items:
    product_data.append(
        {
            "id_product": uuid.uuid4(),
            "name": item,
            "price": round(random.uniform(1.99, 10.99), 2),
        }
    )

# Define the product table
product_table = table(
    "products",
    column("id_product", String),
    column("name", String),
    column("price", Float),
    column("created_at", DateTime),
    column("deleted_at", DateTime),
)


# Insert data into the product table
with engine.connect() as connection:
    for product in product_data:
        stmt = product_table.insert().values(
            id_product=product["id_product"],
            name=product["name"],
            price=product["price"],
            created_at=datetime.now(),
            deleted_at=None,
        )
        connection.execute(stmt)
        connection.commit()
