import datetime

import pytest

BUDGET_BASE_URL = '/api/v1/budget'


def test_create_budget(authed_client, make_budget):
    budget_data = make_budget(is_dummy=True)

    response = authed_client.post(BUDGET_BASE_URL, budget_data, format='json')
    assert response is not None and response.status_code == 201


def test_get_budget(authed_client):
    response = authed_client.get(BUDGET_BASE_URL + '/16')
    assert response is not None and response.status_code == 200

    budget = response.data
    assert budget is not None and budget.get('name') is not None
    assert budget.get('name') == 'test_budget1'


def test_put_budget_name(authed_client, make_budget):
    now = datetime.datetime.now().strftime('%Y%m%d')
    budget_data = make_budget(name='test_budget_{}'.format(now))

    response = authed_client.put(BUDGET_BASE_URL + '/17', budget_data, format='json')
    assert response is not None and response.status_code == 200


def test_put_budget_dates(authed_client, make_budget):
    budget_data = make_budget(start_date='2020-01-01', end_date='2020-01-31')

    response = authed_client.put(BUDGET_BASE_URL + '/17', budget_data, format='json')
    assert response is not None and response.status_code == 200


@pytest.mark.xfail(reason='Budget name is not unique')
def test_create_budget_not_unique(authed_client, make_budget):
    budget_data = make_budget(name='test_budget1')

    response = authed_client.post(BUDGET_BASE_URL, budget_data, format='json')
    assert response is not None and response.status_code == 201


@pytest.mark.xfail(reason='Budget dates are invalid')
def test_create_budget_invalid_dates(authed_client, make_budget):
    budget_data = make_budget(is_dummy=True, start_date='2018-06-30', end_date='2018-06-01')

    response = authed_client.post(BUDGET_BASE_URL, budget_data, format='json')
    assert response is not None and response.status_code == 201


@pytest.mark.xfail(reason='Budget color already in use')
def test_put_budget_color_not_unique(authed_client, make_budget):
    budget_data = make_budget(color_display='#FF5722')

    response = authed_client.put(BUDGET_BASE_URL + '/16', budget_data, format='json')
    assert response is not None and response.status_code == 200
