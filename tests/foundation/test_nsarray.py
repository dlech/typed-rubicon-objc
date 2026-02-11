from rubicon.objc.runtime import objc_id, send_message
from typed_rubicon_objc.Foundation import NSArray, NSData, NSInteger, NSString

# NSNotFound constant - typically NSIntegerMax on 64-bit systems
NSNotFound = 9223372036854775807


def test_nsarray_ptr():
    """Test that the ptr property returns a pointer of the correct type."""
    array = NSArray[NSString].arrayWithArray(["a", "b", "c"])
    ptr = array.ptr
    assert isinstance(ptr, objc_id)


def test_nsarray_array():
    """Test creating an empty array."""
    array = NSArray[NSString].array()
    assert array is not None
    assert len(array) == 0


def test_nsarray_arrayWithObject():
    """Test creating an array with a single object."""
    array = NSArray[NSString].arrayWithObject("test")
    assert array is not None
    assert len(array) == 1
    assert array[0] == "test"


def test_nsarray_arrayWithObjects():
    """Test creating an array with multiple objects."""
    array = NSArray[NSString].arrayWithArray(["a", "b", "c"])
    assert array is not None
    assert len(array) == 3
    assert array[0] == "a"
    assert array[1] == "b"
    assert array[2] == "c"


def test_nsarray_arrayWithArray():
    """Test creating an array from another array."""
    original = NSArray[NSString].arrayWithArray(["x", "y", "z"])
    copy = NSArray[NSString].arrayWithArray(original)
    assert copy is not None
    assert len(copy) == 3
    assert copy[0] == "x"


def test_nsarray_count():
    """Test the count property."""
    array = NSArray[NSString].arrayWithArray(["one", "two", "three"])
    # shadowed by Sequence.count() method
    assert send_message(array, "count", restype=NSInteger) == 3


def test_nsarray_objectAtIndex():
    """Test accessing objects by index."""
    array = NSArray[NSString].arrayWithArray(["first", "second", "third"])
    assert array.objectAtIndex(0) == "first"
    assert array.objectAtIndex(1) == "second"
    assert array.objectAtIndex(2) == "third"


def test_nsarray_firstObject():
    """Test the firstObject property."""
    array = NSArray[NSString].arrayWithArray(["alpha", "beta", "gamma"])
    assert array.firstObject() == "alpha"


def test_nsarray_firstObject_empty():
    """Test the firstObject property on an empty array."""
    array = NSArray[NSString].array()
    assert array.firstObject() is None


def test_nsarray_lastObject():
    """Test the lastObject property."""
    array = NSArray[NSString].arrayWithArray(["alpha", "beta", "gamma"])
    assert array.lastObject() == "gamma"


def test_nsarray_lastObject_empty():
    """Test the lastObject property on an empty array."""
    array = NSArray[NSString].array()
    assert array.lastObject() is None


def test_nsarray_containsObject():
    """Test checking if an array contains an object."""
    array = NSArray[NSString].arrayWithArray(["apple", "banana", "cherry"])
    assert array.containsObject("banana") is True
    assert array.containsObject("grape") is False


def test_nsarray_indexOfObject():
    """Test finding the index of an object."""
    array = NSArray[NSString].arrayWithArray(["red", "green", "blue"])
    assert array.indexOfObject("green") == 1
    assert array.indexOfObject("blue") == 2


def test_nsarray_indexOfObject_not_found():
    """Test finding the index of an object that doesn't exist."""
    array = NSArray[NSString].arrayWithArray(["cat", "dog", "bird"])
    index = array.indexOfObject("fish")
    assert index == NSNotFound


def test_nsarray_indexOfObjectIdenticalTo():
    """Test finding the index of an identical object."""
    obj1 = NSString.stringWithString("test")
    obj2 = NSString.stringWithString("test")
    array = NSArray[NSString].arrayWithArray([obj1, obj2])
    # Should find the first occurrence
    assert array.indexOfObjectIdenticalTo(obj1) == 0


def test_nsarray_arrayByAddingObject():
    """Test adding an object to create a new array."""
    original = NSArray[NSString].arrayWithArray(["one", "two"])
    new_array = original.arrayByAddingObject("three")
    assert len(new_array) == 3
    assert new_array[2] == "three"
    # Original should be unchanged
    assert len(original) == 2


def test_nsarray_arrayByAddingObjectsFromArray():
    """Test adding objects from another array."""
    array1 = NSArray[NSString].arrayWithArray(["a", "b"])
    array2 = NSArray[NSString].arrayWithArray(["c", "d"])
    combined = array1.arrayByAddingObjectsFromArray(array2)
    assert len(combined) == 4
    assert combined[0] == "a"
    assert combined[3] == "d"


def test_nsarray_subarrayWithRange():
    """Test creating a subarray with a range."""
    array = NSArray[NSString].arrayWithArray(["zero", "one", "two", "three", "four"])
    subarray = array.subarrayWithRange((1, 3))  # location=1, length=3
    assert len(subarray) == 3
    assert subarray[0] == "one"
    assert subarray[1] == "two"
    assert subarray[2] == "three"


def test_nsarray_componentsJoinedByString():
    """Test joining array elements with a string."""
    array = NSArray[NSString].arrayWithArray(["hello", "world", "test"])
    result = array.componentsJoinedByString(", ")
    assert isinstance(result, NSString)
    assert str(result) == "hello, world, test"


