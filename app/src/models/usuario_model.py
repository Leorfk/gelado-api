from pydantic import BaseModel
from models.user_role_model import UserRoleModel


class UsuarioViewModel(BaseModel):
    id_usuario: int
    email: str
    senha: str
    role: UserRoleModel


class UsuarioModel(BaseModel):
    email: str
    senha: str
