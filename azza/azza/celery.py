import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'azza.settings')

app = Celery('azza')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'every-5-seconds': {
        'task': 'cakes.tasks.check_expire',
        'schedule': 5
    },
}