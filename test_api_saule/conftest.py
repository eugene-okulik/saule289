import pytest

from test_api_saule.endpoints.delete_request import DeleteRequest
from test_api_saule.endpoints.patch_request import PatchRequest
from test_api_saule.endpoints.post_request import PostRequest
from test_api_saule.endpoints.get_requests import GetRequest
from test_api_saule.endpoints.put_request import PutRequest


@pytest.fixture()
def create_object():
    return PostRequest()


@pytest.fixture()
def delete_object():
    return DeleteRequest()


@pytest.fixture()
def get_object():
    return GetRequest()


@pytest.fixture()
def change_object():
    return PutRequest()


@pytest.fixture()
def change_part_object():
    return PatchRequest()


@pytest.fixture()
def object_id(create_object, delete_object):
    payload = {
        "name": "Temp",
        "data": {"color": "black", "size": "small"}
    }

    response = create_object.create_new_object(payload)
    object_id = response.json()["id"]

    yield object_id

    delete_object.delete_object_by_id(object_id)
