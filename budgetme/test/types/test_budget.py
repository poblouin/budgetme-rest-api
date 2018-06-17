import datetime

import pytest

from budgetme.apps.types.models import Budget

BUDGET_BASE_URL = '/api/v1/budget'


def test_create_budget(authed_client):
    now = datetime.datetime.now().strftime('%Y%m%d')
    budget_data = {
        'name': 'dummy_budget_{}'.format(now),
        'budget_frequency': Budget.WEEKLY,
        'amount': 10.00,
        'start_date': '2018-06-01',
        'end_date': '2018-06-30',
        'color_display': '#00BCD4'
    }

    response = authed_client.post(BUDGET_BASE_URL, budget_data, format='json')
    assert response is not None and response.status_code == 201


def test_get_budget(authed_client):
    response = authed_client.get(BUDGET_BASE_URL + '/16')
    assert response is not None and response.status_code == 200

    budget = response.data
    assert budget is not None and budget.get('name') is not None
    assert budget.get('name') == 'test_budget1'


def test_put_budget_name(authed_client):
    now = datetime.datetime.now().strftime('%Y%m%d')
    budget_data = {
        'name': 'test_budget_{}'.format(now),
        'budget_frequency': Budget.MONTHLY,
        'amount': 200.00,
        'start_date': '2018-06-01',
        'end_date': '2018-06-30',
        'color_display': '#FF5722'
    }

    response = authed_client.put(BUDGET_BASE_URL + '/17', budget_data, format='json')
    assert response is not None and response.status_code == 200


@pytest.mark.xfail(reason='Budget name is not unique')
def test_create_budget_not_unique(authed_client):
    budget_data = {
        'name': 'test_budget1',
        'budget_frequency': Budget.WEEKLY,
        'amount': 10.00
    }

    response = authed_client.post(BUDGET_BASE_URL, budget_data, format='json')
    assert response is not None and response.status_code == 201


@pytest.mark.xfail(reason='Budget dates are invalid')
def test_create_budget_invalid_dates(authed_client):
    budget_data = {
        'name': 'test_budget1',
        'budget_frequency': Budget.WEEKLY,
        'amount': 10.00,
        'start_date': '2018-06-30',
        'end_date': '2018-06-01',
    }

    response = authed_client.post(BUDGET_BASE_URL, budget_data, format='json')
    assert response is not None and response.status_code == 201
