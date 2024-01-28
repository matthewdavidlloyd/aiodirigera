import uuid

from pytest_httpserver import HTTPServer

from aiodirigera.device import Light, EnvironmentSensor
from aiodirigera.hub import Hub

from tests.fixture import (
    HUB_STATUS,
    IKEA_LIGHT_DIMMABLE,
    THIRD_PARTY_SENSOR_ENVIRONMENT
)


async def test_get_status(httpserver: HTTPServer):
    hub = Hub(
        httpserver.host,
        "some-madeup-token",
        scheme="http",
        port=httpserver.port
    )

    httpserver.expect_request(
        "/v1/hub/status",
        method="GET"
    ).respond_with_json(
        HUB_STATUS
    )

    hub_status = await hub.get_status()

    httpserver.check()
    assert hub_status.id == "cb524caf-fed3-4adc-b887-1429d27f6ebf_1"
    assert hub_status.attributes.customName == "Home"
    assert hub_status.attributes.model == "DIRIGERA Hub for smart products"
    assert hub_status.attributes.manufacturer == "IKEA of Sweden"
    assert hub_status.attributes.firmwareVersion == "2.453.3"
    assert hub_status.attributes.serialNumber == "cb524caf-fed3-4adc-b887-1429d27f6ebf"  ## noqa


async def test_get_devices(httpserver: HTTPServer):
    hub = Hub(
        httpserver.host,
        "some-madeup-token",
        scheme="http",
        port=httpserver.port
    )

    httpserver.expect_request(
        "/v1/devices",
        method="GET"
    ).respond_with_json([
        IKEA_LIGHT_DIMMABLE,
        THIRD_PARTY_SENSOR_ENVIRONMENT
    ])

    devices = await hub.get_devices()
    assert type(devices[0]) is Light
    assert type(devices[1]) is EnvironmentSensor


async def test_get_device(httpserver: HTTPServer):
    hub = Hub(
        httpserver.host,
        "some-madeup-token",
        scheme="http",
        port=httpserver.port
    )
    id = str(uuid.uuid4())

    httpserver.expect_request(
        f"/v1/devices/{id}",
        method="GET"
    ).respond_with_json(
        IKEA_LIGHT_DIMMABLE
    )

    light = await hub.get_device(id)

    httpserver.check()
    assert type(light) is Light
