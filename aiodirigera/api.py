import logging
from typing import Any, Dict, List

from aiohttp import ClientSession

from aiodirigera.api_model import HubStatus, DeviceStatus

_LOGGER = logging.getLogger(__name__)

class API:
    _http_base_url: str
    _token: str

    def __init__(self, host: str, token: str, scheme: str = "https", port: int = 8443, version: str = "v1") -> None:
        self._http_base_url = f"{scheme}://{host}:{port}/{version}"
        self._token = token

    async def _get(self, url: str) -> Any:
        _LOGGER.info("Making GET request to %s", url)
        client_session = ClientSession()
        try:
            async with client_session.get(url, headers=self._headers(), ssl=False, timeout=30) as res:
                res.raise_for_status()
                return await res.json()
        finally:
            await client_session.close()

    async def _patch(self, url: str, json: Dict) -> None:
        client_session = ClientSession()
        try:
            async with client_session.patch(url, json=json, headers=self._headers(), ssl=False, timeout=30) as res:
                res.raise_for_status()
        finally:
            await client_session.close()

    def _headers(self) -> Dict[str, Any]:
        return {"Authorization": f"Bearer {self._token}"}


class HubAPI(API):
    async def get_hub_status(self) -> HubStatus:
        url = f"{self._http_base_url}/hub/status"
        raw = await self._get(url)
        return HubStatus(**raw)

    async def get_devices(self) -> List[DeviceStatus]:
        url = f"{self._http_base_url}/devices"
        raw = await self._get(url)
        return [DeviceStatus(**x) for x in raw]
