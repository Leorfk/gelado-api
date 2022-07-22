from repositories.cliente_repository import ClienteRepository
from models.usuario_model import ClienteModel


class ClienteService:

    def __init__(self, client_repo: ClienteRepository) -> None:
        self.__client_repo = client_repo

    def cadastrar_cliente(self, id_usuario, cliente: ClienteModel):
        try:
            params = (cliente.nome, cliente.cpf_cnpj, id_usuario)
            result = self.__client_repo.insert_new_cliente(params)
        except Exception as ex:
            return {'error': ex.args}
