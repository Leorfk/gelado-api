from repositories.user_role_repository import UserRoleRepository
from domains.user_role import UserRole


class UserRoleService:

    def __init__(self,
                 user_repository: UserRoleRepository) -> None:
        self.__repository = user_repository

    def get_role_by_id(self, role_id):
        role = self.__repository.get_user_role_by_id(role_id)
        if role:
            return role
        else:
            return None

    def create_user_role(self, user_role: UserRole):
        try:
            params = (user_role.id_role, user_role.texto_role)
            self.__repository.insert_new_user_role(params)
            self.__repository.database.commit_changes()
            return {'message': f'Role cadastrada com sucesso: {user_role.texto_role}'}
        except Exception as ex:
            return {'error': ex.args}

    def delete_all_roles(self):
        try:
            self.__repository.delete_all_user_role()
            self.__repository.database.commit_changes()
        except Exception as ex:
            print(f'erro ao deletar as roles: {ex}')

    def delete_all_usuarios(self):
        try:
            self.__user_repo.delete_all_usuario()
        except Exception as ex:
            print(f'erro ao deletar as roles: {ex}')
