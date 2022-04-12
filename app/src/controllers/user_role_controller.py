from http import HTTPStatus
from fastapi import APIRouter, Response, status, HTTPException
from configurations.injection import UserRoleInjection
from models.user_role_model import UserRoleModel

router = APIRouter(prefix='/user-role', tags=['user-role'])
user_role_service = UserRoleInjection().get_service()


@router.get('/{role_id}', status_code=200)
def get_role_by_id(role_id, response: Response):
    role = user_role_service.get_role_by_id(role_id)
    if role:
        return role
    response.status_code = status.HTTP_404_NOT_FOUND
    return {'mensagem': f'role com o id {role_id} não localizada'}


@router.get('/', status_code=200)
def get_all_roles():
    roles = user_role_service.get_all_user_role()
    if not roles:
        raise HTTPException(status_code=404, detail="Nenhuma role cadastrada")
    return roles


@router.post('/', status_code=201)
def post(user_role: UserRoleModel):
    result = user_role_service.create_user_role(user_role)
    if result.get('error'):
        raise HTTPException(status_code=400, detail=result)
    return result


@router.delete('/{role_id}', status_code=HTTPStatus.NO_CONTENT)
def delete(role_id):
    result = user_role_service.delete_role_by_id(role_id)
    if not result:
        raise HTTPException(status_code=404, detail="Role inexistente")
    return Response(status_code=HTTPStatus.NO_CONTENT.value)


items = {"foo": "The Foo Wrestlers"}


@router.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item": items[item_id]}
