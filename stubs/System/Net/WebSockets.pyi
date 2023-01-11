# encoding: utf-8
# module System.Net.WebSockets calls itself WebSockets
# from System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class WebSocket(object, IDisposable):
    """The WebSocket class allows applications to send and receive data after the WebSocket upgrade has completed."""

    @property
    def CloseStatus(self):
        """
        Indicates the reason why the remote endpoint initiated the close handshake.

        Get: CloseStatus(self: WebSocket) -> Nullable[WebSocketCloseStatus]
        """
        ...
    @property
    def CloseStatusDescription(self):
        """
        Allows the remote endpoint to describe the reason why the connection was closed.

        Get: CloseStatusDescription(self: WebSocket) -> str
        """
        ...
    @property
    def DefaultKeepAliveInterval(self):
        """
        Gets the default WebSocket protocol keep-alive interval in milliseconds.

        Get: DefaultKeepAliveInterval() -> TimeSpan
        """
        ...
    @property
    def State(self):
        """
        Returns the current state of the WebSocket connection.

        Get: State(self: WebSocket) -> WebSocketState
        """
        ...
    @property
    def SubProtocol(self):
        """
        The subprotocol that was negotiated during the opening handshake.

        Get: SubProtocol(self: WebSocket) -> str
        """
        ...
    def Abort(self):
        """
        Abort(self: WebSocket)

            Aborts the WebSocket connection and cancels any pending IO operations.
        """
        ...
    def CloseAsync(self, closeStatus, statusDescription, cancellationToken):
        """
        CloseAsync(self: WebSocket, closeStatus: WebSocketCloseStatus, statusDescription: str, cancellationToken: CancellationToken) -> Task

            Closes the WebSocket connection as an asynchronous operation using the close handshake defined in the WebSocket protocol specification section 7.

            closeStatus: Indicates the reason for closing the WebSocket connection.

            statusDescription: Specifies a human readable explanation as to why the connection is closed.

            cancellationToken: The token that can be used to propagate notification that operations should be canceled.

            Returns: Returns System.Threading.Tasks.Task.The task object representing the asynchronous operation.
        """
        ...
    def CloseOutputAsync(self, closeStatus, statusDescription, cancellationToken):
        """
        CloseOutputAsync(self: WebSocket, closeStatus: WebSocketCloseStatus, statusDescription: str, cancellationToken: CancellationToken) -> Task

            Initiates or completes the close handshake defined in the WebSocket protocol specification section 7.

            closeStatus: Indicates the reason for closing the WebSocket connection.

            statusDescription: Allows applications to specify a human readable explanation as to why the connection is closed.

            cancellationToken: The token that can be used to propagate notification that operations should be canceled.

            Returns: Returns System.Threading.Tasks.Task.The task object representing the asynchronous operation.
        """
        ...
    @staticmethod
    def CreateClientBuffer(receiveBufferSize, sendBufferSize):
        """
        CreateClientBuffer(receiveBufferSize: int, sendBufferSize: int) -> ArraySegment[Byte]

            Create client buffers to use with this System.Net.WebSockets.WebSocket instance.

            receiveBufferSize: The size, in bytes, of the client receive buffer.

            sendBufferSize: The size, in bytes, of the send buffer.

            Returns: Returns System.ArraySegment.An array with the client buffers.
        """
        ...
    @staticmethod
    def CreateClientWebSocket(
        innerStream,
        subProtocol,
        receiveBufferSize,
        sendBufferSize,
        keepAliveInterval,
        useZeroMaskingKey,
        internalBuffer,
    ):
        """CreateClientWebSocket(innerStream: Stream, subProtocol: str, receiveBufferSize: int, sendBufferSize: int, keepAliveInterval: TimeSpan, useZeroMaskingKey: bool, internalBuffer: ArraySegment[Byte]) -> WebSocket"""
        ...
    @staticmethod
    def CreateServerBuffer(receiveBufferSize):
        """
        CreateServerBuffer(receiveBufferSize: int) -> ArraySegment[Byte]

            Creates a WebSocket server buffer.

            receiveBufferSize: The size, in bytes, of the desired buffer.

            Returns: Returns System.ArraySegment.
        """
        ...
    @staticmethod
    def IsApplicationTargeting45():
        """
        IsApplicationTargeting45() -> bool

            Returns a value that indicates if the WebSocket instance is targeting .NET Framework 4.5.

            Returns: Returns System.Boolean.

                  ue if the System.Net.WebSockets.WebSocket is targeting .NET Framework 4.5; otherwise lse.
        """
        ...
    def IsStateTerminal(self, *args):  # cannot find CLR method
        """
        IsStateTerminal(state: WebSocketState) -> bool

            Returns a value that indicates if the state of the WebSocket instance is closed or aborted.

            state: The current state of the WebSocket.

            Returns: Returns System.Boolean.

                  ue if the System.Net.WebSockets.WebSocket is closed or aborted; otherwise lse.
        """
        ...
    def ReceiveAsync(self, buffer, cancellationToken):
        """ReceiveAsync(self: WebSocket, buffer: ArraySegment[Byte], cancellationToken: CancellationToken) -> Task[WebSocketReceiveResult]"""
        ...
    @staticmethod
    def RegisterPrefixes():
        """
        RegisterPrefixes()

            This API supports the .NET Framework infrastructure and is not intended to be used directly from your code. Allows callers to register prefixes for

             WebSocket requests (ws and wss).
        """
        ...
    def SendAsync(self, buffer, messageType, endOfMessage, cancellationToken):
        """SendAsync(self: WebSocket, buffer: ArraySegment[Byte], messageType: WebSocketMessageType, endOfMessage: bool, cancellationToken: CancellationToken) -> Task"""
        ...
    def ThrowOnInvalidState(self, *args):  # cannot find CLR method
        """
        ThrowOnInvalidState(state: WebSocketState, *validStates: Array[WebSocketState])

            Verifies that the connection is in an expected state.

            state: The current state of the WebSocket to be tested against the list of valid states.

            validStates: List of valid connection states.
        """
        ...
    DefaultKeepAliveInterval = None

