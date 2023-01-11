# encoding: utf-8
# module System.Security.Permissions calls itself Permissions
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class SecurityAttribute(Attribute):  # skipped bases: <type '_Attribute'>
    """Specifies the base attribute class for declarative security from which System.Security.Permissions.CodeAccessSecurityAttribute is derived."""

    def CreatePermission(self):
        """
        CreatePermission(self: SecurityAttribute) -> IPermission

            When overridden in a derived class, creates a permission object that can then be serialized into binary form and persistently stored along with the System.Security.Permissions.SecurityAction in an assembly's metadata.

            Returns: A serializable permission object.
        """
        ...
    @staticmethod  # known case of __new__
    def __new__(cls, *args):  # cannot find CLR constructor
        """__new__(cls: type, action: SecurityAction)"""
        ...
    @property
    def Action(self):
        """
        Gets or sets a security action.

        Get: Action(self: SecurityAttribute) -> SecurityAction

        Set: Action(self: SecurityAttribute) = value
        """
        ...
    @property
    def Unrestricted(self):
        """
        Gets or sets a value indicating whether full (unrestricted) permission to the resource protected by the attribute is declared.

        Get: Unrestricted(self: SecurityAttribute) -> bool

        Set: Unrestricted(self: SecurityAttribute) = value
        """
        ...

class CodeAccessSecurityAttribute(SecurityAttribute):  # skipped bases: <type '_Attribute'>
    """Specifies the base attribute class for code access security."""

    pass

class IUnrestrictedPermission:
    """Allows a permission to expose an unrestricted state."""

    def IsUnrestricted(self):
        """
        IsUnrestricted(self: IUnrestrictedPermission) -> bool

            Returns a value indicating whether unrestricted access to the resource protected by the permission is allowed.

            Returns: ue if unrestricted use of the resource protected by the permission is allowed; otherwise, lse.
        """
        ...

class EnvironmentPermission(
    CodeAccessPermission, IUnrestrictedPermission, IBuiltInPermission
):  # skipped bases: <type 'ISecurityEncodable'>, <type 'IPermission'>, <type 'IStackWalk'>
    """
    Controls access to system and user environment variables. This class cannot be inherited.

    EnvironmentPermission(state: PermissionState)

    EnvironmentPermission(flag: EnvironmentPermissionAccess, pathList: str)
    """

    def AddPathList(self, flag, pathList):
        """
        AddPathList(self: EnvironmentPermission, flag: EnvironmentPermissionAccess, pathList: str)

            Adds access for the specified environment variables to the existing state of the permission.

            flag: One of the System.Security.Permissions.EnvironmentPermissionAccess values.

            pathList: A list of environment variables (semicolon-separated).
        """
        ...
    def GetPathList(self, flag):
        """
        GetPathList(self: EnvironmentPermission, flag: EnvironmentPermissionAccess) -> str

            Gets all environment variables with the specified System.Security.Permissions.EnvironmentPermissionAccess.

            flag: One of the System.Security.Permissions.EnvironmentPermissionAccess values that represents a single type of environment variable access.

            Returns: A list of environment variables (semicolon-separated) for the selected flag.
        """
        ...
    def SetPathList(self, flag, pathList):
        """
        SetPathList(self: EnvironmentPermission, flag: EnvironmentPermissionAccess, pathList: str)

            Sets the specified access to the specified environment variables to the existing state of the permission.

            flag: One of the System.Security.Permissions.EnvironmentPermissionAccess values.

            pathList: A list of environment variables (semicolon-separated).
        """
        ...
    @staticmethod  # known case of __new__
    def __new__(cls, *__args):
        """
        __new__(cls: type, state: PermissionState)

        __new__(cls: type, flag: EnvironmentPermissionAccess, pathList: str)
        """
        ...

class EnvironmentPermissionAccess(
    Enum
):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies access to environment variables.

    enum (flags) EnvironmentPermissionAccess, values: AllAccess (3), NoAccess (0), Read (1), Write (2)
    """

    AllAccess = None
    NoAccess = None
    Read = None
    value__ = None
    Write = None

class EnvironmentPermissionAttribute(CodeAccessSecurityAttribute):  # skipped bases: <type '_Attribute'>
    """
    Allows security actions for System.Security.Permissions.EnvironmentPermission to be applied to code using declarative security. This class cannot be inherited.

    EnvironmentPermissionAttribute(action: SecurityAction)
    """

    def CreatePermission(self):
        """
        CreatePermission(self: EnvironmentPermissionAttribute) -> IPermission

            Creates and returns a new System.Security.Permissions.EnvironmentPermission.

            Returns: An System.Security.Permissions.EnvironmentPermission that corresponds to this attribute.
        """
        ...
    @property
    def All(self):
        """
        Sets full access for the environment variables specified by the string value.

        Get: All(self: EnvironmentPermissionAttribute) -> str

        Set: All(self: EnvironmentPermissionAttribute) = value
        """
        ...
    @property
    def Read(self):
        """
        Gets or sets read access for the environment variables specified by the string value.

        Get: Read(self: EnvironmentPermissionAttribute) -> str

        Set: Read(self: EnvironmentPermissionAttribute) = value
        """
        ...
    @property
    def Write(self):
        """
        Gets or sets write access for the environment variables specified by the string value.

        Get: Write(self: EnvironmentPermissionAttribute) -> str

        Set: Write(self: EnvironmentPermissionAttribute) = value
        """
        ...

class FileDialogPermission(
    CodeAccessPermission, IUnrestrictedPermission, IBuiltInPermission
):  # skipped bases: <type 'ISecurityEncodable'>, <type 'IPermission'>, <type 'IStackWalk'>
    """
    Controls the ability to access files or folders through a File dialog box. This class cannot be inherited.

    FileDialogPermission(state: PermissionState)

    FileDialogPermission(access: FileDialogPermissionAccess)
    """

    @staticmethod  # known case of __new__
    def __new__(cls, *__args):
        """
        __new__(cls: type, state: PermissionState)

        __new__(cls: type, access: FileDialogPermissionAccess)
        """
        ...
    @property
    def Access(self):
        """
        Gets or sets the permitted access to files.

        Get: Access(self: FileDialogPermission) -> FileDialogPermissionAccess

        Set: Access(self: FileDialogPermission) = value
        """
        ...

class FileDialogPermissionAccess(
    Enum
):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies the type of access to files allowed through the File dialog boxes.

    enum (flags) FileDialogPermissionAccess, values: None (0), Open (1), OpenSave (3), Save (2)
    """

    Open = None
    OpenSave = None
    Save = None
    value__ = None

class FileDialogPermissionAttribute(CodeAccessSecurityAttribute):  # skipped bases: <type '_Attribute'>
    """
    Allows security actions for System.Security.Permissions.FileDialogPermission to be applied to code using declarative security. This class cannot be inherited.

    FileDialogPermissionAttribute(action: SecurityAction)
    """

    def CreatePermission(self):
        """
        CreatePermission(self: FileDialogPermissionAttribute) -> IPermission

            Creates and returns a new System.Security.Permissions.FileDialogPermission.

            Returns: A System.Security.Permissions.FileDialogPermission that corresponds to this attribute.
        """
        ...
    @property
    def Open(self):
        """
        Gets or sets a value indicating whether permission to open files through the file dialog is declared.

        Get: Open(self: FileDialogPermissionAttribute) -> bool

        Set: Open(self: FileDialogPermissionAttribute) = value
        """
        ...
    @property
    def Save(self):
        """
        Gets or sets a value indicating whether permission to save files through the file dialog is declared.

        Get: Save(self: FileDialogPermissionAttribute) -> bool

        Set: Save(self: FileDialogPermissionAttribute) = value
        """
        ...

class FileIOPermission(
    CodeAccessPermission, IUnrestrictedPermission, IBuiltInPermission
):  # skipped bases: <type 'ISecurityEncodable'>, <type 'IPermission'>, <type 'IStackWalk'>
    """
    Controls the ability to access files and folders. This class cannot be inherited.

    FileIOPermission(state: PermissionState)

    FileIOPermission(access: FileIOPermissionAccess, path: str)

    FileIOPermission(access: FileIOPermissionAccess, pathList: Array[str])

    FileIOPermission(access: FileIOPermissionAccess, control: AccessControlActions, path: str)

    FileIOPermission(access: FileIOPermissionAccess, control: AccessControlActions, pathList: Array[str])
    """

    def AddPathList(self, access, *__args):
        """
        AddPathList(self: FileIOPermission, access: FileIOPermissionAccess, path: str)

            Adds access for the specified file or directory to the existing state of the permission.

            access: A bitwise combination of the System.Security.Permissions.FileIOPermissionAccess values.

            path: The absolute path of a file or directory.

        AddPathList(self: FileIOPermission, access: FileIOPermissionAccess, pathList: Array[str])

            Adds access for the specified files and directories to the existing state of the permission.

            access: A bitwise combination of the System.Security.Permissions.FileIOPermissionAccess values.

            pathList: An array containing the absolute paths of the files and directories.
        """
        ...
    def GetPathList(self, access):
        """
        GetPathList(self: FileIOPermission, access: FileIOPermissionAccess) -> Array[str]

            Gets all files and directories with the specified System.Security.Permissions.FileIOPermissionAccess.

            access: One of the System.Security.Permissions.FileIOPermissionAccess values that represents a single type of file access.

            Returns: An array containing the paths of the files and directories to which access specified by the access parameter is granted.
        """
        ...
    def SetPathList(self, access, *__args):
        """
        SetPathList(self: FileIOPermission, access: FileIOPermissionAccess, path: str)

            Sets the specified access to the specified file or directory, replacing the existing state of the permission.

            access: A bitwise combination of the System.Security.Permissions.FileIOPermissionAccess values.

            path: The absolute path of the file or directory.

        SetPathList(self: FileIOPermission, access: FileIOPermissionAccess, pathList: Array[str])

            Sets the specified access to the specified files and directories, replacing the current state for the specified access with the new set of paths.

            access: A bitwise combination of the System.Security.Permissions.FileIOPermissionAccess values.

            pathList: An array containing the absolute paths of the files and directories.
        """
        ...
    @staticmethod  # known case of __new__
    def __new__(cls, *__args):
        """
        __new__(cls: type, state: PermissionState)

        __new__(cls: type, access: FileIOPermissionAccess, path: str)

        __new__(cls: type, access: FileIOPermissionAccess, pathList: Array[str])

        __new__(cls: type, access: FileIOPermissionAccess, control: AccessControlActions, path: str)

        __new__(cls: type, access: FileIOPermissionAccess, control: AccessControlActions, pathList: Array[str])
        """
        ...
    @property
    def AllFiles(self):
        """
        Gets or sets the permitted access to all files.

        Get: AllFiles(self: FileIOPermission) -> FileIOPermissionAccess

        Set: AllFiles(self: FileIOPermission) = value
        """
        ...
    @property
    def AllLocalFiles(self):
        """
        Gets or sets the permitted access to all local files.

        Get: AllLocalFiles(self: FileIOPermission) -> FileIOPermissionAccess

        Set: AllLocalFiles(self: FileIOPermission) = value
        """
        ...

