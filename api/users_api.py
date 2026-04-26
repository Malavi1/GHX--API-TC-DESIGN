from config.config import BASE_URL
from utils.api_client import APIClient

# This class contains all API methods (get, post, put, delete)

class UsersAPI:
    def __init__(self, api_context):
        self.client = APIClient(api_context)

    def get_users(self):
        return self.client.get(f"{BASE_URL}/users")

    def get_user_by_id(self, user_id):
        return self.client.get(f"{BASE_URL}/users/{user_id}")

    def create_user(self, payload):
        return self.client.post(f"{BASE_URL}/users", payload)

    def update_user(self, user_id, payload):
        return self.client.put(f"{BASE_URL}/users/{user_id}", payload)

    def delete_user(self, user_id):
        return self.client.delete(f"{BASE_URL}/users/{user_id}")