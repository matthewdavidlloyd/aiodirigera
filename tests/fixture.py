
import json

HUB_STATUS = json.loads(
    """
    {
        "id": "cb524caf-fed3-4adc-b887-1429d27f6ebf_1",
        "relationId": "cb524caf-fed3-4adc-b887-1429d27f6ebf",
        "type": "gateway",
        "deviceType": "gateway",
        "createdAt": "2023-02-10T12:43:53.054Z",
        "isReachable": true,
        "lastSeen": "2024-01-27T18:45:00.285Z",
        "attributes": {
            "customName": "Home",
            "model": "DIRIGERA Hub for smart products",
            "manufacturer": "IKEA of Sweden",
            "firmwareVersion": "2.453.3",
            "hardwareVersion": "P2.5",
            "serialNumber": "cb524caf-fed3-4adc-b887-1429d27f6ebf",
            "identifyStarted": "2023-12-31T03:23:31.000Z",
            "identifyPeriod": 65534,
            "otaStatus": "upToDate",
            "otaState": "readyToCheck",
            "otaProgress": 0,
            "otaPolicy": "autoDownload",
            "otaScheduleStart": "00:00",
            "otaScheduleEnd": "00:00",
            "permittingJoin": false,
            "backendConnected": false,
            "backendConnectionPersistent": false,
            "backendOnboardingComplete": true,
            "backendRegion": "eu-west-1",
            "backendCountryCode": "GB",
            "userConsents": [
                {
                    "name": "analytics",
                    "value": "disabled"
                },
                {
                    "name": "diagnostics",
                    "value": "enabled"
                }
            ],
            "logLevel": 3,
            "coredump": false,
            "timezone": "Europe/London",
            "nextSunSet": null,
            "nextSunRise": null,
            "homestateValue": "home",
            "homestateLastChanged": "2023-11-16T03:23:15Z",
            "countryCode": "XZ",
            "isOn": false
        },
        "capabilities": {
            "canSend": [],
            "canReceive": [
                "customName",
                "permittingJoin",
                "userConsents",
                "logLevel",
                "time",
                "timezone",
                "countryCode",
                "coordinates"
            ]
        },
        "deviceSet": [],
        "remoteLinks": [],
        "apiVersion": "1.3.29"
    }
    """
)

IKEA_LIGHT_DIMMABLE = json.loads(
    """
    {
        "id": "7c3a87ef-d9e4-4997-8d57-ee5d6f903b65_1",
        "type": "light",
        "deviceType": "light",
        "createdAt": "2023-05-31T06:35:14.000Z",
        "isReachable": true,
        "lastSeen": "2024-01-25T16:46:00.000Z",
        "attributes": {
            "customName": "Sitting Room light",
            "model": "TRADFRIbulbE27WWclear250lm",
            "manufacturer": "IKEA of Sweden",
            "firmwareVersion": "1.1.006",
            "hardwareVersion": "1",
            "serialNumber": "943469FFFE71ADD9",
            "productCode": "LED1934G3",
            "isOn": true,
            "startupOnOff": "startOn",
            "lightLevel": 50,
            "identifyStarted": "2000-01-01T00:00:00.000Z",
            "identifyPeriod": 0,
            "permittingJoin": false,
            "otaStatus": "upToDate",
            "otaState": "readyToCheck",
            "otaProgress": 0,
            "otaPolicy": "autoUpdate",
            "otaScheduleStart": "00:00",
            "otaScheduleEnd": "00:00"
        },
        "capabilities": {
            "canSend": [],
            "canReceive": [
                "customName",
                "isOn",
                "lightLevel"
            ]
        },
        "room": {
            "id": "3568dee7-3a10-4de7-864e-a00e391a3344",
            "name": "Sitting Room",
            "color": "ikea_beige_1",
            "icon": "rooms_arm_chair"
        },
        "deviceSet": [],
        "remoteLinks": [],
        "isHidden": false
    }
    """
)

THIRD_PARTY_SENSOR_ENVIRONMENT = json.loads(
    """
    {
        "id": "84e5a365-a501-4642-aaf5-c9f180390843_1",
        "type": "sensor",
        "deviceType": "environmentSensor",
        "createdAt": "2024-01-23T08:54:51.000Z",
        "isReachable": true,
        "lastSeen": "2024-01-25T17:44:10.000Z",
        "attributes": {
            "customName": "Bedroom Air Sensor",
            "firmwareVersion": "",
            "hardwareVersion": "",
            "manufacturer": "",
            "model": "lumi.weather",
            "serialNumber": "00158D000AD5E783",
            "currentTemperature": 18.15,
            "currentRH": 69,
            "permittingJoin": false,
            "otaPolicy": "autoUpdate",
            "otaProgress": 0,
            "otaScheduleEnd": "00:00",
            "otaScheduleStart": "00:00",
            "otaState": "readyToCheck",
            "otaStatus": "upToDate"
        },
        "capabilities": {
            "canSend": [],
            "canReceive": [
                "customName"
            ]
        },
        "room": {
            "id": "2cd56851-e787-4a88-925b-410c3da7d6ed",
            "name": "Bedroom",
            "color": "ikea_beige_1",
            "icon": "rooms_bed"
        },
        "deviceSet": [],
        "remoteLinks": [],
        "isHidden": false
    }
    """
)

DEVICES = [IKEA_LIGHT_DIMMABLE, THIRD_PARTY_SENSOR_ENVIRONMENT]
