import allure

from helpers.orders import create_order, cancel_order, get_order_by_track
from helpers.test_data import VALID_ORDER_NO_COLOR


@allure.feature('Orders')
@allure.story('Get order by track')
class TestGetOrderByTrack:

    @allure.title('Успешный запрос возвращает объект с заказом')
    def test_get_order_by_track_success_returns_order(self):
        track = None

        try:
            create_resp = create_order(VALID_ORDER_NO_COLOR)
            assert create_resp.status_code == 201

            track = create_resp.json().get('track')
            assert track is not None

            response = get_order_by_track(track)

            assert response.status_code == 200

            body = response.json()
            assert 'order' in body

        finally:
            if track:
                cancel_order(track)

    @allure.title('Запрос без номера заказа возвращает ошибку')
    def test_get_order_by_track_without_number_returns_error(self):
        response = get_order_by_track('')

        assert response.status_code == 400

    @allure.title('Запрос с несуществующим заказом возвращает ошибку')
    def test_get_order_by_track_nonexistent_returns_error(self):
        response = get_order_by_track(999999999)

        assert response.status_code == 404
