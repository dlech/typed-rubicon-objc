import pytest
from rubicon.objc.api import ObjCClass, ObjCProtocol
from rubicon.objc.runtime import SEL, objc_id
from rubicon.objc.types import UnknownPointer
from typed_rubicon_objc.Foundation import NSMethodSignature, NSObject, NSString


def test_nsobject_ptr():
    """Test that the ptr property returns a pointer of the correct type."""
    obj = NSObject.new()
    ptr = obj.ptr
    assert isinstance(ptr, objc_id)


def test_nsobject_creation():
    """Test basic NSObject instantiation."""
    obj = NSObject.new()
    assert obj is not None


def test_nsobject_alloc():
    """Test alloc class method."""
    obj = NSObject.alloc()
    assert obj is not None


def test_nsobject_allocWithZone():
    """Test allocWithZone class method."""
    obj = NSObject.allocWithZone(None)
    assert obj is not None


def test_nsobject_init():
    """Test init instance method."""
    obj = NSObject.alloc()
    initialized = obj.init()
    assert initialized is not None


def test_nsobject_copy_property():
    """Test copy property."""
    obj = NSObject.new()
    copy_value = obj.copy
    assert copy_value is not None


def test_nsobject_copyWithZone():
    """Test copyWithZone class method."""
    copied = NSObject.copyWithZone(None)
    assert copied is not None


def test_nsobject_mutableCopy_property():
    """Test mutableCopy property."""
    obj = NSObject.new()
    copy_value = obj.mutableCopy
    assert copy_value is not None


def test_nsobject_mutableCopyWithZone():
    """Test mutableCopyWithZone class method."""
    copied = NSObject.mutableCopyWithZone(None)
    assert copied is not None


def test_nsobject_new():
    """Test new class method."""
    obj = NSObject.new()
    assert obj is not None


def test_nsobject_isSubclassOfClass():
    """Test isSubclassOfClass: class method."""
    result = NSObject.isSubclassOfClass(NSObject)
    assert isinstance(result, bool)
    assert result is True


def test_nsobject_instancesRespondToSelector():
    """Test instancesRespondToSelector: class method."""
    result = NSObject.instancesRespondToSelector(SEL("init"))
    assert isinstance(result, bool)
    assert result is True


def test_nsobject_instanceMethodForSelector():
    """Test instanceMethodForSelector: class method."""
    result = NSObject.instanceMethodForSelector(SEL("init"))
    assert isinstance(result, UnknownPointer)


def test_nsobject_instanceMethodSignatureForSelector():
    """Test instanceMethodSignatureForSelector: class method."""
    result = NSObject.instanceMethodSignatureForSelector(SEL("init"))
    assert result is not None


def test_nsobject_conformsToProtocol():
    """Test conformsToProtocol: class method."""
    protocol = ObjCProtocol("NSObject")
    if protocol is None:
        pytest.skip("NSObject protocol not available")
    result = NSObject.conformsToProtocol(protocol)
    assert isinstance(result, bool)


def test_nsobject_methodForSelector():
    """Test methodForSelector: instance method."""
    obj = NSObject.new()
    result = obj.methodForSelector(SEL("init"))
    assert isinstance(result, UnknownPointer)


def test_nsobject_methodSignatureForSelector():
    """Test methodSignatureForSelector: instance method."""
    obj = NSObject.new()
    result = obj.methodSignatureForSelector(SEL("init"))
    assert isinstance(result, NSMethodSignature)


def test_nsobject_forwardingTargetForSelector():
    """Test forwardingTargetForSelector: instance method."""
    obj = NSObject.new()
    result = obj.forwardingTargetForSelector(SEL("__no_such_selector__"))
    assert result is None


def test_nsobject_resolveClassMethod():
    """Test resolveClassMethod: class method."""
    result = NSObject.resolveClassMethod(SEL("init"))
    assert isinstance(result, bool)


def test_nsobject_resolveInstanceMethod():
    """Test resolveInstanceMethod: class method."""
    result = NSObject.resolveInstanceMethod(SEL("init"))
    assert isinstance(result, bool)


def test_nsobject_load():
    """Test load class method."""
    result = NSObject.load()
    assert result is None


def test_nsobject_initialize():
    """Test initialize class method."""
    result = NSObject.initialize()
    assert result is None


def test_nsobject_class_description():
    """Test class description class method."""
    result = NSObject.description
    assert isinstance(result, NSString)


def test_nsobject_hash():
    """Test hash method."""
    obj = NSObject.new()
    hash_value = obj.hash
    assert isinstance(hash_value, int)


def test_nsobject_class_method():
    """Test class instance method."""
    obj = NSObject.new()
    # class is keyword, so we can use dot notation to access the method or
    # have type hints
    cls = getattr(obj, "class")()
    assert isinstance(cls, type(NSObject))


def test_nsobject_superclass():
    """Test superclass class method."""
    superclass = NSObject.superclass
    assert superclass is None


def test_nsobject_equality():
    """Test isEqual method."""
    obj1 = NSObject.new()
    obj2 = NSObject.new()
    result = obj1.isEqual(obj2)
    assert isinstance(result, bool)


def test_nsobject_description():
    """Test description method."""
    obj = NSObject.new()
    desc = obj.description
    assert desc is not None


def test_nsobject_self_method():
    """Test self instance method."""
    obj = NSObject.new()
    result = obj.self()
    assert result is obj


def test_nsobject_isKindOfClass():
    """Test isKindOfClass: instance method."""
    obj = NSObject.new()
    result = obj.isKindOfClass(NSObject)
    assert isinstance(result, bool)


def test_nsobject_isMemberOfClass():
    """Test isMemberOfClass: instance method."""
    obj = NSObject.new()
    result = obj.isMemberOfClass(NSObject)
    assert isinstance(result, bool)
    assert result is True


def test_nsobject_respondsToSelector():
    """Test respondsToSelector: instance method."""
    obj = NSObject.new()
    result = obj.respondsToSelector(SEL("init"))
    assert isinstance(result, bool)
    assert result is True


def test_nsobject_debugDescription():
    """Test debugDescription property."""
    obj = NSObject.new()
    desc = obj.debugDescription
    assert isinstance(desc, NSString)


def test_nsobject_performSelector():
    """Test performSelector: instance method."""
    obj = NSObject.new()
    result = obj.performSelector(SEL("class"))
    assert isinstance(result, ObjCClass)


def test_nsobject_performSelector_withObject():
    """Test performSelector:withObject: instance method."""
    obj = NSObject.new()
    # Have to be careful with this one. The return value is `id`, so calling
    # a method that returns a primitive type (like `bool`) will cause a crash
    # because the return value will be interpreted as a pointer.
    result = obj.performSelector(SEL("inverseForRelationshipKey:"), withObject="key")
    assert result is None


# TODO: find a suitable method to test performSelector:withObject:withObject:

# def test_nsobject_performSelector_withObject_withObject():
#     """Test performSelector:withObject:withObject: instance method."""
#     obj = NSObject.new()
#     result = obj.performSelector(
#         SEL("setValue:forKey:"),
#         withObject__1="value",
#         withObject__2="key",
#     )
#     assert isinstance(result, bool)


def test_nsobject_isProxy():
    """Test isProxy instance method."""
    obj = NSObject.new()
    result = obj.isProxy()
    assert isinstance(result, bool)
