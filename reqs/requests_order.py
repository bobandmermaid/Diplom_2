import allure
from data import Constants
from reqs.requests_base import RequestsBase


class RequestsOrder(RequestsBase):

    @allure.step('Создание заказа')
    def post_create_order(self, token, data):
        url = Constants.ORDER_URL
        return self.post_request_with_token(url, data=data, token=token)

    @allure.step('Создание заказа без токена')
    def post_create_order_without_token(self, data):
        url = Constants.ORDER_URL
        return self.post_request(url, data=data)

    @allure.step('Получение списка ингредиентов')
    def get_ingredients_list(self):
        url = Constants.INGREDIENTS_URL
        return self.get_request(url)

    @allure.step('Получение заказа пользователя')
    def get_user_orders(self, token):
        url = Constants.ORDER_URL
        return self.get_request_with_token(url, token=token)
