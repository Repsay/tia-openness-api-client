# encoding: utf-8
# module System.Net.Security calls itself Security
# from System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AuthenticatedStream(Stream):  # skipped bases: <type 'IDisposable'>
    """Provides methods for passing credentials across a stream and requesting or performing authentication for client-server applications."""

    @staticmethod  # known case of __new__
    def __new__(cls, *args):  # cannot find CLR constructor
        """__new__(cls: type, innerStream: Stream, leaveInnerStreamOpen: bool)"""
        ...
    @property
    def InnerStream(self):
        """Gets the stream used by this System.Net.Security.AuthenticatedStream for sending and receiving data."""
        ...
    @property
    def IsAuthenticated(self):
        """
        Gets a System.Boolean value that indicates whether authentication was successful.

        Get: IsAuthenticated(self: AuthenticatedStream) -> bool
        """
        ...
    @property
    def IsEncrypted(self):
        """
        Gets a System.Boolean value that indicates whether data sent using this System.Net.Security.AuthenticatedStream is encrypted.

        Get: IsEncrypted(self: AuthenticatedStream) -> bool
        """
        ...
    @property
    def IsMutuallyAuthenticated(self):
        """
        Gets a System.Boolean value that indicates whether both server and client have been authenticated.

        Get: IsMutuallyAuthenticated(self: AuthenticatedStream) -> bool
        """
        ...
    @property
    def IsServer(self):
        """
        Gets a System.Boolean value that indicates whether the local side of the connection was authenticated as the server.

        Get: IsServer(self: AuthenticatedStream) -> bool
        """
        ...
    @property
    def IsSigned(self):
        """
        Gets a System.Boolean value that indicates whether the data sent using this stream is signed.

        Get: IsSigned(self: AuthenticatedStream) -> bool
        """
        ...
    @property
    def LeaveInnerStreamOpen(self):
        """
        Gets whether the stream used by this System.Net.Security.AuthenticatedStream for sending and receiving data has been left open.

        Get: LeaveInnerStreamOpen(self: AuthenticatedStream) -> bool
        """
        ...

