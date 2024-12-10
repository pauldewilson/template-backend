from celery import Celery
from celery_worker.config_environment import REDIS_URL

# Configure Celery
celery = Celery(
    "celery_worker",
    broker=REDIS_URL,
    backend=REDIS_URL,
)

celery.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
)

celery.autodiscover_tasks(packages=[
    "celery_worker",
])
