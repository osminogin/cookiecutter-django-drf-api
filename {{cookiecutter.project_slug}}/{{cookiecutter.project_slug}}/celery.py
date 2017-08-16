{% if cookiecutter.use_celery == 'y' -%}
import os

from celery import Celery

try:
    import dotenv   # noqa
    dotenv.load_dotenv(
        os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
    )
except ImportError:
    pass

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      '{{cookiecutter.project_slug}}.settings')

app = Celery('{{cookiecutter.project_slug}}')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
{% endif -%}
