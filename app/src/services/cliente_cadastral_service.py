from models.usuario_model import UserRoleModel
from repositories.usuario_repository import UsuarioRepository
from repositories.cliente_repository import ClienteRepository
from repositories.telefone_repository import TelefoneRepository
from repositories.endereco_repository import EnderecoRepository
from repositories.user_role_repository import UserRoleRepository
from repositories.database_repository import MysqlConnection
from models.usuario_model import UsuarioRealOficialModel, UsuarioModel, ClienteModel, EnderecoModel, TelefoneModel


class ClienteCadastralService:

    def __init__(self,
                 db_conn: MysqlConnection,
                 role_repo: UserRoleRepository,
                 user_repo: UsuarioRepository,
                 client_repo: ClienteRepository,
                 phone_repo: TelefoneRepository,
                 address_repo: EnderecoRepository) -> None:
        self.__db = db_conn
        self.__user_role_repo = role_repo
        self.__user_repo = user_repo
        self.__client_repo = client_repo
        self.__phone_repo = phone_repo
        self.__address_repo = address_repo

    def efetuar_cadastro_cliente(self, usuario: UsuarioRealOficialModel):
        try:
            self.__db.reopen_connection()
            role = self.resgatar_id_role(
                usuario.user_role)
            if role:
                user_id = self.cadastrar_usuario(usuario.user, role[0])
                self.cadastrar_cliente(usuario.cliente, user_id)
                [self.cadastrar_telefone(t, user_id) for t in usuario.telefones]
                self.cadastrar_endereco(usuario.endereco, user_id)
                self.__db.commit_transaction()
                return {'mensagem': 'cliente cadastrado com sucesso', 'id_usuario': user_id}
            else:
                return {'error': 'role não cadastrada', 'role': usuario.user_role.texto_role}
        except Exception as ex:
            self.__db.rollback_transaction()
            return {'error': ex.args}
        finally:
            self.__db.close_connection()

    def resgatar_id_role(self, user_role: UserRoleModel) -> tuple:
        query, params = self.__user_role_repo.select_user_role_by_texto_role(user_role.texto_role)
        return self.__db.execute_query_with_fetchone(query, params)

    def cadastrar_usuario(self, user: UsuarioModel, id_role):
        query, params = self.__user_repo.insert_new_usuario(user, id_role)
        return self.__db.execute_query_with_lastrowid(query, params)

    def cadastrar_cliente(self, cliente_model: ClienteModel, user_id):
        query, params = self.__client_repo.insert_new_cliente(cliente_model, user_id)
        self.__db.execute_query(query, params)

    def cadastrar_telefone(self, telefone_model: TelefoneModel, user_id):
        query, params = self.__phone_repo.insert_new_telefone(telefone_model, user_id)
        self.__db.execute_query(query, params)

    def cadastrar_endereco(self, endereco_model: EnderecoModel, user_id):
        query, params = self.__address_repo.insert_new_endereco(endereco_model, user_id)
        self.__db.execute_query(query, params)
