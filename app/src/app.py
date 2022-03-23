import uvicorn
from fastapi import FastAPI
from controllers import usuario_controller
import logging

logging.basicConfig(level='INFO')
app = FastAPI()


def create_app():
    app.include_router(usuario_controller.router)
    return app


if __name__ == '__main__':
    uvicorn.run('app:create_app', reload=True)
