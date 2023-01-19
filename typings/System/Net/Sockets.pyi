# encoding: utf-8
# module System.Net.Sockets calls itself Sockets
# from System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AddressFamily(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies the addressing scheme that an instance of the System.Net.Sockets.Socket class can use.

    enum AddressFamily, values: AppleTalk (16), Atm (22), Banyan (21), Ccitt (10), Chaos (5), Cluster (24), DataKit (9), DataLink (13), DecNet (12), Ecma (8), FireFox (19), HyperChannel (15), Ieee12844 (25), ImpLink (3), InterNetwork (2), InterNetworkV6 (23), Ipx (6), Irda (26), Iso (7), Lat (14), Max (29), NetBios (17), NetworkDesigners (28), NS (6), Osi (7), Pup (4), Sna (11), Unix (1), Unknown (-1), Unspecified (0), VoiceView (18)
    """

    AppleTalk = None
    Atm = None
    Banyan = None
    Ccitt = None
    Chaos = None
    Cluster = None
    DataKit = None
    DataLink = None
    DecNet = None
    Ecma = None
    FireFox = None
    HyperChannel = None
    Ieee12844 = None
    ImpLink = None
    InterNetwork = None
    InterNetworkV6 = None
    Ipx = None
    Irda = None
    Iso = None
    Lat = None
    Max = None
    NetBios = None
    NetworkDesigners = None
    NS = None
    Osi = None
    Pup = None
    Sna = None
    Unix = None
    Unknown = None
    Unspecified = None
    value__ = None
    VoiceView = None

class IOControlCode(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies the IO control codes supported by the System.Net.Sockets.Socket.IOControl(System.Int32,System.Byte[],System.Byte[]) method.

    enum IOControlCode, values: AbsorbRouterAlert (2550136837), AddMulticastGroupOnInterface (2550136842), AddressListChange (671088663), AddressListQuery (1207959574), AddressListSort (3355443225), AssociateHandle (2281701377), AsyncIO (2147772029), BindToInterface (2550136840), DataToRead (1074030207), DeleteMulticastGroupFromInterface (2550136843), EnableCircularQueuing (671088642), Flush (671088644), GetBroadcastAddress (1207959557), GetExtensionFunctionPointer (3355443206), GetGroupQos (3355443208), GetQos (3355443207), KeepAliveValues (2550136836), LimitBroadcasts (2550136839), MulticastInterface (2550136841), MulticastScope (2281701386), MultipointLoopback (2281701385), NamespaceChange (2281701401), NonBlockingIO (2147772030), OobDataRead (1074033415), QueryTargetPnpHandle (1207959576), ReceiveAll (2550136833), ReceiveAllIgmpMulticast (2550136835), ReceiveAllMulticast (2550136834), RoutingInterfaceChange (2281701397), RoutingInterfaceQuery (3355443220), SetGroupQos (2281701388), SetQos (2281701387), TranslateHandle (3355443213), UnicastInterface (2550136838)
    """

    AbsorbRouterAlert = None
    AddMulticastGroupOnInterface = None
    AddressListChange = None
    AddressListQuery = None
    AddressListSort = None
    AssociateHandle = None
    AsyncIO = None
    BindToInterface = None
    DataToRead = None
    DeleteMulticastGroupFromInterface = None
    EnableCircularQueuing = None
    Flush = None
    GetBroadcastAddress = None
    GetExtensionFunctionPointer = None
    GetGroupQos = None
    GetQos = None
    KeepAliveValues = None
    LimitBroadcasts = None
    MulticastInterface = None
    MulticastScope = None
    MultipointLoopback = None
    NamespaceChange = None
    NonBlockingIO = None
    OobDataRead = None
    QueryTargetPnpHandle = None
    ReceiveAll = None
    ReceiveAllIgmpMulticast = None
    ReceiveAllMulticast = None
    RoutingInterfaceChange = None
    RoutingInterfaceQuery = None
    SetGroupQos = None
    SetQos = None
    TranslateHandle = None
    UnicastInterface = None
    value__ = None

class IPPacketInformation:  # skipped bases: <type 'object'>
    """Presents the packet information from a call to System.Net.Sockets.Socket.ReceiveMessageFrom(System.Byte[],System.Int32,System.Int32,System.Net.Sockets.SocketFlags@,System.Net.EndPoint@,System.Net.Sockets.IPPacketInformation@) or System.Net.Sockets.Socket.EndReceiveMessageFrom(System.IAsyncResult,System.Net.Sockets.SocketFlags@,System.Net.EndPoint@,System.Net.Sockets.IPPacketInformation@)."""

    def Equals(self, comparand):
        """
        Equals(self: IPPacketInformation, comparand: object) -> bool

            Returns a value that indicates whether this instance is equal to a specified object.

            comparand: The object to compare with this instance.

            Returns: ue if comparand is an instance of System.Net.Sockets.IPPacketInformation and equals the value of the instance; otherwise, lse.
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: IPPacketInformation) -> int

            Returns the hash code for this instance.

            Returns: An Int32 hash code.
        """
        ...
    def __eq__(self, *args):  # cannot find CLR method
        """x.__eq__(y) <==> x==y"""
        ...
    def __ne__(self, *args): ...
    @property
    def Address(self):
        """
        Gets the origin information of the packet that was received as a result of calling the System.Net.Sockets.Socket.ReceiveMessageFrom(System.Byte[],System.Int32,System.Int32,System.Net.Sockets.SocketFlags@,System.Net.EndPoint@,System.Net.Sockets.IPPacketInformation@) method or System.Net.Sockets.Socket.EndReceiveMessageFrom(System.IAsyncResult,System.Net.Sockets.SocketFlags@,System.Net.EndPoint@,System.Net.Sockets.IPPacketInformation@) method.

        Get: Address(self: IPPacketInformation) -> IPAddress
        """
        ...
    @property
    def Interface(self):
        """
        Gets the network interface information that is associated with a call to System.Net.Sockets.Socket.ReceiveMessageFrom(System.Byte[],System.Int32,System.Int32,System.Net.Sockets.SocketFlags@,System.Net.EndPoint@,System.Net.Sockets.IPPacketInformation@) or System.Net.Sockets.Socket.EndReceiveMessageFrom(System.IAsyncResult,System.Net.Sockets.SocketFlags@,System.Net.EndPoint@,System.Net.Sockets.IPPacketInformation@).

        Get: Interface(self: IPPacketInformation) -> int
        """
        ...

