# encoding: utf-8
# module System.Collections.Generic calls itself Generic
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
# no doc
# no imports

# no functions
# classes

from System.Runtime.Serialization import IDeserializationCallback, ISerializable

from System import IDisposable, SystemException


class Comparer(IComparer):
    # no doc
    @staticmethod
    def Create(comparison):
        """
        Create(comparison: Comparison[T]) -> Comparer[T]

            Creates a comparer by using the specified comparison.

            comparison: The comparison to use.

            Returns: The new comparer.
        """
        ...


class Dictionary(IDictionary, IReadOnlyDictionary, ISerializable, IDeserializationCallback): # skipped bases: <type 'ICollection[KeyValuePair[TKey, TValue]]'>, <type 'ICollection'>, <type 'IEnumerable'>, <type 'IReadOnlyCollection[KeyValuePair[TKey, TValue]]'>, <type 'IEnumerable[KeyValuePair[TKey, TValue]]'>
    """
    Dictionary[TKey, TValue]()

    Dictionary[TKey, TValue](capacity: int)

    Dictionary[TKey, TValue](comparer: IEqualityComparer[TKey])

    Dictionary[TKey, TValue](capacity: int, comparer: IEqualityComparer[TKey])

    Dictionary[TKey, TValue](dictionary: IDictionary[TKey, TValue])

    Dictionary[TKey, TValue](dictionary: IDictionary[TKey, TValue], comparer: IEqualityComparer[TKey])
    """
    def ContainsValue(self, value):
        """
        ContainsValue(self: Dictionary[TKey, TValue], value: TValue) -> bool

            Determines whether the System.Collections.Generic.Dictionary contains a specific value.

            value: The value to locate in the System.Collections.Generic.Dictionary. The value can be ll for reference types.

            Returns: ue if the System.Collections.Generic.Dictionary contains an element with the specified value; otherwise, lse.
        """
        ...

    def Enumerator(self, *args): #cannot find CLR method
        # no doc
        ...

    def KeyCollection(self, *args): #cannot find CLR method
        """ KeyCollection(dictionary: Dictionary[TKey, TValue]) """
        ...

    def ValueCollection(self, *args): #cannot find CLR method
        """ ValueCollection(dictionary: Dictionary[TKey, TValue]) """
        ...

    @property
    def Comparer(self):
        """
        Gets the System.Collections.Generic.IEqualityComparer that is used to determine equality of keys for the dictionary.

        Get: Comparer(self: Dictionary[TKey, TValue]) -> IEqualityComparer[TKey]
        """
        ...

    @property
    def Count(self):
        """
        Gets the number of key/value pairs contained in the System.Collections.Generic.Dictionary.

        Get: Count(self: Dictionary[TKey, TValue]) -> int
        """
        ...

    @property
    def Keys(self):
        """
        Gets a collection containing the keys in the System.Collections.Generic.Dictionary.

        Get: Keys(self: Dictionary[TKey, TValue]) -> KeyCollection
        """
        ...

    @property
    def Values(self):
        """
        Gets a collection containing the values in the System.Collections.Generic.Dictionary.

        Get: Values(self: Dictionary[TKey, TValue]) -> ValueCollection
        """
        ...



class EqualityComparer(IEqualityComparer):
    # no doc
    pass

class ICollection(IEnumerable): # skipped bases: <type 'IEnumerable'>
    # no doc
    def Add(self, item):
        """
        Add(self: ICollection[T], item: T)

            Adds an item to the System.Collections.Generic.ICollection.

            item: The object to add to the System.Collections.Generic.ICollection.
        """
        ...

    def Clear(self):
        """
        Clear(self: ICollection[T])

            Removes all items from the System.Collections.Generic.ICollection.
        """
        ...

    def Contains(self, item):
        """
        Contains(self: ICollection[T], item: T) -> bool

            Determines whether the System.Collections.Generic.ICollection contains a specific value.

            item: The object to locate in the System.Collections.Generic.ICollection.

            Returns: ue if item is found in the System.Collections.Generic.ICollection; otherwise, lse.
        """
        ...

    def CopyTo(self, array, arrayIndex):
        """ CopyTo(self: ICollection[T], array: Array[T], arrayIndex: int) """
        ...

    def Remove(self, item):
        """
        Remove(self: ICollection[T], item: T) -> bool

            Removes the first occurrence of a specific object from the System.Collections.Generic.ICollection.

            item: The object to remove from the System.Collections.Generic.ICollection.

            Returns: ue if item was successfully removed from the System.Collections.Generic.ICollection; otherwise, lse. This method also returns lse if item is not found in the original System.Collections.Generic.ICollection.
        """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[T](enumerable: IEnumerable[T], value: T) -> bool """
        ...

    @property
    def Count(self):
        """
        Gets the number of elements contained in the System.Collections.Generic.ICollection.

        Get: Count(self: ICollection[T]) -> int
        """
        ...

    @property
    def IsReadOnly(self):
        """
        Gets a value indicating whether the System.Collections.Generic.ICollection is read-only.

        Get: IsReadOnly(self: ICollection[T]) -> bool
        """
        ...



class IComparer:
    # no doc
    def Compare(self, x, y):
        """
        Compare(self: IComparer[T], x: T, y: T) -> int

            Compares two objects and returns a value indicating whether one is less than, equal to, or greater than the other.

            x: The first object to compare.

            y: The second object to compare.

            Returns: A signed integer that indicates the relative values of x and y, as shown in the following table.Value Meaning Less than zero

                          x is less than y.Zero

                          x equals y.Greater than zero

             x is greater than y.
        """
        ...

    def __cmp__(self, *args): #cannot find CLR method
        """ x.__cmp__(y) <==> cmp(x,y) """
        ...


class IDictionary(ICollection): # skipped bases: <type 'IEnumerable[KeyValuePair[TKey, TValue]]'>, <type 'IEnumerable'>
    # no doc
    def ContainsKey(self, key):
        """
        ContainsKey(self: IDictionary[TKey, TValue], key: TKey) -> bool

            Determines whether the System.Collections.Generic.IDictionary contains an element with the specified key.

            key: The key to locate in the System.Collections.Generic.IDictionary.

            Returns: ue if the System.Collections.Generic.IDictionary contains an element with the key; otherwise, lse.
        """
        ...

    def TryGetValue(self, key, value):
        """ TryGetValue(self: IDictionary[TKey, TValue], key: TKey) -> (bool, TValue) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...

    @property
    def Keys(self):
        """
        Gets an System.Collections.Generic.ICollection containing the keys of the System.Collections.Generic.IDictionary.

        Get: Keys(self: IDictionary[TKey, TValue]) -> ICollection[TKey]
        """
        ...

    @property
    def Values(self):
        """
        Gets an System.Collections.Generic.ICollection containing the values in the System.Collections.Generic.IDictionary.

        Get: Values(self: IDictionary[TKey, TValue]) -> ICollection[TValue]
        """
        ...



