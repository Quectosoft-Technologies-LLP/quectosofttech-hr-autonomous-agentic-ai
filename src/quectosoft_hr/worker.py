from celery import Celery
from quectosoft_hr.config.settings import get_settings
settings = get_settings()
celery_app = Celery("quectosoft_hr", broker=settings.CELERY_BROKER, backend=settings.REDIS_URL)
