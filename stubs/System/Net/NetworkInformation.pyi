# encoding: utf-8
# module System.Net.NetworkInformation calls itself NetworkInformation
# from System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class DuplicateAddressDetectionState(
    Enum
):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies the current state of an IP address.

    enum DuplicateAddressDetectionState, values: Deprecated (3), Duplicate (2), Invalid (0), Preferred (4), Tentative (1)
    """

    Deprecated = None
    Duplicate = None
    Invalid = None
    Preferred = None
    Tentative = None
    value__ = None

class GatewayIPAddressInformation:  # skipped bases: <type 'object'>
    """Represents the IP address of the network gateway. This class cannot be instantiated."""

    @property
    def Address(self):
        """
        Get the IP address of the gateway.

        Get: Address(self: GatewayIPAddressInformation) -> IPAddress
        """
        ...

class GatewayIPAddressInformationCollection(
    object, ICollection[GatewayIPAddressInformation]
):  # skipped bases: <type 'IEnumerable'>, <type 'IEnumerable[GatewayIPAddressInformation]'>
    """Stores a set of System.Net.NetworkInformation.GatewayIPAddressInformation types."""

    def GetEnumerator(self):
        """
        GetEnumerator(self: GatewayIPAddressInformationCollection) -> IEnumerator[GatewayIPAddressInformation]

            Returns an object that can be used to iterate through this collection.

            Returns: An object that implements the System.Collections.IEnumerator interface and provides access to the System.Net.NetworkInformation.UnicastIPAddressInformation types in

             this collection.
        """
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
        Gets the number of System.Net.NetworkInformation.GatewayIPAddressInformation types in this collection.

        Get: Count(self: GatewayIPAddressInformationCollection) -> int
        """
        ...
    @property
    def IsReadOnly(self):
        """
        Gets a value that indicates whether access to this collection is read-only.

        Get: IsReadOnly(self: GatewayIPAddressInformationCollection) -> bool
        """
        ...

class IcmpV4Statistics:  # skipped bases: <type 'object'>
    """Provides Internet Control Message Protocol for IPv4 (ICMPv4) statistical data for the local computer."""

    @property
    def AddressMaskRepliesReceived(self):
        """
        Gets the number of Internet Control Message Protocol version 4 (ICMPv4) Address Mask Reply messages that were received.

        Get: AddressMaskRepliesReceived(self: IcmpV4Statistics) -> Int64
        """
        ...
    @property
    def AddressMaskRepliesSent(self):
        """
        Gets the number of Internet Control Message Protocol version 4 (ICMPv4) Address Mask Reply messages that were sent.

        Get: AddressMaskRepliesSent(self: IcmpV4Statistics) -> Int64
        """
        ...
    @property
    def AddressMaskRequestsReceived(self):
        """
        Gets the number of Internet Control Message Protocol version 4 (ICMPv4) Address Mask Request messages that were received.

        Get: AddressMaskRequestsReceived(self: IcmpV4Statistics) -> Int64
        """
        ...
    @property
    def AddressMaskRequestsSent(self):
        """
        Gets the number of Internet Control Message Protocol version 4 (ICMPv4) Address Mask Request messages that were sent.

        Get: AddressMaskRequestsSent(self: IcmpV4Statistics) -> Int64
        """
        ...
    @property
    def DestinationUnreachableMessagesReceived(self):
        """
        Gets the number of Internet Control Message Protocol version 4 (ICMPv4) messages that were received because of a packet having an unreachable address in its destination.

        Get: DestinationUnreachableMessagesReceived(self: IcmpV4Statistics) -> Int64
        """
        ...
    @property
    def DestinationUnreachableMessagesSent(self):
        """
        Gets the number of Internet Control Message Protocol version 4 (ICMPv4) messages that were sent because of a packet having an unreachable address in its destination.

        Get: DestinationUnreachableMessagesSent(self: IcmpV4Statistics) -> Int64
        """
        ...
    @property
    def EchoRepliesReceived(self):
        """
        Gets the number of Internet Control Message Protocol version 4 (ICMPv4) Echo Reply messages that were received.

        Get: EchoRepliesReceived(self: IcmpV4Statistics) -> Int64
        """
        ...
    @property
    def EchoRepliesSent(self):
        """
        Gets the number of Internet Control Message Protocol version 4 (ICMPv4) Echo Reply messages that were sent.

        Get: EchoRepliesSent(self: IcmpV4Statistics) -> Int64
        """
        ...
    @property
    def EchoRequestsReceived(self):
        """
        Gets the number of Internet Control Message Protocol version 4 (ICMPv4) Echo Request messages that were received.

        Get: EchoRequestsReceived(self: IcmpV4Statistics) -> Int64
        """
        ...
    @property
    def EchoRequestsSent(self):
        """
        Gets the number of Internet Control Message Protocol version 4 (ICMPv4) Echo Request messages that were sent.

        Get: EchoRequestsSent(self: IcmpV4Statistics) -> Int64
        """
        ...
    @property
    def ErrorsReceived(self):
        """
        Gets the number of Internet Control Message Protocol version 4 (ICMPv4) error messages that were received.

        Get: ErrorsReceived(self: IcmpV4Statistics) -> Int64
        """
        ...
    @property
    def ErrorsSent(self):
        """
        Gets the number of Internet Control Message Protocol version 4 (ICMPv4) error messages that were sent.

        Get: ErrorsSent(self: IcmpV4Statistics) -> Int64
        """
        ...
    @property
    def MessagesReceived(self):
        """
        Gets the number of Internet Control Message Protocol messages that were received.

        Get: MessagesReceived(self: IcmpV4Statistics) -> Int64
        """
        ...
    @property
    def MessagesSent(self):
        """
        Gets the number of Internet Control Message Protocol version 4 (ICMPv4) messages that were sent.

        Get: MessagesSent(self: IcmpV4Statistics) -> Int64
        """
        ...
    @property
    def ParameterProblemsReceived(self):
        """
        Gets the number of Internet Control Message Protocol version 4 (ICMPv4) Parameter Problem messages that were received.

        Get: ParameterProblemsReceived(self: IcmpV4Statistics) -> Int64
        """
        ...
    @property
    def ParameterProblemsSent(self):
        """
        Gets the number of Internet Control Message Protocol version 4 (ICMPv4) Parameter Problem messages that were sent.

        Get: ParameterProblemsSent(self: IcmpV4Statistics) -> Int64
        """
        ...
    @property
    def RedirectsReceived(self):
        """
        Gets the number of Internet Control Message Protocol version 4 (ICMPv4) Redirect messages that were received.

        Get: RedirectsReceived(self: IcmpV4Statistics) -> Int64
        """
        ...
    @property
    def RedirectsSent(self):
        """
        Gets the number of Internet Control Message Protocol version 4 (ICMPv4) Redirect messages that were sent.

        Get: RedirectsSent(self: IcmpV4Statistics) -> Int64
        """
        ...
    @property
    def SourceQuenchesReceived(self):
        """
        Gets the number of Internet Control Message Protocol version 4 (ICMPv4) Source Quench messages that were received.

        Get: SourceQuenchesReceived(self: IcmpV4Statistics) -> Int64
        """
        ...
    @property
    def SourceQuenchesSent(self):
        """
        Gets the number of Internet Control Message Protocol version 4 (ICMPv4) Source Quench messages that were sent.

        Get: SourceQuenchesSent(self: IcmpV4Statistics) -> Int64
        """
        ...
    @property
    def TimeExceededMessagesReceived(self):
        """
        Gets the number of Internet Control Message Protocol version 4 (ICMPv4) Time Exceeded messages that were received.

        Get: TimeExceededMessagesReceived(self: IcmpV4Statistics) -> Int64
        """
        ...
    @property
    def TimeExceededMessagesSent(self):
        """
        Gets the number of Internet Control Message Protocol version 4 (ICMPv4) Time Exceeded messages that were sent.

        Get: TimeExceededMessagesSent(self: IcmpV4Statistics) -> Int64
        """
        ...
    @property
    def TimestampRepliesReceived(self):
        """
        Gets the number of Internet Control Message Protocol version 4 (ICMPv4) Timestamp Reply messages that were received.

        Get: TimestampRepliesReceived(self: IcmpV4Statistics) -> Int64
        """
        ...
    @property
    def TimestampRepliesSent(self):
        """
        Gets the number of Internet Control Message Protocol version 4 (ICMPv4) Timestamp Reply messages that were sent.

        Get: TimestampRepliesSent(self: IcmpV4Statistics) -> Int64
        """
        ...
    @property
    def TimestampRequestsReceived(self):
        """
        Gets the number of Internet Control Message Protocol version 4 (ICMPv4) Timestamp Request messages that were received.

        Get: TimestampRequestsReceived(self: IcmpV4Statistics) -> Int64
        """
        ...
    @property
    def TimestampRequestsSent(self):
        """
        Gets the number of Internet Control Message Protocol version 4 (ICMPv4) Timestamp Request messages that were sent.

        Get: TimestampRequestsSent(self: IcmpV4Statistics) -> Int64
        """
        ...

