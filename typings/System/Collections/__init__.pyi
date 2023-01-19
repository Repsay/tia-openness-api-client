# encoding: utf-8
# module System.Collections calls itself Collections
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
# no doc
# no imports

# no functions
# classes

from typing import Generic, Iterator, TypeVar

from System import ICloneable

from System.Runtime.Serialization import IDeserializationCallback, ISerializable

U = TypeVar("U")

class ArrayList(IList, ICloneable):  # skipped bases: <type 'ICollection'>, <type 'IEnumerable'>
    """
    Implements the System.Collections.IList interface using an array whose size is dynamically increased as required.To browse the .NET Framework source code for this type, see the Reference Source.

    ArrayList()

    ArrayList(capacity: int)

    ArrayList(c: ICollection)
    """

    @staticmethod
    def Adapter(list):
        """
        Adapter(list: IList) -> ArrayList

            Creates an System.Collections.ArrayList wrapper for a specific System.Collections.IList.

            list: The System.Collections.IList to wrap.

            Returns: The System.Collections.ArrayList wrapper around the System.Collections.IList.
        """
        ...
    def AddRange(self, c):
        """
        AddRange(self: ArrayList, c: ICollection)

            Adds the elements of an System.Collections.ICollection to the end of the System.Collections.ArrayList.

            c: The System.Collections.ICollection whose elements should be added to the end of the System.Collections.ArrayList. The collection itself cannot be ll, but it can contain elements that are ll.
        """
        ...
    def BinarySearch(self, *__args):
        """
        BinarySearch(self: ArrayList, index: int, count: int, value: object, comparer: IComparer) -> int

            Searches a range of elements in the sorted System.Collections.ArrayList for an element using the specified comparer and returns the zero-based index of the element.

            index: The zero-based starting index of the range to search.

            count: The length of the range to search.

            value: The System.Object to locate. The value can be ll.

            comparer: The System.Collections.IComparer implementation to use when comparing elements.-or-

                    ll to use the default comparer that is the System.IComparable implementation of each element.

            Returns: The zero-based index of value in the sorted System.Collections.ArrayList, if value is found; otherwise, a negative number, which is the bitwise complement of the index of the next element that is larger than value or, if there is no

             larger element, the bitwise complement of System.Collections.ArrayList.Count.

        BinarySearch(self: ArrayList, value: object) -> int

            Searches the entire sorted System.Collections.ArrayList for an element using the default comparer and returns the zero-based index of the element.

            value: The System.Object to locate. The value can be ll.

            Returns: The zero-based index of value in the sorted System.Collections.ArrayList, if value is found; otherwise, a negative number, which is the bitwise complement of the index of the next element that is larger than value or, if there is no

             larger element, the bitwise complement of System.Collections.ArrayList.Count.

        BinarySearch(self: ArrayList, value: object, comparer: IComparer) -> int

            Searches the entire sorted System.Collections.ArrayList for an element using the specified comparer and returns the zero-based index of the element.

            value: The System.Object to locate. The value can be ll.

            comparer: The System.Collections.IComparer implementation to use when comparing elements.-or-

                    ll to use the default comparer that is the System.IComparable implementation of each element.

            Returns: The zero-based index of value in the sorted System.Collections.ArrayList, if value is found; otherwise, a negative number, which is the bitwise complement of the index of the next element that is larger than value or, if there is no

             larger element, the bitwise complement of System.Collections.ArrayList.Count.
        """
        ...
    def CopyTo(self, *__args):
        """
        CopyTo(self: ArrayList, array: Array)

            Copies the entire System.Collections.ArrayList to a compatible one-dimensional System.Array, starting at the beginning of the target array.

            array: The one-dimensional System.Array that is the destination of the elements copied from System.Collections.ArrayList. The System.Array must have zero-based indexing.

        CopyTo(self: ArrayList, array: Array, arrayIndex: int)

            Copies the entire System.Collections.ArrayList to a compatible one-dimensional System.Array, starting at the specified index of the target array.

            array: The one-dimensional System.Array that is the destination of the elements copied from System.Collections.ArrayList. The System.Array must have zero-based indexing.

            arrayIndex: The zero-based index in array at which copying begins.

        CopyTo(self: ArrayList, index: int, array: Array, arrayIndex: int, count: int)

            Copies a range of elements from the System.Collections.ArrayList to a compatible one-dimensional System.Array, starting at the specified index of the target array.

            index: The zero-based index in the source System.Collections.ArrayList at which copying begins.

            array: The one-dimensional System.Array that is the destination of the elements copied from System.Collections.ArrayList. The System.Array must have zero-based indexing.

            arrayIndex: The zero-based index in array at which copying begins.

            count: The number of elements to copy.
        """
        ...
    @staticmethod
    def FixedSize(list):
        """
        FixedSize(list: IList) -> IList

            Returns an System.Collections.IList wrapper with a fixed size.

            list: The System.Collections.IList to wrap.

            Returns: An System.Collections.IList wrapper with a fixed size.

        FixedSize(list: ArrayList) -> ArrayList

            Returns an System.Collections.ArrayList wrapper with a fixed size.

            list: The System.Collections.ArrayList to wrap.

            Returns: An System.Collections.ArrayList wrapper with a fixed size.
        """
        ...
    def GetEnumerator(self, index=None, count=None):
        """
        GetEnumerator(self: ArrayList) -> IEnumerator

            Returns an enumerator for the entire System.Collections.ArrayList.

            Returns: An System.Collections.IEnumerator for the entire System.Collections.ArrayList.

        GetEnumerator(self: ArrayList, index: int, count: int) -> IEnumerator

            Returns an enumerator for a range of elements in the System.Collections.ArrayList.

            index: The zero-based starting index of the System.Collections.ArrayList section that the enumerator should refer to.

            count: The number of elements in the System.Collections.ArrayList section that the enumerator should refer to.

            Returns: An System.Collections.IEnumerator for the specified range of elements in the System.Collections.ArrayList.
        """
        ...
    def GetRange(self, index, count):
        """
        GetRange(self: ArrayList, index: int, count: int) -> ArrayList

            Returns an System.Collections.ArrayList which represents a subset of the elements in the source System.Collections.ArrayList.

            index: The zero-based System.Collections.ArrayList index at which the range starts.

            count: The number of elements in the range.

            Returns: An System.Collections.ArrayList which represents a subset of the elements in the source System.Collections.ArrayList.
        """
        ...
    def InsertRange(self, index, c):
        """
        InsertRange(self: ArrayList, index: int, c: ICollection)

            Inserts the elements of a collection into the System.Collections.ArrayList at the specified index.

            index: The zero-based index at which the new elements should be inserted.

            c: The System.Collections.ICollection whose elements should be inserted into the System.Collections.ArrayList. The collection itself cannot be ll, but it can contain elements that are ll.
        """
        ...
    def LastIndexOf(self, value, startIndex=None, count=None):
        """
        LastIndexOf(self: ArrayList, value: object) -> int

            Searches for the specified System.Object and returns the zero-based index of the last occurrence within the entire System.Collections.ArrayList.

            value: The System.Object to locate in the System.Collections.ArrayList. The value can be ll.

            Returns: The zero-based index of the last occurrence of value within the entire the System.Collections.ArrayList, if found; otherwise, -1.

        LastIndexOf(self: ArrayList, value: object, startIndex: int) -> int

            Searches for the specified System.Object and returns the zero-based index of the last occurrence within the range of elements in the System.Collections.ArrayList that extends from the first element to the specified index.

            value: The System.Object to locate in the System.Collections.ArrayList. The value can be ll.

            startIndex: The zero-based starting index of the backward search.

            Returns: The zero-based index of the last occurrence of value within the range of elements in the System.Collections.ArrayList that extends from the first element to startIndex, if found; otherwise, -1.

        LastIndexOf(self: ArrayList, value: object, startIndex: int, count: int) -> int

            Searches for the specified System.Object and returns the zero-based index of the last occurrence within the range of elements in the System.Collections.ArrayList that contains the specified number of elements and ends at the

             specified index.

            value: The System.Object to locate in the System.Collections.ArrayList. The value can be ll.

            startIndex: The zero-based starting index of the backward search.

            count: The number of elements in the section to search.

            Returns: The zero-based index of the last occurrence of value within the range of elements in the System.Collections.ArrayList that contains count number of elements and ends at startIndex, if found; otherwise, -1.
        """
        ...
    @staticmethod
    def ReadOnly(list):
        """
        ReadOnly(list: IList) -> IList

            Returns a read-only System.Collections.IList wrapper.

            list: The System.Collections.IList to wrap.

            Returns: A read-only System.Collections.IList wrapper around list.

        ReadOnly(list: ArrayList) -> ArrayList

            Returns a read-only System.Collections.ArrayList wrapper.

            list: The System.Collections.ArrayList to wrap.

            Returns: A read-only System.Collections.ArrayList wrapper around list.
        """
        ...
    def RemoveRange(self, index, count):
        """
        RemoveRange(self: ArrayList, index: int, count: int)

            Removes a range of elements from the System.Collections.ArrayList.

            index: The zero-based starting index of the range of elements to remove.

            count: The number of elements to remove.
        """
        ...
    @staticmethod
    def Repeat(value, count):
        """
        Repeat(value: object, count: int) -> ArrayList

            Returns an System.Collections.ArrayList whose elements are copies of the specified value.

            value: The System.Object to copy multiple times in the new System.Collections.ArrayList. The value can be ll.

            count: The number of times value should be copied.

            Returns: An System.Collections.ArrayList with count number of elements, all of which are copies of value.
        """
        ...
    def Reverse(self, index=None, count=None):
        """
        Reverse(self: ArrayList)

            Reverses the order of the elements in the entire System.Collections.ArrayList.

        Reverse(self: ArrayList, index: int, count: int)

            Reverses the order of the elements in the specified range.

            index: The zero-based starting index of the range to reverse.

            count: The number of elements in the range to reverse.
        """
        ...
    def SetRange(self, index, c):
        """
        SetRange(self: ArrayList, index: int, c: ICollection)

            Copies the elements of a collection over a range of elements in the System.Collections.ArrayList.

            index: The zero-based System.Collections.ArrayList index at which to start copying the elements of c.

            c: The System.Collections.ICollection whose elements to copy to the System.Collections.ArrayList. The collection itself cannot be ll, but it can contain elements that are ll.
        """
        ...
    def Sort(self, *__args):
        """
        Sort(self: ArrayList)

            Sorts the elements in the entire System.Collections.ArrayList.

        Sort(self: ArrayList, comparer: IComparer)

            Sorts the elements in the entire System.Collections.ArrayList using the specified comparer.

            comparer: The System.Collections.IComparer implementation to use when comparing elements.-or- A null reference (thing in Visual Basic) to use the System.IComparable implementation of each element.

        Sort(self: ArrayList, index: int, count: int, comparer: IComparer)

            Sorts the elements in a range of elements in System.Collections.ArrayList using the specified comparer.

            index: The zero-based starting index of the range to sort.

            count: The length of the range to sort.

            comparer: The System.Collections.IComparer implementation to use when comparing elements.-or- A null reference (thing in Visual Basic) to use the System.IComparable implementation of each element.
        """
        ...
    @staticmethod
    def Synchronized(list):
        """
        Synchronized(list: IList) -> IList

            Returns an System.Collections.IList wrapper that is synchronized (thread safe).

            list: The System.Collections.IList to synchronize.

            Returns: An System.Collections.IList wrapper that is synchronized (thread safe).

        Synchronized(list: ArrayList) -> ArrayList

            Returns an System.Collections.ArrayList wrapper that is synchronized (thread safe).

            list: The System.Collections.ArrayList to synchronize.

            Returns: An System.Collections.ArrayList wrapper that is synchronized (thread safe).
        """
        ...
    def ToArray(self, type=None):
        """
        ToArray(self: ArrayList) -> Array[object]

            Copies the elements of the System.Collections.ArrayList to a new System.Object array.

            Returns: An System.Object array containing copies of the elements of the System.Collections.ArrayList.

        ToArray(self: ArrayList, type: Type) -> Array

            Copies the elements of the System.Collections.ArrayList to a new array of the specified element type.

            type: The element System.Type of the destination array to create and copy elements to.

            Returns: An array of the specified element type containing copies of the elements of the System.Collections.ArrayList.
        """
        ...
    def TrimToSize(self):
        """
        TrimToSize(self: ArrayList)

            Sets the capacity to the actual number of elements in the System.Collections.ArrayList.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """
        __contains__(self: IList, value: object) -> bool

            Determines whether the System.Collections.IList contains a specific value.

            value: The object to locate in the System.Collections.IList.

            Returns: ue if the System.Object is found in the System.Collections.IList; otherwise, lse.
        """
        ...
    @property
    def Capacity(self):
        """
        Gets or sets the number of elements that the System.Collections.ArrayList can contain.

        Get: Capacity(self: ArrayList) -> int

        Set: Capacity(self: ArrayList) = value
        """
        ...
    @property
    def Count(self):
        """
        Gets the number of elements actually contained in the System.Collections.ArrayList.

        Get: Count(self: ArrayList) -> int
        """
        ...
    @property
    def IsFixedSize(self):
        """
        Gets a value indicating whether the System.Collections.ArrayList has a fixed size.

        Get: IsFixedSize(self: ArrayList) -> bool
        """
        ...
    @property
    def IsReadOnly(self):
        """
        Gets a value indicating whether the System.Collections.ArrayList is read-only.

        Get: IsReadOnly(self: ArrayList) -> bool
        """
        ...
    @property
    def IsSynchronized(self):
        """
        Gets a value indicating whether access to the System.Collections.ArrayList is synchronized (thread safe).

        Get: IsSynchronized(self: ArrayList) -> bool
        """
        ...
    @property
    def SyncRoot(self):
        """
        Gets an object that can be used to synchronize access to the System.Collections.ArrayList.

        Get: SyncRoot(self: ArrayList) -> object
        """
        ...

class BitArray(ICollection, ICloneable):  # skipped bases: <type 'IEnumerable'>
    """
    Manages a compact array of bit values, which are represented as Booleans, where ue indicates that the bit is on (1) and lse indicates the bit is off (0).

    BitArray(length: int)

    BitArray(length: int, defaultValue: bool)

    BitArray(bytes: Array[Byte])

    BitArray(values: Array[bool])

    BitArray(values: Array[int])

    BitArray(bits: BitArray)
    """

    def And(self, value):
        """
        And(self: BitArray, value: BitArray) -> BitArray

            Performs the bitwise AND operation between the elements of the current System.Collections.BitArray object and the corresponding elements in the specified array. The current System.Collections.BitArray object will be modified to

             store the result of the bitwise AND operation.

            value: The array with which to perform the bitwise AND operation.

            Returns: An array containing the result of the bitwise AND operation, which is a reference to the current System.Collections.BitArray object.
        """
        ...
    def Get(self, index):
        """
        Get(self: BitArray, index: int) -> bool

            Gets the value of the bit at a specific position in the System.Collections.BitArray.

            index: The zero-based index of the value to get.

            Returns: The value of the bit at position index.
        """
        ...
    def GetEnumerator(self):
        """
        GetEnumerator(self: BitArray) -> IEnumerator

            Returns an enumerator that iterates through the System.Collections.BitArray.

            Returns: An System.Collections.IEnumerator for the entire System.Collections.BitArray.
        """
        ...
    def Not(self):
        """
        Not(self: BitArray) -> BitArray

            Inverts all the bit values in the current System.Collections.BitArray, so that elements set to ue are changed to lse, and elements set to lse are changed to ue.

            Returns: The current instance with inverted bit values.
        """
        ...
    def Or(self, value):
        """
        Or(self: BitArray, value: BitArray) -> BitArray

            Performs the bitwise OR operation between the elements of the current System.Collections.BitArray object and the corresponding elements in the specified array. The current System.Collections.BitArray object will be modified to store

             the result of the bitwise OR operation.

            value: The array with which to perform the bitwise OR operation.

            Returns: An array containing the result of the bitwise OR operation, which is a reference to the current System.Collections.BitArray object.
        """
        ...
    def Set(self, index, value):
        """
        Set(self: BitArray, index: int, value: bool)

            Sets the bit at a specific position in the System.Collections.BitArray to the specified value.

            index: The zero-based index of the bit to set.

            value: The Boolean value to assign to the bit.
        """
        ...
    def SetAll(self, value):
        """
        SetAll(self: BitArray, value: bool)

            Sets all bits in the System.Collections.BitArray to the specified value.

            value: The Boolean value to assign to all bits.
        """
        ...
    def Xor(self, value):
        """
        Xor(self: BitArray, value: BitArray) -> BitArray

            Performs the bitwise exclusive OR operation between the elements of the current System.Collections.BitArray object against the corresponding elements in the specified array. The current System.Collections.BitArray object will be

             modified to store the result of the bitwise exclusive OR operation.

            value: The array with which to perform the bitwise exclusive OR operation.

            Returns: An array containing the result of the bitwise exclusive OR operation, which is a reference to the current System.Collections.BitArray object.
        """
        ...
    def __getitem__(self, *args):  # cannot find CLR method
        """x.__getitem__(y) <==> x[y]"""
        ...
    def __len__(self, *args):  # cannot find CLR method
        """x.__len__() <==> len(x)"""
        ...
    def __setitem__(self, *args):  # cannot find CLR method
        """x.__setitem__(i, y) <==> x[i]="""
        ...
    @property
    def Count(self):
        """
        Gets the number of elements contained in the System.Collections.BitArray.

        Get: Count(self: BitArray) -> int
        """
        ...
    @property
    def IsReadOnly(self):
        """
        Gets a value indicating whether the System.Collections.BitArray is read-only.

        Get: IsReadOnly(self: BitArray) -> bool
        """
        ...
    @property
    def IsSynchronized(self):
        """
        Gets a value indicating whether access to the System.Collections.BitArray is synchronized (thread safe).

        Get: IsSynchronized(self: BitArray) -> bool
        """
        ...
    @property
    def Length(self):
        """
        Gets or sets the number of elements in the System.Collections.BitArray.

        Get: Length(self: BitArray) -> int

        Set: Length(self: BitArray) = value
        """
        ...
    @property
    def SyncRoot(self):
        """
        Gets an object that can be used to synchronize access to the System.Collections.BitArray.

        Get: SyncRoot(self: BitArray) -> object
        """
        ...

class CaseInsensitiveComparer(IComparer):
    """
    Compares two objects for equivalence, ignoring the case of strings.

    CaseInsensitiveComparer()

    CaseInsensitiveComparer(culture: CultureInfo)
    """

    Default = None
    DefaultInvariant = None

class CaseInsensitiveHashCodeProvider(IHashCodeProvider):
    """
    Supplies a hash code for an object, using a hashing algorithm that ignores the case of strings.

    CaseInsensitiveHashCodeProvider()

    CaseInsensitiveHashCodeProvider(culture: CultureInfo)
    """

    Default = None
    DefaultInvariant = None

class IEnumerable(Generic[U]):
    """Exposes an enumerator, which supports a simple iteration over a non-generic collection.To browse the .NET Framework source code for this type, see the Reference Source."""

    def GetEnumerator(self) -> IEnumerator[U]:
        """
        GetEnumerator(self: IEnumerable) -> IEnumerator

            Returns an enumerator that iterates through a collection.

            Returns: An System.Collections.IEnumerator object that can be used to iterate through the collection.
        """
        ...
    def __iter__(self) -> Iterator[U]:
        """__iter__(self: IEnumerable) -> object"""
        ...

class ICollection(IEnumerable):
    """Defines size, enumerators, and synchronization methods for all nongeneric collections."""

    def CopyTo(self, array, index):
        """
        CopyTo(self: ICollection, array: Array, index: int)

            Copies the elements of the System.Collections.ICollection to an System.Array, starting at a particular System.Array index.

            array: The one-dimensional System.Array that is the destination of the elements copied from System.Collections.ICollection. The System.Array must have zero-based indexing.

            index: The zero-based index in array at which copying begins.
        """
        ...
    @property
    def Count(self):
        """
        Gets the number of elements contained in the System.Collections.ICollection.

        Get: Count(self: ICollection) -> int
        """
        ...
    @property
    def IsSynchronized(self):
        """
        Gets a value indicating whether access to the System.Collections.ICollection is synchronized (thread safe).

        Get: IsSynchronized(self: ICollection) -> bool
        """
        ...
    @property
    def SyncRoot(self):
        """
        Gets an object that can be used to synchronize access to the System.Collections.ICollection.

        Get: SyncRoot(self: ICollection) -> object
        """
        ...

class IList(ICollection):  # skipped bases: <type 'IEnumerable'>
    """Represents a non-generic collection of objects that can be individually accessed by index."""

    def Add(self, value):
        """
        Add(self: IList, value: object) -> int

            Adds an item to the System.Collections.IList.

            value: The object to add to the System.Collections.IList.

            Returns: The position into which the new element was inserted, or -1 to indicate that the item was not inserted into the collection.
        """
        ...
    def Clear(self):
        """
        Clear(self: IList)

            Removes all items from the System.Collections.IList.
        """
        ...
    def Contains(self, value):
        """
        __contains__(self: IList, value: object) -> bool

            Determines whether the System.Collections.IList contains a specific value.

            value: The object to locate in the System.Collections.IList.

            Returns: ue if the System.Object is found in the System.Collections.IList; otherwise, lse.
        """
        ...
    def IndexOf(self, value):
        """
        IndexOf(self: IList, value: object) -> int

            Determines the index of a specific item in the System.Collections.IList.

            value: The object to locate in the System.Collections.IList.

            Returns: The index of value if found in the list; otherwise, -1.
        """
        ...
    def Insert(self, index, value):
        """
        Insert(self: IList, index: int, value: object)

            Inserts an item to the System.Collections.IList at the specified index.

            index: The zero-based index at which value should be inserted.

            value: The object to insert into the System.Collections.IList.
        """
        ...
    def Remove(self, value):
        """
        Remove(self: IList, value: object)

            Removes the first occurrence of a specific object from the System.Collections.IList.

            value: The object to remove from the System.Collections.IList.
        """
        ...
    def RemoveAt(self, index):
        """
        RemoveAt(self: IList, index: int)

            Removes the System.Collections.IList item at the specified index.

            index: The zero-based index of the item to remove.
        """
        ...
    def __add__(self, *args):  # cannot find CLR method
        """x.__add__(y) <==> x+y"""
        ...
    def __getitem__(self, *args):  # cannot find CLR method
        """x.__getitem__(y) <==> x[y]"""
        ...
    def __len__(self, *args):  # cannot find CLR method
        """x.__len__() <==> len(x)"""
        ...
    def __setitem__(self, *args):  # cannot find CLR method
        """x.__setitem__(i, y) <==> x[i]="""
        ...
    @property
    def IsFixedSize(self):
        """
        Gets a value indicating whether the System.Collections.IList has a fixed size.

        Get: IsFixedSize(self: IList) -> bool
        """
        ...
    @property
    def IsReadOnly(self):
        """
        Gets a value indicating whether the System.Collections.IList is read-only.

        Get: IsReadOnly(self: IList) -> bool
        """
        ...

class CollectionBase(IList):  # skipped bases: <type 'ICollection'>, <type 'IEnumerable'>
    """Provides the stract base class for a strongly typed collection."""

    def GetEnumerator(self):
        """
        GetEnumerator(self: CollectionBase) -> IEnumerator

            Returns an enumerator that iterates through the System.Collections.CollectionBase instance.

            Returns: An System.Collections.IEnumerator for the System.Collections.CollectionBase instance.
        """
        ...
    def OnClear(self, *args):  # cannot find CLR method
        """
        OnClear(self: CollectionBase)

            Performs additional custom processes when clearing the contents of the System.Collections.CollectionBase instance.
        """
        ...
    def OnClearComplete(self, *args):  # cannot find CLR method
        """
        OnClearComplete(self: CollectionBase)

            Performs additional custom processes after clearing the contents of the System.Collections.CollectionBase instance.
        """
        ...
    def OnInsert(self, *args):  # cannot find CLR method
        """
        OnInsert(self: CollectionBase, index: int, value: object)

            Performs additional custom processes before inserting a new element into the System.Collections.CollectionBase instance.

            index: The zero-based index at which to insert value.

            value: The new value of the element at index.
        """
        ...
    def OnInsertComplete(self, *args):  # cannot find CLR method
        """
        OnInsertComplete(self: CollectionBase, index: int, value: object)

            Performs additional custom processes after inserting a new element into the System.Collections.CollectionBase instance.

            index: The zero-based index at which to insert value.

            value: The new value of the element at index.
        """
        ...
    def OnRemove(self, *args):  # cannot find CLR method
        """
        OnRemove(self: CollectionBase, index: int, value: object)

            Performs additional custom processes when removing an element from the System.Collections.CollectionBase instance.

            index: The zero-based index at which value can be found.

            value: The value of the element to remove from index.
        """
        ...
    def OnRemoveComplete(self, *args):  # cannot find CLR method
        """
        OnRemoveComplete(self: CollectionBase, index: int, value: object)

            Performs additional custom processes after removing an element from the System.Collections.CollectionBase instance.

            index: The zero-based index at which value can be found.

            value: The value of the element to remove from index.
        """
        ...
    def OnSet(self, *args):  # cannot find CLR method
        """
        OnSet(self: CollectionBase, index: int, oldValue: object, newValue: object)

            Performs additional custom processes before setting a value in the System.Collections.CollectionBase instance.

            index: The zero-based index at which oldValue can be found.

            oldValue: The value to replace with newValue.

            newValue: The new value of the element at index.
        """
        ...
    def OnSetComplete(self, *args):  # cannot find CLR method
        """
        OnSetComplete(self: CollectionBase, index: int, oldValue: object, newValue: object)

            Performs additional custom processes after setting a value in the System.Collections.CollectionBase instance.

            index: The zero-based index at which oldValue can be found.

            oldValue: The value to replace with newValue.

            newValue: The new value of the element at index.
        """
        ...
    def OnValidate(self, *args):  # cannot find CLR method
        """
        OnValidate(self: CollectionBase, value: object)

            Performs additional custom processes when validating a value.

            value: The object to validate.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """
        __contains__(self: IList, value: object) -> bool

            Determines whether the System.Collections.IList contains a specific value.

            value: The object to locate in the System.Collections.IList.

            Returns: ue if the System.Object is found in the System.Collections.IList; otherwise, lse.
        """
        ...
    @property
    def Capacity(self):
        """
        Gets or sets the number of elements that the System.Collections.CollectionBase can contain.

        Get: Capacity(self: CollectionBase) -> int

        Set: Capacity(self: CollectionBase) = value
        """
        ...
    @property
    def Count(self):
        """
        Gets the number of elements contained in the System.Collections.CollectionBase instance. This property cannot be overridden.

        Get: Count(self: CollectionBase) -> int
        """
        ...
    @property
    def InnerList(self):
        """Gets an System.Collections.ArrayList containing the list of elements in the System.Collections.CollectionBase instance."""
        ...
    @property
    def List(self):
        """Gets an System.Collections.IList containing the list of elements in the System.Collections.CollectionBase instance."""
        ...

