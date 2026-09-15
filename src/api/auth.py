from datetime import datetime, timedelta
import requests

class OAuthTokenManager:
    def __init__(self, accounts_url, client_id, client_secret, refresh_token, timeout=60):
        self.accounts_url, self.client_id = accounts_url, client_id
        self.client_secret, self.refresh_token = client_secret, refresh_token
        self.timeout, self.access_token, self.expires_at = timeout, None, None

    def refresh(self):
        r = requests.post(self.accounts_url, data={
            "refresh_token": self.refresh_token, "client_id": self.client_id,
            "client_secret": self.client_secret, "grant_type": "refresh_token"
        }, timeout=self.timeout)
        r.raise_for_status()
        data = r.json()
        self.access_token = data["access_token"]
        self.expires_at = datetime.now() + timedelta(seconds=max(int(data.get("expires_in",3600))-120,1))
        return self.access_token

    def authorization_header(self):
        if self.access_token is None or self.expires_at is None or datetime.now() >= self.expires_at:
            self.refresh()
        return {"Authorization": f"Zoho-oauthtoken {self.access_token}"}
