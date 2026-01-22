import time
import allure

from helpers.couriers import login_courier
from helpers.utils import get_json_or_text
from helpers.data import MSG


@allure.feature('Courier')
@allure.story('Login courier')
class TestCourierLogin:

    @allure.title('Курьер может авторизоваться')
    def test_login_success_returns_id(self, created_courier):
        response = login_courier(
            created_courier['login'],
            created_courier['password'],
        )

        assert response.status_code == 200
        assert 'id' in response.json()

    @allure.title('Авторизация без логина возвращает ошибку')
    def test_login_without_login_returns_error(self):
        response = login_courier('', '123')
        body = get_json_or_text(response)

        assert response.status_code == 400
        assert body.get('message') == MSG['LOGIN_NO_DATA']

    @allure.title('Авторизация без пароля возвращает ошибку')
    def test_login_without_password_returns_error(self):
        response = login_courier('login', '')
        body = get_json_or_text(response)

        assert response.status_code == 400
        assert body.get('message') == MSG['LOGIN_NO_DATA']

    @allure.title('Авторизация несуществующего курьера возвращает ошибку')
    def test_login_nonexistent_courier_returns_error(self):
        uniq = str(int(time.time()))
        response = login_courier(uniq, uniq)
        body = get_json_or_text(response)

        assert response.status_code == 404
        assert body.get('message') == MSG['LOGIN_NOT_FOUND']
