# Load Celery app when Django starts so `config_from_object(..., namespace='CELERY')` runs
# and tasks use broker / eager settings from Django.
from .celery import app as celery_app

__all__ = ("celery_app",)