class Comparer(IComparer, ISerializable):
    """
    Compares two objects for equivalence, where string comparisons are case-sensitive.

    Comparer(culture: CultureInfo)
    """

    Default = None
    DefaultInvariant = None

class IDictionary(ICollection):  # skipped bases: <type 'IEnumerable'>
    """Represents a nongeneric collection of key/value pairs."""

    def Add(self, key, value):
        """
        Add(self: IDictionary, key: object, value: object)

            Adds an element with the provided key and value to the System.Collections.IDictionary object.

            key: The System.Object to use as the key of the element to add.

            value: The System.Object to use as the value of the element to add.
        """
        ...
    def Clear(self):
        """
        Clear(self: IDictionary)

            Removes all elements from the System.Collections.IDictionary object.
        """
        ...
    def Contains(self, key):
        """
        Contains(self: IDictionary, key: object) -> bool

            Determines whether the System.Collections.IDictionary object contains an element with the specified key.

            key: The key to locate in the System.Collections.IDictionary object.

            Returns: ue if the System.Collections.IDictionary contains an element with the key; otherwise, lse.
        """
        ...
    def GetEnumerator(self):
        """
        GetEnumerator(self: IDictionary) -> IDictionaryEnumerator

            Returns an System.Collections.IDictionaryEnumerator object for the System.Collections.IDictionary object.

            Returns: An System.Collections.IDictionaryEnumerator object for the System.Collections.IDictionary object.
        """
        ...
    def Remove(self, key):
        """
        Remove(self: IDictionary, key: object)

            Removes the element with the specified key from the System.Collections.IDictionary object.

            key: The key of the element to remove.
        """
        ...
    def __add__(self, *args):  # cannot find CLR method
        """x.__add__(y) <==> x+y"""
        ...
    def __getitem__(self, *args):  # cannot find CLR method
        """x.__getitem__(y) <==> x[y]"""
        ...
    def __len__(self, *args):  # cannot find CLR method
        """x.__len__() <==> len(x)"""
        ...
    def __setitem__(self, *args):  # cannot find CLR method
        """x.__setitem__(i, y) <==> x[i]="""
        ...
    @property
    def IsFixedSize(self):
        """
        Gets a value indicating whether the System.Collections.IDictionary object has a fixed size.

        Get: IsFixedSize(self: IDictionary) -> bool
        """
        ...
    @property
    def IsReadOnly(self):
        """
        Gets a value indicating whether the System.Collections.IDictionary object is read-only.

        Get: IsReadOnly(self: IDictionary) -> bool
        """
        ...
    @property
    def Keys(self):
        """
        Gets an System.Collections.ICollection object containing the keys of the System.Collections.IDictionary object.

        Get: Keys(self: IDictionary) -> ICollection
        """
        ...
    @property
    def Values(self):
        """
        Gets an System.Collections.ICollection object containing the values in the System.Collections.IDictionary object.

        Get: Values(self: IDictionary) -> ICollection
        """
        ...

