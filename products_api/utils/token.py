import typing as t
from fastapi.security.http import HTTPAuthorizationCredentials, HTTPBearer
from fastapi import HTTPException, Depends
from starlette import status
from pydantic import BaseModel
from .jwt import get_current_user


get_bearer_token = HTTPBearer(auto_error=False)


class UnauthorizedMessage(BaseModel):
    detail: str = "Bearer token missing or unknown"


async def get_user_by_token(
    auth: t.Optional[HTTPAuthorizationCredentials] = Depends(get_bearer_token),
) -> dict:
    # Simulate a database query to find a known token
    if auth is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=UnauthorizedMessage().detail,
        )

    token = auth.credentials
    if auth is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=UnauthorizedMessage().detail,
        )

    return get_current_user(token)
