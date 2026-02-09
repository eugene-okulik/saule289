import requests
import allure

from test_api_saule.endpoints.base import Base


class PostRequest(Base):
    object_id = None

    @allure.step('Create new object')
    def create_new_object(self, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(
            self.url,
            json=payload,
            headers=headers
        )
        self.json = self.response.json()
        self.object_id = self.json['id']
        return self.response
