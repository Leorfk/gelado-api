from repositories import (
    user_role_repository,
    usuario_repository,
    database_repository,
    cliente_repository,
    telefone_repository,
    endereco_repository
)
from services import (
    user_service,
    user_role_service,
    cliente_service
)
from configurations.database_configuration import MysqlConnection
conn = MysqlConnection()
database_service = database_repository.DatabaseRepository(conn)
role_repository = user_role_repository.UserRoleRepository(database_service)
user_repository = usuario_repository.UsuarioRepository(database_service)
client_repository = cliente_repository.ClienteRepository(database_service)
phone_repository = telefone_repository.TelefoneRepository(database_service)
address_repository = endereco_repository.EnderecoRepository(database_service)


class UserRoleInjection:
    def get_service(self):
        return user_role_service.UserRoleService(role_repository)


class UserInjection:
    def get_service(self):
        return user_service.UserService(user_repository, role_repository)


class ClienteInjection:
    def get_service(self):
        return cliente_service.ClienteService(user_repository, client_repository, phone_repository, address_repository)