class IEnumerable:
    # no doc
    pass

class IEnumerator(IDisposable):
    # no doc
    @property
    def Current(self):
        """
        Gets the element in the collection at the current position of the enumerator.

        Get: Current(self: IEnumerator[T]) -> T
        """
        ...



class IEqualityComparer:
    # no doc
    def Equals(self, x, y):
        """
        Equals(self: IEqualityComparer[T], x: T, y: T) -> bool

            Determines whether the specified objects are equal.

            x: The first object of type T to compare.

            y: The second object of type T to compare.

            Returns: ue if the specified objects are equal; otherwise, lse.
        """
        ...

    def GetHashCode(self, obj):
        """
        GetHashCode(self: IEqualityComparer[T], obj: T) -> int

            Returns a hash code for the specified object.

            obj: The System.Object for which a hash code is to be returned.

            Returns: A hash code for the specified object.
        """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...


class IList(ICollection): # skipped bases: <type 'IEnumerable[T]'>, <type 'IEnumerable'>
    # no doc
    def IndexOf(self, item):
        """
        IndexOf(self: IList[T], item: T) -> int

            Determines the index of a specific item in the System.Collections.Generic.IList.

            item: The object to locate in the System.Collections.Generic.IList.

            Returns: The index of item if found in the list; otherwise, -1.
        """
        ...

    def Insert(self, index, item):
        """
        Insert(self: IList[T], index: int, item: T)

            Inserts an item to the System.Collections.Generic.IList at the specified index.

            index: The zero-based index at which item should be inserted.

            item: The object to insert into the System.Collections.Generic.IList.
        """
        ...

    def RemoveAt(self, index):
        """
        RemoveAt(self: IList[T], index: int)

            Removes the System.Collections.Generic.IList item at the specified index.

            index: The zero-based index of the item to remove.
        """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class IReadOnlyCollection(IEnumerable): # skipped bases: <type 'IEnumerable'>
    # no doc
    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[T](enumerable: IEnumerable[T], value: T) -> bool """
        ...

    @property
    def Count(self):
        """
        Gets the number of elements in the collection.

        Get: Count(self: IReadOnlyCollection[T]) -> int
        """
        ...



class IReadOnlyDictionary(IReadOnlyCollection): # skipped bases: <type 'IEnumerable[KeyValuePair[TKey, TValue]]'>, <type 'IEnumerable'>
    # no doc
    def ContainsKey(self, key):
        """
        ContainsKey(self: IReadOnlyDictionary[TKey, TValue], key: TKey) -> bool

            Determines whether the read-only dictionary contains an element that has the specified key.

            key: The key to locate.

            Returns: ue if the read-only dictionary contains an element that has the specified key; otherwise, lse.
        """
        ...

    def TryGetValue(self, key, value):
        """ TryGetValue(self: IReadOnlyDictionary[TKey, TValue], key: TKey) -> (bool, TValue) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    @property
    def Keys(self):
        """
        Gets an enumerable collection that contains the keys in the read-only dictionary.

        Get: Keys(self: IReadOnlyDictionary[TKey, TValue]) -> IEnumerable[TKey]
        """
        ...

    @property
    def Values(self):
        """
        Gets an enumerable collection that contains the values in the read-only dictionary.

        Get: Values(self: IReadOnlyDictionary[TKey, TValue]) -> IEnumerable[TValue]
        """
        ...



class IReadOnlyList(IReadOnlyCollection): # skipped bases: <type 'IEnumerable'>, <type 'IEnumerable[T]'>
    # no doc
    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class ISet(ICollection): # skipped bases: <type 'IEnumerable[T]'>, <type 'IEnumerable'>
    # no doc
    def ExceptWith(self, other):
        """
        ExceptWith(self: ISet[T], other: IEnumerable[T])

            Removes all elements in the specified collection from the current set.

            other: The collection of items to remove from the set.
        """
        ...

    def IntersectWith(self, other):
        """
        IntersectWith(self: ISet[T], other: IEnumerable[T])

            Modifies the current set so that it contains only elements that are also in a specified collection.

            other: The collection to compare to the current set.
        """
        ...

    def IsProperSubsetOf(self, other):
        """
        IsProperSubsetOf(self: ISet[T], other: IEnumerable[T]) -> bool

            Determines whether the current set is a proper (strict) subset of a specified collection.

            other: The collection to compare to the current set.

            Returns: ue if the current set is a proper subset of other; otherwise, lse.
        """
        ...

    def IsProperSupersetOf(self, other):
        """
        IsProperSupersetOf(self: ISet[T], other: IEnumerable[T]) -> bool

            Determines whether the current set is a proper (strict) superset of a specified collection.

            other: The collection to compare to the current set.

            Returns: ue if the current set is a proper superset of other; otherwise, lse.
        """
        ...

    def IsSubsetOf(self, other):
        """
        IsSubsetOf(self: ISet[T], other: IEnumerable[T]) -> bool

            Determines whether a set is a subset of a specified collection.

            other: The collection to compare to the current set.

            Returns: ue if the current set is a subset of other; otherwise, lse.
        """
        ...

    def IsSupersetOf(self, other):
        """
        IsSupersetOf(self: ISet[T], other: IEnumerable[T]) -> bool

            Determines whether the current set is a superset of a specified collection.

            other: The collection to compare to the current set.

            Returns: ue if the current set is a superset of other; otherwise, lse.
        """
        ...

    def Overlaps(self, other):
        """
        Overlaps(self: ISet[T], other: IEnumerable[T]) -> bool

            Determines whether the current set overlaps with the specified collection.

            other: The collection to compare to the current set.

            Returns: ue if the current set and other share at least one common element; otherwise, lse.
        """
        ...

    def SetEquals(self, other):
        """
        SetEquals(self: ISet[T], other: IEnumerable[T]) -> bool

            Determines whether the current set and the specified collection contain the same elements.

            other: The collection to compare to the current set.

            Returns: ue if the current set is equal to other; otherwise, false.
        """
        ...

    def SymmetricExceptWith(self, other):
        """
        SymmetricExceptWith(self: ISet[T], other: IEnumerable[T])

            Modifies the current set so that it contains only elements that are present either in the current set or in the specified collection, but not both.

            other: The collection to compare to the current set.
        """
        ...

    def UnionWith(self, other):
        """
        UnionWith(self: ISet[T], other: IEnumerable[T])

            Modifies the current set so that it contains all elements that are present in the current set, in the specified collection, or in both.

            other: The collection to compare to the current set.
        """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...


