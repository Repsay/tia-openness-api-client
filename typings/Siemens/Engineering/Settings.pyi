# encoding: utf-8
# module Siemens.Engineering.Settings calls itself Settings
# from Siemens.Engineering, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

from Siemens.Engineering import IEngineeringComposition, IEngineeringObject
from System import IEquatable

class TiaPortalSetting(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Represents a TiaPortal setting."""

    @property
    def Name(self):
        """
        Represents the name of a TiaPortalSetting.

        Get: Name(self: TiaPortalSetting) -> str

        Set: Name(self: TiaPortalSetting) = value
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: TiaPortalSetting) -> IEngineeringObject
        """
        ...
    @property
    def Value(self):
        """
        Represents the value of a TiaPortalSetting.

        Get: Value(self: TiaPortalSetting) -> object

        Set: Value(self: TiaPortalSetting) = value
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: TiaPortalSetting) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: TiaPortalSetting) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class TiaPortalSettingComposition(
    IEngineeringComposition, IInternalCompositionAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """Represents a composition of TiaPortalSettings."""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: TiaPortalSettingComposition) -> IEngineeringObject
        """
        ...
    def Find(self, name):
        """
        Find(self: TiaPortalSettingComposition, name: str) -> TiaPortalSetting

            Returns the TiaPortalSetting with the matching name.

            name: The name of the TiaPortalSetting to find.

            Returns: Siemens.Engineering.Settings.TiaPortalSetting
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: TiaPortalSettingComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: TiaPortalSettingComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[TiaPortalSetting](enumerable:  value: TiaPortalSetting) -> bool"""
        ...
    def __ne__(self, *args): ...

class TiaPortalSettingsFolder(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Represents a TiaPortal settings folder"""

    @property
    def Folders(self):
        """
        Composition of TiaPortalSettingsFolders

        Get: Folders(self: TiaPortalSettingsFolder) -> TiaPortalSettingsFolderComposition
        """
        ...
    @property
    def Name(self):
        """
        Represents the name of a TiaPortalSettingsFolder.

        Get: Name(self: TiaPortalSettingsFolder) -> str
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: TiaPortalSettingsFolder) -> IEngineeringObject
        """
        ...
    @property
    def Settings(self):
        """
        Composition of TiaPortalSettings

        Get: Settings(self: TiaPortalSettingsFolder) -> TiaPortalSettingComposition
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: TiaPortalSettingsFolder) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: TiaPortalSettingsFolder) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class TiaPortalSettingsFolderComposition(
    IEngineeringComposition, IInternalCompositionAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """Composition of TiaPortalSettingsFolders"""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: TiaPortalSettingsFolderComposition) -> IEngineeringObject
        """
        ...
    def Find(self, name):
        """
        Find(self: TiaPortalSettingsFolderComposition, name: str) -> TiaPortalSettingsFolder

            Returns the TiaPortalSettingsFolder with the matching name.

            name: The name of the TiaPortalSettingsFolder to find.

            Returns: Siemens.Engineering.Settings.TiaPortalSettingsFolder
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: TiaPortalSettingsFolderComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: TiaPortalSettingsFolderComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[TiaPortalSettingsFolder](enumerable:  value: TiaPortalSettingsFolder) -> bool"""
        ...
    def __ne__(self, *args): ...
