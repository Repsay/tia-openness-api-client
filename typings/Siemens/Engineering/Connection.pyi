# encoding: utf-8
# module Siemens.Engineering.Connection calls itself Connection
# from Siemens.Engineering, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

from Siemens.Engineering import IEngineeringComposition, IEngineeringObject
from System import IEquatable

class IConfiguration:
    """Connection cofiguration path to a device."""

    pass

class ConfigurationAddress(
    IConfiguration, IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """The connection configuration address"""

    @property
    def Address(self):
        """
        The nodeaddress as string

        Get: Address(self: ConfigurationAddress) -> str
        """
        ...
    @property
    def Name(self):
        """
        The name of the configuration address

        Get: Name(self: ConfigurationAddress) -> str
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: ConfigurationAddress) -> IEngineeringObject
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: ConfigurationAddress) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: ConfigurationAddress) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class ConfigurationAddressComposition(
    IEngineeringComposition, IInternalCompositionAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """Composition of ConfigurationAddresses"""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: ConfigurationAddressComposition) -> IEngineeringObject
        """
        ...
    def Find(self, name):
        """
        Find(self: ConfigurationAddressComposition, name: str) -> ConfigurationAddress

            Finds a given configuration address

            name: Name to find

            Returns: Siemens.Engineering.Connection.ConfigurationAddress
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: ConfigurationAddressComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: ConfigurationAddressComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[ConfigurationAddress](enumerable:  value: ConfigurationAddress) -> bool"""
        ...
    def __ne__(self, *args): ...

class ConfigurationGateway(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """The connection configuration gateway"""

    @property
    def Addresses(self):
        """
        Composition of configuration addresses

        Get: Addresses(self: ConfigurationGateway) -> ConfigurationAddressComposition
        """
        ...
    @property
    def Name(self):
        """
        The name of the configuration gateway

        Get: Name(self: ConfigurationGateway) -> str
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: ConfigurationGateway) -> IEngineeringObject
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: ConfigurationGateway) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: ConfigurationGateway) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class ConfigurationGatewayComposition(
    IEngineeringComposition, IInternalCompositionAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """Composition of ConfigurationGateways"""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: ConfigurationGatewayComposition) -> IEngineeringObject
        """
        ...
    def Find(self, name):
        """
        Find(self: ConfigurationGatewayComposition, name: str) -> ConfigurationGateway

            Finds a given configuration gateway

            name: Name to find

            Returns: Siemens.Engineering.Connection.ConfigurationGateway
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: ConfigurationGatewayComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: ConfigurationGatewayComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[ConfigurationGateway](enumerable:  value: ConfigurationGateway) -> bool"""
        ...
    def __ne__(self, *args): ...

class ConfigurationMode(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """The connection configuration mode"""

    @property
    def Name(self):
        """
        The name of the configuration mode

        Get: Name(self: ConfigurationMode) -> str
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: ConfigurationMode) -> IEngineeringObject
        """
        ...
    @property
    def PcInterfaces(self):
        """
        Composition of Pc interfaces

        Get: PcInterfaces(self: ConfigurationMode) -> ConfigurationPcInterfaceComposition
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: ConfigurationMode) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: ConfigurationMode) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class ConfigurationModeComposition(
    IEngineeringComposition, IInternalCompositionAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """Composition of ConfigurationModes"""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: ConfigurationModeComposition) -> IEngineeringObject
        """
        ...
    def Find(self, name):
        """
        Find(self: ConfigurationModeComposition, name: str) -> ConfigurationMode

            Finds a given configuration mode

            name: Name to find

            Returns: Siemens.Engineering.Connection.ConfigurationMode
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: ConfigurationModeComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: ConfigurationModeComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[ConfigurationMode](enumerable:  value: ConfigurationMode) -> bool"""
        ...
    def __ne__(self, *args): ...

class ConfigurationPcInterface(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """The connection configuration pc interface"""

    @property
    def Addresses(self):
        """
        Composition of configurationAddress

        Get: Addresses(self: ConfigurationPcInterface) -> ConfigurationAddressComposition
        """
        ...
    @property
    def Name(self):
        """
        The name of the configuration Pc interface

        Get: Name(self: ConfigurationPcInterface) -> str
        """
        ...
    @property
    def Number(self):
        """
        Number identifying PcInterface

        Get: Number(self: ConfigurationPcInterface) -> int
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: ConfigurationPcInterface) -> IEngineeringObject
        """
        ...
    @property
    def Subnets(self):
        """
        Composition of configuration Subnets

        Get: Subnets(self: ConfigurationPcInterface) -> ConfigurationSubnetComposition
        """
        ...
    @property
    def TargetInterfaces(self):
        """
        Composition of configuration target interfaces

        Get: TargetInterfaces(self: ConfigurationPcInterface) -> ConfigurationTargetInterfaceComposition
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: ConfigurationPcInterface) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: ConfigurationPcInterface) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class ConfigurationPcInterfaceComposition(
    IEngineeringComposition, IInternalCompositionAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """Composition of ConfigurationPcInterfaces"""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: ConfigurationPcInterfaceComposition) -> IEngineeringObject
        """
        ...
    def Find(self, name, number):
        """
        Find(self: ConfigurationPcInterfaceComposition, name: str, number: int) -> ConfigurationPcInterface

            Finds a given configuration pc interface

            name: Name to find

            number: Number to find

            Returns: Siemens.Engineering.Connection.ConfigurationPcInterface
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: ConfigurationPcInterfaceComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: ConfigurationPcInterfaceComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[ConfigurationPcInterface](enumerable:  value: ConfigurationPcInterface) -> bool"""
        ...
    def __ne__(self, *args): ...

class ConfigurationSubnet(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """The connection configuration subnet"""

    @property
    def Addresses(self):
        """
        Composition of configuration addresses

        Get: Addresses(self: ConfigurationSubnet) -> ConfigurationAddressComposition
        """
        ...
    @property
    def Gateways(self):
        """
        Get all gateways associated with this subnet

        Get: Gateways(self: ConfigurationSubnet) -> ConfigurationGatewayComposition
        """
        ...
    @property
    def Name(self):
        """
        The name of the configuration Subnet

        Get: Name(self: ConfigurationSubnet) -> str
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: ConfigurationSubnet) -> IEngineeringObject
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: ConfigurationSubnet) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: ConfigurationSubnet) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class ConfigurationSubnetComposition(
    IEngineeringComposition, IInternalCompositionAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """Composition of ConfigurationSubnets"""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: ConfigurationSubnetComposition) -> IEngineeringObject
        """
        ...
    def Find(self, name):
        """
        Find(self: ConfigurationSubnetComposition, name: str) -> ConfigurationSubnet

            Finds a given configuration Subnet

            name: Name to find

            Returns: Siemens.Engineering.Connection.ConfigurationSubnet
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: ConfigurationSubnetComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: ConfigurationSubnetComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[ConfigurationSubnet](enumerable:  value: ConfigurationSubnet) -> bool"""
        ...
    def __ne__(self, *args): ...

class ConfigurationTargetInterface(
    IConfiguration, IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """The connection configuration target interface"""

    @property
    def Name(self):
        """
        The name of the configuration target interface

        Get: Name(self: ConfigurationTargetInterface) -> str
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: ConfigurationTargetInterface) -> IEngineeringObject
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: ConfigurationTargetInterface) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: ConfigurationTargetInterface) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class ConfigurationTargetInterfaceComposition(
    IEngineeringComposition, IInternalCompositionAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """Composition of ConfigurationTargetInterfaces"""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: ConfigurationTargetInterfaceComposition) -> IEngineeringObject
        """
        ...
    def Find(self, name):
        """
        Find(self: ConfigurationTargetInterfaceComposition, name: str) -> ConfigurationTargetInterface

            Finds a given configuration target interface

            name: Name to find

            Returns: Siemens.Engineering.Connection.ConfigurationTargetInterface
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: ConfigurationTargetInterfaceComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: ConfigurationTargetInterfaceComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[ConfigurationTargetInterface](enumerable:  value: ConfigurationTargetInterface) -> bool"""
        ...
    def __ne__(self, *args): ...

class ConnectionConfiguration(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Provides the online connection"""

    @property
    def IsConfigured(self):
        """
        Indicates if the connection is configured

        Get: IsConfigured(self: ConnectionConfiguration) -> bool
        """
        ...
    @property
    def Modes(self):
        """
        Composition of configuration modes

        Get: Modes(self: ConnectionConfiguration) -> ConfigurationModeComposition
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: ConnectionConfiguration) -> IEngineeringObject
        """
        ...
    def ApplyConfiguration(self, *__args):
        """
        ApplyConfiguration(self: ConnectionConfiguration, address: ConfigurationAddress) -> bool

            If online is configured, then apply the configuration

            address: The address to apply the configuration

            Returns: System.Boolean

        ApplyConfiguration(self: ConnectionConfiguration, targetInterface: ConfigurationTargetInterface) -> bool

            If online is configured, then apply the configuration

            targetInterface: The target interface for which to apply the configuration

            Returns: System.Boolean
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: ConnectionConfiguration) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: ConnectionConfiguration) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...
