import requests
import allure
from test_api_saule.endpoints.base import Base


class PutRequest(Base):

    @allure.step("Change object by id")
    def change_object(self, object_id, payload, headers=None):
        headers = headers or self.headers

        self.response = requests.put(
            f"{self.url}/{object_id}",
            json=payload,
            headers=headers
        )
        self.json = self.response.json()
        return self.response
