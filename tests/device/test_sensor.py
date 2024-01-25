import uuid

from pytest_httpserver import HTTPServer

from aiodirigera.device import DeviceAPI
from aiodirigera.device.sensor import EnvironmentSensor

from tests.fixture import THIRD_PARTY_SENSOR_ENVIRONMENT


async def test_update_state(httpserver: HTTPServer):
    id = str(uuid.uuid4()) 
    api = DeviceAPI(httpserver.host, "some-madeup-token", id, scheme="http", port=httpserver.port)
    device = EnvironmentSensor(api)

    httpserver.expect_request(
        f"/v1/devices/{id}",
        method="GET"
    ).respond_with_json(
        THIRD_PARTY_SENSOR_ENVIRONMENT
    )

    await device.update_state()

    httpserver.check()
    assert device.temperature == 18.15
    assert device.humidity == 69
