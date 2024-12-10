from fastapi_users.authentication import (
    AuthenticationBackend,
    BearerTransport,
    JWTStrategy
)
from app.config import AUTH_SECRET_KEY, API_V1_PREFIX

bearer_transport = BearerTransport(tokenUrl=f"{API_V1_PREFIX}/auth/login")

def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=AUTH_SECRET_KEY, lifetime_seconds=86400)

auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)
