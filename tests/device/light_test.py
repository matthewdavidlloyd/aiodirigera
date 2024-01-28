import pytest
from pytest_httpserver import HTTPServer

from aiodirigera.hub import Hub

from tests.fixture import IKEA_LIGHT_DIMMABLE


async def test_update_state(httpserver: HTTPServer):
    id = IKEA_LIGHT_DIMMABLE["id"]

    hub = Hub(
        httpserver.host,
        "some-madeup-token",
        scheme="http",
        port=httpserver.port
    )

    httpserver.expect_request(
        f"/v1/devices/{id}",
        method="GET"
    ).respond_with_json(
        IKEA_LIGHT_DIMMABLE
    )

    device = await hub.get_device(id)

    httpserver.check()
    assert device.name == "Sitting Room light"
    assert device.manufacturer == "IKEA of Sweden"
    assert device.model == "TRADFRIbulbE27WWclear250lm"
    assert device.serial_number == "943469FFFE71ADD9"
    assert device.firmware_version == "1.1.006"
    assert device.is_on is True
    assert device.brightness == 50

    httpserver.expect_request(
        f"/v1/devices/{id}",
        method="GET"
    ).respond_with_json(
        IKEA_LIGHT_DIMMABLE
    )

    await device.update_state()

    httpserver.check()
    assert device.name == "Sitting Room light"
    assert device.manufacturer == "IKEA of Sweden"
    assert device.model == "TRADFRIbulbE27WWclear250lm"
    assert device.serial_number == "943469FFFE71ADD9"
    assert device.firmware_version == "1.1.006"
    assert device.is_on is True
    assert device.brightness == 50


async def test_turn_on(httpserver: HTTPServer):
    id = IKEA_LIGHT_DIMMABLE["id"]

    hub = Hub(
        httpserver.host,
        "some-madeup-token",
        scheme="http",
        port=httpserver.port
    )

    httpserver.expect_request(
        f"/v1/devices/{id}",
        method="GET"
    ).respond_with_json(
        IKEA_LIGHT_DIMMABLE
    )

    device = await hub.get_device(id)

    httpserver.expect_request(
        f"/v1/devices/{id}",
        method="PATCH",
        json=[{"attributes": {"isOn": True}}]
    ).respond_with_data(status=202)

    await device.turn_on()

    httpserver.check()


async def test_turn_off(httpserver: HTTPServer):
    id = IKEA_LIGHT_DIMMABLE["id"]

    hub = Hub(
        httpserver.host,
        "some-madeup-token",
        scheme="http",
        port=httpserver.port
    )

    httpserver.expect_request(
        f"/v1/devices/{id}",
        method="GET"
    ).respond_with_json(
        IKEA_LIGHT_DIMMABLE
    )

    device = await hub.get_device(id)

    httpserver.expect_request(
        f"/v1/devices/{id}",
        method="PATCH",
        json=[{"attributes": {"isOn": False}}]
    ).respond_with_data(status=202)

    await device.turn_off()

    httpserver.check()


async def test_set_brightness(httpserver: HTTPServer):
    id = IKEA_LIGHT_DIMMABLE["id"]

    hub = Hub(
        httpserver.host,
        "some-madeup-token",
        scheme="http",
        port=httpserver.port
    )

    httpserver.expect_request(
        f"/v1/devices/{id}",
        method="GET"
    ).respond_with_json(
        IKEA_LIGHT_DIMMABLE
    )

    device = await hub.get_device(id)

    brightness = 69

    httpserver.expect_request(
        f"/v1/devices/{id}",
        method="PATCH",
        json=[{"attributes": {"lightLevel": brightness}}]
    ).respond_with_data(status=202)

    await device.set_brightness(brightness)

    httpserver.check()


async def test_set_brightness_fails_if_brightness_less_than_1(httpserver: HTTPServer):
    id = IKEA_LIGHT_DIMMABLE["id"]

    hub = Hub(
        httpserver.host,
        "some-madeup-token",
        scheme="http",
        port=httpserver.port
    )

    httpserver.expect_request(
        f"/v1/devices/{id}",
        method="GET"
    ).respond_with_json(
        IKEA_LIGHT_DIMMABLE
    )

    device = await hub.get_device(id)

    brightness = 0

    with pytest.raises(ValueError):
        await device.set_brightness(brightness)


async def test_set_brightness_fails_if_brightness_more_than_100(httpserver: HTTPServer):
    id = IKEA_LIGHT_DIMMABLE["id"]

    hub = Hub(
        httpserver.host,
        "some-madeup-token",
        scheme="http",
        port=httpserver.port
    )

    httpserver.expect_request(
        f"/v1/devices/{id}",
        method="GET"
    ).respond_with_json(
        IKEA_LIGHT_DIMMABLE
    )

    device = await hub.get_device(id)

    brightness = 101

    with pytest.raises(ValueError):
        await device.set_brightness(brightness)
