from typed_rubicon_objc.Foundation import NSObject


def test_nsobject_creation():
    """Test basic NSObject instantiation."""
    obj = NSObject.alloc().init()
    assert obj is not None


def test_nsobject_hash():
    """Test hash method."""
    obj = NSObject.alloc().init()
    hash_value = obj.hash
    assert isinstance(hash_value, int)


def test_nsobject_equality():
    """Test isEqual method."""
    obj1 = NSObject.alloc().init()
    obj2 = NSObject.alloc().init()
    result = obj1.isEqual(obj2)
    assert isinstance(result, bool)


def test_nsobject_description():
    """Test description method."""
    obj = NSObject.alloc().init()
    desc = obj.description
    assert desc is not None


def test_nsobject_class():
    """Test class method."""
    obj = NSObject.alloc().init()
    cls = obj.__class__
    assert cls is not None


def test_nsobject_respondsToSelector():
    """Test respondsToSelector method."""
    obj = NSObject.alloc().init()
    result = obj.respondsToSelector("init")
    assert isinstance(result, bool)
