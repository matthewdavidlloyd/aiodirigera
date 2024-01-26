import uuid

from pytest_httpserver import HTTPServer

from aiodirigera.device.sensor import EnvironmentSensor
from aiodirigera.hub import Hub

from tests.fixture import THIRD_PARTY_SENSOR_ENVIRONMENT


async def test_update_state(httpserver: HTTPServer):
    hub = Hub(httpserver.host, "some-madeup-token", scheme="http", port=httpserver.port)
    id = str(uuid.uuid4()) 
    device = EnvironmentSensor(hub, id)

    httpserver.expect_request(
        f"/v1/devices/{id}",
        method="GET"
    ).respond_with_json(
        THIRD_PARTY_SENSOR_ENVIRONMENT
    )

    await device.update_state()

    httpserver.check()
    assert device.name == "Bedroom Air Sensor"
    assert device.manufacturer == ""
    assert device.model == "lumi.weather"
    assert device.serial_number == "00158D000AD5E783"
    assert device.firmware_version == ""
    assert device.temperature == 18.15
    assert device.humidity == 69
