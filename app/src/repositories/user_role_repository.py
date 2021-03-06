class UserRoleRepository:

    def __init__(self):
        self.__table = 'user_role'

    def select_user_role_by_id_role(self, id_role):
        query = f'SELECT id_role, texto_role from {self.__table} WHERE id_role = (%s)'
        params = (id_role,)
        return query, params

    def select_user_role_by_texto_role(self, role: str):
        query = f'SELECT id_role, texto_role from {self.__table} WHERE texto_role = (%s)'
        params = (role,)
        return query, params

    def select_all_user_role(self):
        query = f'SELECT id_role, texto_role from {self.__table}'
        return query

    def delete_role_by_id_role(self, id_role):
        query = F'DELETE FROM {self.__table} WHERE id_role = (%s)'
        params = (id_role,)
        return query, params

    def insert_new_user_role(self, user_role_model):
        query = f'INSERT INTO {self.__table} (id_role, texto_role) VALUES (%s, %s)'
        params = (user_role_model.id_role, user_role_model.texto_role)
        return query, params
