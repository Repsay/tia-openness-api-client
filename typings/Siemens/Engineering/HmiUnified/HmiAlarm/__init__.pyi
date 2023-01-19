# encoding: utf-8
# module Siemens.Engineering.HmiUnified.HmiAlarm calls itself HmiAlarm
# from Siemens.Engineering, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

from Siemens.Engineering import IEngineeringComposition
from Siemens.Engineering.HmiUnified.Common import HmiBase
from Siemens.Engineering.HmiUnified.HmiAlarm.HmiAlarmCommon import AlarmBase
from System import IEquatable

class HmiAlarmClass(
    HmiBase
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IValidator'>, <type 'IInternalObjectAccess'>
    """Specifies alarm class."""

    @property
    def AcknowledgedClearedState(self):
        """
        Specifies Alarm incoming outgoing acknowledge or AcknowledgedCleared status

        Get: AcknowledgedClearedState(self: HmiAlarmClass) -> HmiAcknowledgedClearedState
        """
        ...
    @property
    def AcknowledgedState(self):
        """
        Specifies Alarm incoming acknowledge or acknowledged status

        Get: AcknowledgedState(self: HmiAlarmClass) -> HmiAcknowledgedState
        """
        ...
    @property
    def ClearedState(self):
        """
        Specifies Alarm coming going or cleared status

        Get: ClearedState(self: HmiAlarmClass) -> HmiClearedState
        """
        ...
    @property
    def Id(self):
        """
        Specifies the alarm class number that identifies the alarm class in runtime

        Get: Id(self: HmiAlarmClass) -> UInt32
        """
        ...
    @property
    def IsSystem(self):
        """
        Specifies if alarm class is system provided

        Get: IsSystem(self: HmiAlarmClass) -> bool
        """
        ...
    @property
    def Priority(self):
        """
        Specifies the alarm priority

        Get: Priority(self: HmiAlarmClass) -> Byte

        Set: Priority(self: HmiAlarmClass) = value
        """
        ...
    @property
    def RaisedState(self):
        """
        Alarm incoming or raised status

        Get: RaisedState(self: HmiAlarmClass) -> HmiRaisedState
        """
        ...
    @property
    def StateMachine(self):
        """
        Defines the statemachine of the alarm class

        Get: StateMachine(self: HmiAlarmClass) -> HmiAlarmStateMachine

        Set: StateMachine(self: HmiAlarmClass) = value
        """
        ...
    def Delete(self):
        """
        Delete(self: HmiAlarmClass)

            Deletes this instance.
        """
        ...

class HmiAlarmClassComposition(
    IEngineeringComposition, IInternalCompositionAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """HmiAlarmClassComposition"""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: HmiAlarmClassComposition) -> IEngineeringObject
        """
        ...
    def Find(self, name):
        """
        Find(self: HmiAlarmClassComposition, name: str) -> HmiAlarmClass

            Find

            name: Name

            Returns: Siemens.Engineering.HmiUnified.HmiAlarm.HmiAlarmClass
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: HmiAlarmClassComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: HmiAlarmClassComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[HmiAlarmClass](enumerable:  value: HmiAlarmClass) -> bool"""
        ...
    def __ne__(self, *args): ...

class HmiAnalogAlarm(
    AlarmBase
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IValidator'>, <type 'IInternalObjectAccess'>
    """HmiAnalogAlarm"""

    @property
    def Condition(self):
        """
        Specifies Limit Mode.

        Get: Condition(self: HmiAnalogAlarm) -> HmiAlarmCondition

        Set: Condition(self: HmiAnalogAlarm) = value
        """
        ...
    @property
    def ConditionValue(self):
        """
        Condition Value can be specified as constant value.

        Get: ConditionValue(self: HmiAnalogAlarm) -> object

        Set: ConditionValue(self: HmiAnalogAlarm) = value
        """
        ...
    @property
    def Name(self):
        """
        Name

        Get: Name(self: HmiAnalogAlarm) -> str

        Set: Name(self: HmiAnalogAlarm) = value
        """
        ...
    def Delete(self):
        """
        Delete(self: HmiAnalogAlarm)

            Deletes this instance.
        """
        ...

class HmiAnalogAlarmComposition(
    IEngineeringComposition, IInternalCompositionAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """HmiAnalogAlarm Composition"""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: HmiAnalogAlarmComposition) -> IEngineeringObject
        """
        ...
    def Find(self, name):
        """
        Find(self: HmiAnalogAlarmComposition, name: str) -> HmiAnalogAlarm

            Find

            name: Name

            Returns: Siemens.Engineering.HmiUnified.HmiAlarm.HmiAnalogAlarm
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: HmiAnalogAlarmComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: HmiAnalogAlarmComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[HmiAnalogAlarm](enumerable:  value: HmiAnalogAlarm) -> bool"""
        ...
    def __ne__(self, *args): ...

class HmiDiscreteAlarm(
    AlarmBase
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IValidator'>, <type 'IInternalObjectAccess'>
    """HmiDiscreteAlarm"""

    @property
    def Name(self):
        """
        Name

        Get: Name(self: HmiDiscreteAlarm) -> str

        Set: Name(self: HmiDiscreteAlarm) = value
        """
        ...
    @property
    def RaisedStateTagBitNumber(self):
        """
        Trigger bit on the trigger tag

        Get: RaisedStateTagBitNumber(self: HmiDiscreteAlarm) -> UInt32

        Set: RaisedStateTagBitNumber(self: HmiDiscreteAlarm) = value
        """
        ...
    @property
    def TriggerMode(self):
        """
        Specify trigger mode for discrete alarm

        Get: TriggerMode(self: HmiDiscreteAlarm) -> HmiDiscreteAlarmTriggerMode

        Set: TriggerMode(self: HmiDiscreteAlarm) = value
        """
        ...
    def Delete(self):
        """
        Delete(self: HmiDiscreteAlarm)

            Deletes this instance.
        """
        ...

class HmiDiscreteAlarmComposition(
    IEngineeringComposition, IInternalCompositionAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """HmiDiscreteAlarmComposition"""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: HmiDiscreteAlarmComposition) -> IEngineeringObject
        """
        ...
    def Find(self, name):
        """
        Find(self: HmiDiscreteAlarmComposition, name: str) -> HmiDiscreteAlarm

            Find

            name: Name

            Returns: Siemens.Engineering.HmiUnified.HmiAlarm.HmiDiscreteAlarm
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: HmiDiscreteAlarmComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: HmiDiscreteAlarmComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[HmiDiscreteAlarm](enumerable:  value: HmiDiscreteAlarm) -> bool"""
        ...
    def __ne__(self, *args): ...

# variables with complex values
