# encoding: utf-8
# module Siemens.Engineering.Library.MasterCopies calls itself MasterCopies
# from Siemens.Engineering, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

from Siemens.Engineering import IEngineeringAssociation, IEngineeringComposition, IEngineeringObject
from System import Enum, IEquatable
from Siemens.Engineering.SW import ISoftwareCompareTarget

class IMasterCopySource:
    """A source item used to create a master copy"""

    pass

class IMasterCopyTarget:
    """Target for pasting a library master copy"""

    pass

class MasterCopy(
    IEngineeringObject, ISoftwareCompareTarget, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Represents a library master copy"""

    @property
    def Author(self):
        """
        Author of the master copy

        Get: Author(self: MasterCopy) -> str
        """
        ...
    @property
    def ContentDescriptions(self):
        """
        Content descriptions

        Get: ContentDescriptions(self: MasterCopy) -> MasterCopyContentDescriptionComposition
        """
        ...
    @property
    def CreationDate(self):
        """
        Creation date of this master copy

        Get: CreationDate(self: MasterCopy) -> DateTime
        """
        ...
    @property
    def Name(self) -> str:
        """
        The name of the MasterCopy

        Get: Name(self: MasterCopy) -> str

        Set: Name(self: MasterCopy) = value
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: MasterCopy) -> IEngineeringObject
        """
        ...
    def Delete(self):
        """
        Delete(self: MasterCopy)

            Deletes this instance.
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: MasterCopy) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: MasterCopy) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class MasterCopyAssociation(
    IEngineeringAssociation, IInternalAssociationAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalCollectionAccess'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>
    """Associated MasterCopies"""

    @property
    def Parent(self):
        """
        Gets the parent..

        Get: Parent(self: MasterCopyAssociation) -> IEngineeringObject
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: MasterCopyAssociation) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: MasterCopyAssociation) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[MasterCopy](enumerable:  value: MasterCopy) -> bool"""
        ...
    def __ne__(self, *args): ...

class MasterCopyComposition(
    IEngineeringComposition[MasterCopy], IInternalCompositionAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """Composition of MasterCopies"""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: MasterCopyComposition) -> IEngineeringObject
        """
        ...
    def CreateFrom(self, sourceMasterCopy):
        """
        CreateFrom(self: MasterCopyComposition, sourceMasterCopy: MasterCopy) -> MasterCopy

            Create from given Master Copy

            sourceMasterCopy: Source MasterCopy

            Returns: Siemens.Engineering.Library.MasterCopies.MasterCopy
        """
        ...
    def Find(self, name: str) -> MasterCopy:
        """
        Find(self: MasterCopyComposition, name: str) -> MasterCopy

            Finds a given MasterCopy

            name: Name to find

            Returns: Siemens.Engineering.Library.MasterCopies.MasterCopy
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: MasterCopyComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: MasterCopyComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[MasterCopy](enumerable:  value: MasterCopy) -> bool"""
        ...
    def __ne__(self, *args): ...

class MasterCopyContentDescription(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Master copy content description"""

    @property
    def ContentName(self):
        """
        name of master coy content

        Get: ContentName(self: MasterCopyContentDescription) -> str
        """
        ...
    @property
    def ContentType(self):
        """
        Type of master copy content

        Get: ContentType(self: MasterCopyContentDescription) -> Type
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: MasterCopyContentDescription) -> IEngineeringObject
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: MasterCopyContentDescription) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: MasterCopyContentDescription) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class MasterCopyContentDescriptionComposition(
    IEngineeringComposition, IInternalCompositionAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """Composition of master copy contents"""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: MasterCopyContentDescriptionComposition) -> IEngineeringObject
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: MasterCopyContentDescriptionComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: MasterCopyContentDescriptionComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[MasterCopyContentDescription](enumerable:  value: MasterCopyContentDescription) -> bool"""
        ...
    def __ne__(self, *args): ...

class MasterCopyFolder(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Folder containing Master Copies & Master Copy folders"""

    @property
    def Folders(self) -> MasterCopyUserFolderComposition:
        """
        Composition of MasterCopy user folders

        Get: Folders(self: MasterCopyFolder) -> MasterCopyUserFolderComposition
        """
        ...
    @property
    def MasterCopies(self) -> MasterCopyComposition:
        """
        Composition of MasterCopies

        Get: MasterCopies(self: MasterCopyFolder) -> MasterCopyComposition
        """
        ...
    @property
    def Name(self) -> str:
        """
        The name of the MasterCopy folder

        Get: Name(self: MasterCopyFolder) -> str
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: MasterCopyFolder) -> IEngineeringObject
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: MasterCopyFolder) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: MasterCopyFolder) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class MasterCopyMode(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    The list of possible scenarios supported by master copy 'copy' action parameterization

    enum MasterCopyMode, values: Rename (1), Replace (2), ThrowIfExists (0)
    """

    Rename = None
    Replace = None
    ThrowIfExists = None
    value__ = None

class MasterCopySystemFolder(
    MasterCopyFolder
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """System folder containing Master Copies & Master Copy folders"""

    pass

class MasterCopyUserFolder(
    MasterCopyFolder
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """User folder containing Master Copies & Master Copy folders"""

    def Delete(self):
        """
        Delete(self: MasterCopyUserFolder)

            Deletes this instance.
        """
        ...

class MasterCopyUserFolderComposition(
    IEngineeringComposition[MasterCopyUserFolder], IInternalCompositionAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """Composition of MasterCopyUserFolders"""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: MasterCopyUserFolderComposition) -> IEngineeringObject
        """
        ...
    def Find(self, name: str) -> MasterCopyUserFolder:
        """
        Find(self: MasterCopyUserFolderComposition, name: str) -> MasterCopyUserFolder

            Finds a given MasterCopy user folder

            name: Name to find

            Returns: Siemens.Engineering.Library.MasterCopies.MasterCopyUserFolder
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: MasterCopyUserFolderComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: MasterCopyUserFolderComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[MasterCopyUserFolder](enumerable:  value: MasterCopyUserFolder) -> bool"""
        ...
    def __ne__(self, *args): ...