class IPProtectionLevel(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    A value that enables restriction of an IPv6 socket to a specified scope, such as addresses with the same link local or site local prefix.

    enum IPProtectionLevel, values: EdgeRestricted (20), Restricted (30), Unrestricted (10), Unspecified (-1)
    """

    EdgeRestricted = None
    Restricted = None
    Unrestricted = None
    Unspecified = None
    value__ = None

class IPv6MulticastOption:  # skipped bases: <type 'object'>
    """
    Contains option values for joining an IPv6 multicast group.

    IPv6MulticastOption(group: IPAddress, ifindex: Int64)

    IPv6MulticastOption(group: IPAddress)
    """

    @property
    def Group(self):
        """
        Gets or sets the IP address of a multicast group.

        Get: Group(self: IPv6MulticastOption) -> IPAddress

        Set: Group(self: IPv6MulticastOption) = value
        """
        ...
    @property
    def InterfaceIndex(self):
        """
        Gets or sets the interface index that is associated with a multicast group.

        Get: InterfaceIndex(self: IPv6MulticastOption) -> Int64

        Set: InterfaceIndex(self: IPv6MulticastOption) = value
        """
        ...

class LingerOption:  # skipped bases: <type 'object'>
    """
    Specifies whether a System.Net.Sockets.Socket will remain connected after a call to the System.Net.Sockets.Socket.Close or System.Net.Sockets.TcpClient.Close methods and the length of time it will remain connected, if data remains to be sent.

    LingerOption(enable: bool, seconds: int)
    """

    @property
    def Enabled(self):
        """
        Gets or sets a value that indicates whether to linger after the System.Net.Sockets.Socket is closed.

        Get: Enabled(self: LingerOption) -> bool

        Set: Enabled(self: LingerOption) = value
        """
        ...
    @property
    def LingerTime(self):
        """
        Gets or sets the amount of time to remain connected after calling the System.Net.Sockets.Socket.Close method if data remains to be sent.

        Get: LingerTime(self: LingerOption) -> int

        Set: LingerTime(self: LingerOption) = value
        """
        ...

class MulticastOption:  # skipped bases: <type 'object'>
    """
    Contains System.Net.IPAddress values used to join and drop multicast groups.

    MulticastOption(group: IPAddress, mcint: IPAddress)

    MulticastOption(group: IPAddress, interfaceIndex: int)

    MulticastOption(group: IPAddress)
    """

    @property
    def Group(self):
        """
        Gets or sets the IP address of a multicast group.

        Get: Group(self: MulticastOption) -> IPAddress

        Set: Group(self: MulticastOption) = value
        """
        ...
    @property
    def InterfaceIndex(self):
        """
        Gets or sets the index of the interface that is used to send and receive multicast packets.

        Get: InterfaceIndex(self: MulticastOption) -> int

        Set: InterfaceIndex(self: MulticastOption) = value
        """
        ...
    @property
    def LocalAddress(self):
        """
        Gets or sets the local address associated with a multicast group.

        Get: LocalAddress(self: MulticastOption) -> IPAddress

        Set: LocalAddress(self: MulticastOption) = value
        """
        ...

class NetworkStream(Stream):  # skipped bases: <type 'IDisposable'>
    """
    Provides the underlying stream of data for network access.

    NetworkStream(socket: Socket)

    NetworkStream(socket: Socket, ownsSocket: bool)

    NetworkStream(socket: Socket, access: FileAccess)

    NetworkStream(socket: Socket, access: FileAccess, ownsSocket: bool)
    """

    @staticmethod  # known case of __new__
    def __new__(cls, socket, *__args):
        """
        __new__(cls: type, socket: Socket)

        __new__(cls: type, socket: Socket, ownsSocket: bool)

        __new__(cls: type, socket: Socket, access: FileAccess)

        __new__(cls: type, socket: Socket, access: FileAccess, ownsSocket: bool)
        """
        ...
    @property
    def CanRead(self):
        """
        Gets a value that indicates whether the System.Net.Sockets.NetworkStream supports reading.

        Get: CanRead(self: NetworkStream) -> bool
        """
        ...
    @property
    def CanSeek(self):
        """
        Gets a value that indicates whether the stream supports seeking. This property is not currently supported.This property always returns lse.

        Get: CanSeek(self: NetworkStream) -> bool
        """
        ...
    @property
    def CanTimeout(self):
        """
        Indicates whether timeout properties are usable for System.Net.Sockets.NetworkStream.

        Get: CanTimeout(self: NetworkStream) -> bool
        """
        ...
    @property
    def CanWrite(self):
        """
        Gets a value that indicates whether the System.Net.Sockets.NetworkStream supports writing.

        Get: CanWrite(self: NetworkStream) -> bool
        """
        ...
    @property
    def DataAvailable(self):
        """
        Gets a value that indicates whether data is available on the System.Net.Sockets.NetworkStream to be read.

        Get: DataAvailable(self: NetworkStream) -> bool
        """
        ...
    @property
    def Length(self):
        """
        Gets the length of the data available on the stream. This property is not currently supported and always throws a System.NotSupportedException.

        Get: Length(self: NetworkStream) -> Int64
        """
        ...
    @property
    def Position(self):
        """
        Gets or sets the current position in the stream. This property is not currently supported and always throws a System.NotSupportedException.

        Get: Position(self: NetworkStream) -> Int64

        Set: Position(self: NetworkStream) = value
        """
        ...
    @property
    def Readable(self):
        """Gets or sets a value that indicates whether the System.Net.Sockets.NetworkStream can be read."""
        ...
    @property
    def ReadTimeout(self):
        """
        Gets or sets the amount of time that a read operation blocks waiting for data.

        Get: ReadTimeout(self: NetworkStream) -> int

        Set: ReadTimeout(self: NetworkStream) = value
        """
        ...
    @property
    def Socket(self):
        """Gets the underlying System.Net.Sockets.Socket."""
        ...
    @property
    def Writeable(self):
        """Gets a value that indicates whether the System.Net.Sockets.NetworkStream is writable."""
        ...
    @property
    def WriteTimeout(self):
        """
        Gets or sets the amount of time that a write operation blocks waiting for data.

        Get: WriteTimeout(self: NetworkStream) -> int

        Set: WriteTimeout(self: NetworkStream) = value
        """
        ...

class ProtocolFamily(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies the type of protocol that an instance of the System.Net.Sockets.Socket class can use.

    enum ProtocolFamily, values: AppleTalk (16), Atm (22), Banyan (21), Ccitt (10), Chaos (5), Cluster (24), DataKit (9), DataLink (13), DecNet (12), Ecma (8), FireFox (19), HyperChannel (15), Ieee12844 (25), ImpLink (3), InterNetwork (2), InterNetworkV6 (23), Ipx (6), Irda (26), Iso (7), Lat (14), Max (29), NetBios (17), NetworkDesigners (28), NS (6), Osi (7), Pup (4), Sna (11), Unix (1), Unknown (-1), Unspecified (0), VoiceView (18)
    """

    AppleTalk = None
    Atm = None
    Banyan = None
    Ccitt = None
    Chaos = None
    Cluster = None
    DataKit = None
    DataLink = None
    DecNet = None
    Ecma = None
    FireFox = None
    HyperChannel = None
    Ieee12844 = None
    ImpLink = None
    InterNetwork = None
    InterNetworkV6 = None
    Ipx = None
    Irda = None
    Iso = None
    Lat = None
    Max = None
    NetBios = None
    NetworkDesigners = None
    NS = None
    Osi = None
    Pup = None
    Sna = None
    Unix = None
    Unknown = None
    Unspecified = None
    value__ = None
    VoiceView = None

class ProtocolType(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies the protocols that the System.Net.Sockets.Socket class supports.

    enum ProtocolType, values: Ggp (3), Icmp (1), IcmpV6 (58), Idp (22), Igmp (2), IP (0), IPSecAuthenticationHeader (51), IPSecEncapsulatingSecurityPayload (50), IPv4 (4), IPv6 (41), IPv6DestinationOptions (60), IPv6FragmentHeader (44), IPv6HopByHopOptions (0), IPv6NoNextHeader (59), IPv6RoutingHeader (43), Ipx (1000), ND (77), Pup (12), Raw (255), Spx (1256), SpxII (1257), Tcp (6), Udp (17), Unknown (-1), Unspecified (0)
    """

    Ggp = None
    Icmp = None
    IcmpV6 = None
    Idp = None
    Igmp = None
    IP = None
    IPSecAuthenticationHeader = None
    IPSecEncapsulatingSecurityPayload = None
    IPv4 = None
    IPv6 = None
    IPv6DestinationOptions = None
    IPv6FragmentHeader = None
    IPv6HopByHopOptions = None
    IPv6NoNextHeader = None
    IPv6RoutingHeader = None
    Ipx = None
    ND = None
    Pup = None
    Raw = None
    Spx = None
    SpxII = None
    Tcp = None
    Udp = None
    Unknown = None
    Unspecified = None
    value__ = None

class SelectMode(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Defines the polling modes for the System.Net.Sockets.Socket.Poll(System.Int32,System.Net.Sockets.SelectMode) method.

    enum SelectMode, values: SelectError (2), SelectRead (0), SelectWrite (1)
    """

    SelectError = None
    SelectRead = None
    SelectWrite = None
    value__ = None

class SendPacketsElement:  # skipped bases: <type 'object'>
    """
    Represents an element in a System.Net.Sockets.SendPacketsElement array.

    SendPacketsElement(filepath: str)

    SendPacketsElement(filepath: str, offset: int, count: int)

    SendPacketsElement(filepath: str, offset: int, count: int, endOfPacket: bool)

    SendPacketsElement(buffer: Array[Byte])

    SendPacketsElement(buffer: Array[Byte], offset: int, count: int)

    SendPacketsElement(buffer: Array[Byte], offset: int, count: int, endOfPacket: bool)
    """

    @property
    def Buffer(self):
        """
        Gets the buffer to be sent if the System.Net.Sockets.SendPacketsElement class was initialized with a buffer parameter.

        Get: Buffer(self: SendPacketsElement) -> Array[Byte]
        """
        ...
    @property
    def Count(self):
        """
        Gets the count of bytes to be sent.

        Get: Count(self: SendPacketsElement) -> int
        """
        ...
    @property
    def EndOfPacket(self):
        """
        Gets a Boolean value that indicates if this element should not be combined with the next element in a single send request from the sockets layer to the transport.

        Get: EndOfPacket(self: SendPacketsElement) -> bool
        """
        ...
    @property
    def FilePath(self):
        """
        Gets the filename of the file to send if the System.Net.Sockets.SendPacketsElement class was initialized with a filepath parameter.

        Get: FilePath(self: SendPacketsElement) -> str
        """
        ...
    @property
    def Offset(self):
        """
        Gets the offset, in bytes, from the beginning of the data buffer or file to the location in the buffer or file to start sending the data.

        Get: Offset(self: SendPacketsElement) -> int
        """
        ...

class Socket(object, IDisposable):
    """
    Implements the Berkeley sockets interface.

    Socket(socketType: SocketType, protocolType: ProtocolType)

    Socket(addressFamily: AddressFamily, socketType: SocketType, protocolType: ProtocolType)

    Socket(socketInformation: SocketInformation)
    """

    def Accept(self):
        """
        Accept(self: Socket) -> Socket

            Creates a new System.Net.Sockets.Socket for a newly created connection.

            Returns: A System.Net.Sockets.Socket for a newly created connection.
        """
        ...
    def AcceptAsync(self, e):
        """
        AcceptAsync(self: Socket, e: SocketAsyncEventArgs) -> bool

            Begins an asynchronous operation to accept an incoming connection attempt.

            e: The System.Net.Sockets.SocketAsyncEventArgs object to use for this asynchronous socket operation.

            Returns: Returns ue if the I/O operation is pending. The System.Net.Sockets.SocketAsyncEventArgs.Completed event on the e parameter will be raised upon completion of the

             operation.Returns lse if the I/O operation completed synchronously. The System.Net.Sockets.SocketAsyncEventArgs.Completed event on the e parameter will not be raised

             and the e object passed as a parameter may be examined immediately after the method call returns to retrieve the result of the operation.
        """
        ...
    def BeginAccept(self, *__args):
        """
        BeginAccept(self: Socket, receiveSize: int, callback: AsyncCallback, state: object) -> IAsyncResult

            Begins an asynchronous operation to accept an incoming connection attempt and receives the first block of data sent by the client application.

            receiveSize: The number of bytes to accept from the sender.

            callback: The System.AsyncCallback delegate.

            state: An object that contains state information for this request.

            Returns: An System.IAsyncResult that references the asynchronous System.Net.Sockets.Socket creation.

        BeginAccept(self: Socket, callback: AsyncCallback, state: object) -> IAsyncResult

            Begins an asynchronous operation to accept an incoming connection attempt.

            callback: The System.AsyncCallback delegate.

            state: An object that contains state information for this request.

            Returns: An System.IAsyncResult that references the asynchronous System.Net.Sockets.Socket creation.

        BeginAccept(self: Socket, acceptSocket: Socket, receiveSize: int, callback: AsyncCallback, state: object) -> IAsyncResult

            Begins an asynchronous operation to accept an incoming connection attempt from a specified socket and receives the first block of data sent by the client application.

            acceptSocket: The accepted System.Net.Sockets.Socket object. This value may be ll.

            receiveSize: The maximum number of bytes to receive.

            callback: The System.AsyncCallback delegate.

            state: An object that contains state information for this request.

            Returns: An System.IAsyncResult object that references the asynchronous System.Net.Sockets.Socket object creation.
        """
        ...
    def BeginConnect(self, *__args):
        """
        BeginConnect(self: Socket, remoteEP: EndPoint, callback: AsyncCallback, state: object) -> IAsyncResult

            Begins an asynchronous request for a remote host connection.

            remoteEP: An System.Net.EndPoint that represents the remote host.

            callback: The System.AsyncCallback delegate.

            state: An object that contains state information for this request.

            Returns: An System.IAsyncResult that references the asynchronous connection.

        BeginConnect(self: Socket, host: str, port: int, requestCallback: AsyncCallback, state: object) -> IAsyncResult

            Begins an asynchronous request for a remote host connection. The host is specified by a host name and a port number.

            host: The name of the remote host.

            port: The port number of the remote host.

            requestCallback: An System.AsyncCallback delegate that references the method to invoke when the connect operation is complete.

            state: A user-defined object that contains information about the connect operation. This object is passed to the requestCallback delegate when the operation is complete.

            Returns: An System.IAsyncResult that references the asynchronous connection.

        BeginConnect(self: Socket, address: IPAddress, port: int, requestCallback: AsyncCallback, state: object) -> IAsyncResult

            Begins an asynchronous request for a remote host connection. The host is specified by an System.Net.IPAddress and a port number.

            address: The System.Net.IPAddress of the remote host.

            port: The port number of the remote host.

            requestCallback: An System.AsyncCallback delegate that references the method to invoke when the connect operation is complete.

            state: A user-defined object that contains information about the connect operation. This object is passed to the requestCallback delegate when the operation is complete.

            Returns: An System.IAsyncResult that references the asynchronous connection.

        BeginConnect(self: Socket, addresses: Array[IPAddress], port: int, requestCallback: AsyncCallback, state: object) -> IAsyncResult

            Begins an asynchronous request for a remote host connection. The host is specified by an System.Net.IPAddress array and a port number.

            addresses: At least one System.Net.IPAddress, designating the remote host.

            port: The port number of the remote host.

            requestCallback: An System.AsyncCallback delegate that references the method to invoke when the connect operation is complete.

            state: A user-defined object that contains information about the connect operation. This object is passed to the requestCallback delegate when the operation is complete.

            Returns: An System.IAsyncResult that references the asynchronous connections.
        """
        ...
    def BeginDisconnect(self, reuseSocket, callback, state):
        """
        BeginDisconnect(self: Socket, reuseSocket: bool, callback: AsyncCallback, state: object) -> IAsyncResult

            Begins an asynchronous request to disconnect from a remote endpoint.

            reuseSocket: ue if this socket can be reused after the connection is closed; otherwise, lse.

            callback: The System.AsyncCallback delegate.

            state: An object that contains state information for this request.

            Returns: An System.IAsyncResult object that references the asynchronous operation.
        """
        ...
    def BeginReceive(self, *__args):
        """
        BeginReceive(self: Socket, buffer: Array[Byte], offset: int, size: int, socketFlags: SocketFlags, callback: AsyncCallback, state: object) -> IAsyncResult

            Begins to asynchronously receive data from a connected System.Net.Sockets.Socket.

            buffer: An array of type System.Byte that is the storage location for the received data.

            offset: The zero-based position in the buffer parameter at which to store the received data.

            size: The number of bytes to receive.

            socketFlags: A bitwise combination of the System.Net.Sockets.SocketFlags values.

            callback: An System.AsyncCallback delegate that references the method to invoke when the operation is complete.

            state: A user-defined object that contains information about the receive operation. This object is passed to the System.Net.Sockets.Socket.EndReceive(System.IAsyncResult)

             delegate when the operation is complete.

            Returns: An System.IAsyncResult that references the asynchronous read.

        BeginReceive(self: Socket, buffers: IList[ArraySegment[Byte]], socketFlags: SocketFlags, callback: AsyncCallback, state: object) -> IAsyncResult

        BeginReceive(self: Socket, buffers: IList[ArraySegment[Byte]], socketFlags: SocketFlags, callback: AsyncCallback, state: object) -> (IAsyncResult, SocketError)

        BeginReceive(self: Socket, buffer: Array[Byte], offset: int, size: int, socketFlags: SocketFlags, callback: AsyncCallback, state: object) -> (IAsyncResult, SocketError)

            Begins to asynchronously receive data from a connected System.Net.Sockets.Socket.

            buffer: An array of type System.Byte that is the storage location for the received data.

            offset: The location in buffer to store the received data.

            size: The number of bytes to receive.

            socketFlags: A bitwise combination of the System.Net.Sockets.SocketFlags values.

            callback: An System.AsyncCallback delegate that references the method to invoke when the operation is complete.

            state: A user-defined object that contains information about the receive operation. This object is passed to the System.Net.Sockets.Socket.EndReceive(System.IAsyncResult)

             delegate when the operation is complete.

            Returns: An System.IAsyncResult that references the asynchronous read.
        """
        ...
    def BeginReceiveFrom(self, buffer, offset, size, socketFlags, remoteEP, callback, state):
        """
        BeginReceiveFrom(self: Socket, buffer: Array[Byte], offset: int, size: int, socketFlags: SocketFlags, remoteEP: EndPoint, callback: AsyncCallback, state: object) -> (IAsyncResult, EndPoint)

            Begins to asynchronously receive data from a specified network device.

            buffer: An array of type System.Byte that is the storage location for the received data.

            offset: The zero-based position in the buffer parameter at which to store the data.

            size: The number of bytes to receive.

            socketFlags: A bitwise combination of the System.Net.Sockets.SocketFlags values.

            remoteEP: An System.Net.EndPoint that represents the source of the data.

            callback: The System.AsyncCallback delegate.

            state: An object that contains state information for this request.

            Returns: An System.IAsyncResult that references the asynchronous read.
        """
        ...
    def BeginReceiveMessageFrom(self, buffer, offset, size, socketFlags, remoteEP, callback, state):
        """
        BeginReceiveMessageFrom(self: Socket, buffer: Array[Byte], offset: int, size: int, socketFlags: SocketFlags, remoteEP: EndPoint, callback: AsyncCallback, state: object) -> (IAsyncResult, EndPoint)

            Begins to asynchronously receive the specified number of bytes of data into the specified location of the data buffer, using the specified

             System.Net.Sockets.SocketFlags, and stores the endpoint and packet information..

            buffer: An array of type System.Byte that is the storage location for the received data.

            offset: The zero-based position in the buffer parameter at which to store the data.

            size: The number of bytes to receive.

            socketFlags: A bitwise combination of the System.Net.Sockets.SocketFlags values.

            remoteEP: An System.Net.EndPoint that represents the source of the data.

            callback: The System.AsyncCallback delegate.

            state: An object that contains state information for this request.

            Returns: An System.IAsyncResult that references the asynchronous read.
        """
        ...
    def BeginSend(self, *__args):
        """
        BeginSend(self: Socket, buffer: Array[Byte], offset: int, size: int, socketFlags: SocketFlags, callback: AsyncCallback, state: object) -> IAsyncResult

            Sends data asynchronously to a connected System.Net.Sockets.Socket.

            buffer: An array of type System.Byte that contains the data to send.

            offset: The zero-based position in the buffer parameter at which to begin sending data.

            size: The number of bytes to send.

            socketFlags: A bitwise combination of the System.Net.Sockets.SocketFlags values.

            callback: The System.AsyncCallback delegate.

            state: An object that contains state information for this request.

            Returns: An System.IAsyncResult that references the asynchronous send.

        BeginSend(self: Socket, buffers: IList[ArraySegment[Byte]], socketFlags: SocketFlags, callback: AsyncCallback, state: object) -> IAsyncResult

        BeginSend(self: Socket, buffers: IList[ArraySegment[Byte]], socketFlags: SocketFlags, callback: AsyncCallback, state: object) -> (IAsyncResult, SocketError)

        BeginSend(self: Socket, buffer: Array[Byte], offset: int, size: int, socketFlags: SocketFlags, callback: AsyncCallback, state: object) -> (IAsyncResult, SocketError)

            Sends data asynchronously to a connected System.Net.Sockets.Socket.

            buffer: An array of type System.Byte that contains the data to send.

            offset: The zero-based position in the buffer parameter at which to begin sending data.

            size: The number of bytes to send.

            socketFlags: A bitwise combination of the System.Net.Sockets.SocketFlags values.

            callback: The System.AsyncCallback delegate.

            state: An object that contains state information for this request.

            Returns: An System.IAsyncResult that references the asynchronous send.
        """
        ...
    def BeginSendFile(self, fileName, *__args):
        """
        BeginSendFile(self: Socket, fileName: str, callback: AsyncCallback, state: object) -> IAsyncResult

            Sends the file fileName to a connected System.Net.Sockets.Socket object using the System.Net.Sockets.TransmitFileOptions.UseDefaultWorkerThread flag.

            fileName: A string that contains the path and name of the file to send. This parameter can be ll.

            callback: The System.AsyncCallback delegate.

            state: An object that contains state information for this request.

            Returns: An System.IAsyncResult object that represents the asynchronous send.

        BeginSendFile(self: Socket, fileName: str, preBuffer: Array[Byte], postBuffer: Array[Byte], flags: TransmitFileOptions, callback: AsyncCallback, state: object) -> IAsyncResult

            Sends a file and buffers of data asynchronously to a connected System.Net.Sockets.Socket object.

            fileName: A string that contains the path and name of the file to be sent. This parameter can be ll.

            preBuffer: A System.Byte array that contains data to be sent before the file is sent. This parameter can be ll.

            postBuffer: A System.Byte array that contains data to be sent after the file is sent. This parameter can be ll.

            flags: A bitwise combination of System.Net.Sockets.TransmitFileOptions values.

            callback: An System.AsyncCallback delegate to be invoked when this operation completes. This parameter can be ll.

            state: A user-defined object that contains state information for this request. This parameter can be ll.

            Returns: An System.IAsyncResult object that represents the asynchronous operation.
        """
        ...
    def BeginSendTo(self, buffer, offset, size, socketFlags, remoteEP, callback, state):
        """
        BeginSendTo(self: Socket, buffer: Array[Byte], offset: int, size: int, socketFlags: SocketFlags, remoteEP: EndPoint, callback: AsyncCallback, state: object) -> IAsyncResult

            Sends data asynchronously to a specific remote host.

            buffer: An array of type System.Byte that contains the data to send.

            offset: The zero-based position in buffer at which to begin sending data.

            size: The number of bytes to send.

            socketFlags: A bitwise combination of the System.Net.Sockets.SocketFlags values.

            remoteEP: An System.Net.EndPoint that represents the remote device.

            callback: The System.AsyncCallback delegate.

            state: An object that contains state information for this request.

            Returns: An System.IAsyncResult that references the asynchronous send.
        """
        ...
    def Bind(self, localEP):
        """
        Bind(self: Socket, localEP: EndPoint)

            Associates a System.Net.Sockets.Socket with a local endpoint.

            localEP: The local System.Net.EndPoint to associate with the System.Net.Sockets.Socket.
        """
        ...
    @staticmethod
    def CancelConnectAsync(e):
        """
        CancelConnectAsync(e: SocketAsyncEventArgs)

            Cancels an asynchronous request for a remote host connection.

            e: The System.Net.Sockets.SocketAsyncEventArgs object used to request the connection to the remote host by calling one of the

             System.Net.Sockets.Socket.ConnectAsync(System.Net.Sockets.SocketType,System.Net.Sockets.ProtocolType,System.Net.Sockets.SocketAsyncEventArgs) methods.
        """
        ...
    def Close(self, timeout=None):
        """
        Close(self: Socket, timeout: int)

            Closes the System.Net.Sockets.Socket connection and releases all associated resources with a specified timeout to allow queued data to be sent.

            timeout: Wait up to timeout seconds to send any remaining data, then close the socket.

        Close(self: Socket)

            Closes the System.Net.Sockets.Socket connection and releases all associated resources.
        """
        ...
    def Connect(self, *__args):
        """
        Connect(self: Socket, remoteEP: EndPoint)

            Establishes a connection to a remote host.

            remoteEP: An System.Net.EndPoint that represents the remote device.

        Connect(self: Socket, address: IPAddress, port: int)

            Establishes a connection to a remote host. The host is specified by an IP address and a port number.

            address: The IP address of the remote host.

            port: The port number of the remote host.

        Connect(self: Socket, host: str, port: int)

            Establishes a connection to a remote host. The host is specified by a host name and a port number.

            host: The name of the remote host.

            port: The port number of the remote host.

        Connect(self: Socket, addresses: Array[IPAddress], port: int)

            Establishes a connection to a remote host. The host is specified by an array of IP addresses and a port number.

            addresses: The IP addresses of the remote host.

            port: The port number of the remote host.
        """
        ...
    def ConnectAsync(self, *__args):
        """
        ConnectAsync(self: Socket, e: SocketAsyncEventArgs) -> bool

            Begins an asynchronous request for a connection to a remote host.

            e: The System.Net.Sockets.SocketAsyncEventArgs object to use for this asynchronous socket operation.

            Returns: Returns ue if the I/O operation is pending. The System.Net.Sockets.SocketAsyncEventArgs.Completed event on the e parameter will be raised upon completion of the

             operation. Returns lse if the I/O operation completed synchronously. In this case, The System.Net.Sockets.SocketAsyncEventArgs.Completed event on the e parameter will

             not be raised and the e object passed as a parameter may be examined immediately after the method call returns to retrieve the result of the operation.

        ConnectAsync(socketType: SocketType, protocolType: ProtocolType, e: SocketAsyncEventArgs) -> bool

            Begins an asynchronous request for a connection to a remote host.

            socketType: One of the System.Net.Sockets.SocketType values.

            protocolType: One of the System.Net.Sockets.ProtocolType values.

            e: The System.Net.Sockets.SocketAsyncEventArgs object to use for this asynchronous socket operation.

            Returns: Returns ue if the I/O operation is pending. The System.Net.Sockets.SocketAsyncEventArgs.Completed event on the e parameter will be raised upon completion of the

             operation. Returns lse if the I/O operation completed synchronously. In this case, The System.Net.Sockets.SocketAsyncEventArgs.Completed event on the e parameter will

             not be raised and the e object passed as a parameter may be examined immediately after the method call returns to retrieve the result of the operation.
        """
        ...
    def Disconnect(self, reuseSocket):
        """
        Disconnect(self: Socket, reuseSocket: bool)

            Closes the socket connection and allows reuse of the socket.

            reuseSocket: ue if this socket can be reused after the current connection is closed; otherwise, lse.
        """
        ...
    def DisconnectAsync(self, e):
        """
        DisconnectAsync(self: Socket, e: SocketAsyncEventArgs) -> bool

            Begins an asynchronous request to disconnect from a remote endpoint.

            e: The System.Net.Sockets.SocketAsyncEventArgs object to use for this asynchronous socket operation.

            Returns: Returns ue if the I/O operation is pending. The System.Net.Sockets.SocketAsyncEventArgs.Completed event on the e parameter will be raised upon completion of the

             operation. Returns lse if the I/O operation completed synchronously. In this case, The System.Net.Sockets.SocketAsyncEventArgs.Completed event on the e parameter will

             not be raised and the e object passed as a parameter may be examined immediately after the method call returns to retrieve the result of the operation.
        """
        ...
    def DuplicateAndClose(self, targetProcessId):
        """
        DuplicateAndClose(self: Socket, targetProcessId: int) -> SocketInformation

            Duplicates the socket reference for the target process, and closes the socket for this process.

            targetProcessId: The ID of the target process where a duplicate of the socket reference is created.

            Returns: The socket reference to be passed to the target process.
        """
        ...
    def EndAccept(self, *__args):
        """
        EndAccept(self: Socket, asyncResult: IAsyncResult) -> Socket

            Asynchronously accepts an incoming connection attempt and creates a new System.Net.Sockets.Socket to handle remote host communication.

            asyncResult: An System.IAsyncResult that stores state information for this asynchronous operation as well as any user defined data.

            Returns: A System.Net.Sockets.Socket to handle communication with the remote host.

        EndAccept(self: Socket, asyncResult: IAsyncResult) -> (Socket, Array[Byte])

            Asynchronously accepts an incoming connection attempt and creates a new System.Net.Sockets.Socket object to handle remote host communication. This method returns a

             buffer that contains the initial data transferred.

            asyncResult: An System.IAsyncResult object that stores state information for this asynchronous operation as well as any user defined data.

            Returns: A System.Net.Sockets.Socket object to handle communication with the remote host.

        EndAccept(self: Socket, asyncResult: IAsyncResult) -> (Socket, Array[Byte], int)

            Asynchronously accepts an incoming connection attempt and creates a new System.Net.Sockets.Socket object to handle remote host communication. This method returns a

             buffer that contains the initial data and the number of bytes transferred.

            asyncResult: An System.IAsyncResult object that stores state information for this asynchronous operation as well as any user defined data.

            Returns: A System.Net.Sockets.Socket object to handle communication with the remote host.
        """
        ...
    def EndConnect(self, asyncResult):
        """
        EndConnect(self: Socket, asyncResult: IAsyncResult)

            Ends a pending asynchronous connection request.

            asyncResult: An System.IAsyncResult that stores state information and any user defined data for this asynchronous operation.
        """
        ...
    def EndDisconnect(self, asyncResult):
        """
        EndDisconnect(self: Socket, asyncResult: IAsyncResult)

            Ends a pending asynchronous disconnect request.

            asyncResult: An System.IAsyncResult object that stores state information and any user-defined data for this asynchronous operation.
        """
        ...
    def EndReceive(self, asyncResult, errorCode=None):
        """
        EndReceive(self: Socket, asyncResult: IAsyncResult) -> int

            Ends a pending asynchronous read.

            asyncResult: An System.IAsyncResult that stores state information and any user defined data for this asynchronous operation.

            Returns: The number of bytes received.

        EndReceive(self: Socket, asyncResult: IAsyncResult) -> (int, SocketError)

            Ends a pending asynchronous read.

            asyncResult: An System.IAsyncResult that stores state information and any user defined data for this asynchronous operation.

            Returns: The number of bytes received.
        """
        ...
    def EndReceiveFrom(self, asyncResult, endPoint):
        """
        EndReceiveFrom(self: Socket, asyncResult: IAsyncResult, endPoint: EndPoint) -> (int, EndPoint)

            Ends a pending asynchronous read from a specific endpoint.

            asyncResult: An System.IAsyncResult that stores state information and any user defined data for this asynchronous operation.

            endPoint: The source System.Net.EndPoint.

            Returns: If successful, the number of bytes received. If unsuccessful, returns 0.
        """
        ...
    def EndReceiveMessageFrom(self, asyncResult, socketFlags, endPoint, ipPacketInformation):
        """
        EndReceiveMessageFrom(self: Socket, asyncResult: IAsyncResult, socketFlags: SocketFlags, endPoint: EndPoint) -> (int, SocketFlags, EndPoint, IPPacketInformation)

            Ends a pending asynchronous read from a specific endpoint. This method also reveals more information about the packet than

             System.Net.Sockets.Socket.EndReceiveFrom(System.IAsyncResult,System.Net.EndPoint@).

            asyncResult: An System.IAsyncResult that stores state information and any user defined data for this asynchronous operation.

            socketFlags: A bitwise combination of the System.Net.Sockets.SocketFlags values for the received packet.

            endPoint: The source System.Net.EndPoint.

            Returns: If successful, the number of bytes received. If unsuccessful, returns 0.
        """
        ...
    def EndSend(self, asyncResult, errorCode=None):
        """
        EndSend(self: Socket, asyncResult: IAsyncResult) -> int

            Ends a pending asynchronous send.

            asyncResult: An System.IAsyncResult that stores state information for this asynchronous operation.

            Returns: If successful, the number of bytes sent to the System.Net.Sockets.Socket; otherwise, an invalid System.Net.Sockets.Socket error.

        EndSend(self: Socket, asyncResult: IAsyncResult) -> (int, SocketError)

            Ends a pending asynchronous send.

            asyncResult: An System.IAsyncResult that stores state information for this asynchronous operation.

            Returns: If successful, the number of bytes sent to the System.Net.Sockets.Socket; otherwise, an invalid System.Net.Sockets.Socket error.
        """
        ...
    def EndSendFile(self, asyncResult):
        """
        EndSendFile(self: Socket, asyncResult: IAsyncResult)

            Ends a pending asynchronous send of a file.

            asyncResult: An System.IAsyncResult object that stores state information for this asynchronous operation.
        """
        ...
    def EndSendTo(self, asyncResult):
        """
        EndSendTo(self: Socket, asyncResult: IAsyncResult) -> int

            Ends a pending asynchronous send to a specific location.

            asyncResult: An System.IAsyncResult that stores state information and any user defined data for this asynchronous operation.

            Returns: If successful, the number of bytes sent; otherwise, an invalid System.Net.Sockets.Socket error.
        """
        ...
    def GetSocketOption(self, optionLevel, optionName, *__args):
        """
        GetSocketOption(self: Socket, optionLevel: SocketOptionLevel, optionName: SocketOptionName) -> object

            Returns the value of a specified System.Net.Sockets.Socket option, represented as an object.

            optionLevel: One of the System.Net.Sockets.SocketOptionLevel values.

            optionName: One of the System.Net.Sockets.SocketOptionName values.

            Returns: An object that represents the value of the option. When the optionName parameter is set to System.Net.Sockets.SocketOptionName.Linger the return value is an instance

             of the System.Net.Sockets.LingerOption class. When optionName is set to System.Net.Sockets.SocketOptionName.AddMembership or

             System.Net.Sockets.SocketOptionName.DropMembership, the return value is an instance of the System.Net.Sockets.MulticastOption class. When optionName is any other

             value, the return value is an integer.

        GetSocketOption(self: Socket, optionLevel: SocketOptionLevel, optionName: SocketOptionName, optionValue: Array[Byte])

            Returns the specified System.Net.Sockets.Socket option setting, represented as a byte array.

            optionLevel: One of the System.Net.Sockets.SocketOptionLevel values.

            optionName: One of the System.Net.Sockets.SocketOptionName values.

            optionValue: An array of type System.Byte that is to receive the option setting.

        GetSocketOption(self: Socket, optionLevel: SocketOptionLevel, optionName: SocketOptionName, optionLength: int) -> Array[Byte]

            Returns the value of the specified System.Net.Sockets.Socket option in an array.

            optionLevel: One of the System.Net.Sockets.SocketOptionLevel values.

            optionName: One of the System.Net.Sockets.SocketOptionName values.

            optionLength: The length, in bytes, of the expected return value.

            Returns: An array of type System.Byte that contains the value of the socket option.
        """
        ...
    def IOControl(self, ioControlCode, optionInValue, optionOutValue):
        """
        IOControl(self: Socket, ioControlCode: IOControlCode, optionInValue: Array[Byte], optionOutValue: Array[Byte]) -> int

            Sets low-level operating modes for the System.Net.Sockets.Socket using the System.Net.Sockets.IOControlCode enumeration to specify control codes.

            ioControlCode: A System.Net.Sockets.IOControlCode value that specifies the control code of the operation to perform.

            optionInValue: An array of type System.Byte that contains the input data required by the operation.

            optionOutValue: An array of type System.Byte that contains the output data returned by the operation.

            Returns: The number of bytes in the optionOutValue parameter.

        IOControl(self: Socket, ioControlCode: int, optionInValue: Array[Byte], optionOutValue: Array[Byte]) -> int

            Sets low-level operating modes for the System.Net.Sockets.Socket using numerical control codes.

            ioControlCode: An System.Int32 value that specifies the control code of the operation to perform.

            optionInValue: A System.Byte array that contains the input data required by the operation.

            optionOutValue: A System.Byte array that contains the output data returned by the operation.

            Returns: The number of bytes in the optionOutValue parameter.
        """
        ...
    def Listen(self, backlog):
        """
        Listen(self: Socket, backlog: int)

            Places a System.Net.Sockets.Socket in a listening state.

            backlog: The maximum length of the pending connections queue.
        """
        ...
    def Poll(self, microSeconds, mode):
        """
        Poll(self: Socket, microSeconds: int, mode: SelectMode) -> bool

            Determines the status of the System.Net.Sockets.Socket.

            microSeconds: The time to wait for a response, in microseconds.

            mode: One of the System.Net.Sockets.SelectMode values.

            Returns: The status of the System.Net.Sockets.Socket based on the polling mode value passed in the mode parameter.Mode Return Value

             System.Net.Sockets.SelectMode.SelectReadue if System.Net.Sockets.Socket.Listen(System.Int32) has been called and a connection is pending; -or-

                          ue

             if data is available for reading; -or-

                          ue if the connection has been closed, reset, or terminated; otherwise, returns lse.

             System.Net.Sockets.SelectMode.SelectWriteue, if processing a System.Net.Sockets.Socket.Connect(System.Net.EndPoint), and the connection has succeeded; -or-

                     ue if data can be sent; otherwise, returns lse.

                          System.Net.Sockets.SelectMode.SelectErrorue if processing a

             System.Net.Sockets.Socket.Connect(System.Net.EndPoint) that does not block, and the connection has failed; -or-

                          ue if

             System.Net.Sockets.SocketOptionName.OutOfBandInline is not set and out-of-band data is available; otherwise, returns lse.
        """
        ...
    def Receive(self, *__args):
        """
        Receive(self: Socket, buffer: Array[Byte], size: int, socketFlags: SocketFlags) -> int

            Receives the specified number of bytes of data from a bound System.Net.Sockets.Socket into a receive buffer, using the specified System.Net.Sockets.SocketFlags.

            buffer: An array of type System.Byte that is the storage location for the received data.

            size: The number of bytes to receive.

            socketFlags: A bitwise combination of the System.Net.Sockets.SocketFlags values.

            Returns: The number of bytes received.

        Receive(self: Socket, buffer: Array[Byte], socketFlags: SocketFlags) -> int

            Receives data from a bound System.Net.Sockets.Socket into a receive buffer, using the specified System.Net.Sockets.SocketFlags.

            buffer: An array of type System.Byte that is the storage location for the received data.

            socketFlags: A bitwise combination of the System.Net.Sockets.SocketFlags values.

            Returns: The number of bytes received.

        Receive(self: Socket, buffer: Array[Byte]) -> int

            Receives data from a bound System.Net.Sockets.Socket into a receive buffer.

            buffer: An array of type System.Byte that is the storage location for the received data.

            Returns: The number of bytes received.

        Receive(self: Socket, buffer: Array[Byte], offset: int, size: int, socketFlags: SocketFlags) -> int

            Receives the specified number of bytes from a bound System.Net.Sockets.Socket into the specified offset position of the receive buffer, using the specified

             System.Net.Sockets.SocketFlags.

            buffer: An array of type System.Byte that is the storage location for received data.

            offset: The location in buffer to store the received data.

            size: The number of bytes to receive.

            socketFlags: A bitwise combination of the System.Net.Sockets.SocketFlags values.

            Returns: The number of bytes received.

        Receive(self: Socket, buffers: IList[ArraySegment[Byte]]) -> int

        Receive(self: Socket, buffers: IList[ArraySegment[Byte]], socketFlags: SocketFlags) -> int

        Receive(self: Socket, buffers: IList[ArraySegment[Byte]], socketFlags: SocketFlags) -> (int, SocketError)

        Receive(self: Socket, buffer: Array[Byte], offset: int, size: int, socketFlags: SocketFlags) -> (int, SocketError)

            Receives data from a bound System.Net.Sockets.Socket into a receive buffer, using the specified System.Net.Sockets.SocketFlags.

            buffer: An array of type System.Byte that is the storage location for the received data.

            offset: The position in the buffer parameter to store the received data.

            size: The number of bytes to receive.

            socketFlags: A bitwise combination of the System.Net.Sockets.SocketFlags values.

            Returns: The number of bytes received.
        """
        ...
    def ReceiveAsync(self, e):
        """
        ReceiveAsync(self: Socket, e: SocketAsyncEventArgs) -> bool

            Begins an asynchronous request to receive data from a connected System.Net.Sockets.Socket object.

            e: The System.Net.Sockets.SocketAsyncEventArgs object to use for this asynchronous socket operation.

            Returns: Returns ue if the I/O operation is pending. The System.Net.Sockets.SocketAsyncEventArgs.Completed event on the e parameter will be raised upon completion of the

             operation. Returns lse if the I/O operation completed synchronously. In this case, The System.Net.Sockets.SocketAsyncEventArgs.Completed event on the e parameter will

             not be raised and the e object passed as a parameter may be examined immediately after the method call returns to retrieve the result of the operation.
        """
        ...
    def ReceiveFrom(self, buffer, *__args):
        """
        ReceiveFrom(self: Socket, buffer: Array[Byte], size: int, socketFlags: SocketFlags, remoteEP: EndPoint) -> (int, EndPoint)

            Receives the specified number of bytes into the data buffer, using the specified System.Net.Sockets.SocketFlags, and stores the endpoint.

            buffer: An array of type System.Byte that is the storage location for received data.

            size: The number of bytes to receive.

            socketFlags: A bitwise combination of the System.Net.Sockets.SocketFlags values.

            remoteEP: An System.Net.EndPoint, passed by reference, that represents the remote server.

            Returns: The number of bytes received.

        ReceiveFrom(self: Socket, buffer: Array[Byte], socketFlags: SocketFlags, remoteEP: EndPoint) -> (int, EndPoint)

            Receives a datagram into the data buffer, using the specified System.Net.Sockets.SocketFlags, and stores the endpoint.

            buffer: An array of type System.Byte that is the storage location for the received data.

            socketFlags: A bitwise combination of the System.Net.Sockets.SocketFlags values.

            remoteEP: An System.Net.EndPoint, passed by reference, that represents the remote server.

            Returns: The number of bytes received.

        ReceiveFrom(self: Socket, buffer: Array[Byte], remoteEP: EndPoint) -> (int, EndPoint)

            Receives a datagram into the data buffer and stores the endpoint.

            buffer: An array of type System.Byte that is the storage location for received data.

            remoteEP: An System.Net.EndPoint, passed by reference, that represents the remote server.

            Returns: The number of bytes received.

        ReceiveFrom(self: Socket, buffer: Array[Byte], offset: int, size: int, socketFlags: SocketFlags, remoteEP: EndPoint) -> (int, EndPoint)

            Receives the specified number of bytes of data into the specified location of the data buffer, using the specified System.Net.Sockets.SocketFlags, and stores the

             endpoint.

            buffer: An array of type System.Byte that is the storage location for received data.

            offset: The position in the buffer parameter to store the received data.

            size: The number of bytes to receive.

            socketFlags: A bitwise combination of the System.Net.Sockets.SocketFlags values.

            remoteEP: An System.Net.EndPoint, passed by reference, that represents the remote server.

            Returns: The number of bytes received.
        """
        ...
    def ReceiveFromAsync(self, e):
        """
        ReceiveFromAsync(self: Socket, e: SocketAsyncEventArgs) -> bool

            Begins to asynchronously receive data from a specified network device.

            e: The System.Net.Sockets.SocketAsyncEventArgs object to use for this asynchronous socket operation.

            Returns: Returns ue if the I/O operation is pending. The System.Net.Sockets.SocketAsyncEventArgs.Completed event on the e parameter will be raised upon completion of the

             operation. Returns lse if the I/O operation completed synchronously. In this case, The System.Net.Sockets.SocketAsyncEventArgs.Completed event on the e parameter will

             not be raised and the e object passed as a parameter may be examined immediately after the method call returns to retrieve the result of the operation.
        """
        ...
    def ReceiveMessageFrom(self, buffer, offset, size, socketFlags, remoteEP, ipPacketInformation):
        """
        ReceiveMessageFrom(self: Socket, buffer: Array[Byte], offset: int, size: int, socketFlags: SocketFlags, remoteEP: EndPoint) -> (int, SocketFlags, EndPoint, IPPacketInformation)

            Receives the specified number of bytes of data into the specified location of the data buffer, using the specified System.Net.Sockets.SocketFlags, and stores the

             endpoint and packet information.

            buffer: An array of type System.Byte that is the storage location for received data.

            offset: The position in the buffer parameter to store the received data.

            size: The number of bytes to receive.

            socketFlags: A bitwise combination of the System.Net.Sockets.SocketFlags values.

            remoteEP: An System.Net.EndPoint, passed by reference, that represents the remote server.

            Returns: The number of bytes received.
        """
        ...
    def ReceiveMessageFromAsync(self, e):
        """
        ReceiveMessageFromAsync(self: Socket, e: SocketAsyncEventArgs) -> bool

            Begins to asynchronously receive the specified number of bytes of data into the specified location in the data buffer, using the specified

             System.Net.Sockets.SocketAsyncEventArgs.SocketFlags, and stores the endpoint and packet information.

            e: The System.Net.Sockets.SocketAsyncEventArgs object to use for this asynchronous socket operation.

            Returns: Returns ue if the I/O operation is pending. The System.Net.Sockets.SocketAsyncEventArgs.Completed event on the e parameter will be raised upon completion of the

             operation. Returns lse if the I/O operation completed synchronously. In this case, The System.Net.Sockets.SocketAsyncEventArgs.Completed event on the e parameter will

             not be raised and the e object passed as a parameter may be examined immediately after the method call returns to retrieve the result of the operation.
        """
        ...
    @staticmethod
    def Select(checkRead, checkWrite, checkError, microSeconds):
        """
        Select(checkRead: IList, checkWrite: IList, checkError: IList, microSeconds: int)

            Determines the status of one or more sockets.

            checkRead: An System.Collections.IList of System.Net.Sockets.Socket instances to check for readability.

            checkWrite: An System.Collections.IList of System.Net.Sockets.Socket instances to check for writability.

            checkError: An System.Collections.IList of System.Net.Sockets.Socket instances to check for errors.

            microSeconds: The time-out value, in microseconds. A -1 value indicates an infinite time-out.
        """
        ...
    def Send(self, *__args):
        """
        Send(self: Socket, buffer: Array[Byte], size: int, socketFlags: SocketFlags) -> int

            Sends the specified number of bytes of data to a connected System.Net.Sockets.Socket, using the specified System.Net.Sockets.SocketFlags.

            buffer: An array of type System.Byte that contains the data to be sent.

            size: The number of bytes to send.

            socketFlags: A bitwise combination of the System.Net.Sockets.SocketFlags values.

            Returns: The number of bytes sent to the System.Net.Sockets.Socket.

        Send(self: Socket, buffer: Array[Byte], socketFlags: SocketFlags) -> int

            Sends data to a connected System.Net.Sockets.Socket using the specified System.Net.Sockets.SocketFlags.

            buffer: An array of type System.Byte that contains the data to be sent.

            socketFlags: A bitwise combination of the System.Net.Sockets.SocketFlags values.

            Returns: The number of bytes sent to the System.Net.Sockets.Socket.

        Send(self: Socket, buffer: Array[Byte]) -> int

            Sends data to a connected System.Net.Sockets.Socket.

            buffer: An array of type System.Byte that contains the data to be sent.

            Returns: The number of bytes sent to the System.Net.Sockets.Socket.

        Send(self: Socket, buffers: IList[ArraySegment[Byte]]) -> int

        Send(self: Socket, buffers: IList[ArraySegment[Byte]], socketFlags: SocketFlags) -> int

        Send(self: Socket, buffer: Array[Byte], offset: int, size: int, socketFlags: SocketFlags) -> int

            Sends the specified number of bytes of data to a connected System.Net.Sockets.Socket, starting at the specified offset, and using the specified

             System.Net.Sockets.SocketFlags.

            buffer: An array of type System.Byte that contains the data to be sent.

            offset: The position in the data buffer at which to begin sending data.

            size: The number of bytes to send.

            socketFlags: A bitwise combination of the System.Net.Sockets.SocketFlags values.

            Returns: The number of bytes sent to the System.Net.Sockets.Socket.

        Send(self: Socket, buffers: IList[ArraySegment[Byte]], socketFlags: SocketFlags) -> (int, SocketError)

        Send(self: Socket, buffer: Array[Byte], offset: int, size: int, socketFlags: SocketFlags) -> (int, SocketError)

            Sends the specified number of bytes of data to a connected System.Net.Sockets.Socket, starting at the specified offset, and using the specified

             System.Net.Sockets.SocketFlags

            buffer: An array of type System.Byte that contains the data to be sent.

            offset: The position in the data buffer at which to begin sending data.

            size: The number of bytes to send.

            socketFlags: A bitwise combination of the System.Net.Sockets.SocketFlags values.

            Returns: The number of bytes sent to the System.Net.Sockets.Socket.
        """
        ...
    def SendAsync(self, e):
        """
        SendAsync(self: Socket, e: SocketAsyncEventArgs) -> bool

            Sends data asynchronously to a connected System.Net.Sockets.Socket object.

            e: The System.Net.Sockets.SocketAsyncEventArgs object to use for this asynchronous socket operation.

            Returns: Returns ue if the I/O operation is pending. The System.Net.Sockets.SocketAsyncEventArgs.Completed event on the e parameter will be raised upon completion of the

             operation. Returns lse if the I/O operation completed synchronously. In this case, The System.Net.Sockets.SocketAsyncEventArgs.Completed event on the e parameter will

             not be raised and the e object passed as a parameter may be examined immediately after the method call returns to retrieve the result of the operation.
        """
        ...
    def SendFile(self, fileName, preBuffer=None, postBuffer=None, flags=None):
        """
        SendFile(self: Socket, fileName: str)

            Sends the file fileName to a connected System.Net.Sockets.Socket object with the System.Net.Sockets.TransmitFileOptions.UseDefaultWorkerThread transmit flag.

            fileName: A System.String that contains the path and name of the file to be sent. This parameter can be ll.

        SendFile(self: Socket, fileName: str, preBuffer: Array[Byte], postBuffer: Array[Byte], flags: TransmitFileOptions)

            Sends the file fileName and buffers of data to a connected System.Net.Sockets.Socket object using the specified System.Net.Sockets.TransmitFileOptions value.

            fileName: A System.String that contains the path and name of the file to be sent. This parameter can be ll.

            preBuffer: A System.Byte array that contains data to be sent before the file is sent. This parameter can be ll.

            postBuffer: A System.Byte array that contains data to be sent after the file is sent. This parameter can be ll.

            flags: One or more of System.Net.Sockets.TransmitFileOptions values.
        """
        ...
    def SendPacketsAsync(self, e):
        """
        SendPacketsAsync(self: Socket, e: SocketAsyncEventArgs) -> bool

            Sends a collection of files or in memory data buffers asynchronously to a connected System.Net.Sockets.Socket object.

            e: The System.Net.Sockets.SocketAsyncEventArgs object to use for this asynchronous socket operation.

            Returns: Returns ue if the I/O operation is pending. The System.Net.Sockets.SocketAsyncEventArgs.Completed event on the e parameter will be raised upon completion of the

             operation. Returns lse if the I/O operation completed synchronously. In this case, The System.Net.Sockets.SocketAsyncEventArgs.Completed event on the e parameter will

             not be raised and the e object passed as a parameter may be examined immediately after the method call returns to retrieve the result of the operation.
        """
        ...
    def SendTo(self, buffer, *__args):
        """
        SendTo(self: Socket, buffer: Array[Byte], size: int, socketFlags: SocketFlags, remoteEP: EndPoint) -> int

            Sends the specified number of bytes of data to the specified endpoint using the specified System.Net.Sockets.SocketFlags.

            buffer: An array of type System.Byte that contains the data to be sent.

            size: The number of bytes to send.

            socketFlags: A bitwise combination of the System.Net.Sockets.SocketFlags values.

            remoteEP: The System.Net.EndPoint that represents the destination location for the data.

            Returns: The number of bytes sent.

        SendTo(self: Socket, buffer: Array[Byte], socketFlags: SocketFlags, remoteEP: EndPoint) -> int

            Sends data to a specific endpoint using the specified System.Net.Sockets.SocketFlags.

            buffer: An array of type System.Byte that contains the data to be sent.

            socketFlags: A bitwise combination of the System.Net.Sockets.SocketFlags values.

            remoteEP: The System.Net.EndPoint that represents the destination location for the data.

            Returns: The number of bytes sent.

        SendTo(self: Socket, buffer: Array[Byte], remoteEP: EndPoint) -> int

            Sends data to the specified endpoint.

            buffer: An array of type System.Byte that contains the data to be sent.

            remoteEP: The System.Net.EndPoint that represents the destination for the data.

            Returns: The number of bytes sent.

        SendTo(self: Socket, buffer: Array[Byte], offset: int, size: int, socketFlags: SocketFlags, remoteEP: EndPoint) -> int

            Sends the specified number of bytes of data to the specified endpoint, starting at the specified location in the buffer, and using the specified

             System.Net.Sockets.SocketFlags.

            buffer: An array of type System.Byte that contains the data to be sent.

            offset: The position in the data buffer at which to begin sending data.

            size: The number of bytes to send.

            socketFlags: A bitwise combination of the System.Net.Sockets.SocketFlags values.

            remoteEP: The System.Net.EndPoint that represents the destination location for the data.

            Returns: The number of bytes sent.
        """
        ...
    def SendToAsync(self, e):
        """
        SendToAsync(self: Socket, e: SocketAsyncEventArgs) -> bool

            Sends data asynchronously to a specific remote host.

            e: The System.Net.Sockets.SocketAsyncEventArgs object to use for this asynchronous socket operation.

            Returns: Returns ue if the I/O operation is pending. The System.Net.Sockets.SocketAsyncEventArgs.Completed event on the e parameter will be raised upon completion of the

             operation. Returns lse if the I/O operation completed synchronously. In this case, The System.Net.Sockets.SocketAsyncEventArgs.Completed event on the e parameter will

             not be raised and the e object passed as a parameter may be examined immediately after the method call returns to retrieve the result of the operation.
        """
        ...
    def SetIPProtectionLevel(self, level):
        """
        SetIPProtectionLevel(self: Socket, level: IPProtectionLevel)

            Set the IP protection level on a socket.

            level: The IP protection level to set on this socket.
        """
        ...
    def SetSocketOption(self, optionLevel, optionName, optionValue):
        """
        SetSocketOption(self: Socket, optionLevel: SocketOptionLevel, optionName: SocketOptionName, optionValue: int)

            Sets the specified System.Net.Sockets.Socket option to the specified integer value.

            optionLevel: One of the System.Net.Sockets.SocketOptionLevel values.

            optionName: One of the System.Net.Sockets.SocketOptionName values.

            optionValue: A value of the option.

        SetSocketOption(self: Socket, optionLevel: SocketOptionLevel, optionName: SocketOptionName, optionValue: bool)

            Sets the specified System.Net.Sockets.Socket option to the specified System.Boolean value.

            optionLevel: One of the System.Net.Sockets.SocketOptionLevel values.

            optionName: One of the System.Net.Sockets.SocketOptionName values.

            optionValue: The value of the option, represented as a System.Boolean.

        SetSocketOption(self: Socket, optionLevel: SocketOptionLevel, optionName: SocketOptionName, optionValue: Array[Byte])

            Sets the specified System.Net.Sockets.Socket option to the specified value, represented as a byte array.

            optionLevel: One of the System.Net.Sockets.SocketOptionLevel values.

            optionName: One of the System.Net.Sockets.SocketOptionName values.

            optionValue: An array of type System.Byte that represents the value of the option.

        SetSocketOption(self: Socket, optionLevel: SocketOptionLevel, optionName: SocketOptionName, optionValue: object)

            Sets the specified System.Net.Sockets.Socket option to the specified value, represented as an object.

            optionLevel: One of the System.Net.Sockets.SocketOptionLevel values.

            optionName: One of the System.Net.Sockets.SocketOptionName values.

            optionValue: A System.Net.Sockets.LingerOption or System.Net.Sockets.MulticastOption that contains the value of the option.
        """
        ...
    def Shutdown(self, how):
        """
        Shutdown(self: Socket, how: SocketShutdown)

            Disables sends and receives on a System.Net.Sockets.Socket.

            how: One of the System.Net.Sockets.SocketShutdown values that specifies the operation that will no longer be allowed.
        """
        ...
    @property
    def AddressFamily(self):
        """
        Gets the address family of the System.Net.Sockets.Socket.

        Get: AddressFamily(self: Socket) -> AddressFamily
        """
        ...
    @property
    def Available(self):
        """
        Gets the amount of data that has been received from the network and is available to be read.

        Get: Available(self: Socket) -> int
        """
        ...
    @property
    def Blocking(self):
        """
        Gets or sets a value that indicates whether the System.Net.Sockets.Socket is in blocking mode.

        Get: Blocking(self: Socket) -> bool

        Set: Blocking(self: Socket) = value
        """
        ...
    @property
    def Connected(self):
        """
        Gets a value that indicates whether a System.Net.Sockets.Socket is connected to a remote host as of the last erload:System.Net.Sockets.Socket.Send or erload:System.Net.Sockets.Socket.Receive operation.

        Get: Connected(self: Socket) -> bool
        """
        ...
    @property
    def DontFragment(self):
        """
        Gets or sets a System.Boolean value that specifies whether the System.Net.Sockets.Socket allows Internet Protocol (IP) datagrams to be fragmented.

        Get: DontFragment(self: Socket) -> bool

        Set: DontFragment(self: Socket) = value
        """
        ...
    @property
    def DualMode(self):
        """
        Gets or sets a System.Boolean value that specifies whether the System.Net.Sockets.Socket is a dual-mode socket used for both IPv4 and IPv6.

        Get: DualMode(self: Socket) -> bool

        Set: DualMode(self: Socket) = value
        """
        ...
    @property
    def EnableBroadcast(self):
        """
        Gets or sets a System.Boolean value that specifies whether the System.Net.Sockets.Socket can send or receive broadcast packets.

        Get: EnableBroadcast(self: Socket) -> bool

        Set: EnableBroadcast(self: Socket) = value
        """
        ...
    @property
    def ExclusiveAddressUse(self):
        """
        Gets or sets a System.Boolean value that specifies whether the System.Net.Sockets.Socket allows only one process to bind to a port.

        Get: ExclusiveAddressUse(self: Socket) -> bool

        Set: ExclusiveAddressUse(self: Socket) = value
        """
        ...
    @property
    def Handle(self):
        """
        Gets the operating system handle for the System.Net.Sockets.Socket.

        Get: Handle(self: Socket) -> IntPtr
        """
        ...
    @property
    def IsBound(self):
        """
        Gets a value that indicates whether the System.Net.Sockets.Socket is bound to a specific local port.

        Get: IsBound(self: Socket) -> bool
        """
        ...
    @property
    def LingerState(self):
        """
        Gets or sets a value that specifies whether the System.Net.Sockets.Socket will delay closing a socket in an attempt to send all pending data.

        Get: LingerState(self: Socket) -> LingerOption

        Set: LingerState(self: Socket) = value
        """
        ...
    @property
    def LocalEndPoint(self):
        """
        Gets the local endpoint.

        Get: LocalEndPoint(self: Socket) -> EndPoint
        """
        ...
    @property
    def MulticastLoopback(self):
        """
        Gets or sets a value that specifies whether outgoing multicast packets are delivered to the sending application.

        Get: MulticastLoopback(self: Socket) -> bool

        Set: MulticastLoopback(self: Socket) = value
        """
        ...
    @property
    def NoDelay(self):
        """
        Gets or sets a System.Boolean value that specifies whether the stream System.Net.Sockets.Socket is using the Nagle algorithm.

        Get: NoDelay(self: Socket) -> bool

        Set: NoDelay(self: Socket) = value
        """
        ...
    @property
    def ProtocolType(self):
        """
        Gets the protocol type of the System.Net.Sockets.Socket.

        Get: ProtocolType(self: Socket) -> ProtocolType
        """
        ...
    @property
    def ReceiveBufferSize(self):
        """
        Gets or sets a value that specifies the size of the receive buffer of the System.Net.Sockets.Socket.

        Get: ReceiveBufferSize(self: Socket) -> int

        Set: ReceiveBufferSize(self: Socket) = value
        """
        ...
    @property
    def ReceiveTimeout(self):
        """
        Gets or sets a value that specifies the amount of time after which a synchronous erload:System.Net.Sockets.Socket.Receive call will time out.

        Get: ReceiveTimeout(self: Socket) -> int

        Set: ReceiveTimeout(self: Socket) = value
        """
        ...
    @property
    def RemoteEndPoint(self):
        """
        Gets the remote endpoint.

        Get: RemoteEndPoint(self: Socket) -> EndPoint
        """
        ...
    @property
    def SendBufferSize(self):
        """
        Gets or sets a value that specifies the size of the send buffer of the System.Net.Sockets.Socket.

        Get: SendBufferSize(self: Socket) -> int

        Set: SendBufferSize(self: Socket) = value
        """
        ...
    @property
    def SendTimeout(self):
        """
        Gets or sets a value that specifies the amount of time after which a synchronous erload:System.Net.Sockets.Socket.Send call will time out.

        Get: SendTimeout(self: Socket) -> int

        Set: SendTimeout(self: Socket) = value
        """
        ...
    @property
    def SocketType(self):
        """
        Gets the type of the System.Net.Sockets.Socket.

        Get: SocketType(self: Socket) -> SocketType
        """
        ...
    @property
    def Ttl(self):
        """
        Gets or sets a value that specifies the Time To Live (TTL) value of Internet Protocol (IP) packets sent by the System.Net.Sockets.Socket.

        Get: Ttl(self: Socket) -> Int16

        Set: Ttl(self: Socket) = value
        """
        ...
    @property
    def UseOnlyOverlappedIO(self):
        """
        Specifies whether the socket should only use Overlapped I/O mode.

        Get: UseOnlyOverlappedIO(self: Socket) -> bool

        Set: UseOnlyOverlappedIO(self: Socket) = value
        """
        ...
    OSSupportsIPv4 = True
    OSSupportsIPv6 = True
    SupportsIPv4 = True
    SupportsIPv6 = False

class SocketAsyncEventArgs(EventArgs, IDisposable):
    """
    Represents an asynchronous socket operation.

    SocketAsyncEventArgs()
    """

    def OnCompleted(self, *args):  # cannot find CLR method
        """
        OnCompleted(self: SocketAsyncEventArgs, e: SocketAsyncEventArgs)

            Represents a method that is called when an asynchronous operation completes.

            e: The event that is signaled.
        """
        ...
    def SetBuffer(self, *__args):
        """
        SetBuffer(self: SocketAsyncEventArgs, buffer: Array[Byte], offset: int, count: int)

            Sets the data buffer to use with an asynchronous socket method.

            buffer: The data buffer to use with an asynchronous socket method.

            offset: The offset, in bytes, in the data buffer where the operation starts.

            count: The maximum amount of data, in bytes, to send or receive in the buffer.

        SetBuffer(self: SocketAsyncEventArgs, offset: int, count: int)

            Sets the data buffer to use with an asynchronous socket method.

            offset: The offset, in bytes, in the data buffer where the operation starts.

            count: The maximum amount of data, in bytes, to send or receive in the buffer.
        """
        ...
    @property
    def AcceptSocket(self):
        """
        Gets or sets the socket to use or the socket created for accepting a connection with an asynchronous socket method.

        Get: AcceptSocket(self: SocketAsyncEventArgs) -> Socket

        Set: AcceptSocket(self: SocketAsyncEventArgs) = value
        """
        ...
    @property
    def Buffer(self):
        """
        Gets the data buffer to use with an asynchronous socket method.

        Get: Buffer(self: SocketAsyncEventArgs) -> Array[Byte]
        """
        ...
    @property
    def BufferList(self):
        """
        Gets or sets an array of data buffers to use with an asynchronous socket method.

        Get: BufferList(self: SocketAsyncEventArgs) -> IList[ArraySegment[Byte]]

        Set: BufferList(self: SocketAsyncEventArgs) = value
        """
        ...
    @property
    def BytesTransferred(self):
        """
        Gets the number of bytes transferred in the socket operation.

        Get: BytesTransferred(self: SocketAsyncEventArgs) -> int
        """
        ...
    @property
    def ConnectByNameError(self):
        """
        Gets the exception in the case of a connection failure when a System.Net.DnsEndPoint was used.

        Get: ConnectByNameError(self: SocketAsyncEventArgs) -> Exception
        """
        ...
    @property
    def ConnectSocket(self):
        """
        The created and connected System.Net.Sockets.Socket object after successful completion of the erload:System.Net.Sockets.Socket.ConnectAsync method.

        Get: ConnectSocket(self: SocketAsyncEventArgs) -> Socket
        """
        ...
    @property
    def Count(self):
        """
        Gets the maximum amount of data, in bytes, to send or receive in an asynchronous operation.

        Get: Count(self: SocketAsyncEventArgs) -> int
        """
        ...
    @property
    def DisconnectReuseSocket(self):
        """
        Gets or sets a value that specifies if socket can be reused after a disconnect operation.

        Get: DisconnectReuseSocket(self: SocketAsyncEventArgs) -> bool

        Set: DisconnectReuseSocket(self: SocketAsyncEventArgs) = value
        """
        ...
    @property
    def LastOperation(self):
        """
        Gets the type of socket operation most recently performed with this context object.

        Get: LastOperation(self: SocketAsyncEventArgs) -> SocketAsyncOperation
        """
        ...
    @property
    def Offset(self):
        """
        Gets the offset, in bytes, into the data buffer referenced by the System.Net.Sockets.SocketAsyncEventArgs.Buffer property.

        Get: Offset(self: SocketAsyncEventArgs) -> int
        """
        ...
    @property
    def ReceiveMessageFromPacketInfo(self):
        """
        Gets the IP address and interface of a received packet.

        Get: ReceiveMessageFromPacketInfo(self: SocketAsyncEventArgs) -> IPPacketInformation
        """
        ...
    @property
    def RemoteEndPoint(self):
        """
        Gets or sets the remote IP endpoint for an asynchronous operation.

        Get: RemoteEndPoint(self: SocketAsyncEventArgs) -> EndPoint

        Set: RemoteEndPoint(self: SocketAsyncEventArgs) = value
        """
        ...
    @property
    def SendPacketsElements(self):
        """
        Gets or sets an array of buffers to be sent for an asynchronous operation used by the System.Net.Sockets.Socket.SendPacketsAsync(System.Net.Sockets.SocketAsyncEventArgs) method.

        Get: SendPacketsElements(self: SocketAsyncEventArgs) -> Array[SendPacketsElement]

        Set: SendPacketsElements(self: SocketAsyncEventArgs) = value
        """
        ...
    @property
    def SendPacketsFlags(self):
        """
        Gets or sets a bitwise combination of System.Net.Sockets.TransmitFileOptions values for an asynchronous operation used by the System.Net.Sockets.Socket.SendPacketsAsync(System.Net.Sockets.SocketAsyncEventArgs) method.

        Get: SendPacketsFlags(self: SocketAsyncEventArgs) -> TransmitFileOptions

        Set: SendPacketsFlags(self: SocketAsyncEventArgs) = value
        """
        ...
    @property
    def SendPacketsSendSize(self):
        """
        Gets or sets the size, in bytes, of the data block used in the send operation.

        Get: SendPacketsSendSize(self: SocketAsyncEventArgs) -> int

        Set: SendPacketsSendSize(self: SocketAsyncEventArgs) = value
        """
        ...
    @property
    def SocketClientAccessPolicyProtocol(self):
        """
        Gets or sets the protocol to use to download the socket client access policy file.

        Get: SocketClientAccessPolicyProtocol(self: SocketAsyncEventArgs) -> SocketClientAccessPolicyProtocol

        Set: SocketClientAccessPolicyProtocol(self: SocketAsyncEventArgs) = value
        """
        ...
    @property
    def SocketError(self):
        """
        Gets or sets the result of the asynchronous socket operation.

        Get: SocketError(self: SocketAsyncEventArgs) -> SocketError

        Set: SocketError(self: SocketAsyncEventArgs) = value
        """
        ...
    @property
    def SocketFlags(self):
        """
        Gets the results of an asynchronous socket operation or sets the behavior of an asynchronous operation.

        Get: SocketFlags(self: SocketAsyncEventArgs) -> SocketFlags

        Set: SocketFlags(self: SocketAsyncEventArgs) = value
        """
        ...
    @property
    def UserToken(self):
        """
        Gets or sets a user or application object associated with this asynchronous socket operation.

        Get: UserToken(self: SocketAsyncEventArgs) -> object

        Set: UserToken(self: SocketAsyncEventArgs) = value
        """
        ...
    Completed = None

class SocketAsyncOperation(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    The type of asynchronous socket operation most recently performed with this context object.

    enum SocketAsyncOperation, values: Accept (1), Connect (2), Disconnect (3), None (0), Receive (4), ReceiveFrom (5), ReceiveMessageFrom (6), Send (7), SendPackets (8), SendTo (9)
    """

    Accept = None
    Connect = None
    Disconnect = None

    Receive = None
    ReceiveFrom = None
    ReceiveMessageFrom = None
    Send = None
    SendPackets = None
    SendTo = None
    value__ = None

class SocketClientAccessPolicyProtocol(
    Enum
):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies the method to download a client access policy file.

    enum SocketClientAccessPolicyProtocol, values: Http (1), Tcp (0)
    """

    Http = None
    Tcp = None
    value__ = None

class SocketError(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Defines error codes for the System.Net.Sockets.Socket class.

    enum SocketError, values: AccessDenied (10013), AddressAlreadyInUse (10048), AddressFamilyNotSupported (10047), AddressNotAvailable (10049), AlreadyInProgress (10037), ConnectionAborted (10053), ConnectionRefused (10061), ConnectionReset (10054), DestinationAddressRequired (10039), Disconnecting (10101), Fault (10014), HostDown (10064), HostNotFound (11001), HostUnreachable (10065), InProgress (10036), Interrupted (10004), InvalidArgument (10022), IOPending (997), IsConnected (10056), MessageSize (10040), NetworkDown (10050), NetworkReset (10052), NetworkUnreachable (10051), NoBufferSpaceAvailable (10055), NoData (11004), NoRecovery (11003), NotConnected (10057), NotInitialized (10093), NotSocket (10038), OperationAborted (995), OperationNotSupported (10045), ProcessLimit (10067), ProtocolFamilyNotSupported (10046), ProtocolNotSupported (10043), ProtocolOption (10042), ProtocolType (10041), Shutdown (10058), SocketError (-1), SocketNotSupported (10044), Success (0), SystemNotReady (10091), TimedOut (10060), TooManyOpenSockets (10024), TryAgain (11002), TypeNotFound (10109), VersionNotSupported (10092), WouldBlock (10035)
    """

    AccessDenied = None
    AddressAlreadyInUse = None
    AddressFamilyNotSupported = None
    AddressNotAvailable = None
    AlreadyInProgress = None
    ConnectionAborted = None
    ConnectionRefused = None
    ConnectionReset = None
    DestinationAddressRequired = None
    Disconnecting = None
    Fault = None
    HostDown = None
    HostNotFound = None
    HostUnreachable = None
    InProgress = None
    Interrupted = None
    InvalidArgument = None
    IOPending = None
    IsConnected = None
    MessageSize = None
    NetworkDown = None
    NetworkReset = None
    NetworkUnreachable = None
    NoBufferSpaceAvailable = None
    NoData = None
    NoRecovery = None
    NotConnected = None
    NotInitialized = None
    NotSocket = None
    OperationAborted = None
    OperationNotSupported = None
    ProcessLimit = None
    ProtocolFamilyNotSupported = None
    ProtocolNotSupported = None
    ProtocolOption = None
    ProtocolType = None
    Shutdown = None
    SocketError = None
    SocketNotSupported = None
    Success = None
    SystemNotReady = None
    TimedOut = None
    TooManyOpenSockets = None
    TryAgain = None
    TypeNotFound = None
    value__ = None
    VersionNotSupported = None
    WouldBlock = None

class SocketException(Win32Exception):  # skipped bases: <type '_Exception'>, <type 'ISerializable'>
    """
    The exception that is thrown when a socket error occurs.

    SocketException()

    SocketException(errorCode: int)
    """

    @property
    def ErrorCode(self):
        """
        Gets the error code that is associated with this exception.

        Get: ErrorCode(self: SocketException) -> int
        """
        ...
    @property
    def Message(self):
        """
        Gets the error message that is associated with this exception.

        Get: Message(self: SocketException) -> str
        """
        ...
    @property
    def SocketErrorCode(self):
        """
        Gets the error code that is associated with this exception.

        Get: SocketErrorCode(self: SocketException) -> SocketError
        """
        ...
    SerializeObjectState = None

class SocketFlags(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies socket send and receive behaviors.

    enum (flags) SocketFlags, values: Broadcast (1024), ControlDataTruncated (512), DontRoute (4), MaxIOVectorLength (16), Multicast (2048), None (0), OutOfBand (1), Partial (32768), Peek (2), Truncated (256)
    """

    Broadcast = None
    ControlDataTruncated = None
    DontRoute = None
    MaxIOVectorLength = None
    Multicast = None

    OutOfBand = None
    Partial = None
    Peek = None
    Truncated = None
    value__ = None

class SocketInformation:  # skipped bases: <type 'object'>
    """Encapsulates the information that is necessary to duplicate a System.Net.Sockets.Socket."""

    @property
    def Options(self):
        """
        Gets or sets the options for a System.Net.Sockets.Socket.

        Get: Options(self: SocketInformation) -> SocketInformationOptions

        Set: Options(self: SocketInformation) = value
        """
        ...
    @property
    def ProtocolInformation(self):
        """
        Gets or sets the protocol information for a System.Net.Sockets.Socket.

        Get: ProtocolInformation(self: SocketInformation) -> Array[Byte]

        Set: ProtocolInformation(self: SocketInformation) = value
        """
        ...

class SocketInformationOptions(
    Enum
):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Describes states for a System.Net.Sockets.Socket.

    enum (flags) SocketInformationOptions, values: Connected (2), Listening (4), NonBlocking (1), UseOnlyOverlappedIO (8)
    """

    Connected = None
    Listening = None
    NonBlocking = None
    UseOnlyOverlappedIO = None
    value__ = None

class SocketOptionLevel(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Defines socket option levels for the System.Net.Sockets.Socket.SetSocketOption(System.Net.Sockets.SocketOptionLevel,System.Net.Sockets.SocketOptionName,System.Int32) and System.Net.Sockets.Socket.GetSocketOption(System.Net.Sockets.SocketOptionLevel,System.Net.Sockets.SocketOptionName) methods.

    enum SocketOptionLevel, values: IP (0), IPv6 (41), Socket (65535), Tcp (6), Udp (17)
    """

    IP = None
    IPv6 = None
    Socket = None
    Tcp = None
    Udp = None
    value__ = None

class SocketOptionName(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Defines configuration option names.

    enum SocketOptionName, values: AcceptConnection (2), AddMembership (12), AddSourceMembership (15), BlockSource (17), Broadcast (32), BsdUrgent (2), ChecksumCoverage (20), Debug (1), DontFragment (14), DontLinger (-129), DontRoute (16), DropMembership (13), DropSourceMembership (16), Error (4103), ExclusiveAddressUse (-5), Expedited (2), HeaderIncluded (2), HopLimit (21), IPOptions (1), IPProtectionLevel (23), IpTimeToLive (4), IPv6Only (27), KeepAlive (8), Linger (128), MaxConnections (2147483647), MulticastInterface (9), MulticastLoopback (11), MulticastTimeToLive (10), NoChecksum (1), NoDelay (1), OutOfBandInline (256), PacketInformation (19), ReceiveBuffer (4098), ReceiveLowWater (4100), ReceiveTimeout (4102), ReuseAddress (4), ReuseUnicastPort (12295), SendBuffer (4097), SendLowWater (4099), SendTimeout (4101), Type (4104), TypeOfService (3), UnblockSource (18), UpdateAcceptContext (28683), UpdateConnectContext (28688), UseLoopback (64)
    """

    AcceptConnection = None
    AddMembership = None
    AddSourceMembership = None
    BlockSource = None
    Broadcast = None
    BsdUrgent = None
    ChecksumCoverage = None
    Debug = None
    DontFragment = None
    DontLinger = None
    DontRoute = None
    DropMembership = None
    DropSourceMembership = None
    Error = None
    ExclusiveAddressUse = None
    Expedited = None
    HeaderIncluded = None
    HopLimit = None
    IPOptions = None
    IPProtectionLevel = None
    IpTimeToLive = None
    IPv6Only = None
    KeepAlive = None
    Linger = None
    MaxConnections = None
    MulticastInterface = None
    MulticastLoopback = None
    MulticastTimeToLive = None
    NoChecksum = None
    NoDelay = None
    OutOfBandInline = None
    PacketInformation = None
    ReceiveBuffer = None
    ReceiveLowWater = None
    ReceiveTimeout = None
    ReuseAddress = None
    ReuseUnicastPort = None
    SendBuffer = None
    SendLowWater = None
    SendTimeout = None
    Type = None
    TypeOfService = None
    UnblockSource = None
    UpdateAcceptContext = None
    UpdateConnectContext = None
    UseLoopback = None
    value__ = None

class SocketReceiveFromResult:  # skipped bases: <type 'object'>
    """The result of a System.Net.Sockets.SocketTaskExtensions.ReceiveFromAsync(System.Net.Sockets.Socket,System.ArraySegment{System.Byte},System.Net.Sockets.SocketFlags,System.Net.EndPoint) operation."""

    ReceivedBytes = None
    RemoteEndPoint = None

class SocketReceiveMessageFromResult:  # skipped bases: <type 'object'>
    """The result of a System.Net.Sockets.SocketTaskExtensions.ReceiveMessageFromAsync(System.Net.Sockets.Socket,System.ArraySegment{System.Byte},System.Net.Sockets.SocketFlags,System.Net.EndPoint) operation."""

    PacketInformation = None
    ReceivedBytes = None
    RemoteEndPoint = None
    SocketFlags = None

class SocketShutdown(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Defines constants that are used by the System.Net.Sockets.Socket.Shutdown(System.Net.Sockets.SocketShutdown) method.

    enum SocketShutdown, values: Both (2), Receive (0), Send (1)
    """

    Both = None
    Receive = None
    Send = None
    value__ = None

class SocketTaskExtensions:  # skipped bases: <type 'object'>
    """This class contains extension methods to the System.Net.Sockets.Socket class."""

    @staticmethod
    def AcceptAsync(socket, acceptSocket=None):
        """
        AcceptAsync(socket: Socket) -> Task[Socket]

            Performs an asynchronous operation on to accept an incoming connection attempt on the socket.

            socket: The socket that is listening for connections.

            Returns: An asynchronous task that completes with a System.Net.Sockets.Socket to handle communication with the remote host.

        AcceptAsync(socket: Socket, acceptSocket: Socket) -> Task[Socket]

            Performs an asynchronous operation on to accept an incoming connection attempt on the socket.

            socket: The socket that is listening for incoming connections.

            acceptSocket: The accepted System.Net.Sockets.Socket object. This value may be ll.

            Returns: An asynchronous task that completes with a System.Net.Sockets.Socket to handle communication with the remote host.
        """
        ...
    @staticmethod
    def ConnectAsync(socket, *__args):
        """
        ConnectAsync(socket: Socket, remoteEP: EndPoint) -> Task

            Establishes a connection to a remote host.

            socket: The socket that is used for establishing a connection.

            remoteEP: An EndPoint that represents the remote device.

            Returns: An asynchronous Task.

        ConnectAsync(socket: Socket, address: IPAddress, port: int) -> Task

            Establishes a connection to a remote host. The host is specified by an IP address and a port number.

            socket: The socket to perform the connect operation on.

            address: The IP address of the remote host.

            port: The port number of the remote host.

        ConnectAsync(socket: Socket, addresses: Array[IPAddress], port: int) -> Task

            Establishes a connection to a remote host. The host is specified by an array of IP addresses and a port number.

            socket: The socket that the connect operation is performed on.

            addresses: The IP addresses of the remote host.

            port: The port number of the remote host.

            Returns: A task that represents the asynchronous connect operation.

        ConnectAsync(socket: Socket, host: str, port: int) -> Task

            Establishes a connection to a remote host. The host is specified by a host name and a port number.

            socket: The socket to perform the connect operation on.

            host: The name of the remote host.

            port: The port number of the remote host.

            Returns: Returns an asynchronous Task.
        """
        ...
    @staticmethod
    def ReceiveAsync(socket, *__args):
        """
        ReceiveAsync(socket: Socket, buffers: IList[ArraySegment[Byte]], socketFlags: SocketFlags) -> Task[int]

        ReceiveAsync(socket: Socket, buffer: ArraySegment[Byte], socketFlags: SocketFlags) -> Task[int]
        """
        ...
    @staticmethod
    def ReceiveFromAsync(socket, buffer, socketFlags, remoteEndPoint):
        """ReceiveFromAsync(socket: Socket, buffer: ArraySegment[Byte], socketFlags: SocketFlags, remoteEndPoint: EndPoint) -> Task[SocketReceiveFromResult]"""
        ...
    @staticmethod
    def ReceiveMessageFromAsync(socket, buffer, socketFlags, remoteEndPoint):
        """ReceiveMessageFromAsync(socket: Socket, buffer: ArraySegment[Byte], socketFlags: SocketFlags, remoteEndPoint: EndPoint) -> Task[SocketReceiveMessageFromResult]"""
        ...
    @staticmethod
    def SendAsync(socket, *__args):
        """
        SendAsync(socket: Socket, buffers: IList[ArraySegment[Byte]], socketFlags: SocketFlags) -> Task[int]

        SendAsync(socket: Socket, buffer: ArraySegment[Byte], socketFlags: SocketFlags) -> Task[int]
        """
        ...
    @staticmethod
    def SendToAsync(socket, buffer, socketFlags, remoteEP):
        """SendToAsync(socket: Socket, buffer: ArraySegment[Byte], socketFlags: SocketFlags, remoteEP: EndPoint) -> Task[int]"""
        ...
    __all__ = [
        "AcceptAsync",
        "ConnectAsync",
        "ReceiveAsync",
        "ReceiveFromAsync",
        "ReceiveMessageFromAsync",
        "SendAsync",
        "SendToAsync",
    ]

class SocketType(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies the type of socket that an instance of the System.Net.Sockets.Socket class represents.

    enum SocketType, values: Dgram (2), Raw (3), Rdm (4), Seqpacket (5), Stream (1), Unknown (-1)
    """

    Dgram = None
    Raw = None
    Rdm = None
    Seqpacket = None
    Stream = None
    Unknown = None
    value__ = None

class TcpClient(object, IDisposable):
    """
    Provides client connections for TCP network services.

    TcpClient(localEP: IPEndPoint)

    TcpClient()

    TcpClient(family: AddressFamily)

    TcpClient(hostname: str, port: int)
    """

    def BeginConnect(self, *__args):
        """
        BeginConnect(self: TcpClient, host: str, port: int, requestCallback: AsyncCallback, state: object) -> IAsyncResult

            Begins an asynchronous request for a remote host connection. The remote host is specified by a host name (System.String) and a port number (System.Int32).

            host: The name of the remote host.

            port: The port number of the remote host.

            requestCallback: An System.AsyncCallback delegate that references the method to invoke when the operation is complete.

            state: A user-defined object that contains information about the connect operation. This object is passed to the requestCallback delegate when the operation is complete.

            Returns: An System.IAsyncResult object that references the asynchronous connection.

        BeginConnect(self: TcpClient, address: IPAddress, port: int, requestCallback: AsyncCallback, state: object) -> IAsyncResult

            Begins an asynchronous request for a remote host connection. The remote host is specified by an System.Net.IPAddress and a port number (System.Int32).

            address: The System.Net.IPAddress of the remote host.

            port: The port number of the remote host.

            requestCallback: An System.AsyncCallback delegate that references the method to invoke when the operation is complete.

            state: A user-defined object that contains information about the connect operation. This object is passed to the requestCallback delegate when the operation is complete.

            Returns: An System.IAsyncResult object that references the asynchronous connection.

        BeginConnect(self: TcpClient, addresses: Array[IPAddress], port: int, requestCallback: AsyncCallback, state: object) -> IAsyncResult

            Begins an asynchronous request for a remote host connection. The remote host is specified by an System.Net.IPAddress array and a port number (System.Int32).

            addresses: At least one System.Net.IPAddress that designates the remote hosts.

            port: The port number of the remote hosts.

            requestCallback: An System.AsyncCallback delegate that references the method to invoke when the operation is complete.

            state: A user-defined object that contains information about the connect operation. This object is passed to the requestCallback delegate when the operation is complete.

            Returns: An System.IAsyncResult object that references the asynchronous connection.
        """
        ...
    def Close(self):
        """
        Close(self: TcpClient)

            Disposes this System.Net.Sockets.TcpClient instance and requests that the underlying TCP connection be closed.
        """
        ...
    def Connect(self, *__args):
        """
        Connect(self: TcpClient, hostname: str, port: int)

            Connects the client to the specified port on the specified host.

            hostname: The DNS name of the remote host to which you intend to connect.

            port: The port number of the remote host to which you intend to connect.

        Connect(self: TcpClient, address: IPAddress, port: int)

            Connects the client to a remote TCP host using the specified IP address and port number.

            address: The System.Net.IPAddress of the host to which you intend to connect.

            port: The port number to which you intend to connect.

        Connect(self: TcpClient, remoteEP: IPEndPoint)

            Connects the client to a remote TCP host using the specified remote network endpoint.

            remoteEP: The System.Net.IPEndPoint to which you intend to connect.

        Connect(self: TcpClient, ipAddresses: Array[IPAddress], port: int)

            Connects the client to a remote TCP host using the specified IP addresses and port number.

            ipAddresses: The System.Net.IPAddress array of the host to which you intend to connect.

            port: The port number to which you intend to connect.
        """
        ...
    def ConnectAsync(self, *__args):
        """
        ConnectAsync(self: TcpClient, address: IPAddress, port: int) -> Task

            Connects the client to a remote TCP host using the specified IP address and port number as an asynchronous operation.

            address: The System.Net.IPAddress of the host to which you intend to connect.

            port: The port number to which you intend to connect.

            Returns: Returns System.Threading.Tasks.TaskThe task object representing the asynchronous operation.

        ConnectAsync(self: TcpClient, host: str, port: int) -> Task

            Connects the client to the specified TCP port on the specified host as an asynchronous operation.

            host: The DNS name of the remote host to which you intend to connect.

            port: The port number of the remote host to which you intend to connect.

            Returns: Returns System.Threading.Tasks.TaskThe task object representing the asynchronous operation.

        ConnectAsync(self: TcpClient, addresses: Array[IPAddress], port: int) -> Task

            Connects the client to a remote TCP host using the specified IP addresses and port number as an asynchronous operation.

            addresses: The System.Net.IPAddress array of the host to which you intend to connect.

            port: The port number to which you intend to connect.

            Returns: Returns System.Threading.Tasks.TaskThe task object representing the asynchronous operation.
        """
        ...
    def EndConnect(self, asyncResult):
        """
        EndConnect(self: TcpClient, asyncResult: IAsyncResult)

            Ends a pending asynchronous connection attempt.

            asyncResult: An System.IAsyncResult object returned by a call to erload:System.Net.Sockets.TcpClient.BeginConnect.
        """
        ...
    def GetStream(self):
        """
        GetStream(self: TcpClient) -> NetworkStream

            Returns the System.Net.Sockets.NetworkStream used to send and receive data.

            Returns: The underlying System.Net.Sockets.NetworkStream.
        """
        ...
    @property
    def Active(self):
        """Gets or set a value that indicates whether a connection has been made."""
        ...
    @property
    def Available(self):
        """
        Gets the amount of data that has been received from the network and is available to be read.

        Get: Available(self: TcpClient) -> int
        """
        ...
    @property
    def Client(self):
        """
        Gets or sets the underlying System.Net.Sockets.Socket.

        Get: Client(self: TcpClient) -> Socket

        Set: Client(self: TcpClient) = value
        """
        ...
    @property
    def Connected(self):
        """
        Gets a value indicating whether the underlying System.Net.Sockets.Socket for a System.Net.Sockets.TcpClient is connected to a remote host.

        Get: Connected(self: TcpClient) -> bool
        """
        ...
    @property
    def ExclusiveAddressUse(self):
        """
        Gets or sets a System.Boolean value that specifies whether the System.Net.Sockets.TcpClient allows only one client to use a port.

        Get: ExclusiveAddressUse(self: TcpClient) -> bool

        Set: ExclusiveAddressUse(self: TcpClient) = value
        """
        ...
    @property
    def LingerState(self):
        """
        Gets or sets information about the linger state of the associated socket.

        Get: LingerState(self: TcpClient) -> LingerOption

        Set: LingerState(self: TcpClient) = value
        """
        ...
    @property
    def NoDelay(self):
        """
        Gets or sets a value that disables a delay when send or receive buffers are not full.

        Get: NoDelay(self: TcpClient) -> bool

        Set: NoDelay(self: TcpClient) = value
        """
        ...
    @property
    def ReceiveBufferSize(self):
        """
        Gets or sets the size of the receive buffer.

        Get: ReceiveBufferSize(self: TcpClient) -> int

        Set: ReceiveBufferSize(self: TcpClient) = value
        """
        ...
    @property
    def ReceiveTimeout(self):
        """
        Gets or sets the amount of time a System.Net.Sockets.TcpClient will wait to receive data once a read operation is initiated.

        Get: ReceiveTimeout(self: TcpClient) -> int

        Set: ReceiveTimeout(self: TcpClient) = value
        """
        ...
    @property
    def SendBufferSize(self):
        """
        Gets or sets the size of the send buffer.

        Get: SendBufferSize(self: TcpClient) -> int

        Set: SendBufferSize(self: TcpClient) = value
        """
        ...
    @property
    def SendTimeout(self):
        """
        Gets or sets the amount of time a System.Net.Sockets.TcpClient will wait for a send operation to complete successfully.

        Get: SendTimeout(self: TcpClient) -> int

        Set: SendTimeout(self: TcpClient) = value
        """
        ...

class TcpListener:  # skipped bases: <type 'object'>
    """
    Listens for connections from TCP network clients.

    TcpListener(localEP: IPEndPoint)

    TcpListener(localaddr: IPAddress, port: int)

    TcpListener(port: int)
    """

    def AcceptSocket(self):
        """
        AcceptSocket(self: TcpListener) -> Socket

            Accepts a pending connection request.

            Returns: A System.Net.Sockets.Socket used to send and receive data.
        """
        ...
    def AcceptSocketAsync(self):
        """
        AcceptSocketAsync(self: TcpListener) -> Task[Socket]

            Accepts a pending connection request as an asynchronous operation.

            Returns: Returns System.Threading.Tasks.TaskThe task object representing the asynchronous operation. The System.Threading.Tasks.Task property on the task object returns a

             System.Net.Sockets.Socket used to send and receive data.
        """
        ...
    def AcceptTcpClient(self):
        """
        AcceptTcpClient(self: TcpListener) -> TcpClient

            Accepts a pending connection request.

            Returns: A System.Net.Sockets.TcpClient used to send and receive data.
        """
        ...
    def AcceptTcpClientAsync(self):
        """
        AcceptTcpClientAsync(self: TcpListener) -> Task[TcpClient]

            Accepts a pending connection request as an asynchronous operation.

            Returns: Returns System.Threading.Tasks.TaskThe task object representing the asynchronous operation. The System.Threading.Tasks.Task property on the task object returns a

             System.Net.Sockets.TcpClient used to send and receive data.
        """
        ...
    def AllowNatTraversal(self, allowed):
        """
        AllowNatTraversal(self: TcpListener, allowed: bool)

            Enables or disables Network Address Translation (NAT) traversal on a System.Net.Sockets.TcpListener instance.

            allowed: A Boolean value that specifies whether to enable or disable NAT traversal.
        """
        ...
    def BeginAcceptSocket(self, callback, state):
        """
        BeginAcceptSocket(self: TcpListener, callback: AsyncCallback, state: object) -> IAsyncResult

            Begins an asynchronous operation to accept an incoming connection attempt.

            callback: An System.AsyncCallback delegate that references the method to invoke when the operation is complete.

            state: A user-defined object containing information about the accept operation. This object is passed to the callback delegate when the operation is complete.

            Returns: An System.IAsyncResult that references the asynchronous creation of the System.Net.Sockets.Socket.
        """
        ...
    def BeginAcceptTcpClient(self, callback, state):
        """
        BeginAcceptTcpClient(self: TcpListener, callback: AsyncCallback, state: object) -> IAsyncResult

            Begins an asynchronous operation to accept an incoming connection attempt.

            callback: An System.AsyncCallback delegate that references the method to invoke when the operation is complete.

            state: A user-defined object containing information about the accept operation. This object is passed to the callback delegate when the operation is complete.

            Returns: An System.IAsyncResult that references the asynchronous creation of the System.Net.Sockets.TcpClient.
        """
        ...
    @staticmethod
    def Create(port):
        """
        Create(port: int) -> TcpListener

            Creates a new System.Net.Sockets.TcpListener instance to listen on the specified port.

            port: The port on which to listen for incoming connection attempts.

            Returns: Returns System.Net.Sockets.TcpListener.A new System.Net.Sockets.TcpListener instance to listen on the specified port.
        """
        ...
    def EndAcceptSocket(self, asyncResult):
        """
        EndAcceptSocket(self: TcpListener, asyncResult: IAsyncResult) -> Socket

            Asynchronously accepts an incoming connection attempt and creates a new System.Net.Sockets.Socket to handle remote host communication.

            asyncResult: An System.IAsyncResult returned by a call to the System.Net.Sockets.TcpListener.BeginAcceptSocket(System.AsyncCallback,System.Object)  method.

            Returns: A System.Net.Sockets.Socket.The System.Net.Sockets.Socket used to send and receive data.
        """
        ...
    def EndAcceptTcpClient(self, asyncResult):
        """
        EndAcceptTcpClient(self: TcpListener, asyncResult: IAsyncResult) -> TcpClient

            Asynchronously accepts an incoming connection attempt and creates a new System.Net.Sockets.TcpClient to handle remote host communication.

            asyncResult: An System.IAsyncResult returned by a call to the System.Net.Sockets.TcpListener.BeginAcceptTcpClient(System.AsyncCallback,System.Object) method.

            Returns: A System.Net.Sockets.TcpClient.The System.Net.Sockets.TcpClient used to send and receive data.
        """
        ...
    def Pending(self):
        """
        Pending(self: TcpListener) -> bool

            Determines if there are pending connection requests.

            Returns: ue if connections are pending; otherwise, lse.
        """
        ...
    def Start(self, backlog=None):
        """
        Start(self: TcpListener)

            Starts listening for incoming connection requests.

        Start(self: TcpListener, backlog: int)

            Starts listening for incoming connection requests with a maximum number of pending connection.

            backlog: The maximum length of the pending connections queue.
        """
        ...
    def Stop(self):
        """
        Stop(self: TcpListener)

            Closes the listener.
        """
        ...
    @property
    def Active(self):
        """Gets a value that indicates whether System.Net.Sockets.TcpListener is actively listening for client connections."""
        ...
    @property
    def ExclusiveAddressUse(self):
        """
        Gets or sets a System.Boolean value that specifies whether the System.Net.Sockets.TcpListener allows only one underlying socket to listen to a specific port.

        Get: ExclusiveAddressUse(self: TcpListener) -> bool

        Set: ExclusiveAddressUse(self: TcpListener) = value
        """
        ...
    @property
    def LocalEndpoint(self):
        """
        Gets the underlying System.Net.EndPoint of the current System.Net.Sockets.TcpListener.

        Get: LocalEndpoint(self: TcpListener) -> EndPoint
        """
        ...
    @property
    def Server(self):
        """
        Gets the underlying network System.Net.Sockets.Socket.

        Get: Server(self: TcpListener) -> Socket
        """
        ...

class TransmitFileOptions(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    The System.Net.Sockets.TransmitFileOptions enumeration defines values used in file transfer requests.

    enum (flags) TransmitFileOptions, values: Disconnect (1), ReuseSocket (2), UseDefaultWorkerThread (0), UseKernelApc (32), UseSystemThread (16), WriteBehind (4)
    """

    Disconnect = None
    ReuseSocket = None
    UseDefaultWorkerThread = None
    UseKernelApc = None
    UseSystemThread = None
    value__ = None
    WriteBehind = None

class UdpClient(object, IDisposable):
    """
    Provides User Datagram Protocol (UDP) network services.

    UdpClient()

    UdpClient(family: AddressFamily)

    UdpClient(port: int)

    UdpClient(port: int, family: AddressFamily)

    UdpClient(localEP: IPEndPoint)

    UdpClient(hostname: str, port: int)
    """

    def AllowNatTraversal(self, allowed):
        """
        AllowNatTraversal(self: UdpClient, allowed: bool)

            Enables or disables Network Address Translation (NAT) traversal on a System.Net.Sockets.UdpClient instance.

            allowed: A Boolean value that specifies whether to enable or disable NAT traversal.
        """
        ...
    def BeginReceive(self, requestCallback, state):
        """
        BeginReceive(self: UdpClient, requestCallback: AsyncCallback, state: object) -> IAsyncResult

            Receives a datagram from a remote host asynchronously.

            requestCallback: An System.AsyncCallback delegate that references the method to invoke when the operation is complete.

            state: A user-defined object that contains information about the receive operation. This object is passed to the requestCallback delegate when the operation is complete.

            Returns: An System.IAsyncResult object that references the asynchronous receive.
        """
        ...
    def BeginSend(self, datagram, bytes, *__args):
        """
        BeginSend(self: UdpClient, datagram: Array[Byte], bytes: int, endPoint: IPEndPoint, requestCallback: AsyncCallback, state: object) -> IAsyncResult

            Sends a datagram to a destination asynchronously. The destination is specified by a System.Net.EndPoint.

            datagram: A System.Byte array that contains the data to be sent.

            bytes: The number of bytes to send.

            endPoint: The System.Net.EndPoint that represents the destination for the data.

            requestCallback: An System.AsyncCallback delegate that references the method to invoke when the operation is complete.

            state: A user-defined object that contains information about the send operation. This object is passed to the requestCallback delegate when the operation is complete.

            Returns: An System.IAsyncResult object that references the asynchronous send.

        BeginSend(self: UdpClient, datagram: Array[Byte], bytes: int, hostname: str, port: int, requestCallback: AsyncCallback, state: object) -> IAsyncResult

            Sends a datagram to a destination asynchronously. The destination is specified by the host name and port number.

            datagram: A System.Byte array that contains the data to be sent.

            bytes: The number of bytes to send.

            hostname: The destination host.

            port: The destination port number.

            requestCallback: An System.AsyncCallback delegate that references the method to invoke when the operation is complete.

            state: A user-defined object that contains information about the send operation. This object is passed to the requestCallback delegate when the operation is complete.

            Returns: An System.IAsyncResult object that references the asynchronous send.

        BeginSend(self: UdpClient, datagram: Array[Byte], bytes: int, requestCallback: AsyncCallback, state: object) -> IAsyncResult

            Sends a datagram to a remote host asynchronously. The destination was specified previously by a call to erload:System.Net.Sockets.UdpClient.Connect.

            datagram: A System.Byte array that contains the data to be sent.

            bytes: The number of bytes to send.

            requestCallback: An System.AsyncCallback delegate that references the method to invoke when the operation is complete.

            state: A user-defined object that contains information about the send operation. This object is passed to the requestCallback delegate when the operation is complete.

            Returns: An System.IAsyncResult object that references the asynchronous send.
        """
        ...
    def Close(self):
        """
        Close(self: UdpClient)

            Closes the UDP connection.
        """
        ...
    def Connect(self, *__args):
        """
        Connect(self: UdpClient, hostname: str, port: int)

            Establishes a default remote host using the specified host name and port number.

            hostname: The DNS name of the remote host to which you intend send data.

            port: The port number on the remote host to which you intend to send data.

        Connect(self: UdpClient, addr: IPAddress, port: int)

            Establishes a default remote host using the specified IP address and port number.

            addr: The System.Net.IPAddress of the remote host to which you intend to send data.

            port: The port number to which you intend send data.

        Connect(self: UdpClient, endPoint: IPEndPoint)

            Establishes a default remote host using the specified network endpoint.

            endPoint: An System.Net.IPEndPoint that specifies the network endpoint to which you intend to send data.
        """
        ...
    def DropMulticastGroup(self, multicastAddr, ifindex=None):
        """
        DropMulticastGroup(self: UdpClient, multicastAddr: IPAddress, ifindex: int)

            Leaves a multicast group.

            multicastAddr: The System.Net.IPAddress of the multicast group to leave.

            ifindex: The local address of the multicast group to leave.

        DropMulticastGroup(self: UdpClient, multicastAddr: IPAddress)

            Leaves a multicast group.

            multicastAddr: The System.Net.IPAddress of the multicast group to leave.
        """
        ...
    def EndReceive(self, asyncResult, remoteEP):
        """
        EndReceive(self: UdpClient, asyncResult: IAsyncResult, remoteEP: IPEndPoint) -> (Array[Byte], IPEndPoint)

            Ends a pending asynchronous receive.

            asyncResult: An System.IAsyncResult object returned by a call to System.Net.Sockets.UdpClient.BeginReceive(System.AsyncCallback,System.Object).

            remoteEP: The specified remote endpoint.

            Returns: If successful, the number of bytes received. If unsuccessful, this method returns 0.
        """
        ...
    def EndSend(self, asyncResult):
        """
        EndSend(self: UdpClient, asyncResult: IAsyncResult) -> int

            Ends a pending asynchronous send.

            asyncResult: An System.IAsyncResult object returned by a call to erload:System.Net.Sockets.UdpClient.BeginSend.

            Returns: If successful, the number of bytes sent to the System.Net.Sockets.UdpClient.
        """
        ...
    def JoinMulticastGroup(self, *__args):
        """
        JoinMulticastGroup(self: UdpClient, multicastAddr: IPAddress, localAddress: IPAddress)

            Adds a System.Net.Sockets.UdpClient to a multicast group.

            multicastAddr: The multicast System.Net.IPAddress of the group you want to join.

            localAddress: The local System.Net.IPAddress.

        JoinMulticastGroup(self: UdpClient, ifindex: int, multicastAddr: IPAddress)

            Adds a System.Net.Sockets.UdpClient to a multicast group.

            ifindex: The interface index associated with the local IP address on which to join the multicast group.

            multicastAddr: The multicast System.Net.IPAddress of the group you want to join.

        JoinMulticastGroup(self: UdpClient, multicastAddr: IPAddress, timeToLive: int)

            Adds a System.Net.Sockets.UdpClient to a multicast group with the specified Time to Live (TTL).

            multicastAddr: The System.Net.IPAddress of the multicast group to join.

            timeToLive: The Time to Live (TTL), measured in router hops.

        JoinMulticastGroup(self: UdpClient, multicastAddr: IPAddress)

            Adds a System.Net.Sockets.UdpClient to a multicast group.

            multicastAddr: The multicast System.Net.IPAddress of the group you want to join.
        """
        ...
    def Receive(self, remoteEP):
        """
        Receive(self: UdpClient, remoteEP: IPEndPoint) -> (Array[Byte], IPEndPoint)

            Returns a UDP datagram that was sent by a remote host.

            remoteEP: An System.Net.IPEndPoint that represents the remote host from which the data was sent.

            Returns: An array of type System.Byte that contains datagram data.
        """
        ...
    def ReceiveAsync(self):
        """
        ReceiveAsync(self: UdpClient) -> Task[UdpReceiveResult]

            Returns a UDP datagram asynchronously that was sent by a remote host.

            Returns: Returns System.Threading.Tasks.Task.The task object representing the asynchronous operation.
        """
        ...
    def Send(self, dgram, bytes, *__args):
        """
        Send(self: UdpClient, dgram: Array[Byte], bytes: int, endPoint: IPEndPoint) -> int

            Sends a UDP datagram to the host at the specified remote endpoint.

            dgram: An array of type System.Byte that specifies the UDP datagram that you intend to send, represented as an array of bytes.

            bytes: The number of bytes in the datagram.

            endPoint: An System.Net.IPEndPoint that represents the host and port to which to send the datagram.

            Returns: The number of bytes sent.

        Send(self: UdpClient, dgram: Array[Byte], bytes: int, hostname: str, port: int) -> int

            Sends a UDP datagram to a specified port on a specified remote host.

            dgram: An array of type System.Byte that specifies the UDP datagram that you intend to send represented as an array of bytes.

            bytes: The number of bytes in the datagram.

            hostname: The name of the remote host to which you intend to send the datagram.

            port: The remote port number with which you intend to communicate.

            Returns: The number of bytes sent.

        Send(self: UdpClient, dgram: Array[Byte], bytes: int) -> int

            Sends a UDP datagram to a remote host.

            dgram: An array of type System.Byte that specifies the UDP datagram that you intend to send represented as an array of bytes.

            bytes: The number of bytes in the datagram.

            Returns: The number of bytes sent.
        """
        ...
    def SendAsync(self, datagram, bytes, *__args):
        """
        SendAsync(self: UdpClient, datagram: Array[Byte], bytes: int) -> Task[int]

            Sends a UDP datagram asynchronously to a remote host.

            datagram: An array of type System.Byte that specifies the UDP datagram that you intend to send represented as an array of bytes.

            bytes: The number of bytes in the datagram.

            Returns: Returns System.Threading.Tasks.Task.

        SendAsync(self: UdpClient, datagram: Array[Byte], bytes: int, endPoint: IPEndPoint) -> Task[int]

            Sends a UDP datagram asynchronously to a remote host.

            datagram: An array of type System.Byte that specifies the UDP datagram that you intend to send represented as an array of bytes.

            bytes: The number of bytes in the datagram.

            endPoint: An System.Net.IPEndPoint that represents the host and port to which to send the datagram.

            Returns: Returns System.Threading.Tasks.Task.

        SendAsync(self: UdpClient, datagram: Array[Byte], bytes: int, hostname: str, port: int) -> Task[int]

            Sends a UDP datagram asynchronously to a remote host.

            datagram: An array of type System.Byte that specifies the UDP datagram that you intend to send represented as an array of bytes.

            bytes: The number of bytes in the datagram.

            hostname: The name of the remote host to which you intend to send the datagram.

            port: The remote port number with which you intend to communicate.

            Returns: Returns System.Threading.Tasks.Task.
        """
        ...
    @property
    def Active(self):
        """Gets or sets a value indicating whether a default remote host has been established."""
        ...
    @property
    def Available(self):
        """
        Gets the amount of data received from the network that is available to read.

        Get: Available(self: UdpClient) -> int
        """
        ...
    @property
    def Client(self):
        """
        Gets or sets the underlying network System.Net.Sockets.Socket.

        Get: Client(self: UdpClient) -> Socket

        Set: Client(self: UdpClient) = value
        """
        ...
    @property
    def DontFragment(self):
        """
        Gets or sets a System.Boolean value that specifies whether the System.Net.Sockets.UdpClient allows Internet Protocol (IP) datagrams to be fragmented.

        Get: DontFragment(self: UdpClient) -> bool

        Set: DontFragment(self: UdpClient) = value
        """
        ...
    @property
    def EnableBroadcast(self):
        """
        Gets or sets a System.Boolean value that specifies whether the System.Net.Sockets.UdpClient may send or receive broadcast packets.

        Get: EnableBroadcast(self: UdpClient) -> bool

        Set: EnableBroadcast(self: UdpClient) = value
        """
        ...
    @property
    def ExclusiveAddressUse(self):
        """
        Gets or sets a System.Boolean value that specifies whether the System.Net.Sockets.UdpClient allows only one client to use a port.

        Get: ExclusiveAddressUse(self: UdpClient) -> bool

        Set: ExclusiveAddressUse(self: UdpClient) = value
        """
        ...
    @property
    def MulticastLoopback(self):
        """
        Gets or sets a System.Boolean value that specifies whether outgoing multicast packets are delivered to the sending application.

        Get: MulticastLoopback(self: UdpClient) -> bool

        Set: MulticastLoopback(self: UdpClient) = value
        """
        ...
    @property
    def Ttl(self):
        """
        Gets or sets a value that specifies the Time to Live (TTL) value of Internet Protocol (IP) packets sent by the System.Net.Sockets.UdpClient.

        Get: Ttl(self: UdpClient) -> Int16

        Set: Ttl(self: UdpClient) = value
        """
        ...

class UdpReceiveResult(object, IEquatable[UdpReceiveResult]):
    """
    Presents UDP receive result information from a call to the System.Net.Sockets.UdpClient.ReceiveAsync method.

    UdpReceiveResult(buffer: Array[Byte], remoteEndPoint: IPEndPoint)
    """

    def GetHashCode(self):
        """
        GetHashCode(self: UdpReceiveResult) -> int

            Returns the hash code for this instance.

            Returns: Returns System.Int32.The hash code.
        """
        ...
    def __ne__(self, *args): ...
    @property
    def Buffer(self):
        """
        Gets a buffer with the data received in the UDP packet.

        Get: Buffer(self: UdpReceiveResult) -> Array[Byte]
        """
        ...
    @property
    def RemoteEndPoint(self):
        """
        Gets the remote endpoint from which the UDP packet was received.

        Get: RemoteEndPoint(self: UdpReceiveResult) -> IPEndPoint
        """
        ...
