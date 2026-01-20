import pytest

from helpers.couriers import create_courier, login_courier, delete_courier
from helpers.test_data import VALID_COURIER
from helpers.utils import with_unique_login


@pytest.fixture
def courier_payload():
    return with_unique_login(VALID_COURIER)


@pytest.fixture
def created_courier(courier_payload):
    create_courier(courier_payload)
    yield courier_payload

    login_response = login_courier(courier_payload['login'], courier_payload['password'])
    if login_response.status_code == 200:
        courier_id = login_response.json().get('id')
        if courier_id:
            delete_courier(courier_id)


@pytest.fixture
def cleanup_courier(courier_payload):
    yield courier_payload

    login_response = login_courier(courier_payload['login'], courier_payload['password'])
    if login_response.status_code == 200:
        courier_id = login_response.json().get('id')
        if courier_id:
            delete_courier(courier_id)