class DictionaryBase(IDictionary):  # skipped bases: <type 'ICollection'>, <type 'IEnumerable'>
    """Provides the stract base class for a strongly typed collection of key/value pairs."""

    def CopyTo(self, array, index):
        """
        CopyTo(self: DictionaryBase, array: Array, index: int)

            Copies the System.Collections.DictionaryBase elements to a one-dimensional System.Array at the specified index.

            array: The one-dimensional System.Array that is the destination of the System.Collections.DictionaryEntry objects copied from the System.Collections.DictionaryBase instance. The System.Array must have zero-based indexing.

            index: The zero-based index in array at which copying begins.
        """
        ...
    def OnClear(self, *args):  # cannot find CLR method
        """
        OnClear(self: DictionaryBase)

            Performs additional custom processes before clearing the contents of the System.Collections.DictionaryBase instance.
        """
        ...
    def OnClearComplete(self, *args):  # cannot find CLR method
        """
        OnClearComplete(self: DictionaryBase)

            Performs additional custom processes after clearing the contents of the System.Collections.DictionaryBase instance.
        """
        ...
    def OnGet(self, *args):  # cannot find CLR method
        """
        OnGet(self: DictionaryBase, key: object, currentValue: object) -> object

            Gets the element with the specified key and value in the System.Collections.DictionaryBase instance.

            key: The key of the element to get.

            currentValue: The current value of the element associated with key.

            Returns: An System.Object containing the element with the specified key and value.
        """
        ...
    def OnInsert(self, *args):  # cannot find CLR method
        """
        OnInsert(self: DictionaryBase, key: object, value: object)

            Performs additional custom processes before inserting a new element into the System.Collections.DictionaryBase instance.

            key: The key of the element to insert.

            value: The value of the element to insert.
        """
        ...
    def OnInsertComplete(self, *args):  # cannot find CLR method
        """
        OnInsertComplete(self: DictionaryBase, key: object, value: object)

            Performs additional custom processes after inserting a new element into the System.Collections.DictionaryBase instance.

            key: The key of the element to insert.

            value: The value of the element to insert.
        """
        ...
    def OnRemove(self, *args):  # cannot find CLR method
        """
        OnRemove(self: DictionaryBase, key: object, value: object)

            Performs additional custom processes before removing an element from the System.Collections.DictionaryBase instance.

            key: The key of the element to remove.

            value: The value of the element to remove.
        """
        ...
    def OnRemoveComplete(self, *args):  # cannot find CLR method
        """
        OnRemoveComplete(self: DictionaryBase, key: object, value: object)

            Performs additional custom processes after removing an element from the System.Collections.DictionaryBase instance.

            key: The key of the element to remove.

            value: The value of the element to remove.
        """
        ...
    def OnSet(self, *args):  # cannot find CLR method
        """
        OnSet(self: DictionaryBase, key: object, oldValue: object, newValue: object)

            Performs additional custom processes before setting a value in the System.Collections.DictionaryBase instance.

            key: The key of the element to locate.

            oldValue: The old value of the element associated with key.

            newValue: The new value of the element associated with key.
        """
        ...
    def OnSetComplete(self, *args):  # cannot find CLR method
        """
        OnSetComplete(self: DictionaryBase, key: object, oldValue: object, newValue: object)

            Performs additional custom processes after setting a value in the System.Collections.DictionaryBase instance.

            key: The key of the element to locate.

            oldValue: The old value of the element associated with key.

            newValue: The new value of the element associated with key.
        """
        ...
    def OnValidate(self, *args):  # cannot find CLR method
        """
        OnValidate(self: DictionaryBase, key: object, value: object)

            Performs additional custom processes when validating the element with the specified key and value.

            key: The key of the element to validate.

            value: The value of the element to validate.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """
        Contains(self: IDictionary, key: object) -> bool

            Determines whether the System.Collections.IDictionary object contains an element with the specified key.

            key: The key to locate in the System.Collections.IDictionary object.

            Returns: ue if the System.Collections.IDictionary contains an element with the key; otherwise, lse.
        """
        ...
    @property
    def Count(self):
        """
        Gets the number of elements contained in the System.Collections.DictionaryBase instance.

        Get: Count(self: DictionaryBase) -> int
        """
        ...
    @property
    def Dictionary(self):
        """Gets the list of elements contained in the System.Collections.DictionaryBase instance."""
        ...
    @property
    def InnerHashtable(self):
        """Gets the list of elements contained in the System.Collections.DictionaryBase instance."""
        ...

class DictionaryEntry:  # skipped bases: <type 'object'>
    """
    Defines a dictionary key/value pair that can be set or retrieved.

    DictionaryEntry(key: object, value: object)
    """

    @property
    def Key(self):
        """
        Gets or sets the key in the key/value pair.

        Get: Key(self: DictionaryEntry) -> object

        Set: Key(self: DictionaryEntry) = value
        """
        ...
    @property
    def Value(self):
        """
        Gets or sets the value in the key/value pair.

        Get: Value(self: DictionaryEntry) -> object

        Set: Value(self: DictionaryEntry) = value
        """
        ...

class Hashtable(
    IDictionary, ISerializable, IDeserializationCallback, ICloneable
):  # skipped bases: <type 'ICollection'>, <type 'IEnumerable'>
    """
    Represents a collection of key/value pairs that are organized based on the hash code of the key.To browse the .NET Framework source code for this type, see the Reference Source.

    Hashtable()

    Hashtable(capacity: int)

    Hashtable(capacity: int, loadFactor: Single)

    Hashtable(capacity: int, loadFactor: Single, hcp: IHashCodeProvider, comparer: IComparer)

    Hashtable(capacity: int, loadFactor: Single, equalityComparer: IEqualityComparer)

    Hashtable(hcp: IHashCodeProvider, comparer: IComparer)

    Hashtable(equalityComparer: IEqualityComparer)

    Hashtable(capacity: int, hcp: IHashCodeProvider, comparer: IComparer)

    Hashtable(capacity: int, equalityComparer: IEqualityComparer)

    Hashtable(d: IDictionary)

    Hashtable(d: IDictionary, loadFactor: Single)

    Hashtable(d: IDictionary, hcp: IHashCodeProvider, comparer: IComparer)

    Hashtable(d: IDictionary, equalityComparer: IEqualityComparer)

    Hashtable(d: IDictionary, loadFactor: Single, hcp: IHashCodeProvider, comparer: IComparer)

    Hashtable(d: IDictionary, loadFactor: Single, equalityComparer: IEqualityComparer)
    """

    def ContainsKey(self, key):
        """
        ContainsKey(self: Hashtable, key: object) -> bool

            Determines whether the System.Collections.Hashtable contains a specific key.

            key: The key to locate in the System.Collections.Hashtable.

            Returns: ue if the System.Collections.Hashtable contains an element with the specified key; otherwise, lse.
        """
        ...
    def ContainsValue(self, value):
        """
        ContainsValue(self: Hashtable, value: object) -> bool

            Determines whether the System.Collections.Hashtable contains a specific value.

            value: The value to locate in the System.Collections.Hashtable. The value can be ll.

            Returns: ue if the System.Collections.Hashtable contains an element with the specified value; otherwise, lse.
        """
        ...
    def CopyTo(self, array, arrayIndex):
        """
        CopyTo(self: Hashtable, array: Array, arrayIndex: int)

            Copies the System.Collections.Hashtable elements to a one-dimensional System.Array instance at the specified index.

            array: The one-dimensional System.Array that is the destination of the System.Collections.DictionaryEntry objects copied from System.Collections.Hashtable. The System.Array must have zero-based indexing.

            arrayIndex: The zero-based index in array at which copying begins.
        """
        ...
    def GetHash(self, *args):  # cannot find CLR method
        """
        GetHash(self: Hashtable, key: object) -> int

            Returns the hash code for the specified key.

            key: The System.Object for which a hash code is to be returned.

            Returns: The hash code for key.
        """
        ...
    def KeyEquals(self, *args):  # cannot find CLR method
        """
        KeyEquals(self: Hashtable, item: object, key: object) -> bool

            Compares a specific System.Object with a specific key in the System.Collections.Hashtable.

            item: The System.Object to compare with key.

            key: The key in the System.Collections.Hashtable to compare with item.

            Returns: ue if item and key are equal; otherwise, lse.
        """
        ...
    @staticmethod
    def Synchronized(table):
        """
        Synchronized(table: Hashtable) -> Hashtable

            Returns a synchronized (thread-safe) wrapper for the System.Collections.Hashtable.

            table: The System.Collections.Hashtable to synchronize.

            Returns: A synchronized (thread-safe) wrapper for the System.Collections.Hashtable.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """
        Contains(self: IDictionary, key: object) -> bool

            Determines whether the System.Collections.IDictionary object contains an element with the specified key.

            key: The key to locate in the System.Collections.IDictionary object.

            Returns: ue if the System.Collections.IDictionary contains an element with the key; otherwise, lse.
        """
        ...
    @property
    def comparer(self):
        """Gets or sets the System.Collections.IComparer to use for the System.Collections.Hashtable."""
        ...
    @property
    def Count(self):
        """
        Gets the number of key/value pairs contained in the System.Collections.Hashtable.

        Get: Count(self: Hashtable) -> int
        """
        ...
    @property
    def EqualityComparer(self):
        """Gets the System.Collections.IEqualityComparer to use for the System.Collections.Hashtable."""
        ...
    @property
    def hcp(self):
        """Gets or sets the object that can dispense hash codes."""
        ...
    @property
    def IsFixedSize(self):
        """
        Gets a value indicating whether the System.Collections.Hashtable has a fixed size.

        Get: IsFixedSize(self: Hashtable) -> bool
        """
        ...
    @property
    def IsReadOnly(self):
        """
        Gets a value indicating whether the System.Collections.Hashtable is read-only.

        Get: IsReadOnly(self: Hashtable) -> bool
        """
        ...
    @property
    def IsSynchronized(self):
        """
        Gets a value indicating whether access to the System.Collections.Hashtable is synchronized (thread safe).

        Get: IsSynchronized(self: Hashtable) -> bool
        """
        ...
    @property
    def Keys(self):
        """
        Gets an System.Collections.ICollection containing the keys in the System.Collections.Hashtable.

        Get: Keys(self: Hashtable) -> ICollection
        """
        ...
    @property
    def SyncRoot(self):
        """
        Gets an object that can be used to synchronize access to the System.Collections.Hashtable.

        Get: SyncRoot(self: Hashtable) -> object
        """
        ...
    @property
    def Values(self):
        """
        Gets an System.Collections.ICollection containing the values in the System.Collections.Hashtable.

        Get: Values(self: Hashtable) -> ICollection
        """
        ...

