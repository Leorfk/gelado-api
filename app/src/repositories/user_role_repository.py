from domains.user_role import UserRole
from models.user_role_model import User_Role


class UserRoleRepository:
    def __init__(self, database: User_Role) -> None:
        self.__user_role_model = database
    
    def update_user_role(self, id_role, user_role: UserRole) -> bool:
        new_user_role = self.get_user_role_by_id(id_role)
        if new_user_role:
            new_user_role.texto_role = user_role.texto_role
            new_user_role.save()
            return True
        return False

    def create_user_role(self, user_role: UserRole):
        self.__user_role_model.create(
            id_role=user_role.id_role,
            texto_role=user_role.texto_role)

    def delete_user_role(self, id_role: int) -> bool:
        user_role = self.get_user_role_by_id(id_role)
        if user_role:
            user_role.delete_instance()
            return True
        return False

    def get_all_user_roles(self):
        return self.__user_role_model.select(User_Role.id_role == 0)

    def get_user_role_by_id(self, id_role: int) -> User_Role:
        try:
            return self.__user_role_model.get(User_Role.id_role == id_role)
        except User_Role.DoesNotExist as ex:
            print(f'Role com id {id_role} não localizada')
            return None
