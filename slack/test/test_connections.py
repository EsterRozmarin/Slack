import pytest
from unittest.mock import patch, Mock
from src.slack.connections import build_connection_list

@patch("src.slack.connections.SlackClient")
def test_build_connection_list(mock_client_class):
    mock_client = Mock()
    mock_client.get.side_effect = [
        {"members": [{"id": "U123", "name": "test_user"}]},
        {"channels": [{"id": "C123", "name": "general"}]}
    ]
    mock_client_class.return_value = mock_client
    data = build_connection_list("fake-token")
    assert "users" in data
    assert "channels" in data
    assert data["users"][0]["name"] == "test_user"
    assert data["channels"][0]["name"] == "general"
