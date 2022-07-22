class EnderecoRepository:

    def __init__(self):
        self.__table_endereco = 'endereco'

    def select_endereco_by_usuario_id(self, id_cliente):
        query = f'''
        SELECT
        id_endereco, municipio, bairro, nome_rua, numero, cep, usuario_id 
        FROM {self.__table_endereco} WHERE usuario_id = (%s)'''
        params = (id_cliente,)
        # result = self._execute_query_with_fetchone(query, params)
        return query, params

    def select_all_clientes(self):
        query = f'''
        SELECT id_endereco, municipio, bairro, nome_rua, numero, cep, usuario_id 
        FROM {self.__table_endereco}'''
        # result = self._execute_query_with_fetchall(query)
        return query

    def insert_new_endereco(self, params: tuple):
        query = f'''INSERT INTO {self.__table_endereco} 
        (municipio, bairro, nome_rua, numero, cep, usuario_id) 
        VALUES (%s, %s, %s, %s, %s, %s)'''
        # user_id = self._execute_query_with_lastrowid(query, params, False)
        return query, params

    def update_by_id_endereco(self, params: tuple):
        query = f'''
        UPDATE {self.__table_endereco} SET
        municipio = (%s), bairro = (%s), 
        nome_rua = (%s), numero = (%s), 
        cep = (%s), WHERE id_endereco = (%s);'''
        # result = self._execute_query_with_rowcount(query, params, False)
        return query, params

    def delete_by_id_endereco(self, user_id):
        query = f'DELETE FROM {self.__table_endereco} WHERE id_endereco = (%s)'
        params = (user_id,)
        # result = self._execute_query_with_rowcount(query, params, False)
        return query, params
