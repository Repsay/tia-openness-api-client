# encoding: utf-8
# module System.Security.Authentication.ExtendedProtection calls itself ExtendedProtection
# from System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class ChannelBinding(SafeHandleZeroOrMinusOneIsInvalid):  # skipped bases: <type 'IDisposable'>
    """The System.Security.Authentication.ExtendedProtection.ChannelBinding class encapsulates a pointer to the opaque data used to bind an authenticated transaction to a secure channel."""

    @property
    def Size(self):
        """
        The System.Security.Authentication.ExtendedProtection.ChannelBinding.Size property gets the size, in bytes, of the channel binding token associated with the System.Security.Authentication.ExtendedProtection.ChannelBinding instance.

        Get: Size(self: ChannelBinding) -> int
        """
        ...
    handle = None

class ChannelBindingKind(Enum):  # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>
    """
    The System.Security.Authentication.ExtendedProtection.ChannelBindingKind enumeration represents the kinds of channel bindings that can be queried from secure channels.

    enum ChannelBindingKind, values: Endpoint (26), Unique (25), Unknown (0)
    """

    Endpoint = None
    Unique = None
    Unknown = None
    value__ = None

class ExtendedProtectionPolicy(object, ISerializable):
    """
    The System.Security.Authentication.ExtendedProtection.ExtendedProtectionPolicy class represents the extended protection policy used by the server to validate incoming client connections.

    ExtendedProtectionPolicy(policyEnforcement: PolicyEnforcement, protectionScenario: ProtectionScenario, customServiceNames: ServiceNameCollection)

    ExtendedProtectionPolicy(policyEnforcement: PolicyEnforcement, protectionScenario: ProtectionScenario, customServiceNames: ICollection)

    ExtendedProtectionPolicy(policyEnforcement: PolicyEnforcement, customChannelBinding: ChannelBinding)

    ExtendedProtectionPolicy(policyEnforcement: PolicyEnforcement)
    """

    @property
    def CustomChannelBinding(self):
        """
        Gets a custom channel binding token (CBT) to use for validation.

        Get: CustomChannelBinding(self: ExtendedProtectionPolicy) -> ChannelBinding
        """
        ...
    @property
    def CustomServiceNames(self):
        """
        Gets the custom Service Provider Name (SPN) list used to match against a client's SPN.

        Get: CustomServiceNames(self: ExtendedProtectionPolicy) -> ServiceNameCollection
        """
        ...
    @property
    def OSSupportsExtendedProtection(self):
        """
        Indicates whether the operating system supports integrated windows authentication with extended protection.

        Get: OSSupportsExtendedProtection() -> bool
        """
        ...
    @property
    def PolicyEnforcement(self):
        """
        Gets when the extended protection policy should be enforced.

        Get: PolicyEnforcement(self: ExtendedProtectionPolicy) -> PolicyEnforcement
        """
        ...
    @property
    def ProtectionScenario(self):
        """
        Gets the kind of protection enforced by the extended protection policy.

        Get: ProtectionScenario(self: ExtendedProtectionPolicy) -> ProtectionScenario
        """
        ...
    def ToString(self):
        """
        ToString(self: ExtendedProtectionPolicy) -> str

            Gets a string representation for the extended protection policy instance.

            Returns: A System.String instance that contains the representation of the System.Security.Authentication.ExtendedProtection.ExtendedProtectionPolicy instance.
        """
        ...
    OSSupportsExtendedProtection = True

class ExtendedProtectionPolicyTypeConverter(TypeConverter):
    """
    The System.Security.Authentication.ExtendedProtection.ExtendedProtectionPolicyTypeConverter class represents the type converter for extended protection policy used by the server to validate incoming client connections.

    ExtendedProtectionPolicyTypeConverter()
    """

    pass

class PolicyEnforcement(Enum):  # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>
    """
    The System.Security.Authentication.ExtendedProtection.PolicyEnforcement enumeration specifies when the System.Security.Authentication.ExtendedProtection.ExtendedProtectionPolicy should be enforced.

    enum PolicyEnforcement, values: Always (2), Never (0), WhenSupported (1)
    """

    Always = None
    Never = None
    value__ = None
    WhenSupported = None

class ProtectionScenario(Enum):  # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>
    """
    The System.Security.Authentication.ExtendedProtection.ProtectionScenario enumeration specifies the protection scenario enforced by the policy.

    enum ProtectionScenario, values: TransportSelected (0), TrustedProxy (1)
    """

    TransportSelected = None
    TrustedProxy = None
    value__ = None

class ServiceNameCollection(ReadOnlyCollectionBase):  # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>
    """
    The System.Security.Authentication.ExtendedProtection.ServiceNameCollection class is a read-only collection of service principal names.

    ServiceNameCollection(items: ICollection)
    """

    def Contains(self, searchServiceName):
        """
        Contains(self: ServiceNameCollection, searchServiceName: str) -> bool

            Returns a value indicating whether the specified string occurs within this System.Security.Authentication.ExtendedProtection.ServiceNameCollection

             instance.

            searchServiceName: The string to seek.

            Returns: Returns System.Boolean.

                  ue if the searchServiceName parameter occurs within this

             System.Security.Authentication.ExtendedProtection.ServiceNameCollection instance; otherwise, lse.
        """
        ...
    def Merge(self, *__args):
        """
        Merge(self: ServiceNameCollection, serviceName: str) -> ServiceNameCollection

            Merges the current System.Security.Authentication.ExtendedProtection.ServiceNameCollection with the specified values to create a new

             System.Security.Authentication.ExtendedProtection.ServiceNameCollection containing the union.

            serviceName: A string that contains the specified values of service names to be used to initialize the class.

            Returns: A new System.Security.Authentication.ExtendedProtection.ServiceNameCollection instance that contains the union of the existing

             System.Security.Authentication.ExtendedProtection.ServiceNameCollection instance merged with the specified values.

        Merge(self: ServiceNameCollection, serviceNames: IEnumerable) -> ServiceNameCollection

            Merges the current System.Security.Authentication.ExtendedProtection.ServiceNameCollection with the specified values to create a new

             System.Security.Authentication.ExtendedProtection.ServiceNameCollection containing the union.

            serviceNames: An instance of the System.Collections.IEnumerable class that contains the specified values of service names to be merged.

            Returns: A new System.Security.Authentication.ExtendedProtection.ServiceNameCollection instance that contains the union of the existing

             System.Security.Authentication.ExtendedProtection.ServiceNameCollection instance merged with the specified values.
        """
        ...
    @staticmethod  # known case of __new__
    def __new__(cls, items):
        """__new__(cls: type, items: ICollection)"""
        ...

class TokenBinding:  # skipped bases: <type 'object'>
    """Contains APIs used for token binding."""

    @property
    def BindingType(self):
        """
        Gets the token binding type.

        Get: BindingType(self: TokenBinding) -> TokenBindingType
        """
        ...
    def GetRawTokenBindingId(self):
        """
        GetRawTokenBindingId(self: TokenBinding) -> Array[Byte]

            Gets the raw token binding Id.

            Returns: The raw token binding Id. The first byte of the raw Id, which represents the binding type, is removed.
        """
        ...

class TokenBindingType(Enum):  # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>
    """
    Represents types of token binding.

    enum TokenBindingType, values: Provided (0), Referred (1)
    """

    Provided = None
    Referred = None
    value__ = None

# variables with complex values
