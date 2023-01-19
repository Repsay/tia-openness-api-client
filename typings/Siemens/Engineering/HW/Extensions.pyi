# encoding: utf-8
# module Siemens.Engineering.HW.Extensions calls itself Extensions
# from Siemens.Engineering, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

from Siemens.Engineering import IEngineeringObject
from System import IEquatable

class PlugLocation(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Information about a free slot."""

    @property
    def Label(self):
        """
        The label of the free slot.

        Get: Label(self: PlugLocation) -> str
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: PlugLocation) -> IEngineeringObject
        """
        ...
    @property
    def PositionNumber(self):
        """
        The position number of the free slot

        Get: PositionNumber(self: PlugLocation) -> int
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: PlugLocation) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: PlugLocation) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...
