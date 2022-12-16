# encoding: utf-8
# module Siemens.Engineering.Hmi.Cycle calls itself Cycle
# from Siemens.Engineering, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

from Siemens.Engineering import IEngineeringComposition, IEngineeringObject
from System import IEquatable

class Cycle(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Represents a time period for a pass with a possible starting point"""

    @property
    def IsSystemObject(self):
        """
        Gets a value that identifies this is as a system cycle

        Get: IsSystemObject(self: Cycle) -> bool
        """
        ...
    @property
    def Name(self):
        """
        The name of the cycle

        Get: Name(self: Cycle) -> str
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: Cycle) -> IEngineeringObject
        """
        ...
    def Delete(self):
        """
        Delete(self: Cycle)

            Deletes this instance.
        """
        ...
    def Export(self, path, exportOptions):
        """
        Export(self: Cycle, path: FileInfo, exportOptions: ExportOptions)

            Simatic ML export of a cycle

            path: Path to the Simatic ML file

            exportOptions: Option to use for export (default, readonly, etc.)
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: Cycle) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: Cycle) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class CycleComposition(
    IEngineeringComposition, IInternalCompositionAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """Composition of Cycles"""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: CycleComposition) -> IEngineeringObject
        """
        ...
    def Find(self, name):
        """
        Find(self: CycleComposition, name: str) -> Cycle

            Finds a given cycle

            name: Name to find

            Returns: Siemens.Engineering.Hmi.Cycle.Cycle
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: CycleComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def Import(self, path, importOptions):
        """
        Import(self: CycleComposition, path: FileInfo, importOptions: ImportOptions) -> IList[Cycle]

            Simatic ML import of a cycle

            path: Path to the Simatic ML file

            importOptions: Options to use for Import

            Returns: System.Collections.Generic.IList<Siemens.Engineering.Hmi.Cycle.Cycle>
        """
        ...
    def ToString(self):
        """
        ToString(self: CycleComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[Cycle](enumerable:  value: Cycle) -> bool"""
        ...
    def __ne__(self, *args): ...
