# encoding: utf-8
# module System.Reflection calls itself Reflection
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AmbiguousMatchException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>
    """
    The exception that is thrown when binding to a member results in more than one member matching the binding criteria. This class cannot be inherited.

    AmbiguousMatchException()

    AmbiguousMatchException(message: str)

    AmbiguousMatchException(message: str, inner: Exception)
    """
    SerializeObjectState = None


class ICustomAttributeProvider:
    """ Provides custom attributes for reflection objects that support them. """
    def GetCustomAttributes(self, *__args):
        """
        GetCustomAttributes(self: ICustomAttributeProvider, attributeType: Type, inherit: bool) -> Array[object]

            Returns an array of custom attributes defined on this member, identified by type, or an empty array if there are no custom attributes of that type.

            attributeType: The type of the custom attributes.

            inherit: When ue, look up the hierarchy chain for the inherited custom attribute.

            Returns: An array of Objects representing custom attributes, or an empty array.

        GetCustomAttributes(self: ICustomAttributeProvider, inherit: bool) -> Array[object]

            Returns an array of all of the custom attributes defined on this member, excluding named attributes, or an empty array if there are no custom attributes.

            inherit: When ue, look up the hierarchy chain for the inherited custom attribute.

            Returns: An array of Objects representing custom attributes, or an empty array.
        """
        ...

    def IsDefined(self, attributeType, inherit):
        """
        IsDefined(self: ICustomAttributeProvider, attributeType: Type, inherit: bool) -> bool

            Indicates whether one or more instance of attributeType is defined on this member.

            attributeType: The type of the custom attributes.

            inherit: When ue, look up the hierarchy chain for the inherited custom attribute.

            Returns: ue if the attributeType is defined on this member; lse otherwise.
        """
        ...


class Assembly(object, _Assembly, IEvidenceFactory, ICustomAttributeProvider, ISerializable):
    """ Represents an assembly, which is a reusable, versionable, and self-describing building block of a common language runtime application. """
    @staticmethod
    def CreateQualifiedName(assemblyName, typeName):
        """
        CreateQualifiedName(assemblyName: str, typeName: str) -> str

            Creates the name of a type qualified by the display name of its assembly.

            assemblyName: The display name of an assembly.

            typeName: The full name of a type.

            Returns: The full name of the type qualified by the display name of the assembly.
        """
        ...

    @staticmethod
    def GetAssembly(type):
        """
        GetAssembly(type: Type) -> Assembly

            Gets the currently loaded assembly in which the specified type is defined.

            type: An object representing a type in the assembly that will be returned.

            Returns: The assembly in which the specified type is defined.
        """
        ...

    @staticmethod
    def GetCallingAssembly():
        """
        GetCallingAssembly() -> Assembly

            Returns the System.Reflection.Assembly of the method that invoked the currently executing method.

            Returns: The sembly object of the method that invoked the currently executing method.
        """
        ...

    def GetCustomAttributesData(self):
        """
        GetCustomAttributesData(self: Assembly) -> IList[CustomAttributeData]

            Returns information about the attributes that have been applied to the current System.Reflection.Assembly, expressed as System.Reflection.CustomAttributeData objects.

            Returns: A generic list of System.Reflection.CustomAttributeData objects representing data about the attributes that have been applied to the current assembly.
        """
        ...

    @staticmethod
    def GetEntryAssembly():
        """
        GetEntryAssembly() -> Assembly

            Gets the process executable in the default application domain. In other application domains, this is the first executable that was executed by

             System.AppDomain.ExecuteAssembly(System.String).

            Returns: The assembly that is the process executable in the default application domain, or the first executable that was executed by

             System.AppDomain.ExecuteAssembly(System.String). Can return ll when called from unmanaged code.
        """
        ...

    @staticmethod
    def GetExecutingAssembly():
        """
        GetExecutingAssembly() -> Assembly

            Gets the assembly that contains the code that is currently executing.

            Returns: The assembly that contains the code that is currently executing.
        """
        ...

    @staticmethod
    def Load(*__args):
        """
        Load(assemblyString: str) -> Assembly

            Loads an assembly given the long form of its name.

            assemblyString: The long form of the assembly name.

            Returns: The loaded assembly.

        Load(assemblyString: str, assemblySecurity: Evidence) -> Assembly

            Loads an assembly given its display name, loading the assembly into the domain of the caller using the supplied evidence.

            assemblyString: The display name of the assembly.

            assemblySecurity: Evidence for loading the assembly.

            Returns: The loaded assembly.

        Load(assemblyRef: AssemblyName) -> Assembly

            Loads an assembly given its System.Reflection.AssemblyName.

            assemblyRef: The object that describes the assembly to be loaded.

            Returns: The loaded assembly.

        Load(assemblyRef: AssemblyName, assemblySecurity: Evidence) -> Assembly

            Loads an assembly given its System.Reflection.AssemblyName. The assembly is loaded into the domain of the caller using the supplied evidence.

            assemblyRef: The object that describes the assembly to be loaded.

            assemblySecurity: Evidence for loading the assembly.

            Returns: The loaded assembly.

        Load(rawAssembly: Array[Byte]) -> Assembly

            Loads the assembly with a common object file format (COFF)-based image containing an emitted assembly. The assembly is loaded into the application domain of the caller.

            rawAssembly: A byte array that is a COFF-based image containing an emitted assembly.

            Returns: The loaded assembly.

        Load(rawAssembly: Array[Byte], rawSymbolStore: Array[Byte]) -> Assembly

            Loads the assembly with a common object file format (COFF)-based image containing an emitted assembly, optionally including symbols for the assembly. The assembly is

             loaded into the application domain of the caller.

            rawAssembly: A byte array that is a COFF-based image containing an emitted assembly.

            rawSymbolStore: A byte array that contains the raw bytes representing the symbols for the assembly.

            Returns: The loaded assembly.

        Load(rawAssembly: Array[Byte], rawSymbolStore: Array[Byte], securityContextSource: SecurityContextSource) -> Assembly

            Loads the assembly with a common object file format (COFF)-based image containing an emitted assembly, optionally including symbols and specifying the source for the

             security context. The assembly is loaded into the application domain of the caller.

            rawAssembly: A byte array that is a COFF-based image containing an emitted assembly.

            rawSymbolStore: A byte array that contains the raw bytes representing the symbols for the assembly.

            securityContextSource: The source of the security context.

            Returns: The loaded assembly.

        Load(rawAssembly: Array[Byte], rawSymbolStore: Array[Byte], securityEvidence: Evidence) -> Assembly

            Loads the assembly with a common object file format (COFF)-based image containing an emitted assembly, optionally including symbols and evidence for the assembly. The

             assembly is loaded into the application domain of the caller.

            rawAssembly: A byte array that is a COFF-based image containing an emitted assembly.

            rawSymbolStore: A byte array that contains the raw bytes representing the symbols for the assembly.

            securityEvidence: Evidence for loading the assembly.

            Returns: The loaded assembly.
        """
        ...

    @staticmethod
    def LoadFile(path, securityEvidence=None):
        """
        LoadFile(path: str) -> Assembly

            Loads the contents of an assembly file on the specified path.

            path: The fully qualified path of the file to load.

            Returns: The loaded assembly.

        LoadFile(path: str, securityEvidence: Evidence) -> Assembly

            Loads an assembly given its path, loading the assembly into the domain of the caller using the supplied evidence.

            path: The fully qualified path of the assembly file.

            securityEvidence: Evidence for loading the assembly.

            Returns: The loaded assembly.
        """
        ...

    @staticmethod
    def LoadFrom(assemblyFile, *__args):
        """
        LoadFrom(assemblyFile: str) -> Assembly

            Loads an assembly given its file name or path.

            assemblyFile: The name or path of the file that contains the manifest of the assembly.

            Returns: The loaded assembly.

        LoadFrom(assemblyFile: str, securityEvidence: Evidence) -> Assembly

            Loads an assembly given its file name or path and supplying security evidence.

            assemblyFile: The name or path of the file that contains the manifest of the assembly.

            securityEvidence: Evidence for loading the assembly.

            Returns: The loaded assembly.

        LoadFrom(assemblyFile: str, securityEvidence: Evidence, hashValue: Array[Byte], hashAlgorithm: AssemblyHashAlgorithm) -> Assembly

            Loads an assembly given its file name or path, security evidence, hash value, and hash algorithm.

            assemblyFile: The name or path of the file that contains the manifest of the assembly.

            securityEvidence: Evidence for loading the assembly.

            hashValue: The value of the computed hash code.

            hashAlgorithm: The hash algorithm used for hashing files and for generating the strong name.

            Returns: The loaded assembly.

        LoadFrom(assemblyFile: str, hashValue: Array[Byte], hashAlgorithm: AssemblyHashAlgorithm) -> Assembly

            Loads an assembly given its file name or path, hash value, and hash algorithm.

            assemblyFile: The name or path of the file that contains the manifest of the assembly.

            hashValue: The value of the computed hash code.

            hashAlgorithm: The hash algorithm used for hashing files and for generating the strong name.

            Returns: The loaded assembly.
        """
        ...

    @staticmethod
    def LoadWithPartialName(partialName, securityEvidence=None):
        """
        LoadWithPartialName(partialName: str) -> Assembly

            Loads an assembly from the application directory or from the global assembly cache using a partial name.

            partialName: The display name of the assembly.

            Returns: The loaded assembly. If partialName is not found, this method returns ll.

        LoadWithPartialName(partialName: str, securityEvidence: Evidence) -> Assembly

            Loads an assembly from the application directory or from the global assembly cache using a partial name. The assembly is loaded into the domain of the caller using the

             supplied evidence.

            partialName: The display name of the assembly.

            securityEvidence: Evidence for loading the assembly.

            Returns: The loaded assembly. If partialName is not found, this method returns ll.
        """
        ...

    @staticmethod
    def ReflectionOnlyLoad(*__args):
        """
        ReflectionOnlyLoad(assemblyString: str) -> Assembly

            Loads an assembly into the reflection-only context, given its display name.

            assemblyString: The display name of the assembly, as returned by the System.Reflection.AssemblyName.FullName property.

            Returns: The loaded assembly.

        ReflectionOnlyLoad(rawAssembly: Array[Byte]) -> Assembly

            Loads the assembly from a common object file format (COFF)-based image containing an emitted assembly. The assembly is loaded into the reflection-only context of the

             caller's application domain.

            rawAssembly: A byte array that is a COFF-based image containing an emitted assembly.

            Returns: The loaded assembly.
        """
        ...

    @staticmethod
    def ReflectionOnlyLoadFrom(assemblyFile):
        """
        ReflectionOnlyLoadFrom(assemblyFile: str) -> Assembly

            Loads an assembly into the reflection-only context, given its path.

            assemblyFile: The path of the file that contains the manifest of the assembly.

            Returns: The loaded assembly.
        """
        ...

    @staticmethod
    def UnsafeLoadFrom(assemblyFile):
        """
        UnsafeLoadFrom(assemblyFile: str) -> Assembly

            Loads an assembly into the load-from context, bypassing some security checks.

            assemblyFile: The name or path of the file that contains the manifest of the assembly.

            Returns: The loaded assembly.
        """
        ...

    def __dir__(self, *args): #cannot find CLR method
        """ __dir__(self: Assembly) -> list """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    @property
    def CodeBase(self):
        """
        Gets the location of the assembly as specified originally, for example, in an System.Reflection.AssemblyName object.

        Get: CodeBase(self: Assembly) -> str
        """
        ...

    @property
    def CustomAttributes(self):
        """
        Gets a collection that contains this assembly's custom attributes.

        Get: CustomAttributes(self: Assembly) -> IEnumerable[CustomAttributeData]
        """
        ...

    @property
    def DefinedTypes(self):
        """
        Gets a collection of the types defined in this assembly.

        Get: DefinedTypes(self: Assembly) -> IEnumerable[TypeInfo]
        """
        ...

    @property
    def EntryPoint(self):
        """
        Gets the entry point of this assembly.

        Get: EntryPoint(self: Assembly) -> MethodInfo
        """
        ...

    @property
    def EscapedCodeBase(self):
        """
        Gets the URI, including escape characters, that represents the codebase.

        Get: EscapedCodeBase(self: Assembly) -> str
        """
        ...

    @property
    def Evidence(self):
        """
        Gets the evidence for this assembly.

        Get: Evidence(self: Assembly) -> Evidence
        """
        ...

    @property
    def ExportedTypes(self):
        """
        Gets a collection of the public types defined in this assembly that are visible outside the assembly.

        Get: ExportedTypes(self: Assembly) -> IEnumerable[Type]
        """
        ...

    @property
    def FullName(self):
        """
        Gets the display name of the assembly.

        Get: FullName(self: Assembly) -> str
        """
        ...

    @property
    def GlobalAssemblyCache(self):
        """
        Gets a value indicating whether the assembly was loaded from the global assembly cache.

        Get: GlobalAssemblyCache(self: Assembly) -> bool
        """
        ...

    @property
    def HostContext(self):
        """
        Gets the host context with which the assembly was loaded.

        Get: HostContext(self: Assembly) -> Int64
        """
        ...

    @property
    def ImageRuntimeVersion(self):
        """
        Gets a string representing the version of the common language runtime (CLR) saved in the file containing the manifest.

        Get: ImageRuntimeVersion(self: Assembly) -> str
        """
        ...

    @property
    def IsDynamic(self):
        """
        Gets a value that indicates whether the current assembly was generated dynamically in the current process by using reflection emit.

        Get: IsDynamic(self: Assembly) -> bool
        """
        ...

    @property
    def IsFullyTrusted(self):
        """
        Gets a value that indicates whether the current assembly is loaded with full trust.

        Get: IsFullyTrusted(self: Assembly) -> bool
        """
        ...

    @property
    def Location(self):
        """
        Gets the full path or UNC location of the loaded file that contains the manifest.

        Get: Location(self: Assembly) -> str
        """
        ...

    @property
    def ManifestModule(self):
        """
        Gets the module that contains the manifest for the current assembly.

        Get: ManifestModule(self: Assembly) -> Module
        """
        ...

    @property
    def Modules(self):
        """
        Gets a collection that contains the modules in this assembly.

        Get: Modules(self: Assembly) -> IEnumerable[Module]
        """
        ...

    @property
    def PermissionSet(self):
        """
        Gets the grant set of the current assembly.

        Get: PermissionSet(self: Assembly) -> PermissionSet
        """
        ...

    @property
    def ReflectionOnly(self):
        """
        Gets a System.Boolean value indicating whether this assembly was loaded into the reflection-only context.

        Get: ReflectionOnly(self: Assembly) -> bool
        """
        ...

    @property
    def SecurityRuleSet(self):
        """
        Gets a value that indicates which set of security rules the common language runtime (CLR) enforces for this assembly.

        Get: SecurityRuleSet(self: Assembly) -> SecurityRuleSet
        """
        ...


    ModuleResolve = None


class AssemblyAlgorithmIdAttribute(Attribute): # skipped bases: <type '_Attribute'>
    """
    Specifies an algorithm to hash all files in an assembly. This class cannot be inherited.

    AssemblyAlgorithmIdAttribute(algorithmId: AssemblyHashAlgorithm)

    AssemblyAlgorithmIdAttribute(algorithmId: UInt32)
    """
    @staticmethod # known case of __new__
    def __new__(cls, algorithmId):
        """
        __new__(cls: type, algorithmId: AssemblyHashAlgorithm)

        __new__(cls: type, algorithmId: UInt32)
        """
        ...

    @property
    def AlgorithmId(self):
        """
        Gets the hash algorithm of an assembly manifest's contents.

        Get: AlgorithmId(self: AssemblyAlgorithmIdAttribute) -> UInt32
        """
        ...



class AssemblyCompanyAttribute(Attribute): # skipped bases: <type '_Attribute'>
    """
    Defines a company name custom attribute for an assembly manifest.

    AssemblyCompanyAttribute(company: str)
    """
    @staticmethod # known case of __new__
    def __new__(cls, company):
        """ __new__(cls: type, company: str) """
        ...

    @property
    def Company(self):
        """
        Gets company name information.

        Get: Company(self: AssemblyCompanyAttribute) -> str
        """
        ...



class AssemblyConfigurationAttribute(Attribute): # skipped bases: <type '_Attribute'>
    """
    Specifies the build configuration, such as retail or debug, for an assembly.

    AssemblyConfigurationAttribute(configuration: str)
    """
    @staticmethod # known case of __new__
    def __new__(cls, configuration):
        """ __new__(cls: type, configuration: str) """
        ...

    @property
    def Configuration(self):
        """
        Gets assembly configuration information.

        Get: Configuration(self: AssemblyConfigurationAttribute) -> str
        """
        ...



