import requests
import pytest
import allure


BASE_URL = "http://objapi.course.qa-practice.com/object"

@allure.feature('Create objects')
@allure.story('Create parametrized objects')
@allure.title('Создание нескольких объектов с помощью параметрайз')
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
    with allure.step('Отправка запрос на создание объекта'):
        response = requests.post(BASE_URL, json=body)
    with allure.step('Проверка кода ответа'):
        assert response.status_code == 200

    response_data = response.json()

    with allure.step('Проверка на соответствие body ответа'):
        assert response_data["name"] == name
        assert response_data["data"]["color"] == color
        assert response_data["data"]["size"] == size

    with allure.step('Удаление объекта по id'):
        requests.delete(f"{BASE_URL}/{response_data['id']}")


@allure.feature('Create objects')
@allure.story('Create an object')
@allure.title('Создание одного объекта')
def test_create_one_object(name='Uni', color='black', size='very large'):
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

@allure.feature('Get objects')
@allure.story('Get object by id')
@allure.title('Запрос объяекта по id')
@pytest.mark.critical()
def test_get_object_by_id(create_object):
    response = requests.get(f'{BASE_URL}/{create_object}')

    assert response.status_code == 200, f'Expected 200, got {response.status_code}'
    assert 'id' in response.json(), 'Response does not contain id'
    assert response.json()['name'] == 'Building', 'Name is incorrect'
    assert response.json()['data']['color'] == 'white', 'Color is incorrect'
    assert response.json()['data']['size'] == 'small', 'Size is incorrect'


@allure.feature('Get objects')
@allure.story('Get all objects')
@allure.title('Запрос всех объектов')
@pytest.mark.critical()
def test_get_all_objects(create_object):
    response = requests.get(f'{BASE_URL}/{create_object}')

    assert response.status_code == 200, f'Expected 200, got {response.status_code}'
    assert 'id' in response.json(), 'Response does not contain id'
    assert response.json()['name'] == 'Building', 'Name is incorrect'
    assert response.json()['data']['color'] == 'white', 'Color is incorrect'
    assert response.json()['data']['size'] == 'small', 'Size is incorrect'


@allure.feature('Change of objects')
@allure.story('Put object')
@allure.title('Измнение объекта')
@pytest.mark.critical()
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

@allure.feature('Change of objects')
@allure.story('Patch object')
@allure.title('Изменение части объекта')
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

@allure.feature('Get objects')
@allure.story('Delete object by id')
@allure.title('Удаление объекта')
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
