import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BBC.settings')

app = Celery('BBC')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'action_every_monday_8am': {
        'task': 'news.tasks.send_mail_weekly',
        'schedule': crontab(hour=8, minute=0, day_of_week='monday'),
        'args': (),
    },
}

app.conf.timezone = 'UTC'