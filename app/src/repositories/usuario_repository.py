from models.usuario_model import Usuario


class UsuarioRepository:

    def __init__(self, database: Usuario) -> None:
        self.__usuario_model = database

    def create_usuario(self):
        pass

    def delete_usuario(self):
        pass

    def update_usuario(self):
        pass

    def get_all_usuario(self):
        pass