class FileIOPermissionAccess(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies the type of file access requested.

    enum (flags) FileIOPermissionAccess, values: AllAccess (15), Append (4), NoAccess (0), PathDiscovery (8), Read (1), Write (2)
    """

    AllAccess = None
    Append = None
    NoAccess = None
    PathDiscovery = None
    Read = None
    value__ = None
    Write = None

class FileIOPermissionAttribute(CodeAccessSecurityAttribute):  # skipped bases: <type '_Attribute'>
    """
    Allows security actions for System.Security.Permissions.FileIOPermission to be applied to code using declarative security. This class cannot be inherited.

    FileIOPermissionAttribute(action: SecurityAction)
    """

    def CreatePermission(self):
        """
        CreatePermission(self: FileIOPermissionAttribute) -> IPermission

            Creates and returns a new System.Security.Permissions.FileIOPermission.

            Returns: A System.Security.Permissions.FileIOPermission that corresponds to this attribute.
        """
        ...
    @property
    def All(self):
        """
        Gets or sets full access for the file or directory that is specified by the string value.

        Get: All(self: FileIOPermissionAttribute) -> str

        Set: All(self: FileIOPermissionAttribute) = value
        """
        ...
    @property
    def AllFiles(self):
        """
        Gets or sets the permitted access to all files.

        Get: AllFiles(self: FileIOPermissionAttribute) -> FileIOPermissionAccess

        Set: AllFiles(self: FileIOPermissionAttribute) = value
        """
        ...
    @property
    def AllLocalFiles(self):
        """
        Gets or sets the permitted access to all local files.

        Get: AllLocalFiles(self: FileIOPermissionAttribute) -> FileIOPermissionAccess

        Set: AllLocalFiles(self: FileIOPermissionAttribute) = value
        """
        ...
    @property
    def Append(self):
        """
        Gets or sets append access for the file or directory that is specified by the string value.

        Get: Append(self: FileIOPermissionAttribute) -> str

        Set: Append(self: FileIOPermissionAttribute) = value
        """
        ...
    @property
    def ChangeAccessControl(self):
        """
        Gets or sets the file or directory in which access control information can be changed.

        Get: ChangeAccessControl(self: FileIOPermissionAttribute) -> str

        Set: ChangeAccessControl(self: FileIOPermissionAttribute) = value
        """
        ...
    @property
    def PathDiscovery(self):
        """
        Gets or sets the file or directory to which to grant path discovery.

        Get: PathDiscovery(self: FileIOPermissionAttribute) -> str

        Set: PathDiscovery(self: FileIOPermissionAttribute) = value
        """
        ...
    @property
    def Read(self):
        """
        Gets or sets read access for the file or directory specified by the string value.

        Get: Read(self: FileIOPermissionAttribute) -> str

        Set: Read(self: FileIOPermissionAttribute) = value
        """
        ...
    @property
    def ViewAccessControl(self):
        """
        Gets or sets the file or directory in which access control information can be viewed.

        Get: ViewAccessControl(self: FileIOPermissionAttribute) -> str

        Set: ViewAccessControl(self: FileIOPermissionAttribute) = value
        """
        ...
    @property
    def ViewAndModify(self):
        """
        Gets or sets the file or directory in which file data can be viewed and modified.

        Get: ViewAndModify(self: FileIOPermissionAttribute) -> str

        Set: ViewAndModify(self: FileIOPermissionAttribute) = value
        """
        ...
    @property
    def Write(self):
        """
        Gets or sets write access for the file or directory specified by the string value.

        Get: Write(self: FileIOPermissionAttribute) -> str

        Set: Write(self: FileIOPermissionAttribute) = value
        """
        ...

class GacIdentityPermission(
    CodeAccessPermission, IBuiltInPermission
):  # skipped bases: <type 'ISecurityEncodable'>, <type 'IPermission'>, <type 'IStackWalk'>
    """
    Defines the identity permission for files originating in the global assembly cache. This class cannot be inherited.

    GacIdentityPermission(state: PermissionState)

    GacIdentityPermission()
    """

    @staticmethod  # known case of __new__
    def __new__(cls, state=None):
        """
        __new__(cls: type, state: PermissionState)

        __new__(cls: type)
        """
        ...

class GacIdentityPermissionAttribute(CodeAccessSecurityAttribute):  # skipped bases: <type '_Attribute'>
    """
    Allows security actions for System.Security.Permissions.GacIdentityPermission to be applied to code using declarative security. This class cannot be inherited.

    GacIdentityPermissionAttribute(action: SecurityAction)
    """

    def CreatePermission(self):
        """
        CreatePermission(self: GacIdentityPermissionAttribute) -> IPermission

            Creates a new System.Security.Permissions.GacIdentityPermission object.

            Returns: A System.Security.Permissions.GacIdentityPermission that corresponds to this attribute.
        """
        ...

class HostProtectionAttribute(CodeAccessSecurityAttribute):  # skipped bases: <type '_Attribute'>
    """
    Allows the use of declarative security actions to determine host protection requirements. This class cannot be inherited.

    HostProtectionAttribute()

    HostProtectionAttribute(action: SecurityAction)
    """

    def CreatePermission(self):
        """
        CreatePermission(self: HostProtectionAttribute) -> IPermission

            Creates and returns a new host protection permission.

            Returns: An System.Security.IPermission that corresponds to the current attribute.
        """
        ...
    @property
    def ExternalProcessMgmt(self):
        """
        Gets or sets a value indicating whether external process management is exposed.

        Get: ExternalProcessMgmt(self: HostProtectionAttribute) -> bool

        Set: ExternalProcessMgmt(self: HostProtectionAttribute) = value
        """
        ...
    @property
    def ExternalThreading(self):
        """
        Gets or sets a value indicating whether external threading is exposed.

        Get: ExternalThreading(self: HostProtectionAttribute) -> bool

        Set: ExternalThreading(self: HostProtectionAttribute) = value
        """
        ...
    @property
    def MayLeakOnAbort(self):
        """
        Gets or sets a value indicating whether resources might leak memory if the operation is terminated.

        Get: MayLeakOnAbort(self: HostProtectionAttribute) -> bool

        Set: MayLeakOnAbort(self: HostProtectionAttribute) = value
        """
        ...
    @property
    def Resources(self):
        """
        Gets or sets flags specifying categories of functionality that are potentially harmful to the host.

        Get: Resources(self: HostProtectionAttribute) -> HostProtectionResource

        Set: Resources(self: HostProtectionAttribute) = value
        """
        ...
    @property
    def SecurityInfrastructure(self):
        """
        Gets or sets a value indicating whether the security infrastructure is exposed.

        Get: SecurityInfrastructure(self: HostProtectionAttribute) -> bool

        Set: SecurityInfrastructure(self: HostProtectionAttribute) = value
        """
        ...
    @property
    def SelfAffectingProcessMgmt(self):
        """
        Gets or sets a value indicating whether self-affecting process management is exposed.

        Get: SelfAffectingProcessMgmt(self: HostProtectionAttribute) -> bool

        Set: SelfAffectingProcessMgmt(self: HostProtectionAttribute) = value
        """
        ...
    @property
    def SelfAffectingThreading(self):
        """
        Gets or sets a value indicating whether self-affecting threading is exposed.

        Get: SelfAffectingThreading(self: HostProtectionAttribute) -> bool

        Set: SelfAffectingThreading(self: HostProtectionAttribute) = value
        """
        ...
    @property
    def SharedState(self):
        """
        Gets or sets a value indicating whether shared state is exposed.

        Get: SharedState(self: HostProtectionAttribute) -> bool

        Set: SharedState(self: HostProtectionAttribute) = value
        """
        ...
    @property
    def Synchronization(self):
        """
        Gets or sets a value indicating whether synchronization is exposed.

        Get: Synchronization(self: HostProtectionAttribute) -> bool

        Set: Synchronization(self: HostProtectionAttribute) = value
        """
        ...
    @property
    def UI(self):
        """
        Gets or sets a value indicating whether the user interface is exposed.

        Get: UI(self: HostProtectionAttribute) -> bool

        Set: UI(self: HostProtectionAttribute) = value
        """
        ...

class HostProtectionResource(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies categories of functionality potentially harmful to the host if invoked by a method or class.

    enum (flags) HostProtectionResource, values: All (511), ExternalProcessMgmt (4), ExternalThreading (16), MayLeakOnAbort (256), None (0), SecurityInfrastructure (64), SelfAffectingProcessMgmt (8), SelfAffectingThreading (32), SharedState (2), Synchronization (1), UI (128)
    """

    All = None
    ExternalProcessMgmt = None
    ExternalThreading = None
    MayLeakOnAbort = None

    SecurityInfrastructure = None
    SelfAffectingProcessMgmt = None
    SelfAffectingThreading = None
    SharedState = None
    Synchronization = None
    UI = None
    value__ = None

class IsolatedStorageContainment(
    Enum
):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies the permitted use of isolated storage.

    enum IsolatedStorageContainment, values: AdministerIsolatedStorageByUser (112), ApplicationIsolationByMachine (69), ApplicationIsolationByRoamingUser (101), ApplicationIsolationByUser (21), AssemblyIsolationByMachine (64), AssemblyIsolationByRoamingUser (96), AssemblyIsolationByUser (32), DomainIsolationByMachine (48), DomainIsolationByRoamingUser (80), DomainIsolationByUser (16), None (0), UnrestrictedIsolatedStorage (240)
    """

    AdministerIsolatedStorageByUser = None
    ApplicationIsolationByMachine = None
    ApplicationIsolationByRoamingUser = None
    ApplicationIsolationByUser = None
    AssemblyIsolationByMachine = None
    AssemblyIsolationByRoamingUser = None
    AssemblyIsolationByUser = None
    DomainIsolationByMachine = None
    DomainIsolationByRoamingUser = None
    DomainIsolationByUser = None

    UnrestrictedIsolatedStorage = None
    value__ = None

class IsolatedStoragePermission(
    CodeAccessPermission, IUnrestrictedPermission
):  # skipped bases: <type 'ISecurityEncodable'>, <type 'IPermission'>, <type 'IStackWalk'>
    """Represents access to generic isolated storage capabilities."""

    @staticmethod  # known case of __new__
    def __new__(cls, *args):  # cannot find CLR constructor
        """__new__(cls: type, state: PermissionState)"""
        ...
    @property
    def UsageAllowed(self):
        """
        Gets or sets the type of isolated storage containment allowed.

        Get: UsageAllowed(self: IsolatedStoragePermission) -> IsolatedStorageContainment

        Set: UsageAllowed(self: IsolatedStoragePermission) = value
        """
        ...
    @property
    def UserQuota(self):
        """
        Gets or sets the quota on the overall size of each user's total store.

        Get: UserQuota(self: IsolatedStoragePermission) -> Int64

        Set: UserQuota(self: IsolatedStoragePermission) = value
        """
        ...

class IsolatedStorageFilePermission(
    IsolatedStoragePermission, IBuiltInPermission
):  # skipped bases: <type 'IUnrestrictedPermission'>, <type 'ISecurityEncodable'>, <type 'IPermission'>, <type 'IStackWalk'>
    """
    Specifies the allowed usage of a private virtual file system. This class cannot be inherited.

    IsolatedStorageFilePermission(state: PermissionState)
    """

    pass

class IsolatedStoragePermissionAttribute(CodeAccessSecurityAttribute):  # skipped bases: <type '_Attribute'>
    """Allows security actions for System.Security.Permissions.IsolatedStoragePermission to be applied to code using declarative security."""

    @property
    def UsageAllowed(self):
        """
        Gets or sets the level of isolated storage that should be declared.

        Get: UsageAllowed(self: IsolatedStoragePermissionAttribute) -> IsolatedStorageContainment

        Set: UsageAllowed(self: IsolatedStoragePermissionAttribute) = value
        """
        ...
    @property
    def UserQuota(self):
        """
        Gets or sets the maximum user storage quota size.

        Get: UserQuota(self: IsolatedStoragePermissionAttribute) -> Int64

        Set: UserQuota(self: IsolatedStoragePermissionAttribute) = value
        """
        ...

class IsolatedStorageFilePermissionAttribute(IsolatedStoragePermissionAttribute):  # skipped bases: <type '_Attribute'>
    """
    Allows security actions for System.Security.Permissions.IsolatedStorageFilePermission to be applied to code using declarative security. This class cannot be inherited.

    IsolatedStorageFilePermissionAttribute(action: SecurityAction)
    """

    def CreatePermission(self):
        """
        CreatePermission(self: IsolatedStorageFilePermissionAttribute) -> IPermission

            Creates and returns a new System.Security.Permissions.IsolatedStorageFilePermission.

            Returns: An System.Security.Permissions.IsolatedStorageFilePermission that corresponds to this attribute.
        """
        ...

class KeyContainerPermission(
    CodeAccessPermission, IUnrestrictedPermission, IBuiltInPermission
):  # skipped bases: <type 'ISecurityEncodable'>, <type 'IPermission'>, <type 'IStackWalk'>
    """
    Controls the ability to access key containers. This class cannot be inherited.

    KeyContainerPermission(state: PermissionState)

    KeyContainerPermission(flags: KeyContainerPermissionFlags)

    KeyContainerPermission(flags: KeyContainerPermissionFlags, accessList: Array[KeyContainerPermissionAccessEntry])
    """

    @staticmethod  # known case of __new__
    def __new__(cls, *__args):
        """
        __new__(cls: type, state: PermissionState)

        __new__(cls: type, flags: KeyContainerPermissionFlags)

        __new__(cls: type, flags: KeyContainerPermissionFlags, accessList: Array[KeyContainerPermissionAccessEntry])
        """
        ...
    @property
    def AccessEntries(self):
        """
        Gets the collection of System.Security.Permissions.KeyContainerPermissionAccessEntry objects associated with the current permission.

        Get: AccessEntries(self: KeyContainerPermission) -> KeyContainerPermissionAccessEntryCollection
        """
        ...
    @property
    def Flags(self):
        """
        Gets the key container permission flags that apply to all key containers associated with the permission.

        Get: Flags(self: KeyContainerPermission) -> KeyContainerPermissionFlags
        """
        ...

class KeyContainerPermissionAccessEntry:  # skipped bases: <type 'object'>
    """
    Specifies access rights for specific key containers. This class cannot be inherited.

    KeyContainerPermissionAccessEntry(keyContainerName: str, flags: KeyContainerPermissionFlags)

    KeyContainerPermissionAccessEntry(parameters: CspParameters, flags: KeyContainerPermissionFlags)

    KeyContainerPermissionAccessEntry(keyStore: str, providerName: str, providerType: int, keyContainerName: str, keySpec: int, flags: KeyContainerPermissionFlags)
    """

    def Equals(self, o):
        """
        Equals(self: KeyContainerPermissionAccessEntry, o: object) -> bool

            Determines whether the specified System.Security.Permissions.KeyContainerPermissionAccessEntry object is equal to the current instance.

            o: The System.Security.Permissions.KeyContainerPermissionAccessEntry object to compare with the currentinstance.

            Returns: ue if the specified System.Security.Permissions.KeyContainerPermissionAccessEntry is equal to the current System.Security.Permissions.KeyContainerPermissionAccessEntry object; otherwise, lse.
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: KeyContainerPermissionAccessEntry) -> int

            Gets a hash code for the current instance that is suitable for use in hashing algorithms and data structures such as a hash table.

            Returns: A hash code for the current System.Security.Permissions.KeyContainerPermissionAccessEntry object.
        """
        ...
    def __eq__(self, *args):  # cannot find CLR method
        """x.__eq__(y) <==> x==y"""
        ...
    def __ne__(self, *args): ...
    @property
    def Flags(self):
        """
        Gets or sets the key container permissions.

        Get: Flags(self: KeyContainerPermissionAccessEntry) -> KeyContainerPermissionFlags

        Set: Flags(self: KeyContainerPermissionAccessEntry) = value
        """
        ...
    @property
    def KeyContainerName(self):
        """
        Gets or sets the key container name.

        Get: KeyContainerName(self: KeyContainerPermissionAccessEntry) -> str

        Set: KeyContainerName(self: KeyContainerPermissionAccessEntry) = value
        """
        ...
    @property
    def KeySpec(self):
        """
        Gets or sets the key specification.

        Get: KeySpec(self: KeyContainerPermissionAccessEntry) -> int

        Set: KeySpec(self: KeyContainerPermissionAccessEntry) = value
        """
        ...
    @property
    def KeyStore(self):
        """
        Gets or sets the name of the key store.

        Get: KeyStore(self: KeyContainerPermissionAccessEntry) -> str

        Set: KeyStore(self: KeyContainerPermissionAccessEntry) = value
        """
        ...
    @property
    def ProviderName(self):
        """
        Gets or sets the provider name.

        Get: ProviderName(self: KeyContainerPermissionAccessEntry) -> str

        Set: ProviderName(self: KeyContainerPermissionAccessEntry) = value
        """
        ...
    @property
    def ProviderType(self):
        """
        Gets or sets the provider type.

        Get: ProviderType(self: KeyContainerPermissionAccessEntry) -> int

        Set: ProviderType(self: KeyContainerPermissionAccessEntry) = value
        """
        ...

class KeyContainerPermissionAccessEntryCollection(object, ICollection):  # skipped bases: <type 'IEnumerable'>
    """Represents a collection of System.Security.Permissions.KeyContainerPermissionAccessEntry objects. This class cannot be inherited."""

    def Add(self, accessEntry):
        """
        Add(self: KeyContainerPermissionAccessEntryCollection, accessEntry: KeyContainerPermissionAccessEntry) -> int

            Adds a System.Security.Permissions.KeyContainerPermissionAccessEntry object to the collection.

            accessEntry: The System.Security.Permissions.KeyContainerPermissionAccessEntry object to add.

            Returns: The index at which the new element was inserted.
        """
        ...
    def Clear(self):
        """
        Clear(self: KeyContainerPermissionAccessEntryCollection)

            Removes all the System.Security.Permissions.KeyContainerPermissionAccessEntry objects from the collection.
        """
        ...
    def GetEnumerator(self):
        """
        GetEnumerator(self: KeyContainerPermissionAccessEntryCollection) -> KeyContainerPermissionAccessEntryEnumerator

            Returns a System.Security.Permissions.KeyContainerPermissionAccessEntryEnumerator object that can be used to iterate through the objects in the collection.

            Returns: A System.Security.Permissions.KeyContainerPermissionAccessEntryEnumerator object that can be used to iterate through the collection.
        """
        ...
    def IndexOf(self, accessEntry):
        """
        IndexOf(self: KeyContainerPermissionAccessEntryCollection, accessEntry: KeyContainerPermissionAccessEntry) -> int

            Gets the index in the collection of the specified System.Security.Permissions.KeyContainerPermissionAccessEntry object, if it exists in the collection.

            accessEntry: The System.Security.Permissions.KeyContainerPermissionAccessEntry object to locate.

        """
        ...
    def Remove(self, accessEntry):
        """
        Remove(self: KeyContainerPermissionAccessEntryCollection, accessEntry: KeyContainerPermissionAccessEntry)

            Removes the specified System.Security.Permissions.KeyContainerPermissionAccessEntry object from thecollection.

            accessEntry: The System.Security.Permissions.KeyContainerPermissionAccessEntry object to remove.
        """
        ...
    def __add__(self, *args):  # cannot find CLR method
        """x.__add__(y) <==> x+y"""
        ...
    def __getitem__(self, *args):  # cannot find CLR method
        """x.__getitem__(y) <==> x[y]"""
        ...
    def __len__(self, *args):  # cannot find CLR method
        """x.__len__() <==> len(x)"""
        ...
    @property
    def Count(self):
        """
        Gets the number of items in the collection.

        Get: Count(self: KeyContainerPermissionAccessEntryCollection) -> int
        """
        ...
    @property
    def IsSynchronized(self):
        """
        Gets a value indicating whether the collection is synchronized (thread safe).

        Get: IsSynchronized(self: KeyContainerPermissionAccessEntryCollection) -> bool
        """
        ...
    @property
    def SyncRoot(self):
        """
        Gets an object that can be used to synchronize access to the collection.

        Get: SyncRoot(self: KeyContainerPermissionAccessEntryCollection) -> object
        """
        ...

class KeyContainerPermissionAccessEntryEnumerator(object, IEnumerator):
    """Represents the enumerator for System.Security.Permissions.KeyContainerPermissionAccessEntry objects in a System.Security.Permissions.KeyContainerPermissionAccessEntryCollection."""

    @property
    def Current(self):
        """
        Gets the current entry in the collection.

        Get: Current(self: KeyContainerPermissionAccessEntryEnumerator) -> KeyContainerPermissionAccessEntry
        """
        ...

class KeyContainerPermissionAttribute(CodeAccessSecurityAttribute):  # skipped bases: <type '_Attribute'>
    """
    Allows security actions for System.Security.Permissions.KeyContainerPermission to be applied to code using declarative security. This class cannot be inherited.

    KeyContainerPermissionAttribute(action: SecurityAction)
    """

    def CreatePermission(self):
        """
        CreatePermission(self: KeyContainerPermissionAttribute) -> IPermission

            Creates and returns a new System.Security.Permissions.KeyContainerPermission.

            Returns: A System.Security.Permissions.KeyContainerPermission that corresponds to the attribute.
        """
        ...
    @property
    def Flags(self):
        """
        Gets or sets the key container permissions.

        Get: Flags(self: KeyContainerPermissionAttribute) -> KeyContainerPermissionFlags

        Set: Flags(self: KeyContainerPermissionAttribute) = value
        """
        ...
    @property
    def KeyContainerName(self):
        """
        Gets or sets the name of the key container.

        Get: KeyContainerName(self: KeyContainerPermissionAttribute) -> str

        Set: KeyContainerName(self: KeyContainerPermissionAttribute) = value
        """
        ...
    @property
    def KeySpec(self):
        """
        Gets or sets the key specification.

        Get: KeySpec(self: KeyContainerPermissionAttribute) -> int

        Set: KeySpec(self: KeyContainerPermissionAttribute) = value
        """
        ...
    @property
    def KeyStore(self):
        """
        Gets or sets the name of the key store.

        Get: KeyStore(self: KeyContainerPermissionAttribute) -> str

        Set: KeyStore(self: KeyContainerPermissionAttribute) = value
        """
        ...
    @property
    def ProviderName(self):
        """
        Gets or sets the provider name.

        Get: ProviderName(self: KeyContainerPermissionAttribute) -> str

        Set: ProviderName(self: KeyContainerPermissionAttribute) = value
        """
        ...
    @property
    def ProviderType(self):
        """
        Gets or sets the provider type.

        Get: ProviderType(self: KeyContainerPermissionAttribute) -> int

        Set: ProviderType(self: KeyContainerPermissionAttribute) = value
        """
        ...

class KeyContainerPermissionFlags(
    Enum
):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies the type of key container access allowed.

    enum (flags) KeyContainerPermissionFlags, values: AllFlags (13111), ChangeAcl (8192), Create (1), Decrypt (512), Delete (4), Export (32), Import (16), NoFlags (0), Open (2), Sign (256), ViewAcl (4096)
    """

    AllFlags = None
    ChangeAcl = None
    Create = None
    Decrypt = None
    Delete = None
    Export = None
    Import = None
    NoFlags = None
    Open = None
    Sign = None
    value__ = None
    ViewAcl = None

