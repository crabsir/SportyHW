from .base_page import BasePage
from .locators import BettingPageLocators


class BettingPage(BasePage):
    def should_be_betting_page(self):
        self.should_be_betting_page_loaded()
        self.should_be_betting_page_title()

    def should_be_betting_page_loaded(self):
        assert self.is_element_present(*BettingPageLocators.MATCH_SECTION)

    def should_be_betting_page_title(self):
        title = self.find_elements(*BettingPageLocators.BETTING_PAGE_TITLE)
        assert title, "Betting page title not present"
        assert title[0].text == "Sports Betting QA", f"Betting page title is incorrect, found: {title[0].text}"

    def should_be_upcoming_matches_only(self):
        matches = self.find_elements(*BettingPageLocators.MATCH_BADGE)
        for match in matches:
            assert match.text == "UPCOMING", f"Page contains non upcoming matches, found: {match.text}"
