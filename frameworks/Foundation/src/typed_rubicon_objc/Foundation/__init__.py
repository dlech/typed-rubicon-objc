from typing import Any

from rubicon.objc.api import NSArray as NSArray
from rubicon.objc.api import NSData as NSData
from rubicon.objc.api import NSDictionary as NSDictionary
from rubicon.objc.api import NSNumber as NSNumber
from rubicon.objc.api import NSObject as NSObject
from rubicon.objc.api import NSString as NSString
from rubicon.objc.api import ObjCClass
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
]

__all__.extend(_CLASSES)  # pyright: ignore[reportUnsupportedDunderAll]

_CLASS_MAP: dict[str, Any] = {}


def __getattr__(name: str):
    if name in _CLASSES:
        try:
            return _CLASS_MAP[name]
        except KeyError:
            return _CLASS_MAP.setdefault(name, ObjCClass(name))