class PermissionSetAttribute(CodeAccessSecurityAttribute):  # skipped bases: <type '_Attribute'>
    """
    Allows security actions for a System.Security.PermissionSet to be applied to code using declarative security. This class cannot be inherited.

    PermissionSetAttribute(action: SecurityAction)
    """

    def CreatePermission(self):
        """
        CreatePermission(self: PermissionSetAttribute) -> IPermission

            This method is not used.

            Returns: A null reference (thing in Visual Basic) in all cases.
        """
        ...
    def CreatePermissionSet(self):
        """
        CreatePermissionSet(self: PermissionSetAttribute) -> PermissionSet

            Creates and returns a new permission set based on this permission set attribute object.

            Returns: A new permission set.
        """
        ...
    @property
    def File(self):
        """
        Gets or sets a file containing the XML representation of a custom permission set to be declared.

        Get: File(self: PermissionSetAttribute) -> str

        Set: File(self: PermissionSetAttribute) = value
        """
        ...
    @property
    def Hex(self):
        """
        Gets or sets the hexadecimal representation of the XML encoded permission set.

        Get: Hex(self: PermissionSetAttribute) -> str

        Set: Hex(self: PermissionSetAttribute) = value
        """
        ...
    @property
    def Name(self):
        """
        Gets or sets the name of the permission set.

        Get: Name(self: PermissionSetAttribute) -> str

        Set: Name(self: PermissionSetAttribute) = value
        """
        ...
    @property
    def UnicodeEncoded(self):
        """
        Gets or sets a value indicating whether the file specified by System.Security.Permissions.PermissionSetAttribute.File is Unicode or ASCII encoded.

        Get: UnicodeEncoded(self: PermissionSetAttribute) -> bool

        Set: UnicodeEncoded(self: PermissionSetAttribute) = value
        """
        ...
    @property
    def XML(self):
        """
        Gets or sets the XML representation of a permission set.

        Get: XML(self: PermissionSetAttribute) -> str

        Set: XML(self: PermissionSetAttribute) = value
        """
        ...

