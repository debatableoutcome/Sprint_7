import allure

from helpers.utils import get_json_or_text
from helpers.couriers import login_courier
from helpers.orders import create_order, accept_order, get_order_by_track
from helpers.data import VALID_ORDER_NO_COLOR, MSG


@allure.feature('Orders')
@allure.story('Accept order')
class TestAcceptOrder:

    @allure.title('Успешный запрос возвращает ok true')
    def test_accept_order_success_returns_ok(self, created_courier, cleanup_order):
        create_resp = create_order(VALID_ORDER_NO_COLOR)
        assert create_resp.status_code == 201

        track = create_resp.json().get('track')
        assert track is not None
        cleanup_order.append(track)

        order_resp = get_order_by_track(track)
        assert order_resp.status_code == 200
        order_id = order_resp.json()['order']['id']

        courier_login = login_courier(created_courier['login'], created_courier['password'])
        assert courier_login.status_code == 200
        courier_id = courier_login.json().get('id')
        assert courier_id is not None

        response = accept_order(order_id=order_id, courier_id=courier_id)
        body = get_json_or_text(response)

        assert response.status_code == 200
        assert body == {'ok': True}

    @allure.title('Если не передать id курьера, запрос вернёт ошибку')
    def test_accept_order_without_courier_id_returns_error(self):
        response = accept_order(order_id=1, courier_id='')
        body = get_json_or_text(response)

        assert response.status_code == 400
        assert body.get('message') == MSG['ORDER_ACCEPT_NO_DATA']

    @allure.title('Если передать неверный id курьера, запрос вернёт ошибку')
    def test_accept_order_with_wrong_courier_id_returns_error(self):
        response = accept_order(order_id=1, courier_id=999999999)
        body = get_json_or_text(response)

        assert response.status_code == 404
        assert body.get('message') == MSG['ORDER_ACCEPT_COURIER_NOT_FOUND']

    @allure.title('Если передать неверный id заказа, запрос вернёт ошибку')
    def test_accept_order_with_wrong_order_id_returns_error(self):
        response = accept_order(order_id=999999999, courier_id=123456)
        body = get_json_or_text(response)

        assert response.status_code == 404
        assert body.get('message') == MSG['ORDER_ACCEPT_COURIER_NOT_FOUND']
