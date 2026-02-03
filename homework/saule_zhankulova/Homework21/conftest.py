import pytest
import requests

BASE_URL = "http://objapi.course.qa-practice.com/object"


@pytest.fixture(scope='session', autouse=True)
def before_and_after_all_tests():
    print('\nStart testing')
    yield
    print('\nTesting completed')


@pytest.fixture(autouse=True)
def before_and_after_one_test():
    print('\nbefore test')
    yield
    print('\nafter test')


@pytest.fixture()
def create_object():
    body = {
        "name": "Building",
        "data": {
            "color": "white",
            "size": "small"
        }
    }
    response = requests.post(BASE_URL, json=body)
    object_id = response.json()['id']

    yield object_id

    requests.delete(f"{BASE_URL}/{object_id}")