from rubicon.objc.runtime import objc_id
from typed_rubicon_objc.Foundation import NSArray, NSString

# NSNotFound constant - typically NSIntegerMax on 64-bit systems
NSNotFound = 9223372036854775807


def test_nsarray_ptr():
    """Test that the ptr property returns a pointer of the correct type."""
    array = NSArray.arrayWithObjects(["a", "b", "c"])
    ptr = array.ptr
    assert isinstance(ptr, objc_id)


def test_nsarray_array():
    """Test creating an empty array."""
    array = NSArray.array()
    assert array is not None
    assert len(array) == 0


def test_nsarray_arrayWithObject():
    """Test creating an array with a single object."""
    array = NSArray.arrayWithObject("test")
    assert array is not None
    assert len(array) == 1
    assert array[0] == "test"


def test_nsarray_arrayWithObjects():
    """Test creating an array with multiple objects."""
    array = NSArray.arrayWithObjects(["a", "b", "c"])
    assert array is not None
    assert len(array) == 3
    assert array[0] == "a"
    assert array[1] == "b"
    assert array[2] == "c"


def test_nsarray_arrayWithArray():
    """Test creating an array from another array."""
    original = NSArray.arrayWithObjects(["x", "y", "z"])
    copy = NSArray.arrayWithArray(original)
    assert copy is not None
    assert len(copy) == 3
    assert copy[0] == "x"


def test_nsarray_count():
    """Test the count property."""
    array = NSArray.arrayWithObjects(["one", "two", "three"])
    assert len(array) == 3


def test_nsarray_objectAtIndex():
    """Test accessing objects by index."""
    array = NSArray.arrayWithObjects(["first", "second", "third"])
    assert array.objectAtIndex(0) == "first"
    assert array.objectAtIndex(1) == "second"
    assert array.objectAtIndex(2) == "third"


def test_nsarray_firstObject():
    """Test the firstObject property."""
    array = NSArray.arrayWithObjects(["alpha", "beta", "gamma"])
    assert array.firstObject() == "alpha"


def test_nsarray_firstObject_empty():
    """Test the firstObject property on an empty array."""
    array = NSArray.array()
    assert array.firstObject() is None


def test_nsarray_lastObject():
    """Test the lastObject property."""
    array = NSArray.arrayWithObjects(["alpha", "beta", "gamma"])
    assert array.lastObject() == "gamma"


def test_nsarray_lastObject_empty():
    """Test the lastObject property on an empty array."""
    array = NSArray.array()
    assert array.lastObject() is None


def test_nsarray_containsObject():
    """Test checking if an array contains an object."""
    array = NSArray.arrayWithObjects(["apple", "banana", "cherry"])
    assert array.containsObject("banana") is True
    assert array.containsObject("grape") is False


def test_nsarray_indexOfObject():
    """Test finding the index of an object."""
    array = NSArray.arrayWithObjects(["red", "green", "blue"])
    assert array.indexOfObject("green") == 1
    assert array.indexOfObject("blue") == 2


def test_nsarray_indexOfObject_not_found():
    """Test finding the index of an object that doesn't exist."""
    array = NSArray.arrayWithObjects(["cat", "dog", "bird"])
    index = array.indexOfObject("fish")
    assert index == NSNotFound


def test_nsarray_indexOfObjectIdenticalTo():
    """Test finding the index of an identical object."""
    obj1 = NSString.stringWithString("test")
    obj2 = NSString.stringWithString("test")
    array = NSArray.arrayWithObjects([obj1, obj2])
    # Should find the first occurrence
    assert array.indexOfObjectIdenticalTo(obj1) == 0


def test_nsarray_arrayByAddingObject():
    """Test adding an object to create a new array."""
    original = NSArray.arrayWithObjects(["one", "two"])
    new_array = original.arrayByAddingObject("three")
    assert len(new_array) == 3
    assert new_array[2] == "three"
    # Original should be unchanged
    assert len(original) == 2


def test_nsarray_arrayByAddingObjectsFromArray():
    """Test adding objects from another array."""
    array1 = NSArray.arrayWithObjects(["a", "b"])
    array2 = NSArray.arrayWithObjects(["c", "d"])
    combined = array1.arrayByAddingObjectsFromArray(array2)
    assert len(combined) == 4
    assert combined[0] == "a"
    assert combined[3] == "d"


def test_nsarray_subarrayWithRange():
    """Test creating a subarray with a range."""
    array = NSArray.arrayWithObjects(["zero", "one", "two", "three", "four"])
    subarray = array.subarrayWithRange((1, 3))  # location=1, length=3
    assert len(subarray) == 3
    assert subarray[0] == "one"
    assert subarray[1] == "two"
    assert subarray[2] == "three"


def test_nsarray_componentsJoinedByString():
    """Test joining array elements with a string."""
    array = NSArray.arrayWithObjects(["hello", "world", "test"])
    result = array.componentsJoinedByString(", ")
    assert isinstance(result, NSString)
    assert str(result) == "hello, world, test"


def test_nsarray_getitem():
    """Test __getitem__ method for index access."""
    array = NSArray.arrayWithObjects(["x", "y", "z"])
    assert array[0] == "x"
    assert array[1] == "y"
    assert array[2] == "z"


def test_nsarray_len():
    """Test __len__ method."""
    array = NSArray.arrayWithObjects(["a", "b", "c", "d"])
    assert len(array) == 4


def test_nsarray_iter():
    """Test __iter__ method for iteration."""
    array = NSArray.arrayWithObjects(["one", "two", "three"])
    items = list(array)
    assert items == ["one", "two", "three"]


def test_nsarray_contains():
    """Test __contains__ method for 'in' operator."""
    array = NSArray.arrayWithObjects(["apple", "banana", "cherry"])
    assert "banana" in array
    assert "grape" not in array


def test_nsarray_with_nsstrings():
    """Test NSArray with NSString objects."""
    str1 = NSString.stringWithString("first")
    str2 = NSString.stringWithString("second")
    array = NSArray.arrayWithObjects([str1, str2])
    assert len(array) == 2
    assert isinstance(array[0], NSString)


def test_nsarray_sortedArrayHint():
    """Test sortedArrayHint property."""
    array = NSArray.arrayWithObjects(["a", "b", "c"])
    hint = array.sortedArrayHint()
    # Just verify it returns something - exact value is implementation-defined
    assert hint is not None
