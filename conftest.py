import random
import pytest
import allure

from faker import Faker
from reqs.requests_user import RequestsUser
from reqs.requests_order import RequestsOrder


@pytest.fixture
def create_user_payload():
    @allure.step('Конструируем запрос пользователя')
    def _create_user_payload(name=None, email=None, password=None):
        faker = Faker()
        payload = {}
        if name == 'rand':
            payload['name'] = faker.name()
        elif name is not None:
            payload['name'] = name
        if password == 'rand':
            payload['password'] = faker.pyint()
        elif password is not None:
            payload['password'] = password
        if email == 'rand':
            payload['email'] = faker.email()
        elif email is not None:
            payload['email'] = email
        return payload

    return _create_user_payload


@pytest.fixture
@allure.step('Конструируем запрос для отправки заказа')
def create_order_payload():
    ingredients_list = RequestsOrder().get_ingredients_list()
    ids = [element['_id'] for element in ingredients_list['text']['data']]
    ids_for_payload = random.sample(ids, 3)
    payload = {"ingredients": ids_for_payload}
    return payload


@pytest.fixture(scope='function')
def make_user():
    user = {}

    def _make_user(data):
        nonlocal user
        user_requests = RequestsUser()
        user = user_requests.post_create_user(data=data)
        return user

    yield _make_user
    RequestsUser().delete_user(token=user['text']['accessToken'])


@pytest.fixture(scope='function')
def del_user():
    user = {}
    yield user
    RequestsUser().delete_user(token=user['token'])
