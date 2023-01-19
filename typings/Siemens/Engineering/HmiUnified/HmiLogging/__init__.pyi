# encoding: utf-8
# module Siemens.Engineering.HmiUnified.HmiLogging calls itself HmiLogging
# from Siemens.Engineering, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

from Siemens.Engineering import IEngineeringComposition
from Siemens.Engineering.HmiUnified.HmiLogging.HmiLoggingCommon import LoggingBase
from System import IEquatable

class HmiAlarmLog(
    LoggingBase
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IValidator'>, <type 'IInternalObjectAccess'>
    """Alarm logging"""

    @property
    def Name(self):
        """
        Name

        Get: Name(self: HmiAlarmLog) -> str

        Set: Name(self: HmiAlarmLog) = value
        """
        ...
    def Delete(self):
        """
        Delete(self: HmiAlarmLog)

            Deletes this instance.
        """
        ...

class HmiAlarmLogComposition(
    IEngineeringComposition, IInternalCompositionAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """Alarm log collection"""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: HmiAlarmLogComposition) -> IEngineeringObject
        """
        ...
    def Find(self, name):
        """
        Find(self: HmiAlarmLogComposition, name: str) -> HmiAlarmLog

            Find method of alarmlog

            name: Name

            Returns: Siemens.Engineering.HmiUnified.HmiLogging.HmiAlarmLog
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: HmiAlarmLogComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: HmiAlarmLogComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[HmiAlarmLog](enumerable:  value: HmiAlarmLog) -> bool"""
        ...
    def __ne__(self, *args): ...

class HmiDataLog(
    LoggingBase
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IValidator'>, <type 'IInternalObjectAccess'>
    """Data log configuration"""

    @property
    def Name(self):
        """
        Name

        Get: Name(self: HmiDataLog) -> str

        Set: Name(self: HmiDataLog) = value
        """
        ...
    def Delete(self):
        """
        Delete(self: HmiDataLog)

            Deletes this instance.
        """
        ...

class HmiDataLogComposition(
    IEngineeringComposition, IInternalCompositionAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """Data log collection"""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: HmiDataLogComposition) -> IEngineeringObject
        """
        ...
    def Find(self, name):
        """
        Find(self: HmiDataLogComposition, name: str) -> HmiDataLog

            Find method of HmiDataLog

            name: Name

            Returns: Siemens.Engineering.HmiUnified.HmiLogging.HmiDataLog
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: HmiDataLogComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: HmiDataLogComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[HmiDataLog](enumerable:  value: HmiDataLog) -> bool"""
        ...
    def __ne__(self, *args): ...

# variables with complex values
