from fastapi import Request
from sqladmin import ModelView
from app.models.users import User
from typing import Any
from datetime import datetime
from datetime import UTC


class UserAdmin(ModelView, model=User):
    column_list = [
        User.id,
        User.email,
        User.timezone,
        User.is_active,
        User.is_superuser,
        User.is_verified,
        User.created_at,
    ]
    column_details_list = [
        User.id,
        User.email,
        User.timezone,
        User.is_active,
        User.is_superuser,
        User.is_verified,
        User.created_at,
    ]
    column_searchable_list = [User.email]
    column_sortable_list = [User.id, User.email]
    column_default_sort = [(User.email, True)]
    can_create = True
    can_edit = True
    can_delete = True
    can_view_details = True
    name = "User"
    name_plural = "Users"
    icon = "fa-solid fa-users"
    form_columns = [
        "email",
        "hashed_password",
        "timezone",
        "is_active",
        "is_superuser",
        "is_verified",
    ]

    async def on_model_change(self, data: dict, model: Any, is_created: bool, request: Request) -> None:
        """Hash password using bcrypt directly"""
        if 'hashed_password' in data and data['hashed_password']:
            import bcrypt
            password = data['hashed_password'].encode('utf-8')
            salt = bcrypt.gensalt()
            hashed = bcrypt.hashpw(password, salt)
            data['hashed_password'] = hashed.decode('utf-8')

            # Set is_verified and is_active for new users
            if is_created:
                data['is_active'] = True
                data['created_at'] = datetime.now(UTC)
