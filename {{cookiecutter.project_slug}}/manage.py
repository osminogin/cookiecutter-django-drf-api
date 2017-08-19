#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    # Loads environment variables from .env file
    try:
        import dotenv   # noqa
        dotenv.load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))
    except ImportError:
        pass

    # Use settings_local.py config first and then default settings
    try:
        settings_local_path = os.path.join(
            os.path.dirname(__file__), '{{cookiecutter.project_slug}}', 'settings_local.py'
        )
        assert os.path.isfile(settings_local_path)
        os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                              '{{cookiecutter.project_slug}}.settings_local')
    except AssertionError:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                              '{{cookiecutter.project_slug}}.settings')

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
    execute_from_command_line(sys.argv)
