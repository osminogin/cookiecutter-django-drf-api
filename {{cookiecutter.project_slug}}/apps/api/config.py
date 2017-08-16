{% if cookiecutter.use_django_rest_framework == 'y' %}
from django.apps import AppConfig


class APIConfig(AppConfig):
    name = 'apps.api'
    verbose_name = 'API'
{% endif -%}