class KeyNotFoundException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>
    """
    The exception that is thrown when the key specified for accessing an element in a collection does not match any key in the collection.

    KeyNotFoundException()

    KeyNotFoundException(message: str)

    KeyNotFoundException(message: str, innerException: Exception)
    """
    SerializeObjectState = None


class KeyValuePair: # skipped bases: <type 'object'>
    """ KeyValuePair[TKey, TValue](key: TKey, value: TValue) """
    def ToString(self):
        """
        ToString(self: KeyValuePair[TKey, TValue]) -> str

            Returns a string representation of the System.Collections.Generic.KeyValuePair, using the string representations of the key and value.

            Returns: A string representation of the System.Collections.Generic.KeyValuePair, which includes the string representations of the key and value.
        """
        ...

    @property
    def Key(self):
        """
        Gets the key in the key/value pair.

        Get: Key(self: KeyValuePair[TKey, TValue]) -> TKey
        """
        ...

    @property
    def Value(self):
        """
        Gets the value in the key/value pair.

        Get: Value(self: KeyValuePair[TKey, TValue]) -> TValue
        """
        ...



class LinkedList(ICollection, IReadOnlyCollection, ISerializable, IDeserializationCallback): # skipped bases: <type 'IEnumerable'>, <type 'IEnumerable[T]'>
    """
    LinkedList[T]()

    LinkedList[T](collection: IEnumerable[T])
    """
    def AddAfter(self, node, *__args):
        """
        AddAfter(self: LinkedList[T], node: LinkedListNode[T], newNode: LinkedListNode[T])

            Adds the specified new node after the specified existing node in the System.Collections.Generic.LinkedList.

            node: The System.Collections.Generic.LinkedListNode after which to insert newNode.

            newNode: The new System.Collections.Generic.LinkedListNode to add to the System.Collections.Generic.LinkedList.

        AddAfter(self: LinkedList[T], node: LinkedListNode[T], value: T) -> LinkedListNode[T]

            Adds a new node containing the specified value after the specified existing node in the System.Collections.Generic.LinkedList.

            node: The System.Collections.Generic.LinkedListNode after which to insert a new System.Collections.Generic.LinkedListNode containing value.

            value: The value to add to the System.Collections.Generic.LinkedList.

            Returns: The new System.Collections.Generic.LinkedListNode containing value.
        """
        ...

    def AddBefore(self, node, *__args):
        """
        AddBefore(self: LinkedList[T], node: LinkedListNode[T], value: T) -> LinkedListNode[T]

            Adds a new node containing the specified value before the specified existing node in the System.Collections.Generic.LinkedList.

            node: The System.Collections.Generic.LinkedListNode before which to insert a new System.Collections.Generic.LinkedListNode containing value.

            value: The value to add to the System.Collections.Generic.LinkedList.

            Returns: The new System.Collections.Generic.LinkedListNode containing value.

        AddBefore(self: LinkedList[T], node: LinkedListNode[T], newNode: LinkedListNode[T])

            Adds the specified new node before the specified existing node in the System.Collections.Generic.LinkedList.

            node: The System.Collections.Generic.LinkedListNode before which to insert newNode.

            newNode: The new System.Collections.Generic.LinkedListNode to add to the System.Collections.Generic.LinkedList.
        """
        ...

    def AddFirst(self, *__args):
        """
        AddFirst(self: LinkedList[T], value: T) -> LinkedListNode[T]

            Adds a new node containing the specified value at the start of the System.Collections.Generic.LinkedList.

            value: The value to add at the start of the System.Collections.Generic.LinkedList.

            Returns: The new System.Collections.Generic.LinkedListNode containing value.

        AddFirst(self: LinkedList[T], node: LinkedListNode[T])

            Adds the specified new node at the start of the System.Collections.Generic.LinkedList.

            node: The new System.Collections.Generic.LinkedListNode to add at the start of the System.Collections.Generic.LinkedList.
        """
        ...

    def AddLast(self, *__args):
        """
        AddLast(self: LinkedList[T], value: T) -> LinkedListNode[T]

            Adds a new node containing the specified value at the end of the System.Collections.Generic.LinkedList.

            value: The value to add at the end of the System.Collections.Generic.LinkedList.

            Returns: The new System.Collections.Generic.LinkedListNode containing value.

        AddLast(self: LinkedList[T], node: LinkedListNode[T])

            Adds the specified new node at the end of the System.Collections.Generic.LinkedList.

            node: The new System.Collections.Generic.LinkedListNode to add at the end of the System.Collections.Generic.LinkedList.
        """
        ...

    def Enumerator(self, *args): #cannot find CLR method
        # no doc
        ...

    def Find(self, value):
        """
        Find(self: LinkedList[T], value: T) -> LinkedListNode[T]

            Finds the first node that contains the specified value.

            value: The value to locate in the System.Collections.Generic.LinkedList.

            Returns: The first System.Collections.Generic.LinkedListNode that contains the specified value, if found; otherwise, ll.
        """
        ...

    def FindLast(self, value):
        """
        FindLast(self: LinkedList[T], value: T) -> LinkedListNode[T]

            Finds the last node that contains the specified value.

            value: The value to locate in the System.Collections.Generic.LinkedList.

            Returns: The last System.Collections.Generic.LinkedListNode that contains the specified value, if found; otherwise, ll.
        """
        ...

    def GetEnumerator(self):
        """
        GetEnumerator(self: LinkedList[T]) -> Enumerator

            Returns an enumerator that iterates through the System.Collections.Generic.LinkedList.

            Returns: An System.Collections.Generic.LinkedList for the System.Collections.Generic.LinkedList.
        """
        ...

    def RemoveFirst(self):
        """
        RemoveFirst(self: LinkedList[T])

            Removes the node at the start of the System.Collections.Generic.LinkedList.
        """
        ...

    def RemoveLast(self):
        """
        RemoveLast(self: LinkedList[T])

            Removes the node at the end of the System.Collections.Generic.LinkedList.
        """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...

    @property
    def Count(self):
        """
        Gets the number of nodes actually contained in the System.Collections.Generic.LinkedList.

        Get: Count(self: LinkedList[T]) -> int
        """
        ...

    @property
    def First(self):
        """
        Gets the first node of the System.Collections.Generic.LinkedList.

        Get: First(self: LinkedList[T]) -> LinkedListNode[T]
        """
        ...

    @property
    def Last(self):
        """
        Gets the last node of the System.Collections.Generic.LinkedList.

        Get: Last(self: LinkedList[T]) -> LinkedListNode[T]
        """
        ...



