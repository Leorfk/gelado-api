from domains.user_role import UserRole
from models.user_role_model import User_Role
from repositories.user_role_repository import UserRoleRepository
import peewee
if __name__ == '__main__':
    role = UserRole(70, 'XAMBRE')
    repo = UserRoleRepository(User_Role)
    # repo.create_user_role(role)
    # role = repo.get_user_role_by_id(9)
    # print(xap.id_role)
    # print(xap.texto_role)
    # roles = repo.get_all_user_roles()
    # for role in roles:
    #     print(role.id_role)
    # repo.update_user_role(7, role)
    # repo.delete_user_role(7)
