import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from controllers import (
    user_role_controller,
    user_controller)
import logging

from fastapi.openapi.utils import get_openapi

from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import Optional

logging.basicConfig(level='DEBUG')
app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None


class UserInDB(User):
    hashed_password: str


fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "fakehashedsecret",
        "disabled": False,
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderson",
        "email": "alice@example.com",
        "hashed_password": "fakehashedsecret2",
        "disabled": True,
    },
}


def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)


def fake_decode_token(token):
    # This doesn't provide any security at all
    # Check the next version
    user = get_user(fake_users_db, token)
    return user


async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


def fake_hash_password(password: str):
    return "fakehashed" + password


@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(
            status_code=400, detail="Incorrect username or password")
    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(
            status_code=400, detail="Incorrect username or password")

    return {"access_token": user.username, "token_type": "bearer"}


@app.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user


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