class AssemblyContentType(Enum): # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Provides information about the type of code contained in an assembly.

    enum AssemblyContentType, values: Default (0), WindowsRuntime (1)
    """
    Default = None
    value__ = None
    WindowsRuntime = None


class AssemblyCopyrightAttribute(Attribute): # skipped bases: <type '_Attribute'>
    """
    Defines a copyright custom attribute for an assembly manifest.

    AssemblyCopyrightAttribute(copyright: str)
    """
    @staticmethod # known case of __new__
    def __new__(cls, copyright):
        """ __new__(cls: type, copyright: str) """
        ...

    @property
    def Copyright(self):
        """
        Gets copyright information.

        Get: Copyright(self: AssemblyCopyrightAttribute) -> str
        """
        ...



class AssemblyCultureAttribute(Attribute): # skipped bases: <type '_Attribute'>
    """
    Specifies which culture the assembly supports.

    AssemblyCultureAttribute(culture: str)
    """
    @staticmethod # known case of __new__
    def __new__(cls, culture):
        """ __new__(cls: type, culture: str) """
        ...

    @property
    def Culture(self):
        """
        Gets the supported culture of the attributed assembly.

        Get: Culture(self: AssemblyCultureAttribute) -> str
        """
        ...



class AssemblyDefaultAliasAttribute(Attribute): # skipped bases: <type '_Attribute'>
    """
    Defines a friendly default alias for an assembly manifest.

    AssemblyDefaultAliasAttribute(defaultAlias: str)
    """
    @staticmethod # known case of __new__
    def __new__(cls, defaultAlias):
        """ __new__(cls: type, defaultAlias: str) """
        ...

    @property
    def DefaultAlias(self):
        """
        Gets default alias information.

        Get: DefaultAlias(self: AssemblyDefaultAliasAttribute) -> str
        """
        ...



class AssemblyDelaySignAttribute(Attribute): # skipped bases: <type '_Attribute'>
    """
    Specifies that the assembly is not fully signed when created.

    AssemblyDelaySignAttribute(delaySign: bool)
    """
    @staticmethod # known case of __new__
    def __new__(cls, delaySign):
        """ __new__(cls: type, delaySign: bool) """
        ...

    @property
    def DelaySign(self):
        """
        Gets a value indicating the state of the attribute.

        Get: DelaySign(self: AssemblyDelaySignAttribute) -> bool
        """
        ...



class AssemblyDescriptionAttribute(Attribute): # skipped bases: <type '_Attribute'>
    """
    Provides a text description for an assembly.

    AssemblyDescriptionAttribute(description: str)
    """
    @staticmethod # known case of __new__
    def __new__(cls, description):
        """ __new__(cls: type, description: str) """
        ...

    @property
    def Description(self):
        """
        Gets assembly description information.

        Get: Description(self: AssemblyDescriptionAttribute) -> str
        """
        ...



class AssemblyFileVersionAttribute(Attribute): # skipped bases: <type '_Attribute'>
    """
    Instructs a compiler to use a specific version number for the Win32 file version resource. The Win32 file version is not required to be the same as the assembly's version number.

    AssemblyFileVersionAttribute(version: str)
    """
    @staticmethod # known case of __new__
    def __new__(cls, version):
        """ __new__(cls: type, version: str) """
        ...

    @property
    def Version(self):
        """
        Gets the Win32 file version resource name.

        Get: Version(self: AssemblyFileVersionAttribute) -> str
        """
        ...



class AssemblyFlagsAttribute(Attribute): # skipped bases: <type '_Attribute'>
    """
    Specifies a bitwise combination of System.Reflection.AssemblyNameFlags flags for an assembly, describing just-in-time (JIT) compiler options, whether the assembly is retargetable, and whether it has a full or tokenized public key. This class cannot be inherited.

    AssemblyFlagsAttribute(flags: UInt32)

    AssemblyFlagsAttribute(assemblyFlags: int)

    AssemblyFlagsAttribute(assemblyFlags: AssemblyNameFlags)
    """
    @staticmethod # known case of __new__
    def __new__(cls, *__args):
        """
        __new__(cls: type, flags: UInt32)

        __new__(cls: type, assemblyFlags: int)

        __new__(cls: type, assemblyFlags: AssemblyNameFlags)
        """
        ...

    @property
    def AssemblyFlags(self):
        """
        Gets an integer value representing the combination of System.Reflection.AssemblyNameFlags flags specified when this attribute instance was created.

        Get: AssemblyFlags(self: AssemblyFlagsAttribute) -> int
        """
        ...

    @property
    def Flags(self):
        """
        Gets an unsigned integer value representing the combination of System.Reflection.AssemblyNameFlags flags specified when this attribute instance was created.

        Get: Flags(self: AssemblyFlagsAttribute) -> UInt32
        """
        ...



class AssemblyInformationalVersionAttribute(Attribute): # skipped bases: <type '_Attribute'>
    """
    Defines additional version information for an assembly manifest.

    AssemblyInformationalVersionAttribute(informationalVersion: str)
    """
    @staticmethod # known case of __new__
    def __new__(cls, informationalVersion):
        """ __new__(cls: type, informationalVersion: str) """
        ...

    @property
    def InformationalVersion(self):
        """
        Gets version information.

        Get: InformationalVersion(self: AssemblyInformationalVersionAttribute) -> str
        """
        ...



class AssemblyKeyFileAttribute(Attribute): # skipped bases: <type '_Attribute'>
    """
    Specifies the name of a file containing the key pair used to generate a strong name.

    AssemblyKeyFileAttribute(keyFile: str)
    """
    @staticmethod # known case of __new__
    def __new__(cls, keyFile):
        """ __new__(cls: type, keyFile: str) """
        ...

    @property
    def KeyFile(self):
        """
        Gets the name of the file containing the key pair used to generate a strong name for the attributed assembly.

        Get: KeyFile(self: AssemblyKeyFileAttribute) -> str
        """
        ...



class AssemblyKeyNameAttribute(Attribute): # skipped bases: <type '_Attribute'>
    """
    Specifies the name of a key container within the CSP containing the key pair used to generate a strong name.

    AssemblyKeyNameAttribute(keyName: str)
    """
    @staticmethod # known case of __new__
    def __new__(cls, keyName):
        """ __new__(cls: type, keyName: str) """
        ...

    @property
    def KeyName(self):
        """
        Gets the name of the container having the key pair that is used to generate a strong name for the attributed assembly.

        Get: KeyName(self: AssemblyKeyNameAttribute) -> str
        """
        ...



class AssemblyMetadataAttribute(Attribute): # skipped bases: <type '_Attribute'>
    """
    Defines a key/value metadata pair for the decorated assembly.

    AssemblyMetadataAttribute(key: str, value: str)
    """
    @staticmethod # known case of __new__
    def __new__(cls, key, value):
        """ __new__(cls: type, key: str, value: str) """
        ...

    @property
    def Key(self):
        """
        Gets the metadata key.

        Get: Key(self: AssemblyMetadataAttribute) -> str
        """
        ...

    @property
    def Value(self):
        """
        Gets the metadata value.

        Get: Value(self: AssemblyMetadataAttribute) -> str
        """
        ...



class AssemblyName(object, _AssemblyName, ICloneable, ISerializable, IDeserializationCallback):
    """
    Describes an assembly's unique identity in full.

    AssemblyName()

    AssemblyName(assemblyName: str)
    """
    @staticmethod
    def GetAssemblyName(assemblyFile):
        """
        GetAssemblyName(assemblyFile: str) -> AssemblyName

            Gets the System.Reflection.AssemblyName for a given file.

            assemblyFile: The path for the assembly whose System.Reflection.AssemblyName is to be returned.

            Returns: An object that represents the given assembly file.
        """
        ...

    def GetPublicKey(self):
        """
        GetPublicKey(self: AssemblyName) -> Array[Byte]

            Gets the public key of the assembly.

            Returns: A byte array that contains the public key of the assembly.
        """
        ...

    def GetPublicKeyToken(self):
        """
        GetPublicKeyToken(self: AssemblyName) -> Array[Byte]

            Gets the public key token, which is the last 8 bytes of the SHA-1 hash of the public key under which the application or assembly is signed.

            Returns: A byte array that contains the public key token.
        """
        ...

    @staticmethod
    def ReferenceMatchesDefinition(reference, definition):
        """
        ReferenceMatchesDefinition(reference: AssemblyName, definition: AssemblyName) -> bool

            Returns a value indicating whether two assembly names are the same. The comparison is based on the simple assembly names.

            reference: The reference assembly name.

            definition: The assembly name that is compared to the reference assembly.

            Returns: ue if the simple assembly names are the same; otherwise, lse.
        """
        ...

    def SetPublicKey(self, publicKey):
        """
        SetPublicKey(self: AssemblyName, publicKey: Array[Byte])

            Sets the public key identifying the assembly.

            publicKey: A byte array containing the public key of the assembly.
        """
        ...

    def SetPublicKeyToken(self, publicKeyToken):
        """
        SetPublicKeyToken(self: AssemblyName, publicKeyToken: Array[Byte])

            Sets the public key token, which is the last 8 bytes of the SHA-1 hash of the public key under which the application or assembly is signed.

            publicKeyToken: A byte array containing the public key token of the assembly.
        """
        ...

    def ToString(self):
        """
        ToString(self: AssemblyName) -> str

            Returns the full name of the assembly, also known as the display name.

            Returns: The full name of the assembly, or the class name if the full name cannot be determined.
        """
        ...

    @property
    def CodeBase(self):
        """
        Gets or sets the location of the assembly as a URL.

        Get: CodeBase(self: AssemblyName) -> str

        Set: CodeBase(self: AssemblyName) = value
        """
        ...

    @property
    def ContentType(self):
        """
        Gets or sets a value that indicates what type of content the assembly contains.

        Get: ContentType(self: AssemblyName) -> AssemblyContentType

        Set: ContentType(self: AssemblyName) = value
        """
        ...

    @property
    def CultureInfo(self):
        """
        Gets or sets the culture supported by the assembly.

        Get: CultureInfo(self: AssemblyName) -> CultureInfo

        Set: CultureInfo(self: AssemblyName) = value
        """
        ...

    @property
    def CultureName(self):
        """
        Gets or sets the name of the culture associated with the assembly.

        Get: CultureName(self: AssemblyName) -> str

        Set: CultureName(self: AssemblyName) = value
        """
        ...

    @property
    def EscapedCodeBase(self):
        """
        Gets the URI, including escape characters, that represents the codebase.

        Get: EscapedCodeBase(self: AssemblyName) -> str
        """
        ...

    @property
    def Flags(self):
        """
        Gets or sets the attributes of the assembly.

        Get: Flags(self: AssemblyName) -> AssemblyNameFlags

        Set: Flags(self: AssemblyName) = value
        """
        ...

    @property
    def FullName(self):
        """
        Gets the full name of the assembly, also known as the display name.

        Get: FullName(self: AssemblyName) -> str
        """
        ...

    @property
    def HashAlgorithm(self):
        """
        Gets or sets the hash algorithm used by the assembly manifest.

        Get: HashAlgorithm(self: AssemblyName) -> AssemblyHashAlgorithm

        Set: HashAlgorithm(self: AssemblyName) = value
        """
        ...

    @property
    def KeyPair(self):
        """
        Gets or sets the public and private cryptographic key pair that is used to create a strong name signature for the assembly.

        Get: KeyPair(self: AssemblyName) -> StrongNameKeyPair

        Set: KeyPair(self: AssemblyName) = value
        """
        ...

    @property
    def Name(self):
        """
        Gets or sets the simple name of the assembly. This is usually, but not necessarily, the file name of the manifest file of the assembly, minus its extension.

        Get: Name(self: AssemblyName) -> str

        Set: Name(self: AssemblyName) = value
        """
        ...

    @property
    def ProcessorArchitecture(self):
        """
        Gets or sets a value that identifies the processor and bits-per-word of the platform targeted by an executable.

        Get: ProcessorArchitecture(self: AssemblyName) -> ProcessorArchitecture

        Set: ProcessorArchitecture(self: AssemblyName) = value
        """
        ...

    @property
    def Version(self):
        """
        Gets or sets the major, minor, build, and revision numbers of the assembly.

        Get: Version(self: AssemblyName) -> Version

        Set: Version(self: AssemblyName) = value
        """
        ...

    @property
    def VersionCompatibility(self):
        """
        Gets or sets the information related to the assembly's compatibility with other assemblies.

        Get: VersionCompatibility(self: AssemblyName) -> AssemblyVersionCompatibility

        Set: VersionCompatibility(self: AssemblyName) = value
        """
        ...



class AssemblyNameFlags(Enum): # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Provides information about an System.Reflection.Assembly reference.

    enum (flags) AssemblyNameFlags, values: EnableJITcompileOptimizer (16384), EnableJITcompileTracking (32768), None (0), PublicKey (1), Retargetable (256)
    """
    EnableJITcompileOptimizer = None
    EnableJITcompileTracking = None

    PublicKey = None
    Retargetable = None
    value__ = None


class AssemblyNameProxy(MarshalByRefObject):
    """
    Provides a remotable version of the semblyName.

    AssemblyNameProxy()
    """
    def GetAssemblyName(self, assemblyFile):
        """
        GetAssemblyName(self: AssemblyNameProxy, assemblyFile: str) -> AssemblyName

            Gets the semblyName for a given file.

            assemblyFile: The assembly file for which to get the semblyName.

            Returns: An semblyName object representing the given file.
        """
        ...


class AssemblyProductAttribute(Attribute): # skipped bases: <type '_Attribute'>
    """
    Defines a product name custom attribute for an assembly manifest.

    AssemblyProductAttribute(product: str)
    """
    @staticmethod # known case of __new__
    def __new__(cls, product):
        """ __new__(cls: type, product: str) """
        ...

    @property
    def Product(self):
        """
        Gets product name information.

        Get: Product(self: AssemblyProductAttribute) -> str
        """
        ...



class AssemblySignatureKeyAttribute(Attribute): # skipped bases: <type '_Attribute'>
    """
    Provides migration from an older, simpler strong name key to a larger key with a stronger hashing algorithm.

    AssemblySignatureKeyAttribute(publicKey: str, countersignature: str)
    """
    @staticmethod # known case of __new__
    def __new__(cls, publicKey, countersignature):
        """ __new__(cls: type, publicKey: str, countersignature: str) """
        ...

    @property
    def Countersignature(self):
        """
        Gets the countersignature for the strong name for this assembly.

        Get: Countersignature(self: AssemblySignatureKeyAttribute) -> str
        """
        ...

    @property
    def PublicKey(self):
        """
        Gets the public key for the strong name used to sign the assembly.

        Get: PublicKey(self: AssemblySignatureKeyAttribute) -> str
        """
        ...



class AssemblyTitleAttribute(Attribute): # skipped bases: <type '_Attribute'>
    """
    Specifies a description for an assembly.

    AssemblyTitleAttribute(title: str)
    """
    @staticmethod # known case of __new__
    def __new__(cls, title):
        """ __new__(cls: type, title: str) """
        ...

    @property
    def Title(self):
        """
        Gets assembly title information.

        Get: Title(self: AssemblyTitleAttribute) -> str
        """
        ...



class AssemblyTrademarkAttribute(Attribute): # skipped bases: <type '_Attribute'>
    """
    Defines a trademark custom attribute for an assembly manifest.

    AssemblyTrademarkAttribute(trademark: str)
    """
    @staticmethod # known case of __new__
    def __new__(cls, trademark):
        """ __new__(cls: type, trademark: str) """
        ...

    @property
    def Trademark(self):
        """
        Gets trademark information.

        Get: Trademark(self: AssemblyTrademarkAttribute) -> str
        """
        ...



class AssemblyVersionAttribute(Attribute): # skipped bases: <type '_Attribute'>
    """
    Specifies the version of the assembly being attributed.

    AssemblyVersionAttribute(version: str)
    """
    @staticmethod # known case of __new__
    def __new__(cls, version):
        """ __new__(cls: type, version: str) """
        ...

    @property
    def Version(self):
        """
        Gets the version number of the attributed assembly.

        Get: Version(self: AssemblyVersionAttribute) -> str
        """
        ...



