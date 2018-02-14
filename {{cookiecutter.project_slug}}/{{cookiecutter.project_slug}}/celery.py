{% if cookiecutter.use_celery == 'y' -%}
import os

from celery import Celery

app = Celery('{{cookiecutter.project_slug}}')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
{% endif -%}
