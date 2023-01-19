# encoding: utf-8
# module Siemens.Engineering.SiVArc calls itself SiVArc
# from Siemens.Engineering, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

from Siemens.Engineering import IEngineeringComposition, IEngineeringObject, IEngineeringService
from System import Enum, IEquatable

class AlarmRule(IEngineeringObject, IInternalObjectAccess, IEquatable):  # type: ignore
    # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Represents alarm rule object"""
    @property
    def Comment(self):
        """
        Alarm rule comment

        Get: Comment(self: AlarmRule) -> str
        """
        ...
    @property
    def Condition(self):
        """
        Alarm rule condition

        Get: Condition(self: AlarmRule) -> str
        """
        ...
    @property
    def Enabled(self):
        """
        Checks whether alarm rule is selected

        Get: Enabled(self: AlarmRule) -> bool
        """
        ...
    @property
    def Name(self):
        """
        Alarm rule name

        Get: Name(self: AlarmRule) -> str
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: AlarmRule) -> IEngineeringObject
        """
        ...
    def Delete(self):
        """
        Delete(self: AlarmRule)

            Deletes this instance.
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: AlarmRule) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: AlarmRule) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class AlarmRuleComposition(
    IEngineeringComposition, IInternalCompositionAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """Collection of immediate alarm rules"""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: AlarmRuleComposition) -> IEngineeringObject
        """
        ...
    def CreateFrom(self, ruleMasterCopy, createOption=...):
        """
        CreateFrom(self: AlarmRuleComposition, ruleMasterCopy: MasterCopy) -> AlarmRule

            Copy alarm rule from library to project with default replace option

            ruleMasterCopy: Alarm rule master copy

            Returns: Siemens.Engineering.SiVArc.AlarmRule

        CreateFrom(self: AlarmRuleComposition, ruleMasterCopy: MasterCopy, createOption: CreateOptions) -> AlarmRule

            Copy alarm rule from library to project with create options

            ruleMasterCopy: Alarm rule master copy

            createOption: Create option

            Returns: Siemens.Engineering.SiVArc.AlarmRule
        """
        ...
    def Find(self, name):
        """
        Find(self: AlarmRuleComposition, name: str) -> AlarmRule

            Finds alarm rule based on name

            name: Alarm rule name

            Returns: Siemens.Engineering.SiVArc.AlarmRule
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: AlarmRuleComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: AlarmRuleComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[AlarmRule](enumerable:  value: AlarmRule) -> bool"""
        ...
    def __ne__(self, *args): ...

