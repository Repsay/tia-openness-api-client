# encoding: utf-8
# module Siemens.Engineering.Library calls itself Library
# from Siemens.Engineering, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes
from typing import Any, List, Union, overload
from Siemens.Engineering.SW import ISoftwareCompareTarget
from Siemens.Engineering import IEngineeringComposition, IEngineeringObject, ITransactionSupport, OpenMode
from System import Enum, IEquatable

from System.IO import FileInfo

from Siemens.Engineering.Library.MasterCopies import MasterCopySystemFolder, MasterCopyFolder

from Siemens.Engineering.Library.Types import LibraryTypeSystemFolder, LibraryTypeFolder

class ILibrary:
    """Base interface implemented by all libraries"""

    @property
    def MasterCopyFolder(self) -> Union[MasterCopySystemFolder, MasterCopyFolder]:
        """
        System folder containing master copies and master copy folders

        Get: MasterCopyFolder(self: ILibrary) -> MasterCopySystemFolder
        """
        ...
    @property
    def TypeFolder(self) -> Union[LibraryTypeSystemFolder, LibraryTypeFolder]:
        """
        System folder containing library types and library type folders

        Get: TypeFolder(self: ILibrary) -> LibraryTypeSystemFolder
        """
        ...
    def FindType(self, typeGuid):
        """
        FindType(self: ILibrary, typeGuid: Guid) -> LibraryType

            Searches the global library for a type object using a type GUID as the search criteria

            typeGuid: Globally unique identifier of the type object to be searched for

            Returns: Siemens.Engineering.Library.Types.LibraryType
        """
        ...
    def FindVersion(self, versionGuid):
        """
        FindVersion(self: ILibrary, versionGuid: Guid) -> LibraryTypeVersion

            Searches the global library for a version object using a version GUID as the search criteria

            versionGuid: Globally unique identifier of the version object to be searched for

            Returns: Siemens.Engineering.Library.Types.LibraryTypeVersion
        """
        ...
    def UpdateCheck(self, project, updateCheckMode):
        """
        UpdateCheck(self: ILibrary, project: Project, updateCheckMode: UpdateCheckMode) -> UpdateCheckResult

            Identify all instances in a project that require updating based on the content of this library

            project: The project to be compared with this library

            updateCheckMode: Used to control whether or not to log out of date instances

            Returns: Siemens.Engineering.Library.Types.UpdateCheckResult
        """
        ...
    def UpdateLibrary(self, sourceTypesAndFolders, targetLibrary):
        """UpdateLibrary(self: ILibrary, sourceTypesAndFolders:  targetLibrary: ILibrary)"""
        ...
    def UpdateProject(self, sourceTypesAndFolders, updateProjectScopes):
        """UpdateProject(self: ILibrary, sourceTypesAndFolders:  updateProjectScopes: IEnumerable[IUpdateProjectScope])"""
        ...

