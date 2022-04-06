from repositories.database_repository import DatabaseRepository


class UserRoleRepository:

    def __init__(self, database: DatabaseRepository):
        self.__database = database
        self.__table = 'user_role'

    def select_user_role_by_id_role(self, id_role):
        query = f'SELECT id_role, texto_role from {self.__table} WHERE id_role = (%s)'
        params = (id_role,)
        result = self.__database.execute_query_with_fetchone(query, params)
        return result

    def select_all_user_role(self):
        query = f'SELECT id_role, texto_role from {self.__table}'
        result = self.__database.execute_query_with_fetchall(query)
        return result

    def delete_role_by_id_role(self, id_role):
        try:
            query = F'DELETE FROM {self.__table} WHERE id_role = (%s)'
            params = (id_role,)
            result = self.__database.execute_query_with_rowcount(query, params, True)
            return result
        except Exception as ex:
            print(ex)

    def insert_new_user_role(self, params: tuple):
        query = f'INSERT INTO {self.__table} (id_role, texto_role) VALUES (%s, %s)'
        self.__database.execute_query(query, params, True)
