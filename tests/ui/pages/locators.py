from selenium.webdriver.common.by import By


class BettingPageLocators:
    BETTING_PAGE_TITLE = (By.CSS_SELECTOR, "#header-title")
    MATCH_BADGE = (By.CSS_SELECTOR, ".badge")
    MATCH_CARD = (By.CSS_SELECTOR, ".matchCard")
    MATCH_SECTION = (By.CSS_SELECTOR, "#match-section")
