import pytest
import allure
from reqs.requests_user import RequestsUser
from faker import Faker


@allure.feature('Проверки обновления данных пользователя')
class TestUpdateUser:

    @pytest.mark.parametrize('key_to_be_changed',
                             {'email',
                              'password',
                              'name'}
                             )
    @allure.title('Проверка изменений данных пользователя с авторизацией')
    def test_authorized(self, create_user_payload, make_user, key_to_be_changed):
        faker = Faker()
        payload = create_user_payload(email='rand', password='0987', name='rand')
        user = make_user(data=payload)

        payload[key_to_be_changed] = faker.name()
        updated_user = RequestsUser().patch_user(data=payload, token=user['text']['accessToken'])
        assert (payload['name'] == updated_user['text']['user']['name'] and
                payload['email'].lower() == updated_user['text']['user']['email'])

    @pytest.mark.parametrize('key_to_be_changed',
                             ['email',
                              'password',
                              'name']
                             )
    @allure.title('Проверка изменений данных пользователя без авторизации')
    def test_not_authorized(self, create_user_payload, make_user, key_to_be_changed):
        faker = Faker()
        payload = create_user_payload(email='rand', password='0987', name='rand')
        user = make_user(data=payload)
        payload[key_to_be_changed] = faker.pyint()
        patched_user = RequestsUser().patch_user(data=payload, token=user['text']['accessToken'])
        updated_user = RequestsUser().get_user_data(token=user['text']['accessToken'])
        assert (patched_user['text']['user']['name'] == updated_user['text']['user']['name'] and
                patched_user['text']['user']['email'] == updated_user['text']['user']['email'])

    @pytest.mark.parametrize('key_to_be_changed',
                             ['email',
                              'password',
                              'name']
                             )
    @allure.title('Проверка изменений данных пользователя с невалидным токеном')
    def test_incorrect_token(self, create_user_payload, make_user, key_to_be_changed):
        faker = Faker()
        payload = create_user_payload(email='rand', password='0987', name='rand')
        user = make_user(data=payload)
        new_payload = payload
        new_payload[key_to_be_changed] = faker.pyint()
        token = user['text']['accessToken'] + str(faker.pyint())
        resp = RequestsUser().patch_user(data=new_payload, token=token)
        updated_user = RequestsUser().get_user_data(token=user['text']['accessToken'])
        assert (resp['status_code'] == 403 and updated_user['text']['user']['name'] == user['text']['user']['name']
                and updated_user['text']['user']['email'] == user['text']['user']['email'])
