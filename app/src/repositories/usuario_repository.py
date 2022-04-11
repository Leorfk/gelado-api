from repositories.database_repository import DatabaseRepository


class UsuarioRepository:

    def __init__(self, database: DatabaseRepository):
        self.__database = database
        self.__table_usuario = 'usuario'
        self.__table_role = 'user_role'

    def select_usuario_by_id(self, id_usuario):
        query = f'''
        SELECT id_usuario, email, senha, texto_role 
        FROM {self.__table_usuario} INNER JOIN {self.__table_role}
        ON (id_role = role_id) WHERE id_usuario = (%s)'''
        params = (id_usuario,)
        result = self.__database.execute_query_with_fetchone(query, params)
        return result

    def insert_new_usuario(self, params: tuple):
        query = f'INSERT INTO {self.__table_usuario} (id_usuario, email, senha, role_id) VALUES (%s, %s, %s, %s)'
        self.__database.execute_query(query, params)

    def delete_all_usuario(self):
        self.database.delete_any(self.__table_usuario)
