import time
import pytest
import allure

from helpers.couriers import login_courier
from helpers.test_data import INVALID_LOGIN_NO_LOGIN, INVALID_LOGIN_NO_PASSWORD


@allure.feature('Courier')
@allure.story('Login courier')
class TestCourierLogin:

    def test_login_success_returns_id(self, created_courier):
        response = login_courier(
            created_courier['login'],
            created_courier['password'],
        )

        assert response.status_code == 200
        assert 'id' in response.json()


    @allure.title('Авторизация без обязательных полей возвращает ошибку')
    @pytest.mark.parametrize(
        'login_data',
        [
            INVALID_LOGIN_NO_LOGIN,
            INVALID_LOGIN_NO_PASSWORD,
        ]
    )
    def test_login_lacks_required_data_returns_error(self, login_data):
        response = login_courier(
            login_data.get('login'),
            login_data.get('password'),
        )

        body = response.json()
        assert response.status_code == 400
        assert body.get('message') == 'Недостаточно данных для входа'

    @allure.title('Авторизация под незарегистрированным курьером возвращает ошибку')
    def test_login_non_existent_courier_returns_error(self):
        timestamp = str(int(time.time()))

        login = timestamp
        password = timestamp

        response = login_courier(login, password)

        body = response.json()
        assert response.status_code == 404
        assert body.get('message') == 'Учетная запись не найдена'


    @allure.title('Система вернёт ошибку, если неправильно указать логин или пароль')
    @pytest.mark.parametrize('wrong_field', ['login', 'password'])
    def test_login_with_wrong_credentials_returns_error(self, created_courier, wrong_field):
        login = created_courier['login']
        password = created_courier['password']

        if wrong_field == 'login':
            login = f'{login}1'
        if wrong_field == 'password':
            password = f'{password}1'

        response = login_courier(login, password)

        body = response.json()
        assert response.status_code == 404
        assert body.get('message') == 'Учетная запись не найдена'


        