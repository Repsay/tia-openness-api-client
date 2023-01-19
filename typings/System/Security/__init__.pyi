# encoding: utf-8
# module System.Security calls itself Security
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AllowPartiallyTrustedCallersAttribute(Attribute):  # skipped bases: <type '_Attribute'>
    """
    Allows an assembly to be called by partially trusted code. Without this declaration, only fully trusted callers are able to use the assembly. This class cannot be inherited.

    AllowPartiallyTrustedCallersAttribute()
    """

    @property
    def PartialTrustVisibilityLevel(self):
        """
        Gets or sets the default partial trust visibility for code that is marked with the System.Security.AllowPartiallyTrustedCallersAttribute (APTCA) attribute.

        Get: PartialTrustVisibilityLevel(self: AllowPartiallyTrustedCallersAttribute) -> PartialTrustVisibilityLevel

        Set: PartialTrustVisibilityLevel(self: AllowPartiallyTrustedCallersAttribute) = value
        """
        ...

class CodeAccessPermission(object, IPermission, IStackWalk):  # skipped bases: <type 'ISecurityEncodable'>
    """Defines the underlying structure of all code access permissions."""

    def Equals(self, obj):
        """
        Equals(self: CodeAccessPermission, obj: object) -> bool

            Determines whether the specified System.Security.CodeAccessPermission object is equal to the current System.Security.CodeAccessPermission.

            obj: The System.Security.CodeAccessPermission object to compare with the current System.Security.CodeAccessPermission.

            Returns: ue if the specified System.Security.CodeAccessPermission object is equal to the current System.Security.CodeAccessPermission; otherwise, lse.
        """
        ...
    def FromXml(self, elem):
        """
        FromXml(self: CodeAccessPermission, elem: SecurityElement)

            When overridden in a derived class, reconstructs a security object with a specified state from an XML encoding.

            elem: The XML encoding to use to reconstruct the security object.
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: CodeAccessPermission) -> int

            Gets a hash code for the System.Security.CodeAccessPermission object that is suitable for use in hashing algorithms and data structures such as a hash table.

            Returns: A hash code for the current System.Security.CodeAccessPermission object.
        """
        ...
    @staticmethod
    def RevertAll():
        """
        RevertAll()

            Causes all previous overrides for the current frame to be removed and no longer in effect.
        """
        ...
    @staticmethod
    def RevertAssert():
        """
        RevertAssert()

            Causes any previous System.Security.CodeAccessPermission.Assert for the current frame to be removed and no longer in effect.
        """
        ...
    @staticmethod
    def RevertDeny():
        """
        RevertDeny()

            Causes any previous System.Security.CodeAccessPermission.Deny for the current frame to be removed and no longer in effect.
        """
        ...
    @staticmethod
    def RevertPermitOnly():
        """
        RevertPermitOnly()

            Causes any previous System.Security.CodeAccessPermission.PermitOnly for the current frame to be removed and no longer in effect.
        """
        ...
    def ToString(self):
        """
        ToString(self: CodeAccessPermission) -> str

            Creates and returns a string representation of the current permission object.

            Returns: A string representation of the current permission object.
        """
        ...
    def ToXml(self):
        """
        ToXml(self: CodeAccessPermission) -> SecurityElement

            When overridden in a derived class, creates an XML encoding of the security object and its current state.

            Returns: An XML encoding of the security object, including any state information.
        """
        ...
    def __eq__(self, *args):  # cannot find CLR method
        """x.__eq__(y) <==> x==y"""
        ...
    def __ne__(self, *args): ...

class HostProtectionException(SystemException):  # skipped bases: <type '_Exception'>, <type 'ISerializable'>
    """
    The exception that is thrown when a denied host resource is detected.

    HostProtectionException()

    HostProtectionException(message: str)

    HostProtectionException(message: str, e: Exception)

    HostProtectionException(message: str, protectedResources: HostProtectionResource, demandedResources: HostProtectionResource)
    """

    @property
    def DemandedResources(self):
        """
        Gets or sets the demanded host protection resources that caused the exception to be thrown.

        Get: DemandedResources(self: HostProtectionException) -> HostProtectionResource
        """
        ...
    @property
    def ProtectedResources(self):
        """
        Gets or sets the host protection resources that are inaccessible to partially trusted code.

        Get: ProtectedResources(self: HostProtectionException) -> HostProtectionResource
        """
        ...
    SerializeObjectState = None

class HostSecurityManager:  # skipped bases: <type 'object'>
    """
    Allows the control and customization of security behavior for application domains.

    HostSecurityManager()
    """

    def DetermineApplicationTrust(self, applicationEvidence, activatorEvidence, context):
        """
        DetermineApplicationTrust(self: HostSecurityManager, applicationEvidence: Evidence, activatorEvidence: Evidence, context: TrustManagerContext) -> ApplicationTrust

            Determines whether an application should be executed.

            applicationEvidence: The evidence for the application to be activated.

            activatorEvidence: Optionally, the evidence for the activating application domain.

            context: The trust context.

            Returns: An object that contains trust information about the application.
        """
        ...
    def GenerateAppDomainEvidence(self, evidenceType):
        """
        GenerateAppDomainEvidence(self: HostSecurityManager, evidenceType: Type) -> EvidenceBase

            Requests a specific evidence type for the application domain.

            evidenceType: The evidence type.

            Returns: The requested application domain evidence.
        """
        ...
    def GenerateAssemblyEvidence(self, evidenceType, assembly):
        """
        GenerateAssemblyEvidence(self: HostSecurityManager, evidenceType: Type, assembly: Assembly) -> EvidenceBase

            Requests a specific evidence type for the assembly.

            evidenceType: The evidence type.

            assembly: The target assembly.

            Returns: The requested assembly evidence.
        """
        ...
    def GetHostSuppliedAppDomainEvidenceTypes(self):
        """
        GetHostSuppliedAppDomainEvidenceTypes(self: HostSecurityManager) -> Array[Type]

            Determines which evidence types the host can supply for the application domain, if requested.

            Returns: An array of evidence types.
        """
        ...
    def GetHostSuppliedAssemblyEvidenceTypes(self, assembly):
        """
        GetHostSuppliedAssemblyEvidenceTypes(self: HostSecurityManager, assembly: Assembly) -> Array[Type]

            Determines which evidence types the host can supply for the assembly, if requested.

            assembly: The target assembly.

            Returns: An array of evidence types.
        """
        ...
    def ProvideAppDomainEvidence(self, inputEvidence):
        """
        ProvideAppDomainEvidence(self: HostSecurityManager, inputEvidence: Evidence) -> Evidence

            Provides the application domain evidence for an assembly being loaded.

            inputEvidence: Additional evidence to add to the System.AppDomain evidence.

            Returns: The evidence to be used for the System.AppDomain.
        """
        ...
    def ProvideAssemblyEvidence(self, loadedAssembly, inputEvidence):
        """
        ProvideAssemblyEvidence(self: HostSecurityManager, loadedAssembly: Assembly, inputEvidence: Evidence) -> Evidence

            Provides the assembly evidence for an assembly being loaded.

            loadedAssembly: The loaded assembly.

            inputEvidence: Additional evidence to add to the assembly evidence.

            Returns: The evidence to be used for the assembly.
        """
        ...
    def ResolvePolicy(self, evidence):
        """
        ResolvePolicy(self: HostSecurityManager, evidence: Evidence) -> PermissionSet

            Determines what permissions to grant to code based on the specified evidence.

            evidence: The evidence set used to evaluate policy.

            Returns: The permission set that can be granted by the security system.
        """
        ...
    @property
    def DomainPolicy(self):
        """
        When overridden in a derived class, gets the security policy for the current application domain.

        Get: DomainPolicy(self: HostSecurityManager) -> PolicyLevel
        """
        ...
    @property
    def Flags(self):
        """
        Gets the flag representing the security policy components of concern to the host.

        Get: Flags(self: HostSecurityManager) -> HostSecurityManagerOptions
        """
        ...

