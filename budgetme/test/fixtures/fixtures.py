import datetime

import pytest
from rest_framework.test import APIClient

from budgetme.apps.core.models import User
from budgetme.apps.types.models import Budget


@pytest.mark.django_db
@pytest.fixture
def access_token(db, django_db_setup):
    users = User.objects.all()
    assert users is not None and len(users) > 0
    user = users[0]

    client = APIClient()
    response = client.post('/api/v1/token', {'email': user.email, 'password': 'test1234'}, format='json')
    assert response is not None
    assert response.status_code == 200
    assert response.data.get('access') is not None

    return response.data['access']


@pytest.fixture
def authed_client(access_token):
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION='Token ' + access_token)
    return client


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

        budget_data = {
            'name': name,
            'budget_frequency': budget_frequency,
            'amount': amount,
            'start_date': start_date,
            'end_date': end_date,
            'color_display': color_display
        }

        return budget_data

    return _format_budget_data
