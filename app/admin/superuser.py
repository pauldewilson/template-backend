from app.models.users import User
from app.database import async_session
from fastapi_users.password import PasswordHelper


async def create_superuser():
    async with async_session() as session:
        email = input("Enter the email: ")

        # check if user already exists
        user = await session.execute(User.__table__.select().where(User.email == email))
        user = user.scalars().first()
        if user:
            print("User already exists")
            return

        password = input("Enter the password: ")
        pwd_helper = PasswordHelper()
        hashed_password = pwd_helper.hash(password)

        user = User(
            email=email,
            hashed_password=hashed_password,
            is_superuser=True,
            is_verified=True,
            is_active=True
        )
        session.add(user)
        await session.commit()
