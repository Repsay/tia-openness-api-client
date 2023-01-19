# encoding: utf-8
# module Siemens.Engineering.Compiler calls itself Compiler
# from Siemens.Engineering, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

from Siemens.Engineering import IEngineeringComposition, IEngineeringObject, IEngineeringService
from System import Enum, IEquatable

class CompilerResult(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """The results of a compilation"""

    @property
    def ErrorCount(self):
        """
        Number of errors in a given compile scenario

        Get: ErrorCount(self: CompilerResult) -> int
        """
        ...
    @property
    def Messages(self):
        """
        Collection of output messages for the result of a given compile scenario

        Get: Messages(self: CompilerResult) -> CompilerResultMessageComposition
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: CompilerResult) -> IEngineeringObject
        """
        ...
    @property
    def State(self):
        """
        Final state of a given compile scenario

        Get: State(self: CompilerResult) -> CompilerResultState
        """
        ...
    @property
    def WarningCount(self):
        """
        Number of warnings in a given compile scenario

        Get: WarningCount(self: CompilerResult) -> int
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: CompilerResult) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: CompilerResult) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class CompilerResultMessage(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Compilation results message"""

    @property
    def DateTime(self):
        """
        Date and time in a compiler message

        Get: DateTime(self: CompilerResultMessage) -> DateTime
        """
        ...
    @property
    def Description(self):
        """
        Description or content of a compiler message

        Get: Description(self: CompilerResultMessage) -> str
        """
        ...
    @property
    def ErrorCount(self):
        """
        Number of errors in a compiler message

        Get: ErrorCount(self: CompilerResultMessage) -> int
        """
        ...
    @property
    def Messages(self):
        """
        Access to the compiler messages for a given compile scenario

        Get: Messages(self: CompilerResultMessage) -> CompilerResultMessageComposition
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: CompilerResultMessage) -> IEngineeringObject
        """
        ...
    @property
    def Path(self):
        """
        Path to a compiler message

        Get: Path(self: CompilerResultMessage) -> str
        """
        ...
    @property
    def State(self):
        """
        Final state in a compiler message

        Get: State(self: CompilerResultMessage) -> CompilerResultState
        """
        ...
    @property
    def WarningCount(self):
        """
        Number of warnings in a compiler message

        Get: WarningCount(self: CompilerResultMessage) -> int
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: CompilerResultMessage) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: CompilerResultMessage) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class CompilerResultMessageComposition(
    IEngineeringComposition, IInternalCompositionAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """Composition of CompareResultMessages"""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: CompilerResultMessageComposition) -> IEngineeringObject
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: CompilerResultMessageComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: CompilerResultMessageComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[CompilerResultMessage](enumerable:  value: CompilerResultMessage) -> bool"""
        ...
    def __ne__(self, *args): ...

class CompilerResultState(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    The list of possible compiler result options

    enum CompilerResultState, values: Error (3), Information (1), Success (0), Warning (2)
    """

    Error = None
    Information = None
    Success = None
    value__ = None
    Warning = None

class ICompilable(IEngineeringService):
    """An interface indication that the item supports compilation"""

    def Compile(self) -> CompilerResult:
        """Compiles the item

        Returns:
            CompilerResult: The result of the compilation
        """
        ...
