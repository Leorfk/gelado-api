from fastapi import APIRouter, Response, status
from configurations.injection import User
from domains.user_role import UserRole

router = APIRouter(prefix='/usuario')
user_service = User().get_service()


@router.get('/roles/{role_id}', status_code=200)
def get_by_id(role_id, response: Response):
    user = user_service.get_role_by_id(role_id)
    if user:
        return user.__data__
    response.status_code = status.HTTP_404_NOT_FOUND
    return {'mensagem': f'role com o id {role_id} não localizada'}


@router.post('/roles', status_code=201)
def post(user_role: UserRole, response: Response):
    result = user_service.create_user_role(user_role)
    if result.get('error'):
        response.status_code = status.HTTP_400_BAD_REQUEST
        return result
    return result

@router.put('/roles/{role_id}', status_code=204)
def update(role_id, user_role: UserRole, response: Response):
    return 'depois'
