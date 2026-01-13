from .client import SlackClient

def build_connection_list(token: str):
    client = SlackClient(token)
    users = client.get("users.list").get("members", [])
    channels = client.get(
        "conversations.list",
        params={"types": "public_channel,private_channel"}
    ).get("channels", [])
    return {
        "users": users,
        "channels": channels
    }
