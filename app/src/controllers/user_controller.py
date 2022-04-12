from http import HTTPStatus
from fastapi import APIRouter, Response, status, HTTPException
from configurations.injection import UserInjection
from models.usuario_model import UsuarioModel
from models.user_role_model import UserRoleModel

router = APIRouter(prefix='/usuario', tags=["usuario"])
user_service = UserInjection().get_service()


@router.get('/{id_usuario}', status_code=200)
def get_usuario_by_id(id_usuario):
    user = user_service.get_usuario_by_id(id_usuario)
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return user


@router.get('/', status_code=200)
def get_all_usuario():
    users = user_service.get_all_usuario()
    if not users:
        raise HTTPException(
            status_code=404, detail="Nenhum usuário cadastrado até o momento")
    return users


@router.post('/', status_code=201)
def cadastrar_usuario(usuario: UsuarioModel):
    result = user_service.create_usuario(usuario)
    if result.get('error'):
        raise HTTPException(status_code=400, detail=result)
    return result


@router.put('/{id_usuario}', status_code=HTTPStatus.NO_CONTENT)
def update_usuario(id_usuario, usuario: UsuarioModel):
    result = user_service.atualizar_usuario(id_usuario, usuario)
    if not result:
        return Response(status_code=HTTPStatus.NO_CONTENT.value)
    elif result.get('warnning'):
        raise HTTPException(status_code=404, detail=result)
    else:
        raise HTTPException(status_code=400, detail=result)


@router.delete('/{id_usuario}', status_code=HTTPStatus.NO_CONTENT)
def delete_usuario(id_usuario: int):
    result = user_service.delete_usuario(id_usuario)
    if not result:
        return Response(status_code=HTTPStatus.NO_CONTENT.value)
    elif result.get('warnning'):
        raise HTTPException(status_code=404, detail=result)
    else:
        raise HTTPException(status_code=400, detail=result)
