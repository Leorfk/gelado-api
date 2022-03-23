from repositories import (
    user_role_repository,
    usuario_repository
)
from services import (
    user_service
)
from models import (
    user_role_model,
    usuario_model
)


class User:
    def get_service(self):
        return user_service.UserService(
            usuario_repository.UsuarioRepository(),
            user_role_repository.UserRoleRepository())
