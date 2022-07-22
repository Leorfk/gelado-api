class ClienteRepository:

    def __init__(self):
        self.__table_cliente = 'cliente'

    def select_cliente_by_id(self, id_cliente):
        query = f'''
        SELECT id_cliente, nome, cpf_cnpj, usuario_id 
        FROM {self.__table_cliente} WHERE id_cliente = (%s)'''
        params = (id_cliente,)
        # result = self._execute_query_with_fetchone(query, params)
        return query, params

    def select_all_clientes(self):
        query = f'''
        SELECT id_cliente, nome, cpf_cnpj, usuario_id 
        FROM {self.__table_cliente}'''
        # result = self._execute_query_with_fetchall(query)
        return query

    def insert_new_cliente(self, params: tuple):
        query = f'INSERT INTO {self.__table_cliente} (nome, cpf_cnpj, usuario_id) VALUES (%s, %s, %s)'
        # user_id = self._execute_query_with_lastrowid(query, params, False)
        return query, params

    def update_cliente_by_id(self, params: tuple):
        query = f'''
        UPDATE {self.__table_cliente} SET
        nome = (%s), cpf_cnpj = (%s), usuario_id = (%s)
        WHERE id_cliente = (%s);'''
        # result = self._execute_query_with_rowcount(query, params, False)
        return query, params

    def delete_cliente_by_id(self, user_id):
        query = f'DELETE FROM {self.__table_cliente} WHERE id_cliente = (%s)'
        params = (user_id,)
        # result = self._execute_query_with_rowcount(query, params, False)
        return query, params
