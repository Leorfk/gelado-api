from fastapi import APIRouter, Response, status, HTTPException
from configurations.injection import UserRoleInjection
from domains.user_role import UserRole

router = APIRouter(prefix='/user-role')
user_service = UserRoleInjection().get_service()


@router.get('/{role_id}', status_code=200)
def get_by_id(role_id, response: Response):
    user = user_service.get_role_by_id(role_id)
    if user:
        return user.__data__
    response.status_code = status.HTTP_404_NOT_FOUND
    return {'mensagem': f'role com o id {role_id} não localizada'}


@router.post('/', status_code=201)
def post(user_role: UserRole, response: Response):
    result = user_service.create_user_role(user_role)
    if result.get('error'):
        response.status_code = status.HTTP_400_BAD_REQUEST
        return result
    return result

@router.put('/{role_id}', status_code=204)
def update(role_id, user_role: UserRole, response: Response):
    return 'depois'

@router.delete('/', status_code=204)
def delete():
    user_service.delete_all_roles()

@router.delete('/usuario', status_code=204)
def delete_usuarios():
    user_service.delete_all_usuarios()

items = {"foo": "The Foo Wrestlers"}


@router.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item": items[item_id]}
