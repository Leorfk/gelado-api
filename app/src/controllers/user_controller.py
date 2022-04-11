from http import HTTPStatus
from fastapi import APIRouter, Response, status, HTTPException
from configurations.injection import UserInjection
from models.usuario_model import UsuarioModel
from models.user_role_model import UserRoleModel

router = APIRouter(prefix='/usuario', tags=["usuario"])
user_service = UserInjection().get_service()


@router.get('/{id_usuario}', status_code=200)
def get_by_id(id_usuario):
    resp = user_service.get_usuario_by_id(id_usuario)
    return resp
    return UsuarioModel(id_usuario=id_usuario, email='toma', senha='xap', role=UserRoleModel(id_role=1, texto_role='toma'))


@router.get('/', status_code=200)
def get_all_usuario(id_usuario):
    return UsuarioModel(id_usuario=id_usuario, email='toma', senha='xap', role=UserRoleModel(id_role=1, texto_role='toma'))


@router.post('/', status_code=201)
def cadastrar_usuario(usuario: UsuarioModel):
    result = user_service.create_usuario(usuario)
    if result.get('error'):
        raise HTTPException(status_code=400, detail=result)
    return result


@router.delete('/{id_usuario}', status_code=HTTPStatus.NO_CONTENT)
def apagar_usuario(role_id):

    return Response(status_code=HTTPStatus.NO_CONTENT.value)
