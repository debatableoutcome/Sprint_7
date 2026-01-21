VALID_COURIER = {
    'login': 'test_courier',
    'password': 'password123',
    'firstName': 'Ivan',
}

INVALID_COURIER_NO_LOGIN = {
    'password': 'password123',
    'firstName': 'Ivan',
}

INVALID_COURIER_NO_PASSWORD = {
    'login': 'test_courier',
    'firstName': 'Ivan',
}

VALID_LOGIN_DATA = {
    'login': 'test_courier',
    'password': 'password123',
}

INVALID_LOGIN_NO_LOGIN = {
    'login': '',
    'password': 'password123',
}

INVALID_LOGIN_NO_PASSWORD = {
    'login': 'test_courier',
    'password': '',
}

VALID_ORDER_BOTH_COLORS = {
    'firstName': 'Василий',
    'lastName': 'Васильев',
    'address': 'Василькова, 14',
    'metroStation': 4,
    'phone': '+79011234567',
    'rentTime': 5,
    'deliveryDate': '2026-01-23T21:00:00.000Z',
    'comment': 'Тестовый заказ',
    'color': ['BLACK', 'GREY']
}


VALID_ORDER_BLACK = {
    'firstName': 'Василий',
    'lastName': 'Васильев',
    'address': 'Василькова, 14',
    'metroStation': 4,
    'phone': '+79011234567',
    'rentTime': 5,
    'deliveryDate': '2026-01-23T21:00:00.000Z',
    'comment': 'Тестовый заказ',
    'color': ['BLACK']
}
VALID_ORDER_GREY = {
    'firstName': 'Василий',
    'lastName': 'Васильев',
    'address': 'Василькова, 14',
    'metroStation': 4,
    'phone': '+79011234567',
    'rentTime': 5,
    'deliveryDate': '2026-01-23T21:00:00.000Z',
    'comment': 'Тестовый заказ',
    'color': ['GREY']
}


VALID_ORDER_NO_COLOR = {
    'firstName': 'Василий',
    'lastName': 'Васильев',
    'address': 'Василькова, 14',
    'metroStation': 4,
    'phone': '+79011234567',
    'rentTime': 5,
    'deliveryDate': '2026-01-23T21:00:00.000Z',
    'comment': '"Тестовый заказ"'
}