class AuthenticationLevel(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies client requirements for authentication and impersonation when using the System.Net.WebRequest class and derived classes to request a resource.

    enum AuthenticationLevel, values: MutualAuthRequested (1), MutualAuthRequired (2), None (0)
    """

    MutualAuthRequested = None
    MutualAuthRequired = None

    value__ = None

class EncryptionPolicy(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    The EncryptionPolicy to use.

    enum EncryptionPolicy, values: AllowNoEncryption (1), NoEncryption (2), RequireEncryption (0)
    """

    AllowNoEncryption = None
    NoEncryption = None
    RequireEncryption = None
    value__ = None

class LocalCertificateSelectionCallback(
    MulticastDelegate
):  # skipped bases: <type 'ICloneable'>, <type 'ISerializable'>
    """
    Selects the local Secure Sockets Layer (SSL) certificate used for authentication.

    LocalCertificateSelectionCallback(object: object, method: IntPtr)
    """

    def BeginInvoke(
        self, sender, targetHost, localCertificates, remoteCertificate, acceptableIssuers, callback, object
    ):
        """BeginInvoke(self: LocalCertificateSelectionCallback, sender: object, targetHost: str, localCertificates: X509CertificateCollection, remoteCertificate: X509Certificate, acceptableIssuers: Array[str], callback: AsyncCallback, object: object) -> IAsyncResult"""
        ...
    def EndInvoke(self, result):
        """EndInvoke(self: LocalCertificateSelectionCallback, result: IAsyncResult) -> X509Certificate"""
        ...
    def Invoke(self, sender, targetHost, localCertificates, remoteCertificate, acceptableIssuers):
        """Invoke(self: LocalCertificateSelectionCallback, sender: object, targetHost: str, localCertificates: X509CertificateCollection, remoteCertificate: X509Certificate, acceptableIssuers: Array[str]) -> X509Certificate"""
        ...

class NegotiateStream(AuthenticatedStream):  # skipped bases: <type 'IDisposable'>
    """
    Provides a stream that uses the Negotiate security protocol to authenticate the client, and optionally the server, in client-server communication.

    NegotiateStream(innerStream: Stream)

    NegotiateStream(innerStream: Stream, leaveInnerStreamOpen: bool)
    """

    def AuthenticateAsClient(self, credential=None, *__args):
        """
        AuthenticateAsClient(self: NegotiateStream)

            Called by clients to authenticate the client, and optionally the server, in a client-server connection.

        AuthenticateAsClient(self: NegotiateStream, credential: NetworkCredential, targetName: str)

            Called by clients to authenticate the client, and optionally the server, in a client-server connection. The authentication process uses the specified client credential.

            credential: The System.Net.NetworkCredential that is used to establish the identity of the client.

            targetName: The Service Principal Name (SPN) that uniquely identifies the server to authenticate.

        AuthenticateAsClient(self: NegotiateStream, credential: NetworkCredential, binding: ChannelBinding, targetName: str)

            Called by clients to authenticate the client, and optionally the server, in a client-server connection. The authentication process uses the specified client credential

             and the channel binding.

            credential: The System.Net.NetworkCredential that is used to establish the identity of the client.

            binding: The System.Security.Authentication.ExtendedProtection.ChannelBinding that is used for extended protection.

            targetName: The Service Principal Name (SPN) that uniquely identifies the server to authenticate.

        AuthenticateAsClient(self: NegotiateStream, credential: NetworkCredential, targetName: str, requiredProtectionLevel: ProtectionLevel, allowedImpersonationLevel: TokenImpersonationLevel)

            Called by clients to authenticate the client, and optionally the server, in a client-server connection. The authentication process uses the specified credentials and

             authentication options.

            credential: The System.Net.NetworkCredential that is used to establish the identity of the client.

            targetName: The Service Principal Name (SPN) that uniquely identifies the server to authenticate.

            requiredProtectionLevel: One of the System.Net.Security.ProtectionLevel values, indicating the security services for the stream.

            allowedImpersonationLevel: One of the System.Security.Principal.TokenImpersonationLevel values, indicating how the server can use the client's credentials to access resources.

        AuthenticateAsClient(self: NegotiateStream, credential: NetworkCredential, binding: ChannelBinding, targetName: str, requiredProtectionLevel: ProtectionLevel, allowedImpersonationLevel: TokenImpersonationLevel)

            Called by clients to authenticate the client, and optionally the server, in a client-server connection. The authentication process uses the specified credential,

             authentication options, and channel binding.

            credential: The System.Net.NetworkCredential that is used to establish the identity of the client.

            binding: The System.Security.Authentication.ExtendedProtection.ChannelBinding that is used for extended protection.

            targetName: The Service Principal Name (SPN) that uniquely identifies the server to authenticate.

            requiredProtectionLevel: One of the System.Net.Security.ProtectionLevel values, indicating the security services for the stream.

            allowedImpersonationLevel: One of the System.Security.Principal.TokenImpersonationLevel values, indicating how the server can use the client's credentials to access resources.
        """
        ...
    def AuthenticateAsClientAsync(self, credential=None, *__args):
        """
        AuthenticateAsClientAsync(self: NegotiateStream) -> Task

            Called by clients to authenticate the client, and optionally the server, in a client-server connection as an asynchronous operation.

            Returns: Returns System.Threading.Tasks.TaskThe task object representing the asynchronous operation.

        AuthenticateAsClientAsync(self: NegotiateStream, credential: NetworkCredential, targetName: str) -> Task

            Called by clients to authenticate the client, and optionally the server, in a client-server connection as an asynchronous operation. The authentication process uses

             the specified client credential.

            credential: The System.Net.NetworkCredential that is used to establish the identity of the client.

            targetName: The Service Principal Name (SPN) that uniquely identifies the server to authenticate.

            Returns: Returns System.Threading.Tasks.TaskThe task object representing the asynchronous operation.

        AuthenticateAsClientAsync(self: NegotiateStream, credential: NetworkCredential, targetName: str, requiredProtectionLevel: ProtectionLevel, allowedImpersonationLevel: TokenImpersonationLevel) -> Task

            Called by clients to authenticate the client, and optionally the server, in a client-server connection as an asynchronous operation. The authentication process uses

             the specified credentials and authentication options.

            credential: The System.Net.NetworkCredential that is used to establish the identity of the client.

            targetName: The Service Principal Name (SPN) that uniquely identifies the server to authenticate.

            requiredProtectionLevel: One of the System.Net.Security.ProtectionLevel values, indicating the security services for the stream.

            allowedImpersonationLevel: One of the System.Security.Principal.TokenImpersonationLevel values, indicating how the server can use the client's credentials to access resources.

            Returns: Returns System.Threading.Tasks.TaskThe task object representing the asynchronous operation.

        AuthenticateAsClientAsync(self: NegotiateStream, credential: NetworkCredential, binding: ChannelBinding, targetName: str) -> Task

            Called by clients to authenticate the client, and optionally the server, in a client-server connection as an asynchronous operation. The authentication process uses

             the specified client credential and the channel binding.

            credential: The System.Net.NetworkCredential that is used to establish the identity of the client.

            binding: The System.Security.Authentication.ExtendedProtection.ChannelBinding that is used for extended protection.

            targetName: The Service Principal Name (SPN) that uniquely identifies the server to authenticate.

            Returns: Returns System.Threading.Tasks.TaskThe task object representing the asynchronous operation.

        AuthenticateAsClientAsync(self: NegotiateStream, credential: NetworkCredential, binding: ChannelBinding, targetName: str, requiredProtectionLevel: ProtectionLevel, allowedImpersonationLevel: TokenImpersonationLevel) -> Task

            Called by clients to authenticate the client, and optionally the server, in a client-server connection as an asynchronous operation. The authentication process uses

             the specified credential, authentication options, and channel binding.

            credential: The System.Net.NetworkCredential that is used to establish the identity of the client.

            binding: The System.Security.Authentication.ExtendedProtection.ChannelBinding that is used for extended protection.

            targetName: The Service Principal Name (SPN) that uniquely identifies the server to authenticate.

            requiredProtectionLevel: One of the System.Net.Security.ProtectionLevel values, indicating the security services for the stream.

            allowedImpersonationLevel: One of the System.Security.Principal.TokenImpersonationLevel values, indicating how the server can use the client's credentials to access resources.

            Returns: Returns System.Threading.Tasks.TaskThe task object representing the asynchronous operation.
        """
        ...
    def AuthenticateAsServer(self, *__args):
        """
        AuthenticateAsServer(self: NegotiateStream)

            Called by servers to authenticate the client, and optionally the server, in a client-server connection.

        AuthenticateAsServer(self: NegotiateStream, policy: ExtendedProtectionPolicy)

            Called by servers to authenticate the client, and optionally the server, in a client-server connection. The authentication process uses the specified extended

             protection policy.

            policy: The System.Security.Authentication.ExtendedProtection.ExtendedProtectionPolicy that is used for extended protection.

        AuthenticateAsServer(self: NegotiateStream, credential: NetworkCredential, requiredProtectionLevel: ProtectionLevel, requiredImpersonationLevel: TokenImpersonationLevel)

            Called by servers to authenticate the client, and optionally the server, in a client-server connection. The authentication process uses the specified server

             credentials and authentication options.

            credential: The System.Net.NetworkCredential that is used to establish the identity of the server.

            requiredProtectionLevel: One of the System.Net.Security.ProtectionLevel values, indicating the security services for the stream.

            requiredImpersonationLevel: One of the System.Security.Principal.TokenImpersonationLevel values, indicating how the server can use the client's credentials to access resources.

        AuthenticateAsServer(self: NegotiateStream, credential: NetworkCredential, policy: ExtendedProtectionPolicy, requiredProtectionLevel: ProtectionLevel, requiredImpersonationLevel: TokenImpersonationLevel)

            Called by servers to authenticate the client, and optionally the server, in a client-server connection. The authentication process uses the specified server

             credentials, authentication options, and extended protection policy.

            credential: The System.Net.NetworkCredential that is used to establish the identity of the client.

            policy: The System.Security.Authentication.ExtendedProtection.ExtendedProtectionPolicy that is used for extended protection.

            requiredProtectionLevel: One of the System.Net.Security.ProtectionLevel values, indicating the security services for the stream.

            requiredImpersonationLevel: One of the System.Security.Principal.TokenImpersonationLevel values, indicating how the server can use the client's credentials to access resources.
        """
        ...
    def AuthenticateAsServerAsync(self, *__args):
        """
        AuthenticateAsServerAsync(self: NegotiateStream) -> Task

            Called by servers to authenticate the client, and optionally the server, in a client-server connection as an asynchronous operation.

            Returns: Returns System.Threading.Tasks.TaskThe task object representing the asynchronous operation.

        AuthenticateAsServerAsync(self: NegotiateStream, policy: ExtendedProtectionPolicy) -> Task

            Called by servers to authenticate the client, and optionally the server, in a client-server connection as an asynchronous operation. The authentication process uses

             the specified extended protection policy.

            policy: The System.Security.Authentication.ExtendedProtection.ExtendedProtectionPolicy that is used for extended protection.

            Returns: Returns System.Threading.Tasks.TaskThe task object representing the asynchronous operation.

        AuthenticateAsServerAsync(self: NegotiateStream, credential: NetworkCredential, requiredProtectionLevel: ProtectionLevel, requiredImpersonationLevel: TokenImpersonationLevel) -> Task

            Called by servers to authenticate the client, and optionally the server, in a client-server connection as an asynchronous operation. The authentication process uses

             the specified server credentials and authentication options.

            credential: The System.Net.NetworkCredential that is used to establish the identity of the server.

            requiredProtectionLevel: One of the System.Net.Security.ProtectionLevel values, indicating the security services for the stream.

            requiredImpersonationLevel: One of the System.Security.Principal.TokenImpersonationLevel values, indicating how the server can use the client's credentials to access resources.

            Returns: Returns System.Threading.Tasks.TaskThe task object representing the asynchronous operation.

        AuthenticateAsServerAsync(self: NegotiateStream, credential: NetworkCredential, policy: ExtendedProtectionPolicy, requiredProtectionLevel: ProtectionLevel, requiredImpersonationLevel: TokenImpersonationLevel) -> Task

            Called by servers to authenticate the client, and optionally the server, in a client-server connection as an asynchronous operation. The authentication process uses

             the specified server credentials, authentication options, and extended protection policy.

            credential: The System.Net.NetworkCredential that is used to establish the identity of the client.

            policy: The System.Security.Authentication.ExtendedProtection.ExtendedProtectionPolicy that is used for extended protection.

            requiredProtectionLevel: One of the System.Net.Security.ProtectionLevel values, indicating the security services for the stream.

            requiredImpersonationLevel: One of the System.Security.Principal.TokenImpersonationLevel values, indicating how the server can use the client's credentials to access resources.

            Returns: Returns System.Threading.Tasks.TaskThe task object representing the asynchronous operation.
        """
        ...
    def BeginAuthenticateAsClient(self, *__args):
        """
        BeginAuthenticateAsClient(self: NegotiateStream, asyncCallback: AsyncCallback, asyncState: object) -> IAsyncResult

            Called by clients to begin an asynchronous operation to authenticate the client, and optionally the server, in a client-server connection. This method does not block.

            asyncCallback: An System.AsyncCallback delegate that references the method to invoke when the authentication is complete.

            asyncState: A user-defined object containing information about the operation. This object is passed to the asyncCallback delegate when the operation completes.

            Returns: An System.IAsyncResult object indicating the status of the asynchronous operation.

        BeginAuthenticateAsClient(self: NegotiateStream, credential: NetworkCredential, targetName: str, asyncCallback: AsyncCallback, asyncState: object) -> IAsyncResult

            Called by clients to begin an asynchronous operation to authenticate the client, and optionally the server, in a client-server connection. The authentication process

             uses the specified credentials. This method does not block.

            credential: The System.Net.NetworkCredential that is used to establish the identity of the client.

            targetName: The Service Principal Name (SPN) that uniquely identifies the server to authenticate.

            asyncCallback: An System.AsyncCallback delegate that references the method to invoke when the authentication is complete.

            asyncState: A user-defined object containing information about the write operation. This object is passed to the asyncCallback delegate when the operation completes.

            Returns: An System.IAsyncResult object indicating the status of the asynchronous operation.

        BeginAuthenticateAsClient(self: NegotiateStream, credential: NetworkCredential, binding: ChannelBinding, targetName: str, asyncCallback: AsyncCallback, asyncState: object) -> IAsyncResult

            Called by clients to begin an asynchronous operation to authenticate the client, and optionally the server, in a client-server connection. The authentication process

             uses the specified credentials and channel binding. This method does not block.

            credential: The System.Net.NetworkCredential that is used to establish the identity of the client.

            binding: The System.Security.Authentication.ExtendedProtection.ChannelBinding that is used for extended protection.

            targetName: The Service Principal Name (SPN) that uniquely identifies the server to authenticate.

            asyncCallback: An System.AsyncCallback delegate that references the method to invoke when the authentication is complete.

            asyncState: A user-defined object containing information about the write operation. This object is passed to the asyncCallback delegate when the operation completes.

            Returns: An System.IAsyncResult object indicating the status of the asynchronous operation.

        BeginAuthenticateAsClient(self: NegotiateStream, credential: NetworkCredential, targetName: str, requiredProtectionLevel: ProtectionLevel, allowedImpersonationLevel: TokenImpersonationLevel, asyncCallback: AsyncCallback, asyncState: object) -> IAsyncResult

            Called by clients to begin an asynchronous operation to authenticate the client, and optionally the server, in a client-server connection. The authentication process

             uses the specified credentials and authentication options. This method does not block.

            credential: The System.Net.NetworkCredential that is used to establish the identity of the client.

            targetName: The Service Principal Name (SPN) that uniquely identifies the server to authenticate.

            requiredProtectionLevel: One of the System.Net.Security.ProtectionLevel values, indicating the security services for the stream.

            allowedImpersonationLevel: One of the System.Security.Principal.TokenImpersonationLevel values, indicating how the server can use the client's credentials to access resources.

            asyncCallback: An System.AsyncCallback delegate that references the method to invoke when the authentication is complete.

            asyncState: A user-defined object containing information about the write operation. This object is passed to the asyncCallback delegate when the operation completes.

            Returns: An System.IAsyncResult object indicating the status of the asynchronous operation.

        BeginAuthenticateAsClient(self: NegotiateStream, credential: NetworkCredential, binding: ChannelBinding, targetName: str, requiredProtectionLevel: ProtectionLevel, allowedImpersonationLevel: TokenImpersonationLevel, asyncCallback: AsyncCallback, asyncState: object) -> IAsyncResult

            Called by clients to begin an asynchronous operation to authenticate the client, and optionally the server, in a client-server connection. The authentication process

             uses the specified credentials, authentication options, and channel binding. This method does not block.

            credential: The System.Net.NetworkCredential that is used to establish the identity of the client.

            binding: The System.Security.Authentication.ExtendedProtection.ChannelBinding that is used for extended protection.

            targetName: The Service Principal Name (SPN) that uniquely identifies the server to authenticate.

            requiredProtectionLevel: One of the System.Net.Security.ProtectionLevel values, indicating the security services for the stream.

            allowedImpersonationLevel: One of the System.Security.Principal.TokenImpersonationLevel values, indicating how the server can use the client's credentials to access resources.

            asyncCallback: An System.AsyncCallback delegate that references the method to invoke when the authentication is complete.

            asyncState: A user-defined object containing information about the write operation. This object is passed to the asyncCallback delegate when the operation completes.

            Returns: An System.IAsyncResult object indicating the status of the asynchronous operation.
        """
        ...
    def BeginAuthenticateAsServer(self, *__args):
        """
        BeginAuthenticateAsServer(self: NegotiateStream, asyncCallback: AsyncCallback, asyncState: object) -> IAsyncResult

            Called by servers to begin an asynchronous operation to authenticate the client, and optionally the server, in a client-server connection. This method does not block.

            asyncCallback: An System.AsyncCallback delegate that references the method to invoke when the authentication is complete.

            asyncState: A user-defined object containing information about the operation. This object is passed to the asyncCallback delegate when the operation completes.

            Returns: An System.IAsyncResult object indicating the status of the asynchronous operation.

        BeginAuthenticateAsServer(self: NegotiateStream, policy: ExtendedProtectionPolicy, asyncCallback: AsyncCallback, asyncState: object) -> IAsyncResult

            Called by servers to begin an asynchronous operation to authenticate the client, and optionally the server, in a client-server connection. The authentication process

             uses the specified extended protection policy. This method does not block.

            policy: The System.Security.Authentication.ExtendedProtection.ExtendedProtectionPolicy that is used for extended protection.

            asyncCallback: An System.AsyncCallback delegate that references the method to invoke when the authentication is complete.

            asyncState: A user-defined object containing information about the write operation. This object is passed to the asyncCallback delegate when the operation completes.

            Returns: An System.IAsyncResult object indicating the status of the asynchronous operation.

        BeginAuthenticateAsServer(self: NegotiateStream, credential: NetworkCredential, requiredProtectionLevel: ProtectionLevel, requiredImpersonationLevel: TokenImpersonationLevel, asyncCallback: AsyncCallback, asyncState: object) -> IAsyncResult

            Called by servers to begin an asynchronous operation to authenticate the client, and optionally the server, in a client-server connection. The authentication process

             uses the specified server credentials and authentication options. This method does not block.

            credential: The System.Net.NetworkCredential that is used to establish the identity of the client.

            requiredProtectionLevel: One of the System.Net.Security.ProtectionLevel values, indicating the security services for the stream.

            requiredImpersonationLevel: One of the System.Security.Principal.TokenImpersonationLevel values, indicating how the server can use the client's credentials to access resources.

            asyncCallback: An System.AsyncCallback delegate that references the method to invoke when the authentication is complete.

            asyncState: A user-defined object containing information about the operation. This object is passed to the asyncCallback delegate when the operation completes.

            Returns: An System.IAsyncResult object indicating the status of the asynchronous operation.

        BeginAuthenticateAsServer(self: NegotiateStream, credential: NetworkCredential, policy: ExtendedProtectionPolicy, requiredProtectionLevel: ProtectionLevel, requiredImpersonationLevel: TokenImpersonationLevel, asyncCallback: AsyncCallback, asyncState: object) -> IAsyncResult

            Called by servers to begin an asynchronous operation to authenticate the client, and optionally the server, in a client-server connection. The authentication process

             uses the specified server credentials, authentication options, and extended protection policy. This method does not block.

            credential: The System.Net.NetworkCredential that is used to establish the identity of the client.

            policy: The System.Security.Authentication.ExtendedProtection.ExtendedProtectionPolicy that is used for extended protection.

            requiredProtectionLevel: One of the System.Net.Security.ProtectionLevel values, indicating the security services for the stream.

            requiredImpersonationLevel: One of the System.Security.Principal.TokenImpersonationLevel values, indicating how the server can use the client's credentials to access resources.

            asyncCallback: An System.AsyncCallback delegate that references the method to invoke when the authentication is complete.

            asyncState: A user-defined object containing information about the write operation. This object is passed to the asyncCallback delegate when the operation completes.

            Returns: An System.IAsyncResult object indicating the status of the asynchronous operation.
        """
        ...
    def BeginRead(self, buffer, offset, count, asyncCallback, asyncState):
        """
        BeginRead(self: NegotiateStream, buffer: Array[Byte], offset: int, count: int, asyncCallback: AsyncCallback, asyncState: object) -> IAsyncResult

            Begins an asynchronous read operation that reads data from the stream and stores it in the specified array.

            buffer: A System.Byte array that receives the bytes read from the stream.

            offset: The zero-based location in buffer at which to begin storing the data read from this stream.

            count: The maximum number of bytes to read from the stream.

            asyncCallback: An System.AsyncCallback delegate that references the method to invoke when the read operation is complete.

            asyncState: A user-defined object containing information about the read operation. This object is passed to the asyncCallback delegate when the operation completes.

            Returns: An System.IAsyncResult object indicating the status of the asynchronous operation.
        """
        ...
    def BeginWrite(self, buffer, offset, count, asyncCallback, asyncState):
        """
        BeginWrite(self: NegotiateStream, buffer: Array[Byte], offset: int, count: int, asyncCallback: AsyncCallback, asyncState: object) -> IAsyncResult

            Begins an asynchronous write operation that writes System.Bytes from the specified buffer to the stream.

            buffer: A System.Byte array that supplies the bytes to be written to the stream.

            offset: The zero-based location in buffer at which to begin reading bytes to be written to the stream.

            count: An System.Int32 value that specifies the number of bytes to read from buffer.

            asyncCallback: An System.AsyncCallback delegate that references the method to invoke when the write operation is complete.

            asyncState: A user-defined object containing information about the write operation. This object is passed to the asyncCallback delegate when the operation completes.

            Returns: An System.IAsyncResult object indicating the status of the asynchronous operation.
        """
        ...
    def EndAuthenticateAsClient(self, asyncResult):
        """
        EndAuthenticateAsClient(self: NegotiateStream, asyncResult: IAsyncResult)

            Ends a pending asynchronous client authentication operation that was started with a call to erload:System.Net.Security.NegotiateStream.BeginAuthenticateAsClient.

            asyncResult: An System.IAsyncResult instance returned by a call to erload:System.Net.Security.NegotiateStream.BeginAuthenticateAsClient.
        """
        ...
    def EndAuthenticateAsServer(self, asyncResult):
        """
        EndAuthenticateAsServer(self: NegotiateStream, asyncResult: IAsyncResult)

            Ends a pending asynchronous client authentication operation that was started with a call to erload:System.Net.Security.NegotiateStream.BeginAuthenticateAsServer.

            asyncResult: An System.IAsyncResult instance returned by a call to erload:System.Net.Security.NegotiateStream.BeginAuthenticateAsServer.
        """
        ...
    def EndRead(self, asyncResult):
        """
        EndRead(self: NegotiateStream, asyncResult: IAsyncResult) -> int

            Ends an asynchronous read operation that was started with a call to

             System.Net.Security.NegotiateStream.BeginRead(System.Byte[],System.Int32,System.Int32,System.AsyncCallback,System.Object).

            asyncResult: An System.IAsyncResult instance returned by a call to

             System.Net.Security.NegotiateStream.BeginRead(System.Byte[],System.Int32,System.Int32,System.AsyncCallback,System.Object)

            Returns: A System.Int32 value that specifies the number of bytes read from the underlying stream.
        """
        ...
    def EndWrite(self, asyncResult):
        """
        EndWrite(self: NegotiateStream, asyncResult: IAsyncResult)

            Ends an asynchronous write operation that was started with a call to

             System.Net.Security.NegotiateStream.BeginWrite(System.Byte[],System.Int32,System.Int32,System.AsyncCallback,System.Object).

            asyncResult: An System.IAsyncResult instance returned by a call to

             System.Net.Security.NegotiateStream.BeginWrite(System.Byte[],System.Int32,System.Int32,System.AsyncCallback,System.Object)
        """
        ...
    def Flush(self):
        """
        Flush(self: NegotiateStream)

            Causes any buffered data to be written to the underlying device.
        """
        ...
    def Read(self, buffer, offset, count):
        """
        Read(self: NegotiateStream, buffer: Array[Byte], offset: int, count: int) -> int

            Reads data from this stream and stores it in the specified array.

            buffer: A System.Byte array that receives the bytes read from the stream.

            offset: A System.Int32 containing the zero-based location in buffer at which to begin storing the data read from this stream.

            count: A System.Int32 containing the maximum number of bytes to read from the stream.

            Returns: A System.Int32 value that specifies the number of bytes read from the underlying stream. When there is no more data to be read, returns 0.
        """
        ...
    def Seek(self, offset, origin):
        """
        Seek(self: NegotiateStream, offset: Int64, origin: SeekOrigin) -> Int64

            Throws System.NotSupportedException.

            offset: This value is ignored.

            origin: This value is ignored.

            Returns: Always throws a System.NotSupportedException.
        """
        ...
    def SetLength(self, value):
        """
        SetLength(self: NegotiateStream, value: Int64)

            Sets the length of the underlying stream.

            value: An System.Int64 value that specifies the length of the stream.
        """
        ...
    def Write(self, buffer, offset, count):
        """
        Write(self: NegotiateStream, buffer: Array[Byte], offset: int, count: int)

            Write the specified number of System.Bytes to the underlying stream using the specified buffer and offset.

            buffer: A System.Byte array that supplies the bytes written to the stream.

            offset: An System.Int32 containing the zero-based location in buffer at which to begin reading bytes to be written to the stream.

            count: A System.Int32 containing the number of bytes to read from buffer.
        """
        ...
    @property
    def CanRead(self):
        """
        Gets a System.Boolean value that indicates whether the underlying stream is readable.

        Get: CanRead(self: NegotiateStream) -> bool
        """
        ...
    @property
    def CanSeek(self):
        """
        Gets a System.Boolean value that indicates whether the underlying stream is seekable.

        Get: CanSeek(self: NegotiateStream) -> bool
        """
        ...
    @property
    def CanTimeout(self):
        """
        Gets a System.Boolean value that indicates whether the underlying stream supports time-outs.

        Get: CanTimeout(self: NegotiateStream) -> bool
        """
        ...
    @property
    def CanWrite(self):
        """
        Gets a System.Boolean value that indicates whether the underlying stream is writable.

        Get: CanWrite(self: NegotiateStream) -> bool
        """
        ...
    @property
    def ImpersonationLevel(self):
        """
        Gets a value that indicates how the server can use the client's credentials.

        Get: ImpersonationLevel(self: NegotiateStream) -> TokenImpersonationLevel
        """
        ...
    @property
    def InnerStream(self):
        """Gets the stream used by this System.Net.Security.AuthenticatedStream for sending and receiving data."""
        ...
    @property
    def IsAuthenticated(self):
        """
        Gets a System.Boolean value that indicates whether authentication was successful.

        Get: IsAuthenticated(self: NegotiateStream) -> bool
        """
        ...
    @property
    def IsEncrypted(self):
        """
        Gets a System.Boolean value that indicates whether this System.Net.Security.NegotiateStream uses data encryption.

        Get: IsEncrypted(self: NegotiateStream) -> bool
        """
        ...
    @property
    def IsMutuallyAuthenticated(self):
        """
        Gets a System.Boolean value that indicates whether both the server and the client have been authenticated.

        Get: IsMutuallyAuthenticated(self: NegotiateStream) -> bool
        """
        ...
    @property
    def IsServer(self):
        """
        Gets a System.Boolean value that indicates whether the local side of the connection used by this System.Net.Security.NegotiateStream was authenticated as the server.

        Get: IsServer(self: NegotiateStream) -> bool
        """
        ...
    @property
    def IsSigned(self):
        """
        Gets a System.Boolean value that indicates whether the data sent using this stream is signed.

        Get: IsSigned(self: NegotiateStream) -> bool
        """
        ...
    @property
    def Length(self):
        """
        Gets the length of the underlying stream.

        Get: Length(self: NegotiateStream) -> Int64
        """
        ...
    @property
    def Position(self):
        """
        Gets or sets the current position in the underlying stream.

        Get: Position(self: NegotiateStream) -> Int64

        Set: Position(self: NegotiateStream) = value
        """
        ...
    @property
    def ReadTimeout(self):
        """
        Gets or sets the amount of time a read operation blocks waiting for data.

        Get: ReadTimeout(self: NegotiateStream) -> int

        Set: ReadTimeout(self: NegotiateStream) = value
        """
        ...
    @property
    def RemoteIdentity(self):
        """
        Gets information about the identity of the remote party sharing this authenticated stream.

        Get: RemoteIdentity(self: NegotiateStream) -> IIdentity
        """
        ...
    @property
    def WriteTimeout(self):
        """
        Gets or sets the amount of time a write operation blocks waiting for data.

        Get: WriteTimeout(self: NegotiateStream) -> int

        Set: WriteTimeout(self: NegotiateStream) = value
        """
        ...

class ProtectionLevel(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Indicates the security services requested for an authenticated stream.

    enum ProtectionLevel, values: EncryptAndSign (2), None (0), Sign (1)
    """

    EncryptAndSign = None

    Sign = None
    value__ = None

class RemoteCertificateValidationCallback(
    MulticastDelegate
):  # skipped bases: <type 'ICloneable'>, <type 'ISerializable'>
    """
    Verifies the remote Secure Sockets Layer (SSL) certificate used for authentication.

    RemoteCertificateValidationCallback(object: object, method: IntPtr)
    """

    def BeginInvoke(self, sender, certificate, chain, sslPolicyErrors, callback, object):
        """BeginInvoke(self: RemoteCertificateValidationCallback, sender: object, certificate: X509Certificate, chain: X509Chain, sslPolicyErrors: SslPolicyErrors, callback: AsyncCallback, object: object) -> IAsyncResult"""
        ...
    def EndInvoke(self, result):
        """EndInvoke(self: RemoteCertificateValidationCallback, result: IAsyncResult) -> bool"""
        ...
    def Invoke(self, sender, certificate, chain, sslPolicyErrors):
        """Invoke(self: RemoteCertificateValidationCallback, sender: object, certificate: X509Certificate, chain: X509Chain, sslPolicyErrors: SslPolicyErrors) -> bool"""
        ...

class SslPolicyErrors(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Enumerates Secure Socket Layer (SSL) policy errors.

    enum (flags) SslPolicyErrors, values: None (0), RemoteCertificateChainErrors (4), RemoteCertificateNameMismatch (2), RemoteCertificateNotAvailable (1)
    """

    RemoteCertificateChainErrors = None
    RemoteCertificateNameMismatch = None
    RemoteCertificateNotAvailable = None
    value__ = None

class SslStream(AuthenticatedStream):  # skipped bases: <type 'IDisposable'>
    """
    Provides a stream used for client-server communication that uses the Secure Socket Layer (SSL) security protocol to authenticate the server and optionally the client.

    SslStream(innerStream: Stream)

    SslStream(innerStream: Stream, leaveInnerStreamOpen: bool)

    SslStream(innerStream: Stream, leaveInnerStreamOpen: bool, userCertificateValidationCallback: RemoteCertificateValidationCallback)

    SslStream(innerStream: Stream, leaveInnerStreamOpen: bool, userCertificateValidationCallback: RemoteCertificateValidationCallback, userCertificateSelectionCallback: LocalCertificateSelectionCallback)

    SslStream(innerStream: Stream, leaveInnerStreamOpen: bool, userCertificateValidationCallback: RemoteCertificateValidationCallback, userCertificateSelectionCallback: LocalCertificateSelectionCallback, encryptionPolicy: EncryptionPolicy)
    """

    def AuthenticateAsClient(self, targetHost, clientCertificates=None, *__args):
        """
        AuthenticateAsClient(self: SslStream, targetHost: str, clientCertificates: X509CertificateCollection, enabledSslProtocols: SslProtocols, checkCertificateRevocation: bool)

            Called by clients to authenticate the server and optionally the client in a client-server connection. The authentication process uses the specified certificate

             collection and SSL protocol.

            targetHost: The name of the server that will share this System.Net.Security.SslStream.

            clientCertificates: The System.Security.Cryptography.X509Certificates.X509CertificateCollection that contains client certificates.

            enabledSslProtocols: The System.Security.Authentication.SslProtocols value that represents the protocol used for authentication.

            checkCertificateRevocation: A System.Boolean value that specifies whether the certificate revocation list is checked during authentication.

        AuthenticateAsClient(self: SslStream, targetHost: str)

            Called by clients to authenticate the server and optionally the client in a client-server connection.

            targetHost: The name of the server that shares this System.Net.Security.SslStream.

        AuthenticateAsClient(self: SslStream, targetHost: str, clientCertificates: X509CertificateCollection, checkCertificateRevocation: bool)

            Called by clients to authenticate the server and optionally the client in a client-server connection. The authentication process uses the specified certificate

             collection, and the system default SSL protocol.

            targetHost: The name of the server that will share this System.Net.Security.SslStream.

            clientCertificates: The System.Security.Cryptography.X509Certificates.X509CertificateCollection that contains client certificates.

            checkCertificateRevocation: A System.Boolean value that specifies whether the certificate revocation list is checked during authentication.
        """
        ...
    def AuthenticateAsClientAsync(self, targetHost, clientCertificates=None, *__args):
        """
        AuthenticateAsClientAsync(self: SslStream, targetHost: str, clientCertificates: X509CertificateCollection, checkCertificateRevocation: bool) -> Task

            Called by clients to authenticate the server and optionally the client in a client-server connection as an asynchronous operation. The authentication process uses the

             specified certificate collection and the system default SSL protocol.

            targetHost: The name of the server that will share this System.Net.Security.SslStream.

            clientCertificates: The System.Security.Cryptography.X509Certificates.X509CertificateCollection that contains client certificates.

            checkCertificateRevocation: A System.Boolean value that specifies whether the certificate revocation list is checked during authentication.

            Returns: The task object representing the asynchronous operation.

        AuthenticateAsClientAsync(self: SslStream, targetHost: str) -> Task

            Called by clients to authenticate the server and optionally the client in a client-server connection as an asynchronous operation.

            targetHost: The name of the server that shares this System.Net.Security.SslStream.

            Returns: Returns System.Threading.Tasks.TaskThe task object representing the asynchronous operation.

        AuthenticateAsClientAsync(self: SslStream, targetHost: str, clientCertificates: X509CertificateCollection, enabledSslProtocols: SslProtocols, checkCertificateRevocation: bool) -> Task

            Called by clients to authenticate the server and optionally the client in a client-server connection as an asynchronous operation. The authentication process uses the

             specified certificate collection and SSL protocol.

            targetHost: The name of the server that will share this System.Net.Security.SslStream.

            clientCertificates: The System.Security.Cryptography.X509Certificates.X509CertificateCollection that contains client certificates.

            enabledSslProtocols: The System.Security.Authentication.SslProtocols value that represents the protocol used for authentication.

            checkCertificateRevocation: A System.Boolean value that specifies whether the certificate revocation list is checked during authentication.

            Returns: Returns System.Threading.Tasks.TaskThe task object representing the asynchronous operation.
        """
        ...
    def AuthenticateAsServer(self, serverCertificate, clientCertificateRequired=None, *__args):
        """
        AuthenticateAsServer(self: SslStream, serverCertificate: X509Certificate)

            Called by servers to authenticate the server and optionally the client in a client-server connection using the specified certificate.

            serverCertificate: The certificate used to authenticate the server.

        AuthenticateAsServer(self: SslStream, serverCertificate: X509Certificate, clientCertificateRequired: bool, checkCertificateRevocation: bool)

            Called by servers to authenticate the server and optionally the client in a client-server connection using the specified certificates and requirements, and using the

             sytem default security protocol.

            serverCertificate: The X509Certificate used to authenticate the server.

            clientCertificateRequired: A System.Boolean value that specifies whether the client is asked for a certificate for authentication. Note that this is only a request -- if no certificate is

             provided, the server still accepts the connection request.

            checkCertificateRevocation: A System.Boolean value that specifies whether the certificate revocation list is checked during authentication.

        AuthenticateAsServer(self: SslStream, serverCertificate: X509Certificate, clientCertificateRequired: bool, enabledSslProtocols: SslProtocols, checkCertificateRevocation: bool)

            Called by servers to authenticate the server and optionally the client in a client-server connection using the specified certificates, requirements and security

             protocol.

            serverCertificate: The X509Certificate used to authenticate the server.

            clientCertificateRequired: A System.Boolean value that specifies whether the client is asked for a certificate for authentication. Note that this is only a request -- if no certificate is

             provided, the server still accepts the connection request.

            enabledSslProtocols: The System.Security.Authentication.SslProtocols  value that represents the protocol used for authentication.

            checkCertificateRevocation: A System.Boolean value that specifies whether the certificate revocation list is checked during authentication.
        """
        ...
    def AuthenticateAsServerAsync(self, serverCertificate, clientCertificateRequired=None, *__args):
        """
        AuthenticateAsServerAsync(self: SslStream, serverCertificate: X509Certificate, clientCertificateRequired: bool, checkCertificateRevocation: bool) -> Task

            Called by servers to authenticate the server and optionally the client in a client-server connection using the specified certificates, requirements and security

             protocol as an asynchronous operation.

            serverCertificate: The X509Certificate used to authenticate the server.

            clientCertificateRequired: A System.Boolean value that specifies whether the client is asked for a certificate for authentication. Note that this is only a request -- if no certificate is

             provided, the server still accepts the connection request.

            checkCertificateRevocation: A System.Boolean value that specifies whether the certificate revocation list is checked during authentication.

            Returns: The task object representing the asynchronous operation.

        AuthenticateAsServerAsync(self: SslStream, serverCertificate: X509Certificate) -> Task

            Called by servers to authenticate the server and optionally the client in a client-server connection using the specified certificate as an asynchronous operation.

            serverCertificate: The certificate used to authenticate the server.

            Returns: Returns System.Threading.Tasks.TaskThe task object representing the asynchronous operation.

        AuthenticateAsServerAsync(self: SslStream, serverCertificate: X509Certificate, clientCertificateRequired: bool, enabledSslProtocols: SslProtocols, checkCertificateRevocation: bool) -> Task

            Called by servers to authenticate the server and optionally the client in a client-server connection using the specified certificates, requirements and security

             protocol as an asynchronous operation.

            serverCertificate: The X509Certificate used to authenticate the server.

            clientCertificateRequired: A System.Boolean value that specifies whether the client is asked for a certificate for authentication. Note that this is only a request -- if no certificate is

             provided, the server still accepts the connection request.

            enabledSslProtocols: The System.Security.Authentication.SslProtocols  value that represents the protocol used for authentication.

            checkCertificateRevocation: A System.Boolean value that specifies whether the certificate revocation list is checked during authentication.

            Returns: Returns System.Threading.Tasks.TaskThe task object representing the asynchronous operation.
        """
        ...
    def BeginAuthenticateAsClient(self, targetHost, *__args):
        """
        BeginAuthenticateAsClient(self: SslStream, targetHost: str, asyncCallback: AsyncCallback, asyncState: object) -> IAsyncResult

            Called by clients to begin an asynchronous operation to authenticate the server and optionally the client.

            targetHost: The name of the server that shares this System.Net.Security.SslStream.

            asyncCallback: An System.AsyncCallback delegate that references the method to invoke when the authentication is complete.

            asyncState: A user-defined object that contains information about the operation. This object is passed to the asyncCallback delegate when the operation completes.

            Returns: An System.IAsyncResult object that indicates the status of the asynchronous operation.

        BeginAuthenticateAsClient(self: SslStream, targetHost: str, clientCertificates: X509CertificateCollection, checkCertificateRevocation: bool, asyncCallback: AsyncCallback, asyncState: object) -> IAsyncResult

            Called by clients to begin an asynchronous operation to authenticate the server and optionally the client using the specified certificates and the system default

             security protocol.

            targetHost: The name of the server that shares this System.Net.Security.SslStream.

            clientCertificates: The System.Security.Cryptography.X509Certificates.X509CertificateCollection containing client certificates.

            checkCertificateRevocation: A System.Boolean value that specifies whether the certificate revocation list is checked during authentication.

            asyncCallback: An System.AsyncCallback delegate that references the method to invoke when the authentication is complete.

            asyncState: A user-defined object that contains information about the operation. This object is passed to the asyncCallback delegate when the operation completes.

            Returns: An System.IAsyncResult object that indicates the status of the asynchronous operation.

        BeginAuthenticateAsClient(self: SslStream, targetHost: str, clientCertificates: X509CertificateCollection, enabledSslProtocols: SslProtocols, checkCertificateRevocation: bool, asyncCallback: AsyncCallback, asyncState: object) -> IAsyncResult

            Called by clients to begin an asynchronous operation to authenticate the server and optionally the client using the specified certificates and security protocol.

            targetHost: The name of the server that shares this System.Net.Security.SslStream.

            clientCertificates: The System.Security.Cryptography.X509Certificates.X509CertificateCollection containing client certificates.

            enabledSslProtocols: The System.Security.Authentication.SslProtocols value that represents the protocol used for authentication.

            checkCertificateRevocation: A System.Boolean value that specifies whether the certificate revocation list is checked during authentication.

            asyncCallback: An System.AsyncCallback delegate that references the method to invoke when the authentication is complete.

            asyncState: A user-defined object that contains information about the operation. This object is passed to the asyncCallback delegate when the operation completes.

            Returns: An System.IAsyncResult object that indicates the status of the asynchronous operation.
        """
        ...
    def BeginAuthenticateAsServer(self, serverCertificate, *__args):
        """
        BeginAuthenticateAsServer(self: SslStream, serverCertificate: X509Certificate, asyncCallback: AsyncCallback, asyncState: object) -> IAsyncResult

            Called by servers to begin an asynchronous operation to authenticate the client and optionally the server in a client-server connection.

            serverCertificate: The X509Certificate used to authenticate the server.

            asyncCallback: An System.AsyncCallback delegate that references the method to invoke when the authentication is complete.

            asyncState: A user-defined object that contains information about the operation. This object is passed to the asyncCallback delegate when the operation completes.

            Returns: An System.IAsyncResult object indicating the status of the asynchronous operation.

        BeginAuthenticateAsServer(self: SslStream, serverCertificate: X509Certificate, clientCertificateRequired: bool, checkCertificateRevocation: bool, asyncCallback: AsyncCallback, asyncState: object) -> IAsyncResult

            Called by servers to begin an asynchronous operation to authenticate the server and optionally the client using the specified certificates and requirements, and the

             system default security protocol.

            serverCertificate: The X509Certificate used to authenticate the server.

            clientCertificateRequired: A System.Boolean value that specifies whether the client is asked for a certificate for authentication. Note that this is only a request -- if no certificate is

             provided, the server still accepts the connection request.

            checkCertificateRevocation: A System.Boolean value that specifies whether the certificate revocation list is checked during authentication.

            asyncCallback: An System.AsyncCallback delegate that references the method to invoke when the authentication is complete.

            asyncState: A user-defined object that contains information about the operation. This object is passed to the asyncCallback delegate when the operation completes.

            Returns: An System.IAsyncResult object that indicates the status of the asynchronous operation.

        BeginAuthenticateAsServer(self: SslStream, serverCertificate: X509Certificate, clientCertificateRequired: bool, enabledSslProtocols: SslProtocols, checkCertificateRevocation: bool, asyncCallback: AsyncCallback, asyncState: object) -> IAsyncResult

            Called by servers to begin an asynchronous operation to authenticate the server and optionally the client using the specified certificates, requirements and security

             protocol.

            serverCertificate: The X509Certificate used to authenticate the server.

            clientCertificateRequired: A System.Boolean value that specifies whether the client is asked for a certificate for authentication. Note that this is only a request -- if no certificate is

             provided, the server still accepts the connection request.

            enabledSslProtocols: The System.Security.Authentication.SslProtocols  value that represents the protocol used for authentication.

            checkCertificateRevocation: A System.Boolean value that specifies whether the certificate revocation list is checked during authentication.

            asyncCallback: An System.AsyncCallback delegate that references the method to invoke when the authentication is complete.

            asyncState: A user-defined object that contains information about the operation. This object is passed to the asyncCallback delegate when the operation completes.

            Returns: An System.IAsyncResult object that indicates the status of the asynchronous operation.
        """
        ...
    def BeginRead(self, buffer, offset, count, asyncCallback, asyncState):
        """
        BeginRead(self: SslStream, buffer: Array[Byte], offset: int, count: int, asyncCallback: AsyncCallback, asyncState: object) -> IAsyncResult

            Begins an asynchronous read operation that reads data from the stream and stores it in the specified array.

            buffer: A System.Byte array that receives the bytes read from the stream.

            offset: The zero-based location in buffer at which to begin storing the data read from this stream.

            count: The maximum number of bytes to read from the stream.

            asyncCallback: An System.AsyncCallback delegate that references the method to invoke when the read operation is complete.

            asyncState: A user-defined object that contains information about the read operation. This object is passed to the asyncCallback delegate when the operation completes.

            Returns: An System.IAsyncResult object that indicates the status of the asynchronous operation.
        """
        ...
    def BeginWrite(self, buffer, offset, count, asyncCallback, asyncState):
        """
        BeginWrite(self: SslStream, buffer: Array[Byte], offset: int, count: int, asyncCallback: AsyncCallback, asyncState: object) -> IAsyncResult

            Begins an asynchronous write operation that writes System.Bytes from the specified buffer to the stream.

            buffer: A System.Byte array that supplies the bytes to be written to the stream.

            offset: The zero-based location in buffer at which to begin reading bytes to be written to the stream.

            count: An System.Int32 value that specifies the number of bytes to read from buffer.

            asyncCallback: An System.AsyncCallback delegate that references the method to invoke when the write operation is complete.

            asyncState: A user-defined object that contains information about the write operation. This object is passed to the asyncCallback delegate when the operation completes.

            Returns: An System.IAsyncResult object indicating the status of the asynchronous operation.
        """
        ...
    def EndAuthenticateAsClient(self, asyncResult):
        """
        EndAuthenticateAsClient(self: SslStream, asyncResult: IAsyncResult)

            Ends a pending asynchronous server authentication operation started with a previous call to erload:System.Net.Security.SslStream.BeginAuthenticateAsServer.

            asyncResult: An System.IAsyncResult instance returned by a call to erload:System.Net.Security.SslStream.BeginAuthenticateAsServer.
        """
        ...
    def EndAuthenticateAsServer(self, asyncResult):
        """
        EndAuthenticateAsServer(self: SslStream, asyncResult: IAsyncResult)

            Ends a pending asynchronous client authentication operation started with a previous call to erload:System.Net.Security.SslStream.BeginAuthenticateAsClient.

            asyncResult: An System.IAsyncResult instance returned by a call to erload:System.Net.Security.SslStream.BeginAuthenticateAsClient.
        """
        ...
    def EndRead(self, asyncResult):
        """
        EndRead(self: SslStream, asyncResult: IAsyncResult) -> int

            Ends an asynchronous read operation started with a previous call to

             System.Net.Security.SslStream.BeginRead(System.Byte[],System.Int32,System.Int32,System.AsyncCallback,System.Object).

            asyncResult: An System.IAsyncResult instance returned by a call to

             System.Net.Security.SslStream.BeginRead(System.Byte[],System.Int32,System.Int32,System.AsyncCallback,System.Object)

            Returns: A System.Int32 value that specifies the number of bytes read from the underlying stream.
        """
        ...
    def EndWrite(self, asyncResult):
        """
        EndWrite(self: SslStream, asyncResult: IAsyncResult)

            Ends an asynchronous write operation started with a previous call to

             System.Net.Security.SslStream.BeginWrite(System.Byte[],System.Int32,System.Int32,System.AsyncCallback,System.Object).

            asyncResult: An System.IAsyncResult instance returned by a call to

             System.Net.Security.SslStream.BeginWrite(System.Byte[],System.Int32,System.Int32,System.AsyncCallback,System.Object)
        """
        ...
    def Flush(self):
        """
        Flush(self: SslStream)

            Causes any buffered data to be written to the underlying device.
        """
        ...
    def Read(self, buffer, offset, count):
        """
        Read(self: SslStream, buffer: Array[Byte], offset: int, count: int) -> int

            Reads data from this stream and stores it in the specified array.

            buffer: A System.Byte array that receives the bytes read from this stream.

            offset: A System.Int32 that contains the zero-based location in buffer at which to begin storing the data read from this stream.

            count: A System.Int32 that contains the maximum number of bytes to read from this stream.

            Returns: A System.Int32 value that specifies the number of bytes read. When there is no more data to be read, returns 0.
        """
        ...
    def Seek(self, offset, origin):
        """
        Seek(self: SslStream, offset: Int64, origin: SeekOrigin) -> Int64

            Throws a System.NotSupportedException.

            offset: This value is ignored.

            origin: This value is ignored.

            Returns: Always throws a System.NotSupportedException.
        """
        ...
    def SetLength(self, value):
        """
        SetLength(self: SslStream, value: Int64)

            Sets the length of the underlying stream.

            value: An System.Int64 value that specifies the length of the stream.
        """
        ...
    def ShutdownAsync(self):
        """
        ShutdownAsync(self: SslStream) -> Task

            Shuts down this SslStream.

            Returns: The task object representing the asynchronous operation.
        """
        ...
    def Write(self, buffer, offset=None, count=None):
        """
        Write(self: SslStream, buffer: Array[Byte], offset: int, count: int)

            Write the specified number of System.Bytes to the underlying stream using the specified buffer and offset.

            buffer: A System.Byte array that supplies the bytes written to the stream.

            offset: A System.Int32 that contains the zero-based location in buffer at which to begin reading bytes to be written to the stream.

            count: A System.Int32 that contains the number of bytes to read from buffer.

        Write(self: SslStream, buffer: Array[Byte])

            Writes the specified data to this stream.

            buffer: A System.Byte array that supplies the bytes written to the stream.
        """
        ...
    @property
    def CanRead(self):
        """
        Gets a System.Boolean value that indicates whether the underlying stream is readable.

        Get: CanRead(self: SslStream) -> bool
        """
        ...
    @property
    def CanSeek(self):
        """
        Gets a System.Boolean value that indicates whether the underlying stream is seekable.

        Get: CanSeek(self: SslStream) -> bool
        """
        ...
    @property
    def CanTimeout(self):
        """
        Gets a System.Boolean value that indicates whether the underlying stream supports time-outs.

        Get: CanTimeout(self: SslStream) -> bool
        """
        ...
    @property
    def CanWrite(self):
        """
        Gets a System.Boolean value that indicates whether the underlying stream is writable.

        Get: CanWrite(self: SslStream) -> bool
        """
        ...
    @property
    def CheckCertRevocationStatus(self):
        """
        Gets a System.Boolean value that indicates whether the certificate revocation list is checked during the certificate validation process.

        Get: CheckCertRevocationStatus(self: SslStream) -> bool
        """
        ...
    @property
    def CipherAlgorithm(self):
        """
        Gets a value that identifies the bulk encryption algorithm used by this System.Net.Security.SslStream.

        Get: CipherAlgorithm(self: SslStream) -> CipherAlgorithmType
        """
        ...
    @property
    def CipherStrength(self):
        """
        Gets a value that identifies the strength of the cipher algorithm used by this System.Net.Security.SslStream.

        Get: CipherStrength(self: SslStream) -> int
        """
        ...
    @property
    def HashAlgorithm(self):
        """
        Gets the algorithm used for generating message authentication codes (MACs).

        Get: HashAlgorithm(self: SslStream) -> HashAlgorithmType
        """
        ...
    @property
    def HashStrength(self):
        """
        Gets a value that identifies the strength of the hash algorithm used by this instance.

        Get: HashStrength(self: SslStream) -> int
        """
        ...
    @property
    def InnerStream(self):
        """Gets the stream used by this System.Net.Security.AuthenticatedStream for sending and receiving data."""
        ...
    @property
    def IsAuthenticated(self):
        """
        Gets a System.Boolean value that indicates whether authentication was successful.

        Get: IsAuthenticated(self: SslStream) -> bool
        """
        ...
    @property
    def IsEncrypted(self):
        """
        Gets a System.Boolean value that indicates whether this System.Net.Security.SslStream uses data encryption.

        Get: IsEncrypted(self: SslStream) -> bool
        """
        ...
    @property
    def IsMutuallyAuthenticated(self):
        """
        Gets a System.Boolean value that indicates whether both server and client have been authenticated.

        Get: IsMutuallyAuthenticated(self: SslStream) -> bool
        """
        ...
    @property
    def IsServer(self):
        """
        Gets a System.Boolean value that indicates whether the local side of the connection used by this System.Net.Security.SslStream was authenticated as the server.

        Get: IsServer(self: SslStream) -> bool
        """
        ...
    @property
    def IsSigned(self):
        """
        Gets a System.Boolean value that indicates whether the data sent using this stream is signed.

        Get: IsSigned(self: SslStream) -> bool
        """
        ...
    @property
    def KeyExchangeAlgorithm(self):
        """
        Gets the key exchange algorithm used by this System.Net.Security.SslStream.

        Get: KeyExchangeAlgorithm(self: SslStream) -> ExchangeAlgorithmType
        """
        ...
    @property
    def KeyExchangeStrength(self):
        """
        Gets a value that identifies the strength of the key exchange algorithm used by this instance.

        Get: KeyExchangeStrength(self: SslStream) -> int
        """
        ...
    @property
    def Length(self):
        """
        Gets the length of the underlying stream.

        Get: Length(self: SslStream) -> Int64
        """
        ...
    @property
    def LocalCertificate(self):
        """
        Gets the certificate used to authenticate the local endpoint.

        Get: LocalCertificate(self: SslStream) -> X509Certificate
        """
        ...
    @property
    def Position(self):
        """
        Gets or sets the current position in the underlying stream.

        Get: Position(self: SslStream) -> Int64

        Set: Position(self: SslStream) = value
        """
        ...
    @property
    def ReadTimeout(self):
        """
        Gets or sets the amount of time a read operation blocks waiting for data.

        Get: ReadTimeout(self: SslStream) -> int

        Set: ReadTimeout(self: SslStream) = value
        """
        ...
    @property
    def RemoteCertificate(self):
        """
        Gets the certificate used to authenticate the remote endpoint.

        Get: RemoteCertificate(self: SslStream) -> X509Certificate
        """
        ...
    @property
    def SslProtocol(self):
        """
        Gets a value that indicates the security protocol used to authenticate this connection.

        Get: SslProtocol(self: SslStream) -> SslProtocols
        """
        ...
    @property
    def TransportContext(self):
        """
        Gets the System.Net.TransportContext used for authentication using extended protection.

        Get: TransportContext(self: SslStream) -> TransportContext
        """
        ...
    @property
    def WriteTimeout(self):
        """
        Gets or sets the amount of time a write operation blocks waiting for data.

        Get: WriteTimeout(self: SslStream) -> int

        Set: WriteTimeout(self: SslStream) = value
        """
        ...
