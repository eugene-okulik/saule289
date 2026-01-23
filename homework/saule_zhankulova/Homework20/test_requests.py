import requests
import pytest


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


@pytest.mark.parametrize(
    "name,color,size",
    [
        ("House", "white", "small"),
        ("Office", "blue", "medium"),
        ("Mall", "red", "large")
    ]
)
def test_create_object(name, color, size):
    body = {
        "name": name,
        "data": {
            "color": color,
            "size": size
        }
    }

    response = requests.post(BASE_URL, json=body)

    assert response.status_code == 200
    response_data = response.json()

    assert response_data["name"] == name
    assert response_data["data"]["color"] == color
    assert response_data["data"]["size"] == size

    requests.delete(f"{BASE_URL}/{response_data['id']}")


@pytest.mark.critical()
def test_get_object_by_id(create_object):
    response = requests.get(f'{BASE_URL}/{create_object}')

    assert response.status_code == 200, f'Expected 200, got {response.status_code}'
    assert 'id' in response.json(), 'Response does not contain id'
    assert response.json()['name'] == 'Building', 'Name is incorrect'
    assert response.json()['data']['color'] == 'white', 'Color is incorrect'
    assert response.json()['data']['size'] == 'small', 'Size is incorrect'


@pytest.mark.medium()
def test_put_an_object(create_object):
    body = {
        "name": "Building",
        "data": {
            "color": "red",
            "size": "small"
        }
    }
    response = requests.put(
        f'{BASE_URL}/{create_object}',
        json=body
    )
    response_data = response.json()
    assert response_data['data']['color'] == 'red', f'Expected color: red, got {response_data["data"]["color"]}'
    assert response_data['data']['size'] == 'small', f'Expected size: small, got {response_data["data"]["size"]}'


def test_patch_an_object(create_object):
    body = {
        "data": {
            "size": "large"
        }
    }
    response = requests.patch(
        f'{BASE_URL}/{create_object}',
        json=body
    )
    response_data = response.json()
    assert response_data['data']['size'] == 'large', f'Expected size: large, got {response_data["data"]["size"]}'
    print(response)


def test_delete_an_object():
    body = {
        "name": "Temp",
        "data": {
            "color": "black",
            "size": "small"
        }
    }
    create_response = requests.post(BASE_URL, json=body)
    object_id = create_response.json()["id"]

    delete_response = requests.delete(f"{BASE_URL}/{object_id}")
    assert delete_response.status_code == 200

    get_response = requests.get(f"{BASE_URL}/{object_id}")
    assert get_response.status_code == 404