def test_nsarray_getitem():
    """Test __getitem__ method for index access."""
    array = NSArray[NSString].arrayWithArray(["x", "y", "z"])
    assert array[0] == "x"
    assert array[1] == "y"
    assert array[2] == "z"


def test_nsarray_len():
    """Test __len__ method."""
    array = NSArray[NSString].arrayWithArray(["a", "b", "c", "d"])
    assert len(array) == 4


def test_nsarray_iter():
    """Test __iter__ method for iteration."""
    array = NSArray[NSString].arrayWithArray(["one", "two", "three"])
    items = list(array)
    assert items == ["one", "two", "three"]


def test_nsarray_contains():
    """Test __contains__ method for 'in' operator."""
    array = NSArray[NSString].arrayWithArray(["apple", "banana", "cherry"])
    assert "banana" in array
    assert "grape" not in array


def test_nsarray_with_nsstrings():
    """Test NSArray with NSString objects."""
    str1 = NSString.stringWithString("first")
    str2 = NSString.stringWithString("second")
    array = NSArray[NSString].arrayWithArray([str1, str2])
    assert len(array) == 2
    assert isinstance(array[0], NSString)


def test_nsarray_sortedArrayHint():
    """Test sortedArrayHint property."""
    array = NSArray[NSString].arrayWithArray(["a", "b", "c"])
    hint = array.sortedArrayHint()
    # Just verify it returns something - exact value is implementation-defined
    assert isinstance(hint, NSData)


def test_nsarray_isEqualToArray():
    """Test comparing two arrays for equality."""
    array1 = NSArray[NSString].arrayWithArray(["a", "b", "c"])
    array2 = NSArray[NSString].arrayWithArray(["a", "b", "c"])
    array3 = NSArray[NSString].arrayWithArray(["x", "y", "z"])
    assert array1.isEqualToArray(array2) is True
    assert array1.isEqualToArray(array3) is False


def test_nsarray_firstObjectCommonWithArray():
    """Test finding the first common object between two arrays."""
    array1 = NSArray[NSString].arrayWithArray(["a", "b", "c"])
    array2 = NSArray[NSString].arrayWithArray(["x", "b", "z"])
    array3 = NSArray[NSString].arrayWithArray(["x", "y", "z"])
    common = array1.firstObjectCommonWithArray(array2)
    assert common == "b"
    # No common objects
    no_common = array1.firstObjectCommonWithArray(array3)
    assert no_common is None


def test_nsarray_sortedArrayUsingSelector():
    """Test sorting an array using a selector."""
    array = NSArray[NSString].arrayWithArray(["cherry", "apple", "banana"])
    # Use the compare: selector which is available on NSString
    from rubicon.objc import SEL
    sorted_array = array.sortedArrayUsingSelector(SEL("compare:"))
    assert len(sorted_array) == 3
    assert sorted_array[0] == "apple"
    assert sorted_array[1] == "banana"
    assert sorted_array[2] == "cherry"


def test_nsarray_indexOfObject_inRange():
    """Test finding the index of an object within a specific range."""
    array = NSArray[NSString].arrayWithArray(["a", "b", "c", "b", "d"])
    # Find "b" starting from index 2
    index = array.indexOfObject("b", inRange=(2, 3))  # location=2, length=3
    assert index == 3  # Should find the second "b"


def test_nsarray_indexOfObjectIdenticalTo_inRange():
    """Test finding the index of an identical object within a specific range."""
    obj1 = NSString.stringWithString("test")
    obj2 = NSString.stringWithString("other")
    obj3 = NSString.stringWithString("test")
    array = NSArray[NSString].arrayWithArray([obj1, obj2, obj3, obj2])
    # Find obj3 starting from index 2
    index = array.indexOfObjectIdenticalTo(obj3, inRange=(2, 2))  # location=2, length=2
    assert index == 2


def test_nsarray_objectsAtIndexes():
    """Test getting objects at specific indexes."""
    from rubicon.objc import NSIndexSet
    array = NSArray[NSString].arrayWithArray(["a", "b", "c", "d", "e"])
    # Create an index set with indexes 1, 3
    index_set = NSIndexSet.indexSetWithIndex(1)
    index_set = index_set.indexSetByAddingIndex(3)
    objects = array.objectsAtIndexes(index_set)
    assert len(objects) == 2
    assert objects[0] == "b"
    assert objects[1] == "d"


def test_nsarray_descriptionWithLocale():
    """Test getting a localized description of the array."""
    array = NSArray[NSString].arrayWithArray(["hello", "world"])
    description = array.descriptionWithLocale(None)
    assert isinstance(description, NSString)
    # Should contain the array contents in some form
    desc_str = str(description)
    assert "hello" in desc_str or "world" in desc_str


def test_nsarray_shuffledArray():
    """Test creating a shuffled copy of the array."""
    array = NSArray[NSString].arrayWithArray(["a", "b", "c", "d", "e"])
    shuffled = array.shuffledArray()
    # Should have same length
    assert len(shuffled) == 5
    # Should contain all same elements (though order may differ)
    for item in array:
        assert item in shuffled


def test_nsarray_getitem_slice():
    """Test __getitem__ with slice notation."""
    array = NSArray[NSString].arrayWithArray(["a", "b", "c", "d", "e"])
    # Test basic slicing
    subarray = array[1:3]
    assert len(subarray) == 2
    assert subarray[0] == "b"
    assert subarray[1] == "c"
