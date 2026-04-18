"""
Celery workers consume tasks from CELERY_BROKER_URL (Redis).

If nothing runs from the queue, typical causes are:
1. No worker process — from the project root (same venv as Django):
     celery -A config worker -l info
2. CELERY_TASK_ALWAYS_EAGER is True — tasks never hit Redis (see config.settings).
   For a real queue: export CELERY_TASK_ALWAYS_EAGER=false (or run with DEBUG=False).
3. Redis URL mismatch — web app and worker must use the same CELERY_BROKER_URL / DB index.
"""
import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()