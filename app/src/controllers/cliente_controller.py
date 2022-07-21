from http import HTTPStatus
from fastapi import APIRouter, Response, HTTPException
from configurations.injection import ClienteInjection
from models.usuario_model import UsuarioRealOficialModel

router = APIRouter(prefix='/cliente', tags=["cliente"])
cliente_service = ClienteInjection().get_service()


@router.post('/', status_code=201)
def cadastrar_cliente(usuario: UsuarioRealOficialModel):
    result = cliente_service.cadastrar_cliente(usuario)
    return result
