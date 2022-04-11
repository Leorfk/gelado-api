from repositories import (
    user_role_repository,
    usuario_repository,
    database_repository
)
from services import (
    user_service,
    user_role_service
)

from configurations.database_configuration import MysqlConnection
conn = MysqlConnection()
database_service = database_repository.DatabaseRepository(conn)


class UserRoleInjection:
    def get_service(self):
        role_repository = user_role_repository.UserRoleRepository(
            database_service)
        service = user_role_service.UserRoleService(role_repository)
        return service


class UserInjection:
    def get_service(self):
        user_repository = usuario_repository.UsuarioRepository(
            database_service)
        role_repository = user_role_repository.UserRoleRepository(
            database_service)
        service = user_service.UserService(user_repository, role_repository)
        return service
