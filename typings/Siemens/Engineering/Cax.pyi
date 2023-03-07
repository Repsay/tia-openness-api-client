# encoding: utf-8
# module Siemens.Engineering.Cax calls itself Cax
# from Siemens.Engineering, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

from Siemens.Engineering import IEngineeringObject, IEngineeringService
from System import Enum, IEquatable
from System.IO import FileInfo

class CaxImportOptions(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Cax Import Merge options

        Options for CAx Import Merge:
            MoveToParkingLot(0): Move the existing TIA Device to Parking Lot and import the CAx Device
            OverwriteTiaDevice(1): Overwrite the existing TIA Device with the CAx Device
            RetainTiaDevice(2): Retain the existing TIA Device and do not import the CAx Device

    """

    MoveToParkingLot = ...
    OverwriteTiaDevice = ...
    RetainTiaDevice = ...
    value__ = ...

class CaxProvider(
    IEngineeringObject, IEngineeringService, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Service Provider for CAx Export/Import operations"""

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: CaxProvider) -> IEngineeringObject
        """
        ...
    def Export(self, *__args) -> bool:
        """Command to CAx Export at Device level

        Returns:
            bool: System.Boolean
        """
        ...
    def GetHashCode(self) -> int:
        """Returns a hash code for this instance.

        Returns:
            int: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def Import(self, importFilePath: FileInfo, logFilePath: FileInfo, importOption: CaxImportOptions) -> bool:
        """Command to CAx Import

        Parameters:
            importFilePath (FileInfo): Import file path
            logFilePath (FileInfo): Log file path
            importOption (CaxImportOptions): Cax Import Merge options

        Returns:
            bool: System.Boolean
        """
        ...
    def ToString(self) -> str:
        """Returns a System.String that represents the current System.Object.

        Returns:
            str: A System.String that represents the current System.Object.
        """
        ...
