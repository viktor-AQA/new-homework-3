import pytest
import requests
from faker import Faker
from utils.helpers import AUTH_HEADERS, AUTH_DATA, API_HEADERS
from src.models.api_config import api_config


@pytest.fixture(scope="session")
def auth_session():
    session = requests.Session()
    response = session.post(f"{api_config.BASE_URL}/api/v1/login/access-token", data=AUTH_DATA, headers=AUTH_HEADERS)
    assert response.status_code == 200, f"Auth failed: {response.status_code}, {response.text}"

    token = response.json().get("access_token")
    assert token, "No access_token found"

    session.headers.update(API_HEADERS)
    session.headers.update({"Authorization": f"Bearer {token}"})

    return session

fake = Faker()

@pytest.fixture()
def item_data():
    return {
        "title": fake.word().capitalize(),
        "description": fake.sentence(nb_words=10)
    }

@pytest.fixture
def item_id(auth_session, item_data):
    response = auth_session.post(f"{api_config.BASE_URL}/api/v1/items/", json=item_data)
    assert response.status_code in (200, 201), f"Item creation failed: {response.text}"

    item_id = response.json().get("id")
    assert item_id, "Item ID not found in response"

    yield item_id

    auth_session.delete(f"{api_config.BASE_URL}/api/v1/items/{item_id}")

@pytest.fixture()
def upd_item_data():
    return {
        "title": fake.word().capitalize(),
        "description": fake.sentence(nb_words=10)
    }
