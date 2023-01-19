# encoding: utf-8
# module Siemens.Engineering.Hmi.RuntimeScripting calls itself RuntimeScripting
# from Siemens.Engineering, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

from Siemens.Engineering import IEngineeringObject, IEngineeringServiceProvider, IEngineeringComposition
from Siemens.Engineering.Library.Types import LibraryType, LibraryTypeVersion, ILibraryTypeInstantiationTarget
from Siemens.Engineering.Library.MasterCopies import IMasterCopySource, IMasterCopyTarget
from System import IEquatable

class CScriptLibraryType(
    LibraryType
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'ILibraryTypeOrFolderSelection'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """Class representing a Cscript library type"""

    pass

class CScriptLibraryTypeVersion(
    LibraryTypeVersion
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """Class representing a Cscript library type version"""

    pass

class VBScript(
    IEngineeringObject, IMasterCopySource, IInternalObjectAccess, IEngineeringServiceProvider, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IServiceProvider'>, <type 'IInternalInstanceAccess'>
    """Represents a VBscript"""

    @property
    def Name(self):
        """
        The name of the VBScript

        Get: Name(self: VBScript) -> str
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: VBScript) -> IEngineeringObject
        """
        ...
    def Delete(self):
        """
        Delete(self: VBScript)

            Deletes this instance.
        """
        ...
    def Export(self, path, exportOptions):
        """
        Export(self: VBScript, path: FileInfo, exportOptions: ExportOptions)

            Simatic ML export of a VBScript

            path: Path to the Simatic ML file

            exportOptions: Option to use for export (default, readonly, etc.)
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: VBScript) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: VBScript) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class VBScriptComposition(
    IEngineeringComposition, IInternalCompositionAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """Composition of VBScripts"""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: VBScriptComposition) -> IEngineeringObject
        """
        ...
    def CreateFrom(self, *__args):
        """
        CreateFrom(self: VBScriptComposition, libraryTypeVersion: VBScriptLibraryTypeVersion) -> VBScript

            Create script from library type version

            libraryTypeVersion: library type version

            Returns: Siemens.Engineering.Hmi.RuntimeScripting.VBScript

        CreateFrom(self: VBScriptComposition, sourceMasterCopy: MasterCopy) -> VBScript

            Create VBScript from MasterCopy

            sourceMasterCopy: The source master copy

            Returns: Siemens.Engineering.Hmi.RuntimeScripting.VBScript
        """
        ...
    def Find(self, name):
        """
        Find(self: VBScriptComposition, name: str) -> VBScript

            Finds a given VBScript

            name: Name to find

            Returns: Siemens.Engineering.Hmi.RuntimeScripting.VBScript
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: VBScriptComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def Import(self, path, importOptions):
        """
        Import(self: VBScriptComposition, path: FileInfo, importOptions: ImportOptions) -> IList[VBScript]

            Simatic ML import of a VBScript

            path: Path to the Simatic ML file

            importOptions: Options to use for Import

            Returns: System.Collections.Generic.IList<Siemens.Engineering.Hmi.RuntimeScripting.VBScript>
        """
        ...
    def ToString(self):
        """
        ToString(self: VBScriptComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[VBScript](enumerable:  value: VBScript) -> bool"""
        ...
    def __ne__(self, *args): ...

class VBScriptFolder(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Folder containing VBScripts & VBScript user folders"""

    @property
    def Folders(self):
        """
        Composition of VBScript user folders

        Get: Folders(self: VBScriptFolder) -> VBScriptUserFolderComposition
        """
        ...
    @property
    def Name(self):
        """
        The name of the VBScript folder

        Get: Name(self: VBScriptFolder) -> str
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: VBScriptFolder) -> IEngineeringObject
        """
        ...
    @property
    def VBScripts(self):
        """
        Composition of VBScripts

        Get: VBScripts(self: VBScriptFolder) -> VBScriptComposition
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: VBScriptFolder) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: VBScriptFolder) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class VBScriptLibraryType(
    LibraryType
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'ILibraryTypeOrFolderSelection'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """Represents a library type made from a VBScript"""

    pass

class VBScriptLibraryTypeVersion(
    LibraryTypeVersion
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """Represents a library type version made from a VBScript"""

    pass

class VBScriptSystemFolder(
    VBScriptFolder, IMasterCopyTarget, ILibraryTypeInstantiationTarget
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """System folder containing VBScripts & VBScript user folders"""

    pass

class VBScriptUserFolder(
    VBScriptFolder, IMasterCopySource, IMasterCopyTarget, ILibraryTypeInstantiationTarget
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """User folder containing VBScripts & VBScript user folders"""

    def Delete(self):
        """
        Delete(self: VBScriptUserFolder)

            Deletes this instance.
        """
        ...

class VBScriptUserFolderComposition(
    IEngineeringComposition, IInternalCompositionAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """Composition of VBScriptUserFolders"""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: VBScriptUserFolderComposition) -> IEngineeringObject
        """
        ...
    def Find(self, name):
        """
        Find(self: VBScriptUserFolderComposition, name: str) -> VBScriptUserFolder

            Finds a given VBScript user folder

            name: Name to find

            Returns: Siemens.Engineering.Hmi.RuntimeScripting.VBScriptUserFolder
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: VBScriptUserFolderComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: VBScriptUserFolderComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[VBScriptUserFolder](enumerable:  value: VBScriptUserFolder) -> bool"""
        ...
    def __ne__(self, *args): ...
