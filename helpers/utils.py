import time


def unique_suffix():
    return str(int(time.time()))[-4:]

def with_unique_login(data):
    payload = data.copy()
    payload['login'] = f"{data['login']}_{unique_suffix()}"
    return payload

def get_json_or_text(response):
    try:
        return response.json()
    except ValueError:
        return response.text


