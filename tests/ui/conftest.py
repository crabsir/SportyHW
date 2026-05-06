import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def base_url_ui(base_url, request):
    return f"{base_url}/?user-id={request.config.getoption('user_id')}"

@pytest.fixture(scope="function")
def browser():
    print("\nStarting Chrome browser for testing..")
    browser = webdriver.Chrome()

    yield browser

    print("\nQuiting browser..")
    browser.quit()
