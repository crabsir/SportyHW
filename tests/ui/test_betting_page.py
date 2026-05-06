import pytest
from .pages.betting_page import BettingPage


@pytest.mark.ui
class TestBettingPage:
    """
    This test covers the event list on the betting page.
    It was chosen for automation since it is the start off point for the bet placement user journey.
    It also regulates the events and odds available for the user to place bets on.
    """
    def test_match_list_contains_upcoming_only(self, browser, base_url_ui):
        betting_page = BettingPage(browser, base_url_ui)
        betting_page.open()
        betting_page.should_be_betting_page()
        betting_page.should_be_upcoming_matches_only()
