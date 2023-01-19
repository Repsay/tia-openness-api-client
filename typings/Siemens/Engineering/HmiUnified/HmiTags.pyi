# encoding: utf-8
# module Siemens.Engineering.HmiUnified.HmiTags calls itself HmiTags
# from Siemens.Engineering, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

from Siemens.Engineering import IEngineeringComposition, IEngineeringObject
from Siemens.Engineering.HmiUnified.Common import IValidator
from System import Enum, IEquatable

class HmiAccessMode(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Hmi Tag Access Mode

    enum HmiAccessMode, values: AbsoluteAccess (1), None (0), SymbolicAccess (2)
    """

    AbsoluteAccess = None
    SymbolicAccess = None
    value__ = None

class HmiAcquisitionMode(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    AcquisitionMode of Hmi Tag

    enum HmiAcquisitionMode, values: CyclicContinuous (16), CyclicOnUse (13), None (0), OnDemand (12)
    """

    CyclicContinuous = None
    CyclicOnUse = None
    OnDemand = None
    value__ = None

class HmiLimitValueType(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Description for limit value type

    enum HmiLimitValueType, values: Constant (1), None (0), Tag (2)
    """

    Constant = None
    Tag = None
    value__ = None

class HmiSubstituteValue(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Description for substitute value"""

    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: HmiSubstituteValue) -> IEngineeringObject
        """
        ...
    @property
    def SubstituteValueUsage(self):
        """
        Get or set substitute value

        Get: SubstituteValueUsage(self: HmiSubstituteValue) -> HmiSubstituteValueUsage

        Set: SubstituteValueUsage(self: HmiSubstituteValue) = value
        """
        ...
    @property
    def Value(self):
        """
        Get and set substitute value

        Get: Value(self: HmiSubstituteValue) -> object

        Set: Value(self: HmiSubstituteValue) = value
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: HmiSubstituteValue) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: HmiSubstituteValue) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class HmiSubstituteValueUsage(
    Enum
):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Hmi Substitute Value Usage

    enum HmiSubstituteValueUsage, values: InvalidValue (1), InvalidValueOrRangeViolation (3), None (0), RangeViolation (2)
    """

    InvalidValue = None
    InvalidValueOrRangeViolation = None
    RangeViolation = None
    value__ = None

class HmiSystemTag(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Hmi system tag"""

    @property
    def DataType(self):
        """
        Data type of the system tag

        Get: DataType(self: HmiSystemTag) -> str
        """
        ...
    @property
    def Name(self):
        """
        Name of system tag

        Get: Name(self: HmiSystemTag) -> str
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: HmiSystemTag) -> IEngineeringObject
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: HmiSystemTag) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: HmiSystemTag) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class HmiSystemTagComposition(
    IEngineeringComposition, IInternalCompositionAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """Collection of hmi system tag"""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: HmiSystemTagComposition) -> IEngineeringObject
        """
        ...
    def Find(self, name):
        """
        Find(self: HmiSystemTagComposition, name: str) -> HmiSystemTag

            Finds the hmi system tag based on the given name

            name: Hmi system tag name

            Returns: Siemens.Engineering.HmiUnified.HmiTags.HmiSystemTag
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: HmiSystemTagComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: HmiSystemTagComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[HmiSystemTag](enumerable:  value: HmiSystemTag) -> bool"""
        ...
    def __ne__(self, *args): ...

