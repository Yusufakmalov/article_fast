from fastapi import APIRouter
from user import LoginUserValidator, RegisterUserValidator

from database.userservice import login_user_db, register_user_db, get_all_users_db, get_exact_user_db

user_router = APIRouter(prefix='/user', tags=['control users'])


@user_router.post('/login')
async def login_user(data: LoginUserValidator):
    result = login_user_db(**data.model_dump())

    return {'message': result}



@user_router.post('/register')
async def register_user(data: RegisterUserValidator):
    result = register_user_db(**data.model_dump())


    if result:
        return {'message': result}
    else:
        return {'message': 'already at list'}


@user_router.get('/get_user')
async def get_user(user_id: int = 0):
    if user_id == 0:
        result = get_all_users_db()

        return {'message': result}
    else:
        result = get_exact_user_db(user_id)
        return {'message': result}