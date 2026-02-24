import types
from typing import Any

from rubicon.objc.api import NSArray as NSArray
from rubicon.objc.api import NSData as NSData
from rubicon.objc.api import NSDictionary as NSDictionary
from rubicon.objc.api import NSNumber as NSNumber
from rubicon.objc.api import NSObject as NSObject
from rubicon.objc.api import NSString as NSString
from rubicon.objc.api import ObjCClass, ObjCProtocol
from rubicon.objc.types import NSInteger as NSInteger
from rubicon.objc.types import NSUInteger as NSUInteger

__all__ = [
    "NSArray",
    "NSData",
    "NSDictionary",
    "NSNumber",
    "NSObject",
    "NSString",
    "NSInteger",
    "NSUInteger",
]

_CLASSES = [
    "NSMethodSignature",
    "NSUUID",
    "NSValue",
    "NSException",
    "NSProcessInfo",
    "NSRunLoop",
    "NSThread",
    "NSInvocation",
    "NSInvocationOperation",
    "NSOperation",
    "NSOperationQueue",
    "NSCache",
    "NSSet",
    "NSOrderedSet",
    "NSCountedSet",
    "NSCharacterSet",
    "NSXPCConnection",
    "NSXPCListener",
    "NSXPCListenerEndpoint",
    "NSXPCInterface",
]

__all__.extend(_CLASSES)  # pyright: ignore[reportUnsupportedDunderAll]

_CLASS_MAP: dict[str, Any] = {}


_DELEGATES = [
    "NSSecureCoding",
    "NSXPCListenerDelegate",
]

__all__.extend(_DELEGATES)  # pyright: ignore[reportUnsupportedDunderAll]

_DELEGATE_MAP: dict[str, Any] = {}

# HACK: Add __class_getitem__ to NSArray to support NSArray[T] generics
if not hasattr(NSArray, "__class_getitem__"):
    setattr(NSArray, "__class_getitem__", types.MethodType(types.GenericAlias, NSArray))


def __getattr__(name: str):
    if name in _CLASSES:
        try:
            return _CLASS_MAP[name]
        except KeyError:
            cls = ObjCClass(name)

            return _CLASS_MAP.setdefault(name, cls)

    if name in _DELEGATES:
        try:
            return _DELEGATE_MAP[name]
        except KeyError:
            protocol = ObjCProtocol(name)

            return _DELEGATE_MAP.setdefault(name, protocol)

    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
