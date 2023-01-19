# encoding: utf-8
# module Siemens.Engineering.Compare calls itself Compare
# from Siemens.Engineering, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

from Siemens.Engineering import IEngineeringComposition, IEngineeringObject
from System import Enum, IEquatable

class CompareResult(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Summary object that contains the result of a comparison"""

    @property
    def Parent(self) -> IEngineeringObject:
        """EOM parent of this object

        Returns:
            IEngineeringObject: EOM parent of this object
        """
        ...
    @property
    def RootElement(self) -> CompareResultElement:
        """Browse to the element containing the result of a given compare scenario

        Returns:
            CompareResultElement: Browse to the element containing the result of a given compare scenario
        """
        ...
    def GetHashCode(self) -> int:
        """Returns a hash code for this instance.

        Returns:
            int: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self) -> str:
        """Returns a System.String that represents the current System.Object.

        Returns:
            str: A System.String that represents the current System.Object.
        """
        ...

class CompareResultElement(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Compare results on an element"""

    @property
    def ComparisonResult(self) -> CompareResultState:
        """The result of a comparison

        Returns:
            CompareResultState: The result of a comparison
        """
        ...
    @property
    def DetailedInformation(self) -> str:
        """
        Information on the result of a given compare scenario

        Get: DetailedInformation(self: CompareResultElement) -> str
        """
        ...
    @property
    def Elements(self):
        """
        Browse to the collection of compare scenarios on a single element

        Get: Elements(self: CompareResultElement) -> CompareResultElementComposition
        """
        ...
    @property
    def LeftName(self):
        """
        Left side name of a compare scenario on a single element

        Get: LeftName(self: CompareResultElement) -> str
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: CompareResultElement) -> IEngineeringObject
        """
        ...
    @property
    def RightName(self):
        """
        Right side name of a compare scenario on a single element

        Get: RightName(self: CompareResultElement) -> str
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: CompareResultElement) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: CompareResultElement) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class CompareResultElementComposition(
    IEngineeringComposition, IInternalCompositionAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """Composition of CompareResultElements"""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: CompareResultElementComposition) -> IEngineeringObject
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: CompareResultElementComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: CompareResultElementComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[CompareResultElement](enumerable:  value: CompareResultElement) -> bool"""
        ...
    def __ne__(self, *args): ...

class CompareResultState(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    The list of possible states of a compare result

    enum CompareResultState, values: CompareIrrelevant (8), FolderContainsDifferencesOwnStateDifferent (2), FolderContentEqualOwnStateDifferent (3), FolderContentsDifferent (0), FolderContentsIdentical (1), LeftMissing (5), ObjectsDifferent (4), ObjectsIdentical (7), RightMissing (6)
    """

    CompareIrrelevant = None
    FolderContainsDifferencesOwnStateDifferent = None
    FolderContentEqualOwnStateDifferent = None
    FolderContentsDifferent = None
    FolderContentsIdentical = None
    LeftMissing = None
    ObjectsDifferent = None
    ObjectsIdentical = None
    RightMissing = None
    value__ = None
