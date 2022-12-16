# encoding: utf-8
# module System.Timers calls itself Timers
# from System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class ElapsedEventArgs(EventArgs):
    """Provides data for the System.Timers.Timer.Elapsed event."""

    @property
    def SignalTime(self):
        """
        Gets the date/time when the System.Timers.Timer.Elapsed event was raised.

        Get: SignalTime(self: ElapsedEventArgs) -> DateTime
        """
        ...

class ElapsedEventHandler(MulticastDelegate):  # skipped bases: <type 'ICloneable'>, <type 'ISerializable'>
    """
    Represents the method that will handle the System.Timers.Timer.Elapsed event of a System.Timers.Timer.

    ElapsedEventHandler(object: object, method: IntPtr)
    """

    def BeginInvoke(self, sender, e, callback, object):
        """BeginInvoke(self: ElapsedEventHandler, sender: object, e: ElapsedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult"""
        ...
    def EndInvoke(self, result):
        """EndInvoke(self: ElapsedEventHandler, result: IAsyncResult)"""
        ...
    def Invoke(self, sender, e):
        """Invoke(self: ElapsedEventHandler, sender: object, e: ElapsedEventArgs)"""
        ...

class Timer(Component, ISupportInitialize):  # skipped bases: <type 'IComponent'>, <type 'IDisposable'>
    """
    Generates an event after a set interval, with an option to generate recurring events.To browse the .NET Framework source code for this type, see the Reference Source.

    Timer()

    Timer(interval: float)
    """

    def Close(self):
        """
        Close(self: Timer)

            Releases the resources used by the System.Timers.Timer.
        """
        ...
    def Start(self):
        """
        Start(self: Timer)

            Starts raising the System.Timers.Timer.Elapsed event by setting System.Timers.Timer.Enabled to ue.
        """
        ...
    def Stop(self):
        """
        Stop(self: Timer)

            Stops raising the System.Timers.Timer.Elapsed event by setting System.Timers.Timer.Enabled to lse.
        """
        ...
    @staticmethod  # known case of __new__
    def __new__(cls, interval=None):
        """
        __new__(cls: type)

        __new__(cls: type, interval: float)
        """
        ...
    @property
    def AutoReset(self):
        """
        Gets or sets a Boolean indicating whether the System.Timers.Timer should raise the System.Timers.Timer.Elapsed event only once (lse) or repeatedly (ue).

        Get: AutoReset(self: Timer) -> bool

        Set: AutoReset(self: Timer) = value
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
    def Enabled(self):
        """
        Gets or sets a value indicating whether the System.Timers.Timer should raise the System.Timers.Timer.Elapsed event.

        Get: Enabled(self: Timer) -> bool

        Set: Enabled(self: Timer) = value
        """
        ...
    @property
    def Events(self):
        """Gets the list of event handlers that are attached to this System.ComponentModel.Component."""
        ...
    @property
    def Interval(self):
        """
        Gets or sets the interval, expressed in milliseconds, at which to raise the System.Timers.Timer.Elapsed event.

        Get: Interval(self: Timer) -> float

        Set: Interval(self: Timer) = value
        """
        ...
    @property
    def Site(self):
        """
        Gets or sets the site that binds the System.Timers.Timer to its container in design mode.

        Get: Site(self: Timer) -> ISite

        Set: Site(self: Timer) = value
        """
        ...
    @property
    def SynchronizingObject(self):
        """
        Gets or sets the object used to marshal event-handler calls that are issued when an interval has elapsed.

        Get: SynchronizingObject(self: Timer) -> ISynchronizeInvoke

        Set: SynchronizingObject(self: Timer) = value
        """
        ...
    Elapsed = None

class TimersDescriptionAttribute(DescriptionAttribute):  # skipped bases: <type '_Attribute'>
    """
    Sets the description that visual designers can display when referencing an event, extender, or property.

    TimersDescriptionAttribute(description: str)
    """

    @property
    def Description(self):
        """
        Gets the description that visual designers can display when referencing an event, extender, or property.

        Get: Description(self: TimersDescriptionAttribute) -> str
        """
        ...
    @property
    def DescriptionValue(self):
        """Gets or sets the string stored as the description."""
        ...