class HmiTag(
    IValidator, IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Hmi tag class"""

    @property
    def AccessMode(self):
        """
        The Hmi Tag Access Mode

        Get: AccessMode(self: HmiTag) -> HmiAccessMode

        Set: AccessMode(self: HmiTag) = value
        """
        ...
    @property
    def AcquisitionCycle(self):
        """
        The Acquisition cycle attribute

        Get: AcquisitionCycle(self: HmiTag) -> str

        Set: AcquisitionCycle(self: HmiTag) = value
        """
        ...
    @property
    def AcquisitionMode(self):
        """
        Hmi Tag AcquisitionMode

        Get: AcquisitionMode(self: HmiTag) -> HmiAcquisitionMode

        Set: AcquisitionMode(self: HmiTag) = value
        """
        ...
    @property
    def Address(self):
        """
        The Hmi Tag Address Attribute

        Get: Address(self: HmiTag) -> str

        Set: Address(self: HmiTag) = value
        """
        ...
    @property
    def Comment(self):
        """
        Get/set comment of tag

        Get: Comment(self: HmiTag) -> MultilingualText
        """
        ...
    @property
    def Connection(self):
        """
        The Hmi Connection

        Get: Connection(self: HmiTag) -> str

        Set: Connection(self: HmiTag) = value
        """
        ...
    @property
    def DataType(self):
        """
        DataType of the Tag

        Get: DataType(self: HmiTag) -> str

        Set: DataType(self: HmiTag) = value
        """
        ...
    @property
    def DisplayName(self):
        """
        Get/set display name of tag

        Get: DisplayName(self: HmiTag) -> MultilingualText
        """
        ...
    @property
    def InitialMaxValue(self):
        """
        Upper limit

        Get: InitialMaxValue(self: HmiTag) -> UpperRange
        """
        ...
    @property
    def InitialMinValue(self):
        """
        Lower limit

        Get: InitialMinValue(self: HmiTag) -> LowerRange
        """
        ...
    @property
    def InitialValue(self):
        """
        Initial value attribute

        Get: InitialValue(self: HmiTag) -> object

        Set: InitialValue(self: HmiTag) = value
        """
        ...
    @property
    def LoggingTags(self):
        """
        Represents

        Get: LoggingTags(self: HmiTag) -> HmiLoggingTagComposition
        """
        ...
    @property
    def MaxLength(self):
        """
        The hmi tag DataTypeLength

        Get: MaxLength(self: HmiTag) -> UInt32

        Set: MaxLength(self: HmiTag) = value
        """
        ...
    @property
    def Members(self):
        """
        Members of the composite Hmi tag

        Get: Members(self: HmiTag) -> HmiTagComposition
        """
        ...
    @property
    def Name(self):
        """
        Name of Hmi Tag

        Get: Name(self: HmiTag) -> str

        Set: Name(self: HmiTag) = value
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: HmiTag) -> IEngineeringObject
        """
        ...
    @property
    def Persistent(self):
        """
        The Persistence attribute

        Get: Persistent(self: HmiTag) -> bool

        Set: Persistent(self: HmiTag) = value
        """
        ...
    @property
    def PlcName(self):
        """
        The Plc Name Attribute

        Get: PlcName(self: HmiTag) -> str
        """
        ...
    @property
    def PlcTag(self):
        """
        The Plc Tag attribute

        Get: PlcTag(self: HmiTag) -> str

        Set: PlcTag(self: HmiTag) = value
        """
        ...
    @property
    def QualityCode(self):
        """
        The Hmi tag  QualityCode

        Get: QualityCode(self: HmiTag) -> bool

        Set: QualityCode(self: HmiTag) = value
        """
        ...
    @property
    def SubstituteValue(self):
        """
        The SubstituteValue

        Get: SubstituteValue(self: HmiTag) -> HmiSubstituteValue
        """
        ...
    @property
    def TagTableName(self):
        """
        The parent tag table

        Get: TagTableName(self: HmiTag) -> str
        """
        ...
    @property
    def TagType(self):
        """
        Indicates different types of hmi tag

        Get: TagType(self: HmiTag) -> HmiTagType
        """
        ...
    @property
    def TextReference(self):
        """
        Get/set text referenceof tag

        Get: TextReference(self: HmiTag) -> MultilingualText
        """
        ...
    @property
    def UpdateId(self):
        """
        The Update Id Attribute

        Get: UpdateId(self: HmiTag) -> UInt32

        Set: UpdateId(self: HmiTag) = value
        """
        ...
    @property
    def UpdateScope(self):
        """
        The Update Scope

        Get: UpdateScope(self: HmiTag) -> HmiUpdateScope

        Set: UpdateScope(self: HmiTag) = value
        """
        ...
    def Delete(self):
        """
        Delete(self: HmiTag)

            Deletes this instance.
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: HmiTag) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: HmiTag) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class HmiTagComposition(
    IEngineeringComposition, IInternalCompositionAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """Collection of hmi tags"""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: HmiTagComposition) -> IEngineeringObject
        """
        ...
    def Find(self, name):
        """
        Find(self: HmiTagComposition, name: str) -> HmiTag

            Finds the hmi tag based on the given name

            name: Hmi tag name

            Returns: Siemens.Engineering.HmiUnified.HmiTags.HmiTag
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: HmiTagComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: HmiTagComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[HmiTag](enumerable:  value: HmiTag) -> bool"""
        ...
    def __ne__(self, *args): ...

class HmiTagTable(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Hmi tag tables"""

    @property
    def Name(self):
        """
        Name of HmitagTable

        Get: Name(self: HmiTagTable) -> str

        Set: Name(self: HmiTagTable) = value
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: HmiTagTable) -> IEngineeringObject
        """
        ...
    @property
    def Tags(self):
        """
        Hmi tag collection

        Get: Tags(self: HmiTagTable) -> HmiTagComposition
        """
        ...
    def Delete(self):
        """
        Delete(self: HmiTagTable)

            Deletes this instance.
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: HmiTagTable) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: HmiTagTable) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class HmiTagTableComposition(
    IEngineeringComposition, IInternalCompositionAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """HmitagTable composition"""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: HmiTagTableComposition) -> IEngineeringObject
        """
        ...
    def Find(self, name):
        """
        Find(self: HmiTagTableComposition, name: str) -> HmiTagTable

            Finding the given tagtable

            name: Name of hmi tagtable

            Returns: Siemens.Engineering.HmiUnified.HmiTags.HmiTagTable
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: HmiTagTableComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: HmiTagTableComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[HmiTagTable](enumerable:  value: HmiTagTable) -> bool"""
        ...
    def __ne__(self, *args): ...

class HmiTagType(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Indicates different types of hmi tag

    enum HmiTagType, values: Array (2), Simple (0), UDT (1)
    """

    Array = None
    Simple = None
    UDT = None
    value__ = None

class HmiUpdateScope(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    The hmi tag Update Scope

    enum HmiUpdateScope, values: ClientServerWide (1), LocalHmiDevice (2), None (0)
    """

    ClientServerWide = None
    LocalHmiDevice = None
    value__ = None

class Range(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """To set value range"""

    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: Range) -> IEngineeringObject
        """
        ...
    @property
    def Value(self):
        """
        Value of upper/lower

        Get: Value(self: Range) -> object

        Set: Value(self: Range) = value
        """
        ...
    @property
    def ValueType(self):
        """
        Get and set Vlaue type

        Get: ValueType(self: Range) -> HmiLimitValueType

        Set: ValueType(self: Range) = value
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: Range) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: Range) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class LowerRange(
    Range
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """Lower limit range"""

    pass

class UpperRange(
    Range
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """Range for limit high"""

    pass
