from typing import List

from fastapi import APIRouter
from schema import UserStat
from services import UserManage

router = APIRouter()


@router.get('/{email}', response_model=List[UserStat])
def get(email: str):
    return UserManage.get_user(email)


@router.get('/all', response_model=List[UserStat])
def get_all():
    return UserManage.get_users()


@router.delete("/{email}", response_model=List[UserStat])
def delete(email: str):
    return UserManage.delete_user(email)