class IcmpV6Statistics:  # skipped bases: <type 'object'>
    """Provides Internet Control Message Protocol for Internet Protocol version 6 (ICMPv6) statistical data for the local computer."""

    @property
    def DestinationUnreachableMessagesReceived(self):
        """
        Gets the number of Internet Control Message Protocol version 6 (ICMPv6) messages received because of a packet having an unreachable address in its destination.

        Get: DestinationUnreachableMessagesReceived(self: IcmpV6Statistics) -> Int64
        """
        ...
    @property
    def DestinationUnreachableMessagesSent(self):
        """
        Gets the number of Internet Control Message Protocol version 6 (ICMPv6) messages sent because of a packet having an unreachable address in its destination.

        Get: DestinationUnreachableMessagesSent(self: IcmpV6Statistics) -> Int64
        """
        ...
    @property
    def EchoRepliesReceived(self):
        """
        Gets the number of Internet Control Message Protocol version 6 (ICMPv6) Echo Reply messages received.

        Get: EchoRepliesReceived(self: IcmpV6Statistics) -> Int64
        """
        ...
    @property
    def EchoRepliesSent(self):
        """
        Gets the number of Internet Control Message Protocol version 6 (ICMPv6) Echo Reply messages sent.

        Get: EchoRepliesSent(self: IcmpV6Statistics) -> Int64
        """
        ...
    @property
    def EchoRequestsReceived(self):
        """
        Gets the number of Internet Control Message Protocol version 6 (ICMPv6) Echo Request messages received.

        Get: EchoRequestsReceived(self: IcmpV6Statistics) -> Int64
        """
        ...
    @property
    def EchoRequestsSent(self):
        """
        Gets the number of Internet Control Message Protocol version 6 (ICMPv6) Echo Request messages sent.

        Get: EchoRequestsSent(self: IcmpV6Statistics) -> Int64
        """
        ...
    @property
    def ErrorsReceived(self):
        """
        Gets the number of Internet Control Message Protocol version 6 (ICMPv6) error messages received.

        Get: ErrorsReceived(self: IcmpV6Statistics) -> Int64
        """
        ...
    @property
    def ErrorsSent(self):
        """
        Gets the number of Internet Control Message Protocol version 6 (ICMPv6) error messages sent.

        Get: ErrorsSent(self: IcmpV6Statistics) -> Int64
        """
        ...
    @property
    def MembershipQueriesReceived(self):
        """
        Gets the number of Internet Group management Protocol (IGMP) Group Membership Query messages received.

        Get: MembershipQueriesReceived(self: IcmpV6Statistics) -> Int64
        """
        ...
    @property
    def MembershipQueriesSent(self):
        """
        Gets the number of Internet Group management Protocol (IGMP) Group Membership Query messages sent.

        Get: MembershipQueriesSent(self: IcmpV6Statistics) -> Int64
        """
        ...
    @property
    def MembershipReductionsReceived(self):
        """
        Gets the number of Internet Group Management Protocol (IGMP) Group Membership Reduction messages received.

        Get: MembershipReductionsReceived(self: IcmpV6Statistics) -> Int64
        """
        ...
    @property
    def MembershipReductionsSent(self):
        """
        Gets the number of Internet Group Management Protocol (IGMP) Group Membership Reduction messages sent.

        Get: MembershipReductionsSent(self: IcmpV6Statistics) -> Int64
        """
        ...
    @property
    def MembershipReportsReceived(self):
        """
        Gets the number of Internet Group Management Protocol (IGMP) Group Membership Report messages received.

        Get: MembershipReportsReceived(self: IcmpV6Statistics) -> Int64
        """
        ...
    @property
    def MembershipReportsSent(self):
        """
        Gets the number of Internet Group Management Protocol (IGMP) Group Membership Report messages sent.

        Get: MembershipReportsSent(self: IcmpV6Statistics) -> Int64
        """
        ...
    @property
    def MessagesReceived(self):
        """
        Gets the number of Internet Control Message Protocol version 6 (ICMPv6) messages received.

        Get: MessagesReceived(self: IcmpV6Statistics) -> Int64
        """
        ...
    @property
    def MessagesSent(self):
        """
        Gets the number of Internet Control Message Protocol version 6 (ICMPv6) messages sent.

        Get: MessagesSent(self: IcmpV6Statistics) -> Int64
        """
        ...
    @property
    def NeighborAdvertisementsReceived(self):
        """
        Gets the number of Internet Control Message Protocol version 6 (ICMPv6) Neighbor Advertisement messages received.

        Get: NeighborAdvertisementsReceived(self: IcmpV6Statistics) -> Int64
        """
        ...
    @property
    def NeighborAdvertisementsSent(self):
        """
        Gets the number of Internet Control Message Protocol version 6 (ICMPv6) Neighbor Advertisement messages sent.

        Get: NeighborAdvertisementsSent(self: IcmpV6Statistics) -> Int64
        """
        ...
    @property
    def NeighborSolicitsReceived(self):
        """
        Gets the number of Internet Control Message Protocol version 6 (ICMPv6) Neighbor Solicitation messages received.

        Get: NeighborSolicitsReceived(self: IcmpV6Statistics) -> Int64
        """
        ...
    @property
    def NeighborSolicitsSent(self):
        """
        Gets the number of Internet Control Message Protocol version 6 (ICMPv6) Neighbor Solicitation messages sent.

        Get: NeighborSolicitsSent(self: IcmpV6Statistics) -> Int64
        """
        ...
    @property
    def PacketTooBigMessagesReceived(self):
        """
        Gets the number of Internet Control Message Protocol version 6 (ICMPv6) Packet Too Big messages received.

        Get: PacketTooBigMessagesReceived(self: IcmpV6Statistics) -> Int64
        """
        ...
    @property
    def PacketTooBigMessagesSent(self):
        """
        Gets the number of Internet Control Message Protocol version 6 (ICMPv6) Packet Too Big messages sent.

        Get: PacketTooBigMessagesSent(self: IcmpV6Statistics) -> Int64
        """
        ...
    @property
    def ParameterProblemsReceived(self):
        """
        Gets the number of Internet Control Message Protocol version 6 (ICMPv6) Parameter Problem messages received.

        Get: ParameterProblemsReceived(self: IcmpV6Statistics) -> Int64
        """
        ...
    @property
    def ParameterProblemsSent(self):
        """
        Gets the number of Internet Control Message Protocol version 6 (ICMPv6) Parameter Problem messages sent.

        Get: ParameterProblemsSent(self: IcmpV6Statistics) -> Int64
        """
        ...
    @property
    def RedirectsReceived(self):
        """
        Gets the number of Internet Control Message Protocol version 6 (ICMPv6) Redirect messages received.

        Get: RedirectsReceived(self: IcmpV6Statistics) -> Int64
        """
        ...
    @property
    def RedirectsSent(self):
        """
        Gets the number of Internet Control Message Protocol version 6 (ICMPv6) Redirect messages sent.

        Get: RedirectsSent(self: IcmpV6Statistics) -> Int64
        """
        ...
    @property
    def RouterAdvertisementsReceived(self):
        """
        Gets the number of Internet Control Message Protocol version 6 (ICMPv6) Router Advertisement messages received.

        Get: RouterAdvertisementsReceived(self: IcmpV6Statistics) -> Int64
        """
        ...
    @property
    def RouterAdvertisementsSent(self):
        """
        Gets the number of Internet Control Message Protocol version 6 (ICMPv6) Router Advertisement messages sent.

        Get: RouterAdvertisementsSent(self: IcmpV6Statistics) -> Int64
        """
        ...
    @property
    def RouterSolicitsReceived(self):
        """
        Gets the number of Internet Control Message Protocol version 6 (ICMPv6) Router Solicitation messages received.

        Get: RouterSolicitsReceived(self: IcmpV6Statistics) -> Int64
        """
        ...
    @property
    def RouterSolicitsSent(self):
        """
        Gets the number of Internet Control Message Protocol version 6 (ICMPv6) Router Solicitation messages sent.

        Get: RouterSolicitsSent(self: IcmpV6Statistics) -> Int64
        """
        ...
    @property
    def TimeExceededMessagesReceived(self):
        """
        Gets the number of Internet Control Message Protocol version 6 (ICMPv6) Time Exceeded messages received.

        Get: TimeExceededMessagesReceived(self: IcmpV6Statistics) -> Int64
        """
        ...
    @property
    def TimeExceededMessagesSent(self):
        """
        Gets the number of Internet Control Message Protocol version 6 (ICMPv6) Time Exceeded messages sent.

        Get: TimeExceededMessagesSent(self: IcmpV6Statistics) -> Int64
        """
        ...

class IPAddressCollection(
    object, ICollection[IPAddress]
):  # skipped bases: <type 'IEnumerable'>, <type 'IEnumerable[IPAddress]'>
    """Stores a set of System.Net.IPAddress types."""

    def GetEnumerator(self):
        """
        GetEnumerator(self: IPAddressCollection) -> IEnumerator[IPAddress]

            Returns an object that can be used to iterate through this collection.

            Returns: An object that implements the System.Collections.IEnumerator interface and provides access to the System.Net.NetworkInformation.IPAddressCollection types in this

             collection.
        """
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
        Gets the number of System.Net.IPAddress types in this collection.

        Get: Count(self: IPAddressCollection) -> int
        """
        ...
    @property
    def IsReadOnly(self):
        """
        Gets a value that indicates whether access to this collection is read-only.

        Get: IsReadOnly(self: IPAddressCollection) -> bool
        """
        ...

class IPAddressInformation:  # skipped bases: <type 'object'>
    """Provides information about a network interface address."""

    @property
    def Address(self):
        """
        Gets the Internet Protocol (IP) address.

        Get: Address(self: IPAddressInformation) -> IPAddress
        """
        ...
    @property
    def IsDnsEligible(self):
        """
        Gets a System.Boolean value that indicates whether the Internet Protocol (IP) address is valid to appear in a Domain Name System (DNS) server database.

        Get: IsDnsEligible(self: IPAddressInformation) -> bool
        """
        ...
    @property
    def IsTransient(self):
        """
        Gets a System.Boolean value that indicates whether the Internet Protocol (IP) address is transient (a cluster address).

        Get: IsTransient(self: IPAddressInformation) -> bool
        """
        ...

class IPAddressInformationCollection(
    object, ICollection[IPAddressInformation]
):  # skipped bases: <type 'IEnumerable[IPAddressInformation]'>, <type 'IEnumerable'>
    """Stores a set of System.Net.NetworkInformation.IPAddressInformation types."""

    def GetEnumerator(self):
        """
        GetEnumerator(self: IPAddressInformationCollection) -> IEnumerator[IPAddressInformation]

            Returns an object that can be used to iterate through this collection.

            Returns: An object that implements the System.Collections.IEnumerator interface and provides access to the System.Net.NetworkInformation.IPAddressInformation types in this

             collection.
        """
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
        Gets the number of System.Net.NetworkInformation.IPAddressInformation types in this collection.

        Get: Count(self: IPAddressInformationCollection) -> int
        """
        ...
    @property
    def IsReadOnly(self):
        """
        Gets a value that indicates whether access to this collection is read-only.

        Get: IsReadOnly(self: IPAddressInformationCollection) -> bool
        """
        ...

class IPGlobalProperties:  # skipped bases: <type 'object'>
    """Provides information about the network connectivity of the local computer."""

    def BeginGetUnicastAddresses(self, callback, state):
        """
        BeginGetUnicastAddresses(self: IPGlobalProperties, callback: AsyncCallback, state: object) -> IAsyncResult

            Begins an asynchronous request to retrieve the stable unicast IP address table on the local computer.

            callback: The System.AsyncCallback delegate.

            state: An object that contains state information for this request.

            Returns: An System.IAsyncResult that references the asynchronous request.
        """
        ...
    def EndGetUnicastAddresses(self, asyncResult):
        """
        EndGetUnicastAddresses(self: IPGlobalProperties, asyncResult: IAsyncResult) -> UnicastIPAddressInformationCollection

            Ends a pending asynchronous request to retrieve the stable unicast IP address table on the local computer.

            asyncResult: An System.IAsyncResult that references the asynchronous request.

            Returns: An System.IAsyncResult that stores state information and any user defined data for this asynchronous operation.
        """
        ...
    def GetActiveTcpConnections(self):
        """
        GetActiveTcpConnections(self: IPGlobalProperties) -> Array[TcpConnectionInformation]

            Returns information about the Internet Protocol version 4 (IPv4) and IPv6 Transmission Control Protocol (TCP) connections on the local computer.

            Returns: A System.Net.NetworkInformation.TcpConnectionInformation array that contains objects that describe the active TCP connections, or an empty array if no active TCP

             connections are detected.
        """
        ...
    def GetActiveTcpListeners(self):
        """
        GetActiveTcpListeners(self: IPGlobalProperties) -> Array[IPEndPoint]

            Returns endpoint information about the Internet Protocol version 4 (IPv4) and IPv6 Transmission Control Protocol (TCP) listeners on the local computer.

            Returns: A System.Net.IPEndPoint array that contains objects that describe the active TCP listeners, or an empty array, if no active TCP listeners are detected.
        """
        ...
    def GetActiveUdpListeners(self):
        """
        GetActiveUdpListeners(self: IPGlobalProperties) -> Array[IPEndPoint]

            Returns information about the Internet Protocol version 4 (IPv4) and IPv6 User Datagram Protocol (UDP) listeners on the local computer.

            Returns: An System.Net.IPEndPoint array that contains objects that describe the UDP listeners, or an empty array if no UDP listeners are detected.
        """
        ...
    def GetIcmpV4Statistics(self):
        """
        GetIcmpV4Statistics(self: IPGlobalProperties) -> IcmpV4Statistics

            Provides Internet Control Message Protocol (ICMP) version 4 statistical data for the local computer.

            Returns: An System.Net.NetworkInformation.IcmpV4Statistics object that provides ICMP version 4 traffic statistics for the local computer.
        """
        ...
    def GetIcmpV6Statistics(self):
        """
        GetIcmpV6Statistics(self: IPGlobalProperties) -> IcmpV6Statistics

            Provides Internet Control Message Protocol (ICMP) version 6 statistical data for the local computer.

            Returns: An System.Net.NetworkInformation.IcmpV6Statistics object that provides ICMP version 6 traffic statistics for the local computer.
        """
        ...
    @staticmethod
    def GetIPGlobalProperties():
        """
        GetIPGlobalProperties() -> IPGlobalProperties

            Gets an object that provides information about the local computer's network connectivity and traffic statistics.

            Returns: A System.Net.NetworkInformation.IPGlobalProperties object that contains information about the local computer.
        """
        ...
    def GetIPv4GlobalStatistics(self):
        """
        GetIPv4GlobalStatistics(self: IPGlobalProperties) -> IPGlobalStatistics

            Provides Internet Protocol version 4 (IPv4) statistical data for the local computer.

            Returns: An System.Net.NetworkInformation.IPGlobalStatistics object that provides IPv4 traffic statistics for the local computer.
        """
        ...
    def GetIPv6GlobalStatistics(self):
        """
        GetIPv6GlobalStatistics(self: IPGlobalProperties) -> IPGlobalStatistics

            Provides Internet Protocol version 6 (IPv6) statistical data for the local computer.

            Returns: An System.Net.NetworkInformation.IPGlobalStatistics object that provides IPv6 traffic statistics for the local computer.
        """
        ...
    def GetTcpIPv4Statistics(self):
        """
        GetTcpIPv4Statistics(self: IPGlobalProperties) -> TcpStatistics

            Provides Transmission Control Protocol/Internet Protocol version 4 (TCP/IPv4) statistical data for the local computer.

            Returns: A System.Net.NetworkInformation.TcpStatistics object that provides TCP/IPv4 traffic statistics for the local computer.
        """
        ...
    def GetTcpIPv6Statistics(self):
        """
        GetTcpIPv6Statistics(self: IPGlobalProperties) -> TcpStatistics

            Provides Transmission Control Protocol/Internet Protocol version 6 (TCP/IPv6) statistical data for the local computer.

            Returns: A System.Net.NetworkInformation.TcpStatistics object that provides TCP/IPv6 traffic statistics for the local computer.
        """
        ...
    def GetUdpIPv4Statistics(self):
        """
        GetUdpIPv4Statistics(self: IPGlobalProperties) -> UdpStatistics

            Provides User Datagram Protocol/Internet Protocol version 4 (UDP/IPv4) statistical data for the local computer.

            Returns: A System.Net.NetworkInformation.UdpStatistics object that provides UDP/IPv4 traffic statistics for the local computer.
        """
        ...
    def GetUdpIPv6Statistics(self):
        """
        GetUdpIPv6Statistics(self: IPGlobalProperties) -> UdpStatistics

            Provides User Datagram Protocol/Internet Protocol version 6 (UDP/IPv6) statistical data for the local computer.

            Returns: A System.Net.NetworkInformation.UdpStatistics object that provides UDP/IPv6 traffic statistics for the local computer.
        """
        ...
    def GetUnicastAddresses(self):
        """
        GetUnicastAddresses(self: IPGlobalProperties) -> UnicastIPAddressInformationCollection

            Retrieves the stable unicast IP address table on the local computer.

            Returns: A System.Net.NetworkInformation.UnicastIPAddressInformationCollection that contains a list of stable unicast IP addresses on the local computer.
        """
        ...
    def GetUnicastAddressesAsync(self):
        """
        GetUnicastAddressesAsync(self: IPGlobalProperties) -> Task[UnicastIPAddressInformationCollection]

            Retrieves the stable unicast IP address table on the local computer as an asynchronous operation.

            Returns: Returns System.Threading.Tasks.Task.The task object representing the asynchronous operation.
        """
        ...
    @property
    def DhcpScopeName(self):
        """
        Gets the Dynamic Host Configuration Protocol (DHCP) scope name.

        Get: DhcpScopeName(self: IPGlobalProperties) -> str
        """
        ...
    @property
    def DomainName(self):
        """
        Gets the domain in which the local computer is registered.

        Get: DomainName(self: IPGlobalProperties) -> str
        """
        ...
    @property
    def HostName(self):
        """
        Gets the host name for the local computer.

        Get: HostName(self: IPGlobalProperties) -> str
        """
        ...
    @property
    def IsWinsProxy(self):
        """
        Gets a System.Boolean value that specifies whether the local computer is acting as a Windows Internet Name Service (WINS) proxy.

        Get: IsWinsProxy(self: IPGlobalProperties) -> bool
        """
        ...
    @property
    def NodeType(self):
        """
        Gets the Network Basic Input/Output System (NetBIOS) node type of the local computer.

        Get: NodeType(self: IPGlobalProperties) -> NetBiosNodeType
        """
        ...

