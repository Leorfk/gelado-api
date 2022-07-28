from models.usuario_model import TelefoneModel
class TelefoneRepository:

    def __init__(self):
        self.__table_telefone = 'telefone'

    def select_telefone_by_usuario_id(self, user_id):
        query = f'''
        SELECT id_telefone, numero_telefone, usuario_id
        FROM {self.__table_telefone} WHERE usuario_id = (%s)'''
        params = (user_id,)
        # result = self._execute_query_with_fetchone(query, params)
        return query, params

    def select_all_telefones(self):
        query = f'''
        SELECT id_telefone, numero_telefone, usuario_id 
        FROM {self.__table_telefone}'''
        # result = self._execute_query_with_fetchall(query)
        return query

    def insert_new_telefone(self, telefone_model: TelefoneModel, user_id):
        params = (telefone_model.numero_telefone, user_id)
        query = f'INSERT INTO {self.__table_telefone} (numero_telefone, usuario_id) VALUES (%s, %s)'
        # user_id = self._execute_query_with_lastrowid(query, params, False)
        return query, params

    def delete_telefone_by_numero(self, user_id):
        query = f'DELETE FROM {self.__table_telefone} WHERE numero_telefone = (%s)'
        params = (user_id,)
        # result = self._execute_query_with_rowcount(query, params, False)
        return query, params
