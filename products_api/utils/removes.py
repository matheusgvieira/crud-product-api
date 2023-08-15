def remove_key_with_value_none(dictionary: dict) -> dict:
    return {key: value for key, value in dictionary.items() if value is not None}