class IPGlobalStatistics:  # skipped bases: <type 'object'>
    """Provides Internet Protocol (IP) statistical data."""

    @property
    def DefaultTtl(self):
        """
        Gets the default time-to-live (TTL) value for Internet Protocol (IP) packets.

        Get: DefaultTtl(self: IPGlobalStatistics) -> int
        """
        ...
    @property
    def ForwardingEnabled(self):
        """
        Gets a System.Boolean value that specifies whether Internet Protocol (IP) packet forwarding is enabled.

        Get: ForwardingEnabled(self: IPGlobalStatistics) -> bool
        """
        ...
    @property
    def NumberOfInterfaces(self):
        """
        Gets the number of network interfaces.

        Get: NumberOfInterfaces(self: IPGlobalStatistics) -> int
        """
        ...
    @property
    def NumberOfIPAddresses(self):
        """
        Gets the number of Internet Protocol (IP) addresses assigned to the local computer.

        Get: NumberOfIPAddresses(self: IPGlobalStatistics) -> int
        """
        ...
    @property
    def NumberOfRoutes(self):
        """
        Gets the number of routes in the Internet Protocol (IP) routing table.

        Get: NumberOfRoutes(self: IPGlobalStatistics) -> int
        """
        ...
    @property
    def OutputPacketRequests(self):
        """
        Gets the number of outbound Internet Protocol (IP) packets.

        Get: OutputPacketRequests(self: IPGlobalStatistics) -> Int64
        """
        ...
    @property
    def OutputPacketRoutingDiscards(self):
        """
        Gets the number of routes that have been discarded from the routing table.

        Get: OutputPacketRoutingDiscards(self: IPGlobalStatistics) -> Int64
        """
        ...
    @property
    def OutputPacketsDiscarded(self):
        """
        Gets the number of transmitted Internet Protocol (IP) packets that have been discarded.

        Get: OutputPacketsDiscarded(self: IPGlobalStatistics) -> Int64
        """
        ...
    @property
    def OutputPacketsWithNoRoute(self):
        """
        Gets the number of Internet Protocol (IP) packets for which the local computer could not determine a route to the destination address.

        Get: OutputPacketsWithNoRoute(self: IPGlobalStatistics) -> Int64
        """
        ...
    @property
    def PacketFragmentFailures(self):
        """
        Gets the number of Internet Protocol (IP) packets that could not be fragmented.

        Get: PacketFragmentFailures(self: IPGlobalStatistics) -> Int64
        """
        ...
    @property
    def PacketReassembliesRequired(self):
        """
        Gets the number of Internet Protocol (IP) packets that required reassembly.

        Get: PacketReassembliesRequired(self: IPGlobalStatistics) -> Int64
        """
        ...
    @property
    def PacketReassemblyFailures(self):
        """
        Gets the number of Internet Protocol (IP) packets that were not successfully reassembled.

        Get: PacketReassemblyFailures(self: IPGlobalStatistics) -> Int64
        """
        ...
    @property
    def PacketReassemblyTimeout(self):
        """
        Gets the maximum amount of time within which all fragments of an Internet Protocol (IP) packet must arrive.

        Get: PacketReassemblyTimeout(self: IPGlobalStatistics) -> Int64
        """
        ...
    @property
    def PacketsFragmented(self):
        """
        Gets the number of Internet Protocol (IP) packets fragmented.

        Get: PacketsFragmented(self: IPGlobalStatistics) -> Int64
        """
        ...
    @property
    def PacketsReassembled(self):
        """
        Gets the number of Internet Protocol (IP) packets reassembled.

        Get: PacketsReassembled(self: IPGlobalStatistics) -> Int64
        """
        ...
    @property
    def ReceivedPackets(self):
        """
        Gets the number of Internet Protocol (IP) packets received.

        Get: ReceivedPackets(self: IPGlobalStatistics) -> Int64
        """
        ...
    @property
    def ReceivedPacketsDelivered(self):
        """
        Gets the number of Internet Protocol (IP) packets delivered.

        Get: ReceivedPacketsDelivered(self: IPGlobalStatistics) -> Int64
        """
        ...
    @property
    def ReceivedPacketsDiscarded(self):
        """
        Gets the number of Internet Protocol (IP) packets that have been received and discarded.

        Get: ReceivedPacketsDiscarded(self: IPGlobalStatistics) -> Int64
        """
        ...
    @property
    def ReceivedPacketsForwarded(self):
        """
        Gets the number of Internet Protocol (IP) packets forwarded.

        Get: ReceivedPacketsForwarded(self: IPGlobalStatistics) -> Int64
        """
        ...
    @property
    def ReceivedPacketsWithAddressErrors(self):
        """
        Gets the number of Internet Protocol (IP) packets with address errors that were received.

        Get: ReceivedPacketsWithAddressErrors(self: IPGlobalStatistics) -> Int64
        """
        ...
    @property
    def ReceivedPacketsWithHeadersErrors(self):
        """
        Gets the number of Internet Protocol (IP) packets with header errors that were received.

        Get: ReceivedPacketsWithHeadersErrors(self: IPGlobalStatistics) -> Int64
        """
        ...
    @property
    def ReceivedPacketsWithUnknownProtocol(self):
        """
        Gets the number of Internet Protocol (IP) packets received on the local machine with an unknown protocol in the header.

        Get: ReceivedPacketsWithUnknownProtocol(self: IPGlobalStatistics) -> Int64
        """
        ...

class IPInterfaceProperties:  # skipped bases: <type 'object'>
    """Provides information about network interfaces that support Internet Protocol version 4 (IPv4) or Internet Protocol version 6 (IPv6)."""

    def GetIPv4Properties(self):
        """
        GetIPv4Properties(self: IPInterfaceProperties) -> IPv4InterfaceProperties

            Provides Internet Protocol version 4 (IPv4) configuration data for this network interface.

            Returns: An System.Net.NetworkInformation.IPv4InterfaceProperties object that contains IPv4 configuration data, or ll if no data is available for the interface.
        """
        ...
    def GetIPv6Properties(self):
        """
        GetIPv6Properties(self: IPInterfaceProperties) -> IPv6InterfaceProperties

            Provides Internet Protocol version 6 (IPv6) configuration data for this network interface.

            Returns: An System.Net.NetworkInformation.IPv6InterfaceProperties object that contains IPv6 configuration data.
        """
        ...
    @property
    def AnycastAddresses(self):
        """
        Gets the anycast IP addresses assigned to this interface.

        Get: AnycastAddresses(self: IPInterfaceProperties) -> IPAddressInformationCollection
        """
        ...
    @property
    def DhcpServerAddresses(self):
        """
        Gets the addresses of Dynamic Host Configuration Protocol (DHCP) servers for this interface.

        Get: DhcpServerAddresses(self: IPInterfaceProperties) -> IPAddressCollection
        """
        ...
    @property
    def DnsAddresses(self):
        """
        Gets the addresses of Domain Name System (DNS) servers for this interface.

        Get: DnsAddresses(self: IPInterfaceProperties) -> IPAddressCollection
        """
        ...
    @property
    def DnsSuffix(self):
        """
        Gets the Domain Name System (DNS) suffix associated with this interface.

        Get: DnsSuffix(self: IPInterfaceProperties) -> str
        """
        ...
    @property
    def GatewayAddresses(self):
        """
        Gets the IPv4 network gateway addresses for this interface.

        Get: GatewayAddresses(self: IPInterfaceProperties) -> GatewayIPAddressInformationCollection
        """
        ...
    @property
    def IsDnsEnabled(self):
        """
        Gets a System.Boolean value that indicates whether NetBt is configured to use DNS name resolution on this interface.

        Get: IsDnsEnabled(self: IPInterfaceProperties) -> bool
        """
        ...
    @property
    def IsDynamicDnsEnabled(self):
        """
        Gets a System.Boolean value that indicates whether this interface is configured to automatically register its IP address information with the Domain Name System (DNS).

        Get: IsDynamicDnsEnabled(self: IPInterfaceProperties) -> bool
        """
        ...
    @property
    def MulticastAddresses(self):
        """
        Gets the multicast addresses assigned to this interface.

        Get: MulticastAddresses(self: IPInterfaceProperties) -> MulticastIPAddressInformationCollection
        """
        ...
    @property
    def UnicastAddresses(self):
        """
        Gets the unicast addresses assigned to this interface.

        Get: UnicastAddresses(self: IPInterfaceProperties) -> UnicastIPAddressInformationCollection
        """
        ...
    @property
    def WinsServersAddresses(self):
        """
        Gets the addresses of Windows Internet Name Service (WINS) servers.

        Get: WinsServersAddresses(self: IPInterfaceProperties) -> IPAddressCollection
        """
        ...

