from repositories.database_repository import DatabaseRepository


class UsuarioRepository:

    def __init__(self, database: DatabaseRepository):
        self.database = database
        self.__table = 'usuario'

    def insert_new_usuario(self, params: tuple):
        query = f'INSERT INTO {self.__table} (id_usuario, email, senha, role_id) VALUES (%s, %s, %s, %s)'
        try:
            self.database.execute_query(query, params)
        except Exception as e:
            print(f'pau ao inserir item na tabela {self.__table}\nErro: {e}')
    
    def delete_all_usuario(self):
        self.database.delete_any(self.__table)
