from locust import task, HttpUser


class GetObject(HttpUser):
    object_id = None

    def on_start(self):
        response = self.client.post(
            '/object',
            json={
                "name": "Building",
                "data": {
                    "color": "red",
                    "size": "small"
                }
            }
        )
        self.object_id = response.json()['id']

    @task(3)
    def get_all_objects(self):
        self.client.get('/object')

    @task(3)
    def get_one_object(self):
        if self.object_id:
            self.client.get(f'/object/{self.object_id}')

    @task(3)
    def update_object(self):
        if self.object_id:
            self.client.put(
                f'/object/{self.object_id}',
                json={
                    "name": "Building Updated",
                    "data": {
                        "color": "blue",
                        "size": "large"
                    }
                }
            )
