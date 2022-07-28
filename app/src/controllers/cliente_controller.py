from http import HTTPStatus
from fastapi import APIRouter, Response, HTTPException
from models.usuario_model import UsuarioRealOficialModel

from repositories.database_repository import MysqlConnection
from repositories.usuario_repository import UsuarioRepository
from repositories.user_role_repository import UserRoleRepository
from repositories.cliente_repository import ClienteRepository
from repositories.telefone_repository import TelefoneRepository
from repositories.endereco_repository import EnderecoRepository

from services.cliente_cadastral_service import ClienteCadastralService


router = APIRouter(prefix='/cliente', tags=["cliente"])

cliente_cadastral_service = ClienteCadastralService(
    MysqlConnection(),
    UserRoleRepository(),
    UsuarioRepository(),
    ClienteRepository(),
    TelefoneRepository(),
    EnderecoRepository()
)


@router.post('/', status_code=201)
def cadastrar_cliente(usuario: UsuarioRealOficialModel):
    result = cliente_cadastral_service.efetuar_cadastro_cliente(usuario)
    if result.get('error'):
        raise HTTPException(status_code=400, detail=result)
    return result