class AlarmRuleGroup(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Represents alarm rule group"""

    @property
    def Comment(self):
        """
        Alarm rule group comment

        Get: Comment(self: AlarmRuleGroup) -> str
        """
        ...
    @property
    def Condition(self):
        """
        Alarm rule group condition

        Get: Condition(self: AlarmRuleGroup) -> str
        """
        ...
    @property
    def Enabled(self):
        """
        Checks whether alarm rule group is selected

        Get: Enabled(self: AlarmRuleGroup) -> bool
        """
        ...
    @property
    def Groups(self):
        """
        Collection of immediate groups

        Get: Groups(self: AlarmRuleGroup) -> AlarmRuleGroupComposition
        """
        ...
    @property
    def Name(self):
        """
        Alarm rule group name

        Get: Name(self: AlarmRuleGroup) -> str
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: AlarmRuleGroup) -> IEngineeringObject
        """
        ...
    @property
    def Rules(self):
        """
        Collection of immediate rules

        Get: Rules(self: AlarmRuleGroup) -> AlarmRuleComposition
        """
        ...
    def Delete(self):
        """
        Delete(self: AlarmRuleGroup)

            Deletes this instance.
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: AlarmRuleGroup) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: AlarmRuleGroup) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class AlarmRuleGroupComposition(
    IEngineeringComposition, IInternalCompositionAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """Collection of immediate alarm rule groups"""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: AlarmRuleGroupComposition) -> IEngineeringObject
        """
        ...
    def CreateFrom(self, groupMasterCopy, createOption=...):
        """
        CreateFrom(self: AlarmRuleGroupComposition, groupMasterCopy: MasterCopy) -> AlarmRuleGroup

            Copy alarm rule group from library to project with default replace option

            groupMasterCopy: Alarm rule group master copy

            Returns: Siemens.Engineering.SiVArc.AlarmRuleGroup

        CreateFrom(self: AlarmRuleGroupComposition, groupMasterCopy: MasterCopy, createOption: CreateOptions) -> AlarmRuleGroup

            Copy alarm rule group from library to project with create options

            groupMasterCopy: Alarm rule group master copy

            createOption: Create option

            Returns: Siemens.Engineering.SiVArc.AlarmRuleGroup
        """
        ...
    def Find(self, name):
        """
        Find(self: AlarmRuleGroupComposition, name: str) -> AlarmRuleGroup

            Finds alarm rule group based on name

            name: Alarm rule group name

            Returns: Siemens.Engineering.SiVArc.AlarmRuleGroup
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: AlarmRuleGroupComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: AlarmRuleGroupComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[AlarmRuleGroup](enumerable:  value: AlarmRuleGroup) -> bool"""
        ...
    def __ne__(self, *args): ...

class AlarmRules(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Represents alarm rules editor"""

    @property
    def Groups(self):
        """
        Navigate to all immediate alarm rule groups

        Get: Groups(self: AlarmRules) -> AlarmRuleGroupComposition
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: AlarmRules) -> IEngineeringObject
        """
        ...
    @property
    def Rules(self):
        """
        Navigate to all immediate alarm rules

        Get: Rules(self: AlarmRules) -> AlarmRuleComposition
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: AlarmRules) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: AlarmRules) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class CopyRule(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Represents copy rule object"""

    @property
    def Comment(self):
        """
        Copy rule comment

        Get: Comment(self: CopyRule) -> str
        """
        ...
    @property
    def Enabled(self):
        """
        Checks whether copy rule is selected

        Get: Enabled(self: CopyRule) -> bool
        """
        ...
    @property
    def Name(self):
        """
        Copy rule name

        Get: Name(self: CopyRule) -> str
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: CopyRule) -> IEngineeringObject
        """
        ...
    def Delete(self):
        """
        Delete(self: CopyRule)

            Deletes this instance.
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: CopyRule) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: CopyRule) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class CopyRuleComposition(
    IEngineeringComposition, IInternalCompositionAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """Collection of immediate copy rules"""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: CopyRuleComposition) -> IEngineeringObject
        """
        ...
    def CreateFrom(self, ruleMasterCopy, createOption=...):
        """
        CreateFrom(self: CopyRuleComposition, ruleMasterCopy: MasterCopy) -> CopyRule

            Copy the copy rule from library to project with default replace option

            ruleMasterCopy: Copy rule master copy

            Returns: Siemens.Engineering.SiVArc.CopyRule

        CreateFrom(self: CopyRuleComposition, ruleMasterCopy: MasterCopy, createOption: CreateOptions) -> CopyRule

            Copy the copy rule from library to project with create options

            ruleMasterCopy: Copy rule master copy

            createOption: Create option

            Returns: Siemens.Engineering.SiVArc.CopyRule
        """
        ...
    def Find(self, name):
        """
        Find(self: CopyRuleComposition, name: str) -> CopyRule

            Finds copy rule based on name

            name: Copy rule name

            Returns: Siemens.Engineering.SiVArc.CopyRule
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: CopyRuleComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: CopyRuleComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[CopyRule](enumerable:  value: CopyRule) -> bool"""
        ...
    def __ne__(self, *args): ...

