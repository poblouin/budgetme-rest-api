import datetime

import pytest

from budgetme.apps.types.models import Budget


@pytest.fixture
def make_budget():

    def _format_budget_data(is_dummy=False, name='test_budget2', color_display='#FF5722', **kwargs):
        dummy_name = None
        dummy_color_display = None
        if is_dummy:
            now = datetime.datetime.now().strftime('%Y%m%d%s')
            dummy_name = 'dummy_{}'.format(now)
            dummy_color_display = '#00BCD4'

        name = name if not is_dummy else dummy_name
        budget_frequency = kwargs['budget_frequency'] if kwargs.get('budget_frequency') else Budget.MONTHLY
        amount = kwargs['amount'] if kwargs.get('amount') else 200.00
        start_date = kwargs['start_date'] if kwargs.get('start_date') else '2018-06-01'
        end_date = kwargs['end_date'] if kwargs.get('end_date') else '2018-06-30'
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

    def _make_transaction_category(budget=None, is_dummy=False, name='test_tc1'):
        dummy_name = None
        if is_dummy:
            now = datetime.datetime.now().strftime('%Y%m%d%s')
            dummy_name = 'dummy_{}'.format(now)
        name = name if not is_dummy else dummy_name
        budget = budget if budget else make_budget()

        return {
            'name': name,
            'budget': budget
        }

    return _make_transaction_category
