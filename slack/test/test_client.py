import pytest
from unittest.mock import patch, Mock
from slack.client import SlackClient

def test_slack_client_get_success():
    with patch("slack.client.requests.get") as mock_get:
        mock_response = Mock()
        mock_response.json.return_value = {"ok": True, "members": []}
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response
        client = SlackClient(token="fake-token")
        result = client.get("users.list")
        assert result == {"ok": True, "members": []}
        mock_get.assert_called_once_with(
            f"{client.base_url}/users.list",
            headers=client.headers,
            params=None
        )

def test_slack_client_get_http_error():
    with patch("slack.client.requests.get") as mock_get:
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = Exception("HTTP Error")
        mock_get.return_value = mock_response
        client = SlackClient(token="fake-token")
        with pytest.raises(Exception) as e:
            client.get("users.list")
        assert str(e.value) == "HTTP Error"