class Binder: # skipped bases: <type 'object'>
    """ Selects a member from a list of candidates, and performs type conversion from actual argument type to formal argument type. """
    def BindToField(self, bindingAttr, match, value, culture):
        """
        BindToField(self: Binder, bindingAttr: BindingFlags, match: Array[FieldInfo], value: object, culture: CultureInfo) -> FieldInfo

            Selects a field from the given set of fields, based on the specified criteria.

            bindingAttr: A bitwise combination of System.Reflection.BindingFlags values.

            match: The set of fields that are candidates for matching. For example, when a System.Reflection.Binder object is used by erload:System.Type.InvokeMember, this parameter

             specifies the set of fields that reflection has determined to be possible matches, typically because they have the correct member name. The default implementation

             provided by System.Type.DefaultBinder changes the order of this array.

            value: The field value used to locate a matching field.

            culture: An instance of System.Globalization.CultureInfo that is used to control the coercion of data types, in binder implementations that coerce types. If culture is ll, the

             System.Globalization.CultureInfo for the current thread is used.Note���For example, if a binder implementation allows coercion of string values to numeric types, this

             parameter is necessary to convert a ring that represents 1000 to a uble value, because 1000 is represented differently by different cultures. The default binder does

             not do such string coercions.

            Returns: The matching field.
        """
        ...

    def BindToMethod(self, bindingAttr, match, args, modifiers, culture, names, state):
        """
        BindToMethod(self: Binder, bindingAttr: BindingFlags, match: Array[MethodBase], args: Array[object], modifiers: Array[ParameterModifier], culture: CultureInfo, names: Array[str]) -> (MethodBase, Array[object], object)

            Selects a method to invoke from the given set of methods, based on the supplied arguments.

            bindingAttr: A bitwise combination of System.Reflection.BindingFlags values.

            match: The set of methods that are candidates for matching. For example, when a System.Reflection.Binder object is used by erload:System.Type.InvokeMember, this parameter

             specifies the set of methods that reflection has determined to be possible matches, typically because they have the correct member name. The default implementation

             provided by System.Type.DefaultBinder changes the order of this array.

            args: The arguments that are passed in. The binder can change the order of the arguments in this array; for example, the default binder changes the order of arguments if the

             names parameter is used to specify an order other than positional order. If a binder implementation coerces argument types, the types and values of the arguments can

             be changed as well.

            modifiers: An array of parameter modifiers that enable binding to work with parameter signatures in which the types have been modified. The default binder implementation does not

             use this parameter.

            culture: An instance of System.Globalization.CultureInfo that is used to control the coercion of data types, in binder implementations that coerce types. If culture is ll, the

             System.Globalization.CultureInfo for the current thread is used. Note���For example, if a binder implementation allows coercion of string values to numeric types, this

             parameter is necessary to convert a ring that represents 1000 to a uble value, because 1000 is represented differently by different cultures. The default binder does

             not do such string coercions.

            names: The parameter names, if parameter names are to be considered when matching, or ll if arguments are to be treated as purely positional. For example, parameter names

             must be used if arguments are not supplied in positional order.

            Returns: The matching method.
        """
        ...

    def ChangeType(self, value, type, culture):
        """
        ChangeType(self: Binder, value: object, type: Type, culture: CultureInfo) -> object

            Changes the type of the given ject to the given pe.

            value: The object to change into a new pe.

            type: The new pe that value will become.

            culture: An instance of System.Globalization.CultureInfo that is used to control the coercion of data types. If culture is ll, the System.Globalization.CultureInfo for the

             current thread is used.Note���For example, this parameter is necessary to convert a ring that represents 1000 to a uble value, because 1000 is represented differently

             by different cultures.

            Returns: An object that contains the given value as the new type.
        """
        ...

    def ReorderArgumentArray(self, args, state):
        """
        ReorderArgumentArray(self: Binder, args: Array[object], state: object) -> Array[object]

            Upon returning from

             System.Reflection.Binder.BindToMethod(System.Reflection.BindingFlags,System.Reflection.MethodBase[],System.Object[]@,System.Reflection.ParameterModifier[],System.Global

             ization.CultureInfo,System.String[],System.Object@), restores the args argument to what it was when it came from ndToMethod.

            args: The actual arguments that are passed in. Both the types and values of the arguments can be changed.

            state: A binder-provided object that keeps track of argument reordering.
        """
        ...

    def SelectMethod(self, bindingAttr, match, types, modifiers):
        """
        SelectMethod(self: Binder, bindingAttr: BindingFlags, match: Array[MethodBase], types: Array[Type], modifiers: Array[ParameterModifier]) -> MethodBase

            Selects a method from the given set of methods, based on the argument type.

            bindingAttr: A bitwise combination of System.Reflection.BindingFlags values.

            match: The set of methods that are candidates for matching. For example, when a System.Reflection.Binder object is used by erload:System.Type.InvokeMember, this parameter

             specifies the set of methods that reflection has determined to be possible matches, typically because they have the correct member name. The default implementation

             provided by System.Type.DefaultBinder changes the order of this array.

            types: The parameter types used to locate a matching method.

            modifiers: An array of parameter modifiers that enable binding to work with parameter signatures in which the types have been modified.

            Returns: The matching method, if found; otherwise, ll.
        """
        ...

    def SelectProperty(self, bindingAttr, match, returnType, indexes, modifiers):
        """
        SelectProperty(self: Binder, bindingAttr: BindingFlags, match: Array[PropertyInfo], returnType: Type, indexes: Array[Type], modifiers: Array[ParameterModifier]) -> PropertyInfo

            Selects a property from the given set of properties, based on the specified criteria.

            bindingAttr: A bitwise combination of System.Reflection.BindingFlags values.

            match: The set of properties that are candidates for matching. For example, when a System.Reflection.Binder object is used by erload:System.Type.InvokeMember, this parameter

             specifies the set of properties that reflection has determined to be possible matches, typically because they have the correct member name. The default implementation

             provided by System.Type.DefaultBinder changes the order of this array.

            returnType: The return value the matching property must have.

            indexes: The index types of the property being searched for. Used for index properties such as the indexer for a class.

            modifiers: An array of parameter modifiers that enable binding to work with parameter signatures in which the types have been modified.

            Returns: The matching property.
        """
        ...


class BindingFlags(Enum): # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies flags that control binding and the way in which the search for members and types is conducted by reflection.

    enum (flags) BindingFlags, values: CreateInstance (512), DeclaredOnly (2), Default (0), ExactBinding (65536), FlattenHierarchy (64), GetField (1024), GetProperty (4096), IgnoreCase (1), IgnoreReturn (16777216), Instance (4), InvokeMethod (256), NonPublic (32), OptionalParamBinding (262144), Public (16), PutDispProperty (16384), PutRefDispProperty (32768), SetField (2048), SetProperty (8192), Static (8), SuppressChangeType (131072)
    """
    CreateInstance = None
    DeclaredOnly = None
    Default = None
    ExactBinding = None
    FlattenHierarchy = None
    GetField = None
    GetProperty = None
    IgnoreCase = None
    IgnoreReturn = None
    Instance = None
    InvokeMethod = None
    NonPublic = None
    OptionalParamBinding = None
    Public = None
    PutDispProperty = None
    PutRefDispProperty = None
    SetField = None
    SetProperty = None
    Static = None
    SuppressChangeType = None
    value__ = None


class CallingConventions(Enum): # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Defines the valid calling conventions for a method.

    enum (flags) CallingConventions, values: Any (3), ExplicitThis (64), HasThis (32), Standard (1), VarArgs (2)
    """
    Any = None
    ExplicitThis = None
    HasThis = None
    Standard = None
    value__ = None
    VarArgs = None


