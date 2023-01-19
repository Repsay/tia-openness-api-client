# encoding: utf-8
# module System.Collections.Concurrent calls itself Concurrent
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
# no doc
# no imports

# no functions
# classes

from System.Collections import ICollection, IDictionary
from System import Enum, IDisposable

from System.Collections.Generic import IReadOnlyCollection
from System.Collections.ObjectModel import ReadOnlyDictionary

class BlockingCollection(
    ICollection, IDisposable, IReadOnlyCollection
):  # skipped bases: <type 'IEnumerable'>, <type 'IEnumerable[T]'>
    """
    BlockingCollection[T]()

    BlockingCollection[T](boundedCapacity: int)

    BlockingCollection[T](collection: IProducerConsumerCollection[T], boundedCapacity: int)

    BlockingCollection[T](collection: IProducerConsumerCollection[T])
    """

    def Add(self, item, cancellationToken=None):
        """
        Add(self: BlockingCollection[T], item: T)

            Adds the item to the System.Collections.Concurrent.BlockingCollection.

            item: The item to be added to the collection. The value can be a null reference.

        Add(self: BlockingCollection[T], item: T, cancellationToken: CancellationToken)

            Adds the item to the System.Collections.Concurrent.BlockingCollection.

            item: The item to be added to the collection. The value can be a null reference.

            cancellationToken: A cancellation token to observe.
        """
        ...
    @staticmethod
    def AddToAny(collections, item, cancellationToken=None):
        """
        AddToAny(collections: Array[BlockingCollection[T]], item: T) -> int

        AddToAny(collections: Array[BlockingCollection[T]], item: T, cancellationToken: CancellationToken) -> int
        """
        ...
    def CompleteAdding(self):
        """
        CompleteAdding(self: BlockingCollection[T])

            Marks the System.Collections.Concurrent.BlockingCollection instances as not accepting any more additions.
        """
        ...
    def GetConsumingEnumerable(self, cancellationToken=None):
        """
        GetConsumingEnumerable(self: BlockingCollection[T]) -> IEnumerable[T]

            Provides a consuming System.Collections.Generic.IEnumerator for items in the collection.

            Returns: An System.Collections.Generic.IEnumerable that removes and returns items from the collection.

        GetConsumingEnumerable(self: BlockingCollection[T], cancellationToken: CancellationToken) -> IEnumerable[T]

            Provides a consuming System.Collections.Generic.IEnumerable for items in the collection.

            cancellationToken: A cancellation token to observe.

            Returns: An System.Collections.Generic.IEnumerable that removes and returns items from the collection.
        """
        ...
    def Take(self, cancellationToken=None):
        """
        Take(self: BlockingCollection[T]) -> T

            Removes  an item from the System.Collections.Concurrent.BlockingCollection.

            Returns: The item removed from the collection.

        Take(self: BlockingCollection[T], cancellationToken: CancellationToken) -> T

            Removes an item from the System.Collections.Concurrent.BlockingCollection.

            cancellationToken: Object that can be used to cancel the take operation.

            Returns: The item removed from the collection.
        """
        ...
    @staticmethod
    def TakeFromAny(collections, item, cancellationToken=None):
        """
        TakeFromAny(collections: Array[BlockingCollection[T]]) -> (int, T)

        TakeFromAny(collections: Array[BlockingCollection[T]], cancellationToken: CancellationToken) -> (int, T)
        """
        ...
    def ToArray(self):
        """
        ToArray(self: BlockingCollection[T]) -> Array[T]

            Copies the items from the System.Collections.Concurrent.BlockingCollection instance into a new array.

            Returns: An array containing copies of the elements of the collection.
        """
        ...
    def TryAdd(self, item, *__args):
        """
        TryAdd(self: BlockingCollection[T], item: T) -> bool

            Tries to add the specified item to the System.Collections.Concurrent.BlockingCollection.

            item: The item to be added to the collection.

            Returns: true if item could be added; otherwise false. If the item is a duplicate, and the underlying collection does not accept duplicate items, then an System.InvalidOperationException is thrown.

        TryAdd(self: BlockingCollection[T], item: T, timeout: TimeSpan) -> bool

            Tries to add the specified item to the System.Collections.Concurrent.BlockingCollection.

            item: The item to be added to the collection.

            timeout: A System.TimeSpan that represents the number of milliseconds to wait, or a System.TimeSpan that represents -1 milliseconds to wait indefinitely.

            Returns: true if the item could be added to the collection within the specified time span; otherwise, false.

        TryAdd(self: BlockingCollection[T], item: T, millisecondsTimeout: int) -> bool

            Tries to add the specified item to the System.Collections.Concurrent.BlockingCollection within the specified time period.

            item: The item to be added to the collection.

            millisecondsTimeout: The number of milliseconds to wait, or System.Threading.Timeout.Infinite (-1) to wait indefinitely.

            Returns: true if the item could be added to the collection within the specified time; otherwise, false. If the item is a duplicate, and the underlying collection does not accept duplicate items, then an System.InvalidOperationException is

             thrown.

        TryAdd(self: BlockingCollection[T], item: T, millisecondsTimeout: int, cancellationToken: CancellationToken) -> bool

            Tries to add the specified item to the System.Collections.Concurrent.BlockingCollection within the specified time period, while observing a cancellation token.

            item: The item to be added to the collection.

            millisecondsTimeout: The number of milliseconds to wait, or System.Threading.Timeout.Infinite (-1) to wait indefinitely.

            cancellationToken: A cancellation token to observe.

            Returns: true if the item could be added to the collection within the specified time; otherwise, false. If the item is a duplicate, and the underlying collection does not accept duplicate items, then an System.InvalidOperationException is

             thrown.
        """
        ...
    @staticmethod
    def TryAddToAny(collections, item, *__args):
        """
        TryAddToAny(collections: Array[BlockingCollection[T]], item: T) -> int

        TryAddToAny(collections: Array[BlockingCollection[T]], item: T, timeout: TimeSpan) -> int

        TryAddToAny(collections: Array[BlockingCollection[T]], item: T, millisecondsTimeout: int) -> int

        TryAddToAny(collections: Array[BlockingCollection[T]], item: T, millisecondsTimeout: int, cancellationToken: CancellationToken) -> int
        """
        ...
    def TryTake(self, item, *__args):
        """
        TryTake(self: BlockingCollection[T]) -> (bool, T)

        TryTake(self: BlockingCollection[T], timeout: TimeSpan) -> (bool, T)

        TryTake(self: BlockingCollection[T], millisecondsTimeout: int) -> (bool, T)

        TryTake(self: BlockingCollection[T], millisecondsTimeout: int, cancellationToken: CancellationToken) -> (bool, T)
        """
        ...
    @staticmethod
    def TryTakeFromAny(collections, item, *__args):
        """
        TryTakeFromAny(collections: Array[BlockingCollection[T]]) -> (int, T)

        TryTakeFromAny(collections: Array[BlockingCollection[T]], timeout: TimeSpan) -> (int, T)

        TryTakeFromAny(collections: Array[BlockingCollection[T]], millisecondsTimeout: int) -> (int, T)

        TryTakeFromAny(collections: Array[BlockingCollection[T]], millisecondsTimeout: int, cancellationToken: CancellationToken) -> (int, T)
        """
        ...
    def __add__(self, *args):  # cannot find CLR method
        """x.__add__(y) <==> x+yx.__add__(y) <==> x+y"""
        ...
    def __len__(self, *args):  # cannot find CLR method
        """x.__len__() <==> len(x)"""
        ...
    @property
    def BoundedCapacity(self):
        """
        Gets the bounded capacity of this System.Collections.Concurrent.BlockingCollection instance.

        Get: BoundedCapacity(self: BlockingCollection[T]) -> int
        """
        ...
    @property
    def Count(self):
        """
        Gets the number of items contained in the System.Collections.Concurrent.BlockingCollection.

        Get: Count(self: BlockingCollection[T]) -> int
        """
        ...
    @property
    def IsAddingCompleted(self):
        """
        Gets whether this System.Collections.Concurrent.BlockingCollection has been marked as complete for adding.

        Get: IsAddingCompleted(self: BlockingCollection[T]) -> bool
        """
        ...
    @property
    def IsCompleted(self):
        """
        Gets whether this System.Collections.Concurrent.BlockingCollection has been marked as complete for adding and is empty.

        Get: IsCompleted(self: BlockingCollection[T]) -> bool
        """
        ...

