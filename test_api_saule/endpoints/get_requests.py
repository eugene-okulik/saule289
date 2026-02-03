import requests
import allure


from test_api_saule.endpoints.base import Base


class GetRequest(Base):
    object_id = None
    @allure.step('Get all objects')
    def get_all_objects(self):
        self.response = requests.get(self.url)
        return self.response


    @allure.step('Get object by id')
    def get_object_by_id(self, object_id):
        self.response = requests.get(f"{self.url}/{object_id}")
        try:
            self.json = self.response.json()
        except ValueError:  # если ответ не JSON (например 404)
            self.json = None
        return self.response
