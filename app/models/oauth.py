from typing import List
from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import Mapped, relationship, mapped_column
from fastapi_users.db import SQLAlchemyBaseOAuthAccountTable
from app.database import Base

class OAuthAccount(SQLAlchemyBaseOAuthAccountTable[int], Base):
    __tablename__ = "oauth_accounts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("users.id", ondelete="cascade"),
        nullable=False
    )

    oauth_name: Mapped[str] = mapped_column(String(length=100), nullable=False)
    access_token: Mapped[str] = mapped_column(String(length=1024), nullable=False)
    expires_at: Mapped[int] = mapped_column(Integer, nullable=True)
    refresh_token: Mapped[str] = mapped_column(String(length=1024), nullable=True)
    account_id: Mapped[str] = mapped_column(String(length=320), nullable=False)
    account_email: Mapped[str] = mapped_column(String(length=320), nullable=False)