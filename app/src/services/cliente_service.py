from repositories.usuario_repository import UsuarioRepository
from repositories.cliente_repository import ClienteRepository
from repositories.telefone_repository import TelefoneRepository
from repositories.endereco_repository import EnderecoRepository
from models.usuario_model import UsuarioRealOficialModel


class ClienteService:

    def __init__(self,
                 user_repo: UsuarioRepository,
                 client_repo: ClienteRepository,
                 phone_repo: TelefoneRepository,
                 address_repo: EnderecoRepository) -> None:
        self.__user_repo = user_repo
        self.__client_repo = client_repo
        self.__phone_repo = phone_repo
        self.__address_repo = address_repo

    def cadastrar_cliente(self, usuario: UsuarioRealOficialModel):
        user = usuario.user
        role = usuario.user_role
        cliente = usuario.cliente
        telefones = usuario.telefones
        endereco = usuario.endereco
        self.__user_repo.insert_new_usuario()
        
        return usuario
