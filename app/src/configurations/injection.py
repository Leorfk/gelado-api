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
    cliente_service,
    cliente_cadastral_service
)
from configurations.database_configuration import MysqlConnection
conn = MysqlConnection()
role_repo = user_role_repository.UserRoleRepository()
user_repo = usuario_repository.UsuarioRepository()
client_repo = cliente_repository.ClienteRepository()
phone_repo = telefone_repository.TelefoneRepository()
address_repo = endereco_repository.EnderecoRepository()


class UserRoleInjection:
    def get_service(self):
        return user_role_service.UserRoleService(role_repo, conn)


class UserInjection:
    def get_service(self):
        return user_service.UserService(user_repo, role_repo, conn)


class ClienteInjection:
    def get_service(self):
        return cliente_service.ClienteService(client_repo)


class ClienteCadastralInjection:
    def get_service(self):
        return cliente_cadastral_service.ClienteCadastralService(

            role_repo=role_repo,
            user_repo=user_repo,
            client_repo=client_repo,
            phone_repo=phone_repo,
            address_repo=address_repo
        )
