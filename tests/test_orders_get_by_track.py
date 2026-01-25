import allure

from helpers.orders import create_order, get_order_by_track
from helpers.data import VALID_ORDER_NO_COLOR, MSG
from helpers.utils import get_json_or_text


@allure.feature('Orders')
@allure.story('Get order by track')
class TestGetOrderByTrack:

    @allure.title('Успешный запрос возвращает объект с заказом')
    def test_get_order_by_track_success_returns_order(self, cleanup_order):
        create_resp = create_order(VALID_ORDER_NO_COLOR)
        assert create_resp.status_code == 201

        track = create_resp.json().get('track')
        assert track is not None

        cleanup_order.append(track)

        response = get_order_by_track(track)
        body = get_json_or_text(response)

        assert response.status_code == 200
        assert 'order' in body

    @allure.title('Запрос без номера заказа возвращает ошибку')
    def test_get_order_by_track_without_number_returns_error(self):
        response = get_order_by_track('')
        body = get_json_or_text(response)

        assert response.status_code == 400
        assert body.get('message') == MSG['ORDER_TRACK_NO_DATA']

    @allure.title('Запрос с несуществующим заказом возвращает ошибку')
    def test_get_order_by_track_nonexistent_returns_error(self):
        response = get_order_by_track(999999999)
        body = get_json_or_text(response)

        assert response.status_code == 404
        assert body.get('message') == MSG['ORDER_TRACK_NOT_FOUND']