class HostSecurityManagerOptions(
    Enum
):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies the security policy components to be used by the host security manager.

    enum (flags) HostSecurityManagerOptions, values: AllFlags (31), HostAppDomainEvidence (1), HostAssemblyEvidence (4), HostDetermineApplicationTrust (8), HostPolicyLevel (2), HostResolvePolicy (16), None (0)
    """

    AllFlags = None
    HostAppDomainEvidence = None
    HostAssemblyEvidence = None
    HostDetermineApplicationTrust = None
    HostPolicyLevel = None
    HostResolvePolicy = None

    value__ = None

class IEvidenceFactory:
    """Gets an object's System.Security.Policy.Evidence."""

    @property
    def Evidence(self):
        """
        Gets System.Security.Policy.Evidence that verifies the current object's identity.

        Get: Evidence(self: IEvidenceFactory) -> Evidence
        """
        ...

class ISecurityEncodable:
    """Defines the methods that convert permission object state to and from XML element representation."""

    def FromXml(self, e):
        """
        FromXml(self: ISecurityEncodable, e: SecurityElement)

            Reconstructs a security object with a specified state from an XML encoding.

            e: The XML encoding to use to reconstruct the security object.
        """
        ...
    def ToXml(self):
        """
        ToXml(self: ISecurityEncodable) -> SecurityElement

            Creates an XML encoding of the security object and its current state.

            Returns: An XML encoding of the security object, including any state information.
        """
        ...

class IPermission(ISecurityEncodable):
    """Defines methods implemented by permission types."""

    def Copy(self):
        """
        Copy(self: IPermission) -> IPermission

            Creates and returns an identical copy of the current permission.

            Returns: A copy of the current permission.
        """
        ...
    def Demand(self):
        """
        Demand(self: IPermission)

            Throws a System.Security.SecurityException at run time if the security requirement is not met.
        """
        ...
    def Intersect(self, target):
        """
        Intersect(self: IPermission, target: IPermission) -> IPermission

            Creates and returns a permission that is the intersection of the current permission and the specified permission.

            target: A permission to intersect with the current permission. It must be of the same type as the current permission.

            Returns: A new permission that represents the intersection of the current permission and the specified permission. This new permission is ll if the intersection is empty.
        """
        ...
    def IsSubsetOf(self, target):
        """
        IsSubsetOf(self: IPermission, target: IPermission) -> bool

            Determines whether the current permission is a subset of the specified permission.

            target: A permission that is to be tested for the subset relationship. This permission must be of the same type as the current permission.

            Returns: ue if the current permission is a subset of the specified permission; otherwise, lse.
        """
        ...
    def Union(self, target):
        """
        Union(self: IPermission, target: IPermission) -> IPermission

            Creates a permission that is the union of the current permission and the specified permission.

            target: A permission to combine with the current permission. It must be of the same type as the current permission.

            Returns: A new permission that represents the union of the current permission and the specified permission.
        """
        ...

class ISecurityPolicyEncodable:
    """Supports the methods that convert permission object state to and from an XML element representation."""

    def FromXml(self, e, level):
        """
        FromXml(self: ISecurityPolicyEncodable, e: SecurityElement, level: PolicyLevel)

            Reconstructs a security object with a specified state from an XML encoding.

            e: The XML encoding to use to reconstruct the security object.

            level: The policy-level context to resolve named permission set references.
        """
        ...
    def ToXml(self, level):
        """
        ToXml(self: ISecurityPolicyEncodable, level: PolicyLevel) -> SecurityElement

            Creates an XML encoding of the security object and its current state.

            level: The policy-level context to resolve named permission set references.

            Returns: The root element of the XML representation of the policy object.
        """
        ...

class IStackWalk:
    """Manages the stack walk that determines whether all callers in the call stack have the required permissions to access a protected resource."""

    def Assert(self):
        """
        Assert(self: IStackWalk)

            Asserts that the calling code can access the resource identified by the current permission object, even if callers higher in the stack have not been granted permission to access the resource.
        """
        ...
    def Demand(self):
        """
        Demand(self: IStackWalk)

            Determines at run time whether all callers in the call stack have been granted the permission specified by the current permission object.
        """
        ...
    def Deny(self):
        """
        Deny(self: IStackWalk)

            Causes every System.Security.IStackWalk.Demand for the current object that passes through the calling code to fail.
        """
        ...
    def PermitOnly(self):
        """
        PermitOnly(self: IStackWalk)

            Causes every System.Security.IStackWalk.Demand for all objects except the current one that passes through the calling code to fail, even if code higher in the call stack has been granted permission to access other resources.
        """
        ...

