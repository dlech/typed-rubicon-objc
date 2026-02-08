from rubicon.objc import ObjCClass, ObjCProtocol
from rubicon.objc.runtime import load_library

IOBluetooth = load_library("IOBluetooth")

_CLASS_NAMES = [
    "IOBluetoothDevice",
    "IOBluetoothDeviceInquiry",
    "IOBluetoothSDPUUID",
    "IOBluetoothRFCOMMChannel",
    "IOBluetoothRFCOMMChannelDelegate",
]

_CLASSES: dict[str, ObjCClass] = {}

_PROTOCOL_NAMES = [
    "IOBluetoothRFCOMMChannelDelegate",
    "IOBluetoothDeviceInquiryDelegate",
]

_PROTOCOLS: dict[str, ObjCProtocol] = {}


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

    return
