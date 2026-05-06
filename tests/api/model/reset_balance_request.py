from .base_request import BaseRequest


class ResetBalanceRequest(BaseRequest):
    def reset_balance(self):
        self.url = f"{self.url}/api/reset-balance"

        response = self.send()
        assert response.status_code == 200, f"Response was not 200: {response.status_code}"
