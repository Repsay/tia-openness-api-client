# encoding: utf-8
# module Siemens.Engineering.Hmi.Screen calls itself Screen
# from Siemens.Engineering, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

from Siemens.Engineering import IEngineeringComposition, IEngineeringObject, IEngineeringServiceProvider
from Siemens.Engineering.Library.MasterCopies import IMasterCopySource, IMasterCopyTarget
from Siemens.Engineering.Library.Types import ILibraryTypeInstantiationTarget, LibraryType, LibraryTypeVersion
from System import Enum, IEquatable

class Screen(
    IEngineeringObject, IMasterCopySource, IInternalObjectAccess, IEngineeringServiceProvider, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IServiceProvider'>, <type 'IInternalInstanceAccess'>
    """Represents a screen"""

    @property
    def Name(self):
        """
        The name of the screen

        Get: Name(self: Screen) -> str
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: Screen) -> IEngineeringObject
        """
        ...
    def Delete(self):
        """
        Delete(self: Screen)

            Deletes this instance.
        """
        ...
    def Export(self, path, exportOptions):
        """
        Export(self: Screen, path: FileInfo, exportOptions: ExportOptions)

            Simatic ML export of a screen

            path: Path to the Simatic ML file

            exportOptions: Option to use for export (default, readonly, etc.)
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: Screen) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: Screen) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class ScreenComposition(
    IEngineeringComposition, IInternalCompositionAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """Composition of Screens"""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: ScreenComposition) -> IEngineeringObject
        """
        ...
    def CreateFrom(self, *__args):
        """
        CreateFrom(self: ScreenComposition, libraryTypeVersion: ScreenLibraryTypeVersion) -> Screen

            Create screen from type version

            libraryTypeVersion: screen version

            Returns: Siemens.Engineering.Hmi.Screen.Screen

        CreateFrom(self: ScreenComposition, sourceMasterCopy: MasterCopy) -> Screen

            Create Screen from MasterCopy

            sourceMasterCopy: The source master copy

            Returns: Siemens.Engineering.Hmi.Screen.Screen
        """
        ...
    def Find(self, name):
        """
        Find(self: ScreenComposition, name: str) -> Screen

            Finds a given screen

            name: Name to find

            Returns: Siemens.Engineering.Hmi.Screen.Screen
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: ScreenComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def Import(self, path, importOptions):
        """
        Import(self: ScreenComposition, path: FileInfo, importOptions: ImportOptions) -> IList[Screen]

            Simatic ML import of a screen

            path: Path to the Simatic ML file

            importOptions: Options to use for Import

            Returns: System.Collections.Generic.IList<Siemens.Engineering.Hmi.Screen.Screen>
        """
        ...
    def ToString(self):
        """
        ToString(self: ScreenComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[Screen](enumerable:  value: Screen) -> bool"""
        ...
    def __ne__(self, *args): ...

class ScreenFolder(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Represents a screen folder"""

    @property
    def Folders(self):
        """
        Composition of screen user folders

        Get: Folders(self: ScreenFolder) -> ScreenUserFolderComposition
        """
        ...
    @property
    def Name(self):
        """
        The name of the screen folder

        Get: Name(self: ScreenFolder) -> str
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: ScreenFolder) -> IEngineeringObject
        """
        ...
    @property
    def Screens(self):
        """
        Composition of screens

        Get: Screens(self: ScreenFolder) -> ScreenComposition
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: ScreenFolder) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: ScreenFolder) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class ScreenGlobalElements(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Represents the screen global elements"""

    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: ScreenGlobalElements) -> IEngineeringObject
        """
        ...
    def Export(self, path, exportOptions):
        """
        Export(self: ScreenGlobalElements, path: FileInfo, exportOptions: ExportOptions)

            Simatic ML export of screen global elements

            path: Path to the Simatic ML file

            exportOptions: Option to use for export (default, readonly, etc.)
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: ScreenGlobalElements) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: ScreenGlobalElements) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class ScreenLibraryType(
    LibraryType
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'ILibraryTypeOrFolderSelection'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """Represents a library type made from a screen"""

    pass

class ScreenLibraryTypeVersion(
    LibraryTypeVersion
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """Represents a library type version made from a screen"""

    pass

class ScreenOverview(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Editor for elements in the overview"""

    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: ScreenOverview) -> IEngineeringObject
        """
        ...
    def Export(self, path, exportOptions):
        """
        Export(self: ScreenOverview, path: FileInfo, exportOptions: ExportOptions)

            Simatic ML export of a screen overview

            path: Path to the Simatic ML file

            exportOptions: Option to use for export (default, readonly, etc.)
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: ScreenOverview) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: ScreenOverview) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class ScreenPopup(
    IEngineeringObject, IMasterCopySource, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Pop-up screen"""

    @property
    def Name(self):
        """
        Gets or sets the screen name.

        Get: Name(self: ScreenPopup) -> str
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: ScreenPopup) -> IEngineeringObject
        """
        ...
    def Delete(self):
        """
        Delete(self: ScreenPopup)

            Deletes this instance.
        """
        ...
    def Export(self, path, exportOptions):
        """
        Export(self: ScreenPopup, path: FileInfo, exportOptions: ExportOptions)

            Common export

            path: Path to the Simatic ML file

            exportOptions: Determines whether the default values are exported or not
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: ScreenPopup) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: ScreenPopup) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class ScreenPopupComposition(
    IEngineeringComposition, IInternalCompositionAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """Composition of popup screens."""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: ScreenPopupComposition) -> IEngineeringObject
        """
        ...
    def CreateFrom(self, sourceMasterCopy):
        """
        CreateFrom(self: ScreenPopupComposition, sourceMasterCopy: MasterCopy) -> ScreenPopup

            Create ScreenPopup from MasterCopy

            sourceMasterCopy: The source master copy

            Returns: Siemens.Engineering.Hmi.Screen.ScreenPopup
        """
        ...
    def Find(self, name):
        """
        Find(self: ScreenPopupComposition, name: str) -> ScreenPopup

            Finds a given screen popup

            name: Name to find

            Returns: Siemens.Engineering.Hmi.Screen.ScreenPopup
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: ScreenPopupComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def Import(self, path, importOptions):
        """
        Import(self: ScreenPopupComposition, path: FileInfo, importOptions: ImportOptions) -> IList[ScreenPopup]

            Import Action

            path: Path to the Simatic ML file

            importOptions: Options to use for the Import

            Returns: System.Collections.Generic.IList<Siemens.Engineering.Hmi.Screen.ScreenPopup>
        """
        ...
    def ToString(self):
        """
        ToString(self: ScreenPopupComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[ScreenPopup](enumerable:  value: ScreenPopup) -> bool"""
        ...
    def __ne__(self, *args): ...

class ScreenPopupFolder(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Folder containing screen popups"""

    @property
    def Folders(self):
        """
        Composition of screen popup user folders

        Get: Folders(self: ScreenPopupFolder) -> ScreenPopupUserFolderComposition
        """
        ...
    @property
    def Name(self):
        """
        The name of the screen popup folder

        Get: Name(self: ScreenPopupFolder) -> str
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: ScreenPopupFolder) -> IEngineeringObject
        """
        ...
    @property
    def ScreenPopups(self):
        """
        Composition of screen popups

        Get: ScreenPopups(self: ScreenPopupFolder) -> ScreenPopupComposition
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: ScreenPopupFolder) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: ScreenPopupFolder) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class ScreenPopupSystemFolder(
    ScreenPopupFolder, IMasterCopyTarget
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """System folder containing screen popups"""

    pass

class ScreenPopupUserFolder(
    ScreenPopupFolder, IMasterCopySource, IMasterCopyTarget
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """User folder containing screen popups"""

    def Delete(self):
        """
        Delete(self: ScreenPopupUserFolder)

            Deletes this instance.
        """
        ...

class ScreenPopupUserFolderComposition(
    IEngineeringComposition, IInternalCompositionAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """Composition of ScreenPopupUserFolders"""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: ScreenPopupUserFolderComposition) -> IEngineeringObject
        """
        ...
    def Find(self, name):
        """
        Find(self: ScreenPopupUserFolderComposition, name: str) -> ScreenPopupUserFolder

            Finds a given screen popup user folder

            name: Name to find

            Returns: Siemens.Engineering.Hmi.Screen.ScreenPopupUserFolder
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: ScreenPopupUserFolderComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: ScreenPopupUserFolderComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[ScreenPopupUserFolder](enumerable:  value: ScreenPopupUserFolder) -> bool"""
        ...
    def __ne__(self, *args): ...

class ScreenSlidein(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Slide-In screen"""

    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: ScreenSlidein) -> IEngineeringObject
        """
        ...
    @property
    def SlideinType(self):
        """
        Type of a Slide-In screen.

        Get: SlideinType(self: ScreenSlidein) -> SlideinType
        """
        ...
    def Export(self, path, exportOptions):
        """
        Export(self: ScreenSlidein, path: FileInfo, exportOptions: ExportOptions)

            Common export

            path: Path to the Simatic ML file

            exportOptions: Determines whether the default values are exported or not
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: ScreenSlidein) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: ScreenSlidein) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class ScreenSlideinComposition(
    IEngineeringComposition, IInternalCompositionAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """Composition of slidein screens."""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: ScreenSlideinComposition) -> IEngineeringObject
        """
        ...
    def Find(self, slideinType):
        """
        Find(self: ScreenSlideinComposition, slideinType: SlideinType) -> ScreenSlidein

            Find a slidein screen.

            slideinType: Slidein to find

            Returns: Siemens.Engineering.Hmi.Screen.ScreenSlidein
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: ScreenSlideinComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def Import(self, path, importOptions):
        """
        Import(self: ScreenSlideinComposition, path: FileInfo, importOptions: ImportOptions) -> IList[ScreenSlidein]

            Import Action

            path: Path to the Simatic ML file

            importOptions: Options to use for the Import

            Returns: System.Collections.Generic.IList<Siemens.Engineering.Hmi.Screen.ScreenSlidein>
        """
        ...
    def ToString(self):
        """
        ToString(self: ScreenSlideinComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[ScreenSlidein](enumerable:  value: ScreenSlidein) -> bool"""
        ...
    def __ne__(self, *args): ...

class ScreenSlideinSystemFolder(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Folder for slide-in screens"""

    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: ScreenSlideinSystemFolder) -> IEngineeringObject
        """
        ...
    @property
    def ScreenSlideins(self):
        """
        Returns a collection of slide-in screens in that folder.

        Get: ScreenSlideins(self: ScreenSlideinSystemFolder) -> ScreenSlideinComposition
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: ScreenSlideinSystemFolder) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: ScreenSlideinSystemFolder) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class ScreenSystemFolder(
    ScreenFolder, IMasterCopyTarget, ILibraryTypeInstantiationTarget
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """System folder containing screens"""

    pass

class ScreenTemplate(
    IEngineeringObject, IMasterCopySource, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Represents a screen template"""

    @property
    def Name(self):
        """
        The name of the screen template

        Get: Name(self: ScreenTemplate) -> str
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: ScreenTemplate) -> IEngineeringObject
        """
        ...
    def Delete(self):
        """
        Delete(self: ScreenTemplate)

            Deletes this instance.
        """
        ...
    def Export(self, path, exportOptions):
        """
        Export(self: ScreenTemplate, path: FileInfo, exportOptions: ExportOptions)

            Simatic ML export of a screen template

            path: Path to the Simatic ML file

            exportOptions: Option to use for export (default, readonly, etc.)
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: ScreenTemplate) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: ScreenTemplate) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class ScreenTemplateComposition(
    IEngineeringComposition, IInternalCompositionAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """Composition of ScreenTemplates"""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: ScreenTemplateComposition) -> IEngineeringObject
        """
        ...
    def CreateFrom(self, sourceMasterCopy):
        """
        CreateFrom(self: ScreenTemplateComposition, sourceMasterCopy: MasterCopy) -> ScreenTemplate

            Create ScreenTemplate from MasterCopy

            sourceMasterCopy: The source master copy

            Returns: Siemens.Engineering.Hmi.Screen.ScreenTemplate
        """
        ...
    def Find(self, name):
        """
        Find(self: ScreenTemplateComposition, name: str) -> ScreenTemplate

            Finds a given screen template

            name: Name to find

            Returns: Siemens.Engineering.Hmi.Screen.ScreenTemplate
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: ScreenTemplateComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def Import(self, path, importOptions):
        """
        Import(self: ScreenTemplateComposition, path: FileInfo, importOptions: ImportOptions) -> IList[ScreenTemplate]

            Simatic ML import of a screen template

            path: Path to the Simatic ML file

            importOptions: Options to use for Import

            Returns: System.Collections.Generic.IList<Siemens.Engineering.Hmi.Screen.ScreenTemplate>
        """
        ...
    def ToString(self):
        """
        ToString(self: ScreenTemplateComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[ScreenTemplate](enumerable:  value: ScreenTemplate) -> bool"""
        ...
    def __ne__(self, *args): ...

class ScreenTemplateFolder(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Folder containing screen templates"""

    @property
    def Folders(self):
        """
        Composition of screen template user folders

        Get: Folders(self: ScreenTemplateFolder) -> ScreenTemplateUserFolderComposition
        """
        ...
    @property
    def Name(self):
        """
        The name of the screen template folder

        Get: Name(self: ScreenTemplateFolder) -> str
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: ScreenTemplateFolder) -> IEngineeringObject
        """
        ...
    @property
    def ScreenTemplates(self):
        """
        Composition of screen templates

        Get: ScreenTemplates(self: ScreenTemplateFolder) -> ScreenTemplateComposition
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: ScreenTemplateFolder) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: ScreenTemplateFolder) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class ScreenTemplateSystemFolder(
    ScreenTemplateFolder, IMasterCopyTarget
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """System folder containing screen templates"""

    pass

class ScreenTemplateUserFolder(
    ScreenTemplateFolder, IMasterCopySource, IMasterCopyTarget
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """User folder containing screen templates"""

    def Delete(self):
        """
        Delete(self: ScreenTemplateUserFolder)

            Deletes this instance.
        """
        ...

class ScreenTemplateUserFolderComposition(
    IEngineeringComposition, IInternalCompositionAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """Composition of ScreenTemplateUserFolders"""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: ScreenTemplateUserFolderComposition) -> IEngineeringObject
        """
        ...
    def Find(self, name):
        """
        Find(self: ScreenTemplateUserFolderComposition, name: str) -> ScreenTemplateUserFolder

            Finds a given screen template user folder

            name: Name to find

            Returns: Siemens.Engineering.Hmi.Screen.ScreenTemplateUserFolder
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: ScreenTemplateUserFolderComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: ScreenTemplateUserFolderComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[ScreenTemplateUserFolder](enumerable:  value: ScreenTemplateUserFolder) -> bool"""
        ...
    def __ne__(self, *args): ...

class ScreenUserFolder(
    ScreenFolder, IMasterCopySource, IMasterCopyTarget, ILibraryTypeInstantiationTarget
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """User folder containing screens"""

    def Delete(self):
        """
        Delete(self: ScreenUserFolder)

            Deletes this instance.
        """
        ...

class ScreenUserFolderComposition(
    IEngineeringComposition, IInternalCompositionAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """Composition of ScreenUserFolders"""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: ScreenUserFolderComposition) -> IEngineeringObject
        """
        ...
    def Find(self, name):
        """
        Find(self: ScreenUserFolderComposition, name: str) -> ScreenUserFolder

            Finds a given screen user folder

            name: Name to find

            Returns: Siemens.Engineering.Hmi.Screen.ScreenUserFolder
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: ScreenUserFolderComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: ScreenUserFolderComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[ScreenUserFolder](enumerable:  value: ScreenUserFolder) -> bool"""
        ...
    def __ne__(self, *args): ...

class SlideinType(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Defines the available Slide-In screen types.

    enum SlideinType, values: Bottom (1), Left (2), Right (3), Top (0)
    """

    Bottom = None
    Left = None
    Right = None
    Top = None
    value__ = None

class StyleLibraryType(
    LibraryType
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'ILibraryTypeOrFolderSelection'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """Represents a library type made from a style"""

    pass

class StyleLibraryTypeVersion(
    LibraryTypeVersion
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """Represents a library type version made from a style"""

    pass

class StyleSheetLibraryType(
    LibraryType
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'ILibraryTypeOrFolderSelection'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """Represents a library type made from a style sheet"""

    pass

class StyleSheetLibraryTypeVersion(
    LibraryTypeVersion
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """Represents a library type version made from a style sheet"""

    pass

class VisibilityModes(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Defindes the VisibilityModes

    enum VisibilityModes, values: FadeOut (0), ShowAlways (1), ShowNever (2)
    """

    FadeOut = None
    ShowAlways = None
    ShowNever = None
    value__ = None
