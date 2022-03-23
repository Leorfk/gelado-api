from pydantic import BaseModel


class UserRole(BaseModel):
    id_role: int
    texto_role: str
