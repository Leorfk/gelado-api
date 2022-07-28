from models.usuario_model import UsuarioModel
class UsuarioRepository:

    def __init__(self):
        self.__table_usuario = 'usuario'

    def select_usuario_by_id(self, id_usuario):
        query = f'''
        SELECT id_usuario, email, role_id 
        FROM {self.__table_usuario} WHERE id_usuario = (%s)'''
        params = (id_usuario,)
        # result = self._execute_query_with_fetchone(query, params)
        return query, params

    def select_all_usuario(self):
        query = f'''
        SELECT id_usuario, email, role_id 
        FROM {self.__table_usuario}'''
        # result = self._execute_query_with_fetchall(query)
        return query

    def insert_new_usuario(self, usuario: UsuarioModel, role_id):
        query = f'INSERT INTO {self.__table_usuario} (email, senha, role_id) VALUES (%s, %s, %s)'
        params = (usuario.email, usuario.senha, role_id)
        # user_id = self._execute_query_with_lastrowid(query, params, True)
        return query, params

    def update_usuario_by_id(self, usuario: UsuarioModel, role_id, user_id):
        query = f'''
        UPDATE {self.__table_usuario} SET
        email = (%s), senha = (%s), role_id = (%s)
        WHERE id_usuario = (%s);'''
        params = (usuario.email, usuario.senha, role_id, user_id)
        return query, params

    def delete_usuario_by_id(self, user_id):
        query = f'DELETE FROM {self.__table_usuario} WHERE id_usuario = (%s)'
        params = (user_id,)
        # result = self._execute_query_with_rowcount(query, params, True)
        return query, params

