TRANSACTION_BASE_URL = '/api/v1/transaction'


def test_create_transaction(authed_client, make_transaction):
    budget = {
        "pk": 16,
        "name": "test_budget1",
        "amount": "100.00",
        "budget_frequency": "Weekly",
        "start_date": None,
        "end_date": None,
        "color_display": None,
    }
    transaction_data = make_transaction(budget=budget)

    response = authed_client.post(TRANSACTION_BASE_URL, transaction_data, format='json')
    assert response is not None and response.status_code == 201


def test_get_single_transaction(authed_client):
    response = authed_client.get(TRANSACTION_BASE_URL + '/23')
    assert response is not None and response.status_code == 200

    transaction = response.data
    assert transaction is not None and transaction.get('description') is not None
    assert transaction.get('description') == 'test'


def test_get_all_transaction_for_user(authed_client):
    response = authed_client.get(TRANSACTION_BASE_URL)
    assert response is not None and response.status_code == 200

    transactions = response.data.get('results')
    assert len(transactions) == 4
    total = sum(float(list(transaction.items())[1][1]) for transaction in transactions)
    assert total == 300


def test_get_all_transaction_for_budget(authed_client):
    response = authed_client.get(TRANSACTION_BASE_URL + '?budget_name=test_budget1')
    assert response is not None and response.status_code == 200

    transactions = response.data.get('results')
    assert len(transactions) == 2
    total = sum(float(list(transaction.items())[1][1]) for transaction in transactions)
    assert total == 100
