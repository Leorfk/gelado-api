from repositories.user_role_repository import UserRoleRepository
from models.usuario_model import UserRoleModel


class UserRoleService:

    def __init__(self,
                 user_repository: UserRoleRepository) -> None:
        self.__repository = user_repository

    def get_role_by_id(self, role_id):
        role = self.__repository.select_user_role_by_id_role(role_id)
        if role:
            return self.to_model(role)
        else:
            return None

    def get_all_user_role(self):
        result = self.__repository.select_all_user_role()
        if result:
            return self.to_array_model(result)
        else:
            return None

    def create_user_role(self, user_role: UserRoleModel):
        try:
            params = (user_role.id_role, user_role.texto_role)
            self.__repository.insert_new_user_role(params)
            return {'message': f'Role cadastrada com sucesso: {user_role.texto_role}'}
        except Exception as ex:
            return {'error': ex.args}
        
    def delete_role_by_id(self, role_id):
        return self.__repository.delete_role_by_id_role(role_id)

    def to_model(self, result: tuple):
        return UserRoleModel(id_role=result[0], texto_role=result[1])

    def to_array_model(self, result_set: list):
        return [self.to_model(r) for r in result_set]
