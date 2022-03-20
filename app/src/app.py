import uvicorn
from fastapi import FastAPI
from controllers import app_controller, usuario_controller

app = FastAPI()


def create_app():
    app.include_router(app_controller.router)
    app.include_router(usuario_controller.router)
    return app


if __name__ == '__main__':
    uvicorn.run('app:create_app', reload=True)