class PermissionState(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies whether a permission should have all or no access to resources at creation.

    enum PermissionState, values: None (0), Unrestricted (1)
    """

    Unrestricted = None
    value__ = None

class PrincipalPermission(
    object, IPermission, IUnrestrictedPermission, IBuiltInPermission
):  # skipped bases: <type 'ISecurityEncodable'>
    """
    Allows checks against the active principal (see System.Security.Principal.IPrincipal) using the language constructs defined for both declarative and imperative security actions. This class cannot be inherited.

    PrincipalPermission(state: PermissionState)

    PrincipalPermission(name: str, role: str)

    PrincipalPermission(name: str, role: str, isAuthenticated: bool)
    """

    def Equals(self, obj):
        """
        Equals(self: PrincipalPermission, obj: object) -> bool

            Determines whether the specified System.Security.Permissions.PrincipalPermission object is equal to the current System.Security.Permissions.PrincipalPermission.

            obj: The System.Security.Permissions.PrincipalPermission object to compare with the current System.Security.Permissions.PrincipalPermission.

            Returns: ue if the specified System.Security.Permissions.PrincipalPermission is equal to the current System.Security.Permissions.PrincipalPermission object; otherwise, lse.
        """
        ...
    def FromXml(self, elem):
        """
        FromXml(self: PrincipalPermission, elem: SecurityElement)

            Reconstructs a permission with a specified state from an XML encoding.

            elem: The XML encoding to use to reconstruct the permission.
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: PrincipalPermission) -> int

            Gets a hash code for the System.Security.Permissions.PrincipalPermission object that is suitable for use in hashing algorithms and data structures such as a hash table.

            Returns: A hash code for the current System.Security.Permissions.PrincipalPermission object.
        """
        ...
    def ToString(self):
        """
        ToString(self: PrincipalPermission) -> str

            Creates and returns a string representing the current permission.

            Returns: A representation of the current permission.
        """
        ...
    def ToXml(self):
        """
        ToXml(self: PrincipalPermission) -> SecurityElement

            Creates an XML encoding of the permission and its current state.

            Returns: An XML encoding of the permission, including any state information.
        """
        ...
    def __eq__(self, *args):  # cannot find CLR method
        """x.__eq__(y) <==> x==y"""
        ...
    def __ne__(self, *args): ...

class PrincipalPermissionAttribute(CodeAccessSecurityAttribute):  # skipped bases: <type '_Attribute'>
    """
    Allows security actions for System.Security.Permissions.PrincipalPermission to be applied to code using declarative security. This class cannot be inherited.

    PrincipalPermissionAttribute(action: SecurityAction)
    """

    def CreatePermission(self):
        """
        CreatePermission(self: PrincipalPermissionAttribute) -> IPermission

            Creates and returns a new System.Security.Permissions.PrincipalPermission.

            Returns: A System.Security.Permissions.PrincipalPermission that corresponds to this attribute.
        """
        ...
    @property
    def Authenticated(self):
        """
        Gets or sets a value indicating whether the current principal has been authenticated by the underlying role-based security provider.

        Get: Authenticated(self: PrincipalPermissionAttribute) -> bool

        Set: Authenticated(self: PrincipalPermissionAttribute) = value
        """
        ...
    @property
    def Name(self):
        """
        Gets or sets the name of the identity associated with the current principal.

        Get: Name(self: PrincipalPermissionAttribute) -> str

        Set: Name(self: PrincipalPermissionAttribute) = value
        """
        ...
    @property
    def Role(self):
        """
        Gets or sets membership in a specified security role.

        Get: Role(self: PrincipalPermissionAttribute) -> str

        Set: Role(self: PrincipalPermissionAttribute) = value
        """
        ...

class PublisherIdentityPermission(
    CodeAccessPermission, IBuiltInPermission
):  # skipped bases: <type 'ISecurityEncodable'>, <type 'IPermission'>, <type 'IStackWalk'>
    """
    Represents the identity of a software publisher. This class cannot be inherited.

    PublisherIdentityPermission(state: PermissionState)

    PublisherIdentityPermission(certificate: X509Certificate)
    """

    @staticmethod  # known case of __new__
    def __new__(cls, *__args):
        """
        __new__(cls: type, state: PermissionState)

        __new__(cls: type, certificate: X509Certificate)
        """
        ...
    @property
    def Certificate(self):
        """
        Gets or sets an Authenticode X.509v3 certificate that represents the identity of the software publisher.

        Get: Certificate(self: PublisherIdentityPermission) -> X509Certificate

        Set: Certificate(self: PublisherIdentityPermission) = value
        """
        ...

class PublisherIdentityPermissionAttribute(CodeAccessSecurityAttribute):  # skipped bases: <type '_Attribute'>
    """
    Allows security actions for System.Security.Permissions.PublisherIdentityPermission to be applied to code using declarative security. This class cannot be inherited.

    PublisherIdentityPermissionAttribute(action: SecurityAction)
    """

    def CreatePermission(self):
        """
        CreatePermission(self: PublisherIdentityPermissionAttribute) -> IPermission

            Creates and returns a new instance of System.Security.Permissions.PublisherIdentityPermission.

            Returns: A System.Security.Permissions.PublisherIdentityPermission that corresponds to this attribute.
        """
        ...
    @property
    def CertFile(self):
        """
        Gets or sets a certification file containing an Authenticode X.509v3 certificate.

        Get: CertFile(self: PublisherIdentityPermissionAttribute) -> str

        Set: CertFile(self: PublisherIdentityPermissionAttribute) = value
        """
        ...
    @property
    def SignedFile(self):
        """
        Gets or sets a signed file from which to extract an Authenticode X.509v3 certificate.

        Get: SignedFile(self: PublisherIdentityPermissionAttribute) -> str

        Set: SignedFile(self: PublisherIdentityPermissionAttribute) = value
        """
        ...
    @property
    def X509Certificate(self):
        """
        Gets or sets an Authenticode X.509v3 certificate that identifies the publisher of the calling code.

        Get: X509Certificate(self: PublisherIdentityPermissionAttribute) -> str

        Set: X509Certificate(self: PublisherIdentityPermissionAttribute) = value
        """
        ...

class ReflectionPermission(
    CodeAccessPermission, IUnrestrictedPermission, IBuiltInPermission
):  # skipped bases: <type 'ISecurityEncodable'>, <type 'IPermission'>, <type 'IStackWalk'>
    """
    Controls access to non-public types and members through the System.Reflection APIs. Controls some features of the System.Reflection.Emit APIs.

    ReflectionPermission(state: PermissionState)

    ReflectionPermission(flag: ReflectionPermissionFlag)
    """

    @staticmethod  # known case of __new__
    def __new__(cls, *__args):
        """
        __new__(cls: type, state: PermissionState)

        __new__(cls: type, flag: ReflectionPermissionFlag)
        """
        ...
    @property
    def Flags(self):
        """
        Gets or sets the type of reflection allowed for the current permission.

        Get: Flags(self: ReflectionPermission) -> ReflectionPermissionFlag

        Set: Flags(self: ReflectionPermission) = value
        """
        ...

class ReflectionPermissionAttribute(CodeAccessSecurityAttribute):  # skipped bases: <type '_Attribute'>
    """
    Allows security actions for System.Security.Permissions.ReflectionPermission to be applied to code using declarative security.

    ReflectionPermissionAttribute(action: SecurityAction)
    """

    def CreatePermission(self):
        """
        CreatePermission(self: ReflectionPermissionAttribute) -> IPermission

            Creates and returns a new System.Security.Permissions.ReflectionPermission.

            Returns: A System.Security.Permissions.ReflectionPermission that corresponds to this attribute.
        """
        ...
    @property
    def Flags(self):
        """
        Gets or sets the current allowed uses of reflection.

        Get: Flags(self: ReflectionPermissionAttribute) -> ReflectionPermissionFlag

        Set: Flags(self: ReflectionPermissionAttribute) = value
        """
        ...
    @property
    def MemberAccess(self):
        """
        Gets or sets a value that indicates whether invocation of operations on non-public members is allowed.

        Get: MemberAccess(self: ReflectionPermissionAttribute) -> bool

        Set: MemberAccess(self: ReflectionPermissionAttribute) = value
        """
        ...
    @property
    def ReflectionEmit(self):
        """
        Gets or sets a value that indicates whether use of certain features in System.Reflection.Emit, such as emitting debug symbols, is allowed.

        Get: ReflectionEmit(self: ReflectionPermissionAttribute) -> bool

        Set: ReflectionEmit(self: ReflectionPermissionAttribute) = value
        """
        ...
    @property
    def RestrictedMemberAccess(self):
        """
        Gets or sets a value that indicates whether restricted invocation of non-public members is allowed. Restricted invocation means that the grant set of the assembly that contains the non-public member that is being invoked must be equal to, or a subset of, the grant set of the invoking assembly.

        Get: RestrictedMemberAccess(self: ReflectionPermissionAttribute) -> bool

        Set: RestrictedMemberAccess(self: ReflectionPermissionAttribute) = value
        """
        ...
    @property
    def TypeInformation(self):
        """
        Gets or sets a value that indicates whether reflection on members that are not visible is allowed.

        Get: TypeInformation(self: ReflectionPermissionAttribute) -> bool

        Set: TypeInformation(self: ReflectionPermissionAttribute) = value
        """
        ...

class ReflectionPermissionFlag(
    Enum
):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies the permitted use of the System.Reflection and System.Reflection.Emit namespaces.

    enum (flags) ReflectionPermissionFlag, values: AllFlags (7), MemberAccess (2), NoFlags (0), ReflectionEmit (4), RestrictedMemberAccess (8), TypeInformation (1)
    """

    AllFlags = None
    MemberAccess = None
    NoFlags = None
    ReflectionEmit = None
    RestrictedMemberAccess = None
    TypeInformation = None
    value__ = None

