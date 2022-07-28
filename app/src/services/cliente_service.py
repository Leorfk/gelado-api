from repositories.cliente_repository import ClienteRepository
from models.usuario_model import ClienteModel
from repositories.database_repository import MysqlConnection


class ClienteService:

    def __init__(self, db_conn: MysqlConnection, client_repo: ClienteRepository) -> None:
        self.__db = db_conn
        self.__client_repo = client_repo

    def cadastrar_cliente(self, id_usuario, cliente: ClienteModel):
        try:
            self.__db.reopen_connection()
            query, params = self.__client_repo.insert_new_cliente(
                cliente, id_usuario)
            id_cliente = self.__db.execute_query_with_lastrowid(query, params)
            self.__db.commit_transaction()
            return {
                'mensagem': 'cliente cadastrado com sucesso',
                'id_cliente': id_cliente,
                'cliente': cliente.dict(),
                'id_usuario': id_usuario
            }
        except Exception as ex:
            return {'error': ex.args}
        finally:
            self.__db.close_connection()
