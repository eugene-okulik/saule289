import requests
import allure

from test_api_saule.endpoints.base import Base


class PatchRequest(Base):

    @allure.step('Change part of object')
    def change_part_of_object(self, object_id, payload, headers=None):
        headers = headers or self.headers
        self.response = requests.patch(
            f"{self.url}/{object_id}",
            json=payload,
            headers=headers
        )
        self.json = self.response.json()
        return self.response
