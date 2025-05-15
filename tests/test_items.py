from src.api_manager import ItemApiClient
from src.api_scenarios import ItemScenarios


class TestItems:

    def test_create_item(self, item_data, auth_session):
        api_client = ItemApiClient(auth_session)
        scenarios = ItemScenarios(api_client)
        scenarios.create_item_and_immediately_delete(item_data)

    def test_get_items(self, auth_session):
        api_client = ItemApiClient(auth_session)
        scenarios = ItemScenarios(api_client)
        scenarios.get_and_verify_items_exist()

    def test_put_items(self, upd_item_data, auth_session, item_id):
        api_client = ItemApiClient(auth_session)
        scenarios = ItemScenarios(api_client)
        scenarios.update_item_and_verify_changes(item_id, upd_item_data)

    def test_delete_items(self, auth_session, item_id):
        api_client = ItemApiClient(auth_session)
        scenarios = ItemScenarios(api_client)
        scenarios.delete_existing_item_and_verify(item_id)