class ConcurrentBag(
    IProducerConsumerCollection, IReadOnlyCollection
):  # skipped bases: <type 'ICollection'>, <type 'IEnumerable'>, <type 'IEnumerable[T]'>
    """
    ConcurrentBag[T]()

    ConcurrentBag[T](collection: IEnumerable[T])
    """

    def Add(self, item):
        """
        Add(self: ConcurrentBag[T], item: T)

            Adds an object to the System.Collections.Concurrent.ConcurrentBag.

            item: The object to be added to the System.Collections.Concurrent.ConcurrentBag. The value can be a null reference (Nothing in Visual Basic) for reference types.
        """
        ...
    def GetEnumerator(self):
        """
        GetEnumerator(self: ConcurrentBag[T]) -> IEnumerator[T]

            Returns an enumerator that iterates through the System.Collections.Concurrent.ConcurrentBag.

            Returns: An enumerator for the contents of the System.Collections.Concurrent.ConcurrentBag.
        """
        ...
    def TryPeek(self, result):
        """TryPeek(self: ConcurrentBag[T]) -> (bool, T)"""
        ...
    def __add__(self, *args):  # cannot find CLR method
        """x.__add__(y) <==> x+y"""
        ...
    @property
    def Count(self):
        """
        Gets the number of elements contained in the System.Collections.Concurrent.ConcurrentBag.

        Get: Count(self: ConcurrentBag[T]) -> int
        """
        ...
    @property
    def IsEmpty(self):
        """
        Gets a value that indicates whether the System.Collections.Concurrent.ConcurrentBag is empty.

        Get: IsEmpty(self: ConcurrentBag[T]) -> bool
        """
        ...

