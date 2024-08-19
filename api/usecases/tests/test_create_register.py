import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIRequestFactory
from api.models import Register
from api.usecases.create_register import CreateRegisterUseCase

@pytest.mark.django_db
class TestCreateRegisterUseCase:

    @pytest.fixture
    def user(self):
        return User.objects.create_user(username='testuser', password='12345')

    @pytest.fixture
    def request_factory(self):
        return APIRequestFactory()

    @pytest.fixture
    def use_case(self):
        return CreateRegisterUseCase()

    def test_create_register_success(self, user, request_factory, use_case):
        data = {
            'user_id': user.id,
            'amount': 500
        }
        request = request_factory.post('/api/register/', data, format='json')
        response = use_case.execute(request)

        assert response is not None
        assert response['user_id'] == user.id
        assert response['amount'] == 500

    def test_create_register_invalid_data(self, request_factory, use_case):
        data = {
            'user_id': None,
            'amount': 500
        }
        request = request_factory.post('/api/register/', data, format='json')
        response = use_case.execute(request)

        assert response is None