class CopyRuleGroup(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Represents copy rule group"""

    @property
    def Comment(self):
        """
        Copy rule group comment

        Get: Comment(self: CopyRuleGroup) -> str
        """
        ...
    @property
    def Enabled(self):
        """
        Checks whether copy rule group is selected

        Get: Enabled(self: CopyRuleGroup) -> bool
        """
        ...
    @property
    def Groups(self):
        """
        Collection of immediate groups

        Get: Groups(self: CopyRuleGroup) -> CopyRuleGroupComposition
        """
        ...
    @property
    def Name(self):
        """
        Copy rule group name

        Get: Name(self: CopyRuleGroup) -> str
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: CopyRuleGroup) -> IEngineeringObject
        """
        ...
    @property
    def Rules(self):
        """
        Collection of immediate rules

        Get: Rules(self: CopyRuleGroup) -> CopyRuleComposition
        """
        ...
    def Delete(self):
        """
        Delete(self: CopyRuleGroup)

            Deletes this instance.
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: CopyRuleGroup) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: CopyRuleGroup) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class CopyRuleGroupComposition(
    IEngineeringComposition, IInternalCompositionAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """Collection of immediate copy rule groups"""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: CopyRuleGroupComposition) -> IEngineeringObject
        """
        ...
    def CreateFrom(self, groupMasterCopy, createOption=...):
        """
        CreateFrom(self: CopyRuleGroupComposition, groupMasterCopy: MasterCopy) -> CopyRuleGroup

            Copy the copy rule group from library to project with default replace option

            groupMasterCopy: Copy rule group master copy

            Returns: Siemens.Engineering.SiVArc.CopyRuleGroup

        CreateFrom(self: CopyRuleGroupComposition, groupMasterCopy: MasterCopy, createOption: CreateOptions) -> CopyRuleGroup

            Copy the copy rule group from library to project with create options

            groupMasterCopy: Copy rule group master copy

            createOption: Create option

            Returns: Siemens.Engineering.SiVArc.CopyRuleGroup
        """
        ...
    def Find(self, name):
        """
        Find(self: CopyRuleGroupComposition, name: str) -> CopyRuleGroup

            Finds copy rule group based on name

            name: Copy rule group name

            Returns: Siemens.Engineering.SiVArc.CopyRuleGroup
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: CopyRuleGroupComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: CopyRuleGroupComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[CopyRuleGroup](enumerable:  value: CopyRuleGroup) -> bool"""
        ...
    def __ne__(self, *args): ...

class CopyRules(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Represents copy rules editor"""

    @property
    def Groups(self):
        """
        Navigate to all immediate copy rule groups

        Get: Groups(self: CopyRules) -> CopyRuleGroupComposition
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: CopyRules) -> IEngineeringObject
        """
        ...
    @property
    def Rules(self):
        """
        Navigate to all immediate copy rules

        Get: Rules(self: CopyRules) -> CopyRuleComposition
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: CopyRules) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: CopyRules) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class CreateOptions(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Indicates the kind of create options

    enum CreateOptions, values: Rename (1), Replace (0)
    """

    Rename = None
    Replace = None
    value__ = None

