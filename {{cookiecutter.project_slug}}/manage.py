#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    # Loads environment variables from .env file
    try:
        import dotenv   # noqa
        dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
        assert os.path.isfile(dotenv_path)
        dotenv.load_dotenv(dotenv_path)
    except (ImportError, AssertionError):
        pass

    # Use settings_local.py config first and then default settings
    try:
        settings_local_path = os.path.join(
            os.path.dirname(__file__), '{{cookiecutter.project_slug}}', 'settings_local.py'
        )
        assert os.path.isfile(settings_local_path)
        settings = '{{cookiecutter.project_slug}}.settings_local'
    except AssertionError:
        settings = '{{cookiecutter.project_slug}}.settings'

    try:
        from django.core.management import execute_from_command_line    # noqa
    except ImportError:
        try:
            import django   # noqa
        except ImportError:
            raise ImportError(
                'Couldn\'t import Django. Are you sure it\'s installed and '
                'available on your PYTHONPATH environment variable? Did you '
                'forget to activate a virtual environment?'
            )
        raise

    os.environ.setdefault('PYTHONUNBUFFERED', '1')
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings)

    execute_from_command_line(sys.argv)
