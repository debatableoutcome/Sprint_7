import requests

from helpers.urls import BASE_URL


def create_order(payload):
    return requests.post(f'{BASE_URL}/api/v1/orders', json=payload)

def cancel_order(track):
    return requests.put(f'{BASE_URL}/api/v1/orders/cancel', json={'track': track})

def accept_order(order_id, courier_id=None):
    params = {}
    if courier_id is not None and courier_id != '':
        params['courierId'] = courier_id

    return requests.put(
        f'{BASE_URL}/api/v1/orders/accept/{order_id}',
        params=params
    )


def get_order_by_track(track):
    return requests.get(
        f'{BASE_URL}/api/v1/orders/track',
        params={'t': track}
    )

def get_orders_list(params=None):
    return requests.get(f'{BASE_URL}/api/v1/orders', params=params)