class PermissionSet(
    object, ISecurityEncodable, ICollection, IStackWalk, IDeserializationCallback
):  # skipped bases: <type 'IEnumerable'>
    """
    Represents a collection that can contain many different types of permissions.

    PermissionSet(state: PermissionState)

    PermissionSet(permSet: PermissionSet)
    """

    def AddPermission(self, perm):
        """
        AddPermission(self: PermissionSet, perm: IPermission) -> IPermission

            Adds a specified permission to the System.Security.PermissionSet.

            perm: The permission to add.

            Returns: The union of the permission added and any permission of the same type that already exists in the System.Security.PermissionSet.
        """
        ...
    def AddPermissionImpl(self, *args):  # cannot find CLR method
        """
        AddPermissionImpl(self: PermissionSet, perm: IPermission) -> IPermission

            Adds a specified permission to the System.Security.PermissionSet.

            perm: The permission to add.

            Returns: The union of the permission added and any permission of the same type that already exists in the System.Security.PermissionSet, or ll if perm is ll.
        """
        ...
    def ContainsNonCodeAccessPermissions(self):
        """
        ContainsNonCodeAccessPermissions(self: PermissionSet) -> bool

            Gets a value indicating whether the System.Security.PermissionSet contains permissions that are not derived from System.Security.CodeAccessPermission.

            Returns: ue if the System.Security.PermissionSet contains permissions that are not derived from System.Security.CodeAccessPermission; otherwise, lse.
        """
        ...
    @staticmethod
    def ConvertPermissionSet(inFormat, inData, outFormat):
        """
        ConvertPermissionSet(inFormat: str, inData: Array[Byte], outFormat: str) -> Array[Byte]

            Converts an encoded System.Security.PermissionSet from one XML encoding format to another XML encoding format.

            inFormat: A string representing one of the following encoding formats: ASCII, Unicode, or Binary. Possible values are "XMLASCII" or "XML", "XMLUNICODE", and "BINARY".

            inData: An XML-encoded permission set.

            outFormat: A string representing one of the following encoding formats: ASCII, Unicode, or Binary. Possible values are "XMLASCII" or "XML", "XMLUNICODE", and "BINARY".

            Returns: An encrypted permission set with the specified output format.
        """
        ...
    def Copy(self):
        """
        Copy(self: PermissionSet) -> PermissionSet

            Creates a copy of the System.Security.PermissionSet.

            Returns: A copy of the System.Security.PermissionSet.
        """
        ...
    def Equals(self, obj):
        """
        Equals(self: PermissionSet, obj: object) -> bool

            Determines whether the specified System.Security.PermissionSet or System.Security.NamedPermissionSet object is equal to the current System.Security.PermissionSet.

            obj: The object to compare with the current System.Security.PermissionSet.

            Returns: ue if the specified object is equal to the current System.Security.PermissionSet object; otherwise, lse.
        """
        ...
    def GetEnumerator(self):
        """
        GetEnumerator(self: PermissionSet) -> IEnumerator

            Returns an enumerator for the permissions of the set.

            Returns: An enumerator object for the permissions of the set.
        """
        ...
    def GetEnumeratorImpl(self, *args):  # cannot find CLR method
        """
        GetEnumeratorImpl(self: PermissionSet) -> IEnumerator

            Returns an enumerator for the permissions of the set.

            Returns: An enumerator object for the permissions of the set.
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: PermissionSet) -> int

            Gets a hash code for the System.Security.PermissionSet object that is suitable for use in hashing algorithms and data structures such as a hash table.

            Returns: A hash code for the current System.Security.PermissionSet object.
        """
        ...
    def GetPermission(self, permClass):
        """
        GetPermission(self: PermissionSet, permClass: Type) -> IPermission

            Gets a permission object of the specified type, if it exists in the set.

            permClass: The type of the desired permission object.

            Returns: A copy of the permission object of the type specified by the permClass parameter contained in the System.Security.PermissionSet, or ll if none exists.
        """
        ...
    def GetPermissionImpl(self, *args):  # cannot find CLR method
        """
        GetPermissionImpl(self: PermissionSet, permClass: Type) -> IPermission

            Gets a permission object of the specified type, if it exists in the set.

            permClass: The type of the permission object.

            Returns: A copy of the permission object, of the type specified by the permClass parameter, contained in the System.Security.PermissionSet, or ll if none exists.
        """
        ...
    def Intersect(self, other):
        """
        Intersect(self: PermissionSet, other: PermissionSet) -> PermissionSet

            Creates and returns a permission set that is the intersection of the current System.Security.PermissionSet and the specified System.Security.PermissionSet.

            other: A permission set to intersect with the current System.Security.PermissionSet.

            Returns: A new permission set that represents the intersection of the current System.Security.PermissionSet and the specified target. This object is ll if the intersection is empty.
        """
        ...
    def IsEmpty(self):
        """
        IsEmpty(self: PermissionSet) -> bool

            Gets a value indicating whether the System.Security.PermissionSet is empty.

            Returns: ue if the System.Security.PermissionSet is empty; otherwise, lse.
        """
        ...
    def IsSubsetOf(self, target):
        """
        IsSubsetOf(self: PermissionSet, target: PermissionSet) -> bool

            Determines whether the current System.Security.PermissionSet is a subset of the specified System.Security.PermissionSet.

            target: The permission set to test for the subset relationship. This must be either a System.Security.PermissionSet or a System.Security.NamedPermissionSet.

            Returns: ue if the current System.Security.PermissionSet is a subset of the target parameter; otherwise, lse.
        """
        ...
    def IsUnrestricted(self):
        """
        IsUnrestricted(self: PermissionSet) -> bool

            Determines whether the System.Security.PermissionSet is restricted.

            Returns: ue if the System.Security.PermissionSet is restricted; otherwise, lse.
        """
        ...
    def RemovePermission(self, permClass):
        """
        RemovePermission(self: PermissionSet, permClass: Type) -> IPermission

            Removes a permission of a certain type from the set.

            permClass: The type of permission to delete.

            Returns: The permission removed from the set.
        """
        ...
    def RemovePermissionImpl(self, *args):  # cannot find CLR method
        """
        RemovePermissionImpl(self: PermissionSet, permClass: Type) -> IPermission

            Removes a permission of a certain type from the set.

            permClass: The type of the permission to remove.

            Returns: The permission removed from the set.
        """
        ...
    @staticmethod
    def RevertAssert():
        """
        RevertAssert()

            Causes any previous System.Security.CodeAccessPermission.Assert for the current frame to be removed and no longer be in effect.
        """
        ...
    def SetPermission(self, perm):
        """
        SetPermission(self: PermissionSet, perm: IPermission) -> IPermission

            Sets a permission to the System.Security.PermissionSet, replacing any existing permission of the same type.

            perm: The permission to set.

            Returns: The set permission.
        """
        ...
    def SetPermissionImpl(self, *args):  # cannot find CLR method
        """
        SetPermissionImpl(self: PermissionSet, perm: IPermission) -> IPermission

            Sets a permission to the System.Security.PermissionSet, replacing any existing permission of the same type.

            perm: The permission to set.

            Returns: The set permission.
        """
        ...
    def ToString(self):
        """
        ToString(self: PermissionSet) -> str

            Returns a string representation of the System.Security.PermissionSet.

            Returns: A representation of the System.Security.PermissionSet.
        """
        ...
    def Union(self, other):
        """
        Union(self: PermissionSet, other: PermissionSet) -> PermissionSet

            Creates a System.Security.PermissionSet that is the union of the current System.Security.PermissionSet and the specified System.Security.PermissionSet.

            other: The permission set to form the union with the current System.Security.PermissionSet.

            Returns: A new permission set that represents the union of the current System.Security.PermissionSet and the specified System.Security.PermissionSet.
        """
        ...
    def __eq__(self, *args):  # cannot find CLR method
        """x.__eq__(y) <==> x==y"""
        ...
    def __len__(self, *args):  # cannot find CLR method
        """x.__len__() <==> len(x)"""
        ...
    def __ne__(self, *args): ...
    @property
    def Count(self):
        """
        Gets the number of permission objects contained in the permission set.

        Get: Count(self: PermissionSet) -> int
        """
        ...
    @property
    def IsReadOnly(self):
        """
        Gets a value indicating whether the collection is read-only.

        Get: IsReadOnly(self: PermissionSet) -> bool
        """
        ...
    @property
    def IsSynchronized(self):
        """
        Gets a value indicating whether the collection is guaranteed to be thread safe.

        Get: IsSynchronized(self: PermissionSet) -> bool
        """
        ...
    @property
    def SyncRoot(self):
        """
        Gets the root object of the current collection.

        Get: SyncRoot(self: PermissionSet) -> object
        """
        ...