class MemberInfo(object, ICustomAttributeProvider, _MemberInfo):
    """ Obtains information about the attributes of a member and provides access to member metadata. """
    def GetCustomAttributesData(self):
        """
        GetCustomAttributesData(self: MemberInfo) -> IList[CustomAttributeData]

            Returns a list of System.Reflection.CustomAttributeData objects representing data about the attributes that have been applied to the target member.

            Returns: A generic list of System.Reflection.CustomAttributeData objects representing data about the attributes that have been applied to the target member.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    @property
    def CustomAttributes(self):
        """
        Gets a collection that contains this member's custom attributes.

        Get: CustomAttributes(self: MemberInfo) -> IEnumerable[CustomAttributeData]
        """
        ...

    @property
    def DeclaringType(self):
        """
        Gets the class that declares this member.

        Get: DeclaringType(self: MemberInfo) -> Type
        """
        ...

    @property
    def MemberType(self):
        """
                Get: MemberType(self: MemberInfo) -> MemberTypes
        """
        ...

    @property
    def MetadataToken(self):
        """
        Gets a value that identifies a metadata element.

        Get: MetadataToken(self: MemberInfo) -> int
        """
        ...

    @property
    def Module(self):
        """
        Gets the module in which the type that declares the member represented by the current System.Reflection.MemberInfo is defined.

        Get: Module(self: MemberInfo) -> Module
        """
        ...

    @property
    def Name(self):
        """
        Gets the name of the current member.

        Get: Name(self: MemberInfo) -> str
        """
        ...

    @property
    def ReflectedType(self):
        """
        Gets the class object that was used to obtain this instance of mberInfo.

        Get: ReflectedType(self: MemberInfo) -> Type
        """
        ...



class MethodBase(MemberInfo, _MethodBase): # skipped bases: <type 'ICustomAttributeProvider'>, <type '_MemberInfo'>
    """ Provides information about methods and constructors. """
    @staticmethod
    def GetCurrentMethod():
        """
        GetCurrentMethod() -> MethodBase

            Returns a thodBase object representing the currently executing method.

            Returns: System.Reflection.MethodBase.GetCurrentMethod is a static method that is called from within an executing method and that returns information about that method.A

             thodBase object representing the currently executing method.
        """
        ...

    def GetGenericArguments(self):
        """
        GetGenericArguments(self: MethodBase) -> Array[Type]

            Returns an array of System.Type objects that represent the type arguments of a generic method or the type parameters of a generic method definition.

            Returns: An array of System.Type objects that represent the type arguments of a generic method or the type parameters of a generic method definition. Returns an empty array if

             the current method is not a generic method.
        """
        ...

    def GetMethodBody(self):
        """
        GetMethodBody(self: MethodBase) -> MethodBody

            When overridden in a derived class, gets a System.Reflection.MethodBody object that provides access to the MSIL stream, local variables, and exceptions for the current

             method.

            Returns: A System.Reflection.MethodBody object that provides access to the MSIL stream, local variables, and exceptions for the current method.
        """
        ...

    @staticmethod
    def GetMethodFromHandle(handle, declaringType=None):
        """
        GetMethodFromHandle(handle: RuntimeMethodHandle) -> MethodBase

            Gets method information by using the method's internal metadata representation (handle).

            handle: The method's handle.

            Returns: A thodBase containing information about the method.

        GetMethodFromHandle(handle: RuntimeMethodHandle, declaringType: RuntimeTypeHandle) -> MethodBase

            Gets a System.Reflection.MethodBase object for the constructor or method represented by the specified handle, for the specified generic type.

            handle: A handle to the internal metadata representation of a constructor or method.

            declaringType: A handle to the generic type that defines the constructor or method.

            Returns: A System.Reflection.MethodBase object representing the method or constructor specified by handle, in the generic type specified by declaringType.
        """
        ...

    @property
    def Attributes(self):
        """
        Gets the attributes associated with this method.

        Get: Attributes(self: MethodBase) -> MethodAttributes
        """
        ...

    @property
    def CallingConvention(self):
        """
        Gets a value indicating the calling conventions for this method.

        Get: CallingConvention(self: MethodBase) -> CallingConventions
        """
        ...

    @property
    def ContainsGenericParameters(self):
        """
        Gets a value indicating whether the generic method contains unassigned generic type parameters.

        Get: ContainsGenericParameters(self: MethodBase) -> bool
        """
        ...

    @property
    def IsAbstract(self):
        """
        Gets a value indicating whether the method is abstract.

        Get: IsAbstract(self: MethodBase) -> bool
        """
        ...

    @property
    def IsAssembly(self):
        """
        Gets a value indicating whether the potential visibility of this method or constructor is described by System.Reflection.MethodAttributes.Assembly; that is, the method or constructor is visible at most to other types in the same assembly, and is not visible to derived types outside the assembly.

        Get: IsAssembly(self: MethodBase) -> bool
        """
        ...

    @property
    def IsConstructor(self):
        """
        Gets a value indicating whether the method is a constructor.

        Get: IsConstructor(self: MethodBase) -> bool
        """
        ...

    @property
    def IsFamily(self):
        """
        Gets a value indicating whether the visibility of this method or constructor is described by System.Reflection.MethodAttributes.Family; that is, the method or constructor is visible only within its class and derived classes.

        Get: IsFamily(self: MethodBase) -> bool
        """
        ...

    @property
    def IsFamilyAndAssembly(self):
        """
        Gets a value indicating whether the visibility of this method or constructor is described by System.Reflection.MethodAttributes.FamANDAssem; that is, the method or constructor can be called by derived classes, but only if they are in the same assembly.

        Get: IsFamilyAndAssembly(self: MethodBase) -> bool
        """
        ...

    @property
    def IsFamilyOrAssembly(self):
        """
        Gets a value indicating whether the potential visibility of this method or constructor is described by System.Reflection.MethodAttributes.FamORAssem; that is, the method or constructor can be called by derived classes wherever they are, and by classes in the same assembly.

        Get: IsFamilyOrAssembly(self: MethodBase) -> bool
        """
        ...

    @property
    def IsFinal(self):
        """
        Gets a value indicating whether this method is nal.

        Get: IsFinal(self: MethodBase) -> bool
        """
        ...

    @property
    def IsGenericMethod(self):
        """
        Gets a value indicating whether the method is generic.

        Get: IsGenericMethod(self: MethodBase) -> bool
        """
        ...

    @property
    def IsGenericMethodDefinition(self):
        """
        Gets a value indicating whether the method is a generic method definition.

        Get: IsGenericMethodDefinition(self: MethodBase) -> bool
        """
        ...

    @property
    def IsHideBySig(self):
        """
        Gets a value indicating whether only a member of the same kind with exactly the same signature is hidden in the derived class.

        Get: IsHideBySig(self: MethodBase) -> bool
        """
        ...

    @property
    def IsPrivate(self):
        """
        Gets a value indicating whether this member is private.

        Get: IsPrivate(self: MethodBase) -> bool
        """
        ...

    @property
    def IsPublic(self):
        """
        Gets a value indicating whether this is a public method.

        Get: IsPublic(self: MethodBase) -> bool
        """
        ...

    @property
    def IsSecurityCritical(self):
        """
        Gets a value that indicates whether the current method or constructor is security-critical or security-safe-critical at the current trust level, and therefore can perform critical operations.

        Get: IsSecurityCritical(self: MethodBase) -> bool
        """
        ...

    @property
    def IsSecuritySafeCritical(self):
        """
        Gets a value that indicates whether the current method or constructor is security-safe-critical at the current trust level; that is, whether it can perform critical operations and can be accessed by transparent code.

        Get: IsSecuritySafeCritical(self: MethodBase) -> bool
        """
        ...

    @property
    def IsSecurityTransparent(self):
        """
        Gets a value that indicates whether the current method or constructor is transparent at the current trust level, and therefore cannot perform critical operations.

        Get: IsSecurityTransparent(self: MethodBase) -> bool
        """
        ...

    @property
    def IsSpecialName(self):
        """
        Gets a value indicating whether this method has a special name.

        Get: IsSpecialName(self: MethodBase) -> bool
        """
        ...

    @property
    def IsStatic(self):
        """
        Gets a value indicating whether the method is atic.

        Get: IsStatic(self: MethodBase) -> bool
        """
        ...

    @property
    def IsVirtual(self):
        """
        Gets a value indicating whether the method is rtual.

        Get: IsVirtual(self: MethodBase) -> bool
        """
        ...

    @property
    def MethodHandle(self):
        """
        Gets a handle to the internal metadata representation of a method.

        Get: MethodHandle(self: MethodBase) -> RuntimeMethodHandle
        """
        ...

    @property
    def MethodImplementationFlags(self):
        """
        Gets the System.Reflection.MethodImplAttributes flags that specify the attributes of a method implementation.

        Get: MethodImplementationFlags(self: MethodBase) -> MethodImplAttributes
        """
        ...



class ConstructorInfo(MethodBase, _ConstructorInfo): # skipped bases: <type '_MethodBase'>, <type 'ICustomAttributeProvider'>, <type '_MemberInfo'>
    """ Discovers the attributes of a class constructor and provides access to constructor metadata. """
    @property
    def MemberType(self):
        """
        Gets a System.Reflection.MemberTypes value indicating that this member is a constructor.

        Get: MemberType(self: ConstructorInfo) -> MemberTypes
        """
        ...


    ConstructorName = '.ctor'
    TypeConstructorName = '.cctor'


class CustomAttributeData: # skipped bases: <type 'object'>
    """ Provides access to custom attribute data for assemblies, modules, types, members and parameters that are loaded into the reflection-only context. """
    def Equals(self, obj):
        """
        Equals(self: CustomAttributeData, obj: object) -> bool

            Returns a value that indicates whether this instance is equal to a specified object.

            obj: An object to compare with this instance, or ll.

            Returns: ue if obj is equal to the current instance; otherwise, lse.
        """
        ...

    @staticmethod
    def GetCustomAttributes(target):
        """
        GetCustomAttributes(target: MemberInfo) -> IList[CustomAttributeData]

            Returns a list of System.Reflection.CustomAttributeData objects representing data about the attributes that have been applied to the target member.

            target: The member whose attribute data is to be retrieved.

            Returns: A list of objects that represent data about the attributes that have been applied to the target member.

        GetCustomAttributes(target: Module) -> IList[CustomAttributeData]

            Returns a list of System.Reflection.CustomAttributeData objects representing data about the attributes that have been applied to the target module.

            target: The module whose custom attribute data is to be retrieved.

            Returns: A list of objects that represent data about the attributes that have been applied to the target module.

        GetCustomAttributes(target: Assembly) -> IList[CustomAttributeData]

            Returns a list of System.Reflection.CustomAttributeData objects representing data about the attributes that have been applied to the target assembly.

            target: The assembly whose custom attribute data is to be retrieved.

            Returns: A list of objects that represent data about the attributes that have been applied to the target assembly.

        GetCustomAttributes(target: ParameterInfo) -> IList[CustomAttributeData]

            Returns a list of System.Reflection.CustomAttributeData objects representing data about the attributes that have been applied to the target parameter.

            target: The parameter whose attribute data is to be retrieved.

            Returns: A list of objects that represent data about the attributes that have been applied to the target parameter.
        """
        ...

    def GetHashCode(self):
        """
        GetHashCode(self: CustomAttributeData) -> int

            Serves as a hash function for a particular type.

            Returns: A hash code for the current System.Object.
        """
        ...

    def ToString(self):
        """
        ToString(self: CustomAttributeData) -> str

            Returns a string representation of the custom attribute.

            Returns: A string value that represents the custom attribute.
        """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    @property
    def AttributeType(self):
        """
        Gets the type of the attribute.

        Get: AttributeType(self: CustomAttributeData) -> Type
        """
        ...

    @property
    def Constructor(self):
        """
        Gets a System.Reflection.ConstructorInfo object that represents the constructor that would have initialized the custom attribute.

        Get: Constructor(self: CustomAttributeData) -> ConstructorInfo
        """
        ...

    @property
    def ConstructorArguments(self):
        """
        Gets the list of positional arguments specified for the attribute instance represented by the System.Reflection.CustomAttributeData object.

        Get: ConstructorArguments(self: CustomAttributeData) -> IList[CustomAttributeTypedArgument]
        """
        ...

    @property
    def NamedArguments(self):
        """
        Gets the list of named arguments specified for the attribute instance represented by the System.Reflection.CustomAttributeData object.

        Get: NamedArguments(self: CustomAttributeData) -> IList[CustomAttributeNamedArgument]
        """
        ...



class CustomAttributeExtensions: # skipped bases: <type 'object'>
    """ Contains static methods for retrieving custom attributes. """
    @staticmethod
    def GetCustomAttribute(element, *__args):
        pass

    @staticmethod
    def GetCustomAttributes(element, *__args):
        """
        GetCustomAttributes(element: Assembly) -> IEnumerable[Attribute]

            Retrieves a collection of custom attributes that are applied to a specified assembly.

            element: The assembly to inspect.

            Returns: A collection of the custom attributes that are applied to element, or an empty collection if no such attributes exist.

        GetCustomAttributes[T](element: ParameterInfo) -> IEnumerable[T]

            Retrieves a collection of custom attributes that are applied to a specified parameter.

            element: The parameter to inspect.

            Returns: A collection of the custom attributes that are applied to element, or an empty collection if no such attributes exist.

        GetCustomAttributes[T](element: MemberInfo) -> IEnumerable[T]

            Retrieves a collection of custom attributes that are applied to a specified member.

            element: The member to inspect.

            Returns: A collection of the custom attributes that are applied to element, or an empty collection if no such attributes exist.

        GetCustomAttributes[T](element: Module) -> IEnumerable[T]

            Retrieves a collection of custom attributes that are applied to a specified module.

            element: The module to inspect.

            Returns: A collection of the custom attributes that are applied to element, or an empty collection if no such attributes exist.

        GetCustomAttributes[T](element: Assembly) -> IEnumerable[T]

            Retrieves a collection of custom attributes that are applied to a specified assembly.

            element: The assembly to inspect.

            Returns: A collection of the custom attributes that are applied to element, or an empty collection if no such attributes exist.

        GetCustomAttributes(element: ParameterInfo, attributeType: Type, inherit: bool) -> IEnumerable[Attribute]

            Retrieves a collection of custom attributes of a specified type that are applied to a specified parameter, and optionally inspects the ancestors of that parameter.

            element: The parameter to inspect.

            attributeType: The type of attribute to search for.

            inherit: ue to inspect the ancestors of element; otherwise, lse.

            Returns: A collection of the custom attributes that are applied to element and that match attributeType, or an empty collection if no such attributes exist.

        GetCustomAttributes(element: MemberInfo, attributeType: Type, inherit: bool) -> IEnumerable[Attribute]

            Retrieves a collection of custom attributes of a specified type that are applied to a specified member, and optionally inspects the ancestors of that member.

            element: The member to inspect.

            attributeType: The type of attribute to search for.

            inherit: ue to inspect the ancestors of element; otherwise, lse.

            Returns: A collection of the custom attributes that are applied to element and that match attributeType, or an empty collection if no such attributes exist.

        GetCustomAttributes(element: ParameterInfo, attributeType: Type) -> IEnumerable[Attribute]

            Retrieves a collection of custom attributes of a specified type that are applied to a specified parameter.

            element: The parameter to inspect.

            attributeType: The type of attribute to search for.

            Returns: A collection of the custom attributes that are applied to element and that match attributeType, or an empty collection if no such attributes exist.

        GetCustomAttributes(element: MemberInfo, attributeType: Type) -> IEnumerable[Attribute]

            Retrieves a collection of custom attributes of a specified type that are applied to a specified member.

            element: The member to inspect.

            attributeType: The type of attribute to search for.

            Returns: A collection of the custom attributes that are applied to element and that match attributeType, or an empty collection if no such attributes exist.

        GetCustomAttributes(element: Module, attributeType: Type) -> IEnumerable[Attribute]

            Retrieves a collection of custom attributes of a specified type that are applied to a specified module.

            element: The module to inspect.

            attributeType: The type of attribute to search for.

            Returns: A collection of the custom attributes that are applied to element and that match attributeType, or an empty collection if no such attributes exist.

        GetCustomAttributes(element: Assembly, attributeType: Type) -> IEnumerable[Attribute]

            Retrieves a collection of custom attributes of a specified type that are applied to a specified assembly.

            element: The assembly to inspect.

            attributeType: The type of attribute to search for.

            Returns: A collection of the custom attributes that are applied to element and that match attributeType, or an empty collection if no such attributes exist.

        GetCustomAttributes(element: ParameterInfo, inherit: bool) -> IEnumerable[Attribute]

            Retrieves a collection of custom attributes that are applied to a specified parameter, and optionally inspects the ancestors of that parameter.

            element: The parameter to inspect.

            inherit: ue to inspect the ancestors of element; otherwise, lse.

            Returns: A collection of the custom attributes that are applied to element, or an empty collection if no such attributes exist.

        GetCustomAttributes(element: MemberInfo, inherit: bool) -> IEnumerable[Attribute]

            Retrieves a collection of custom attributes that are applied to a specified member, and optionally inspects the ancestors of that member.

            element: The member to inspect.

            inherit: ue to inspect the ancestors of element; otherwise, lse.

            Returns: A collection of the custom attributes that are applied to element that match the specified criteria, or an empty collection if no such attributes exist.

        GetCustomAttributes(element: ParameterInfo) -> IEnumerable[Attribute]

            Retrieves a collection of custom attributes that are applied to a specified parameter.

            element: The parameter to inspect.

            Returns: A collection of the custom attributes that are applied to element, or an empty collection if no such attributes exist.

        GetCustomAttributes(element: MemberInfo) -> IEnumerable[Attribute]

            Retrieves a collection of custom attributes that are applied to a specified member.

            element: The member to inspect.

            Returns: A collection of the custom attributes that are applied to element, or an empty collection if no such attributes exist.

        GetCustomAttributes(element: Module) -> IEnumerable[Attribute]

            Retrieves a collection of custom attributes that are applied to a specified module.

            element: The module to inspect.

            Returns: A collection of the custom attributes that are applied to element, or an empty collection if no such attributes exist.

        GetCustomAttributes[T](element: MemberInfo, inherit: bool) -> IEnumerable[T]

            Retrieves a collection of custom attributes that are applied to a specified member, and optionally inspects the ancestors of that member.

            element: The member to inspect.

            inherit: ue to inspect the ancestors of element; otherwise, lse.

            Returns: A collection of the custom attributes that are applied to element that match the specified criteria, or an empty collection if no such attributes exist.

        GetCustomAttributes[T](element: ParameterInfo, inherit: bool) -> IEnumerable[T]

            Retrieves a collection of custom attributes that are applied to a specified parameter, and optionally inspects the ancestors of that parameter.

            element: The parameter to inspect.

            inherit: ue to inspect the ancestors of element; otherwise, lse.

            Returns: A collection of the custom attributes that are applied to element, or an empty collection if no such attributes exist.
        """
        ...

    @staticmethod
    def IsDefined(element, attributeType, inherit=None):
        """
        IsDefined(element: Assembly, attributeType: Type) -> bool

            Indicates whether custom attributes of a specified type are applied to a specified assembly.

            element: The assembly to inspect.

            attributeType: The type of the attribute to search for.

            Returns: ue if an attribute of the specified type is applied to element; otherwise, lse.

        IsDefined(element: Module, attributeType: Type) -> bool

            Indicates whether custom attributes of a specified type are applied to a specified module.

            element: The module to inspect.

            attributeType: The type of attribute to search for.

            Returns: ue if an attribute of the specified type is applied to element; otherwise, lse.

        IsDefined(element: MemberInfo, attributeType: Type) -> bool

            Indicates whether custom attributes of a specified type are applied to a specified member.

            element: The member to inspect.

            attributeType: The type of attribute to search for.

            Returns: ue if an attribute of the specified type is applied to element; otherwise, lse.

        IsDefined(element: ParameterInfo, attributeType: Type) -> bool

            Indicates whether custom attributes of a specified type are applied to a specified parameter.

            element: The parameter to inspect.

            attributeType: The type of attribute to search for.

            Returns: ue if an attribute of the specified type is applied to element; otherwise, lse.

        IsDefined(element: MemberInfo, attributeType: Type, inherit: bool) -> bool

            Indicates whether custom attributes of a specified type are applied to a specified member, and, optionally, applied to its ancestors.

            element: The member to inspect.

            attributeType: The type of the attribute to search for.

            inherit: ue to inspect the ancestors of element; otherwise, lse.

            Returns: ue if an attribute of the specified type is applied to element; otherwise, lse.

        IsDefined(element: ParameterInfo, attributeType: Type, inherit: bool) -> bool

            Indicates whether custom attributes of a specified type are applied to a specified parameter, and, optionally, applied to its ancestors.

            element: The parameter to inspect.

            attributeType: The type of attribute to search for.

            inherit: ue to inspect the ancestors of element; otherwise, lse.

            Returns: ue if an attribute of the specified type is applied to element; otherwise, lse.
        """
        ...

    __all__ = [
        'GetCustomAttribute',
        'GetCustomAttributes',
        'IsDefined',
    ]


class CustomAttributeFormatException(FormatException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>
    """
    The exception that is thrown when the binary format of a custom attribute is invalid.

    CustomAttributeFormatException()

    CustomAttributeFormatException(message: str)

    CustomAttributeFormatException(message: str, inner: Exception)
    """
    SerializeObjectState = None


class CustomAttributeNamedArgument: # skipped bases: <type 'object'>
    """
    Represents a named argument of a custom attribute in the reflection-only context.

    CustomAttributeNamedArgument(memberInfo: MemberInfo, value: object)

    CustomAttributeNamedArgument(memberInfo: MemberInfo, typedArgument: CustomAttributeTypedArgument)
    """
    def Equals(self, obj):
        """
        Equals(self: CustomAttributeNamedArgument, obj: object) -> bool

            Returns a value that indicates whether this instance is equal to a specified object.

            obj: An object to compare with this instance, or ll.

            Returns: ue if obj equals the type and value of this instance; otherwise, lse.
        """
        ...

    def GetHashCode(self):
        """
        GetHashCode(self: CustomAttributeNamedArgument) -> int

            Returns the hash code for this instance.

            Returns: A 32-bit signed integer hash code.
        """
        ...

    def ToString(self):
        """
        ToString(self: CustomAttributeNamedArgument) -> str

            Returns a string that consists of the argument name, the equal sign, and a string representation of the argument value.

            Returns: A string that consists of the argument name, the equal sign, and a string representation of the argument value.
        """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    @property
    def IsField(self):
        """
        Gets a value that indicates whether the named argument is a field.

        Get: IsField(self: CustomAttributeNamedArgument) -> bool
        """
        ...

    @property
    def MemberInfo(self):
        """
        Gets the attribute member that would be used to set the named argument.

        Get: MemberInfo(self: CustomAttributeNamedArgument) -> MemberInfo
        """
        ...

    @property
    def MemberName(self):
        """
        Gets the name of the attribute member that would be used to set the named argument.

        Get: MemberName(self: CustomAttributeNamedArgument) -> str
        """
        ...

    @property
    def TypedValue(self):
        """
        Gets a System.Reflection.CustomAttributeTypedArgument structure that can be used to obtain the type and value of the current named argument.

        Get: TypedValue(self: CustomAttributeNamedArgument) -> CustomAttributeTypedArgument
        """
        ...



class CustomAttributeTypedArgument: # skipped bases: <type 'object'>
    """
    Represents an argument of a custom attribute in the reflection-only context, or an element of an array argument.

    CustomAttributeTypedArgument(argumentType: Type, value: object)

    CustomAttributeTypedArgument(value: object)
    """
    def Equals(self, obj):
        """
        Equals(self: CustomAttributeTypedArgument, obj: object) -> bool

            Indicates whether this instance and a specified object are equal.

            obj: Another object to compare to.

            Returns: ue if obj and this instance are the same type and represent the same value; otherwise, lse.
        """
        ...

    def GetHashCode(self):
        """
        GetHashCode(self: CustomAttributeTypedArgument) -> int

            Returns the hash code for this instance.

            Returns: A 32-bit signed integer that is the hash code for this instance.
        """
        ...

    def ToString(self):
        """
        ToString(self: CustomAttributeTypedArgument) -> str

            Returns a string consisting of the argument name, the equal sign, and a string representation of the argument value.

            Returns: A string consisting of the argument name, the equal sign, and a string representation of the argument value.
        """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    @property
    def ArgumentType(self):
        """
        Gets the type of the argument or of the array argument element.

        Get: ArgumentType(self: CustomAttributeTypedArgument) -> Type
        """
        ...

    @property
    def Value(self):
        """
        Gets the value of the argument for a simple argument or for an element of an array argument; gets a collection of values for an array argument.

        Get: Value(self: CustomAttributeTypedArgument) -> object
        """
        ...



class DefaultMemberAttribute(Attribute): # skipped bases: <type '_Attribute'>
    """
    Defines the member of a type that is the default member used by System.Type.InvokeMember(System.String,System.Reflection.BindingFlags,System.Reflection.Binder,System.Object,System.Object[],System.Reflection.ParameterModifier[],System.Globalization.CultureInfo,System.String[]).

    DefaultMemberAttribute(memberName: str)
    """
    @staticmethod # known case of __new__
    def __new__(cls, memberName):
        """ __new__(cls: type, memberName: str) """
        ...

    @property
    def MemberName(self):
        """
        Gets the name from the attribute.

        Get: MemberName(self: DefaultMemberAttribute) -> str
        """
        ...



class EventAttributes(Enum): # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies the attributes of an event.

    enum (flags) EventAttributes, values: None (0), ReservedMask (1024), RTSpecialName (1024), SpecialName (512)
    """

    ReservedMask = None
    RTSpecialName = None
    SpecialName = None
    value__ = None


class EventInfo(MemberInfo, _EventInfo): # skipped bases: <type 'ICustomAttributeProvider'>, <type '_MemberInfo'>
    """ Discovers the attributes of an event and provides access to event metadata. """
    def GetOtherMethods(self, nonPublic=None):
        """
        GetOtherMethods(self: EventInfo, nonPublic: bool) -> Array[MethodInfo]

            Returns the methods that have been associated with the event in metadata using the ther directive, specifying whether to include non-public methods.

            nonPublic: ue to include non-public methods; otherwise, lse.

            Returns: An array of System.Reflection.EventInfo objects representing methods that have been associated with an event in metadata by using the ther directive. If there are no

             methods matching the specification, an empty array is returned.

        GetOtherMethods(self: EventInfo) -> Array[MethodInfo]

            Returns the public methods that have been associated with an event in metadata using the ther directive.

            Returns: An array of System.Reflection.EventInfo objects representing the public methods that have been associated with the event in metadata by using the ther directive. If

             there are no such public methods, an empty array is returned.
        """
        ...

    @property
    def AddMethod(self):
        """
        Gets the System.Reflection.MethodInfo object for the System.Reflection.EventInfo.AddEventHandler(System.Object,System.Delegate) method of the event, including non-public methods.

        Get: AddMethod(self: EventInfo) -> MethodInfo
        """
        ...

    @property
    def Attributes(self):
        """
        Gets the attributes for this event.

        Get: Attributes(self: EventInfo) -> EventAttributes
        """
        ...

    @property
    def EventHandlerType(self):
        """
        Gets the pe object of the underlying event-handler delegate associated with this event.

        Get: EventHandlerType(self: EventInfo) -> Type
        """
        ...

    @property
    def IsMulticast(self):
        """
        Gets a value indicating whether the event is multicast.

        Get: IsMulticast(self: EventInfo) -> bool
        """
        ...

    @property
    def IsSpecialName(self):
        """
        Gets a value indicating whether the entInfo has a name with a special meaning.

        Get: IsSpecialName(self: EventInfo) -> bool
        """
        ...

    @property
    def MemberType(self):
        """
        Gets a System.Reflection.MemberTypes value indicating that this member is an event.

        Get: MemberType(self: EventInfo) -> MemberTypes
        """
        ...

    @property
    def RaiseMethod(self):
        """
        Gets the method that is called when the event is raised, including non-public methods.

        Get: RaiseMethod(self: EventInfo) -> MethodInfo
        """
        ...

    @property
    def RemoveMethod(self):
        """
        Gets the thodInfo object for removing a method of the event, including non-public methods.

        Get: RemoveMethod(self: EventInfo) -> MethodInfo
        """
        ...



class ExceptionHandlingClause: # skipped bases: <type 'object'>
    """ Represents a clause in a structured exception-handling block. """
    def ToString(self):
        """
        ToString(self: ExceptionHandlingClause) -> str

            A string representation of the exception-handling clause.

            Returns: A string that lists appropriate property values for the filter clause type.
        """
        ...

    @property
    def CatchType(self):
        """
        Gets the type of exception handled by this clause.

        Get: CatchType(self: ExceptionHandlingClause) -> Type
        """
        ...

    @property
    def FilterOffset(self):
        """
        Gets the offset within the method body, in bytes, of the user-supplied filter code.

        Get: FilterOffset(self: ExceptionHandlingClause) -> int
        """
        ...

    @property
    def Flags(self):
        """
        Gets a value indicating whether this exception-handling clause is a finally clause, a type-filtered clause, or a user-filtered clause.

        Get: Flags(self: ExceptionHandlingClause) -> ExceptionHandlingClauseOptions
        """
        ...

    @property
    def HandlerLength(self):
        """
        Gets the length, in bytes, of the body of this exception-handling clause.

        Get: HandlerLength(self: ExceptionHandlingClause) -> int
        """
        ...

    @property
    def HandlerOffset(self):
        """
        Gets the offset within the method body, in bytes, of this exception-handling clause.

        Get: HandlerOffset(self: ExceptionHandlingClause) -> int
        """
        ...

    @property
    def TryLength(self):
        """
        The total length, in bytes, of the try block that includes this exception-handling clause.

        Get: TryLength(self: ExceptionHandlingClause) -> int
        """
        ...

    @property
    def TryOffset(self):
        """
        The offset within the method, in bytes, of the try block that includes this exception-handling clause.

        Get: TryOffset(self: ExceptionHandlingClause) -> int
        """
        ...



