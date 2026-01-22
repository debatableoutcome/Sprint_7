import allure

from helpers.couriers import create_courier
from helpers.utils import get_json_or_text
from helpers.data import (
    INVALID_COURIER_NO_LOGIN,
    INVALID_COURIER_NO_PASSWORD,
    MSG,
)


@allure.feature('Courier')
@allure.story('Create courier')
class TestCreateCourier:

    @allure.title('Курьера можно создать')
    def test_create_courier_success(self, cleanup_courier):
        response = create_courier(cleanup_courier)
        body = get_json_or_text(response)

        assert response.status_code == 201
        assert body == {'ok': True}

    @allure.title('Нельзя создать двух курьеров с одинаковым логином')
    def test_create_duplicate_courier_returns_error(self, cleanup_courier):
        create_courier(cleanup_courier)
        response = create_courier(cleanup_courier)
        body = get_json_or_text(response)

        assert response.status_code == 409
        assert body.get('message') == MSG['COURIER_DUPLICATE_LOGIN']

    @allure.title('Создание курьера без логина возвращает ошибку')
    def test_create_courier_without_login_returns_error(self):
        response = create_courier(INVALID_COURIER_NO_LOGIN)
        body = get_json_or_text(response)

        assert response.status_code == 400
        assert body.get('message') == MSG['COURIER_CREATE_NO_DATA']

    @allure.title('Создание курьера без пароля возвращает ошибку')
    def test_create_courier_without_password_returns_error(self):
        response = create_courier(INVALID_COURIER_NO_PASSWORD)
        body = get_json_or_text(response)

        assert response.status_code == 400
        assert body.get('message') == MSG['COURIER_CREATE_NO_DATA']
