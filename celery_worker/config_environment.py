import os
from dotenv import load_dotenv
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("celery_workers")

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
REDIS_URL: str = os.getenv("REDIS_URL")
DATABASE_URL: str = os.getenv("DATABASE_URL")

# Configuration checks
if REDIS_URL is None:
    raise ValueError("REDIS_URL is not set")

if DATABASE_URL is None:
    raise ValueError("DATABASE_URL is not set")

logger.info("ENVIRONMENT: %s", ENVIRONMENT)
logger.info("IS_DOCKER: %s", IS_DOCKER)
logger.info("REDIS_URL: %s", REDIS_URL)
logger.info("DATABASE_URL: %s", DATABASE_URL)
