from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqladmin import Admin
from app.logging import logger
from app.database import engine
from app.routers.hello_world import router as hello_world_router
from app.admin.models import UserAdmin
from app.routers.users import fastapi_users
from app.auth.backend import auth_backend
from app.schemas import UserRead, UserCreate, UserUpdate
from app.config import ALLOWED_ORIGINS, API_V1_PREFIX, AUTH_PREFIX

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure SQLAdmin
admin = Admin(app, engine)
admin.add_view(UserAdmin)

# Include routers
app.include_router(
    hello_world_router,
    prefix=API_V1_PREFIX,
    tags=["hello_world"]
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix=API_V1_PREFIX + AUTH_PREFIX,
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix=API_V1_PREFIX + AUTH_PREFIX,
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix=API_V1_PREFIX + "/users",
    tags=["users"],
)

app.include_router(
    fastapi_users.get_reset_password_router(),
    prefix=API_V1_PREFIX + AUTH_PREFIX,
    tags=["auth"],
)
