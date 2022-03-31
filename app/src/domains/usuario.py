from pydantic import BaseModel

class Usuario(BaseModel):

    def __init__(self, email, senha, role) -> None:
        self.__email = email
        self.__senha = senha
        self.__role_id = role

    @property
    def email(self):
        return self.__email

    @property
    def senha(self):
        return self.__senha

    @property
    def role_id(self):
        return self.__role_id