class IComparer:
    """Exposes a method that compares two objects."""

    def Compare(self, x, y):
        """
        Compare(self: IComparer, x: object, y: object) -> int

            Compares two objects and returns a value indicating whether one is less than, equal to, or greater than the other.

            x: The first object to compare.

            y: The second object to compare.

            Returns: A signed integer that indicates the relative values of x and y, as shown in the following table.Value Meaning Less than zero

                          x is less than y. Zero

                          x equals y. Greater than zero

                  x is greater than y.
        """
        ...
    def __cmp__(self, *args):  # cannot find CLR method
        """x.__cmp__(y) <==> cmp(x,y)"""
        ...

class IEnumerator(Generic[U]):
    """Supports a simple iteration over a non-generic collection."""

    def MoveNext(self):
        """
        MoveNext(self: IEnumerator) -> bool

            Advances the enumerator to the next element of the collection.

            Returns: ue if the enumerator was successfully advanced to the next element; lse if the enumerator has passed the end of the collection.
        """
        ...
    def next(self, *args):  # cannot find CLR method
        """next(self: object) -> object"""
        ...
    def Reset(self):
        """
        Reset(self: IEnumerator)

            Sets the enumerator to its initial position, which is before the first element in the collection.
        """
        ...
    def __iter__(self, *args) -> U:  # cannot find CLR method
        """__iter__(self: IEnumerator) -> object"""
        ...
    def __next__(self, *args) -> U:
        """__next__(self: IEnumerator) -> object"""
        ...
    @property
    def Current(self):
        """
        Gets the element in the collection at the current position of the enumerator.

        Get: Current(self: IEnumerator) -> object
        """
        ...