class IPInterfaceStatistics:  # skipped bases: <type 'object'>
    """Provides Internet Protocol (IP) statistical data for an network interface on the local computer."""

    @property
    def BytesReceived(self):
        """
        Gets the number of bytes that were received on the interface.

        Get: BytesReceived(self: IPInterfaceStatistics) -> Int64
        """
        ...
    @property
    def BytesSent(self):
        """
        Gets the number of bytes that were sent on the interface.

        Get: BytesSent(self: IPInterfaceStatistics) -> Int64
        """
        ...
    @property
    def IncomingPacketsDiscarded(self):
        """
        Gets the number of incoming packets that were discarded.

        Get: IncomingPacketsDiscarded(self: IPInterfaceStatistics) -> Int64
        """
        ...
    @property
    def IncomingPacketsWithErrors(self):
        """
        Gets the number of incoming packets with errors.

        Get: IncomingPacketsWithErrors(self: IPInterfaceStatistics) -> Int64
        """
        ...
    @property
    def IncomingUnknownProtocolPackets(self):
        """
        Gets the number of incoming packets with an unknown protocol that were received on the interface.

        Get: IncomingUnknownProtocolPackets(self: IPInterfaceStatistics) -> Int64
        """
        ...
    @property
    def NonUnicastPacketsReceived(self):
        """
        Gets the number of non-unicast packets that were received on the interface.

        Get: NonUnicastPacketsReceived(self: IPInterfaceStatistics) -> Int64
        """
        ...
    @property
    def NonUnicastPacketsSent(self):
        """
        Gets the number of non-unicast packets that were sent on the interface.

        Get: NonUnicastPacketsSent(self: IPInterfaceStatistics) -> Int64
        """
        ...
    @property
    def OutgoingPacketsDiscarded(self):
        """
        Gets the number of outgoing packets that were discarded.

        Get: OutgoingPacketsDiscarded(self: IPInterfaceStatistics) -> Int64
        """
        ...
    @property
    def OutgoingPacketsWithErrors(self):
        """
        Gets the number of outgoing packets with errors.

        Get: OutgoingPacketsWithErrors(self: IPInterfaceStatistics) -> Int64
        """
        ...
    @property
    def OutputQueueLength(self):
        """
        Gets the length of the output queue.

        Get: OutputQueueLength(self: IPInterfaceStatistics) -> Int64
        """
        ...
    @property
    def UnicastPacketsReceived(self):
        """
        Gets the number of unicast packets that were received on the interface.

        Get: UnicastPacketsReceived(self: IPInterfaceStatistics) -> Int64
        """
        ...
    @property
    def UnicastPacketsSent(self):
        """
        Gets the number of unicast packets that were sent on the interface.

        Get: UnicastPacketsSent(self: IPInterfaceStatistics) -> Int64
        """
        ...

