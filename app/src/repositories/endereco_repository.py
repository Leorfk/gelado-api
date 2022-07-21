from repositories.database_repository import DatabaseRepository


class EnderecoRepository:

    def __init__(self, database: DatabaseRepository):
        self.__database = database
        self.__table_endereco = 'endereco'

    def select_endereco_by_usuario_id(self, id_cliente):
        query = f'''
        SELECT
        id_endereco, municipio, bairro, nome_rua, numero, cep, usuario_id 
        FROM {self.__table_endereco} WHERE usuario_id = (%s)'''
        params = (id_cliente,)
        result = self.__database.execute_query_with_fetchone(query, params)
        return result

    def select_all_clientes(self):
        query = f'''
        SELECT id_endereco, municipio, bairro, nome_rua, numero, cep, usuario_id 
        FROM {self.__table_endereco}'''
        result = self.__database.execute_query_with_fetchall(query)
        return result

    def insert_new_cliente(self, params: tuple):
        query = f'''INSERT INTO {self.__table_endereco} 
        (municipio, bairro, nome_rua, numero, cep, usuario_id) 
        VALUES (%s, %s, %s, %s, %s, %s)'''
        user_id = self.__database.execute_query_with_lastrowid(
            query, params, True)
        return user_id

    def update_by_id_endereco(self, params: tuple):
        query = f'''
        UPDATE {self.__table_endereco} SET
        municipio = (%s), 
        bairro = (%s), 
        nome_rua = (%s), 
        numero = (%s), 
        cep = (%s), 
        WHERE id_endereco = (%s);'''
        result = self.__database.execute_query_with_rowcount(
            query, params, True)
        return result

    def delete_by_id_endereco(self, user_id):
        query = f'DELETE FROM {self.__table_endereco} WHERE id_endereco = (%s)'
        params = (user_id,)
        result = self.__database.execute_query_with_rowcount(
            query, params, True)
        return result
