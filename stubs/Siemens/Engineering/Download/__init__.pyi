# encoding: utf-8
# module Siemens.Engineering.Download calls itself Download
# from Siemens.Engineering, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

from Siemens.Engineering import IEngineeringComposition, IEngineeringObject, IEngineeringService
from System import Enum, IEquatable, MulticastDelegate

class DownloadConfigurationDelegate(MulticastDelegate):  # skipped bases: <type 'ICloneable'>, <type 'ISerializable'>
    """DownloadConfigurationDelegate(object: object, method: IntPtr)"""

    def BeginInvoke(self, downloadConfiguration, callback, object):
        """BeginInvoke(self: DownloadConfigurationDelegate, downloadConfiguration: DownloadConfiguration, callback: AsyncCallback, object: object) -> IAsyncResult"""
        ...
    def EndInvoke(self, result):
        """EndInvoke(self: DownloadConfigurationDelegate, result: IAsyncResult)"""
        ...
    def Invoke(self, downloadConfiguration):
        """Invoke(self: DownloadConfigurationDelegate, downloadConfiguration: DownloadConfiguration)"""
        ...

class DownloadOptions(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    The list of possible download options

    enum (flags) DownloadOptions, values: Hardware (1), None (0), Software (2)
    """

    Hardware = None
    Software = None
    value__ = None

class DownloadProvider(
    IEngineeringObject, IEngineeringService, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Service provides download functionality"""

    @property
    def Configuration(self):
        """
        Connection Configuration.

        Get: Configuration(self: DownloadProvider) -> ConnectionConfiguration
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: DownloadProvider) -> IEngineeringObject
        """
        ...
    def Download(
        self, configuration, preDownloadConfigurationDelegate, postDownloadConfigurationDelegate, downloadOptions
    ):
        """
        Download(self: DownloadProvider, configuration: IConfiguration, preDownloadConfigurationDelegate: DownloadConfigurationDelegate, postDownloadConfigurationDelegate: DownloadConfigurationDelegate, downloadOptions: DownloadOptions) -> DownloadResult

            Downloads hardware and software to the device

            configuration: Connection cofiguration path to a device.

            preDownloadConfigurationDelegate: This delegate will be called for each configuration before the download.

            postDownloadConfigurationDelegate: This delegate will be called for each configuration after the download.

            downloadOptions: Download options

            Returns: Siemens.Engineering.Download.DownloadResult
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: DownloadProvider) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: DownloadProvider) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class DownloadResult(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """The results of a download"""

    @property
    def ErrorCount(self):
        """
        Number of errors in a given download scenario

        Get: ErrorCount(self: DownloadResult) -> int
        """
        ...
    @property
    def Messages(self):
        """
        Collection of output messages for the result of a given download scenario.

        Get: Messages(self: DownloadResult) -> DownloadResultMessageComposition
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: DownloadResult) -> IEngineeringObject
        """
        ...
    @property
    def State(self):
        """
        Final state of a given compile scenario

        Get: State(self: DownloadResult) -> DownloadResultState
        """
        ...
    @property
    def WarningCount(self):
        """
        Number of warnings in a given download scenario

        Get: WarningCount(self: DownloadResult) -> int
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: DownloadResult) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: DownloadResult) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class DownloadResultMessage(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Download result message"""

    @property
    def DateTime(self):
        """
        Date and time in a download message

        Get: DateTime(self: DownloadResultMessage) -> DateTime
        """
        ...
    @property
    def ErrorCount(self):
        """
        Number of errors in a download message

        Get: ErrorCount(self: DownloadResultMessage) -> int
        """
        ...
    @property
    def Message(self):
        """
        Description or content of a download message

        Get: Message(self: DownloadResultMessage) -> str
        """
        ...
    @property
    def Messages(self):
        """
        Access to the download messages for a given download scenario

        Get: Messages(self: DownloadResultMessage) -> DownloadResultMessageComposition
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: DownloadResultMessage) -> IEngineeringObject
        """
        ...
    @property
    def State(self):
        """
        Final state in a download message

        Get: State(self: DownloadResultMessage) -> DownloadResultState
        """
        ...
    @property
    def WarningCount(self):
        """
        Number of warnings in a download message

        Get: WarningCount(self: DownloadResultMessage) -> int
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: DownloadResultMessage) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: DownloadResultMessage) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class DownloadResultMessageComposition(
    IEngineeringComposition, IInternalCompositionAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """Composition of download result messages."""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: DownloadResultMessageComposition) -> IEngineeringObject
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: DownloadResultMessageComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: DownloadResultMessageComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[DownloadResultMessage](enumerable:  value: DownloadResultMessage) -> bool"""
        ...
    def __ne__(self, *args): ...

class DownloadResultState(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    The list of possible compiler result options

    enum DownloadResultState, values: Error (3), Information (1), Success (0), Warning (2)
    """

    Error = None
    Information = None
    Success = None
    value__ = None
    Warning = None

class RHDownloadProvider(
    IEngineeringService, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>
    """Service provides download functionality for R/H systems"""

    @property
    def Configuration(self):
        """
        Connection Configuration.

        Get: Configuration(self: RHDownloadProvider) -> ConnectionConfiguration
        """
        ...
    def DownloadToBackup(
        self, configuration, preDownloadConfigurationDelegate, postDownloadConfigurationDelegate, downloadOptions
    ):
        """
        DownloadToBackup(self: RHDownloadProvider, configuration: IConfiguration, preDownloadConfigurationDelegate: DownloadConfigurationDelegate, postDownloadConfigurationDelegate: DownloadConfigurationDelegate, downloadOptions: DownloadOptions) -> DownloadResult

            Downloads hardware and software to the backup device

            configuration: Connection cofiguration path to a device.

            preDownloadConfigurationDelegate: This delegate will be called for each configuration before the download.

            postDownloadConfigurationDelegate: This delegate will be called for each configuration after the download.

            downloadOptions: Download options

            Returns: Siemens.Engineering.Download.DownloadResult
        """
        ...
    def DownloadToPrimary(
        self, configuration, preDownloadConfigurationDelegate, postDownloadConfigurationDelegate, downloadOptions
    ):
        """
        DownloadToPrimary(self: RHDownloadProvider, configuration: IConfiguration, preDownloadConfigurationDelegate: DownloadConfigurationDelegate, postDownloadConfigurationDelegate: DownloadConfigurationDelegate, downloadOptions: DownloadOptions) -> DownloadResult

            Downloads hardware and software to the primary device

            configuration: Connection cofiguration path to a device.

            preDownloadConfigurationDelegate: This delegate will be called for each configuration before the download.

            postDownloadConfigurationDelegate: This delegate will be called for each configuration after the download.

            downloadOptions: Download options

            Returns: Siemens.Engineering.Download.DownloadResult
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: RHDownloadProvider) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: RHDownloadProvider) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

# variables with complex values
