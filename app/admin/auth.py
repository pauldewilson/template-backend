from typing import Optional
from sqlalchemy import select
from fastapi_users.password import PasswordHelper
from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request
from starlette.responses import RedirectResponse
from app.models.users import User
from app.database import async_session
from app.logging import logger


class AdminAuth(AuthenticationBackend):
    def __init__(self, secret_key: str):
        super().__init__(secret_key=secret_key)

    async def login(self, request: Request) -> bool:
        form = await request.form()
        email, password = form["username"], form["password"]

        logger.info("Admin Login attempt for email: %s", email)

        async with async_session() as session:
            result = await session.execute(
                select(User).where(User.email == email)
            )
            user = result.scalar_one_or_none()

            if not user:
                return False

            if not user.is_superuser:
                return False

            pwd_helper = PasswordHelper()
            verified = pwd_helper.verify_and_update(
                password, user.hashed_password
            )[0]

            if not verified:
                return False

            # Set session data using SQLAdmin's expected format
            request.session.update({
                "admin_user_id": user.id,  # Changed key name
                "admin_authenticated": True  # Added explicit authentication flag
            })

            return True

    async def authenticate(self, request: Request) -> Optional[RedirectResponse]:
        # Check authentication using SQLAdmin's expected session keys
        user_id = request.session.get("admin_user_id")
        is_authenticated = request.session.get("admin_authenticated")

        if not all([user_id, is_authenticated]):
            return RedirectResponse(
                request.url_for("admin:login"),
                status_code=302
            )

        # Verify user still exists and is superuser
        async with async_session() as session:
            result = await session.execute(
                select(User).where(User.id == user_id)
            )
            user = result.scalar_one_or_none()

            if not user or not user.is_superuser:
                request.session.clear()
                return RedirectResponse(
                    request.url_for("admin:login"),
                    status_code=302
                )

        return True

    async def logout(self, request: Request) -> bool:
        request.session.clear()
        return True