class ExceptionHandlingClauseOptions(Enum): # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Identifies kinds of exception-handling clauses.

    enum (flags) ExceptionHandlingClauseOptions, values: Clause (0), Fault (4), Filter (1), Finally (2)
    """
    Clause = None
    Fault = None
    Filter = None
    Finally = None
    value__ = None


class FieldAttributes(Enum): # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies flags that describe the attributes of a field.

    enum (flags) FieldAttributes, values: Assembly (3), FamANDAssem (2), Family (4), FamORAssem (5), FieldAccessMask (7), HasDefault (32768), HasFieldMarshal (4096), HasFieldRVA (256), InitOnly (32), Literal (64), NotSerialized (128), PinvokeImpl (8192), Private (1), PrivateScope (0), Public (6), ReservedMask (38144), RTSpecialName (1024), SpecialName (512), Static (16)
    """
    Assembly = None
    FamANDAssem = None
    Family = None
    FamORAssem = None
    FieldAccessMask = None
    HasDefault = None
    HasFieldMarshal = None
    HasFieldRVA = None
    InitOnly = None
    Literal = None
    NotSerialized = None
    PinvokeImpl = None
    Private = None
    PrivateScope = None
    Public = None
    ReservedMask = None
    RTSpecialName = None
    SpecialName = None
    Static = None
    value__ = None


class FieldInfo(MemberInfo, _FieldInfo): # skipped bases: <type 'ICustomAttributeProvider'>, <type '_MemberInfo'>
    """ Discovers the attributes of a field and provides access to field metadata. """
    @staticmethod
    def GetFieldFromHandle(handle, declaringType=None):
        """
        GetFieldFromHandle(handle: RuntimeFieldHandle) -> FieldInfo

            Gets a System.Reflection.FieldInfo for the field represented by the specified handle.

            handle: A System.RuntimeFieldHandle structure that contains the handle to the internal metadata representation of a field.

            Returns: A System.Reflection.FieldInfo object representing the field specified by handle.

        GetFieldFromHandle(handle: RuntimeFieldHandle, declaringType: RuntimeTypeHandle) -> FieldInfo

            Gets a System.Reflection.FieldInfo for the field represented by the specified handle, for the specified generic type.

            handle: A System.RuntimeFieldHandle structure that contains the handle to the internal metadata representation of a field.

            declaringType: A System.RuntimeTypeHandle structure that contains the handle to the generic type that defines the field.

            Returns: A System.Reflection.FieldInfo object representing the field specified by handle, in the generic type specified by declaringType.
        """
        ...

    def GetOptionalCustomModifiers(self):
        """
        GetOptionalCustomModifiers(self: FieldInfo) -> Array[Type]

            Gets an array of types that identify the optional custom modifiers of the field.

            Returns: An array of System.Type objects that identify the optional custom modifiers of the current field, such as System.Runtime.CompilerServices.IsConst.
        """
        ...

    def GetRawConstantValue(self):
        """
        GetRawConstantValue(self: FieldInfo) -> object

            Returns a literal value associated with the field by a compiler.

            Returns: An System.Object that contains the literal value associated with the field. If the literal value is a class type with an element value of zero, the return value is ll.
        """
        ...

    def GetRequiredCustomModifiers(self):
        """
        GetRequiredCustomModifiers(self: FieldInfo) -> Array[Type]

            Gets an array of types that identify the required custom modifiers of the property.

            Returns: An array of System.Type objects that identify the required custom modifiers of the current property, such as System.Runtime.CompilerServices.IsConst or

             System.Runtime.CompilerServices.IsImplicitlyDereferenced.
        """
        ...

    @property
    def Attributes(self):
        """
        Gets the attributes associated with this field.

        Get: Attributes(self: FieldInfo) -> FieldAttributes
        """
        ...

    @property
    def FieldHandle(self):
        """
        Gets a ntimeFieldHandle, which is a handle to the internal metadata representation of a field.

        Get: FieldHandle(self: FieldInfo) -> RuntimeFieldHandle
        """
        ...

    @property
    def FieldType(self):
        """
        Gets the type of this field object.

        Get: FieldType(self: FieldInfo) -> Type
        """
        ...

    @property
    def IsAssembly(self):
        """
        Gets a value indicating whether the potential visibility of this field is described by System.Reflection.FieldAttributes.Assembly; that is, the field is visible at most to other types in the same assembly, and is not visible to derived types outside the assembly.

        Get: IsAssembly(self: FieldInfo) -> bool
        """
        ...

    @property
    def IsFamily(self):
        """
        Gets a value indicating whether the visibility of this field is described by System.Reflection.FieldAttributes.Family; that is, the field is visible only within its class and derived classes.

        Get: IsFamily(self: FieldInfo) -> bool
        """
        ...

    @property
    def IsFamilyAndAssembly(self):
        """
        Gets a value indicating whether the visibility of this field is described by System.Reflection.FieldAttributes.FamANDAssem; that is, the field can be accessed from derived classes, but only if they are in the same assembly.

        Get: IsFamilyAndAssembly(self: FieldInfo) -> bool
        """
        ...

    @property
    def IsFamilyOrAssembly(self):
        """
        Gets a value indicating whether the potential visibility of this field is described by System.Reflection.FieldAttributes.FamORAssem; that is, the field can be accessed by derived classes wherever they are, and by classes in the same assembly.

        Get: IsFamilyOrAssembly(self: FieldInfo) -> bool
        """
        ...

    @property
    def IsInitOnly(self):
        """
        Gets a value indicating whether the field can only be set in the body of the constructor.

        Get: IsInitOnly(self: FieldInfo) -> bool
        """
        ...

    @property
    def IsLiteral(self):
        """
        Gets a value indicating whether the value is written at compile time and cannot be changed.

        Get: IsLiteral(self: FieldInfo) -> bool
        """
        ...

    @property
    def IsNotSerialized(self):
        """
        Gets a value indicating whether this field has the tSerialized attribute.

        Get: IsNotSerialized(self: FieldInfo) -> bool
        """
        ...

    @property
    def IsPinvokeImpl(self):
        """
        Gets a value indicating whether the corresponding nvokeImpl attribute is set in System.Reflection.FieldAttributes.

        Get: IsPinvokeImpl(self: FieldInfo) -> bool
        """
        ...

    @property
    def IsPrivate(self):
        """
        Gets a value indicating whether the field is private.

        Get: IsPrivate(self: FieldInfo) -> bool
        """
        ...

    @property
    def IsPublic(self):
        """
        Gets a value indicating whether the field is public.

        Get: IsPublic(self: FieldInfo) -> bool
        """
        ...

    @property
    def IsSecurityCritical(self):
        """
        Gets a value that indicates whether the current field is security-critical or security-safe-critical at the current trust level.

        Get: IsSecurityCritical(self: FieldInfo) -> bool
        """
        ...

    @property
    def IsSecuritySafeCritical(self):
        """
        Gets a value that indicates whether the current field is security-safe-critical at the current trust level.

        Get: IsSecuritySafeCritical(self: FieldInfo) -> bool
        """
        ...

    @property
    def IsSecurityTransparent(self):
        """
        Gets a value that indicates whether the current field is transparent at the current trust level.

        Get: IsSecurityTransparent(self: FieldInfo) -> bool
        """
        ...

    @property
    def IsSpecialName(self):
        """
        Gets a value indicating whether the corresponding ecialName attribute is set in the System.Reflection.FieldAttributes enumerator.

        Get: IsSpecialName(self: FieldInfo) -> bool
        """
        ...

    @property
    def IsStatic(self):
        """
        Gets a value indicating whether the field is static.

        Get: IsStatic(self: FieldInfo) -> bool
        """
        ...

    @property
    def MemberType(self):
        """
        Gets a System.Reflection.MemberTypes value indicating that this member is a field.

        Get: MemberType(self: FieldInfo) -> MemberTypes
        """
        ...



class GenericParameterAttributes(Enum): # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Describes the constraints on a generic type parameter of a generic type or method.

    enum (flags) GenericParameterAttributes, values: Contravariant (2), Covariant (1), DefaultConstructorConstraint (16), None (0), NotNullableValueTypeConstraint (8), ReferenceTypeConstraint (4), SpecialConstraintMask (28), VarianceMask (3)
    """
    Contravariant = None
    Covariant = None
    DefaultConstructorConstraint = None

    NotNullableValueTypeConstraint = None
    ReferenceTypeConstraint = None
    SpecialConstraintMask = None
    value__ = None
    VarianceMask = None


class ICustomTypeProvider:
    """ Represents an object that provides a custom type. """
    def GetCustomType(self):
        """
        GetCustomType(self: ICustomTypeProvider) -> Type

            Gets the custom type provided by this object.

            Returns: The custom type.
        """
        ...


class ImageFileMachine(Enum): # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Identifies the platform targeted by an executable.

    enum ImageFileMachine, values: AMD64 (34404), ARM (452), I386 (332), IA64 (512)
    """
    AMD64 = None
    ARM = None
    I386 = None
    IA64 = None
    value__ = None


class InterfaceMapping: # skipped bases: <type 'object'>
    """ Retrieves the mapping of an interface into the actual methods on a class that implements that interface. """
    InterfaceMethods = None
    InterfaceType = None
    TargetMethods = None
    TargetType = None


class IntrospectionExtensions: # skipped bases: <type 'object'>
    """ Contains methods for converting System.Type objects. """
    @staticmethod
    def GetTypeInfo(type):
        """
        GetTypeInfo(type: Type) -> TypeInfo

            Returns the System.Reflection.TypeInfo representation of the specified type.

            type: The type to convert.

            Returns: The converted object.
        """
        ...

    __all__ = [
        'GetTypeInfo',
    ]


