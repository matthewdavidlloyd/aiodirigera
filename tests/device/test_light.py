import uuid

from pytest_httpserver import HTTPServer

from aiodirigera.device.light import Light
from aiodirigera.hub import Hub

from tests.fixture import IKEA_LIGHT_DIMMABLE


async def test_update_state(httpserver: HTTPServer):
    hub = Hub(httpserver.host, "some-madeup-token", scheme="http", port=httpserver.port)
    id = str(uuid.uuid4()) 
    device = Light(hub, id)

    httpserver.expect_request(
        f"/v1/devices/{id}",
        method="GET"
    ).respond_with_json(
        IKEA_LIGHT_DIMMABLE
    )

    await device.update_state()

    httpserver.check()
    assert device.is_on is True
    assert device.brightness == 50


async def test_turn_on(httpserver: HTTPServer):
    hub = Hub(httpserver.host, "some-madeup-token", scheme="http", port=httpserver.port)
    id = str(uuid.uuid4()) 
    device = Light(hub, id)

    httpserver.expect_request(
        f"/v1/devices/{id}",
        method="PATCH",
        json=[{"attributes": {"isOn": True}}]
    ).respond_with_data(status=202)

    await device.turn_on()

    httpserver.check()


async def test_turn_off(httpserver: HTTPServer):
    hub = Hub(httpserver.host, "some-madeup-token", scheme="http", port=httpserver.port)
    id = str(uuid.uuid4()) 
    device = Light(hub, id)

    httpserver.expect_request(
        f"/v1/devices/{id}",
        method="PATCH",
        json=[{"attributes": {"isOn": False}}]
    ).respond_with_data(status=202)

    await device.turn_off()

    httpserver.check()


async def test_set_brightness(httpserver: HTTPServer):
    hub = Hub(httpserver.host, "some-madeup-token", scheme="http", port=httpserver.port)
    id = str(uuid.uuid4()) 
    device = Light(hub, id)

    brightness = 69

    httpserver.expect_request(
        f"/v1/devices/{id}",
        method="PATCH",
        json=[{"attributes": {"lightLevel": brightness}}]
    ).respond_with_data(status=202)

    await device.set_brightness(brightness)

    httpserver.check()
    