# encoding: utf-8
# module System.Diagnostics calls itself Diagnostics
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
# no doc
# no imports

# no functions
# classes

from typing import Optional

class Switch:  # skipped bases: <type 'object'>
    """Provides an abstract base class to create new debugging and tracing switches."""

    def GetSupportedAttributes(self, *args):  # cannot find CLR method
        """
        GetSupportedAttributes(self: Switch) -> Array[str]

            Gets the custom attributes supported by the switch.

            Returns: A string array that contains the names of the custom attributes supported by the switch, or ll if there no custom attributes are supported.
        """
        ...
    def OnSwitchSettingChanged(self, *args):  # cannot find CLR method
        """
        OnSwitchSettingChanged(self: Switch)

            Invoked when the System.Diagnostics.Switch.SwitchSetting property is changed.
        """
        ...
    def OnValueChanged(self, *args):  # cannot find CLR method
        """
        OnValueChanged(self: Switch)

            Invoked when the System.Diagnostics.Switch.Value property is changed.
        """
        ...
    @property
    def Attributes(self):
        """
        Gets the custom switch attributes defined in the application configuration file.

        Get: Attributes(self: Switch) -> StringDictionary
        """
        ...
    @property
    def Description(self):
        """
        Gets a description of the switch.

        Get: Description(self: Switch) -> str
        """
        ...
    @property
    def DisplayName(self):
        """
        Gets a name used to identify the switch.

        Get: DisplayName(self: Switch) -> str
        """
        ...
    @property
    def SwitchSetting(self):
        """Gets or sets the current setting for this switch."""
        ...
    @property
    def Value(self):
        """Gets or sets the value of the switch."""
        ...

class BooleanSwitch(Switch):
    """
    Provides a simple on/off switch that controls debugging and tracing output.

    BooleanSwitch(displayName: str, description: str)

    BooleanSwitch(displayName: str, description: str, defaultSwitchValue: str)
    """

    @property
    def Enabled(self):
        """
        Gets or sets a value indicating whether the switch is enabled or disabled.

        Get: Enabled(self: BooleanSwitch) -> bool

        Set: Enabled(self: BooleanSwitch) = value
        """
        ...
    @property
    def SwitchSetting(self):
        """Gets or sets the current setting for this switch."""
        ...
    @property
    def Value(self):
        """Gets or sets the value of the switch."""
        ...

class ConditionalAttribute(Attribute):  # skipped bases: <type '_Attribute'>
    """
    Indicates to compilers that a method call or attribute should be ignored unless a specified conditional compilation symbol is defined.

    ConditionalAttribute(conditionString: str)
    """

    @staticmethod  # known case of __new__
    def __new__(cls, conditionString):
        """__new__(cls: type, conditionString: str)"""
        ...
    @property
    def ConditionString(self):
        """
        Gets the conditional compilation symbol that is associated with the System.Diagnostics.ConditionalAttribute attribute.

        Get: ConditionString(self: ConditionalAttribute) -> str
        """
        ...

class TraceListener(MarshalByRefObject, IDisposable):
    """Provides the stract base class for the listeners who monitor trace and debug output."""

    def Close(self):
        """
        Close(self: TraceListener)

            When overridden in a derived class, closes the output stream so it no longer receives tracing or debugging output.
        """
        ...
    def Fail(self, message, detailMessage=None):
        """
        Fail(self: TraceListener, message: str)

            Emits an error message to the listener you create when you implement the System.Diagnostics.TraceListener class.

            message: A message to emit.

        Fail(self: TraceListener, message: str, detailMessage: str)

            Emits an error message and a detailed error message to the listener you create when you implement the System.Diagnostics.TraceListener class.

            message: A message to emit.

            detailMessage: A detailed message to emit.
        """
        ...
    def Flush(self):
        """
        Flush(self: TraceListener)

            When overridden in a derived class, flushes the output buffer.
        """
        ...
    def GetSupportedAttributes(self, *args):  # cannot find CLR method
        """
        GetSupportedAttributes(self: TraceListener) -> Array[str]

            Gets the custom attributes supported by the trace listener.

            Returns: A string array naming the custom attributes supported by the trace listener, or ll if there are no custom attributes.
        """
        ...
    def TraceData(self, eventCache, source, eventType, id, data):
        """
        TraceData(self: TraceListener, eventCache: TraceEventCache, source: str, eventType: TraceEventType, id: int, data: object)

            Writes trace information, a data object and event information to the listener specific output.

            eventCache: A System.Diagnostics.TraceEventCache object that contains the current process ID, thread ID, and stack trace information.

            source: A name used to identify the output, typically the name of the application that generated the trace event.

            eventType: One of the System.Diagnostics.TraceEventType values specifying the type of event that has caused the trace.

            id: A numeric identifier for the event.

            data: The trace data to emit.

        TraceData(self: TraceListener, eventCache: TraceEventCache, source: str, eventType: TraceEventType, id: int, *data: Array[object])

            Writes trace information, an array of data objects and event information to the listener specific output.

            eventCache: A System.Diagnostics.TraceEventCache object that contains the current process ID, thread ID, and stack trace information.

            source: A name used to identify the output, typically the name of the application that generated the trace event.

            eventType: One of the System.Diagnostics.TraceEventType values specifying the type of event that has caused the trace.

            id: A numeric identifier for the event.

            data: An array of objects to emit as data.
        """
        ...
    def TraceEvent(self, eventCache, source, eventType, id, *__args):
        """
        TraceEvent(self: TraceListener, eventCache: TraceEventCache, source: str, eventType: TraceEventType, id: int)

            Writes trace and event information to the listener specific output.

            eventCache: A System.Diagnostics.TraceEventCache object that contains the current process ID, thread ID, and stack trace information.

            source: A name used to identify the output, typically the name of the application that generated the trace event.

            eventType: One of the System.Diagnostics.TraceEventType values specifying the type of event that has caused the trace.

            id: A numeric identifier for the event.

        TraceEvent(self: TraceListener, eventCache: TraceEventCache, source: str, eventType: TraceEventType, id: int, message: str)

            Writes trace information, a message, and event information to the listener specific output.

            eventCache: A System.Diagnostics.TraceEventCache object that contains the current process ID, thread ID, and stack trace information.

            source: A name used to identify the output, typically the name of the application that generated the trace event.

            eventType: One of the System.Diagnostics.TraceEventType values specifying the type of event that has caused the trace.

            id: A numeric identifier for the event.

            message: A message to write.

        TraceEvent(self: TraceListener, eventCache: TraceEventCache, source: str, eventType: TraceEventType, id: int, format: str, *args: Array[object])

            Writes trace information, a formatted array of objects and event information to the listener specific output.

            eventCache: A System.Diagnostics.TraceEventCache object that contains the current process ID, thread ID, and stack trace information.

            source: A name used to identify the output, typically the name of the application that generated the trace event.

            eventType: One of the System.Diagnostics.TraceEventType values specifying the type of event that has caused the trace.

            id: A numeric identifier for the event.

            format: A format string that contains zero or more format items, which correspond to objects in the args array.

            args: An ject array containing zero or more objects to format.
        """
        ...
    def TraceTransfer(self, eventCache, source, id, message, relatedActivityId):
        """
        TraceTransfer(self: TraceListener, eventCache: TraceEventCache, source: str, id: int, message: str, relatedActivityId: Guid)

            Writes trace information, a message, a related activity identity and event information to the listener specific output.

            eventCache: A System.Diagnostics.TraceEventCache object that contains the current process ID, thread ID, and stack trace information.

            source: A name used to identify the output, typically the name of the application that generated the trace event.

            id: A numeric identifier for the event.

            message: A message to write.

            relatedActivityId: A System.Guid  object identifying a related activity.
        """
        ...
    def Write(self, *__args):
        """
        Write(self: TraceListener, o: object)

            Writes the value of the object's System.Object.ToString method to the listener you create when you implement the System.Diagnostics.TraceListener class.

            o: An System.Object whose fully qualified class name you want to write.

        Write(self: TraceListener, o: object, category: str)

            Writes a category name and the value of the object's System.Object.ToString method to the listener you create when you implement the System.Diagnostics.TraceListener class.

            o: An System.Object whose fully qualified class name you want to write.

            category: A category name used to organize the output.

        Write(self: TraceListener, message: str)

            When overridden in a derived class, writes the specified message to the listener you create in the derived class.

            message: A message to write.

        Write(self: TraceListener, message: str, category: str)

            Writes a category name and a message to the listener you create when you implement the System.Diagnostics.TraceListener class.

            message: A message to write.

            category: A category name used to organize the output.
        """
        ...
    def WriteIndent(self, *args):  # cannot find CLR method
        """
        WriteIndent(self: TraceListener)

            Writes the indent to the listener you create when you implement this class, and resets the System.Diagnostics.TraceListener.NeedIndent property to lse.
        """
        ...
    def WriteLine(self, *__args):
        """
        WriteLine(self: TraceListener, o: object)

            Writes the value of the object's System.Object.ToString method to the listener you create when you implement the System.Diagnostics.TraceListener class, followed by a line terminator.

            o: An System.Object whose fully qualified class name you want to write.

        WriteLine(self: TraceListener, o: object, category: str)

            Writes a category name and the value of the object's System.Object.ToString method to the listener you create when you implement the System.Diagnostics.TraceListener class, followed by a line terminator.

            o: An System.Object whose fully qualified class name you want to write.

            category: A category name used to organize the output.

        WriteLine(self: TraceListener, message: str)

            When overridden in a derived class, writes a message to the listener you create in the derived class, followed by a line terminator.

            message: A message to write.

        WriteLine(self: TraceListener, message: str, category: str)

            Writes a category name and a message to the listener you create when you implement the System.Diagnostics.TraceListener class, followed by a line terminator.

            message: A message to write.

            category: A category name used to organize the output.
        """
        ...
    @staticmethod  # known case of __new__
    def __new__(cls, *args):  # cannot find CLR constructor
        """
        __new__(cls: type)

        __new__(cls: type, name: str)
        """
        ...
    @property
    def Attributes(self):
        """
        Gets the custom trace listener attributes defined in the application configuration file.

        Get: Attributes(self: TraceListener) -> StringDictionary
        """
        ...
    @property
    def Filter(self):
        """
        Gets and sets the trace filter for the trace listener.

        Get: Filter(self: TraceListener) -> TraceFilter

        Set: Filter(self: TraceListener) = value
        """
        ...
    @property
    def IndentLevel(self):
        """
        Gets or sets the indent level.

        Get: IndentLevel(self: TraceListener) -> int

        Set: IndentLevel(self: TraceListener) = value
        """
        ...
    @property
    def IndentSize(self):
        """
        Gets or sets the number of spaces in an indent.

        Get: IndentSize(self: TraceListener) -> int

        Set: IndentSize(self: TraceListener) = value
        """
        ...
    @property
    def IsThreadSafe(self):
        """
        Gets a value indicating whether the trace listener is thread safe.

        Get: IsThreadSafe(self: TraceListener) -> bool
        """
        ...
    @property
    def Name(self):
        """
        Gets or sets a name for this System.Diagnostics.TraceListener.

        Get: Name(self: TraceListener) -> str

        Set: Name(self: TraceListener) = value
        """
        ...
    @property
    def NeedIndent(self):
        """Gets or sets a value indicating whether to indent the output."""
        ...
    @property
    def TraceOutputOptions(self):
        """
        Gets or sets the trace output options.

        Get: TraceOutputOptions(self: TraceListener) -> TraceOptions

        Set: TraceOutputOptions(self: TraceListener) = value
        """
        ...

class TextWriterTraceListener(TraceListener):  # skipped bases: <type 'IDisposable'>
    """
    Directs tracing or debugging output to a System.IO.TextWriter or to a System.IO.Stream, such as System.IO.FileStream.

    TextWriterTraceListener()

    TextWriterTraceListener(stream: Stream)

    TextWriterTraceListener(stream: Stream, name: str)

    TextWriterTraceListener(writer: TextWriter)

    TextWriterTraceListener(writer: TextWriter, name: str)

    TextWriterTraceListener(fileName: str)

    TextWriterTraceListener(fileName: str, name: str)
    """

    @property
    def NeedIndent(self):
        """Gets or sets a value indicating whether to indent the output."""
        ...
    @property
    def Writer(self):
        """
        Gets or sets the text writer that receives the tracing or debugging output.

        Get: Writer(self: TextWriterTraceListener) -> TextWriter

        Set: Writer(self: TextWriterTraceListener) = value
        """
        ...

class ConsoleTraceListener(TextWriterTraceListener):  # skipped bases: <type 'IDisposable'>
    """
    Directs tracing or debugging output to either the standard output or the standard error stream.

    ConsoleTraceListener()

    ConsoleTraceListener(useErrorStream: bool)
    """

    @property
    def NeedIndent(self):
        """Gets or sets a value indicating whether to indent the output."""
        ...

class CorrelationManager:  # skipped bases: <type 'object'>
    """Correlates traces that are part of a logical transaction."""

    def StartLogicalOperation(self, operationId=None):
        """
        StartLogicalOperation(self: CorrelationManager, operationId: object)

            Starts a logical operation with the specified identity on a thread.

            operationId: An object identifying the operation.

        StartLogicalOperation(self: CorrelationManager)

            Starts a logical operation on a thread.
        """
        ...
    def StopLogicalOperation(self):
        """
        StopLogicalOperation(self: CorrelationManager)

            Stops the current logical operation.
        """
        ...
    @property
    def ActivityId(self):
        """
        Gets or sets the identity for a global activity.

        Get: ActivityId(self: CorrelationManager) -> Guid

        Set: ActivityId(self: CorrelationManager) = value
        """
        ...
    @property
    def LogicalOperationStack(self):
        """
        Gets the logical operation stack from the call context.

        Get: LogicalOperationStack(self: CorrelationManager) -> Stack
        """
        ...

class CounterCreationData:  # skipped bases: <type 'object'>
    """
    Defines the counter type, name, and Help string for a custom counter.

    CounterCreationData()

    CounterCreationData(counterName: str, counterHelp: str, counterType: PerformanceCounterType)
    """

    @property
    def CounterHelp(self):
        """
        Gets or sets the custom counter's description.

        Get: CounterHelp(self: CounterCreationData) -> str

        Set: CounterHelp(self: CounterCreationData) = value
        """
        ...
    @property
    def CounterName(self):
        """
        Gets or sets the name of the custom counter.

        Get: CounterName(self: CounterCreationData) -> str

        Set: CounterName(self: CounterCreationData) = value
        """
        ...
    @property
    def CounterType(self):
        """
        Gets or sets the performance counter type of the custom counter.

        Get: CounterType(self: CounterCreationData) -> PerformanceCounterType

        Set: CounterType(self: CounterCreationData) = value
        """
        ...

class CounterCreationDataCollection(
    CollectionBase
):  # skipped bases: <type 'IList'>, <type 'ICollection'>, <type 'IEnumerable'>
    """
    Provides a strongly typed collection of System.Diagnostics.CounterCreationData objects.

    CounterCreationDataCollection()

    CounterCreationDataCollection(value: CounterCreationDataCollection)

    CounterCreationDataCollection(value: Array[CounterCreationData])
    """

    def Add(self, value):
        """
        Add(self: CounterCreationDataCollection, value: CounterCreationData) -> int

            Adds an instance of the System.Diagnostics.CounterCreationData class to the collection.

            value: A System.Diagnostics.CounterCreationData object to append to the existing collection.

            Returns: The index of the new System.Diagnostics.CounterCreationData object.
        """
        ...
    def AddRange(self, value):
        """
        AddRange(self: CounterCreationDataCollection, value: Array[CounterCreationData])

            Adds the specified array of System.Diagnostics.CounterCreationData instances to the collection.

            value: An array of System.Diagnostics.CounterCreationData instances to append to the existing collection.

        AddRange(self: CounterCreationDataCollection, value: CounterCreationDataCollection)

            Adds the specified collection of System.Diagnostics.CounterCreationData instances to the collection.

            value: A collection of System.Diagnostics.CounterCreationData instances to append to the existing collection.
        """
        ...
    def Contains(self, value):
        """
        Contains(self: CounterCreationDataCollection, value: CounterCreationData) -> bool

            Determines whether a System.Diagnostics.CounterCreationData instance exists in the collection.

            value: The System.Diagnostics.CounterCreationData object to find in the collection.

            Returns: ue if the specified System.Diagnostics.CounterCreationData object exists in the collection; otherwise, lse.
        """
        ...
    def CopyTo(self, array, index):
        """
        CopyTo(self: CounterCreationDataCollection, array: Array[CounterCreationData], index: int)

            Copies the elements of the System.Diagnostics.CounterCreationData to an array, starting at the specified index of the array.

            array: An array of System.Diagnostics.CounterCreationData instances to add to the collection.

            index: The location at which to add the new instances.
        """
        ...
    def IndexOf(self, value):
        """
        IndexOf(self: CounterCreationDataCollection, value: CounterCreationData) -> int

            Returns the index of a System.Diagnostics.CounterCreationData object in the collection.

            value: The System.Diagnostics.CounterCreationData object to locate in the collection.

            Returns: The zero-based index of the specified System.Diagnostics.CounterCreationData, if it is found, in the collection; otherwise, -1.
        """
        ...
    def Insert(self, index, value):
        """
        Insert(self: CounterCreationDataCollection, index: int, value: CounterCreationData)

            Inserts a System.Diagnostics.CounterCreationData object into the collection, at the specified index.

            index: The zero-based index of the location at which the System.Diagnostics.CounterCreationData is to be inserted.

            value: The System.Diagnostics.CounterCreationData to insert into the collection.
        """
        ...
    def Remove(self, value):
        """
        Remove(self: CounterCreationDataCollection, value: CounterCreationData)

            Removes a System.Diagnostics.CounterCreationData object from the collection.

            value: The System.Diagnostics.CounterCreationData to remove from the collection.
        """
        ...
    def __add__(self, *args):  # cannot find CLR method
        """x.__add__(y) <==> x+y"""
        ...
    def __getitem__(self, *args):  # cannot find CLR method
        """x.__getitem__(y) <==> x[y]"""
        ...
    def __setitem__(self, *args):  # cannot find CLR method
        """x.__setitem__(i, y) <==> x[i]="""
        ...
    @property
    def InnerList(self):
        """Gets an System.Collections.ArrayList containing the list of elements in the System.Collections.CollectionBase instance."""
        ...
    @property
    def List(self):
        """Gets an System.Collections.IList containing the list of elements in the System.Collections.CollectionBase instance."""
        ...

class CounterSample:  # skipped bases: <type 'object'>
    """
    Defines a structure that holds the raw data for a performance counter.

    CounterSample(rawValue: Int64, baseValue: Int64, counterFrequency: Int64, systemFrequency: Int64, timeStamp: Int64, timeStamp100nSec: Int64, counterType: PerformanceCounterType)

    CounterSample(rawValue: Int64, baseValue: Int64, counterFrequency: Int64, systemFrequency: Int64, timeStamp: Int64, timeStamp100nSec: Int64, counterType: PerformanceCounterType, counterTimeStamp: Int64)
    """

    @staticmethod
    def Calculate(counterSample, nextCounterSample=None):
        """
        Calculate(counterSample: CounterSample) -> Single

            Calculates the performance data of the counter, using a single sample point. This method is generally used for uncalculated performance counter types.

            counterSample: The System.Diagnostics.CounterSample structure to use as a base point for calculating performance data.

            Returns: The calculated performance value.

        Calculate(counterSample: CounterSample, nextCounterSample: CounterSample) -> Single

            Calculates the performance data of the counter, using two sample points. This method is generally used for calculated performance counter types, such as averages.

            counterSample: The System.Diagnostics.CounterSample structure to use as a base point for calculating performance data.

            nextCounterSample: The System.Diagnostics.CounterSample structure to use as an ending point for calculating performance data.

            Returns: The calculated performance value.
        """
        ...
    def Equals(self, *__args):
        """
        Equals(self: CounterSample, o: object) -> bool

            Indicates whether the specified structure is a System.Diagnostics.CounterSample structure and is identical to the current System.Diagnostics.CounterSample structure.

            o: The System.Diagnostics.CounterSample structure to be compared with the current structure.

            Returns: ue if o is a System.Diagnostics.CounterSample structure and is identical to the current instance; otherwise, lse.

        Equals(self: CounterSample, sample: CounterSample) -> bool

            Indicates whether the specified System.Diagnostics.CounterSample structure is equal to the current System.Diagnostics.CounterSample structure.

            sample: The System.Diagnostics.CounterSample structure to be compared with this instance.

            Returns: ue if sample is equal to the current instance; otherwise, lse.
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: CounterSample) -> int

            Gets a hash code for the current counter sample.

            Returns: A hash code for the current counter sample.
        """
        ...
    def __eq__(self, *args):  # cannot find CLR method
        """x.__eq__(y) <==> x==y"""
        ...
    def __ne__(self, *args): ...
    @property
    def BaseValue(self):
        """
        Gets an optional, base raw value for the counter.

        Get: BaseValue(self: CounterSample) -> Int64
        """
        ...
    @property
    def CounterFrequency(self):
        """
        Gets the raw counter frequency.

        Get: CounterFrequency(self: CounterSample) -> Int64
        """
        ...
    @property
    def CounterTimeStamp(self):
        """
        Gets the counter's time stamp.

        Get: CounterTimeStamp(self: CounterSample) -> Int64
        """
        ...
    @property
    def CounterType(self):
        """
        Gets the performance counter type.

        Get: CounterType(self: CounterSample) -> PerformanceCounterType
        """
        ...
    @property
    def RawValue(self):
        """
        Gets the raw value of the counter.

        Get: RawValue(self: CounterSample) -> Int64
        """
        ...
    @property
    def SystemFrequency(self):
        """
        Gets the raw system frequency.

        Get: SystemFrequency(self: CounterSample) -> Int64
        """
        ...
    @property
    def TimeStamp(self):
        """
        Gets the raw time stamp.

        Get: TimeStamp(self: CounterSample) -> Int64
        """
        ...
    @property
    def TimeStamp100nSec(self):
        """
        Gets the raw, high-fidelity time stamp.

        Get: TimeStamp100nSec(self: CounterSample) -> Int64
        """
        ...
    Empty = None

class CounterSampleCalculator:  # skipped bases: <type 'object'>
    """Provides a set of utility functions for interpreting performance counter data."""

    @staticmethod
    def ComputeCounterValue(*__args):
        """
        ComputeCounterValue(newSample: CounterSample) -> Single

            Computes the calculated value of a single raw counter sample.

            newSample: A System.Diagnostics.CounterSample that indicates the most recent sample the system has taken.

            Returns: A floating-point representation of the performance counter's calculated value.

        ComputeCounterValue(oldSample: CounterSample, newSample: CounterSample) -> Single

            Computes the calculated value of two raw counter samples.

            oldSample: A System.Diagnostics.CounterSample that indicates a previous sample the system has taken.

            newSample: A System.Diagnostics.CounterSample that indicates the most recent sample the system has taken.

            Returns: A floating-point representation of the performance counter's calculated value.
        """
        ...
    __all__ = [
        "ComputeCounterValue",
    ]

