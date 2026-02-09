import requests


def create_object():
    body = {
        "name": "Building",
        "data": {
            "color": "white",
            "size": "small"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'http://objapi.course.qa-practice.com/object',
        json=body,
        headers=headers
    )
    assert response.status_code == 200, f'Expected 200, got {response.status_code}'
    assert 'id' in response.json(), 'Response does not contain id'
    assert response.json()['name'] == 'Building', 'Name is incorrect'
    assert response.json()['data']['color'] == 'white', 'Color is incorrect'
    assert response.json()['data']['size'] == 'small', 'Size is incorrect'

    print(f"Object created successfully with id: {response.json()['id']}")
    return response.json()['id']


def get_object_by_id(object_id):
    response = requests.get(f'http://objapi.course.qa-practice.com/object/{object_id}')
    return response


def clear(object_id):
    requests.delete(f'http://objapi.course.qa-practice.com/object/{object_id}')


def put_an_object():
    object_id = create_object()
    body = {
        "name": "Building",
        "data": {
            "color": "red",
            "size": "small"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(
        f'http://objapi.course.qa-practice.com/object/{object_id}',
        json=body,
        headers=headers
    )
    response_data = response.json()
    assert response_data['data']['color'] == 'red', f'Expected color: red, got {response_data["data"]["color"]}'
    assert response_data['data']['size'] == 'small', f'Expected size: small, got {response_data["data"]["size"]}'
    clear(object_id)


def patch_an_object():
    object_id = create_object()
    body = {
        "data": {
            "size": "large"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        f'http://objapi.course.qa-practice.com/object/{object_id}',
        json=body,
        headers=headers
    )
    response_data = response.json()
    assert response_data['data']['size'] == 'large', f'Expected size: large, got {response_data["data"]["size"]}'
    print(response)
    clear(object_id)


def delete_an_object():
    object_id = create_object()
    response = requests.delete(f'http://objapi.course.qa-practice.com/object/{object_id}')
    assert response.status_code == 200, f'Expected 200, got {response.status_code}'
    get_response = get_object_by_id(object_id)
    assert get_response.status_code == 404, f'Expected 404 after deletion, got {get_response.status_code}'
    print(f"Object {object_id} deleted successfully")


create_object()
put_an_object()
patch_an_object()
delete_an_object()
