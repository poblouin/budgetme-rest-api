import datetime

import pytest

from budgetme.apps.core.constants import WEEKLY


@pytest.fixture
def make_budget():

    def _format_budget_data(is_dummy=False, name='test-budget1', color_display=None, **kwargs):
        dummy_name = None
        dummy_color_display = None
        if is_dummy:
            now = datetime.datetime.now().strftime('%Y%m%d%s')
            dummy_name = 'dummy-{}'.format(now)
            dummy_color_display = '#00BCD4'

        name = name if not is_dummy else dummy_name
        budget_frequency = kwargs['budget_frequency'] if kwargs.get('budget_frequency') else WEEKLY
        amount = kwargs['amount'] if kwargs.get('amount') else 100.00
        start_date = kwargs.get('start_date')
        end_date = kwargs.get('end_date')
        color_display = color_display if not is_dummy else dummy_color_display

        return {
            'name': name,
            'budget_frequency': budget_frequency,
            'amount': amount,
            'start_date': start_date,
            'end_date': end_date,
            'color_display': color_display
        }

    return _format_budget_data


@pytest.fixture
def make_transaction_category(make_budget):

    def _make_transaction_category(budget=None, is_dummy=False, name='test-tc1'):
        dummy_name = None
        if is_dummy:
            now = datetime.datetime.now().strftime('%Y%m%d%s')
            dummy_name = 'dummy-{}'.format(now)
        name = name if not is_dummy else dummy_name
        budget = budget if budget else make_budget()

        return {
            'name': name,
            'budget': budget
        }

    return _make_transaction_category
