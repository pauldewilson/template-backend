import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base
from app.config import DATABASE_URL, TEST_DATABASE_URL

# Determine the database URL to use
current_database_url = TEST_DATABASE_URL if os.getenv("TESTING") == "true" else DATABASE_URL

# For async engine, the database URL needs to use 'asyncpg' driver
if current_database_url.startswith("postgresql://"):
    current_database_url = current_database_url.replace("postgresql://", "postgresql+asyncpg://")

# Initialize the async engine and session
engine = create_async_engine(current_database_url, echo=False, future=True)

# Use `async_sessionmaker` from `sqlalchemy.ext.asyncio` instead of the regular `sessionmaker`
async_session = async_sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)

# Base class for models
Base = declarative_base()

# Dependency to get the database session
async def get_db():
    """
    Get the database session.
    """
    async with async_session() as session:
        yield session
