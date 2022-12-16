# encoding: utf-8
# module Siemens.Engineering.HW.Utilities calls itself Utilities
# from Siemens.Engineering, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

from Siemens.Engineering import IEngineeringObject, IEngineeringComposition
from System import IEquatable

class HardwareUtility(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Abstract base class for all extensions to the HW model"""

    @property
    def Identifier(self):
        """
        Identifier for this HW extension

        Get: Identifier(self: HardwareUtility) -> str
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: HardwareUtility) -> IEngineeringObject
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: HardwareUtility) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: HardwareUtility) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class CardReaderPscProvider(
    HardwareUtility
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """Card reader provider utility for .psc file"""

    def Export(self, device, fileName):
        """
        Export(self: CardReaderPscProvider, device: Device, fileName: FileInfo)

            Exports device configuration to file

            device: device to be exported

            fileName: file name that will be saved(*.psc)
        """
        ...

class HardwareUtilityComposition(
    IEngineeringComposition, IInternalCompositionAccess, IEquatable # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """Composition of HardwareUtilities"""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: HardwareUtilityComposition) -> IEngineeringObject
        """
        ...
    def Find(self, identifier):
        """
        Find(self: HardwareUtilityComposition, identifier: str) -> HardwareUtility

            Finds a given extension

            identifier: Identifier to find

            Returns: Siemens.Engineering.HW.Utilities.HardwareUtility
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: HardwareUtilityComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: HardwareUtilityComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[HardwareUtility](enumerable:  value: HardwareUtility) -> bool"""
        ...
    def __ne__(self, *args): ...

class ModuleInformationProvider(
    HardwareUtility
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """Service provider for module information"""

    def FindContainerTypes(self, typeIdentifier):
        """
        FindContainerTypes(self: ModuleInformationProvider, typeIdentifier: str) -> Array[str]

            Finds the possible container types

            typeIdentifier: The type identifier to use to find a given container type

            Returns: System.String[]
        """
        ...
    def FindModuleTypes(self, partialTypeIdentifier):
        """
        FindModuleTypes(self: ModuleInformationProvider, partialTypeIdentifier: str) -> Array[str]

            Finds the possible module types

            partialTypeIdentifier: The partial type identifier to be used to find a given module type

            Returns: System.String[]
        """
        ...

class OpcUaExportProvider(
    HardwareUtility
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """Service provider for export of OPC UA"""

    def Export(self, deviceItem, path):
        """
        Export(self: OpcUaExportProvider, deviceItem: DeviceItem, path: FileInfo)

            Simatic ML export of a OPC UA

            deviceItem: The device item to be exported

            path: Path to the export file
        """
        ...
