from repositories.database_repository import DatabaseRepository


class ClienteRepository:

    def __init__(self, database: DatabaseRepository):
        self.__database = database
        self.__table_cliente = 'cliente'

    def select_cliente_by_id(self, id_cliente):
        query = f'''
        SELECT id_cliente, nome, cpf_cnpj, usuario_id 
        FROM {self.__table_cliente} WHERE id_cliente = (%s)'''
        params = (id_cliente,)
        result = self.__database.execute_query_with_fetchone(query, params)
        return result

    def select_all_clientes(self):
        query = f'''
        SELECT id_cliente, nome, cpf_cnpj, usuario_id 
        FROM {self.__table_cliente}'''
        result = self.__database.execute_query_with_fetchall(query)
        return result

    def insert_new_cliente(self, params: tuple):
        query = f'INSERT INTO {self.__table_cliente} (nome, cpf_cnpj, usuario_id) VALUES (%s, %s, %s)'
        user_id = self.__database.execute_query_with_lastrowid(
            query, params, True)
        return user_id

    def update_cliente_by_id(self, params: tuple):
        query = f'''
        UPDATE {self.__table_cliente} SET
        nome = (%s), cpf_cnpj = (%s), usuario_id = (%s)
        WHERE id_cliente = (%s);'''
        result = self.__database.execute_query_with_rowcount(
            query, params, True)
        return result

    def delete_cliente_by_id(self, user_id):
        query = f'DELETE FROM {self.__table_cliente} WHERE id_cliente = (%s)'
        params = (user_id,)
        result = self.__database.execute_query_with_rowcount(
            query, params, True)
        return result

    def delete_all_clientes(self):
        self.__database.delete_any(self.__table_cliente)
