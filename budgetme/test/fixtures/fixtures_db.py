from django.core.management import call_command
import pytest


@pytest.fixture(scope='session')
def django_db_setup():
    pass


@pytest.fixture(scope='session')
def django_db_modify_db_settings():
    pass


@pytest.fixture(scope='session')
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command('loaddata', 'budgetme/test/fixtures/user_data.json')
        call_command('loaddata', 'budgetme/test/fixtures/budget_data.json')
