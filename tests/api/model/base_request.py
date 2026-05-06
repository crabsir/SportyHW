from pprint import pprint
from requests.exceptions import RequestException


class BaseRequest:
    def __init__(self, client, url, method="POST", data=None, timeout=10):
        self.client = client
        self.url = url
        self.method = method
        self.data = {} if data is None else data
        self.timeout = timeout

    def send(self):
        try:
            print(f"\nSending {self.method} request to {self.url}")
            if self.data != {}:
                print("\nRequest payload:")
                pprint(self.data)
            response = self.client.request(self.method, self.url, json=self.data, timeout=self.timeout)
            response.raise_for_status()
        except RequestException as e:
            print(f"Request exception occurred: {e}")
            return False

        print("\nResponse payload:")
        pprint(response.json())
        return response