class LinkedListNode: # skipped bases: <type 'object'>
    """ LinkedListNode[T](value: T) """
    @property
    def List(self):
        """
        Gets the System.Collections.Generic.LinkedList that the System.Collections.Generic.LinkedListNode belongs to.

        Get: List(self: LinkedListNode[T]) -> LinkedList[T]
        """
        ...

    @property
    def Next(self):
        """
        Gets the next node in the System.Collections.Generic.LinkedList.

        Get: Next(self: LinkedListNode[T]) -> LinkedListNode[T]
        """
        ...

    @property
    def Previous(self):
        """
        Gets the previous node in the System.Collections.Generic.LinkedList.

        Get: Previous(self: LinkedListNode[T]) -> LinkedListNode[T]
        """
        ...

    @property
    def Value(self):
        """
        Gets the value contained in the node.

        Get: Value(self: LinkedListNode[T]) -> T

        Set: Value(self: LinkedListNode[T]) = value
        """
        ...



class List(IList, IReadOnlyList): # skipped bases: <type 'IEnumerable[T]'>, <type 'IReadOnlyCollection[T]'>, <type 'ICollection[T]'>, <type 'IEnumerable'>, <type 'ICollection'>
    """
    List[T]()

    List[T](capacity: int)

    List[T](collection: IEnumerable[T])
    """
    def AddRange(self, collection):
        """
        AddRange(self: List[T], collection: IEnumerable[T])

            Adds the elements of the specified collection to the end of the System.Collections.Generic.List.

            collection: The collection whose elements should be added to the end of the System.Collections.Generic.List. The collection itself cannot be ll, but it can contain elements that are ll, if type T is a reference type.
        """
        ...

    def AsReadOnly(self):
        """
        AsReadOnly(self: List[T]) -> ReadOnlyCollection[T]

            Returns a read-only System.Collections.ObjectModel.ReadOnlyCollection wrapper for the current collection.

            Returns: An object that acts as a read-only wrapper around the current System.Collections.Generic.List.
        """
        ...

    def BinarySearch(self, *__args):
        """
        BinarySearch(self: List[T], index: int, count: int, item: T, comparer: IComparer[T]) -> int

            Searches a range of elements in the sorted System.Collections.Generic.List for an element using the specified comparer and returns the zero-based index of the element.

            index: The zero-based starting index of the range to search.

            count: The length of the range to search.

            item: The object to locate. The value can be ll for reference types.

            comparer: The System.Collections.Generic.IComparer implementation to use when comparing elements, or ll to use the default comparer System.Collections.Generic.Comparer.

            Returns: The zero-based index of item in the sorted System.Collections.Generic.List, if item is found; otherwise, a negative number that is the bitwise complement of the index of the next element that is larger than item or, if there is no

             larger element, the bitwise complement of System.Collections.Generic.List.

        BinarySearch(self: List[T], item: T) -> int

            Searches the entire sorted System.Collections.Generic.List for an element using the default comparer and returns the zero-based index of the element.

            item: The object to locate. The value can be ll for reference types.

            Returns: The zero-based index of item in the sorted System.Collections.Generic.List, if item is found; otherwise, a negative number that is the bitwise complement of the index of the next element that is larger than item or, if there is no

             larger element, the bitwise complement of System.Collections.Generic.List.

        BinarySearch(self: List[T], item: T, comparer: IComparer[T]) -> int

            Searches the entire sorted System.Collections.Generic.List for an element using the specified comparer and returns the zero-based index of the element.

            item: The object to locate. The value can be ll for reference types.

            comparer: The System.Collections.Generic.IComparer implementation to use when comparing elements.-or-

                    ll to use the default comparer System.Collections.Generic.Comparer.

            Returns: The zero-based index of item in the sorted System.Collections.Generic.List, if item is found; otherwise, a negative number that is the bitwise complement of the index of the next element that is larger than item or, if there is no

             larger element, the bitwise complement of System.Collections.Generic.List.
        """
        ...

    def ConvertAll(self, converter):
        """ ConvertAll[TOutput](self: List[T], converter: Converter[T, TOutput]) -> List[TOutput] """
        ...

    def CopyTo(self, *__args):
        """ CopyTo(self: List[T], index: int, array: Array[T], arrayIndex: int, count: int)CopyTo(self: List[T], array: Array[T])CopyTo(self: List[T], array: Array[T], arrayIndex: int) """
        ...

    def Enumerator(self, *args): #cannot find CLR method
        # no doc
        ...

    def Exists(self, match):
        """
        Exists(self: List[T], match: Predicate[T]) -> bool

            Determines whether the System.Collections.Generic.List contains elements that match the conditions defined by the specified predicate.

            match: The System.Predicate delegate that defines the conditions of the elements to search for.

            Returns: ue if the System.Collections.Generic.List contains one or more elements that match the conditions defined by the specified predicate; otherwise, lse.
        """
        ...

    def Find(self, match):
        """
        Find(self: List[T], match: Predicate[T]) -> T

            Searches for an element that matches the conditions defined by the specified predicate, and returns the first occurrence within the entire System.Collections.Generic.List.

            match: The System.Predicate delegate that defines the conditions of the element to search for.

            Returns: The first element that matches the conditions defined by the specified predicate, if found; otherwise, the default value for type T.
        """
        ...

    def FindAll(self, match):
        """
        FindAll(self: List[T], match: Predicate[T]) -> List[T]

            Retrieves all the elements that match the conditions defined by the specified predicate.

            match: The System.Predicate delegate that defines the conditions of the elements to search for.

            Returns: A System.Collections.Generic.List containing all the elements that match the conditions defined by the specified predicate, if found; otherwise, an empty System.Collections.Generic.List.
        """
        ...

    def FindIndex(self, *__args):
        """
        FindIndex(self: List[T], startIndex: int, count: int, match: Predicate[T]) -> int

            Searches for an element that matches the conditions defined by the specified predicate, and returns the zero-based index of the first occurrence within the range of elements in the System.Collections.Generic.List that starts at the

             specified index and contains the specified number of elements.

            startIndex: The zero-based starting index of the search.

            count: The number of elements in the section to search.

            match: The System.Predicate delegate that defines the conditions of the element to search for.

                FindIndex(self: List[T], match: Predicate[T]) -> int

            Searches for an element that matches the conditions defined by the specified predicate, and returns the zero-based index of the first occurrence within the entire System.Collections.Generic.List.

            match: The System.Predicate delegate that defines the conditions of the element to search for.

                FindIndex(self: List[T], startIndex: int, match: Predicate[T]) -> int

            Searches for an element that matches the conditions defined by the specified predicate, and returns the zero-based index of the first occurrence within the range of elements in the System.Collections.Generic.List that extends from

             the specified index to the last element.

            startIndex: The zero-based starting index of the search.

            match: The System.Predicate delegate that defines the conditions of the element to search for.

                """
        ...

    def FindLast(self, match):
        """
        FindLast(self: List[T], match: Predicate[T]) -> T

            Searches for an element that matches the conditions defined by the specified predicate, and returns the last occurrence within the entire System.Collections.Generic.List.

            match: The System.Predicate delegate that defines the conditions of the element to search for.

            Returns: The last element that matches the conditions defined by the specified predicate, if found; otherwise, the default value for type T.
        """
        ...

    def FindLastIndex(self, *__args):
        """
        FindLastIndex(self: List[T], match: Predicate[T]) -> int

            Searches for an element that matches the conditions defined by the specified predicate, and returns the zero-based index of the last occurrence within the entire System.Collections.Generic.List.

            match: The System.Predicate delegate that defines the conditions of the element to search for.

                FindLastIndex(self: List[T], startIndex: int, match: Predicate[T]) -> int

            Searches for an element that matches the conditions defined by the specified predicate, and returns the zero-based index of the last occurrence within the range of elements in the System.Collections.Generic.List that extends from

             the first element to the specified index.

            startIndex: The zero-based starting index of the backward search.

            match: The System.Predicate delegate that defines the conditions of the element to search for.

                FindLastIndex(self: List[T], startIndex: int, count: int, match: Predicate[T]) -> int

            Searches for an element that matches the conditions defined by the specified predicate, and returns the zero-based index of the last occurrence within the range of elements in the System.Collections.Generic.List that contains the

             specified number of elements and ends at the specified index.

            startIndex: The zero-based starting index of the backward search.

            count: The number of elements in the section to search.

            match: The System.Predicate delegate that defines the conditions of the element to search for.

                """
        ...

    def ForEach(self, action):
        """
        ForEach(self: List[T], action: Action[T])

            Performs the specified action on each element of the System.Collections.Generic.List.

            action: The System.Action delegate to perform on each element of the System.Collections.Generic.List.
        """
        ...

    def GetEnumerator(self):
        """
        GetEnumerator(self: List[T]) -> Enumerator

            Returns an enumerator that iterates through the System.Collections.Generic.List.

            Returns: A System.Collections.Generic.List for the System.Collections.Generic.List.
        """
        ...

    def GetRange(self, index, count):
        """
        GetRange(self: List[T], index: int, count: int) -> List[T]

            Creates a shallow copy of a range of elements in the source System.Collections.Generic.List.

            index: The zero-based System.Collections.Generic.List index at which the range starts.

            count: The number of elements in the range.

            Returns: A shallow copy of a range of elements in the source System.Collections.Generic.List.
        """
        ...

    def InsertRange(self, index, collection):
        """
        InsertRange(self: List[T], index: int, collection: IEnumerable[T])

            Inserts the elements of a collection into the System.Collections.Generic.List at the specified index.

            index: The zero-based index at which the new elements should be inserted.

            collection: The collection whose elements should be inserted into the System.Collections.Generic.List. The collection itself cannot be ll, but it can contain elements that are ll, if type T is a reference type.
        """
        ...

    def LastIndexOf(self, item, index=None, count=None):
        """
        LastIndexOf(self: List[T], item: T) -> int

            Searches for the specified object and returns the zero-based index of the last occurrence within the entire System.Collections.Generic.List.

            item: The object to locate in the System.Collections.Generic.List. The value can be ll for reference types.

                LastIndexOf(self: List[T], item: T, index: int) -> int

            Searches for the specified object and returns the zero-based index of the last occurrence within the range of elements in the System.Collections.Generic.List that extends from the first element to the specified index.

            item: The object to locate in the System.Collections.Generic.List. The value can be ll for reference types.

            index: The zero-based starting index of the backward search.

                LastIndexOf(self: List[T], item: T, index: int, count: int) -> int

            Searches for the specified object and returns the zero-based index of the last occurrence within the range of elements in the System.Collections.Generic.List that contains the specified number of elements and ends at the specified

             index.

            item: The object to locate in the System.Collections.Generic.List. The value can be ll for reference types.

            index: The zero-based starting index of the backward search.

            count: The number of elements in the section to search.

                """
        ...

    def RemoveAll(self, match):
        """
        RemoveAll(self: List[T], match: Predicate[T]) -> int

            Removes all the elements that match the conditions defined by the specified predicate.

            match: The System.Predicate delegate that defines the conditions of the elements to remove.

            Returns: The number of elements removed from the System.Collections.Generic.List .
        """
        ...

    def RemoveRange(self, index, count):
        """
        RemoveRange(self: List[T], index: int, count: int)

            Removes a range of elements from the System.Collections.Generic.List.

            index: The zero-based starting index of the range of elements to remove.

            count: The number of elements to remove.
        """
        ...

    def Reverse(self, index=None, count=None):
        """
        Reverse(self: List[T], index: int, count: int)

            Reverses the order of the elements in the specified range.

            index: The zero-based starting index of the range to reverse.

            count: The number of elements in the range to reverse.

        Reverse(self: List[T])

            Reverses the order of the elements in the entire System.Collections.Generic.List.
        """
        ...

    def Sort(self, *__args):
        """
        Sort(self: List[T])

            Sorts the elements in the entire System.Collections.Generic.List using the default comparer.

        Sort(self: List[T], comparer: IComparer[T])

            Sorts the elements in the entire System.Collections.Generic.List using the specified comparer.

            comparer: The System.Collections.Generic.IComparer implementation to use when comparing elements, or ll to use the default comparer System.Collections.Generic.Comparer.

        Sort(self: List[T], index: int, count: int, comparer: IComparer[T])

            Sorts the elements in a range of elements in System.Collections.Generic.List using the specified comparer.

            index: The zero-based starting index of the range to sort.

            count: The length of the range to sort.

            comparer: The System.Collections.Generic.IComparer implementation to use when comparing elements, or ll to use the default comparer System.Collections.Generic.Comparer.

        Sort(self: List[T], comparison: Comparison[T])

            Sorts the elements in the entire System.Collections.Generic.List using the specified System.Comparison.

            comparison: The System.Comparison to use when comparing elements.
        """
        ...

    def ToArray(self):
        """
        ToArray(self: List[T]) -> Array[T]

            Copies the elements of the System.Collections.Generic.List to a new array.

            Returns: An array containing copies of the elements of the System.Collections.Generic.List.
        """
        ...

    def TrimExcess(self):
        """
        TrimExcess(self: List[T])

            Sets the capacity to the actual number of elements in the System.Collections.Generic.List, if that number is less than a threshold value.
        """
        ...

    def TrueForAll(self, match):
        """
        TrueForAll(self: List[T], match: Predicate[T]) -> bool

            Determines whether every element in the System.Collections.Generic.List matches the conditions defined by the specified predicate.

            match: The System.Predicate delegate that defines the conditions to check against the elements.

            Returns: ue if every element in the System.Collections.Generic.List matches the conditions defined by the specified predicate; otherwise, lse. If the list has no elements, the return value is ue.
        """
        ...

    def __delitem__(self, *args): #cannot find CLR method
        """ x.__delitem__(y) <==> del x[y]x.__delitem__(y) <==> del x[y]x.__delitem__(y) <==> del x[y] """
        ...

    def __getslice__(self, *args): #cannot find CLR method
        """
        __getslice__(self: List[T], x: int, y: int) -> List[T]

        __getslice__(self: List[T], x: int, y: int) -> List[T]
        """
        ...

    @property
    def Capacity(self):
        """
        Gets or sets the total number of elements the internal data structure can hold without resizing.

        Get: Capacity(self: List[T]) -> int

        Set: Capacity(self: List[T]) = value
        """
        ...

    @property
    def Count(self):
        """
        Gets the number of elements contained in the System.Collections.Generic.List.

        Get: Count(self: List[T]) -> int
        """
        ...


