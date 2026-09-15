import requests

class SurveyApiClient:
    def __init__(self, base_url, token_manager, timeout=60):
        self.base_url, self.token_manager, self.timeout = base_url.rstrip("/"), token_manager, timeout

    def get(self, path, params=None):
        url = f"{self.base_url}/{path.lstrip('/')}"
        r = requests.get(url, headers=self.token_manager.authorization_header(), params=params, timeout=self.timeout)
        if r.status_code == 401:
            self.token_manager.refresh()
            r = requests.get(url, headers=self.token_manager.authorization_header(), params=params, timeout=self.timeout)
        r.raise_for_status()
        return r.json()
