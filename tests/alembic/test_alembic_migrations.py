import pytest
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import inspect
from app.database import Base
from app.config import TEST_DATABASE_URL

@pytest.mark.migrations
@pytest.mark.asyncio
async def test_alembic_migrations():
    """
    Ensure that the database tables match the expected tables from Alembic
    """
    # Ensure test database connection
    test_database_url = TEST_DATABASE_URL
    if test_database_url.startswith("postgresql://"):
        test_database_url = test_database_url.replace("postgresql://", "postgresql+asyncpg://")

    engine = create_async_engine(test_database_url, echo=False, future=True)

    async with engine.begin() as conn:
        def get_tables(connection):
            inspector = inspect(connection)
            return inspector.get_table_names()

        tables = await conn.run_sync(get_tables)

    # Extract the metadata table names and add 'alembic_version' as it's expected from Alembic
    expected_tables = set(Base.metadata.tables.keys()) | {'alembic_version'}

    # Check that the database tables match the expected tables
    assert set(tables) == expected_tables, f"Mismatch between Alembic and metadata tables: {set(tables)} vs {expected_tables}"

    await engine.dispose()
