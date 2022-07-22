from http import HTTPStatus
from fastapi import APIRouter, Response, HTTPException
from configurations.injection import ClienteInjection, ClienteCadastralInjection
from models.usuario_model import UsuarioRealOficialModel

router = APIRouter(prefix='/cliente', tags=["cliente"])
cliente_service = ClienteInjection().get_service()
cliente_cadastral_service = ClienteCadastralInjection().get_service()


@router.post('/toma', status_code=201)
def cadastrar_cliente(usuario: UsuarioRealOficialModel):
    result = cliente_service.cadastrar_cliente(usuario)
    return result
@router.post('/', status_code=201)
def cadastrar_cliente(usuario: UsuarioRealOficialModel):
    result = cliente_cadastral_service.efetuar_cadastro_cliente(usuario)
    if result.get('error'):
        raise HTTPException(status_code=400, detail=result)
    return result
