import asyncio
from app.admin.superuser import create_superuser

if __name__ == "__main__":
    asyncio.run(create_superuser())
