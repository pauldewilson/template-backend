###############
# Note that this part still needs to be followed: https://support.google.com/cloud/answer/6158849?hl=en
# Stopped here because would need to get verified.
###############

# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from app.logging import logger # Empty import required for logging to work
# from sqladmin import Admin
# from starlette.middleware.sessions import SessionMiddleware
# from app.database import engine
# from app.routers.hello_world import router as hello_world_router
# from app.admin.models import UserAdmin
# from app.admin.auth import AdminAuth
# from app.routers.users import fastapi_users
# from app.routers.celery import router as celery_router
# from app.auth.backend import auth_backend
# from app.auth.oauth import google_oauth_client
# from app.schemas.users import UserRead, UserCreate, UserUpdate
# from app.config import (
#     ALLOWED_ORIGINS,
#     API_V1_PREFIX,
#     AUTH_PREFIX,
#     SECRET_KEY,
#     AUTH_SECRET_KEY
# )


# app = FastAPI()

# app.add_middleware(
#     SessionMiddleware,
#     secret_key=SECRET_KEY,
#     session_cookie="admin-session",
#     max_age=86400,
#     same_site="lax",
#     https_only=False,
#     path="/",
# )

# # Add CORS middleware
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=ALLOWED_ORIGINS,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Add admin panel
# authentication_backend = AdminAuth(secret_key=SECRET_KEY)
# admin = Admin(
#     app,
#     engine,
#     authentication_backend=authentication_backend,
#     base_url="/admin/",
#     title="Admin Panel"
# )
# admin.add_view(UserAdmin)
# app.include_router(celery_router, prefix=API_V1_PREFIX, tags=["celery"])

# # Include routers
# app.include_router(
#     hello_world_router,
#     prefix=API_V1_PREFIX,
#     tags=["hello_world"]
# )

# app.include_router(
#     fastapi_users.get_auth_router(auth_backend),
#     prefix=API_V1_PREFIX + AUTH_PREFIX,
#     tags=["auth"],
# )

# app.include_router(
#     fastapi_users.get_register_router(UserRead, UserCreate),
#     prefix=API_V1_PREFIX + AUTH_PREFIX,
#     tags=["auth"],
# )

# app.include_router(
#     fastapi_users.get_users_router(UserRead, UserUpdate),
#     prefix=API_V1_PREFIX + "/users",
#     tags=["users"],
# )

# app.include_router(
#     fastapi_users.get_reset_password_router(),
#     prefix=API_V1_PREFIX + AUTH_PREFIX,
#     tags=["auth"],
# )

# app.include_router(
#     fastapi_users.get_oauth_router(
#         google_oauth_client,
#         auth_backend,
#         AUTH_SECRET_KEY,
#         associate_by_email=True
#     ),
#     prefix=f"{API_V1_PREFIX}/auth/google",
#     tags=["auth"]
# )