class GenerationOptions(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Indicates the kind of generation options

    enum (flags) GenerationOptions, values: AllTags (1), FullGeneration (4), None (0), UsedHmiTags (2)
    """

    AllTags = None
    FullGeneration = None
    UsedHmiTags = None
    value__ = None

class MessageType(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Message type

    enum MessageType, values: Error (0), Information (2), Warning (1)
    """

    Error = None
    Information = None
    value__ = None
    Warning = None

class ScreenRule(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Represents screen rule object"""

    @property
    def Comment(self):
        """
        Screen rule comment

        Get: Comment(self: ScreenRule) -> str
        """
        ...
    @property
    def Condition(self):
        """
        Screen rule condition

        Get: Condition(self: ScreenRule) -> str
        """
        ...
    @property
    def Enabled(self):
        """
        Checks whether screen rule is selected

        Get: Enabled(self: ScreenRule) -> bool
        """
        ...
    @property
    def Name(self):
        """
        Screen rule name

        Get: Name(self: ScreenRule) -> str
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: ScreenRule) -> IEngineeringObject
        """
        ...
    def Delete(self):
        """
        Delete(self: ScreenRule)

            Deletes this instance.
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: ScreenRule) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: ScreenRule) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class ScreenRuleComposition(
    IEngineeringComposition, IInternalCompositionAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """Collection of immediate screen rules"""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: ScreenRuleComposition) -> IEngineeringObject
        """
        ...
    def CreateFrom(self, ruleMasterCopy, createOption=...):
        """
        CreateFrom(self: ScreenRuleComposition, ruleMasterCopy: MasterCopy) -> ScreenRule

            Copy screen rule from library to project with default replace option

            ruleMasterCopy: Screen rule master copy

            Returns: Siemens.Engineering.SiVArc.ScreenRule

        CreateFrom(self: ScreenRuleComposition, ruleMasterCopy: MasterCopy, createOption: CreateOptions) -> ScreenRule

            Copy screen rule from library to project with create options

            ruleMasterCopy: Screen rule master copy

            createOption: Create option

            Returns: Siemens.Engineering.SiVArc.ScreenRule
        """
        ...
    def Find(self, name):
        """
        Find(self: ScreenRuleComposition, name: str) -> ScreenRule

            Finds screen rule based on name

            name: Screen rule name

            Returns: Siemens.Engineering.SiVArc.ScreenRule
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: ScreenRuleComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: ScreenRuleComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[ScreenRule](enumerable:  value: ScreenRule) -> bool"""
        ...
    def __ne__(self, *args): ...

class ScreenRuleGroup(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Represents screen rule group"""

    @property
    def Comment(self):
        """
        Screen rule group comment

        Get: Comment(self: ScreenRuleGroup) -> str
        """
        ...
    @property
    def Condition(self):
        """
        Screen rule group condition

        Get: Condition(self: ScreenRuleGroup) -> str
        """
        ...
    @property
    def Enabled(self):
        """
        Checks whether screen rule group is selected

        Get: Enabled(self: ScreenRuleGroup) -> bool
        """
        ...
    @property
    def Groups(self):
        """
        Collection of immediate groups

        Get: Groups(self: ScreenRuleGroup) -> ScreenRuleGroupComposition
        """
        ...
    @property
    def Name(self):
        """
        Screen rule group name

        Get: Name(self: ScreenRuleGroup) -> str
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: ScreenRuleGroup) -> IEngineeringObject
        """
        ...
    @property
    def Rules(self):
        """
        Collection of immediate rules

        Get: Rules(self: ScreenRuleGroup) -> ScreenRuleComposition
        """
        ...
    def Delete(self):
        """
        Delete(self: ScreenRuleGroup)

            Deletes this instance.
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: ScreenRuleGroup) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: ScreenRuleGroup) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class ScreenRuleGroupComposition(
    IEngineeringComposition, IInternalCompositionAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """Collection of immediate screen rule groups"""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: ScreenRuleGroupComposition) -> IEngineeringObject
        """
        ...
    def CreateFrom(self, groupMasterCopy, createOption=...):
        """
        CreateFrom(self: ScreenRuleGroupComposition, groupMasterCopy: MasterCopy) -> ScreenRuleGroup

            Copy screen rule group from library to project with default replace option

            groupMasterCopy: Screen rule group master copy

            Returns: Siemens.Engineering.SiVArc.ScreenRuleGroup

        CreateFrom(self: ScreenRuleGroupComposition, groupMasterCopy: MasterCopy, createOption: CreateOptions) -> ScreenRuleGroup

            Copy screen rule group from library to project with create options

            groupMasterCopy: Screen rule group master copy

            createOption: Create option

            Returns: Siemens.Engineering.SiVArc.ScreenRuleGroup
        """
        ...
    def Find(self, name):
        """
        Find(self: ScreenRuleGroupComposition, name: str) -> ScreenRuleGroup

            Finds screen rule group based on name

            name: Screen rule group name

            Returns: Siemens.Engineering.SiVArc.ScreenRuleGroup
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: ScreenRuleGroupComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: ScreenRuleGroupComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[ScreenRuleGroup](enumerable:  value: ScreenRuleGroup) -> bool"""
        ...
    def __ne__(self, *args): ...

