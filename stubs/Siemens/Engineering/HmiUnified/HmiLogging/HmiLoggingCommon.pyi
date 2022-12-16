# encoding: utf-8
# module Siemens.Engineering.HmiUnified.HmiLogging.HmiLoggingCommon calls itself HmiLoggingCommon
# from Siemens.Engineering, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

from Siemens.Engineering import IEngineeringObject
from Siemens.Engineering.HmiUnified.Common import HmiBase
from System import Enum, IEquatable

class HmiBackupMode(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    HmiBackupMode

    enum HmiBackupMode, values: NoBackup (0), PrimaryPath (1)
    """

    NoBackup = None
    PrimaryPath = None
    value__ = None

class LogBackup(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Logging backup configuration"""

    @property
    def BackupMode(self):
        """
        Defines the backup mode

        Get: BackupMode(self: LogBackup) -> HmiBackupMode

        Set: BackupMode(self: LogBackup) = value
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: LogBackup) -> IEngineeringObject
        """
        ...
    @property
    def PrimaryPath(self):
        """
        Logging backup path

        Get: PrimaryPath(self: LogBackup) -> str

        Set: PrimaryPath(self: LogBackup) = value
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: LogBackup) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: LogBackup) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class LogDuration(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Specifies the time period type"""

    @property
    def Days(self):
        """
        Specifies number of days

        Get: Days(self: LogDuration) -> UInt32

        Set: Days(self: LogDuration) = value
        """
        ...
    @property
    def Hours(self):
        """
        Specifies number of hours

        Get: Hours(self: LogDuration) -> UInt32

        Set: Hours(self: LogDuration) = value
        """
        ...
    @property
    def Minutes(self):
        """
        Specifies minutes

        Get: Minutes(self: LogDuration) -> UInt32

        Set: Minutes(self: LogDuration) = value
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: LogDuration) -> IEngineeringObject
        """
        ...
    @property
    def Seconds(self):
        """
        Specifies seconds

        Get: Seconds(self: LogDuration) -> UInt32

        Set: Seconds(self: LogDuration) = value
        """
        ...
    @property
    def Ticks(self):
        """
        Hundred Nonoseconds

        Get: Ticks(self: LogDuration) -> UInt32

        Set: Ticks(self: LogDuration) = value
        """
        ...
    def GetDoubleLogDuration(self):
        """
        GetDoubleLogDuration(self: LogDuration) -> float

            Return timeperiod in double

            Returns: System.Double
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: LogDuration) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def GetStringLogDuration(self):
        """
        GetStringLogDuration(self: LogDuration) -> str

            Return Log Duration in String

            Returns: System.String
        """
        ...
    def SetLogDuration(self, days, hours, minutes, seconds, ticks):
        """
        SetLogDuration(self: LogDuration, days: UInt32, hours: UInt32, minutes: UInt32, seconds: UInt32, ticks: UInt32) -> str

            Set timeperiod in double

            days: Day

            hours: hours

            minutes: minutes

            seconds: seconds

            ticks: hundred nanoseconds

            Returns: System.String
        """
        ...
    def ToString(self):
        """
        ToString(self: LogDuration) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class LoggingBase(
    HmiBase
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IValidator'>, <type 'IInternalObjectAccess'>
    """Base class for Alarm and Data logging"""

    @property
    def Backup(self):
        """
        Log backup

        Get: Backup(self: LoggingBase) -> LogBackup
        """
        ...
    @property
    def Segment(self):
        """
        Log segment for backup

        Get: Segment(self: LoggingBase) -> LogSegment
        """
        ...
    @property
    def Settings(self):
        """
        Logging settings

        Get: Settings(self: LoggingBase) -> LogSettings
        """
        ...

class LogSegment(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Logging segment configuration"""

    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: LogSegment) -> IEngineeringObject
        """
        ...
    @property
    def SegmentMaxSize(self):
        """
        Defines the maximum size of a segment of the log on the storage medium in units of megabytes. When the value is set to 0, the size of the segment is not considered.

        Get: SegmentMaxSize(self: LogSegment) -> UInt32

        Set: SegmentMaxSize(self: LogSegment) = value
        """
        ...
    @property
    def SegmentStartTime(self):
        """
        Start time of the logging segment

        Get: SegmentStartTime(self: LogSegment) -> DateTime

        Set: SegmentStartTime(self: LogSegment) = value
        """
        ...
    @property
    def SegmentTimePeriod(self):
        """
        Segment Time Period

        Get: SegmentTimePeriod(self: LogSegment) -> SegmentDuration
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: LogSegment) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: LogSegment) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class LogSettings(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Logging configuration"""

    @property
    def LogMaxSize(self):
        """
        Maximum size of data storage in MB

        Get: LogMaxSize(self: LogSettings) -> UInt32

        Set: LogMaxSize(self: LogSettings) = value
        """
        ...
    @property
    def LogTimePeriod(self):
        """
        Log Time period

        Get: LogTimePeriod(self: LogSettings) -> LogDuration
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: LogSettings) -> IEngineeringObject
        """
        ...
    @property
    def StoragePath(self):
        """
        Path for storage

        Get: StoragePath(self: LogSettings) -> str

        Set: StoragePath(self: LogSettings) = value
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: LogSettings) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: LogSettings) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class SegmentDuration(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Segment duration Class"""

    @property
    def Days(self):
        """
        Days

        Get: Days(self: SegmentDuration) -> UInt32

        Set: Days(self: SegmentDuration) = value
        """
        ...
    @property
    def Hours(self):
        """
        Hours

        Get: Hours(self: SegmentDuration) -> UInt32

        Set: Hours(self: SegmentDuration) = value
        """
        ...
    @property
    def Minutes(self):
        """
        Minutes

        Get: Minutes(self: SegmentDuration) -> UInt32

        Set: Minutes(self: SegmentDuration) = value
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: SegmentDuration) -> IEngineeringObject
        """
        ...
    @property
    def Seconds(self):
        """
        Seconds

        Get: Seconds(self: SegmentDuration) -> UInt32

        Set: Seconds(self: SegmentDuration) = value
        """
        ...
    @property
    def Ticks(self):
        """
        Hundred Nanoseconds

        Get: Ticks(self: SegmentDuration) -> UInt32

        Set: Ticks(self: SegmentDuration) = value
        """
        ...
    def GetDoubleSegmentDuration(self):
        """
        GetDoubleSegmentDuration(self: SegmentDuration) -> float

            Method for getting segment timeperiod

            Returns: System.Double
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: SegmentDuration) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def GetStringSegmentDuration(self):
        """
        GetStringSegmentDuration(self: SegmentDuration) -> str

            Return Segment Duration in String

            Returns: System.String
        """
        ...
    def SetSegmentDuration(self, days, hours, minutes, seconds, ticks):
        """
        SetSegmentDuration(self: SegmentDuration, days: UInt32, hours: UInt32, minutes: UInt32, seconds: UInt32, ticks: UInt32) -> str

            Method for setting segment timeperiod

            days: days

            hours: hours

            minutes: minutes

            seconds: seconds

            ticks: Hundred Nanoseconds

            Returns: System.String
        """
        ...
    def ToString(self):
        """
        ToString(self: SegmentDuration) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...
