import os
from celery import Celery
from dotenv import load_dotenv

load_dotenv()

celery_app = Celery(
    "worker",
    broker=os.getenv("REDIS_BROKER_URL"),
    backend=os.getenv("REDIS_BACKEND_URL"),
    include=["src.tasks.prediction"]
)