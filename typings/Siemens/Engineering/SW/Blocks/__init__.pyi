# encoding: utf-8
# module Siemens.Engineering.SW.Blocks calls itself Blocks
# from Siemens.Engineering, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

from typing import Optional
from Siemens.Engineering import (
    ExportOptions,
    IEngineeringObject,
    IShowable,
    IEngineeringServiceProvider,
    IEngineeringService,
    IEngineeringComposition,
    ImportOptions,
)
from Siemens.Engineering.SW.ExternalSources import IGenerateSource
from Siemens.Engineering.Library.MasterCopies import IMasterCopySource, IMasterCopyTarget
from Siemens.Engineering.Library.Types import LibraryType, LibraryTypeVersion, ILibraryTypeInstantiationTarget
from Siemens.Engineering.AdvancedProtection import ProtectionProviderBase
from System import IEquatable, Enum

from System.IO import FileInfo

from Siemens.Engineering.SW import SWImportOptions

class PlcBlock(IEngineeringObject, IShowable, IGenerateSource, IInternalObjectAccess, IEngineeringServiceProvider, IEquatable):  # type: ignore
    # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IServiceProvider'>, <type 'IInternalInstanceAccess'>
    """Represents a Plc block"""
    @property
    def AutoNumber(self):
        """
        Determines if the block gets the block number automatically or manually

        Get: AutoNumber(self: PlcBlock) -> bool

        Set: AutoNumber(self: PlcBlock) = value
        """
        ...
    @property
    def CodeModifiedDate(self):
        """
        Last code modification date

        Get: CodeModifiedDate(self: PlcBlock) -> DateTime
        """
        ...
    @property
    def CompileDate(self):
        """
        Last compilation date

        Get: CompileDate(self: PlcBlock) -> DateTime
        """
        ...
    @property
    def CreationDate(self):
        """
        Creation date of this Plc block

        Get: CreationDate(self: PlcBlock) -> DateTime
        """
        ...
    @property
    def HeaderAuthor(self):
        """
        PLC header attribute author

        Get: HeaderAuthor(self: PlcBlock) -> str
        """
        ...
    @property
    def HeaderFamily(self):
        """
        PLC header attribute family

        Get: HeaderFamily(self: PlcBlock) -> str
        """
        ...
    @property
    def HeaderName(self):
        """
        PLC header attribute name

        Get: HeaderName(self: PlcBlock) -> str
        """
        ...
    @property
    def HeaderVersion(self):
        """
        PLC header attribute version

        Get: HeaderVersion(self: PlcBlock) -> Version
        """
        ...
    @property
    def InterfaceModifiedDate(self):
        """
        Last interface modification

        Get: InterfaceModifiedDate(self: PlcBlock) -> DateTime
        """
        ...
    @property
    def IsConsistent(self) -> bool:
        """
        True if block and used data is consistent

        Get: IsConsistent(self: PlcBlock) -> bool
        """
        ...
    @property
    def IsKnowHowProtected(self):
        """
        Gets the know-how protection status of the block

        Get: IsKnowHowProtected(self: PlcBlock) -> bool
        """
        ...
    @property
    def MemoryLayout(self):
        """
        Indicates if a block has been optimized

        Get: MemoryLayout(self: PlcBlock) -> MemoryLayout
        """
        ...
    @property
    def ModifiedDate(self):
        """
        Last modification date including e.g. comments

        Get: ModifiedDate(self: PlcBlock) -> DateTime
        """
        ...
    @property
    def Name(self) -> str:
        """Gets the name of the Plc block."""
        ...
    @Name.setter
    def Name(self, value: str) -> None:
        """Sets the name of the Plc block."""
        ...
    @property
    def Number(self):
        """
        The number of this Plc block

        Get: Number(self: PlcBlock) -> int

        Set: Number(self: PlcBlock) = value
        """
        ...
    @property
    def ParameterModified(self):
        """
        Date of the last parameter modification

        Get: ParameterModified(self: PlcBlock) -> DateTime
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: PlcBlock) -> IEngineeringObject
        """
        ...
    @property
    def ProgrammingLanguage(self):
        """
        The language of this block

        Get: ProgrammingLanguage(self: PlcBlock) -> ProgrammingLanguage
        """
        ...
    @property
    def StructureModified(self):
        """
        Date of the last structure modification

        Get: StructureModified(self: PlcBlock) -> DateTime
        """
        ...
    def Delete(self):
        """
        Delete(self: PlcBlock)

            Deletes this instance.
        """
        ...
    def Export(self, path: FileInfo, exportOptions: ExportOptions) -> None:
        """
        Export(self: PlcBlock, path: FileInfo, exportOptions: ExportOptions)

            Simatic ML export of a Plc block

            path: Path to the Simatic ML file

            exportOptions: Option to use for export (default, readonly, etc.)
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: PlcBlock) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: PlcBlock) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...
    def __next__(self, *args) -> PlcBlock: ...

class DataBlock(
    PlcBlock, IMasterCopySource
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IServiceProvider'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IGenerateSource'>, <type 'IEngineeringServiceProvider'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEquatable'>, <type 'IShowable'>, <type 'IInternalObjectAccess'>
    """Class representing a data block"""

    pass

class ArrayDB(
    DataBlock
):  # skipped bases: <type 'IEngineeringServiceProvider'>, <type 'IEngineeringObject'>, <type 'IShowable'>, <type 'IInternalObjectAccess'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IGenerateSource'>, <type 'IServiceProvider'>, <type 'IInternalInstanceAccess'>, <type 'IEquatable'>, <type 'IMasterCopySource'>, <type 'IEngineeringCompositionOrObject'>
    """Class representing array DBs"""

    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: ArrayDB) -> IEngineeringObject
        """
        ...

