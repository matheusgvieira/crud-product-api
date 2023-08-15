import uuid
from datetime import datetime


def value_to_string(value):
    if isinstance(value, str):
        return f"'{value}'"
    if isinstance(value, uuid.UUID):
        return f"'{value}'"
    if isinstance(value, datetime):
        return f"'{value}'"
    return str(value)