class RegistryPermission(
    CodeAccessPermission, IUnrestrictedPermission, IBuiltInPermission
):  # skipped bases: <type 'ISecurityEncodable'>, <type 'IPermission'>, <type 'IStackWalk'>
    """
    Controls the ability to access registry variables. This class cannot be inherited.

    RegistryPermission(state: PermissionState)

    RegistryPermission(access: RegistryPermissionAccess, pathList: str)

    RegistryPermission(access: RegistryPermissionAccess, control: AccessControlActions, pathList: str)
    """

    def AddPathList(self, access, *__args):
        """
        AddPathList(self: RegistryPermission, access: RegistryPermissionAccess, pathList: str)

            Adds access for the specified registry variables to the existing state of the permission.

            access: One of the System.Security.Permissions.RegistryPermissionAccess values.

            pathList: A list of registry variables (semicolon-separated).

        AddPathList(self: RegistryPermission, access: RegistryPermissionAccess, control: AccessControlActions, pathList: str)

            Adds access for the specified registry variables to the existing state of the permission, specifying registry permission access and access control actions.

            access: One of the System.Security.Permissions.RegistryPermissionAccess values.

            control: One of the System.Security.AccessControl.AccessControlActions values.

            pathList: A list of registry variables (separated by semicolons).
        """
        ...
    def GetPathList(self, access):
        """
        GetPathList(self: RegistryPermission, access: RegistryPermissionAccess) -> str

            Gets paths for all registry variables with the specified System.Security.Permissions.RegistryPermissionAccess.

            access: One of the System.Security.Permissions.RegistryPermissionAccess values that represents a single type of registry variable access.

            Returns: A list of the registry variables (semicolon-separated) with the specified System.Security.Permissions.RegistryPermissionAccess.
        """
        ...
    def SetPathList(self, access, pathList):
        """
        SetPathList(self: RegistryPermission, access: RegistryPermissionAccess, pathList: str)

            Sets new access for the specified registry variable names to the existing state of the permission.

            access: One of the System.Security.Permissions.RegistryPermissionAccess values.

            pathList: A list of registry variables (semicolon-separated).
        """
        ...
    @staticmethod  # known case of __new__
    def __new__(cls, *__args):
        """
        __new__(cls: type, state: PermissionState)

        __new__(cls: type, access: RegistryPermissionAccess, pathList: str)

        __new__(cls: type, access: RegistryPermissionAccess, control: AccessControlActions, pathList: str)
        """
        ...

