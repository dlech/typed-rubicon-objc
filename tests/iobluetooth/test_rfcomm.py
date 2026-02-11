from rubicon.objc.api import ObjCProtocol
from typed_rubicon_objc.IOBluetooth import IOBluetoothRFCOMMChannelDelegate


def takes_protocol(protocol: ObjCProtocol) -> None:
    """A helper function to test that the protocol can be used as a type."""
    assert isinstance(protocol, ObjCProtocol)


def test_rfcomm_channel_delegate():
    """Test that the IOBluetoothRFCOMMChannelDelegate protocol typing is correct."""
    takes_protocol(IOBluetoothRFCOMMChannelDelegate)