class InvalidFilterCriteriaException(ApplicationException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>
    """
    The exception that is thrown in System.Type.FindMembers(System.Reflection.MemberTypes,System.Reflection.BindingFlags,System.Reflection.MemberFilter,System.Object) when the filter criteria is not valid for the type of filter you are using.

    InvalidFilterCriteriaException()

    InvalidFilterCriteriaException(message: str)

    InvalidFilterCriteriaException(message: str, inner: Exception)
    """
    SerializeObjectState = None


class IReflect:
    """ Interoperates with the IDispatch interface. """
    def GetField(self, name, bindingAttr):
        """
        GetField(self: IReflect, name: str, bindingAttr: BindingFlags) -> FieldInfo

            Returns the System.Reflection.FieldInfo object that corresponds to the specified field and binding flag.

            name: The name of the field to find.

            bindingAttr: The binding attributes used to control the search.

            Returns: A System.Reflection.FieldInfo object containing the field information for the named object that meets the search constraints specified in bindingAttr.
        """
        ...

    def GetFields(self, bindingAttr):
        """
        GetFields(self: IReflect, bindingAttr: BindingFlags) -> Array[FieldInfo]

            Returns an array of System.Reflection.FieldInfo objects that correspond to all fields of the current class.

            bindingAttr: The binding attributes used to control the search.

            Returns: An array of System.Reflection.FieldInfo objects containing all the field information for this reflection object that meets the search constraints specified in

             bindingAttr.
        """
        ...

    def GetMember(self, name, bindingAttr):
        """
        GetMember(self: IReflect, name: str, bindingAttr: BindingFlags) -> Array[MemberInfo]

            Retrieves an array of System.Reflection.MemberInfo objects corresponding to all public members or to all members that match a specified name.

            name: The name of the member to find.

            bindingAttr: The binding attributes used to control the search.

            Returns: An array of System.Reflection.MemberInfo objects matching the name parameter.
        """
        ...

    def GetMembers(self, bindingAttr):
        """
        GetMembers(self: IReflect, bindingAttr: BindingFlags) -> Array[MemberInfo]

            Retrieves an array of System.Reflection.MemberInfo objects that correspond either to all public members or to all members of the current class.

            bindingAttr: The binding attributes used to control the search.

            Returns: An array of System.Reflection.MemberInfo objects containing all the member information for this reflection object.
        """
        ...

    def GetMethod(self, name, bindingAttr, binder=None, types=None, modifiers=None):
        """
        GetMethod(self: IReflect, name: str, bindingAttr: BindingFlags, binder: Binder, types: Array[Type], modifiers: Array[ParameterModifier]) -> MethodInfo

            Retrieves a System.Reflection.MethodInfo object corresponding to a specified method, using a System.Type array to choose from among overloaded methods.

            name: The name of the member to find.

            bindingAttr: The binding attributes used to control the search.

            binder: An object that implements System.Reflection.Binder, containing properties related to this method.

            types: An array used to choose among overloaded methods.

            modifiers: An array of parameter modifiers used to make binding work with parameter signatures in which the types have been modified.

            Returns: The requested method that matches all the specified parameters.

        GetMethod(self: IReflect, name: str, bindingAttr: BindingFlags) -> MethodInfo

            Retrieves a System.Reflection.MethodInfo object that corresponds to a specified method under specified search constraints.

            name: The name of the member to find.

            bindingAttr: The binding attributes used to control the search.

            Returns: A System.Reflection.MethodInfo object containing the method information, with the match being based on the method name and search constraints specified in bindingAttr.
        """
        ...

    def GetMethods(self, bindingAttr):
        """
        GetMethods(self: IReflect, bindingAttr: BindingFlags) -> Array[MethodInfo]

            Retrieves an array of System.Reflection.MethodInfo objects with all public methods or all methods of the current class.

            bindingAttr: The binding attributes used to control the search.

            Returns: An array of System.Reflection.MethodInfo objects containing all the methods defined for this reflection object that meet the search constraints specified in

             bindingAttr.
        """
        ...

    def GetProperties(self, bindingAttr):
        """
        GetProperties(self: IReflect, bindingAttr: BindingFlags) -> Array[PropertyInfo]

            Retrieves an array of System.Reflection.PropertyInfo objects corresponding to all public properties or to all properties of the current class.

            bindingAttr: The binding attribute used to control the search.

            Returns: An array of System.Reflection.PropertyInfo objects for all the properties defined on the reflection object.
        """
        ...

    def GetProperty(self, name, bindingAttr, binder=None, returnType=None, types=None, modifiers=None):
        """
        GetProperty(self: IReflect, name: str, bindingAttr: BindingFlags) -> PropertyInfo

            Retrieves a System.Reflection.PropertyInfo object corresponding to a specified property under specified search constraints.

            name: The name of the property to find.

            bindingAttr: The binding attributes used to control the search.

            Returns: A System.Reflection.PropertyInfo object for the located property that meets the search constraints specified in bindingAttr, or ll if the property was not located.

        GetProperty(self: IReflect, name: str, bindingAttr: BindingFlags, binder: Binder, returnType: Type, types: Array[Type], modifiers: Array[ParameterModifier]) -> PropertyInfo

            Retrieves a System.Reflection.PropertyInfo object that corresponds to a specified property with specified search constraints.

            name: The name of the member to find.

            bindingAttr: The binding attribute used to control the search.

            binder: An object that implements System.Reflection.Binder, containing properties related to this method.

            returnType: The type of the property.

            types: An array used to choose among overloaded methods with the same name.

            modifiers: An array used to choose the parameter modifiers.

            Returns: A System.Reflection.PropertyInfo object for the located property, if a property with the specified name was located in this reflection object, or ll if the property

             was not located.
        """
        ...

    def InvokeMember(self, name, invokeAttr, binder, target, args, modifiers, culture, namedParameters):
        """
        InvokeMember(self: IReflect, name: str, invokeAttr: BindingFlags, binder: Binder, target: object, args: Array[object], modifiers: Array[ParameterModifier], culture: CultureInfo, namedParameters: Array[str]) -> object

            Invokes a specified member.

            name: The name of the member to find.

            invokeAttr: One of the System.Reflection.BindingFlags invocation attributes. The invokeAttr parameter may be a constructor, method, property, or field. A suitable invocation

             attribute must be specified. Invoke the default member of a class by passing the empty string ("") as the name of the member.

            binder: One of the System.Reflection.BindingFlags bit flags. Implements System.Reflection.Binder, containing properties related to this method.

            target: The object on which to invoke the specified member. This parameter is ignored for static members.

            args: An array of objects that contains the number, order, and type of the parameters of the member to be invoked. This is an empty array if there are no parameters.

            modifiers: An array of System.Reflection.ParameterModifier objects. This array has the same length as the args parameter, representing the invoked member's argument attributes in

             the metadata. A parameter can have the following attributes: In, Out, Retval, Optional, and HasDefault. These represent [In], [Out], [retval], [optional], and a

             default parameter, respectively. These attributes are used by various interoperability services.

            culture: An instance of System.Globalization.CultureInfo used to govern the coercion of types. For example, culture converts a ring that represents 1000 to a uble value, since

             1000 is represented differently by different cultures. If this parameter is ll, the System.Globalization.CultureInfo for the current thread is used.

            namedParameters: A ring array of parameters.

            Returns: The specified member.
        """
        ...

    @property
    def UnderlyingSystemType(self):
        """
        Gets the underlying type that represents the System.Reflection.IReflect object.

        Get: UnderlyingSystemType(self: IReflect) -> Type
        """
        ...



class IReflectableType:
    """ Represents a type that you can reflect over. """
    def GetTypeInfo(self):
        """
        GetTypeInfo(self: IReflectableType) -> TypeInfo

            Retrieves an object that represents this type.

            Returns: An object that represents this type.
        """
        ...


class LocalVariableInfo: # skipped bases: <type 'object'>
    """ Discovers the attributes of a local variable and provides access to local variable metadata. """
    def ToString(self):
        """
        ToString(self: LocalVariableInfo) -> str

            Returns a user-readable string that describes the local variable.

            Returns: A string that displays information about the local variable, including the type name, index, and pinned status.
        """
        ...

    @property
    def IsPinned(self):
        """
        Gets a System.Boolean value that indicates whether the object referred to by the local variable is pinned in memory.

        Get: IsPinned(self: LocalVariableInfo) -> bool
        """
        ...

    @property
    def LocalIndex(self):
        """
        Gets the index of the local variable within the method body.

        Get: LocalIndex(self: LocalVariableInfo) -> int
        """
        ...

    @property
    def LocalType(self):
        """
        Gets the type of the local variable.

        Get: LocalType(self: LocalVariableInfo) -> Type
        """
        ...



class ManifestResourceInfo: # skipped bases: <type 'object'>
    """
    Provides access to manifest resources, which are XML files that describe application dependencies.

    ManifestResourceInfo(containingAssembly: Assembly, containingFileName: str, resourceLocation: ResourceLocation)
    """
    @property
    def FileName(self):
        """
        Gets the name of the file that contains the manifest resource, if it is not the same as the manifest file.

        Get: FileName(self: ManifestResourceInfo) -> str
        """
        ...

    @property
    def ReferencedAssembly(self):
        """
        Gets the containing assembly for the manifest resource.

        Get: ReferencedAssembly(self: ManifestResourceInfo) -> Assembly
        """
        ...

    @property
    def ResourceLocation(self):
        """
        Gets the manifest resource's location.

        Get: ResourceLocation(self: ManifestResourceInfo) -> ResourceLocation
        """
        ...



class MemberFilter(MulticastDelegate): # skipped bases: <type 'ICloneable'>, <type 'ISerializable'>
    """
    Represents a delegate that is used to filter a list of members represented in an array of System.Reflection.MemberInfo objects.

    MemberFilter(object: object, method: IntPtr)
    """
    def BeginInvoke(self, m, filterCriteria, callback, object):
        """ BeginInvoke(self: MemberFilter, m: MemberInfo, filterCriteria: object, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result):
        """ EndInvoke(self: MemberFilter, result: IAsyncResult) -> bool """
        ...

    def Invoke(self, m, filterCriteria):
        """ Invoke(self: MemberFilter, m: MemberInfo, filterCriteria: object) -> bool """
        ...


class MemberTypes(Enum): # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Marks each type of member that is defined as a derived class of System.Reflection.MemberInfo.

    enum (flags) MemberTypes, values: All (191), Constructor (1), Custom (64), Event (2), Field (4), Method (8), NestedType (128), Property (16), TypeInfo (32)
    """
    All = None
    Constructor = None
    Custom = None
    Event = None
    Field = None
    Method = None
    NestedType = None
    Property = None
    TypeInfo = None
    value__ = None


class MethodAttributes(Enum): # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies flags for method attributes. These flags are defined in the corhdr.h file.

    enum (flags) MethodAttributes, values: Abstract (1024), Assembly (3), CheckAccessOnOverride (512), FamANDAssem (2), Family (4), FamORAssem (5), Final (32), HasSecurity (16384), HideBySig (128), MemberAccessMask (7), NewSlot (256), PinvokeImpl (8192), Private (1), PrivateScope (0), Public (6), RequireSecObject (32768), ReservedMask (53248), ReuseSlot (0), RTSpecialName (4096), SpecialName (2048), Static (16), UnmanagedExport (8), Virtual (64), VtableLayoutMask (256)
    """
    Abstract = None
    Assembly = None
    CheckAccessOnOverride = None
    FamANDAssem = None
    Family = None
    FamORAssem = None
    Final = None
    HasSecurity = None
    HideBySig = None
    MemberAccessMask = None
    NewSlot = None
    PinvokeImpl = None
    Private = None
    PrivateScope = None
    Public = None
    RequireSecObject = None
    ReservedMask = None
    ReuseSlot = None
    RTSpecialName = None
    SpecialName = None
    Static = None
    UnmanagedExport = None
    value__ = None
    Virtual = None
    VtableLayoutMask = None


class MethodBody: # skipped bases: <type 'object'>
    """ Provides access to the metadata and MSIL for the body of a method. """
    def GetILAsByteArray(self):
        """
        GetILAsByteArray(self: MethodBody) -> Array[Byte]

            Returns the MSIL for the method body, as an array of bytes.

            Returns: An array of type System.Byte that contains the MSIL for the method body.
        """
        ...

    @property
    def ExceptionHandlingClauses(self):
        """
        Gets a list that includes all the exception-handling clauses in the method body.

        Get: ExceptionHandlingClauses(self: MethodBody) -> IList[ExceptionHandlingClause]
        """
        ...

    @property
    def InitLocals(self):
        """
        Gets a value indicating whether local variables in the method body are initialized to the default values for their types.

        Get: InitLocals(self: MethodBody) -> bool
        """
        ...

    @property
    def LocalSignatureMetadataToken(self):
        """
        Gets a metadata token for the signature that describes the local variables for the method in metadata.

        Get: LocalSignatureMetadataToken(self: MethodBody) -> int
        """
        ...

    @property
    def LocalVariables(self):
        """
        Gets the list of local variables declared in the method body.

        Get: LocalVariables(self: MethodBody) -> IList[LocalVariableInfo]
        """
        ...

    @property
    def MaxStackSize(self):
        """
        Gets the maximum number of items on the operand stack when the method is executing.

        Get: MaxStackSize(self: MethodBody) -> int
        """
        ...



class MethodImplAttributes(Enum): # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies flags for the attributes of a method implementation.

    enum MethodImplAttributes, values: AggressiveInlining (256), CodeTypeMask (3), ForwardRef (16), IL (0), InternalCall (4096), Managed (0), ManagedMask (4), MaxMethodImplVal (65535), Native (1), NoInlining (8), NoOptimization (64), OPTIL (2), PreserveSig (128), Runtime (3), SecurityMitigations (1024), Synchronized (32), Unmanaged (4)
    """
    AggressiveInlining = None
    CodeTypeMask = None
    ForwardRef = None
    IL = None
    InternalCall = None
    Managed = None
    ManagedMask = None
    MaxMethodImplVal = None
    Native = None
    NoInlining = None
    NoOptimization = None
    OPTIL = None
    PreserveSig = None
    Runtime = None
    SecurityMitigations = None
    Synchronized = None
    Unmanaged = None
    value__ = None


class MethodInfo(MethodBase, _MethodInfo): # skipped bases: <type '_MethodBase'>, <type 'ICustomAttributeProvider'>, <type '_MemberInfo'>
    """ Discovers the attributes of a method and provides access to method metadata. """
    def CreateDelegate(self, delegateType, target=None):
        """
        CreateDelegate(self: MethodInfo, delegateType: Type) -> Delegate

            Creates a delegate of the specified type from this method.

            delegateType: The type of the delegate to create.

            Returns: The delegate for this method.

        CreateDelegate(self: MethodInfo, delegateType: Type, target: object) -> Delegate

            Creates a delegate of the specified type with the specified target from this method.

            delegateType: The type of the delegate to create.

            target: The object targeted by the delegate.

            Returns: The delegate for this method.
        """
        ...

    def GetGenericMethodDefinition(self):
        """
        GetGenericMethodDefinition(self: MethodInfo) -> MethodInfo

            Returns a System.Reflection.MethodInfo object that represents a generic method definition from which the current method can be constructed.

            Returns: A System.Reflection.MethodInfo object representing a generic method definition from which the current method can be constructed.
        """
        ...

    def MakeGenericMethod(self, typeArguments):
        """
        MakeGenericMethod(self: MethodInfo, *typeArguments: Array[Type]) -> MethodInfo

            Substitutes the elements of an array of types for the type parameters of the current generic method definition, and returns a System.Reflection.MethodInfo object

             representing the resulting constructed method.

            typeArguments: An array of types to be substituted for the type parameters of the current generic method definition.

            Returns: A System.Reflection.MethodInfo object that represents the constructed method formed by substituting the elements of typeArguments for the type parameters of the

             current generic method definition.
        """
        ...

    @property
    def MemberType(self):
        """
        Gets a System.Reflection.MemberTypes value indicating that this member is a method.

        Get: MemberType(self: MethodInfo) -> MemberTypes
        """
        ...

    @property
    def ReturnParameter(self):
        """
        Gets a System.Reflection.ParameterInfo object that contains information about the return type of the method, such as whether the return type has custom modifiers.

        Get: ReturnParameter(self: MethodInfo) -> ParameterInfo
        """
        ...

    @property
    def ReturnType(self):
        """
        Gets the return type of this method.

        Get: ReturnType(self: MethodInfo) -> Type
        """
        ...

    @property
    def ReturnTypeCustomAttributes(self):
        """
        Gets the custom attributes for the return type.

        Get: ReturnTypeCustomAttributes(self: MethodInfo) -> ICustomAttributeProvider
        """
        ...



class Missing(object, ISerializable):
    """ Represents a missing System.Object. This class cannot be inherited. """
    Value = None


class Module(object, _Module, ISerializable, ICustomAttributeProvider):
    """ Performs reflection on a module. """
    def Equals(self, o):
        """
        Equals(self: Module, o: object) -> bool

            Determines whether this module and the specified object are equal.

            o: The object to compare with this instance.

            Returns: ue if o is equal to this instance; otherwise, lse.
        """
        ...

    def FindTypes(self, filter, filterCriteria):
        """
        FindTypes(self: Module, filter: TypeFilter, filterCriteria: object) -> Array[Type]

            Returns an array of classes accepted by the given filter and filter criteria.

            filter: The delegate used to filter the classes.

            filterCriteria: An Object used to filter the classes.

            Returns: An array of type pe containing classes that were accepted by the filter.
        """
        ...

    def GetCustomAttributesData(self):
        """
        GetCustomAttributesData(self: Module) -> IList[CustomAttributeData]

            Returns a list of System.Reflection.CustomAttributeData objects for the current module, which can be used in the reflection-only context.

            Returns: A generic list of System.Reflection.CustomAttributeData objects representing data about the attributes that have been applied to the current module.
        """
        ...

    def GetField(self, name, bindingAttr=None):
        """
        GetField(self: Module, name: str) -> FieldInfo

            Returns a field having the specified name.

            name: The field name.

            Returns: A eldInfo object having the specified name, or ll if the field does not exist.

        GetField(self: Module, name: str, bindingAttr: BindingFlags) -> FieldInfo

            Returns a field having the specified name and binding attributes.

            name: The field name.

            bindingAttr: One of the ndingFlags bit flags used to control the search.

            Returns: A eldInfo object having the specified name and binding attributes, or ll if the field does not exist.
        """
        ...

    def GetFields(self, bindingFlags=None):
        """
        GetFields(self: Module) -> Array[FieldInfo]

            Returns the global fields defined on the module.

            Returns: An array of System.Reflection.FieldInfo objects representing the global fields defined on the module; if there are no global fields, an empty array is returned.

        GetFields(self: Module, bindingFlags: BindingFlags) -> Array[FieldInfo]

            Returns the global fields defined on the module that match the specified binding flags.

            bindingFlags: A bitwise combination of System.Reflection.BindingFlags values that limit the search.

            Returns: An array of type System.Reflection.FieldInfo representing the global fields defined on the module that match the specified binding flags; if no global fields match the

             binding flags, an empty array is returned.
        """
        ...

    def GetHashCode(self):
        """
        GetHashCode(self: Module) -> int

            Returns the hash code for this instance.

            Returns: A 32-bit signed integer hash code.
        """
        ...

    def GetMethod(self, name, *__args):
        """
        GetMethod(self: Module, name: str, bindingAttr: BindingFlags, binder: Binder, callConvention: CallingConventions, types: Array[Type], modifiers: Array[ParameterModifier]) -> MethodInfo

            Returns a method having the specified name, binding information, calling convention, and parameter types and modifiers.

            name: The method name.

            bindingAttr: One of the ndingFlags bit flags used to control the search.

            binder: An object that implements nder, containing properties related to this method.

            callConvention: The calling convention for the method.

            types: The parameter types to search for.

            modifiers: An array of parameter modifiers used to make binding work with parameter signatures in which the types have been modified.

            Returns: A thodInfo object in accordance with the specified criteria, or ll if the method does not exist.

        GetMethod(self: Module, name: str, types: Array[Type]) -> MethodInfo

            Returns a method having the specified name and parameter types.

            name: The method name.

            types: The parameter types to search for.

            Returns: A thodInfo object in accordance with the specified criteria, or ll if the method does not exist.

        GetMethod(self: Module, name: str) -> MethodInfo

            Returns a method having the specified name.

            name: The method name.

            Returns: A thodInfo object having the specified name, or ll if the method does not exist.
        """
        ...

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: Module, name: str, bindingAttr: BindingFlags, binder: Binder, callConvention: CallingConventions, types: Array[Type], modifiers: Array[ParameterModifier]) -> MethodInfo

            Returns the method implementation in accordance with the specified criteria.

            name: The method name.

            bindingAttr: One of the ndingFlags bit flags used to control the search.

            binder: An object that implements nder, containing properties related to this method.

            callConvention: The calling convention for the method.

            types: The parameter types to search for.

            modifiers: An array of parameter modifiers used to make binding work with parameter signatures in which the types have been modified.

            Returns: A thodInfo object containing implementation information as specified, or ll if the method does not exist.
        """
        ...

    def GetMethods(self, bindingFlags=None):
        """
        GetMethods(self: Module) -> Array[MethodInfo]

            Returns the global methods defined on the module.

            Returns: An array of System.Reflection.MethodInfo objects representing all the global methods defined on the module; if there are no global methods, an empty array is returned.

        GetMethods(self: Module, bindingFlags: BindingFlags) -> Array[MethodInfo]

            Returns the global methods defined on the module that match the specified binding flags.

            bindingFlags: A bitwise combination of System.Reflection.BindingFlags values that limit the search.

            Returns: An array of type System.Reflection.MethodInfo representing the global methods defined on the module that match the specified binding flags; if no global methods match

             the binding flags, an empty array is returned.
        """
        ...

    def GetPEKind(self, peKind, machine):
        """
        GetPEKind(self: Module) -> (PortableExecutableKinds, ImageFileMachine)

            Gets a pair of values indicating the nature of the code in a module and the platform targeted by the module.
        """
        ...

    def GetSignerCertificate(self):
        """
        GetSignerCertificate(self: Module) -> X509Certificate

            Returns an 09Certificate object corresponding to the certificate included in the Authenticode signature of the assembly which this module belongs to. If the assembly

             has not been Authenticode signed, ll is returned.

            Returns: An 09Certificate object, or ll if the assembly to which this module belongs has not been Authenticode signed.
        """
        ...

    def GetType(self, className=None, *__args):
        """
        GetType(self: Module, className: str, ignoreCase: bool) -> Type

            Returns the specified type, searching the module with the specified case sensitivity.

            className: The name of the type to locate. The name must be fully qualified with the namespace.

            ignoreCase: ue for case-insensitive search; otherwise, lse.

            Returns: A pe object representing the given type, if the type is in this module; otherwise, ll.

        GetType(self: Module, className: str) -> Type

            Returns the specified type, performing a case-sensitive search.

            className: The name of the type to locate. The name must be fully qualified with the namespace.

            Returns: A pe object representing the given type, if the type is in this module; otherwise, ll.

        GetType(self: Module, className: str, throwOnError: bool, ignoreCase: bool) -> Type

            Returns the specified type, specifying whether to make a case-sensitive search of the module and whether to throw an exception if the type cannot be found.

            className: The name of the type to locate. The name must be fully qualified with the namespace.

            throwOnError: ue to throw an exception if the type cannot be found; lse to return ll.

            ignoreCase: ue for case-insensitive search; otherwise, lse.

            Returns: A System.Type object representing the specified type, if the type is declared in this module; otherwise, ll.
        """
        ...

    def GetTypes(self):
        """
        GetTypes(self: Module) -> Array[Type]

            Returns all the types defined within this module.

            Returns: An array of type pe containing types defined within the module that is reflected by this instance.
        """
        ...

    def IsResource(self):
        """
        IsResource(self: Module) -> bool

            Gets a value indicating whether the object is a resource.

            Returns: ue if the object is a resource; otherwise, lse.
        """
        ...

    def ResolveField(self, metadataToken, genericTypeArguments=None, genericMethodArguments=None):
        """
        ResolveField(self: Module, metadataToken: int) -> FieldInfo

            Returns the field identified by the specified metadata token.

            metadataToken: A metadata token that identifies a field in the module.

            Returns: A System.Reflection.FieldInfo object representing the field that is identified by the specified metadata token.

        ResolveField(self: Module, metadataToken: int, genericTypeArguments: Array[Type], genericMethodArguments: Array[Type]) -> FieldInfo

            Returns the field identified by the specified metadata token, in the context defined by the specified generic type parameters.

            metadataToken: A metadata token that identifies a field in the module.

            genericTypeArguments: An array of System.Type objects representing the generic type arguments of the type where the token is in scope, or ll if that type is not generic.

            genericMethodArguments: An array of System.Type objects representing the generic type arguments of the method where the token is in scope, or ll if that method is not generic.

            Returns: A System.Reflection.FieldInfo object representing the field that is identified by the specified metadata token.
        """
        ...

    def ResolveMember(self, metadataToken, genericTypeArguments=None, genericMethodArguments=None):
        """
        ResolveMember(self: Module, metadataToken: int) -> MemberInfo

            Returns the type or member identified by the specified metadata token.

            metadataToken: A metadata token that identifies a type or member in the module.

            Returns: A System.Reflection.MemberInfo object representing the type or member that is identified by the specified metadata token.

        ResolveMember(self: Module, metadataToken: int, genericTypeArguments: Array[Type], genericMethodArguments: Array[Type]) -> MemberInfo

            Returns the type or member identified by the specified metadata token, in the context defined by the specified generic type parameters.

            metadataToken: A metadata token that identifies a type or member in the module.

            genericTypeArguments: An array of System.Type objects representing the generic type arguments of the type where the token is in scope, or ll if that type is not generic.

            genericMethodArguments: An array of System.Type objects representing the generic type arguments of the method where the token is in scope, or ll if that method is not generic.

            Returns: A System.Reflection.MemberInfo object representing the type or member that is identified by the specified metadata token.
        """
        ...

    def ResolveMethod(self, metadataToken, genericTypeArguments=None, genericMethodArguments=None):
        """
        ResolveMethod(self: Module, metadataToken: int) -> MethodBase

            Returns the method or constructor identified by the specified metadata token.

            metadataToken: A metadata token that identifies a method or constructor in the module.

            Returns: A System.Reflection.MethodBase object representing the method or constructor that is identified by the specified metadata token.

        ResolveMethod(self: Module, metadataToken: int, genericTypeArguments: Array[Type], genericMethodArguments: Array[Type]) -> MethodBase

            Returns the method or constructor identified by the specified metadata token, in the context defined by the specified generic type parameters.

            metadataToken: A metadata token that identifies a method or constructor in the module.

            genericTypeArguments: An array of System.Type objects representing the generic type arguments of the type where the token is in scope, or ll if that type is not generic.

            genericMethodArguments: An array of System.Type objects representing the generic type arguments of the method where the token is in scope, or ll if that method is not generic.

            Returns: A System.Reflection.MethodBase object representing the method that is identified by the specified metadata token.
        """
        ...

    def ResolveSignature(self, metadataToken):
        """
        ResolveSignature(self: Module, metadataToken: int) -> Array[Byte]

            Returns the signature blob identified by a metadata token.

            metadataToken: A metadata token that identifies a signature in the module.

            Returns: An array of bytes representing the signature blob.
        """
        ...

    def ResolveString(self, metadataToken):
        """
        ResolveString(self: Module, metadataToken: int) -> str

            Returns the string identified by the specified metadata token.

            metadataToken: A metadata token that identifies a string in the string heap of the module.

            Returns: A System.String containing a string value from the metadata string heap.
        """
        ...

    def ResolveType(self, metadataToken, genericTypeArguments=None, genericMethodArguments=None):
        """
        ResolveType(self: Module, metadataToken: int) -> Type

            Returns the type identified by the specified metadata token.

            metadataToken: A metadata token that identifies a type in the module.

            Returns: A System.Type object representing the type that is identified by the specified metadata token.

        ResolveType(self: Module, metadataToken: int, genericTypeArguments: Array[Type], genericMethodArguments: Array[Type]) -> Type

            Returns the type identified by the specified metadata token, in the context defined by the specified generic type parameters.

            metadataToken: A metadata token that identifies a type in the module.

            genericTypeArguments: An array of System.Type objects representing the generic type arguments of the type where the token is in scope, or ll if that type is not generic.

            genericMethodArguments: An array of System.Type objects representing the generic type arguments of the method where the token is in scope, or ll if that method is not generic.

            Returns: A System.Type object representing the type that is identified by the specified metadata token.
        """
        ...

    def ToString(self):
        """
        ToString(self: Module) -> str

            Returns the name of the module.

            Returns: A ring representing the name of this module.
        """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    @property
    def Assembly(self):
        """
        Gets the appropriate System.Reflection.Assembly for this instance of System.Reflection.Module.

        Get: Assembly(self: Module) -> Assembly
        """
        ...

    @property
    def CustomAttributes(self):
        """
        Gets a collection that contains this module's custom attributes.

        Get: CustomAttributes(self: Module) -> IEnumerable[CustomAttributeData]
        """
        ...

    @property
    def FullyQualifiedName(self):
        """
        Gets a string representing the fully qualified name and path to this module.

        Get: FullyQualifiedName(self: Module) -> str
        """
        ...

    @property
    def MDStreamVersion(self):
        """
        Gets the metadata stream version.

        Get: MDStreamVersion(self: Module) -> int
        """
        ...

    @property
    def MetadataToken(self):
        """
        Gets a token that identifies the module in metadata.

        Get: MetadataToken(self: Module) -> int
        """
        ...

    @property
    def ModuleHandle(self):
        """
        Gets a handle for the module.

        Get: ModuleHandle(self: Module) -> ModuleHandle
        """
        ...

    @property
    def ModuleVersionId(self):
        """
        Gets a universally unique identifier (UUID) that can be used to distinguish between two versions of a module.

        Get: ModuleVersionId(self: Module) -> Guid
        """
        ...

    @property
    def Name(self):
        """
        Gets a ring representing the name of the module with the path removed.

        Get: Name(self: Module) -> str
        """
        ...

    @property
    def ScopeName(self):
        """
        Gets a string representing the name of the module.

        Get: ScopeName(self: Module) -> str
        """
        ...



class ModuleResolveEventHandler(MulticastDelegate): # skipped bases: <type 'ICloneable'>, <type 'ISerializable'>
    """
    Represents the method that will handle the System.Reflection.Assembly.ModuleResolve event of an System.Reflection.Assembly.

    ModuleResolveEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: ModuleResolveEventHandler, sender: object, e: ResolveEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result):
        """ EndInvoke(self: ModuleResolveEventHandler, result: IAsyncResult) -> Module """
        ...

    def Invoke(self, sender, e):
        """ Invoke(self: ModuleResolveEventHandler, sender: object, e: ResolveEventArgs) -> Module """
        ...