class NamedPermissionSet(
    PermissionSet
):  # skipped bases: <type 'ISecurityEncodable'>, <type 'ICollection'>, <type 'IEnumerable'>, <type 'IDeserializationCallback'>, <type 'IStackWalk'>
    """
    Defines a permission set that has a name and description associated with it. This class cannot be inherited.

    NamedPermissionSet(name: str)

    NamedPermissionSet(name: str, state: PermissionState)

    NamedPermissionSet(name: str, permSet: PermissionSet)

    NamedPermissionSet(permSet: NamedPermissionSet)
    """

    @property
    def Description(self):
        """
        Gets or sets the text description of the current named permission set.

        Get: Description(self: NamedPermissionSet) -> str

        Set: Description(self: NamedPermissionSet) = value
        """
        ...
    @property
    def Name(self):
        """
        Gets or sets the name of the current named permission set.

        Get: Name(self: NamedPermissionSet) -> str

        Set: Name(self: NamedPermissionSet) = value
        """
        ...

class PartialTrustVisibilityLevel(
    Enum
):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies the default partial-trust visibility for code that is marked with the System.Security.AllowPartiallyTrustedCallersAttribute (APTCA) attribute.

    enum PartialTrustVisibilityLevel, values: NotVisibleByDefault (1), VisibleToAllHosts (0)
    """

    NotVisibleByDefault = None
    value__ = None
    VisibleToAllHosts = None

class PolicyLevelType(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies the type of a managed code policy level.

    enum PolicyLevelType, values: AppDomain (3), Enterprise (2), Machine (1), User (0)
    """

    AppDomain = None
    Enterprise = None
    Machine = None
    User = None
    value__ = None

class ReadOnlyPermissionSet(
    PermissionSet
):  # skipped bases: <type 'ISecurityEncodable'>, <type 'ICollection'>, <type 'IEnumerable'>, <type 'IDeserializationCallback'>, <type 'IStackWalk'>
    """
    Represents a read-only collection that can contain many different types of permissions.

    ReadOnlyPermissionSet(permissionSetXml: SecurityElement)
    """

    @property
    def IsReadOnly(self):
        """
        Gets a value that indicates whether the collection is read-only.

        Get: IsReadOnly(self: ReadOnlyPermissionSet) -> bool
        """
        ...

class SecureString(object, IDisposable):
    """
    Represents text that should be kept confidential, such as by deleting it from computer memory when no longer needed. This class cannot be inherited.

    SecureString()

    SecureString(value: Char*, length: int)
    """

    def AppendChar(self, c):
        """
        AppendChar(self: SecureString, c: Char)

            Appends a character to the end of the current secure string.

            c: A character to append to this secure string.
        """
        ...
    def Clear(self):
        """
        Clear(self: SecureString)

            Deletes the value of the current secure string.
        """
        ...
    def Copy(self):
        """
        Copy(self: SecureString) -> SecureString

            Creates a copy of the current secure string.

            Returns: A duplicate of this secure string.
        """
        ...
    def InsertAt(self, index, c):
        """
        InsertAt(self: SecureString, index: int, c: Char)

            Inserts a character in this secure string at the specified index position.

            index: The index position where parameter c is inserted.

            c: The character to insert.
        """
        ...
    def IsReadOnly(self):
        """
        IsReadOnly(self: SecureString) -> bool

            Indicates whether this secure string is marked read-only.

            Returns: ue if this secure string is marked read-only; otherwise, lse.
        """
        ...
    def MakeReadOnly(self):
        """
        MakeReadOnly(self: SecureString)

            Makes the text value of this secure string read-only.
        """
        ...
    def RemoveAt(self, index):
        """
        RemoveAt(self: SecureString, index: int)

            Removes the character at the specified index position from this secure string.

            index: The index position of a character in this secure string.
        """
        ...
    def SetAt(self, index, c):
        """
        SetAt(self: SecureString, index: int, c: Char)

            Replaces the existing character at the specified index position with another character.

            index: The index position of an existing character in this secure string

            c: A character that replaces the existing character.
        """
        ...
    @property
    def Length(self):
        """
        Gets the number of characters in the current secure string.

        Get: Length(self: SecureString) -> int
        """
        ...

