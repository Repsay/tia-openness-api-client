# encoding: utf-8
# module Siemens.Engineering.SW calls itself SW
# from Siemens.Engineering, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

from Siemens.Engineering import IEngineeringObject, IEngineeringService, IEngineeringServiceProvider
from Siemens.Engineering.Library.Types import IInstanceSearchScope, IUpdateProjectScope
from Siemens.Engineering.HW import Software
from System import Enum, IEquatable

from Siemens.Engineering.SW.Blocks import PlcBlockSystemGroup

class Fingerprint(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """fingerprint"""

    @property
    def Id(self):
        """
        ID of the fingerprint

        Get: Id(self: Fingerprint) -> FingerprintId
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: Fingerprint) -> IEngineeringObject
        """
        ...
    @property
    def Value(self):
        """
        fingerprint data

        Get: Value(self: Fingerprint) -> str
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: Fingerprint) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: Fingerprint) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class FingerprintId(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    fingerprint id

    enum FingerprintId, values: Alarms (5), Code (0), Comments (1), Events (8), Interface (2), LibraryType (3), Properties (10), Supervisions (6), TechnologyObject (7), Texts (4), TextualInterface (9)
    """

    Alarms = None
    Code = None
    Comments = None
    Events = None
    Interface = None
    LibraryType = None
    Properties = None
    Supervisions = None
    TechnologyObject = None
    Texts = None
    TextualInterface = None
    value__ = None

class FingerprintProvider(
    IEngineeringObject, IEngineeringService, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Provides fingerprints."""

    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: FingerprintProvider) -> IEngineeringObject
        """
        ...
    def GetFingerprints(self):
        """
        GetFingerprints(self: FingerprintProvider) -> IList[Fingerprint]

            Read Fingerprint

            Returns: System.Collections.Generic.IList<Siemens.Engineering.SW.Fingerprint>
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: FingerprintProvider) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: FingerprintProvider) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class ISoftwareCompareTarget:
    """Access to the controller in a compare scenario"""

    pass

class PlcChecksumProvider(
    IEngineeringObject, IEngineeringService, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Provides checksums."""

    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: PlcChecksumProvider) -> IEngineeringObject
        """
        ...
    @property
    def Software(self):
        """
        Software checksum

        Get: Software(self: PlcChecksumProvider) -> str
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: PlcChecksumProvider) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: PlcChecksumProvider) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class PlcSoftware(
    Software, IInstanceSearchScope, IUpdateProjectScope, ISoftwareCompareTarget, IEngineeringServiceProvider
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IServiceProvider'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """Represents the software components of a Plc"""

    @property
    def BlockGroup(self) -> PlcBlockSystemGroup:
        """Gets the Plc block system group"""
        ...
    @property
    def ExternalSourceGroup(self):
        """
        Gets the Plc external source system group

        Get: ExternalSourceGroup(self: PlcSoftware) -> PlcExternalSourceSystemGroup
        """
        ...
    @property
    def TagTableGroup(self):
        """
        Get the Plc tag table system group

        Get: TagTableGroup(self: PlcSoftware) -> PlcTagTableSystemGroup
        """
        ...
    @property
    def TechnologicalObjectGroup(self):
        """
        This system folder can contain technological objects

        Get: TechnologicalObjectGroup(self: PlcSoftware) -> TechnologicalInstanceDBGroup
        """
        ...
    @property
    def TypeGroup(self):
        """
        Gets Plc type system group

        Get: TypeGroup(self: PlcSoftware) -> PlcTypeSystemGroup
        """
        ...
    @property
    def WatchAndForceTableGroup(self):
        """
        Get the Plc watch table system group

        Get: WatchAndForceTableGroup(self: PlcSoftware) -> PlcWatchAndForceTableSystemGroup
        """
        ...
    def CompareTo(self, compareTarget):
        """
        CompareTo(self: PlcSoftware, compareTarget: ISoftwareCompareTarget) -> CompareResult

            Compare the PLC software to the given target

            compareTarget: The target to compare to the PLC software

            Returns: Siemens.Engineering.Compare.CompareResult
        """
        ...
    def CompareToOnline(self):
        """
        CompareToOnline(self: PlcSoftware) -> CompareResult

            Compare the PLC software to the online target

            Returns: Siemens.Engineering.Compare.CompareResult
        """
        ...

class SWImportOptions(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    The list of possible sw importoptions for Import

    enum (flags) SWImportOptions, values: IgnoreMissingReferencedObjects (2), IgnoreStructuralChanges (1), None (0)
    """

    IgnoreMissingReferencedObjects = None
    IgnoreStructuralChanges = None
    value__ = None

# variables with complex values
