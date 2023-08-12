from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
from products_api.database import engine

Session = sessionmaker(bind=engine)
session = Session()


def create(table: str, values: dict) -> None:
    query = text(
        f"INSERT INTO {table} ({', '.join(values.keys())}) VALUES ({', '.join(':' + value for value in values.values())})"
    )
    session.execute(query, values)
    session.commit()


def find(table: str, conditions: str) -> list:
    query = text(f"SELECT * FROM {table} WHERE {conditions}")
    result = session.execute(query).fetchall()
    return result


def find_by_id(table: str, id: str):
    query = text(f"SELECT * FROM {table} WHERE id = :id")
    result = session.execute(query, {"id": id}).fetchone()
    return result


def find_all(table: str) -> list:
    query = text(f"SELECT * FROM {table}")
    result = session.execute(query).fetchall()
    return result


def find_all_pagination(table: str, page: int, limit: int) -> list:
    query = text(f"SELECT * FROM {table} LIMIT :limit OFFSET :offset")
    result = session.execute(
        query, {"limit": limit, "offset": (page - 1) * limit}
    ).fetchall()
    return result


def delete(table: str, id: str) -> None:
    query = text(f"DELETE FROM {table} WHERE id = :id")
    session.execute(query, {"id": id})
    session.commit()


def update(table: str, id: str, values: dict):
    query = text(
        f"UPDATE {table} SET {', '.join(key + ' = ' + value for key, value in values.items())} WHERE id = :id"
    )
    session.execute(query, {"id": id, **values})
    session.commit()
