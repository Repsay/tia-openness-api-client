# encoding: utf-8
# module Siemens.Engineering.Online calls itself Online
# from Siemens.Engineering, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

from Siemens.Engineering import IEngineeringObject, IEngineeringService
from System import Enum, IEquatable

class OnlineProvider(
    IEngineeringObject, IEngineeringService, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Service provider for online behaviors"""

    @property
    def Configuration(self):
        """
        Gets the connection configuration

        Get: Configuration(self: OnlineProvider) -> ConnectionConfiguration
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: OnlineProvider) -> IEngineeringObject
        """
        ...
    @property
    def State(self):
        """
        Check the Online state.

        Get: State(self: OnlineProvider) -> OnlineState
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: OnlineProvider) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def GoOffline(self):
        """
        GoOffline(self: OnlineProvider)

            Command to go offline
        """
        ...
    def GoOnline(self):
        """
        GoOnline(self: OnlineProvider) -> OnlineState

            Command to go online

            Returns: Siemens.Engineering.Online.OnlineState
        """
        ...
    def ToString(self):
        """
        ToString(self: OnlineProvider) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class OnlineState(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    The list of possible online states

    enum OnlineState, values: Connecting (1), Disconnecting (6), Incompatible (3), NotReachable (4), Offline (0), Online (2), Protected (5)
    """

    Connecting = None
    Disconnecting = None
    Incompatible = None
    NotReachable = None
    Offline = None
    Online = None
    Protected = None
    value__ = None

class RHOnlineProvider(
    IEngineeringService, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>
    """Service provides online functionality for R/H systems"""

    @property
    def BackupState(self):
        """
        Check the Online state of the Backup PLC.

        Get: BackupState(self: RHOnlineProvider) -> OnlineState
        """
        ...
    @property
    def Configuration(self):
        """
        Gets the connection configuration

        Get: Configuration(self: RHOnlineProvider) -> ConnectionConfiguration
        """
        ...
    @property
    def PrimaryState(self):
        """
        Check the Online state of the Primary PLC.

        Get: PrimaryState(self: RHOnlineProvider) -> OnlineState
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: RHOnlineProvider) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def GoOffline(self):
        """
        GoOffline(self: RHOnlineProvider)

            Command to go offline
        """
        ...
    def GoOnlineToBackup(self):
        """
        GoOnlineToBackup(self: RHOnlineProvider) -> OnlineState

            Command to go online to the backup PLC

            Returns: Siemens.Engineering.Online.OnlineState
        """
        ...
    def GoOnlineToPrimary(self):
        """
        GoOnlineToPrimary(self: RHOnlineProvider) -> OnlineState

            Command to go online to the primary Primary

            Returns: Siemens.Engineering.Online.OnlineState
        """
        ...
    def ToString(self):
        """
        ToString(self: RHOnlineProvider) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...
