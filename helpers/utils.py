import time


def unique_suffix():
    return str(int(time.time()))[-4:]

def with_unique_login(data):
    payload = data.copy()
    payload['login'] = f"{data['login']}_{unique_suffix()}"
    return payload

