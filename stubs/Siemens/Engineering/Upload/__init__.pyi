# encoding: utf-8
# module Siemens.Engineering.Upload calls itself Upload
# from Siemens.Engineering, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

from Siemens.Engineering import IEngineeringComposition, IEngineeringObject, IEngineeringService
from System import Enum, IEquatable, MulticastDelegate

class StationUploadProvider(
    IEngineeringObject, IEngineeringService, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Service provides station upload"""

    @property
    def Configuration(self):
        """
        Connection Configuration.

        Get: Configuration(self: StationUploadProvider) -> ConnectionConfiguration
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: StationUploadProvider) -> IEngineeringObject
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: StationUploadProvider) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def StationUpload(self, configurationAddress, uploadConfigurationDelegate):
        """
        StationUpload(self: StationUploadProvider, configurationAddress: ConfigurationAddress, uploadConfigurationDelegate: UploadConfigurationDelegate) -> UploadResult

            Service provides station upload functionality

            configurationAddress: Configuration address for station upload

            uploadConfigurationDelegate: Upload parameter

            Returns: Siemens.Engineering.Upload.UploadResult
        """
        ...
    def ToString(self):
        """
        ToString(self: StationUploadProvider) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class UploadConfigurationDelegate(MulticastDelegate):  # skipped bases: <type 'ICloneable'>, <type 'ISerializable'>
    """UploadConfigurationDelegate(object: object, method: IntPtr)"""

    def BeginInvoke(self, uploadConfiguration, callback, object):
        """BeginInvoke(self: UploadConfigurationDelegate, uploadConfiguration: UploadConfiguration, callback: AsyncCallback, object: object) -> IAsyncResult"""
        ...
    def EndInvoke(self, result):
        """EndInvoke(self: UploadConfigurationDelegate, result: IAsyncResult)"""
        ...
    def Invoke(self, uploadConfiguration):
        """Invoke(self: UploadConfigurationDelegate, uploadConfiguration: UploadConfiguration)"""
        ...

class UploadResult(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """The results of a Upload"""

    @property
    def ErrorCount(self):
        """
        Number of errors in a given Upload scenario

        Get: ErrorCount(self: UploadResult) -> int
        """
        ...
    @property
    def Messages(self):
        """
        Collection of output messages for the result of a given Upload scenario.

        Get: Messages(self: UploadResult) -> UploadResultMessageComposition
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: UploadResult) -> IEngineeringObject
        """
        ...
    @property
    def State(self):
        """
        Final state of a given compile scenario

        Get: State(self: UploadResult) -> UploadResultState
        """
        ...
    @property
    def UploadedStation(self):
        """
        The uploaded station if upload was successful.

        Get: UploadedStation(self: UploadResult) -> Device
        """
        ...
    @property
    def WarningCount(self):
        """
        Number of warnings in a given Upload scenario

        Get: WarningCount(self: UploadResult) -> int
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: UploadResult) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: UploadResult) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class UploadResultMessage(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Upload result message"""

    @property
    def DateTime(self):
        """
        Date and time in a Upload message

        Get: DateTime(self: UploadResultMessage) -> DateTime
        """
        ...
    @property
    def ErrorCount(self):
        """
        Number of errors in a Upload message

        Get: ErrorCount(self: UploadResultMessage) -> int
        """
        ...
    @property
    def Message(self):
        """
        Description or content of a Upload message

        Get: Message(self: UploadResultMessage) -> str
        """
        ...
    @property
    def Messages(self):
        """
        Access to the Upload messages for a given Upload scenario

        Get: Messages(self: UploadResultMessage) -> UploadResultMessageComposition
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: UploadResultMessage) -> IEngineeringObject
        """
        ...
    @property
    def State(self):
        """
        Final state in a Upload message

        Get: State(self: UploadResultMessage) -> UploadResultState
        """
        ...
    @property
    def WarningCount(self):
        """
        Number of warnings in a Upload message

        Get: WarningCount(self: UploadResultMessage) -> int
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: UploadResultMessage) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: UploadResultMessage) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class UploadResultMessageComposition(
    IEngineeringComposition, IInternalCompositionAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """Composition of Upload result messages."""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: UploadResultMessageComposition) -> IEngineeringObject
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: UploadResultMessageComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: UploadResultMessageComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[UploadResultMessage](enumerable:  value: UploadResultMessage) -> bool"""
        ...
    def __ne__(self, *args): ...

class UploadResultState(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    The list of possible compiler result options

    enum UploadResultState, values: Error (3), Information (1), Success (0), Warning (2)
    """

    Error = None
    Information = None
    Success = None
    value__ = None
    Warning = None

# variables with complex values
