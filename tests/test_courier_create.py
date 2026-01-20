import allure

from helpers.couriers import create_courier
from helpers.test_data import INVALID_COURIER_NO_LOGIN, INVALID_COURIER_NO_PASSWORD


@allure.feature('Courier')
@allure.story('Create courier')
class TestCreateCourier:

    @allure.title('Курьера можно создать')
    def test_create_courier_success(self, created_courier):
        response = create_courier(created_courier)
        assert response.status_code == 201
        assert response.json() == {'ok': True}

    @allure.title('Нельзя создать двух одинаковых курьеров')
    def test_create_duplicate_courier_returns_error(self, cleanup_courier):
        first_response = create_courier(cleanup_courier)
        second_response = create_courier(cleanup_courier)

        assert first_response.status_code == 201
        assert first_response.json() == {'ok': True}

        assert second_response.status_code == 409
        assert 'message' in second_response.json()

    @allure.title('Нельзя создать курьера без логина')
    def test_create_courier_without_login_returns_error(self):
        response = create_courier(INVALID_COURIER_NO_LOGIN.copy())
        assert response.status_code == 400
        assert 'message' in response.json()

    @allure.title('Нельзя создать курьера без пароля')
    def test_create_courier_without_password_returns_error(self):
        response = create_courier(INVALID_COURIER_NO_PASSWORD.copy())
        assert response.status_code == 400
        assert 'message' in response.json()
