from celery import Celery
from dotenv import load_dotenv,find_dotenv
import os

load_dotenv()
dotenv_path = find_dotenv(raise_error_if_not_found=True, usecwd=True)
load_dotenv(dotenv_path)

CELERY_BROKER_URL = "redis://localhost:6379/0"
CELERY_RESULT_BACKEND = "redis://localhost:6379/0"
CELERY_BROKER_URL_TEST = "redis://localhost:6379/1"
CELERY_RESULT_BACKEND_TEST = "redis://localhost:6379/1"
CELERY_TIMEZONE = "UTC"


if os.getenv("TESTING"):
    celery = Celery(
        "tasks",
        broker=CELERY_BROKER_URL_TEST,
        backend=CELERY_RESULT_BACKEND_TEST,
        timezone=CELERY_TIMEZONE        
    )

else:
    celery = Celery(
        "tasks",
        broker=CELERY_BROKER_URL,
        backend=CELERY_RESULT_BACKEND,
        timezone=CELERY_TIMEZONE
    )