class SecureStringMarshal:  # skipped bases: <type 'object'>
    """Provides a collection of methods for allocating unmanaged memory and copying unmanaged memory blocks."""

    @staticmethod
    def SecureStringToCoTaskMemAnsi(s):
        """
        SecureStringToCoTaskMemAnsi(s: SecureString) -> IntPtr

            Copies the contents of a managed System.Security.SecureString object to a block of memory allocated from the unmanaged COM task allocator.

            s: The managed object to copy.

            Returns: The address, in unmanaged memory, where the s parameter was copied to, or 0 if a null object was supplied.
        """
        ...
    @staticmethod
    def SecureStringToCoTaskMemUnicode(s):
        """
        SecureStringToCoTaskMemUnicode(s: SecureString) -> IntPtr

            Copies the contents of a managed System.Security.SecureString object to a block of memory allocated from the unmanaged COM task allocator.

            s: The managed object to copy.

            Returns: The address, in unmanaged memory, where the s parameter was copied to, or 0 if a null object was supplied.
        """
        ...
    @staticmethod
    def SecureStringToGlobalAllocAnsi(s):
        """
        SecureStringToGlobalAllocAnsi(s: SecureString) -> IntPtr

            Copies the contents of a managed System.Security.SecureString into unmanaged memory, converting into ANSI format as it copies.

            s: The managed object to copy.

            Returns: The address, in unmanaged memory, to where the s parameter was copied, or 0 if a null object was supplied.
        """
        ...
    @staticmethod
    def SecureStringToGlobalAllocUnicode(s):
        """
        SecureStringToGlobalAllocUnicode(s: SecureString) -> IntPtr

            Copies the contents of a managed System.Security.SecureString object into unmanaged memory.

            s: The managed object to copy.

            Returns: The address, in unmanaged memory, where s was copied, or 0 if s is a System.Security.SecureString object whose length is 0.
        """
        ...
    __all__ = [
        "SecureStringToCoTaskMemAnsi",
        "SecureStringToCoTaskMemUnicode",
        "SecureStringToGlobalAllocAnsi",
        "SecureStringToGlobalAllocUnicode",
    ]

class SecurityContext(object, IDisposable):
    """Encapsulates and propagates all security-related data for execution contexts transferred across threads. This class cannot be inherited."""

    @staticmethod
    def Capture():
        """
        Capture() -> SecurityContext

            Captures the security context for the current thread.

            Returns: The security context for the current thread.
        """
        ...
    def CreateCopy(self):
        """
        CreateCopy(self: SecurityContext) -> SecurityContext

            Creates a copy of the current security context.

            Returns: The security context for the current thread.
        """
        ...
    @staticmethod
    def IsFlowSuppressed():
        """
        IsFlowSuppressed() -> bool

            Determines whether the flow of the security context has been suppressed.

            Returns: ue if the flow has been suppressed; otherwise, lse.
        """
        ...
    @staticmethod
    def IsWindowsIdentityFlowSuppressed():
        """
        IsWindowsIdentityFlowSuppressed() -> bool

            Determines whether the flow of the Windows identity portion of the current security context has been suppressed.

            Returns: ue if the flow has been suppressed; otherwise, lse.
        """
        ...
    @staticmethod
    def RestoreFlow():
        """
        RestoreFlow()

            Restores the flow of the security context across asynchronous threads.
        """
        ...
    @staticmethod
    def Run(securityContext, callback, state):
        """
        Run(securityContext: SecurityContext, callback: ContextCallback, state: object)

            Runs the specified method in the specified security context on the current thread.

            securityContext: The security context to set.

            callback: The delegate that represents the method to run in the specified security context.

            state: The object to pass to the callback method.
        """
        ...
    @staticmethod
    def SuppressFlow():
        """
        SuppressFlow() -> AsyncFlowControl

            Suppresses the flow of the security context across asynchronous threads.

            Returns: An System.Threading.AsyncFlowControl structure for restoring the flow.
        """
        ...
    @staticmethod
    def SuppressFlowWindowsIdentity():
        """
        SuppressFlowWindowsIdentity() -> AsyncFlowControl

            Suppresses the flow of the Windows identity portion of the current security context across asynchronous threads.

            Returns: A structure for restoring the flow.
        """
        ...