class Queue(ICollection, IReadOnlyCollection): # skipped bases: <type 'IEnumerable[T]'>, <type 'IEnumerable'>
    """
    Queue[T]()

    Queue[T](capacity: int)

    Queue[T](collection: IEnumerable[T])
    """
    def Clear(self):
        """
        Clear(self: Queue[T])

            Removes all objects from the System.Collections.Generic.Queue.
        """
        ...

    def Contains(self, item):
        """
        Contains(self: Queue[T], item: T) -> bool

            Determines whether an element is in the System.Collections.Generic.Queue.

            item: The object to locate in the System.Collections.Generic.Queue. The value can be ll for reference types.

            Returns: ue if item is found in the System.Collections.Generic.Queue; otherwise, lse.
        """
        ...

    def Dequeue(self):
        """
        Dequeue(self: Queue[T]) -> T

            Removes and returns the object at the beginning of the System.Collections.Generic.Queue.

            Returns: The object that is removed from the beginning of the System.Collections.Generic.Queue.
        """
        ...

    def Enqueue(self, item):
        """
        Enqueue(self: Queue[T], item: T)

            Adds an object to the end of the System.Collections.Generic.Queue.

            item: The object to add to the System.Collections.Generic.Queue. The value can be ll for reference types.
        """
        ...

    def Enumerator(self, *args): #cannot find CLR method
        # no doc
        ...

    def GetEnumerator(self):
        """
        GetEnumerator(self: Queue[T]) -> Enumerator

            Returns an enumerator that iterates through the System.Collections.Generic.Queue.

            Returns: An System.Collections.Generic.Queue for the System.Collections.Generic.Queue.
        """
        ...

    def Peek(self):
        """
        Peek(self: Queue[T]) -> T

            Returns the object at the beginning of the System.Collections.Generic.Queue without removing it.

            Returns: The object at the beginning of the System.Collections.Generic.Queue.
        """
        ...

    def ToArray(self):
        """
        ToArray(self: Queue[T]) -> Array[T]

            Copies the System.Collections.Generic.Queue elements to a new array.

            Returns: A new array containing elements copied from the System.Collections.Generic.Queue.
        """
        ...

    def TrimExcess(self):
        """
        TrimExcess(self: Queue[T])

            Sets the capacity to the actual number of elements in the System.Collections.Generic.Queue, if that number is less than 90 percent of current capacity.
        """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...

    @property
    def Count(self):
        """
        Gets the number of elements contained in the System.Collections.Generic.Queue.

        Get: Count(self: Queue[T]) -> int
        """
        ...




