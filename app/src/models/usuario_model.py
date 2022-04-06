from pydantic import BaseModel
class UsuarioModel(BaseModel):
    email: str
    senha: str
    role: int
