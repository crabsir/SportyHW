from .base_request import BaseRequest


class BalanceRequest(BaseRequest):
    def get_balance(self):
        self.url = f"{self.url}/api/balance"
        self.method = 'GET'

        response = self.send()
        assert response.status_code == 200, f"Response was not 200: {response.status_code}"

        return response.json()["balance"]
