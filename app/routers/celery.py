from fastapi import APIRouter, Depends
from app.models.users import User
from app.celery_tasks import enqueue_hello_world
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.routers.users import fastapi_users

current_user = fastapi_users.current_user(active=True)

router = APIRouter()


@router.post("/celery/helloworld/")
async def hello_world_celery(
    user: User = Depends(current_user),
    db: AsyncSession = Depends(get_db)
):
    task_id = await enqueue_hello_world()  # Await the coroutine
    return {"task_id": task_id, "status": "Hello World task enqueued"}
