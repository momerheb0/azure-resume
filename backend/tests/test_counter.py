import pytest
from unittest.mock import patch, MagicMock
import azure.functions as func
from api import function_app
import json

@pytest.fixture
def req():
    # Create a mock HTTP request object
    return func.HttpRequest(
        method="GET",
        url="/api/GetResumeCounter",
        body=None,
        headers={}
    )

# Mock the CosmosClient to avoid the real connection being attempted
@patch('api.function_app.CosmosClient')
def test_http_trigger_should_return_known_value(mock_cosmos_client, req):
    # Mock the Cosmos DB container behavior
    mock_container = MagicMock()
    mock_item = {"id": "1", "count": 2}
    mock_container.read_item.return_value = mock_item

    # Mock the client and container
    mock_database = MagicMock()
    mock_database.get_container_client.return_value = mock_container
    mock_cosmos_client.from_connection_string.return_value = MagicMock(get_database_client=lambda db_name: mock_database)
    
    # Call the function
    response = function_app.get_resume_counter(req)
    
    # Parse the JSON response body
    response_json = json.loads(response.get_body().decode('utf-8'))

    # Verify the count was incremented
    assert response.status_code == 200
    assert response_json["count"] == 3  # Count should be incremented by 1