class ScreenRules(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Represents screen rules editor"""

    @property
    def Groups(self):
        """
        Navigate to all immediate screen rule groups

        Get: Groups(self: ScreenRules) -> ScreenRuleGroupComposition
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: ScreenRules) -> IEngineeringObject
        """
        ...
    @property
    def Rules(self):
        """
        Navigate to all immediate screen rules

        Get: Rules(self: ScreenRules) -> ScreenRuleComposition
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: ScreenRules) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: ScreenRules) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class Sivarc(
    IEngineeringObject, IEngineeringService, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Represents SiVArc folder"""

    @property
    def AlarmRules(self):
        """
        Alarm rules editor

        Get: AlarmRules(self: Sivarc) -> AlarmRules
        """
        ...
    @property
    def CopyRules(self):
        """
        Copy rules editor

        Get: CopyRules(self: Sivarc) -> CopyRules
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: Sivarc) -> IEngineeringObject
        """
        ...
    @property
    def ScreenRules(self):
        """
        Screen rules editor

        Get: ScreenRules(self: Sivarc) -> ScreenRules
        """
        ...
    @property
    def TagRules(self):
        """
        Tag rules editor

        Get: TagRules(self: Sivarc) -> TagRules
        """
        ...
    @property
    def TextlistRules(self):
        """
        Textlist rules editor

        Get: TextlistRules(self: Sivarc) -> TextlistRules
        """
        ...
    def Generate(self, deviceName, plcs, genrationOptions):
        """Generate(self: Sivarc, deviceName: str, plcs:  genrationOptions: GenerationOptions) -> SivarcGenerationResult"""
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: Sivarc) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: Sivarc) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class SivarcFeedbackMessage(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Generation result message"""

    @property
    def DateTime(self):
        """
        Date and time for generation message

        Get: DateTime(self: SivarcFeedbackMessage) -> DateTime
        """
        ...
    @property
    def Description(self):
        """
        Description of a generation message

        Get: Description(self: SivarcFeedbackMessage) -> str
        """
        ...
    @property
    def ErrorCount(self):
        """
        Number of errors of generation message

        Get: ErrorCount(self: SivarcFeedbackMessage) -> int
        """
        ...
    @property
    def Messages(self):
        """
        Access to the child messages for a given scenario

        Get: Messages(self: SivarcFeedbackMessage) -> SivarcFeedbackMessageComposition
        """
        ...
    @property
    def MessageType(self):
        """
        Message type of a generation message

        Get: MessageType(self: SivarcFeedbackMessage) -> MessageType
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: SivarcFeedbackMessage) -> IEngineeringObject
        """
        ...
    @property
    def Path(self):
        """
        Path to a generation message

        Get: Path(self: SivarcFeedbackMessage) -> str
        """
        ...
    @property
    def WarningCount(self):
        """
        Number of warnings of generation message

        Get: WarningCount(self: SivarcFeedbackMessage) -> int
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: SivarcFeedbackMessage) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: SivarcFeedbackMessage) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class SivarcFeedbackMessageComposition(
    IEngineeringComposition, IInternalCompositionAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """Composition of GeneratedResultMessages"""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: SivarcFeedbackMessageComposition) -> IEngineeringObject
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: SivarcFeedbackMessageComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: SivarcFeedbackMessageComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[SivarcFeedbackMessage](enumerable:  value: SivarcFeedbackMessage) -> bool"""
        ...
    def __ne__(self, *args): ...

