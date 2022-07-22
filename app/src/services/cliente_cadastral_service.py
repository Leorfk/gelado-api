from repositories.usuario_repository import UsuarioRepository
from repositories.cliente_repository import ClienteRepository
from repositories.telefone_repository import TelefoneRepository
from repositories.endereco_repository import EnderecoRepository
from repositories.user_role_repository import UserRoleRepository
from models.usuario_model import UsuarioRealOficialModel, UsuarioModel, ClienteModel, EnderecoModel, TelefoneModel


class ClienteCadastralService:

    def __init__(self,
                 role_repo: UserRoleRepository,
                 user_repo: UsuarioRepository,
                 client_repo: ClienteRepository,
                 phone_repo: TelefoneRepository,
                 address_repo: EnderecoRepository) -> None:
        self.__user_role_repo = role_repo
        self.__user_repo = user_repo
        self.__client_repo = client_repo
        self.__phone_repo = phone_repo
        self.__address_repo = address_repo

    def efetuar_cadastro_cliente(self, usuario: UsuarioRealOficialModel):
        try:
            self.__user_role_repo.get_connection()
            role = self.__user_role_repo.select_user_role_by_texto_role(
                usuario.user_role.texto_role)
            if role:
                user_id = self.cadastrar_usuario(usuario.user, role[0])
                self.cadastrar_cliente(usuario.cliente, user_id)
                [self.cadastrar_telefone(t, user_id)
                 for t in usuario.telefones]
                self.cadastrar_endereco(usuario.endereco, user_id)
                self.__user_role_repo.commit_changes()
            else:
                return {'error': 'role não cadastrada', 'role': usuario.user_role.texto_role}
        except Exception as ex:
            self.__user_role_repo.rollback()
            return {'error': ex}
        finally:
            self.__user_role_repo.close_connection()

    def cadastrar_usuario(self, user: UsuarioModel, id_role):
        user_attributes = (user.email, user.senha, id_role)
        user_id = self.__user_repo.insert_new_usuario(user_attributes)
        return user_id

    def cadastrar_cliente(self, cliente_model: ClienteModel, user_id):
        cliente_attributes = (cliente_model.nome,
                              cliente_model.cpf_cnpj, user_id)
        self.__client_repo.insert_new_cliente(cliente_attributes)

    def cadastrar_telefone(self, telefone_model: TelefoneModel, user_id):
        telefone_attributes = (telefone_model.numero_telefone, user_id)
        self.__phone_repo.insert_new_telefone(telefone_attributes)

    def cadastrar_endereco(self, endereco_model: EnderecoModel, user_id):
        endereco_attributes = (
            endereco_model.municipio,
            endereco_model.bairro,
            endereco_model.nome_rua,
            endereco_model.cep,
            user_id)
        self.__address_repo.insert_new_endereco(endereco_attributes)
