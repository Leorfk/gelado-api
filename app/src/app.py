import uvicorn
from fastapi import FastAPI
from controllers import (
    user_role_controller,
    user_controller)
import logging

from fastapi.openapi.utils import get_openapi

logging.basicConfig(level='DEBUG')
app = FastAPI()


def swagger_configure():
    openapi_schema = get_openapi(
        title="Gelado API",
        version="1.0",
        description="Imagine uma descrição legal aqui",
        routes=app.routes,
    )
    return openapi_schema


def create_app():
    app.include_router(user_role_controller.router)
    app.include_router(user_controller.router)
    app.openapi_schema = swagger_configure()
    return app


if __name__ == '__main__':
    uvicorn.run('app:create_app', reload=True)
