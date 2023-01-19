# encoding: utf-8
# module System.Runtime.Versioning calls itself Versioning
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class CompatibilitySwitch: # skipped bases: <type 'object'>
    # no doc
    @staticmethod
    def GetValue(compatibilitySwitchName):
        """ GetValue(compatibilitySwitchName: str) -> str """
        ...

    @staticmethod
    def IsEnabled(compatibilitySwitchName):
        """ IsEnabled(compatibilitySwitchName: str) -> bool """
        ...

    __all__ = [
        'GetValue',
        'IsEnabled',
    ]


class ComponentGuaranteesAttribute(Attribute): # skipped bases: <type '_Attribute'>
    """
    Defines the compatibility guarantee of a component, type, or type member that may span multiple versions.

    ComponentGuaranteesAttribute(guarantees: ComponentGuaranteesOptions)
    """
    @staticmethod # known case of __new__
    def __new__(cls, guarantees):
        """ __new__(cls: type, guarantees: ComponentGuaranteesOptions) """
        ...

    @property
    def Guarantees(self):
        """
        Gets a value that indicates the guaranteed level of compatibility of a library, type, or type member that spans multiple versions.

        Get: Guarantees(self: ComponentGuaranteesAttribute) -> ComponentGuaranteesOptions
        """
        ...



class ComponentGuaranteesOptions(Enum): # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Describes the compatibility guarantee of a component, type, or type member that may span multiple versions.

    enum (flags) ComponentGuaranteesOptions, values: Exchange (1), None (0), SideBySide (4), Stable (2)
    """
    Exchange = None

    SideBySide = None
    Stable = None
    value__ = None


class FrameworkName(object, IEquatable[FrameworkName]):
    """
    Represents the name of a version of the .NET Framework.

    FrameworkName(identifier: str, version: Version)

    FrameworkName(identifier: str, version: Version, profile: str)

    FrameworkName(frameworkName: str)
    """
    def GetHashCode(self):
        """
        GetHashCode(self: FrameworkName) -> int

            Returns the hash code for the System.Runtime.Versioning.FrameworkName object.

            Returns: A 32-bit signed integer that represents the hash code of this instance.
        """
        ...

    def ToString(self):
        """
        ToString(self: FrameworkName) -> str

            Returns the string representation of this System.Runtime.Versioning.FrameworkName object.

            Returns: A string that represents this System.Runtime.Versioning.FrameworkName object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    @property
    def FullName(self):
        """
        Gets the full name of this System.Runtime.Versioning.FrameworkName object.

        Get: FullName(self: FrameworkName) -> str
        """
        ...

    @property
    def Identifier(self):
        """
        Gets the identifier of this System.Runtime.Versioning.FrameworkName object.

        Get: Identifier(self: FrameworkName) -> str
        """
        ...

    @property
    def Profile(self):
        """
        Gets the profile name of this System.Runtime.Versioning.FrameworkName object.

        Get: Profile(self: FrameworkName) -> str
        """
        ...

    @property
    def Version(self):
        """
        Gets the version of this System.Runtime.Versioning.FrameworkName object.

        Get: Version(self: FrameworkName) -> Version
        """
        ...



class ResourceConsumptionAttribute(Attribute): # skipped bases: <type '_Attribute'>
    """
    Specifies the resource consumed by the member of a class. This class cannot be inherited.

    ResourceConsumptionAttribute(resourceScope: ResourceScope)

    ResourceConsumptionAttribute(resourceScope: ResourceScope, consumptionScope: ResourceScope)
    """
    @staticmethod # known case of __new__
    def __new__(cls, resourceScope, consumptionScope=None):
        """
        __new__(cls: type, resourceScope: ResourceScope)

        __new__(cls: type, resourceScope: ResourceScope, consumptionScope: ResourceScope)
        """
        ...

    @property
    def ConsumptionScope(self):
        """
        Gets the consumption scope for this member.

        Get: ConsumptionScope(self: ResourceConsumptionAttribute) -> ResourceScope
        """
        ...

    @property
    def ResourceScope(self):
        """
        Gets the resource scope for the consumed resource.

        Get: ResourceScope(self: ResourceConsumptionAttribute) -> ResourceScope
        """
        ...



class ResourceExposureAttribute(Attribute): # skipped bases: <type '_Attribute'>
    """
    Specifies the resource exposure for a member of a class. This class cannot be inherited.

    ResourceExposureAttribute(exposureLevel: ResourceScope)
    """
    @staticmethod # known case of __new__
    def __new__(cls, exposureLevel):
        """ __new__(cls: type, exposureLevel: ResourceScope) """
        ...

    @property
    def ResourceExposureLevel(self):
        """
        Gets the resource exposure scope.

        Get: ResourceExposureLevel(self: ResourceExposureAttribute) -> ResourceScope
        """
        ...



class ResourceScope(Enum): # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Identifies the scope of a sharable resource.

    enum (flags) ResourceScope, values: AppDomain (4), Assembly (32), Library (8), Machine (1), None (0), Private (16), Process (2)
    """
    AppDomain = None
    Assembly = None
    Library = None
    Machine = None

    Private = None
    Process = None
    value__ = None


class TargetFrameworkAttribute(Attribute): # skipped bases: <type '_Attribute'>
    """
    Identifies the version of the .NET Framework that a particular assembly was compiled against.

    TargetFrameworkAttribute(frameworkName: str)
    """
    @staticmethod # known case of __new__
    def __new__(cls, frameworkName):
        """ __new__(cls: type, frameworkName: str) """
        ...

    @property
    def FrameworkDisplayName(self):
        """
        Gets the display name of the .NET Framework version against which an assembly was built.

        Get: FrameworkDisplayName(self: TargetFrameworkAttribute) -> str

        Set: FrameworkDisplayName(self: TargetFrameworkAttribute) = value
        """
        ...

    @property
    def FrameworkName(self):
        """
        Gets the name of the .NET Framework version against which a particular assembly was compiled.

        Get: FrameworkName(self: TargetFrameworkAttribute) -> str
        """
        ...



class VersioningHelper: # skipped bases: <type 'object'>
    """ Provides methods to aid developers in writing version-safe code. This class cannot be inherited. """
    @staticmethod
    def MakeVersionSafeName(name, from, to, type=None):
        """
        MakeVersionSafeName(name: str, from: ResourceScope, to: ResourceScope, type: Type) -> str

            Returns a version-safe name based on the specified resource name, the intended resource consumption scope, and the type using the resource.

            name: The name of the resource.

            from: The beginning of the scope range.

            to: The end of the scope range.

            type: The System.Type of the resource.

            Returns: A version-safe name.

        MakeVersionSafeName(name: str, from: ResourceScope, to: ResourceScope) -> str

            Returns a version-safe name based on the specified resource name and the intended resource consumption source.

            name: The name of the resource.

            from: The scope of the resource.

            to: The desired resource consumption scope.

            Returns: A version-safe name.
        """
        ...

    __all__ = [
        'MakeVersionSafeName',
    ]