class ClientWebSocket(WebSocket):  # skipped bases: <type 'IDisposable'>
    """
    Provides a client for connecting to WebSocket services.

    ClientWebSocket()
    """

    @property
    def Options(self):
        """
        Gets the WebSocket options for the System.Net.WebSockets.ClientWebSocket instance.

        Get: Options(self: ClientWebSocket) -> ClientWebSocketOptions
        """
        ...
    def ConnectAsync(self, uri, cancellationToken):
        """
        ConnectAsync(self: ClientWebSocket, uri: Uri, cancellationToken: CancellationToken) -> Task

            Connect to a WebSocket server as an asynchronous operation.

            uri: The URI of the WebSocket server to connect to.

            cancellationToken: A cancellation token used to propagate notification that the  operation should be canceled.

            Returns: Returns System.Threading.Tasks.Task.The task object representing the asynchronous operation.
        """
        ...

class ClientWebSocketOptions:  # skipped bases: <type 'object'>
    """Options to use with a  System.Net.WebSockets.ClientWebSocket object."""

    @property
    def ClientCertificates(self):
        """
        Gets or sets a collection of client side certificates.

        Get: ClientCertificates(self: ClientWebSocketOptions) -> X509CertificateCollection

        Set: ClientCertificates(self: ClientWebSocketOptions) = value
        """
        ...
    @property
    def Cookies(self):
        """
        Gets or sets the cookies associated with the request.

        Get: Cookies(self: ClientWebSocketOptions) -> CookieContainer

        Set: Cookies(self: ClientWebSocketOptions) = value
        """
        ...
    @property
    def Credentials(self):
        """
        Gets or sets the credential information for the client.

        Get: Credentials(self: ClientWebSocketOptions) -> ICredentials

        Set: Credentials(self: ClientWebSocketOptions) = value
        """
        ...
    @property
    def KeepAliveInterval(self):
        """
        Gets or sets the WebSocket protocol keep-alive interval in milliseconds.

        Get: KeepAliveInterval(self: ClientWebSocketOptions) -> TimeSpan

        Set: KeepAliveInterval(self: ClientWebSocketOptions) = value
        """
        ...
    @property
    def Proxy(self):
        """
        Gets or sets the proxy for WebSocket requests.

        Get: Proxy(self: ClientWebSocketOptions) -> IWebProxy

        Set: Proxy(self: ClientWebSocketOptions) = value
        """
        ...
    @property
    def UseDefaultCredentials(self):
        """
        Gets or sets a System.Boolean value that indicates if default credentials should be used during WebSocket handshake.

        Get: UseDefaultCredentials(self: ClientWebSocketOptions) -> bool

        Set: UseDefaultCredentials(self: ClientWebSocketOptions) = value
        """
        ...
    def AddSubProtocol(self, subProtocol):
        """
        AddSubProtocol(self: ClientWebSocketOptions, subProtocol: str)

            Adds a sub-protocol to be negotiated during the WebSocket connection handshake.

            subProtocol: The WebSocket sub-protocol to add.
        """
        ...
    def SetBuffer(self, receiveBufferSize, sendBufferSize, buffer=None):
        """
        SetBuffer(self: ClientWebSocketOptions, receiveBufferSize: int, sendBufferSize: int)

            Sets the client buffer parameters.

            receiveBufferSize: The size, in bytes, of the client receive buffer.

            sendBufferSize: The size, in bytes, of the client send buffer.

        SetBuffer(self: ClientWebSocketOptions, receiveBufferSize: int, sendBufferSize: int, buffer: ArraySegment[Byte])
        """
        ...
    def SetRequestHeader(self, headerName, headerValue):
        """
        SetRequestHeader(self: ClientWebSocketOptions, headerName: str, headerValue: str)

            Creates a HTTP request header and its value.

            headerName: The name of the HTTP header.

            headerValue: The value of the HTTP header.
        """
        ...