class DataReceivedEventArgs(EventArgs):
    """Provides data for the System.Diagnostics.Process.OutputDataReceived and System.Diagnostics.Process.ErrorDataReceived events."""

    @property
    def Data(self):
        """
        Gets the line of characters that was written to a redirected System.Diagnostics.Process output stream.

        Get: Data(self: DataReceivedEventArgs) -> str
        """
        ...

class DataReceivedEventHandler(MulticastDelegate):  # skipped bases: <type 'ICloneable'>, <type 'ISerializable'>
    """
    Represents the method that will handle the System.Diagnostics.Process.OutputDataReceived event or System.Diagnostics.Process.ErrorDataReceived event of a System.Diagnostics.Process.

    DataReceivedEventHandler(object: object, method: IntPtr)
    """

    def BeginInvoke(self, sender, e, callback, object):
        """BeginInvoke(self: DataReceivedEventHandler, sender: object, e: DataReceivedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult"""
        ...
    def EndInvoke(self, result):
        """EndInvoke(self: DataReceivedEventHandler, result: IAsyncResult)"""
        ...
    def Invoke(self, sender, e):
        """Invoke(self: DataReceivedEventHandler, sender: object, e: DataReceivedEventArgs)"""
        ...

class Debug:  # skipped bases: <type 'object'>
    """Provides a set of methods and properties that help debug your code."""

    @staticmethod
    def Assert(condition, message=None, *__args):
        """
        Assert(condition: bool)

            Checks for a condition; if the condition is lse, displays a message box that shows the call stack.

            condition: The conditional expression to evaluate. If the condition is ue, a failure message is not sent and the message box is not displayed.

        Assert(condition: bool, message: str)

            Checks for a condition; if the condition is lse, outputs a specified message and displays a message box that shows the call stack.

            condition: The conditional expression to evaluate. If the condition is ue, the specified message is not sent and the message box is not displayed.

            message: The message to send to the System.Diagnostics.Trace.Listeners collection.

        Assert(condition: bool, message: str, detailMessage: str)

            Checks for a condition; if the condition is lse, outputs two specified messages and displays a message box that shows the call stack.

            condition: The conditional expression to evaluate. If the condition is ue, the specified messages are not sent and the message box is not displayed.

            message: The message to send to the System.Diagnostics.Trace.Listeners collection.

            detailMessage: The detailed message to send to the System.Diagnostics.Trace.Listeners collection.

        Assert(condition: bool, message: str, detailMessageFormat: str, *args: Array[object])

            Checks for a condition; if the condition is lse, outputs two messages (simple and formatted) and displays a message box that shows the call stack.

            condition: The conditional expression to evaluate. If the condition is ue, the specified messages are not sent and the message box is not displayed.

            message: The message to send to the System.Diagnostics.Trace.Listeners collection.

            detailMessageFormat: The composite format string (see Remarks) to send to the System.Diagnostics.Trace.Listeners collection. This message contains text intermixed with zero or more format items, which correspond to objects in the args array.

            args: An object array that contains zero or more objects to format.
        """
        ...
    @staticmethod
    def Close():
        """
        Close()

            Flushes the output buffer and then calls the ose method on each of the System.Diagnostics.Debug.Listeners.
        """
        ...
    @staticmethod
    def Fail(message, detailMessage=None):
        """
        Fail(message: str)

            Emits the specified error message.

            message: A message to emit.

        Fail(message: str, detailMessage: str)

            Emits an error message and a detailed error message.

            message: A message to emit.

            detailMessage: A detailed message to emit.
        """
        ...
    @staticmethod
    def Flush():
        """
        Flush()

            Flushes the output buffer and causes buffered data to write to the System.Diagnostics.Debug.Listeners collection.
        """
        ...
    @staticmethod
    def Indent():
        """
        Indent()

            Increases the current System.Diagnostics.Debug.IndentLevel by one.
        """
        ...
    @staticmethod
    def Print(*__args):
        """
        Print(message: str)

            Writes a message followed by a line terminator to the trace listeners in the System.Diagnostics.Debug.Listeners collection.

            message: The message to write.

        Print(format: str, *args: Array[object])

            Writes a formatted string followed by a line terminator to the trace listeners in the System.Diagnostics.Debug.Listeners collection.

            format: A composite format string (see Remarks) that contains text intermixed with zero or more format items, which correspond to objects in the args array.

            args: An object array containing zero or more objects to format.
        """
        ...
    @staticmethod
    def Unindent():
        """
        Unindent()

            Decreases the current System.Diagnostics.Debug.IndentLevel by one.
        """
        ...
    @staticmethod
    def Write(*__args):
        """
        Write(message: str)

            Writes a message to the trace listeners in the System.Diagnostics.Debug.Listeners collection.

            message: A message to write.

        Write(value: object)

            Writes the value of the object's System.Object.ToString method to the trace listeners in the System.Diagnostics.Debug.Listeners collection.

            value: An object whose name is sent to the System.Diagnostics.Debug.Listeners.

        Write(message: str, category: str)

            Writes a category name and message to the trace listeners in the System.Diagnostics.Debug.Listeners collection.

            message: A message to write.

            category: A category name used to organize the output.

        Write(value: object, category: str)

            Writes a category name and the value of the object's System.Object.ToString method to the trace listeners in the System.Diagnostics.Debug.Listeners collection.

            value: An object whose name is sent to the System.Diagnostics.Debug.Listeners.

            category: A category name used to organize the output.
        """
        ...
    @staticmethod
    def WriteIf(condition, *__args):
        """
        WriteIf(condition: bool, message: str)

            Writes a message to the trace listeners in the System.Diagnostics.Debug.Listeners collection if a condition is ue.

            condition: The conditional expression to evaluate. If the condition is ue, the message is written to the trace listeners in the collection.

            message: A message to write.

        WriteIf(condition: bool, value: object)

            Writes the value of the object's System.Object.ToString method to the trace listeners in the System.Diagnostics.Debug.Listeners collection if a condition is ue.

            condition: The conditional expression to evaluate. If the condition is ue, the value is written to the trace listeners in the collection.

            value: An object whose name is sent to the System.Diagnostics.Debug.Listeners.

        WriteIf(condition: bool, message: str, category: str)

            Writes a category name and message to the trace listeners in the System.Diagnostics.Debug.Listeners collection if a condition is ue.

            condition: The conditional expression to evaluate. If the condition is ue, the category name and message are written to the trace listeners in the collection.

            message: A message to write.

            category: A category name used to organize the output.

        WriteIf(condition: bool, value: object, category: str)

            Writes a category name and the value of the object's System.Object.ToString method to the trace listeners in the System.Diagnostics.Debug.Listeners collection if a condition is ue.

            condition: The conditional expression to evaluate. If the condition is ue, the category name and value are written to the trace listeners in the collection.

            value: An object whose name is sent to the System.Diagnostics.Debug.Listeners.

            category: A category name used to organize the output.
        """
        ...
    @staticmethod
    def WriteLine(*__args):
        """
        WriteLine(message: str)

            Writes a message followed by a line terminator to the trace listeners in the System.Diagnostics.Debug.Listeners collection.

            message: A message to write.

        WriteLine(value: object)

            Writes the value of the object's System.Object.ToString method to the trace listeners in the System.Diagnostics.Debug.Listeners collection.

            value: An object whose name is sent to the System.Diagnostics.Debug.Listeners.

        WriteLine(message: str, category: str)

            Writes a category name and message to the trace listeners in the System.Diagnostics.Debug.Listeners collection.

            message: A message to write.

            category: A category name used to organize the output.

        WriteLine(value: object, category: str)

            Writes a category name and the value of the object's System.Object.ToString method to the trace listeners in the System.Diagnostics.Debug.Listeners collection.

            value: An object whose name is sent to the System.Diagnostics.Debug.Listeners.

            category: A category name used to organize the output.

        WriteLine(format: str, *args: Array[object])

            Writes a formatted message followed by a line terminator to the trace listeners in the System.Diagnostics.Debug.Listeners collection.

            format: A composite format string (see Remarks) that contains text intermixed with zero or more format items, which correspond to objects in the args array.

            args: An object array that contains zero or more objects to format.
        """
        ...
    @staticmethod
    def WriteLineIf(condition, *__args):
        """
        WriteLineIf(condition: bool, message: str)

            Writes a message to the trace listeners in the System.Diagnostics.Debug.Listeners collection if a condition is ue.

            condition: The conditional expression to evaluate. If the condition is ue, the message is written to the trace listeners in the collection.

            message: A message to write.

        WriteLineIf(condition: bool, value: object)

            Writes the value of the object's System.Object.ToString method to the trace listeners in the System.Diagnostics.Debug.Listeners collection if a condition is ue.

            condition: The conditional expression to evaluate. If the condition is ue, the value is written to the trace listeners in the collection.

            value: An object whose name is sent to the System.Diagnostics.Debug.Listeners.

        WriteLineIf(condition: bool, message: str, category: str)

            Writes a category name and message to the trace listeners in the System.Diagnostics.Debug.Listeners collection if a condition is ue.

            condition: ue to cause a message to be written; otherwise, lse.

            message: A message to write.

            category: A category name used to organize the output.

        WriteLineIf(condition: bool, value: object, category: str)

            Writes a category name and the value of the object's System.Object.ToString method to the trace listeners in the System.Diagnostics.Debug.Listeners collection if a condition is ue.

            condition: The conditional expression to evaluate. If the condition is ue, the category name and value are written to the trace listeners in the collection.

            value: An object whose name is sent to the System.Diagnostics.Debug.Listeners.

            category: A category name used to organize the output.
        """
        ...
    AutoFlush = False
    IndentLevel = 0
    IndentSize = 4
    Listeners = None
    __all__ = [
        "Assert",
        "Close",
        "Fail",
        "Flush",
        "Indent",
        "Print",
        "Unindent",
        "Write",
        "WriteIf",
        "WriteLine",
        "WriteLineIf",
    ]

class DebuggableAttribute(Attribute):  # skipped bases: <type '_Attribute'>
    """
    Modifies code generation for runtime just-in-time (JIT) debugging. This class cannot be inherited.

    DebuggableAttribute(isJITTrackingEnabled: bool, isJITOptimizerDisabled: bool)

    DebuggableAttribute(modes: DebuggingModes)
    """

    def DebuggingModes(self, *args):  # cannot find CLR method
        """enum (flags) DebuggingModes, values: Default (1), DisableOptimizations (256), EnableEditAndContinue (4), IgnoreSymbolStoreSequencePoints (2), None (0)"""
        ...
    @staticmethod  # known case of __new__
    def __new__(cls, *__args):
        """
        __new__(cls: type, isJITTrackingEnabled: bool, isJITOptimizerDisabled: bool)

        __new__(cls: type, modes: DebuggingModes)
        """
        ...
    @property
    def DebuggingFlags(self):
        """
        Gets the debugging modes for the attribute.

        Get: DebuggingFlags(self: DebuggableAttribute) -> DebuggingModes
        """
        ...
    @property
    def IsJITOptimizerDisabled(self):
        """
        Gets a value that indicates whether the runtime optimizer is disabled.

        Get: IsJITOptimizerDisabled(self: DebuggableAttribute) -> bool
        """
        ...
    @property
    def IsJITTrackingEnabled(self):
        """
        Gets a value that indicates whether the runtime will track information during code generation for the debugger.

        Get: IsJITTrackingEnabled(self: DebuggableAttribute) -> bool
        """
        ...
    DebuggingModes = None

class Debugger:  # skipped bases: <type 'object'>
    """
    Enables communication with a debugger. This class cannot be inherited.

    Debugger()
    """

    @staticmethod
    def Break():
        """
        Break()

            Signals a breakpoint to an attached debugger.
        """
        ...
    @staticmethod
    def IsLogging():
        """
        IsLogging() -> bool

            Checks to see if logging is enabled by an attached debugger.

            Returns: ue if a debugger is attached and logging is enabled; otherwise, lse. The attached debugger is the registered managed debugger in the gManagedDebugger registry key. For more information on this key, see Enabling JIT-Attach Debugging.
        """
        ...
    @staticmethod
    def Launch():
        """
        Launch() -> bool

            Launches and attaches a debugger to the process.

            Returns: ue if the startup is successful or if the debugger is already attached; otherwise, lse.
        """
        ...
    @staticmethod
    def Log(level, category, message):
        """
        Log(level: int, category: str, message: str)

            Posts a message for the attached debugger.

            level: A description of the importance of the message.

            category: The category of the message.

            message: The message to show.
        """
        ...
    @staticmethod
    def NotifyOfCrossThreadDependency():
        """
        NotifyOfCrossThreadDependency()

            Notifies a debugger that execution is about to enter a path that involves a cross-thread dependency.
        """
        ...
    DefaultCategory = None
    IsAttached = False

class DebuggerBrowsableAttribute(Attribute):  # skipped bases: <type '_Attribute'>
    """
    Determines if and how a member is displayed in the debugger variable windows. This class cannot be inherited.

    DebuggerBrowsableAttribute(state: DebuggerBrowsableState)
    """

    @staticmethod  # known case of __new__
    def __new__(cls, state):
        """__new__(cls: type, state: DebuggerBrowsableState)"""
        ...
    @property
    def State(self):
        """
        Gets the display state for the attribute.

        Get: State(self: DebuggerBrowsableAttribute) -> DebuggerBrowsableState
        """
        ...

