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
class HubCoordinates:
    latitude: Optional[float]
    longitude: Optional[float]
    accuracy: Optional[float] # -1 for me

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
    coordinates: Optional[HubCoordinates]

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
    otaStatus: Optional[str] = None # Not everything is OTA capable
    otaState: Optional[str] = None
    otaProgress: Optional[str] = None
    otaPolicy: Optional[str] = None
    otaScheduleStart: Optional[str] = None
    otaScheduleEnd: Optional[str] = None
    productCode: Optional[str] = None  # Only on Ikea devices
    isOn: Optional[bool] = None  # Only on On/Off devices
    startupOnOff: Optional[str] = None  # Only on On/Off devices
    lightLevel: Optional[bool] = None  # Only on lights
    currentTemperature: Optional[str] = None  # Only on environment sensors
    currentRH: Optional[str] = None  # Only on environment sensors
    identifyStarted: Optional[str] = None  # Only on Ikea devices
    identifyPeriod: Optional[int] = None  # Only on Ikea devices
    permittingJoin: Optional[bool] = None  # ???
    batteryPercentage: Optional[str] = None
    blindsCurrentLevel: Optional[str] = None
    blindsState: Optional[str] = None # Probably an enum?
    blindsTargetLevel: Optional[str] = None
    circadianPresets: Optional[str] = None # donno
    colorHue: Optional[str] = None # donno
    colorSaturation: Optional[str] = None # donno
    colorTemperature: Optional[str] = None # donno
    colorTemperatureMin: Optional[str] = None # donno
    colorTemperatureMax: Optional[str] = None # donno
    startupTemperature: Optional[str] = None # donno
    colorMode: Optional[str] = None # donno
    playback: Optional[str] = None # donno
    playbackLastChangedTimestamp: Optional[str] = None # donno
    playbackAudio: Optional[str] = None # speaker?
    playbackPosition: Optional[str] = None # speaker?
    playbackAvailableActions: Optional[str] = None # speaker?
    playbackModes: Optional[str] = None # speaker?
    volume: Optional[str] = None # speaker?
    isMuted: Optional[str] = None # speaker?
    audioGroup: Optional[str] = None # speaker?
    sensorConfig: Optional[str] = None # no idea

@dataclass
class DeviceRoom:
    id: Optional[str] = None
    name: Optional[str] = "Unassigned"
    color: Optional[str] = None
    icon: Optional[str] = None

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
    deviceSet: List[str]
    remoteLinks: List[str]
    isHidden: bool
    room: Optional[DeviceRoom] = None
    customIcon: Optional[str] = None

    def __post_init__(self):
        self.attributes = DeviceAttributes(**self.attributes)
        self.capabilities = Capabilities(**self.capabilities)

        if(self.room is not None):
            self.room = DeviceRoom(**self.room)
