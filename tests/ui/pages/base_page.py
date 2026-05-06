from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def find_elements(self, how, what, timeout=4):
        try:
            elements = WebDriverWait(self.browser, timeout, 1, [TimeoutException]). \
                until(expected_conditions.presence_of_all_elements_located((how, what)))
        except TimeoutException:
            return False

        return elements

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False

        return True

    def open(self):
        self.browser.get(self.url)
