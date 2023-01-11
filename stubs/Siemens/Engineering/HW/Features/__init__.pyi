# encoding: utf-8
# module Siemens.Engineering.HW.Features calls itself Features
# from Siemens.Engineering, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

from typing import Union
from Siemens.Engineering import IEngineeringAssociation, IEngineeringObject, IEngineeringService
from System import IEquatable
from Siemens.Engineering.HmiUnified import HmiSoftware

from Siemens.Engineering.SW import PlcSoftware

class HardwareFeature(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Base class for all HW related services"""

    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: HardwareFeature) -> IEngineeringObject
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: HardwareFeature) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: HardwareFeature) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class DeviceItemFeature(
    HardwareFeature
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """Base class for all DeviceItem related services"""

    @property
    def OwnedBy(self):
        """
        DeviceItem Object that owns this role

        Get: OwnedBy(self: DeviceItemFeature) -> DeviceItem
        """
        ...

class AddressController(
    DeviceItemFeature, IEngineeringService
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """Address controller device"""

    @property
    def RegisteredAddresses(self):
        """
        Associated registered address

        Get: RegisteredAddresses(self: AddressController) -> AddressAssociation
        """
        ...

class AddressControllerAssociation(
    IEngineeringAssociation, IInternalAssociationAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalCollectionAccess'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>
    """Associated address controllers"""

    @property
    def Parent(self):
        """
        Gets the parent..

        Get: Parent(self: AddressControllerAssociation) -> IEngineeringObject
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: AddressControllerAssociation) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: AddressControllerAssociation) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[AddressController](enumerable:  value: AddressController) -> bool"""
        ...
    def __ne__(self, *args): ...

class DeviceFeature(
    HardwareFeature
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """Base class for all Device related services"""

    @property
    def OwnedBy(self):
        """
        Device Object that owns this role

        Get: OwnedBy(self: DeviceFeature) -> Device
        """
        ...

class FrontPanelDisplay(
    DeviceItemFeature, IEngineeringService
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """Represents the Front Panel Display"""

    @property
    def AdaptLogoActivated(self):
        """
        Adapt the logo to the display

        Get: AdaptLogoActivated(self: FrontPanelDisplay) -> bool

        Set: AdaptLogoActivated(self: FrontPanelDisplay) = value
        """
        ...
    @property
    def UserDefinedLogoActivated(self):
        """
        Activate or deactivate the User Defined Logo

        Get: UserDefinedLogoActivated(self: FrontPanelDisplay) -> bool

        Set: UserDefinedLogoActivated(self: FrontPanelDisplay) = value
        """
        ...
    def SetUserDefinedLogo(self, logoImagePath):
        """
        SetUserDefinedLogo(self: FrontPanelDisplay, logoImagePath: FileInfo)

            Sets the Logo on the Display

            logoImagePath: Specifies the file info of the logo
        """
        ...

class IGsdObject:
    """Properties of a Gsd hardware object"""

    @property
    def GsdId(self):
        """
        The Gsd ID of the Gsd object

        Get: GsdId(self: IGsdObject) -> str
        """
        ...
    @property
    def GsdName(self):
        """
        The Gsd Name of the Gsd object

        Get: GsdName(self: IGsdObject) -> str
        """
        ...
    @property
    def GsdType(self):
        """
        The Gsd Type of the Gsd object

        Get: GsdType(self: IGsdObject) -> str
        """
        ...
    @property
    def IsProfibus(self):
        """
        Indicates if this Gsd device item supports Profibus

        Get: IsProfibus(self: IGsdObject) -> bool
        """
        ...
    @property
    def IsProfinet(self):
        """
        Indicates if this Gsd object supports Profinet

        Get: IsProfinet(self: IGsdObject) -> bool
        """
        ...

class GsdDevice(
    DeviceFeature, IGsdObject, IEngineeringService
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """Represents a Gsd device"""

    pass

class GsdDeviceItem(
    DeviceItemFeature, IGsdObject, IEngineeringService
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """Represents a Gsd device item"""

    def GetPrmData(self, dsNumber, byteOffset, length):
        """
        GetPrmData(self: GsdDeviceItem, dsNumber: int, byteOffset: int, length: int) -> Array[Byte]

            Returns the Prm Data for this Gsd device item

            dsNumber: Specifies which dsNumber to set the Prm Data to this Gsd device item

            byteOffset: The byte offset

            length: Specifies which length to get the Prm Data from this Gsd device item

            Returns: System.Byte[]
        """
        ...
    def SetPrmData(self, dsNumber, byteOffset, prmData):
        """SetPrmData(self: GsdDeviceItem, dsNumber: int, byteOffset: int, prmData: IEnumerable[Byte])"""
        ...

class HwIdentifierController(
    DeviceItemFeature, IEngineeringService
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """Represents a HW identifier controller"""

    @property
    def RegisteredHwIdentifiers(self):
        """
        Associated registered HW identifiers

        Get: RegisteredHwIdentifiers(self: HwIdentifierController) -> HwIdentifierAssociation
        """
        ...

class HwIdentifierControllerAssociation(
    IEngineeringAssociation, IInternalAssociationAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalCollectionAccess'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>
    """Associated Hw identifier controllers"""

    @property
    def Parent(self):
        """
        Gets the parent..

        Get: Parent(self: HwIdentifierControllerAssociation) -> IEngineeringObject
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: HwIdentifierControllerAssociation) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: HwIdentifierControllerAssociation) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[HwIdentifierController](enumerable:  value: HwIdentifierController) -> bool"""
        ...
    def __ne__(self, *args): ...

class NetworkInterface(
    DeviceItemFeature, IEngineeringService
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """Represents a HW interface"""

    @property
    def InterfaceOperatingMode(self):
        """
        The operating mode of this interface

        Get: InterfaceOperatingMode(self: NetworkInterface) -> InterfaceOperatingModes

        Set: InterfaceOperatingMode(self: NetworkInterface) = value
        """
        ...
    @property
    def InterfaceType(self):
        """
        The type of this interface

        Get: InterfaceType(self: NetworkInterface) -> NetType

        Set: InterfaceType(self: NetworkInterface) = value
        """
        ...
    @property
    def IoConnectors(self):
        """
        Composition of IO connectors

        Get: IoConnectors(self: NetworkInterface) -> IoConnectorComposition
        """
        ...
    @property
    def IoControllers(self):
        """
        Composition of IO controllers

        Get: IoControllers(self: NetworkInterface) -> IoControllerComposition
        """
        ...
    @property
    def Nodes(self):
        """
        Composition of nodes

        Get: Nodes(self: NetworkInterface) -> NodeComposition
        """
        ...
    @property
    def Ports(self):
        """
        Associated ports

        Get: Ports(self: NetworkInterface) -> NetworkPortAssociation
        """
        ...
    @property
    def TransferAreas(self):
        """
        Composition of transfer areas

        Get: TransferAreas(self: NetworkInterface) -> TransferAreaComposition
        """
        ...

class NetworkPort(
    DeviceItemFeature, IEngineeringService
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """Represents a port on a device item"""

    @property
    def ConnectedPorts(self):
        """
        Internal use only

        Get: ConnectedPorts(self: NetworkPort) -> NetworkPortAssociation
        """
        ...
    @property
    def Interface(self):
        """
        The interface supported by this port

        Get: Interface(self: NetworkPort) -> NetworkInterface
        """
        ...
    def ConnectToPort(self, partnerPort):
        """
        ConnectToPort(self: NetworkPort, partnerPort: NetworkPort)

            Connects to the Port

            partnerPort: The partner port to be disconnected
        """
        ...
    def DisconnectFromPort(self, partnerPort):
        """
        DisconnectFromPort(self: NetworkPort, partnerPort: NetworkPort)

            Disconnects a device from the given port

            partnerPort: The partner port to be disconnected
        """
        ...

class NetworkPortAssociation(
    IEngineeringAssociation, IInternalAssociationAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalCollectionAccess'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>
    """Associated ports"""

    @property
    def Parent(self):
        """
        Gets the parent..

        Get: Parent(self: NetworkPortAssociation) -> IEngineeringObject
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: NetworkPortAssociation) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: NetworkPortAssociation) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[NetworkPort](enumerable:  value: NetworkPort) -> bool"""
        ...
    def __ne__(self, *args): ...

class PcInterfaceAssignment(
    DeviceItemFeature, IEngineeringService
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """Interface Assignment Provider"""

    @property
    def HardwareResource(self):
        """
        Get or set hardware resource of interface

        Get: HardwareResource(self: PcInterfaceAssignment) -> HardwareResource

        Set: HardwareResource(self: PcInterfaceAssignment) = value
        """
        ...
    @property
    def IpcExpansion(self):
        """
        Get or set hardware IPC Expansion of interface

        Get: IpcExpansion(self: PcInterfaceAssignment) -> str

        Set: IpcExpansion(self: PcInterfaceAssignment) = value
        """
        ...
    @property
    def PcInterfaceAssignmentMode(self):
        """
        Returns type of interface assignment

        Get: PcInterfaceAssignmentMode(self: PcInterfaceAssignment) -> PcInterfaceAssignmentMode
        """
        ...
    @property
    def SoftwarePlc(self):
        """
        Returns cpu DeviceItem

        Get: SoftwarePlc(self: PcInterfaceAssignment) -> DeviceItem
        """
        ...
    def AssignInterface(self, interfaceAssignmentFor, softwareTarget=...):
        """
        AssignInterface(self: PcInterfaceAssignment, interfaceAssignmentFor: PcInterfaceAssignmentMode)

            Assign interface to one of the following( None, PC Station)

            interfaceAssignmentFor: assignment type for interface

        AssignInterface(self: PcInterfaceAssignment, interfaceAssignmentFor: PcInterfaceAssignmentMode, softwareTarget: DeviceItem)

            Assign interface to Software PLC

            interfaceAssignmentFor: assignment type for interface

            softwareTarget: if interface assignment will be to CPU, provide cpu device item
        """
        ...
    def GetAvailableIPCExpansions(self):
        """
        GetAvailableIPCExpansions(self: PcInterfaceAssignment) -> IEnumerable[str]

            Get available IPC expansion list that can be selected

            Returns: System.Collections.Generic.IEnumerable<System.String>
        """
        ...

class PlcAccessLevelProvider(
    DeviceItemFeature, IEngineeringService
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """Represents the Access level of the PLC Plus"""

    @property
    def PlcProtectionAccessLevel(self):
        """
        To set the protection access level type

        Get: PlcProtectionAccessLevel(self: PlcAccessLevelProvider) -> PlcProtectionAccessLevel

        Set: PlcProtectionAccessLevel(self: PlcAccessLevelProvider) = value
        """
        ...
    def ResetPassword(self, accessLevelType):
        """
        ResetPassword(self: PlcAccessLevelProvider, accessLevelType: PlcProtectionAccessLevel)

            Reset the password for the specific Access Level Type

            accessLevelType: Specifies the Access level type
        """
        ...
    def SetPassword(self, accessLevelType, password):
        """
        SetPassword(self: PlcAccessLevelProvider, accessLevelType: PlcProtectionAccessLevel, password: SecureString)

            set the password for the specific Access Level Type

            accessLevelType: Specifies the protection Access level type

            password: Specifies the password for the access level type
        """
        ...

class SoftwareContainer(
    DeviceItemFeature, IEngineeringService
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """Represents a class containing software components"""

    @property
    def Software(self) -> Union[PlcSoftware, HmiSoftware, None]:
        """Gets the software target containing the software elements of the device"""
        ...

class SubnetOwner(
    DeviceItemFeature, IEngineeringService
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """Represents a Subnet owner"""

    @property
    def Subnets(self):
        """
        Composition of Subnets

        Get: Subnets(self: SubnetOwner) -> SubnetComposition
        """
        ...