class BlockType(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    The list of possible IECPL block types

    enum BlockType, values: FB (1), FBT (4), SDT (5), SFB (2), UDT (3), Undef (0)
    """

    FB = ...
    FBT = ...
    SDT = ...
    SFB = ...
    UDT = ...
    Undef = ...
    value__ = ...

class CodeBlock(
    PlcBlock, IMasterCopySource
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IServiceProvider'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IGenerateSource'>, <type 'IEngineeringServiceProvider'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEquatable'>, <type 'IShowable'>, <type 'IInternalObjectAccess'>
    """Class representing a code block"""

    pass

class CodeBlockLibraryType(
    LibraryType
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'ILibraryTypeOrFolderSelection'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """Class representing a code block library type"""

    pass

class CodeBlockLibraryTypeVersion(
    LibraryTypeVersion
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """Class representing a code block library type version"""

    pass

class FB(
    CodeBlock
):  # skipped bases: <type 'IEngineeringServiceProvider'>, <type 'IEngineeringObject'>, <type 'IShowable'>, <type 'IInternalObjectAccess'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IGenerateSource'>, <type 'IServiceProvider'>, <type 'IInternalInstanceAccess'>, <type 'IEquatable'>, <type 'IMasterCopySource'>, <type 'IEngineeringCompositionOrObject'>
    """Represents an FB"""

    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: FB) -> IEngineeringObject
        """
        ...
    @property
    def Supervisions(self):
        """
        Get supervisions

        Get: Supervisions(self: FB) -> SupervisionComposition
        """
        ...

class FC(
    CodeBlock
):  # skipped bases: <type 'IEngineeringServiceProvider'>, <type 'IEngineeringObject'>, <type 'IShowable'>, <type 'IInternalObjectAccess'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IGenerateSource'>, <type 'IServiceProvider'>, <type 'IInternalInstanceAccess'>, <type 'IEquatable'>, <type 'IMasterCopySource'>, <type 'IEngineeringCompositionOrObject'>
    """Represents an FC"""

    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: FC) -> IEngineeringObject
        """
        ...

class GlobalDB(
    DataBlock
):  # skipped bases: <type 'IEngineeringServiceProvider'>, <type 'IEngineeringObject'>, <type 'IShowable'>, <type 'IInternalObjectAccess'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IGenerateSource'>, <type 'IServiceProvider'>, <type 'IInternalInstanceAccess'>, <type 'IEquatable'>, <type 'IMasterCopySource'>, <type 'IEngineeringCompositionOrObject'>
    """Represents a global DB"""

    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: GlobalDB) -> IEngineeringObject
        """
        ...

class InstanceDB(
    DataBlock
):  # skipped bases: <type 'IEngineeringServiceProvider'>, <type 'IEngineeringObject'>, <type 'IShowable'>, <type 'IInternalObjectAccess'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IGenerateSource'>, <type 'IServiceProvider'>, <type 'IInternalInstanceAccess'>, <type 'IEquatable'>, <type 'IMasterCopySource'>, <type 'IEngineeringCompositionOrObject'>
    """Represents an instance DB"""

    @property
    def InstanceOfName(self):
        """
        The block name of the father instance (FB/SFB/UDT/SDT)

        Get: InstanceOfName(self: InstanceDB) -> str
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: InstanceDB) -> IEngineeringObject
        """
        ...

