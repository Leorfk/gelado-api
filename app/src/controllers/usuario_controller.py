from fastapi import APIRouter

router = APIRouter(prefix='/usuario')


@router.get('/')
def xap():
    return {'xap': 'mama'}


@router.get('/glub/{toma}')
def xapxap(toma: str):
    return {'xap': toma}
