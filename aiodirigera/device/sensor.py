from typing import Optional

from aiodirigera.device import DeviceState, DeviceAPI


class EnvironmentSensorState(DeviceState):
    temperature: Optional[int] = None
    humidity: Optional[int] = None


class EnvironmentSensor(EnvironmentSensorState):
    _delegate: DeviceAPI
    
    def __init__(self, delegate: DeviceAPI):
        self._delegate = delegate

    async def update_state(self) -> None:
        device_status = await self._delegate.get_status()

        self.name = device_status.attributes.customName
        self.manufacturer = device_status.attributes.manufacturer
        self.model = device_status.attributes.model
        self.serial_number = device_status.attributes.serialNumber
        self.firmware_version = device_status.attributes.firmwareVersion
        self.temperature = device_status.attributes.currentTemperature
        self.humidity = device_status.attributes.currentRH
