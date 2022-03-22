from fastapi import APIRouter, Response, status
from configurations.injection import User


router = APIRouter(prefix='/usuario')
user_service = User().get()

@router.get('/roles/{role_id:int}', status_code=200)
def xap(role_id, response: Response):
    role = user_service
    user = role.get_role_by_id(role_id)
    if user:
        return {'id': user.id_role, 'tipo': user.texto_role}
    response.status_code = status.HTTP_404_NOT_FOUND
    return {'mensagem': f'role com o id {role_id} não localizada'}


@router.get('/glub/{toma}')
def xapxap(toma: str):
    return {'xap': toma}
