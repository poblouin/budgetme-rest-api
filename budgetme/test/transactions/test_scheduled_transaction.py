SCHEDULED_TRANSACTION_BASE_URL = '/api/v1/scheduled-transaction'


def test_create_transaction(authed_client, make_scheduled_transaction):
    budget = {
        "pk": 16,
        "name": "test-budget1",
        "amount": "100.00",
        "budget_frequency": "Weekly",
        "start_date": None,
        "end_date": None,
        "color_display": None,
    }
    scheduled_transaction_data = make_scheduled_transaction(budget=budget)

    response = authed_client.post(SCHEDULED_TRANSACTION_BASE_URL, scheduled_transaction_data, format='json')
    assert response is not None and response.status_code == 201