class GlobalLibrary(
    IEngineeringObject, ITransactionSupport, ILibrary, ISoftwareCompareTarget, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Represents a global library"""

    @property
    def Author(self):
        """
        Author of the Global Library

        Get: Author(self: GlobalLibrary) -> str
        """
        ...
    @property
    def Comment(self):
        """
        The global libraries comment

        Get: Comment(self: GlobalLibrary) -> MultilingualText
        """
        ...
    @property
    def IsModified(self):
        """
        True if the global library has been modified

        Get: IsModified(self: GlobalLibrary) -> bool
        """
        ...
    @property
    def IsReadOnly(self):
        """
        Is the global library open only for read

        Get: IsReadOnly(self: GlobalLibrary) -> bool
        """
        ...
    @property
    def LanguageSettings(self):
        """
        Global Library language settings

        Get: LanguageSettings(self: GlobalLibrary) -> LanguageSettings
        """
        ...
    @property
    def Name(self) -> str:
        """
        The name of the global library.

        Get: Name(self: GlobalLibrary) -> str
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: GlobalLibrary) -> IEngineeringObject
        """
        ...
    @property
    def Path(self):
        """
        The path to this global library

        Get: Path(self: GlobalLibrary) -> FileInfo
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: GlobalLibrary) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: GlobalLibrary) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class CorporateGlobalLibrary(
    GlobalLibrary
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'ISoftwareCompareTarget'>, <type 'IEngineeringCompositionOrObject'>, <type 'ITransactionSupport'>, <type 'IInternalObjectAccess'>, <type 'ILibrary'>
    """A corporate global library."""

    pass

class GlobalLibraryComposition(
    IEngineeringComposition[GlobalLibrary], IInternalCompositionAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """Composition of GlobalLibraries"""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: GlobalLibraryComposition) -> IEngineeringObject
        """
        ...
    def GetGlobalLibraryInfos(self) -> List[GlobalLibraryInfo]:
        """
        GetGlobalLibraryInfos(self: GlobalLibraryComposition) -> IList[GlobalLibraryInfo]

            Returns a list of LibraryInfo's representing preview state Global Libraries

            Returns: System.Collections.Generic.IList<Siemens.Engineering.Library.GlobalLibraryInfo>
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: GlobalLibraryComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    @overload
    def Open(self, libraryInfo: GlobalLibraryInfo) -> GlobalLibrary:
        """ Open(self: GlobalLibraryComposition, libraryInfo: GlobalLibraryInfo) -> GlobalLibrary """
        ...
    @overload
    def Open(self, path: FileInfo, openMode: OpenMode) -> UserGlobalLibrary:
        """ Open(self: GlobalLibraryComposition, path: FileInfo, openMode: OpenMode) -> UserGlobalLibrary """
        ...
    def Open(self, *__args: Any) -> Union[GlobalLibrary, UserGlobalLibrary]:
        """
        Open(self: GlobalLibraryComposition, libraryInfo: GlobalLibraryInfo) -> GlobalLibrary

            Opens the specified global library

            libraryInfo: The global library info associated with a global library to be opened

            Returns: Siemens.Engineering.Library.GlobalLibrary

        Open(self: GlobalLibraryComposition, path: FileInfo, openMode: OpenMode) -> UserGlobalLibrary

            Opens the specified global library

            path: Path to the global library

            openMode: The open mode to open the global library with.

            Returns: Siemens.Engineering.Library.UserGlobalLibrary
        """
        ...
    def OpenWithUpgrade(self, path):
        """
        OpenWithUpgrade(self: GlobalLibraryComposition, path: FileInfo) -> UserGlobalLibrary

            Opens the specified global library and allows for upgrade of older versions if possible.

            path: Path to the global library

            Returns: Siemens.Engineering.Library.UserGlobalLibrary
        """
        ...
    def Retrieve(self, sourcePath, targetDirectory, openMode):
        """
        Retrieve(self: GlobalLibraryComposition, sourcePath: FileInfo, targetDirectory: DirectoryInfo, openMode: OpenMode) -> UserGlobalLibrary

            Retrieves an archived library

            sourcePath: The path of the archived library file

            targetDirectory: The path to the folder where library would be retrieved.

            openMode: The open mode to open the global library with.

            Returns: Siemens.Engineering.Library.UserGlobalLibrary
        """
        ...
    def RetrieveWithUpgrade(self, sourcePath, targetDirectory, openMode):
        """
        RetrieveWithUpgrade(self: GlobalLibraryComposition, sourcePath: FileInfo, targetDirectory: DirectoryInfo, openMode: OpenMode) -> UserGlobalLibrary

            Retrieves a library from an archive and upgrades it to the current version

            sourcePath: The path of the archived library file

            targetDirectory: The path to the folder where library would be retrieved.

            openMode: The open mode to open the global library with.

            Returns: Siemens.Engineering.Library.UserGlobalLibrary
        """
        ...
    def ToString(self):
        """
        ToString(self: GlobalLibraryComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[GlobalLibrary](enumerable:  value: GlobalLibrary) -> bool"""
        ...
    def __ne__(self, *args): ...

class GlobalLibraryInfo(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Represents information for a Global Library"""

    @property
    def IsOpen(self):
        """
        Returns a Boolean representing if the global library associated with this GlobalLibraryInfo is already open or not.

        Get: IsOpen(self: GlobalLibraryInfo) -> bool
        """
        ...
    @property
    def IsReadOnly(self):
        """
        True if the globa library is currently read only.

        Get: IsReadOnly(self: GlobalLibraryInfo) -> bool
        """
        ...
    @property
    def LibraryType(self):
        """
        The Global Library Type

        Get: LibraryType(self: GlobalLibraryInfo) -> GlobalLibraryType
        """
        ...
    @property
    def Name(self) -> str:
        """
        The name of the global library.

        Get: Name(self: GlobalLibraryInfo) -> str
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: GlobalLibraryInfo) -> IEngineeringObject
        """
        ...
    @property
    def Path(self):
        """
        The full library path.

        Get: Path(self: GlobalLibraryInfo) -> FileInfo
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: GlobalLibraryInfo) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: GlobalLibraryInfo) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class GlobalLibraryType(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Represents the GlobalLibrary Types such as System, User, or Corporate

    enum GlobalLibraryType, values: Corporate (1), System (0), User (2)
    """

    Corporate = None
    System = None
    User = None
    value__ = None

class LibraryArchivationMode(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Library archivation modes

    enum LibraryArchivationMode, values: Compressed (1), DiscardRestorableData (2), DiscardRestorableDataAndCompressed (3), None (0)
    """

    Compressed = None
    DiscardRestorableData = None
    DiscardRestorableDataAndCompressed = None
    value__ = None

class ProjectLibrary(
    IEngineeringObject, ILibrary, ISoftwareCompareTarget, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Represents the project library"""

    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: ProjectLibrary) -> IEngineeringObject
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: ProjectLibrary) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: ProjectLibrary) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class SystemGlobalLibrary(
    GlobalLibrary
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'ISoftwareCompareTarget'>, <type 'IEngineeringCompositionOrObject'>, <type 'ITransactionSupport'>, <type 'IInternalObjectAccess'>, <type 'ILibrary'>
    """Represents a System Library"""

    pass

class UserGlobalLibrary(
    GlobalLibrary
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'ISoftwareCompareTarget'>, <type 'IEngineeringCompositionOrObject'>, <type 'ITransactionSupport'>, <type 'IInternalObjectAccess'>, <type 'ILibrary'>
    """Represents a User Global Library"""

    def Archive(self, targetDirectory, targetName, archivationMode):
        """
        Archive(self: UserGlobalLibrary, targetDirectory: DirectoryInfo, targetName: str, archivationMode: LibraryArchivationMode)

            Archives the User Global library.

            targetDirectory: Directory where the library to be archived

            targetName: File name for the archived file

            archivationMode: Archivation mode
        """
        ...
    def Close(self):
        """
        Close(self: UserGlobalLibrary)

            Closes the User Library
        """
        ...
    def Save(self):
        """
        Save(self: UserGlobalLibrary)

            Saves the User Library
        """
        ...
    def SaveAs(self, targetDirectory):
        """
        SaveAs(self: UserGlobalLibrary, targetDirectory: DirectoryInfo)

            Save a User Library to another location

            targetDirectory: The target directory path to save the User Library
        """
        ...

# variables with complex values