class SortedDictionary(IDictionary, IReadOnlyDictionary): # skipped bases: <type 'ICollection[KeyValuePair[TKey, TValue]]'>, <type 'ICollection'>, <type 'IEnumerable'>, <type 'IReadOnlyCollection[KeyValuePair[TKey, TValue]]'>, <type 'IEnumerable[KeyValuePair[TKey, TValue]]'>
    """
    SortedDictionary[TKey, TValue]()

    SortedDictionary[TKey, TValue](dictionary: IDictionary[TKey, TValue])

    SortedDictionary[TKey, TValue](dictionary: IDictionary[TKey, TValue], comparer: IComparer[TKey])

    SortedDictionary[TKey, TValue](comparer: IComparer[TKey])
    """
    def ContainsValue(self, value):
        """
        ContainsValue(self: SortedDictionary[TKey, TValue], value: TValue) -> bool

            Determines whether the System.Collections.Generic.SortedDictionary contains an element with the specified value.

            value: The value to locate in the System.Collections.Generic.SortedDictionary. The value can be ll for reference types.

            Returns: ue if the System.Collections.Generic.SortedDictionary contains an element with the specified value; otherwise, lse.
        """
        ...

    def CopyTo(self, array, index):
        """ CopyTo(self: SortedDictionary[TKey, TValue], array: Array[KeyValuePair[TKey, TValue]], index: int) """
        ...

    def Enumerator(self, *args): #cannot find CLR method
        # no doc
        ...

    def KeyCollection(self, *args): #cannot find CLR method
        """ KeyCollection(dictionary: SortedDictionary[TKey, TValue]) """
        ...

    def ValueCollection(self, *args): #cannot find CLR method
        """ ValueCollection(dictionary: SortedDictionary[TKey, TValue]) """
        ...

    @property
    def Comparer(self):
        """
        Gets the System.Collections.Generic.IComparer used to order the elements of the System.Collections.Generic.SortedDictionary.

        Get: Comparer(self: SortedDictionary[TKey, TValue]) -> IComparer[TKey]
        """
        ...

    @property
    def Count(self):
        """
        Gets the number of key/value pairs contained in the System.Collections.Generic.SortedDictionary.

        Get: Count(self: SortedDictionary[TKey, TValue]) -> int
        """
        ...

    @property
    def Keys(self):
        """
        Gets a collection containing the keys in the System.Collections.Generic.SortedDictionary.

        Get: Keys(self: SortedDictionary[TKey, TValue]) -> KeyCollection
        """
        ...

    @property
    def Values(self):
        """
        Gets a collection containing the values in the System.Collections.Generic.SortedDictionary.

        Get: Values(self: SortedDictionary[TKey, TValue]) -> ValueCollection
        """
        ...



