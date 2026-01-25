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


MSG = {
    'COURIER_CREATE_NO_DATA': 'Недостаточно данных для создания учетной записи',
    'COURIER_DUPLICATE_LOGIN': 'Этот логин уже используется. Попробуйте другой.',

    'COURIER_DELETE_NO_ID': 'Недостаточно данных для удаления курьера',
    'COURIER_DELETE_NOT_FOUND': 'Курьера с таким id нет.',
    'NOT_FOUND': 'Not Found.',
    

    'LOGIN_NO_DATA': 'Недостаточно данных для входа',
    'LOGIN_NOT_FOUND': 'Учетная запись не найдена',

    'ORDER_ACCEPT_NO_DATA': 'Недостаточно данных для поиска',
    'ORDER_ACCEPT_NOT_FOUND': 'Заказа с таким id не существует',
    'ORDER_ACCEPT_COURIER_NOT_FOUND': 'Курьера с таким id не существует',
    'ORDER_ALREADY_IN_WORK': 'Этот заказ уже в работе',

    'ORDER_TRACK_NO_DATA': 'Недостаточно данных для поиска',
    'ORDER_TRACK_NOT_FOUND': 'Заказ не найден',
    'ORDERS_LIST_COURIER_NOT_FOUND_START': 'Курьер с идентификатором',
    'ORDERS_LIST_COURIER_NOT_FOUND_END': 'не найден',
}