class IDictionaryEnumerator(IEnumerator):
    """Enumerates the elements of a nongeneric dictionary."""

    @property
    def Entry(self):
        """
        Gets both the key and the value of the current dictionary entry.

        Get: Entry(self: IDictionaryEnumerator) -> DictionaryEntry
        """
        ...
    @property
    def Key(self):
        """
        Gets the key of the current dictionary entry.

        Get: Key(self: IDictionaryEnumerator) -> object
        """
        ...
    @property
    def Value(self):
        """
        Gets the value of the current dictionary entry.

        Get: Value(self: IDictionaryEnumerator) -> object
        """
        ...

class IEqualityComparer:
    """Defines methods to support the comparison of objects for equality."""

    def Equals(self, x, y):
        """
        Equals(self: IEqualityComparer, x: object, y: object) -> bool

            Determines whether the specified objects are equal.

            x: The first object to compare.

            y: The second object to compare.

            Returns: ue if the specified objects are equal; otherwise, lse.
        """
        ...
    def GetHashCode(self, obj):
        """
        GetHashCode(self: IEqualityComparer, obj: object) -> int

            Returns a hash code for the specified object.

            obj: The System.Object for which a hash code is to be returned.

            Returns: A hash code for the specified object.
        """
        ...
    def __eq__(self, *args):  # cannot find CLR method
        """x.__eq__(y) <==> x==y"""
        ...

