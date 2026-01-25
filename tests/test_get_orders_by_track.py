import allure

from helpers.orders import create_order, get_order_by_track
from helpers.utils import get_json_or_text
from helpers.data import VALID_ORDER_NO_COLOR, MSG


@allure.feature('Orders')
@allure.story('Get order by track')
class TestGetOrderByTrack:

    @allure.title('Можно получить заказ по треку')
    def test_get_order_by_track_success(self, cleanup_order):
        create_resp = create_order(VALID_ORDER_NO_COLOR)
        track = create_resp.json()['track']
        cleanup_order.append(track)

        response = get_order_by_track(track)
        body = get_json_or_text(response)

        assert response.status_code == 200
        assert 'order' in body

    @allure.title('Запрос без трека возвращает ошибку')
    def test_get_order_without_track_returns_error(self):
        response = get_order_by_track('')
        body = get_json_or_text(response)

        assert response.status_code == 400
        assert body.get('message') == MSG['ORDER_ACCEPT_NO_DATA']

    @allure.title('Запрос с несуществующим треком возвращает ошибку')
    def test_get_order_with_wrong_track_returns_error(self):
        response = get_order_by_track(999999999)
        body = get_json_or_text(response)

        assert response.status_code == 404
        assert body.get('message') == MSG['ORDER_TRACK_NOT_FOUND']