class RegistryPermissionAccess(
    Enum
):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies the permitted access to registry keys and values.

    enum (flags) RegistryPermissionAccess, values: AllAccess (7), Create (4), NoAccess (0), Read (1), Write (2)
    """

    AllAccess = None
    Create = None
    NoAccess = None
    Read = None
    value__ = None
    Write = None

class RegistryPermissionAttribute(CodeAccessSecurityAttribute):  # skipped bases: <type '_Attribute'>
    """
    Allows security actions for System.Security.Permissions.RegistryPermission to be applied to code using declarative security. This class cannot be inherited.

    RegistryPermissionAttribute(action: SecurityAction)
    """

    def CreatePermission(self):
        """
        CreatePermission(self: RegistryPermissionAttribute) -> IPermission

            Creates and returns a new System.Security.Permissions.RegistryPermission.

            Returns: A System.Security.Permissions.RegistryPermission that corresponds to this attribute.
        """
        ...
    @property
    def All(self):
        """
        Gets or sets full access for the specified registry keys.

        Get: All(self: RegistryPermissionAttribute) -> str

        Set: All(self: RegistryPermissionAttribute) = value
        """
        ...
    @property
    def ChangeAccessControl(self):
        """
        Gets or sets change access control for the specified registry keys.

        Get: ChangeAccessControl(self: RegistryPermissionAttribute) -> str

        Set: ChangeAccessControl(self: RegistryPermissionAttribute) = value
        """
        ...
    @property
    def Create(self):
        """
        Gets or sets create-level access for the specified registry keys.

        Get: Create(self: RegistryPermissionAttribute) -> str

        Set: Create(self: RegistryPermissionAttribute) = value
        """
        ...
    @property
    def Read(self):
        """
        Gets or sets read access for the specified registry keys.

        Get: Read(self: RegistryPermissionAttribute) -> str

        Set: Read(self: RegistryPermissionAttribute) = value
        """
        ...
    @property
    def ViewAccessControl(self):
        """
        Gets or sets view access control for the specified registry keys.

        Get: ViewAccessControl(self: RegistryPermissionAttribute) -> str

        Set: ViewAccessControl(self: RegistryPermissionAttribute) = value
        """
        ...
    @property
    def ViewAndModify(self):
        """
        Gets or sets a specified set of registry keys that can be viewed and modified.

        Get: ViewAndModify(self: RegistryPermissionAttribute) -> str

        Set: ViewAndModify(self: RegistryPermissionAttribute) = value
        """
        ...
    @property
    def Write(self):
        """
        Gets or sets write access for the specified registry keys.

        Get: Write(self: RegistryPermissionAttribute) -> str

        Set: Write(self: RegistryPermissionAttribute) = value
        """
        ...

class ResourcePermissionBase(
    CodeAccessPermission, IUnrestrictedPermission
):  # skipped bases: <type 'ISecurityEncodable'>, <type 'IPermission'>, <type 'IStackWalk'>
    """Allows control of code access security permissions."""

    def AddPermissionAccess(self, *args):  # cannot find CLR method
        """
        AddPermissionAccess(self: ResourcePermissionBase, entry: ResourcePermissionBaseEntry)

            Adds a permission entry to the permission.

            entry: The System.Security.Permissions.ResourcePermissionBaseEntry to add.
        """
        ...
    def Clear(self, *args):  # cannot find CLR method
        """
        Clear(self: ResourcePermissionBase)

            Clears the permission of the added permission entries.
        """
        ...
    def GetPermissionEntries(self, *args):  # cannot find CLR method
        """
        GetPermissionEntries(self: ResourcePermissionBase) -> Array[ResourcePermissionBaseEntry]

            Returns an array of the System.Security.Permissions.ResourcePermissionBaseEntry objects added to this permission.

            Returns: An array of System.Security.Permissions.ResourcePermissionBaseEntry objects that were added to this permission.
        """
        ...
    def RemovePermissionAccess(self, *args):  # cannot find CLR method
        """
        RemovePermissionAccess(self: ResourcePermissionBase, entry: ResourcePermissionBaseEntry)

            Removes a permission entry from the permission.

            entry: The System.Security.Permissions.ResourcePermissionBaseEntry to remove.
        """
        ...
    @staticmethod  # known case of __new__
    def __new__(cls, *args):  # cannot find CLR constructor
        """
        __new__(cls: type)

        __new__(cls: type, state: PermissionState)
        """
        ...
    @property
    def PermissionAccessType(self):
        """Gets or sets an enumeration value that describes the types of access that you are giving the resource."""
        ...
    @property
    def TagNames(self):
        """Gets or sets an array of strings that identify the resource you are protecting."""
        ...
    Any = "*"
    Local = "."

class ResourcePermissionBaseEntry:  # skipped bases: <type 'object'>
    """
    Defines the smallest unit of a code access security permission set.

    ResourcePermissionBaseEntry()

    ResourcePermissionBaseEntry(permissionAccess: int, permissionAccessPath: Array[str])
    """

    @property
    def PermissionAccess(self):
        """
        Gets an integer representation of the access level enumeration value.

        Get: PermissionAccess(self: ResourcePermissionBaseEntry) -> int
        """
        ...
    @property
    def PermissionAccessPath(self):
        """
        Gets an array of strings that identify the resource you are protecting.

        Get: PermissionAccessPath(self: ResourcePermissionBaseEntry) -> Array[str]
        """
        ...

class SecurityAction(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies the security actions that can be performed using declarative security.

    enum SecurityAction, values: Assert (3), Demand (2), Deny (4), InheritanceDemand (7), LinkDemand (6), PermitOnly (5), RequestMinimum (8), RequestOptional (9), RequestRefuse (10)
    """

    Assert = None
    Demand = None
    Deny = None
    InheritanceDemand = None
    LinkDemand = None
    PermitOnly = None
    RequestMinimum = None
    RequestOptional = None
    RequestRefuse = None
    value__ = None

class SecurityPermission(
    CodeAccessPermission, IUnrestrictedPermission, IBuiltInPermission
):  # skipped bases: <type 'ISecurityEncodable'>, <type 'IPermission'>, <type 'IStackWalk'>
    """
    Describes a set of security permissions applied to code. This class cannot be inherited.

    SecurityPermission(state: PermissionState)

    SecurityPermission(flag: SecurityPermissionFlag)
    """

    @staticmethod  # known case of __new__
    def __new__(cls, *__args):
        """
        __new__(cls: type, state: PermissionState)

        __new__(cls: type, flag: SecurityPermissionFlag)
        """
        ...
    @property
    def Flags(self):
        """
        Gets or sets the security permission flags.

        Get: Flags(self: SecurityPermission) -> SecurityPermissionFlag

        Set: Flags(self: SecurityPermission) = value
        """
        ...

class SecurityPermissionAttribute(CodeAccessSecurityAttribute):  # skipped bases: <type '_Attribute'>
    """
    Allows security actions for System.Security.Permissions.SecurityPermission to be applied to code using declarative security. This class cannot be inherited.

    SecurityPermissionAttribute(action: SecurityAction)
    """

    def CreatePermission(self):
        """
        CreatePermission(self: SecurityPermissionAttribute) -> IPermission

            Creates and returns a new System.Security.Permissions.SecurityPermission.

            Returns: A System.Security.Permissions.SecurityPermission that corresponds to this attribute.
        """
        ...
    @property
    def Assertion(self):
        """
        Gets or sets a value indicating whether permission to assert that all this code's callers have the requisite permission for the operation is declared.

        Get: Assertion(self: SecurityPermissionAttribute) -> bool

        Set: Assertion(self: SecurityPermissionAttribute) = value
        """
        ...
    @property
    def BindingRedirects(self):
        """
        Gets or sets a value that indicates whether code has permission to perform binding redirection in the application configuration file.

        Get: BindingRedirects(self: SecurityPermissionAttribute) -> bool

        Set: BindingRedirects(self: SecurityPermissionAttribute) = value
        """
        ...
    @property
    def ControlAppDomain(self):
        """
        Gets or sets a value indicating whether permission to manipulate System.AppDomain is declared.

        Get: ControlAppDomain(self: SecurityPermissionAttribute) -> bool

        Set: ControlAppDomain(self: SecurityPermissionAttribute) = value
        """
        ...
    @property
    def ControlDomainPolicy(self):
        """
        Gets or sets a value indicating whether permission to alter or manipulate domain security policy is declared.

        Get: ControlDomainPolicy(self: SecurityPermissionAttribute) -> bool

        Set: ControlDomainPolicy(self: SecurityPermissionAttribute) = value
        """
        ...
    @property
    def ControlEvidence(self):
        """
        Gets or sets a value indicating whether permission to alter or manipulate evidence is declared.

        Get: ControlEvidence(self: SecurityPermissionAttribute) -> bool

        Set: ControlEvidence(self: SecurityPermissionAttribute) = value
        """
        ...
    @property
    def ControlPolicy(self):
        """
        Gets or sets a value indicating whether permission to view and manipulate security policy is declared.

        Get: ControlPolicy(self: SecurityPermissionAttribute) -> bool

        Set: ControlPolicy(self: SecurityPermissionAttribute) = value
        """
        ...
    @property
    def ControlPrincipal(self):
        """
        Gets or sets a value indicating whether permission to manipulate the current principal is declared.

        Get: ControlPrincipal(self: SecurityPermissionAttribute) -> bool

        Set: ControlPrincipal(self: SecurityPermissionAttribute) = value
        """
        ...
    @property
    def ControlThread(self):
        """
        Gets or sets a value indicating whether permission to manipulate threads is declared.

        Get: ControlThread(self: SecurityPermissionAttribute) -> bool

        Set: ControlThread(self: SecurityPermissionAttribute) = value
        """
        ...
    @property
    def Execution(self):
        """
        Gets or sets a value indicating whether permission to execute code is declared.

        Get: Execution(self: SecurityPermissionAttribute) -> bool

        Set: Execution(self: SecurityPermissionAttribute) = value
        """
        ...
    @property
    def Flags(self):
        """
        Gets or sets all permission flags comprising the System.Security.Permissions.SecurityPermission permissions.

        Get: Flags(self: SecurityPermissionAttribute) -> SecurityPermissionFlag

        Set: Flags(self: SecurityPermissionAttribute) = value
        """
        ...
    @property
    def Infrastructure(self):
        """
        Gets or sets a value indicating whether code can plug into the common language runtime infrastructure, such as adding Remoting Context Sinks, Envoy Sinks and Dynamic Sinks.

        Get: Infrastructure(self: SecurityPermissionAttribute) -> bool

        Set: Infrastructure(self: SecurityPermissionAttribute) = value
        """
        ...
    @property
    def RemotingConfiguration(self):
        """
        Gets or sets a value indicating whether code can configure remoting types and channels.

        Get: RemotingConfiguration(self: SecurityPermissionAttribute) -> bool

        Set: RemotingConfiguration(self: SecurityPermissionAttribute) = value
        """
        ...
    @property
    def SerializationFormatter(self):
        """
        Gets or sets a value indicating whether code can use a serialization formatter to serialize or deserialize an object.

        Get: SerializationFormatter(self: SecurityPermissionAttribute) -> bool

        Set: SerializationFormatter(self: SecurityPermissionAttribute) = value
        """
        ...
    @property
    def SkipVerification(self):
        """
        Gets or sets a value indicating whether permission to bypass code verification is declared.

        Get: SkipVerification(self: SecurityPermissionAttribute) -> bool

        Set: SkipVerification(self: SecurityPermissionAttribute) = value
        """
        ...
    @property
    def UnmanagedCode(self):
        """
        Gets or sets a value indicating whether permission to call unmanaged code is declared.

        Get: UnmanagedCode(self: SecurityPermissionAttribute) -> bool

        Set: UnmanagedCode(self: SecurityPermissionAttribute) = value
        """
        ...