class IHashCodeProvider:
    """Supplies a hash code for an object, using a custom hash function."""

    def GetHashCode(self, obj):
        """
        GetHashCode(self: IHashCodeProvider, obj: object) -> int

            Returns a hash code for the specified object.

            obj: The System.Object for which a hash code is to be returned.

            Returns: A hash code for the specified object.
        """
        ...

class IStructuralComparable:
    """Supports the structural comparison of collection objects."""

    def CompareTo(self, other, comparer):
        """
        CompareTo(self: IStructuralComparable, other: object, comparer: IComparer) -> int

            Determines whether the current collection object precedes, occurs in the same position as, or follows another object in the sort order.

            other: The object to compare with the current instance.

            comparer: An object that compares members of the current collection object with the corresponding members of other.

            Returns: An integer that indicates the relationship of the current collection object to other, as shown in the following table.Return valueDescription-1The current instance precedes other.0The current instance and other are equal.1The

             current instance follows other.
        """
        ...
    def __eq__(self, *args):  # cannot find CLR method
        """x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y"""
        ...
    def __ge__(self, *args): ...
    def __gt__(self, *args): ...
    def __le__(self, *args): ...
    def __lt__(self, *args): ...
    def __ne__(self, *args): ...

class IStructuralEquatable:
    """Defines methods to support the comparison of objects for structural equality."""

    def Equals(self, other, comparer):
        """
        Equals(self: IStructuralEquatable, other: object, comparer: IEqualityComparer) -> bool

            Determines whether an object is structurally equal to the current instance.

            other: The object to compare with the current instance.

            comparer: An object that determines whether the current instance and other are equal.

            Returns: ue if the two objects are equal; otherwise, lse.
        """
        ...
    def GetHashCode(self, comparer):
        """
        GetHashCode(self: IStructuralEquatable, comparer: IEqualityComparer) -> int

            Returns a hash code for the current instance.

            comparer: An object that computes the hash code of the current object.

            Returns: The hash code for the current instance.
        """
        ...
    def __eq__(self, *args):  # cannot find CLR method
        """x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y"""
        ...
    def __ne__(self, *args): ...

