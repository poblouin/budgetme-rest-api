import datetime
import random

import pytest

from budgetme.apps.core.constants import DAILY


@pytest.fixture
def make_transaction(make_transaction_category):

    def _make_transaction(transaction_category=None, budget=None, **kwargs):
        now = datetime.datetime.now().strftime('%Y%m%d%s')
        amount = kwargs['amount'] if kwargs.get('amount') else round(random.uniform(0.0, 9999.99), random.randint(0, 2))
        date = kwargs['date'] if kwargs.get('date') else datetime.datetime.now().strftime('%Y-%m-%d')
        description = kwargs['description'] if kwargs.get('description') else 'dummy_{}'.format(now)
        transaction_category = transaction_category if transaction_category else make_transaction_category(budget=budget)

        return {
            'amount': amount,
            'date': date,
            'description': description,
            'transaction_category': transaction_category
        }

    return _make_transaction


@pytest.fixture
def make_scheduled_transaction(make_transaction_category):

    def _make_scheduled_transaction(transaction_category=None, budget=None, **kwargs):
        now = datetime.datetime.now().strftime('%Y%m%d%s')
        amount = kwargs['amount'] if kwargs.get('amount') else round(random.uniform(0.0, 9999.99), random.randint(0, 2))
        description = kwargs['description'] if kwargs.get('description') else 'dummy_{}'.format(now)
        frequency = kwargs['frequency'] if kwargs.get('frequency') else DAILY
        start_date = datetime.datetime.now().strftime('%Y-%m-%d')
        end_date = kwargs['end_date'] if kwargs.get('end_date') else None
        transaction_category = transaction_category if transaction_category else make_transaction_category(budget=budget)

        return {
            'amount': amount,
            'description': description,
            'frequency': frequency,
            'start_date': start_date,
            'end_date': end_date,
            'transaction_category': transaction_category
        }

    return _make_scheduled_transaction
