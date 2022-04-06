from http import HTTPStatus
from fastapi import APIRouter, Response, status, HTTPException
from configurations.injection import UserRoleInjection
from models.usuario_model import UsuarioModel
from models.user_role_model import UserRoleModel

router = APIRouter(prefix='/usuario', tags=["usuario"])


@router.get('/{id_usuario}', status_code=200)
def get_by_id(id_usuario):
    return UsuarioModel(id_usuario=id_usuario, email='toma', senha='xap', role=UserRoleModel(id_role=1, texto_role='toma'))


@router.get('/', status_code=200)
def get_all_usuario(id_usuario):
    return UsuarioModel(id_usuario=id_usuario, email='toma', senha='xap', role=UserRoleModel(id_role=1, texto_role='toma'))


@router.post('/', status_code=201)
def cadastrar_usuario(usuario: UsuarioModel):
    return usuario


@router.delete('/{id_usuario}', status_code=HTTPStatus.NO_CONTENT)
def apagar_usuario(role_id):
    return Response(status_code=HTTPStatus.NO_CONTENT.value)