class InterfaceSnapshot(
    IEngineeringObject, IEngineeringService, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Provides Snapshot Value functionality."""

    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: InterfaceSnapshot) -> IEngineeringObject
        """
        ...
    def Export(self, path, exportOptions):
        """
        Export(self: InterfaceSnapshot, path: FileInfo, exportOptions: ExportOptions)

            Simatic ML export of snapshot values.

            path: Path to the Simatic ML file

            exportOptions: Option to use for export (default, readonly, etc.)
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: InterfaceSnapshot) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: InterfaceSnapshot) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class MemoryLayout(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Determines if a block access is optimized or not

    enum MemoryLayout, values: Optimized (1), Standard (0)
    """

    Optimized = ...
    Standard = ...
    value__ = ...

class OB(
    CodeBlock
):  # skipped bases: <type 'IEngineeringServiceProvider'>, <type 'IEngineeringObject'>, <type 'IShowable'>, <type 'IInternalObjectAccess'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IGenerateSource'>, <type 'IServiceProvider'>, <type 'IInternalInstanceAccess'>, <type 'IEquatable'>, <type 'IMasterCopySource'>, <type 'IEngineeringCompositionOrObject'>
    """Represents an OB"""

    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: OB) -> IEngineeringObject
        """
        ...
    @property
    def SecondaryType(self):
        """
        Additional information about the type

        Get: SecondaryType(self: OB) -> str
        """
        ...

class OBDataExchangeMode(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Enum for OBDataExchangeMode

    enum OBDataExchangeMode, values: Cyclic (1), None (0), Synchronous (2)
    """

    Cyclic = ...
    Synchronous = ...
    value__ = ...