class ConcurrentDictionary(
    IDictionary, ReadOnlyDictionary
):  # skipped bases: <type 'ICollection'>, <type 'IEnumerable'>, <type 'IEnumerable[KeyValuePair[TKey, TValue]]'>, <type 'ICollection[KeyValuePair[TKey, TValue]]'>, <type 'IReadOnlyCollection[KeyValuePair[TKey, TValue]]'>
    """
    ConcurrentDictionary[TKey, TValue]()

    ConcurrentDictionary[TKey, TValue](concurrencyLevel: int, capacity: int)

    ConcurrentDictionary[TKey, TValue](collection: IEnumerable[KeyValuePair[TKey, TValue]])

    ConcurrentDictionary[TKey, TValue](comparer: IEqualityComparer[TKey])

    ConcurrentDictionary[TKey, TValue](collection: IEnumerable[KeyValuePair[TKey, TValue]], comparer: IEqualityComparer[TKey])

    ConcurrentDictionary[TKey, TValue](concurrencyLevel: int, collection: IEnumerable[KeyValuePair[TKey, TValue]], comparer: IEqualityComparer[TKey])

    ConcurrentDictionary[TKey, TValue](concurrencyLevel: int, capacity: int, comparer: IEqualityComparer[TKey])
    """

    def AddOrUpdate(self, key, *__args):
        """
        AddOrUpdate[TArg](self: ConcurrentDictionary[TKey, TValue], key: TKey, addValueFactory: Func[TKey, TArg, TValue], updateValueFactory: Func[TKey, TValue, TArg, TValue], factoryArgument: TArg) -> TValue

        AddOrUpdate(self: ConcurrentDictionary[TKey, TValue], key: TKey, addValueFactory: Func[TKey, TValue], updateValueFactory: Func[TKey, TValue, TValue]) -> TValue

        AddOrUpdate(self: ConcurrentDictionary[TKey, TValue], key: TKey, addValue: TValue, updateValueFactory: Func[TKey, TValue, TValue]) -> TValue
        """
        ...
    def GetOrAdd(self, key, *__args):
        """
        GetOrAdd(self: ConcurrentDictionary[TKey, TValue], key: TKey, valueFactory: Func[TKey, TValue]) -> TValue

            Adds a key/value pair to the System.Collections.Concurrent.ConcurrentDictionary by using the specified function, if the key does not already exist.

            key: The key of the element to add.

            valueFactory: The function used to generate a value for the key

            Returns: The value for the key. This will be either the existing value for the key if the key is already in the dictionary, or the new value for the key as returned by valueFactory if the key was not in the dictionary.

        GetOrAdd(self: ConcurrentDictionary[TKey, TValue], key: TKey, value: TValue) -> TValue

            Adds a key/value pair to the System.Collections.Concurrent.ConcurrentDictionary if the key does not already exist.

            key: The key of the element to add.

            value: the value to be added, if the key does not already exist

            Returns: The value for the key. This will be either the existing value for the key if the key is already in the dictionary, or the new value if the key was not in the dictionary.

        GetOrAdd[TArg](self: ConcurrentDictionary[TKey, TValue], key: TKey, valueFactory: Func[TKey, TArg, TValue], factoryArgument: TArg) -> TValue
        """
        ...
    def ToArray(self):
        """
        ToArray(self: ConcurrentDictionary[TKey, TValue]) -> Array[KeyValuePair[TKey, TValue]]

            Copies the key and value pairs stored in the System.Collections.Concurrent.ConcurrentDictionary to a new array.

            Returns: A new array containing a snapshot of key and value pairs copied from the System.Collections.Concurrent.ConcurrentDictionary.
        """
        ...
    def TryAdd(self, key, value):
        """
        TryAdd(self: ConcurrentDictionary[TKey, TValue], key: TKey, value: TValue) -> bool

            Attempts to add the specified key and value to the System.Collections.Concurrent.ConcurrentDictionary.

            key: The key of the element to add.

            value: The value of the element to add. The value can be  ll for reference types.

            Returns: ue if the key/value pair was added to the System.Collections.Concurrent.ConcurrentDictionary successfully; lse if the key already exists.
        """
        ...
    def TryRemove(self, key, value):
        """TryRemove(self: ConcurrentDictionary[TKey, TValue], key: TKey) -> (bool, TValue)"""
        ...
    def TryUpdate(self, key, newValue, comparisonValue):
        """
        TryUpdate(self: ConcurrentDictionary[TKey, TValue], key: TKey, newValue: TValue, comparisonValue: TValue) -> bool

            Compares the existing value for the specified key with a specified value, and if they are equal, updates the key with a third value.

            key: The key whose value is compared with comparisonValue and possibly replaced.

            newValue: The value that replaces the value of the element that has the specified key if the comparison results in equality.

            comparisonValue: The value that is compared to the value of the element that has the specified key.

            Returns: ue if the value with key was equal to comparisonValue and was replaced with newValue; otherwise, lse.
        """
        ...
    @property
    def Count(self):
        """
        Gets the number of key/value pairs contained in the System.Collections.Concurrent.ConcurrentDictionary.

        Get: Count(self: ConcurrentDictionary[TKey, TValue]) -> int
        """
        ...
    @property
    def IsEmpty(self):
        """
        Gets a value that indicates whether the System.Collections.Concurrent.ConcurrentDictionary is empty.

        Get: IsEmpty(self: ConcurrentDictionary[TKey, TValue]) -> bool
        """
        ...
    @property
    def Keys(self):
        """
        Gets a collection containing the keys in the System.Collections.Generic.Dictionary.

        Get: Keys(self: ConcurrentDictionary[TKey, TValue]) -> ICollection[TKey]
        """
        ...
    @property
    def Values(self):
        """
        Gets a collection that contains the values in the System.Collections.Generic.Dictionary.

        Get: Values(self: ConcurrentDictionary[TKey, TValue]) -> ICollection[TValue]
        """
        ...

