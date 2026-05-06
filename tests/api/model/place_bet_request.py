from .base_request import BaseRequest


class PlaceBetRequest(BaseRequest):
    def should_be_able_to_place_bet(self, match, old_balance):
        self.url = f"{self.url}/api/place-bet"

        self.data = {
            "matchId": match["id"],
            "selection": "HOME",
            "stake": 10,
            "additionalProp1": {}
        }

        response = self.send()
        assert response.status_code == 200, f"Response was not 200: {response.status_code}"

        response_data = response.json()
        assert response_data["message"] == "Bet placed successfully", f"Unexpected message: {response_data['message']}"
        assert response_data["matchId"] == self.data["matchId"], f"Unexpected matchId: {response_data['matchId']}"
        assert response_data["selection"] == self.data["selection"], f"Unexpected selection: {response_data['selection']}"
        assert response_data["stake"] == self.data["stake"], f"Unexpected stake: {response_data['stake']}"
        assert response_data["odds"] == match["odds"]["home"], f"Unexpected odds: {response_data['odds']}"
        assert response_data["payout"] == match["odds"]["home"] * self.data["stake"], f"Unexpected payout: {response_data['payout']}"
        assert response_data["balance"] == old_balance - self.data["stake"], f"Unexpected balance: {response_data['balance']}"
        assert response_data["currency"] == "EUR", f"Unexpected currency: {response_data['currency']}"
