import allure

from helpers.orders import get_orders_list


@allure.feature('Orders')
@allure.story('Get orders list')
class TestOrdersList:

    @allure.title('В ответе возвращается список заказов')
    def test_get_orders_list_returns_orders(self):
        response = get_orders_list()

        assert response.status_code == 200

        body = response.json()
        assert 'orders' in body
        assert type(body['orders']) is list