class DebuggerBrowsableState(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Provides display instructions for the debugger.

    enum DebuggerBrowsableState, values: Collapsed (2), Never (0), RootHidden (3)
    """

    Collapsed = None
    Never = None
    RootHidden = None
    value__ = None

class DebuggerDisplayAttribute(Attribute):  # skipped bases: <type '_Attribute'>
    """
    Determines how a class or field is displayed in the debugger variable windows.

    DebuggerDisplayAttribute(value: str)
    """

    @staticmethod  # known case of __new__
    def __new__(cls, value):
        """__new__(cls: type, value: str)"""
        ...
    @property
    def Name(self):
        """
        Gets or sets the name to display in the debugger variable windows.

        Get: Name(self: DebuggerDisplayAttribute) -> str

        Set: Name(self: DebuggerDisplayAttribute) = value
        """
        ...
    @property
    def Target(self):
        """
        Gets or sets the type of the attribute's target.

        Get: Target(self: DebuggerDisplayAttribute) -> Type

        Set: Target(self: DebuggerDisplayAttribute) = value
        """
        ...
    @property
    def TargetTypeName(self):
        """
        Gets or sets the type name of the attribute's target.

        Get: TargetTypeName(self: DebuggerDisplayAttribute) -> str

        Set: TargetTypeName(self: DebuggerDisplayAttribute) = value
        """
        ...
    @property
    def Type(self):
        """
        Gets or sets the string to display in the type column of the debugger variable windows.

        Get: Type(self: DebuggerDisplayAttribute) -> str

        Set: Type(self: DebuggerDisplayAttribute) = value
        """
        ...
    @property
    def Value(self):
        """
        Gets the string to display in the value column of the debugger variable windows.

        Get: Value(self: DebuggerDisplayAttribute) -> str
        """
        ...

class DebuggerHiddenAttribute(Attribute):  # skipped bases: <type '_Attribute'>
    """
    Specifies the System.Diagnostics.DebuggerHiddenAttribute. This class cannot be inherited.

    DebuggerHiddenAttribute()
    """

    pass

class DebuggerNonUserCodeAttribute(Attribute):  # skipped bases: <type '_Attribute'>
    """
    Identifies a type or member that is not part of the user code for an application.

    DebuggerNonUserCodeAttribute()
    """

    pass

class DebuggerStepperBoundaryAttribute(Attribute):  # skipped bases: <type '_Attribute'>
    """
    Indicates the code following the attribute is to be executed in run, not step, mode.

    DebuggerStepperBoundaryAttribute()
    """

    pass

class DebuggerStepThroughAttribute(Attribute):  # skipped bases: <type '_Attribute'>
    """
    Instructs the debugger to step through the code instead of stepping into the code. This class cannot be inherited.

    DebuggerStepThroughAttribute()
    """

    pass

class DebuggerTypeProxyAttribute(Attribute):  # skipped bases: <type '_Attribute'>
    """
    Specifies the display proxy for a type.

    DebuggerTypeProxyAttribute(type: Type)

    DebuggerTypeProxyAttribute(typeName: str)
    """

    @staticmethod  # known case of __new__
    def __new__(cls, *__args):
        """
        __new__(cls: type, type: Type)

        __new__(cls: type, typeName: str)
        """
        ...
    @property
    def ProxyTypeName(self):
        """
        Gets the type name of the proxy type.

        Get: ProxyTypeName(self: DebuggerTypeProxyAttribute) -> str
        """
        ...
    @property
    def Target(self):
        """
        Gets or sets the target type for the attribute.

        Get: Target(self: DebuggerTypeProxyAttribute) -> Type

        Set: Target(self: DebuggerTypeProxyAttribute) = value
        """
        ...
    @property
    def TargetTypeName(self):
        """
        Gets or sets the name of the target type.

        Get: TargetTypeName(self: DebuggerTypeProxyAttribute) -> str

        Set: TargetTypeName(self: DebuggerTypeProxyAttribute) = value
        """
        ...

class DebuggerVisualizerAttribute(Attribute):  # skipped bases: <type '_Attribute'>
    """
    Specifies that the type has a visualizer. This class cannot be inherited.

    DebuggerVisualizerAttribute(visualizerTypeName: str)

    DebuggerVisualizerAttribute(visualizerTypeName: str, visualizerObjectSourceTypeName: str)

    DebuggerVisualizerAttribute(visualizerTypeName: str, visualizerObjectSource: Type)

    DebuggerVisualizerAttribute(visualizer: Type)

    DebuggerVisualizerAttribute(visualizer: Type, visualizerObjectSource: Type)

    DebuggerVisualizerAttribute(visualizer: Type, visualizerObjectSourceTypeName: str)
    """

    @staticmethod  # known case of __new__
    def __new__(cls, *__args):
        """
        __new__(cls: type, visualizerTypeName: str)

        __new__(cls: type, visualizerTypeName: str, visualizerObjectSourceTypeName: str)

        __new__(cls: type, visualizerTypeName: str, visualizerObjectSource: Type)

        __new__(cls: type, visualizer: Type)

        __new__(cls: type, visualizer: Type, visualizerObjectSource: Type)

        __new__(cls: type, visualizer: Type, visualizerObjectSourceTypeName: str)
        """
        ...
    @property
    def Description(self):
        """
        Gets or sets the description of the visualizer.

        Get: Description(self: DebuggerVisualizerAttribute) -> str

        Set: Description(self: DebuggerVisualizerAttribute) = value
        """
        ...
    @property
    def Target(self):
        """
        Gets or sets the target type when the attribute is applied at the assembly level.

        Get: Target(self: DebuggerVisualizerAttribute) -> Type

        Set: Target(self: DebuggerVisualizerAttribute) = value
        """
        ...
    @property
    def TargetTypeName(self):
        """
        Gets or sets the fully qualified type name when the attribute is applied at the assembly level.

        Get: TargetTypeName(self: DebuggerVisualizerAttribute) -> str

        Set: TargetTypeName(self: DebuggerVisualizerAttribute) = value
        """
        ...
    @property
    def VisualizerObjectSourceTypeName(self):
        """
        Gets the fully qualified type name of the visualizer object source.

        Get: VisualizerObjectSourceTypeName(self: DebuggerVisualizerAttribute) -> str
        """
        ...
    @property
    def VisualizerTypeName(self):
        """
        Gets the fully qualified type name of the visualizer.

        Get: VisualizerTypeName(self: DebuggerVisualizerAttribute) -> str
        """
        ...

class DefaultTraceListener(TraceListener):  # skipped bases: <type 'IDisposable'>
    """
    Provides the default output methods and behavior for tracing.

    DefaultTraceListener()
    """

    @property
    def AssertUiEnabled(self):
        """
        Gets or sets a value indicating whether the application is running in user-interface mode.

        Get: AssertUiEnabled(self: DefaultTraceListener) -> bool

        Set: AssertUiEnabled(self: DefaultTraceListener) = value
        """
        ...
    @property
    def LogFileName(self):
        """
        Gets or sets the name of a log file to write trace or debug messages to.

        Get: LogFileName(self: DefaultTraceListener) -> str

        Set: LogFileName(self: DefaultTraceListener) = value
        """
        ...
    @property
    def NeedIndent(self):
        """Gets or sets a value indicating whether to indent the output."""
        ...

class DelimitedListTraceListener(TextWriterTraceListener):  # skipped bases: <type 'IDisposable'>
    """
    Directs tracing or debugging output to a text writer, such as a stream writer, or to a stream, such as a file stream.

    DelimitedListTraceListener(stream: Stream)

    DelimitedListTraceListener(stream: Stream, name: str)

    DelimitedListTraceListener(writer: TextWriter)

    DelimitedListTraceListener(writer: TextWriter, name: str)

    DelimitedListTraceListener(fileName: str)

    DelimitedListTraceListener(fileName: str, name: str)
    """

    def TraceData(self, eventCache, source, eventType, id, data):
        """
        TraceData(self: DelimitedListTraceListener, eventCache: TraceEventCache, source: str, eventType: TraceEventType, id: int, data: object)

            Writes trace information, a data object, and event information to the output file or stream.

            eventCache: A System.Diagnostics.TraceEventCache object that contains the current process ID, thread ID, and stack trace information.

            source: A name used to identify the output, typically the name of the application that generated the trace event.

            eventType: One of the System.Diagnostics.TraceEventType values specifying the type of event that has caused the trace.

            id: A numeric identifier for the event.

            data: A data object to write to the output file or stream.

        TraceData(self: DelimitedListTraceListener, eventCache: TraceEventCache, source: str, eventType: TraceEventType, id: int, *data: Array[object])

            Writes trace information, an array of data objects, and event information to the output file or stream.

            eventCache: A System.Diagnostics.TraceEventCache object that contains the current process ID, thread ID, and stack trace information.

            source: A name used to identify the output, typically the name of the application that generated the trace event.

            eventType: One of the System.Diagnostics.TraceEventType values specifying the type of event that has caused the trace.

            id: A numeric identifier for the event.

            data: An array of data objects to write to the output file or stream.
        """
        ...
    def TraceEvent(self, eventCache, source, eventType, id, *__args):
        """
        TraceEvent(self: DelimitedListTraceListener, eventCache: TraceEventCache, source: str, eventType: TraceEventType, id: int, format: str, *args: Array[object])

            Writes trace information, a formatted array of objects, and event information to the output file or stream.

            eventCache: A System.Diagnostics.TraceEventCache object that contains the current process ID, thread ID, and stack trace information.

            source: A name used to identify the output, typically the name of the application that generated the trace event.

            eventType: One of the System.Diagnostics.TraceEventType values specifying the type of event that has caused the trace.

            id: A numeric identifier for the event.

            format: A format string that contains zero or more format items that correspond to objects in the args array.

            args: An array containing zero or more objects to format.

        TraceEvent(self: DelimitedListTraceListener, eventCache: TraceEventCache, source: str, eventType: TraceEventType, id: int, message: str)

            Writes trace information, a message, and event information to the output file or stream.

            eventCache: A System.Diagnostics.TraceEventCache object that contains the current process ID, thread ID, and stack trace information.

            source: A name used to identify the output, typically the name of the application that generated the trace event.

            eventType: One of the System.Diagnostics.TraceEventType values specifying the type of event that has caused the trace.

            id: A numeric identifier for the event.

            message: The trace message to write to the output file or stream.
        """
        ...
    @property
    def Delimiter(self):
        """
        Gets or sets the delimiter for the delimited list.

        Get: Delimiter(self: DelimitedListTraceListener) -> str

        Set: Delimiter(self: DelimitedListTraceListener) = value
        """
        ...
    @property
    def NeedIndent(self):
        """Gets or sets a value indicating whether to indent the output."""
        ...

class DiagnosticsConfigurationHandler(object, IConfigurationSectionHandler):
    """
    Handles the diagnostics section of configuration files.

    DiagnosticsConfigurationHandler()
    """

    pass

class EntryWrittenEventArgs(EventArgs):
    """
    Provides data for the System.Diagnostics.EventLog.EntryWritten event.

    EntryWrittenEventArgs()

    EntryWrittenEventArgs(entry: EventLogEntry)
    """

    @staticmethod  # known case of __new__
    def __new__(cls, entry=None):
        """
        __new__(cls: type)

        __new__(cls: type, entry: EventLogEntry)
        """
        ...
    @property
    def Entry(self):
        """
        Gets the event log entry that was written to the log.

        Get: Entry(self: EntryWrittenEventArgs) -> EventLogEntry
        """
        ...

class EntryWrittenEventHandler(MulticastDelegate):  # skipped bases: <type 'ICloneable'>, <type 'ISerializable'>
    """
    Represents the method that will handle the System.Diagnostics.EventLog.EntryWritten event of an System.Diagnostics.EventLog.

    EntryWrittenEventHandler(object: object, method: IntPtr)
    """

    def BeginInvoke(self, sender, e, callback, object):
        """BeginInvoke(self: EntryWrittenEventHandler, sender: object, e: EntryWrittenEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult"""
        ...
    def EndInvoke(self, result):
        """EndInvoke(self: EntryWrittenEventHandler, result: IAsyncResult)"""
        ...
    def Invoke(self, sender, e):
        """Invoke(self: EntryWrittenEventHandler, sender: object, e: EntryWrittenEventArgs)"""
        ...

class EventInstance:  # skipped bases: <type 'object'>
    """
    Represents language-neutral information for an event log entry.

    EventInstance(instanceId: Int64, categoryId: int)

    EventInstance(instanceId: Int64, categoryId: int, entryType: EventLogEntryType)
    """

    @property
    def CategoryId(self):
        """
        Gets or sets the resource identifier that specifies the application-defined category of the event entry.

        Get: CategoryId(self: EventInstance) -> int

        Set: CategoryId(self: EventInstance) = value
        """
        ...
    @property
    def EntryType(self):
        """
        Gets or sets the event type of the event log entry.

        Get: EntryType(self: EventInstance) -> EventLogEntryType

        Set: EntryType(self: EventInstance) = value
        """
        ...
    @property
    def InstanceId(self):
        """
        Gets or sets the resource identifier that designates the message text of the event entry.

        Get: InstanceId(self: EventInstance) -> Int64

        Set: InstanceId(self: EventInstance) = value
        """
        ...

class EventLog(Component, ISupportInitialize):  # skipped bases: <type 'IComponent'>, <type 'IDisposable'>
    """
    Provides interaction with Windows event logs.

    EventLog()

    EventLog(logName: str)

    EventLog(logName: str, machineName: str)

    EventLog(logName: str, machineName: str, source: str)
    """

    def Clear(self):
        """
        Clear(self: EventLog)

            Removes all entries from the event log.
        """
        ...
    def Close(self):
        """
        Close(self: EventLog)

            Closes the event log and releases read and write handles.
        """
        ...
    @staticmethod
    def CreateEventSource(*__args):
        """
        CreateEventSource(source: str, logName: str, machineName: str)

            Establishes the specified source name as a valid event source for writing entries to a log on the specified computer. This method can also be used to create a new custom log on the specified computer.

            source: The source by which the application is registered on the specified computer.

            logName: The name of the log the source's entries are written to. Possible values include Application, System, or a custom event log. If you do not specify a value, logName defaults to Application.

            machineName: The name of the computer to register this event source with, or "." for the local computer.

        CreateEventSource(source: str, logName: str)

            Establishes the specified source name as a valid event source for writing entries to a log on the local computer. This method can also create a new custom log on the local computer.

            source: The source name by which the application is registered on the local computer.

            logName: The name of the log the source's entries are written to. Possible values include Application, System, or a custom event log.

        CreateEventSource(sourceData: EventSourceCreationData)

            Establishes a valid event source for writing localized event messages, using the specified configuration properties for the event source and the corresponding event log.

            sourceData: The configuration properties for the event source and its target event log.
        """
        ...
    @staticmethod
    def Delete(logName, machineName=None):
        """
        Delete(logName: str)

            Removes an event log from the local computer.

            logName: The name of the log to delete. Possible values include: Application, Security, System, and any custom event logs on the computer.

        Delete(logName: str, machineName: str)

            Removes an event log from the specified computer.

            logName: The name of the log to delete. Possible values include: Application, Security, System, and any custom event logs on the specified computer.

            machineName: The name of the computer to delete the log from, or "." for the local computer.
        """
        ...
    @staticmethod
    def DeleteEventSource(source, machineName=None):
        """
        DeleteEventSource(source: str)

            Removes the event source registration from the event log of the local computer.

            source: The name by which the application is registered in the event log system.

        DeleteEventSource(source: str, machineName: str)

            Removes the application's event source registration from the specified computer.

            source: The name by which the application is registered in the event log system.

            machineName: The name of the computer to remove the registration from, or "." for the local computer.
        """
        ...
    @staticmethod
    def Exists(logName, machineName=None):
        """
        Exists(logName: str) -> bool

            Determines whether the log exists on the local computer.

            logName: The name of the log to search for. Possible values include: Application, Security, System, other application-specific logs (such as those associated with Active Directory), or any custom log on the computer.

            Returns: ue if the log exists on the local computer; otherwise, lse.

        Exists(logName: str, machineName: str) -> bool

            Determines whether the log exists on the specified computer.

            logName: The log for which to search. Possible values include: Application, Security, System, other application-specific logs (such as those associated with Active Directory), or any custom log on the computer.

            machineName: The name of the computer on which to search for the log, or "." for the local computer.

            Returns: ue if the log exists on the specified computer; otherwise, lse.
        """
        ...
    @staticmethod
    def GetEventLogs(machineName=None):
        """
        GetEventLogs() -> Array[EventLog]

            Searches for all event logs on the local computer and creates an array of System.Diagnostics.EventLog objects that contain the list.

            Returns: An array of type System.Diagnostics.EventLog that represents the logs on the local computer.

        GetEventLogs(machineName: str) -> Array[EventLog]

            Searches for all event logs on the given computer and creates an array of System.Diagnostics.EventLog objects that contain the list.

            machineName: The computer on which to search for event logs.

            Returns: An array of type System.Diagnostics.EventLog that represents the logs on the given computer.
        """
        ...
    @staticmethod
    def LogNameFromSourceName(source, machineName):
        """
        LogNameFromSourceName(source: str, machineName: str) -> str

            Gets the name of the log to which the specified source is registered.

            source: The name of the event source.

            machineName: The name of the computer on which to look, or "." for the local computer.

            Returns: The name of the log associated with the specified source in the registry.
        """
        ...
    def ModifyOverflowPolicy(self, action, retentionDays):
        """
        ModifyOverflowPolicy(self: EventLog, action: OverflowAction, retentionDays: int)

            Changes the configured behavior for writing new entries when the event log reaches its maximum file size.

            action: The overflow behavior for writing new entries to the event log.

            retentionDays: The minimum number of days each event log entry is retained. This parameter is used only if action is set to System.Diagnostics.OverflowAction.OverwriteOlder.
        """
        ...
    def RegisterDisplayName(self, resourceFile, resourceId):
        """
        RegisterDisplayName(self: EventLog, resourceFile: str, resourceId: Int64)

            Specifies the localized name of the event log, which is displayed in the server Event Viewer.

            resourceFile: The fully specified path to a localized resource file.

            resourceId: The resource identifier that indexes a localized string within the resource file.
        """
        ...
    @staticmethod
    def SourceExists(source, machineName=None):
        """
        SourceExists(source: str, machineName: str) -> bool

            Determines whether an event source is registered on a specified computer.

            source: The name of the event source.

            machineName: The name the computer on which to look, or "." for the local computer.

            Returns: ue if the event source is registered on the given computer; otherwise, lse.

        SourceExists(source: str) -> bool

            Determines whether an event source is registered on the local computer.

            source: The name of the event source.

            Returns: ue if the event source is registered on the local computer; otherwise, lse.
        """
        ...
    @staticmethod
    def WriteEntry(*__args):
        """
        WriteEntry(source: str, message: str)

            Writes an information type entry with the given message text to the event log, using the specified registered event source.

            source: The source by which the application is registered on the specified computer.

            message: The string to write to the event log.

        WriteEntry(source: str, message: str, type: EventLogEntryType)

            Writes an error, warning, information, success audit, or failure audit entry with the given message text to the event log, using the specified registered event source.

            source: The source by which the application is registered on the specified computer.

            message: The string to write to the event log.

            type: One of the System.Diagnostics.EventLogEntryType values.

        WriteEntry(source: str, message: str, type: EventLogEntryType, eventID: int)

            Writes an entry with the given message text and application-defined event identifier to the event log, using the specified registered event source.

            source: The source by which the application is registered on the specified computer.

            message: The string to write to the event log.

            type: One of the System.Diagnostics.EventLogEntryType values.

            eventID: The application-specific identifier for the event.

        WriteEntry(source: str, message: str, type: EventLogEntryType, eventID: int, category: Int16)

            Writes an entry with the given message text, application-defined event identifier, and application-defined category to the event log, using the specified registered event source. The category can be used by the Event Viewer to

             filter events in the log.

            source: The source by which the application is registered on the specified computer.

            message: The string to write to the event log.

            type: One of the System.Diagnostics.EventLogEntryType values.

            eventID: The application-specific identifier for the event.

            category: The application-specific subcategory associated with the message.

        WriteEntry(self: EventLog, message: str)

            Writes an information type entry, with the given message text, to the event log.

            message: The string to write to the event log.

        WriteEntry(self: EventLog, message: str, type: EventLogEntryType)

            Writes an error, warning, information, success audit, or failure audit entry with the given message text to the event log.

            message: The string to write to the event log.

            type: One of the System.Diagnostics.EventLogEntryType values.

        WriteEntry(self: EventLog, message: str, type: EventLogEntryType, eventID: int)

            Writes an entry with the given message text and application-defined event identifier to the event log.

            message: The string to write to the event log.

            type: One of the System.Diagnostics.EventLogEntryType values.

            eventID: The application-specific identifier for the event.

        WriteEntry(self: EventLog, message: str, type: EventLogEntryType, eventID: int, category: Int16)

            Writes an entry with the given message text, application-defined event identifier, and application-defined category to the event log.

            message: The string to write to the event log.

            type: One of the System.Diagnostics.EventLogEntryType values.

            eventID: The application-specific identifier for the event.

            category: The application-specific subcategory associated with the message.

        WriteEntry(source: str, message: str, type: EventLogEntryType, eventID: int, category: Int16, rawData: Array[Byte])

            Writes an entry with the given message text, application-defined event identifier, and application-defined category to the event log (using the specified registered event source) and appends binary data to the message.

            source: The source by which the application is registered on the specified computer.

            message: The string to write to the event log.

            type: One of the System.Diagnostics.EventLogEntryType values.

            eventID: The application-specific identifier for the event.

            category: The application-specific subcategory associated with the message.

            rawData: An array of bytes that holds the binary data associated with the entry.

        WriteEntry(self: EventLog, message: str, type: EventLogEntryType, eventID: int, category: Int16, rawData: Array[Byte])

            Writes an entry with the given message text, application-defined event identifier, and application-defined category to the event log, and appends binary data to the message.

            message: The string to write to the event log.

            type: One of the System.Diagnostics.EventLogEntryType values.

            eventID: The application-specific identifier for the event.

            category: The application-specific subcategory associated with the message.

            rawData: An array of bytes that holds the binary data associated with the entry.
        """
        ...
    def WriteEvent(self, *__args):
        """
        WriteEvent(self: EventLog, instance: EventInstance, *values: Array[object])

            Writes a localized entry to the event log.

            instance: An System.Diagnostics.EventInstance instance that represents a localized event log entry.

            values: An array of strings to merge into the message text of the event log entry.

        WriteEvent(self: EventLog, instance: EventInstance, data: Array[Byte], *values: Array[object])

            Writes an event log entry with the given event data, message replacement strings, and associated binary data.

            instance: An System.Diagnostics.EventInstance instance that represents a localized event log entry.

            data: An array of bytes that holds the binary data associated with the entry.

            values: An array of strings to merge into the message text of the event log entry.

        WriteEvent(source: str, instance: EventInstance, *values: Array[object])

            Writes an event log entry with the given event data and message replacement strings, using the specified registered event source.

            source: The name of the event source registered for the application on the specified computer.

            instance: An System.Diagnostics.EventInstance instance that represents a localized event log entry.

            values: An array of strings to merge into the message text of the event log entry.

        WriteEvent(source: str, instance: EventInstance, data: Array[Byte], *values: Array[object])

            Writes an event log entry with the given event data, message replacement strings, and associated binary data, and using the specified registered event source.

            source: The name of the event source registered for the application on the specified computer.

            instance: An System.Diagnostics.EventInstance instance that represents a localized event log entry.

            data: An array of bytes that holds the binary data associated with the entry.

            values: An array of strings to merge into the message text of the event log entry.
        """
        ...
    @staticmethod  # known case of __new__
    def __new__(cls, logName=None, machineName=None, source=None):
        """
        __new__(cls: type)

        __new__(cls: type, logName: str)

        __new__(cls: type, logName: str, machineName: str)

        __new__(cls: type, logName: str, machineName: str, source: str)
        """
        ...
    @property
    def CanRaiseEvents(self):
        """Gets a value indicating whether the component can raise an event."""
        ...
    @property
    def DesignMode(self):
        """Gets a value that indicates whether the System.ComponentModel.Component is currently in design mode."""
        ...
    @property
    def EnableRaisingEvents(self):
        """
        Gets or sets a value indicating whether the System.Diagnostics.EventLog receives System.Diagnostics.EventLog.EntryWritten event notifications.

        Get: EnableRaisingEvents(self: EventLog) -> bool

        Set: EnableRaisingEvents(self: EventLog) = value
        """
        ...
    @property
    def Entries(self):
        """
        Gets the contents of the event log.

        Get: Entries(self: EventLog) -> EventLogEntryCollection
        """
        ...
    @property
    def Events(self):
        """Gets the list of event handlers that are attached to this System.ComponentModel.Component."""
        ...
    @property
    def Log(self):
        """
        Gets or sets the name of the log to read from or write to.

        Get: Log(self: EventLog) -> str

        Set: Log(self: EventLog) = value
        """
        ...
    @property
    def LogDisplayName(self):
        """
        Gets the event log's friendly name.

        Get: LogDisplayName(self: EventLog) -> str
        """
        ...
    @property
    def MachineName(self):
        """
        Gets or sets the name of the computer on which to read or write events.

        Get: MachineName(self: EventLog) -> str

        Set: MachineName(self: EventLog) = value
        """
        ...
    @property
    def MaximumKilobytes(self):
        """
        Gets or sets the maximum event log size in kilobytes.

        Get: MaximumKilobytes(self: EventLog) -> Int64

        Set: MaximumKilobytes(self: EventLog) = value
        """
        ...
    @property
    def MinimumRetentionDays(self):
        """
        Gets the number of days to retain entries in the event log.

        Get: MinimumRetentionDays(self: EventLog) -> int
        """
        ...
    @property
    def OverflowAction(self):
        """
        Gets the configured behavior for storing new entries when the event log reaches its maximum log file size.

        Get: OverflowAction(self: EventLog) -> OverflowAction
        """
        ...
    @property
    def Source(self):
        """
        Gets or sets the source name to register and use when writing to the event log.

        Get: Source(self: EventLog) -> str

        Set: Source(self: EventLog) = value
        """
        ...
    @property
    def SynchronizingObject(self):
        """
        Gets or sets the object used to marshal the event handler calls issued as a result of an System.Diagnostics.EventLog entry written event.

        Get: SynchronizingObject(self: EventLog) -> ISynchronizeInvoke

        Set: SynchronizingObject(self: EventLog) = value
        """
        ...
    EntryWritten = None

class EventLogEntry(Component, ISerializable):  # skipped bases: <type 'IComponent'>, <type 'IDisposable'>
    """Encapsulates a single record in the event log. This class cannot be inherited."""

    def Equals(self, *__args):
        """
        Equals(self: EventLogEntry, otherEntry: EventLogEntry) -> bool

            Performs a comparison between two event log entries.

            otherEntry: The System.Diagnostics.EventLogEntry to compare.

            Returns: ue if the System.Diagnostics.EventLogEntry objects are identical; otherwise, lse.
        """
        ...
    def __eq__(self, *args):  # cannot find CLR method
        """x.__eq__(y) <==> x==y"""
        ...
    def __reduce_ex__(self, *args): ...
    @property
    def CanRaiseEvents(self):
        """Gets a value indicating whether the component can raise an event."""
        ...
    @property
    def Category(self):
        """
        Gets the text associated with the System.Diagnostics.EventLogEntry.CategoryNumber property for this entry.

        Get: Category(self: EventLogEntry) -> str
        """
        ...
    @property
    def CategoryNumber(self):
        """
        Gets the category number of the event log entry.

        Get: CategoryNumber(self: EventLogEntry) -> Int16
        """
        ...
    @property
    def Data(self):
        """
        Gets the binary data associated with the entry.

        Get: Data(self: EventLogEntry) -> Array[Byte]
        """
        ...
    @property
    def DesignMode(self):
        """Gets a value that indicates whether the System.ComponentModel.Component is currently in design mode."""
        ...
    @property
    def EntryType(self):
        """
        Gets the event type of this entry.

        Get: EntryType(self: EventLogEntry) -> EventLogEntryType
        """
        ...
    @property
    def EventID(self):
        """
        Gets the application-specific event identifier for the current event entry.

        Get: EventID(self: EventLogEntry) -> int
        """
        ...
    @property
    def Events(self):
        """Gets the list of event handlers that are attached to this System.ComponentModel.Component."""
        ...
    @property
    def Index(self):
        """
        Gets the index of this entry in the event log.

        Get: Index(self: EventLogEntry) -> int
        """
        ...
    @property
    def InstanceId(self):
        """
        Gets the resource identifier that designates the message text of the event entry.

        Get: InstanceId(self: EventLogEntry) -> Int64
        """
        ...
    @property
    def MachineName(self):
        """
        Gets the name of the computer on which this entry was generated.

        Get: MachineName(self: EventLogEntry) -> str
        """
        ...
    @property
    def Message(self):
        """
        Gets the localized message associated with this event entry.

        Get: Message(self: EventLogEntry) -> str
        """
        ...
    @property
    def ReplacementStrings(self):
        """
        Gets the replacement strings associated with the event log entry.

        Get: ReplacementStrings(self: EventLogEntry) -> Array[str]
        """
        ...
    @property
    def Source(self):
        """
        Gets the name of the application that generated this event.

        Get: Source(self: EventLogEntry) -> str
        """
        ...
    @property
    def TimeGenerated(self):
        """
        Gets the local time at which this event was generated.

        Get: TimeGenerated(self: EventLogEntry) -> DateTime
        """
        ...
    @property
    def TimeWritten(self):
        """
        Gets the local time at which this event was written to the log.

        Get: TimeWritten(self: EventLogEntry) -> DateTime
        """
        ...
    @property
    def UserName(self):
        """
        Gets the name of the user who is responsible for this event.

        Get: UserName(self: EventLogEntry) -> str
        """
        ...

class EventLogEntryCollection(object, ICollection):  # skipped bases: <type 'IEnumerable'>
    """Defines size and enumerators for a collection of System.Diagnostics.EventLogEntry instances."""

    def GetEnumerator(self):
        """
        GetEnumerator(self: EventLogEntryCollection) -> IEnumerator

            Supports a simple iteration over the System.Diagnostics.EventLogEntryCollection object.

            Returns: An object that can be used to iterate over the collection.
        """
        ...
    def __getitem__(self, *args):  # cannot find CLR method
        """x.__getitem__(y) <==> x[y]"""
        ...
    def __len__(self, *args):  # cannot find CLR method
        """x.__len__() <==> len(x)"""
        ...
    @property
    def Count(self):
        """
        Gets the number of entries in the event log (that is, the number of elements in the System.Diagnostics.EventLogEntry collection).

        Get: Count(self: EventLogEntryCollection) -> int
        """
        ...

class EventLogEntryType(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies the event type of an event log entry.

    enum EventLogEntryType, values: Error (1), FailureAudit (16), Information (4), SuccessAudit (8), Warning (2)
    """

    Error = None
    FailureAudit = None
    Information = None
    SuccessAudit = None
    value__ = None
    Warning = None

class EventLogPermission(
    ResourcePermissionBase
):  # skipped bases: <type 'IUnrestrictedPermission'>, <type 'ISecurityEncodable'>, <type 'IPermission'>, <type 'IStackWalk'>
    """
    Controls code access permissions for event logging.

    EventLogPermission()

    EventLogPermission(state: PermissionState)

    EventLogPermission(permissionAccess: EventLogPermissionAccess, machineName: str)

    EventLogPermission(permissionAccessEntries: Array[EventLogPermissionEntry])
    """

    @property
    def PermissionAccessType(self):
        """Gets or sets an enumeration value that describes the types of access that you are giving the resource."""
        ...
    @property
    def PermissionEntries(self):
        """
        Gets the collection of permission entries for this permissions request.

        Get: PermissionEntries(self: EventLogPermission) -> EventLogPermissionEntryCollection
        """
        ...
    @property
    def TagNames(self):
        """Gets or sets an array of strings that identify the resource you are protecting."""
        ...

class EventLogPermissionAccess(
    Enum
):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Defines access levels used by System.Diagnostics.EventLog permission classes.

    enum (flags) EventLogPermissionAccess, values: Administer (48), Audit (10), Browse (2), Instrument (6), None (0), Write (16)
    """

    Administer = None
    Audit = None
    Browse = None
    Instrument = None
    value__ = None
    Write = None

class EventLogPermissionAttribute(CodeAccessSecurityAttribute):  # skipped bases: <type '_Attribute'>
    """
    Allows declaritive permission checks for event logging.

    EventLogPermissionAttribute(action: SecurityAction)
    """

    def CreatePermission(self):
        """
        CreatePermission(self: EventLogPermissionAttribute) -> IPermission

            Creates the permission based on the System.Diagnostics.EventLogPermissionAttribute.MachineName property and the requested access levels that are set through the System.Diagnostics.EventLogPermissionAttribute.PermissionAccess

             property on the attribute.

            Returns: An System.Security.IPermission that represents the created permission.
        """
        ...
    @property
    def MachineName(self):
        """
        Gets or sets the name of the computer on which events might be read.

        Get: MachineName(self: EventLogPermissionAttribute) -> str

        Set: MachineName(self: EventLogPermissionAttribute) = value
        """
        ...
    @property
    def PermissionAccess(self):
        """
        Gets or sets the access levels used in the permissions request.

        Get: PermissionAccess(self: EventLogPermissionAttribute) -> EventLogPermissionAccess

        Set: PermissionAccess(self: EventLogPermissionAttribute) = value
        """
        ...

class EventLogPermissionEntry:  # skipped bases: <type 'object'>
    """
    Defines the smallest unit of a code access security permission that is set for an System.Diagnostics.EventLog.

    EventLogPermissionEntry(permissionAccess: EventLogPermissionAccess, machineName: str)
    """

    @property
    def MachineName(self):
        """
        Gets the name of the computer on which to read or write events.

        Get: MachineName(self: EventLogPermissionEntry) -> str
        """
        ...
    @property
    def PermissionAccess(self):
        """
        Gets the permission access levels used in the permissions request.

        Get: PermissionAccess(self: EventLogPermissionEntry) -> EventLogPermissionAccess
        """
        ...

class EventLogPermissionEntryCollection(
    CollectionBase
):  # skipped bases: <type 'IList'>, <type 'ICollection'>, <type 'IEnumerable'>
    """Contains a strongly typed collection of System.Diagnostics.EventLogPermissionEntry objects."""

    def Add(self, value):
        """
        Add(self: EventLogPermissionEntryCollection, value: EventLogPermissionEntry) -> int

            Adds a specified System.Diagnostics.EventLogPermissionEntry to this collection.

            value: The System.Diagnostics.EventLogPermissionEntry to add.

            Returns: The zero-based index of the added System.Diagnostics.EventLogPermissionEntry.
        """
        ...
    def AddRange(self, value):
        """
        AddRange(self: EventLogPermissionEntryCollection, value: Array[EventLogPermissionEntry])

            Appends a set of specified permission entries to this collection.

            value: An array of type System.Diagnostics.EventLogPermissionEntry objects that contains the permission entries to add.

        AddRange(self: EventLogPermissionEntryCollection, value: EventLogPermissionEntryCollection)

            Appends a set of specified permission entries to this collection.

            value: A System.Diagnostics.EventLogPermissionEntryCollection that contains the permission entries to add.
        """
        ...
    def Contains(self, value):
        """
        Contains(self: EventLogPermissionEntryCollection, value: EventLogPermissionEntry) -> bool

            Determines whether this collection contains a specified System.Diagnostics.EventLogPermissionEntry.

            value: The System.Diagnostics.EventLogPermissionEntry to find.

            Returns: ue if the specified System.Diagnostics.EventLogPermissionEntry belongs to this collection; otherwise, lse.
        """
        ...
    def CopyTo(self, array, index):
        """
        CopyTo(self: EventLogPermissionEntryCollection, array: Array[EventLogPermissionEntry], index: int)

            Copies the permission entries from this collection to an array, starting at a particular index of the array.

            array: An array of type System.Diagnostics.EventLogPermissionEntry that receives this collection's permission entries.

            index: The zero-based index at which to begin copying the permission entries.
        """
        ...
    def IndexOf(self, value):
        """
        IndexOf(self: EventLogPermissionEntryCollection, value: EventLogPermissionEntry) -> int

            Determines the index of a specified permission entry in this collection.

            value: The permission entry to search for.

            Returns: The zero-based index of the specified permission entry, or -1 if the permission entry was not found in the collection.
        """
        ...
    def Insert(self, index, value):
        """
        Insert(self: EventLogPermissionEntryCollection, index: int, value: EventLogPermissionEntry)

            Inserts a permission entry into this collection at a specified index.

            index: The zero-based index of the collection at which to insert the permission entry.

            value: The permission entry to insert into this collection.
        """
        ...
    def Remove(self, value):
        """
        Remove(self: EventLogPermissionEntryCollection, value: EventLogPermissionEntry)

            Removes a specified permission entry from this collection.

            value: The permission entry to remove.
        """
        ...
    def __add__(self, *args):  # cannot find CLR method
        """x.__add__(y) <==> x+y"""
        ...
    def __getitem__(self, *args):  # cannot find CLR method
        """x.__getitem__(y) <==> x[y]"""
        ...
    def __setitem__(self, *args):  # cannot find CLR method
        """x.__setitem__(i, y) <==> x[i]="""
        ...
    @property
    def InnerList(self):
        """Gets an System.Collections.ArrayList containing the list of elements in the System.Collections.CollectionBase instance."""
        ...
    @property
    def List(self):
        """Gets an System.Collections.IList containing the list of elements in the System.Collections.CollectionBase instance."""
        ...

class EventLogTraceListener(TraceListener):  # skipped bases: <type 'IDisposable'>
    """
    Provides a simple listener that directs tracing or debugging output to an System.Diagnostics.EventLog.

    EventLogTraceListener()

    EventLogTraceListener(eventLog: EventLog)

    EventLogTraceListener(source: str)
    """

    @property
    def EventLog(self):
        """
        Gets or sets the event log to write to.

        Get: EventLog(self: EventLogTraceListener) -> EventLog

        Set: EventLog(self: EventLogTraceListener) = value
        """
        ...
    @property
    def Name(self):
        """
        Gets or sets the name of this System.Diagnostics.EventLogTraceListener.

        Get: Name(self: EventLogTraceListener) -> str

        Set: Name(self: EventLogTraceListener) = value
        """
        ...
    @property
    def NeedIndent(self):
        """Gets or sets a value indicating whether to indent the output."""
        ...

class EventSourceCreationData:  # skipped bases: <type 'object'>
    """
    Represents the configuration settings used to create an event log source on the local computer or a remote computer.

    EventSourceCreationData(source: str, logName: str)
    """

    @property
    def CategoryCount(self):
        """
        Gets or sets the number of categories in the category resource file.

        Get: CategoryCount(self: EventSourceCreationData) -> int

        Set: CategoryCount(self: EventSourceCreationData) = value
        """
        ...
    @property
    def CategoryResourceFile(self):
        """
        Gets or sets the path of the resource file that contains category strings for the source.

        Get: CategoryResourceFile(self: EventSourceCreationData) -> str

        Set: CategoryResourceFile(self: EventSourceCreationData) = value
        """
        ...
    @property
    def LogName(self):
        """
        Gets or sets the name of the event log to which the source writes entries.

        Get: LogName(self: EventSourceCreationData) -> str

        Set: LogName(self: EventSourceCreationData) = value
        """
        ...
    @property
    def MachineName(self):
        """
        Gets or sets the name of the computer on which to register the event source.

        Get: MachineName(self: EventSourceCreationData) -> str

        Set: MachineName(self: EventSourceCreationData) = value
        """
        ...
    @property
    def MessageResourceFile(self):
        """
        Gets or sets the path of the message resource file that contains message formatting strings for the source.

        Get: MessageResourceFile(self: EventSourceCreationData) -> str

        Set: MessageResourceFile(self: EventSourceCreationData) = value
        """
        ...
    @property
    def ParameterResourceFile(self):
        """
        Gets or sets the path of the resource file that contains message parameter strings for the source.

        Get: ParameterResourceFile(self: EventSourceCreationData) -> str

        Set: ParameterResourceFile(self: EventSourceCreationData) = value
        """
        ...
    @property
    def Source(self):
        """
        Gets or sets the name to register with the event log as an event source.

        Get: Source(self: EventSourceCreationData) -> str

        Set: Source(self: EventSourceCreationData) = value
        """
        ...

class TraceFilter:  # skipped bases: <type 'object'>
    """Provides the base class for trace filter implementations."""

    def ShouldTrace(self, cache, source, eventType, id, formatOrMessage, args, data1, data):
        """
        ShouldTrace(self: TraceFilter, cache: TraceEventCache, source: str, eventType: TraceEventType, id: int, formatOrMessage: str, args: Array[object], data1: object, data: Array[object]) -> bool

            When overridden in a derived class, determines whether the trace listener should trace the event.

            cache: The System.Diagnostics.TraceEventCache that contains information for the trace event.

            source: The name of the source.

            eventType: One of the System.Diagnostics.TraceEventType values specifying the type of event that has caused the trace.

            id: A trace identifier number.

            formatOrMessage: Either the format to use for writing an array of arguments specified by the args parameter, or a message to write.

            args: An array of argument objects.

            data1: A trace data object.

            data: An array of trace data objects.

            Returns: ue to trace the specified event; otherwise, lse.
        """
        ...

class EventTypeFilter(TraceFilter):
    """
    Indicates whether a listener should trace based on the event type.

    EventTypeFilter(level: SourceLevels)
    """

    @staticmethod  # known case of __new__
    def __new__(cls, level):
        """__new__(cls: type, level: SourceLevels)"""
        ...
    @property
    def EventType(self):
        """
        Gets or sets the event type of the messages to trace.

        Get: EventType(self: EventTypeFilter) -> SourceLevels

        Set: EventType(self: EventTypeFilter) = value
        """
        ...

class FileVersionInfo:  # skipped bases: <type 'object'>
    """Provides version information for a physical file on disk."""

    @staticmethod
    def GetVersionInfo(fileName):
        """
        GetVersionInfo(fileName: str) -> FileVersionInfo

            Returns a System.Diagnostics.FileVersionInfo representing the version information associated with the specified file.

            fileName: The fully qualified path and name of the file to retrieve the version information for.

            Returns: A System.Diagnostics.FileVersionInfo containing information about the file. If the file did not contain version information, the System.Diagnostics.FileVersionInfo contains only the name of the file requested.
        """
        ...
    def ToString(self):
        """
        ToString(self: FileVersionInfo) -> str

            Returns a partial list of properties in the System.Diagnostics.FileVersionInfo and their values.

            Returns: A list of the following properties in this class and their values:

                  System.Diagnostics.FileVersionInfo.FileName, System.Diagnostics.FileVersionInfo.InternalName, System.Diagnostics.FileVersionInfo.OriginalFilename,

             System.Diagnostics.FileVersionInfo.FileVersion, System.Diagnostics.FileVersionInfo.FileDescription, System.Diagnostics.FileVersionInfo.ProductName, System.Diagnostics.FileVersionInfo.ProductVersion,

             System.Diagnostics.FileVersionInfo.IsDebug, System.Diagnostics.FileVersionInfo.IsPatched, System.Diagnostics.FileVersionInfo.IsPreRelease, System.Diagnostics.FileVersionInfo.IsPrivateBuild,

             System.Diagnostics.FileVersionInfo.IsSpecialBuild,

                  System.Diagnostics.FileVersionInfo.Language.If the file did not contain version information, this list will contain only the name of the requested file. Boolean values

             will be lse, and all other entries will be ll.
        """
        ...
    @property
    def Comments(self):
        """
        Gets the comments associated with the file.

        Get: Comments(self: FileVersionInfo) -> str
        """
        ...
    @property
    def CompanyName(self):
        """
        Gets the name of the company that produced the file.

        Get: CompanyName(self: FileVersionInfo) -> str
        """
        ...
    @property
    def FileBuildPart(self):
        """
        Gets the build number of the file.

        Get: FileBuildPart(self: FileVersionInfo) -> int
        """
        ...
    @property
    def FileDescription(self):
        """
        Gets the description of the file.

        Get: FileDescription(self: FileVersionInfo) -> str
        """
        ...
    @property
    def FileMajorPart(self):
        """
        Gets the major part of the version number.

        Get: FileMajorPart(self: FileVersionInfo) -> int
        """
        ...
    @property
    def FileMinorPart(self):
        """
        Gets the minor part of the version number of the file.

        Get: FileMinorPart(self: FileVersionInfo) -> int
        """
        ...
    @property
    def FileName(self):
        """
        Gets the name of the file that this instance of System.Diagnostics.FileVersionInfo describes.

        Get: FileName(self: FileVersionInfo) -> str
        """
        ...
    @property
    def FilePrivatePart(self):
        """
        Gets the file private part number.

        Get: FilePrivatePart(self: FileVersionInfo) -> int
        """
        ...
    @property
    def FileVersion(self):
        """
        Gets the file version number.

        Get: FileVersion(self: FileVersionInfo) -> str
        """
        ...
    @property
    def InternalName(self):
        """
        Gets the internal name of the file, if one exists.

        Get: InternalName(self: FileVersionInfo) -> str
        """
        ...
    @property
    def IsDebug(self):
        """
        Gets a value that specifies whether the file contains debugging information or is compiled with debugging features enabled.

        Get: IsDebug(self: FileVersionInfo) -> bool
        """
        ...
    @property
    def IsPatched(self):
        """
        Gets a value that specifies whether the file has been modified and is not identical to the original shipping file of the same version number.

        Get: IsPatched(self: FileVersionInfo) -> bool
        """
        ...
    @property
    def IsPreRelease(self):
        """
        Gets a value that specifies whether the file is a development version, rather than a commercially released product.

        Get: IsPreRelease(self: FileVersionInfo) -> bool
        """
        ...
    @property
    def IsPrivateBuild(self):
        """
        Gets a value that specifies whether the file was built using standard release procedures.

        Get: IsPrivateBuild(self: FileVersionInfo) -> bool
        """
        ...
    @property
    def IsSpecialBuild(self):
        """
        Gets a value that specifies whether the file is a special build.

        Get: IsSpecialBuild(self: FileVersionInfo) -> bool
        """
        ...
    @property
    def Language(self):
        """
        Gets the default language string for the version info block.

        Get: Language(self: FileVersionInfo) -> str
        """
        ...
    @property
    def LegalCopyright(self):
        """
        Gets all copyright notices that apply to the specified file.

        Get: LegalCopyright(self: FileVersionInfo) -> str
        """
        ...
    @property
    def LegalTrademarks(self):
        """
        Gets the trademarks and registered trademarks that apply to the file.

        Get: LegalTrademarks(self: FileVersionInfo) -> str
        """
        ...
    @property
    def OriginalFilename(self):
        """
        Gets the name the file was created with.

        Get: OriginalFilename(self: FileVersionInfo) -> str
        """
        ...
    @property
    def PrivateBuild(self):
        """
        Gets information about a private version of the file.

        Get: PrivateBuild(self: FileVersionInfo) -> str
        """
        ...
    @property
    def ProductBuildPart(self):
        """
        Gets the build number of the product this file is associated with.

        Get: ProductBuildPart(self: FileVersionInfo) -> int
        """
        ...
    @property
    def ProductMajorPart(self):
        """
        Gets the major part of the version number for the product this file is associated with.

        Get: ProductMajorPart(self: FileVersionInfo) -> int
        """
        ...
    @property
    def ProductMinorPart(self):
        """
        Gets the minor part of the version number for the product the file is associated with.

        Get: ProductMinorPart(self: FileVersionInfo) -> int
        """
        ...
    @property
    def ProductName(self):
        """
        Gets the name of the product this file is distributed with.

        Get: ProductName(self: FileVersionInfo) -> str
        """
        ...
    @property
    def ProductPrivatePart(self):
        """
        Gets the private part number of the product this file is associated with.

        Get: ProductPrivatePart(self: FileVersionInfo) -> int
        """
        ...
    @property
    def ProductVersion(self):
        """
        Gets the version of the product this file is distributed with.

        Get: ProductVersion(self: FileVersionInfo) -> str
        """
        ...
    @property
    def SpecialBuild(self):
        """
        Gets the special build information for the file.

        Get: SpecialBuild(self: FileVersionInfo) -> str
        """
        ...

class ICollectData:
    """Prepares performance data for the performance DLL the system loads when working with performance counters."""

    def CloseData(self):
        """
        CloseData(self: ICollectData)

            Called by the performance DLL's close performance data function.
        """
        ...
    def CollectData(self, id, valueName, data, totalBytes, res):
        """
        CollectData(self: ICollectData, id: int, valueName: IntPtr, data: IntPtr, totalBytes: int) -> IntPtr

            Collects the performance data for the performance DLL.

            id: The call index.

            valueName: A pointer to a Unicode string list with the requested object identifiers.

            data: A pointer to the data buffer.

            totalBytes: A pointer to a number of bytes.
        """
        ...

class InstanceData:  # skipped bases: <type 'object'>
    """
    Holds instance data associated with a performance counter sample.

    InstanceData(instanceName: str, sample: CounterSample)
    """

    @property
    def InstanceName(self):
        """
        Gets the instance name associated with this instance data.

        Get: InstanceName(self: InstanceData) -> str
        """
        ...
    @property
    def RawValue(self):
        """
        Gets the raw data value associated with the performance counter sample.

        Get: RawValue(self: InstanceData) -> Int64
        """
        ...
    @property
    def Sample(self):
        """
        Gets the performance counter sample that generated this data.

        Get: Sample(self: InstanceData) -> CounterSample
        """
        ...

class InstanceDataCollection(
    DictionaryBase
):  # skipped bases: <type 'ICollection'>, <type 'IEnumerable'>, <type 'IDictionary'>
    """
    Provides a strongly typed collection of System.Diagnostics.InstanceData objects.

    InstanceDataCollection(counterName: str)
    """

    def Contains(self, instanceName):
        """
        Contains(self: InstanceDataCollection, instanceName: str) -> bool

            Determines whether a performance instance with a specified name (identified by one of the indexed System.Diagnostics.InstanceData objects) exists in the collection.

            instanceName: The name of the instance to find in this collection.

            Returns: ue if the instance exists in the collection; otherwise, lse.
        """
        ...
    def __getitem__(self, *args):  # cannot find CLR method
        """x.__getitem__(y) <==> x[y]"""
        ...
    @staticmethod  # known case of __new__
    def __new__(cls, counterName):
        """__new__(cls: type, counterName: str)"""
        ...
    @property
    def CounterName(self):
        """
        Gets the name of the performance counter whose instance data you want to get.

        Get: CounterName(self: InstanceDataCollection) -> str
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
    @property
    def Keys(self):
        """
        Gets the object and counter registry keys for the objects associated with this instance data.

        Get: Keys(self: InstanceDataCollection) -> ICollection
        """
        ...
    @property
    def Values(self):
        """
        Gets the raw counter values that comprise the instance data for the counter.

        Get: Values(self: InstanceDataCollection) -> ICollection
        """
        ...

class InstanceDataCollectionCollection(
    DictionaryBase
):  # skipped bases: <type 'ICollection'>, <type 'IEnumerable'>, <type 'IDictionary'>
    """
    Provides a strongly typed collection of System.Diagnostics.InstanceDataCollection objects.

    InstanceDataCollectionCollection()
    """

    def Contains(self, counterName):
        """
        Contains(self: InstanceDataCollectionCollection, counterName: str) -> bool

            Determines whether an instance data collection for the specified counter (identified by one of the indexed System.Diagnostics.InstanceDataCollection objects) exists in the collection.

            counterName: The name of the performance counter.

            Returns: ue if an instance data collection containing the specified counter exists in the collection; otherwise, lse.
        """
        ...
    def __getitem__(self, *args):  # cannot find CLR method
        """x.__getitem__(y) <==> x[y]"""
        ...
    @property
    def Dictionary(self):
        """Gets the list of elements contained in the System.Collections.DictionaryBase instance."""
        ...
    @property
    def InnerHashtable(self):
        """Gets the list of elements contained in the System.Collections.DictionaryBase instance."""
        ...
    @property
    def Keys(self):
        """
        Gets the object and counter registry keys for the objects associated with this instance data collection.

        Get: Keys(self: InstanceDataCollectionCollection) -> ICollection
        """
        ...
    @property
    def Values(self):
        """
        Gets the instance data values that comprise the collection of instances for the counter.

        Get: Values(self: InstanceDataCollectionCollection) -> ICollection
        """
        ...

class MonitoringDescriptionAttribute(DescriptionAttribute):  # skipped bases: <type '_Attribute'>
    """
    Specifies a description for a property or event.

    MonitoringDescriptionAttribute(description: str)
    """

    @property
    def Description(self):
        """
        Gets description text associated with the item monitored.

        Get: Description(self: MonitoringDescriptionAttribute) -> str
        """
        ...
    @property
    def DescriptionValue(self):
        """Gets or sets the string stored as the description."""
        ...

class OverflowAction(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies how to handle entries in an event log that has reached its maximum file size.

    enum OverflowAction, values: DoNotOverwrite (-1), OverwriteAsNeeded (0), OverwriteOlder (1)
    """

    DoNotOverwrite = None
    OverwriteAsNeeded = None
    OverwriteOlder = None
    value__ = None

class PerformanceCounter(Component, ISupportInitialize):  # skipped bases: <type 'IComponent'>, <type 'IDisposable'>
    """
    Represents a Windows NT performance counter component.

    PerformanceCounter()

    PerformanceCounter(categoryName: str, counterName: str, instanceName: str, machineName: str)

    PerformanceCounter(categoryName: str, counterName: str, instanceName: str)

    PerformanceCounter(categoryName: str, counterName: str, instanceName: str, readOnly: bool)

    PerformanceCounter(categoryName: str, counterName: str)

    PerformanceCounter(categoryName: str, counterName: str, readOnly: bool)
    """

    def Close(self):
        """
        Close(self: PerformanceCounter)

            Closes the performance counter and frees all the resources allocated by this performance counter instance.
        """
        ...
    @staticmethod
    def CloseSharedResources():
        """
        CloseSharedResources()

            Frees the performance counter library shared state allocated by the counters.
        """
        ...
    def Decrement(self):
        """
        Decrement(self: PerformanceCounter) -> Int64

            Decrements the associated performance counter by one through an efficient atomic operation.

            Returns: The decremented counter value.
        """
        ...
    def Increment(self):
        """
        Increment(self: PerformanceCounter) -> Int64

            Increments the associated performance counter by one through an efficient atomic operation.

            Returns: The incremented counter value.
        """
        ...
    def IncrementBy(self, value):
        """
        IncrementBy(self: PerformanceCounter, value: Int64) -> Int64

            Increments or decrements the value of the associated performance counter by a specified amount through an efficient atomic operation.

            value: The value to increment by. (A negative value decrements the counter.)

            Returns: The new counter value.
        """
        ...
    def NextSample(self):
        """
        NextSample(self: PerformanceCounter) -> CounterSample

            Obtains a counter sample, and returns the raw, or uncalculated, value for it.

            Returns: A System.Diagnostics.CounterSample that represents the next raw value that the system obtains for this counter.
        """
        ...
    def NextValue(self):
        """
        NextValue(self: PerformanceCounter) -> Single

            Obtains a counter sample and returns the calculated value for it.

            Returns: The next calculated value that the system obtains for this counter.
        """
        ...
    def RemoveInstance(self):
        """
        RemoveInstance(self: PerformanceCounter)

            Deletes the category instance specified by the System.Diagnostics.PerformanceCounter object System.Diagnostics.PerformanceCounter.InstanceName property.
        """
        ...
    @staticmethod  # known case of __new__
    def __new__(cls, categoryName=None, counterName=None, *__args):
        """
        __new__(cls: type)

        __new__(cls: type, categoryName: str, counterName: str, instanceName: str, machineName: str)

        __new__(cls: type, categoryName: str, counterName: str, instanceName: str)

        __new__(cls: type, categoryName: str, counterName: str, instanceName: str, readOnly: bool)

        __new__(cls: type, categoryName: str, counterName: str)

        __new__(cls: type, categoryName: str, counterName: str, readOnly: bool)
        """
        ...
    @property
    def CanRaiseEvents(self):
        """Gets a value indicating whether the component can raise an event."""
        ...
    @property
    def CategoryName(self):
        """
        Gets or sets the name of the performance counter category for this performance counter.

        Get: CategoryName(self: PerformanceCounter) -> str

        Set: CategoryName(self: PerformanceCounter) = value
        """
        ...
    @property
    def CounterHelp(self):
        """
        Gets the description for this performance counter.

        Get: CounterHelp(self: PerformanceCounter) -> str
        """
        ...
    @property
    def CounterName(self):
        """
        Gets or sets the name of the performance counter that is associated with this System.Diagnostics.PerformanceCounter instance.

        Get: CounterName(self: PerformanceCounter) -> str

        Set: CounterName(self: PerformanceCounter) = value
        """
        ...
    @property
    def CounterType(self):
        """
        Gets the counter type of the associated performance counter.

        Get: CounterType(self: PerformanceCounter) -> PerformanceCounterType
        """
        ...
    @property
    def DesignMode(self):
        """Gets a value that indicates whether the System.ComponentModel.Component is currently in design mode."""
        ...
    @property
    def Events(self):
        """Gets the list of event handlers that are attached to this System.ComponentModel.Component."""
        ...
    @property
    def InstanceLifetime(self):
        """
        Gets or sets the lifetime of a process.

        Get: InstanceLifetime(self: PerformanceCounter) -> PerformanceCounterInstanceLifetime

        Set: InstanceLifetime(self: PerformanceCounter) = value
        """
        ...
    @property
    def InstanceName(self):
        """
        Gets or sets an instance name for this performance counter.

        Get: InstanceName(self: PerformanceCounter) -> str

        Set: InstanceName(self: PerformanceCounter) = value
        """
        ...
    @property
    def MachineName(self):
        """
        Gets or sets the computer name for this performance counter

        Get: MachineName(self: PerformanceCounter) -> str

        Set: MachineName(self: PerformanceCounter) = value
        """
        ...
    @property
    def RawValue(self):
        """
        Gets or sets the raw, or uncalculated, value of this counter.

        Get: RawValue(self: PerformanceCounter) -> Int64

        Set: RawValue(self: PerformanceCounter) = value
        """
        ...
    @property
    def ReadOnly(self):
        """
        Gets or sets a value indicating whether this System.Diagnostics.PerformanceCounter instance is in read-only mode.

        Get: ReadOnly(self: PerformanceCounter) -> bool

        Set: ReadOnly(self: PerformanceCounter) = value
        """
        ...
    DefaultFileMappingSize = 524288

class PerformanceCounterCategory:  # skipped bases: <type 'object'>
    """
    Represents a performance object, which defines a category of performance counters.

    PerformanceCounterCategory()

    PerformanceCounterCategory(categoryName: str)

    PerformanceCounterCategory(categoryName: str, machineName: str)
    """

    def CounterExists(self, counterName, categoryName=None, machineName=None):
        """
        CounterExists(self: PerformanceCounterCategory, counterName: str) -> bool

            Determines whether the specified counter is registered to this category, which is indicated by the System.Diagnostics.PerformanceCounterCategory.CategoryName and System.Diagnostics.PerformanceCounterCategory.MachineName properties.

            counterName: The name of the performance counter to look for.

            Returns: ue if the counter is registered to the category that is specified by the System.Diagnostics.PerformanceCounterCategory.CategoryName and System.Diagnostics.PerformanceCounterCategory.MachineName properties; otherwise, lse.

        CounterExists(counterName: str, categoryName: str) -> bool

            Determines whether the specified counter is registered to the specified category on the local computer.

            counterName: The name of the performance counter to look for.

            categoryName: The name of the performance counter category, or performance object, with which the specified performance counter is associated.

            Returns: ue, if the counter is registered to the specified category on the local computer; otherwise, lse.

        CounterExists(counterName: str, categoryName: str, machineName: str) -> bool

            Determines whether the specified counter is registered to the specified category on a remote computer.

            counterName: The name of the performance counter to look for.

            categoryName: The name of the performance counter category, or performance object, with which the specified performance counter is associated.

            machineName: The name of the computer on which the performance counter category and its associated counters exist.

            Returns: ue, if the counter is registered to the specified category on the specified computer; otherwise, lse.
        """
        ...
    @staticmethod
    def Create(categoryName, categoryHelp, *__args):
        """
        Create(categoryName: str, categoryHelp: str, counterData: CounterCreationDataCollection) -> PerformanceCounterCategory

            Registers the custom performance counter category containing the specified counters on the local computer.

            categoryName: The name of the custom performance counter category to create and register with the system.

            categoryHelp: A description of the custom category.

            counterData: A System.Diagnostics.CounterCreationDataCollection that specifies the counters to create as part of the new category.

            Returns: A System.Diagnostics.PerformanceCounterCategory that is associated with the new custom category, or performance object.

        Create(categoryName: str, categoryHelp: str, counterName: str, counterHelp: str) -> PerformanceCounterCategory

            Registers a custom performance counter category containing a single counter of type mberOfItems32 on the local computer.

            categoryName: The name of the custom performance counter category to create and register with the system.

            categoryHelp: A description of the custom category.

            counterName: The name of a new counter, of type mberOfItems32, to create as part of the new category.

            counterHelp: A description of the counter that is associated with the new custom category.

            Returns: A System.Diagnostics.PerformanceCounterCategory that is associated with the new system category, or performance object.

        Create(categoryName: str, categoryHelp: str, categoryType: PerformanceCounterCategoryType, counterName: str, counterHelp: str) -> PerformanceCounterCategory

            Registers the custom performance counter category containing a single counter of type System.Diagnostics.PerformanceCounterType.NumberOfItems32 on the local computer.

            categoryName: The name of the custom performance counter category to create and register with the system.

            categoryHelp: A description of the custom category.

            categoryType: One of the System.Diagnostics.PerformanceCounterCategoryType  values specifying whether the category is System.Diagnostics.PerformanceCounterCategoryType.MultiInstance,

             System.Diagnostics.PerformanceCounterCategoryType.SingleInstance, or System.Diagnostics.PerformanceCounterCategoryType.Unknown.

            counterName: The name of a new counter to create as part of the new category.

            counterHelp: A description of the counter that is associated with the new custom category.

            Returns: A System.Diagnostics.PerformanceCounterCategory that is associated with the new system category, or performance object.

        Create(categoryName: str, categoryHelp: str, categoryType: PerformanceCounterCategoryType, counterData: CounterCreationDataCollection) -> PerformanceCounterCategory

            Registers the custom performance counter category containing the specified counters on the local computer.

            categoryName: The name of the custom performance counter category to create and register with the system.

            categoryHelp: A description of the custom category.

            categoryType: One of the System.Diagnostics.PerformanceCounterCategoryType  values.

            counterData: A System.Diagnostics.CounterCreationDataCollection that specifies the counters to create as part of the new category.

            Returns: A System.Diagnostics.PerformanceCounterCategory that is associated with the new custom category, or performance object.
        """
        ...
    @staticmethod
    def Delete(categoryName):
        """
        Delete(categoryName: str)

            Removes the category and its associated counters from the local computer.

            categoryName: The name of the custom performance counter category to delete.
        """
        ...
    @staticmethod
    def Exists(categoryName, machineName=None):
        """
        Exists(categoryName: str) -> bool

            Determines whether the category is registered on the local computer.

            categoryName: The name of the performance counter category to look for.

            Returns: ue if the category is registered; otherwise, lse.

        Exists(categoryName: str, machineName: str) -> bool

            Determines whether the category is registered on the specified computer.

            categoryName: The name of the performance counter category to look for.

            machineName: The name of the computer to examine for the category.

            Returns: ue if the category is registered; otherwise, lse.
        """
        ...
    @staticmethod
    def GetCategories(machineName=None):
        """
        GetCategories() -> Array[PerformanceCounterCategory]

            Retrieves a list of the performance counter categories that are registered on the local computer.

            Returns: An array of System.Diagnostics.PerformanceCounterCategory objects indicating the categories that are registered on the local computer.

        GetCategories(machineName: str) -> Array[PerformanceCounterCategory]

            Retrieves a list of the performance counter categories that are registered on the specified computer.

            machineName: The computer to look on.

            Returns: An array of System.Diagnostics.PerformanceCounterCategory objects indicating the categories that are registered on the specified computer.
        """
        ...
    def GetCounters(self, instanceName=None):
        """
        GetCounters(self: PerformanceCounterCategory) -> Array[PerformanceCounter]

            Retrieves a list of the counters in a performance counter category that contains exactly one instance.

            Returns: An array of System.Diagnostics.PerformanceCounter objects indicating the counters that are associated with this single-instance performance counter category.

        GetCounters(self: PerformanceCounterCategory, instanceName: str) -> Array[PerformanceCounter]

            Retrieves a list of the counters in a performance counter category that contains one or more instances.

            instanceName: The performance object instance for which to retrieve the list of associated counters.

            Returns: An array of System.Diagnostics.PerformanceCounter objects indicating the counters that are associated with the specified object instance of this performance counter category.
        """
        ...
    def GetInstanceNames(self):
        """
        GetInstanceNames(self: PerformanceCounterCategory) -> Array[str]

            Retrieves the list of performance object instances that are associated with this category.

            Returns: An array of strings representing the performance object instance names that are associated with this category or, if the category contains only one performance object instance, a single-entry array that contains an empty string ("").
        """
        ...
    def InstanceExists(self, instanceName, categoryName=None, machineName=None):
        """
        InstanceExists(self: PerformanceCounterCategory, instanceName: str) -> bool

            Determines whether the specified performance object instance exists in the category that is identified by this System.Diagnostics.PerformanceCounterCategory object's System.Diagnostics.PerformanceCounterCategory.CategoryName

             property.

            instanceName: The performance object instance in this performance counter category to search for.

            Returns: ue if the category contains the specified performance object instance; otherwise, lse.

        InstanceExists(instanceName: str, categoryName: str) -> bool

            Determines whether a specified category on the local computer contains the specified performance object instance.

            instanceName: The performance object instance to search for.

            categoryName: The performance counter category to search.

            Returns: ue if the category contains the specified performance object instance; otherwise, lse.

        InstanceExists(instanceName: str, categoryName: str, machineName: str) -> bool

            Determines whether a specified category on a specified computer contains the specified performance object instance.

            instanceName: The performance object instance to search for.

            categoryName: The performance counter category to search.

            machineName: The name of the computer on which to look for the category instance pair.

            Returns: ue if the category contains the specified performance object instance; otherwise, lse.
        """
        ...
    def ReadCategory(self):
        """
        ReadCategory(self: PerformanceCounterCategory) -> InstanceDataCollectionCollection

            Reads all the counter and performance object instance data that is associated with this performance counter category.

            Returns: An System.Diagnostics.InstanceDataCollectionCollection that contains the counter and performance object instance data for the category.
        """
        ...
    @property
    def CategoryHelp(self):
        """
        Gets the category's help text.

        Get: CategoryHelp(self: PerformanceCounterCategory) -> str
        """
        ...
    @property
    def CategoryName(self):
        """
        Gets or sets the name of the performance object that defines this category.

        Get: CategoryName(self: PerformanceCounterCategory) -> str

        Set: CategoryName(self: PerformanceCounterCategory) = value
        """
        ...
    @property
    def CategoryType(self):
        """
        Gets the performance counter category type.

        Get: CategoryType(self: PerformanceCounterCategory) -> PerformanceCounterCategoryType
        """
        ...
    @property
    def MachineName(self):
        """
        Gets or sets the name of the computer on which this category exists.

        Get: MachineName(self: PerformanceCounterCategory) -> str

        Set: MachineName(self: PerformanceCounterCategory) = value
        """
        ...

class PerformanceCounterCategoryType(
    Enum
):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Indicates whether the performance counter category can have multiple instances.

    enum PerformanceCounterCategoryType, values: MultiInstance (1), SingleInstance (0), Unknown (-1)
    """

    MultiInstance = None
    SingleInstance = None
    Unknown = None
    value__ = None

class PerformanceCounterInstanceLifetime(
    Enum
):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies the lifetime of a performance counter instance.

    enum PerformanceCounterInstanceLifetime, values: Global (0), Process (1)
    """

    Global = None
    Process = None
    value__ = None

class PerformanceCounterManager(object, ICollectData):
    """
    Prepares performance data for the performance.dll the system loads when working with performance counters.

    PerformanceCounterManager()
    """

    pass

class PerformanceCounterPermission(
    ResourcePermissionBase
):  # skipped bases: <type 'IUnrestrictedPermission'>, <type 'ISecurityEncodable'>, <type 'IPermission'>, <type 'IStackWalk'>
    """
    Allows control of code access permissions for System.Diagnostics.PerformanceCounter.

    PerformanceCounterPermission()

    PerformanceCounterPermission(state: PermissionState)

    PerformanceCounterPermission(permissionAccess: PerformanceCounterPermissionAccess, machineName: str, categoryName: str)

    PerformanceCounterPermission(permissionAccessEntries: Array[PerformanceCounterPermissionEntry])
    """

    @property
    def PermissionAccessType(self):
        """Gets or sets an enumeration value that describes the types of access that you are giving the resource."""
        ...
    @property
    def PermissionEntries(self):
        """
        Gets the collection of permission entries for this permissions request.

        Get: PermissionEntries(self: PerformanceCounterPermission) -> PerformanceCounterPermissionEntryCollection
        """
        ...
    @property
    def TagNames(self):
        """Gets or sets an array of strings that identify the resource you are protecting."""
        ...

class PerformanceCounterPermissionAccess(
    Enum
):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Defines access levels used by System.Diagnostics.PerformanceCounter permission classes.

    enum (flags) PerformanceCounterPermissionAccess, values: Administer (7), Browse (1), Instrument (3), None (0), Read (1), Write (2)
    """

    Administer = None
    Browse = None
    Instrument = None
    Read = None
    value__ = None
    Write = None

class PerformanceCounterPermissionAttribute(CodeAccessSecurityAttribute):  # skipped bases: <type '_Attribute'>
    """
    Allows declaritive performance counter permission checks.

    PerformanceCounterPermissionAttribute(action: SecurityAction)
    """

    def CreatePermission(self):
        """
        CreatePermission(self: PerformanceCounterPermissionAttribute) -> IPermission

            Creates the permission based on the requested access levels that are set through the System.Diagnostics.PerformanceCounterPermissionAttribute.PermissionAccess property on the attribute.

            Returns: An System.Security.IPermission that represents the created permission.
        """
        ...
    @property
    def CategoryName(self):
        """
        Gets or sets the name of the performance counter category.

        Get: CategoryName(self: PerformanceCounterPermissionAttribute) -> str

        Set: CategoryName(self: PerformanceCounterPermissionAttribute) = value
        """
        ...
    @property
    def MachineName(self):
        """
        Gets or sets the computer name for the performance counter.

        Get: MachineName(self: PerformanceCounterPermissionAttribute) -> str

        Set: MachineName(self: PerformanceCounterPermissionAttribute) = value
        """
        ...
    @property
    def PermissionAccess(self):
        """
        Gets or sets the access levels used in the permissions request.

        Get: PermissionAccess(self: PerformanceCounterPermissionAttribute) -> PerformanceCounterPermissionAccess

        Set: PermissionAccess(self: PerformanceCounterPermissionAttribute) = value
        """
        ...

class PerformanceCounterPermissionEntry:  # skipped bases: <type 'object'>
    """
    Defines the smallest unit of a code access security permission that is set for a System.Diagnostics.PerformanceCounter.

    PerformanceCounterPermissionEntry(permissionAccess: PerformanceCounterPermissionAccess, machineName: str, categoryName: str)
    """

    @property
    def CategoryName(self):
        """
        Gets the name of the performance counter category (performance object).

        Get: CategoryName(self: PerformanceCounterPermissionEntry) -> str
        """
        ...
    @property
    def MachineName(self):
        """
        Gets the name of the server on which the category of the performance counter resides.

        Get: MachineName(self: PerformanceCounterPermissionEntry) -> str
        """
        ...
    @property
    def PermissionAccess(self):
        """
        Gets the permission access level of the entry.

        Get: PermissionAccess(self: PerformanceCounterPermissionEntry) -> PerformanceCounterPermissionAccess
        """
        ...

class PerformanceCounterPermissionEntryCollection(
    CollectionBase
):  # skipped bases: <type 'IList'>, <type 'ICollection'>, <type 'IEnumerable'>
    """Contains a strongly typed collection of System.Diagnostics.PerformanceCounterPermissionEntry objects."""

    def Add(self, value):
        """
        Add(self: PerformanceCounterPermissionEntryCollection, value: PerformanceCounterPermissionEntry) -> int

            Adds a specified System.Diagnostics.PerformanceCounterPermissionEntry to this collection.

            value: The System.Diagnostics.PerformanceCounterPermissionEntry object to add.

            Returns: The zero-based index of the added System.Diagnostics.PerformanceCounterPermissionEntry object.
        """
        ...
    def AddRange(self, value):
        """
        AddRange(self: PerformanceCounterPermissionEntryCollection, value: Array[PerformanceCounterPermissionEntry])

            Appends a set of specified permission entries to this collection.

            value: An array of type System.Diagnostics.PerformanceCounterPermissionEntry objects that contains the permission entries to add.

        AddRange(self: PerformanceCounterPermissionEntryCollection, value: PerformanceCounterPermissionEntryCollection)

            Appends a set of specified permission entries to this collection.

            value: A System.Diagnostics.PerformanceCounterPermissionEntryCollection that contains the permission entries to add.
        """
        ...
    def Contains(self, value):
        """
        Contains(self: PerformanceCounterPermissionEntryCollection, value: PerformanceCounterPermissionEntry) -> bool

            Determines whether this collection contains a specified System.Diagnostics.PerformanceCounterPermissionEntry object.

            value: The System.Diagnostics.PerformanceCounterPermissionEntry object to find.

            Returns: ue if the specified System.Diagnostics.PerformanceCounterPermissionEntry object belongs to this collection; otherwise, lse.
        """
        ...
    def CopyTo(self, array, index):
        """
        CopyTo(self: PerformanceCounterPermissionEntryCollection, array: Array[PerformanceCounterPermissionEntry], index: int)

            Copies the permission entries from this collection to an array, starting at a particular index of the array.

            array: An array of type System.Diagnostics.PerformanceCounterPermissionEntry that receives this collection's permission entries.

            index: The zero-based index at which to begin copying the permission entries.
        """
        ...
    def IndexOf(self, value):
        """
        IndexOf(self: PerformanceCounterPermissionEntryCollection, value: PerformanceCounterPermissionEntry) -> int

            Determines the index of a specified permission entry in this collection.

            value: The permission entry for which to search.

            Returns: The zero-based index of the specified permission entry, or -1 if the permission entry was not found in the collection.
        """
        ...
    def Insert(self, index, value):
        """
        Insert(self: PerformanceCounterPermissionEntryCollection, index: int, value: PerformanceCounterPermissionEntry)

            Inserts a permission entry into this collection at a specified index.

            index: The zero-based index of the collection at which to insert the permission entry.

            value: The permission entry to insert into this collection.
        """
        ...
    def Remove(self, value):
        """
        Remove(self: PerformanceCounterPermissionEntryCollection, value: PerformanceCounterPermissionEntry)

            Removes a specified permission entry from this collection.

            value: The permission entry to remove.
        """
        ...
    def __add__(self, *args):  # cannot find CLR method
        """x.__add__(y) <==> x+y"""
        ...
    def __getitem__(self, *args):  # cannot find CLR method
        """x.__getitem__(y) <==> x[y]"""
        ...
    def __setitem__(self, *args):  # cannot find CLR method
        """x.__setitem__(i, y) <==> x[i]="""
        ...
    @property
    def InnerList(self):
        """Gets an System.Collections.ArrayList containing the list of elements in the System.Collections.CollectionBase instance."""
        ...
    @property
    def List(self):
        """Gets an System.Collections.IList containing the list of elements in the System.Collections.CollectionBase instance."""
        ...

class PerformanceCounterType(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies the formula used to calculate the System.Diagnostics.PerformanceCounter.NextValue method for a System.Diagnostics.PerformanceCounter instance.

    enum PerformanceCounterType, values: AverageBase (1073939458), AverageCount64 (1073874176), AverageTimer32 (805438464), CounterDelta32 (4195328), CounterDelta64 (4195584), CounterMultiBase (1107494144), CounterMultiTimer (574686464), CounterMultiTimer100Ns (575735040), CounterMultiTimer100NsInverse (592512256), CounterMultiTimerInverse (591463680), CounterTimer (541132032), CounterTimerInverse (557909248), CountPerTimeInterval32 (4523008), CountPerTimeInterval64 (4523264), ElapsedTime (807666944), NumberOfItems32 (65536), NumberOfItems64 (65792), NumberOfItemsHEX32 (0), NumberOfItemsHEX64 (256), RateOfCountsPerSecond32 (272696320), RateOfCountsPerSecond64 (272696576), RawBase (1073939459), RawFraction (537003008), SampleBase (1073939457), SampleCounter (4260864), SampleFraction (549585920), Timer100Ns (542180608), Timer100NsInverse (558957824)
    """

    AverageBase = None
    AverageCount64 = None
    AverageTimer32 = None
    CounterDelta32 = None
    CounterDelta64 = None
    CounterMultiBase = None
    CounterMultiTimer = None
    CounterMultiTimer100Ns = None
    CounterMultiTimer100NsInverse = None
    CounterMultiTimerInverse = None
    CounterTimer = None
    CounterTimerInverse = None
    CountPerTimeInterval32 = None
    CountPerTimeInterval64 = None
    ElapsedTime = None
    NumberOfItems32 = None
    NumberOfItems64 = None
    NumberOfItemsHEX32 = None
    NumberOfItemsHEX64 = None
    RateOfCountsPerSecond32 = None
    RateOfCountsPerSecond64 = None
    RawBase = None
    RawFraction = None
    SampleBase = None
    SampleCounter = None
    SampleFraction = None
    Timer100Ns = None
    Timer100NsInverse = None
    value__ = None

class Process(Component):  # skipped bases: <type 'IComponent'>, <type 'IDisposable'>
    """
    Provides access to local and remote processes and enables you to start and stop local system processes.To browse the .NET Framework source code for this type, see the Reference Source.

    Process()
    """

    def BeginErrorReadLine(self):
        """
        BeginErrorReadLine(self: Process)

            Begins asynchronous read operations on the redirected System.Diagnostics.Process.StandardError stream of the application.
        """
        ...
    def BeginOutputReadLine(self):
        """
        BeginOutputReadLine(self: Process)

            Begins asynchronous read operations on the redirected System.Diagnostics.Process.StandardOutput stream of the application.
        """
        ...
    def CancelErrorRead(self):
        """
        CancelErrorRead(self: Process)

            Cancels the asynchronous read operation on the redirected System.Diagnostics.Process.StandardError stream of an application.
        """
        ...
    def CancelOutputRead(self):
        """
        CancelOutputRead(self: Process)

            Cancels the asynchronous read operation on the redirected System.Diagnostics.Process.StandardOutput stream of an application.
        """
        ...
    def Close(self):
        """
        Close(self: Process)

            Frees all the resources that are associated with this component.
        """
        ...
    def CloseMainWindow(self):
        """
        CloseMainWindow(self: Process) -> bool

            Closes a process that has a user interface by sending a close message to its main window.

            Returns: ue if the close message was successfully sent; lse if the associated process does not have a main window or if the main window is disabled (for example if a modal dialog is being shown).
        """
        ...
    @staticmethod
    def EnterDebugMode():
        """
        EnterDebugMode()

            Puts a System.Diagnostics.Process component in state to interact with operating system processes that run in a special mode by enabling the native property DebugPrivilege on the current thread.
        """
        ...
    @staticmethod
    def GetCurrentProcess():
        """
        GetCurrentProcess() -> Process

            Gets a new System.Diagnostics.Process component and associates it with the currently active process.

            Returns: A new System.Diagnostics.Process component associated with the process resource that is running the calling application.
        """
        ...
    @staticmethod
    def GetProcessById(processId: int, machineName: Optional[str] = None) -> Process:
        """Returns a new System.Diagnostics.Process component, given a process identifier and the name of a computer on the network.


        Parameters:
            processId (int): The system-unique identifier of a process resource.
            machineName (Optional[str], optional): The name of a computer on the network. Defaults to None.

        Returns:
            Process: A System.Diagnostics.Process component that is associated with a remote process resource identified by the processId parameter.
        """
        ...
    @staticmethod
    def GetProcesses(machineName=None):
        """
        GetProcesses() -> Array[Process]

            Creates a new System.Diagnostics.Process component for each process resource on the local computer.

            Returns: An array of type System.Diagnostics.Process that represents all the process resources running on the local computer.

        GetProcesses(machineName: str) -> Array[Process]

            Creates a new System.Diagnostics.Process component for each process resource on the specified computer.

            machineName: The computer from which to read the list of processes.

            Returns: An array of type System.Diagnostics.Process that represents all the process resources running on the specified computer.
        """
        ...
    @staticmethod
    def GetProcessesByName(processName, machineName=None):
        """
        GetProcessesByName(processName: str) -> Array[Process]

            Creates an array of new System.Diagnostics.Process components and associates them with all the process resources on the local computer that share the specified process name.

            processName: The friendly name of the process.

            Returns: An array of type System.Diagnostics.Process that represents the process resources running the specified application or file.

        GetProcessesByName(processName: str, machineName: str) -> Array[Process]

            Creates an array of new System.Diagnostics.Process components and associates them with all the process resources on a remote computer that share the specified process name.

            processName: The friendly name of the process.

            machineName: The name of a computer on the network.

            Returns: An array of type System.Diagnostics.Process that represents the process resources running the specified application or file.
        """
        ...
    def Kill(self) -> None:
        """Kills the associated process immediately."""
        ...
    @staticmethod
    def LeaveDebugMode():
        """
        LeaveDebugMode()

            Takes a System.Diagnostics.Process component out of the state that lets it interact with operating system processes that run in a special mode.
        """
        ...
    def OnExited(self, *args):  # cannot find CLR method
        """
        OnExited(self: Process)

            Raises the System.Diagnostics.Process.Exited event.
        """
        ...
    def Refresh(self):
        """
        Refresh(self: Process)

            Discards any information about the associated process that has been cached inside the process component.
        """
        ...
    @staticmethod
    def Start(*__args):
        """
        Start(fileName: str, userName: str, password: SecureString, domain: str) -> Process

            Starts a process resource by specifying the name of an application, a user name, a password, and a domain and associates the resource with a new System.Diagnostics.Process component.

            fileName: The name of an application file to run in the process.

            userName: The user name to use when starting the process.

            password: A System.Security.SecureString that contains the password to use when starting the process.

            domain: The domain to use when starting the process.

                     independent from the others. In addition, Start may return a non-null Process with its System.Diagnostics.Process.HasExited property already set to ue. In this case, the started process may have activated an existing instance of

             itself and then exited.

        Start(fileName: str, arguments: str, userName: str, password: SecureString, domain: str) -> Process

            Starts a process resource by specifying the name of an application, a set of command-line arguments, a user name, a password, and a domain and associates the resource with a new System.Diagnostics.Process component.

            fileName: The name of an application file to run in the process.

            arguments: Command-line arguments to pass when starting the process.

            userName: The user name to use when starting the process.

            password: A System.Security.SecureString that contains the password to use when starting the process.

            domain: The domain to use when starting the process.

                     independent from the others. In addition, Start may return a non-null Process with its System.Diagnostics.Process.HasExited property already set to ue. In this case, the started process may have activated an existing instance of

             itself and then exited.

        Start(fileName: str) -> Process

            Starts a process resource by specifying the name of a document or application file and associates the resource with a new System.Diagnostics.Process component.

            fileName: The name of a document or application file to run in the process.

                     independent from the others. In addition, Start may return a non-null Process with its System.Diagnostics.Process.HasExited property already set to ue. In this case, the started process may have activated an existing instance of

             itself and then exited.

        Start(fileName: str, arguments: str) -> Process

            Starts a process resource by specifying the name of an application and a set of command-line arguments, and associates the resource with a new System.Diagnostics.Process component.

            fileName: The name of an application file to run in the process.

            arguments: Command-line arguments to pass when starting the process.

                     independent from the others. In addition, Start may return a non-null Process with its System.Diagnostics.Process.HasExited property already set to ue. In this case, the started process may have activated an existing instance of

             itself and then exited.

        Start(startInfo: ProcessStartInfo) -> Process

            Starts the process resource that is specified by the parameter containing process start information (for example, the file name of the process to start) and associates the resource with a new System.Diagnostics.Process component.

            startInfo: The System.Diagnostics.ProcessStartInfo that contains the information that is used to start the process, including the file name and any command-line arguments.

                     independent from the others. In addition, Start may return a non-null Process with its System.Diagnostics.Process.HasExited property already set to ue. In this case, the started process may have activated an existing instance of

             itself and then exited.

        Start(self: Process) -> bool

            Starts (or reuses) the process resource that is specified by the System.Diagnostics.Process.StartInfo property of this System.Diagnostics.Process component and associates it with the component.

            Returns: ue if a process resource is started; lse if no new process resource is started (for example, if an existing process is reused).
        """
        ...
    def WaitForExit(self, milliseconds=None):
        """
        WaitForExit(self: Process, milliseconds: int) -> bool

            Instructs the System.Diagnostics.Process component to wait the specified number of milliseconds for the associated process to exit.

            milliseconds: The amount of time, in milliseconds, to wait for the associated process to exit. The maximum is the largest possible value of a 32-bit integer, which represents infinity to the operating system.

            Returns: ue if the associated process has exited; otherwise, lse.

        WaitForExit(self: Process)

            Instructs the System.Diagnostics.Process component to wait indefinitely for the associated process to exit.
        """
        ...
    def WaitForInputIdle(self, milliseconds=None):
        """
        WaitForInputIdle(self: Process, milliseconds: int) -> bool

            Causes the System.Diagnostics.Process component to wait the specified number of milliseconds for the associated process to enter an idle state. This overload applies only to processes with a user interface and, therefore, a message

             loop.

            milliseconds: A value of 1 to System.Int32.MaxValue that specifies the amount of time, in milliseconds, to wait for the associated process to become idle. A value of 0 specifies an immediate return, and a value of -1 specifies an infinite wait.

            Returns: ue if the associated process has reached an idle state; otherwise, lse.

        WaitForInputIdle(self: Process) -> bool

            Causes the System.Diagnostics.Process component to wait indefinitely for the associated process to enter an idle state. This overload applies only to processes with a user interface and, therefore, a message loop.

            Returns: ue if the associated process has reached an idle state.
        """
        ...
    @property
    def BasePriority(self):
        """
        Gets the base priority of the associated process.

        Get: BasePriority(self: Process) -> int
        """
        ...
    @property
    def CanRaiseEvents(self):
        """Gets a value indicating whether the component can raise an event."""
        ...
    @property
    def DesignMode(self):
        """Gets a value that indicates whether the System.ComponentModel.Component is currently in design mode."""
        ...
    @property
    def EnableRaisingEvents(self):
        """
        Gets or sets whether the System.Diagnostics.Process.Exited event should be raised when the process terminates.

        Get: EnableRaisingEvents(self: Process) -> bool

        Set: EnableRaisingEvents(self: Process) = value
        """
        ...
    @property
    def Events(self):
        """Gets the list of event handlers that are attached to this System.ComponentModel.Component."""
        ...
    @property
    def ExitCode(self):
        """
        Gets the value that the associated process specified when it terminated.

        Get: ExitCode(self: Process) -> int
        """
        ...
    @property
    def ExitTime(self):
        """
        Gets the time that the associated process exited.

        Get: ExitTime(self: Process) -> DateTime
        """
        ...
    @property
    def Handle(self):
        """
        Gets the native handle of the associated process.

        Get: Handle(self: Process) -> IntPtr
        """
        ...
    @property
    def HandleCount(self):
        """
        Gets the number of handles opened by the process.

        Get: HandleCount(self: Process) -> int
        """
        ...
    @property
    def HasExited(self):
        """
        Gets a value indicating whether the associated process has been terminated.

        Get: HasExited(self: Process) -> bool
        """
        ...
    @property
    def Id(self):
        """
        Gets the unique identifier for the associated process.

        Get: Id(self: Process) -> int
        """
        ...
    @property
    def MachineName(self):
        """
        Gets the name of the computer the associated process is running on.

        Get: MachineName(self: Process) -> str
        """
        ...
    @property
    def MainModule(self):
        """
        Gets the main module for the associated process.

        Get: MainModule(self: Process) -> ProcessModule
        """
        ...
    @property
    def MainWindowHandle(self):
        """
        Gets the window handle of the main window of the associated process.

        Get: MainWindowHandle(self: Process) -> IntPtr
        """
        ...
    @property
    def MainWindowTitle(self):
        """
        Gets the caption of the main window of the process.

        Get: MainWindowTitle(self: Process) -> str
        """
        ...
    @property
    def MaxWorkingSet(self):
        """
        Gets or sets the maximum allowable working set size, in bytes, for the associated process.

        Get: MaxWorkingSet(self: Process) -> IntPtr

        Set: MaxWorkingSet(self: Process) = value
        """
        ...
    @property
    def MinWorkingSet(self):
        """
        Gets or sets the minimum allowable working set size, in bytes, for the associated process.

        Get: MinWorkingSet(self: Process) -> IntPtr

        Set: MinWorkingSet(self: Process) = value
        """
        ...
    @property
    def Modules(self):
        """
        Gets the modules that have been loaded by the associated process.

        Get: Modules(self: Process) -> ProcessModuleCollection
        """
        ...
    @property
    def NonpagedSystemMemorySize(self):
        """
        Gets the amount of nonpaged system memory, in bytes, allocated for the associated process.

        Get: NonpagedSystemMemorySize(self: Process) -> int
        """
        ...
    @property
    def NonpagedSystemMemorySize64(self):
        """
        Gets the amount of nonpaged system memory, in bytes, allocated for the associated process.

        Get: NonpagedSystemMemorySize64(self: Process) -> Int64
        """
        ...
    @property
    def PagedMemorySize(self):
        """
        Gets the amount of paged memory, in bytes, allocated for the associated process.

        Get: PagedMemorySize(self: Process) -> int
        """
        ...
    @property
    def PagedMemorySize64(self):
        """
        Gets the amount of paged memory, in bytes, allocated for the associated process.

        Get: PagedMemorySize64(self: Process) -> Int64
        """
        ...
    @property
    def PagedSystemMemorySize(self):
        """
        Gets the amount of pageable system memory, in bytes, allocated for the associated process.

        Get: PagedSystemMemorySize(self: Process) -> int
        """
        ...
    @property
    def PagedSystemMemorySize64(self):
        """
        Gets the amount of pageable system memory, in bytes, allocated for the associated process.

        Get: PagedSystemMemorySize64(self: Process) -> Int64
        """
        ...
    @property
    def PeakPagedMemorySize(self):
        """
        Gets the maximum amount of memory in the virtual memory paging file, in bytes, used by the associated process.

        Get: PeakPagedMemorySize(self: Process) -> int
        """
        ...
    @property
    def PeakPagedMemorySize64(self):
        """
        Gets the maximum amount of memory in the virtual memory paging file, in bytes, used by the associated process.

        Get: PeakPagedMemorySize64(self: Process) -> Int64
        """
        ...
    @property
    def PeakVirtualMemorySize(self):
        """
        Gets the maximum amount of virtual memory, in bytes, used by the associated process.

        Get: PeakVirtualMemorySize(self: Process) -> int
        """
        ...
    @property
    def PeakVirtualMemorySize64(self):
        """
        Gets the maximum amount of virtual memory, in bytes, used by the associated process.

        Get: PeakVirtualMemorySize64(self: Process) -> Int64
        """
        ...
    @property
    def PeakWorkingSet(self):
        """
        Gets the peak working set size for the associated process, in bytes.

        Get: PeakWorkingSet(self: Process) -> int
        """
        ...
    @property
    def PeakWorkingSet64(self):
        """
        Gets the maximum amount of physical memory, in bytes, used by the associated process.

        Get: PeakWorkingSet64(self: Process) -> Int64
        """
        ...
    @property
    def PriorityBoostEnabled(self):
        """
        Gets or sets a value indicating whether the associated process priority should temporarily be boosted by the operating system when the main window has the focus.

        Get: PriorityBoostEnabled(self: Process) -> bool

        Set: PriorityBoostEnabled(self: Process) = value
        """
        ...
    @property
    def PriorityClass(self):
        """
        Gets or sets the overall priority category for the associated process.

        Get: PriorityClass(self: Process) -> ProcessPriorityClass

        Set: PriorityClass(self: Process) = value
        """
        ...
    @property
    def PrivateMemorySize(self):
        """
        Gets the amount of private memory, in bytes, allocated for the associated process.

        Get: PrivateMemorySize(self: Process) -> int
        """
        ...
    @property
    def PrivateMemorySize64(self):
        """
        Gets the amount of private memory, in bytes, allocated for the associated process.

        Get: PrivateMemorySize64(self: Process) -> Int64
        """
        ...
    @property
    def PrivilegedProcessorTime(self):
        """
        Gets the privileged processor time for this process.

        Get: PrivilegedProcessorTime(self: Process) -> TimeSpan
        """
        ...
    @property
    def ProcessName(self):
        """
        Gets the name of the process.

        Get: ProcessName(self: Process) -> str
        """
        ...
    @property
    def ProcessorAffinity(self):
        """
        Gets or sets the processors on which the threads in this process can be scheduled to run.

        Get: ProcessorAffinity(self: Process) -> IntPtr

        Set: ProcessorAffinity(self: Process) = value
        """
        ...
    @property
    def Responding(self):
        """
        Gets a value indicating whether the user interface of the process is responding.

        Get: Responding(self: Process) -> bool
        """
        ...
    @property
    def SafeHandle(self):
        """
        Gets the native handle to this process.

        Get: SafeHandle(self: Process) -> SafeProcessHandle
        """
        ...
    @property
    def SessionId(self):
        """
        Gets the Terminal Services session identifier for the associated process.

        Get: SessionId(self: Process) -> int
        """
        ...
    @property
    def StandardError(self):
        """
        Gets a stream used to read the error output of the application.

        Get: StandardError(self: Process) -> StreamReader
        """
        ...
    @property
    def StandardInput(self):
        """
        Gets a stream used to write the input of the application.

        Get: StandardInput(self: Process) -> StreamWriter
        """
        ...
    @property
    def StandardOutput(self):
        """
        Gets a stream used to read the textual output of the application.

        Get: StandardOutput(self: Process) -> StreamReader
        """
        ...
    @property
    def StartInfo(self):
        """
        Gets or sets the properties to pass to the System.Diagnostics.Process.Start method of the System.Diagnostics.Process.

        Get: StartInfo(self: Process) -> ProcessStartInfo

        Set: StartInfo(self: Process) = value
        """
        ...
    @property
    def StartTime(self):
        """
        Gets the time that the associated process was started.

        Get: StartTime(self: Process) -> DateTime
        """
        ...
    @property
    def SynchronizingObject(self):
        """
        Gets or sets the object used to marshal the event handler calls that are issued as a result of a process exit event.

        Get: SynchronizingObject(self: Process) -> ISynchronizeInvoke

        Set: SynchronizingObject(self: Process) = value
        """
        ...
    @property
    def Threads(self):
        """
        Gets the set of threads that are running in the associated process.

        Get: Threads(self: Process) -> ProcessThreadCollection
        """
        ...
    @property
    def TotalProcessorTime(self):
        """
        Gets the total processor time for this process.

        Get: TotalProcessorTime(self: Process) -> TimeSpan
        """
        ...
    @property
    def UserProcessorTime(self):
        """
        Gets the user processor time for this process.

        Get: UserProcessorTime(self: Process) -> TimeSpan
        """
        ...
    @property
    def VirtualMemorySize(self):
        """
        Gets the size of the process's virtual memory, in bytes.

        Get: VirtualMemorySize(self: Process) -> int
        """
        ...
    @property
    def VirtualMemorySize64(self):
        """
        Gets the amount of the virtual memory, in bytes, allocated for the associated process.

        Get: VirtualMemorySize64(self: Process) -> Int64
        """
        ...
    @property
    def WorkingSet(self):
        """
        Gets the associated process's physical memory usage, in bytes.

        Get: WorkingSet(self: Process) -> int
        """
        ...
    @property
    def WorkingSet64(self):
        """
        Gets the amount of physical memory, in bytes, allocated for the associated process.

        Get: WorkingSet64(self: Process) -> Int64
        """
        ...
    ErrorDataReceived = None
    Exited = None
    OutputDataReceived = None

class ProcessModule(Component):  # skipped bases: <type 'IComponent'>, <type 'IDisposable'>
    """Represents a.dll or .exe file that is loaded into a particular process."""

    @property
    def BaseAddress(self):
        """
        Gets the memory address where the module was loaded.

        Get: BaseAddress(self: ProcessModule) -> IntPtr
        """
        ...
    @property
    def CanRaiseEvents(self):
        """Gets a value indicating whether the component can raise an event."""
        ...
    @property
    def DesignMode(self):
        """Gets a value that indicates whether the System.ComponentModel.Component is currently in design mode."""
        ...
    @property
    def EntryPointAddress(self):
        """
        Gets the memory address for the function that runs when the system loads and runs the module.

        Get: EntryPointAddress(self: ProcessModule) -> IntPtr
        """
        ...
    @property
    def Events(self):
        """Gets the list of event handlers that are attached to this System.ComponentModel.Component."""
        ...
    @property
    def FileName(self):
        """
        Gets the full path to the module.

        Get: FileName(self: ProcessModule) -> str
        """
        ...
    @property
    def FileVersionInfo(self):
        """
        Gets version information about the module.

        Get: FileVersionInfo(self: ProcessModule) -> FileVersionInfo
        """
        ...
    @property
    def ModuleMemorySize(self):
        """
        Gets the amount of memory that is required to load the module.

        Get: ModuleMemorySize(self: ProcessModule) -> int
        """
        ...
    @property
    def ModuleName(self):
        """
        Gets the name of the process module.

        Get: ModuleName(self: ProcessModule) -> str
        """
        ...

class ProcessModuleCollection(ReadOnlyCollectionBase):  # skipped bases: <type 'ICollection'>, <type 'IEnumerable'>
    """
    Provides a strongly typed collection of System.Diagnostics.ProcessModule objects.

    ProcessModuleCollection(processModules: Array[ProcessModule])
    """

    def Contains(self, module):
        """
        Contains(self: ProcessModuleCollection, module: ProcessModule) -> bool

            Determines whether the specified process module exists in the collection.

            module: A System.Diagnostics.ProcessModule instance that indicates the module to find in this collection.

            Returns: ue if the module exists in the collection; otherwise, lse.
        """
        ...
    def CopyTo(self, array, index):
        """
        CopyTo(self: ProcessModuleCollection, array: Array[ProcessModule], index: int)

            Copies an array of System.Diagnostics.ProcessModule instances to the collection, at the specified index.

            array: An array of System.Diagnostics.ProcessModule instances to add to the collection.

            index: The location at which to add the new instances.
        """
        ...
    def IndexOf(self, module):
        """
        IndexOf(self: ProcessModuleCollection, module: ProcessModule) -> int

            Provides the location of a specified module within the collection.

            module: The System.Diagnostics.ProcessModule whose index is retrieved.

            Returns: The zero-based index that defines the location of the module within the System.Diagnostics.ProcessModuleCollection.
        """
        ...
    def __getitem__(self, *args):  # cannot find CLR method
        """x.__getitem__(y) <==> x[y]"""
        ...
    @staticmethod  # known case of __new__
    def __new__(cls, processModules):
        """
        __new__(cls: type)

        __new__(cls: type, processModules: Array[ProcessModule])
        """
        ...
    @property
    def InnerList(self):
        """Gets the list of elements contained in the System.Collections.ReadOnlyCollectionBase instance."""
        ...

class ProcessPriorityClass(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Indicates the priority that the system associates with a process. This value, together with the priority value of each thread of the process, determines each thread's base priority level.

    enum ProcessPriorityClass, values: AboveNormal (32768), BelowNormal (16384), High (128), Idle (64), Normal (32), RealTime (256)
    """

    AboveNormal = None
    BelowNormal = None
    High = None
    Idle = None
    Normal = None
    RealTime = None
    value__ = None

class ProcessStartInfo:  # skipped bases: <type 'object'>
    """
    Specifies a set of values that are used when you start a process.

    ProcessStartInfo()

    ProcessStartInfo(fileName: str)

    ProcessStartInfo(fileName: str, arguments: str)
    """

    @property
    def Arguments(self):
        """
        Gets or sets the set of command-line arguments to use when starting the application.

        Get: Arguments(self: ProcessStartInfo) -> str

        Set: Arguments(self: ProcessStartInfo) = value
        """
        ...
    @property
    def CreateNoWindow(self):
        """
        Gets or sets a value indicating whether to start the process in a new window.

        Get: CreateNoWindow(self: ProcessStartInfo) -> bool

        Set: CreateNoWindow(self: ProcessStartInfo) = value
        """
        ...
    @property
    def Domain(self):
        """
        Gets or sets a value that identifies the domain to use when starting the process.

        Get: Domain(self: ProcessStartInfo) -> str

        Set: Domain(self: ProcessStartInfo) = value
        """
        ...
    @property
    def Environment(self):
        """
        Gets the environment variables that apply to this process and its child processes.

        Get: Environment(self: ProcessStartInfo) -> IDictionary[str, str]
        """
        ...
    @property
    def EnvironmentVariables(self):
        """
        Gets search paths for files, directories for temporary files, application-specific options, and other similar information.

        Get: EnvironmentVariables(self: ProcessStartInfo) -> StringDictionary
        """
        ...
    @property
    def ErrorDialog(self):
        """
        Gets or sets a value indicating whether an error dialog box is displayed to the user if the process cannot be started.

        Get: ErrorDialog(self: ProcessStartInfo) -> bool

        Set: ErrorDialog(self: ProcessStartInfo) = value
        """
        ...
    @property
    def ErrorDialogParentHandle(self):
        """
        Gets or sets the window handle to use when an error dialog box is shown for a process that cannot be started.

        Get: ErrorDialogParentHandle(self: ProcessStartInfo) -> IntPtr

        Set: ErrorDialogParentHandle(self: ProcessStartInfo) = value
        """
        ...
    @property
    def FileName(self):
        """
        Gets or sets the application or document to start.

        Get: FileName(self: ProcessStartInfo) -> str

        Set: FileName(self: ProcessStartInfo) = value
        """
        ...
    @property
    def LoadUserProfile(self):
        """
        Gets or sets a value that indicates whether the Windows user profile is to be loaded from the registry.

        Get: LoadUserProfile(self: ProcessStartInfo) -> bool

        Set: LoadUserProfile(self: ProcessStartInfo) = value
        """
        ...
    @property
    def Password(self):
        """
        Gets or sets a secure string that contains the user password to use when starting the process.

        Get: Password(self: ProcessStartInfo) -> SecureString

        Set: Password(self: ProcessStartInfo) = value
        """
        ...
    @property
    def PasswordInClearText(self):
        """
        Gets or sets the user password in clear text to use when starting the process.

        Get: PasswordInClearText(self: ProcessStartInfo) -> str

        Set: PasswordInClearText(self: ProcessStartInfo) = value
        """
        ...
    @property
    def RedirectStandardError(self):
        """
        Gets or sets a value that indicates whether the error output of an application is written to the System.Diagnostics.Process.StandardError stream.

        Get: RedirectStandardError(self: ProcessStartInfo) -> bool

        Set: RedirectStandardError(self: ProcessStartInfo) = value
        """
        ...
    @property
    def RedirectStandardInput(self):
        """
        Gets or sets a value indicating whether the input for an application is read from the System.Diagnostics.Process.StandardInput stream.

        Get: RedirectStandardInput(self: ProcessStartInfo) -> bool

        Set: RedirectStandardInput(self: ProcessStartInfo) = value
        """
        ...
    @property
    def RedirectStandardOutput(self):
        """
        Gets or sets a value that indicates whether the textual output of an application is written to the System.Diagnostics.Process.StandardOutput stream.

        Get: RedirectStandardOutput(self: ProcessStartInfo) -> bool

        Set: RedirectStandardOutput(self: ProcessStartInfo) = value
        """
        ...
    @property
    def StandardErrorEncoding(self):
        """
        Gets or sets the preferred encoding for error output.

        Get: StandardErrorEncoding(self: ProcessStartInfo) -> Encoding

        Set: StandardErrorEncoding(self: ProcessStartInfo) = value
        """
        ...
    @property
    def StandardOutputEncoding(self):
        """
        Gets or sets the preferred encoding for standard output.

        Get: StandardOutputEncoding(self: ProcessStartInfo) -> Encoding

        Set: StandardOutputEncoding(self: ProcessStartInfo) = value
        """
        ...
    @property
    def UserName(self):
        """
        Gets or sets the user name to be used when starting the process.

        Get: UserName(self: ProcessStartInfo) -> str

        Set: UserName(self: ProcessStartInfo) = value
        """
        ...
    @property
    def UseShellExecute(self):
        """
        Gets or sets a value indicating whether to use the operating system shell to start the process.

        Get: UseShellExecute(self: ProcessStartInfo) -> bool

        Set: UseShellExecute(self: ProcessStartInfo) = value
        """
        ...
    @property
    def Verb(self):
        """
        Gets or sets the verb to use when opening the application or document specified by the System.Diagnostics.ProcessStartInfo.FileName property.

        Get: Verb(self: ProcessStartInfo) -> str

        Set: Verb(self: ProcessStartInfo) = value
        """
        ...
    @property
    def Verbs(self):
        """
        Gets the set of verbs associated with the type of file specified by the System.Diagnostics.ProcessStartInfo.FileName property.

        Get: Verbs(self: ProcessStartInfo) -> Array[str]
        """
        ...
    @property
    def WindowStyle(self):
        """
        Gets or sets the window state to use when the process is started.

        Get: WindowStyle(self: ProcessStartInfo) -> ProcessWindowStyle

        Set: WindowStyle(self: ProcessStartInfo) = value
        """
        ...
    @property
    def WorkingDirectory(self):
        """
        When the System.Diagnostics.ProcessStartInfo.UseShellExecute property is lse, gets or sets the working directory for the process to be started. When System.Diagnostics.ProcessStartInfo.UseShellExecute is ue, gets or sets the directory that contains the process to be started.

        Get: WorkingDirectory(self: ProcessStartInfo) -> str

        Set: WorkingDirectory(self: ProcessStartInfo) = value
        """
        ...

class ProcessThread(Component):  # skipped bases: <type 'IComponent'>, <type 'IDisposable'>
    """Represents an operating system process thread."""

    def ResetIdealProcessor(self):
        """
        ResetIdealProcessor(self: ProcessThread)

            Resets the ideal processor for this thread to indicate that there is no single ideal processor. In other words, so that any processor is ideal.
        """
        ...
    @property
    def BasePriority(self):
        """
        Gets the base priority of the thread.

        Get: BasePriority(self: ProcessThread) -> int
        """
        ...
    @property
    def CanRaiseEvents(self):
        """Gets a value indicating whether the component can raise an event."""
        ...
    @property
    def CurrentPriority(self):
        """
        Gets the current priority of the thread.

        Get: CurrentPriority(self: ProcessThread) -> int
        """
        ...
    @property
    def DesignMode(self):
        """Gets a value that indicates whether the System.ComponentModel.Component is currently in design mode."""
        ...
    @property
    def Events(self):
        """Gets the list of event handlers that are attached to this System.ComponentModel.Component."""
        ...
    @property
    def Id(self):
        """
        Gets the unique identifier of the thread.

        Get: Id(self: ProcessThread) -> int
        """
        ...
    @property
    def IdealProcessor(self):
        """
        Sets the preferred processor for this thread to run on.

        Set: IdealProcessor(self: ProcessThread) = value
        """
        ...
    @property
    def PriorityBoostEnabled(self):
        """
        Gets or sets a value indicating whether the operating system should temporarily boost the priority of the associated thread whenever the main window of the thread's process receives the focus.

        Get: PriorityBoostEnabled(self: ProcessThread) -> bool

        Set: PriorityBoostEnabled(self: ProcessThread) = value
        """
        ...
    @property
    def PriorityLevel(self):
        """
        Gets or sets the priority level of the thread.

        Get: PriorityLevel(self: ProcessThread) -> ThreadPriorityLevel

        Set: PriorityLevel(self: ProcessThread) = value
        """
        ...
    @property
    def PrivilegedProcessorTime(self):
        """
        Gets the amount of time that the thread has spent running code inside the operating system core.

        Get: PrivilegedProcessorTime(self: ProcessThread) -> TimeSpan
        """
        ...
    @property
    def ProcessorAffinity(self):
        """
        Sets the processors on which the associated thread can run.

        Set: ProcessorAffinity(self: ProcessThread) = value
        """
        ...
    @property
    def StartAddress(self):
        """
        Gets the memory address of the function that the operating system called that started this thread.

        Get: StartAddress(self: ProcessThread) -> IntPtr
        """
        ...
    @property
    def StartTime(self):
        """
        Gets the time that the operating system started the thread.

        Get: StartTime(self: ProcessThread) -> DateTime
        """
        ...
    @property
    def ThreadState(self):
        """
        Gets the current state of this thread.

        Get: ThreadState(self: ProcessThread) -> ThreadState
        """
        ...
    @property
    def TotalProcessorTime(self):
        """
        Gets the total amount of time that this thread has spent using the processor.

        Get: TotalProcessorTime(self: ProcessThread) -> TimeSpan
        """
        ...
    @property
    def UserProcessorTime(self):
        """
        Gets the amount of time that the associated thread has spent running code inside the application.

        Get: UserProcessorTime(self: ProcessThread) -> TimeSpan
        """
        ...
    @property
    def WaitReason(self):
        """
        Gets the reason that the thread is waiting.

        Get: WaitReason(self: ProcessThread) -> ThreadWaitReason
        """
        ...

class ProcessThreadCollection(ReadOnlyCollectionBase):  # skipped bases: <type 'ICollection'>, <type 'IEnumerable'>
    """
    Provides a strongly typed collection of System.Diagnostics.ProcessThread objects.

    ProcessThreadCollection(processThreads: Array[ProcessThread])
    """

    def Add(self, thread):
        """
        Add(self: ProcessThreadCollection, thread: ProcessThread) -> int

            Appends a process thread to the collection.

            thread: The thread to add to the collection.

            Returns: The zero-based index of the thread in the collection.
        """
        ...
    def Contains(self, thread):
        """
        Contains(self: ProcessThreadCollection, thread: ProcessThread) -> bool

            Determines whether the specified process thread exists in the collection.

            thread: A System.Diagnostics.ProcessThread instance that indicates the thread to find in this collection.

            Returns: ue if the thread exists in the collection; otherwise, lse.
        """
        ...
    def CopyTo(self, array, index):
        """
        CopyTo(self: ProcessThreadCollection, array: Array[ProcessThread], index: int)

            Copies an array of System.Diagnostics.ProcessThread instances to the collection, at the specified index.

            array: An array of System.Diagnostics.ProcessThread instances to add to the collection.

            index: The location at which to add the new instances.
        """
        ...
    def IndexOf(self, thread):
        """
        IndexOf(self: ProcessThreadCollection, thread: ProcessThread) -> int

            Provides the location of a specified thread within the collection.

            thread: The System.Diagnostics.ProcessThread whose index is retrieved.

            Returns: The zero-based index that defines the location of the thread within the System.Diagnostics.ProcessThreadCollection.
        """
        ...
    def Insert(self, index, thread):
        """
        Insert(self: ProcessThreadCollection, index: int, thread: ProcessThread)

            Inserts a process thread at the specified location in the collection.

            index: The zero-based index indicating the location at which to insert the thread.

            thread: The thread to insert into the collection.
        """
        ...
    def Remove(self, thread):
        """
        Remove(self: ProcessThreadCollection, thread: ProcessThread)

            Deletes a process thread from the collection.

            thread: The thread to remove from the collection.
        """
        ...
    def __add__(self, *args):  # cannot find CLR method
        """x.__add__(y) <==> x+y"""
        ...
    def __getitem__(self, *args):  # cannot find CLR method
        """x.__getitem__(y) <==> x[y]"""
        ...
    @staticmethod  # known case of __new__
    def __new__(cls, processThreads):
        """
        __new__(cls: type)

        __new__(cls: type, processThreads: Array[ProcessThread])
        """
        ...
    @property
    def InnerList(self):
        """Gets the list of elements contained in the System.Collections.ReadOnlyCollectionBase instance."""
        ...

class ProcessWindowStyle(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specified how a new window should appear when the system starts a process.

    enum ProcessWindowStyle, values: Hidden (1), Maximized (3), Minimized (2), Normal (0)
    """

    Hidden = None
    Maximized = None
    Minimized = None
    Normal = None
    value__ = None

class SourceFilter(TraceFilter):
    """
    Indicates whether a listener should trace a message based on the source of a trace.

    SourceFilter(source: str)
    """

    @staticmethod  # known case of __new__
    def __new__(cls, source):
        """__new__(cls: type, source: str)"""
        ...
    @property
    def Source(self):
        """
        Gets or sets the name of the trace source.

        Get: Source(self: SourceFilter) -> str

        Set: Source(self: SourceFilter) = value
        """
        ...

class SourceLevels(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies the levels of trace messages filtered by the source switch and event type filter.

    enum (flags) SourceLevels, values: ActivityTracing (65280), All (-1), Critical (1), Error (3), Information (15), Off (0), Verbose (31), Warning (7)
    """

    ActivityTracing = None
    All = None
    Critical = None
    Error = None
    Information = None
    Off = None
    value__ = None
    Verbose = None
    Warning = None

class SourceSwitch(Switch):
    """
    Provides a multilevel switch to control tracing and debug output without recompiling your code.

    SourceSwitch(name: str)

    SourceSwitch(displayName: str, defaultSwitchValue: str)
    """

    def ShouldTrace(self, eventType):
        """
        ShouldTrace(self: SourceSwitch, eventType: TraceEventType) -> bool

            Determines if trace listeners should be called, based on the trace event type.

            eventType: One of the System.Diagnostics.TraceEventType values.

            Returns: ue if the trace listeners should be called; otherwise, lse.
        """
        ...
    @property
    def Level(self):
        """
        Gets or sets the level of the switch.

        Get: Level(self: SourceSwitch) -> SourceLevels

        Set: Level(self: SourceSwitch) = value
        """
        ...
    @property
    def SwitchSetting(self):
        """Gets or sets the current setting for this switch."""
        ...
    @property
    def Value(self):
        """Gets or sets the value of the switch."""
        ...

class StackFrame:  # skipped bases: <type 'object'>
    """
    Provides information about a System.Diagnostics.StackFrame, which represents a function call on the call stack for the current thread.

    StackFrame()

    StackFrame(fNeedFileInfo: bool)

    StackFrame(skipFrames: int)

    StackFrame(skipFrames: int, fNeedFileInfo: bool)

    StackFrame(fileName: str, lineNumber: int)

    StackFrame(fileName: str, lineNumber: int, colNumber: int)
    """

    def GetFileColumnNumber(self):
        """
        GetFileColumnNumber(self: StackFrame) -> int

            Gets the column number in the file that contains the code that is executing. This information is typically extracted from the debugging symbols for the executable.

            Returns: The file column number, or 0 (zero) if the file column number cannot be determined.
        """
        ...
    def GetFileLineNumber(self):
        """
        GetFileLineNumber(self: StackFrame) -> int

            Gets the line number in the file that contains the code that is executing. This information is typically extracted from the debugging symbols for the executable.

            Returns: The file line number, or 0 (zero) if the file line number cannot be determined.
        """
        ...
    def GetFileName(self):
        """
        GetFileName(self: StackFrame) -> str

            Gets the file name that contains the code that is executing. This information is typically extracted from the debugging symbols for the executable.

            Returns: The file name, or ll if the file name cannot be determined.
        """
        ...
    def GetILOffset(self):
        """
        GetILOffset(self: StackFrame) -> int

            Gets the offset from the start of the Microsoft intermediate language (MSIL) code for the method that is executing. This offset might be an approximation depending on whether or not the just-in-time (JIT) compiler is generating

             debugging code. The generation of this debugging information is controlled by the System.Diagnostics.DebuggableAttribute.

            Returns: The offset from the start of the MSIL code for the method that is executing.
        """
        ...
    def GetMethod(self):
        """
        GetMethod(self: StackFrame) -> MethodBase

            Gets the method in which the frame is executing.

            Returns: The method in which the frame is executing.
        """
        ...
    def GetNativeOffset(self):
        """
        GetNativeOffset(self: StackFrame) -> int

            Gets the offset from the start of the native just-in-time (JIT)-compiled code for the method that is being executed. The generation of this debugging information is controlled by the System.Diagnostics.DebuggableAttribute class.

            Returns: The offset from the start of the JIT-compiled code for the method that is being executed.
        """
        ...
    def ToString(self):
        """
        ToString(self: StackFrame) -> str

            Builds a readable representation of the stack trace.

            Returns: A readable representation of the stack trace.
        """
        ...
    OFFSET_UNKNOWN = -1

class StackFrameExtensions:  # skipped bases: <type 'object'>
    """Provides extension methods for the System.Diagnostics.StackFrame class, which represents a function call on the call stack for the current thread."""

    @staticmethod
    def GetNativeImageBase(stackFrame):
        """
        GetNativeImageBase(stackFrame: StackFrame) -> IntPtr

            Returns a pointer to the base address of the native just-in-time (JIT)-compiled image that this stack frame is executing.

            stackFrame: A stack frame.

            Returns: This method always returns System.IntPtr.Zero.
        """
        ...
    @staticmethod
    def GetNativeIP(stackFrame):
        """
        GetNativeIP(stackFrame: StackFrame) -> IntPtr

            Gets an interface pointer to the start of the native code for the method that is being executed.

            stackFrame: A stack frame.

            Returns: This method always returns  System.IntPtr.Zero.
        """
        ...
    @staticmethod
    def HasILOffset(stackFrame):
        """
        HasILOffset(stackFrame: StackFrame) -> bool

            Indicates whether an offset from the start of the IL code for the method that is executing is available.

            stackFrame: A stack frame.

            Returns: ue if the offset is available; otherwise, lse.
        """
        ...
    @staticmethod
    def HasMethod(stackFrame):
        """
        HasMethod(stackFrame: StackFrame) -> bool

            Indicates whether information about the method in which the specified frame is executing is available.

            stackFrame: A stack frame.

            Returns: ue if information about the method in which the current frame is executing is available; otherwise, lse.
        """
        ...
    @staticmethod
    def HasNativeImage(stackFrame):
        """
        HasNativeImage(stackFrame: StackFrame) -> bool

            Indicates whether the native just-in-time (JIT)-compiled image is available for the specified stack frame.

            stackFrame: A stack frame.

            Returns: ue if a native image is available for this stack frame; otherwise, lse.
        """
        ...
    @staticmethod
    def HasSource(stackFrame):
        """
        HasSource(stackFrame: StackFrame) -> bool

            Indicates whether the file that contains the code that the specified stack frame is executing is available.

            stackFrame: A stack frame.

            Returns: ue if the code that the specified stack frame is executing is available; otherwise, lse.
        """
        ...
    __all__ = [
        "GetNativeImageBase",
        "GetNativeIP",
        "HasILOffset",
        "HasMethod",
        "HasNativeImage",
        "HasSource",
    ]

class StackTrace:  # skipped bases: <type 'object'>
    """
    Represents a stack trace, which is an ordered collection of one or more stack frames.

    StackTrace()

    StackTrace(fNeedFileInfo: bool)

    StackTrace(skipFrames: int)

    StackTrace(skipFrames: int, fNeedFileInfo: bool)

    StackTrace(e: Exception)

    StackTrace(e: Exception, fNeedFileInfo: bool)

    StackTrace(e: Exception, skipFrames: int)

    StackTrace(e: Exception, skipFrames: int, fNeedFileInfo: bool)

    StackTrace(frame: StackFrame)

    StackTrace(targetThread: Thread, needFileInfo: bool)
    """

    def GetFrame(self, index):
        """
        GetFrame(self: StackTrace, index: int) -> StackFrame

            Gets the specified stack frame.

            index: The index of the stack frame requested.

            Returns: The specified stack frame.
        """
        ...
    def GetFrames(self):
        """
        GetFrames(self: StackTrace) -> Array[StackFrame]

            Returns a copy of all stack frames in the current stack trace.

            Returns: An array of type System.Diagnostics.StackFrame representing the function calls in the stack trace.
        """
        ...
    def ToString(self):
        """
        ToString(self: StackTrace) -> str

            Builds a readable representation of the stack trace.

            Returns: A readable representation of the stack trace.
        """
        ...
    @property
    def FrameCount(self):
        """
        Gets the number of frames in the stack trace.

        Get: FrameCount(self: StackTrace) -> int
        """
        ...
    METHODS_TO_SKIP = 0

class Stopwatch:  # skipped bases: <type 'object'>
    """
    Provides a set of methods and properties that you can use to accurately measure elapsed time.To browse the .NET Framework source code for this type, see the Reference Source.

    Stopwatch()
    """

    @staticmethod
    def GetTimestamp():
        """
        GetTimestamp() -> Int64

            Gets the current number of ticks in the timer mechanism.

            Returns: A long integer representing the tick counter value of the underlying timer mechanism.
        """
        ...
    def Reset(self):
        """
        Reset(self: Stopwatch)

            Stops time interval measurement and resets the elapsed time to zero.
        """
        ...
    def Restart(self):
        """
        Restart(self: Stopwatch)

            Stops time interval measurement, resets the elapsed time to zero, and starts measuring elapsed time.
        """
        ...
    def Start(self):
        """
        Start(self: Stopwatch)

            Starts, or resumes, measuring elapsed time for an interval.
        """
        ...
    @staticmethod
    def StartNew():
        """
        StartNew() -> Stopwatch

            Initializes a new System.Diagnostics.Stopwatch instance, sets the elapsed time property to zero, and starts measuring elapsed time.

            Returns: A System.Diagnostics.Stopwatch that has just begun measuring elapsed time.
        """
        ...
    def Stop(self):
        """
        Stop(self: Stopwatch)

            Stops measuring elapsed time for an interval.
        """
        ...
    @property
    def Elapsed(self):
        """
        Gets the total elapsed time measured by the current instance.

        Get: Elapsed(self: Stopwatch) -> TimeSpan
        """
        ...
    @property
    def ElapsedMilliseconds(self):
        """
        Gets the total elapsed time measured by the current instance, in milliseconds.

        Get: ElapsedMilliseconds(self: Stopwatch) -> Int64
        """
        ...
    @property
    def ElapsedTicks(self):
        """
        Gets the total elapsed time measured by the current instance, in timer ticks.

        Get: ElapsedTicks(self: Stopwatch) -> Int64
        """
        ...
    @property
    def IsRunning(self):
        """
        Gets a value indicating whether the System.Diagnostics.Stopwatch timer is running.

        Get: IsRunning(self: Stopwatch) -> bool
        """
        ...
    Frequency = None
    IsHighResolution = True

class SwitchAttribute(Attribute):  # skipped bases: <type '_Attribute'>
    """
    Identifies a switch used in an assembly, class, or member.

    SwitchAttribute(switchName: str, switchType: Type)
    """

    @staticmethod
    def GetAll(assembly):
        """
        GetAll(assembly: Assembly) -> Array[SwitchAttribute]

            Returns all switch attributes for the specified assembly.

            assembly: The assembly to check for switch attributes.

            Returns: An array that contains all the switch attributes for the assembly.
        """
        ...
    @staticmethod  # known case of __new__
    def __new__(cls, switchName, switchType):
        """__new__(cls: type, switchName: str, switchType: Type)"""
        ...
    @property
    def SwitchDescription(self):
        """
        Gets or sets the description of the switch.

        Get: SwitchDescription(self: SwitchAttribute) -> str

        Set: SwitchDescription(self: SwitchAttribute) = value
        """
        ...
    @property
    def SwitchName(self):
        """
        Gets or sets the display name of the switch.

        Get: SwitchName(self: SwitchAttribute) -> str

        Set: SwitchName(self: SwitchAttribute) = value
        """
        ...
    @property
    def SwitchType(self):
        """
        Gets or sets the type of the switch.

        Get: SwitchType(self: SwitchAttribute) -> Type

        Set: SwitchType(self: SwitchAttribute) = value
        """
        ...

class SwitchLevelAttribute(Attribute):  # skipped bases: <type '_Attribute'>
    """
    Identifies the level type for a switch.

    SwitchLevelAttribute(switchLevelType: Type)
    """

    @staticmethod  # known case of __new__
    def __new__(cls, switchLevelType):
        """__new__(cls: type, switchLevelType: Type)"""
        ...
    @property
    def SwitchLevelType(self):
        """
        Gets or sets the type that determines whether a trace should be written.

        Get: SwitchLevelType(self: SwitchLevelAttribute) -> Type

        Set: SwitchLevelType(self: SwitchLevelAttribute) = value
        """
        ...

class ThreadPriorityLevel(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies the priority level of a thread.

    enum ThreadPriorityLevel, values: AboveNormal (1), BelowNormal (-1), Highest (2), Idle (-15), Lowest (-2), Normal (0), TimeCritical (15)
    """

    AboveNormal = None
    BelowNormal = None
    Highest = None
    Idle = None
    Lowest = None
    Normal = None
    TimeCritical = None
    value__ = None

class ThreadState(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies the current execution state of the thread.

    enum ThreadState, values: Initialized (0), Ready (1), Running (2), Standby (3), Terminated (4), Transition (6), Unknown (7), Wait (5)
    """

    Initialized = None
    Ready = None
    Running = None
    Standby = None
    Terminated = None
    Transition = None
    Unknown = None
    value__ = None
    Wait = None

class ThreadWaitReason(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies the reason a thread is waiting.

    enum ThreadWaitReason, values: EventPairHigh (7), EventPairLow (8), ExecutionDelay (4), Executive (0), FreePage (1), LpcReceive (9), LpcReply (10), PageIn (2), PageOut (12), Suspended (5), SystemAllocation (3), Unknown (13), UserRequest (6), VirtualMemory (11)
    """

    EventPairHigh = None
    EventPairLow = None
    ExecutionDelay = None
    Executive = None
    FreePage = None
    LpcReceive = None
    LpcReply = None
    PageIn = None
    PageOut = None
    Suspended = None
    SystemAllocation = None
    Unknown = None
    UserRequest = None
    value__ = None
    VirtualMemory = None

class Trace:  # skipped bases: <type 'object'>
    """Provides a set of methods and properties that help you trace the execution of your code. This class cannot be inherited."""

    @staticmethod
    def Assert(condition, message=None, detailMessage=None):
        """
        Assert(condition: bool)

            Checks for a condition; if the condition is lse, displays a message box that shows the call stack.

            condition: The conditional expression to evaluate. If the condition is ue, a failure message is not sent and the message box is not displayed.

        Assert(condition: bool, message: str)

            Checks for a condition; if the condition is lse, outputs a specified message and displays a message box that shows the call stack.

            condition: The conditional expression to evaluate. If the condition is ue, the specified message is not sent and the message box is not displayed.

            message: The message to send to the System.Diagnostics.Trace.Listeners collection.

        Assert(condition: bool, message: str, detailMessage: str)

            Checks for a condition; if the condition is lse, outputs two specified messages and displays a message box that shows the call stack.

            condition: The conditional expression to evaluate. If the condition is ue, the specified messages are not sent and the message box is not displayed.

            message: The message to send to the System.Diagnostics.Trace.Listeners collection.

            detailMessage: The detailed message to send to the System.Diagnostics.Trace.Listeners collection.
        """
        ...
    @staticmethod
    def Close():
        """
        Close()

            Flushes the output buffer, and then closes the System.Diagnostics.Trace.Listeners.
        """
        ...
    @staticmethod
    def Fail(message, detailMessage=None):
        """
        Fail(message: str)

            Emits the specified error message.

            message: A message to emit.

        Fail(message: str, detailMessage: str)

            Emits an error message, and a detailed error message.

            message: A message to emit.

            detailMessage: A detailed message to emit.
        """
        ...
    @staticmethod
    def Flush():
        """
        Flush()

            Flushes the output buffer, and causes buffered data to be written to the System.Diagnostics.Trace.Listeners.
        """
        ...
    @staticmethod
    def Indent():
        """
        Indent()

            Increases the current System.Diagnostics.Trace.IndentLevel by one.
        """
        ...
    @staticmethod
    def Refresh():
        """
        Refresh()

            Refreshes the trace configuration data.
        """
        ...
    @staticmethod
    def TraceError(*__args):
        """
        TraceError(message: str)

            Writes an error message to the trace listeners in the System.Diagnostics.Trace.Listeners collection using the specified message.

            message: The informative message to write.

        TraceError(format: str, *args: Array[object])

            Writes an error message to the trace listeners in the System.Diagnostics.Trace.Listeners collection using the specified array of objects and formatting information.

            format: A format string that contains zero or more format items, which correspond to objects in the args array.

            args: An ject array containing zero or more objects to format.
        """
        ...
    @staticmethod
    def TraceInformation(*__args):
        """
        TraceInformation(message: str)

            Writes an informational message to the trace listeners in the System.Diagnostics.Trace.Listeners collection using the specified message.

            message: The informative message to write.

        TraceInformation(format: str, *args: Array[object])

            Writes an informational message to the trace listeners in the System.Diagnostics.Trace.Listeners collection using the specified array of objects and formatting information.

            format: A format string that contains zero or more format items, which correspond to objects in the args array.

            args: An ject array containing zero or more objects to format.
        """
        ...
    @staticmethod
    def TraceWarning(*__args):
        """
        TraceWarning(message: str)

            Writes a warning message to the trace listeners in the System.Diagnostics.Trace.Listeners collection using the specified message.

            message: The informative message to write.

        TraceWarning(format: str, *args: Array[object])

            Writes a warning message to the trace listeners in the System.Diagnostics.Trace.Listeners collection using the specified array of objects and formatting information.

            format: A format string that contains zero or more format items, which correspond to objects in the args array.

            args: An ject array containing zero or more objects to format.
        """
        ...
    @staticmethod
    def Unindent():
        """
        Unindent()

            Decreases the current System.Diagnostics.Trace.IndentLevel by one.
        """
        ...
    @staticmethod
    def Write(*__args):
        """
        Write(message: str)

            Writes a message to the trace listeners in the System.Diagnostics.Trace.Listeners collection.

            message: A message to write.

        Write(value: object)

            Writes the value of the object's System.Object.ToString method to the trace listeners in the System.Diagnostics.Trace.Listeners collection.

            value: An System.Object whose name is sent to the System.Diagnostics.Trace.Listeners.

        Write(message: str, category: str)

            Writes a category name and a message to the trace listeners in the System.Diagnostics.Trace.Listeners collection.

            message: A message to write.

            category: A category name used to organize the output.

        Write(value: object, category: str)

            Writes a category name and the value of the object's System.Object.ToString method to the trace listeners in the System.Diagnostics.Trace.Listeners collection.

            value: An System.Object name is sent to the System.Diagnostics.Trace.Listeners.

            category: A category name used to organize the output.
        """
        ...
    @staticmethod
    def WriteIf(condition, *__args):
        """
        WriteIf(condition: bool, message: str)

            Writes a message to the trace listeners in the System.Diagnostics.Trace.Listeners collection if a condition is ue.

            condition: ue to cause a message to be written; otherwise, lse.

            message: A message to write.

        WriteIf(condition: bool, value: object)

            Writes the value of the object's System.Object.ToString method to the trace listeners in the System.Diagnostics.Trace.Listeners collection if a condition is ue.

            condition: ue to cause a message to be written; otherwise, lse.

            value: An System.Object whose name is sent to the System.Diagnostics.Trace.Listeners.

        WriteIf(condition: bool, message: str, category: str)

            Writes a category name and message to the trace listeners in the System.Diagnostics.Trace.Listeners collection if a condition is ue.

            condition: ue to cause a message to be written; otherwise, lse.

            message: A message to write.

            category: A category name used to organize the output.

        WriteIf(condition: bool, value: object, category: str)

            Writes a category name and the value of the object's System.Object.ToString method to the trace listeners in the System.Diagnostics.Trace.Listeners collection if a condition is ue.

            condition: ue to cause a message to be written; otherwise, lse.

            value: An System.Object whose name is sent to the System.Diagnostics.Trace.Listeners.

            category: A category name used to organize the output.
        """
        ...
    @staticmethod
    def WriteLine(*__args):
        """
        WriteLine(message: str)

            Writes a message to the trace listeners in the System.Diagnostics.Trace.Listeners collection.

            message: A message to write.

        WriteLine(value: object)

            Writes the value of the object's System.Object.ToString method to the trace listeners in the System.Diagnostics.Trace.Listeners collection.

            value: An System.Object whose name is sent to the System.Diagnostics.Trace.Listeners.

        WriteLine(message: str, category: str)

            Writes a category name and message to the trace listeners in the System.Diagnostics.Trace.Listeners collection.

            message: A message to write.

            category: A category name used to organize the output.

        WriteLine(value: object, category: str)

            Writes a category name and the value of the object's System.Object.ToString method to the trace listeners in the System.Diagnostics.Trace.Listeners collection.

            value: An System.Object whose name is sent to the System.Diagnostics.Trace.Listeners.

            category: A category name used to organize the output.
        """
        ...
    @staticmethod
    def WriteLineIf(condition, *__args):
        """
        WriteLineIf(condition: bool, message: str)

            Writes a message to the trace listeners in the System.Diagnostics.Trace.Listeners collection if a condition is ue.

            condition: ue to cause a message to be written; otherwise, lse.

            message: A message to write.

        WriteLineIf(condition: bool, value: object)

            Writes the value of the object's System.Object.ToString method to the trace listeners in the System.Diagnostics.Trace.Listeners collection if a condition is ue.

            condition: ue to cause a message to be written; otherwise, lse.

            value: An System.Object whose name is sent to the System.Diagnostics.Trace.Listeners.

        WriteLineIf(condition: bool, message: str, category: str)

            Writes a category name and message to the trace listeners in the System.Diagnostics.Trace.Listeners collection if a condition is ue.

            condition: ue to cause a message to be written; otherwise, lse.

            message: A message to write.

            category: A category name used to organize the output.

        WriteLineIf(condition: bool, value: object, category: str)

            Writes a category name and the value of the object's System.Object.ToString method to the trace listeners in the System.Diagnostics.Trace.Listeners collection if a condition is ue.

            condition: ue to cause a message to be written; otherwise, lse.

            value: An System.Object whose name is sent to the System.Diagnostics.Trace.Listeners.

            category: A category name used to organize the output.
        """
        ...
    AutoFlush = False
    CorrelationManager = None
    IndentLevel = 0
    IndentSize = 4
    Listeners = None
    UseGlobalLock = True

class TraceEventCache:  # skipped bases: <type 'object'>
    """
    Provides trace event data specific to a thread and a process.

    TraceEventCache()
    """

    @property
    def Callstack(self):
        """
        Gets the call stack for the current thread.

        Get: Callstack(self: TraceEventCache) -> str
        """
        ...
    @property
    def DateTime(self):
        """
        Gets the date and time at which the event trace occurred.

        Get: DateTime(self: TraceEventCache) -> DateTime
        """
        ...
    @property
    def LogicalOperationStack(self):
        """
        Gets the correlation data, contained in a stack.

        Get: LogicalOperationStack(self: TraceEventCache) -> Stack
        """
        ...
    @property
    def ProcessId(self):
        """
        Gets the unique identifier of the current process.

        Get: ProcessId(self: TraceEventCache) -> int
        """
        ...
    @property
    def ThreadId(self):
        """
        Gets a unique identifier for the current managed thread.

        Get: ThreadId(self: TraceEventCache) -> str
        """
        ...
    @property
    def Timestamp(self):
        """
        Gets the current number of ticks in the timer mechanism.

        Get: Timestamp(self: TraceEventCache) -> Int64
        """
        ...

class TraceEventType(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Identifies the type of event that has caused the trace.

    enum TraceEventType, values: Critical (1), Error (2), Information (8), Resume (2048), Start (256), Stop (512), Suspend (1024), Transfer (4096), Verbose (16), Warning (4)
    """

    Critical = None
    Error = None
    Information = None
    Resume = None
    Start = None
    Stop = None
    Suspend = None
    Transfer = None
    value__ = None
    Verbose = None
    Warning = None

class TraceLevel(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies what messages to output for the System.Diagnostics.Debug, System.Diagnostics.Trace and System.Diagnostics.TraceSwitch classes.

    enum TraceLevel, values: Error (1), Info (3), Off (0), Verbose (4), Warning (2)
    """

    Error = None
    Info = None
    Off = None
    value__ = None
    Verbose = None
    Warning = None

class TraceListenerCollection(object, IList):  # skipped bases: <type 'ICollection'>, <type 'IEnumerable'>
    """Provides a thread-safe list of System.Diagnostics.TraceListener objects."""

    def AddRange(self, value):
        """
        AddRange(self: TraceListenerCollection, value: Array[TraceListener])

            Adds an array of System.Diagnostics.TraceListener objects to the list.

            value: An array of System.Diagnostics.TraceListener objects to add to the list.

        AddRange(self: TraceListenerCollection, value: TraceListenerCollection)

            Adds the contents of another System.Diagnostics.TraceListenerCollection to the list.

            value: Another System.Diagnostics.TraceListenerCollection whose contents are added to the list.
        """
        ...
    def CopyTo(self, listeners, index):
        """
        CopyTo(self: TraceListenerCollection, listeners: Array[TraceListener], index: int)

            Copies a section of the current System.Diagnostics.TraceListenerCollection list to the specified array at the specified index.

            listeners: An array of type System.Array to copy the elements into.

            index: The starting index number in the current list to copy from.
        """
        ...
    def GetEnumerator(self):
        """
        GetEnumerator(self: TraceListenerCollection) -> IEnumerator

            Gets an enumerator for this list.

            Returns: An enumerator of type System.Collections.IEnumerator.
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
    def Count(self):
        """
        Gets the number of listeners in the list.

        Get: Count(self: TraceListenerCollection) -> int
        """
        ...

class TraceOptions(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies trace data options to be written to the trace output.

    enum (flags) TraceOptions, values: Callstack (32), DateTime (2), LogicalOperationStack (1), None (0), ProcessId (8), ThreadId (16), Timestamp (4)
    """

    Callstack = None
    DateTime = None
    LogicalOperationStack = None

    ProcessId = None
    ThreadId = None
    Timestamp = None
    value__ = None

class TraceSource:  # skipped bases: <type 'object'>
    """
    Provides a set of methods and properties that enable applications to trace the execution of code and associate trace messages with their source.

    TraceSource(name: str)

    TraceSource(name: str, defaultLevel: SourceLevels)
    """

    def Close(self):
        """
        Close(self: TraceSource)

            Closes all the trace listeners in the trace listener collection.
        """
        ...
    def Flush(self):
        """
        Flush(self: TraceSource)

            Flushes all the trace listeners in the trace listener collection.
        """
        ...
    def GetSupportedAttributes(self, *args):  # cannot find CLR method
        """
        GetSupportedAttributes(self: TraceSource) -> Array[str]

            Gets the custom attributes supported by the trace source.

            Returns: A string array naming the custom attributes supported by the trace source, or ll if there are no custom attributes.
        """
        ...
    def TraceData(self, eventType, id, data):
        """
        TraceData(self: TraceSource, eventType: TraceEventType, id: int, data: object)

            Writes trace data to the trace listeners in the System.Diagnostics.TraceSource.Listeners collection using the specified event type, event identifier, and trace data.

            eventType: One of the enumeration values that specifies the event type of the trace data.

            id: A numeric identifier for the event.

            data: The trace data.

        TraceData(self: TraceSource, eventType: TraceEventType, id: int, *data: Array[object])

            Writes trace data to the trace listeners in the System.Diagnostics.TraceSource.Listeners collection using the specified event type, event identifier, and trace data array.

            eventType: One of the enumeration values that specifies the event type of the trace data.

            id: A numeric identifier for the event.

            data: An object array containing the trace data.
        """
        ...
    def TraceEvent(self, eventType, id, *__args):
        """
        TraceEvent(self: TraceSource, eventType: TraceEventType, id: int)

            Writes a trace event message to the trace listeners in the System.Diagnostics.TraceSource.Listeners collection using the specified event type and event identifier.

            eventType: One of the enumeration values that specifies the event type of the trace data.

            id: A numeric identifier for the event.

        TraceEvent(self: TraceSource, eventType: TraceEventType, id: int, message: str)

            Writes a trace event message to the trace listeners in the System.Diagnostics.TraceSource.Listeners collection using the specified event type, event identifier, and message.

            eventType: One of the enumeration values that specifies the event type of the trace data.

            id: A numeric identifier for the event.

            message: The trace message to write.

        TraceEvent(self: TraceSource, eventType: TraceEventType, id: int, format: str, *args: Array[object])

            Writes a trace event to the trace listeners in the System.Diagnostics.TraceSource.Listeners collection using the specified event type, event identifier, and argument array and format.

            eventType: One of the enumeration values that specifies the event type of the trace data.

            id: A numeric identifier for the event.

            format: A composite format string (see Remarks) that contains text intermixed with zero or more format items, which correspond to objects in the args array.

            args: An ject array containing zero or more objects to format.
        """
        ...
    def TraceInformation(self, *__args):
        """
        TraceInformation(self: TraceSource, message: str)

            Writes an informational message to the trace listeners in the System.Diagnostics.TraceSource.Listeners collection using the specified message.

            message: The informative message to write.

        TraceInformation(self: TraceSource, format: str, *args: Array[object])

            Writes an informational message to the trace listeners in the System.Diagnostics.TraceSource.Listeners collection using the specified object array and formatting information.

            format: A composite format string (see Remarks) that contains text intermixed with zero or more format items, which correspond to objects in the args array.

            args: An array containing zero or more objects to format.
        """
        ...
    def TraceTransfer(self, id, message, relatedActivityId):
        """
        TraceTransfer(self: TraceSource, id: int, message: str, relatedActivityId: Guid)

            Writes a trace transfer message to the trace listeners in the System.Diagnostics.TraceSource.Listeners collection using the specified numeric identifier, message, and related activity identifier.

            id: A numeric identifier for the event.

            message: The trace message to write.

            relatedActivityId: A structure that identifies the related activity.
        """
        ...
    @property
    def Attributes(self):
        """
        Gets the custom switch attributes defined in the application configuration file.

        Get: Attributes(self: TraceSource) -> StringDictionary
        """
        ...
    @property
    def Listeners(self):
        """
        Gets the collection of trace listeners for the trace source.

        Get: Listeners(self: TraceSource) -> TraceListenerCollection
        """
        ...
    @property
    def Name(self):
        """
        Gets the name of the trace source.

        Get: Name(self: TraceSource) -> str
        """
        ...
    @property
    def Switch(self):
        """
        Gets or sets the source switch value.

        Get: Switch(self: TraceSource) -> SourceSwitch

        Set: Switch(self: TraceSource) = value
        """
        ...

class TraceSwitch(Switch):
    """
    Provides a multilevel switch to control tracing and debug output without recompiling your code.

    TraceSwitch(displayName: str, description: str)

    TraceSwitch(displayName: str, description: str, defaultSwitchValue: str)
    """

    @property
    def Level(self):
        """
        Gets or sets the trace level that determines the messages the switch allows.

        Get: Level(self: TraceSwitch) -> TraceLevel

        Set: Level(self: TraceSwitch) = value
        """
        ...
    @property
    def SwitchSetting(self):
        """Gets or sets the current setting for this switch."""
        ...
    @property
    def TraceError(self):
        """
        Gets a value indicating whether the switch allows error-handling messages.

        Get: TraceError(self: TraceSwitch) -> bool
        """
        ...
    @property
    def TraceInfo(self):
        """
        Gets a value indicating whether the switch allows informational messages.

        Get: TraceInfo(self: TraceSwitch) -> bool
        """
        ...
    @property
    def TraceVerbose(self):
        """
        Gets a value indicating whether the switch allows all messages.

        Get: TraceVerbose(self: TraceSwitch) -> bool
        """
        ...
    @property
    def TraceWarning(self):
        """
        Gets a value indicating whether the switch allows warning messages.

        Get: TraceWarning(self: TraceSwitch) -> bool
        """
        ...
    @property
    def Value(self):
        """Gets or sets the value of the switch."""
        ...

class XmlWriterTraceListener(TextWriterTraceListener):  # skipped bases: <type 'IDisposable'>
    """
    Directs tracing or debugging output as XML-encoded data to a System.IO.TextWriter or to a System.IO.Stream, such as a System.IO.FileStream.

    XmlWriterTraceListener(stream: Stream)

    XmlWriterTraceListener(stream: Stream, name: str)

    XmlWriterTraceListener(writer: TextWriter)

    XmlWriterTraceListener(writer: TextWriter, name: str)

    XmlWriterTraceListener(filename: str)

    XmlWriterTraceListener(filename: str, name: str)
    """

    def Fail(self, message, detailMessage=None):
        """
        Fail(self: XmlWriterTraceListener, message: str, detailMessage: str)

            Writes trace information including an error message and a detailed error message to the file or stream.

            message: The error message to write.

            detailMessage: The detailed error message to append to the error message.
        """
        ...
    def TraceData(self, eventCache, source, eventType, id, data):
        """
        TraceData(self: XmlWriterTraceListener, eventCache: TraceEventCache, source: str, eventType: TraceEventType, id: int, data: object)

            Writes trace information, a data object, and event information to the file or stream.

            eventCache: A System.Diagnostics.TraceEventCache that contains the current process ID, thread ID, and stack trace information.

            source: The source name.

            eventType: One of the System.Diagnostics.TraceEventType values.

            id: A numeric identifier for the event.

            data: A data object to emit.

        TraceData(self: XmlWriterTraceListener, eventCache: TraceEventCache, source: str, eventType: TraceEventType, id: int, *data: Array[object])

            Writes trace information, data objects, and event information to the file or stream.

            eventCache: A System.Diagnostics.TraceEventCache that contains the current process ID, thread ID, and stack trace information.

            source: The source name.

            eventType: One of the System.Diagnostics.TraceEventType values.

            id: A numeric identifier for the event.

            data: An array of data objects to emit.
        """
        ...
    def TraceEvent(self, eventCache, source, eventType, id, *__args):
        """
        TraceEvent(self: XmlWriterTraceListener, eventCache: TraceEventCache, source: str, eventType: TraceEventType, id: int, format: str, *args: Array[object])

            Writes trace information, a formatted message, and event information to the file or stream.

            eventCache: A System.Diagnostics.TraceEventCache that contains the current process ID, thread ID, and stack trace information.

            source: The source name.

            eventType: One of the System.Diagnostics.TraceEventType values.

            id: A numeric identifier for the event.

            format: A format string that contains zero or more format items that correspond to objects in the args array.

            args: An object array containing zero or more objects to format.

        TraceEvent(self: XmlWriterTraceListener, eventCache: TraceEventCache, source: str, eventType: TraceEventType, id: int, message: str)

            Writes trace information, a message, and event information to the file or stream.

            eventCache: A System.Diagnostics.TraceEventCache that contains the current process ID, thread ID, and stack trace information.

            source: The source name.

            eventType: One of the System.Diagnostics.TraceEventType values.

            id: A numeric identifier for the event.

            message: The message to write.
        """
        ...
    def TraceTransfer(self, eventCache, source, id, message, relatedActivityId):
        """
        TraceTransfer(self: XmlWriterTraceListener, eventCache: TraceEventCache, source: str, id: int, message: str, relatedActivityId: Guid)

            Writes trace information including the identity of a related activity, a message, and event information to the file or stream.

            eventCache: A System.Diagnostics.TraceEventCache that contains the current process ID, thread ID, and stack trace information.

            source: The source name.

            id: A numeric identifier for the event.

            message: A trace message to write.

            relatedActivityId: A System.Guid structure that identifies a related activity.
        """
        ...
    @property
    def NeedIndent(self):
        """Gets or sets a value indicating whether to indent the output."""
        ...

# variables with complex values