class Queue(ICollection, ICloneable):  # skipped bases: <type 'IEnumerable'>
    """
    Represents a first-in, first-out collection of objects.

    Queue()

    Queue(capacity: int)

    Queue(capacity: int, growFactor: Single)

    Queue(col: ICollection)
    """

    def Clear(self):
        """
        Clear(self: Queue)

            Removes all objects from the System.Collections.Queue.
        """
        ...
    def Contains(self, obj):
        """
        Contains(self: Queue, obj: object) -> bool

            Determines whether an element is in the System.Collections.Queue.

            obj: The System.Object to locate in the System.Collections.Queue. The value can be ll.

            Returns: ue if obj is found in the System.Collections.Queue; otherwise, lse.
        """
        ...
    def Dequeue(self):
        """
        Dequeue(self: Queue) -> object

            Removes and returns the object at the beginning of the System.Collections.Queue.

            Returns: The object that is removed from the beginning of the System.Collections.Queue.
        """
        ...
    def Enqueue(self, obj):
        """
        Enqueue(self: Queue, obj: object)

            Adds an object to the end of the System.Collections.Queue.

            obj: The object to add to the System.Collections.Queue. The value can be ll.
        """
        ...
    def GetEnumerator(self):
        """
        GetEnumerator(self: Queue) -> IEnumerator

            Returns an enumerator that iterates through the System.Collections.Queue.

            Returns: An System.Collections.IEnumerator for the System.Collections.Queue.
        """
        ...
    def Peek(self):
        """
        Peek(self: Queue) -> object

            Returns the object at the beginning of the System.Collections.Queue without removing it.

            Returns: The object at the beginning of the System.Collections.Queue.
        """
        ...
    @staticmethod
    def Synchronized(queue):
        """
        Synchronized(queue: Queue) -> Queue

            Returns a new System.Collections.Queue that wraps the original queue, and is thread safe.

            queue: The System.Collections.Queue to synchronize.

            Returns: A System.Collections.Queue wrapper that is synchronized (thread safe).
        """
        ...
    def ToArray(self):
        """
        ToArray(self: Queue) -> Array[object]

            Copies the System.Collections.Queue elements to a new array.

            Returns: A new array containing elements copied from the System.Collections.Queue.
        """
        ...
    def TrimToSize(self):
        """
        TrimToSize(self: Queue)

            Sets the capacity to the actual number of elements in the System.Collections.Queue.
        """
        ...
    def __len__(self, *args):  # cannot find CLR method
        """x.__len__() <==> len(x)"""
        ...
    @property
    def Count(self):
        """
        Gets the number of elements contained in the System.Collections.Queue.

        Get: Count(self: Queue) -> int
        """
        ...
    @property
    def IsSynchronized(self):
        """
        Gets a value indicating whether access to the System.Collections.Queue is synchronized (thread safe).

        Get: IsSynchronized(self: Queue) -> bool
        """
        ...
    @property
    def SyncRoot(self):
        """
        Gets an object that can be used to synchronize access to the System.Collections.Queue.

        Get: SyncRoot(self: Queue) -> object
        """
        ...

class ReadOnlyCollectionBase(ICollection):  # skipped bases: <type 'IEnumerable'>
    """Provides the stract base class for a strongly typed non-generic read-only collection."""

    def GetEnumerator(self):
        """
        GetEnumerator(self: ReadOnlyCollectionBase) -> IEnumerator

            Returns an enumerator that iterates through the System.Collections.ReadOnlyCollectionBase instance.

            Returns: An System.Collections.IEnumerator for the System.Collections.ReadOnlyCollectionBase instance.
        """
        ...
    def __len__(self, *args):  # cannot find CLR method
        """x.__len__() <==> len(x)"""
        ...
    @property
    def Count(self):
        """
        Gets the number of elements contained in the System.Collections.ReadOnlyCollectionBase instance.

        Get: Count(self: ReadOnlyCollectionBase) -> int
        """
        ...
    @property
    def InnerList(self):
        """Gets the list of elements contained in the System.Collections.ReadOnlyCollectionBase instance."""
        ...

