import uvicorn
from fastapi import FastAPI
from controllers import app_controller

def create_app():
    fast_app = FastAPI()
    fast_app.include_router(app_controller.router)
    return fast_app

if __name__ == '__main__':
    app = create_app()
    uvicorn.run('app:create_app', reload=True)