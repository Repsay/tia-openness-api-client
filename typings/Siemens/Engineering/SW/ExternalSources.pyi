# encoding: utf-8
# module Siemens.Engineering.SW.ExternalSources calls itself ExternalSources
# from Siemens.Engineering, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

from Siemens.Engineering import IEngineeringObject, IEngineeringComposition
from Siemens.Engineering.Library.MasterCopies import IMasterCopySource
from System import Enum, IEquatable

class GenerateBlockOption(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Lists the possible options for block generation from source

    enum GenerateBlockOption, values: KeepOnError (1), None (0)
    """

    KeepOnError = None
    value__ = None

class GenerateOptions(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Options for source generation

    enum GenerateOptions, values: None (0), WithDependencies (1)
    """

    value__ = None
    WithDependencies = None

class IGenerateSource:
    """Can generate source."""

    pass

class PlcExternalSource(
    IEngineeringObject, IMasterCopySource, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Represents a Plc external source"""

    @property
    def Name(self):
        """
        The name of the Plc external source

        Get: Name(self: PlcExternalSource) -> str
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: PlcExternalSource) -> IEngineeringObject
        """
        ...
    def Delete(self):
        """
        Delete(self: PlcExternalSource)

            Deletes this instance.
        """
        ...
    def GenerateBlocksFromSource(self, generateBlockOption=...):
        """
        GenerateBlocksFromSource(self: PlcExternalSource)

            Creates a block or blocks from the current source file object

        GenerateBlocksFromSource(self: PlcExternalSource, generateBlockOption: GenerateBlockOption) -> IList[IEngineeringObject]

            Creates a block or blocks from the current source file object

            generateBlockOption: Option to use for block generation from source

            Returns: System.Collections.Generic.IList<Siemens.Engineering.IEngineeringObject>
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: PlcExternalSource) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: PlcExternalSource) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class PlcExternalSourceComposition(
    IEngineeringComposition, IInternalCompositionAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """Composition of PlcExternalSources"""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: PlcExternalSourceComposition) -> IEngineeringObject
        """
        ...
    def CreateFrom(self, sourceMasterCopy):
        """
        CreateFrom(self: PlcExternalSourceComposition, sourceMasterCopy: MasterCopy) -> PlcExternalSource

            Create External Source from MasterCopy

            sourceMasterCopy: The source master copy

            Returns: Siemens.Engineering.SW.ExternalSources.PlcExternalSource
        """
        ...
    def CreateFromFile(self, name, path):
        """
        CreateFromFile(self: PlcExternalSourceComposition, name: str, path: str) -> PlcExternalSource

            Create an external source from a specified file

            name: Name of Plc external source to be created

            path: Path to the external source file

            Returns: Siemens.Engineering.SW.ExternalSources.PlcExternalSource
        """
        ...
    def Find(self, name):
        """
        Find(self: PlcExternalSourceComposition, name: str) -> PlcExternalSource

            Finds a given Plc external source

            name: Name to find

            Returns: Siemens.Engineering.SW.ExternalSources.PlcExternalSource
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: PlcExternalSourceComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: PlcExternalSourceComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[PlcExternalSource](enumerable:  value: PlcExternalSource) -> bool"""
        ...
    def __ne__(self, *args): ...

class PlcExternalSourceGroup(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Group containing Plc external sources & Plc external source user groups"""

    @property
    def ExternalSources(self):
        """
        Composition of Plc external sources

        Get: ExternalSources(self: PlcExternalSourceGroup) -> PlcExternalSourceComposition
        """
        ...
    @property
    def Groups(self):
        """
        Composition of Plc external source user groups

        Get: Groups(self: PlcExternalSourceGroup) -> PlcExternalSourceUserGroupComposition
        """
        ...
    @property
    def Name(self):
        """
        The name of the Plc external source group

        Get: Name(self: PlcExternalSourceGroup) -> str
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: PlcExternalSourceGroup) -> IEngineeringObject
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: PlcExternalSourceGroup) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: PlcExternalSourceGroup) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class PlcExternalSourceSystemGroup(
    PlcExternalSourceGroup
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """System group containing Plc external sources & Plc external source user groups"""

    def GenerateSource(self, blocks, sourceFile, generateOption=...):
        """GenerateSource(self: PlcExternalSourceSystemGroup, blocks:  sourceFile: FileInfo, generateOption: GenerateOptions)"""
        ...

class PlcExternalSourceUserGroup(
    PlcExternalSourceGroup
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """User group containing Plc external sources & Plc external source user groups"""

    def Delete(self):
        """
        Delete(self: PlcExternalSourceUserGroup)

            Deletes this instance.
        """
        ...

class PlcExternalSourceUserGroupComposition(
    IEngineeringComposition, IInternalCompositionAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """Composition of PlcExternalSourceUserGroups"""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: PlcExternalSourceUserGroupComposition) -> IEngineeringObject
        """
        ...
    def CreateFrom(self, sourceMasterCopy):
        """
        CreateFrom(self: PlcExternalSourceUserGroupComposition, sourceMasterCopy: MasterCopy) -> PlcExternalSourceUserGroup

            Create ExternalSourceUserGroup from MasterCopy

            sourceMasterCopy: The source master copy

            Returns: Siemens.Engineering.SW.ExternalSources.PlcExternalSourceUserGroup
        """
        ...
    def Find(self, name):
        """
        Find(self: PlcExternalSourceUserGroupComposition, name: str) -> PlcExternalSourceUserGroup

            Finds a given Plc external source user group

            name: Name to find

            Returns: Siemens.Engineering.SW.ExternalSources.PlcExternalSourceUserGroup
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: PlcExternalSourceUserGroupComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: PlcExternalSourceUserGroupComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[PlcExternalSourceUserGroup](enumerable:  value: PlcExternalSourceUserGroup) -> bool"""
        ...
    def __ne__(self, *args): ...
