# Note: Foundation types (NS*) from rubicon.objc.api and rubicon.objc.types are
# intentionally redefined here in order to be able to include more methods that
# reference other types not available in rubicon.objc package.

# pyright: reportPrivateUsage=false

import ctypes
import typing
from abc import ABCMeta
from collections.abc import Callable, Iterator, Mapping, Sequence
from typing import (
    TYPE_CHECKING,
    TypeAlias,
    TypeVar,
    overload,
    type_check_only,
)

from rubicon.objc.api import Block, ObjCClass, ObjCInstance, ObjCProtocol, Protocol
from rubicon.objc.runtime import SEL, Class, objc_id
from rubicon.objc.types import NSInteger as NSInteger
from rubicon.objc.types import NSUInteger as NSUInteger
from rubicon.objc.types import UnknownPointer
from typing_extensions import Self

if TYPE_CHECKING:
    from rubicon.objc.api import _ConvertablePyType

__all__ = [
    "NSInteger",
    "NSUInteger",
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

class NSString(NSObject):
    @classmethod
    def stringWithString(cls, string: NSString | str, /) -> Self: ...

class NSData(NSObject): ...

_T = TypeVar("_T")

@type_check_only
class _NSArrayMeta(ObjCClass, ABCMeta): ...

_T_co = TypeVar("_T_co", covariant=True)

class _ConvertableTo(typing.Protocol[_T_co]): ...

class NSArray(NSObject, Sequence[_T], metaclass=_NSArrayMeta):
    """An object representing a static ordered collection.

    NSArray is immutable. For a mutable array, use NSMutableArray.
    """

    # Creating an Array

    @classmethod
    def array(cls) -> Self:
        """Creates and returns an empty array."""
        ...

    @classmethod
    def arrayWithArray(cls, array: Sequence[_ConvertableTo[_T]], /) -> Self:
        """Creates and returns an array containing the objects in another given array."""
        ...

    @classmethod
    def arrayWithObject(cls, anObject: _ConvertableTo[_T], /) -> Self:
        """Creates and returns an array containing a given object."""
        ...

    # FIXME: not sure how to call varargs method without crashing
    @overload
    @classmethod
    def arrayWithObjects(cls, objects: list[_ConvertableTo[_T]], /) -> Self:
        """Creates and returns an array containing the objects in the argument list."""
        ...

    @overload
    @classmethod
    def arrayWithObjects(cls, objects: _ConvertableTo[_T], /, *, count: int) -> Self:
        """Creates and returns an array that includes a given number of objects from a given C array."""
        ...

    # Initializing an Array

    def init(self) -> Self:
        """Initializes a newly allocated array."""
        ...

    @overload
    def initWithArray(self, array: Sequence[_T], /) -> Self:
        """Initializes a newly allocated array by placing in it the objects contained in a given array."""
        ...

    @overload
    def initWithArray(self, array: Sequence[_T], /, *, copyItems: bool) -> Self:
        """Initializes a newly allocated array using anArray as the source of data objects for the array."""
        ...

    @overload
    def initWithObjects(self, objects: list[_ConvertableTo[_T]], /) -> Self:
        """Initializes a newly allocated array by placing in it the objects in the argument list."""
        ...

    @overload
    def initWithObjects(self, objects: _ConvertableTo[_T], /, *, count: int) -> Self:
        """Initializes a newly allocated array to include a given number of objects from a given C array."""
        ...

    def initWithCoder(self, coder: object, /) -> Self | None:
        """Initializes an array with the contents of a coder."""
        ...

    # Querying an Array

    def containsObject(self, anObject: _ConvertableTo[_T], /) -> bool:
        """Returns a Boolean value that indicates whether a given object is present in the array."""
        ...

    # Python Sequence count takes precedence
    # @property
    # def count(self) -> int:
    #     """The number of objects in the array."""
    #     ...

    @overload
    def getObjects(self, objects: object, /) -> None:
        """Copies all the objects contained in the array to aBuffer."""
        ...

    @overload
    def getObjects(self, objects: object, /, *, range: tuple[int, int]) -> None:
        """Copies references to objects contained in the array that fall within the specified range to aBuffer."""
        ...

    def firstObject(self) -> _T | None:
        """The first object in the array."""
        ...

    def lastObject(self) -> _T | None:
        """The last object in the array."""
        ...

    def objectAtIndex(self, index: int, /) -> _T:
        """Returns the object located at the specified index."""
        ...

    def objectAtIndexedSubscript(self, idx: int, /) -> _T:
        """Returns the object at the specified index."""
        ...

    def objectsAtIndexes(self, indexes: object, /) -> NSArray[_T]:
        """Returns an array containing the objects in the array at the indexes specified by a given index set."""
        ...

    def objectEnumerator(self) -> object:
        """Returns an enumerator object that lets you access each object in the array."""
        ...

    def reverseObjectEnumerator(self) -> object:
        """Returns an enumerator object that lets you access each object in the array, in reverse order."""
        ...

    # Finding Objects in an Array

    @overload
    def indexOfObject(self, anObject: _ConvertableTo[_T], /) -> int:
        """Returns the lowest index whose corresponding array value is equal to a given object."""
        ...

    @overload
    def indexOfObject(
        self, anObject: _ConvertableTo[_T], /, *, inRange: tuple[int, int]
    ) -> int:
        """Returns the lowest index within a specified range whose corresponding array value is equal to a given object."""
        ...

    @overload
    def indexOfObjectIdenticalTo(self, anObject: _ConvertableTo[_T], /) -> int:
        """Returns the lowest index whose corresponding array value is identical to a given object."""
        ...

    @overload
    def indexOfObjectIdenticalTo(
        self, anObject: _ConvertableTo[_T], /, *, inRange: tuple[int, int]
    ) -> int:
        """Returns the lowest index within a specified range whose corresponding array value is identical to a given object."""
        ...

    def indexOfObjectPassingTest(self, predicate: object, /) -> int:
        """Returns the index of the first object in the array that passes a test in a given block."""
        ...

    def indexOfObjectWithOptions(self, opts: int, /, *, passingTest: object) -> int:
        """Returns the index of an object in the array that passes a test in a given block for a given set of enumeration options."""
        ...

    def indexOfObjectAtIndexes(
        self,
        s: object,
        /,
        *,
        options: int,
        passingTest: Callable[[_T, int, ctypes._Pointer[ctypes.c_bool]], bool],
    ) -> int:
        """Returns the index, from a given set of indexes, of the first object in the array that passes a test in a given block for a given set of enumeration options."""
        ...

    def indexesOfObjectsPassingTest(
        self, predicate: Callable[[_T, int, ctypes._Pointer[ctypes.c_bool]], bool], /
    ) -> object:
        """Returns the indexes of objects in the array that pass a test in a given block."""
        ...

    def indexesOfObjectsWithOptions(
        self,
        opts: int,
        /,
        *,
        passingTest: Callable[[_T, int, ctypes._Pointer[ctypes.c_bool]], bool],
    ) -> object:
        """Returns the indexes of objects in the array that pass a test in a given block for a given set of enumeration options."""
        ...

    def indexesOfObjectsAtIndexes(
        self,
        s: object,
        /,
        *,
        options: int,
        passingTest: Callable[[_T, int, ctypes._Pointer[ctypes.c_bool]], bool],
    ) -> object:
        """Returns the indexes, from a given set of indexes, of objects in the array that pass a test in a given block for a given set of enumeration options."""
        ...

    # Sending Messages to Elements

    @overload
    def makeObjectsPerformSelector(self, aSelector: SEL, /) -> None:
        """Sends to each object in the array the message identified by a given selector, starting with the first object and continuing through the array to the last object."""
        ...

    @overload
    def makeObjectsPerformSelector(
        self, aSelector: SEL, /, *, withObject: object
    ) -> None:
        """Sends the aSelector message to each object in the array, starting with the first object and continuing through the array to the last object."""
        ...

    def enumerateObjectsUsingBlock(self, block: object, /) -> None:
        """Executes a given closure or block using each object in the array, starting with the first object and continuing through the array to the last object."""
        ...

    def enumerateObjectsWithOptions(self, opts: int, /, *, usingBlock: object) -> None:
        """Executes a given closure or block using each object in the array with the specified options."""
        ...

    def enumerateObjectsAtIndexes(
        self,
        s: object,
        /,
        *,
        options: int,
        usingBlock: Callable[[_T, int, ctypes._Pointer[ctypes.c_bool]], None],
    ) -> None:
        """Executes a given block using the objects in the array at the specified indexes."""
        ...

    # Comparing Arrays

    def firstObjectCommonWithArray(self, otherArray: NSArray[_T], /) -> _T | None:
        """Returns the first object contained in the receiving array that's equal to an object in another given array."""
        ...

    def isEqualToArray(self, otherArray: NSArray[_T], /) -> bool:
        """Compares the receiving array to another array."""
        ...

    # Deriving New Arrays

    def arrayByAddingObject(self, anObject: _ConvertableTo[_T], /) -> Self:
        """Returns a new array that is a copy of the receiving array with a given object added to the end."""
        ...

    def arrayByAddingObjectsFromArray(self, otherArray: NSArray[_T], /) -> Self:
        """Returns a new array that is a copy of the receiving array with the objects contained in another array added to the end."""
        ...

    def filteredArrayUsingPredicate(self, predicate: object, /) -> Self:
        """Evaluates a given predicate against each object in the receiving array and returns a new array containing the objects for which the predicate returns true."""
        ...

    def subarrayWithRange(self, range: tuple[int, int], /) -> Self:
        """Returns a new array containing the receiving array's elements that fall within the limits specified by a given range."""
        ...

    # Sorting

    def sortedArrayHint(self) -> NSData:
        """Analyzes the array and returns a "hint" that speeds the sorting of the array when the hint is supplied to sortedArrayUsingFunction:context:hint:."""
        ...

    @overload
    def sortedArrayUsingFunction(
        self, comparator: object, /, *, context: object
    ) -> Self:
        """Returns a new array that lists the receiving array's elements in ascending order as defined by the comparison function comparator."""
        ...

    @overload
    def sortedArrayUsingFunction(
        self, comparator: object, /, *, context: object, hint: NSData
    ) -> Self:
        """Returns a new array that lists the receiving array's elements in ascending order as defined by the comparison function comparator."""
        ...

    def sortedArrayUsingDescriptors(self, sortDescriptors: object, /) -> Self:
        """Returns a copy of the receiving array sorted as specified by a given array of sort descriptors."""
        ...

    def sortedArrayUsingSelector(self, comparator: SEL, /) -> Self:
        """Returns an array that lists the receiving array's elements in ascending order, as determined by the comparison method specified by a given selector."""
        ...

    def sortedArrayUsingComparator(self, cmptr: object, /) -> Self:
        """Returns an array that lists the receiving array's elements in ascending order, as determined by the comparison method specified by a given NSComparator block."""
        ...

    def sortedArrayWithOptions(self, opts: int, /, *, usingComparator: object) -> Self:
        """Returns an array that lists the receiving array's elements in ascending order, as determined by the comparison method specified by a given NSComparator block."""
        ...

    # Working with String Elements

    def componentsJoinedByString(self, separator: str | NSString, /) -> NSString:
        """Constructs and returns an NSString object that is the result of interposing a given separator between the elements of the array."""
        ...

    # Creating a Description

    @property
    def description(self) -> NSString:
        """A string that represents the contents of the array, formatted as a property list."""
        ...

    @overload
    def descriptionWithLocale(self, locale: object, /) -> NSString:
        """Returns a string that represents the contents of the array, formatted as a property list."""
        ...

    @overload
    def descriptionWithLocale(self, locale: object, /, *, indent: int) -> NSString:
        """Returns a string that represents the contents of the array, formatted as a property list."""
        ...

    # Collecting Paths

    def pathsMatchingExtensions(self, filterTypes: list[str], /) -> list[str]:
        """Returns an array containing all the pathname elements in the receiving array that have filename extensions from a given array."""
        ...

    # Randomly Shuffling an Array

    def shuffledArray(self) -> Self:
        """Returns a new array that lists this array's elements in a random order."""
        ...

    def shuffledArrayWithRandomSource(self, source: object, /) -> Self:
        """Returns a new array that lists this array's elements in a random order, using the specified random source."""
        ...

    # Comparing with Another Array

    @overload
    def differenceFromArray(self, other: NSArray[_T], /) -> object:
        """Compares two arrays to create a difference object that represents the changes between them."""
        ...

    @overload
    def differenceFromArray(self, other: NSArray[_T], /, *, withOptions: int) -> object:
        """Compares two arrays, with options, to create a difference object that represents the changes between them."""
        ...

    @overload
    def differenceFromArray(
        self, other: NSArray[_T], /, *, withOptions: int, usingEquivalenceTest: object
    ) -> object:
        """Compares two arrays, using the provided block and with options, to create a difference object that represents the changes between them."""
        ...

    def arrayByApplyingDifference(self, difference: object, /) -> Self | None:
        """Creates a new array by applying a difference object to an existing array."""
        ...

    # Sequence protocol methods (inherited from Sequence[_T])

    @overload
    def __getitem__(self, index: int) -> _T:
        """Returns the object at the specified index."""
        ...

    @overload
    def __getitem__(self, index: slice) -> Self:
        """Returns a subarray for the specified slice."""
        ...

    def __len__(self) -> int:
        """Returns the number of objects in the array."""
        ...

    def __iter__(self) -> Iterator[_T]:
        """Returns an iterator over the array elements."""
        ...

    def __contains__(self, value: object) -> bool:
        """Returns True if the array contains the specified item."""
        ...

NSMutableArray = ...

_TKey = TypeVar("_TKey")
_TValue = TypeVar("_TValue")

@type_check_only
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

class NSError(NSObject):
    @property
    def domain(self) -> NSString: ...
    @property
    def code(self) -> NSInteger: ...
    @property
    def userInfo(self) -> NSDictionary[NSString, objc_id]: ...

NSXPCConnectionOptions: TypeAlias = NSUInteger

NSXPCConnectionPrivileged: NSXPCConnectionOptions

class NSXPCConnection(NSObject):
    """A bidirectional communication channel between two processes."""

    def initWithListenerEndpoint(self, endpoint: NSXPCListenerEndpoint, /) -> Self:
        """Initializes a connection to a listener identified by an endpoint object."""
        ...

    def initWithMachServiceName(
        self,
        name: NSString | str,
        /,
        *,
        options: NSXPCConnectionOptions,
    ) -> Self:
        """Initializes a connection to a LaunchAgent or LaunchDaemon by mach service name."""
        ...

    def initWithServiceName(self, serviceName: NSString | str, /) -> Self:
        """Initializes a connection to an XPC service in the current app's bundle."""
        ...

    def activate(self) -> None:
        """Activates the connection."""
        ...

    def resume(self) -> None:
        """Starts or resumes handling of messages on the connection."""
        ...

    def invalidate(self) -> None:
        """Invalidates the connection so it can't be resumed or reused."""
        ...

    def suspend(self) -> None:
        """Suspends handling of incoming messages on the connection."""
        ...

    @property
    def interruptionHandler(self) -> Block | None:
        """A handler called when the remote process exits or crashes."""
        ...

    @interruptionHandler.setter
    def interruptionHandler(self, handler: Block | None) -> None: ...
    @property
    def invalidationHandler(self) -> Block | None:
        """A handler called when the connection becomes invalid and can't be re-established."""
        ...

    @invalidationHandler.setter
    def invalidationHandler(self, handler: Block | None) -> None: ...
    @classmethod
    def currentConnection(cls) -> Self | None:
        """Returns the current connection while handling a call on an exported object."""
        ...

    def scheduleSendBarrierBlock(self, barrier: Block, /) -> None:
        """Schedules a barrier block to run after all currently enqueued outgoing messages are sent."""
        ...

    @property
    def serviceName(self) -> NSString | None:
        """The service name this connection is configured to connect to."""
        ...

    @property
    def endpoint(self) -> NSXPCListenerEndpoint | None:
        """The listener endpoint used to create this connection, if any."""
        ...

    @property
    def exportedInterface(self) -> NSXPCInterface | None:
        """The interface that describes methods exposed by the exported object."""
        ...

    @exportedInterface.setter
    def exportedInterface(self, interface: NSXPCInterface | None) -> None: ...
    @property
    def exportedObject(self) -> NSObject | None:
        """The local object exported to the remote process."""
        ...

    @exportedObject.setter
    def exportedObject(self, object: objc_id | NSObject | None) -> None: ...
    @property
    def remoteObjectInterface(self) -> NSXPCInterface | None:
        """The interface describing methods available on the remote object."""
        ...

    @remoteObjectInterface.setter
    def remoteObjectInterface(self, interface: NSXPCInterface | None) -> None: ...
    def remoteObjectProxy(self) -> objc_id:
        """Returns a proxy for the remote object exported by the other process."""
        ...

    @property
    def auditSessionIdentifier(self) -> int:
        """The BSM audit session identifier for the connecting process."""
        ...

    @property
    def processIdentifier(self) -> int:
        """The process identifier (PID) of the connecting process."""
        ...

    @property
    def effectiveGroupIdentifier(self) -> int:
        """The effective group identifier (EGID) of the connecting process."""
        ...

    @property
    def effectiveUserIdentifier(self) -> int:
        """The effective user identifier (EUID) of the connecting process."""
        ...

    def remoteObjectProxyWithErrorHandler(
        self, handler: Block | Callable[[NSError], None], /
    ) -> objc_id:
        """Returns a remote object proxy that invokes a handler when message sending fails."""
        ...

    def synchronousRemoteObjectProxyWithErrorHandler(
        self, handler: Block | Callable[[NSError], None], /
    ) -> objc_id:
        """Returns a synchronous remote object proxy with an error handler."""
        ...

    def setCodeSigningRequirement(self, requirement: NSString | str, /) -> None:
        """Sets the code-signing requirement that remote code must satisfy for this connection."""
        ...

class NSXPCInterface(NSObject):
    """Describes the messaging protocol and allowed classes for an XPC endpoint."""

    @property
    def protocol(self) -> Protocol:
        """The Objective-C protocol that this interface is based on."""
        ...

    def classesForSelector(
        self,
        sel: SEL,
        /,
        *,
        argumentIndex: NSUInteger,
        ofReply: bool,
    ) -> object | None:
        """Returns allowed classes for the specified collection argument of a selector."""
        ...

    def interfaceForSelector(
        self,
        sel: SEL,
        /,
        *,
        argumentIndex: NSUInteger,
        ofReply: bool,
    ) -> NSXPCInterface | None:
        """
        Returns the interface configured for the specified selector argument.

        .. danger:: This isn't usable with protocols created in Python, it will
            cause a crash if called with the following error message:

            *** Terminating app due to uncaught exception 'NSInvalidArgumentException',
            reason: 'NSXPCInterface: Unable to get extended method signature from Protocol
            data (...). Use of clang is required for NSXPCInterface.'
        """
        ...

    def setClasses(
        self,
        classes: object,
        /,
        *,
        forSelector: SEL,
        argumentIndex: NSUInteger,
        ofReply: bool,
    ) -> None:
        """Sets allowed classes for the specified collection argument of a selector."""
        ...

    def setInterface(
        self,
        ifc: NSXPCInterface | None,
        /,
        *,
        forSelector: SEL,
        argumentIndex: NSUInteger,
        ofReply: bool,
    ) -> None:
        """Configures a selector argument to be transmitted as a proxy using another interface."""
        ...

    def setXPCType(
        self,
        xpcType: objc_id,
        /,
        *,
        forSelector: SEL,
        argumentIndex: NSUInteger,
        ofReply: bool,
    ) -> None:
        """Sets the required low-level XPC type for a selector argument."""
        ...

    def xpcTypeForSelector(
        self,
        sel: SEL,
        /,
        *,
        argumentIndex: NSUInteger,
        ofReply: bool,
    ) -> objc_id | None:
        """Returns the configured low-level XPC type for a selector argument."""
        ...

    @classmethod
    def interfaceWithProtocol(cls, protocol: ObjCProtocol, /) -> Self:
        """Returns an interface instance for the given Objective-C protocol."""
        ...

NSXPCListenerDelegate: ObjCProtocol

class NSXPCListener(NSObject):
    """A listener object that accepts incoming XPC connections."""

    def initWithMachServiceName(self, name: NSString | str, /) -> Self:
        """Initializes a listener for a LaunchAgent or LaunchDaemon mach service name."""
        ...

    @classmethod
    def serviceListener(cls) -> Self:
        """Returns the singleton listener for the current XPC service."""
        ...

    @classmethod
    def anonymousListener(cls) -> Self:
        """Returns a new anonymous listener."""
        ...

    @property
    def delegate(self) -> NSObject | None:
        """The delegate object that decides whether to accept incoming connections."""
        ...

    @delegate.setter
    def delegate(self, delegate: objc_id | NSObject | None) -> None: ...
    @property
    def endpoint(self) -> NSXPCListenerEndpoint:
        """An endpoint that can be sent over an existing connection to allow clients to connect."""
        ...

    def activate(self) -> None:
        """Activates the listener."""
        ...

    def resume(self) -> None:
        """Starts processing incoming connection requests."""
        ...

    def invalidate(self) -> None:
        """Invalidates the listener."""
        ...

    def suspend(self) -> None:
        """Suspends the listener."""
        ...

    def setConnectionCodeSigningRequirement(
        self, requirement: NSString | str, /
    ) -> None:
        """Sets the code-signing requirement for connections accepted by this listener."""
        ...

class NSXPCListenerEndpoint(NSObject):
    """An endpoint object that identifies an NSXPCListener in another process."""

NSSecureCoding: ObjCProtocol
