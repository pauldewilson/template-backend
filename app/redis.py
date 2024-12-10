import redis.asyncio as redis
from redis.asyncio.client import Redis
from typing import Dict, Any, Optional
from app.config import REDIS_URL

redis_client: Redis = None


async def get_redis() -> Redis:
    global redis_client
    if redis_client is None:
        redis_client = redis.from_url(REDIS_URL, decode_responses=True)
    return redis_client
