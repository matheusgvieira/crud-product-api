from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
from products_api.database import engine
from products_api.utils.strings import value_to_string

Session = sessionmaker(bind=engine)
session = Session()


def helth_check():
    query = text("SELECT 1")
    session.execute(query)
    return True


def list_tables():
    query = text("SHOW TABLES")
    result = session.execute(query).fetchall()
    return result


def create(table: str, values: dict) -> None:
    query = text(
        f"INSERT INTO {table} ({', '.join(values.keys())}) VALUES ({', '.join(value_to_string(value) for value in values.values())})"
    )
    session.execute(query, values)
    session.commit()


def count(table: str) -> int:
    query = text(f"SELECT COUNT(*) FROM {table} WHERE deleted_at IS NULL")
    result = session.execute(query).fetchone()
    return result[0]


def count_removed(table: str) -> int:
    query = text(f"SELECT COUNT(*) FROM {table} WHERE deleted_at IS NOT NULL")
    result = session.execute(query).fetchone()
    return result[0]


def find(table: str, conditions: str) -> list:
    query = text(f"SELECT * FROM {table} WHERE {conditions}")
    result = session.execute(query).fetchall()
    return result


def find_by_id(table: str, id: str):
    query = text(f"SELECT * FROM {table} WHERE id_product = :id")
    result = session.execute(query, {"id": id}).fetchone()
    return result


def find_all(table: str) -> list:
    query = text(f"SELECT * FROM {table}")
    result = session.execute(query).fetchall()
    return result


def find_all_pagination(table: str, page: int, limit: int) -> list:
    query = text(
        f"SELECT * FROM {table} WHERE deleted_at IS NULL LIMIT :limit OFFSET :offset"
    )
    result = session.execute(
        query, {"limit": limit, "offset": (page - 1) * limit}
    ).fetchall()
    return result


def delete(table: str, id: str) -> None:
    query = text(f"DELETE FROM {table} WHERE id_product = :id")
    session.execute(query, {"id": id})
    session.commit()


def soft_delete(table: str, id: str) -> None:
    query = text(f"UPDATE {table} SET deleted_at = NOW() WHERE id_product = :id")
    session.execute(query, {"id": id})
    session.commit()


def update(table: str, id: str, values: dict):
    query = text(
        f"UPDATE {table} SET {', '.join(f'{key} = {value_to_string(value)}' for key, value in values.items())} WHERE id_product = :id"
    )
    session.execute(query, {"id": id})
    session.commit()
