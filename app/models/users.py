import enum

from typing import Optional, Union, Dict, Any

from fastapi import Depends, Request
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from fastapi_users import (
    BaseUserManager,
    IntegerIDMixin,
    InvalidPasswordException,
)

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import (
    Column,
    Integer,
    Enum,
)
from sqlalchemy.orm import mapped_column, Mapped

from app.database import Base, get_db
from app.config import AUTH_SECRET_KEY
from app.logging import logger
from app.schemas import UserCreate


class TimezoneEnum(str, enum.Enum):
    PACIFIC_KIRITIMATI = "Pacific/Kiritimati"  # UTC +14
    PACIFIC_AUCKLAND = "Pacific/Auckland"      # UTC +13
    PACIFIC_CHATHAM = "Pacific/Chatham"        # UTC +12:45
    PACIFIC_FIJI = "Pacific/Fiji"              # UTC +12
    PACIFIC_NOUMEA = "Pacific/Noumea"          # UTC +11
    AUSTRALIA_SYDNEY = "Australia/Sydney"      # UTC +10
    AUSTRALIA_DARWIN = "Australia/Darwin"      # UTC +9:30
    ASIA_TOKYO = "Asia/Tokyo"                  # UTC +9
    ASIA_KUALA_LUMPUR = "Asia/Kuala_Lumpur"    # UTC +8
    ASIA_BANGKOK = "Asia/Bangkok"              # UTC +7
    ASIA_DHAKA = "Asia/Dhaka"                  # UTC +6
    ASIA_KOLKATA = "Asia/Kolkata"              # UTC +5:30
    ASIA_TASHKENT = "Asia/Tashkent"            # UTC +5
    ASIA_DUBAI = "Asia/Dubai"                  # UTC +4
    ASIA_TEHRAN = "Asia/Tehran"                # UTC +3:30
    EUROPE_MOSCOW = "Europe/Moscow"            # UTC +3
    EUROPE_ATHENS = "Europe/Athens"            # UTC +2
    EUROPE_BERLIN = "Europe/Berlin"            # UTC +1
    EUROPE_LONDON = "Europe/London"            # UTC +0
    ATLANTIC_AZORES = "Atlantic/Azores"        # UTC -1
    AMERICA_NORONHA = "America/Noronha"        # UTC -2
    AMERICA_ARGENTINA_BUENOS_AIRES = "America/Argentina/Buenos_Aires"  # UTC -3
    AMERICA_HALIFAX = "America/Halifax"        # UTC -4
    AMERICA_NEW_YORK = "America/New_York"      # UTC -5
    AMERICA_CHICAGO = "America/Chicago"        # UTC -6
    AMERICA_DENVER = "America/Denver"          # UTC -7
    AMERICA_LOS_ANGELES = "America/Los_Angeles"  # UTC -8
    AMERICA_ANCHORAGE = "America/Anchorage"    # UTC -9
    PACIFIC_HONOLULU = "Pacific/Honolulu"      # UTC -10
    PACIFIC_PAGO_PAGO = "Pacific/Pago_Pago"    # UTC -11
    PACIFIC_MIDWAY = "Pacific/Midway"          # UTC -12


class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    # Use Enum for timezone
    timezone = Column(
        Enum(TimezoneEnum),
        nullable=False,
        default=TimezoneEnum.EUROPE_LONDON
    )


async def get_user_db(session: AsyncSession = Depends(get_db)):
    """
    Provides a SQLAlchemyUserDatabase instance for interacting with the user table.

    Args:
        session (AsyncSession): The SQLAlchemy async session.

    Yields:
        SQLAlchemyUserDatabase: The user database handler.
    """
    yield SQLAlchemyUserDatabase(session, User)


class UserManager(IntegerIDMixin, BaseUserManager[User, Integer]):
    """
    UserManager handles operations related to user management, such as login, registration,
    password resets, and verification.

    Attributes:
        reset_password_token_secret (str): Secret key for reset password token.
        verification_token_secret (str): Secret key for email verification token.
        reset_password_token_lifetime_seconds (int): Lifetime of the reset password token in seconds.
    """
    reset_password_token_secret = AUTH_SECRET_KEY
    verification_token_secret = AUTH_SECRET_KEY
    reset_password_token_lifetime_seconds = 86400

    async def on_after_register(
        self,
        user: User,
        request: Optional[Request] = None,
        response: Optional[Any] = None
    ):
        """
        Called after a user has registered.

        Args:
            user (User): The user who has registered.
            request (Optional[Request]): The request that triggered this action.
            response (Optional[Any]): The response object.
        """
        logger.info("User %d has registered.", user.id)

    async def on_after_forgot_password(
        self,
        user: User,
        token: str,
        request: Optional[Request] = None,
        response: Optional[Any] = None
    ):
        """
        Called after a user requests to reset their password.

        Args:
            user (User): The user who requested the password reset.
            token (str): The reset password token.
            request (Optional[Request]): The request that triggered this action.
            response (Optional[Any]): The response object.
        """
        logger.info(
            "User %d has forgotten their password. Reset token: %s", user.id, token)

    async def on_after_request_verify(
        self,
        user: User,
        token: str,
        request: Optional[Request] = None,
        response: Optional[Any] = None
    ):
        """
        Called after a user requests email verification.

        Args:
            user (User): The user requesting email verification.
            token (str): The verification token.
            request (Optional[Request]): The request that triggered this action.
            response (Optional[Any]): The response object.
        """
        logger.info(
            "Verification requested for user %d. Verification token: %s", user.id, token)

    async def on_after_login(
        self,
        user: User,
        request: Optional[Request] = None,
        response: Optional[Any] = None,
    ):
        """
        Called after a user successfully logs in.

        Args:
            user (User): The user who has logged in.
            request (Optional[Request]): The request that triggered this action.
            response (Optional[Any]): The response object.
        """
        logger.info("User %d has logged in.", user.id)

    async def on_after_update(
        self,
        user: User,
        update_dict: Dict[str, Any],
        request: Optional[Request] = None,
        response: Optional[Any] = None
    ):
        """
        Called after a user profile update.

        Args:
            user (User): The user being updated.
            update_dict (Dict[str, Any]): Dictionary containing the updates made to the user.
            request (Optional[Request]): The request that triggered this action.
            response (Optional[Any]): The response object.
        """
        logger.info("User %d has been updated with %s.", user.id, update_dict)

    async def validate_password(
        self,
        password: str,
        user: Union[UserCreate, User],
    ) -> None:
        """
        Validates a user's password according to custom business rules.

        Args:
            password (str): The password to validate.
            user (Union[UserCreate, User]): The user object being validated.

        Raises:
            InvalidPasswordException: If the password is invalid according to business rules.
        """
        if len(password) < 8:
            raise InvalidPasswordException(
                reason="Password should be at least 8 characters"
            )
        if user.email in password:
            raise InvalidPasswordException(
                reason="Password should not contain email"
            )


async def get_user_manager(user_db=Depends(get_user_db)):
    """
    Provides a UserManager instance to manage user-related actions.

    Args:
        user_db (SQLAlchemyUserDatabase): The user database handler.

    Yields:
        UserManager: The user manager for handling user actions.
    """
    yield UserManager(user_db)
