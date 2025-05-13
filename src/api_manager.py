from src.models.api_config import api_config


class ItemApiClient:
    def __init__(self, auth_session):
        self.auth_session = auth_session
        self.base_url = api_config

    def create_item(self, item_data):
        """Отправляет запрос на создание item."""
        response = self.auth_session.post(f"{self.base_url}/api/v1/items/", json=item_data)
        # Базовая проверка, что запрос успешен и мы можем парсить JSON
        if response.status_code not in (200, 201):
            response.raise_for_status() # Выбросит HTTPError для плохих статусов
        return response.json()

    def get_items(self):
        """Отправляет запрос на получение списка items."""
        response = self.auth_session.get(f"{self.base_url}/api/v1/items/")
        if response.status_code != 200:
            response.raise_for_status()
        return response.json()

    def update_item(self, item_id, upd_item_data):
        """Отправляет запрос на обновление item."""
        response = self.auth_session.put(f"{self.base_url}/api/v1/items/{item_id}", json=upd_item_data)
        if response.status_code != 200:
            response.raise_for_status()
        return response.json()

    def delete_item(self, item_id):
        """Отправляет запрос на удаление item."""
        response = self.auth_session.delete(f"{self.base_url}/api/v1/items/{item_id}")
        if response.status_code != 200: # В REST API для DELETE часто возвращают 204 No Content или 200 OK
            response.raise_for_status()
        # Для DELETE часто нечего возвращать из тела, либо можно вернуть статус-код или сам response
        return response # или response.status_code