class SivarcGenerationResult(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Sivarc generation result"""

    @property
    def ErrorCount(self):
        """
        Error count

        Get: ErrorCount(self: SivarcGenerationResult) -> int
        """
        ...
    @property
    def IsGenerationSuccessful(self):
        """
        Checks whether generation is successful or not

        Get: IsGenerationSuccessful(self: SivarcGenerationResult) -> bool
        """
        ...
    @property
    def Messages(self):
        """
        Collection of messages

        Get: Messages(self: SivarcGenerationResult) -> SivarcFeedbackMessageComposition
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: SivarcGenerationResult) -> IEngineeringObject
        """
        ...
    @property
    def WarningCount(self):
        """
        Warning Count

        Get: WarningCount(self: SivarcGenerationResult) -> int
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: SivarcGenerationResult) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: SivarcGenerationResult) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class TagRule(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Represents tag rule object"""

    @property
    def Comment(self):
        """
        Tag rule comment

        Get: Comment(self: TagRule) -> str
        """
        ...
    @property
    def Condition(self):
        """
        Tag rule condition

        Get: Condition(self: TagRule) -> str
        """
        ...
    @property
    def Enabled(self):
        """
        Checks whether tag rule is selected

        Get: Enabled(self: TagRule) -> bool
        """
        ...
    @property
    def Name(self):
        """
        Tag rule name

        Get: Name(self: TagRule) -> str
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: TagRule) -> IEngineeringObject
        """
        ...
    def Delete(self):
        """
        Delete(self: TagRule)

            Deletes this instance.
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: TagRule) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: TagRule) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class TagRuleComposition(
    IEngineeringComposition, IInternalCompositionAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """Collection of immediate tag rules"""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: TagRuleComposition) -> IEngineeringObject
        """
        ...
    def CreateFrom(self, ruleMasterCopy, createOption=...):
        """
        CreateFrom(self: TagRuleComposition, ruleMasterCopy: MasterCopy) -> TagRule

            Copy tag rule from library to project with default replace option

            ruleMasterCopy: Tag rule master copy

            Returns: Siemens.Engineering.SiVArc.TagRule

        CreateFrom(self: TagRuleComposition, ruleMasterCopy: MasterCopy, createOption: CreateOptions) -> TagRule

            Copy tag rule from library to project with create options

            ruleMasterCopy: Tag rule master copy

            createOption: Create option

            Returns: Siemens.Engineering.SiVArc.TagRule
        """
        ...
    def Find(self, name):
        """
        Find(self: TagRuleComposition, name: str) -> TagRule

            Finds tag rule based on name

            name: Tag rule name

            Returns: Siemens.Engineering.SiVArc.TagRule
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: TagRuleComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: TagRuleComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[TagRule](enumerable:  value: TagRule) -> bool"""
        ...
    def __ne__(self, *args): ...

class TagRuleGroup(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Represents tag rule group"""

    @property
    def Comment(self):
        """
        Tag rule group comment

        Get: Comment(self: TagRuleGroup) -> str
        """
        ...
    @property
    def Condition(self):
        """
        Tag rule group condition

        Get: Condition(self: TagRuleGroup) -> str
        """
        ...
    @property
    def Enabled(self):
        """
        Checks whether tag rule group is selected

        Get: Enabled(self: TagRuleGroup) -> bool
        """
        ...
    @property
    def Groups(self):
        """
        Collection of immediate groups

        Get: Groups(self: TagRuleGroup) -> TagRuleGroupComposition
        """
        ...
    @property
    def Name(self):
        """
        Tag rule group name

        Get: Name(self: TagRuleGroup) -> str
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: TagRuleGroup) -> IEngineeringObject
        """
        ...
    @property
    def Rules(self):
        """
        Collection of immediate rules

        Get: Rules(self: TagRuleGroup) -> TagRuleComposition
        """
        ...
    def Delete(self):
        """
        Delete(self: TagRuleGroup)

            Deletes this instance.
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: TagRuleGroup) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: TagRuleGroup) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class TagRuleGroupComposition(
    IEngineeringComposition, IInternalCompositionAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """Collection of immediate tag rule groups"""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: TagRuleGroupComposition) -> IEngineeringObject
        """
        ...
    def CreateFrom(self, groupMasterCopy, createOption=...):
        """
        CreateFrom(self: TagRuleGroupComposition, groupMasterCopy: MasterCopy) -> TagRuleGroup

            Copy tag rule group from library to project with default replace option

            groupMasterCopy: Tag rule group master copy

            Returns: Siemens.Engineering.SiVArc.TagRuleGroup

        CreateFrom(self: TagRuleGroupComposition, groupMasterCopy: MasterCopy, createOption: CreateOptions) -> TagRuleGroup

            Copy tag rule group from library to project with create options

            groupMasterCopy: Tag rule group master copy

            createOption: Create option

            Returns: Siemens.Engineering.SiVArc.TagRuleGroup
        """
        ...
    def Find(self, name):
        """
        Find(self: TagRuleGroupComposition, name: str) -> TagRuleGroup

            Finds tag rule group based on name

            name: Tag rule group name

            Returns: Siemens.Engineering.SiVArc.TagRuleGroup
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: TagRuleGroupComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: TagRuleGroupComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[TagRuleGroup](enumerable:  value: TagRuleGroup) -> bool"""
        ...
    def __ne__(self, *args): ...

