from typing import Optional

from aiodirigera.device import OnOffDeviceState, OnOffDeviceAPI


class LightState(OnOffDeviceState):
    brightness: Optional[int] = None


class LightAPI(OnOffDeviceAPI):
    async def set_brightness(self, brightness: int) -> None:
        if brightness < 1 or brightness > 100:
            raise ValueError("Brightness must be in range [1, 100]")
        
        await self.update_status(
            [{"attributes": {"lightLevel": brightness}}]
        )


class Light(LightState):
    _delegate: LightAPI

    def __init__(self, delegate: LightAPI):
        self._delegate = delegate

    async def update_state(self) -> None:
        device_status = await self._delegate.get_status()

        self.name = device_status.attributes.customName
        self.manufacturer = device_status.attributes.manufacturer
        self.model = device_status.attributes.model
        self.serial_number = device_status.attributes.serialNumber
        self.firmware_version = device_status.attributes.firmwareVersion
        self.is_on = device_status.attributes.isOn
        self.brightness = device_status.attributes.lightLevel

    async def turn_on(self) -> None:
        await self._delegate.turn_on()

    async def turn_off(self) -> None:
        await self._delegate.turn_off()

    async def set_brightness(self, brightness: int) -> None:
        await self._delegate.set_brightness(brightness)

