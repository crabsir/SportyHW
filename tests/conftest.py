import pytest


def pytest_addoption(parser):
    parser.addoption("--user_id",
        action="store",
        default="userId",
        help="Specify user ID to use in testing"
    )

def pytest_configure(config):
    config.addinivalue_line("markers", "api: this is an API test.")
    config.addinivalue_line("markers", "ui: this is a UI test.")

@pytest.fixture(scope="session")
def base_url():
    return "https://qae-assignment-tau.vercel.app"
