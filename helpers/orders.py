import requests

from helpers.urls import BASE_URL


def create_order(payload):
    return requests.post(f'{BASE_URL}/api/v1/orders', json=payload)

def cancel_order(track):
    return requests.put(f'{BASE_URL}/api/v1/orders/cancel', json={'track': track})

def get_orders_list(params=None):
    return requests.get(f'{BASE_URL}/api/v1/orders', params=params)