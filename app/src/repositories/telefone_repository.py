from repositories.database_repository import DatabaseRepository


class TelefoneRepository:

    def __init__(self, database: DatabaseRepository):
        self.__database = database
        self.__table_telefone = 'telefone'

    def select_telefone_by_usuario_id(self, id_usuario):
        query = f'''
        SELECT id_telefone, numero_telefone, usuario_id
        FROM {self.__table_telefone} WHERE usuario_id = (%s)'''
        params = (id_usuario,)
        result = self.__database.execute_query_with_fetchone(query, params)
        return result

    def select_all_telefones(self):
        query = f'''
        SELECT id_telefone, numero_telefone, usuario_id 
        FROM {self.__table_telefone}'''
        result = self.__database.execute_query_with_fetchall(query)
        return result

    def insert_new_telefone(self, params: tuple):
        query = f'INSERT INTO {self.__table_telefone} (numero_telefone, usuario_id) VALUES (%s, %s)'
        user_id = self.__database.execute_query_with_lastrowid(
            query, params, True)
        return user_id

    def delete_telefone_by_numero(self, user_id):
        query = f'DELETE FROM {self.__table_telefone} WHERE numero_telefone = (%s)'
        params = (user_id,)
        result = self.__database.execute_query_with_rowcount(
            query, params, True)
        return result
