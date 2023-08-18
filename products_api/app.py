import io
import os

from fastapi import FastAPI, Request
from starlette.middleware.cors import CORSMiddleware

from .config import settings
from .controllers import main_router

# from fastapi_jwt_auth.exceptions import AuthJWTException
# from fastapi.responses import JSONResponse


description = """
Products API 🚀
"""


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("VERSION")
    """
    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


app = FastAPI(
    title="Products API",
    description=description,
    version=read("VERSION"),
    contact={
        "name": "Matheus Gois Vieira",
        "url": "http://api.products.com/",
        "email": "matheusgoisv@gmail.com",
    },
)


# @app.exception_handler(AuthJWTException)
# def authjwt_exception_handler(request: Request, exc: AuthJWTException):
#     return JSONResponse(status_code=exc.status_code, content={"detail": exc.message})


if settings.server and settings.server.get("cors_origins", None):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.server.cors_origins,
        allow_credentials=settings.get("server.cors_allow_credentials", True),
        allow_methods=settings.get("server.cors_allow_methods", ["*"]),
        allow_headers=settings.get("server.cors_allow_headers", ["*"]),
    )

app.include_router(main_router)
