import pytest
from .model.balance_request import BalanceRequest
from .model.matches_request import MatchesRequest
from .model.place_bet_request import PlaceBetRequest
from .model.reset_balance_request import ResetBalanceRequest


@pytest.mark.api
class TestPlaceBet:
    """
    This test covers the place bet API functionality.
    It was prioritized because of it being the core of the tested feature.
    It resets the user balance as part of its data setup,
    while also pulling any upcoming match and the balance value for later bet placement and assertions.
    """
    def test_place_bet(self, client, base_url):
        reset_balance_request = ResetBalanceRequest(client, base_url)
        reset_balance_request.reset_balance()

        matches_request = MatchesRequest(client, base_url)
        balance_request = BalanceRequest(client, base_url)

        request = PlaceBetRequest(client, base_url)
        request.should_be_able_to_place_bet(matches_request.get_any_upcoming_match(), balance_request.get_balance())
