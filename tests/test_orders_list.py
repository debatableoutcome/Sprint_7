import allure

from helpers.orders import get_orders_list
from helpers.utils import get_json_or_text
from helpers.data import MSG


@allure.feature('Orders')
@allure.story('Get orders list')
class TestOrdersList:

    @allure.title('Без courierId возвращается список заказов')
    def test_get_orders_list_without_courier_id_returns_orders(self):
        response = get_orders_list()
        body = get_json_or_text(response)

        assert response.status_code == 200
        assert 'orders' in body
        assert isinstance(body['orders'], list)

    @allure.title('С несуществующим courierId возвращается ошибка')
    def test_get_orders_list_with_invalid_courier_id_returns_error(self):
        courier_id = 999999999

        response = get_orders_list(params={'courierId': courier_id})
        body = get_json_or_text(response)

        assert response.status_code == 404

        message = body.get('message')
        assert MSG['ORDERS_LIST_COURIER_NOT_FOUND_START'] in message
        assert str(courier_id) in message
        assert MSG['ORDERS_LIST_COURIER_NOT_FOUND_END'] in message
