from typing import Dict, Optional

from aiodirigera.api import API
from aiodirigera.api_model import DeviceStatus


class DeviceState:
    name: Optional[str] = None
    manufacturer: Optional[str] = None
    model: Optional[str] = None
    serial_number: Optional[str] = None
    firmware_version: Optional[str] = None


class DeviceAPI(API):
    _id: str

    def __init__(self, host: str, token: str, id: str, scheme: str = "https", port: int = 8443, version: str = "v1") -> None:
        super().__init__(host, token, scheme=scheme, port=port, version=version)
        self._id = id

    async def get_status(self) -> DeviceStatus:
        url = f"{self._http_base_url}/devices/{self._id}"
        raw = await self._get(url)
        return DeviceStatus(**raw)

    async def update_status(self, data: Dict) -> None:
        url = f"{self._http_base_url}/devices/{self._id}"
        await self._patch(url, data)


class OnOffDeviceState(DeviceState):
    is_on: Optional[bool] = None


class OnOffDeviceAPI(DeviceAPI):
    async def turn_on(self) -> None:
        await self.update_status(
            [{"attributes": {"isOn": True}}]
        )

    async def turn_off(self) -> None:
        await self.update_status(
            [{"attributes": {"isOn": False}}]
        )
