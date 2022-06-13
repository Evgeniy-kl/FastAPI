from fastapi import APIRouter
from models import UserStat
from funcs import get_user, get_users, delete_user

router = APIRouter()


@router.get('/get/{email}')
def get(email: str):
    return get_user(email)


@router.get('/all/')
def get_all():
    return get_users()


@router.post("/delete")
def delete(user: UserStat):
    return delete_user(user.dict())
