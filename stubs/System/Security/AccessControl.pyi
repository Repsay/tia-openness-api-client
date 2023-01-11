# encoding: utf-8
# module System.Security.AccessControl calls itself AccessControl
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AccessControlActions(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies the actions that are permitted for securable objects.

    enum (flags) AccessControlActions, values: Change (2), None (0), View (1)
    """

    Change = None

    value__ = None
    View = None

class AccessControlModification(
    Enum
):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies the type of access control modification to perform. This enumeration is used by methods of the System.Security.AccessControl.ObjectSecurity class and its descendents.

    enum AccessControlModification, values: Add (0), Remove (3), RemoveAll (4), RemoveSpecific (5), Reset (2), Set (1)
    """

    Add = None
    Remove = None
    RemoveAll = None
    RemoveSpecific = None
    Reset = None
    Set = None
    value__ = None

class AccessControlSections(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies which sections of a security descriptor to save or load.

    enum (flags) AccessControlSections, values: Access (2), All (15), Audit (1), Group (8), None (0), Owner (4)
    """

    Access = None
    All = None
    Audit = None
    Group = None

    Owner = None
    value__ = None

class AccessControlType(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies whether an System.Security.AccessControl.AccessRule object is used to allow or deny access. These values are not flags, and they cannot be combined.

    enum AccessControlType, values: Allow (0), Deny (1)
    """

    Allow = None
    Deny = None
    value__ = None

class AccessRule:
    """Represents a combination of a user's identity, an access mask, and an access control type (allow or deny). An System.Security.AccessControl.AccessRule object also contains information about the how the rule is inherited by child objects and how that inheritance is propagated."""

    @staticmethod  # known case of __new__
    def __new__(cls, *args):  # cannot find CLR constructor
        """__new__(cls: type, identity: IdentityReference, accessMask: int, isInherited: bool, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, type: AccessControlType)"""
        ...
    @property
    def AccessControlType(self):
        """
        Gets the System.Security.AccessControl.AccessControlType value associated with this System.Security.AccessControl.AccessRule object.

        Get: AccessControlType(self: AccessRule) -> AccessControlType
        """
        ...
    @property
    def AccessMask(self):
        """Gets the access mask for this rule."""
        ...

class AceEnumerator(object, IEnumerator):
    """Provides the ability to iterate through the access control entries (ACEs) in an access control list (ACL)."""

    @property
    def Current(self):
        """
        Gets the current element in the System.Security.AccessControl.GenericAce collection. This property gets the type-friendly version of the object.

        Get: Current(self: AceEnumerator) -> GenericAce
        """
        ...

class AceFlags(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies the inheritance and auditing behavior of an access control entry (ACE).

    enum (flags) AceFlags, values: AuditFlags (192), ContainerInherit (2), FailedAccess (128), InheritanceFlags (15), Inherited (16), InheritOnly (8), None (0), NoPropagateInherit (4), ObjectInherit (1), SuccessfulAccess (64)
    """

    AuditFlags = None
    ContainerInherit = None
    FailedAccess = None
    InheritanceFlags = None
    Inherited = None
    InheritOnly = None

    NoPropagateInherit = None
    ObjectInherit = None
    SuccessfulAccess = None
    value__ = None

class AceQualifier(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies the function of an access control entry (ACE).

    enum AceQualifier, values: AccessAllowed (0), AccessDenied (1), SystemAlarm (3), SystemAudit (2)
    """

    AccessAllowed = None
    AccessDenied = None
    SystemAlarm = None
    SystemAudit = None
    value__ = None

class AceType(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Defines the available access control entry (ACE) types.

    enum AceType, values: AccessAllowed (0), AccessAllowedCallback (9), AccessAllowedCallbackObject (11), AccessAllowedCompound (4), AccessAllowedObject (5), AccessDenied (1), AccessDeniedCallback (10), AccessDeniedCallbackObject (12), AccessDeniedObject (6), MaxDefinedAceType (16), SystemAlarm (3), SystemAlarmCallback (14), SystemAlarmCallbackObject (16), SystemAlarmObject (8), SystemAudit (2), SystemAuditCallback (13), SystemAuditCallbackObject (15), SystemAuditObject (7)
    """

    AccessAllowed = None
    AccessAllowedCallback = None
    AccessAllowedCallbackObject = None
    AccessAllowedCompound = None
    AccessAllowedObject = None
    AccessDenied = None
    AccessDeniedCallback = None
    AccessDeniedCallbackObject = None
    AccessDeniedObject = None
    MaxDefinedAceType = None
    SystemAlarm = None
    SystemAlarmCallback = None
    SystemAlarmCallbackObject = None
    SystemAlarmObject = None
    SystemAudit = None
    SystemAuditCallback = None
    SystemAuditCallbackObject = None
    SystemAuditObject = None
    value__ = None

class AuditFlags(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies the conditions for auditing attempts to access a securable object.

    enum (flags) AuditFlags, values: Failure (2), None (0), Success (1)
    """

    Failure = None

    Success = None
    value__ = None

class AuditRule:
    """Represents a combination of a user's identity and an access mask. An System.Security.AccessControl.AuditRule object also contains information about how the rule is inherited by child objects, how that inheritance is propagated, and for what conditions it is audited."""

    @staticmethod  # known case of __new__
    def __new__(cls, *args):  # cannot find CLR constructor
        """__new__(cls: type, identity: IdentityReference, accessMask: int, isInherited: bool, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, auditFlags: AuditFlags)"""
        ...
    @property
    def AccessMask(self):
        """Gets the access mask for this rule."""
        ...
    @property
    def AuditFlags(self):
        """
        Gets the audit flags for this audit rule.

        Get: AuditFlags(self: AuditRule) -> AuditFlags
        """
        ...

class AuthorizationRule:  # skipped bases: <type 'object'>
    """Determines access to securable objects. The derived classes System.Security.AccessControl.AccessRule and System.Security.AccessControl.AuditRule offer specializations for access and audit functionality."""

    @property
    def AccessMask(self):
        """Gets the access mask for this rule."""
        ...
    @property
    def IdentityReference(self):
        """
        Gets the System.Security.Principal.IdentityReference to which this rule applies.

        Get: IdentityReference(self: AuthorizationRule) -> IdentityReference
        """
        ...
    @property
    def InheritanceFlags(self):
        """
        Gets the value of flags that determine how this rule is inherited by child objects.

        Get: InheritanceFlags(self: AuthorizationRule) -> InheritanceFlags
        """
        ...
    @property
    def IsInherited(self):
        """
        Gets a value indicating whether this rule is explicitly set or is inherited from a parent container object.

        Get: IsInherited(self: AuthorizationRule) -> bool
        """
        ...
    @property
    def PropagationFlags(self):
        """
        Gets the value of the propagation flags, which determine how inheritance of this rule is propagated to child objects. This property is significant only when the value of the System.Security.AccessControl.InheritanceFlags enumeration is not System.Security.AccessControl.InheritanceFlags.None.

        Get: PropagationFlags(self: AuthorizationRule) -> PropagationFlags
        """
        ...

class AuthorizationRuleCollection(ReadOnlyCollectionBase):  # skipped bases: <type 'ICollection'>, <type 'IEnumerable'>
    """
    Represents a collection of System.Security.AccessControl.AuthorizationRule objects.

    AuthorizationRuleCollection()
    """

    def AddRule(self, rule):
        """
        AddRule(self: AuthorizationRuleCollection, rule: AuthorizationRule)

            Adds an System.Web.Configuration.AuthorizationRule object to the collection.

            rule: The System.Web.Configuration.AuthorizationRule object to add to the collection.
        """
        ...
    def CopyTo(self, rules, index):
        """
        CopyTo(self: AuthorizationRuleCollection, rules: Array[AuthorizationRule], index: int)

            Copies the contents of the collection to an array.

            rules: An array to which to copy the contents of the collection.

            index: The zero-based index from which to begin copying.
        """
        ...
    def __getitem__(self, *args):  # cannot find CLR method
        """x.__getitem__(y) <==> x[y]"""
        ...
    @property
    def InnerList(self):
        """Gets the list of elements contained in the System.Collections.ReadOnlyCollectionBase instance."""
        ...

class GenericAce:  # skipped bases: <type 'object'>
    """Represents an Access Control Entry (ACE), and is the base class for all other ACE classes."""

    def Copy(self):
        """
        Copy(self: GenericAce) -> GenericAce

            Creates a deep copy of this Access Control Entry (ACE).

            Returns: The System.Security.AccessControl.GenericAce object that this method creates.
        """
        ...
    @staticmethod
    def CreateFromBinaryForm(binaryForm, offset):
        """
        CreateFromBinaryForm(binaryForm: Array[Byte], offset: int) -> GenericAce

            Creates a System.Security.AccessControl.GenericAce object from the specified binary data.

            binaryForm: The binary data from which to create the new System.Security.AccessControl.GenericAce object.

            offset: The offset at which to begin unmarshaling.

            Returns: The System.Security.AccessControl.GenericAce object this method creates.
        """
        ...
    def Equals(self, o):
        """
        Equals(self: GenericAce, o: object) -> bool

            Determines whether the specified System.Security.AccessControl.GenericAce object is equal to the current System.Security.AccessControl.GenericAce object.

            o: The System.Security.AccessControl.GenericAce object to compare to the current System.Security.AccessControl.GenericAce object.

            Returns: ue if the specified System.Security.AccessControl.GenericAce object is equal to the current System.Security.AccessControl.GenericAce object; otherwise, lse.
        """
        ...
    def GetBinaryForm(self, binaryForm, offset):
        """
        GetBinaryForm(self: GenericAce, binaryForm: Array[Byte], offset: int)

            Marshals the contents of the System.Security.AccessControl.GenericAce object into the specified byte array beginning at the specified offset.

            binaryForm: The byte array into which the contents of the System.Security.AccessControl.GenericAce is marshaled.

            offset: The offset at which to start marshaling.
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: GenericAce) -> int

            Serves as a hash function for the System.Security.AccessControl.GenericAce class. The  System.Security.AccessControl.GenericAce.GetHashCode method is suitable for use in hashing algorithms and data structures like a hash table.

            Returns: A hash code for the current System.Security.AccessControl.GenericAce object.
        """
        ...
    def __eq__(self, *args):  # cannot find CLR method
        """x.__eq__(y) <==> x==y"""
        ...
    def __ne__(self, *args): ...
    @property
    def AceFlags(self):
        """
        Gets or sets the System.Security.AccessControl.AceFlags associated with this System.Security.AccessControl.GenericAce object.

        Get: AceFlags(self: GenericAce) -> AceFlags

        Set: AceFlags(self: GenericAce) = value
        """
        ...
    @property
    def AceType(self):
        """
        Gets the type of this Access Control Entry (ACE).

        Get: AceType(self: GenericAce) -> AceType
        """
        ...
    @property
    def AuditFlags(self):
        """
        Gets the audit information associated with this Access Control Entry (ACE).

        Get: AuditFlags(self: GenericAce) -> AuditFlags
        """
        ...
    @property
    def BinaryLength(self):
        """
        Gets the length, in bytes, of the binary representation of the current System.Security.AccessControl.GenericAce object. This length should be used before marshaling the ACL into a binary array with the System.Security.AccessControl.GenericAce.GetBinaryForm(System.Byte[],System.Int32) method.

        Get: BinaryLength(self: GenericAce) -> int
        """
        ...
    @property
    def InheritanceFlags(self):
        """
        Gets flags that specify the inheritance properties of this Access Control Entry (ACE).

        Get: InheritanceFlags(self: GenericAce) -> InheritanceFlags
        """
        ...
    @property
    def IsInherited(self):
        """
        Gets a Boolean value that specifies whether this Access Control Entry (ACE) is inherited or is set explicitly.

        Get: IsInherited(self: GenericAce) -> bool
        """
        ...
    @property
    def PropagationFlags(self):
        """
        Gets flags that specify the inheritance propagation properties of this Access Control Entry (ACE).

        Get: PropagationFlags(self: GenericAce) -> PropagationFlags
        """
        ...

class KnownAce(GenericAce):
    """Encapsulates all Access Control Entry (ACE) types currently defined by Microsoft Corporation. All System.Security.AccessControl.KnownAce objects contain a 32-bit access mask and a System.Security.Principal.SecurityIdentifier object."""

    @property
    def AccessMask(self):
        """
        Gets or sets the access mask for this System.Security.AccessControl.KnownAce object.

        Get: AccessMask(self: KnownAce) -> int

        Set: AccessMask(self: KnownAce) = value
        """
        ...
    @property
    def SecurityIdentifier(self):
        """
        Gets or sets the System.Security.Principal.SecurityIdentifier object associated with this System.Security.AccessControl.KnownAce object.

        Get: SecurityIdentifier(self: KnownAce) -> SecurityIdentifier

        Set: SecurityIdentifier(self: KnownAce) = value
        """
        ...

class QualifiedAce(KnownAce):
    """Represents an Access Control Entry (ACE) that contains a qualifier. The qualifier, represented by an System.Security.AccessControl.AceQualifier object, specifies whether the ACE allows access, denies access, causes system audits, or causes system alarms. The System.Security.AccessControl.QualifiedAce class is the abstract base class for the System.Security.AccessControl.CommonAce and System.Security.AccessControl.ObjectAce classes."""

    def GetOpaque(self):
        """
        GetOpaque(self: QualifiedAce) -> Array[Byte]

            Returns the opaque callback data associated with this System.Security.AccessControl.QualifiedAce object.

            Returns: An array of byte values that represents the opaque callback data associated with this System.Security.AccessControl.QualifiedAce object.
        """
        ...
    def SetOpaque(self, opaque):
        """
        SetOpaque(self: QualifiedAce, opaque: Array[Byte])

            Sets the opaque callback data associated with this System.Security.AccessControl.QualifiedAce object.

            opaque: An array of byte values that represents the opaque callback data for this System.Security.AccessControl.QualifiedAce object.
        """
        ...
    @property
    def AceQualifier(self):
        """
        Gets a value that specifies whether the ACE allows access, denies access, causes system audits, or causes system alarms.

        Get: AceQualifier(self: QualifiedAce) -> AceQualifier
        """
        ...
    @property
    def IsCallback(self):
        """
        Specifies whether this System.Security.AccessControl.QualifiedAce object contains callback data.

        Get: IsCallback(self: QualifiedAce) -> bool
        """
        ...
    @property
    def OpaqueLength(self):
        """
        Gets the length of the opaque callback data associated with this System.Security.AccessControl.QualifiedAce object. This property is valid only for callback Access Control Entries (ACEs).

        Get: OpaqueLength(self: QualifiedAce) -> int
        """
        ...

class CommonAce(QualifiedAce):
    """
    Represents an access control entry (ACE).

    CommonAce(flags: AceFlags, qualifier: AceQualifier, accessMask: int, sid: SecurityIdentifier, isCallback: bool, opaque: Array[Byte])
    """

    def GetBinaryForm(self, binaryForm, offset):
        """
        GetBinaryForm(self: CommonAce, binaryForm: Array[Byte], offset: int)

            Marshals the contents of the System.Security.AccessControl.CommonAce object into the specified byte array beginning at the specified offset.

            binaryForm: The byte array into which the contents of the System.Security.AccessControl.CommonAce object is marshaled.

            offset: The offset at which to start marshaling.
        """
        ...
    @staticmethod
    def MaxOpaqueLength(isCallback):
        """
        MaxOpaqueLength(isCallback: bool) -> int

            Gets the maximum allowed length of an opaque data BLOB for callback access control entries (ACEs).

            isCallback: ue to specify that the System.Security.AccessControl.CommonAce object is a callback ACE type.

            Returns: The allowed length of an opaque data BLOB.
        """
        ...
    @staticmethod  # known case of __new__
    def __new__(cls, flags, qualifier, accessMask, sid, isCallback, opaque):
        """__new__(cls: type, flags: AceFlags, qualifier: AceQualifier, accessMask: int, sid: SecurityIdentifier, isCallback: bool, opaque: Array[Byte])"""
        ...
    @property
    def BinaryLength(self):
        """
        Gets the length, in bytes, of the binary representation of the current System.Security.AccessControl.CommonAce object. Use this length with the System.Security.AccessControl.CommonAce.GetBinaryForm(System.Byte[],System.Int32) method before marshaling the ACL into a binary array.

        Get: BinaryLength(self: CommonAce) -> int
        """
        ...

class GenericAcl(object, ICollection):  # skipped bases: <type 'IEnumerable'>
    """Represents an access control list (ACL) and is the base class for the System.Security.AccessControl.CommonAcl, System.Security.AccessControl.DiscretionaryAcl, System.Security.AccessControl.RawAcl, and System.Security.AccessControl.SystemAcl classes."""

    def GetBinaryForm(self, binaryForm, offset):
        """
        GetBinaryForm(self: GenericAcl, binaryForm: Array[Byte], offset: int)

            Marshals the contents of the System.Security.AccessControl.GenericAcl object into the specified byte array beginning at the specified offset.

            binaryForm: The byte array into which the contents of the System.Security.AccessControl.GenericAcl is marshaled.

            offset: The offset at which to start marshaling.
        """
        ...
    def GetEnumerator(self):
        """
        GetEnumerator(self: GenericAcl) -> AceEnumerator

            Retrieves an object that you can use to iterate through the access control entries (ACEs) in an access control list (ACL).

            Returns: An enumerator object.
        """
        ...
    def __getitem__(self, *args):  # cannot find CLR method
        """x.__getitem__(y) <==> x[y]"""
        ...
    def __len__(self, *args):  # cannot find CLR method
        """x.__len__() <==> len(x)"""
        ...
    def __setitem__(self, *args):  # cannot find CLR method
        """x.__setitem__(i, y) <==> x[i]="""
        ...
    @property
    def BinaryLength(self):
        """
        Gets the length, in bytes, of the binary representation of the current System.Security.AccessControl.GenericAcl object. This length should be used before marshaling the ACL into a binary array with the System.Security.AccessControl.GenericAcl.GetBinaryForm(System.Byte[],System.Int32) method.

        Get: BinaryLength(self: GenericAcl) -> int
        """
        ...
    @property
    def Count(self):
        """
        Gets the number of access control entries (ACEs) in the current System.Security.AccessControl.GenericAcl object.

        Get: Count(self: GenericAcl) -> int
        """
        ...
    @property
    def IsSynchronized(self):
        """
        This property is always set to lse. It is implemented only because it is required for the implementation of the System.Collections.ICollection interface.

        Get: IsSynchronized(self: GenericAcl) -> bool
        """
        ...
    @property
    def Revision(self):
        """
        Gets the revision level of the System.Security.AccessControl.GenericAcl.

        Get: Revision(self: GenericAcl) -> Byte
        """
        ...
    @property
    def SyncRoot(self):
        """
        This property always returns ll. It is implemented only because it is required for the implementation of the System.Collections.ICollection interface.

        Get: SyncRoot(self: GenericAcl) -> object
        """
        ...
    AclRevision = None
    AclRevisionDS = None
    MaxBinaryLength = 65535

class CommonAcl(GenericAcl):  # skipped bases: <type 'ICollection'>, <type 'IEnumerable'>
    """Represents an access control list (ACL) and is the base class for the System.Security.AccessControl.DiscretionaryAcl and System.Security.AccessControl.SystemAcl classes."""

    def Purge(self, sid):
        """
        Purge(self: CommonAcl, sid: SecurityIdentifier)

            Removes all access control entries (ACEs) contained by this System.Security.AccessControl.CommonAcl object that are associated with the specified System.Security.Principal.SecurityIdentifier object.

            sid: The System.Security.Principal.SecurityIdentifier object to check for.
        """
        ...
    def RemoveInheritedAces(self):
        """
        RemoveInheritedAces(self: CommonAcl)

            Removes all inherited access control entries (ACEs) from this System.Security.AccessControl.CommonAcl object.
        """
        ...
    @property
    def BinaryLength(self):
        """
        Gets the length, in bytes, of the binary representation of the current System.Security.AccessControl.CommonAcl object. This length should be used before marshaling the access control list (ACL) into a binary array by using the System.Security.AccessControl.CommonAcl.GetBinaryForm(System.Byte[],System.Int32) method.

        Get: BinaryLength(self: CommonAcl) -> int
        """
        ...
    @property
    def Count(self):
        """
        Gets the number of access control entries (ACEs) in the current System.Security.AccessControl.CommonAcl object.

        Get: Count(self: CommonAcl) -> int
        """
        ...
    @property
    def IsCanonical(self):
        """
        Gets a Boolean value that specifies whether the access control entries (ACEs) in the current System.Security.AccessControl.CommonAcl object are in canonical order.

        Get: IsCanonical(self: CommonAcl) -> bool
        """
        ...
    @property
    def IsContainer(self):
        """
        Sets whether the System.Security.AccessControl.CommonAcl object is a container.

        Get: IsContainer(self: CommonAcl) -> bool
        """
        ...
    @property
    def IsDS(self):
        """
        Sets whether the current System.Security.AccessControl.CommonAcl object is a directory object access control list (ACL).

        Get: IsDS(self: CommonAcl) -> bool
        """
        ...
    @property
    def Revision(self):
        """
        Gets the revision level of the System.Security.AccessControl.CommonAcl.

        Get: Revision(self: CommonAcl) -> Byte
        """
        ...

class CommonObjectSecurity(ObjectSecurity):
    """Controls access to objects without direct manipulation of access control lists (ACLs). This class is the abstract base class for the System.Security.AccessControl.NativeObjectSecurity class."""

    def AddAccessRule(self, *args):  # cannot find CLR method
        """
        AddAccessRule(self: CommonObjectSecurity, rule: AccessRule)

            Adds the specified access rule to the Discretionary Access Control List (DACL) associated with this System.Security.AccessControl.CommonObjectSecurity object.

            rule: The access rule to add.
        """
        ...
    def AddAuditRule(self, *args):  # cannot find CLR method
        """
        AddAuditRule(self: CommonObjectSecurity, rule: AuditRule)

            Adds the specified audit rule to the System Access Control List (SACL) associated with this System.Security.AccessControl.CommonObjectSecurity object.

            rule: The audit rule to add.
        """
        ...
    def GetAccessRules(self, includeExplicit, includeInherited, targetType):
        """
        GetAccessRules(self: CommonObjectSecurity, includeExplicit: bool, includeInherited: bool, targetType: Type) -> AuthorizationRuleCollection

            Gets a collection of the access rules associated with the specified security identifier.

            includeExplicit: ue to include access rules explicitly set for the object.

            includeInherited: ue to include inherited access rules.

            targetType: Specifies whether the security identifier for which to retrieve access rules is of type T:System.Security.Principal.SecurityIdentifier or type T:System.Security.Principal.NTAccount. The value of this parameter must be a type that

             can be translated to  the System.Security.Principal.SecurityIdentifier type.

            Returns: The collection of access rules associated with the specified System.Security.Principal.SecurityIdentifier object.
        """
        ...
    def GetAuditRules(self, includeExplicit, includeInherited, targetType):
        """
        GetAuditRules(self: CommonObjectSecurity, includeExplicit: bool, includeInherited: bool, targetType: Type) -> AuthorizationRuleCollection

            Gets a collection of the audit rules associated with the specified security identifier.

            includeExplicit: ue to include audit rules explicitly set for the object.

            includeInherited: ue to include inherited audit rules.

            targetType: The security identifier for which to retrieve audit rules. This must be an object that can be cast as a System.Security.Principal.SecurityIdentifier object.

            Returns: The collection of audit rules associated with the specified System.Security.Principal.SecurityIdentifier object.
        """
        ...
    def RemoveAccessRule(self, *args):  # cannot find CLR method
        """
        RemoveAccessRule(self: CommonObjectSecurity, rule: AccessRule) -> bool

            Removes access rules that contain the same security identifier and access mask as the specified access rule from the Discretionary Access Control List (DACL) associated with this System.Security.AccessControl.CommonObjectSecurity

             object.

            rule: The access rule to remove.

            Returns: ue if the access rule was successfully removed; otherwise, lse.
        """
        ...
    def RemoveAccessRuleAll(self, *args):  # cannot find CLR method
        """
        RemoveAccessRuleAll(self: CommonObjectSecurity, rule: AccessRule)

            Removes all access rules that have the same security identifier as the specified access rule from the Discretionary Access Control List (DACL) associated with this System.Security.AccessControl.CommonObjectSecurity object.

            rule: The access rule to remove.
        """
        ...
    def RemoveAccessRuleSpecific(self, *args):  # cannot find CLR method
        """
        RemoveAccessRuleSpecific(self: CommonObjectSecurity, rule: AccessRule)

            Removes all access rules that exactly match the specified access rule from the Discretionary Access Control List (DACL) associated with this System.Security.AccessControl.CommonObjectSecurity object.

            rule: The access rule to remove.
        """
        ...
    def RemoveAuditRule(self, *args):  # cannot find CLR method
        """
        RemoveAuditRule(self: CommonObjectSecurity, rule: AuditRule) -> bool

            Removes audit rules that contain the same security identifier and access mask as the specified audit rule from the System Access Control List (SACL) associated with this System.Security.AccessControl.CommonObjectSecurity object.

            rule: The audit rule to remove.

            Returns: ue if the audit rule was successfully removed; otherwise, lse.
        """
        ...
    def RemoveAuditRuleAll(self, *args):  # cannot find CLR method
        """
        RemoveAuditRuleAll(self: CommonObjectSecurity, rule: AuditRule)

            Removes all audit rules that have the same security identifier as the specified audit rule from the System Access Control List (SACL) associated with this System.Security.AccessControl.CommonObjectSecurity object.

            rule: The audit rule to remove.
        """
        ...
    def RemoveAuditRuleSpecific(self, *args):  # cannot find CLR method
        """
        RemoveAuditRuleSpecific(self: CommonObjectSecurity, rule: AuditRule)

            Removes all audit rules that exactly match the specified audit rule from the System Access Control List (SACL) associated with this System.Security.AccessControl.CommonObjectSecurity object.

            rule: The audit rule to remove.
        """
        ...
    def ResetAccessRule(self, *args):  # cannot find CLR method
        """
        ResetAccessRule(self: CommonObjectSecurity, rule: AccessRule)

            Removes all access rules in the Discretionary Access Control List (DACL) associated with this System.Security.AccessControl.CommonObjectSecurity object and then adds the specified access rule.

            rule: The access rule to reset.
        """
        ...
    def SetAccessRule(self, *args):  # cannot find CLR method
        """
        SetAccessRule(self: CommonObjectSecurity, rule: AccessRule)

            Removes all access rules that contain the same security identifier and qualifier as the specified access rule in the Discretionary Access Control List (DACL) associated with this System.Security.AccessControl.CommonObjectSecurity

             object and then adds the specified access rule.

            rule: The access rule to set.
        """
        ...
    def SetAuditRule(self, *args):  # cannot find CLR method
        """
        SetAuditRule(self: CommonObjectSecurity, rule: AuditRule)

            Removes all audit rules that contain the same security identifier and qualifier as the specified audit rule in the System Access Control List (SACL) associated with this System.Security.AccessControl.CommonObjectSecurity object and

             then adds the specified audit rule.

            rule: The audit rule to set.
        """
        ...
    @property
    def AccessRulesModified(self):
        """Gets or sets a Boolean value that specifies whether the access rules associated with this System.Security.AccessControl.ObjectSecurity object have been modified."""
        ...
    @property
    def AuditRulesModified(self):
        """Gets or sets a Boolean value that specifies whether the audit rules associated with this System.Security.AccessControl.ObjectSecurity object have been modified."""
        ...
    @property
    def GroupModified(self):
        """Gets or sets a Boolean value that specifies whether the group associated with the securable object has been modified."""
        ...
    @property
    def IsContainer(self):
        """Gets a Boolean value that specifies whether this System.Security.AccessControl.ObjectSecurity object is a container object."""
        ...
    @property
    def IsDS(self):
        """Gets a Boolean value that specifies whether this System.Security.AccessControl.ObjectSecurity object is a directory object."""
        ...
    @property
    def OwnerModified(self):
        """Gets or sets a Boolean value that specifies whether the owner of the securable object has been modified."""
        ...

class GenericSecurityDescriptor:  # skipped bases: <type 'object'>
    """Represents a security descriptor. A security descriptor includes an owner, a primary group, a Discretionary Access Control List (DACL), and a System Access Control List (SACL)."""

    def GetBinaryForm(self, binaryForm, offset):
        """
        GetBinaryForm(self: GenericSecurityDescriptor, binaryForm: Array[Byte], offset: int)

            Returns an array of byte values that represents the information contained in this System.Security.AccessControl.GenericSecurityDescriptor object.

            binaryForm: The byte array into which the contents of the System.Security.AccessControl.GenericSecurityDescriptor is marshaled.

            offset: The offset at which to start marshaling.
        """
        ...
    def GetSddlForm(self, includeSections):
        """
        GetSddlForm(self: GenericSecurityDescriptor, includeSections: AccessControlSections) -> str

            Returns the Security Descriptor Definition Language (SDDL) representation of the specified sections of the security descriptor that this System.Security.AccessControl.GenericSecurityDescriptor object represents.

            includeSections: Specifies which sections (access rules, audit rules, primary group, owner) of the security descriptor to get.

            Returns: The SDDL representation of the specified sections of the security descriptor associated with this System.Security.AccessControl.GenericSecurityDescriptor object.
        """
        ...
    @staticmethod
    def IsSddlConversionSupported():
        """
        IsSddlConversionSupported() -> bool

            Returns a boolean value that specifies whether the security descriptor associated with this  System.Security.AccessControl.GenericSecurityDescriptor object can be converted to the Security Descriptor Definition Language (SDDL)

             format.

            Returns: ue if the security descriptor associated with this  System.Security.AccessControl.GenericSecurityDescriptor object can be converted to the Security Descriptor Definition Language (SDDL) format; otherwise, lse.
        """
        ...
    @property
    def BinaryLength(self):
        """
        Gets the length, in bytes, of the binary representation of the current System.Security.AccessControl.GenericSecurityDescriptor object. This length should be used before marshaling the ACL into a binary array with the System.Security.AccessControl.GenericSecurityDescriptor.GetBinaryForm(System.Byte[],System.Int32) method.

        Get: BinaryLength(self: GenericSecurityDescriptor) -> int
        """
        ...
    @property
    def ControlFlags(self):
        """
        Gets values that specify behavior of the System.Security.AccessControl.GenericSecurityDescriptor object.

        Get: ControlFlags(self: GenericSecurityDescriptor) -> ControlFlags
        """
        ...
    @property
    def Group(self):
        """
        Gets or sets the primary group for this System.Security.AccessControl.GenericSecurityDescriptor object.

        Get: Group(self: GenericSecurityDescriptor) -> SecurityIdentifier

        Set: Group(self: GenericSecurityDescriptor) = value
        """
        ...
    @property
    def Owner(self):
        """
        Gets or sets the owner of the object associated with this System.Security.AccessControl.GenericSecurityDescriptor object.

        Get: Owner(self: GenericSecurityDescriptor) -> SecurityIdentifier

        Set: Owner(self: GenericSecurityDescriptor) = value
        """
        ...
    Revision = None

class CommonSecurityDescriptor(GenericSecurityDescriptor):
    """
    Represents a security descriptor. A security descriptor includes an owner, a primary group, a Discretionary Access Control List (DACL), and a System Access Control List (SACL).

    CommonSecurityDescriptor(isContainer: bool, isDS: bool, flags: ControlFlags, owner: SecurityIdentifier, group: SecurityIdentifier, systemAcl: SystemAcl, discretionaryAcl: DiscretionaryAcl)

    CommonSecurityDescriptor(isContainer: bool, isDS: bool, rawSecurityDescriptor: RawSecurityDescriptor)

    CommonSecurityDescriptor(isContainer: bool, isDS: bool, sddlForm: str)

    CommonSecurityDescriptor(isContainer: bool, isDS: bool, binaryForm: Array[Byte], offset: int)
    """

    def AddDiscretionaryAcl(self, revision, trusted):
        """
        AddDiscretionaryAcl(self: CommonSecurityDescriptor, revision: Byte, trusted: int)

            Sets the System.Security.AccessControl.CommonSecurityDescriptor.DiscretionaryAcl property for this System.Security.AccessControl.CommonSecurityDescriptor instance and sets the

             System.Security.AccessControl.ControlFlags.DiscretionaryAclPresent flag.

            revision: The revision level of the new System.Security.AccessControl.DiscretionaryAcl object.

            trusted: The number of Access Control Entries (ACEs) this System.Security.AccessControl.DiscretionaryAcl object can contain. This number is to be used only as a hint.
        """
        ...
    def AddSystemAcl(self, revision, trusted):
        """
        AddSystemAcl(self: CommonSecurityDescriptor, revision: Byte, trusted: int)

            Sets the System.Security.AccessControl.CommonSecurityDescriptor.SystemAcl property for this System.Security.AccessControl.CommonSecurityDescriptor instance and sets the System.Security.AccessControl.ControlFlags.SystemAclPresent

             flag.

            revision: The revision level of the new System.Security.AccessControl.SystemAcl object.

            trusted: The number of Access Control Entries (ACEs) this System.Security.AccessControl.SystemAcl object can contain. This number is to be used only as a hint.
        """
        ...
    def PurgeAccessControl(self, sid):
        """
        PurgeAccessControl(self: CommonSecurityDescriptor, sid: SecurityIdentifier)

            Removes all access rules for the specified security identifier from the Discretionary Access Control List (DACL) associated with this System.Security.AccessControl.CommonSecurityDescriptor object.

            sid: The security identifier for which to remove access rules.
        """
        ...
    def PurgeAudit(self, sid):
        """
        PurgeAudit(self: CommonSecurityDescriptor, sid: SecurityIdentifier)

            Removes all audit rules for the specified security identifier from the System Access Control List (SACL) associated with this System.Security.AccessControl.CommonSecurityDescriptor object.

            sid: The security identifier for which to remove audit rules.
        """
        ...
    def SetDiscretionaryAclProtection(self, isProtected, preserveInheritance):
        """
        SetDiscretionaryAclProtection(self: CommonSecurityDescriptor, isProtected: bool, preserveInheritance: bool)

            Sets the inheritance protection for the Discretionary Access Control List (DACL) associated with this System.Security.AccessControl.CommonSecurityDescriptor object. DACLs that are protected do not inherit access rules from parent

             containers.

            isProtected: ue to protect the DACL from inheritance.

            preserveInheritance: ue to keep inherited access rules in the DACL; lse to remove inherited access rules from the DACL.
        """
        ...
    def SetSystemAclProtection(self, isProtected, preserveInheritance):
        """
        SetSystemAclProtection(self: CommonSecurityDescriptor, isProtected: bool, preserveInheritance: bool)

            Sets the inheritance protection for the System Access Control List (SACL) associated with this System.Security.AccessControl.CommonSecurityDescriptor object. SACLs that are protected do not inherit audit rules from parent containers.

            isProtected: ue to protect the SACL from inheritance.

            preserveInheritance: ue to keep inherited audit rules in the SACL; lse to remove inherited audit rules from the SACL.
        """
        ...
    @staticmethod  # known case of __new__
    def __new__(cls, isContainer, isDS, *__args):
        """
        __new__(cls: type, isContainer: bool, isDS: bool, flags: ControlFlags, owner: SecurityIdentifier, group: SecurityIdentifier, systemAcl: SystemAcl, discretionaryAcl: DiscretionaryAcl)

        __new__(cls: type, isContainer: bool, isDS: bool, rawSecurityDescriptor: RawSecurityDescriptor)

        __new__(cls: type, isContainer: bool, isDS: bool, sddlForm: str)

        __new__(cls: type, isContainer: bool, isDS: bool, binaryForm: Array[Byte], offset: int)
        """
        ...
    @property
    def ControlFlags(self):
        """
        Gets values that specify behavior of the System.Security.AccessControl.CommonSecurityDescriptor object.

        Get: ControlFlags(self: CommonSecurityDescriptor) -> ControlFlags
        """
        ...
    @property
    def DiscretionaryAcl(self):
        """
        Gets or sets the discretionary access control list (DACL) for this System.Security.AccessControl.CommonSecurityDescriptor object. The DACL contains access rules.

        Get: DiscretionaryAcl(self: CommonSecurityDescriptor) -> DiscretionaryAcl

        Set: DiscretionaryAcl(self: CommonSecurityDescriptor) = value
        """
        ...
    @property
    def Group(self):
        """
        Gets or sets the primary group for this System.Security.AccessControl.CommonSecurityDescriptor object.

        Get: Group(self: CommonSecurityDescriptor) -> SecurityIdentifier

        Set: Group(self: CommonSecurityDescriptor) = value
        """
        ...
    @property
    def IsContainer(self):
        """
        Gets a Boolean value that specifies whether the object associated with this System.Security.AccessControl.CommonSecurityDescriptor object is a container object.

        Get: IsContainer(self: CommonSecurityDescriptor) -> bool
        """
        ...
    @property
    def IsDiscretionaryAclCanonical(self):
        """
        Gets a Boolean value that specifies whether the Discretionary Access Control List (DACL) associated with this System.Security.AccessControl.CommonSecurityDescriptor object is in canonical order.

        Get: IsDiscretionaryAclCanonical(self: CommonSecurityDescriptor) -> bool
        """
        ...
    @property
    def IsDS(self):
        """
        Gets a Boolean value that specifies whether the object associated with this System.Security.AccessControl.CommonSecurityDescriptor object is a directory object.

        Get: IsDS(self: CommonSecurityDescriptor) -> bool
        """
        ...
    @property
    def IsSystemAclCanonical(self):
        """
        Gets a Boolean value that specifies whether the System Access Control List (SACL) associated with this System.Security.AccessControl.CommonSecurityDescriptor object is in canonical order.

        Get: IsSystemAclCanonical(self: CommonSecurityDescriptor) -> bool
        """
        ...
    @property
    def Owner(self):
        """
        Gets or sets the owner of the object associated with this System.Security.AccessControl.CommonSecurityDescriptor object.

        Get: Owner(self: CommonSecurityDescriptor) -> SecurityIdentifier

        Set: Owner(self: CommonSecurityDescriptor) = value
        """
        ...
    @property
    def SystemAcl(self):
        """
        Gets or sets the System Access Control List (SACL) for this System.Security.AccessControl.CommonSecurityDescriptor object. The SACL contains audit rules.

        Get: SystemAcl(self: CommonSecurityDescriptor) -> SystemAcl

        Set: SystemAcl(self: CommonSecurityDescriptor) = value
        """
        ...

class CompoundAce(KnownAce):
    """
    Represents a compound Access Control Entry (ACE).

    CompoundAce(flags: AceFlags, accessMask: int, compoundAceType: CompoundAceType, sid: SecurityIdentifier)
    """

    def GetBinaryForm(self, binaryForm, offset):
        """
        GetBinaryForm(self: CompoundAce, binaryForm: Array[Byte], offset: int)

            Marshals the contents of the System.Security.AccessControl.CompoundAce object into the specified byte array beginning at the specified offset.

            binaryForm: The byte array into which the contents of the System.Security.AccessControl.CompoundAce is marshaled.

            offset: The offset at which to start marshaling.
        """
        ...
    @staticmethod  # known case of __new__
    def __new__(cls, flags, accessMask, compoundAceType, sid):
        """__new__(cls: type, flags: AceFlags, accessMask: int, compoundAceType: CompoundAceType, sid: SecurityIdentifier)"""
        ...
    @property
    def BinaryLength(self):
        """
        Gets the length, in bytes, of the binary representation of the current System.Security.AccessControl.CompoundAce object. This length should be used before marshaling the ACL into a binary array with the System.Security.AccessControl.CompoundAce.GetBinaryForm(System.Byte[],System.Int32) method.

        Get: BinaryLength(self: CompoundAce) -> int
        """
        ...
    @property
    def CompoundAceType(self):
        """
        Gets or sets the type of this System.Security.AccessControl.CompoundAce object.

        Get: CompoundAceType(self: CompoundAce) -> CompoundAceType

        Set: CompoundAceType(self: CompoundAce) = value
        """
        ...

class CompoundAceType(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies the type of a System.Security.AccessControl.CompoundAce object.

    enum CompoundAceType, values: Impersonation (1)
    """

    Impersonation = None
    value__ = None

class ControlFlags(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    These flags affect the security descriptor behavior.

    enum (flags) ControlFlags, values: DiscretionaryAclAutoInherited (1024), DiscretionaryAclAutoInheritRequired (256), DiscretionaryAclDefaulted (8), DiscretionaryAclPresent (4), DiscretionaryAclProtected (4096), DiscretionaryAclUntrusted (64), GroupDefaulted (2), None (0), OwnerDefaulted (1), RMControlValid (16384), SelfRelative (32768), ServerSecurity (128), SystemAclAutoInherited (2048), SystemAclAutoInheritRequired (512), SystemAclDefaulted (32), SystemAclPresent (16), SystemAclProtected (8192)
    """

    DiscretionaryAclAutoInherited = None
    DiscretionaryAclAutoInheritRequired = None
    DiscretionaryAclDefaulted = None
    DiscretionaryAclPresent = None
    DiscretionaryAclProtected = None
    DiscretionaryAclUntrusted = None
    GroupDefaulted = None

    OwnerDefaulted = None
    RMControlValid = None
    SelfRelative = None
    ServerSecurity = None
    SystemAclAutoInherited = None
    SystemAclAutoInheritRequired = None
    SystemAclDefaulted = None
    SystemAclPresent = None
    SystemAclProtected = None
    value__ = None

class CryptoKeyAccessRule(AccessRule):
    """
    Represents an access rule for a cryptographic key. An access rule represents a combination of a user's identity, an access mask, and an access control type (allow or deny). An access rule object also contains information about the how the rule is inherited by child objects and how that inheritance is propagated.

    CryptoKeyAccessRule(identity: IdentityReference, cryptoKeyRights: CryptoKeyRights, type: AccessControlType)

    CryptoKeyAccessRule(identity: str, cryptoKeyRights: CryptoKeyRights, type: AccessControlType)
    """

    @property
    def AccessMask(self):
        """Gets the access mask for this rule."""
        ...
    @property
    def CryptoKeyRights(self):
        """
        Gets the cryptographic key operation to which this access rule controls access.

        Get: CryptoKeyRights(self: CryptoKeyAccessRule) -> CryptoKeyRights
        """
        ...

class CryptoKeyAuditRule(AuditRule):
    """
    Represents an audit rule for a cryptographic key. An audit rule represents a combination of a user's identity and an access mask. An audit rule also contains information about the how the rule is inherited by child objects, how that inheritance is propagated, and for what conditions it is audited.

    CryptoKeyAuditRule(identity: IdentityReference, cryptoKeyRights: CryptoKeyRights, flags: AuditFlags)

    CryptoKeyAuditRule(identity: str, cryptoKeyRights: CryptoKeyRights, flags: AuditFlags)
    """

    @property
    def AccessMask(self):
        """Gets the access mask for this rule."""
        ...
    @property
    def CryptoKeyRights(self):
        """
        Gets the cryptographic key operation for which this audit rule generates audits.

        Get: CryptoKeyRights(self: CryptoKeyAuditRule) -> CryptoKeyRights
        """
        ...

class CryptoKeyRights(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies the cryptographic key operation for which an authorization rule controls access or auditing.

    enum (flags) CryptoKeyRights, values: ChangePermissions (262144), Delete (65536), FullControl (2032027), GenericAll (268435456), GenericExecute (536870912), GenericRead (-2147483648), GenericWrite (1073741824), ReadAttributes (128), ReadData (1), ReadExtendedAttributes (8), ReadPermissions (131072), Synchronize (1048576), TakeOwnership (524288), WriteAttributes (256), WriteData (2), WriteExtendedAttributes (16)
    """

    ChangePermissions = None
    Delete = None
    FullControl = None
    GenericAll = None
    GenericExecute = None
    GenericRead = None
    GenericWrite = None
    ReadAttributes = None
    ReadData = None
    ReadExtendedAttributes = None
    ReadPermissions = None
    Synchronize = None
    TakeOwnership = None
    value__ = None
    WriteAttributes = None
    WriteData = None
    WriteExtendedAttributes = None

class NativeObjectSecurity(CommonObjectSecurity):
    """Provides the ability to control access to native objects without direct manipulation of Access Control Lists (ACLs). Native object types are defined by the System.Security.AccessControl.ResourceType enumeration."""

    def ExceptionFromErrorCode(self, *args):  # cannot find CLR method
        """ExceptionFromErrorCode(object: object, method: IntPtr)"""
        ...
    @property
    def AccessRulesModified(self):
        """Gets or sets a Boolean value that specifies whether the access rules associated with this System.Security.AccessControl.ObjectSecurity object have been modified."""
        ...
    @property
    def AuditRulesModified(self):
        """Gets or sets a Boolean value that specifies whether the audit rules associated with this System.Security.AccessControl.ObjectSecurity object have been modified."""
        ...
    @property
    def GroupModified(self):
        """Gets or sets a Boolean value that specifies whether the group associated with the securable object has been modified."""
        ...
    @property
    def IsContainer(self):
        """Gets a Boolean value that specifies whether this System.Security.AccessControl.ObjectSecurity object is a container object."""
        ...
    @property
    def IsDS(self):
        """Gets a Boolean value that specifies whether this System.Security.AccessControl.ObjectSecurity object is a directory object."""
        ...
    @property
    def OwnerModified(self):
        """Gets or sets a Boolean value that specifies whether the owner of the securable object has been modified."""
        ...
    ExceptionFromErrorCode = None

class CryptoKeySecurity(NativeObjectSecurity):
    """
    Provides the ability to control access to a cryptographic key object without direct manipulation of  an Access Control List (ACL).

    CryptoKeySecurity()

    CryptoKeySecurity(securityDescriptor: CommonSecurityDescriptor)
    """

    def AccessRuleFactory(self, identityReference, accessMask, isInherited, inheritanceFlags, propagationFlags, type):
        """
        AccessRuleFactory(self: CryptoKeySecurity, identityReference: IdentityReference, accessMask: int, isInherited: bool, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, type: AccessControlType) -> AccessRule

            Initializes a new instance of the System.Security.AccessControl.AccessRule class with the specified values.

            identityReference: The identity to which the access rule applies.  It must be an object that can be cast as a System.Security.Principal.SecurityIdentifier.

            accessMask: The access mask of this rule. The access mask is a 32-bit collection of anonymous bits, the meaning of which is defined by the individual integrators.

            isInherited: true if this rule is inherited from a parent container.

            inheritanceFlags: Specifies the inheritance properties of the access rule.

            propagationFlags: Specifies whether inherited access rules are automatically propagated. The propagation flags are ignored if inheritanceFlags is set to System.Security.AccessControl.InheritanceFlags.None.

            type: Specifies the valid access control type.

            Returns: The System.Security.AccessControl.AccessRule object that this method creates.
        """
        ...
    def AuditRuleFactory(self, identityReference, accessMask, isInherited, inheritanceFlags, propagationFlags, flags):
        """
        AuditRuleFactory(self: CryptoKeySecurity, identityReference: IdentityReference, accessMask: int, isInherited: bool, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, flags: AuditFlags) -> AuditRule

            Initializes a new instance of the System.Security.AccessControl.AuditRule class with the specified values.

            identityReference: The identity to which the audit rule applies.  It must be an object that can be cast as a System.Security.Principal.SecurityIdentifier.

            accessMask: The access mask of this rule. The access mask is a 32-bit collection of anonymous bits, the meaning of which is defined by the individual integrators.

            isInherited: ue if this rule is inherited from a parent container.

            inheritanceFlags: Specifies the inheritance properties of the audit rule.

            propagationFlags: Specifies whether inherited audit rules are automatically propagated. The propagation flags are ignored if inheritanceFlags is set to System.Security.AccessControl.InheritanceFlags.None.

            flags: Specifies the conditions for which the rule is audited.

            Returns: The System.Security.AccessControl.AuditRule object that this method creates.
        """
        ...
    @property
    def AccessRightType(self):
        """
        Gets the System.Type of the securable object associated with this System.Security.AccessControl.CryptoKeySecurity object.

        Get: AccessRightType(self: CryptoKeySecurity) -> Type
        """
        ...
    @property
    def AccessRulesModified(self):
        """Gets or sets a Boolean value that specifies whether the access rules associated with this System.Security.AccessControl.ObjectSecurity object have been modified."""
        ...
    @property
    def AccessRuleType(self):
        """
        Gets the System.Type of the object associated with the access rules of this System.Security.AccessControl.CryptoKeySecurity object. The System.Type object must be an object that can be cast as a System.Security.Principal.SecurityIdentifier object.

        Get: AccessRuleType(self: CryptoKeySecurity) -> Type
        """
        ...
    @property
    def AuditRulesModified(self):
        """Gets or sets a Boolean value that specifies whether the audit rules associated with this System.Security.AccessControl.ObjectSecurity object have been modified."""
        ...
    @property
    def AuditRuleType(self):
        """
        Gets the System.Type object associated with the audit rules of this System.Security.AccessControl.CryptoKeySecurity object. The System.Type object must be an object that can be cast as a System.Security.Principal.SecurityIdentifier object.

        Get: AuditRuleType(self: CryptoKeySecurity) -> Type
        """
        ...
    @property
    def GroupModified(self):
        """Gets or sets a Boolean value that specifies whether the group associated with the securable object has been modified."""
        ...
    @property
    def IsContainer(self):
        """Gets a Boolean value that specifies whether this System.Security.AccessControl.ObjectSecurity object is a container object."""
        ...
    @property
    def IsDS(self):
        """Gets a Boolean value that specifies whether this System.Security.AccessControl.ObjectSecurity object is a directory object."""
        ...
    @property
    def OwnerModified(self):
        """Gets or sets a Boolean value that specifies whether the owner of the securable object has been modified."""
        ...

class CustomAce(GenericAce):
    """
    Represents an Access Control Entry (ACE) that is not defined by one of the members of the System.Security.AccessControl.AceType enumeration.

    CustomAce(type: AceType, flags: AceFlags, opaque: Array[Byte])
    """

    def GetOpaque(self):
        """
        GetOpaque(self: CustomAce) -> Array[Byte]

            Returns the opaque data associated with this System.Security.AccessControl.CustomAce object.

            Returns: An array of byte values that represents the opaque data associated with this System.Security.AccessControl.CustomAce object.
        """
        ...
    def SetOpaque(self, opaque):
        """
        SetOpaque(self: CustomAce, opaque: Array[Byte])

            Sets the opaque callback data associated with this System.Security.AccessControl.CustomAce object.

            opaque: An array of byte values that represents the opaque callback data for this System.Security.AccessControl.CustomAce object.
        """
        ...
    @staticmethod  # known case of __new__
    def __new__(cls, type, flags, opaque):
        """__new__(cls: type, type: AceType, flags: AceFlags, opaque: Array[Byte])"""
        ...
    @property
    def BinaryLength(self):
        """
        Gets the length, in bytes, of the binary representation of the current System.Security.AccessControl.CustomAce object. This length should be used before marshaling the ACL into a binary array with the System.Security.AccessControl.CustomAce.GetBinaryForm(System.Byte[],System.Int32) method.

        Get: BinaryLength(self: CustomAce) -> int
        """
        ...
    @property
    def OpaqueLength(self):
        """
        Gets the length of the opaque data associated with this System.Security.AccessControl.CustomAce object.

        Get: OpaqueLength(self: CustomAce) -> int
        """
        ...
    MaxOpaqueLength = 65531

class DirectoryObjectSecurity(ObjectSecurity):
    """Provides the ability to control access to directory objects without direct manipulation of Access Control Lists (ACLs)."""

    def AddAccessRule(self, *args):  # cannot find CLR method
        """
        AddAccessRule(self: DirectoryObjectSecurity, rule: ObjectAccessRule)

            Adds the specified access rule to the Discretionary Access Control List (DACL) associated with this System.Security.AccessControl.DirectoryObjectSecurity object.

            rule: The access rule to add.
        """
        ...
    def AddAuditRule(self, *args):  # cannot find CLR method
        """
        AddAuditRule(self: DirectoryObjectSecurity, rule: ObjectAuditRule)

            Adds the specified audit rule to the System Access Control List (SACL) associated with this System.Security.AccessControl.DirectoryObjectSecurity object.

            rule: The audit rule to add.
        """
        ...
    def GetAccessRules(self, includeExplicit, includeInherited, targetType):
        """
        GetAccessRules(self: DirectoryObjectSecurity, includeExplicit: bool, includeInherited: bool, targetType: Type) -> AuthorizationRuleCollection

            Gets a collection of the access rules associated with the specified security identifier.

            includeExplicit: ue to include access rules explicitly set for the object.

            includeInherited: ue to include inherited access rules.

            targetType: The security identifier for which to retrieve access rules. This must be an object that can be cast as a System.Security.Principal.SecurityIdentifier object.

            Returns: The collection of access rules associated with the specified System.Security.Principal.SecurityIdentifier object.
        """
        ...
    def GetAuditRules(self, includeExplicit, includeInherited, targetType):
        """
        GetAuditRules(self: DirectoryObjectSecurity, includeExplicit: bool, includeInherited: bool, targetType: Type) -> AuthorizationRuleCollection

            Gets a collection of the audit rules associated with the specified security identifier.

            includeExplicit: ue to include audit rules explicitly set for the object.

            includeInherited: ue to include inherited audit rules.

            targetType: The security identifier for which to retrieve audit rules. This must be an object that can be cast as a System.Security.Principal.SecurityIdentifier object.

            Returns: The collection of audit rules associated with the specified System.Security.Principal.SecurityIdentifier object.
        """
        ...
    def RemoveAccessRule(self, *args):  # cannot find CLR method
        """
        RemoveAccessRule(self: DirectoryObjectSecurity, rule: ObjectAccessRule) -> bool

            Removes access rules that contain the same security identifier and access mask as the specified access rule from the Discretionary Access Control List (DACL) associated with this System.Security.AccessControl.DirectoryObjectSecurity

             object.

            rule: The access rule to remove.

            Returns: ue if the access rule was successfully removed; otherwise, lse.
        """
        ...
    def RemoveAccessRuleAll(self, *args):  # cannot find CLR method
        """
        RemoveAccessRuleAll(self: DirectoryObjectSecurity, rule: ObjectAccessRule)

            Removes all access rules that have the same security identifier as the specified access rule from the Discretionary Access Control List (DACL) associated with this System.Security.AccessControl.DirectoryObjectSecurity object.

            rule: The access rule to remove.
        """
        ...
    def RemoveAccessRuleSpecific(self, *args):  # cannot find CLR method
        """
        RemoveAccessRuleSpecific(self: DirectoryObjectSecurity, rule: ObjectAccessRule)

            Removes all access rules that exactly match the specified access rule from the Discretionary Access Control List (DACL) associated with this System.Security.AccessControl.DirectoryObjectSecurity object.

            rule: The access rule to remove.
        """
        ...
    def RemoveAuditRule(self, *args):  # cannot find CLR method
        """
        RemoveAuditRule(self: DirectoryObjectSecurity, rule: ObjectAuditRule) -> bool

            Removes audit rules that contain the same security identifier and access mask as the specified audit rule from the System Access Control List (SACL) associated with this System.Security.AccessControl.CommonObjectSecurity object.

            rule: The audit rule to remove.

            Returns: ue if the audit rule was successfully removed; otherwise, lse.
        """
        ...
    def RemoveAuditRuleAll(self, *args):  # cannot find CLR method
        """
        RemoveAuditRuleAll(self: DirectoryObjectSecurity, rule: ObjectAuditRule)

            Removes all audit rules that have the same security identifier as the specified audit rule from the System Access Control List (SACL) associated with this System.Security.AccessControl.DirectoryObjectSecurity object.

            rule: The audit rule to remove.
        """
        ...
    def RemoveAuditRuleSpecific(self, *args):  # cannot find CLR method
        """
        RemoveAuditRuleSpecific(self: DirectoryObjectSecurity, rule: ObjectAuditRule)

            Removes all audit rules that exactly match the specified audit rule from the System Access Control List (SACL) associated with this System.Security.AccessControl.DirectoryObjectSecurity object.

            rule: The audit rule to remove.
        """
        ...
    def ResetAccessRule(self, *args):  # cannot find CLR method
        """
        ResetAccessRule(self: DirectoryObjectSecurity, rule: ObjectAccessRule)

            Removes all access rules in the Discretionary Access Control List (DACL) associated with this System.Security.AccessControl.DirectoryObjectSecurity object and then adds the specified access rule.

            rule: The access rule to reset.
        """
        ...
    def SetAccessRule(self, *args):  # cannot find CLR method
        """
        SetAccessRule(self: DirectoryObjectSecurity, rule: ObjectAccessRule)

            Removes all access rules that contain the same security identifier and qualifier as the specified access rule in the Discretionary Access Control List (DACL) associated with this System.Security.AccessControl.DirectoryObjectSecurity

             object and then adds the specified access rule.

            rule: The access rule to set.
        """
        ...
    def SetAuditRule(self, *args):  # cannot find CLR method
        """
        SetAuditRule(self: DirectoryObjectSecurity, rule: ObjectAuditRule)

            Removes all audit rules that contain the same security identifier and qualifier as the specified audit rule in the System Access Control List (SACL) associated with this System.Security.AccessControl.DirectoryObjectSecurity object

             and then adds the specified audit rule.

            rule: The audit rule to set.
        """
        ...
    @property
    def AccessRulesModified(self):
        """Gets or sets a Boolean value that specifies whether the access rules associated with this System.Security.AccessControl.ObjectSecurity object have been modified."""
        ...
    @property
    def AuditRulesModified(self):
        """Gets or sets a Boolean value that specifies whether the audit rules associated with this System.Security.AccessControl.ObjectSecurity object have been modified."""
        ...
    @property
    def GroupModified(self):
        """Gets or sets a Boolean value that specifies whether the group associated with the securable object has been modified."""
        ...
    @property
    def IsContainer(self):
        """Gets a Boolean value that specifies whether this System.Security.AccessControl.ObjectSecurity object is a container object."""
        ...
    @property
    def IsDS(self):
        """Gets a Boolean value that specifies whether this System.Security.AccessControl.ObjectSecurity object is a directory object."""
        ...
    @property
    def OwnerModified(self):
        """Gets or sets a Boolean value that specifies whether the owner of the securable object has been modified."""
        ...

class FileSystemSecurity(NativeObjectSecurity):
    """Represents the access control and audit security for a file or directory."""

    def AccessRuleFactory(self, identityReference, accessMask, isInherited, inheritanceFlags, propagationFlags, type):
        """
        AccessRuleFactory(self: FileSystemSecurity, identityReference: IdentityReference, accessMask: int, isInherited: bool, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, type: AccessControlType) -> AccessRule

            Initializes a new instance of the System.Security.AccessControl.FileSystemAccessRule class that represents a new access control rule for the specified user, with the specified access rights, access control, and flags.

            identityReference: An System.Security.Principal.IdentityReference object that represents a user account.

            accessMask: An integer that specifies an access type.

            isInherited: ue if the access rule is inherited; otherwise, lse.

            inheritanceFlags: One of the System.Security.AccessControl.InheritanceFlags values that specifies how to propagate access masks to child objects.

            propagationFlags: One of the System.Security.AccessControl.PropagationFlags values that specifies how to propagate Access Control Entries (ACEs) to child objects.

            type: One of the System.Security.AccessControl.AccessControlType values that specifies whether access is allowed or denied.

            Returns: A new System.Security.AccessControl.FileSystemAccessRule object that represents a new access control rule for the specified user, with the specified access rights, access control, and flags.
        """
        ...
    def AuditRuleFactory(self, identityReference, accessMask, isInherited, inheritanceFlags, propagationFlags, flags):
        """
        AuditRuleFactory(self: FileSystemSecurity, identityReference: IdentityReference, accessMask: int, isInherited: bool, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, flags: AuditFlags) -> AuditRule

            Initializes a new instance of the System.Security.AccessControl.FileSystemAuditRule class representing the specified audit rule for the specified user.

            identityReference: An System.Security.Principal.IdentityReference object that represents a user account.

            accessMask: An integer that specifies an access type.

            isInherited: ue if the access rule is inherited; otherwise, lse.

            inheritanceFlags: One of the System.Security.AccessControl.InheritanceFlags values that specifies how to propagate access masks to child objects.

            propagationFlags: One of the System.Security.AccessControl.PropagationFlags values that specifies how to propagate Access Control Entries (ACEs) to child objects.

            flags: One of the System.Security.AccessControl.AuditFlags values that specifies the type of auditing to perform.

            Returns: A new System.Security.AccessControl.FileSystemAuditRule object representing the specified audit rule for the specified user.
        """
        ...
    @property
    def AccessRightType(self):
        """
        Gets the enumeration that the System.Security.AccessControl.FileSystemSecurity class uses to represent access rights.

        Get: AccessRightType(self: FileSystemSecurity) -> Type
        """
        ...
    @property
    def AccessRulesModified(self):
        """Gets or sets a Boolean value that specifies whether the access rules associated with this System.Security.AccessControl.ObjectSecurity object have been modified."""
        ...
    @property
    def AccessRuleType(self):
        """
        Gets the enumeration that the System.Security.AccessControl.FileSystemSecurity class uses to represent access rules.

        Get: AccessRuleType(self: FileSystemSecurity) -> Type
        """
        ...
    @property
    def AuditRulesModified(self):
        """Gets or sets a Boolean value that specifies whether the audit rules associated with this System.Security.AccessControl.ObjectSecurity object have been modified."""
        ...
    @property
    def AuditRuleType(self):
        """
        Gets the type that the System.Security.AccessControl.FileSystemSecurity class uses to represent audit rules.

        Get: AuditRuleType(self: FileSystemSecurity) -> Type
        """
        ...
    @property
    def GroupModified(self):
        """Gets or sets a Boolean value that specifies whether the group associated with the securable object has been modified."""
        ...
    @property
    def IsContainer(self):
        """Gets a Boolean value that specifies whether this System.Security.AccessControl.ObjectSecurity object is a container object."""
        ...
    @property
    def IsDS(self):
        """Gets a Boolean value that specifies whether this System.Security.AccessControl.ObjectSecurity object is a directory object."""
        ...
    @property
    def OwnerModified(self):
        """Gets or sets a Boolean value that specifies whether the owner of the securable object has been modified."""
        ...

class DirectorySecurity(FileSystemSecurity):
    """
    Represents the access control and audit security for a directory. This class cannot be inherited.

    DirectorySecurity()

    DirectorySecurity(name: str, includeSections: AccessControlSections)
    """

    @staticmethod  # known case of __new__
    def __new__(cls, name=None, includeSections=None):
        """
        __new__(cls: type)

        __new__(cls: type, name: str, includeSections: AccessControlSections)
        """
        ...
    @property
    def AccessRulesModified(self):
        """Gets or sets a Boolean value that specifies whether the access rules associated with this System.Security.AccessControl.ObjectSecurity object have been modified."""
        ...
    @property
    def AuditRulesModified(self):
        """Gets or sets a Boolean value that specifies whether the audit rules associated with this System.Security.AccessControl.ObjectSecurity object have been modified."""
        ...
    @property
    def GroupModified(self):
        """Gets or sets a Boolean value that specifies whether the group associated with the securable object has been modified."""
        ...
    @property
    def IsContainer(self):
        """Gets a Boolean value that specifies whether this System.Security.AccessControl.ObjectSecurity object is a container object."""
        ...
    @property
    def IsDS(self):
        """Gets a Boolean value that specifies whether this System.Security.AccessControl.ObjectSecurity object is a directory object."""
        ...
    @property
    def OwnerModified(self):
        """Gets or sets a Boolean value that specifies whether the owner of the securable object has been modified."""
        ...

class DiscretionaryAcl(CommonAcl):  # skipped bases: <type 'ICollection'>, <type 'IEnumerable'>
    """
    Represents a Discretionary Access Control List (DACL).

    DiscretionaryAcl(isContainer: bool, isDS: bool, capacity: int)

    DiscretionaryAcl(isContainer: bool, isDS: bool, revision: Byte, capacity: int)

    DiscretionaryAcl(isContainer: bool, isDS: bool, rawAcl: RawAcl)
    """

    def AddAccess(self, accessType, sid, *__args):
        """
        AddAccess(self: DiscretionaryAcl, accessType: AccessControlType, sid: SecurityIdentifier, accessMask: int, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags)

            Adds an Access Control Entry (ACE) with the specified settings to the current System.Security.AccessControl.DiscretionaryAcl object.

            accessType: The type of access control (allow or deny) to add.

            sid: The System.Security.Principal.SecurityIdentifier for which to add an ACE.

            accessMask: The access rule for the new ACE.

            inheritanceFlags: Flags that specify the inheritance properties of the new ACE.

            propagationFlags: Flags that specify the inheritance propagation properties for the new ACE.

        AddAccess(self: DiscretionaryAcl, accessType: AccessControlType, sid: SecurityIdentifier, rule: ObjectAccessRule)

            Adds an Access Control Entry (ACE) with the specified settings to the current System.Security.AccessControl.DiscretionaryAcl object.

            accessType: The type of access control (allow or deny) to add.

            sid: The System.Security.Principal.SecurityIdentifier for which to add an ACE.

            rule: The System.Security.AccessControl.ObjectAccessRule for the new access.

        AddAccess(self: DiscretionaryAcl, accessType: AccessControlType, sid: SecurityIdentifier, accessMask: int, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, objectFlags: ObjectAceFlags, objectType: Guid, inheritedObjectType: Guid)

            Adds an Access Control Entry (ACE) with the specified settings to the current System.Security.AccessControl.DiscretionaryAcl object. Use this method for directory object Access Control Lists (ACLs) when specifying the object type or

             the inherited object type for the new ACE.

            accessType: The type of access control (allow or deny) to add.

            sid: The System.Security.Principal.SecurityIdentifier for which to add an ACE.

            accessMask: The access rule for the new ACE.

            inheritanceFlags: Flags that specify the inheritance properties of the new ACE.

            propagationFlags: Flags that specify the inheritance propagation properties for the new ACE.

            objectFlags: Flags that specify if the objectType and inheritedObjectType parameters contain non-ll values.

            objectType: The identity of the class of objects to which the new ACE applies.

            inheritedObjectType: The identity of the class of child objects which can inherit the new ACE.
        """
        ...
    def RemoveAccess(self, accessType, sid, *__args):
        """
        RemoveAccess(self: DiscretionaryAcl, accessType: AccessControlType, sid: SecurityIdentifier, accessMask: int, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags) -> bool

            Removes the specified access control rule from the current System.Security.AccessControl.DiscretionaryAcl object.

            accessType: The type of access control (allow or deny) to remove.

            sid: The System.Security.Principal.SecurityIdentifier for which to remove an access control rule.

            accessMask: The access mask for the rule to be removed.

            inheritanceFlags: Flags that specify the inheritance properties of the rule to be removed.

            propagationFlags: Flags that specify the inheritance propagation properties for the rule to be removed.

            Returns: ue if this method successfully removes the specified access; otherwise, lse.

        RemoveAccess(self: DiscretionaryAcl, accessType: AccessControlType, sid: SecurityIdentifier, rule: ObjectAccessRule) -> bool

            Removes the specified access control rule from the current System.Security.AccessControl.DiscretionaryAcl object.

            accessType: The type of access control (allow or deny) to remove.

            sid: The System.Security.Principal.SecurityIdentifier for which to remove an access control rule.

            rule: The System.Security.AccessControl.ObjectAccessRule for which to remove access.

            Returns: Returns System.Boolean.

        RemoveAccess(self: DiscretionaryAcl, accessType: AccessControlType, sid: SecurityIdentifier, accessMask: int, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, objectFlags: ObjectAceFlags, objectType: Guid, inheritedObjectType: Guid) -> bool

            Removes the specified access control rule from the current System.Security.AccessControl.DiscretionaryAcl object. Use this method for directory object Access Control Lists (ACLs) when specifying the object type or the inherited

             object type.

            accessType: The type of access control (allow or deny) to remove.

            sid: The System.Security.Principal.SecurityIdentifier for which to remove an access control rule.

            accessMask: The access mask for the access control rule to be removed.

            inheritanceFlags: Flags that specify the inheritance properties of the access control rule to be removed.

            propagationFlags: Flags that specify the inheritance propagation properties for the access control rule to be removed.

            objectFlags: Flags that specify if the objectType and inheritedObjectType parameters contain non-ll values.

            objectType: The identity of the class of objects to which the removed access control rule applies.

            inheritedObjectType: The identity of the class of child objects which can inherit the removed access control rule.

            Returns: ue if this method successfully removes the specified access; otherwise, lse.
        """
        ...
    def RemoveAccessSpecific(self, accessType, sid, *__args):
        """
        RemoveAccessSpecific(self: DiscretionaryAcl, accessType: AccessControlType, sid: SecurityIdentifier, accessMask: int, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags)

            Removes the specified Access Control Entry (ACE) from the current System.Security.AccessControl.DiscretionaryAcl object.

            accessType: The type of access control (allow or deny) to remove.

            sid: The System.Security.Principal.SecurityIdentifier for which to remove an ACE.

            accessMask: The access mask for the ACE to be removed.

            inheritanceFlags: Flags that specify the inheritance properties of the ACE to be removed.

            propagationFlags: Flags that specify the inheritance propagation properties for the ACE to be removed.

        RemoveAccessSpecific(self: DiscretionaryAcl, accessType: AccessControlType, sid: SecurityIdentifier, rule: ObjectAccessRule)

            Removes the specified Access Control Entry (ACE) from the current System.Security.AccessControl.DiscretionaryAcl object.

            accessType: The type of access control (allow or deny) to remove.

            sid: The System.Security.Principal.SecurityIdentifier for which to remove an ACE.

            rule: The System.Security.AccessControl.ObjectAccessRule for which to remove access.

        RemoveAccessSpecific(self: DiscretionaryAcl, accessType: AccessControlType, sid: SecurityIdentifier, accessMask: int, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, objectFlags: ObjectAceFlags, objectType: Guid, inheritedObjectType: Guid)

            Removes the specified Access Control Entry (ACE) from the current System.Security.AccessControl.DiscretionaryAcl object. Use this method for directory object Access Control Lists (ACLs) when specifying the object type or the

             inherited object type for the ACE to be removed.

            accessType: The type of access control (allow or deny) to remove.

            sid: The System.Security.Principal.SecurityIdentifier for which to remove an ACE.

            accessMask: The access mask for the ACE to be removed.

            inheritanceFlags: Flags that specify the inheritance properties of the ACE to be removed.

            propagationFlags: Flags that specify the inheritance propagation properties for the ACE to be removed.

            objectFlags: Flags that specify if the objectType and inheritedObjectType parameters contain non-ll values.

            objectType: The identity of the class of objects to which the removed ACE applies.

            inheritedObjectType: The identity of the class of child objects which can inherit the removed ACE.
        """
        ...
    def SetAccess(self, accessType, sid, *__args):
        """
        SetAccess(self: DiscretionaryAcl, accessType: AccessControlType, sid: SecurityIdentifier, accessMask: int, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags)

            Sets the specified access control for the specified System.Security.Principal.SecurityIdentifier object.

            accessType: The type of access control (allow or deny) to set.

            sid: The System.Security.Principal.SecurityIdentifier for which to set an ACE.

            accessMask: The access rule for the new ACE.

            inheritanceFlags: Flags that specify the inheritance properties of the new ACE.

            propagationFlags: Flags that specify the inheritance propagation properties for the new ACE.

        SetAccess(self: DiscretionaryAcl, accessType: AccessControlType, sid: SecurityIdentifier, rule: ObjectAccessRule)

            Sets the specified access control for the specified System.Security.Principal.SecurityIdentifier object.

            accessType: The type of access control (allow or deny) to set.

            sid: The System.Security.Principal.SecurityIdentifier for which to set an ACE.

            rule: The System.Security.AccessControl.ObjectAccessRule for which to set access.

        SetAccess(self: DiscretionaryAcl, accessType: AccessControlType, sid: SecurityIdentifier, accessMask: int, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, objectFlags: ObjectAceFlags, objectType: Guid, inheritedObjectType: Guid)

            Sets the specified access control for the specified System.Security.Principal.SecurityIdentifier object.

            accessType: The type of access control (allow or deny) to set.

            sid: The System.Security.Principal.SecurityIdentifier for which to set an ACE.

            accessMask: The access rule for the new ACE.

            inheritanceFlags: Flags that specify the inheritance properties of the new ACE.

            propagationFlags: Flags that specify the inheritance propagation properties for the new ACE.

            objectFlags: Flags that specify if the objectType and inheritedObjectType parameters contain non-ll values.

            objectType: The identity of the class of objects to which the new ACE applies.

            inheritedObjectType: The identity of the class of child objects which can inherit the new ACE.
        """
        ...
    @staticmethod  # known case of __new__
    def __new__(cls, isContainer, isDS, *__args):
        """
        __new__(cls: type, isContainer: bool, isDS: bool, capacity: int)

        __new__(cls: type, isContainer: bool, isDS: bool, revision: Byte, capacity: int)

        __new__(cls: type, isContainer: bool, isDS: bool, rawAcl: RawAcl)
        """
        ...

class EventWaitHandleAccessRule(AccessRule):
    """
    Represents a set of access rights allowed or denied for a user or group. This class cannot be inherited.

    EventWaitHandleAccessRule(identity: IdentityReference, eventRights: EventWaitHandleRights, type: AccessControlType)

    EventWaitHandleAccessRule(identity: str, eventRights: EventWaitHandleRights, type: AccessControlType)
    """

    @property
    def AccessMask(self):
        """Gets the access mask for this rule."""
        ...
    @property
    def EventWaitHandleRights(self):
        """
        Gets the rights allowed or denied by the access rule.

        Get: EventWaitHandleRights(self: EventWaitHandleAccessRule) -> EventWaitHandleRights
        """
        ...

class EventWaitHandleAuditRule(AuditRule):
    """
    Represents a set of access rights to be audited for a user or group. This class cannot be inherited.

    EventWaitHandleAuditRule(identity: IdentityReference, eventRights: EventWaitHandleRights, flags: AuditFlags)
    """

    @property
    def AccessMask(self):
        """Gets the access mask for this rule."""
        ...
    @property
    def EventWaitHandleRights(self):
        """
        Gets the access rights affected by the audit rule.

        Get: EventWaitHandleRights(self: EventWaitHandleAuditRule) -> EventWaitHandleRights
        """
        ...

class EventWaitHandleRights(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies the access control rights that can be applied to named system event objects.

    enum (flags) EventWaitHandleRights, values: ChangePermissions (262144), Delete (65536), FullControl (2031619), Modify (2), ReadPermissions (131072), Synchronize (1048576), TakeOwnership (524288)
    """

    ChangePermissions = None
    Delete = None
    FullControl = None
    Modify = None
    ReadPermissions = None
    Synchronize = None
    TakeOwnership = None
    value__ = None

class EventWaitHandleSecurity(NativeObjectSecurity):
    """
    Represents the Windows access control security applied to a named system wait handle. This class cannot be inherited.

    EventWaitHandleSecurity()
    """

    def AccessRuleFactory(self, identityReference, accessMask, isInherited, inheritanceFlags, propagationFlags, type):
        """
        AccessRuleFactory(self: EventWaitHandleSecurity, identityReference: IdentityReference, accessMask: int, isInherited: bool, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, type: AccessControlType) -> AccessRule

            Creates a new access control rule for the specified user, with the specified access rights, access control, and flags.

            identityReference: An System.Security.Principal.IdentityReference that identifies the user or group the rule applies to.

            accessMask: A bitwise combination of System.Security.AccessControl.EventWaitHandleRights values specifying the access rights to allow or deny, cast to an integer.

            isInherited: Meaningless for named wait handles, because they have no hierarchy.

            inheritanceFlags: Meaningless for named wait handles, because they have no hierarchy.

            propagationFlags: Meaningless for named wait handles, because they have no hierarchy.

            type: One of the System.Security.AccessControl.AccessControlType values specifying whether the rights are allowed or denied.

            Returns: An System.Security.AccessControl.EventWaitHandleAccessRule object representing the specified rights for the specified user.
        """
        ...
    def AuditRuleFactory(self, identityReference, accessMask, isInherited, inheritanceFlags, propagationFlags, flags):
        """
        AuditRuleFactory(self: EventWaitHandleSecurity, identityReference: IdentityReference, accessMask: int, isInherited: bool, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, flags: AuditFlags) -> AuditRule

            Creates a new audit rule, specifying the user the rule applies to, the access rights to audit, and the outcome that triggers the audit rule.

            identityReference: An System.Security.Principal.IdentityReference that identifies the user or group the rule applies to.

            accessMask: A bitwise combination of System.Security.AccessControl.EventWaitHandleRights values specifying the access rights to audit, cast to an integer.

            isInherited: Meaningless for named wait handles, because they have no hierarchy.

            inheritanceFlags: Meaningless for named wait handles, because they have no hierarchy.

            propagationFlags: Meaningless for named wait handles, because they have no hierarchy.

            flags: A bitwise combination of System.Security.AccessControl.AuditFlags values specifying whether to audit successful access, failed access, or both.

            Returns: An System.Security.AccessControl.EventWaitHandleAuditRule object representing the specified audit rule for the specified user. The return type of the method is the base class, System.Security.AccessControl.AuditRule, but the return

             value can be cast safely to the derived class.
        """
        ...
    @property
    def AccessRightType(self):
        """
        Gets the enumeration type that the System.Security.AccessControl.EventWaitHandleSecurity class uses to represent access rights.

        Get: AccessRightType(self: EventWaitHandleSecurity) -> Type
        """
        ...
    @property
    def AccessRulesModified(self):
        """Gets or sets a Boolean value that specifies whether the access rules associated with this System.Security.AccessControl.ObjectSecurity object have been modified."""
        ...
    @property
    def AccessRuleType(self):
        """
        Gets the type that the System.Security.AccessControl.EventWaitHandleSecurity class uses to represent access rules.

        Get: AccessRuleType(self: EventWaitHandleSecurity) -> Type
        """
        ...
    @property
    def AuditRulesModified(self):
        """Gets or sets a Boolean value that specifies whether the audit rules associated with this System.Security.AccessControl.ObjectSecurity object have been modified."""
        ...
    @property
    def AuditRuleType(self):
        """
        Gets the type that the System.Security.AccessControl.EventWaitHandleSecurity class uses to represent audit rules.

        Get: AuditRuleType(self: EventWaitHandleSecurity) -> Type
        """
        ...
    @property
    def GroupModified(self):
        """Gets or sets a Boolean value that specifies whether the group associated with the securable object has been modified."""
        ...
    @property
    def IsContainer(self):
        """Gets a Boolean value that specifies whether this System.Security.AccessControl.ObjectSecurity object is a container object."""
        ...
    @property
    def IsDS(self):
        """Gets a Boolean value that specifies whether this System.Security.AccessControl.ObjectSecurity object is a directory object."""
        ...
    @property
    def OwnerModified(self):
        """Gets or sets a Boolean value that specifies whether the owner of the securable object has been modified."""
        ...

class FileSecurity(FileSystemSecurity):
    """
    Represents the access control and audit security for a file. This class cannot be inherited.

    FileSecurity()

    FileSecurity(fileName: str, includeSections: AccessControlSections)
    """

    @staticmethod  # known case of __new__
    def __new__(cls, fileName=None, includeSections=None):
        """
        __new__(cls: type)

        __new__(cls: type, fileName: str, includeSections: AccessControlSections)
        """
        ...
    @property
    def AccessRulesModified(self):
        """Gets or sets a Boolean value that specifies whether the access rules associated with this System.Security.AccessControl.ObjectSecurity object have been modified."""
        ...
    @property
    def AuditRulesModified(self):
        """Gets or sets a Boolean value that specifies whether the audit rules associated with this System.Security.AccessControl.ObjectSecurity object have been modified."""
        ...
    @property
    def GroupModified(self):
        """Gets or sets a Boolean value that specifies whether the group associated with the securable object has been modified."""
        ...
    @property
    def IsContainer(self):
        """Gets a Boolean value that specifies whether this System.Security.AccessControl.ObjectSecurity object is a container object."""
        ...
    @property
    def IsDS(self):
        """Gets a Boolean value that specifies whether this System.Security.AccessControl.ObjectSecurity object is a directory object."""
        ...
    @property
    def OwnerModified(self):
        """Gets or sets a Boolean value that specifies whether the owner of the securable object has been modified."""
        ...

class FileSystemAccessRule(AccessRule):
    """
    Represents an abstraction of an access control entry (ACE) that defines an access rule for a file or directory. This class cannot be inherited.

    FileSystemAccessRule(identity: IdentityReference, fileSystemRights: FileSystemRights, type: AccessControlType)

    FileSystemAccessRule(identity: str, fileSystemRights: FileSystemRights, type: AccessControlType)

    FileSystemAccessRule(identity: IdentityReference, fileSystemRights: FileSystemRights, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, type: AccessControlType)

    FileSystemAccessRule(identity: str, fileSystemRights: FileSystemRights, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, type: AccessControlType)
    """

    @property
    def AccessMask(self):
        """Gets the access mask for this rule."""
        ...
    @property
    def FileSystemRights(self):
        """
        Gets the System.Security.AccessControl.FileSystemRights flags associated with the current System.Security.AccessControl.FileSystemAccessRule object.

        Get: FileSystemRights(self: FileSystemAccessRule) -> FileSystemRights
        """
        ...

class FileSystemAuditRule(AuditRule):
    """
    Represents an abstraction of an access control entry (ACE) that defines an audit rule for a file or directory. This class cannot be inherited.

    FileSystemAuditRule(identity: IdentityReference, fileSystemRights: FileSystemRights, flags: AuditFlags)

    FileSystemAuditRule(identity: IdentityReference, fileSystemRights: FileSystemRights, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, flags: AuditFlags)

    FileSystemAuditRule(identity: str, fileSystemRights: FileSystemRights, flags: AuditFlags)

    FileSystemAuditRule(identity: str, fileSystemRights: FileSystemRights, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, flags: AuditFlags)
    """

    @property
    def AccessMask(self):
        """Gets the access mask for this rule."""
        ...
    @property
    def FileSystemRights(self):
        """
        Gets the System.Security.AccessControl.FileSystemRights flags associated with the current System.Security.AccessControl.FileSystemAuditRule object.

        Get: FileSystemRights(self: FileSystemAuditRule) -> FileSystemRights
        """
        ...

class FileSystemRights(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Defines the access rights to use when creating access and audit rules.

    enum (flags) FileSystemRights, values: AppendData (4), ChangePermissions (262144), CreateDirectories (4), CreateFiles (2), Delete (65536), DeleteSubdirectoriesAndFiles (64), ExecuteFile (32), FullControl (2032127), ListDirectory (1), Modify (197055), Read (131209), ReadAndExecute (131241), ReadAttributes (128), ReadData (1), ReadExtendedAttributes (8), ReadPermissions (131072), Synchronize (1048576), TakeOwnership (524288), Traverse (32), Write (278), WriteAttributes (256), WriteData (2), WriteExtendedAttributes (16)
    """

    AppendData = None
    ChangePermissions = None
    CreateDirectories = None
    CreateFiles = None
    Delete = None
    DeleteSubdirectoriesAndFiles = None
    ExecuteFile = None
    FullControl = None
    ListDirectory = None
    Modify = None
    Read = None
    ReadAndExecute = None
    ReadAttributes = None
    ReadData = None
    ReadExtendedAttributes = None
    ReadPermissions = None
    Synchronize = None
    TakeOwnership = None
    Traverse = None
    value__ = None
    Write = None
    WriteAttributes = None
    WriteData = None
    WriteExtendedAttributes = None

class InheritanceFlags(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Inheritance flags specify the semantics of inheritance for access control entries (ACEs).

    enum (flags) InheritanceFlags, values: ContainerInherit (1), None (0), ObjectInherit (2)
    """

    ContainerInherit = None

    ObjectInherit = None
    value__ = None

class MutexAccessRule(AccessRule):
    """
    Represents a set of access rights allowed or denied for a user or group. This class cannot be inherited.

    MutexAccessRule(identity: IdentityReference, eventRights: MutexRights, type: AccessControlType)

    MutexAccessRule(identity: str, eventRights: MutexRights, type: AccessControlType)
    """

    @property
    def AccessMask(self):
        """Gets the access mask for this rule."""
        ...
    @property
    def MutexRights(self):
        """
        Gets the rights allowed or denied by the access rule.

        Get: MutexRights(self: MutexAccessRule) -> MutexRights
        """
        ...

class MutexAuditRule(AuditRule):
    """
    Represents a set of access rights to be audited for a user or group. This class cannot be inherited.

    MutexAuditRule(identity: IdentityReference, eventRights: MutexRights, flags: AuditFlags)
    """

    @property
    def AccessMask(self):
        """Gets the access mask for this rule."""
        ...
    @property
    def MutexRights(self):
        """
        Gets the access rights affected by the audit rule.

        Get: MutexRights(self: MutexAuditRule) -> MutexRights
        """
        ...

class MutexRights(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies the access control rights that can be applied to named system mutex objects.

    enum (flags) MutexRights, values: ChangePermissions (262144), Delete (65536), FullControl (2031617), Modify (1), ReadPermissions (131072), Synchronize (1048576), TakeOwnership (524288)
    """

    ChangePermissions = None
    Delete = None
    FullControl = None
    Modify = None
    ReadPermissions = None
    Synchronize = None
    TakeOwnership = None
    value__ = None

class MutexSecurity(NativeObjectSecurity):
    """
    Represents the Windows access control security for a named mutex. This class cannot be inherited.

    MutexSecurity()

    MutexSecurity(name: str, includeSections: AccessControlSections)
    """

    def AccessRuleFactory(self, identityReference, accessMask, isInherited, inheritanceFlags, propagationFlags, type):
        """
        AccessRuleFactory(self: MutexSecurity, identityReference: IdentityReference, accessMask: int, isInherited: bool, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, type: AccessControlType) -> AccessRule

            Creates a new access control rule for the specified user, with the specified access rights, access control, and flags.

            identityReference: An System.Security.Principal.IdentityReference that identifies the user or group the rule applies to.

            accessMask: A bitwise combination of System.Security.AccessControl.MutexRights values specifying the access rights to allow or deny, cast to an integer.

            isInherited: Meaningless for named mutexes, because they have no hierarchy.

            inheritanceFlags: Meaningless for named mutexes, because they have no hierarchy.

            propagationFlags: Meaningless for named mutexes, because they have no hierarchy.

            type: One of the System.Security.AccessControl.AccessControlType values specifying whether the rights are allowed or denied.

            Returns: A System.Security.AccessControl.MutexAccessRule object representing the specified rights for the specified user.
        """
        ...
    def AuditRuleFactory(self, identityReference, accessMask, isInherited, inheritanceFlags, propagationFlags, flags):
        """
        AuditRuleFactory(self: MutexSecurity, identityReference: IdentityReference, accessMask: int, isInherited: bool, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, flags: AuditFlags) -> AuditRule

            Creates a new audit rule, specifying the user the rule applies to, the access rights to audit, and the outcome that triggers the audit rule.

            identityReference: An System.Security.Principal.IdentityReference that identifies the user or group the rule applies to.

            accessMask: A bitwise combination of System.Security.AccessControl.MutexRights values specifying the access rights to audit, cast to an integer.

            isInherited: Meaningless for named wait handles, because they have no hierarchy.

            inheritanceFlags: Meaningless for named wait handles, because they have no hierarchy.

            propagationFlags: Meaningless for named wait handles, because they have no hierarchy.

            flags: A bitwise combination of System.Security.AccessControl.AuditFlags values that specify whether to audit successful access, failed access, or both.

            Returns: A System.Security.AccessControl.MutexAuditRule object representing the specified audit rule for the specified user. The return type of the method is the base class, System.Security.AccessControl.AuditRule, but the return value can

             be cast safely to the derived class.
        """
        ...
    @property
    def AccessRightType(self):
        """
        Gets the enumeration that the System.Security.AccessControl.MutexSecurity class uses to represent access rights.

        Get: AccessRightType(self: MutexSecurity) -> Type
        """
        ...
    @property
    def AccessRulesModified(self):
        """Gets or sets a Boolean value that specifies whether the access rules associated with this System.Security.AccessControl.ObjectSecurity object have been modified."""
        ...
    @property
    def AccessRuleType(self):
        """
        Gets the type that the System.Security.AccessControl.MutexSecurity class uses to represent access rules.

        Get: AccessRuleType(self: MutexSecurity) -> Type
        """
        ...
    @property
    def AuditRulesModified(self):
        """Gets or sets a Boolean value that specifies whether the audit rules associated with this System.Security.AccessControl.ObjectSecurity object have been modified."""
        ...
    @property
    def AuditRuleType(self):
        """
        Gets the type that the System.Security.AccessControl.MutexSecurity class uses to represent audit rules.

        Get: AuditRuleType(self: MutexSecurity) -> Type
        """
        ...
    @property
    def GroupModified(self):
        """Gets or sets a Boolean value that specifies whether the group associated with the securable object has been modified."""
        ...
    @property
    def IsContainer(self):
        """Gets a Boolean value that specifies whether this System.Security.AccessControl.ObjectSecurity object is a container object."""
        ...
    @property
    def IsDS(self):
        """Gets a Boolean value that specifies whether this System.Security.AccessControl.ObjectSecurity object is a directory object."""
        ...
    @property
    def OwnerModified(self):
        """Gets or sets a Boolean value that specifies whether the owner of the securable object has been modified."""
        ...

class ObjectAccessRule(AccessRule):
    """Represents a combination of a user's identity, an access mask, and an access control type (allow or deny). An System.Security.AccessControl.ObjectAccessRule object also contains information about the type of object to which the rule applies, the type of child object that can inherit the rule, how the rule is inherited by child objects, and how that inheritance is propagated."""

    @property
    def AccessMask(self):
        """Gets the access mask for this rule."""
        ...
    @property
    def InheritedObjectType(self):
        """
        Gets the type of child object that can inherit the System.Security.AccessControl.ObjectAccessRule object.

        Get: InheritedObjectType(self: ObjectAccessRule) -> Guid
        """
        ...
    @property
    def ObjectFlags(self):
        """
        Gets flags that specify if the System.Security.AccessControl.ObjectAccessRule.ObjectType and System.Security.AccessControl.ObjectAccessRule.InheritedObjectType properties of the System.Security.AccessControl.ObjectAccessRule object contain valid values.

        Get: ObjectFlags(self: ObjectAccessRule) -> ObjectAceFlags
        """
        ...
    @property
    def ObjectType(self):
        """
        Gets the type of object to which the System.Security.AccessControl.ObjectAccessRule applies.

        Get: ObjectType(self: ObjectAccessRule) -> Guid
        """
        ...

class ObjectAce(QualifiedAce):
    """
    Controls access to Directory Services objects. This class represents an Access Control Entry (ACE) associated with a directory object.

    ObjectAce(aceFlags: AceFlags, qualifier: AceQualifier, accessMask: int, sid: SecurityIdentifier, flags: ObjectAceFlags, type: Guid, inheritedType: Guid, isCallback: bool, opaque: Array[Byte])
    """

    def GetBinaryForm(self, binaryForm, offset):
        """
        GetBinaryForm(self: ObjectAce, binaryForm: Array[Byte], offset: int)

            Marshals the contents of the System.Security.AccessControl.ObjectAce object into the specified byte array beginning at the specified offset.

            binaryForm: The byte array into which the contents of the System.Security.AccessControl.ObjectAce is marshaled.

            offset: The offset at which to start marshaling.
        """
        ...
    @staticmethod
    def MaxOpaqueLength(isCallback):
        """
        MaxOpaqueLength(isCallback: bool) -> int

            Returns the maximum allowed length, in bytes, of an opaque data BLOB for callback Access Control Entries (ACEs).

            isCallback: True if the System.Security.AccessControl.ObjectAce is a callback ACE type.

            Returns: The maximum allowed length, in bytes, of an opaque data BLOB for callback Access Control Entries (ACEs).
        """
        ...
    @staticmethod  # known case of __new__
    def __new__(cls, aceFlags, qualifier, accessMask, sid, flags, type, inheritedType, isCallback, opaque):
        """__new__(cls: type, aceFlags: AceFlags, qualifier: AceQualifier, accessMask: int, sid: SecurityIdentifier, flags: ObjectAceFlags, type: Guid, inheritedType: Guid, isCallback: bool, opaque: Array[Byte])"""
        ...
    @property
    def BinaryLength(self):
        """
        Gets the length, in bytes, of the binary representation of the current System.Security.AccessControl.ObjectAce object. This length should be used before marshaling the ACL into a binary array with the System.Security.AccessControl.ObjectAce.GetBinaryForm(System.Byte[],System.Int32) method.

        Get: BinaryLength(self: ObjectAce) -> int
        """
        ...
    @property
    def InheritedObjectAceType(self):
        """
        Gets or sets the GUID of the object type that can inherit the Access Control Entry (ACE) that this System.Security.AccessControl.ObjectAce object represents.

        Get: InheritedObjectAceType(self: ObjectAce) -> Guid

        Set: InheritedObjectAceType(self: ObjectAce) = value
        """
        ...
    @property
    def ObjectAceFlags(self):
        """
        Gets or sets flags that specify whether the System.Security.AccessControl.ObjectAce.ObjectAceType and System.Security.AccessControl.ObjectAce.InheritedObjectAceType properties contain values that identify valid object types.

        Get: ObjectAceFlags(self: ObjectAce) -> ObjectAceFlags

        Set: ObjectAceFlags(self: ObjectAce) = value
        """
        ...
    @property
    def ObjectAceType(self):
        """
        Gets or sets the GUID of the object type associated with this System.Security.AccessControl.ObjectAce object.

        Get: ObjectAceType(self: ObjectAce) -> Guid

        Set: ObjectAceType(self: ObjectAce) = value
        """
        ...

class ObjectAceFlags(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies the presence of object types for Access Control Entries (ACEs).

    enum (flags) ObjectAceFlags, values: InheritedObjectAceTypePresent (2), None (0), ObjectAceTypePresent (1)
    """

    InheritedObjectAceTypePresent = None

    ObjectAceTypePresent = None
    value__ = None

class ObjectAuditRule(AuditRule):
    """Represents a combination of a user's identity, an access mask, and audit conditions. An System.Security.AccessControl.ObjectAuditRule object also contains information about the type of object to which the rule applies, the type of child object that can inherit the rule, how the rule is inherited by child objects, and how that inheritance is propagated."""

    @property
    def AccessMask(self):
        """Gets the access mask for this rule."""
        ...
    @property
    def InheritedObjectType(self):
        """
        Gets the type of child object that can inherit the System.Security.AccessControl.ObjectAuditRule object.

        Get: InheritedObjectType(self: ObjectAuditRule) -> Guid
        """
        ...
    @property
    def ObjectFlags(self):
        """
        System.Security.AccessControl.ObjectAuditRule.ObjectType and System.Security.AccessControl.ObjectAuditRule.InheritedObjectType properties of the System.Security.AccessControl.ObjectAuditRule object contain valid values.

        Get: ObjectFlags(self: ObjectAuditRule) -> ObjectAceFlags
        """
        ...
    @property
    def ObjectType(self):
        """
        Gets the type of object to which the System.Security.AccessControl.ObjectAuditRule applies.

        Get: ObjectType(self: ObjectAuditRule) -> Guid
        """
        ...

class ObjectSecurity:
    """Provides the ability to control access to objects without direct manipulation of Access Control Lists (ACLs). This class is the abstract base class for the System.Security.AccessControl.CommonObjectSecurity and System.Security.AccessControl.DirectoryObjectSecurity classes."""

    def AccessRuleFactory(self, identityReference, accessMask, isInherited, inheritanceFlags, propagationFlags, type):
        """
        AccessRuleFactory(self: ObjectSecurity, identityReference: IdentityReference, accessMask: int, isInherited: bool, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, type: AccessControlType) -> AccessRule

            Initializes a new instance of the System.Security.AccessControl.AccessRule class with the specified values.

            identityReference: The identity to which the access rule applies.  It must be an object that can be cast as a System.Security.Principal.SecurityIdentifier.

            accessMask: The access mask of this rule. The access mask is a 32-bit collection of anonymous bits, the meaning of which is defined by the individual integrators.

            isInherited: true if this rule is inherited from a parent container.

            inheritanceFlags: Specifies the inheritance properties of the access rule.

            propagationFlags: Specifies whether inherited access rules are automatically propagated. The propagation flags are ignored if inheritanceFlags is set to System.Security.AccessControl.InheritanceFlags.None.

            type: Specifies the valid access control type.

            Returns: The System.Security.AccessControl.AccessRule object that this method creates.
        """
        ...
    def AuditRuleFactory(self, identityReference, accessMask, isInherited, inheritanceFlags, propagationFlags, flags):
        """
        AuditRuleFactory(self: ObjectSecurity, identityReference: IdentityReference, accessMask: int, isInherited: bool, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, flags: AuditFlags) -> AuditRule

            Initializes a new instance of the System.Security.AccessControl.AuditRule class with the specified values.

            identityReference: The identity to which the audit rule applies.  It must be an object that can be cast as a System.Security.Principal.SecurityIdentifier.

            accessMask: The access mask of this rule. The access mask is a 32-bit collection of anonymous bits, the meaning of which is defined by the individual integrators.

            isInherited: ue if this rule is inherited from a parent container.

            inheritanceFlags: Specifies the inheritance properties of the audit rule.

            propagationFlags: Specifies whether inherited audit rules are automatically propagated. The propagation flags are ignored if inheritanceFlags is set to System.Security.AccessControl.InheritanceFlags.None.

            flags: Specifies the conditions for which the rule is audited.

            Returns: The System.Security.AccessControl.AuditRule object that this method creates.
        """
        ...
    def GetGroup(self, targetType):
        """
        GetGroup(self: ObjectSecurity, targetType: Type) -> IdentityReference

            Gets the primary group associated with the specified owner.

            targetType: The owner for which to get the primary group.

            Returns: The primary group associated with the specified owner.
        """
        ...
    def GetOwner(self, targetType):
        """
        GetOwner(self: ObjectSecurity, targetType: Type) -> IdentityReference

            Gets the owner associated with the specified primary group.

            targetType: The primary group for which to get the owner.

            Returns: The owner associated with the specified group.
        """
        ...
    def GetSecurityDescriptorBinaryForm(self):
        """
        GetSecurityDescriptorBinaryForm(self: ObjectSecurity) -> Array[Byte]

            Returns an array of byte values that represents the security descriptor information for this System.Security.AccessControl.ObjectSecurity object.

            Returns: An array of byte values that represents the security descriptor for this System.Security.AccessControl.ObjectSecurity object. This method returns ll if there is no security information in this

             System.Security.AccessControl.ObjectSecurity object.
        """
        ...
    def GetSecurityDescriptorSddlForm(self, includeSections):
        """
        GetSecurityDescriptorSddlForm(self: ObjectSecurity, includeSections: AccessControlSections) -> str

            Returns the Security Descriptor Definition Language (SDDL) representation of the specified sections of the security descriptor associated with this System.Security.AccessControl.ObjectSecurity object.

            includeSections: Specifies which sections (access rules, audit rules, primary group, owner) of the security descriptor to get.

            Returns: The SDDL representation of the specified sections of the security descriptor associated with this System.Security.AccessControl.ObjectSecurity object.
        """
        ...
    @staticmethod
    def IsSddlConversionSupported():
        """
        IsSddlConversionSupported() -> bool

            Returns a Boolean value that specifies whether the security descriptor associated with this  System.Security.AccessControl.ObjectSecurity object can be converted to the Security Descriptor Definition Language (SDDL) format.

            Returns: ue if the security descriptor associated with this  System.Security.AccessControl.ObjectSecurity object can be converted to the Security Descriptor Definition Language (SDDL) format; otherwise, lse.
        """
        ...
    # Error generating skeleton for function ModifyAccess: 'type' object has no attribute '__bases__'

    def ModifyAccessRule(self, modification, rule, modified):
        """
        ModifyAccessRule(self: ObjectSecurity, modification: AccessControlModification, rule: AccessRule) -> (bool, bool)

            Applies the specified modification to the Discretionary Access Control List (DACL) associated with this System.Security.AccessControl.ObjectSecurity object.

            modification: The modification to apply to the DACL.

            rule: The access rule to modify.

            Returns: ue if the DACL is successfully modified; otherwise, lse.
        """
        ...
    # Error generating skeleton for function ModifyAudit: 'type' object has no attribute '__bases__'

    def ModifyAuditRule(self, modification, rule, modified):
        """
        ModifyAuditRule(self: ObjectSecurity, modification: AccessControlModification, rule: AuditRule) -> (bool, bool)

            Applies the specified modification to the System Access Control List (SACL) associated with this System.Security.AccessControl.ObjectSecurity object.

            modification: The modification to apply to the SACL.

            rule: The audit rule to modify.

            Returns: ue if the SACL is successfully modified; otherwise, lse.
        """
        ...
    # Error generating skeleton for function Persist: 'type' object has no attribute '__bases__'

    def PurgeAccessRules(self, identity):
        """
        PurgeAccessRules(self: ObjectSecurity, identity: IdentityReference)

            Removes all access rules associated with the specified System.Security.Principal.IdentityReference.

            identity: The System.Security.Principal.IdentityReference for which to remove all access rules.
        """
        ...
    def PurgeAuditRules(self, identity):
        """
        PurgeAuditRules(self: ObjectSecurity, identity: IdentityReference)

            Removes all audit rules associated with the specified System.Security.Principal.IdentityReference.

            identity: The System.Security.Principal.IdentityReference for which to remove all audit rules.
        """
        ...
    # Error generating skeleton for function ReadLock: 'type' object has no attribute '__bases__'

    # Error generating skeleton for function ReadUnlock: 'type' object has no attribute '__bases__'

    def SetAccessRuleProtection(self, isProtected, preserveInheritance):
        """
        SetAccessRuleProtection(self: ObjectSecurity, isProtected: bool, preserveInheritance: bool)

            Sets or removes protection of the access rules associated with this System.Security.AccessControl.ObjectSecurity object. Protected access rules cannot be modified by parent objects through inheritance.

            isProtected: ue to protect the access rules associated with this System.Security.AccessControl.ObjectSecurity object from inheritance; lse to allow inheritance.

            preserveInheritance: ue to preserve inherited access rules; lse to remove inherited access rules. This parameter is ignored if isProtected is lse.
        """
        ...
    def SetAuditRuleProtection(self, isProtected, preserveInheritance):
        """
        SetAuditRuleProtection(self: ObjectSecurity, isProtected: bool, preserveInheritance: bool)

            Sets or removes protection of the audit rules associated with this System.Security.AccessControl.ObjectSecurity object. Protected audit rules cannot be modified by parent objects through inheritance.

            isProtected: ue to protect the audit rules associated with this System.Security.AccessControl.ObjectSecurity object from inheritance; lse to allow inheritance.

            preserveInheritance: ue to preserve inherited audit rules; lse to remove inherited audit rules. This parameter is ignored if isProtected is lse.
        """
        ...
    def SetGroup(self, identity):
        """
        SetGroup(self: ObjectSecurity, identity: IdentityReference)

            Sets the primary group for the security descriptor associated with this System.Security.AccessControl.ObjectSecurity object.

            identity: The primary group to set.
        """
        ...
    def SetOwner(self, identity):
        """
        SetOwner(self: ObjectSecurity, identity: IdentityReference)

            Sets the owner for the security descriptor associated with this System.Security.AccessControl.ObjectSecurity object.

            identity: The owner to set.
        """
        ...
    def SetSecurityDescriptorBinaryForm(self, binaryForm, includeSections=None):
        """
        SetSecurityDescriptorBinaryForm(self: ObjectSecurity, binaryForm: Array[Byte])

            Sets the security descriptor for this System.Security.AccessControl.ObjectSecurity object from the specified array of byte values.

            binaryForm: The array of bytes from which to set the security descriptor.

        SetSecurityDescriptorBinaryForm(self: ObjectSecurity, binaryForm: Array[Byte], includeSections: AccessControlSections)

            Sets the specified sections of the security descriptor for this System.Security.AccessControl.ObjectSecurity object from the specified array of byte values.

            binaryForm: The array of bytes from which to set the security descriptor.

            includeSections: The sections (access rules, audit rules, owner, primary group) of the security descriptor to set.
        """
        ...
    def SetSecurityDescriptorSddlForm(self, sddlForm, includeSections=None):
        """
        SetSecurityDescriptorSddlForm(self: ObjectSecurity, sddlForm: str)

            Sets the security descriptor for this System.Security.AccessControl.ObjectSecurity object from the specified Security Descriptor Definition Language (SDDL) string.

            sddlForm: The SDDL string from which to set the security descriptor.

        SetSecurityDescriptorSddlForm(self: ObjectSecurity, sddlForm: str, includeSections: AccessControlSections)

            Sets the specified sections of the security descriptor for this System.Security.AccessControl.ObjectSecurity object from the specified Security Descriptor Definition Language (SDDL) string.

            sddlForm: The SDDL string from which to set the security descriptor.

            includeSections: The sections (access rules, audit rules, owner, primary group) of the security descriptor to set.
        """
        ...
    # Error generating skeleton for function WriteLock: 'type' object has no attribute '__bases__'

    # Error generating skeleton for function WriteUnlock: 'type' object has no attribute '__bases__'

    @staticmethod  # known case of __new__
    def __new__(cls, *args):  # cannot find CLR constructor
        """
        __new__(cls: type)

        __new__(cls: type, isContainer: bool, isDS: bool)

        __new__(cls: type, securityDescriptor: CommonSecurityDescriptor)
        """
        ...
    # Error generating skeleton for function __repr__: 'type' object has no attribute '__bases__'

    @property
    def AccessRightType(self):
        """
        Gets the System.Type of the securable object associated with this System.Security.AccessControl.ObjectSecurity object.

        Get: AccessRightType(self: ObjectSecurity) -> Type
        """
        ...
    @property
    def AccessRulesModified(self):
        """Gets or sets a Boolean value that specifies whether the access rules associated with this System.Security.AccessControl.ObjectSecurity object have been modified."""
        ...
    @property
    def AccessRuleType(self):
        """
        Gets the System.Type of the object associated with the access rules of this System.Security.AccessControl.ObjectSecurity object. The System.Type object must be an object that can be cast as a System.Security.Principal.SecurityIdentifier object.

        Get: AccessRuleType(self: ObjectSecurity) -> Type
        """
        ...
    @property
    def AreAccessRulesCanonical(self):
        """
        Gets a Boolean value that specifies whether the access rules associated with this System.Security.AccessControl.ObjectSecurity object are in canonical order.

        Get: AreAccessRulesCanonical(self: ObjectSecurity) -> bool
        """
        ...
    @property
    def AreAccessRulesProtected(self):
        """
        Gets a Boolean value that specifies whether the Discretionary Access Control List (DACL) associated with this System.Security.AccessControl.ObjectSecurity object is protected.

        Get: AreAccessRulesProtected(self: ObjectSecurity) -> bool
        """
        ...
    @property
    def AreAuditRulesCanonical(self):
        """
        Gets a Boolean value that specifies whether the audit rules associated with this System.Security.AccessControl.ObjectSecurity object are in canonical order.

        Get: AreAuditRulesCanonical(self: ObjectSecurity) -> bool
        """
        ...
    @property
    def AreAuditRulesProtected(self):
        """
        Gets a Boolean value that specifies whether the System Access Control List (SACL) associated with this System.Security.AccessControl.ObjectSecurity object is protected.

        Get: AreAuditRulesProtected(self: ObjectSecurity) -> bool
        """
        ...
    @property
    def AuditRulesModified(self):
        """Gets or sets a Boolean value that specifies whether the audit rules associated with this System.Security.AccessControl.ObjectSecurity object have been modified."""
        ...
    @property
    def AuditRuleType(self):
        """
        Gets the System.Type object associated with the audit rules of this System.Security.AccessControl.ObjectSecurity object. The System.Type object must be an object that can be cast as a System.Security.Principal.SecurityIdentifier object.

        Get: AuditRuleType(self: ObjectSecurity) -> Type
        """
        ...
    @property
    def GroupModified(self):
        """Gets or sets a Boolean value that specifies whether the group associated with the securable object has been modified."""
        ...
    @property
    def IsContainer(self):
        """Gets a Boolean value that specifies whether this System.Security.AccessControl.ObjectSecurity object is a container object."""
        ...
    @property
    def IsDS(self):
        """Gets a Boolean value that specifies whether this System.Security.AccessControl.ObjectSecurity object is a directory object."""
        ...
    @property
    def OwnerModified(self):
        """Gets or sets a Boolean value that specifies whether the owner of the securable object has been modified."""
        ...

class PrivilegeNotHeldException(
    UnauthorizedAccessException
):  # skipped bases: <type '_Exception'>, <type 'ISerializable'>
    """
    The exception that is thrown when a method in the System.Security.AccessControl namespace attempts to enable a privilege that it does not have.

    PrivilegeNotHeldException()

    PrivilegeNotHeldException(privilege: str)

    PrivilegeNotHeldException(privilege: str, inner: Exception)
    """

    def GetObjectData(self, info, context):
        """
        GetObjectData(self: PrivilegeNotHeldException, info: SerializationInfo, context: StreamingContext)

            Sets the info parameter with information about the exception.

            info: The System.Runtime.Serialization.SerializationInfo that holds the serialized object data about the exception being thrown.

            context: The System.Runtime.Serialization.StreamingContext that contains contextual information about the source or destination.
        """
        ...
    @property
    def PrivilegeName(self):
        """
        Gets the name of the privilege that is not enabled.

        Get: PrivilegeName(self: PrivilegeNotHeldException) -> str
        """
        ...
    SerializeObjectState = None

class PropagationFlags(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies how Access Control Entries (ACEs) are propagated to child objects.  These flags are significant only if inheritance flags are present.

    enum (flags) PropagationFlags, values: InheritOnly (2), None (0), NoPropagateInherit (1)
    """

    InheritOnly = None

    NoPropagateInherit = None
    value__ = None

class RawAcl(GenericAcl):  # skipped bases: <type 'ICollection'>, <type 'IEnumerable'>
    """
    Represents an Access Control List (ACL).

    RawAcl(revision: Byte, capacity: int)

    RawAcl(binaryForm: Array[Byte], offset: int)
    """

    def InsertAce(self, index, ace):
        """
        InsertAce(self: RawAcl, index: int, ace: GenericAce)

            Inserts the specified Access Control Entry (ACE) at the specified index.

            index: The position at which to add the new ACE. Specify the value of the System.Security.AccessControl.RawAcl.Count property to insert an ACE at the end of the System.Security.AccessControl.RawAcl object.

            ace: The ACE to insert.
        """
        ...
    def RemoveAce(self, index):
        """
        RemoveAce(self: RawAcl, index: int)

            Removes the Access Control Entry (ACE) at the specified location.

            index: The zero-based index of the ACE to remove.
        """
        ...
    @staticmethod  # known case of __new__
    def __new__(cls, *__args):
        """
        __new__(cls: type, revision: Byte, capacity: int)

        __new__(cls: type, binaryForm: Array[Byte], offset: int)
        """
        ...
    @property
    def BinaryLength(self):
        """
        Gets the length, in bytes, of the binary representation of the current System.Security.AccessControl.RawAcl object. This length should be used before marshaling the ACL into a binary array with the System.Security.AccessControl.RawAcl.GetBinaryForm(System.Byte[],System.Int32) method.

        Get: BinaryLength(self: RawAcl) -> int
        """
        ...
    @property
    def Count(self):
        """
        Gets the number of access control entries (ACEs) in the current System.Security.AccessControl.RawAcl object.

        Get: Count(self: RawAcl) -> int
        """
        ...
    @property
    def Revision(self):
        """
        Gets the revision level of the System.Security.AccessControl.RawAcl.

        Get: Revision(self: RawAcl) -> Byte
        """
        ...

class RawSecurityDescriptor(GenericSecurityDescriptor):
    """
    Represents a security descriptor. A security descriptor includes an owner, a primary group, a Discretionary Access Control List (DACL), and a System Access Control List (SACL).

    RawSecurityDescriptor(flags: ControlFlags, owner: SecurityIdentifier, group: SecurityIdentifier, systemAcl: RawAcl, discretionaryAcl: RawAcl)

    RawSecurityDescriptor(sddlForm: str)

    RawSecurityDescriptor(binaryForm: Array[Byte], offset: int)
    """

    def SetFlags(self, flags):
        """
        SetFlags(self: RawSecurityDescriptor, flags: ControlFlags)

            Sets the System.Security.AccessControl.RawSecurityDescriptor.ControlFlags property of this System.Security.AccessControl.RawSecurityDescriptor object to the specified value.

            flags: One or more values of the System.Security.AccessControl.ControlFlags enumeration combined with a logical OR operation.
        """
        ...
    @staticmethod  # known case of __new__
    def __new__(cls, *__args):
        """
        __new__(cls: type, flags: ControlFlags, owner: SecurityIdentifier, group: SecurityIdentifier, systemAcl: RawAcl, discretionaryAcl: RawAcl)

        __new__(cls: type, sddlForm: str)

        __new__(cls: type, binaryForm: Array[Byte], offset: int)
        """
        ...
    @property
    def ControlFlags(self):
        """
        Gets values that specify behavior of the System.Security.AccessControl.RawSecurityDescriptor object.

        Get: ControlFlags(self: RawSecurityDescriptor) -> ControlFlags
        """
        ...
    @property
    def DiscretionaryAcl(self):
        """
        Gets or sets the Discretionary Access Control List (DACL) for this System.Security.AccessControl.RawSecurityDescriptor object. The DACL contains access rules.

        Get: DiscretionaryAcl(self: RawSecurityDescriptor) -> RawAcl

        Set: DiscretionaryAcl(self: RawSecurityDescriptor) = value
        """
        ...
    @property
    def Group(self):
        """
        Gets or sets the primary group for this System.Security.AccessControl.RawSecurityDescriptor object.

        Get: Group(self: RawSecurityDescriptor) -> SecurityIdentifier

        Set: Group(self: RawSecurityDescriptor) = value
        """
        ...
    @property
    def Owner(self):
        """
        Gets or sets the owner of the object associated with this System.Security.AccessControl.RawSecurityDescriptor object.

        Get: Owner(self: RawSecurityDescriptor) -> SecurityIdentifier

        Set: Owner(self: RawSecurityDescriptor) = value
        """
        ...
    @property
    def ResourceManagerControl(self):
        """
        Gets or sets a byte value that represents the resource manager control bits associated with this System.Security.AccessControl.RawSecurityDescriptor object.

        Get: ResourceManagerControl(self: RawSecurityDescriptor) -> Byte

        Set: ResourceManagerControl(self: RawSecurityDescriptor) = value
        """
        ...
    @property
    def SystemAcl(self):
        """
        Gets or sets the System Access Control List (SACL) for this System.Security.AccessControl.RawSecurityDescriptor object. The SACL contains audit rules.

        Get: SystemAcl(self: RawSecurityDescriptor) -> RawAcl

        Set: SystemAcl(self: RawSecurityDescriptor) = value
        """
        ...

class RegistryAccessRule(AccessRule):
    """
    Represents a set of access rights allowed or denied for a user or group. This class cannot be inherited.

    RegistryAccessRule(identity: IdentityReference, registryRights: RegistryRights, type: AccessControlType)

    RegistryAccessRule(identity: str, registryRights: RegistryRights, type: AccessControlType)

    RegistryAccessRule(identity: IdentityReference, registryRights: RegistryRights, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, type: AccessControlType)

    RegistryAccessRule(identity: str, registryRights: RegistryRights, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, type: AccessControlType)
    """

    @property
    def AccessMask(self):
        """Gets the access mask for this rule."""
        ...
    @property
    def RegistryRights(self):
        """
        Gets the rights allowed or denied by the access rule.

        Get: RegistryRights(self: RegistryAccessRule) -> RegistryRights
        """
        ...

class RegistryAuditRule(AuditRule):
    """
    Represents a set of access rights to be audited for a user or group. This class cannot be inherited.

    RegistryAuditRule(identity: IdentityReference, registryRights: RegistryRights, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, flags: AuditFlags)

    RegistryAuditRule(identity: str, registryRights: RegistryRights, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, flags: AuditFlags)
    """

    @property
    def AccessMask(self):
        """Gets the access mask for this rule."""
        ...
    @property
    def RegistryRights(self):
        """
        Gets the access rights affected by the audit rule.

        Get: RegistryRights(self: RegistryAuditRule) -> RegistryRights
        """
        ...

class RegistryRights(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies the access control rights that can be applied to registry objects.

    enum (flags) RegistryRights, values: ChangePermissions (262144), CreateLink (32), CreateSubKey (4), Delete (65536), EnumerateSubKeys (8), ExecuteKey (131097), FullControl (983103), Notify (16), QueryValues (1), ReadKey (131097), ReadPermissions (131072), SetValue (2), TakeOwnership (524288), WriteKey (131078)
    """

    ChangePermissions = None
    CreateLink = None
    CreateSubKey = None
    Delete = None
    EnumerateSubKeys = None
    ExecuteKey = None
    FullControl = None
    Notify = None
    QueryValues = None
    ReadKey = None
    ReadPermissions = None
    SetValue = None
    TakeOwnership = None
    value__ = None
    WriteKey = None

class RegistrySecurity(NativeObjectSecurity):
    """
    Represents the Windows access control security for a registry key. This class cannot be inherited.

    RegistrySecurity()
    """

    def AccessRuleFactory(self, identityReference, accessMask, isInherited, inheritanceFlags, propagationFlags, type):
        """
        AccessRuleFactory(self: RegistrySecurity, identityReference: IdentityReference, accessMask: int, isInherited: bool, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, type: AccessControlType) -> AccessRule

            Creates a new access control rule for the specified user, with the specified access rights, access control, and flags.

            identityReference: An System.Security.Principal.IdentityReference that identifies the user or group the rule applies to.

            accessMask: A bitwise combination of System.Security.AccessControl.RegistryRights values specifying the access rights to allow or deny, cast to an integer.

            isInherited: A Boolean value specifying whether the rule is inherited.

            inheritanceFlags: A bitwise combination of System.Security.AccessControl.InheritanceFlags values specifying how the rule is inherited by subkeys.

            propagationFlags: A bitwise combination of System.Security.AccessControl.PropagationFlags values that modify the way the rule is inherited by subkeys. Meaningless if the value of inheritanceFlags is System.Security.AccessControl.InheritanceFlags.None.

            type: One of the System.Security.AccessControl.AccessControlType values specifying whether the rights are allowed or denied.

            Returns: A System.Security.AccessControl.RegistryAccessRule object representing the specified rights for the specified user.
        """
        ...
    def AuditRuleFactory(self, identityReference, accessMask, isInherited, inheritanceFlags, propagationFlags, flags):
        """
        AuditRuleFactory(self: RegistrySecurity, identityReference: IdentityReference, accessMask: int, isInherited: bool, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, flags: AuditFlags) -> AuditRule

            Creates a new audit rule, specifying the user the rule applies to, the access rights to audit, the inheritance and propagation of the rule, and the outcome that triggers the rule.

            identityReference: An System.Security.Principal.IdentityReference that identifies the user or group the rule applies to.

            accessMask: A bitwise combination of System.Security.AccessControl.RegistryRights values specifying the access rights to audit, cast to an integer.

            isInherited: A Boolean value specifying whether the rule is inherited.

            inheritanceFlags: A bitwise combination of System.Security.AccessControl.InheritanceFlags values specifying how the rule is inherited by subkeys.

            propagationFlags: A bitwise combination of System.Security.AccessControl.PropagationFlags values that modify the way the rule is inherited by subkeys. Meaningless if the value of inheritanceFlags is System.Security.AccessControl.InheritanceFlags.None.

            flags: A bitwise combination of System.Security.AccessControl.AuditFlags values specifying whether to audit successful access, failed access, or both.

            Returns: A System.Security.AccessControl.RegistryAuditRule object representing the specified audit rule for the specified user, with the specified flags. The return type of the method is the base class,

             System.Security.AccessControl.AuditRule, but the return value can be cast safely to the derived class.
        """
        ...
    @property
    def AccessRightType(self):
        """
        Gets the enumeration type that the System.Security.AccessControl.RegistrySecurity class uses to represent access rights.

        Get: AccessRightType(self: RegistrySecurity) -> Type
        """
        ...
    @property
    def AccessRulesModified(self):
        """Gets or sets a Boolean value that specifies whether the access rules associated with this System.Security.AccessControl.ObjectSecurity object have been modified."""
        ...
    @property
    def AccessRuleType(self):
        """
        Gets the type that the System.Security.AccessControl.RegistrySecurity class uses to represent access rules.

        Get: AccessRuleType(self: RegistrySecurity) -> Type
        """
        ...
    @property
    def AuditRulesModified(self):
        """Gets or sets a Boolean value that specifies whether the audit rules associated with this System.Security.AccessControl.ObjectSecurity object have been modified."""
        ...
    @property
    def AuditRuleType(self):
        """
        Gets the type that the System.Security.AccessControl.RegistrySecurity class uses to represent audit rules.

        Get: AuditRuleType(self: RegistrySecurity) -> Type
        """
        ...
    @property
    def GroupModified(self):
        """Gets or sets a Boolean value that specifies whether the group associated with the securable object has been modified."""
        ...
    @property
    def IsContainer(self):
        """Gets a Boolean value that specifies whether this System.Security.AccessControl.ObjectSecurity object is a container object."""
        ...
    @property
    def IsDS(self):
        """Gets a Boolean value that specifies whether this System.Security.AccessControl.ObjectSecurity object is a directory object."""
        ...
    @property
    def OwnerModified(self):
        """Gets or sets a Boolean value that specifies whether the owner of the securable object has been modified."""
        ...

class ResourceType(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies the defined native object types.

    enum ResourceType, values: DSObject (8), DSObjectAll (9), FileObject (1), KernelObject (6), LMShare (5), Printer (3), ProviderDefined (10), RegistryKey (4), RegistryWow6432Key (12), Service (2), Unknown (0), WindowObject (7), WmiGuidObject (11)
    """

    DSObject = None
    DSObjectAll = None
    FileObject = None
    KernelObject = None
    LMShare = None
    Printer = None
    ProviderDefined = None
    RegistryKey = None
    RegistryWow6432Key = None
    Service = None
    Unknown = None
    value__ = None
    WindowObject = None
    WmiGuidObject = None

class SecurityInfos(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies the section of a security descriptor to be queried or set.

    enum (flags) SecurityInfos, values: DiscretionaryAcl (4), Group (2), Owner (1), SystemAcl (8)
    """

    DiscretionaryAcl = None
    Group = None
    Owner = None
    SystemAcl = None
    value__ = None

class SemaphoreAccessRule(AccessRule):
    """
    Represents a set of access rights allowed or denied for a user or group. This class cannot be inherited.

    SemaphoreAccessRule(identity: IdentityReference, eventRights: SemaphoreRights, type: AccessControlType)

    SemaphoreAccessRule(identity: str, eventRights: SemaphoreRights, type: AccessControlType)
    """

    @property
    def AccessMask(self):
        """Gets the access mask for this rule."""
        ...
    @property
    def SemaphoreRights(self):
        """
        Gets the rights allowed or denied by the access rule.

        Get: SemaphoreRights(self: SemaphoreAccessRule) -> SemaphoreRights
        """
        ...

class SemaphoreAuditRule(AuditRule):
    """
    Represents a set of access rights to be audited for a user or group. This class cannot be inherited.

    SemaphoreAuditRule(identity: IdentityReference, eventRights: SemaphoreRights, flags: AuditFlags)
    """

    @property
    def AccessMask(self):
        """Gets the access mask for this rule."""
        ...
    @property
    def SemaphoreRights(self):
        """
        Gets the access rights affected by the audit rule.

        Get: SemaphoreRights(self: SemaphoreAuditRule) -> SemaphoreRights
        """
        ...

class SemaphoreRights(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies the access control rights that can be applied to named system semaphore objects.

    enum (flags) SemaphoreRights, values: ChangePermissions (262144), Delete (65536), FullControl (2031619), Modify (2), ReadPermissions (131072), Synchronize (1048576), TakeOwnership (524288)
    """

    ChangePermissions = None
    Delete = None
    FullControl = None
    Modify = None
    ReadPermissions = None
    Synchronize = None
    TakeOwnership = None
    value__ = None

class SemaphoreSecurity(NativeObjectSecurity):
    """
    Represents the Windows access control security for a named semaphore. This class cannot be inherited.

    SemaphoreSecurity()

    SemaphoreSecurity(name: str, includeSections: AccessControlSections)
    """

    def AccessRuleFactory(self, identityReference, accessMask, isInherited, inheritanceFlags, propagationFlags, type):
        """
        AccessRuleFactory(self: SemaphoreSecurity, identityReference: IdentityReference, accessMask: int, isInherited: bool, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, type: AccessControlType) -> AccessRule

            Creates a new access control rule for the specified user, with the specified access rights, access control, and flags.

            identityReference: An System.Security.Principal.IdentityReference that identifies the user or group the rule applies to.

            accessMask: A bitwise combination of System.Security.AccessControl.SemaphoreRights values specifying the access rights to allow or deny, cast to an integer.

            isInherited: Meaningless for named semaphores, because they have no hierarchy.

            inheritanceFlags: Meaningless for named semaphores, because they have no hierarchy.

            propagationFlags: Meaningless for named semaphores, because they have no hierarchy.

            type: One of the System.Security.AccessControl.AccessControlType values specifying whether the rights are allowed or denied.

            Returns: A System.Security.AccessControl.SemaphoreAccessRule object representing the specified rights for the specified user.
        """
        ...
    def AuditRuleFactory(self, identityReference, accessMask, isInherited, inheritanceFlags, propagationFlags, flags):
        """
        AuditRuleFactory(self: SemaphoreSecurity, identityReference: IdentityReference, accessMask: int, isInherited: bool, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, flags: AuditFlags) -> AuditRule

            Creates a new audit rule, specifying the user the rule applies to, the access rights to audit, and the outcome that triggers the audit rule.

            identityReference: An System.Security.Principal.IdentityReference that identifies the user or group the rule applies to.

            accessMask: A bitwise combination of System.Security.AccessControl.SemaphoreRights values specifying the access rights to audit, cast to an integer.

            isInherited: Meaningless for named wait handles, because they have no hierarchy.

            inheritanceFlags: Meaningless for named wait handles, because they have no hierarchy.

            propagationFlags: Meaningless for named wait handles, because they have no hierarchy.

            flags: A bitwise combination of System.Security.AccessControl.AuditFlags values that specify whether to audit successful access, failed access, or both.

            Returns: A System.Security.AccessControl.SemaphoreAuditRule object representing the specified audit rule for the specified user. The return type of the method is the base class, System.Security.AccessControl.AuditRule, but the return value

             can be cast safely to the derived class.
        """
        ...
    @property
    def AccessRightType(self):
        """
        Gets the enumeration that the System.Security.AccessControl.SemaphoreSecurity class uses to represent access rights.

        Get: AccessRightType(self: SemaphoreSecurity) -> Type
        """
        ...
    @property
    def AccessRulesModified(self):
        """Gets or sets a Boolean value that specifies whether the access rules associated with this System.Security.AccessControl.ObjectSecurity object have been modified."""
        ...
    @property
    def AccessRuleType(self):
        """
        Gets the type that the System.Security.AccessControl.SemaphoreSecurity class uses to represent access rules.

        Get: AccessRuleType(self: SemaphoreSecurity) -> Type
        """
        ...
    @property
    def AuditRulesModified(self):
        """Gets or sets a Boolean value that specifies whether the audit rules associated with this System.Security.AccessControl.ObjectSecurity object have been modified."""
        ...
    @property
    def AuditRuleType(self):
        """
        Gets the type that the System.Security.AccessControl.SemaphoreSecurity class uses to represent audit rules.

        Get: AuditRuleType(self: SemaphoreSecurity) -> Type
        """
        ...
    @property
    def GroupModified(self):
        """Gets or sets a Boolean value that specifies whether the group associated with the securable object has been modified."""
        ...
    @property
    def IsContainer(self):
        """Gets a Boolean value that specifies whether this System.Security.AccessControl.ObjectSecurity object is a container object."""
        ...
    @property
    def IsDS(self):
        """Gets a Boolean value that specifies whether this System.Security.AccessControl.ObjectSecurity object is a directory object."""
        ...
    @property
    def OwnerModified(self):
        """Gets or sets a Boolean value that specifies whether the owner of the securable object has been modified."""
        ...

class SystemAcl(CommonAcl):  # skipped bases: <type 'ICollection'>, <type 'IEnumerable'>
    """
    Represents a System Access Control List (SACL).

    SystemAcl(isContainer: bool, isDS: bool, capacity: int)

    SystemAcl(isContainer: bool, isDS: bool, revision: Byte, capacity: int)

    SystemAcl(isContainer: bool, isDS: bool, rawAcl: RawAcl)
    """

    def AddAudit(self, *__args):
        """
        AddAudit(self: SystemAcl, auditFlags: AuditFlags, sid: SecurityIdentifier, accessMask: int, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags)

            Adds an audit rule to the current System.Security.AccessControl.SystemAcl object.

            auditFlags: The type of audit rule to add.

            sid: The System.Security.Principal.SecurityIdentifier for which to add an audit rule.

            accessMask: The access mask for the new audit rule.

            inheritanceFlags: Flags that specify the inheritance properties of the new audit rule.

            propagationFlags: Flags that specify the inheritance propagation properties for the new audit rule.

        AddAudit(self: SystemAcl, sid: SecurityIdentifier, rule: ObjectAuditRule)

            Adds an audit rule to the current System.Security.AccessControl.SystemAcl object.

            sid: The System.Security.Principal.SecurityIdentifier for which to add an audit rule.

            rule: The System.Security.AccessControl.ObjectAuditRulefor the new audit rule.

        AddAudit(self: SystemAcl, auditFlags: AuditFlags, sid: SecurityIdentifier, accessMask: int, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, objectFlags: ObjectAceFlags, objectType: Guid, inheritedObjectType: Guid)

            Adds an audit rule with the specified settings to the current System.Security.AccessControl.SystemAcl object. Use this method for directory object Access Control Lists (ACLs) when specifying the object type or the inherited object

             type for the new audit rule.

            auditFlags: The type of audit rule to add.

            sid: The System.Security.Principal.SecurityIdentifier for which to add an audit rule.

            accessMask: The access mask for the new audit rule.

            inheritanceFlags: Flags that specify the inheritance properties of the new audit rule.

            propagationFlags: Flags that specify the inheritance propagation properties for the new audit rule.

            objectFlags: Flags that specify if the objectType and inheritedObjectType parameters contain non-ll values.

            objectType: The identity of the class of objects to which the new audit rule applies.

            inheritedObjectType: The identity of the class of child objects which can inherit the new audit rule.
        """
        ...
    def RemoveAudit(self, *__args):
        """
        RemoveAudit(self: SystemAcl, auditFlags: AuditFlags, sid: SecurityIdentifier, accessMask: int, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags) -> bool

            Removes the specified audit rule from the current System.Security.AccessControl.SystemAcl object.

            auditFlags: The type of audit rule to remove.

            sid: The System.Security.Principal.SecurityIdentifier for which to remove an audit rule.

            accessMask: The access mask for the rule to be removed.

            inheritanceFlags: Flags that specify the inheritance properties of the rule to be removed.

            propagationFlags: Flags that specify the inheritance propagation properties for the rule to be removed.

            Returns: ue if this method successfully removes the specified audit rule; otherwise, lse.

        RemoveAudit(self: SystemAcl, sid: SecurityIdentifier, rule: ObjectAuditRule) -> bool

            Removes the specified audit rule from the current System.Security.AccessControl.SystemAcl object.

            sid: The System.Security.Principal.SecurityIdentifier for which to remove an audit rule.

            rule: The System.Security.AccessControl.ObjectAuditRule for which to remove an audit rule.

            Returns: ue if this method successfully removes the specified audit rule; otherwise, lse.

        RemoveAudit(self: SystemAcl, auditFlags: AuditFlags, sid: SecurityIdentifier, accessMask: int, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, objectFlags: ObjectAceFlags, objectType: Guid, inheritedObjectType: Guid) -> bool

            Removes the specified audit rule from the current System.Security.AccessControl.SystemAcl object. Use this method for directory object Access Control Lists (ACLs) when specifying the object type or the inherited object type.

            auditFlags: The type of audit rule to remove.

            sid: The System.Security.Principal.SecurityIdentifier for which to remove an audit rule.

            accessMask: The access mask for the rule to be removed.

            inheritanceFlags: Flags that specify the inheritance properties of the rule to be removed.

            propagationFlags: Flags that specify the inheritance propagation properties for the rule to be removed.

            objectFlags: Flags that specify if the objectType and inheritedObjectType parameters contain non-ll values.

            objectType: The identity of the class of objects to which the removed audit control rule applies.

            inheritedObjectType: The identity of the class of child objects which can inherit the removed audit rule.

            Returns: ue if this method successfully removes the specified audit rule; otherwise, lse.
        """
        ...
    def RemoveAuditSpecific(self, *__args):
        """
        RemoveAuditSpecific(self: SystemAcl, auditFlags: AuditFlags, sid: SecurityIdentifier, accessMask: int, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags)

            Removes the specified audit rule from the current System.Security.AccessControl.DiscretionaryAcl object.

            auditFlags: The type of audit rule to remove.

            sid: The System.Security.Principal.SecurityIdentifier for which to remove an audit rule.

            accessMask: The access mask for the rule to be removed.

            inheritanceFlags: Flags that specify the inheritance properties of the rule to be removed.

            propagationFlags: Flags that specify the inheritance propagation properties for the rule to be removed.

        RemoveAuditSpecific(self: SystemAcl, sid: SecurityIdentifier, rule: ObjectAuditRule)

            Removes the specified audit rule from the current System.Security.AccessControl.DiscretionaryAcl object.

            sid: The System.Security.Principal.SecurityIdentifier for which to remove an audit rule.

            rule: The System.Security.AccessControl.ObjectAuditRule for the rule to be removed.

        RemoveAuditSpecific(self: SystemAcl, auditFlags: AuditFlags, sid: SecurityIdentifier, accessMask: int, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, objectFlags: ObjectAceFlags, objectType: Guid, inheritedObjectType: Guid)

            Removes the specified audit rule from the current System.Security.AccessControl.DiscretionaryAcl object. Use this method for directory object Access Control Lists (ACLs) when specifying the object type or the inherited object type.

            auditFlags: The type of audit rule to remove.

            sid: The System.Security.Principal.SecurityIdentifier for which to remove an audit rule.

            accessMask: The access mask for the rule to be removed.

            inheritanceFlags: Flags that specify the inheritance properties of the rule to be removed.

            propagationFlags: Flags that specify the inheritance propagation properties for the rule to be removed.

            objectFlags: Flags that specify if the objectType and inheritedObjectType parameters contain non-ll values.

            objectType: The identity of the class of objects to which the removed audit control rule applies.

            inheritedObjectType: The identity of the class of child objects which can inherit the removed audit rule.
        """
        ...
    def SetAudit(self, *__args):
        """
        SetAudit(self: SystemAcl, auditFlags: AuditFlags, sid: SecurityIdentifier, accessMask: int, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags)

            Sets the specified audit rule for the specified System.Security.Principal.SecurityIdentifier object.

            auditFlags: The audit condition to set.

            sid: The System.Security.Principal.SecurityIdentifier for which to set an audit rule.

            accessMask: The access mask for the new audit rule.

            inheritanceFlags: Flags that specify the inheritance properties of the new audit rule.

            propagationFlags: Flags that specify the inheritance propagation properties for the new audit rule.

        SetAudit(self: SystemAcl, sid: SecurityIdentifier, rule: ObjectAuditRule)

            Sets the specified audit rule for the specified System.Security.Principal.SecurityIdentifier object.

            sid: The System.Security.Principal.SecurityIdentifier for which to set an audit rule.

            rule: The System.Security.AccessControl.ObjectAuditRulefor which to set an audit rule.

        SetAudit(self: SystemAcl, auditFlags: AuditFlags, sid: SecurityIdentifier, accessMask: int, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, objectFlags: ObjectAceFlags, objectType: Guid, inheritedObjectType: Guid)

            Sets the specified audit rule for the specified System.Security.Principal.SecurityIdentifier object. Use this method for directory object Access Control Lists (ACLs) when specifying the object type or the inherited object type.

            auditFlags: The audit condition to set.

            sid: The System.Security.Principal.SecurityIdentifier for which to set an audit rule.

            accessMask: The access mask for the new audit rule.

            inheritanceFlags: Flags that specify the inheritance properties of the new audit rule.

            propagationFlags: Flags that specify the inheritance propagation properties for the new audit rule.

            objectFlags: Flags that specify if the objectType and inheritedObjectType parameters contain non-ll values.

            objectType: The identity of the class of objects to which the new audit rule applies.

            inheritedObjectType: The identity of the class of child objects which can inherit the new audit rule.
        """
        ...
    @staticmethod  # known case of __new__
    def __new__(cls, isContainer, isDS, *__args):
        """
        __new__(cls: type, isContainer: bool, isDS: bool, capacity: int)

        __new__(cls: type, isContainer: bool, isDS: bool, revision: Byte, capacity: int)

        __new__(cls: type, isContainer: bool, isDS: bool, rawAcl: RawAcl)
        """
        ...
