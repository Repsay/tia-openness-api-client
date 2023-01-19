# encoding: utf-8
# module Siemens.Engineering.HmiUnified.HmiConnections calls itself HmiConnections
# from Siemens.Engineering, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

from Siemens.Engineering import IEngineeringComposition, IEngineeringObject
from Siemens.Engineering.HmiUnified.Common import IValidator
from System import IEquatable

class HmiConnection(
    IValidator, IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Represents the HmiConnection"""

    @property
    def Comment(self):
        """
        Additional comments if any

        Get: Comment(self: HmiConnection) -> str

        Set: Comment(self: HmiConnection) = value
        """
        ...
    @property
    def CommunicationDriver(self):
        """
        Gives the communication driver

        Get: CommunicationDriver(self: HmiConnection) -> str

        Set: CommunicationDriver(self: HmiConnection) = value
        """
        ...
    @property
    def DisabledAtStartup(self):
        """
        Connection initially will be online or not in runtime.

        Get: DisabledAtStartup(self: HmiConnection) -> bool

        Set: DisabledAtStartup(self: HmiConnection) = value
        """
        ...
    @property
    def InitialAddress(self):
        """
                Get: InitialAddress(self: HmiConnection) -> str

        Set: InitialAddress(self: HmiConnection) = value
        """
        ...
    @property
    def Name(self):
        """
        Name of connection

        Get: Name(self: HmiConnection) -> str

        Set: Name(self: HmiConnection) = value
        """
        ...
    @property
    def Node(self):
        """
        Shows access point of Partner (eg PLC)

        Get: Node(self: HmiConnection) -> str
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: HmiConnection) -> IEngineeringObject
        """
        ...
    @property
    def Partner(self):
        """
        Name of connected partner

        Get: Partner(self: HmiConnection) -> str
        """
        ...
    @property
    def Station(self):
        """
        Name of the station to which partner is located.

        Get: Station(self: HmiConnection) -> str
        """
        ...
    def Delete(self):
        """
        Delete(self: HmiConnection)

            Deletes this instance.
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: HmiConnection) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: HmiConnection) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class HmiConnectionComposition(
    IEngineeringComposition, IInternalCompositionAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """Represents the Composition of Hmi Connections"""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: HmiConnectionComposition) -> IEngineeringObject
        """
        ...
    def Find(self, name):
        """
        Find(self: HmiConnectionComposition, name: str) -> HmiConnection

            Find method for Connection

            name: Connection Name

            Returns: Siemens.Engineering.HmiUnified.HmiConnections.HmiConnection
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: HmiConnectionComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: HmiConnectionComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[HmiConnection](enumerable:  value: HmiConnection) -> bool"""
        ...
    def __ne__(self, *args): ...
