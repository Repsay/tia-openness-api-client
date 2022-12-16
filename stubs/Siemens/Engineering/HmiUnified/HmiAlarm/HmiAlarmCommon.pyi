# encoding: utf-8
# module Siemens.Engineering.HmiUnified.HmiAlarm.HmiAlarmCommon calls itself HmiAlarmCommon
# from Siemens.Engineering, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

from Siemens.Engineering import IEngineeringObject
from Siemens.Engineering.HmiUnified.Common import HmiBase
from System import Enum, IEquatable

class AlarmBase(
    HmiBase
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IValidator'>, <type 'IInternalObjectAccess'>
    """This is base class for AnalogAlarm and DiscreteAlarm"""

    @property
    def AlarmClass(self):
        """
        Specifies the alarm class

        Get: AlarmClass(self: AlarmBase) -> str

        Set: AlarmClass(self: AlarmBase) = value
        """
        ...
    @property
    def AlarmParameterTags(self):
        """
        Specifies the alarm pararmeters

        Get: AlarmParameterTags(self: AlarmBase) -> object

        Set: AlarmParameterTags(self: AlarmBase) = value
        """
        ...
    @property
    def Area(self):
        """
        Specifies the area of the alarm

        Get: Area(self: AlarmBase) -> str

        Set: Area(self: AlarmBase) = value
        """
        ...
    @property
    def EventText(self):
        """
        Specifies event/alarm text of alarm.

        Get: EventText(self: AlarmBase) -> MultilingualText
        """
        ...
    @property
    def Id(self):
        """
        Alarm row identification Number

        Get: Id(self: AlarmBase) -> UInt32

        Set: Id(self: AlarmBase) = value
        """
        ...
    @property
    def InfoText(self):
        """
        Specifies the multilingual InfoText of the alarm

        Get: InfoText(self: AlarmBase) -> MultilingualText
        """
        ...
    @property
    def Origin(self):
        """
        Specifies the origin of the alarm

        Get: Origin(self: AlarmBase) -> str

        Set: Origin(self: AlarmBase) = value
        """
        ...
    @property
    def Priority(self):
        """
        Specifies the alarm priority

        Get: Priority(self: AlarmBase) -> Byte

        Set: Priority(self: AlarmBase) = value
        """
        ...
    @property
    def RaisedStateTag(self):
        """
        Specifies the tag that raise/trigger the alarm

        Get: RaisedStateTag(self: AlarmBase) -> str

        Set: RaisedStateTag(self: AlarmBase) = value
        """
        ...

class AlarmStatusVisuals(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Specifies the alarm status visuals"""

    @property
    def BackColor(self):
        """
        Specifies the background color

        Get: BackColor(self: AlarmStatusVisuals) -> Color

        Set: BackColor(self: AlarmStatusVisuals) = value
        """
        ...
    @property
    def Flashing(self):
        """
        Specifies the flashing color

        Get: Flashing(self: AlarmStatusVisuals) -> bool

        Set: Flashing(self: AlarmStatusVisuals) = value
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: AlarmStatusVisuals) -> IEngineeringObject
        """
        ...
    @property
    def TextColor(self):
        """
        Specifies the text color

        Get: TextColor(self: AlarmStatusVisuals) -> Color

        Set: TextColor(self: AlarmStatusVisuals) = value
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: AlarmStatusVisuals) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: AlarmStatusVisuals) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class HmiAcknowledgedClearedState(
    AlarmStatusVisuals
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """HmiAcknowledgedClearedState"""

    pass

class HmiAcknowledgedState(
    AlarmStatusVisuals
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """HmiAcknowledgedState"""

    pass

class HmiAlarmCondition(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    HmiAlarmCondition

    enum HmiAlarmCondition, values: Equal (2), LowerLimit (0), LowerLimitOrEqual (4), NotEqual (3), UpperLimit (1), UpperLimitOrEqual (5)
    """

    Equal = None
    LowerLimit = None
    LowerLimitOrEqual = None
    NotEqual = None
    UpperLimit = None
    UpperLimitOrEqual = None
    value__ = None

class HmiAlarmStateMachine(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    HmiAlarmStateMachine

    enum HmiAlarmStateMachine, values: Raise (0), RaiseClear (3), RaiseClearOptionalAcknowledgement (6), RaiseClearRequiresAcknowledgement (7), RaiseClearRequiresAcknowledgementAndReset (15), RaiseRequiresAcknowledgement (5)
    """

    Raise = None
    RaiseClear = None
    RaiseClearOptionalAcknowledgement = None
    RaiseClearRequiresAcknowledgement = None
    RaiseClearRequiresAcknowledgementAndReset = None
    RaiseRequiresAcknowledgement = None
    value__ = None

class HmiClearedState(
    AlarmStatusVisuals
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """HmiClearedState"""

    pass

class HmiDiscreteAlarmTriggerMode(
    Enum
):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    HmiDiscreteAlarmTriggerMode

    enum HmiDiscreteAlarmTriggerMode, values: OnFallingEdge (1), OnRisingEdge (0)
    """

    OnFallingEdge = None
    OnRisingEdge = None
    value__ = None

class HmiRaisedState(
    AlarmStatusVisuals
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """HmiRaisedState"""

    pass
