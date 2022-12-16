# encoding: utf-8
# module Siemens.Engineering.MC.Drives.DFI calls itself DFI
# from Siemens.Engineering, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

from Siemens.Engineering import IEngineeringComposition, IEngineeringObject, IEngineeringService
from System import IEquatable

class ConfigurationEntry(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """It stores data about parameter"""

    @property
    def Description(self):
        """
        The description of the configuration entry

        Get: Description(self: ConfigurationEntry) -> str
        """
        ...
    @property
    def EnumValueList(self):
        """
        List of possible labels of the enum parameters

        Get: EnumValueList(self: ConfigurationEntry) -> IDictionary[int, str]
        """
        ...
    @property
    def MaxValue(self):
        """
        Maximum value of the configuration entry

        Get: MaxValue(self: ConfigurationEntry) -> object
        """
        ...
    @property
    def MinValue(self):
        """
        Minimum value of the configuration entry

        Get: MinValue(self: ConfigurationEntry) -> object
        """
        ...
    @property
    def Name(self):
        """
        The name of the configuration entry

        Get: Name(self: ConfigurationEntry) -> str
        """
        ...
    @property
    def Number(self):
        """
        Numeric representation of the configuration entry name

        Get: Number(self: ConfigurationEntry) -> UInt32
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: ConfigurationEntry) -> IEngineeringObject
        """
        ...
    @property
    def Unit(self):
        """
        The unit of the configuration entry

        Get: Unit(self: ConfigurationEntry) -> str
        """
        ...
    @property
    def Value(self):
        """
        The value of the configuration entry

        Get: Value(self: ConfigurationEntry) -> object

        Set: Value(self: ConfigurationEntry) = value
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: ConfigurationEntry) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: ConfigurationEntry) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class ConfigurationEntryComposition(
    IEngineeringComposition, IInternalCompositionAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """Composition of configuration entries"""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: ConfigurationEntryComposition) -> IEngineeringObject
        """
        ...
    def Find(self, *__args):
        """
        Find(self: ConfigurationEntryComposition, name: str) -> ConfigurationEntry

            Find configuration entry by name

            name: Name of the configuration entry

            Returns: Siemens.Engineering.MC.Drives.DFI.ConfigurationEntry

        Find(self: ConfigurationEntryComposition, number: UInt32) -> ConfigurationEntry

            Find a configuration entry by numeric values

            number: Numeric representation of the configuration entry name

            Returns: Siemens.Engineering.MC.Drives.DFI.ConfigurationEntry
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: ConfigurationEntryComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: ConfigurationEntryComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[ConfigurationEntry](enumerable:  value: ConfigurationEntry) -> bool"""
        ...
    def __ne__(self, *args): ...

class DriveDomainFunctions(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """This class is responsible to execute domain functions on the Drive"""

    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: DriveDomainFunctions) -> IEngineeringObject
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: DriveDomainFunctions) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def PerformFactoryReset(self, resetMode):
        """
        PerformFactoryReset(self: DriveDomainFunctions, resetMode: ResetMode) -> bool

            Perform a factory reset

            resetMode: Reset mode (normal or safety)

            Returns: System.Boolean
        """
        ...
    def PerformRAMtoROMCopyAllDriveObject(self):
        """
        PerformRAMtoROMCopyAllDriveObject(self: DriveDomainFunctions) -> bool

            Perform a RAM to ROM copy in all DriveObject

            Returns: System.Boolean
        """
        ...
    def ToString(self):
        """
        ToString(self: DriveDomainFunctions) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class DriveFunctionInterface(
    IEngineeringObject, IEngineeringService, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """An interface for calling drive functions"""

    @property
    def DriveObjectFunctions(self):
        """
        Gets the DriveObjectFunctions object

        Get: DriveObjectFunctions(self: DriveFunctionInterface) -> DriveObjectFunctions
        """
        ...
    @property
    def HardwareProjection(self):
        """
        Gets the HardwareProjection object

        Get: HardwareProjection(self: DriveFunctionInterface) -> HardwareProjection
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: DriveFunctionInterface) -> IEngineeringObject
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: DriveFunctionInterface) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: DriveFunctionInterface) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class DriveObjectActivation(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """This class is responsible for activating and deactivating the DriveObject"""

    @property
    def ActivationState(self):
        """
        Gets the state of the activation

        Get: ActivationState(self: DriveObjectActivation) -> DriveObjectActivationState
        """
        ...
    @property
    def IsActive(self):
        """
        Returns true if the DriveObject is active

        Get: IsActive(self: DriveObjectActivation) -> bool
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: DriveObjectActivation) -> IEngineeringObject
        """
        ...
    def ChangeActivationState(self, activationState):
        """
        ChangeActivationState(self: DriveObjectActivation, activationState: DriveObjectActivationState) -> bool

            Changes the activation state of the DriveObject

            activationState: Requested activation state

            Returns: System.Boolean
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: DriveObjectActivation) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: DriveObjectActivation) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class DriveObjectFunctions(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Interface for calling drive object functions"""

    @property
    def DriveObjectActivation(self):
        """
        Gets the DriveObjectActivation object

        Get: DriveObjectActivation(self: DriveObjectFunctions) -> DriveObjectActivation
        """
        ...
    @property
    def DriveObjectTypeHandler(self):
        """
        Gets the DriveObjectTypeHandler object

        Get: DriveObjectTypeHandler(self: DriveObjectFunctions) -> DriveObjectTypeHandler
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: DriveObjectFunctions) -> IEngineeringObject
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: DriveObjectFunctions) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: DriveObjectFunctions) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class DriveObjectType(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """It stores data about DriveObjectType"""

    @property
    def Name(self):
        """
        The name of the DriveObjectType

        Get: Name(self: DriveObjectType) -> str
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: DriveObjectType) -> IEngineeringObject
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: DriveObjectType) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: DriveObjectType) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class DriveObjectTypeComposition(
    IEngineeringComposition, IInternalCompositionAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """Composition of DriveObjectTypes"""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: DriveObjectTypeComposition) -> IEngineeringObject
        """
        ...
    def Find(self, name):
        """
        Find(self: DriveObjectTypeComposition, name: str) -> DriveObjectType

            Find DriveObjectType by name

            name: Name of the DriveObjectType

            Returns: Siemens.Engineering.MC.Drives.DFI.DriveObjectType
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: DriveObjectTypeComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: DriveObjectTypeComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[DriveObjectType](enumerable:  value: DriveObjectType) -> bool"""
        ...
    def __ne__(self, *args): ...

class DriveObjectTypeHandler(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """This class is responsible for change and get the possible types of the current DriveObject"""

    @property
    def CurrentDriveObjectType(self):
        """
        Gets the type of the current DriveObject

        Get: CurrentDriveObjectType(self: DriveObjectTypeHandler) -> DriveObjectType
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: DriveObjectTypeHandler) -> IEngineeringObject
        """
        ...
    @property
    def PossibleDriveObjectTypes(self):
        """
        Possible DriveObjectTypes of the current DriveObject

        Get: PossibleDriveObjectTypes(self: DriveObjectTypeHandler) -> DriveObjectTypeComposition
        """
        ...
    def ChangeDriveObjectType(self, targetDriveObjectType):
        """
        ChangeDriveObjectType(self: DriveObjectTypeHandler, targetDriveObjectType: DriveObjectType) -> bool

            Changes the type of the DriveObject

            targetDriveObjectType: Required type of the DriveObject

            Returns: System.Boolean
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: DriveObjectTypeHandler) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: DriveObjectTypeHandler) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class EncoderConfiguration(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """EncoderConfiguration is used for storing non siemens encoder data"""

    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: EncoderConfiguration) -> IEngineeringObject
        """
        ...
    @property
    def RequiredConfigurationEntries(self):
        """
        Accessible configuration entries on this EncoderConfiguration

        Get: RequiredConfigurationEntries(self: EncoderConfiguration) -> ConfigurationEntryComposition
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: EncoderConfiguration) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: EncoderConfiguration) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class HardwareProjection(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """This DFI are used for creating non siemens hardware elements on Sinamics drives"""

    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: HardwareProjection) -> IEngineeringObject
        """
        ...
    def GetCurrentEncoderConfiguration(self, encoderNumber):
        """
        GetCurrentEncoderConfiguration(self: HardwareProjection, encoderNumber: UInt16) -> EncoderConfiguration

            Get the currently existing configuration container according to the encoder dataset number

            encoderNumber: Requested encoder number

            Returns: Siemens.Engineering.MC.Drives.DFI.EncoderConfiguration
        """
        ...
    def GetCurrentMotorConfiguration(self, driveDataSetNumber):
        """
        GetCurrentMotorConfiguration(self: HardwareProjection, driveDataSetNumber: UInt16) -> MotorConfiguration

            Get the currently existing configuration container according to the motor dataset number

            driveDataSetNumber: Requested drive data set number

            Returns: Siemens.Engineering.MC.Drives.DFI.MotorConfiguration
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: HardwareProjection) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ProjectEncoderConfiguration(self, encoderConfiguration, encoderNumber):
        """
        ProjectEncoderConfiguration(self: HardwareProjection, encoderConfiguration: EncoderConfiguration, encoderNumber: UInt16) -> bool

            Project a configuration for the encoder

            encoderConfiguration: Encoder configuration object

            encoderNumber: Requested encoder number

            Returns: System.Boolean
        """
        ...
    def ProjectMotorConfiguration(self, motorConfiguration, driveDataSetNumber):
        """
        ProjectMotorConfiguration(self: HardwareProjection, motorConfiguration: MotorConfiguration, driveDataSetNumber: UInt16) -> bool

            Project a configuration for the motor

            motorConfiguration: Motor configuration object

            driveDataSetNumber: Requested drive data set number

            Returns: System.Boolean
        """
        ...
    def SetEncoder(self, encoderInterface, encoderType, absoluteIncrementalFlag, rotaryLinearFlag, encoderNumber):
        """
        SetEncoder(self: HardwareProjection, encoderInterface: EncoderInterface, encoderType: EncoderType, absoluteIncrementalFlag: AbsoluteIncrementalFlag, rotaryLinearFlag: RotaryLinearFlag, encoderNumber: UInt16) -> bool

            Set the encoder

            encoderInterface: Requested encoder interface

            encoderType: Requested encoder type

            absoluteIncrementalFlag: Requested absolute incremental flag

            rotaryLinearFlag: Requested rotary linear flag

            encoderNumber: Requested encoder number

            Returns: System.Boolean
        """
        ...
    def SetMotorType(self, motorType, driveDataSetNumber):
        """
        SetMotorType(self: HardwareProjection, motorType: MotorType, driveDataSetNumber: UInt16) -> bool

            Set the motor type

            motorType: Requested motor type

            driveDataSetNumber: Requested drive data set number

            Returns: System.Boolean
        """
        ...
    def ToString(self):
        """
        ToString(self: HardwareProjection) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class MotorConfiguration(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """MotorConfiguration is used for storing non siemens motor data"""

    @property
    def OptionalConfigurationEntries(self):
        """
        Accessible configuration entries on this MotorConfiguration

        Get: OptionalConfigurationEntries(self: MotorConfiguration) -> ConfigurationEntryComposition
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: MotorConfiguration) -> IEngineeringObject
        """
        ...
    @property
    def RequiredConfigurationEntries(self):
        """
        Accessible configuration entries on this MotorConfiguration

        Get: RequiredConfigurationEntries(self: MotorConfiguration) -> ConfigurationEntryComposition
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: MotorConfiguration) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: MotorConfiguration) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class OnlineDriveFunctionInterface(
    IEngineeringObject, IEngineeringService, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """An interface for calling online drive functions"""

    @property
    def DriveDomainFunctions(self):
        """
        Gets the DriveDomainFunctions object

        Get: DriveDomainFunctions(self: OnlineDriveFunctionInterface) -> DriveDomainFunctions
        """
        ...
    @property
    def DriveObjectFunctions(self):
        """
        Gets the DriveObjectFunctions object

        Get: DriveObjectFunctions(self: OnlineDriveFunctionInterface) -> DriveObjectFunctions
        """
        ...
    @property
    def HardwareProjection(self):
        """
        Gets the HardwareProjection object

        Get: HardwareProjection(self: OnlineDriveFunctionInterface) -> HardwareProjection
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: OnlineDriveFunctionInterface) -> IEngineeringObject
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: OnlineDriveFunctionInterface) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: OnlineDriveFunctionInterface) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...