class WebSocketContext:  # skipped bases: <type 'object'>
    """Used for accessing the information in the WebSocket handshake."""

    @property
    def CookieCollection(self):
        """
        The cookies that were passed to the server during the opening handshake.

        Get: CookieCollection(self: WebSocketContext) -> CookieCollection
        """
        ...
    @property
    def Headers(self):
        """
        The HTTP headers that were sent to the server during the opening handshake.

        Get: Headers(self: WebSocketContext) -> NameValueCollection
        """
        ...
    @property
    def IsAuthenticated(self):
        """
        Whether the WebSocket client is authenticated.

        Get: IsAuthenticated(self: WebSocketContext) -> bool
        """
        ...
    @property
    def IsLocal(self):
        """
        Whether the WebSocket client connected from the local machine.

        Get: IsLocal(self: WebSocketContext) -> bool
        """
        ...
    @property
    def IsSecureConnection(self):
        """
        Whether the WebSocket connection is secured using Secure Sockets Layer (SSL).

        Get: IsSecureConnection(self: WebSocketContext) -> bool
        """
        ...
    @property
    def Origin(self):
        """
        The value of the Origin HTTP header included in the opening handshake.

        Get: Origin(self: WebSocketContext) -> str
        """
        ...
    @property
    def RequestUri(self):
        """
        The URI requested by the WebSocket client.

        Get: RequestUri(self: WebSocketContext) -> Uri
        """
        ...
    @property
    def SecWebSocketKey(self):
        """
        The value of the SecWebSocketKey HTTP header included in the opening handshake.

        Get: SecWebSocketKey(self: WebSocketContext) -> str
        """
        ...
    @property
    def SecWebSocketProtocols(self):
        """
        The value of the SecWebSocketKey HTTP header included in the opening handshake.

        Get: SecWebSocketProtocols(self: WebSocketContext) -> IEnumerable[str]
        """
        ...
    @property
    def SecWebSocketVersion(self):
        """
        The list of subprotocols requested by the WebSocket client.

        Get: SecWebSocketVersion(self: WebSocketContext) -> str
        """
        ...
    @property
    def User(self):
        """
        An object used to obtain identity, authentication information, and security roles for the WebSocket client.

        Get: User(self: WebSocketContext) -> IPrincipal
        """
        ...
    @property
    def WebSocket(self):
        """
        The WebSocket instance used to interact (send/receive/close/etc) with the WebSocket connection.

        Get: WebSocket(self: WebSocketContext) -> WebSocket
        """
        ...

class HttpListenerWebSocketContext(WebSocketContext):
    """Provides access to information received by the System.Net.HttpListener class when accepting WebSocket connections."""

    pass

class WebSocketCloseStatus(Enum):  # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>
    """
    Represents well known WebSocket close codes as defined in section 11.7 of the WebSocket protocol spec.

    enum WebSocketCloseStatus, values: Empty (1005), EndpointUnavailable (1001), InternalServerError (1011), InvalidMessageType (1003), InvalidPayloadData (1007), MandatoryExtension (1010), MessageTooBig (1009), NormalClosure (1000), PolicyViolation (1008), ProtocolError (1002)
    """

    Empty = None
    EndpointUnavailable = None
    InternalServerError = None
    InvalidMessageType = None
    InvalidPayloadData = None
    MandatoryExtension = None
    MessageTooBig = None
    NormalClosure = None
    PolicyViolation = None
    ProtocolError = None
    value__ = None

