# encoding: utf-8
# module System.Collections.ObjectModel calls itself ObjectModel
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class Collection(object, IList[T], IList, IReadOnlyList[T]): # skipped bases: <type 'IReadOnlyCollection[T]'>, <type 'ICollection'>, <type 'IEnumerable'>, <type 'IEnumerable[T]'>, <type 'ICollection[T]'>
    """
    Collection[T]()

    Collection[T](list: IList[T])
    """
    def ClearItems(self, *args): #cannot find CLR method
        """
        ClearItems(self: Collection[T])

            Removes all elements from the System.Collections.ObjectModel.Collection.
        """
        ...

    def CopyTo(self, array, index):
        """ CopyTo(self: Collection[T], array: Array[T], index: int) """
        ...

    def GetEnumerator(self):
        """
        GetEnumerator(self: Collection[T]) -> IEnumerator[T]

            Returns an enumerator that iterates through the System.Collections.ObjectModel.Collection.

            Returns: An System.Collections.Generic.IEnumerator for the System.Collections.ObjectModel.Collection.
        """
        ...

    def InsertItem(self, *args): #cannot find CLR method
        """
        InsertItem(self: Collection[T], index: int, item: T)

            Inserts an element into the System.Collections.ObjectModel.Collection at the specified index.

            index: The zero-based index at which item should be inserted.

            item: The object to insert. The value can be ll for reference types.
        """
        ...

    def RemoveItem(self, *args): #cannot find CLR method
        """
        RemoveItem(self: Collection[T], index: int)

            Removes the element at the specified index of the System.Collections.ObjectModel.Collection.

            index: The zero-based index of the element to remove.
        """
        ...

    def SetItem(self, *args): #cannot find CLR method
        """
        SetItem(self: Collection[T], index: int, item: T)

            Replaces the element at the specified index.

            index: The zero-based index of the element to replace.

            item: The new value for the element at the specified index. The value can be ll for reference types.
        """
        ...

    @property
    def Count(self):
        """
        Gets the number of elements actually contained in the System.Collections.ObjectModel.Collection.

        Get: Count(self: Collection[T]) -> int
        """
        ...

    @property
    def Items(self):
        """ Gets a System.Collections.Generic.IList wrapper around the System.Collections.ObjectModel.Collection. """
        ...



class KeyedCollection(Collection[TItem]): # skipped bases: <type 'ICollection[TItem]'>, <type 'IReadOnlyCollection[TItem]'>, <type 'IEnumerable[TItem]'>, <type 'IList[TItem]'>, <type 'IList'>, <type 'ICollection'>, <type 'IEnumerable'>, <type 'IReadOnlyList[TItem]'>
    # no doc
    def ChangeItemKey(self, *args): #cannot find CLR method
        """
        ChangeItemKey(self: KeyedCollection[TKey, TItem], item: TItem, newKey: TKey)

            Changes the key associated with the specified element in the lookup dictionary.

            item: The element to change the key of.

            newKey: The new key for item.
        """
        ...

    def GetKeyForItem(self, *args): #cannot find CLR method
        """
        GetKeyForItem(self: KeyedCollection[TKey, TItem], item: TItem) -> TKey

            When implemented in a derived class, extracts the key from the specified element.

            item: The element from which to extract the key.

            Returns: The key for the specified element.
        """
        ...

    @property
    def Comparer(self):
        """
        Gets the generic equality comparer that is used to determine equality of keys in the collection.

        Get: Comparer(self: KeyedCollection[TKey, TItem]) -> IEqualityComparer[TKey]
        """
        ...

    @property
    def Dictionary(self):
        """ Gets the lookup dictionary of the System.Collections.ObjectModel.KeyedCollection. """
        ...

    @property
    def Items(self):
        """ Gets a System.Collections.Generic.IList wrapper around the System.Collections.ObjectModel.Collection. """
        ...



class ObservableCollection(Collection[T], INotifyCollectionChanged, INotifyPropertyChanged): # skipped bases: <type 'IList[T]'>, <type 'IReadOnlyList[T]'>, <type 'IReadOnlyCollection[T]'>, <type 'IList'>, <type 'IEnumerable[T]'>, <type 'IEnumerable'>, <type 'ICollection[T]'>, <type 'ICollection'>
    """
    ObservableCollection[T]()

    ObservableCollection[T](list: List[T])

    ObservableCollection[T](collection: IEnumerable[T])
    """
    def BlockReentrancy(self, *args): #cannot find CLR method
        """
        BlockReentrancy(self: ObservableCollection[T]) -> IDisposable

            Disallows reentrant attempts to change this collection.

            Returns: An System.IDisposable object that can be used to dispose of the object.
        """
        ...

    def CheckReentrancy(self, *args): #cannot find CLR method
        """
        CheckReentrancy(self: ObservableCollection[T])

            Checks for reentrant attempts to change this collection.
        """
        ...

    def Move(self, oldIndex, newIndex):
        """
        Move(self: ObservableCollection[T], oldIndex: int, newIndex: int)

            Moves the item at the specified index to a new location in the collection.

            oldIndex: The zero-based index specifying the location of the item to be moved.

            newIndex: The zero-based index specifying the new location of the item.
        """
        ...

    def MoveItem(self, *args): #cannot find CLR method
        """
        MoveItem(self: ObservableCollection[T], oldIndex: int, newIndex: int)

            Moves the item at the specified index to a new location in the collection.

            oldIndex: The zero-based index specifying the location of the item to be moved.

            newIndex: The zero-based index specifying the new location of the item.
        """
        ...

    def OnCollectionChanged(self, *args): #cannot find CLR method
        """
        OnCollectionChanged(self: ObservableCollection[T], e: NotifyCollectionChangedEventArgs)

            Raises the System.Collections.ObjectModel.ObservableCollection event with the provided arguments.

            e: Arguments of the event being raised.
        """
        ...

    def OnPropertyChanged(self, *args): #cannot find CLR method
        """
        OnPropertyChanged(self: ObservableCollection[T], e: PropertyChangedEventArgs)

            Raises the System.Collections.ObjectModel.ObservableCollection event with the provided arguments.

            e: Arguments of the event being raised.
        """
        ...

    @property
    def Items(self):
        """ Gets a System.Collections.Generic.IList wrapper around the System.Collections.ObjectModel.Collection. """
        ...


    CollectionChanged = None
    PropertyChanged = None


