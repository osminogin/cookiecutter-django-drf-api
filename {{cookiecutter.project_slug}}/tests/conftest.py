import pytest
from django.core import management


def pytest_addoption(parser):
    parser.addoption('--online', action='store_true',
                     help='network connection required tests')


@pytest.fixture(scope='session')
def initial_data(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        management.call_command('loaddata', 'fixtures/initial_data.json')


@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db):
    pass
