from app.models.users import User, get_user_manager
from sqlalchemy import Integer
from fastapi_users import FastAPIUsers
from app.auth.backend import auth_backend

fastapi_users = FastAPIUsers[User, Integer](
    get_user_manager,
    [auth_backend],
)
