# Modern FastAPI Backend Template with SQLAlchemy and Redis

A production-ready template for backend applications using FastAPI, SQLAlchemy for database operations, and Redis for caching. This template includes a preconfigured authentication system, admin interface, database migrations, environment management, and more.

## Features

- ⚡️ **FastAPI** - Modern, fast web framework for building APIs with Python
- 🗄️ **SQLAlchemy** - Powerful SQL toolkit and ORM with async support
- 📦 **Alembic** - Lightweight database migration tool
- 🔒 **FastAPI Users** - Complete user management and authentication
- 👮 **Admin Interface** - Built-in admin panel with SQLAdmin and secure authentication
- 🔄 **Redis** - High-performance caching and session management
- 🌍 **CORS** - Configurable Cross-Origin Resource Sharing
- 🔐 **JWT Authentication** - Secure token-based authentication
- 📝 **Logging** - Comprehensive logging system
- 🐳 **Docker Ready** - Containerization support with Docker and docker-compose
- ✨ **Type Hints** - Full type annotation support
- 🧪 **Testing** - Pytest configuration with async support

## Getting Started

### Local Development

1. Clone the repository:
```bash
git clone https://github.com/yourusername/template-backend
cd template-backend
```

2. Create a virtual environment and install dependencies:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: .\venv\Scripts\activate
pip install -r requirements.txt
```

3. Create a `.env.dev` file with required variables:
```env
ENVIRONMENT=dev
IS_DOCKER=false
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
TEST_DATABASE_URL=postgresql://user:password@localhost:5432/test_dbname
ALLOWED_ORIGINS=http://localhost:5173,http://localhost:3000
SECRET_KEY=your-secret-key
AUTH_SECRET_KEY=your-auth-secret-key
REDIS_URL=redis://localhost:6379
```

4. Run database migrations:
```bash
alembic upgrade head
```

5. Create a superuser for admin access:
```python
# Using the FastAPI shell or a script
from app.models.users import User
from app.database import async_session
from fastapi_users.password import PasswordHelper

async with async_session() as session:
    pwd_helper = PasswordHelper()
    hashed_password = pwd_helper.hash("your-password")

    user = User(
        email="admin@example.com",
        hashed_password=hashed_password,
        is_superuser=True,
        is_verified=True,
        is_active=True
    )
    session.add(user)
    await session.commit()
```

6. Start the development server:
```bash
uvicorn app.main:app --reload
```

### Docker Development

1. Build and run using docker-compose:
```bash
docker-compose up --build
```

The API will be available at `http://localhost:8000`

## Project Structure

```bash
template-backend/
├── alembic/                # Database migrations
│   ├── versions/          # Migration versions
│   └── env.py            # Alembic configuration
├── app/
│   ├── admin/            # Admin interface
│   │   ├── auth.py      # Admin authentication
│   │   └── models.py    # Admin model views
│   ├── auth/            # Authentication
│   │   └── backend.py   # JWT authentication
│   ├── models/          # Database models
│   │   └── users.py     # User model
│   ├── routers/         # API routes
│   │   ├── hello_world.py
│   │   └── users.py
│   ├── utils/           # Utility functions
│   ├── config.py        # Configuration management
│   ├── database.py      # Database setup
│   ├── logging.py       # Logging configuration
│   ├── main.py          # Application entry point
│   ├── redis.py         # Redis configuration
│   └── schemas.py       # Pydantic models
├── tests/               # Test suite
├── .env.dev            # Development environment variables
├── Dockerfile          # Docker configuration
├── docker-compose.yml  # Docker Compose configuration
└── requirements.txt    # Python dependencies
```

## Authentication System

### User Authentication
This template includes a comprehensive authentication system featuring:
- Complete user management (register, login, password reset)
- JWT token-based authentication
- Timezone support for users
- Customizable password validation

The system provides several endpoints for user management:
- `/api/v1/auth/register` - User registration
- `/api/v1/auth/login` - User login
- `/api/v1/auth/reset-password` - Password reset
- `/api/v1/users/me` - Current user information

### Admin Interface

Access the admin interface at `/admin` with the following features:
- Secure admin authentication
- Superuser access control
- User management with CRUD operations
- Interactive dashboard
- Customizable model views

To access the admin interface:
1. Create a superuser as shown in the setup instructions
2. Navigate to `/admin`
3. Login with superuser credentials
4. Only users with `is_superuser=True` can access the admin interface

## Environment Configuration

The template supports different environment configurations:

### Local Development
Use `.env.dev` for local development settings.

### Docker Development
Environment variables are configured in:
- `Dockerfile` - Build-time defaults
- `docker-compose.yml` - Runtime overrides
- `.env.dev` - Development settings

## Database Management

### Migrations

Create and apply database migrations:
```bash
# Create a new migration
alembic revision --autogenerate -m "description"

# Apply migrations
alembic upgrade head

# Rollback migrations
alembic downgrade -1
```

### Redis Cache

The template includes Redis for caching and session management:
- Configurable connection settings
- Async Redis client
- Helper functions for common operations

## API Documentation

Once running, access the API documentation at:
- Swagger UI: `/docs`
- ReDoc: `/redoc`

## Testing

Run the test suite:
```bash
pytest
```

The template includes:
- Async test support
- Database migration testing
- Separate test database configuration
- Test utilities and fixtures

## Available Scripts

- `uvicorn app.main:app --reload` - Start development server
- `pytest` - Run test suite
- `alembic upgrade head` - Apply all migrations
- `start_backend.bat` - Windows startup script

## Docker Commands

- `docker-compose up --build` - Build and start containers
- `docker-compose up` - Start existing containers
- `docker-compose down` - Stop and remove containers

## License

Proprietary. Not for reuse.