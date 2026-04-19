import requests
import logging

class ServiceClient:
    def __init__(self, base_url="https://jsonplaceholder.typicode.com/"):
        self.base_url = base_url
        self.session = requests.Session()


    def _request(self, method, endpoint, **kwargs):
        url = f"{self.base_url.rstrip('/')}/{endpoint.lstrip('/')}"
        try:
            response = self.session.request(method, url, timeout=10, **kwargs)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as err:
            logging.error(f"HTTP error: {err}")
        except requests.exceptions.ConnectionError:
            logging.error("Connection error")
        except requests.exceptions.Timeout:
            logging.error("Timeout error")
        except requests.exceptions.RequestException as e:
            logging.error(f"Unexpected error: {e}")
        return None


    def get_users(self):
        return self._request("GET", f"users")


    def get_posts(self):
        return self._request("GET", f"posts")


    def get_comments(self):
        return self._request("GET", f"comments")


    def close(self):
        self.session.close()


    def __enter__(self):
        return self


    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()