from repositories.usuario_repository import UsuarioRepository
from repositories.user_role_repository import UserRoleRepository
from models.usuario_model import UsuarioModel


class UserService:

    def __init__(self,
                 user_repository: UsuarioRepository, role_repository: UserRoleRepository) -> None:
        self.__user_repo = user_repository

    def get_all_usuario(self):
        pass

    def get_usuario_by_id(self, id_user):
        result = self.__user_repo.select_usuario_by_id(id_user)
        if result:
            return self.to_model(result)
        else:
            return None

    def create_usuario(self, usuario: UsuarioModel):
        try:
            params = (
                usuario.id_usuario,
                usuario.email,
                usuario.senha,
                usuario.role.id_role)
            self.__user_repo.insert_new_usuario(params)
            return {'message': f'Usuário cadastrado com sucesso: {usuario.email}'}
        except Exception as ex:
            return {'error': ex.args}

    def delete_usuario(self):
        pass

    def update_usuario(self):
        pass

    def to_model(result_query: tuple):
        toma = UsuarioModel([p for p in result_query])
        print(toma)
