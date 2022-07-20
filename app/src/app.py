# https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/
import uvicorn
from fastapi import FastAPI
from controllers import (user_role_controller, user_controller)
import logging
from fastapi.openapi.utils import get_openapi


logging.basicConfig(level='DEBUG')
app = FastAPI()


def get_tags():
    return [
        {
            'name': 'usuario',
            'description': 'crud para usuários genéricos'
        },
        {
            'name': 'user-role',
            'description': 'roles para controle de usuário'
        }
    ]


def swagger_configure():
    app.include_router(user_role_controller.router)
    app.include_router(user_controller.router)
    openapi_schema = get_openapi(
        title="Gelado API",
        version="1.0",
        description="Imagine uma descrição legal aqui",
        routes=app.routes,
        tags=get_tags()
    )
    return openapi_schema


def create_app():
    app.openapi_schema = swagger_configure()
    return app


if __name__ == '__main__':
    uvicorn.run('app:create_app', reload=True)