class ConcurrentQueue(
    IProducerConsumerCollection, IReadOnlyCollection
):  # skipped bases: <type 'ICollection'>, <type 'IEnumerable'>, <type 'IEnumerable[T]'>
    """
    ConcurrentQueue[T]()

    ConcurrentQueue[T](collection: IEnumerable[T])
    """

    def Enqueue(self, item):
        """
        Enqueue(self: ConcurrentQueue[T], item: T)

            Adds an object to the end of the System.Collections.Concurrent.ConcurrentQueue.

            item: The object to add to the end of the System.Collections.Concurrent.ConcurrentQueue. The value can be a null reference (Nothing in Visual Basic) for reference types.
        """
        ...
    def GetEnumerator(self):
        """
        GetEnumerator(self: ConcurrentQueue[T]) -> IEnumerator[T]

            Returns an enumerator that iterates through the System.Collections.Concurrent.ConcurrentQueue.

            Returns: An enumerator for the contents of the System.Collections.Concurrent.ConcurrentQueue.
        """
        ...
    def TryDequeue(self, result):
        """TryDequeue(self: ConcurrentQueue[T]) -> (bool, T)"""
        ...
    def TryPeek(self, result):
        """TryPeek(self: ConcurrentQueue[T]) -> (bool, T)"""
        ...
    @property
    def Count(self):
        """
        Gets the number of elements contained in the System.Collections.Concurrent.ConcurrentQueue.

        Get: Count(self: ConcurrentQueue[T]) -> int
        """
        ...
    @property
    def IsEmpty(self):
        """
        Gets a value that indicates whether the System.Collections.Concurrent.ConcurrentQueue is empty.

        Get: IsEmpty(self: ConcurrentQueue[T]) -> bool
        """
        ...

