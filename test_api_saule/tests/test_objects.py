new_object = {
    "name": "University",
    "data": {
        "color": "red",
        "size": "large"
    }
}


def test_create_object(create_object, delete_object, object_id):
    create_object.create_new_object(payload=new_object)
    create_object.check_response_name_is_correct(new_object['name'])
    create_object.check_response_data_size_is_correct(new_object['data']['size'])
    create_object.check_response_data_color_is_correct(new_object['data']['color'])
    create_object.check_that_status_is_200()


def test_get_created_object(create_object, delete_object, get_object, object_id):
    get_object.get_object_by_id(object_id)
    get_object.check_that_status_is_200()
    get_object.check_response_name_is_correct("Temp")
    get_object.check_response_data_size_is_correct("small")
    get_object.check_response_data_color_is_correct("black")


def test_change_object(create_object, delete_object, change_object, object_id):
    payload = {
        "name": "Insitute",
        "data": {
            "color": "green",
            "size": "small"
        }
    }

    change_object.change_object(object_id, payload)
    change_object.check_response_data_size_is_correct(payload['data']['size'])
    change_object.check_response_data_color_is_correct(payload['data']['color'])
    change_object.check_response_name_is_correct(payload['name'])
    change_object.check_that_status_is_200()


def test_change_part_of_object(create_object, delete_object, change_part_object, object_id):
    patch_payload = {
        "data": {
            "size": "large"
        }
    }
    change_part_object.change_part_of_object(object_id, payload=patch_payload)
    change_part_object.check_response_data_size_is_correct(patch_payload['data']['size'])
    change_part_object.check_that_status_is_200()


def test_delete_created_object(create_object, delete_object, get_object, object_id):

    delete_object.delete_object_by_id(object_id)
    get_object.get_object_by_id(object_id)
    get_object.check_not_found_object()