class ObfuscateAssemblyAttribute(Attribute): # skipped bases: <type '_Attribute'>
    """
    Instructs obfuscation tools to use their standard obfuscation rules for the appropriate assembly type.

    ObfuscateAssemblyAttribute(assemblyIsPrivate: bool)
    """
    @staticmethod # known case of __new__
    def __new__(cls, assemblyIsPrivate):
        """ __new__(cls: type, assemblyIsPrivate: bool) """
        ...

    @property
    def AssemblyIsPrivate(self):
        """
        Gets a System.Boolean value indicating whether the assembly was marked private.

        Get: AssemblyIsPrivate(self: ObfuscateAssemblyAttribute) -> bool
        """
        ...

    @property
    def StripAfterObfuscation(self):
        """
        Gets or sets a System.Boolean value indicating whether the obfuscation tool should remove the attribute after processing.

        Get: StripAfterObfuscation(self: ObfuscateAssemblyAttribute) -> bool

        Set: StripAfterObfuscation(self: ObfuscateAssemblyAttribute) = value
        """
        ...



class ObfuscationAttribute(Attribute): # skipped bases: <type '_Attribute'>
    """
    Instructs obfuscation tools to take the specified actions for an assembly, type, or member.

    ObfuscationAttribute()
    """
    @property
    def ApplyToMembers(self):
        """
        Gets or sets a System.Boolean value indicating whether the attribute of a type is to apply to the members of the type.

        Get: ApplyToMembers(self: ObfuscationAttribute) -> bool

        Set: ApplyToMembers(self: ObfuscationAttribute) = value
        """
        ...

    @property
    def Exclude(self):
        """
        Gets or sets a System.Boolean value indicating whether the obfuscation tool should exclude the type or member from obfuscation.

        Get: Exclude(self: ObfuscationAttribute) -> bool

        Set: Exclude(self: ObfuscationAttribute) = value
        """
        ...

    @property
    def Feature(self):
        """
        Gets or sets a string value that is recognized by the obfuscation tool, and which specifies processing options.

        Get: Feature(self: ObfuscationAttribute) -> str

        Set: Feature(self: ObfuscationAttribute) = value
        """
        ...

    @property
    def StripAfterObfuscation(self):
        """
        Gets or sets a System.Boolean value indicating whether the obfuscation tool should remove this attribute after processing.

        Get: StripAfterObfuscation(self: ObfuscationAttribute) -> bool

        Set: StripAfterObfuscation(self: ObfuscationAttribute) = value
        """
        ...



class ParameterAttributes(Enum): # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Defines the attributes that can be associated with a parameter. These are defined in CorHdr.h.

    enum (flags) ParameterAttributes, values: HasDefault (4096), HasFieldMarshal (8192), In (1), Lcid (4), None (0), Optional (16), Out (2), Reserved3 (16384), Reserved4 (32768), ReservedMask (61440), Retval (8)
    """
    HasDefault = None
    HasFieldMarshal = None
    In = None
    Lcid = None

    Optional = None
    Out = None
    Reserved3 = None
    Reserved4 = None
    ReservedMask = None
    Retval = None
    value__ = None


class ParameterInfo(object, _ParameterInfo, ICustomAttributeProvider, IObjectReference):
    """ Discovers the attributes of a parameter and provides access to parameter metadata. """
    def GetCustomAttributesData(self):
        """
        GetCustomAttributesData(self: ParameterInfo) -> IList[CustomAttributeData]

            Returns a list of System.Reflection.CustomAttributeData objects for the current parameter, which can be used in the reflection-only context.

            Returns: A generic list of System.Reflection.CustomAttributeData objects representing data about the attributes that have been applied to the current parameter.
        """
        ...

    def GetOptionalCustomModifiers(self):
        """
        GetOptionalCustomModifiers(self: ParameterInfo) -> Array[Type]

            Gets the optional custom modifiers of the parameter.

            Returns: An array of System.Type objects that identify the optional custom modifiers of the current parameter, such as System.Runtime.CompilerServices.IsConst or

             System.Runtime.CompilerServices.IsImplicitlyDereferenced.
        """
        ...

    def GetRequiredCustomModifiers(self):
        """
        GetRequiredCustomModifiers(self: ParameterInfo) -> Array[Type]

            Gets the required custom modifiers of the parameter.

            Returns: An array of System.Type objects that identify the required custom modifiers of the current parameter, such as System.Runtime.CompilerServices.IsConst or

             System.Runtime.CompilerServices.IsImplicitlyDereferenced.
        """
        ...

    def ToString(self):
        """
        ToString(self: ParameterInfo) -> str

            Gets the parameter type and name represented as a string.

            Returns: A string containing the type and the name of the parameter.
        """
        ...

    @property
    def Attributes(self):
        """
        Gets the attributes for this parameter.

        Get: Attributes(self: ParameterInfo) -> ParameterAttributes
        """
        ...

    @property
    def CustomAttributes(self):
        """
        Gets a collection that contains this parameter's custom attributes.

        Get: CustomAttributes(self: ParameterInfo) -> IEnumerable[CustomAttributeData]
        """
        ...

    @property
    def DefaultValue(self):
        """
        Gets a value indicating the default value if the parameter has a default value.

        Get: DefaultValue(self: ParameterInfo) -> object
        """
        ...

    @property
    def HasDefaultValue(self):
        """
        Gets a value that indicates whether this parameter has a default value.

        Get: HasDefaultValue(self: ParameterInfo) -> bool
        """
        ...

    @property
    def IsIn(self):
        """
        Gets a value indicating whether this is an input parameter.

        Get: IsIn(self: ParameterInfo) -> bool
        """
        ...

    @property
    def IsLcid(self):
        """
        Gets a value indicating whether this parameter is a locale identifier (lcid).

        Get: IsLcid(self: ParameterInfo) -> bool
        """
        ...

    @property
    def IsOptional(self):
        """
        Gets a value indicating whether this parameter is optional.

        Get: IsOptional(self: ParameterInfo) -> bool
        """
        ...

    @property
    def IsOut(self):
        """
        Gets a value indicating whether this is an output parameter.

        Get: IsOut(self: ParameterInfo) -> bool
        """
        ...

    @property
    def IsRetval(self):
        """
        Gets a value indicating whether this is a tval parameter.

        Get: IsRetval(self: ParameterInfo) -> bool
        """
        ...

    @property
    def Member(self):
        """
        Gets a value indicating the member in which the parameter is implemented.

        Get: Member(self: ParameterInfo) -> MemberInfo
        """
        ...

    @property
    def MetadataToken(self):
        """
        Gets a value that identifies this parameter in metadata.

        Get: MetadataToken(self: ParameterInfo) -> int
        """
        ...

    @property
    def Name(self):
        """
        Gets the name of the parameter.

        Get: Name(self: ParameterInfo) -> str
        """
        ...

    @property
    def ParameterType(self):
        """
        Gets the pe of this parameter.

        Get: ParameterType(self: ParameterInfo) -> Type
        """
        ...

    @property
    def Position(self):
        """
        Gets the zero-based position of the parameter in the formal parameter list.

        Get: Position(self: ParameterInfo) -> int
        """
        ...

    @property
    def RawDefaultValue(self):
        """
        Gets a value indicating the default value if the parameter has a default value.

        Get: RawDefaultValue(self: ParameterInfo) -> object
        """
        ...


    AttrsImpl = None
    ClassImpl = None
    DefaultValueImpl = None
    MemberImpl = None
    NameImpl = None
    PositionImpl = None


class ParameterModifier: # skipped bases: <type 'object'>
    """
    Attaches a modifier to parameters so that binding can work with parameter signatures in which the types have been modified.

    ParameterModifier(parameterCount: int)
    """
    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class Pointer(object, ISerializable):
    """ Provides a wrapper class for pointers. """
    @staticmethod
    def Box(ptr, type):
        """
        Box(ptr: Void*, type: Type) -> object

            Boxes the supplied unmanaged memory pointer and the type associated with that pointer into a managed System.Reflection.Pointer wrapper object. The value and the type

             are saved so they can be accessed from the native code during an invocation.

            ptr: The supplied unmanaged memory pointer.

            type: The type associated with the ptr parameter.

            Returns: A pointer object.
        """
        ...

    @staticmethod
    def Unbox(ptr):
        """
        Unbox(ptr: object) -> Void*

            Returns the stored pointer.

            ptr: The stored pointer.

            Returns: This method returns void.
        """
        ...


class PortableExecutableKinds(Enum): # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Identifies the nature of the code in an executable file.

    enum (flags) PortableExecutableKinds, values: ILOnly (1), NotAPortableExecutableImage (0), PE32Plus (4), Preferred32Bit (16), Required32Bit (2), Unmanaged32Bit (8)
    """
    ILOnly = None
    NotAPortableExecutableImage = None
    PE32Plus = None
    Preferred32Bit = None
    Required32Bit = None
    Unmanaged32Bit = None
    value__ = None


class ProcessorArchitecture(Enum): # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Identifies the processor and bits-per-word of the platform targeted by an executable.

    enum ProcessorArchitecture, values: Amd64 (4), Arm (5), IA64 (3), MSIL (1), None (0), X86 (2)
    """
    Amd64 = None
    Arm = None
    IA64 = None
    MSIL = None

    value__ = None
    X86 = None


class PropertyAttributes(Enum): # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Defines the attributes that can be associated with a property. These attribute values are defined in corhdr.h.

    enum (flags) PropertyAttributes, values: HasDefault (4096), None (0), Reserved2 (8192), Reserved3 (16384), Reserved4 (32768), ReservedMask (62464), RTSpecialName (1024), SpecialName (512)
    """
    HasDefault = None

    Reserved2 = None
    Reserved3 = None
    Reserved4 = None
    ReservedMask = None
    RTSpecialName = None
    SpecialName = None
    value__ = None


class PropertyInfo(MemberInfo, _PropertyInfo): # skipped bases: <type 'ICustomAttributeProvider'>, <type '_MemberInfo'>
    """ Discovers the attributes of a property and provides access to property metadata. """
    def GetConstantValue(self):
        """
        GetConstantValue(self: PropertyInfo) -> object

            Returns a literal value associated with the property by a compiler.

            Returns: An System.Object that contains the literal value associated with the property. If the literal value is a class type with an element value of zero, the return value is

             ll.
        """
        ...

    def GetOptionalCustomModifiers(self):
        """
        GetOptionalCustomModifiers(self: PropertyInfo) -> Array[Type]

            Returns an array of types representing the optional custom modifiers of the property.

            Returns: An array of System.Type objects that identify the optional custom modifiers of the current property, such as System.Runtime.CompilerServices.IsConst or

             System.Runtime.CompilerServices.IsImplicitlyDereferenced.
        """
        ...

    def GetRawConstantValue(self):
        """
        GetRawConstantValue(self: PropertyInfo) -> object

            Returns a literal value associated with the property by a compiler.

            Returns: An System.Object that contains the literal value associated with the property. If the literal value is a class type with an element value of zero, the return value is

             ll.
        """
        ...

    def GetRequiredCustomModifiers(self):
        """
        GetRequiredCustomModifiers(self: PropertyInfo) -> Array[Type]

            Returns an array of types representing the required custom modifiers of the property.

            Returns: An array of System.Type objects that identify the required custom modifiers of the current property, such as System.Runtime.CompilerServices.IsConst or

             System.Runtime.CompilerServices.IsImplicitlyDereferenced.
        """
        ...

    @property
    def Attributes(self):
        """
        Gets the attributes for this property.

        Get: Attributes(self: PropertyInfo) -> PropertyAttributes
        """
        ...

    @property
    def CanRead(self):
        """
        Gets a value indicating whether the property can be read.

        Get: CanRead(self: PropertyInfo) -> bool
        """
        ...

    @property
    def CanWrite(self):
        """
        Gets a value indicating whether the property can be written to.

        Get: CanWrite(self: PropertyInfo) -> bool
        """
        ...

    @property
    def GetMethod(self):
        """
        Gets the t accessor for this property.

        Get: GetMethod(self: PropertyInfo) -> MethodInfo
        """
        ...

    @property
    def IsSpecialName(self):
        """
        Gets a value indicating whether the property is the special name.

        Get: IsSpecialName(self: PropertyInfo) -> bool
        """
        ...

    @property
    def MemberType(self):
        """
        Gets a System.Reflection.MemberTypes value indicating that this member is a property.

        Get: MemberType(self: PropertyInfo) -> MemberTypes
        """
        ...

    @property
    def PropertyType(self):
        """
        Gets the type of this property.

        Get: PropertyType(self: PropertyInfo) -> Type
        """
        ...

    @property
    def SetMethod(self):
        """
        Gets the t accessor for this property.

        Get: SetMethod(self: PropertyInfo) -> MethodInfo
        """
        ...