class SortedList(IDictionary, ICloneable):  # skipped bases: <type 'ICollection'>, <type 'IEnumerable'>
    """
    Represents a collection of key/value pairs that are sorted by the keys and are accessible by key and by index.

    SortedList()

    SortedList(initialCapacity: int)

    SortedList(comparer: IComparer)

    SortedList(comparer: IComparer, capacity: int)

    SortedList(d: IDictionary)

    SortedList(d: IDictionary, comparer: IComparer)
    """

    def ContainsKey(self, key):
        """
        ContainsKey(self: SortedList, key: object) -> bool

            Determines whether a System.Collections.SortedList object contains a specific key.

            key: The key to locate in the System.Collections.SortedList object.

            Returns: ue if the System.Collections.SortedList object contains an element with the specified key; otherwise, lse.
        """
        ...
    def ContainsValue(self, value):
        """
        ContainsValue(self: SortedList, value: object) -> bool

            Determines whether a System.Collections.SortedList object contains a specific value.

            value: The value to locate in the System.Collections.SortedList object. The value can be ll.

            Returns: ue if the System.Collections.SortedList object contains an element with the specified value; otherwise, lse.
        """
        ...
    def CopyTo(self, array, arrayIndex):
        """
        CopyTo(self: SortedList, array: Array, arrayIndex: int)

            Copies System.Collections.SortedList elements to a one-dimensional System.Array object, starting at the specified index in the array.

            array: The one-dimensional System.Array object that is the destination of the System.Collections.DictionaryEntry objects copied from System.Collections.SortedList. The System.Array must have zero-based indexing.

            arrayIndex: The zero-based index in array at which copying begins.
        """
        ...
    def GetByIndex(self, index):
        """
        GetByIndex(self: SortedList, index: int) -> object

            Gets the value at the specified index of a System.Collections.SortedList object.

            index: The zero-based index of the value to get.

            Returns: The value at the specified index of the System.Collections.SortedList object.
        """
        ...
    def GetKey(self, index):
        """
        GetKey(self: SortedList, index: int) -> object

            Gets the key at the specified index of a System.Collections.SortedList object.

            index: The zero-based index of the key to get.

            Returns: The key at the specified index of the System.Collections.SortedList object.
        """
        ...
    def GetKeyList(self):
        """
        GetKeyList(self: SortedList) -> IList

            Gets the keys in a System.Collections.SortedList object.

            Returns: An System.Collections.IList object containing the keys in the System.Collections.SortedList object.
        """
        ...
    def GetValueList(self):
        """
        GetValueList(self: SortedList) -> IList

            Gets the values in a System.Collections.SortedList object.

            Returns: An System.Collections.IList object containing the values in the System.Collections.SortedList object.
        """
        ...
    def IndexOfKey(self, key):
        """
        IndexOfKey(self: SortedList, key: object) -> int

            Returns the zero-based index of the specified key in a System.Collections.SortedList object.

            key: The key to locate in the System.Collections.SortedList object.

            Returns: The zero-based index of the key parameter, if key is found in the System.Collections.SortedList object; otherwise, -1.
        """
        ...
    def IndexOfValue(self, value):
        """
        IndexOfValue(self: SortedList, value: object) -> int

            Returns the zero-based index of the first occurrence of the specified value in a System.Collections.SortedList object.

            value: The value to locate in the System.Collections.SortedList object. The value can be ll.

            Returns: The zero-based index of the first occurrence of the value parameter, if value is found in the System.Collections.SortedList object; otherwise, -1.
        """
        ...
    def RemoveAt(self, index):
        """
        RemoveAt(self: SortedList, index: int)

            Removes the element at the specified index of a System.Collections.SortedList object.

            index: The zero-based index of the element to remove.
        """
        ...
    def SetByIndex(self, index, value):
        """
        SetByIndex(self: SortedList, index: int, value: object)

            Replaces the value at a specific index in a System.Collections.SortedList object.

            index: The zero-based index at which to save value.

            value: The System.Object to save into the System.Collections.SortedList object. The value can be ll.
        """
        ...
    @staticmethod
    def Synchronized(list):
        """
        Synchronized(list: SortedList) -> SortedList

            Returns a synchronized (thread-safe) wrapper for a System.Collections.SortedList object.

            list: The System.Collections.SortedList object to synchronize.

            Returns: A synchronized (thread-safe) wrapper for the System.Collections.SortedList object.
        """
        ...
    def TrimToSize(self):
        """
        TrimToSize(self: SortedList)

            Sets the capacity to the actual number of elements in a System.Collections.SortedList object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """
        Contains(self: IDictionary, key: object) -> bool

            Determines whether the System.Collections.IDictionary object contains an element with the specified key.

            key: The key to locate in the System.Collections.IDictionary object.

            Returns: ue if the System.Collections.IDictionary contains an element with the key; otherwise, lse.
        """
        ...
    @property
    def Capacity(self):
        """
        Gets or sets the capacity of a System.Collections.SortedList object.

        Get: Capacity(self: SortedList) -> int

        Set: Capacity(self: SortedList) = value
        """
        ...
    @property
    def Count(self):
        """
        Gets the number of elements contained in a System.Collections.SortedList object.

        Get: Count(self: SortedList) -> int
        """
        ...
    @property
    def IsFixedSize(self):
        """
        Gets a value indicating whether a System.Collections.SortedList object has a fixed size.

        Get: IsFixedSize(self: SortedList) -> bool
        """
        ...
    @property
    def IsReadOnly(self):
        """
        Gets a value indicating whether a System.Collections.SortedList object is read-only.

        Get: IsReadOnly(self: SortedList) -> bool
        """
        ...
    @property
    def IsSynchronized(self):
        """
        Gets a value indicating whether access to a System.Collections.SortedList object is synchronized (thread safe).

        Get: IsSynchronized(self: SortedList) -> bool
        """
        ...
    @property
    def Keys(self):
        """
        Gets the keys in a System.Collections.SortedList object.

        Get: Keys(self: SortedList) -> ICollection
        """
        ...
    @property
    def SyncRoot(self):
        """
        Gets an object that can be used to synchronize access to a System.Collections.SortedList object.

        Get: SyncRoot(self: SortedList) -> object
        """
        ...
    @property
    def Values(self):
        """
        Gets the values in a System.Collections.SortedList object.

        Get: Values(self: SortedList) -> ICollection
        """
        ...

class Stack(ICollection, ICloneable):  # skipped bases: <type 'IEnumerable'>
    """
    Represents a simple last-in-first-out (LIFO) non-generic collection of objects.

    Stack()

    Stack(initialCapacity: int)

    Stack(col: ICollection)
    """

    def Clear(self):
        """
        Clear(self: Stack)

            Removes all objects from the System.Collections.Stack.
        """
        ...
    def Contains(self, obj):
        """
        Contains(self: Stack, obj: object) -> bool

            Determines whether an element is in the System.Collections.Stack.

            obj: The object to locate in the System.Collections.Stack. The value can be ll.

            Returns: ue, if obj is found in the System.Collections.Stack; otherwise, lse.
        """
        ...
    def GetEnumerator(self):
        """
        GetEnumerator(self: Stack) -> IEnumerator

            Returns an System.Collections.IEnumerator for the System.Collections.Stack.

            Returns: An System.Collections.IEnumerator for the System.Collections.Stack.
        """
        ...
    def Peek(self):
        """
        Peek(self: Stack) -> object

            Returns the object at the top of the System.Collections.Stack without removing it.

            Returns: The System.Object at the top of the System.Collections.Stack.
        """
        ...
    def Pop(self):
        """
        Pop(self: Stack) -> object

            Removes and returns the object at the top of the System.Collections.Stack.

            Returns: The System.Object removed from the top of the System.Collections.Stack.
        """
        ...
    def Push(self, obj):
        """
        Push(self: Stack, obj: object)

            Inserts an object at the top of the System.Collections.Stack.

            obj: The System.Object to push onto the System.Collections.Stack. The value can be ll.
        """
        ...
    @staticmethod
    def Synchronized(stack):
        """
        Synchronized(stack: Stack) -> Stack

            Returns a synchronized (thread safe) wrapper for the System.Collections.Stack.

            stack: The System.Collections.Stack to synchronize.

            Returns: A synchronized wrapper around the System.Collections.Stack.
        """
        ...
    def ToArray(self):
        """
        ToArray(self: Stack) -> Array[object]

            Copies the System.Collections.Stack to a new array.

            Returns: A new array containing copies of the elements of the System.Collections.Stack.
        """
        ...
    def __len__(self, *args):  # cannot find CLR method
        """x.__len__() <==> len(x)"""
        ...
    @property
    def Count(self):
        """
        Gets the number of elements contained in the System.Collections.Stack.

        Get: Count(self: Stack) -> int
        """
        ...
    @property
    def IsSynchronized(self):
        """
        Gets a value indicating whether access to the System.Collections.Stack is synchronized (thread safe).

        Get: IsSynchronized(self: Stack) -> bool
        """
        ...
    @property
    def SyncRoot(self):
        """
        Gets an object that can be used to synchronize access to the System.Collections.Stack.

        Get: SyncRoot(self: Stack) -> object
        """
        ...

class StructuralComparisons:  # skipped bases: <type 'object'>
    """Provides objects for performing a structural comparison of two collection objects."""

    StructuralComparer = None
    StructuralEqualityComparer = None
    __all__ = []

# variables with complex values
