from .config import celery

@celery.task(
    name="celery_worker.tasks.hello_world",
    result_backend_transport_options={
        'key_prefix': 'hello_world_from_celery'
    }
)
def hello_world():
    """
    A simple task that returns a dictionary with a key 'celery hello' and value 'world'.
    """
    return {"celery hello": "world"}
