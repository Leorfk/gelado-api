from fastapi import APIRouter

router = APIRouter(prefix='/toma')

@router.get('/')
def xap():
    return {'xap':'mama'}