class TagRules(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Represents tag rules editor"""

    @property
    def Groups(self):
        """
        Navigate to all immediate tag rule groups

        Get: Groups(self: TagRules) -> TagRuleGroupComposition
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: TagRules) -> IEngineeringObject
        """
        ...
    @property
    def Rules(self):
        """
        Navigate to all immediate tag rules

        Get: Rules(self: TagRules) -> TagRuleComposition
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: TagRules) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: TagRules) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class TextlistRule(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Represents textlist rule object"""

    @property
    def Comment(self):
        """
        Textlist rule comment

        Get: Comment(self: TextlistRule) -> str
        """
        ...
    @property
    def Condition(self):
        """
        Textlist rule condition

        Get: Condition(self: TextlistRule) -> str
        """
        ...
    @property
    def Enabled(self):
        """
        Checks whether textlist rule is selected

        Get: Enabled(self: TextlistRule) -> bool
        """
        ...
    @property
    def Name(self):
        """
        Textlist rule name

        Get: Name(self: TextlistRule) -> str
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: TextlistRule) -> IEngineeringObject
        """
        ...
    def Delete(self):
        """
        Delete(self: TextlistRule)

            Deletes this instance.
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: TextlistRule) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: TextlistRule) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class TextlistRuleComposition(
    IEngineeringComposition, IInternalCompositionAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """Collection of immediate textlist rules"""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: TextlistRuleComposition) -> IEngineeringObject
        """
        ...
    def CreateFrom(self, ruleMasterCopy, createOption=...):
        """
        CreateFrom(self: TextlistRuleComposition, ruleMasterCopy: MasterCopy) -> TextlistRule

            Copy textlist rule from library to project with default replace option

            ruleMasterCopy: Textlist rule master copy

            Returns: Siemens.Engineering.SiVArc.TextlistRule

        CreateFrom(self: TextlistRuleComposition, ruleMasterCopy: MasterCopy, createOption: CreateOptions) -> TextlistRule

            Copy textlist rule from library to project with create options

            ruleMasterCopy: Textlist rule master copy

            createOption: Create option

            Returns: Siemens.Engineering.SiVArc.TextlistRule
        """
        ...
    def Find(self, name):
        """
        Find(self: TextlistRuleComposition, name: str) -> TextlistRule

            Finds textlist rule based on name

            name: Textlist rule name

            Returns: Siemens.Engineering.SiVArc.TextlistRule
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: TextlistRuleComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: TextlistRuleComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[TextlistRule](enumerable:  value: TextlistRule) -> bool"""
        ...
    def __ne__(self, *args): ...

class TextlistRuleGroup(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Represents textlist rule group"""

    @property
    def Comment(self):
        """
        Textlist rule group comment

        Get: Comment(self: TextlistRuleGroup) -> str
        """
        ...
    @property
    def Condition(self):
        """
        Textlist rule group condition

        Get: Condition(self: TextlistRuleGroup) -> str
        """
        ...
    @property
    def Enabled(self):
        """
        Checks whether textlist rule group is selected

        Get: Enabled(self: TextlistRuleGroup) -> bool
        """
        ...
    @property
    def Groups(self):
        """
        Collection of immediate groups

        Get: Groups(self: TextlistRuleGroup) -> TextlistRuleGroupComposition
        """
        ...
    @property
    def Name(self):
        """
        Textlist rule group name

        Get: Name(self: TextlistRuleGroup) -> str
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: TextlistRuleGroup) -> IEngineeringObject
        """
        ...
    @property
    def Rules(self):
        """
        Collection of immediate rules

        Get: Rules(self: TextlistRuleGroup) -> TextlistRuleComposition
        """
        ...
    def Delete(self):
        """
        Delete(self: TextlistRuleGroup)

            Deletes this instance.
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: TextlistRuleGroup) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: TextlistRuleGroup) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class TextlistRuleGroupComposition(
    IEngineeringComposition, IInternalCompositionAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """Collection of immediate textlist rule groups"""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: TextlistRuleGroupComposition) -> IEngineeringObject
        """
        ...
    def CreateFrom(self, groupMasterCopy, createOption=...):
        """
        CreateFrom(self: TextlistRuleGroupComposition, groupMasterCopy: MasterCopy) -> TextlistRuleGroup

            Copy textlist rule group from library to project with default replace option

            groupMasterCopy: Textlist rule group master copy

            Returns: Siemens.Engineering.SiVArc.TextlistRuleGroup

        CreateFrom(self: TextlistRuleGroupComposition, groupMasterCopy: MasterCopy, createOption: CreateOptions) -> TextlistRuleGroup

            Copy textlist rule group from library to project with create options

            groupMasterCopy: Textlist rule group master copy

            createOption: Create option

            Returns: Siemens.Engineering.SiVArc.TextlistRuleGroup
        """
        ...
    def Find(self, name):
        """
        Find(self: TextlistRuleGroupComposition, name: str) -> TextlistRuleGroup

            Finds textlist rule group based on name

            name: Textlist rule group name

            Returns: Siemens.Engineering.SiVArc.TextlistRuleGroup
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: TextlistRuleGroupComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: TextlistRuleGroupComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[TextlistRuleGroup](enumerable:  value: TextlistRuleGroup) -> bool"""
        ...
    def __ne__(self, *args): ...

class TextlistRules(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Represents textlist rules editor"""

    @property
    def Groups(self):
        """
        Navigate to all immediate textlist rule groups

        Get: Groups(self: TextlistRules) -> TextlistRuleGroupComposition
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: TextlistRules) -> IEngineeringObject
        """
        ...
    @property
    def Rules(self):
        """
        Navigate to all immediate textlist rules

        Get: Rules(self: TextlistRules) -> TextlistRuleComposition
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: TextlistRules) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: TextlistRules) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...