class SecurityContextSource(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Identifies the source for the security context.

    enum SecurityContextSource, values: CurrentAppDomain (0), CurrentAssembly (1)
    """

    CurrentAppDomain = None
    CurrentAssembly = None
    value__ = None

class SecurityCriticalAttribute(Attribute):  # skipped bases: <type '_Attribute'>
    """
    Specifies that code or an assembly performs security-critical operations.

    SecurityCriticalAttribute()

    SecurityCriticalAttribute(scope: SecurityCriticalScope)
    """

    @staticmethod  # known case of __new__
    def __new__(cls, scope=None):
        """
        __new__(cls: type)

        __new__(cls: type, scope: SecurityCriticalScope)
        """
        ...
    @property
    def Scope(self):
        """
        Gets the scope for the attribute.

        Get: Scope(self: SecurityCriticalAttribute) -> SecurityCriticalScope
        """
        ...

class SecurityCriticalScope(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies the scope of a System.Security.SecurityCriticalAttribute.

    enum SecurityCriticalScope, values: Everything (1), Explicit (0)
    """

    Everything = None
    Explicit = None
    value__ = None

class SecurityElement(object, ISecurityElementFactory):
    """
    Represents the XML object model for encoding security objects. This class cannot be inherited.

    SecurityElement(tag: str)

    SecurityElement(tag: str, text: str)
    """

    def AddAttribute(self, name, value):
        """
        AddAttribute(self: SecurityElement, name: str, value: str)

            Adds a name/value attribute to an XML element.

            name: The name of the attribute.

            value: The value of the attribute.
        """
        ...
    def AddChild(self, child):
        """
        AddChild(self: SecurityElement, child: SecurityElement)

            Adds a child element to the XML element.

            child: The child element to add.
        """
        ...
    def Attribute(self, name):
        """
        Attribute(self: SecurityElement, name: str) -> str

            Finds an attribute by name in an XML element.

            name: The name of the attribute for which to search.

            Returns: The value associated with the named attribute, or ll if no attribute with name exists.
        """
        ...
    def Copy(self):
        """
        Copy(self: SecurityElement) -> SecurityElement

            Creates and returns an identical copy of the current System.Security.SecurityElement object.

            Returns: A copy of the current System.Security.SecurityElement object.
        """
        ...
    def Equal(self, other):
        """
        Equal(self: SecurityElement, other: SecurityElement) -> bool

            Compares two XML element objects for equality.

            other: An XML element object to which to compare the current XML element object.

            Returns: ue if the tag, attribute names and values, child elements, and text fields in the current XML element are identical to their counterparts in the other parameter; otherwise, lse.
        """
        ...
    @staticmethod
    def Escape(str):
        """
        Escape(str: str) -> str

            Replaces invalid XML characters in a string with their valid XML equivalent.

            str: The string within which to escape invalid characters.

            Returns: The input string with invalid characters replaced.
        """
        ...
    @staticmethod
    def FromString(xml):
        """
        FromString(xml: str) -> SecurityElement

            Creates a security element from an XML-encoded string.

            xml: The XML-encoded string from which to create the security element.

            Returns: A System.Security.SecurityElement created from the XML.
        """
        ...
    @staticmethod
    def IsValidAttributeName(name):
        """
        IsValidAttributeName(name: str) -> bool

            Determines whether a string is a valid attribute name.

            name: The attribute name to test for validity.

            Returns: ue if the name parameter is a valid XML attribute name; otherwise, lse.
        """
        ...
    @staticmethod
    def IsValidAttributeValue(value):
        """
        IsValidAttributeValue(value: str) -> bool

            Determines whether a string is a valid attribute value.

            value: The attribute value to test for validity.

            Returns: ue if the value parameter is a valid XML attribute value; otherwise, lse.
        """
        ...
    @staticmethod
    def IsValidTag(tag):
        """
        IsValidTag(tag: str) -> bool

            Determines whether a string is a valid tag.

            tag: The tag to test for validity.

            Returns: ue if the tag parameter is a valid XML tag; otherwise, lse.
        """
        ...
    @staticmethod
    def IsValidText(text):
        """
        IsValidText(text: str) -> bool

            Determines whether a string is valid as text within an XML element.

            text: The text to test for validity.

            Returns: ue if the text parameter is a valid XML text element; otherwise, lse.
        """
        ...
    def SearchForChildByTag(self, tag):
        """
        SearchForChildByTag(self: SecurityElement, tag: str) -> SecurityElement

            Finds a child by its tag name.

            tag: The tag for which to search in child elements.

            Returns: The first child XML element with the specified tag value, or ll if no child element with tag exists.
        """
        ...
    def SearchForTextOfTag(self, tag):
        """
        SearchForTextOfTag(self: SecurityElement, tag: str) -> str

            Finds a child by its tag name and returns the contained text.

            tag: The tag for which to search in child elements.

            Returns: The text contents of the first child element with the specified tag value.
        """
        ...
    def ToString(self):
        """
        ToString(self: SecurityElement) -> str

            Produces a string representation of an XML element and its constituent attributes, child elements, and text.

            Returns: The XML element and its contents.
        """
        ...
    @property
    def Attributes(self):
        """
        Gets or sets the attributes of an XML element as name/value pairs.

        Get: Attributes(self: SecurityElement) -> Hashtable

        Set: Attributes(self: SecurityElement) = value
        """
        ...
    @property
    def Children(self):
        """
        Gets or sets the array of child elements of the XML element.

        Get: Children(self: SecurityElement) -> ArrayList

        Set: Children(self: SecurityElement) = value
        """
        ...
    @property
    def Tag(self):
        """
        Gets or sets the tag name of an XML element.

        Get: Tag(self: SecurityElement) -> str

        Set: Tag(self: SecurityElement) = value
        """
        ...
    @property
    def Text(self):
        """
        Gets or sets the text within an XML element.

        Get: Text(self: SecurityElement) -> str

        Set: Text(self: SecurityElement) = value
        """
        ...

class SecurityException(SystemException):  # skipped bases: <type '_Exception'>, <type 'ISerializable'>
    """
    The exception that is thrown when a security error is detected.

    SecurityException()

    SecurityException(message: str)

    SecurityException(message: str, type: Type)

    SecurityException(message: str, type: Type, state: str)

    SecurityException(message: str, inner: Exception)

    SecurityException(message: str, assemblyName: AssemblyName, grant: PermissionSet, refused: PermissionSet, method: MethodInfo, action: SecurityAction, demanded: object, permThatFailed: IPermission, evidence: Evidence)

    SecurityException(message: str, deny: object, permitOnly: object, method: MethodInfo, demanded: object, permThatFailed: IPermission)
    """

    @property
    def Action(self):
        """
        Gets or sets the security action that caused the exception.

        Get: Action(self: SecurityException) -> SecurityAction

        Set: Action(self: SecurityException) = value
        """
        ...
    @property
    def Demanded(self):
        """
        Gets or sets the demanded security permission, permission set, or permission set collection that failed.

        Get: Demanded(self: SecurityException) -> object

        Set: Demanded(self: SecurityException) = value
        """
        ...
    @property
    def DenySetInstance(self):
        """
        Gets or sets the denied security permission, permission set, or permission set collection that caused a demand to fail.

        Get: DenySetInstance(self: SecurityException) -> object

        Set: DenySetInstance(self: SecurityException) = value
        """
        ...
    @property
    def FailedAssemblyInfo(self):
        """
        Gets or sets information about the failed assembly.

        Get: FailedAssemblyInfo(self: SecurityException) -> AssemblyName

        Set: FailedAssemblyInfo(self: SecurityException) = value
        """
        ...
    @property
    def FirstPermissionThatFailed(self):
        """
        Gets or sets the first permission in a permission set or permission set collection that failed the demand.

        Get: FirstPermissionThatFailed(self: SecurityException) -> IPermission

        Set: FirstPermissionThatFailed(self: SecurityException) = value
        """
        ...
    @property
    def GrantedSet(self):
        """
        Gets or sets the granted permission set of the assembly that caused the System.Security.SecurityException.

        Get: GrantedSet(self: SecurityException) -> str

        Set: GrantedSet(self: SecurityException) = value
        """
        ...
    @property
    def Method(self):
        """
        Gets or sets the information about the method associated with the exception.

        Get: Method(self: SecurityException) -> MethodInfo

        Set: Method(self: SecurityException) = value
        """
        ...
    @property
    def PermissionState(self):
        """
        Gets or sets the state of the permission that threw the exception.

        Get: PermissionState(self: SecurityException) -> str

        Set: PermissionState(self: SecurityException) = value
        """
        ...
    @property
    def PermissionType(self):
        """
        Gets or sets the type of the permission that failed.

        Get: PermissionType(self: SecurityException) -> Type

        Set: PermissionType(self: SecurityException) = value
        """
        ...
    @property
    def PermitOnlySetInstance(self):
        """
        Gets or sets the permission, permission set, or permission set collection that is part of the permit-only stack frame that caused a security check to fail.

        Get: PermitOnlySetInstance(self: SecurityException) -> object

        Set: PermitOnlySetInstance(self: SecurityException) = value
        """
        ...
    @property
    def RefusedSet(self):
        """
        Gets or sets the refused permission set of the assembly that caused the System.Security.SecurityException.

        Get: RefusedSet(self: SecurityException) -> str

        Set: RefusedSet(self: SecurityException) = value
        """
        ...
    @property
    def Url(self):
        """
        Gets or sets the URL of the assembly that caused the exception.

        Get: Url(self: SecurityException) -> str

        Set: Url(self: SecurityException) = value
        """
        ...
    @property
    def Zone(self):
        """
        Gets or sets the zone of the assembly that caused the exception.

        Get: Zone(self: SecurityException) -> SecurityZone

        Set: Zone(self: SecurityException) = value
        """
        ...
    SerializeObjectState = None

class SecurityManager:  # skipped bases: <type 'object'>
    """Provides the main access point for classes interacting with the security system. This class cannot be inherited."""

    @staticmethod
    def CurrentThreadRequiresSecurityContextCapture():
        """
        CurrentThreadRequiresSecurityContextCapture() -> bool

            Determines whether the current thread requires a security context capture if its security state has to be re-created at a later point in time.

            Returns: lse if the stack contains no partially trusted application domains, no partially trusted assemblies, and no currently active System.Security.CodeAccessPermission.PermitOnly or System.Security.CodeAccessPermission.Deny modifiers; ue

             if the common language runtime cannot guarantee that the stack contains none of these.
        """
        ...
    @staticmethod
    def GetStandardSandbox(evidence):
        """
        GetStandardSandbox(evidence: Evidence) -> PermissionSet

            Gets a permission set that is safe to grant to an application that has the provided evidence.

            evidence: The host evidence to match to a permission set.

            Returns: A permission set that can be used as a grant set for the application that has the provided evidence.
        """
        ...
    @staticmethod
    def GetZoneAndOrigin(zone, origin):
        """
        GetZoneAndOrigin() -> (ArrayList, ArrayList)

            Gets the granted zone identity and URL identity permission sets for the current assembly.
        """
        ...
    @staticmethod
    def IsGranted(perm):
        """
        IsGranted(perm: IPermission) -> bool

            Determines whether a permission is granted to the caller.

            perm: The permission to test against the grant of the caller.

            Returns: ue if the permissions granted to the caller include the permission perm; otherwise, lse.
        """
        ...
    @staticmethod
    def LoadPolicyLevelFromFile(path, type):
        """
        LoadPolicyLevelFromFile(path: str, type: PolicyLevelType) -> PolicyLevel

            Loads a System.Security.Policy.PolicyLevel from the specified file.

            path: The physical file path to a file containing the security policy information.

            type: One of the enumeration values that specifies the type of the policy level to be loaded.

            Returns: The loaded policy level.
        """
        ...
    @staticmethod
    def LoadPolicyLevelFromString(str, type):
        """
        LoadPolicyLevelFromString(str: str, type: PolicyLevelType) -> PolicyLevel

            Loads a System.Security.Policy.PolicyLevel from the specified string.

            str: The XML representation of a security policy level in the same form in which it appears in a configuration file.

            type: One of the enumeration values that specifies the type of the policy level to be loaded.

            Returns: The loaded policy level.
        """
        ...
    @staticmethod
    def PolicyHierarchy():
        """
        PolicyHierarchy() -> IEnumerator

            Provides an enumerator to access the security policy hierarchy by levels, such as computer policy and user policy.

            Returns: An enumerator for System.Security.Policy.PolicyLevel objects that compose the security policy hierarchy.
        """
        ...
    @staticmethod
    def ResolvePolicy(*__args):
        """
        ResolvePolicy(evidence: Evidence, reqdPset: PermissionSet, optPset: PermissionSet, denyPset: PermissionSet) -> (PermissionSet, PermissionSet)

            Determines what permissions to grant to code based on the specified evidence and requests.

            evidence: The evidence set used to evaluate policy.

            reqdPset: The required permissions the code needs to run.

            optPset: The optional permissions that will be used if granted, but aren't required for the code to run.

            denyPset: The denied permissions that must never be granted to the code even if policy otherwise permits it.

            Returns: The set of permissions that would be granted by the security system.

        ResolvePolicy(evidence: Evidence) -> PermissionSet

            Determines what permissions to grant to code based on the specified evidence.

            evidence: The evidence set used to evaluate policy.

            Returns: The set of permissions that can be granted by the security system.

        ResolvePolicy(evidences: Array[Evidence]) -> PermissionSet

            Determines what permissions to grant to code based on the specified evidence.

            evidences: An array of evidence objects used to evaluate policy.

            Returns: The set of permissions that is appropriate for all of the provided evidence.
        """
        ...
    @staticmethod
    def ResolvePolicyGroups(evidence):
        """
        ResolvePolicyGroups(evidence: Evidence) -> IEnumerator

            Gets a collection of code groups matching the specified evidence.

            evidence: The evidence set against which the policy is evaluated.

            Returns: An enumeration of the set of code groups matching the evidence.
        """
        ...
    @staticmethod
    def ResolveSystemPolicy(evidence):
        """
        ResolveSystemPolicy(evidence: Evidence) -> PermissionSet

            Determines which permissions to grant to code based on the specified evidence, excluding the policy for the System.AppDomain level.

            evidence: The evidence set used to evaluate policy.

            Returns: The set of permissions that can be granted by the security system.
        """
        ...
    @staticmethod
    def SavePolicy():
        """
        SavePolicy()

            Saves the modified security policy state.
        """
        ...
    @staticmethod
    def SavePolicyLevel(level):
        """
        SavePolicyLevel(level: PolicyLevel)

            Saves a modified security policy level loaded with System.Security.SecurityManager.LoadPolicyLevelFromFile(System.String,System.Security.PolicyLevelType).

            level: The policy level object to be saved.
        """
        ...
    CheckExecutionRights = True
    SecurityEnabled = True
    __all__ = [
        "CurrentThreadRequiresSecurityContextCapture",
        "GetStandardSandbox",
        "GetZoneAndOrigin",
        "IsGranted",
        "LoadPolicyLevelFromFile",
        "LoadPolicyLevelFromString",
        "PolicyHierarchy",
        "ResolvePolicy",
        "ResolvePolicyGroups",
        "ResolveSystemPolicy",
        "SavePolicy",
        "SavePolicyLevel",
    ]

class SecurityRulesAttribute(Attribute):  # skipped bases: <type '_Attribute'>
    """
    Indicates the set of security rules the common language runtime should enforce for an assembly.

    SecurityRulesAttribute(ruleSet: SecurityRuleSet)
    """

    @staticmethod  # known case of __new__
    def __new__(cls, ruleSet):
        """__new__(cls: type, ruleSet: SecurityRuleSet)"""
        ...
    @property
    def RuleSet(self):
        """
        Gets the rule set to be applied.

        Get: RuleSet(self: SecurityRulesAttribute) -> SecurityRuleSet
        """
        ...
    @property
    def SkipVerificationInFullTrust(self):
        """
        Determines whether fully trusted transparent code should skip Microsoft intermediate language (MSIL) verification.

        Get: SkipVerificationInFullTrust(self: SecurityRulesAttribute) -> bool

        Set: SkipVerificationInFullTrust(self: SecurityRulesAttribute) = value
        """
        ...

class SecurityRuleSet(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Identifies the set of security rules the common language runtime should enforce for an assembly.

    enum SecurityRuleSet, values: Level1 (1), Level2 (2), None (0)
    """

    Level1 = None
    Level2 = None

    value__ = None

class SecuritySafeCriticalAttribute(Attribute):  # skipped bases: <type '_Attribute'>
    """
    Identifies types or members as security-critical and safely accessible by transparent code.

    SecuritySafeCriticalAttribute()
    """

    pass

class SecurityState:  # skipped bases: <type 'object'>
    """Provides a base class for requesting the security status of an action from the System.AppDomainManager object."""

    def EnsureState(self):
        """
        EnsureState(self: SecurityState)

            When overridden in a derived class, ensures that the state that is represented by System.Security.SecurityState is available on the host.
        """
        ...
    def IsStateAvailable(self):
        """
        IsStateAvailable(self: SecurityState) -> bool

            Gets a value that indicates whether the state for this implementation of the System.Security.SecurityState class is available on the current host.

            Returns: ue if the state is available; otherwise, lse.
        """
        ...

class SecurityTransparentAttribute(Attribute):  # skipped bases: <type '_Attribute'>
    """
    Specifies that an assembly cannot cause an elevation of privilege.

    SecurityTransparentAttribute()
    """

    pass

class SecurityTreatAsSafeAttribute(Attribute):  # skipped bases: <type '_Attribute'>
    """
    Identifies which of the nonpublic System.Security.SecurityCriticalAttribute members are accessible by transparent code within the assembly.

    SecurityTreatAsSafeAttribute()
    """

    pass

class SecurityZone(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Defines the integer values corresponding to security zones used by security policy.

    enum SecurityZone, values: Internet (3), Intranet (1), MyComputer (0), NoZone (-1), Trusted (2), Untrusted (4)
    """

    Internet = None
    Intranet = None
    MyComputer = None
    NoZone = None
    Trusted = None
    Untrusted = None
    value__ = None

class SuppressUnmanagedCodeSecurityAttribute(Attribute):  # skipped bases: <type '_Attribute'>
    """
    Allows managed code to call into unmanaged code without a stack walk. This class cannot be inherited.

    SuppressUnmanagedCodeSecurityAttribute()
    """

    pass

class UnverifiableCodeAttribute(Attribute):  # skipped bases: <type '_Attribute'>
    """
    Marks modules containing unverifiable code. This class cannot be inherited.

    UnverifiableCodeAttribute()
    """

    pass

class VerificationException(SystemException):  # skipped bases: <type '_Exception'>, <type 'ISerializable'>
    """
    The exception that is thrown when the security policy requires code to be type safe and the verification process is unable to verify that the code is type safe.

    VerificationException()

    VerificationException(message: str)

    VerificationException(message: str, innerException: Exception)
    """

    SerializeObjectState = None

class XmlSyntaxException(SystemException):  # skipped bases: <type '_Exception'>, <type 'ISerializable'>
    """
    The exception that is thrown when there is a syntax error in XML parsing. This class cannot be inherited.

    XmlSyntaxException()

    XmlSyntaxException(message: str)

    XmlSyntaxException(message: str, inner: Exception)

    XmlSyntaxException(lineNumber: int)

    XmlSyntaxException(lineNumber: int, message: str)
    """

    SerializeObjectState = None

# variables with complex values
