from repositories.user_role_repository import UserRoleRepository
from repositories.usuario_repository import UsuarioRepository


class UserService:

    def __init__(self,
                 user_repository: UsuarioRepository,
                 user_role_repository: UserRoleRepository) -> None:
        self.__user_repo = user_repository
        self.__role_repo = user_role_repository

    def get_role_by_id(self, role_id):
        role = self.__role_repo.get_user_role_by_id(role_id)
        if role:
            return role
        else:
            return None
