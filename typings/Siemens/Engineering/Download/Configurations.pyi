# encoding: utf-8
# module Siemens.Engineering.Download.Configurations calls itself Configurations
# from Siemens.Engineering, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

from Siemens.Engineering import IEngineeringObject
from System import IEquatable, Enum

class DownloadConfiguration(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Donwload configuration base class."""

    @property
    def Message(self):
        """
        Descriptions of this onfiguration

        Get: Message(self: DownloadConfiguration) -> str
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: DownloadConfiguration) -> IEngineeringObject
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: DownloadConfiguration) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: DownloadConfiguration) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class DownloadSelectionConfiguration(
    DownloadConfiguration
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """Download configuration that provides choices."""

    pass

class ActiveTestCanBeAborted(
    DownloadSelectionConfiguration
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """Active test and commissioning functions could be canceled by loading to the device."""

    @property
    def CurrentSelection(self):
        """
        Current selection for this configuration.

        Get: CurrentSelection(self: ActiveTestCanBeAborted) -> ActiveTestCanBeAbortedSelections

        Set: CurrentSelection(self: ActiveTestCanBeAborted) = value
        """
        ...

class ActiveTestCanBeAbortedSelections(
    Enum
):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Available selections for ActiveTestCanBeAborted configuration

    enum ActiveTestCanBeAbortedSelections, values: AcceptAll (1), NoAction (0)
    """

    AcceptAll = None
    NoAction = None
    value__ = None

class AlarmTextLibrariesDownload(
    DownloadSelectionConfiguration
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """Download all alarm texts and text list texts"""

    @property
    def CurrentSelection(self):
        """
        Current selection for this configuration.

        Get: CurrentSelection(self: AlarmTextLibrariesDownload) -> AlarmTextLibrariesDownloadSelections

        Set: CurrentSelection(self: AlarmTextLibrariesDownload) = value
        """
        ...

class AlarmTextLibrariesDownloadSelections(
    Enum
):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Available selections for AlarmTextLibrariesDownload configuration

    enum AlarmTextLibrariesDownloadSelections, values: ConsistentDownload (0), NoAction (1)
    """

    ConsistentDownload = None
    NoAction = None
    value__ = None

class AllBlocksDownload(
    DownloadSelectionConfiguration
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """Download software to device"""

    @property
    def CurrentSelection(self):
        """
        Current selection for this configuration.

        Get: CurrentSelection(self: AllBlocksDownload) -> AllBlocksDownloadSelections

        Set: CurrentSelection(self: AllBlocksDownload) = value
        """
        ...

class AllBlocksDownloadSelections(
    Enum
):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Available selections for AllBlocksDownload configuration

    enum AllBlocksDownloadSelections, values: DownloadAllBlocks (0)
    """

    DownloadAllBlocks = None
    value__ = None

class DownloadPasswordConfiguration(
    DownloadConfiguration
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """Download password configuration."""

    def SetPassword(self, password):
        """
        SetPassword(self: DownloadPasswordConfiguration, password: SecureString)

            Sets password

            password: Required password.
        """
        ...

class BlockBindingPassword(
    DownloadPasswordConfiguration
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """Block binding password configuration"""

    pass

class DownloadCheckConfiguration(
    DownloadConfiguration
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """Download configuration that can be checked/unchecked."""

    @property
    def Checked(self):
        """
        Specifies if this configuration checked.

        Get: Checked(self: DownloadCheckConfiguration) -> bool

        Set: Checked(self: DownloadCheckConfiguration) = value
        """
        ...

class CheckBeforeDownload(
    DownloadCheckConfiguration
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """Checks before downloading to the device."""

    pass

class ConsistentBlocksDownload(
    DownloadSelectionConfiguration
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """Download software to device"""

    @property
    def CurrentSelection(self):
        """
        Current selection for this configuration.

        Get: CurrentSelection(self: ConsistentBlocksDownload) -> ConsistentBlocksDownloadSelections

        Set: CurrentSelection(self: ConsistentBlocksDownload) = value
        """
        ...

class ConsistentBlocksDownloadSelections(
    Enum
):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Available selections for ConsistentBlocksDownload configuration

    enum ConsistentBlocksDownloadSelections, values: ConsistentDownload (0)
    """

    ConsistentDownload = None
    value__ = None

class DifferentTargetConfiguration(
    DownloadSelectionConfiguration
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """Differences between configured and target modules (online)"""

    @property
    def CurrentSelection(self):
        """
        Current selection for this configuration.

        Get: CurrentSelection(self: DifferentTargetConfiguration) -> DifferentTargetConfigurationSelections

        Set: CurrentSelection(self: DifferentTargetConfiguration) = value
        """
        ...

class DifferentTargetConfigurationSelections(
    Enum
):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Available selections for DifferentTargetConfiguration configuration

    enum DifferentTargetConfigurationSelections, values: AcceptAll (1), NoAction (0)
    """

    AcceptAll = None
    NoAction = None
    value__ = None

class DowngradeTargetDevice(
    DownloadCheckConfiguration
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """Different data formats in online and offline project."""

    pass

class ExpandDownload(
    DownloadSelectionConfiguration
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """The download must be expanded beyond your selection."""

    @property
    def CurrentSelection(self):
        """
        Current selection for this configuration.

        Get: CurrentSelection(self: ExpandDownload) -> ExpandDownloadSelections

        Set: CurrentSelection(self: ExpandDownload) = value
        """
        ...

class ExpandDownloadSelections(
    Enum
):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Available selections for ExpandDownload configuration

    enum ExpandDownloadSelections, values: Download (1), NoAction (0)
    """

    Download = None
    NoAction = None
    value__ = None

class FitHmiComponents(
    DownloadCheckConfiguration
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """Components with a different version are installed on the target device."""

    pass

class InitializeMemory(
    DownloadSelectionConfiguration
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """The modules will initialize memory."""

    @property
    def CurrentSelection(self):
        """
        Current selection for this configuration.

        Get: CurrentSelection(self: InitializeMemory) -> InitializeMemorySelections

        Set: CurrentSelection(self: InitializeMemory) = value
        """
        ...

class InitializeMemorySelections(
    Enum
):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Available selections for InitializeMemory configuration

    enum InitializeMemorySelections, values: AcceptAll (1), NoAction (0)
    """

    AcceptAll = None
    NoAction = None
    value__ = None

class LoadIdentificationData(
    DownloadSelectionConfiguration
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """Load identification data to the PROFINET IO devices and their modules."""

    @property
    def CurrentSelection(self):
        """
        Current selection for this configuration.

        Get: CurrentSelection(self: LoadIdentificationData) -> LoadIdentificationDataSelections

        Set: CurrentSelection(self: LoadIdentificationData) = value
        """
        ...

class LoadIdentificationDataSelections(
    Enum
):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Available selections for LoadIdentificationData configuration

    enum LoadIdentificationDataSelections, values: LoadData (1), LoadNothing (0)
    """

    LoadData = None
    LoadNothing = None
    value__ = None

class ModuleReadAccessPassword(
    DownloadPasswordConfiguration
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """Enter a password to gain read access to the module."""

    pass

class ModuleWriteAccessPassword(
    DownloadPasswordConfiguration
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """Enter a password to gain write access to the module"""

    pass

class OverwriteHmiData(
    DownloadCheckConfiguration
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """Overwrite if object exists online?"""

    pass

class OverwriteSystemData(
    DownloadSelectionConfiguration
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """Delete and replace system data in target"""

    @property
    def CurrentSelection(self):
        """
        Current selection for this configuration.

        Get: CurrentSelection(self: OverwriteSystemData) -> OverwriteSystemDataSelections

        Set: CurrentSelection(self: OverwriteSystemData) = value
        """
        ...

class OverwriteSystemDataSelections(
    Enum
):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Available selections for OverwriteSystemData configuration

    enum OverwriteSystemDataSelections, values: NoAction (0), Overwrite (1)
    """

    NoAction = None
    Overwrite = None
    value__ = None

class OverwriteTargetLanguages(
    DownloadCheckConfiguration
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """There are differences between the settings for the project and the settings for PLC programming."""

    pass

class ProtectionLevelChanged(
    DownloadSelectionConfiguration
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """CPU protection will be changed to a lower level."""

    @property
    def CurrentSelection(self):
        """
        Current selection for this configuration.

        Get: CurrentSelection(self: ProtectionLevelChanged) -> ProtectionLevelChangedSelections

        Set: CurrentSelection(self: ProtectionLevelChanged) = value
        """
        ...

class ProtectionLevelChangedSelections(
    Enum
):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Available selections for ProtectionLevelChanged configuration

    enum ProtectionLevelChangedSelections, values: ContinueDownloading (1), NoChange (0)
    """

    ContinueDownloading = None
    NoChange = None
    value__ = None

class ResetModule(
    DownloadSelectionConfiguration
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """Reset module"""

    @property
    def CurrentSelection(self):
        """
        Current selection for this configuration.

        Get: CurrentSelection(self: ResetModule) -> ResetModuleSelections

        Set: CurrentSelection(self: ResetModule) = value
        """
        ...

class ResetModuleSelections(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Available selections for ResetModule configuration

    enum ResetModuleSelections, values: DeleteAll (1), NoAction (0)
    """

    DeleteAll = None
    NoAction = None
    value__ = None

class StartBackupModules(
    DownloadSelectionConfiguration
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """Start modules after downloading to device."""

    @property
    def CurrentSelection(self):
        """
        Current selection for this configuration.

        Get: CurrentSelection(self: StartBackupModules) -> StartBackupModulesSelections

        Set: CurrentSelection(self: StartBackupModules) = value
        """
        ...

class StartBackupModulesSelections(
    Enum
):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Available selections for StartBackupModules configuration

    enum StartBackupModulesSelections, values: NoAction (0), StartModule (2), SwitchToPrimaryCpu (1)
    """

    NoAction = None
    StartModule = None
    SwitchToPrimaryCpu = None
    value__ = None

class StartDriveDownloadCheckConfiguration(
    DownloadCheckConfiguration
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """Download check configuration for StartDrive"""

    pass

class StartModules(
    DownloadSelectionConfiguration
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """Start modules after downloading to device."""

    @property
    def CurrentSelection(self):
        """
        Current selection for this configuration.

        Get: CurrentSelection(self: StartModules) -> StartModulesSelections

        Set: CurrentSelection(self: StartModules) = value
        """
        ...

class StartModulesSelections(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Available selections for StartModules configuration

    enum StartModulesSelections, values: NoAction (0), StartModule (1)
    """

    NoAction = None
    StartModule = None
    value__ = None

class StopHSystem(
    DownloadSelectionConfiguration
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """The modules are stopped for downloading to device."""

    @property
    def CurrentSelection(self):
        """
        Current selection for this configuration.

        Get: CurrentSelection(self: StopHSystem) -> StopHSystemSelections

        Set: CurrentSelection(self: StopHSystem) = value
        """
        ...

class StopHSystemOrModule(
    DownloadSelectionConfiguration
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """The modules are stopped for downloading to device."""

    @property
    def CurrentSelection(self):
        """
        Current selection for this configuration.

        Get: CurrentSelection(self: StopHSystemOrModule) -> StopHSystemOrModuleSelections

        Set: CurrentSelection(self: StopHSystemOrModule) = value
        """
        ...

class StopHSystemOrModuleSelections(
    Enum
):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Available selections for StopHSystemOrModule configuration

    enum StopHSystemOrModuleSelections, values: NoAction (0), StopHSystem (1), StopModule (2)
    """

    NoAction = None
    StopHSystem = None
    StopModule = None
    value__ = None

class StopHSystemSelections(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Available selections for StopHSystem configuration

    enum StopHSystemSelections, values: NoAction (0), StopHSystem (1)
    """

    NoAction = None
    StopHSystem = None
    value__ = None

class StopModules(
    DownloadSelectionConfiguration
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """The modules are stopped for downloading to device."""

    @property
    def CurrentSelection(self):
        """
        Current selection for this configuration.

        Get: CurrentSelection(self: StopModules) -> StopModulesSelections

        Set: CurrentSelection(self: StopModules) = value
        """
        ...

class StopModulesSelections(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Available selections for StopModules configuration

    enum StopModulesSelections, values: NoAction (0), StopAll (1)
    """

    NoAction = None
    StopAll = None
    value__ = None

class SwitchBackupToPrimary(
    DownloadSelectionConfiguration
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """Start modules after downloading to device."""

    @property
    def CurrentSelection(self):
        """
        Current selection for this configuration.

        Get: CurrentSelection(self: SwitchBackupToPrimary) -> SwitchBackupToPrimarySelections

        Set: CurrentSelection(self: SwitchBackupToPrimary) = value
        """
        ...

class SwitchBackupToPrimarySelections(
    Enum
):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Available selections for SwitchBackupToPrimary configuration

    enum SwitchBackupToPrimarySelections, values: NoAction (0), SwitchToPrimaryCpu (1)
    """

    NoAction = None
    SwitchToPrimaryCpu = None
    value__ = None

class TurnOffSequence(
    DownloadCheckConfiguration
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """Turn off the sequence before loading."""

    pass

class UpgradeTargetDevice(
    DownloadCheckConfiguration
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """Different project versions in the configured device and target device (online)."""

    pass

class WaitOnReboot(
    DownloadSelectionConfiguration
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """Wait on reboot of a pc system."""

    @property
    def CurrentSelection(self):
        """
        Current selection for this configuation.

        Get: CurrentSelection(self: WaitOnReboot) -> WaitOnRebootSelections

        Set: CurrentSelection(self: WaitOnReboot) = value
        """
        ...

class WaitOnRebootSelections(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Available selections for WaitOnReboot configuration.

    enum WaitOnRebootSelections, values: NoAction (0), Wait (1)
    """

    NoAction = None
    value__ = None
    Wait = None
