# encoding: utf-8
# module Siemens.Engineering.Hmi.Communication calls itself Communication
# from Siemens.Engineering, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

from Siemens.Engineering import IEngineeringComposition, IEngineeringObject
from System import IEquatable

class Connection(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Represents a logical connection between an HMI device and a PLC device"""

    @property
    def Name(self):
        """
        The name of the connection

        Get: Name(self: Connection) -> str
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: Connection) -> IEngineeringObject
        """
        ...
    def Delete(self):
        """
        Delete(self: Connection)

            Deletes this instance.
        """
        ...
    def Export(self, path, exportOptions):
        """
        Export(self: Connection, path: FileInfo, exportOptions: ExportOptions)

            Simatic ML export of a connection

            path: Path to the Simatic ML file

            exportOptions: Option to use for export (default, readonly, etc.)
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: Connection) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: Connection) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class ConnectionComposition(
    IEngineeringComposition, IInternalCompositionAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """Composition of Connections"""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: ConnectionComposition) -> IEngineeringObject
        """
        ...
    def Find(self, name):
        """
        Find(self: ConnectionComposition, name: str) -> Connection

            Finds a given connection

            name: Name to find

            Returns: Siemens.Engineering.Hmi.Communication.Connection
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: ConnectionComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def Import(self, path, importOptions):
        """
        Import(self: ConnectionComposition, path: FileInfo, importOptions: ImportOptions) -> IList[Connection]

            Simatic ML import of a connection

            path: Path to the Simatic ML file

            importOptions: Options to use for Import

            Returns: System.Collections.Generic.IList<Siemens.Engineering.Hmi.Communication.Connection>
        """
        ...
    def ToString(self):
        """
        ToString(self: ConnectionComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[Connection](enumerable:  value: Connection) -> bool"""
        ...
    def __ne__(self, *args): ...
