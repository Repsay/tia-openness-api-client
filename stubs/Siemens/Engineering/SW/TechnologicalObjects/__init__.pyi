# encoding: utf-8
# module Siemens.Engineering.SW.TechnologicalObjects calls itself TechnologicalObjects
# from Siemens.Engineering, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

from Siemens.Engineering import (
    IEngineeringAssociation,
    IEngineeringComposition,
    IEngineeringObject,
    IEngineeringServiceProvider,
)
from Siemens.Engineering.SW.Blocks import InstanceDB
from System import IEquatable

class TechnologicalInstanceDB(
    InstanceDB
):  # skipped bases: <type 'IEngineeringServiceProvider'>, <type 'IEngineeringObject'>, <type 'IShowable'>, <type 'IInternalObjectAccess'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IGenerateSource'>, <type 'IServiceProvider'>, <type 'IInternalInstanceAccess'>, <type 'IEquatable'>, <type 'IMasterCopySource'>, <type 'IEngineeringCompositionOrObject'>
    """Instance of a technological DB"""

    @property
    def Name(self):
        """
        Name of the Block

        Get: Name(self: TechnologicalInstanceDB) -> str

        Set: Name(self: TechnologicalInstanceDB) = value
        """
        ...
    @property
    def OfSystemLibElement(self):
        """
        Gets the name of the system library element associated with the DB

        Get: OfSystemLibElement(self: TechnologicalInstanceDB) -> str
        """
        ...
    @property
    def OfSystemLibVersion(self):
        """
        Gets the version of the system library element associated with the DB

        Get: OfSystemLibVersion(self: TechnologicalInstanceDB) -> Version

        Set: OfSystemLibVersion(self: TechnologicalInstanceDB) = value
        """
        ...
    @property
    def Parameters(self):
        """
        Get all technological parameters

        Get: Parameters(self: TechnologicalInstanceDB) -> TechnologicalParameterComposition
        """
        ...
    def Export(self, path, exportOptions):
        """
        Export(self: TechnologicalInstanceDB, path: FileInfo, exportOptions: ExportOptions)

            Simatic ML export of a TechnlogicalInstanceDB

            path: Path to the Simatic ML file

            exportOptions: Option to use for export (default, readonly, etc.)
        """
        ...

class TechnologicalInstanceDBAssociation(
    IEngineeringAssociation, IInternalAssociationAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalCollectionAccess'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>
    """TO Association"""

    @property
    def Parent(self):
        """
        Gets the parent..

        Get: Parent(self: TechnologicalInstanceDBAssociation) -> IEngineeringObject
        """
        ...
    def Add(self, item):
        """
        Add(self: TechnologicalInstanceDBAssociation, item: TechnologicalInstanceDB)

            Adds an item.

            item: The item to be added.
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: TechnologicalInstanceDBAssociation) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def Remove(self, item):
        """
        Remove(self: TechnologicalInstanceDBAssociation, item: TechnologicalInstanceDB) -> bool

            Removes an item.

            item: The item to be removed.

            Returns: true if the item was removed; otherwise false.
        """
        ...
    def ToString(self):
        """
        ToString(self: TechnologicalInstanceDBAssociation) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __add__(self, *args):  # cannot find CLR method
        """x.__add__(y) <==> x+y"""
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[TechnologicalInstanceDB](enumerable:  value: TechnologicalInstanceDB) -> bool"""
        ...
    def __ne__(self, *args): ...

class TechnologicalInstanceDBComposition(
    IEngineeringComposition, IInternalCompositionAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """TO composition"""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: TechnologicalInstanceDBComposition) -> IEngineeringObject
        """
        ...
    def CreateFrom(self, sourceMasterCopy):
        """
        CreateFrom(self: TechnologicalInstanceDBComposition, sourceMasterCopy: MasterCopy) -> TechnologicalInstanceDB

            Create TechnologicalInstanceDB from MasterCopy

            sourceMasterCopy: The source master copy

            Returns: Siemens.Engineering.SW.TechnologicalObjects.TechnologicalInstanceDB
        """
        ...
    def Find(self, name):
        """
        Find(self: TechnologicalInstanceDBComposition, name: str) -> TechnologicalInstanceDB

            Find by its name

            name: Name of the TechnologicalInstanceDB

            Returns: Siemens.Engineering.SW.TechnologicalObjects.TechnologicalInstanceDB
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: TechnologicalInstanceDBComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: TechnologicalInstanceDBComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[TechnologicalInstanceDB](enumerable:  value: TechnologicalInstanceDB) -> bool"""
        ...
    def __ne__(self, *args): ...

class TechnologicalInstanceDBGroup(
    IEngineeringObject, IInternalObjectAccess, IEngineeringServiceProvider, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IServiceProvider'>, <type 'IInternalInstanceAccess'>
    """Contains Technological Objects"""

    @property
    def Name(self):
        """
        Name of external source group

        Get: Name(self: TechnologicalInstanceDBGroup) -> str
        """
        ...
    @property
    def Parent(self):
        """
        Parent of this object

        Get: Parent(self: TechnologicalInstanceDBGroup) -> IEngineeringObject
        """
        ...
    @property
    def TechnologicalObjects(self):
        """
        Get all technological objects

        Get: TechnologicalObjects(self: TechnologicalInstanceDBGroup) -> TechnologicalInstanceDBComposition
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: TechnologicalInstanceDBGroup) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: TechnologicalInstanceDBGroup) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class TechnologicalInstanceDBSystemGroup(
    TechnologicalInstanceDBGroup
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IServiceProvider'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringServiceProvider'>, <type 'IEquatable'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """Contains Technological Objects"""

    pass

class TechnologicalParameter(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Represenst a technological parameter"""

    @property
    def Name(self):
        """
        Represents the name of a technological parameter

        Get: Name(self: TechnologicalParameter) -> str
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: TechnologicalParameter) -> IEngineeringObject
        """
        ...
    @property
    def Value(self):
        """
        Represents the value of a technological parameter

        Get: Value(self: TechnologicalParameter) -> object

        Set: Value(self: TechnologicalParameter) = value
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: TechnologicalParameter) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: TechnologicalParameter) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class TechnologicalParameterComposition(
    IEngineeringComposition, IInternalCompositionAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """Parameter composition"""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: TechnologicalParameterComposition) -> IEngineeringObject
        """
        ...
    def Find(self, name):
        """
        Find(self: TechnologicalParameterComposition, name: str) -> TechnologicalParameter

            Finds a TechnologicalParameter by name

            name: The name of the TechnologicalParameter

            Returns: Siemens.Engineering.SW.TechnologicalObjects.TechnologicalParameter
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: TechnologicalParameterComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: TechnologicalParameterComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[TechnologicalParameter](enumerable:  value: TechnologicalParameter) -> bool"""
        ...
    def __ne__(self, *args): ...

# variables with complex values
