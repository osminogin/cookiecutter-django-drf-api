#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':

    try:
        import dotenv   # noqa
        dotenv.load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))
    except ImportError:
        pass

    os.environ.setdefault('PYTHONUNBUFFERED', '1')
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

    execute_from_command_line(sys.argv)