class IPStatus(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Reports the status of sending an Internet Control Message Protocol (ICMP) echo message to a computer.

    enum IPStatus, values: BadDestination (11018), BadHeader (11042), BadOption (11007), BadRoute (11012), DestinationHostUnreachable (11003), DestinationNetworkUnreachable (11002), DestinationPortUnreachable (11005), DestinationProhibited (11004), DestinationProtocolUnreachable (11004), DestinationScopeMismatch (11045), DestinationUnreachable (11040), HardwareError (11008), IcmpError (11044), NoResources (11006), PacketTooBig (11009), ParameterProblem (11015), SourceQuench (11016), Success (0), TimedOut (11010), TimeExceeded (11041), TtlExpired (11013), TtlReassemblyTimeExceeded (11014), Unknown (-1), UnrecognizedNextHeader (11043)
    """

    BadDestination = None
    BadHeader = None
    BadOption = None
    BadRoute = None
    DestinationHostUnreachable = None
    DestinationNetworkUnreachable = None
    DestinationPortUnreachable = None
    DestinationProhibited = None
    DestinationProtocolUnreachable = None
    DestinationScopeMismatch = None
    DestinationUnreachable = None
    HardwareError = None
    IcmpError = None
    NoResources = None
    PacketTooBig = None
    ParameterProblem = None
    SourceQuench = None
    Success = None
    TimedOut = None
    TimeExceeded = None
    TtlExpired = None
    TtlReassemblyTimeExceeded = None
    Unknown = None
    UnrecognizedNextHeader = None
    value__ = None

class IPv4InterfaceProperties:  # skipped bases: <type 'object'>
    """Provides information about network interfaces that support Internet Protocol version 4 (IPv4)."""

    @property
    def Index(self):
        """
        Gets the index of the network interface associated with the Internet Protocol version 4 (IPv4) address.

        Get: Index(self: IPv4InterfaceProperties) -> int
        """
        ...
    @property
    def IsAutomaticPrivateAddressingActive(self):
        """
        Gets a System.Boolean value that indicates whether this interface has an automatic private IP addressing (APIPA) address.

        Get: IsAutomaticPrivateAddressingActive(self: IPv4InterfaceProperties) -> bool
        """
        ...
    @property
    def IsAutomaticPrivateAddressingEnabled(self):
        """
        Gets a System.Boolean value that indicates whether this interface has automatic private IP addressing (APIPA) enabled.

        Get: IsAutomaticPrivateAddressingEnabled(self: IPv4InterfaceProperties) -> bool
        """
        ...
    @property
    def IsDhcpEnabled(self):
        """
        Gets a System.Boolean value that indicates whether the interface is configured to use a Dynamic Host Configuration Protocol (DHCP) server to obtain an IP address.

        Get: IsDhcpEnabled(self: IPv4InterfaceProperties) -> bool
        """
        ...
    @property
    def IsForwardingEnabled(self):
        """
        Gets a System.Boolean value that indicates whether this interface can forward (route) packets.

        Get: IsForwardingEnabled(self: IPv4InterfaceProperties) -> bool
        """
        ...
    @property
    def Mtu(self):
        """
        Gets the maximum transmission unit (MTU) for this network interface.

        Get: Mtu(self: IPv4InterfaceProperties) -> int
        """
        ...
    @property
    def UsesWins(self):
        """
        Gets a System.Boolean value that indicates whether an interface uses Windows Internet Name Service (WINS).

        Get: UsesWins(self: IPv4InterfaceProperties) -> bool
        """
        ...

class IPv4InterfaceStatistics:  # skipped bases: <type 'object'>
    """Provides statistical data for a network interface on the local computer."""

    @property
    def BytesReceived(self):
        """
        Gets the number of bytes that were received on the interface.

        Get: BytesReceived(self: IPv4InterfaceStatistics) -> Int64
        """
        ...
    @property
    def BytesSent(self):
        """
        Gets the number of bytes that were sent on the interface.

        Get: BytesSent(self: IPv4InterfaceStatistics) -> Int64
        """
        ...
    @property
    def IncomingPacketsDiscarded(self):
        """
        Gets the number of incoming packets that were discarded.

        Get: IncomingPacketsDiscarded(self: IPv4InterfaceStatistics) -> Int64
        """
        ...
    @property
    def IncomingPacketsWithErrors(self):
        """
        Gets the number of incoming packets with errors.

        Get: IncomingPacketsWithErrors(self: IPv4InterfaceStatistics) -> Int64
        """
        ...
    @property
    def IncomingUnknownProtocolPackets(self):
        """
        Gets the number of incoming packets with an unknown protocol that were received on the interface.

        Get: IncomingUnknownProtocolPackets(self: IPv4InterfaceStatistics) -> Int64
        """
        ...
    @property
    def NonUnicastPacketsReceived(self):
        """
        Gets the number of non-unicast packets that were received on the interface.

        Get: NonUnicastPacketsReceived(self: IPv4InterfaceStatistics) -> Int64
        """
        ...
    @property
    def NonUnicastPacketsSent(self):
        """
        Gets the number of non-unicast packets that were sent on the interface.

        Get: NonUnicastPacketsSent(self: IPv4InterfaceStatistics) -> Int64
        """
        ...
    @property
    def OutgoingPacketsDiscarded(self):
        """
        Gets the number of outgoing packets that were discarded.

        Get: OutgoingPacketsDiscarded(self: IPv4InterfaceStatistics) -> Int64
        """
        ...
    @property
    def OutgoingPacketsWithErrors(self):
        """
        Gets the number of outgoing packets with errors.

        Get: OutgoingPacketsWithErrors(self: IPv4InterfaceStatistics) -> Int64
        """
        ...
    @property
    def OutputQueueLength(self):
        """
        Gets the length of the output queue.

        Get: OutputQueueLength(self: IPv4InterfaceStatistics) -> Int64
        """
        ...
    @property
    def UnicastPacketsReceived(self):
        """
        Gets the number of unicast packets that were received on the interface.

        Get: UnicastPacketsReceived(self: IPv4InterfaceStatistics) -> Int64
        """
        ...
    @property
    def UnicastPacketsSent(self):
        """
        Gets the number of unicast packets that were sent on the interface.

        Get: UnicastPacketsSent(self: IPv4InterfaceStatistics) -> Int64
        """
        ...

class IPv6InterfaceProperties:  # skipped bases: <type 'object'>
    """Provides information about network interfaces that support Internet Protocol version 6 (IPv6)."""

    def GetScopeId(self, scopeLevel):
        """
        GetScopeId(self: IPv6InterfaceProperties, scopeLevel: ScopeLevel) -> Int64

            Gets the scope ID of the network interface associated with an Internet Protocol version 6 (IPv6) address.

            scopeLevel: The scope level.

            Returns: Returns System.Int64.The scope ID of the network interface associated with an IPv6 address.
        """
        ...
    @property
    def Index(self):
        """
        Gets the index of the network interface associated with an Internet Protocol version 6 (IPv6) address.

        Get: Index(self: IPv6InterfaceProperties) -> int
        """
        ...
    @property
    def Mtu(self):
        """
        Gets the maximum transmission unit (MTU) for this network interface.

        Get: Mtu(self: IPv6InterfaceProperties) -> int
        """
        ...

class MulticastIPAddressInformation(IPAddressInformation):
    """Provides information about a network interface's multicast address."""

    @property
    def AddressPreferredLifetime(self):
        """
        Gets the number of seconds remaining during which this address is the preferred address.

        Get: AddressPreferredLifetime(self: MulticastIPAddressInformation) -> Int64
        """
        ...
    @property
    def AddressValidLifetime(self):
        """
        Gets the number of seconds remaining during which this address is valid.

        Get: AddressValidLifetime(self: MulticastIPAddressInformation) -> Int64
        """
        ...
    @property
    def DhcpLeaseLifetime(self):
        """
        Specifies the amount of time remaining on the Dynamic Host Configuration Protocol (DHCP) lease for this IP address.

        Get: DhcpLeaseLifetime(self: MulticastIPAddressInformation) -> Int64
        """
        ...
    @property
    def DuplicateAddressDetectionState(self):
        """
        Gets a value that indicates the state of the duplicate address detection algorithm.

        Get: DuplicateAddressDetectionState(self: MulticastIPAddressInformation) -> DuplicateAddressDetectionState
        """
        ...
    @property
    def PrefixOrigin(self):
        """
        Gets a value that identifies the source of a Multicast Internet Protocol (IP) address prefix.

        Get: PrefixOrigin(self: MulticastIPAddressInformation) -> PrefixOrigin
        """
        ...
    @property
    def SuffixOrigin(self):
        """
        Gets a value that identifies the source of a Multicast Internet Protocol (IP) address suffix.

        Get: SuffixOrigin(self: MulticastIPAddressInformation) -> SuffixOrigin
        """
        ...

class MulticastIPAddressInformationCollection(
    object, ICollection[MulticastIPAddressInformation]
):  # skipped bases: <type 'IEnumerable[MulticastIPAddressInformation]'>, <type 'IEnumerable'>
    """Stores a set of System.Net.NetworkInformation.MulticastIPAddressInformation types."""

    def GetEnumerator(self):
        """
        GetEnumerator(self: MulticastIPAddressInformationCollection) -> IEnumerator[MulticastIPAddressInformation]

            Returns an object that can be used to iterate through this collection.

            Returns: An object that implements the System.Collections.IEnumerator interface and provides access to the System.Net.NetworkInformation.UnicastIPAddressInformation types in

             this collection.
        """
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
        Gets the number of System.Net.NetworkInformation.MulticastIPAddressInformation types in this collection.

        Get: Count(self: MulticastIPAddressInformationCollection) -> int
        """
        ...
    @property
    def IsReadOnly(self):
        """
        Gets a value that indicates whether access to this collection is read-only.

        Get: IsReadOnly(self: MulticastIPAddressInformationCollection) -> bool
        """
        ...

class NetBiosNodeType(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies the Network Basic Input/Output System (NetBIOS) node type.

    enum NetBiosNodeType, values: Broadcast (1), Hybrid (8), Mixed (4), Peer2Peer (2), Unknown (0)
    """

    Broadcast = None
    Hybrid = None
    Mixed = None
    Peer2Peer = None
    Unknown = None
    value__ = None

class NetworkAddressChangedEventHandler(
    MulticastDelegate
):  # skipped bases: <type 'ICloneable'>, <type 'ISerializable'>
    """
    References one or more methods to be called when the address of a network interface changes.

    NetworkAddressChangedEventHandler(object: object, method: IntPtr)
    """

    def BeginInvoke(self, sender, e, callback, object):
        """BeginInvoke(self: NetworkAddressChangedEventHandler, sender: object, e: EventArgs, callback: AsyncCallback, object: object) -> IAsyncResult"""
        ...
    def EndInvoke(self, result):
        """EndInvoke(self: NetworkAddressChangedEventHandler, result: IAsyncResult)"""
        ...
    def Invoke(self, sender, e):
        """Invoke(self: NetworkAddressChangedEventHandler, sender: object, e: EventArgs)"""
        ...

class NetworkAvailabilityChangedEventHandler(
    MulticastDelegate
):  # skipped bases: <type 'ICloneable'>, <type 'ISerializable'>
    """
    References one or more methods to be called when the availability of the network changes.

    NetworkAvailabilityChangedEventHandler(object: object, method: IntPtr)
    """

    def BeginInvoke(self, sender, e, callback, object):
        """BeginInvoke(self: NetworkAvailabilityChangedEventHandler, sender: object, e: NetworkAvailabilityEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult"""
        ...
    def EndInvoke(self, result):
        """EndInvoke(self: NetworkAvailabilityChangedEventHandler, result: IAsyncResult)"""
        ...
    def Invoke(self, sender, e):
        """Invoke(self: NetworkAvailabilityChangedEventHandler, sender: object, e: NetworkAvailabilityEventArgs)"""
        ...

class NetworkAvailabilityEventArgs(EventArgs):
    """Provides data for the System.Net.NetworkInformation.NetworkChange.NetworkAvailabilityChanged event."""

    @property
    def IsAvailable(self):
        """
        Gets the current status of the network connection.

        Get: IsAvailable(self: NetworkAvailabilityEventArgs) -> bool
        """
        ...

class NetworkChange:  # skipped bases: <type 'object'>
    """
    Allows applications to receive notification when the Internet Protocol (IP) address of a network interface, also called a network card or adapter, changes.

    NetworkChange()
    """

    @staticmethod
    def RegisterNetworkChange(nc):
        """
        RegisterNetworkChange(nc: NetworkChange)

            Registers a network change instance to receive network change events.

            nc: The instance to register.
        """
        ...
    NetworkAddressChanged = None
    NetworkAvailabilityChanged = None

class NetworkInformationAccess(
    Enum
):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies permission to access information about network interfaces and traffic statistics.

    enum (flags) NetworkInformationAccess, values: None (0), Ping (4), Read (1)
    """

    Ping = None
    Read = None
    value__ = None

class NetworkInformationException(Win32Exception):  # skipped bases: <type '_Exception'>, <type 'ISerializable'>
    """
    The exception that is thrown when an error occurs while retrieving network information.

    NetworkInformationException()

    NetworkInformationException(errorCode: int)
    """

    @property
    def ErrorCode(self):
        """
        Gets the n32 error code for this exception.

        Get: ErrorCode(self: NetworkInformationException) -> int
        """
        ...
    SerializeObjectState = None

class NetworkInformationPermission(
    CodeAccessPermission, IUnrestrictedPermission
):  # skipped bases: <type 'ISecurityEncodable'>, <type 'IPermission'>, <type 'IStackWalk'>
    """
    Controls access to network information and traffic statistics for the local computer. This class cannot be inherited.

    NetworkInformationPermission(state: PermissionState)

    NetworkInformationPermission(access: NetworkInformationAccess)
    """

    def AddPermission(self, access):
        """
        AddPermission(self: NetworkInformationPermission, access: NetworkInformationAccess)

            Adds the specified value to this permission.

            access: One of the System.Net.NetworkInformation.NetworkInformationAccess values.
        """
        ...
    @staticmethod  # known case of __new__
    def __new__(cls, *__args):
        """
        __new__(cls: type, state: PermissionState)

        __new__(cls: type, access: NetworkInformationAccess)
        """
        ...
    @property
    def Access(self):
        """
        Gets the level of access to network information controlled by this permission.

        Get: Access(self: NetworkInformationPermission) -> NetworkInformationAccess
        """
        ...

class NetworkInformationPermissionAttribute(CodeAccessSecurityAttribute):  # skipped bases: <type '_Attribute'>
    """
    Allows security actions for System.Net.NetworkInformation.NetworkInformationPermission to be applied to code using declarative security.

    NetworkInformationPermissionAttribute(action: SecurityAction)
    """

    def CreatePermission(self):
        """
        CreatePermission(self: NetworkInformationPermissionAttribute) -> IPermission

            Creates and returns a new System.Net.NetworkInformation.NetworkInformationPermission object.

            Returns: A System.Net.NetworkInformation.NetworkInformationPermission that corresponds to this attribute.
        """
        ...
    @property
    def Access(self):
        """
        Gets or sets the network information access level.

        Get: Access(self: NetworkInformationPermissionAttribute) -> str

        Set: Access(self: NetworkInformationPermissionAttribute) = value
        """
        ...

class NetworkInterface:  # skipped bases: <type 'object'>
    """Provides configuration and statistical information for a network interface."""

    @staticmethod
    def GetAllNetworkInterfaces():
        """
        GetAllNetworkInterfaces() -> Array[NetworkInterface]

            Returns objects that describe the network interfaces on the local computer.

            Returns: A System.Net.NetworkInformation.NetworkInterface array that contains objects that describe the available network interfaces, or an empty array if no interfaces are

             detected.
        """
        ...
    def GetIPProperties(self):
        """
        GetIPProperties(self: NetworkInterface) -> IPInterfaceProperties

            Returns an object that describes the configuration of this network interface.

            Returns: An System.Net.NetworkInformation.IPInterfaceProperties object that describes this network interface.
        """
        ...
    def GetIPStatistics(self):
        """
        GetIPStatistics(self: NetworkInterface) -> IPInterfaceStatistics

            Gets the IP statistics for this System.Net.NetworkInformation.NetworkInterface instance.

            Returns: Returns System.Net.NetworkInformation.IPInterfaceStatistics.The IP statistics.
        """
        ...
    def GetIPv4Statistics(self):
        """
        GetIPv4Statistics(self: NetworkInterface) -> IPv4InterfaceStatistics

            Gets the IPv4 statistics for this System.Net.NetworkInformation.NetworkInterface instance.

            Returns: An System.Net.NetworkInformation.IPv4InterfaceStatistics object.
        """
        ...
    @staticmethod
    def GetIsNetworkAvailable():
        """
        GetIsNetworkAvailable() -> bool

            Indicates whether any network connection is available.

            Returns: ue if a network connection is available; otherwise, lse.
        """
        ...
    def GetPhysicalAddress(self):
        """
        GetPhysicalAddress(self: NetworkInterface) -> PhysicalAddress

            Returns the Media Access Control (MAC) or physical address for this adapter.

            Returns: A System.Net.NetworkInformation.PhysicalAddress object that contains the physical address.
        """
        ...
    def Supports(self, networkInterfaceComponent):
        """
        Supports(self: NetworkInterface, networkInterfaceComponent: NetworkInterfaceComponent) -> bool

            Gets a System.Boolean value that indicates whether the interface supports the specified protocol.

            networkInterfaceComponent: A System.Net.NetworkInformation.NetworkInterfaceComponent value.

            Returns: ue if the specified protocol is supported; otherwise, lse.
        """
        ...
    @property
    def Description(self):
        """
        Gets the description of the interface.

        Get: Description(self: NetworkInterface) -> str
        """
        ...
    @property
    def Id(self):
        """
        Gets the identifier of the network adapter.

        Get: Id(self: NetworkInterface) -> str
        """
        ...
    @property
    def IsReceiveOnly(self):
        """
        Gets a System.Boolean value that indicates whether the network interface is set to only receive data packets.

        Get: IsReceiveOnly(self: NetworkInterface) -> bool
        """
        ...
    @property
    def Name(self):
        """
        Gets the name of the network adapter.

        Get: Name(self: NetworkInterface) -> str
        """
        ...
    @property
    def NetworkInterfaceType(self):
        """
        Gets the interface type.

        Get: NetworkInterfaceType(self: NetworkInterface) -> NetworkInterfaceType
        """
        ...
    @property
    def OperationalStatus(self):
        """
        Gets the current operational state of the network connection.

        Get: OperationalStatus(self: NetworkInterface) -> OperationalStatus
        """
        ...
    @property
    def Speed(self):
        """
        Gets the speed of the network interface.

        Get: Speed(self: NetworkInterface) -> Int64
        """
        ...
    @property
    def SupportsMulticast(self):
        """
        Gets a System.Boolean value that indicates whether the network interface is enabled to receive multicast packets.

        Get: SupportsMulticast(self: NetworkInterface) -> bool
        """
        ...
    IPv6LoopbackInterfaceIndex = 1
    LoopbackInterfaceIndex = 1

class NetworkInterfaceComponent(
    Enum
):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies the Internet Protocol versions that are supported by a network interface.

    enum NetworkInterfaceComponent, values: IPv4 (0), IPv6 (1)
    """

    IPv4 = None
    IPv6 = None
    value__ = None

class NetworkInterfaceType(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies types of network interfaces.

    enum NetworkInterfaceType, values: AsymmetricDsl (94), Atm (37), BasicIsdn (20), Ethernet (6), Ethernet3Megabit (26), FastEthernetFx (69), FastEthernetT (62), Fddi (15), GenericModem (48), GigabitEthernet (117), HighPerformanceSerialBus (144), IPOverAtm (114), Isdn (63), Loopback (24), MultiRateSymmetricDsl (143), Ppp (23), PrimaryIsdn (21), RateAdaptDsl (95), Slip (28), SymmetricDsl (96), TokenRing (9), Tunnel (131), Unknown (1), VeryHighSpeedDsl (97), Wireless80211 (71), Wman (237), Wwanpp (243), Wwanpp2 (244)
    """

    AsymmetricDsl = None
    Atm = None
    BasicIsdn = None
    Ethernet = None
    Ethernet3Megabit = None
    FastEthernetFx = None
    FastEthernetT = None
    Fddi = None
    GenericModem = None
    GigabitEthernet = None
    HighPerformanceSerialBus = None
    IPOverAtm = None
    Isdn = None
    Loopback = None
    MultiRateSymmetricDsl = None
    Ppp = None
    PrimaryIsdn = None
    RateAdaptDsl = None
    Slip = None
    SymmetricDsl = None
    TokenRing = None
    Tunnel = None
    Unknown = None
    value__ = None
    VeryHighSpeedDsl = None
    Wireless80211 = None
    Wman = None
    Wwanpp = None
    Wwanpp2 = None

class OperationalStatus(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies the operational state of a network interface.

    enum OperationalStatus, values: Dormant (5), Down (2), LowerLayerDown (7), NotPresent (6), Testing (3), Unknown (4), Up (1)
    """

    Dormant = None
    Down = None
    LowerLayerDown = None
    NotPresent = None
    Testing = None
    Unknown = None
    Up = None
    value__ = None

class PhysicalAddress:  # skipped bases: <type 'object'>
    """
    Provides the Media Access Control (MAC) address for a network interface (adapter).

    PhysicalAddress(address: Array[Byte])
    """

    def Equals(self, comparand):
        """
        Equals(self: PhysicalAddress, comparand: object) -> bool

            Compares two System.Net.NetworkInformation.PhysicalAddress instances.

            comparand: The System.Net.NetworkInformation.PhysicalAddress  to compare to the current instance.

            Returns: ue if this instance and the specified instance contain the same address; otherwise lse.
        """
        ...
    def GetAddressBytes(self):
        """
        GetAddressBytes(self: PhysicalAddress) -> Array[Byte]

            Returns the address of the current instance.

            Returns: A System.Byte array containing the address.
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: PhysicalAddress) -> int

            Returns the hash value of a physical address.

            Returns: An integer hash value.
        """
        ...
    @staticmethod
    def Parse(address):
        """
        Parse(address: str) -> PhysicalAddress

            Parses the specified System.String and stores its contents as the address bytes of the System.Net.NetworkInformation.PhysicalAddress returned by this method.

            address: A System.String containing the address that will be used to initialize the System.Net.NetworkInformation.PhysicalAddress instance returned by this method.

            Returns: A System.Net.NetworkInformation.PhysicalAddress instance with the specified address.
        """
        ...
    def ToString(self):
        """
        ToString(self: PhysicalAddress) -> str

            Returns the System.String representation of the address of this instance.

            Returns: A System.String containing the address contained in this instance.
        """
        ...
    def __eq__(self, *args):  # cannot find CLR method
        """x.__eq__(y) <==> x==y"""
        ...
    def __ne__(self, *args): ...

class Ping(Component):  # skipped bases: <type 'IComponent'>, <type 'IDisposable'>
    """
    Allows an application to determine whether a remote computer is accessible over the network.

    Ping()
    """

    def OnPingCompleted(self, *args):  # cannot find CLR method
        """
        OnPingCompleted(self: Ping, e: PingCompletedEventArgs)

            Raises the System.Net.NetworkInformation.Ping.PingCompleted event.

            e: A System.Net.NetworkInformation.PingCompletedEventArgs  object that contains event data.
        """
        ...
    def Send(self, *__args):
        """
        Send(self: Ping, hostNameOrAddress: str) -> PingReply

            Attempts to send an Internet Control Message Protocol (ICMP) echo message to the specified computer, and receive a corresponding ICMP echo reply message from that

             computer.

            hostNameOrAddress: A System.String that identifies the computer that is the destination for the ICMP echo message. The value specified for this parameter can be a host name or a string

             representation of an IP address.

            Returns: A System.Net.NetworkInformation.PingReply object that provides information about the ICMP echo reply message, if one was received, or provides the reason for the

             failure, if no message was received.

        Send(self: Ping, hostNameOrAddress: str, timeout: int) -> PingReply

            Attempts to send an Internet Control Message Protocol (ICMP) echo message to the specified computer, and receive a corresponding ICMP echo reply message from that

             computer. This method allows you to specify a time-out value for the operation.

            hostNameOrAddress: A System.String that identifies the computer that is the destination for the ICMP echo message. The value specified for this parameter can be a host name or a string

             representation of an IP address.

            timeout: An System.Int32 value that specifies the maximum number of milliseconds (after sending the echo message) to wait for the ICMP echo reply message.

            Returns: A System.Net.NetworkInformation.PingReply object that provides information about the ICMP echo reply message if one was received, or provides the reason for the

             failure if no message was received.

        Send(self: Ping, address: IPAddress) -> PingReply

            Attempts to send an Internet Control Message Protocol (ICMP) echo message to the computer that has the specified System.Net.IPAddress, and receive a corresponding ICMP

             echo reply message from that computer.

            address: An System.Net.IPAddress that identifies the computer that is the destination for the ICMP echo message.

            Returns: A System.Net.NetworkInformation.PingReply object that provides information about the ICMP echo reply message, if one was received, or describes the reason for the

             failure if no message was received.

        Send(self: Ping, address: IPAddress, timeout: int) -> PingReply

            Attempts to send an Internet Control Message Protocol (ICMP) echo message with the specified data buffer to the computer that has the specified System.Net.IPAddress,

             and receive a corresponding ICMP echo reply message from that computer. This method allows you to specify a time-out value for the operation.

            address: An System.Net.IPAddress that identifies the computer that is the destination for the ICMP echo message.

            timeout: An System.Int32 value that specifies the maximum number of milliseconds (after sending the echo message) to wait for the ICMP echo reply message.

            Returns: A System.Net.NetworkInformation.PingReply object that provides information about the ICMP echo reply message if one was received, or provides the reason for the

             failure if no message was received.

        Send(self: Ping, hostNameOrAddress: str, timeout: int, buffer: Array[Byte]) -> PingReply

            Attempts to send an Internet Control Message Protocol (ICMP) echo message with the specified data buffer to the specified computer, and receive a corresponding ICMP

             echo reply message from that computer. This overload allows you to specify a time-out value for the operation.

            hostNameOrAddress: A System.String that identifies the computer that is the destination for the ICMP echo message. The value specified for this parameter can be a host name or a string

             representation of an IP address.

            timeout: An System.Int32 value that specifies the maximum number of milliseconds (after sending the echo message) to wait for the ICMP echo reply message.

            buffer: A System.Byte array that contains data to be sent with the ICMP echo message and returned in the ICMP echo reply message. The array cannot contain more than 65,500

             bytes.

            Returns: A System.Net.NetworkInformation.PingReply object that provides information about the ICMP echo reply message if one was received, or provides the reason for the

             failure if no message was received.

        Send(self: Ping, address: IPAddress, timeout: int, buffer: Array[Byte]) -> PingReply

            Attempts to send an Internet Control Message Protocol (ICMP) echo message with the specified data buffer to the computer that has the specified System.Net.IPAddress,

             and receive a corresponding ICMP echo reply message from that computer. This overload allows you to specify a time-out value for the operation.

            address: An System.Net.IPAddress that identifies the computer that is the destination for the ICMP echo message.

            timeout: An System.Int32 value that specifies the maximum number of milliseconds (after sending the echo message) to wait for the ICMP echo reply message.

            buffer: A System.Byte array that contains data to be sent with the ICMP echo message and returned in the ICMP echo reply message. The array cannot contain more than 65,500

             bytes.

            Returns: A System.Net.NetworkInformation.PingReply object that provides information about the ICMP echo reply message, if one was received, or provides the reason for the

             failure, if no message was received. The method will return System.Net.NetworkInformation.IPStatus.PacketTooBig if the packet exceeds the Maximum Transmission Unit

             (MTU).

        Send(self: Ping, hostNameOrAddress: str, timeout: int, buffer: Array[Byte], options: PingOptions) -> PingReply

            Attempts to send an Internet Control Message Protocol (ICMP) echo message with the specified data buffer to the specified computer, and receive a corresponding ICMP

             echo reply message from that computer. This overload allows you to specify a time-out value for the operation and control fragmentation and Time-to-Live values for the

             ICMP packet.

            hostNameOrAddress: A System.String that identifies the computer that is the destination for the ICMP echo message. The value specified for this parameter can be a host name or a string

             representation of an IP address.

            timeout: An System.Int32 value that specifies the maximum number of milliseconds (after sending the echo message) to wait for the ICMP echo reply message.

            buffer: A System.Byte array that contains data to be sent with the ICMP echo message and returned in the ICMP echo reply message. The array cannot contain more than 65,500

             bytes.

            options: A System.Net.NetworkInformation.PingOptions  object used to control fragmentation and Time-to-Live values for the ICMP echo message packet.

            Returns: A System.Net.NetworkInformation.PingReply object that provides information about the ICMP echo reply message if one was received, or provides the reason for the

             failure if no message was received.

        Send(self: Ping, address: IPAddress, timeout: int, buffer: Array[Byte], options: PingOptions) -> PingReply

            Attempts to send an Internet Control Message Protocol (ICMP) echo message with the specified data buffer to the computer that has the specified System.Net.IPAddress

             and receive a corresponding ICMP echo reply message from that computer. This overload allows you to specify a time-out value for the operation and control

             fragmentation and Time-to-Live values for the ICMP echo message packet.

            address: An System.Net.IPAddress that identifies the computer that is the destination for the ICMP echo message.

            timeout: An System.Int32 value that specifies the maximum number of milliseconds (after sending the echo message) to wait for the ICMP echo reply message.

            buffer: A System.Byte array that contains data to be sent with the ICMP echo message and returned in the ICMP echo reply message. The array cannot contain more than 65,500

             bytes.

            options: A System.Net.NetworkInformation.PingOptions  object used to control fragmentation and Time-to-Live values for the ICMP echo message packet.

            Returns: A System.Net.NetworkInformation.PingReply object that provides information about the ICMP echo reply message, if one was received, or provides the reason for the

             failure, if no message was received. The method will return System.Net.NetworkInformation.IPStatus.PacketTooBig if the packet exceeds the Maximum Transmission Unit

             (MTU).
        """
        ...
    def SendAsync(self, *__args):
        """
        SendAsync(self: Ping, hostNameOrAddress: str, userToken: object)

            Asynchronously attempts to send an Internet Control Message Protocol (ICMP) echo message to the specified computer, and receive a corresponding ICMP echo reply message

             from that computer.

            hostNameOrAddress: A System.String that identifies the computer that is the destination for the ICMP echo message. The value specified for this parameter can be a host name or a string

             representation of an IP address.

            userToken: An object that is passed to the method invoked when the asynchronous operation completes.

        SendAsync(self: Ping, hostNameOrAddress: str, timeout: int, userToken: object)

            Asynchronously attempts to send an Internet Control Message Protocol (ICMP) echo message to the specified computer, and receive a corresponding ICMP echo reply message

             from that computer. This overload allows you to specify a time-out value for the operation.

            hostNameOrAddress: A System.String that identifies the computer that is the destination for the ICMP echo message. The value specified for this parameter can be a host name or a string

             representation of an IP address.

            timeout: An System.Int32 value that specifies the maximum number of milliseconds (after sending the echo message) to wait for the ICMP echo reply message.

            userToken: An object that is passed to the method invoked when the asynchronous operation completes.

        SendAsync(self: Ping, address: IPAddress, userToken: object)

            Asynchronously attempts to send an Internet Control Message Protocol (ICMP) echo message to the computer that has the specified System.Net.IPAddress, and receive a

             corresponding ICMP echo reply message from that computer.

            address: An System.Net.IPAddress that identifies the computer that is the destination for the ICMP echo message.

            userToken: An object that is passed to the method invoked when the asynchronous operation completes.

        SendAsync(self: Ping, address: IPAddress, timeout: int, userToken: object)

            Asynchronously attempts to send an Internet Control Message Protocol (ICMP) echo message to the computer that has the specified System.Net.IPAddress, and receive a

             corresponding ICMP echo reply message from that computer. This overload allows you to specify a time-out value for the operation.

            address: An System.Net.IPAddress that identifies the computer that is the destination for the ICMP echo message.

            timeout: An System.Int32 value that specifies the maximum number of milliseconds (after sending the echo message) to wait for the ICMP echo reply message.

            userToken: An object that is passed to the method invoked when the asynchronous operation completes.

        SendAsync(self: Ping, hostNameOrAddress: str, timeout: int, buffer: Array[Byte], userToken: object)

            Asynchronously attempts to send an Internet Control Message Protocol (ICMP) echo message with the specified data buffer to the specified computer, and receive a

             corresponding ICMP echo reply message from that computer. This overload allows you to specify a time-out value for the operation.

            hostNameOrAddress: A System.String that identifies the computer that is the destination for the ICMP echo message. The value specified for this parameter can be a host name or a string

             representation of an IP address.

            timeout: An System.Int32 value that specifies the maximum number of milliseconds (after sending the echo message) to wait for the ICMP echo reply message.

            buffer: A System.Byte array that contains data to be sent with the ICMP echo message and returned in the ICMP echo reply message. The array cannot contain more than 65,500

             bytes.

            userToken: An object that is passed to the method invoked when the asynchronous operation completes.

        SendAsync(self: Ping, address: IPAddress, timeout: int, buffer: Array[Byte], userToken: object)

            Asynchronously attempts to send an Internet Control Message Protocol (ICMP) echo message with the specified data buffer to the computer that has the specified

             System.Net.IPAddress, and receive a corresponding ICMP echo reply message from that computer. This overload allows you to specify a time-out value for the operation.

            address: An System.Net.IPAddress that identifies the computer that is the destination for the ICMP echo message.

            timeout: An System.Int32 value that specifies the maximum number of milliseconds (after sending the echo message) to wait for the ICMP echo reply message.

            buffer: A System.Byte array that contains data to be sent with the ICMP echo message and returned in the ICMP echo reply message. The array cannot contain more than 65,500

             bytes.

            userToken: An object that is passed to the method invoked when the asynchronous operation completes.

        SendAsync(self: Ping, hostNameOrAddress: str, timeout: int, buffer: Array[Byte], options: PingOptions, userToken: object)

            Asynchronously attempts to send an Internet Control Message Protocol (ICMP) echo message with the specified data buffer to the specified computer, and receive a

             corresponding ICMP echo reply message from that computer. This overload allows you to specify a time-out value for the operation and control fragmentation and

             Time-to-Live values for the ICMP packet.

            hostNameOrAddress: A System.String that identifies the computer that is the destination for the ICMP echo message. The value specified for this parameter can be a host name or a string

             representation of an IP address.

            timeout: A System.Byte array that contains data to be sent with the ICMP echo message and returned in the ICMP echo reply message. The array cannot contain more than 65,500

             bytes.

            buffer: An System.Int32 value that specifies the maximum number of milliseconds (after sending the echo message) to wait for the ICMP echo reply message.

            options: A System.Net.NetworkInformation.PingOptions  object used to control fragmentation and Time-to-Live values for the ICMP echo message packet.

            userToken: An object that is passed to the method invoked when the asynchronous operation completes.

        SendAsync(self: Ping, address: IPAddress, timeout: int, buffer: Array[Byte], options: PingOptions, userToken: object)

            Asynchronously attempts to send an Internet Control Message Protocol (ICMP) echo message with the specified data buffer to the computer that has the specified

             System.Net.IPAddress, and receive a corresponding ICMP echo reply message from that computer. This overload allows you to specify a time-out value for the operation

             and control fragmentation and Time-to-Live values for the ICMP echo message packet.

            address: An System.Net.IPAddress that identifies the computer that is the destination for the ICMP echo message.

            timeout: An System.Int32 value that specifies the maximum number of milliseconds (after sending the echo message) to wait for the ICMP echo reply message.

            buffer: A System.Byte array that contains data to be sent with the ICMP echo message and returned in the ICMP echo reply message. The array cannot contain more than 65,500

             bytes.

            options: A System.Net.NetworkInformation.PingOptions  object used to control fragmentation and Time-to-Live values for the ICMP echo message packet.

            userToken: An object that is passed to the method invoked when the asynchronous operation completes.
        """
        ...
    def SendAsyncCancel(self):
        """
        SendAsyncCancel(self: Ping)

            Cancels all pending asynchronous requests to send an Internet Control Message Protocol (ICMP) echo message and receives a corresponding ICMP echo reply message.
        """
        ...
    def SendPingAsync(self, *__args):
        """
        SendPingAsync(self: Ping, address: IPAddress) -> Task[PingReply]

            Send an Internet Control Message Protocol (ICMP) echo message with the specified data buffer to the computer that has the specified System.Net.IPAddress, and receives

             a corresponding ICMP echo reply message from that computer as an asynchronous operation.

            address: An IP address that identifies the computer that is the destination for the ICMP echo message.

            Returns: Returns System.Threading.Tasks.Task.The task object representing the asynchronous operation.

        SendPingAsync(self: Ping, hostNameOrAddress: str) -> Task[PingReply]

            Sends an Internet Control Message Protocol (ICMP) echo message with the specified data buffer to the specified computer, and receive a corresponding ICMP echo reply

             message from that computer as an asynchronous operation.

            hostNameOrAddress: The computer that is the destination for the ICMP echo message. The value specified for this parameter can be a host name or a string representation of an IP address.

            Returns: Returns System.Threading.Tasks.Task.The task object representing the asynchronous operation.

        SendPingAsync(self: Ping, address: IPAddress, timeout: int) -> Task[PingReply]

            Send an Internet Control Message Protocol (ICMP) echo message with the specified data buffer to the computer that has the specified System.Net.IPAddress, and receives

             a corresponding ICMP echo reply message from that computer as an asynchronous operation. This overload allows you to specify a time-out value for the operation.

            address: An IP address that identifies the computer that is the destination for the ICMP echo message.

            timeout: The maximum number of milliseconds (after sending the echo message) to wait for the ICMP echo reply message.

            Returns: Returns System.Threading.Tasks.Task.The task object representing the asynchronous operation.

        SendPingAsync(self: Ping, hostNameOrAddress: str, timeout: int) -> Task[PingReply]

            Sends an Internet Control Message Protocol (ICMP) echo message with the specified data buffer to the specified computer, and receive a corresponding ICMP echo reply

             message from that computer as an asynchronous operation. This overload allows you to specify a time-out value for the operation.

            hostNameOrAddress: The computer that is the destination for the ICMP echo message. The value specified for this parameter can be a host name or a string representation of an IP address.

            timeout: The maximum number of milliseconds (after sending the echo message) to wait for the ICMP echo reply message.

            Returns: Returns System.Threading.Tasks.Task.The task object representing the asynchronous operation.

        SendPingAsync(self: Ping, address: IPAddress, timeout: int, buffer: Array[Byte]) -> Task[PingReply]

            Send an Internet Control Message Protocol (ICMP) echo message with the specified data buffer to the computer that has the specified System.Net.IPAddress, and receives

             a corresponding ICMP echo reply message from that computer as an asynchronous operation. This overload allows you to specify a time-out value for the operation and a

             buffer to use for send and receive.

            address: An IP address that identifies the computer that is the destination for the ICMP echo message.

            timeout: The maximum number of milliseconds (after sending the echo message) to wait for the ICMP echo reply message.

            buffer: A System.Byte array that contains data to be sent with the ICMP echo message and returned in the ICMP echo reply message. The array cannot contain more than 65,500

             bytes.

            Returns: Returns System.Threading.Tasks.Task.The task object representing the asynchronous operation.

        SendPingAsync(self: Ping, hostNameOrAddress: str, timeout: int, buffer: Array[Byte]) -> Task[PingReply]

            Sends an Internet Control Message Protocol (ICMP) echo message with the specified data buffer to the specified computer, and receive a corresponding ICMP echo reply

             message from that computer as an asynchronous operation. This overload allows you to specify a time-out value for the operation and a buffer to use for send and

             receive.

            hostNameOrAddress: The computer that is the destination for the ICMP echo message. The value specified for this parameter can be a host name or a string representation of an IP address.

            timeout: The maximum number of milliseconds (after sending the echo message) to wait for the ICMP echo reply message.

            buffer: A System.Byte array that contains data to be sent with the ICMP echo message and returned in the ICMP echo reply message. The array cannot contain more than 65,500

             bytes.

            Returns: Returns System.Threading.Tasks.Task.The task object representing the asynchronous operation.

        SendPingAsync(self: Ping, address: IPAddress, timeout: int, buffer: Array[Byte], options: PingOptions) -> Task[PingReply]

            Send an Internet Control Message Protocol (ICMP) echo message with the specified data buffer to the computer that has the specified System.Net.IPAddress, and receives

             a corresponding ICMP echo reply message from that computer as an asynchronous operation. This overload allows you to specify a time-out value for the operation, a

             buffer to use for send and receive, and control fragmentation and Time-to-Live values for the ICMP echo message packet.

            address: An IP address that identifies the computer that is the destination for the ICMP echo message.

            timeout: The maximum number of milliseconds (after sending the echo message) to wait for the ICMP echo reply message.

            buffer: A System.Byte array that contains data to be sent with the ICMP echo message and returned in the ICMP echo reply message. The array cannot contain more than 65,500

             bytes.

            options: A System.Net.NetworkInformation.PingOptions  object used to control fragmentation and Time-to-Live values for the ICMP echo message packet.

            Returns: Returns System.Threading.Tasks.Task.The task object representing the asynchronous operation.

        SendPingAsync(self: Ping, hostNameOrAddress: str, timeout: int, buffer: Array[Byte], options: PingOptions) -> Task[PingReply]

            Sends an Internet Control Message Protocol (ICMP) echo message with the specified data buffer to the specified computer, and receive a corresponding ICMP echo reply

             message from that computer as an asynchronous operation. This overload allows you to specify a time-out value for the operation, a buffer to use for send and receive,

             and control fragmentation and Time-to-Live values for the ICMP echo message packet.

            hostNameOrAddress: The computer that is the destination for the ICMP echo message. The value specified for this parameter can be a host name or a string representation of an IP address.

            timeout: The maximum number of milliseconds (after sending the echo message) to wait for the ICMP echo reply message.

            buffer: A System.Byte array that contains data to be sent with the ICMP echo message and returned in the ICMP echo reply message. The array cannot contain more than 65,500

             bytes.

            options: A System.Net.NetworkInformation.PingOptions  object used to control fragmentation and Time-to-Live values for the ICMP echo message packet.

            Returns: Returns System.Threading.Tasks.Task.The task object representing the asynchronous operation.
        """
        ...
    @property
    def CanRaiseEvents(self):
        """Gets a value indicating whether the component can raise an event."""
        ...
    @property
    def DesignMode(self):
        """Gets a value that indicates whether the System.ComponentModel.Component is currently in design mode."""
        ...
    @property
    def Events(self):
        """Gets the list of event handlers that are attached to this System.ComponentModel.Component."""
        ...
    PingCompleted = None

class PingCompletedEventArgs(AsyncCompletedEventArgs):
    """Provides data for the System.Net.NetworkInformation.Ping.PingCompleted event."""

    @property
    def Reply(self):
        """
        Gets an object that contains data that describes an attempt to send an Internet Control Message Protocol (ICMP) echo request message and receive a corresponding ICMP echo reply message.

        Get: Reply(self: PingCompletedEventArgs) -> PingReply
        """
        ...

class PingCompletedEventHandler(MulticastDelegate):  # skipped bases: <type 'ICloneable'>, <type 'ISerializable'>
    """
    Represents the method that will handle the System.Net.NetworkInformation.Ping.PingCompleted event of a System.Net.NetworkInformation.Ping object.

    PingCompletedEventHandler(object: object, method: IntPtr)
    """

    def BeginInvoke(self, sender, e, callback, object):
        """BeginInvoke(self: PingCompletedEventHandler, sender: object, e: PingCompletedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult"""
        ...
    def EndInvoke(self, result):
        """EndInvoke(self: PingCompletedEventHandler, result: IAsyncResult)"""
        ...
    def Invoke(self, sender, e):
        """Invoke(self: PingCompletedEventHandler, sender: object, e: PingCompletedEventArgs)"""
        ...

class PingException(InvalidOperationException):  # skipped bases: <type '_Exception'>, <type 'ISerializable'>
    """
    The exception that is thrown when a erload:System.Net.NetworkInformation.Ping.Send or erload:System.Net.NetworkInformation.Ping.SendAsync method calls a method that throws an exception.

    PingException(message: str)

    PingException(message: str, innerException: Exception)
    """

    SerializeObjectState = None

class PingOptions:  # skipped bases: <type 'object'>
    """
    Used to control how System.Net.NetworkInformation.Ping data packets are transmitted.

    PingOptions(ttl: int, dontFragment: bool)

    PingOptions()
    """

    @property
    def DontFragment(self):
        """
        Gets or sets a System.Boolean value that controls fragmentation of the data sent to the remote host.

        Get: DontFragment(self: PingOptions) -> bool

        Set: DontFragment(self: PingOptions) = value
        """
        ...
    @property
    def Ttl(self):
        """
        Gets or sets the number of routing nodes that can forward the System.Net.NetworkInformation.Ping data before it is discarded.

        Get: Ttl(self: PingOptions) -> int

        Set: Ttl(self: PingOptions) = value
        """
        ...

class PingReply:  # skipped bases: <type 'object'>
    """Provides information about the status and data resulting from a erload:System.Net.NetworkInformation.Ping.Send or erload:System.Net.NetworkInformation.Ping.SendAsync operation."""

    @property
    def Address(self):
        """
        Gets the address of the host that sends the Internet Control Message Protocol (ICMP) echo reply.

        Get: Address(self: PingReply) -> IPAddress
        """
        ...
    @property
    def Buffer(self):
        """
        Gets the buffer of data received in an Internet Control Message Protocol (ICMP) echo reply message.

        Get: Buffer(self: PingReply) -> Array[Byte]
        """
        ...
    @property
    def Options(self):
        """
        Gets the options used to transmit the reply to an Internet Control Message Protocol (ICMP) echo request.

        Get: Options(self: PingReply) -> PingOptions
        """
        ...
    @property
    def RoundtripTime(self):
        """
        Gets the number of milliseconds taken to send an Internet Control Message Protocol (ICMP) echo request and receive the corresponding ICMP echo reply message.

        Get: RoundtripTime(self: PingReply) -> Int64
        """
        ...
    @property
    def Status(self):
        """
        Gets the status of an attempt to send an Internet Control Message Protocol (ICMP) echo request and receive the corresponding ICMP echo reply message.

        Get: Status(self: PingReply) -> IPStatus
        """
        ...

class PrefixOrigin(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies how an IP address network prefix was located.

    enum PrefixOrigin, values: Dhcp (3), Manual (1), Other (0), RouterAdvertisement (4), WellKnown (2)
    """

    Dhcp = None
    Manual = None
    Other = None
    RouterAdvertisement = None
    value__ = None
    WellKnown = None

class ScopeLevel(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    The scope level for an IPv6 address.

    enum ScopeLevel, values: Admin (4), Global (14), Interface (1), Link (2), None (0), Organization (8), Site (5), Subnet (3)
    """

    Admin = None
    Global = None
    Interface = None
    Link = None

    Organization = None
    Site = None
    Subnet = None
    value__ = None

class SuffixOrigin(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies how an IP address host suffix was located.

    enum SuffixOrigin, values: LinkLayerAddress (4), Manual (1), OriginDhcp (3), Other (0), Random (5), WellKnown (2)
    """

    LinkLayerAddress = None
    Manual = None
    OriginDhcp = None
    Other = None
    Random = None
    value__ = None
    WellKnown = None

class TcpConnectionInformation:  # skipped bases: <type 'object'>
    """Provides information about the Transmission Control Protocol (TCP) connections on the local computer."""

    @property
    def LocalEndPoint(self):
        """
        Gets the local endpoint of a Transmission Control Protocol (TCP) connection.

        Get: LocalEndPoint(self: TcpConnectionInformation) -> IPEndPoint
        """
        ...
    @property
    def RemoteEndPoint(self):
        """
        Gets the remote endpoint of a Transmission Control Protocol (TCP) connection.

        Get: RemoteEndPoint(self: TcpConnectionInformation) -> IPEndPoint
        """
        ...
    @property
    def State(self):
        """
        Gets the state of this Transmission Control Protocol (TCP) connection.

        Get: State(self: TcpConnectionInformation) -> TcpState
        """
        ...

class TcpState(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies the states of a Transmission Control Protocol (TCP) connection.

    enum TcpState, values: Closed (1), CloseWait (8), Closing (9), DeleteTcb (12), Established (5), FinWait1 (6), FinWait2 (7), LastAck (10), Listen (2), SynReceived (4), SynSent (3), TimeWait (11), Unknown (0)
    """

    Closed = None
    CloseWait = None
    Closing = None
    DeleteTcb = None
    Established = None
    FinWait1 = None
    FinWait2 = None
    LastAck = None
    Listen = None
    SynReceived = None
    SynSent = None
    TimeWait = None
    Unknown = None
    value__ = None

class TcpStatistics:  # skipped bases: <type 'object'>
    """Provides Transmission Control Protocol (TCP) statistical data."""

    @property
    def ConnectionsAccepted(self):
        """
        Gets the number of accepted Transmission Control Protocol (TCP) connection requests.

        Get: ConnectionsAccepted(self: TcpStatistics) -> Int64
        """
        ...
    @property
    def ConnectionsInitiated(self):
        """
        Gets the number of Transmission Control Protocol (TCP) connection requests made by clients.

        Get: ConnectionsInitiated(self: TcpStatistics) -> Int64
        """
        ...
    @property
    def CumulativeConnections(self):
        """
        Specifies the total number of Transmission Control Protocol (TCP) connections established.

        Get: CumulativeConnections(self: TcpStatistics) -> Int64
        """
        ...
    @property
    def CurrentConnections(self):
        """
        Gets the number of current Transmission Control Protocol (TCP) connections.

        Get: CurrentConnections(self: TcpStatistics) -> Int64
        """
        ...
    @property
    def ErrorsReceived(self):
        """
        Gets the number of Transmission Control Protocol (TCP) errors received.

        Get: ErrorsReceived(self: TcpStatistics) -> Int64
        """
        ...
    @property
    def FailedConnectionAttempts(self):
        """
        Gets the number of failed Transmission Control Protocol (TCP) connection attempts.

        Get: FailedConnectionAttempts(self: TcpStatistics) -> Int64
        """
        ...
    @property
    def MaximumConnections(self):
        """
        Gets the maximum number of supported Transmission Control Protocol (TCP) connections.

        Get: MaximumConnections(self: TcpStatistics) -> Int64
        """
        ...
    @property
    def MaximumTransmissionTimeout(self):
        """
        Gets the maximum retransmission time-out value for Transmission Control Protocol (TCP) segments.

        Get: MaximumTransmissionTimeout(self: TcpStatistics) -> Int64
        """
        ...
    @property
    def MinimumTransmissionTimeout(self):
        """
        Gets the minimum retransmission time-out value for Transmission Control Protocol (TCP) segments.

        Get: MinimumTransmissionTimeout(self: TcpStatistics) -> Int64
        """
        ...
    @property
    def ResetConnections(self):
        """
        Gets the number of RST packets received by Transmission Control Protocol (TCP) connections.

        Get: ResetConnections(self: TcpStatistics) -> Int64
        """
        ...
    @property
    def ResetsSent(self):
        """
        Gets the number of Transmission Control Protocol (TCP) segments sent with the reset flag set.

        Get: ResetsSent(self: TcpStatistics) -> Int64
        """
        ...
    @property
    def SegmentsReceived(self):
        """
        Gets the number of Transmission Control Protocol (TCP) segments received.

        Get: SegmentsReceived(self: TcpStatistics) -> Int64
        """
        ...
    @property
    def SegmentsResent(self):
        """
        Gets the number of Transmission Control Protocol (TCP) segments re-sent.

        Get: SegmentsResent(self: TcpStatistics) -> Int64
        """
        ...
    @property
    def SegmentsSent(self):
        """
        Gets the number of Transmission Control Protocol (TCP) segments sent.

        Get: SegmentsSent(self: TcpStatistics) -> Int64
        """
        ...

class UdpStatistics:  # skipped bases: <type 'object'>
    """Provides User Datagram Protocol (UDP) statistical data."""

    @property
    def DatagramsReceived(self):
        """
        Gets the number of User Datagram Protocol (UDP) datagrams that were received.

        Get: DatagramsReceived(self: UdpStatistics) -> Int64
        """
        ...
    @property
    def DatagramsSent(self):
        """
        Gets the number of User Datagram Protocol (UDP) datagrams that were sent.

        Get: DatagramsSent(self: UdpStatistics) -> Int64
        """
        ...
    @property
    def IncomingDatagramsDiscarded(self):
        """
        Gets the number of User Datagram Protocol (UDP) datagrams that were received and discarded because of port errors.

        Get: IncomingDatagramsDiscarded(self: UdpStatistics) -> Int64
        """
        ...
    @property
    def IncomingDatagramsWithErrors(self):
        """
        Gets the number of User Datagram Protocol (UDP) datagrams that were received and discarded because of errors other than bad port information.

        Get: IncomingDatagramsWithErrors(self: UdpStatistics) -> Int64
        """
        ...
    @property
    def UdpListeners(self):
        """
        Gets the number of local endpoints that are listening for User Datagram Protocol (UDP) datagrams.

        Get: UdpListeners(self: UdpStatistics) -> int
        """
        ...

class UnicastIPAddressInformation(IPAddressInformation):
    """Provides information about a network interface's unicast address."""

    @property
    def AddressPreferredLifetime(self):
        """
        Gets the number of seconds remaining during which this address is the preferred address.

        Get: AddressPreferredLifetime(self: UnicastIPAddressInformation) -> Int64
        """
        ...
    @property
    def AddressValidLifetime(self):
        """
        Gets the number of seconds remaining during which this address is valid.

        Get: AddressValidLifetime(self: UnicastIPAddressInformation) -> Int64
        """
        ...
    @property
    def DhcpLeaseLifetime(self):
        """
        Specifies the amount of time remaining on the Dynamic Host Configuration Protocol (DHCP) lease for this IP address.

        Get: DhcpLeaseLifetime(self: UnicastIPAddressInformation) -> Int64
        """
        ...
    @property
    def DuplicateAddressDetectionState(self):
        """
        Gets a value that indicates the state of the duplicate address detection algorithm.

        Get: DuplicateAddressDetectionState(self: UnicastIPAddressInformation) -> DuplicateAddressDetectionState
        """
        ...
    @property
    def IPv4Mask(self):
        """
        Gets the IPv4 mask.

        Get: IPv4Mask(self: UnicastIPAddressInformation) -> IPAddress
        """
        ...
    @property
    def PrefixLength(self):
        """
        Gets the length, in bits, of the prefix or network part of the IP address.

        Get: PrefixLength(self: UnicastIPAddressInformation) -> int
        """
        ...
    @property
    def PrefixOrigin(self):
        """
        Gets a value that identifies the source of a unicast Internet Protocol (IP) address prefix.

        Get: PrefixOrigin(self: UnicastIPAddressInformation) -> PrefixOrigin
        """
        ...
    @property
    def SuffixOrigin(self):
        """
        Gets a value that identifies the source of a unicast Internet Protocol (IP) address suffix.

        Get: SuffixOrigin(self: UnicastIPAddressInformation) -> SuffixOrigin
        """
        ...

class UnicastIPAddressInformationCollection(
    object, ICollection[UnicastIPAddressInformation]
):  # skipped bases: <type 'IEnumerable'>, <type 'IEnumerable[UnicastIPAddressInformation]'>
    """Stores a set of System.Net.NetworkInformation.UnicastIPAddressInformation types."""

    def GetEnumerator(self):
        """
        GetEnumerator(self: UnicastIPAddressInformationCollection) -> IEnumerator[UnicastIPAddressInformation]

            Returns an object that can be used to iterate through this collection.

            Returns: An object that implements the System.Collections.IEnumerator interface and provides access to the System.Net.NetworkInformation.UnicastIPAddressInformation types in

             this collection.
        """
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
        Gets the number of System.Net.NetworkInformation.UnicastIPAddressInformation types in this collection.

        Get: Count(self: UnicastIPAddressInformationCollection) -> int
        """
        ...
    @property
    def IsReadOnly(self):
        """
        Gets a value that indicates whether access to this collection is read-only.

        Get: IsReadOnly(self: UnicastIPAddressInformationCollection) -> bool
        """
        ...