class ConcurrentStack(
    IProducerConsumerCollection, IReadOnlyCollection
):  # skipped bases: <type 'IEnumerable[T]'>, <type 'IEnumerable'>, <type 'ICollection'>
    """
    ConcurrentStack[T]()

    ConcurrentStack[T](collection: IEnumerable[T])
    """

    def Clear(self):
        """
        Clear(self: ConcurrentStack[T])

            Removes all objects from the System.Collections.Concurrent.ConcurrentStack.
        """
        ...
    def GetEnumerator(self):
        """
        GetEnumerator(self: ConcurrentStack[T]) -> IEnumerator[T]

            Returns an enumerator that iterates through the System.Collections.Concurrent.ConcurrentStack.

            Returns: An enumerator for the System.Collections.Concurrent.ConcurrentStack.
        """
        ...
    def Push(self, item):
        """
        Push(self: ConcurrentStack[T], item: T)

            Inserts an object at the top of the System.Collections.Concurrent.ConcurrentStack.

            item: The object to push onto the System.Collections.Concurrent.ConcurrentStack. The value can be a null reference (Nothing in Visual Basic) for reference types.
        """
        ...
    def PushRange(self, items, startIndex=None, count=None):
        """PushRange(self: ConcurrentStack[T], items: Array[T])PushRange(self: ConcurrentStack[T], items: Array[T], startIndex: int, count: int)"""
        ...
    def TryPeek(self, result):
        """TryPeek(self: ConcurrentStack[T]) -> (bool, T)"""
        ...
    def TryPop(self, result):
        """TryPop(self: ConcurrentStack[T]) -> (bool, T)"""
        ...
    def TryPopRange(self, items, startIndex=None, count=None):
        """
        TryPopRange(self: ConcurrentStack[T], items: Array[T]) -> int

        TryPopRange(self: ConcurrentStack[T], items: Array[T], startIndex: int, count: int) -> int
        """
        ...
    @property
    def Count(self):
        """
        Gets the number of elements contained in the System.Collections.Concurrent.ConcurrentStack.

        Get: Count(self: ConcurrentStack[T]) -> int
        """
        ...
    @property
    def IsEmpty(self):
        """
        Gets a value that indicates whether the System.Collections.Concurrent.ConcurrentStack is empty.

        Get: IsEmpty(self: ConcurrentStack[T]) -> bool
        """
        ...

class EnumerablePartitionerOptions(
    Enum
):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies options to control the buffering behavior of a partitioner

    enum (flags) EnumerablePartitionerOptions, values: NoBuffering (1), None (0)
    """

    NoBuffering = None
    value__ = None

class IProducerConsumerCollection(ICollection):  # skipped bases: <type 'IEnumerable'>
    # no doc
    def ToArray(self):
        """
        ToArray(self: IProducerConsumerCollection[T]) -> Array[T]

            Copies the elements contained in the System.Collections.Concurrent.IProducerConsumerCollection to a new array.

            Returns: A new array containing the elements copied from the System.Collections.Concurrent.IProducerConsumerCollection.
        """
        ...
    def TryAdd(self, item):
        """
        TryAdd(self: IProducerConsumerCollection[T], item: T) -> bool

            Attempts to add an object to the System.Collections.Concurrent.IProducerConsumerCollection.

            item: The object to add to the System.Collections.Concurrent.IProducerConsumerCollection.

            Returns: true if the object was added successfully; otherwise, false.
        """
        ...
    def TryTake(self, item):
        """TryTake(self: IProducerConsumerCollection[T]) -> (bool, T)"""
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[T](enumerable: IEnumerable[T], value: T) -> bool"""
        ...
    def __len__(self, *args):  # cannot find CLR method
        """x.__len__() <==> len(x)"""
        ...

