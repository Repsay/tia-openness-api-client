# encoding: utf-8
# module Siemens.Engineering.HmiUnified.LoggingTags calls itself LoggingTags
# from Siemens.Engineering, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

from Siemens.Engineering import IEngineeringComposition, IEngineeringObject
from Siemens.Engineering.HmiUnified.Common import IValidator
from System import Enum, IEquatable

class HmiLimitScope(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Defines the limit scope for the logging tag

    enum HmiLimitScope, values: Greater (1), GreaterOrEqual (3), Less (2), LessOrEqual (4), NoLimitsUsed (0), OutsideLimits (7), OutsideOrEqualLimits (8), WithinLimits (5), WithinOrEqualLimits (6)
    """

    Greater = None
    GreaterOrEqual = None
    Less = None
    LessOrEqual = None
    NoLimitsUsed = None
    OutsideLimits = None
    OutsideOrEqualLimits = None
    value__ = None
    WithinLimits = None
    WithinOrEqualLimits = None

class HmiLoggingMode(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Hmi Logging mode enum

    enum HmiLoggingMode, values: Cyclic (1), OnChange (3), OnDemand (2), Undefined (0)
    """

    Cyclic = None
    OnChange = None
    OnDemand = None
    Undefined = None
    value__ = None

class HmiLoggingTag(
    IValidator, IEngineeringObject, IInternalObjectAccess, IEquatable # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Represents the LoggingTag"""

    @property
    def HighLimit(self):
        """
        Defines the Higher limit

        Get: HighLimit(self: HmiLoggingTag) -> object

        Set: HighLimit(self: HmiLoggingTag) = value
        """
        ...
    @property
    def LimitScope(self):
        """
        LimitScope of Hmi Logging Tag

        Get: LimitScope(self: HmiLoggingTag) -> HmiLimitScope

        Set: LimitScope(self: HmiLoggingTag) = value
        """
        ...
    @property
    def LogConfiguration(self):
        """
        Reference to the used data log configuration

        Get: LogConfiguration(self: HmiLoggingTag) -> str

        Set: LogConfiguration(self: HmiLoggingTag) = value
        """
        ...
    @property
    def LoggingMode(self):
        """
        Logging Mode

        Get: LoggingMode(self: HmiLoggingTag) -> HmiLoggingMode
        """
        ...
    @property
    def LowLimit(self):
        """
        Defines the Lower limit

        Get: LowLimit(self: HmiLoggingTag) -> object

        Set: LowLimit(self: HmiLoggingTag) = value
        """
        ...
    @property
    def Name(self):
        """
        Name of the Logging Tag

        Get: Name(self: HmiLoggingTag) -> str

        Set: Name(self: HmiLoggingTag) = value
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: HmiLoggingTag) -> IEngineeringObject
        """
        ...
    @property
    def SmoothingDeltaValue(self):
        """
        Smoothing delta value

        Get: SmoothingDeltaValue(self: HmiLoggingTag) -> float

        Set: SmoothingDeltaValue(self: HmiLoggingTag) = value
        """
        ...
    @property
    def SmoothingMaxTime(self):
        """
        Smoothing max time

        Get: SmoothingMaxTime(self: HmiLoggingTag) -> TimeSpan

        Set: SmoothingMaxTime(self: HmiLoggingTag) = value
        """
        ...
    @property
    def SmoothingMinTime(self):
        """
        Smoothing min time

        Get: SmoothingMinTime(self: HmiLoggingTag) -> TimeSpan

        Set: SmoothingMinTime(self: HmiLoggingTag) = value
        """
        ...
    @property
    def SmoothingMode(self):
        """
        Smoothing mode of the logging tag

        Get: SmoothingMode(self: HmiLoggingTag) -> HmiSmoothingMode

        Set: SmoothingMode(self: HmiLoggingTag) = value
        """
        ...
    def Delete(self):
        """
        Delete(self: HmiLoggingTag)

            Deletes this instance.
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: HmiLoggingTag) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: HmiLoggingTag) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class HmiLoggingTagComposition(
    IEngineeringComposition, IInternalCompositionAccess, IEquatable # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """Represensts Logging Tag Composition"""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: HmiLoggingTagComposition) -> IEngineeringObject
        """
        ...
    def Find(self, name):
        """
        Find(self: HmiLoggingTagComposition, name: str) -> HmiLoggingTag

            Find method for Logging Tag

            name: Name of the Logging Tag

            Returns: Siemens.Engineering.HmiUnified.LoggingTags.HmiLoggingTag
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: HmiLoggingTagComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: HmiLoggingTagComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[HmiLoggingTag](enumerable:  value: HmiLoggingTag) -> bool"""
        ...
    def __ne__(self, *args): ...

class HmiSmoothingMode(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Hmi Smoothing Mode

    enum HmiSmoothingMode, values: NoSmoothing (0), SwingingDoor (11), Value (1), ValueRelative (8)
    """

    NoSmoothing = None
    SwingingDoor = None
    Value = None
    ValueRelative = None
    value__ = None
