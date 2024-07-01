import allure

from data import Constants
from reqs.requests_base import RequestsBase


class RequestsUser(RequestsBase):
    @allure.step('Создание пользователя')
    def post_create_user(self, data=None):
        url = Constants.REGISTER_URL
        return self.post_request(url=url, data=data)

    @allure.step('Логин пользователя')
    def post_login_user(self, token, data=None):
        url = Constants.USER_LOGIN_URL
        return self.post_request_with_token(url, data=data, token=token)

    @allure.step('Удаление пользователя')
    def delete_user(self, token):
        url = Constants.USER_EDIT_URL
        return self.delete_request(url, token=token)

    @allure.step('Обновление данных пользователя')
    def patch_user(self, data, token):
        url = Constants.USER_EDIT_URL
        return self.patch_request(url, data=data, token=token)

    @allure.step('Получение данных пользователя')
    def get_user_data(self, token):
        url = Constants.USER_EDIT_URL
        return self.get_request_with_token(url, token=token)
