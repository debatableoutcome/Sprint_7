import allure

from helpers.couriers import login_courier, delete_courier
from helpers.utils import get_json_or_text
from helpers.data import MSG


@allure.feature('Courier')
@allure.story('Delete courier')
class TestDeleteCourier:

    @allure.title('Курьера можно удалить, успешный ответ возвращает ok true')
    def test_delete_courier_success_returns_ok(self, created_courier):
        login_response = login_courier(
            created_courier['login'],
            created_courier['password']
        )
        courier_id = login_response.json().get('id')

        response = delete_courier(courier_id)
        body = get_json_or_text(response)

        assert response.status_code == 200
        assert body == {'ok': True}

    @allure.title('Запрос на удаление без id возвращает ошибку')
    def test_delete_courier_without_id_returns_error(self):
        response = delete_courier('')
        body = get_json_or_text(response)
        
        assert response.status_code in [404, 400]
        assert body.get('message') == MSG['NOT_FOUND']

    @allure.title('Запрос на удаление с несуществующим id возвращает ошибку')
    def test_delete_courier_with_nonexistent_id_returns_error(self):
        response = delete_courier(999999999)
        body = get_json_or_text(response)
   
        assert response.status_code in [404, 400]
        assert body.get('message') == MSG['COURIER_DELETE_NOT_FOUND']
