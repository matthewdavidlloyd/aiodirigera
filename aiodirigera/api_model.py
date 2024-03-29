from typing import Optional, List

from dataclasses import dataclass

# Generic


@dataclass
class Capabilities:
    canSend: List[str]
    canReceive: List[str]


# Hub Specific


@dataclass
class UserConsents:
    name: str
    value: str


@dataclass
class HubAttributes:
    customName: str
    model: str
    manufacturer: str
    firmwareVersion: str
    hardwareVersion: str
    serialNumber: str
    identifyStarted: str
    identifyPeriod: str
    otaStatus: str
    otaState: str
    otaProgress: str
    otaPolicy: str
    otaScheduleStart: str
    otaScheduleEnd: str
    permittingJoin: str
    backendConnected: str
    backendConnectionPersistent: str
    backendOnboardingComplete: str
    backendRegion: str
    backendCountryCode: str
    userConsents: List[UserConsents]
    logLevel: int
    coredump: bool
    timezone: str
    nextSunSet: str
    nextSunRise: str
    homestateValue: str
    homestateLastChanged: str
    countryCode: str
    isOn: bool

    def __post_init__(self):
        self.userConsents = [UserConsents(**x) for x in self.userConsents]


@dataclass
class HubStatus:
    id: str
    relationId: str
    type: str
    deviceType: str
    createdAt: str
    isReachable: bool
    lastSeen: str
    attributes: HubAttributes
    capabilities: Capabilities
    deviceSet: List[str]
    remoteLinks: List[str]
    environment: str
    apiVersion: str

    def __post_init__(self):
        self.attributes = HubAttributes(**self.attributes)
        self.capabilities = Capabilities(**self.capabilities)


# Device Specific


@dataclass
class DeviceAttributes:
    customName: str
    model: str
    manufacturer: str
    firmwareVersion: str
    hardwareVersion: str
    serialNumber: str
    otaStatus: str
    otaState: str
    otaProgress: int
    otaPolicy: str
    otaScheduleStart: str
    otaScheduleEnd: str
    productCode: Optional[str] = None  # Only on Ikea devices
    isOn: Optional[bool] = None  # Only on On/Off devices
    startupOnOff: Optional[str] = None  # Only on On/Off devices
    lightLevel: Optional[bool] = None  # Only on lights
    currentTemperature: Optional[str] = None  # Only on environment sensors
    currentRH: Optional[str] = None  # Only on environment sensors
    identifyStarted: Optional[str] = None  # Only on Ikea devices
    identifyPeriod: Optional[int] = None  # Only on Ikea devices
    permittingJoin: Optional[bool] = None  # ???


@dataclass
class DeviceRoom:
    id: str
    name: str
    color: str
    icon: str


@dataclass
class DeviceStatus:
    id: str
    type: str
    deviceType: str
    createdAt: str
    isReachable: bool
    lastSeen: str
    attributes: DeviceAttributes
    capabilities: Capabilities
    room: DeviceRoom
    deviceSet: List[str]
    remoteLinks: List[str]
    isHidden: bool
    customIcon: Optional[str] = None

    def __post_init__(self):
        self.attributes = DeviceAttributes(**self.attributes)
        self.capabilities = Capabilities(**self.capabilities)
        self.room = DeviceRoom(**self.room)