class OrderablePartitioner(Partitioner):
    # no doc
    def GetOrderableDynamicPartitions(self):
        """
        GetOrderableDynamicPartitions(self: OrderablePartitioner[TSource]) -> IEnumerable[KeyValuePair[Int64, TSource]]

            Creates an object that can partition the underlying collection into a variable number of partitions.

            Returns: An object that can create partitions over the underlying data source.
        """
        ...
    def GetOrderablePartitions(self, partitionCount):
        """
        GetOrderablePartitions(self: OrderablePartitioner[TSource], partitionCount: int) -> IList[IEnumerator[KeyValuePair[Int64, TSource]]]

            Partitions the underlying collection into the specified number of orderable partitions.

            partitionCount: The number of partitions to create.

            Returns: A list containing partitionCount enumerators.
        """
        ...
    @staticmethod  # known case of __new__
    def __new__(cls, *args):  # cannot find CLR constructor
        """__new__(cls: type, keysOrderedInEachPartition: bool, keysOrderedAcrossPartitions: bool, keysNormalized: bool)"""
        ...
    @property
    def KeysNormalized(self):
        """
        Gets whether order keys are normalized.

        Get: KeysNormalized(self: OrderablePartitioner[TSource]) -> bool
        """
        ...
    @property
    def KeysOrderedAcrossPartitions(self):
        """
        Gets whether elements in an earlier partition always come before elements in a later partition.

        Get: KeysOrderedAcrossPartitions(self: OrderablePartitioner[TSource]) -> bool
        """
        ...
    @property
    def KeysOrderedInEachPartition(self):
        """
        Gets whether elements in each partition are yielded in the order of increasing keys.

        Get: KeysOrderedInEachPartition(self: OrderablePartitioner[TSource]) -> bool
        """
        ...

class Partitioner:
    """Provides common partitioning strategies for arrays, lists, and enumerables."""

    @staticmethod
    def Create(*__args):
        """
        Create(fromInclusive: Int64, toExclusive: Int64) -> OrderablePartitioner[Tuple[Int64, Int64]]

            Creates a partitioner that chunks the user-specified range.

            fromInclusive: The lower, inclusive bound of the range.

            toExclusive: The upper, exclusive bound of the range.

            Returns: A partitioner.

        Create(fromInclusive: Int64, toExclusive: Int64, rangeSize: Int64) -> OrderablePartitioner[Tuple[Int64, Int64]]

            Creates a partitioner that chunks the user-specified range.

            fromInclusive: The lower, inclusive bound of the range.

            toExclusive: The upper, exclusive bound of the range.

            rangeSize: The size of each subrange.

            Returns: A partitioner.

        Create(fromInclusive: int, toExclusive: int) -> OrderablePartitioner[Tuple[int, int]]

            Creates a partitioner that chunks the user-specified range.

            fromInclusive: The lower, inclusive bound of the range.

            toExclusive: The upper, exclusive bound of the range.

            Returns: A partitioner.

        Create(fromInclusive: int, toExclusive: int, rangeSize: int) -> OrderablePartitioner[Tuple[int, int]]

            Creates a partitioner that chunks the user-specified range.

            fromInclusive: The lower, inclusive bound of the range.

            toExclusive: The upper, exclusive bound of the range.

            rangeSize: The size of each subrange.

            Returns: A partitioner.

        Create[TSource](list: IList[TSource], loadBalance: bool) -> OrderablePartitioner[TSource]

        Create[TSource](array: Array[TSource], loadBalance: bool) -> OrderablePartitioner[TSource]

        Create[TSource](source: IEnumerable[TSource]) -> OrderablePartitioner[TSource]

        Create[TSource](source: IEnumerable[TSource], partitionerOptions: EnumerablePartitionerOptions) -> OrderablePartitioner[TSource]
        """
        ...
    __all__ = [
        "Create",
    ]