class OBExecution(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Enum for Execution

    enum OBExecution, values: Daily (4), End_of_month (8), Every_minute (2), Hourly (3), Monthly (6), Never (0), Once (1), Weekly (5), Yearly (7)
    """

    Daily = ...
    End_of_month = ...
    Every_minute = ...
    Hourly = ...
    Monthly = ...
    Never = ...
    Once = ...
    value__ = ...
    Weekly = ...
    Yearly = ...

class OBTimeMode(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Enum for TimeMode

    enum OBTimeMode, values: Local (1), None (0), System (2)
    """

    Local = ...
    System = ...
    value__ = ...

class PlcBlockComposition(
    IEngineeringComposition[PlcBlock], IInternalCompositionAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """Composition of PlcBlocks"""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: PlcBlockComposition) -> IEngineeringObject
        """
        ...
    def CreateFB(self, name: str, isAutoNumbered: bool, number: int, programmingLanguage: ProgrammingLanguage) -> FB:
        """
        CreateFB(self: PlcBlockComposition, name: str, isAutoNumbered: bool, number: int, programmingLanguage: ProgrammingLanguage) -> FB

            Creates a block.

            name: Name of the block.

            isAutoNumbered: Indicates if block is autonumbered.

            number: Number of the block.

            programmingLanguage: Language of the block.

            Returns: Siemens.Engineering.SW.Blocks.FB
        """
        ...
    def CreateFrom(self, *__args):
        """
        CreateFrom(self: PlcBlockComposition, sourceMasterCopy: MasterCopy) -> PlcBlock

            Create PlcBlock from MasterCopy

            sourceMasterCopy: The source master copy

            Returns: Siemens.Engineering.SW.Blocks.PlcBlock

        CreateFrom(self: PlcBlockComposition, libraryTypeVersion: CodeBlockLibraryTypeVersion) -> PlcBlock

            Create from version

            libraryTypeVersion: type version

            Returns: Siemens.Engineering.SW.Blocks.PlcBlock
        """
        ...
    def CreateInstanceDB(self, name: str, isAutoNumbered: bool, number: int, instanceOfName: str):
        """
        CreateInstanceDB(self: PlcBlockComposition, name: str, isAutoNumbered: bool, number: int, instanceOfName: str) -> InstanceDB

            Creates an instance DB for Prodiag block.

            name: Name of the block.

            isAutoNumbered: Indicates if block is autonumbered.

            number: Number of the block.

            instanceOfName: Name of the block where db belongs to.

            Returns: Siemens.Engineering.SW.Blocks.InstanceDB
        """
        ...
    def Find(self, name: str) -> PlcBlock:
        """
        Find(self: PlcBlockComposition, name: str) -> PlcBlock

            Finds a given Plc block

            name: Name to find

            Returns: Siemens.Engineering.SW.Blocks.PlcBlock
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: PlcBlockComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def Import(
        self, path: FileInfo, importOptions: ImportOptions, swImportOptions: Optional[SWImportOptions] = ...
    ) -> list[PlcBlock]:
        """
        Import(self: PlcBlockComposition, path: FileInfo, importOptions: ImportOptions) -> IList[PlcBlock]

            Simatic ML import of a Plc block

            path: Path to the Simatic ML file

            importOptions: Options to use for Import

            Returns: System.Collections.Generic.IList<Siemens.Engineering.SW.Blocks.PlcBlock>

        Import(self: PlcBlockComposition, path: FileInfo, importOptions: ImportOptions, swImportOptions: SWImportOptions) -> IList[PlcBlock]

            Simatic ML import of a Plc block with ignore flags.

            path: Path to the Simatic ML file

            importOptions: Options to use for Import

            swImportOptions: Sw import options to use for Import

            Returns: System.Collections.Generic.IList<Siemens.Engineering.SW.Blocks.PlcBlock>
        """
        ...
    def ToString(self):
        """
        ToString(self: PlcBlockComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[PlcBlock](enumerable:  value: PlcBlock) -> bool"""
        ...
    def __ne__(self, *args): ...

class PlcBlockGroup(
    IEngineeringObject, IInternalObjectAccess, IEngineeringServiceProvider, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IServiceProvider'>, <type 'IInternalInstanceAccess'>
    """Group containing Plc blocks & Plc block user groups"""

    @property
    def Blocks(self) -> PlcBlockComposition:
        """Composition of Plc blocks"""
        ...
    @property
    def Groups(self) -> PlcBlockUserGroupComposition:
        """Composition of Plc block user groups"""
        ...
    @property
    def Name(self) -> str:
        """
        The name of the Plc block group

        Get: Name(self: PlcBlockGroup) -> str
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: PlcBlockGroup) -> IEngineeringObject
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: PlcBlockGroup) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: PlcBlockGroup) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class PlcBlockProtectionProvider(
    ProtectionProviderBase
):  # skipped bases: <type 'IEquatable'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringService'>, <type 'IInternalObjectAccess'>, <type 'IInternalInstanceAccess'>
    """Provides protection services."""

    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: PlcBlockProtectionProvider) -> IEngineeringObject
        """
        ...

class PlcBlockSystemGroup(
    PlcBlockGroup, IMasterCopyTarget, ILibraryTypeInstantiationTarget
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IServiceProvider'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringServiceProvider'>, <type 'IEquatable'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """System group containing Plc blocks & Plc block user groups"""

    @property
    def SystemBlockGroups(self) -> PlcSystemBlockGroupComposition:
        """
        Composition of Plc system block groups

        Get: SystemBlockGroups(self: PlcBlockSystemGroup) -> PlcSystemBlockGroupComposition
        """
        ...

class PlcBlockUserGroup(
    PlcBlockGroup, IMasterCopySource, IMasterCopyTarget, ILibraryTypeInstantiationTarget
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IServiceProvider'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringServiceProvider'>, <type 'IEquatable'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """User group containing Plc blocks & Plc block user groups"""

    def Delete(self):
        """
        Delete(self: PlcBlockUserGroup)

            Deletes this instance.
        """
        ...
    def __next__(self) -> PlcBlockUserGroup: ...

class PlcBlockUserGroupComposition(
    IEngineeringComposition[PlcBlockUserGroup], IInternalCompositionAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """Composition of PlcBlockUserGroups"""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: PlcBlockUserGroupComposition) -> IEngineeringObject
        """
        ...
    def Create(self, name: str) -> PlcBlockUserGroup:
        """Create PlcBlockUserGroup with given name

        Parameters:
            name (str): Name of the PlcBlockUserGroup

        Returns:
            PlcBlockUserGroup: PlcBlockUserGroup with given name
        """
    def CreateFrom(self, sourceMasterCopy):
        """
        CreateFrom(self: PlcBlockUserGroupComposition, sourceMasterCopy: MasterCopy) -> PlcBlockUserGroup

            Create PlcBlockUserGroup from MasterCopy

            sourceMasterCopy: The source master copy

            Returns: Siemens.Engineering.SW.Blocks.PlcBlockUserGroup
        """
        ...
    def Find(self, name: str) -> PlcBlockUserGroup:
        """
        Find(self: PlcBlockUserGroupComposition, name: str) -> PlcBlockUserGroup

            Finds a given Plc block user group

            name: Name to find

            Returns: Siemens.Engineering.SW.Blocks.PlcBlockUserGroup
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: PlcBlockUserGroupComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: PlcBlockUserGroupComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[PlcBlockUserGroup](enumerable:  value: PlcBlockUserGroup) -> bool"""
        ...
    def __ne__(self, *args): ...

class PlcSystemBlockGroup(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Group containing Plc system blocks & Plc system block groups"""

    @property
    def Blocks(self) -> PlcBlockComposition:
        """
        Composition of Plc system blocks

        Get: Blocks(self: PlcSystemBlockGroup) -> PlcBlockComposition
        """
        ...
    @property
    def Groups(self) -> PlcSystemBlockGroupComposition:
        """
        Composition of Plc system block groups

        Get: Groups(self: PlcSystemBlockGroup) -> PlcSystemBlockGroupComposition
        """
        ...
    @property
    def Name(self) -> str:
        """
        The name of the Plc system block group

        Get: Name(self: PlcSystemBlockGroup) -> str
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: PlcSystemBlockGroup) -> IEngineeringObject
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: PlcSystemBlockGroup) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: PlcSystemBlockGroup) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...
    def __next__(self) -> PlcSystemBlockGroup: ...

class PlcSystemBlockGroupComposition(
    IEngineeringComposition[PlcSystemBlockGroup], IInternalCompositionAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """Composition of PlcSystemBlockGroups"""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: PlcSystemBlockGroupComposition) -> IEngineeringObject
        """
        ...
    def Create(self, name: str) -> PlcSystemBlockGroup:
        """Create PlcSystemBlockGroup with given name

        Parameters:
            name (str): Name of the PlcSystemBlockGroup

        Returns:
            PlcSystemBlockGroup: PlcSystemBlockGroup with given name
        """
    def Find(self, name: str) -> PlcSystemBlockGroup:
        """
        Find(self: PlcSystemBlockGroupComposition, name: str) -> PlcSystemBlockGroup

            Finds a given Plc system block group

            name: Name to find

            Returns: Siemens.Engineering.SW.Blocks.PlcSystemBlockGroup
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: PlcSystemBlockGroupComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: PlcSystemBlockGroupComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[PlcSystemBlockGroup](enumerable:  value: PlcSystemBlockGroup) -> bool"""
        ...
    def __ne__(self, *args): ...

class ProgrammingLanguage(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    The list of possible creation languages of programming blocks

    enum ProgrammingLanguage, values: CFC (8), CPU_DB (7), DB (5), F_CALL (26), F_DB (18), F_FBD (17), F_FBD_LIB (20), F_LAD (16), F_LAD_LIB (19), F_STL (15), FBD (3), FBD_IEC (10), FCP (21), FLD (22), GRAPH (6), LAD (2), LAD_IEC (11), Motion_DB (25), ProDiag (23), ProDiag_OB (24), RSE (14), S7_PDIAG (13), SCL (4), SDB (12), SFC (9), STL (1), Undef (0)
    """

    CFC = ...
    CPU_DB = ...
    DB = ...
    FBD = ...
    FBD_IEC = ...
    FCP = ...
    FLD = ...
    F_CALL = ...
    F_DB = ...
    F_FBD = ...
    F_FBD_LIB = ...
    F_LAD = ...
    F_LAD_LIB = ...
    F_STL = ...
    GRAPH = ...
    LAD = ...
    LAD_IEC = ...
    Motion_DB = ...
    ProDiag = ...
    ProDiag_OB = ...
    RSE = ...
    S7_PDIAG = ...
    SCL = ...
    SDB = ...
    SFC = ...
    STL = ...
    Undef = ...
    value__ = ...

class Supervision(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Supervision"""

    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: Supervision) -> IEngineeringObject
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: Supervision) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: Supervision) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class SupervisionComposition(
    IEngineeringComposition, IInternalCompositionAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """Supervisions of the block"""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: SupervisionComposition) -> IEngineeringObject
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: SupervisionComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: SupervisionComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[Supervision](enumerable:  value: Supervision) -> bool"""
        ...
    def __ne__(self, *args): ...