class WebSocketError(Enum):  # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>
    """
    Contains the list of possible WebSocket errors.

    enum WebSocketError, values: ConnectionClosedPrematurely (8), Faulted (2), HeaderError (7), InvalidMessageType (1), InvalidState (9), NativeError (3), NotAWebSocket (4), Success (0), UnsupportedProtocol (6), UnsupportedVersion (5)
    """

    ConnectionClosedPrematurely = None
    Faulted = None
    HeaderError = None
    InvalidMessageType = None
    InvalidState = None
    NativeError = None
    NotAWebSocket = None
    Success = None
    UnsupportedProtocol = None
    UnsupportedVersion = None
    value__ = None

class WebSocketException(Win32Exception):  # skipped bases: <type 'ISerializable'>, <type '_Exception'>
    """
    Represents an exception that occurred when performing an operation on a WebSocket connection.

    WebSocketException()

    WebSocketException(error: WebSocketError)

    WebSocketException(error: WebSocketError, message: str)

    WebSocketException(error: WebSocketError, innerException: Exception)

    WebSocketException(error: WebSocketError, message: str, innerException: Exception)

    WebSocketException(nativeError: int)

    WebSocketException(nativeError: int, message: str)

    WebSocketException(nativeError: int, innerException: Exception)

    WebSocketException(error: WebSocketError, nativeError: int)

    WebSocketException(error: WebSocketError, nativeError: int, message: str)

    WebSocketException(error: WebSocketError, nativeError: int, innerException: Exception)

    WebSocketException(error: WebSocketError, nativeError: int, message: str, innerException: Exception)

    WebSocketException(message: str)

    WebSocketException(message: str, innerException: Exception)
    """

    @property
    def ErrorCode(self):
        """
        The native error code for the exception that occurred.

        Get: ErrorCode(self: WebSocketException) -> int
        """
        ...
    @property
    def WebSocketErrorCode(self):
        """
        Returns a WebSocketError indicating the type of error that occurred.

        Get: WebSocketErrorCode(self: WebSocketException) -> WebSocketError
        """
        ...
    SerializeObjectState = None

class WebSocketMessageType(Enum):  # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>
    """
    Indicates the message type.

    enum WebSocketMessageType, values: Binary (1), Close (2), Text (0)
    """

    Binary = None
    Close = None
    Text = None
    value__ = None

class WebSocketReceiveResult:  # skipped bases: <type 'object'>
    """
    An instance of this class represents the result of performing a single ReceiveAsync operation on a WebSocket.

    WebSocketReceiveResult(count: int, messageType: WebSocketMessageType, endOfMessage: bool)

    WebSocketReceiveResult(count: int, messageType: WebSocketMessageType, endOfMessage: bool, closeStatus: Nullable[WebSocketCloseStatus], closeStatusDescription: str)
    """

    @property
    def CloseStatus(self):
        """
        Indicates the reason why the remote endpoint initiated the close handshake.

        Get: CloseStatus(self: WebSocketReceiveResult) -> Nullable[WebSocketCloseStatus]
        """
        ...
    @property
    def CloseStatusDescription(self):
        """
        Returns the optional description that describes why the close handshake has been initiated by the remote endpoint.

        Get: CloseStatusDescription(self: WebSocketReceiveResult) -> str
        """
        ...
    @property
    def Count(self):
        """
        Indicates the number of bytes that the WebSocket received.

        Get: Count(self: WebSocketReceiveResult) -> int
        """
        ...
    @property
    def EndOfMessage(self):
        """
        Indicates whether the message has been received completely.

        Get: EndOfMessage(self: WebSocketReceiveResult) -> bool
        """
        ...
    @property
    def MessageType(self):
        """
        Indicates whether the current message is a UTF-8 message or a binary message.

        Get: MessageType(self: WebSocketReceiveResult) -> WebSocketMessageType
        """
        ...

class WebSocketState(Enum):  # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>
    """
    Defines the different states a WebSockets instance can be in.

    enum WebSocketState, values: Aborted (6), Closed (5), CloseReceived (4), CloseSent (3), Connecting (1), None (0), Open (2)
    """

    Aborted = None
    Closed = None
    CloseReceived = None
    CloseSent = None
    Connecting = None

    Open = None
    value__ = None
