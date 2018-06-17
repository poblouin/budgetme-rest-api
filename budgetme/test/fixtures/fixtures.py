import pytest
from rest_framework.test import APIClient

from budgetme.apps.core.models import User


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