class SortedList(IDictionary, IReadOnlyDictionary): # skipped bases: <type 'ICollection'>, <type 'IEnumerable'>, <type 'IReadOnlyCollection[KeyValuePair[TKey, TValue]]'>, <type 'ICollection[KeyValuePair[TKey, TValue]]'>, <type 'IEnumerable[KeyValuePair[TKey, TValue]]'>
    """
    SortedList[TKey, TValue]()

    SortedList[TKey, TValue](capacity: int)

    SortedList[TKey, TValue](comparer: IComparer[TKey])

    SortedList[TKey, TValue](capacity: int, comparer: IComparer[TKey])

    SortedList[TKey, TValue](dictionary: IDictionary[TKey, TValue])

    SortedList[TKey, TValue](dictionary: IDictionary[TKey, TValue], comparer: IComparer[TKey])
    """
    def ContainsValue(self, value):
        """
        ContainsValue(self: SortedList[TKey, TValue], value: TValue) -> bool

            Determines whether the System.Collections.Generic.SortedList contains a specific value.

            value: The value to locate in the System.Collections.Generic.SortedList. The value can be ll for reference types.

            Returns: ue if the System.Collections.Generic.SortedList contains an element with the specified value; otherwise, lse.
        """
        ...

    def IndexOfKey(self, key):
        """
        IndexOfKey(self: SortedList[TKey, TValue], key: TKey) -> int

            Searches for the specified key and returns the zero-based index within the entire System.Collections.Generic.SortedList.

            key: The key to locate in the System.Collections.Generic.SortedList.

            Returns: The zero-based index of key within the entire System.Collections.Generic.SortedList, if found; otherwise, -1.
        """
        ...

    def IndexOfValue(self, value):
        """
        IndexOfValue(self: SortedList[TKey, TValue], value: TValue) -> int

            Searches for the specified value and returns the zero-based index of the first occurrence within the entire System.Collections.Generic.SortedList.

            value: The value to locate in the System.Collections.Generic.SortedList.  The value can be ll for reference types.

            Returns: The zero-based index of the first occurrence of value within the entire System.Collections.Generic.SortedList, if found; otherwise, -1.
        """
        ...

    def RemoveAt(self, index):
        """
        RemoveAt(self: SortedList[TKey, TValue], index: int)

            Removes the element at the specified index of the System.Collections.Generic.SortedList.

            index: The zero-based index of the element to remove.
        """
        ...

    def TrimExcess(self):
        """
        TrimExcess(self: SortedList[TKey, TValue])

            Sets the capacity to the actual number of elements in the System.Collections.Generic.SortedList, if that number is less than 90 percent of current capacity.
        """
        ...

    @property
    def Capacity(self):
        """
        Gets or sets the number of elements that the System.Collections.Generic.SortedList can contain.

        Get: Capacity(self: SortedList[TKey, TValue]) -> int

        Set: Capacity(self: SortedList[TKey, TValue]) = value
        """
        ...

    @property
    def Comparer(self):
        """
        Gets the System.Collections.Generic.IComparer for the sorted list.

        Get: Comparer(self: SortedList[TKey, TValue]) -> IComparer[TKey]
        """
        ...

    @property
    def Count(self):
        """
        Gets the number of key/value pairs contained in the System.Collections.Generic.SortedList.

        Get: Count(self: SortedList[TKey, TValue]) -> int
        """
        ...

    @property
    def Keys(self):
        """
        Gets a collection containing the keys in the System.Collections.Generic.SortedList, in sorted order.

        Get: Keys(self: SortedList[TKey, TValue]) -> IList[TKey]
        """
        ...

    @property
    def Values(self):
        """
        Gets a collection containing the values in the System.Collections.Generic.SortedList.

        Get: Values(self: SortedList[TKey, TValue]) -> IList[TValue]
        """
        ...



