from repositories.database_repository import DatabaseRepository


class UsuarioRepository:

    def __init__(self, database: DatabaseRepository):
        self.__database = database
        self.__table_usuario = 'usuario'
        self.__table_role = 'user_role'

    def select_usuario_by_id(self, id_usuario):
        query = f'''
        SELECT id_usuario, email, senha, role_id, texto_role 
        FROM {self.__table_usuario} INNER JOIN {self.__table_role}
        ON (id_role = role_id) WHERE id_usuario = (%s)'''
        params = (id_usuario,)
        result = self.__database.execute_query_with_fetchone(query, params)
        return result

    def select_all_usuario(self):
        query = f'''
        SELECT id_usuario, email, senha, role_id, texto_role 
        FROM {self.__table_usuario} INNER JOIN {self.__table_role}
        ON (id_role = role_id)'''
        result = self.__database.execute_query_with_fetchall(query)
        return result

    def insert_new_usuario(self, params: tuple):
        query = f'INSERT INTO {self.__table_usuario} (email, senha, role_id) VALUES (%s, %s, %s)'
        user_id = self.__database.execute_query_with_lastrowid(
            query, params, True)
        return user_id

    def update_usuario_by_id(self, params: tuple):
        query = f'''
        UPDATE {self.__table_usuario} SET
        email = (%s), senha = (%s), role_id = (%s)
        WHERE id_usuario = (%s);'''
        result = self.__database.execute_query_with_rowcount(
            query, params, True)
        return result

    def delete_usuario_by_id(self, user_id):
        query = f'DELETE FROM {self.__table_usuario} WHERE id_usuario = (%s)'
        params = (user_id,)
        result = self.__database.execute_query_with_rowcount(query, params, True)
        return result

    def delete_all_usuario(self):
        self.__database.delete_any(self.__table_usuario)
