import jwt
from datetime import datetime, timedelta
from products_api.config import settings
from fastapi import HTTPException, Depends
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode,
        settings.server.authjwt_secret_key,
        algorithm=settings.server.authjwt_algorithm,
    )
    return encoded_jwt


def get_current_user(token: str):
    try:
        payload = jwt.decode(
            token,
            settings.server.authjwt_secret_key,
            algorithms=[settings.server.authjwt_algorithm],
        )
        if payload is None:
            raise HTTPException(status_code=401, detail="Invalid credentials")

        payload.pop("exp")
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.DecodeError:
        raise HTTPException(status_code=401, detail="Invalid token")


def get_password_hash(password):
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)
