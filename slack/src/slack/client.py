import requests
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(os.path.dirname(__file__)), '..', '.env'))

class SlackClient:
    def __init__(self, token: str):
        self.base_url = os.getenv("BASE_URL")
        self.headers = {
            "Authorization": f"Bearer {token}"
        }

    def get(self, endpoint, params=None):
        r = requests.get(
            f"{self.base_url}/{endpoint}",
            headers=self.headers,
            params=params,
            timeout=10
        )
        r.raise_for_status()
        return r.json()
