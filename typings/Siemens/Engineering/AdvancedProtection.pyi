# encoding: utf-8
# module Siemens.Engineering.AdvancedProtection calls itself AdvancedProtection
# from Siemens.Engineering, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

from Siemens.Engineering import IEngineeringService
from System import IEquatable
from System.Security import SecureString

class ProtectionProviderBase(
    IEngineeringService, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>
    """Defines the contract of a Protection Provider, should be used as the base class for client-specific ProtectionProviders"""

    def GetHashCode(self) -> int:
        """Returns a hash code for this instance.

        Returns:
            int: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def GetInvalidPasswordCharacters(self) -> str:
        """Returns a string containing all characters that are not allowed in a password.

        Returns:
            str: A string containing all characters that are not allowed in a password.
        """
        ...
    def Protect(self, newPassword: SecureString) -> None:
        """Sets protection for the underlying object

        Parameters:
            newPassword (SecureString): the password to protect the object with
        """
        ...
    def ToString(self) -> str:
        """Returns a System.String that represents the current System.Object.

        Returns:
            str: A System.String that represents the current System.Object.
        """
        ...
    def Unprotect(self, currentPassword: SecureString) -> None:
        """Removes protection from the underlying object

        Parameters:
            currentPassword (SecureString): the password the underlying object is currently protected with
        """
        ...
