
import json

LIGHT_DIMMABLE = json.loads(
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