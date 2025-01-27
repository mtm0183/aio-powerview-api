"""Constants for Hunter Douglas Powerview hub."""

# used for is_supported functions
MOTION_VELOCITY = "velocity"
MOTION_JOG = "jog"
MOTION_CALIBRATE = "calibrate"
MOTION_FAVORITE = "heart"
FUNCTION_SET_POWER = "set_power"
FUNCTION_SCHEDULE = "schedule"
FUNCTION_REBOOT = "reboot"
FUNCTION_IDENTIFY = "identify"

# common across all API versions
HUB_NAME = "hubName"

ATTR_SCENE = "scene"
ATTR_SHADE = "shade"
ATTR_ROOM = "room"
ATTR_SCENE_MEMBER = "sceneMember"

ATTR_SHADE_DATA = "shadeData"
ATTR_SCENE_DATA = "sceneData"
SCENE_MEMBER_DATA = "sceneMemberData"
ATTR_ROOM_DATA = "roomData"

ATTR_ICON_ID = "iconId"
ATTR_COLOR_ID = "colorId"
ATTR_SCENE_ID = "sceneId"
ATTR_SHADE_ID = "shadeId"
ATTR_ROOM_ID = "roomId"

ATTR_ID = "id"
ATTR_TYPE = "type"
ATTR_NAME = "name"
ATTR_NAME_UNICODE = "name_unicode"

ATTR_SIGNAL_STRENGTH = "signalStrength"
ATTR_SIGNAL_STRENGTH_MAX = 4

FIRMWARE = "firmware"
FIRMWARE_NAME = "name"
FIRMWARE_REVISION = "revision"
FIRMWARE_SUB_REVISION = "subRevision"
FIRMWARE_BUILD = "build"
FIRMWARE_MAINPROCESSOR = "mainProcessor"

MAC_ADDRESS = "macAddress"
SERIAL_NUMBER = "serialNumber"

ATTR_CAPABILITIES = "capabilities"
ATTR_POSITIONS = "positions"

MOTION_STOP = "stop"

POWERTYPE_HARDWIRED = "Hardwired"
POWERTYPE_BATTERY = "Battery"
POWERTYPE_RECHARGABLE = "Rechargable"

# using percentage based positions in aiopvapi v3
MIN_POSITION = 0
MID_POSITION = 50
MAX_POSITION = 100
CLOSED_POSITION = 0

# v2
FWVERSION = "fwversion"
USER_DATA = "userData"

MAX_POSITION_V2 = 65535

SHADE_BATTERY_STRENGTH = "batteryStrength"
SHADE_BATTERY_STRENGTH_MAX = 200

POSKIND_PRIMARY = 1
POSKIND_SECONDARY = 2
POSKIND_TILT = 3

ATTR_BATTERY_KIND = "batteryKind"
BATTERY_KIND_HARDWIRED = 1
BATTERY_KIND_BATTERY = 2
BATTERY_KIND_RECHARGABLE = 3

ATTR_POSKIND1 = "posKind1"
ATTR_POSKIND2 = "posKind2"
ATTR_POSITION1 = "position1"
ATTR_POSITION2 = "position2"

ATTR_SCHEDULED_EVENT = "scheduledEvent"
ATTR_SCHEDULED_EVENT_DATA = "scheduledEventData"

ATTR_SHADE_IDS = "shadeIds"

POSITIONS_V2 = (
    (ATTR_POSITION1, ATTR_POSKIND1),
    (ATTR_POSITION2, ATTR_POSKIND2),
)

POWERTYPE_MAP_V2 = {
    POWERTYPE_HARDWIRED: 1,
    POWERTYPE_BATTERY: 2,
    POWERTYPE_RECHARGABLE: 3,
}

# v3
NETWORK_STATUS = "networkStatus"
CONFIG = "config"

SHADE_BATTERY_STATUS = "batteryStatus"
SHADE_BATTERY_STATUS_MAX = 3

ATTR_PTNAME = "ptName"
ATTR_POWER_TYPE = "powerType"

ATTR_ROOM_IDS = "roomIds"

ATTR_PRIMARY = "primary"
ATTR_SECONDARY = "secondary"
ATTR_TILT = "tilt"
ATTR_VELOCITY = "velocity"

POSITIONS_V3 = (
    ATTR_PRIMARY,
    ATTR_SECONDARY,
    ATTR_TILT,
    ATTR_VELOCITY,
)

POWERTYPE_MAP_V3 = {
    POWERTYPE_BATTERY: 0,
    POWERTYPE_HARDWIRED: 1,
    POWERTYPE_RECHARGABLE: 2,
}

# Legacy (Gen1) where firmware needs to be hardcoded
DEFAULT_LEGACY_MAINPROCESSOR = {
    FIRMWARE_REVISION: 0,
    FIRMWARE_SUB_REVISION: 1,
    FIRMWARE_BUILD: 0,
    FIRMWARE_NAME: "PowerView Hub",
}

HUB_MODEL_MAPPING = {
    "PV_Gen3": "Powerview Generation 3",
    "PV Hub2.0": "Powerview Generation 2",
    "PowerView Hub": "Powerview Generation 1",
}
