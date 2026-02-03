import requests
import allure


from test_api_saule.endpoints.base import Base


class DeleteRequest(Base):
    object_id = None

    @allure.step('Delete object by  id')
    def delete_object_by_id(self, object_id):
        self.response = requests.delete(f"{self.url}/{object_id}")
        return self.response
