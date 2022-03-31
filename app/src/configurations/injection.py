from repositories import (
    user_role_repository,
    usuario_repository,
    database_repository
)
from services import (
    user_service
)
from models import (
    user_role_model,
    usuario_model
)
from configurations.database_configuration import MysqlConnection
conn = MysqlConnection()
database_service = database_repository.DatabaseRepository(conn)
class User:
    def get_service(self):
        user_repository = usuario_repository.UsuarioRepository(database_service)
        role_repository = user_role_repository.UserRoleRepository(database_service)
        user = user_service.UserService(user_repository, role_repository)
        return user
