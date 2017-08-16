{% if cookiecutter.use_django_rest_framework == 'y' %}
default_app_config = 'apps.api.config.APIConfig'
{% endif -%}
