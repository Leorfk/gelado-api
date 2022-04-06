from pydantic import BaseModel


class UserRoleModel(BaseModel):
    id_role: int
    texto_role: str
