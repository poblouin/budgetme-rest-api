import pytest

TC_BASE_URL = '/api/v1/transaction-category'


def test_create_transaction_category(authed_client, make_transaction_category):
    transaction_category_data = make_transaction_category()

    response = authed_client.post(TC_BASE_URL, transaction_category_data, format='json')
    assert response is not None and response.status_code == 201


def test_get_transaction_category(authed_client):
    response = authed_client.get(TC_BASE_URL + '/12')
    assert response is not None and response.status_code == 200

    transaction_category = response.data
    assert transaction_category is not None and transaction_category.get('name') is not None
    assert transaction_category.get('name') == 'test_tc1'


@pytest.mark.xfail(reason='The Budget does not exist.')
def test_create_transaction_category_invalid_budget(authed_client, make_budget, make_transaction_category):
    budget = make_budget(name='does_not_exist')
    transaction_category_data = make_transaction_category(budget=budget)

    response = authed_client.post(TC_BASE_URL, transaction_category_data, format='json')
    assert response is not None and response.status_code == 201
