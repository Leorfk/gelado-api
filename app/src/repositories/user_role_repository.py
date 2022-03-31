from repositories.database_repository import DatabaseRepository
class UserRoleRepository:

    def __init__(self, database: DatabaseRepository):
        self.database = database
        self.__table = 'user_role'

    def insert_new_user_role(self, params: tuple):
        query = f'INSERT INTO {self.__table} (id_role, texto_role) VALUES (%s, %s)'
        self.database.execute_query(query, params)
    
    def delete_all_user_role(self):
        self.database.delete_any(self.__table)
