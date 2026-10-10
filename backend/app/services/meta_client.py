import os
from typing import Any

import httpx

from app.config import settings


class MetaPageClient:
    def __init__(self):
        self.base_url = settings.meta_api_base_url
        self.page_id = settings.meta_page_id
        self.access_token = settings.meta_page_access_token

    def publish_post(self, message: str, link: str | None = None) -> dict[str, Any]:
        if not self.page_id or not self.access_token:
            return {
                "status": "not_configured",
                "message": "Meta Page ID and Page Access Token are not configured yet.",
                "payload": {"message": message, "link": link},
            }

        payload = {
            "message": message,
            "access_token": self.access_token,
        }
        if link:
            payload["link"] = link

        url = f"{self.base_url}/{self.page_id}/feed"
        response = httpx.post(url, data=payload, timeout=30.0)
        response.raise_for_status()
        return response.json()
