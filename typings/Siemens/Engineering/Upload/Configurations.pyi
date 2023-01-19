# encoding: utf-8
# module Siemens.Engineering.Upload.Configurations calls itself Configurations
# from Siemens.Engineering, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

from Siemens.Engineering import IEngineeringObject
from System import Enum, IEquatable

class UploadConfiguration(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Upload configuration base class."""

    @property
    def Message(self):
        """
        Descriptions of this onfiguration

        Get: Message(self: UploadConfiguration) -> str
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: UploadConfiguration) -> IEngineeringObject
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: UploadConfiguration) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: UploadConfiguration) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class UploadPasswordConfiguration(
    UploadConfiguration
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """Upload password configuration."""

    def SetPassword(self, password):
        """
        SetPassword(self: UploadPasswordConfiguration, password: SecureString)

            Sets password

            password: Required password.
        """
        ...

class ModuleReadAccessPassword(
    UploadPasswordConfiguration
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """Enter a password to gain read access to the module"""

    pass

class ModuleWriteAccessPassword(
    UploadPasswordConfiguration
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """Enter a password to gain write access to the module"""

    pass

class PasswordReadAccess(
    UploadPasswordConfiguration
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """The PLC need a password for Readaccess."""

    pass

class UploadSelectionConfiguration(
    UploadConfiguration
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """Upload configuration that provides choices."""

    pass

class UploadMissingProducts(
    UploadSelectionConfiguration
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """The PLC contains additional data of missing products."""

    @property
    def CurrentSelection(self):
        """
        Current selection for this configuration.

        Get: CurrentSelection(self: UploadMissingProducts) -> UploadMissingProductsSelections

        Set: CurrentSelection(self: UploadMissingProducts) = value
        """
        ...

class UploadMissingProductsSelections(
    Enum
):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Available selections for UploadMissingProductsCategory configuration

    enum UploadMissingProductsSelections, values: NoAction (0), TryUpload (1)
    """

    NoAction = None
    TryUpload = None
    value__ = None
