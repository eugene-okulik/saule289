import allure

class Base():
    url = "http://objapi.course.qa-practice.com/object"
    response = None
    json = None
    headers = {'Content-type': 'application/json'}

    @allure.step('Check that name is the same as sent')
    def check_response_name_is_correct(self, name):
        assert self.json["name"] == name

    @allure.step('Check that color is the same as sent')
    def check_response_data_color_is_correct(self, color):
        assert self.json["data"]["color"] == color

    @allure.step('Check that size is the same as sent')
    def check_response_data_size_is_correct(self, size):
        assert self.json["data"]["size"] == size

    @allure.step('Check that response is 200')
    def check_that_status_is_200(self):
        assert self.response.status_code == 200

    @allure.step('Check that 404 error received')
    def check_not_found_object(self):
        assert self.response.status_code == 404
