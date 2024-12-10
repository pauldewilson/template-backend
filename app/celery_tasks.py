from celery import Celery
from app.config import REDIS_URL

# Configure Celery for the backend
celery = Celery(
    "backend",
    broker=REDIS_URL,
    backend=REDIS_URL,
)


async def enqueue_hello_world():
    """
    Enqueues the 'hello_world' task defined in celery_worker.
    """
    task_name = "celery_worker.tasks.hello_world"
    task = celery.send_task(task_name)
    return task.id