class SortedSet(ISet, ICollection, ISerializable, IDeserializationCallback, IReadOnlyCollection): # skipped bases: <type 'IEnumerable[T]'>, <type 'IEnumerable'>, <type 'ICollection[T]'>
    """
    SortedSet[T]()

    SortedSet[T](comparer: IComparer[T])

    SortedSet[T](collection: IEnumerable[T])

    SortedSet[T](collection: IEnumerable[T], comparer: IComparer[T])
    """
    def Clear(self):
        """
        Clear(self: SortedSet[T])

            Removes all elements from the set.
        """
        ...

    def Contains(self, item):
        """
        Contains(self: SortedSet[T], item: T) -> bool

            Determines whether the set contains a specific element.

            item: The element to locate in the set.

            Returns: ue if the set contains item; otherwise, lse.
        """
        ...

    @staticmethod
    def CreateSetComparer(memberEqualityComparer=None):
        """
        CreateSetComparer() -> IEqualityComparer[SortedSet[T]]

            Returns an System.Collections.IEqualityComparer object that can be used to create a collection that contains individual sets.

            Returns: A comparer for creating a collection of sets.

        CreateSetComparer(memberEqualityComparer: IEqualityComparer[T]) -> IEqualityComparer[SortedSet[T]]

            Returns an System.Collections.IEqualityComparer object, according to a specified comparer, that can be used to create a collection that contains individual sets.

            memberEqualityComparer: The comparer to use for creating the returned comparer.

            Returns: A comparer for creating a collection of sets.
        """
        ...

    def Enumerator(self, *args): #cannot find CLR method
        # no doc
        ...

    def GetEnumerator(self):
        """
        GetEnumerator(self: SortedSet[T]) -> Enumerator

            Returns an enumerator that iterates through the System.Collections.Generic.SortedSet.

            Returns: An enumerator that iterates through the System.Collections.Generic.SortedSet in sorted order.
        """
        ...

    def GetViewBetween(self, lowerValue, upperValue):
        """
        GetViewBetween(self: SortedSet[T], lowerValue: T, upperValue: T) -> SortedSet[T]

            Returns a view of a subset in a System.Collections.Generic.SortedSet.

            lowerValue: The lowest desired value in the view.

            upperValue: The highest desired value in the view.

            Returns: A subset view that contains only the values in the specified range.
        """
        ...

    def Remove(self, item):
        """
        Remove(self: SortedSet[T], item: T) -> bool

            Removes a specified item from the System.Collections.Generic.SortedSet.

            item: The element to remove.

            Returns: ue if the element is found and successfully removed; otherwise, lse.
        """
        ...

    def RemoveWhere(self, match):
        """
        RemoveWhere(self: SortedSet[T], match: Predicate[T]) -> int

            Removes all elements that match the conditions defined by the specified predicate from a System.Collections.Generic.SortedSet.

            match: The delegate that defines the conditions of the elements to remove.

            Returns: The number of elements that were removed from the System.Collections.Generic.SortedSet collection..
        """
        ...

    def Reverse(self):
        """
        Reverse(self: SortedSet[T]) -> IEnumerable[T]

            Returns an System.Collections.Generic.IEnumerable that iterates over the System.Collections.Generic.SortedSet in reverse order.

            Returns: An enumerator that iterates over the System.Collections.Generic.SortedSet in reverse order.
        """
        ...

    def TryGetValue(self, equalValue, actualValue):
        """ TryGetValue(self: SortedSet[T], equalValue: T) -> (bool, T) """
        ...

    @property
    def Comparer(self):
        """
        Gets the System.Collections.Generic.IComparer object that is used to order the values in the System.Collections.Generic.SortedSet.

        Get: Comparer(self: SortedSet[T]) -> IComparer[T]
        """
        ...

    @property
    def Count(self):
        """
        Gets the number of elements in the System.Collections.Generic.SortedSet.

        Get: Count(self: SortedSet[T]) -> int
        """
        ...

    @property
    def Max(self):
        """
        Gets the maximum value in the System.Collections.Generic.SortedSet, as defined by the comparer.

        Get: Max(self: SortedSet[T]) -> T
        """
        ...

    @property
    def Min(self):
        """
        Gets the minimum value in the System.Collections.Generic.SortedSet, as defined by the comparer.

        Get: Min(self: SortedSet[T]) -> T
        """
        ...



class Stack(ICollection, IReadOnlyCollection): # skipped bases: <type 'IEnumerable[T]'>, <type 'IEnumerable'>
    """
    Stack[T]()

    Stack[T](capacity: int)

    Stack[T](collection: IEnumerable[T])
    """
    def Clear(self):
        """
        Clear(self: Stack[T])

            Removes all objects from the System.Collections.Generic.Stack.
        """
        ...

    def Contains(self, item):
        """
        Contains(self: Stack[T], item: T) -> bool

            Determines whether an element is in the System.Collections.Generic.Stack.

            item: The object to locate in the System.Collections.Generic.Stack. The value can be ll for reference types.

            Returns: ue if item is found in the System.Collections.Generic.Stack; otherwise, lse.
        """
        ...

    def Enumerator(self, *args): #cannot find CLR method
        # no doc
        ...

    def GetEnumerator(self):
        """
        GetEnumerator(self: Stack[T]) -> Enumerator

            Returns an enumerator for the System.Collections.Generic.Stack.

            Returns: An System.Collections.Generic.Stack for the System.Collections.Generic.Stack.
        """
        ...

    def Peek(self):
        """
        Peek(self: Stack[T]) -> T

            Returns the object at the top of the System.Collections.Generic.Stack without removing it.

            Returns: The object at the top of the System.Collections.Generic.Stack.
        """
        ...

    def Pop(self):
        """
        Pop(self: Stack[T]) -> T

            Removes and returns the object at the top of the System.Collections.Generic.Stack.

            Returns: The object removed from the top of the System.Collections.Generic.Stack.
        """
        ...

    def Push(self, item):
        """
        Push(self: Stack[T], item: T)

            Inserts an object at the top of the System.Collections.Generic.Stack.

            item: The object to push onto the System.Collections.Generic.Stack. The value can be ll for reference types.
        """
        ...

    def ToArray(self):
        """
        ToArray(self: Stack[T]) -> Array[T]

            Copies the System.Collections.Generic.Stack to a new array.

            Returns: A new array containing copies of the elements of the System.Collections.Generic.Stack.
        """
        ...

    def TrimExcess(self):
        """
        TrimExcess(self: Stack[T])

            Sets the capacity to the actual number of elements in the System.Collections.Generic.Stack, if that number is less than 90 percent of current capacity.
        """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...

    @property
    def Count(self):
        """
        Gets the number of elements contained in the System.Collections.Generic.Stack.

        Get: Count(self: Stack[T]) -> int
        """
        ...
