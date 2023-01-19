# encoding: utf-8
# module Siemens.Engineering.MC.Drives calls itself Drives
# from Siemens.Engineering, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

from Siemens.Engineering import (
    IEngineeringComposition,
    IEngineeringObject,
    IEngineeringService,
    IEngineeringServiceProvider,
)
from System import IEquatable
from Siemens.Engineering.HW.Features import DeviceItemFeature

class DriveObject(
    IEngineeringObject, IInternalObjectAccess, IEngineeringServiceProvider, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IServiceProvider'>, <type 'IInternalInstanceAccess'>
    """Represents a DriveObject"""

    @property
    def Parameters(self):
        """
        Accessible parameters on this DriveObject

        Get: Parameters(self: DriveObject) -> DriveParameterComposition
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: DriveObject) -> IEngineeringObject
        """
        ...
    @property
    def Telegrams(self):
        """
        Composition of Telegrams

        Get: Telegrams(self: DriveObject) -> TelegramComposition
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: DriveObject) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: DriveObject) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class DriveObjectComposition(
    IEngineeringComposition, IInternalCompositionAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """Composition of DriveObjects"""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: DriveObjectComposition) -> IEngineeringObject
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: DriveObjectComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: DriveObjectComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[DriveObject](enumerable:  value: DriveObject) -> bool"""
        ...
    def __ne__(self, *args): ...

class DriveObjectContainer(
    DeviceItemFeature, IEngineeringService
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """Container of DriveObjects"""

    @property
    def DriveObjects(self):
        """
        Composition of DriveObjects

        Get: DriveObjects(self: DriveObjectContainer) -> DriveObjectComposition
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: DriveObjectContainer) -> IEngineeringObject
        """
        ...

class DriveParameter(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Represents a DriveParameter"""

    @property
    def ArrayIndex(self):
        """
        Index of an array parameter

        Get: ArrayIndex(self: DriveParameter) -> int
        """
        ...
    @property
    def ArrayLength(self):
        """
        Number of array elements on array parameter parents

        Get: ArrayLength(self: DriveParameter) -> int
        """
        ...
    @property
    def Bits(self):
        """
        Bits of this parameter

        Get: Bits(self: DriveParameter) -> DriveParameterComposition
        """
        ...
    @property
    def EnumValueList(self):
        """
        List of possible labels of the enum parameters

        Get: EnumValueList(self: DriveParameter) -> IDictionary[int, str]
        """
        ...
    @property
    def MaxValue(self):
        """
        Maximum value of the parameter

        Get: MaxValue(self: DriveParameter) -> object
        """
        ...
    @property
    def MinValue(self):
        """
        Minimum value of the parameter

        Get: MinValue(self: DriveParameter) -> object
        """
        ...
    @property
    def Name(self):
        """
        The name of the parameter

        Get: Name(self: DriveParameter) -> str
        """
        ...
    @property
    def Number(self):
        """
        Numeric representation of the parameter name

        Get: Number(self: DriveParameter) -> int
        """
        ...
    @property
    def ParameterText(self):
        """
        The description of the parameter

        Get: ParameterText(self: DriveParameter) -> str
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: DriveParameter) -> IEngineeringObject
        """
        ...
    @property
    def Unit(self):
        """
        The unit of the parameter

        Get: Unit(self: DriveParameter) -> str
        """
        ...
    @property
    def Value(self):
        """
        The value of the parameter

        Get: Value(self: DriveParameter) -> object

        Set: Value(self: DriveParameter) = value
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: DriveParameter) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: DriveParameter) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class DriveParameterComposition(
    IEngineeringComposition, IInternalCompositionAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """Composition of parameters"""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: DriveParameterComposition) -> IEngineeringObject
        """
        ...
    def Find(self, *__args):
        """
        Find(self: DriveParameterComposition, name: str) -> DriveParameter

            Find Parameter

            name: Name of the parameter

            Returns: Siemens.Engineering.MC.Drives.DriveParameter

        Find(self: DriveParameterComposition, number: int, arrayIndex: int) -> DriveParameter

            Find parameter by numeric values

            number: Numeric representation of the parameter name

            arrayIndex: Index of an array parameter

            Returns: Siemens.Engineering.MC.Drives.DriveParameter
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: DriveParameterComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: DriveParameterComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[DriveParameter](enumerable:  value: DriveParameter) -> bool"""
        ...
    def __ne__(self, *args): ...

class OnlineDriveObject(
    IEngineeringObject, IInternalObjectAccess, IEngineeringServiceProvider, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IServiceProvider'>, <type 'IInternalInstanceAccess'>
    """Service of the online parameters"""

    @property
    def Parameters(self):
        """
        Composition of Parameters

        Get: Parameters(self: OnlineDriveObject) -> DriveParameterComposition
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: OnlineDriveObject) -> IEngineeringObject
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: OnlineDriveObject) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: OnlineDriveObject) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class OnlineDriveObjectComposition(
    IEngineeringComposition, IInternalCompositionAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """Composition of OnlineDriveObjects"""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: OnlineDriveObjectComposition) -> IEngineeringObject
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: OnlineDriveObjectComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: OnlineDriveObjectComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[OnlineDriveObject](enumerable:  value: OnlineDriveObject) -> bool"""
        ...
    def __ne__(self, *args): ...

class OnlineDriveObjectContainer(
    IEngineeringObject, IEngineeringService, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Container of OnlineDriveObjects"""

    @property
    def OnlineDriveObjects(self):
        """
        Composition of OnlineDriveObjects

        Get: OnlineDriveObjects(self: OnlineDriveObjectContainer) -> OnlineDriveObjectComposition
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: OnlineDriveObjectContainer) -> IEngineeringObject
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: OnlineDriveObjectContainer) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: OnlineDriveObjectContainer) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class Telegram(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Represents a Telegram"""

    @property
    def Addresses(self):
        """
        Addresses of the specified Telegram

        Get: Addresses(self: Telegram) -> AddressComposition
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: Telegram) -> IEngineeringObject
        """
        ...
    @property
    def PKW(self):
        """
        PKW relevant ActualValue channel

        Get: PKW(self: Telegram) -> Telegram
        """
        ...
    @property
    def TelegramNumber(self):
        """
        Telegram identifier

        Get: TelegramNumber(self: Telegram) -> int

        Set: TelegramNumber(self: Telegram) = value
        """
        ...
    @property
    def Type(self):
        """
        The type of telegram

        Get: Type(self: Telegram) -> TelegramType
        """
        ...
    def CanChangeSize(self, direction, size, keepOriginalAddress):
        """
        CanChangeSize(self: Telegram, direction: AddressIoType, size: int, keepOriginalAddress: bool) -> bool

            Returns true if the size of proper channel of the telegram can be changed.

            direction: Actual value channel specific size

            size: Setpoint channel specific size

            keepOriginalAddress: Keeps original address if true.

            Returns: System.Boolean
        """
        ...
    def CanChangeTelegram(self, telegramNumber):
        """
        CanChangeTelegram(self: Telegram, telegramNumber: int) -> bool

            Returns true if the telegram can be changed to the given standard telegram type.

            telegramNumber: Telegram identifier

            Returns: System.Boolean
        """
        ...
    def ChangeSize(self, direction, size, keepOriginalAddress):
        """
        ChangeSize(self: Telegram, direction: AddressIoType, size: int, keepOriginalAddress: bool) -> bool

            Change size of the telegram

            direction: Actual value channel specific size

            size: Setpoint channel specific size

            keepOriginalAddress: Keeps original address if true.

            Returns: System.Boolean
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: Telegram) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def GetSize(self, direction):
        """
        GetSize(self: Telegram, direction: AddressIoType) -> int

            Returns size of the proper channel.

            direction: Direction of the channel. Can be Input or Output.

            Returns: System.Int32
        """
        ...
    def ToString(self):
        """
        ToString(self: Telegram) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class TelegramComposition(
    IEngineeringComposition, IInternalCompositionAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """Composition of telegrams: telegrams of a DriveObject"""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: TelegramComposition) -> IEngineeringObject
        """
        ...
    def CanInsertAdditionalTelegram(self, inputSize, outputSize):
        """
        CanInsertAdditionalTelegram(self: TelegramComposition, inputSize: int, outputSize: int) -> bool

            Checks if adding a new Additional telegram with the given sizes to the drive object would be possible.

            inputSize: Size of the input channel.

            outputSize: Size of the output channel.

            Returns: System.Boolean
        """
        ...
    def CanInsertSafetyTelegram(self, telegramNumber):
        """
        CanInsertSafetyTelegram(self: TelegramComposition, telegramNumber: int) -> bool

            Checks if adding a new Safety telegram with the given number to the drive object would be possible.

            telegramNumber: Number of the safety telegram

            Returns: System.Boolean
        """
        ...
    def CanInsertSupplementaryTelegram(self, telegramNumber):
        """
        CanInsertSupplementaryTelegram(self: TelegramComposition, telegramNumber: int) -> bool

            Checks if adding a new Supplementary telegram with the given number to the drive object would be possible.

            telegramNumber: Number of the supplementary telegram

            Returns: System.Boolean
        """
        ...
    def CanInsertTorqueTelegram(self, telegramNumber):
        """
        CanInsertTorqueTelegram(self: TelegramComposition, telegramNumber: int) -> bool

            Checks if adding a new Torque telegram with the given number to the drive object would be possible.

            telegramNumber: Number of the safety telegram

            Returns: System.Boolean
        """
        ...
    def EraseTelegram(self, telegramType):
        """
        EraseTelegram(self: TelegramComposition, telegramType: TelegramType)

            Removes the telegram of the given type.

            telegramType: Type of the telegram to be removed
        """
        ...
    def Find(self, type):
        """
        Find(self: TelegramComposition, type: TelegramType) -> Telegram

            Finds telegram by type

            type: Telegram type

            Returns: Siemens.Engineering.MC.Drives.Telegram
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: TelegramComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def InsertAdditionalTelegram(self, inputSize, outputSize):
        """
        InsertAdditionalTelegram(self: TelegramComposition, inputSize: int, outputSize: int)

            Adds a new Additional telegram with the given sizes to the drive object.

            inputSize: Size of the input channel.

            outputSize: Size of the output channel.
        """
        ...
    def InsertSafetyTelegram(self, telegramNumber):
        """
        InsertSafetyTelegram(self: TelegramComposition, telegramNumber: int)

            Adds a new Safety telegram with the given number to the drive object.

            telegramNumber: Number of the safety telegram
        """
        ...
    def InsertSupplementaryTelegram(self, telegramNumber):
        """
        InsertSupplementaryTelegram(self: TelegramComposition, telegramNumber: int)

            Adds a new Supplementary telegram with the given number to the drive object.

            telegramNumber: Number of the supplementary telegram
        """
        ...
    def InsertTorqueTelegram(self, telegramNumber):
        """
        InsertTorqueTelegram(self: TelegramComposition, telegramNumber: int)

            Adds a new Torque telegram with the given number to the drive object.

            telegramNumber: Number of the safety telegram
        """
        ...
    def ToString(self):
        """
        ToString(self: TelegramComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[Telegram](enumerable:  value: Telegram) -> bool"""
        ...
    def __ne__(self, *args): ...

# variables with complex values
