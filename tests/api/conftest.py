import pytest
import requests


@pytest.fixture(scope="session")
def auth_headers(request):
    return {"X-User-Id": request.config.getoption("user_id")}

@pytest.fixture(scope="class")
def client(auth_headers):
    print("\nStarting API client...")
    session = requests.Session()
    session.headers.update(auth_headers)

    yield session

    print("\nStopping API client...")
    session.close()
