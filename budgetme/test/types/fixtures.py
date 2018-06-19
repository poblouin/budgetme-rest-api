import datetime

import pytest

from budgetme.apps.types.models import Budget


@pytest.fixture
def make_budget():

    def _format_budget_data(**kwargs):
        now = datetime.datetime.now().strftime('%Y%m%d%s')
        name = kwargs['name'] if kwargs.get('name') else 'dummy_{}'.format(now)
        budget_frequency = kwargs['budget_frequency'] if kwargs.get('budget_frequency') else Budget.WEEKLY
        amount = kwargs['amount'] if kwargs.get('amount') else 100.00
        start_date = kwargs['start_date'] if kwargs.get('start_date') else '2018-06-01'
        end_date = kwargs['end_date'] if kwargs.get('end_date') else '2018-06-30'
        color_display = kwargs['color_display'] if kwargs.get('color_display') else '#00BCD4'

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

    def _make_transaction_category(budget=None, **kwargs):
        now = datetime.datetime.now().strftime('%Y%m%d%s')
        name = kwargs['name'] if kwargs.get('name') else 'dummy_{}'.format(now)
        budget = budget if budget else make_budget(
            name='test_budget2',
            budget_frequency=Budget.MONTHLY,
            amount=200.00,
            color_display='#FF5722'
        )

        return {
            'name': name,
            'budget': budget
        }

    return _make_transaction_category