class ReadOnlyCollection(object, IList[T], IList, IReadOnlyList[T]): # skipped bases: <type 'IEnumerable[T]'>, <type 'ICollection'>, <type 'IEnumerable'>, <type 'ICollection[T]'>, <type 'IReadOnlyCollection[T]'>
    """ ReadOnlyCollection[T](list: IList[T]) """
    def CopyTo(self, array, index):
        """ CopyTo(self: ReadOnlyCollection[T], array: Array[T], index: int) """
        ...

    def GetEnumerator(self):
        """
        GetEnumerator(self: ReadOnlyCollection[T]) -> IEnumerator[T]

            Returns an enumerator that iterates through the System.Collections.ObjectModel.ReadOnlyCollection.

            Returns: An System.Collections.Generic.IEnumerator for the System.Collections.ObjectModel.ReadOnlyCollection.
        """
        ...

    @property
    def Count(self):
        """
        Gets the number of elements contained in the System.Collections.ObjectModel.ReadOnlyCollection instance.

        Get: Count(self: ReadOnlyCollection[T]) -> int
        """
        ...

    @property
    def Items(self):
        """ Returns the System.Collections.Generic.IList that the System.Collections.ObjectModel.ReadOnlyCollection wraps. """
        ...



class ReadOnlyDictionary(object, IDictionary[TKey, TValue], IDictionary, IReadOnlyDictionary[TKey, TValue]): # skipped bases: <type 'IEnumerable[KeyValuePair[TKey, TValue]]'>, <type 'ICollection[KeyValuePair[TKey, TValue]]'>, <type 'IEnumerable'>, <type 'ICollection'>, <type 'IReadOnlyCollection[KeyValuePair[TKey, TValue]]'>
    """ ReadOnlyDictionary[TKey, TValue](dictionary: IDictionary[TKey, TValue]) """
    def KeyCollection(self, *args): #cannot find CLR method
        # no doc
        ...

    def ValueCollection(self, *args): #cannot find CLR method
        # no doc
        ...

    @property
    def Count(self):
        """
        Gets the number of items in the dictionary.

        Get: Count(self: ReadOnlyDictionary[TKey, TValue]) -> int
        """
        ...

    @property
    def Dictionary(self):
        """ Gets the dictionary that is wrapped by this System.Collections.ObjectModel.ReadOnlyDictionary object. """
        ...

    @property
    def Keys(self):
        """
        Gets a key collection that contains the keys of the dictionary.

        Get: Keys(self: ReadOnlyDictionary[TKey, TValue]) -> KeyCollection
        """
        ...

    @property
    def Values(self):
        """
        Gets a collection that contains the values in the dictionary.

        Get: Values(self: ReadOnlyDictionary[TKey, TValue]) -> ValueCollection
        """
        ...


    KeyCollection = None
    ValueCollection = None


class ReadOnlyObservableCollection(ReadOnlyCollection[T], INotifyCollectionChanged, INotifyPropertyChanged): # skipped bases: <type 'IReadOnlyCollection[T]'>, <type 'IList[T]'>, <type 'IReadOnlyList[T]'>, <type 'IEnumerable[T]'>, <type 'IList'>, <type 'ICollection'>, <type 'IEnumerable'>, <type 'ICollection[T]'>
    """ ReadOnlyObservableCollection[T](list: ObservableCollection[T]) """
    def OnCollectionChanged(self, *args): #cannot find CLR method
        """
        OnCollectionChanged(self: ReadOnlyObservableCollection[T], args: NotifyCollectionChangedEventArgs)

            Raises the System.Collections.ObjectModel.ReadOnlyObservableCollection event using the provided arguments.

            args: Arguments of the event being raised.
        """
        ...

    def OnPropertyChanged(self, *args): #cannot find CLR method
        """
        OnPropertyChanged(self: ReadOnlyObservableCollection[T], args: PropertyChangedEventArgs)

            Raises the System.Collections.ObjectModel.ReadOnlyObservableCollection event using the provided arguments.

            args: Arguments of the event being raised.
        """
        ...

    @property
    def Items(self):
        """ Returns the System.Collections.Generic.IList that the System.Collections.ObjectModel.ReadOnlyCollection wraps. """
        ...


    CollectionChanged = None
    PropertyChanged = None


