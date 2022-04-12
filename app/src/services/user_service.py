import logging
from repositories.usuario_repository import UsuarioRepository
from repositories.user_role_repository import UserRoleRepository
from models.usuario_model import UsuarioModel
from models.user_role_model import UserRoleModel


class UserService:

    def __init__(self,
                 user_repository: UsuarioRepository, role_repository: UserRoleRepository) -> None:
        self.__user_repo = user_repository
        self.__role_repository = role_repository

    def get_all_usuario(self):
        users = self.__user_repo.select_all_usuario()
        if users:
            return self.to_array_model(users)
        else:
            return None

    def get_usuario_by_id(self, id_user):
        result = self.__user_repo.select_usuario_by_id(id_user)
        if result:
            return self.to_model(result)
        else:
            return None

    def create_usuario(self, usuario: UsuarioModel):
        params = (usuario.email, usuario.senha, usuario.role.id_role)
        try:
            user_id = self.__user_repo.insert_new_usuario(params)
            return {'message': f'Usuário cadastrado com sucesso',
                    'id': user_id,
                    'email': usuario.email}
        except Exception as ex:
            return {'error': ex.args}

    def delete_usuario(self, user_id):
        try:
            if self.__user_repo.delete_usuario_by_id(user_id):
                return None
            else:
                return {'warnning': 'usuario inexistente'}
        except Exception as ex:
            return {'error': ex.args}

    def atualizar_usuario(self, user_id, usuario: UsuarioModel):
        params = (usuario.email, usuario.senha, usuario.role.id_role, user_id)
        try:
            if self.is_role_cadastrada(usuario.role.id_role):
                if self.__user_repo.update_usuario_by_id(params):
                    return None
                else:
                    return {'warnning': 'usuario não encontrado'}
            else:
                return {'warnning': 'role não cadastrada'}
        except Exception as ex:
            return {'error': ex.args}
    
    def is_role_cadastrada(self, id_role):
        return self.__role_repository.select_user_role_by_id_role(id_role)

    def to_model(self, result_query: tuple):
        user_role = UserRoleModel(id_role=result_query[3], texto_role=result_query[4])
        user = UsuarioModel(id_usuario=result_query[0], email=result_query[1], senha=result_query[2], role=user_role)
        return user

    def to_array_model(self, result_set: list):
        return [self.to_model(user) for user in result_set]
