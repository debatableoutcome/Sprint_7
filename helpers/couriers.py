import requests
from helpers.urls import BASE_URL


def create_courier(payload):
    return requests.post(
        f'{BASE_URL}/api/v1/courier',
        data=payload
    )


def login_courier(login, password):
    return requests.post(
        f'{BASE_URL}/api/v1/courier/login',
        data={
            'login': login,
            'password': password,
        }
    )


def delete_courier(courier_id):
    return requests.delete(
        f'{BASE_URL}/api/v1/courier/{courier_id}'
    )
