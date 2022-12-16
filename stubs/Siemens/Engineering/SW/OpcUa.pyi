# encoding: utf-8
# module Siemens.Engineering.SW.OpcUa calls itself OpcUa
# from Siemens.Engineering, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

from Siemens.Engineering import IEngineeringComposition, IEngineeringObject, IEngineeringService
from System import IEquatable

class OpcUaCommunicationGroup(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Top level OpcUa Communication folder"""

    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: OpcUaCommunicationGroup) -> IEngineeringObject
        """
        ...
    @property
    def ServerInterfaceGroup(self):
        """
        OPCUA Server Interface Folder

        Get: ServerInterfaceGroup(self: OpcUaCommunicationGroup) -> ServerInterfaceGroup
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: OpcUaCommunicationGroup) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: OpcUaCommunicationGroup) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class OpcUaProvider(
    IEngineeringObject, IEngineeringService, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """OpcUa Provider"""

    @property
    def CommunicationGroup(self):
        """
        Access the OpcUa Communication Folder

        Get: CommunicationGroup(self: OpcUaProvider) -> OpcUaCommunicationGroup
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: OpcUaProvider) -> IEngineeringObject
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: OpcUaProvider) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: OpcUaProvider) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class ServerInterface(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """OpcUa Server Interface"""

    @property
    def Author(self):
        """
        Author

        Get: Author(self: ServerInterface) -> str

        Set: Author(self: ServerInterface) = value
        """
        ...
    @property
    def Comment(self):
        """
        Comment

        Get: Comment(self: ServerInterface) -> MultilingualText
        """
        ...
    @property
    def CreationTime(self):
        """
        Creation time

        Get: CreationTime(self: ServerInterface) -> DateTime
        """
        ...
    @property
    def Enabled(self):
        """
        Enable server interface and download to PLC

        Get: Enabled(self: ServerInterface) -> bool

        Set: Enabled(self: ServerInterface) = value
        """
        ...
    @property
    def LastModified(self):
        """
        Last modified time

        Get: LastModified(self: ServerInterface) -> DateTime
        """
        ...
    @property
    def Name(self):
        """
        Name

        Get: Name(self: ServerInterface) -> str
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: ServerInterface) -> IEngineeringObject
        """
        ...
    def Delete(self):
        """
        Delete(self: ServerInterface)

            Deletes this instance.
        """
        ...
    def Export(self, filePath):
        """
        Export(self: ServerInterface, filePath: FileInfo)

            Exports the original XML File

            filePath: Path to the location to save
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: ServerInterface) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def Import(self, filePath):
        """
        Import(self: ServerInterface, filePath: FileInfo)

            Import file

            filePath: Path to file
        """
        ...
    def ToString(self):
        """
        ToString(self: ServerInterface) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class ServerInterfaceComposition(
    IEngineeringComposition, IInternalCompositionAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """Composition of Server Interfaces"""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: ServerInterfaceComposition) -> IEngineeringObject
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: ServerInterfaceComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: ServerInterfaceComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[ServerInterface](enumerable:  value: ServerInterface) -> bool"""
        ...
    def __ne__(self, *args): ...

class ServerInterfaceGroup(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Contains Server Interfaces"""

    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: ServerInterfaceGroup) -> IEngineeringObject
        """
        ...
    @property
    def ServerInterfaces(self):
        """
        Returns a list of Server Interfaces

        Get: ServerInterfaces(self: ServerInterfaceGroup) -> ServerInterfaceComposition
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: ServerInterfaceGroup) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: ServerInterfaceGroup) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...
