from typing import Any

from rubicon.objc import ObjCClass, ObjCProtocol
from rubicon.objc.runtime import load_library

IOBluetooth = load_library("IOBluetooth")

_CLASS_NAMES = [
    "IOBluetoothDevice",
    "IOBluetoothDeviceInquiry",
    "IOBluetoothSDPUUID",
    "IOBluetoothRFCOMMChannel",
]

_CLASSES: dict[str, Any] = {}

_PROTOCOL_NAMES = [
    "IOBluetoothRFCOMMChannelDelegate",
    "IOBluetoothDeviceInquiryDelegate",
]

_PROTOCOLS: dict[str, Any] = {}


def __getattr__(name: str):
    if name in _CLASS_NAMES:
        try:
            return _CLASSES[name]
        except KeyError:
            return _CLASSES.setdefault(name, ObjCClass(name))

    if name in _PROTOCOL_NAMES:
        try:
            return _PROTOCOLS[name]
        except KeyError:
            return _PROTOCOLS.setdefault(name, ObjCProtocol(name))

    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
