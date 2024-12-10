import os
from dotenv import load_dotenv
from app.logging import logger
from app.utils.general import string_snippet

# Constants
API_V1_PREFIX: str = "/api/v1"
AUTH_PREFIX: str = "/auth"

# Set the environment
ENVIRONMENT: str = os.getenv("ENVIRONMENT", "dev")
IS_DOCKER: bool = os.getenv("IS_DOCKER", "false") == "True"

# Load local .env file only if in local development
if ENVIRONMENT == "dev" and not IS_DOCKER:
    dotenv_path: str = f".env.{ENVIRONMENT}"
    logger.info(f"Local mode, loading environment variables from: {dotenv_path}")
    load_dotenv(dotenv_path)
else:
    logger.info(f"Running in {ENVIRONMENT} environment; loading environment variables from Dockerfile.")

# Environment variables
DATABASE_URL: str = os.getenv("DATABASE_URL")
TEST_DATABASE_URL: str = os.getenv("TEST_DATABASE_URL")
ALLOWED_ORIGINS: list = os.getenv("ALLOWED_ORIGINS", "").split(",")
SECRET_KEY: str = os.getenv("SECRET_KEY")
AUTH_SECRET_KEY: str = os.getenv("AUTH_SECRET_KEY")
IS_TESTING: bool = os.getenv("TESTING") == "true"
REDIS_URL: str = os.getenv("REDIS_URL")

# Configuration checks
if DATABASE_URL is None:
    raise ValueError("DATABASE_URL is not set")

# Only check TEST_DATABASE_URL if testing
if IS_TESTING:
    if TEST_DATABASE_URL is None:
        raise ValueError("TEST_DATABASE_URL is not set")

if not ALLOWED_ORIGINS:
    raise ValueError("ALLOWED_ORIGINS is not set")

if SECRET_KEY is None:
    raise ValueError("SECRET_KEY is not set")

if AUTH_SECRET_KEY is None:
    raise ValueError("AUTH_SECRET_KEY is not set")

if REDIS_URL is None:
    raise ValueError("REDIS_URL is not set")

logger.info("ENVIRONMENT: %s", ENVIRONMENT)
logger.info("IS_DOCKER: %s", IS_DOCKER)
logger.info("IS_TESTING: %s", IS_TESTING)
logger.info("API_V1_PREFIX: %s", API_V1_PREFIX)
logger.info("AUTH_PREFIX: %s", AUTH_PREFIX)
logger.info("ENVIRONMENT: %s", ENVIRONMENT)
logger.info("ALLOWED_ORIGINS: %s", ALLOWED_ORIGINS)
logger.info("DATABASE_URL: %s", string_snippet(DATABASE_URL))
logger.info("TEST_DATABASE_URL: %s", string_snippet(TEST_DATABASE_URL))
logger.info("SECRET_KEY: %s", string_snippet(SECRET_KEY))
logger.info("SECRET_KEY: %s", string_snippet(SECRET_KEY))
logger.info("AUTH_SECRET_KEY: %s", string_snippet(AUTH_SECRET_KEY))
logger.info("REDIS_URL: %s", string_snippet(REDIS_URL))
