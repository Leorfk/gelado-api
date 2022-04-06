from pydantic import BaseModel
from models.user_role_model import UserRoleModel
class UsuarioModel(BaseModel):
    id_usuario: int
    email: str
    senha: str
    role: UserRoleModel
