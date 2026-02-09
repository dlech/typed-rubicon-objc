# Note: Foundation types (NS*) from rubicon.objc.api and rubicon.objc.types are
# intentionally redefined here in order to be able to include more methods that
# reference other types not available in rubicon.objc package.

# pyright: reportPrivateUsage=false

from abc import ABCMeta
from collections.abc import Iterator, Mapping, Sequence
from typing import TYPE_CHECKING, Self, TypeVar, overload

from rubicon.objc.api import ObjCClass, ObjCInstance, ObjCProtocol
from rubicon.objc.runtime import SEL, Class, objc_id
from rubicon.objc.types import UnknownPointer

if TYPE_CHECKING:
    from rubicon.objc.api import _ConvertablePyType

__all__ = [
    "NSObject",
    "NSNumber",
    "NSDecimalNumber",
    "NSString",
    "NSData",
    "NSArray",
    "NSMutableArray",
    "NSDictionary",
    "NSMutableDictionary",
]

class NSObject(ObjCInstance, metaclass=ObjCClass):
    """The root class of most Objective-C class hierarchies.

    NSObject is the root class providing a basic interface to the runtime system
    and the ability to behave as Objective-C objects.
    """

    @classmethod
    def alloc(cls) -> Self:
        """Returns a new instance of the receiving class."""
        ...

    @classmethod
    def allocWithZone(cls, zone: None, /) -> Self:
        """Returns a new instance of the receiving class."""
        ...

    def init(self) -> Self:
        """Initializes a newly allocated instance.

        Implemented by subclasses to initialize a new object immediately after
        memory for it has been allocated.
        """
        ...

    @property
    def copy(self) -> Self:
        """Returns a shallow copy of the receiver.

        Returns the object returned by copyWithZone(_:).
        """
        ...

    @classmethod
    def copyWithZone(cls, zone: None, /) -> Self:
        """Returns the receiver."""
        ...

    @property
    def mutableCopy(self) -> Self:
        """Returns a mutable copy of the receiver.

        Returns the object returned by mutableCopyWithZone(_:) where the zone is nil.
        """
        ...

    @classmethod
    def mutableCopyWithZone(cls, zone: None, /) -> Self:
        """Returns the receiver."""
        ...

    def dealloc(self) -> None:
        """Deallocates the memory occupied by the receiver."""
        ...

    @classmethod
    def new(cls) -> Self:
        """Returns a new instance of the receiving class.

        Equivalent to alloc().init().
        """
        ...

    # REVISIT: conflicts with `superclass` property
    # @classmethod
    # def superclass(cls) -> type | None:
    #     """Returns the class object for the receiver's superclass."""
    #     ...

    @classmethod
    def isSubclassOfClass(cls, aClass: Class | ObjCClass, /) -> bool:
        """Returns a Boolean value that indicates whether the receiving class
        is a subclass of, or identical to, a given class.
        """
        ...

    @classmethod
    def instancesRespondToSelector(cls, selector: SEL, /) -> bool:
        """Returns a Boolean value indicating whether instances of the receiver
        respond to a given selector.
        """
        ...

    @classmethod
    def instanceMethodForSelector(cls, selector: SEL, /) -> UnknownPointer:
        """Locates and returns the address of the implementation of an instance
        method identified by a given selector.
        """
        ...

    @classmethod
    def instanceMethodSignatureForSelector(cls, selector: SEL, /) -> UnknownPointer:
        """Returns an NSMethodSignature object for the instance method
        identified by a given selector.
        """
        ...

    @classmethod
    def conformsToProtocol(cls, protocol: ObjCProtocol, /) -> bool:
        """Returns a Boolean value indicating whether the target conforms
        to a given protocol.
        """
        ...

    @property
    def description(self) -> NSString:
        """A textual representation of the receiver."""
        ...

    def methodForSelector(self, selector: SEL, /) -> UnknownPointer:
        """Locates and returns the address of the receiver's implementation
        of a method so it can be called as a function.
        """
        ...

    def methodSignatureForSelector(self, selector: SEL, /) -> object:
        """Returns an NSMethodSignature object for the method identified
        by a given selector.
        """
        ...

    def doesNotRecognizeSelector(self, aSelector: SEL, /) -> None:
        """Handles messages the receiver doesn't recognize.

        Raises NSInvalidArgumentException by default.
        """
        ...

    def forwardingTargetForSelector(self, aSelector: SEL, /) -> object | None:
        """Returns the object to which unrecognized messages should first
        be directed.

        Returns None by default, which causes a doesNotRecognizeSelector
        message to be sent and an NSInvalidArgumentException to be raised.
        """
        ...

    def forwardInvocation(self, anInvocation: object, /) -> None:
        """Overridden by subclasses to forward messages to other objects."""
        ...

    @classmethod
    def resolveClassMethod(cls, sel: SEL, /) -> bool:
        """Dynamically provides an implementation for a given selector
        for a class method.
        """
        ...

    @classmethod
    def resolveInstanceMethod(cls, sel: SEL, /) -> bool:
        """Dynamically provides an implementation for a given selector
        for an instance method.
        """
        ...

    @classmethod
    def load(cls) -> None:
        """Invoked whenever a class or category is added to the Objective-C
        runtime.

        Implement this method to perform class-specific behavior upon loading.
        """
        ...

    @classmethod
    def initialize(cls) -> None:
        """Initializes the class before it receives its first message."""
        ...

    # REVISIT: conflicts with `description` property
    # @classmethod
    # def description(cls) -> NSString:
    #     """Returns a string that represents the contents of the receiving class."""
    #     ...

    # REVISIT: conflicts with `hash` property
    # @classmethod
    # def hash(cls) -> int:
    #     """Returns a hash value for the receiver."""
    #     ...

    def awakeAfterUsingCoder(self, aDecoder: _ConvertablePyType, /) -> object:
        """Overridden by subclasses to substitute another object in place
        of the object that was decoded and subsequently received this message.
        """
        ...

    @property
    def autoContentAccessingProxy(self) -> object:
        """A proxy for the receiving object."""
        ...

    # NSObject protocol conformance

    # REVISIT: conflicts with `class` keyword
    # def class(self) -> Class:
    #     """Returns the class object for the receiver's class."""
    #     ...

    @property
    def superclass(self) -> Class | None:
        """Returns the class object for the receiver's superclass."""
        ...

    def isEqual(self, object: _ConvertablePyType, /) -> bool:
        """Returns a Boolean value that indicates whether the receiver and
        a given object are equal.
        """
        ...

    @property
    def hash(self) -> int:
        """Returns an integer that can be used as a table address in a hash
        table structure.
        """
        ...

    def self(self) -> Self:
        """Returns the receiver."""
        ...

    def isKindOfClass(self, aClass: Class | ObjCClass, /) -> bool:
        """Returns a Boolean value that indicates whether the receiver is an
        instance of the given class or an instance of any class that inherits
        from that class.
        """
        ...

    def isMemberOfClass(self, aClass: Class | ObjCClass, /) -> bool:
        """Returns a Boolean value that indicates whether the receiver is an
        instance of the given class.
        """
        ...

    def respondsToSelector(self, aSelector: SEL, /) -> bool:
        """Returns a Boolean value that indicates whether the receiver implements
        or inherits a method that can respond to a specified message.
        """
        ...

    @property
    def debugDescription(self) -> NSString:
        """A textual representation of the receiver to use with a debugger."""
        ...

    @overload
    def performSelector(self, aSelector: SEL, /) -> ObjCInstance | None:
        """Sends a specified message to the receiver and returns the result
        of the message.
        """
        ...
    @overload
    def performSelector(
        self,
        aSelector: SEL,
        /,
        *,
        withObject: _ConvertablePyType,
    ) -> ObjCInstance | None:
        """Sends a message to the receiver with an object as the argument."""
        ...

    @overload
    def performSelector(
        self,
        aSelector: SEL,
        /,
        *,
        withObject__1: _ConvertablePyType,
        withObject__2: _ConvertablePyType,
    ) -> ObjCInstance | None:
        """Sends a message to the receiver with two objects as arguments."""
        ...

    def isProxy(self) -> bool:
        """Returns a Boolean value that indicates whether the receiver does not
        descend from NSObject.
        """
        ...

    # specific to Rubicon ObjC

    @property
    def ptr(self) -> objc_id:
        """The underlying Objective-C object pointer."""
        ...

class NSNumber(NSObject): ...
class NSDecimalNumber(NSObject): ...
class NSString(NSObject): ...
class NSData(NSObject): ...

_T = TypeVar("_T")

class _NSArrayMeta(ObjCClass, ABCMeta): ...
class NSArray(NSObject, Sequence[_T], metaclass=_NSArrayMeta): ...

NSMutableArray = ...

_TKey = TypeVar("_TKey")
_TValue = TypeVar("_TValue")

class _NSDictionaryMeta(ObjCClass, ABCMeta): ...

class NSDictionary(NSObject, Mapping[_TKey, _TValue], metaclass=_NSDictionaryMeta):
    def allKeys(self) -> NSArray[_TKey]: ...
    def allValues(self) -> NSArray[_TValue]: ...
    def objectForKey_(self, key: _TKey) -> _TValue: ...
    def __getitem__(self, key: _TKey) -> _TValue: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[_TKey]: ...

NSMutableDictionary = ...

class NSMethodSignature(NSObject): ...
class NSUUID(NSObject): ...
class NSCoder(NSObject): ...
class NSDate(NSObject): ...
