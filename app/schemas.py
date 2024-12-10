from typing import Optional
from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    timezone: str = None


class UserCreate(schemas.BaseUserCreate):
    timezone: Optional[str] = "Europe/London"


class UserUpdate(schemas.BaseUserUpdate):
    timezone: Optional[str]
