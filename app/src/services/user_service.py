from repositories.usuario_repository import UsuarioRepository
from models.usuario_model import UsuarioModel


class UserService:

    def __init__(self,
                 user_repository: UsuarioRepository) -> None:
        self.__user_repo = user_repository

    def get_all_usuario(self):
        pass
    def get_usuario_by_id(self):
        pass
    def create_usuario(self):
        pass
    def delete_usuario(self):
        pass
    def update_usuario(self):
        pass