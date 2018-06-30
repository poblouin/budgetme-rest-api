import datetime
import random

import pytest


@pytest.fixture
def make_transaction(make_transaction_category):

    def _make_transaction(transaction_category=None, **kwargs):
        now = datetime.datetime.now().strftime('%Y%m%d%s')
        amount = kwargs['amount'] if kwargs.get('amount') else round(random.uniform(0.0, 9999.99), random.randint(0, 2))
        date = kwargs['date'] if kwargs.get('date') else datetime.datetime.now().strftime('%Y-%m-%d')
        description = kwargs['description'] if kwargs.get('description') else 'dummy_{}'.format(now)
        transaction_category = transaction_category if transaction_category else make_transaction_category()

        return {
            'amount': amount,
            'date': date,
            'description': description,
            'transaction_category': transaction_category
        }

    return _make_transaction
