from fastapi import APIRouter, Request, Depends
from app.logging import logger
from app.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from app.redis import get_redis
router = APIRouter()


@router.get("/ping")
async def hello_world(
    request: Request,
    db: AsyncSession = Depends(get_db)
):
    """
    Hello World endpoint.
    """
    logger.info("Ping endpoint")
    return "pong"

@router.get("/ping_redis")
async def hello_world(
    request: Request,
    redis = Depends(get_redis)
):
    """
    Hello Redis endpoint.
    """
    # add redis key hellow world to redis
    await redis.set("ping", "pong from redis server")
    # get redis key hello
    value = await redis.get("ping")
    logger.info("Ping Redis endpoint")
    return value