class SecurityPermissionFlag(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies access flags for the security permission object.

    enum (flags) SecurityPermissionFlag, values: AllFlags (16383), Assertion (1), BindingRedirects (8192), ControlAppDomain (1024), ControlDomainPolicy (256), ControlEvidence (32), ControlPolicy (64), ControlPrincipal (512), ControlThread (16), Execution (8), Infrastructure (4096), NoFlags (0), RemotingConfiguration (2048), SerializationFormatter (128), SkipVerification (4), UnmanagedCode (2)
    """

    AllFlags = None
    Assertion = None
    BindingRedirects = None
    ControlAppDomain = None
    ControlDomainPolicy = None
    ControlEvidence = None
    ControlPolicy = None
    ControlPrincipal = None
    ControlThread = None
    Execution = None
    Infrastructure = None
    NoFlags = None
    RemotingConfiguration = None
    SerializationFormatter = None
    SkipVerification = None
    UnmanagedCode = None
    value__ = None

class SiteIdentityPermission(
    CodeAccessPermission, IBuiltInPermission
):  # skipped bases: <type 'ISecurityEncodable'>, <type 'IPermission'>, <type 'IStackWalk'>
    """
    Defines the identity permission for the Web site from which the code originates. This class cannot be inherited.

    SiteIdentityPermission(state: PermissionState)

    SiteIdentityPermission(site: str)
    """

    @staticmethod  # known case of __new__
    def __new__(cls, *__args):
        """
        __new__(cls: type, state: PermissionState)

        __new__(cls: type, site: str)
        """
        ...
    @property
    def Site(self):
        """
        Gets or sets the current site.

        Get: Site(self: SiteIdentityPermission) -> str

        Set: Site(self: SiteIdentityPermission) = value
        """
        ...

class SiteIdentityPermissionAttribute(CodeAccessSecurityAttribute):  # skipped bases: <type '_Attribute'>
    """
    Allows security actions for System.Security.Permissions.SiteIdentityPermission to be applied to code using declarative security. This class cannot be inherited.

    SiteIdentityPermissionAttribute(action: SecurityAction)
    """

    def CreatePermission(self):
        """
        CreatePermission(self: SiteIdentityPermissionAttribute) -> IPermission

            Creates and returns a new instance of System.Security.Permissions.SiteIdentityPermission.

            Returns: A System.Security.Permissions.SiteIdentityPermission that corresponds to this attribute.
        """
        ...
    @property
    def Site(self):
        """
        Gets or sets the site name of the calling code.

        Get: Site(self: SiteIdentityPermissionAttribute) -> str

        Set: Site(self: SiteIdentityPermissionAttribute) = value
        """
        ...

class StorePermission(
    CodeAccessPermission, IUnrestrictedPermission
):  # skipped bases: <type 'ISecurityEncodable'>, <type 'IPermission'>, <type 'IStackWalk'>
    """
    Controls access to stores containing X.509 certificates. This class cannot be inherited.

    StorePermission(state: PermissionState)

    StorePermission(flag: StorePermissionFlags)
    """

    @staticmethod  # known case of __new__
    def __new__(cls, *__args):
        """
        __new__(cls: type, state: PermissionState)

        __new__(cls: type, flag: StorePermissionFlags)
        """
        ...
    @property
    def Flags(self):
        """
        Gets or sets the type of System.Security.Cryptography.X509Certificates.X509Store access allowed by the current permission.

        Get: Flags(self: StorePermission) -> StorePermissionFlags

        Set: Flags(self: StorePermission) = value
        """
        ...

class StorePermissionAttribute(CodeAccessSecurityAttribute):  # skipped bases: <type '_Attribute'>
    """
    Allows security actions for System.Security.Permissions.StorePermission to be applied to code using declarative security. This class cannot be inherited.

    StorePermissionAttribute(action: SecurityAction)
    """

    def CreatePermission(self):
        """
        CreatePermission(self: StorePermissionAttribute) -> IPermission

            Creates and returns a new System.Security.Permissions.StorePermission.

            Returns: A System.Security.Permissions.StorePermission that corresponds to the attribute.
        """
        ...
    @property
    def AddToStore(self):
        """
        Gets or sets a value indicating whether the code is permitted to add to a store.

        Get: AddToStore(self: StorePermissionAttribute) -> bool

        Set: AddToStore(self: StorePermissionAttribute) = value
        """
        ...
    @property
    def CreateStore(self):
        """
        Gets or sets a value indicating whether the code is permitted to create a store.

        Get: CreateStore(self: StorePermissionAttribute) -> bool

        Set: CreateStore(self: StorePermissionAttribute) = value
        """
        ...
    @property
    def DeleteStore(self):
        """
        Gets or sets a value indicating whether the code is permitted to delete a store.

        Get: DeleteStore(self: StorePermissionAttribute) -> bool

        Set: DeleteStore(self: StorePermissionAttribute) = value
        """
        ...
    @property
    def EnumerateCertificates(self):
        """
        Gets or sets a value indicating whether the code is permitted to enumerate the certificates in a store.

        Get: EnumerateCertificates(self: StorePermissionAttribute) -> bool

        Set: EnumerateCertificates(self: StorePermissionAttribute) = value
        """
        ...
    @property
    def EnumerateStores(self):
        """
        Gets or sets a value indicating whether the code is permitted to enumerate stores.

        Get: EnumerateStores(self: StorePermissionAttribute) -> bool

        Set: EnumerateStores(self: StorePermissionAttribute) = value
        """
        ...
    @property
    def Flags(self):
        """
        Gets or sets the store permissions.

        Get: Flags(self: StorePermissionAttribute) -> StorePermissionFlags

        Set: Flags(self: StorePermissionAttribute) = value
        """
        ...
    @property
    def OpenStore(self):
        """
        Gets or sets a value indicating whether the code is permitted to open a store.

        Get: OpenStore(self: StorePermissionAttribute) -> bool

        Set: OpenStore(self: StorePermissionAttribute) = value
        """
        ...
    @property
    def RemoveFromStore(self):
        """
        Gets or sets a value indicating whether the code is permitted to remove a certificate from a store.

        Get: RemoveFromStore(self: StorePermissionAttribute) -> bool

        Set: RemoveFromStore(self: StorePermissionAttribute) = value
        """
        ...

class StorePermissionFlags(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies the permitted access to X.509 certificate stores.

    enum (flags) StorePermissionFlags, values: AddToStore (32), AllFlags (247), CreateStore (1), DeleteStore (2), EnumerateCertificates (128), EnumerateStores (4), NoFlags (0), OpenStore (16), RemoveFromStore (64)
    """

    AddToStore = None
    AllFlags = None
    CreateStore = None
    DeleteStore = None
    EnumerateCertificates = None
    EnumerateStores = None
    NoFlags = None
    OpenStore = None
    RemoveFromStore = None
    value__ = None

class StrongNameIdentityPermission(
    CodeAccessPermission, IBuiltInPermission
):  # skipped bases: <type 'ISecurityEncodable'>, <type 'IPermission'>, <type 'IStackWalk'>
    """
    Defines the identity permission for strong names. This class cannot be inherited.

    StrongNameIdentityPermission(state: PermissionState)

    StrongNameIdentityPermission(blob: StrongNamePublicKeyBlob, name: str, version: Version)
    """

    @staticmethod  # known case of __new__
    def __new__(cls, *__args):
        """
        __new__(cls: type, state: PermissionState)

        __new__(cls: type, blob: StrongNamePublicKeyBlob, name: str, version: Version)
        """
        ...
    @property
    def Name(self):
        """
        Gets or sets the simple name portion of the strong name identity.

        Get: Name(self: StrongNameIdentityPermission) -> str

        Set: Name(self: StrongNameIdentityPermission) = value
        """
        ...
    @property
    def PublicKey(self):
        """
        Gets or sets the public key blob that defines the strong name identity namespace.

        Get: PublicKey(self: StrongNameIdentityPermission) -> StrongNamePublicKeyBlob

        Set: PublicKey(self: StrongNameIdentityPermission) = value
        """
        ...
    @property
    def Version(self):
        """
        Gets or sets the version number of the identity.

        Get: Version(self: StrongNameIdentityPermission) -> Version

        Set: Version(self: StrongNameIdentityPermission) = value
        """
        ...

class StrongNameIdentityPermissionAttribute(CodeAccessSecurityAttribute):  # skipped bases: <type '_Attribute'>
    """
    Allows security actions for System.Security.Permissions.StrongNameIdentityPermission to be applied to code using declarative security. This class cannot be inherited.

    StrongNameIdentityPermissionAttribute(action: SecurityAction)
    """

    def CreatePermission(self):
        """
        CreatePermission(self: StrongNameIdentityPermissionAttribute) -> IPermission

            Creates and returns a new System.Security.Permissions.StrongNameIdentityPermission.

            Returns: A System.Security.Permissions.StrongNameIdentityPermission that corresponds to this attribute.
        """
        ...
    @property
    def Name(self):
        """
        Gets or sets the name of the strong name identity.

        Get: Name(self: StrongNameIdentityPermissionAttribute) -> str

        Set: Name(self: StrongNameIdentityPermissionAttribute) = value
        """
        ...
    @property
    def PublicKey(self):
        """
        Gets or sets the public key value of the strong name identity expressed as a hexadecimal string.

        Get: PublicKey(self: StrongNameIdentityPermissionAttribute) -> str

        Set: PublicKey(self: StrongNameIdentityPermissionAttribute) = value
        """
        ...
    @property
    def Version(self):
        """
        Gets or sets the version of the strong name identity.

        Get: Version(self: StrongNameIdentityPermissionAttribute) -> str

        Set: Version(self: StrongNameIdentityPermissionAttribute) = value
        """
        ...

class StrongNamePublicKeyBlob:  # skipped bases: <type 'object'>
    """
    Represents the public key information (called a blob) for a strong name. This class cannot be inherited.

    StrongNamePublicKeyBlob(publicKey: Array[Byte])
    """

    def Equals(self, obj):
        """
        Equals(self: StrongNamePublicKeyBlob, obj: object) -> bool

            Gets or sets a value indicating whether the current public key blob is equal to the specified public key blob.

            obj: An object containing a public key blob.

            Returns: ue if the public key blob of the current object is equal to the public key blob of the obj parameter; otherwise, lse.
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: StrongNamePublicKeyBlob) -> int

            Returns a hash code based on the public key.

            Returns: The hash code based on the public key.
        """
        ...
    def ToString(self):
        """
        ToString(self: StrongNamePublicKeyBlob) -> str

            Creates and returns a string representation of the public key blob.

            Returns: A hexadecimal version of the public key blob.
        """
        ...
    def __eq__(self, *args):  # cannot find CLR method
        """x.__eq__(y) <==> x==y"""
        ...
    def __ne__(self, *args): ...

class TypeDescriptorPermission(
    CodeAccessPermission, IUnrestrictedPermission
):  # skipped bases: <type 'ISecurityEncodable'>, <type 'IPermission'>, <type 'IStackWalk'>
    """
    Defines partial-trust access to the System.ComponentModel.TypeDescriptor class.

    TypeDescriptorPermission(state: PermissionState)

    TypeDescriptorPermission(flag: TypeDescriptorPermissionFlags)
    """

    @staticmethod  # known case of __new__
    def __new__(cls, *__args):
        """
        __new__(cls: type, state: PermissionState)

        __new__(cls: type, flag: TypeDescriptorPermissionFlags)
        """
        ...
    @property
    def Flags(self):
        """
        Gets or sets the System.Security.Permissions.TypeDescriptorPermissionFlags for the type descriptor.

        Get: Flags(self: TypeDescriptorPermission) -> TypeDescriptorPermissionFlags

        Set: Flags(self: TypeDescriptorPermission) = value
        """
        ...

class TypeDescriptorPermissionAttribute(CodeAccessSecurityAttribute):  # skipped bases: <type '_Attribute'>
    """
    Determines the permission flags that apply to a System.ComponentModel.TypeDescriptor.

    TypeDescriptorPermissionAttribute(action: SecurityAction)
    """

    def CreatePermission(self):
        """
        CreatePermission(self: TypeDescriptorPermissionAttribute) -> IPermission

            When overridden in a derived class, creates a permission object that can then be serialized into binary form and persistently stored along with the System.Security.Permissions.SecurityAction in an assembly's metadata.

            Returns: A serializable permission object.
        """
        ...
    @property
    def Flags(self):
        """
        Gets or sets the System.Security.Permissions.TypeDescriptorPermissionFlags for the System.ComponentModel.TypeDescriptor.

        Get: Flags(self: TypeDescriptorPermissionAttribute) -> TypeDescriptorPermissionFlags

        Set: Flags(self: TypeDescriptorPermissionAttribute) = value
        """
        ...
    @property
    def RestrictedRegistrationAccess(self):
        """
        Gets or sets a value that indicates whether the type descriptor can be accessed from partial trust.

        Get: RestrictedRegistrationAccess(self: TypeDescriptorPermissionAttribute) -> bool

        Set: RestrictedRegistrationAccess(self: TypeDescriptorPermissionAttribute) = value
        """
        ...

class TypeDescriptorPermissionFlags(
    Enum
):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Defines permission settings for type descriptors.

    enum (flags) TypeDescriptorPermissionFlags, values: NoFlags (0), RestrictedRegistrationAccess (1)
    """

    NoFlags = None
    RestrictedRegistrationAccess = None
    value__ = None

class UIPermission(
    CodeAccessPermission, IUnrestrictedPermission, IBuiltInPermission
):  # skipped bases: <type 'ISecurityEncodable'>, <type 'IPermission'>, <type 'IStackWalk'>
    """
    Controls the permissions related to user interfaces and the Clipboard. This class cannot be inherited.

    UIPermission(state: PermissionState)

    UIPermission(windowFlag: UIPermissionWindow, clipboardFlag: UIPermissionClipboard)

    UIPermission(windowFlag: UIPermissionWindow)

    UIPermission(clipboardFlag: UIPermissionClipboard)
    """

    @staticmethod  # known case of __new__
    def __new__(cls, *__args):
        """
        __new__(cls: type, state: PermissionState)

        __new__(cls: type, windowFlag: UIPermissionWindow, clipboardFlag: UIPermissionClipboard)

        __new__(cls: type, windowFlag: UIPermissionWindow)

        __new__(cls: type, clipboardFlag: UIPermissionClipboard)
        """
        ...
    @property
    def Clipboard(self):
        """
        Gets or sets the Clipboard access represented by the permission.

        Get: Clipboard(self: UIPermission) -> UIPermissionClipboard

        Set: Clipboard(self: UIPermission) = value
        """
        ...
    @property
    def Window(self):
        """
        Gets or sets the window access represented by the permission.

        Get: Window(self: UIPermission) -> UIPermissionWindow

        Set: Window(self: UIPermission) = value
        """
        ...

class UIPermissionAttribute(CodeAccessSecurityAttribute):  # skipped bases: <type '_Attribute'>
    """
    Allows security actions for System.Security.Permissions.UIPermission to be applied to code using declarative security. This class cannot be inherited.

    UIPermissionAttribute(action: SecurityAction)
    """

    def CreatePermission(self):
        """
        CreatePermission(self: UIPermissionAttribute) -> IPermission

            Creates and returns a new System.Security.Permissions.UIPermission.

            Returns: A System.Security.Permissions.UIPermission that corresponds to this attribute.
        """
        ...
    @property
    def Clipboard(self):
        """
        Gets or sets the type of access to the clipboard that is permitted.

        Get: Clipboard(self: UIPermissionAttribute) -> UIPermissionClipboard

        Set: Clipboard(self: UIPermissionAttribute) = value
        """
        ...
    @property
    def Window(self):
        """
        Gets or sets the type of access to the window resources that is permitted.

        Get: Window(self: UIPermissionAttribute) -> UIPermissionWindow

        Set: Window(self: UIPermissionAttribute) = value
        """
        ...

class UIPermissionClipboard(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies the type of clipboard access that is allowed to the calling code.

    enum UIPermissionClipboard, values: AllClipboard (2), NoClipboard (0), OwnClipboard (1)
    """

    AllClipboard = None
    NoClipboard = None
    OwnClipboard = None
    value__ = None

class UIPermissionWindow(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies the type of windows that code is allowed to use.

    enum UIPermissionWindow, values: AllWindows (3), NoWindows (0), SafeSubWindows (1), SafeTopLevelWindows (2)
    """

    AllWindows = None
    NoWindows = None
    SafeSubWindows = None
    SafeTopLevelWindows = None
    value__ = None

class UrlIdentityPermission(
    CodeAccessPermission, IBuiltInPermission
):  # skipped bases: <type 'ISecurityEncodable'>, <type 'IPermission'>, <type 'IStackWalk'>
    """
    Defines the identity permission for the URL from which the code originates. This class cannot be inherited.

    UrlIdentityPermission(state: PermissionState)

    UrlIdentityPermission(site: str)
    """

    @staticmethod  # known case of __new__
    def __new__(cls, *__args):
        """
        __new__(cls: type, state: PermissionState)

        __new__(cls: type, site: str)
        """
        ...
    @property
    def Url(self):
        """
        Gets or sets a URL representing the identity of Internet code.

        Get: Url(self: UrlIdentityPermission) -> str

        Set: Url(self: UrlIdentityPermission) = value
        """
        ...

class UrlIdentityPermissionAttribute(CodeAccessSecurityAttribute):  # skipped bases: <type '_Attribute'>
    """
    Allows security actions for System.Security.Permissions.UrlIdentityPermission to be applied to code using declarative security. This class cannot be inherited.

    UrlIdentityPermissionAttribute(action: SecurityAction)
    """

    def CreatePermission(self):
        """
        CreatePermission(self: UrlIdentityPermissionAttribute) -> IPermission

            Creates and returns a new System.Security.Permissions.UrlIdentityPermission.

            Returns: A System.Security.Permissions.UrlIdentityPermission that corresponds to this attribute.
        """
        ...
    @property
    def Url(self):
        """
        Gets or sets the full URL of the calling code.

        Get: Url(self: UrlIdentityPermissionAttribute) -> str

        Set: Url(self: UrlIdentityPermissionAttribute) = value
        """
        ...

class ZoneIdentityPermission(
    CodeAccessPermission, IBuiltInPermission
):  # skipped bases: <type 'ISecurityEncodable'>, <type 'IPermission'>, <type 'IStackWalk'>
    """
    Defines the identity permission for the zone from which the code originates. This class cannot be inherited.

    ZoneIdentityPermission(state: PermissionState)

    ZoneIdentityPermission(zone: SecurityZone)
    """

    @staticmethod  # known case of __new__
    def __new__(cls, *__args):
        """
        __new__(cls: type, state: PermissionState)

        __new__(cls: type, zone: SecurityZone)
        """
        ...
    @property
    def SecurityZone(self):
        """
        Gets or sets the zone represented by the current System.Security.Permissions.ZoneIdentityPermission.

        Get: SecurityZone(self: ZoneIdentityPermission) -> SecurityZone

        Set: SecurityZone(self: ZoneIdentityPermission) = value
        """
        ...

class ZoneIdentityPermissionAttribute(CodeAccessSecurityAttribute):  # skipped bases: <type '_Attribute'>
    """
    Allows security actions for System.Security.Permissions.ZoneIdentityPermission to be applied to code using declarative security. This class cannot be inherited.

    ZoneIdentityPermissionAttribute(action: SecurityAction)
    """

    def CreatePermission(self):
        """
        CreatePermission(self: ZoneIdentityPermissionAttribute) -> IPermission

            Creates and returns a new System.Security.Permissions.ZoneIdentityPermission.

            Returns: A System.Security.Permissions.ZoneIdentityPermission that corresponds to this attribute.
        """
        ...
    @property
    def Zone(self):
        """
        Gets or sets membership in the content zone specified by the property value.

        Get: Zone(self: ZoneIdentityPermissionAttribute) -> SecurityZone

        Set: Zone(self: ZoneIdentityPermissionAttribute) = value
        """
        ...
