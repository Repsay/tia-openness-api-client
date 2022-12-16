# encoding: utf-8
# module Siemens.Engineering.Hmi.Tag calls itself Tag
# from Siemens.Engineering, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

from Siemens.Engineering import IEngineeringComposition, IEngineeringObject, IEngineeringServiceProvider
from Siemens.Engineering.Library.MasterCopies import IMasterCopySource, IMasterCopyTarget
from Siemens.Engineering.Library.Types import LibraryType, LibraryTypeVersion
from System import IEquatable

class HmiUdtLibraryType(
    LibraryType
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'ILibraryTypeOrFolderSelection'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """Represents a library type made from a Udt"""

    pass

class HmiUdtLibraryTypeVersion(
    LibraryTypeVersion
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """Represents a library type version made from a Udt"""

    pass

class Tag(
    ILimit,  # type: ignore
    IEngineeringObject,
    IMasterCopySource,
    IInternalObjectAccess,  # type: ignore
    IEngineeringServiceProvider,
    IEquatable,
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IServiceProvider'>, <type 'IInternalInstanceAccess'>
    """Represents an Hmi tag"""

    @property
    def Name(self):
        """
        The name of the tag

        Get: Name(self: Tag) -> str
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: Tag) -> IEngineeringObject
        """
        ...
    def Delete(self):
        """
        Delete(self: Tag)

            Deletes this instance.
        """
        ...
    def Export(self, path, exportOptions):
        """
        Export(self: Tag, path: FileInfo, exportOptions: ExportOptions)

            Simatic ML export of a tag

            path: Path to the Simatic ML file

            exportOptions: Option to use for export (default, readonly, etc.)
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: Tag) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: Tag) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class TagComposition(
    IEngineeringComposition, IInternalCompositionAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """Composition of (Hmi)Tags"""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: TagComposition) -> IEngineeringObject
        """
        ...
    def CreateFrom(self, sourceMasterCopy):
        """
        CreateFrom(self: TagComposition, sourceMasterCopy: MasterCopy) -> Tag

            Create Tag from MasterCopy

            sourceMasterCopy: The source master copy

            Returns: Siemens.Engineering.Hmi.Tag.Tag
        """
        ...
    def Find(self, name):
        """
        Find(self: TagComposition, name: str) -> Tag

            Finds a given tag

            name: Name to find

            Returns: Siemens.Engineering.Hmi.Tag.Tag
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: TagComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def Import(self, path, importOptions):
        """
        Import(self: TagComposition, path: FileInfo, importOptions: ImportOptions) -> IList[Tag]

            Simatic ML import of a tag

            path: Path to the Simatic ML file

            importOptions: Options to use for Import

            Returns: System.Collections.Generic.IList<Siemens.Engineering.Hmi.Tag.Tag>
        """
        ...
    def ToString(self):
        """
        ToString(self: TagComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[Tag](enumerable:  value: Tag) -> bool"""
        ...
    def __ne__(self, *args): ...

class TagFolder(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Folder containing Hmi tag tables & Hmi tag user folders"""

    @property
    def Folders(self):
        """
        Composition of tag user folders

        Get: Folders(self: TagFolder) -> TagUserFolderComposition
        """
        ...
    @property
    def Name(self):
        """
        The name of the tag folder

        Get: Name(self: TagFolder) -> str
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: TagFolder) -> IEngineeringObject
        """
        ...
    @property
    def TagTables(self):
        """
        Composition of Hmi tag tables

        Get: TagTables(self: TagFolder) -> TagTableComposition
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: TagFolder) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: TagFolder) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class TagSystemFolder(
    TagFolder, IMasterCopyTarget
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """System folder containing Hmi tag tables & Hmi tag user folders"""

    @property
    def DefaultTagTable(self):
        """
        Get the default Hmi tag table

        Get: DefaultTagTable(self: TagSystemFolder) -> TagTable
        """
        ...

class TagTable(
    IEngineeringObject, IMasterCopySource, IMasterCopyTarget, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Represents an Hmi tag table"""

    @property
    def IsSystemObject(self):
        """
        Gets a value that identifies this is the default tag table

        Get: IsSystemObject(self: TagTable) -> bool
        """
        ...
    @property
    def Name(self):
        """
        The name of the tag table

        Get: Name(self: TagTable) -> str
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: TagTable) -> IEngineeringObject
        """
        ...
    @property
    def Tags(self):
        """
        Composition of Hmi tags

        Get: Tags(self: TagTable) -> TagComposition
        """
        ...
    def Delete(self):
        """
        Delete(self: TagTable)

            Deletes this instance.
        """
        ...
    def Export(self, path, exportOptions):
        """
        Export(self: TagTable, path: FileInfo, exportOptions: ExportOptions)

            Simatic ML export of a tag table

            path: Path to the Simatic ML file

            exportOptions: Option to use for export (default, readonly, etc.)
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: TagTable) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: TagTable) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class TagTableComposition(
    IEngineeringComposition, IInternalCompositionAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """Composition of (Hmi)TagTables"""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: TagTableComposition) -> IEngineeringObject
        """
        ...
    def CreateFrom(self, sourceMasterCopy):
        """
        CreateFrom(self: TagTableComposition, sourceMasterCopy: MasterCopy) -> TagTable

            Create TagTable from MasterCopy

            sourceMasterCopy: The source master copy

            Returns: Siemens.Engineering.Hmi.Tag.TagTable
        """
        ...
    def Find(self, name):
        """
        Find(self: TagTableComposition, name: str) -> TagTable

            Finds a given tag table

            name: Name to find

            Returns: Siemens.Engineering.Hmi.Tag.TagTable
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: TagTableComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def Import(self, path, importOptions):
        """
        Import(self: TagTableComposition, path: FileInfo, importOptions: ImportOptions) -> IList[TagTable]

            Simatic ML import of a tag table

            path: Path to the Simatic ML file

            importOptions: Options to use for Import

            Returns: System.Collections.Generic.IList<Siemens.Engineering.Hmi.Tag.TagTable>
        """
        ...
    def ToString(self):
        """
        ToString(self: TagTableComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[TagTable](enumerable:  value: TagTable) -> bool"""
        ...
    def __ne__(self, *args): ...

class TagUserFolder(
    TagFolder, IMasterCopySource, IMasterCopyTarget
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """User folder containing Hmi tag tables & Hmi tag user folders"""

    def Delete(self):
        """
        Delete(self: TagUserFolder)

            Deletes this instance.
        """
        ...

class TagUserFolderComposition(
    IEngineeringComposition, IInternalCompositionAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """Composition of (Hmi)TagUserFolders"""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: TagUserFolderComposition) -> IEngineeringObject
        """
        ...
    def Find(self, name):
        """
        Find(self: TagUserFolderComposition, name: str) -> TagUserFolder

            Finds a given tag user folder

            name: Name to find

            Returns: Siemens.Engineering.Hmi.Tag.TagUserFolder
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: TagUserFolderComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: TagUserFolderComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[TagUserFolder](enumerable:  value: TagUserFolder) -> bool"""
        ...
    def __ne__(self, *args): ...
