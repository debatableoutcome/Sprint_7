import pytest
import allure

from helpers.orders import create_order
from helpers.utils import get_json_or_text
from helpers.data import (
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
    def test_create_order_returns_track(self, order_data, cleanup_order):
        response = create_order(order_data)
        body = get_json_or_text(response)

        assert response.status_code == 201
        assert isinstance(body, dict)

        track = body.get('track')
        assert track is not None
        assert isinstance(track, int)

        cleanup_order.append(track)
