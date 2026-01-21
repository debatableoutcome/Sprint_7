import pytest
import allure

from helpers.orders import create_order, cancel_order
from helpers.test_data import (
    VALID_ORDER_BLACK,
    VALID_ORDER_GREY,
    VALID_ORDER_BOTH_COLORS,
    VALID_ORDER_NO_COLOR,
)


@allure.feature('Orders')
@allure.story('Create order')
class TestCreateOrder:

    @allure.title('При создании заказа можно указать цвет или не указывать его')
    @pytest.mark.parametrize(
        'order_data',
        [
            VALID_ORDER_BLACK,
            VALID_ORDER_GREY,
            VALID_ORDER_BOTH_COLORS,
            VALID_ORDER_NO_COLOR,
        ]
    )
    def test_create_order_returns_track(self, order_data):
        track = None

        try:
            response = create_order(order_data)
            body = response.json()
            track = body['track']

            assert response.status_code == 201
            assert 'track' in body

        finally:
            if track:
                cancel_order(track)
