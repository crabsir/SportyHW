from datetime import datetime
from .base_request import BaseRequest


class MatchesRequest(BaseRequest):
    def get_any_upcoming_match(self):
        self.url = f"{self.url}/api/matches"
        self.method = 'GET'

        response = self.send()
        assert response.status_code == 200, f"Response was not 200: {response.status_code}"

        try:
            match = [m for m in response.json() if datetime.strptime(m["kickoffDate"], "%Y-%m-%d") > datetime.now()]
            return match[0]
        except IndexError:
            return None
