from fastapi import APIRouter 


router = APIRouter()


@router.get('/')
def login():
    return {'status':'funcionando'}