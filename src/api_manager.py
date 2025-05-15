from src.models.api_config import api_config


class ItemApiClient:
    def __init__(self, auth_session):
        self.auth_session = auth_session
        self.base_url = api_config.BASE_URL

    def create_item(self, item_data):
        response = self.auth_session.post(f"{api_config.BASE_URL}/api/v1/items/", json=item_data)
        if response.status_code not in (200, 201):
            response.raise_for_status() # Выбросит HTTPError для плохих статусов
        return response.json()

    def get_items(self):
        response = self.auth_session.get(f"{api_config.BASE_URL}/api/v1/items/")
        if response.status_code != 200:
            response.raise_for_status()
        return response.json()

    def update_item(self, item_id, upd_item_data):
        response = self.auth_session.put(f"{api_config.BASE_URL}/api/v1/items/{item_id}", json=upd_item_data)
        if response.status_code != 200:
            response.raise_for_status()
        return response.json()

    def delete_item(self, item_id):
        response = self.auth_session.delete(f"{api_config.BASE_URL}/api/v1/items/{item_id}")
        if response.status_code != 200:
            response.raise_for_status()
        return response