class ReflectionContext: # skipped bases: <type 'object'>
    """ Represents a context that can provide reflection objects. """
    def GetTypeForObject(self, value):
        """
        GetTypeForObject(self: ReflectionContext, value: object) -> TypeInfo

            Gets the representation of the type of the specified object in this reflection context.

            value: The object to represent.

            Returns: An object that represents the type of the specified object.
        """
        ...

    def MapAssembly(self, assembly):
        """
        MapAssembly(self: ReflectionContext, assembly: Assembly) -> Assembly

            Gets the representation, in this reflection context, of an assembly that is represented by an object from another reflection context.

            assembly: The external representation of the assembly to represent in this context.

            Returns: The representation of the assembly in this reflection context.
        """
        ...

    def MapType(self, type):
        """
        MapType(self: ReflectionContext, type: TypeInfo) -> TypeInfo

            Gets the representation, in this reflection context, of a type represented by an object from another reflection context.

            type: The external representation of the type to represent in this context.

            Returns: The representation of the type in this reflection context..
        """
        ...


class ReflectionTypeLoadException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>
    """
    The exception that is thrown by the System.Reflection.Module.GetTypes method if any of the classes in a module cannot be loaded. This class cannot be inherited.

    ReflectionTypeLoadException(classes: Array[Type], exceptions: Array[Exception])

    ReflectionTypeLoadException(classes: Array[Type], exceptions: Array[Exception], message: str)
    """
    @property
    def LoaderExceptions(self):
        """
        Gets the array of exceptions thrown by the class loader.

        Get: LoaderExceptions(self: ReflectionTypeLoadException) -> Array[Exception]
        """
        ...

    @property
    def Types(self):
        """
        Gets the array of classes that were defined in the module and loaded.

        Get: Types(self: ReflectionTypeLoadException) -> Array[Type]
        """
        ...


    SerializeObjectState = None


class ResourceAttributes(Enum): # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies the attributes for a manifest resource.

    enum (flags) ResourceAttributes, values: Private (2), Public (1)
    """
    Private = None
    Public = None
    value__ = None


class ResourceLocation(Enum): # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies the resource location.

    enum (flags) ResourceLocation, values: ContainedInAnotherAssembly (2), ContainedInManifestFile (4), Embedded (1)
    """
    ContainedInAnotherAssembly = None
    ContainedInManifestFile = None
    Embedded = None
    value__ = None


class RuntimeReflectionExtensions: # skipped bases: <type 'object'>
    """ Provides methods that retrieve information about types at run time. """
    @staticmethod
    def GetMethodInfo(_):
        """
        GetMethodInfo(del: Delegate) -> MethodInfo

            Gets an object that represents the method represented by the specified delegate.

            del: The delegate to examine.

            Returns: An object that represents the method.
        """
        ...

    @staticmethod
    def GetRuntimeBaseDefinition(method):
        """
        GetRuntimeBaseDefinition(method: MethodInfo) -> MethodInfo

            Retrieves an object that represents the specified method on the direct or indirect base class where the method was first declared.

            method: The method to retrieve information about.

            Returns: An object that represents the specified method's initial declaration on a base class.
        """
        ...

    @staticmethod
    def GetRuntimeEvent(type, name):
        """
        GetRuntimeEvent(type: Type, name: str) -> EventInfo

            Retrieves an object that represents the specified event.

            type: The type that contains the event.

            name: The name of the event.

            Returns: An object that represents the specified event, or ll if the event is not found.
        """
        ...

    @staticmethod
    def GetRuntimeEvents(type):
        """
        GetRuntimeEvents(type: Type) -> IEnumerable[EventInfo]

            Retrieves a collection that represents all the events defined on a specified type.

            type: The type that contains the events.

            Returns: A collection of events for the specified type.
        """
        ...

    @staticmethod
    def GetRuntimeField(type, name):
        """
        GetRuntimeField(type: Type, name: str) -> FieldInfo

            Retrieves an object that represents a specified field.

            type: The type that contains the field.

            name: The name of the field.

            Returns: An object that represents the specified field, or ll if the field is not found.
        """
        ...

    @staticmethod
    def GetRuntimeFields(type):
        """
        GetRuntimeFields(type: Type) -> IEnumerable[FieldInfo]

            Retrieves a collection that represents all the fields defined on a specified type.

            type: The type that contains the fields.

            Returns: A collection of fields for the specified type.
        """
        ...

    @staticmethod
    def GetRuntimeInterfaceMap(typeInfo, interfaceType):
        """
        GetRuntimeInterfaceMap(typeInfo: TypeInfo, interfaceType: Type) -> InterfaceMapping

            Returns an interface mapping for the specified type and the specified interface.

            typeInfo: The type to retrieve a mapping for.

            interfaceType: The interface to retrieve a mapping for.

            Returns: An object that represents the interface mapping for the specified interface and type.
        """
        ...

    @staticmethod
    def GetRuntimeMethod(type, name, parameters):
        """
        GetRuntimeMethod(type: Type, name: str, parameters: Array[Type]) -> MethodInfo

            Retrieves an object that represents a specified method.

            type: The type that contains the method.

            name: The name of the method.

            parameters: An array that contains the method's parameters.

            Returns: An object that represents the specified method, or ll if the method is not found.
        """
        ...

    @staticmethod
    def GetRuntimeMethods(type):
        """
        GetRuntimeMethods(type: Type) -> IEnumerable[MethodInfo]

            Retrieves a collection that represents all methods defined on a specified type.

            type: The type that contains the methods.

            Returns: A collection of methods for the specified type.
        """
        ...

    @staticmethod
    def GetRuntimeProperties(type):
        """
        GetRuntimeProperties(type: Type) -> IEnumerable[PropertyInfo]

            Retrieves a collection that represents all the properties defined on a specified type.

            type: The type that contains the properties.

            Returns: A collection of properties for the specified type.
        """
        ...

    @staticmethod
    def GetRuntimeProperty(type, name):
        """
        GetRuntimeProperty(type: Type, name: str) -> PropertyInfo

            Retrieves an object that represents a specified property.

            type: The type that contains the property.

            name: The name of the property.

            Returns: An object that represents the specified property, or ll if the property is not found.
        """
        ...

    __all__ = [
        'GetMethodInfo',
        'GetRuntimeBaseDefinition',
        'GetRuntimeEvent',
        'GetRuntimeEvents',
        'GetRuntimeField',
        'GetRuntimeFields',
        'GetRuntimeInterfaceMap',
        'GetRuntimeMethod',
        'GetRuntimeMethods',
        'GetRuntimeProperties',
        'GetRuntimeProperty',
    ]


class StrongNameKeyPair(object, IDeserializationCallback, ISerializable):
    """
    Encapsulates access to a public or private key pair used to sign strong name assemblies.

    StrongNameKeyPair(keyPairFile: FileStream)

    StrongNameKeyPair(keyPairArray: Array[Byte])

    StrongNameKeyPair(keyPairContainer: str)
    """
    @property
    def PublicKey(self):
        """
        Gets the public part of the public key or public key token of the key pair.

        Get: PublicKey(self: StrongNameKeyPair) -> Array[Byte]
        """
        ...



class TargetException(ApplicationException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>
    """
    Represents the exception that is thrown when an attempt is made to invoke an invalid target.

    TargetException()

    TargetException(message: str)

    TargetException(message: str, inner: Exception)
    """
    SerializeObjectState = None


class TargetInvocationException(ApplicationException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>
    """
    The exception that is thrown by methods invoked through reflection. This class cannot be inherited.

    TargetInvocationException(inner: Exception)

    TargetInvocationException(message: str, inner: Exception)
    """
    SerializeObjectState = None


class TargetParameterCountException(ApplicationException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>
    """
    The exception that is thrown when the number of parameters for an invocation does not match the number expected. This class cannot be inherited.

    TargetParameterCountException()

    TargetParameterCountException(message: str)

    TargetParameterCountException(message: str, inner: Exception)
    """
    SerializeObjectState = None


class TypeAttributes(Enum): # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies type attributes.

    enum (flags) TypeAttributes, values: Abstract (128), AnsiClass (0), AutoClass (131072), AutoLayout (0), BeforeFieldInit (1048576), Class (0), ClassSemanticsMask (32), CustomFormatClass (196608), CustomFormatMask (12582912), ExplicitLayout (16), HasSecurity (262144), Import (4096), Interface (32), LayoutMask (24), NestedAssembly (5), NestedFamANDAssem (6), NestedFamily (4), NestedFamORAssem (7), NestedPrivate (3), NestedPublic (2), NotPublic (0), Public (1), ReservedMask (264192), RTSpecialName (2048), Sealed (256), SequentialLayout (8), Serializable (8192), SpecialName (1024), StringFormatMask (196608), UnicodeClass (65536), VisibilityMask (7), WindowsRuntime (16384)
    """
    Abstract = None
    AnsiClass = None
    AutoClass = None
    AutoLayout = None
    BeforeFieldInit = None
    Class = None
    ClassSemanticsMask = None
    CustomFormatClass = None
    CustomFormatMask = None
    ExplicitLayout = None
    HasSecurity = None
    Import = None
    Interface = None
    LayoutMask = None
    NestedAssembly = None
    NestedFamANDAssem = None
    NestedFamily = None
    NestedFamORAssem = None
    NestedPrivate = None
    NestedPublic = None
    NotPublic = None
    Public = None
    ReservedMask = None
    RTSpecialName = None
    Sealed = None
    SequentialLayout = None
    Serializable = None
    SpecialName = None
    StringFormatMask = None
    UnicodeClass = None
    value__ = None
    VisibilityMask = None
    WindowsRuntime = None


class TypeInfo(Type, IReflectableType): # skipped bases: <type 'ICustomAttributeProvider'>, <type '_Type'>, <type '_MemberInfo'>, <type 'IReflect'>
    """ Represents type declarations for class types, interface types, array types, value types, enumeration types, type parameters, generic type definitions, and open or closed constructed generic types. """
    def AsType(self):
        """
        AsType(self: TypeInfo) -> Type

            Returns the current type as a System.Type object.

            Returns: The current type.
        """
        ...

    def GetDeclaredEvent(self, name):
        """
        GetDeclaredEvent(self: TypeInfo, name: str) -> EventInfo

            Returns an object that represents the specified public event declared by the current type.

            name: The name of the event.

            Returns: An object that represents the specified event, if found; otherwise, ll.
        """
        ...

    def GetDeclaredField(self, name):
        """
        GetDeclaredField(self: TypeInfo, name: str) -> FieldInfo

            Returns an object that represents the specified public field declared by the current type.

            name: The name of the field.

            Returns: An object that represents the specified field, if found; otherwise, ll.
        """
        ...

    def GetDeclaredMethod(self, name):
        """
        GetDeclaredMethod(self: TypeInfo, name: str) -> MethodInfo

            Returns an object that represents the specified public method declared by the current type.

            name: The name of the method.

            Returns: An object that represents the specified method, if found; otherwise, ll.
        """
        ...

    def GetDeclaredMethods(self, name):
        """
        GetDeclaredMethods(self: TypeInfo, name: str) -> IEnumerable[MethodInfo]

            Returns a collection that contains all public methods declared on the current type that match the specified name.

            name: The method name to search for.

            Returns: A collection that contains methods that match name.
        """
        ...

    def GetDeclaredNestedType(self, name):
        """
        GetDeclaredNestedType(self: TypeInfo, name: str) -> TypeInfo

            Returns an object that represents the specified public nested type declared by the current type.

            name: The name of the nested type.

            Returns: An object that represents the specified nested type, if found; otherwise, ll.
        """
        ...

    def GetDeclaredProperty(self, name):
        """
        GetDeclaredProperty(self: TypeInfo, name: str) -> PropertyInfo

            Returns an object that represents the specified public property declared by the current type.

            name: The name of the property.

            Returns: An object that represents the specified property, if found; otherwise, ll.
        """
        ...

    @property
    def DeclaredConstructors(self):
        """
        Gets a collection of the constructors declared by the current type.

        Get: DeclaredConstructors(self: TypeInfo) -> IEnumerable[ConstructorInfo]
        """
        ...

    @property
    def DeclaredEvents(self):
        """
        Gets a collection of the events defined by the current type.

        Get: DeclaredEvents(self: TypeInfo) -> IEnumerable[EventInfo]
        """
        ...

    @property
    def DeclaredFields(self):
        """
        Gets a collection of the fields defined by the current type.

        Get: DeclaredFields(self: TypeInfo) -> IEnumerable[FieldInfo]
        """
        ...

    @property
    def DeclaredMembers(self):
        """
        Gets a collection of the members defined by the current type.

        Get: DeclaredMembers(self: TypeInfo) -> IEnumerable[MemberInfo]
        """
        ...

    @property
    def DeclaredMethods(self):
        """
        Gets a collection of the methods defined by the current type.

        Get: DeclaredMethods(self: TypeInfo) -> IEnumerable[MethodInfo]
        """
        ...

    @property
    def DeclaredNestedTypes(self):
        """
        Gets a collection of the nested types defined by the current type.

        Get: DeclaredNestedTypes(self: TypeInfo) -> IEnumerable[TypeInfo]
        """
        ...

    @property
    def DeclaredProperties(self):
        """
        Gets a collection of the properties defined by the current type.

        Get: DeclaredProperties(self: TypeInfo) -> IEnumerable[PropertyInfo]
        """
        ...

    @property
    def GenericTypeParameters(self):
        """
        Gets an array of the generic type parameters of the current instance.

        Get: GenericTypeParameters(self: TypeInfo) -> Array[Type]
        """
        ...

    @property
    def ImplementedInterfaces(self):
        """
        Gets a collection of the interfaces implemented by the current type.

        Get: ImplementedInterfaces(self: TypeInfo) -> IEnumerable[Type]
        """
        ...



class TypeDelegator(TypeInfo): # skipped bases: <type 'ICustomAttributeProvider'>, <type '_Type'>, <type 'IReflectableType'>, <type '_MemberInfo'>, <type 'IReflect'>
    """
    Wraps a System.Type object and delegates methods to that pe.

    TypeDelegator(delegatingType: Type)
    """
    @staticmethod # known case of __new__
    def __new__(cls, delegatingType):
        """
        __new__(cls: type)

        __new__(cls: type, delegatingType: Type)
        """
        ...

    @property
    def Assembly(self):
        """
        Gets the assembly of the implemented type.

        Get: Assembly(self: TypeDelegator) -> Assembly
        """
        ...

    @property
    def AssemblyQualifiedName(self):
        """
        Gets the assembly's fully qualified name.

        Get: AssemblyQualifiedName(self: TypeDelegator) -> str
        """
        ...

    @property
    def BaseType(self):
        """
        Gets the base type for the current type.

        Get: BaseType(self: TypeDelegator) -> Type
        """
        ...

    @property
    def FullName(self):
        """
        Gets the fully qualified name of the implemented type.

        Get: FullName(self: TypeDelegator) -> str
        """
        ...

    @property
    def GUID(self):
        """
        Gets the GUID (globally unique identifier) of the implemented type.

        Get: GUID(self: TypeDelegator) -> Guid
        """
        ...

    @property
    def IsConstructedGenericType(self):
        """
        Gets a value that indicates whether this object represents a constructed generic type.

        Get: IsConstructedGenericType(self: TypeDelegator) -> bool
        """
        ...

    @property
    def MetadataToken(self):
        """
        Gets a value that identifies this entity in metadata.

        Get: MetadataToken(self: TypeDelegator) -> int
        """
        ...

    @property
    def Module(self):
        """
        Gets the module that contains the implemented type.

        Get: Module(self: TypeDelegator) -> Module
        """
        ...

    @property
    def Name(self):
        """
        Gets the name of the implemented type, with the path removed.

        Get: Name(self: TypeDelegator) -> str
        """
        ...

    @property
    def Namespace(self):
        """
        Gets the namespace of the implemented type.

        Get: Namespace(self: TypeDelegator) -> str
        """
        ...

    @property
    def TypeHandle(self):
        """
        Gets a handle to the internal metadata representation of an implemented type.

        Get: TypeHandle(self: TypeDelegator) -> RuntimeTypeHandle
        """
        ...

    @property
    def UnderlyingSystemType(self):
        """
        Gets the underlying System.Type that represents the implemented type.

        Get: UnderlyingSystemType(self: TypeDelegator) -> Type
        """
        ...


    typeImpl = None


class TypeFilter(MulticastDelegate): # skipped bases: <type 'ICloneable'>, <type 'ISerializable'>
    """
    Filters the classes represented in an array of System.Type objects.

    TypeFilter(object: object, method: IntPtr)
    """
    def BeginInvoke(self, m, filterCriteria, callback, object):
        """ BeginInvoke(self: TypeFilter, m: Type, filterCriteria: object, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result):
        """ EndInvoke(self: TypeFilter, result: IAsyncResult) -> bool """
        ...

    def Invoke(self, m, filterCriteria):
        """ Invoke(self: TypeFilter, m: Type, filterCriteria: object) -> bool """
        ...


# variables with complex values
