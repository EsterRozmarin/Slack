from slack.connections import build_connection_list
from config import SLACK_BOT_TOKEN

if __name__ == "__main__":
    data = build_connection_list(SLACK_BOT_TOKEN)
    print(data)
