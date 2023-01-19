# encoding: utf-8
# module Siemens.Engineering.HmiUnified.Common calls itself Common
# from Siemens.Engineering, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

from Siemens.Engineering import IEngineeringObject
from System import IEquatable

class IValidator:
    """Validates the object"""

    def Validate(self):
        """
        Validate(self: IValidator) -> IList[HmiValidationResult]

            Validates the object

            Returns: System.Collections.Generic.IList<Siemens.Engineering.HmiUnified.Common.HmiValidationResult>
        """
        ...

class HmiBase(
    IValidator, IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """This class hold the common properties of AlarmClass, AnalogAlarm, DiscretAlarm"""

    @property
    def Name(self):
        """
        Name of the object

        Get: Name(self: HmiBase) -> str

        Set: Name(self: HmiBase) = value
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: HmiBase) -> IEngineeringObject
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: HmiBase) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: HmiBase) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class HmiValidationResult(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Error object that notifies the errors associated with a particular property"""

    @property
    def Errors(self):
        """
        Errors associated with the property

        Get: Errors(self: HmiValidationResult) -> IEnumerable[str]
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: HmiValidationResult) -> IEngineeringObject
        """
        ...
    @property
    def PropertyName(self):
        """
        Name of the property

        Get: PropertyName(self: HmiValidationResult) -> str
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: HmiValidationResult) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: HmiValidationResult) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...
