"""
For more information on XPC services, see Apple's documentation:
https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/CreatingXPCServices.html
"""

import importlib
import sys
from typing import TYPE_CHECKING, cast

from rubicon.objc.api import (
    Block,
    ObjCInstance,
    ObjCProtocol,
    objc_method,
)
from rubicon.objc.runtime import objc_block, objc_id, send_message
from typed_rubicon_objc.Foundation import (
    NSObject,
    NSSecureCoding,
    NSString,
    NSXPCConnection,
    NSXPCInterface,
    NSXPCListener,
    NSXPCListenerDelegate,
)

# This is just to load a library that contains a protocol. We could alternately
# create a regular library and load it with rubicon.objc.api.load_library instead.
# XPC requires that the protocol is compiled with clang in order to get some
# extra metadata that is needed to create the NSXPCInterface. So we can't just
# define the protocol in Python.
importlib.import_module("test_protocol_ext")

# Loads the protocol from the library we just loaded.
TestProtocol = ObjCProtocol("TestProtocol")


if TYPE_CHECKING:

    class ExampleObject(NSObject, protocols=[TestProtocol, NSSecureCoding]):
        @objc_method
        def doSomething(
            self, _name: NSString | str, /, *, withReply: Block
        ) -> None: ...
else:

    class ExampleObject(NSObject, protocols=[TestProtocol, NSSecureCoding]):
        @objc_method
        def doSomething_withReply_(self, name: objc_id, completion: objc_block) -> None:
            if sys.version_info >= (3, 14):
                # https://github.com/astral-sh/ty/issues/2891
                completion(name)  # ty: ignore[call-non-callable]
            else:
                completion(name)


class ExampleListenerDelegate(NSObject, protocols=[NSXPCListenerDelegate]):
    exported_interface: NSXPCInterface
    exported_object: NSObject

    @objc_method
    def listener_shouldAcceptNewConnection_(
        self, _listener: objc_id, _new_connection: objc_id
    ) -> bool:
        new_connection = cast(NSXPCConnection, _new_connection)

        new_connection.exportedInterface = self.exported_interface
        new_connection.exportedObject = self.exported_object
        new_connection.activate()

        return True


def test_nsxpc_listener_and_connection_round_trip() -> None:
    """Create a listener and connection and verify they can exchange a message."""

    interface = NSXPCInterface.interfaceWithProtocol(TestProtocol)
    listener = NSXPCListener.anonymousListener()
    delegate = ExampleListenerDelegate.new()
    delegate.exported_interface = interface
    service = ExampleObject.new()
    delegate.exported_object = service

    listener.delegate = delegate
    listener.activate()

    client = NSXPCConnection.alloc().initWithListenerEndpoint(listener.endpoint)
    client.remoteObjectInterface = interface
    client.activate()

    errors: list[ObjCInstance] = []

    @Block
    def on_error(error: objc_id) -> None:
        errors.append(ObjCInstance(error))

    proxy = cast(
        ExampleObject, client.synchronousRemoteObjectProxyWithErrorHandler(on_error)
    )

    replies: list[str] = []

    @Block
    def callback(_reply: objc_id) -> None:
        reply = ObjCInstance(_reply)
        replies.append(str(reply))

    send_message(
        proxy,
        "doSomething:withReply:",
        NSString.stringWithString("xpc server"),
        callback,
        argtypes=[objc_id, objc_block],
        restype=None,
    )

    client.invalidate()
    listener.invalidate()

    assert errors == []
    assert replies == ["xpc server"]
