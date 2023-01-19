# encoding: utf-8
# module System.Net calls itself Net
# from System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AuthenticationManager: # skipped bases: <type 'object'>
    """ Manages the authentication modules called during the client authentication process. """
    @staticmethod
    def Authenticate(challenge, request, credentials):
        """
        Authenticate(challenge: str, request: WebRequest, credentials: ICredentials) -> Authorization

            Calls each registered authentication module to find the first module that can respond to the authentication request.

            challenge: The challenge returned by the Internet resource.

            request: The System.Net.WebRequest that initiated the authentication challenge.

            credentials: The System.Net.ICredentials associated with this request.

            Returns: An instance of the System.Net.Authorization class containing the result of the authorization attempt. If there is no authentication module to respond to the challenge,

             this method returns ll.
        """
        ...

    @staticmethod
    def PreAuthenticate(request, credentials):
        """
        PreAuthenticate(request: WebRequest, credentials: ICredentials) -> Authorization

            Preauthenticates a request.

            request: A System.Net.WebRequest to an Internet resource.

            credentials: The System.Net.ICredentials associated with the request.

            Returns: An instance of the System.Net.Authorization class if the request can be preauthenticated; otherwise, ll. If credentials is ll, this method returns ll.
        """
        ...

    @staticmethod
    def Register(authenticationModule):
        """
        Register(authenticationModule: IAuthenticationModule)

            Registers an authentication module with the authentication manager.

            authenticationModule: The System.Net.IAuthenticationModule to register with the authentication manager.
        """
        ...

    @staticmethod
    def Unregister(*__args):
        """
        Unregister(authenticationModule: IAuthenticationModule)

            Removes the specified authentication module from the list of registered modules.

            authenticationModule: The System.Net.IAuthenticationModule to remove from the list of registered modules.

        Unregister(authenticationScheme: str)

            Removes authentication modules with the specified authentication scheme from the list of registered modules.

            authenticationScheme: The authentication scheme of the module to remove.
        """
        ...

    CredentialPolicy = None
    CustomTargetNameDictionary = None
    RegisteredModules = None


class AuthenticationSchemes(Enum): # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies protocols for authentication.

    enum (flags) AuthenticationSchemes, values: Anonymous (32768), Basic (8), Digest (1), IntegratedWindowsAuthentication (6), Negotiate (2), None (0), Ntlm (4)
    """
    Anonymous = None
    Basic = None
    Digest = None
    IntegratedWindowsAuthentication = None
    Negotiate = None

    Ntlm = None
    value__ = None


class AuthenticationSchemeSelector(MulticastDelegate): # skipped bases: <type 'ICloneable'>, <type 'ISerializable'>
    """
    Selects the authentication scheme for an System.Net.HttpListener instance.

    AuthenticationSchemeSelector(object: object, method: IntPtr)
    """
    def BeginInvoke(self, httpRequest, callback, object):
        """ BeginInvoke(self: AuthenticationSchemeSelector, httpRequest: HttpListenerRequest, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result):
        """ EndInvoke(self: AuthenticationSchemeSelector, result: IAsyncResult) -> AuthenticationSchemes """
        ...

    def Invoke(self, httpRequest):
        """ Invoke(self: AuthenticationSchemeSelector, httpRequest: HttpListenerRequest) -> AuthenticationSchemes """
        ...


class Authorization: # skipped bases: <type 'object'>
    """
    Contains an authentication message for an Internet server.

    Authorization(token: str)

    Authorization(token: str, finished: bool)

    Authorization(token: str, finished: bool, connectionGroupId: str)
    """
    @property
    def Complete(self):
        """
        Gets the completion status of the authorization.

        Get: Complete(self: Authorization) -> bool
        """
        ...

    @property
    def ConnectionGroupId(self):
        """
        Gets a unique identifier for user-specific connections.

        Get: ConnectionGroupId(self: Authorization) -> str
        """
        ...

    @property
    def Message(self):
        """
        Gets the message returned to the server in response to an authentication challenge.

        Get: Message(self: Authorization) -> str
        """
        ...

    @property
    def MutuallyAuthenticated(self):
        """
        Gets or sets a System.Boolean value that indicates whether mutual authentication occurred.

        Get: MutuallyAuthenticated(self: Authorization) -> bool

        Set: MutuallyAuthenticated(self: Authorization) = value
        """
        ...

    @property
    def ProtectionRealm(self):
        """
        Gets or sets the prefix for Uniform Resource Identifiers (URIs) that can be authenticated with the System.Net.Authorization.Message property.

        Get: ProtectionRealm(self: Authorization) -> Array[str]

        Set: ProtectionRealm(self: Authorization) = value
        """
        ...



class BindIPEndPoint(MulticastDelegate): # skipped bases: <type 'ICloneable'>, <type 'ISerializable'>
    """
    Represents the method that specifies a local Internet Protocol address and port number for a System.Net.ServicePoint.

    BindIPEndPoint(object: object, method: IntPtr)
    """
    def BeginInvoke(self, servicePoint, remoteEndPoint, retryCount, callback, object):
        """ BeginInvoke(self: BindIPEndPoint, servicePoint: ServicePoint, remoteEndPoint: IPEndPoint, retryCount: int, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result):
        """ EndInvoke(self: BindIPEndPoint, result: IAsyncResult) -> IPEndPoint """
        ...

    def Invoke(self, servicePoint, remoteEndPoint, retryCount):
        """ Invoke(self: BindIPEndPoint, servicePoint: ServicePoint, remoteEndPoint: IPEndPoint, retryCount: int) -> IPEndPoint """
        ...


class Cookie: # skipped bases: <type 'object'>
    """
    Provides a set of properties and methods that are used to manage cookies. This class cannot be inherited.

    Cookie()

    Cookie(name: str, value: str)

    Cookie(name: str, value: str, path: str)

    Cookie(name: str, value: str, path: str, domain: str)
    """
    def Equals(self, comparand):
        """
        Equals(self: Cookie, comparand: object) -> bool

            Overrides the System.Object.Equals(System.Object) method.

            comparand: A reference to a System.Net.Cookie.

            Returns: Returns ue if the System.Net.Cookie is equal to comparand. Two System.Net.Cookie instances are equal if their System.Net.Cookie.Name, System.Net.Cookie.Value,

             System.Net.Cookie.Path, System.Net.Cookie.Domain, and System.Net.Cookie.Version properties are equal. System.Net.Cookie.Name and System.Net.Cookie.Domain string

             comparisons are case-insensitive.
        """
        ...

    def GetHashCode(self):
        """
        GetHashCode(self: Cookie) -> int

            Overrides the System.Object.GetHashCode method.

            Returns: The 32-bit signed integer hash code for this instance.
        """
        ...

    def ToString(self):
        """
        ToString(self: Cookie) -> str

            Overrides the System.Object.ToString method.

            Returns: Returns a string representation of this System.Net.Cookie object that is suitable for including in a HTTP Cookie: request header.
        """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    @property
    def Comment(self):
        """
        Gets or sets a comment that the server can add to a System.Net.Cookie.

        Get: Comment(self: Cookie) -> str

        Set: Comment(self: Cookie) = value
        """
        ...

    @property
    def CommentUri(self):
        """
        Gets or sets a URI comment that the server can provide with a System.Net.Cookie.

        Get: CommentUri(self: Cookie) -> Uri

        Set: CommentUri(self: Cookie) = value
        """
        ...

    @property
    def Discard(self):
        """
        Gets or sets the discard flag set by the server.

        Get: Discard(self: Cookie) -> bool

        Set: Discard(self: Cookie) = value
        """
        ...

    @property
    def Domain(self):
        """
        Gets or sets the URI for which the System.Net.Cookie is valid.

        Get: Domain(self: Cookie) -> str

        Set: Domain(self: Cookie) = value
        """
        ...

    @property
    def Expired(self):
        """
        Gets or sets the current state of the System.Net.Cookie.

        Get: Expired(self: Cookie) -> bool

        Set: Expired(self: Cookie) = value
        """
        ...

    @property
    def Expires(self):
        """
        Gets or sets the expiration date and time for the System.Net.Cookie as a System.DateTime.

        Get: Expires(self: Cookie) -> DateTime

        Set: Expires(self: Cookie) = value
        """
        ...

    @property
    def HttpOnly(self):
        """
        Determines whether a page script or other active content can access this cookie.

        Get: HttpOnly(self: Cookie) -> bool

        Set: HttpOnly(self: Cookie) = value
        """
        ...

    @property
    def Name(self):
        """
        Gets or sets the name for the System.Net.Cookie.

        Get: Name(self: Cookie) -> str

        Set: Name(self: Cookie) = value
        """
        ...

    @property
    def Path(self):
        """
        Gets or sets the URIs to which the System.Net.Cookie applies.

        Get: Path(self: Cookie) -> str

        Set: Path(self: Cookie) = value
        """
        ...

    @property
    def Port(self):
        """
        Gets or sets a list of TCP ports that the System.Net.Cookie applies to.

        Get: Port(self: Cookie) -> str

        Set: Port(self: Cookie) = value
        """
        ...

    @property
    def Secure(self):
        """
        Gets or sets the security level of a System.Net.Cookie.

        Get: Secure(self: Cookie) -> bool

        Set: Secure(self: Cookie) = value
        """
        ...

    @property
    def TimeStamp(self):
        """
        Gets the time when the cookie was issued as a System.DateTime.

        Get: TimeStamp(self: Cookie) -> DateTime
        """
        ...

    @property
    def Value(self):
        """
        Gets or sets the System.Net.Cookie.Value for the System.Net.Cookie.

        Get: Value(self: Cookie) -> str

        Set: Value(self: Cookie) = value
        """
        ...

    @property
    def Version(self):
        """
        Gets or sets the version of HTTP state maintenance to which the cookie conforms.

        Get: Version(self: Cookie) -> int

        Set: Version(self: Cookie) = value
        """
        ...



class CookieCollection(object, ICollection): # skipped bases: <type 'IEnumerable'>
    """
    Provides a collection container for instances of the System.Net.Cookie class.

    CookieCollection()
    """
    def Add(self, *__args):
        """
        Add(self: CookieCollection, cookie: Cookie)

            Adds a System.Net.Cookie to a System.Net.CookieCollection.

            cookie: The System.Net.Cookie to be added to a System.Net.CookieCollection.

        Add(self: CookieCollection, cookies: CookieCollection)

            Adds the contents of a System.Net.CookieCollection to the current instance.

            cookies: The System.Net.CookieCollection to be added.
        """
        ...

    def GetEnumerator(self):
        """
        GetEnumerator(self: CookieCollection) -> IEnumerator

            Gets an enumerator that can iterate through a System.Net.CookieCollection.

            Returns: An instance of an implementation of an System.Collections.IEnumerator interface that can iterate through a System.Net.CookieCollection.
        """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...

    @property
    def Count(self):
        """
        Gets the number of cookies contained in a System.Net.CookieCollection.

        Get: Count(self: CookieCollection) -> int
        """
        ...

    @property
    def IsReadOnly(self):
        """
        Gets a value that indicates whether a System.Net.CookieCollection is read-only.

        Get: IsReadOnly(self: CookieCollection) -> bool
        """
        ...

    @property
    def IsSynchronized(self):
        """
        Gets a value that indicates whether access to a System.Net.CookieCollection is thread safe.

        Get: IsSynchronized(self: CookieCollection) -> bool
        """
        ...

    @property
    def SyncRoot(self):
        """
        Gets an object to synchronize access to the System.Net.CookieCollection.

        Get: SyncRoot(self: CookieCollection) -> object
        """
        ...



class CookieContainer: # skipped bases: <type 'object'>
    """
    Provides a container for a collection of System.Net.CookieCollection objects.

    CookieContainer()

    CookieContainer(capacity: int)

    CookieContainer(capacity: int, perDomainCapacity: int, maxCookieSize: int)
    """
    def Add(self, *__args):
        """
        Add(self: CookieContainer, cookies: CookieCollection)

            Adds the contents of a System.Net.CookieCollection to the System.Net.CookieContainer.

            cookies: The System.Net.CookieCollection to be added to the System.Net.CookieContainer.

        Add(self: CookieContainer, uri: Uri, cookie: Cookie)

            Adds a System.Net.Cookie to the System.Net.CookieContainer for a particular URI.

            uri: The URI of the System.Net.Cookie to be added to the System.Net.CookieContainer.

            cookie: The System.Net.Cookie to be added to the System.Net.CookieContainer.

        Add(self: CookieContainer, uri: Uri, cookies: CookieCollection)

            Adds the contents of a System.Net.CookieCollection to the System.Net.CookieContainer for a particular URI.

            uri: The URI of the System.Net.CookieCollection to be added to the System.Net.CookieContainer.

            cookies: The System.Net.CookieCollection to be added to the System.Net.CookieContainer.

        Add(self: CookieContainer, cookie: Cookie)

            Adds a System.Net.Cookie to a System.Net.CookieContainer. This method uses the domain from the System.Net.Cookie to determine which domain collection to associate the

             System.Net.Cookie with.

            cookie: The System.Net.Cookie to be added to the System.Net.CookieContainer.
        """
        ...

    def GetCookieHeader(self, uri):
        """
        GetCookieHeader(self: CookieContainer, uri: Uri) -> str

            Gets the HTTP cookie header that contains the HTTP cookies that represent the System.Net.Cookie instances that are associated with a specific URI.

            uri: The URI of the System.Net.Cookie instances desired.

            Returns: An HTTP cookie header, with strings representing System.Net.Cookie instances delimited by semicolons.
        """
        ...

    def GetCookies(self, uri):
        """
        GetCookies(self: CookieContainer, uri: Uri) -> CookieCollection

            Gets a System.Net.CookieCollection that contains the System.Net.Cookie instances that are associated with a specific URI.

            uri: The URI of the System.Net.Cookie instances desired.

            Returns: A System.Net.CookieCollection that contains the System.Net.Cookie instances that are associated with a specific URI.
        """
        ...

    def SetCookies(self, uri, cookieHeader):
        """
        SetCookies(self: CookieContainer, uri: Uri, cookieHeader: str)

            Adds System.Net.Cookie instances for one or more cookies from an HTTP cookie header to the System.Net.CookieContainer for a specific URI.

            uri: The URI of the System.Net.CookieCollection.

            cookieHeader: The contents of an HTTP set-cookie header as returned by a HTTP server, with System.Net.Cookie instances delimited by commas.
        """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        ...

    @property
    def Capacity(self):
        """
        Gets and sets the number of System.Net.Cookie instances that a System.Net.CookieContainer can hold.

        Get: Capacity(self: CookieContainer) -> int

        Set: Capacity(self: CookieContainer) = value
        """
        ...

    @property
    def Count(self):
        """
        Gets the number of System.Net.Cookie instances that a System.Net.CookieContainer currently holds.

        Get: Count(self: CookieContainer) -> int
        """
        ...

    @property
    def MaxCookieSize(self):
        """
        Represents the maximum allowed length of a System.Net.Cookie.

        Get: MaxCookieSize(self: CookieContainer) -> int

        Set: MaxCookieSize(self: CookieContainer) = value
        """
        ...

    @property
    def PerDomainCapacity(self):
        """
        Gets and sets the number of System.Net.Cookie instances that a System.Net.CookieContainer can hold per domain.

        Get: PerDomainCapacity(self: CookieContainer) -> int

        Set: PerDomainCapacity(self: CookieContainer) = value
        """
        ...


    DefaultCookieLengthLimit = 4096
    DefaultCookieLimit = 300
    DefaultPerDomainCookieLimit = 20


class CookieException(FormatException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>
    """
    The exception that is thrown when an error is made adding a System.Net.Cookie to a System.Net.CookieContainer.

    CookieException()
    """
    def GetObjectData(self, serializationInfo, streamingContext):
        """
        GetObjectData(self: CookieException, serializationInfo: SerializationInfo, streamingContext: StreamingContext)

            Populates a System.Runtime.Serialization.SerializationInfo instance with the data needed to serialize the System.Net.CookieException.

            serializationInfo: The object that holds the serialized object data. The System.Runtime.Serialization.SerializationInfo to populate with data.

            streamingContext: The contextual information about the source or destination. A System.Runtime.Serialization.StreamingContext that specifies the destination for this serialization.
        """
        ...

    SerializeObjectState = None


class CredentialCache(object, ICredentials, ICredentialsByHost, IEnumerable):
    """
    Provides storage for multiple credentials.

    CredentialCache()
    """
    def Add(self, *__args):
        """
        Add(self: CredentialCache, uriPrefix: Uri, authType: str, cred: NetworkCredential)

            Adds a System.Net.NetworkCredential instance to the credential cache for use with protocols other than SMTP and associates it with a Uniform Resource Identifier (URI)

             prefix and authentication protocol.

            uriPrefix: A System.Uri that specifies the URI prefix of the resources that the credential grants access to.

            authType: The authentication scheme used by the resource named in uriPrefix.

            cred: The System.Net.NetworkCredential to add to the credential cache.

        Add(self: CredentialCache, host: str, port: int, authenticationType: str, credential: NetworkCredential)

            Adds a System.Net.NetworkCredential instance for use with SMTP to the credential cache and associates it with a host computer, port, and authentication protocol.

             Credentials added using this method are valid for SMTP only. This method does not work for HTTP or FTP requests.

            host: A System.String that identifies the host computer.

            port: A System.Int32 that specifies the port to connect to on host.

            authenticationType: A System.String that identifies the authentication scheme used when connecting to host using cred. See Remarks.

            credential: The System.Net.NetworkCredential to add to the credential cache.
        """
        ...

    def Remove(self, *__args):
        """
        Remove(self: CredentialCache, uriPrefix: Uri, authType: str)

            Deletes a System.Net.NetworkCredential instance from the cache if it is associated with the specified Uniform Resource Identifier (URI) prefix and authentication

             protocol.

            uriPrefix: A System.Uri that specifies the URI prefix of the resources that the credential is used for.

            authType: The authentication scheme used by the host named in uriPrefix.

        Remove(self: CredentialCache, host: str, port: int, authenticationType: str)

            Deletes a System.Net.NetworkCredential instance from the cache if it is associated with the specified host, port, and authentication protocol.

            host: A System.String that identifies the host computer.

            port: A System.Int32 that specifies the port to connect to on host.

            authenticationType: A System.String that identifies the authentication scheme used when connecting to host. See Remarks.
        """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        ...

    DefaultCredentials = None
    DefaultNetworkCredentials = None


class DecompressionMethods(Enum): # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Represents the file compression and decompression encoding format to be used to compress the data received in response to an System.Net.HttpWebRequest.

    enum (flags) DecompressionMethods, values: Deflate (2), GZip (1), None (0)
    """
    Deflate = None
    GZip = None

    value__ = None


class Dns: # skipped bases: <type 'object'>
    """ Provides simple domain name resolution functionality. """
    @staticmethod
    def BeginGetHostAddresses(hostNameOrAddress, requestCallback, state):
        """
        BeginGetHostAddresses(hostNameOrAddress: str, requestCallback: AsyncCallback, state: object) -> IAsyncResult

            Asynchronously returns the Internet Protocol (IP) addresses for the specified host.

            hostNameOrAddress: The host name or IP address to resolve.

            requestCallback: An System.AsyncCallback delegate that references the method to invoke when the operation is complete.

            state: A user-defined object that contains information about the operation. This object is passed to the requestCallback delegate when the operation is complete.

            Returns: An System.IAsyncResult instance that references the asynchronous request.
        """
        ...

    @staticmethod
    def BeginGetHostByName(hostName, requestCallback, stateObject):
        """
        BeginGetHostByName(hostName: str, requestCallback: AsyncCallback, stateObject: object) -> IAsyncResult

            Begins an asynchronous request for System.Net.IPHostEntry information about the specified DNS host name.

            hostName: The DNS name of the host.

            requestCallback: An System.AsyncCallback delegate that references the method to invoke when the operation is complete.

            stateObject: A user-defined object that contains information about the operation. This object is passed to the requestCallback delegate when the operation is complete.

            Returns: An System.IAsyncResult instance that references the asynchronous request.
        """
        ...

    @staticmethod
    def BeginGetHostEntry(*__args):
        """
        BeginGetHostEntry(hostNameOrAddress: str, requestCallback: AsyncCallback, stateObject: object) -> IAsyncResult

            Asynchronously resolves a host name or IP address to an System.Net.IPHostEntry instance.

            hostNameOrAddress: The host name or IP address to resolve.

            requestCallback: An System.AsyncCallback delegate that references the method to invoke when the operation is complete.

            stateObject: A user-defined object that contains information about the operation. This object is passed to the requestCallback delegate when the operation is complete.

            Returns: An System.IAsyncResult instance that references the asynchronous request.

        BeginGetHostEntry(address: IPAddress, requestCallback: AsyncCallback, stateObject: object) -> IAsyncResult

            Asynchronously resolves an IP address to an System.Net.IPHostEntry instance.

            address: The IP address to resolve.

            requestCallback: An System.AsyncCallback delegate that references the method to invoke when the operation is complete.

            stateObject: A user-defined object that contains information about the operation. This object is passed to the requestCallback delegate when the operation is complete.

            Returns: An System.IAsyncResult instance that references the asynchronous request.
        """
        ...

    @staticmethod
    def BeginResolve(hostName, requestCallback, stateObject):
        """
        BeginResolve(hostName: str, requestCallback: AsyncCallback, stateObject: object) -> IAsyncResult

            Begins an asynchronous request to resolve a DNS host name or IP address to an System.Net.IPAddress instance.

            hostName: The DNS name of the host.

            requestCallback: An System.AsyncCallback delegate that references the method to invoke when the operation is complete.

            stateObject: A user-defined object that contains information about the operation. This object is passed to the requestCallback delegate when the operation is complete.

            Returns: An System.IAsyncResult instance that references the asynchronous request.
        """
        ...

    @staticmethod
    def EndGetHostAddresses(asyncResult):
        """
        EndGetHostAddresses(asyncResult: IAsyncResult) -> Array[IPAddress]

            Ends an asynchronous request for DNS information.

            asyncResult: An System.IAsyncResult instance returned by a call to the System.Net.Dns.BeginGetHostAddresses(System.String,System.AsyncCallback,System.Object) method.

            Returns: An array of type System.Net.IPAddress that holds the IP addresses for the host specified by the hostNameOrAddress parameter of

             System.Net.Dns.BeginGetHostAddresses(System.String,System.AsyncCallback,System.Object).
        """
        ...

    @staticmethod
    def EndGetHostByName(asyncResult):
        """
        EndGetHostByName(asyncResult: IAsyncResult) -> IPHostEntry

            Ends an asynchronous request for DNS information.

            asyncResult: An System.IAsyncResult instance that is returned by a call to the System.Net.Dns.BeginGetHostByName(System.String,System.AsyncCallback,System.Object) method.

            Returns: An System.Net.IPHostEntry object that contains DNS information about a host.
        """
        ...

    @staticmethod
    def EndGetHostEntry(asyncResult):
        """
        EndGetHostEntry(asyncResult: IAsyncResult) -> IPHostEntry

            Ends an asynchronous request for DNS information.

            asyncResult: An System.IAsyncResult instance returned by a call to an erload:System.Net.Dns.BeginGetHostEntry method.

            Returns: An System.Net.IPHostEntry instance that contains address information about the host.
        """
        ...

    @staticmethod
    def EndResolve(asyncResult):
        """
        EndResolve(asyncResult: IAsyncResult) -> IPHostEntry

            Ends an asynchronous request for DNS information.

            asyncResult: An System.IAsyncResult instance that is returned by a call to the System.Net.Dns.BeginResolve(System.String,System.AsyncCallback,System.Object) method.

            Returns: An System.Net.IPHostEntry object that contains DNS information about a host.
        """
        ...

    @staticmethod
    def GetHostAddresses(hostNameOrAddress):
        """
        GetHostAddresses(hostNameOrAddress: str) -> Array[IPAddress]

            Returns the Internet Protocol (IP) addresses for the specified host.

            hostNameOrAddress: The host name or IP address to resolve.

            Returns: An array of type System.Net.IPAddress that holds the IP addresses for the host that is specified by the hostNameOrAddress parameter.
        """
        ...

    @staticmethod
    def GetHostAddressesAsync(hostNameOrAddress):
        """
        GetHostAddressesAsync(hostNameOrAddress: str) -> Task[Array[IPAddress]]

            Returns the Internet Protocol (IP) addresses for the specified host as an asynchronous operation.

            hostNameOrAddress: The host name or IP address to resolve.

            Returns: Returns System.Threading.Tasks.Task.The task object representing the asynchronous operation. The System.Threading.Tasks.Task property on the task object returns an

             array of type System.Net.IPAddress that holds the IP addresses for the host that is specified by the hostNameOrAddress parameter.
        """
        ...

    @staticmethod
    def GetHostByAddress(address):
        """
        GetHostByAddress(address: str) -> IPHostEntry

            Creates an System.Net.IPHostEntry instance from an IP address.

            address: An IP address.

            Returns: An System.Net.IPHostEntry instance.

        GetHostByAddress(address: IPAddress) -> IPHostEntry

            Creates an System.Net.IPHostEntry instance from the specified System.Net.IPAddress.

            address: An System.Net.IPAddress.

            Returns: An System.Net.IPHostEntry.An System.Net.IPHostEntry instance.
        """
        ...

    @staticmethod
    def GetHostByName(hostName):
        """
        GetHostByName(hostName: str) -> IPHostEntry

            Gets the DNS information for the specified DNS host name.

            hostName: The DNS name of the host.

            Returns: An System.Net.IPHostEntry object that contains host information for the address specified in hostName.
        """
        ...

    @staticmethod
    def GetHostEntry(*__args):
        """
        GetHostEntry(hostNameOrAddress: str) -> IPHostEntry

            Resolves a host name or IP address to an System.Net.IPHostEntry instance.

            hostNameOrAddress: The host name or IP address to resolve.

            Returns: An System.Net.IPHostEntry instance that contains address information about the host specified in hostNameOrAddress.

        GetHostEntry(address: IPAddress) -> IPHostEntry

            Resolves an IP address to an System.Net.IPHostEntry instance.

            address: An IP address.

            Returns: An System.Net.IPHostEntry instance that contains address information about the host specified in address.
        """
        ...

    @staticmethod
    def GetHostEntryAsync(*__args):
        """
        GetHostEntryAsync(address: IPAddress) -> Task[IPHostEntry]

            Resolves an IP address to an System.Net.IPHostEntry instance as an asynchronous operation.

            address: An IP address.

            Returns: Returns System.Threading.Tasks.Task.The task object representing the asynchronous operation. The System.Threading.Tasks.Task property on the task object returns an

             System.Net.IPHostEntry instance that contains address information about the host specified in address.

        GetHostEntryAsync(hostNameOrAddress: str) -> Task[IPHostEntry]

            Resolves a host name or IP address to an System.Net.IPHostEntry instance as an asynchronous operation.

            hostNameOrAddress: The host name or IP address to resolve.

            Returns: Returns System.Threading.Tasks.Task.The task object representing the asynchronous operation. The System.Threading.Tasks.Task property on the task object returns an

             System.Net.IPHostEntry instance that contains address information about the host specified in hostNameOrAddress.
        """
        ...

    @staticmethod
    def GetHostName():
        """
        GetHostName() -> str

            Gets the host name of the local computer.

            Returns: A string that contains the DNS host name of the local computer.
        """
        ...

    @staticmethod
    def Resolve(hostName):
        """
        Resolve(hostName: str) -> IPHostEntry

            Resolves a DNS host name or IP address to an System.Net.IPHostEntry instance.

            hostName: A DNS-style host name or IP address.

            Returns: An System.Net.IPHostEntry instance that contains address information about the host specified in hostName.
        """
        ...

    __all__ = [
        'BeginGetHostAddresses',
        'BeginGetHostByName',
        'BeginGetHostEntry',
        'BeginResolve',
        'EndGetHostAddresses',
        'EndGetHostByName',
        'EndGetHostEntry',
        'EndResolve',
        'GetHostAddresses',
        'GetHostAddressesAsync',
        'GetHostByAddress',
        'GetHostByName',
        'GetHostEntry',
        'GetHostEntryAsync',
        'GetHostName',
        'Resolve',
    ]


class EndPoint: # skipped bases: <type 'object'>
    """ Identifies a network address. This is an stract class. """
    def Create(self, socketAddress):
        """
        Create(self: EndPoint, socketAddress: SocketAddress) -> EndPoint

            Creates an System.Net.EndPoint instance from a System.Net.SocketAddress instance.

            socketAddress: The socket address that serves as the endpoint for a connection.

            Returns: A new System.Net.EndPoint instance that is initialized from the specified System.Net.SocketAddress instance.
        """
        ...

    def Serialize(self):
        """
        Serialize(self: EndPoint) -> SocketAddress

            Serializes endpoint information into a System.Net.SocketAddress instance.

            Returns: A System.Net.SocketAddress instance that contains the endpoint information.
        """
        ...

    @property
    def AddressFamily(self):
        """
        Gets the address family to which the endpoint belongs.

        Get: AddressFamily(self: EndPoint) -> AddressFamily
        """
        ...



class DnsEndPoint(EndPoint):
    """
    Represents a network endpoint as a host name or a string representation of an IP address and a port number.

    DnsEndPoint(host: str, port: int)

    DnsEndPoint(host: str, port: int, addressFamily: AddressFamily)
    """
    def Equals(self, comparand):
        """
        Equals(self: DnsEndPoint, comparand: object) -> bool

            Compares two System.Net.DnsEndPoint objects.

            comparand: A System.Net.DnsEndPoint instance to compare to the current instance.

            Returns: ue if the two System.Net.DnsEndPoint instances are equal; otherwise, lse.
        """
        ...

    def GetHashCode(self):
        """
        GetHashCode(self: DnsEndPoint) -> int

            Returns a hash value for a System.Net.DnsEndPoint.

            Returns: An integer hash value for the System.Net.DnsEndPoint.
        """
        ...

    def ToString(self):
        """
        ToString(self: DnsEndPoint) -> str

            Returns the host name or string representation of the IP address and port number of the System.Net.DnsEndPoint.

            Returns: A string containing the address family, host name or IP address string, and the port number of the specified System.Net.DnsEndPoint.
        """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    @staticmethod # known case of __new__
    def __new__(cls, host, port, addressFamily=None):
        """
        __new__(cls: type, host: str, port: int)

        __new__(cls: type, host: str, port: int, addressFamily: AddressFamily)
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    @property
    def AddressFamily(self):
        """
        Gets the Internet Protocol (IP) address family.

        Get: AddressFamily(self: DnsEndPoint) -> AddressFamily
        """
        ...

    @property
    def Host(self):
        """
        Gets the host name or string representation of the Internet Protocol (IP) address of the host.

        Get: Host(self: DnsEndPoint) -> str
        """
        ...

    @property
    def Port(self):
        """
        Gets the port number of the System.Net.DnsEndPoint.

        Get: Port(self: DnsEndPoint) -> int
        """
        ...



class DnsPermission(CodeAccessPermission, IUnrestrictedPermission): # skipped bases: <type 'ISecurityEncodable'>, <type 'IPermission'>, <type 'IStackWalk'>
    """
    Controls rights to access Domain Name System (DNS) servers on the network.

    DnsPermission(state: PermissionState)
    """
    @staticmethod # known case of __new__
    def __new__(cls, state):
        """ __new__(cls: type, state: PermissionState) """
        ...


class DnsPermissionAttribute(CodeAccessSecurityAttribute): # skipped bases: <type '_Attribute'>
    """
    Specifies permission to request information from Domain Name Servers.

    DnsPermissionAttribute(action: SecurityAction)
    """
    def CreatePermission(self):
        """
        CreatePermission(self: DnsPermissionAttribute) -> IPermission

            Creates and returns a new instance of the System.Net.DnsPermission class.

            Returns: A System.Net.DnsPermission that corresponds to the security declaration.
        """
        ...


class DownloadDataCompletedEventArgs(AsyncCompletedEventArgs):
    """ Provides data for the System.Net.WebClient.DownloadDataCompleted event. """
    @property
    def Result(self):
        """
        Gets the data that is downloaded by a erload:System.Net.WebClient.DownloadDataAsync method.

        Get: Result(self: DownloadDataCompletedEventArgs) -> Array[Byte]
        """
        ...



class DownloadDataCompletedEventHandler(MulticastDelegate): # skipped bases: <type 'ICloneable'>, <type 'ISerializable'>
    """
    Represents the method that will handle the System.Net.WebClient.DownloadDataCompleted event of a System.Net.WebClient.

    DownloadDataCompletedEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: DownloadDataCompletedEventHandler, sender: object, e: DownloadDataCompletedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result):
        """ EndInvoke(self: DownloadDataCompletedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender, e):
        """ Invoke(self: DownloadDataCompletedEventHandler, sender: object, e: DownloadDataCompletedEventArgs) """
        ...


class DownloadProgressChangedEventArgs(ProgressChangedEventArgs):
    """ Provides data for the System.Net.WebClient.DownloadProgressChanged event of a System.Net.WebClient. """
    @property
    def BytesReceived(self):
        """
        Gets the number of bytes received.

        Get: BytesReceived(self: DownloadProgressChangedEventArgs) -> Int64
        """
        ...

    @property
    def TotalBytesToReceive(self):
        """
        Gets the total number of bytes in a System.Net.WebClient data download operation.

        Get: TotalBytesToReceive(self: DownloadProgressChangedEventArgs) -> Int64
        """
        ...



class DownloadProgressChangedEventHandler(MulticastDelegate): # skipped bases: <type 'ICloneable'>, <type 'ISerializable'>
    """
    Represents the method that will handle the System.Net.WebClient.DownloadProgressChanged event of a System.Net.WebClient.

    DownloadProgressChangedEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: DownloadProgressChangedEventHandler, sender: object, e: DownloadProgressChangedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result):
        """ EndInvoke(self: DownloadProgressChangedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender, e):
        """ Invoke(self: DownloadProgressChangedEventHandler, sender: object, e: DownloadProgressChangedEventArgs) """
        ...


class DownloadStringCompletedEventArgs(AsyncCompletedEventArgs):
    """ Provides data for the System.Net.WebClient.DownloadStringCompleted event. """
    @property
    def Result(self):
        """
        Gets the data that is downloaded by a erload:System.Net.WebClient.DownloadStringAsync method.

        Get: Result(self: DownloadStringCompletedEventArgs) -> str
        """
        ...



class DownloadStringCompletedEventHandler(MulticastDelegate): # skipped bases: <type 'ICloneable'>, <type 'ISerializable'>
    """
    Represents the method that will handle the System.Net.WebClient.DownloadStringCompleted event of a System.Net.WebClient.

    DownloadStringCompletedEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: DownloadStringCompletedEventHandler, sender: object, e: DownloadStringCompletedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result):
        """ EndInvoke(self: DownloadStringCompletedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender, e):
        """ Invoke(self: DownloadStringCompletedEventHandler, sender: object, e: DownloadStringCompletedEventArgs) """
        ...


class EndpointPermission: # skipped bases: <type 'object'>
    """ Defines an endpoint that is authorized by a System.Net.SocketPermission instance. """
    def Equals(self, obj):
        """
        Equals(self: EndpointPermission, obj: object) -> bool

            Determines whether the specified ject is equal to the current ject.

            obj: The System.Object to compare with the current ject.

            Returns: ue if the specified ject is equal to the current ject; otherwise, lse.
        """
        ...

    def GetHashCode(self):
        """
        GetHashCode(self: EndpointPermission) -> int

            Serves as a hash function for a particular type.

            Returns: A hash code for the current System.Object.
        """
        ...

    def ToString(self):
        """
        ToString(self: EndpointPermission) -> str

            Returns a string that represents the current System.Net.EndpointPermission instance.

            Returns: A string that represents the current System.Net.EndpointPermission instance.
        """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    @property
    def Hostname(self):
        """
        Gets the DNS host name or IP address of the server that is associated with this endpoint.

        Get: Hostname(self: EndpointPermission) -> str
        """
        ...

    @property
    def Port(self):
        """
        Gets the network port number that is associated with this endpoint.

        Get: Port(self: EndpointPermission) -> int
        """
        ...

    @property
    def Transport(self):
        """
        Gets the transport type that is associated with this endpoint.

        Get: Transport(self: EndpointPermission) -> TransportType
        """
        ...



class WebRequest(MarshalByRefObject, ISerializable):
    """ Makes a request to a Uniform Resource Identifier (URI). This is an stract class. """
    def Abort(self):
        """
        Abort(self: WebRequest)

            Aborts the Request
        """
        ...

    def BeginGetRequestStream(self, callback, state):
        """
        BeginGetRequestStream(self: WebRequest, callback: AsyncCallback, state: object) -> IAsyncResult

            When overridden in a descendant class, provides an asynchronous version of the System.Net.WebRequest.GetRequestStream method.

            callback: The System.AsyncCallback delegate.

            state: An object containing state information for this asynchronous request.

            Returns: An System.IAsyncResult that references the asynchronous request.
        """
        ...

    def BeginGetResponse(self, callback, state):
        """
        BeginGetResponse(self: WebRequest, callback: AsyncCallback, state: object) -> IAsyncResult

            When overridden in a descendant class, begins an asynchronous request for an Internet resource.

            callback: The System.AsyncCallback delegate.

            state: An object containing state information for this asynchronous request.

            Returns: An System.IAsyncResult that references the asynchronous request.
        """
        ...

    @staticmethod
    def Create(*__args):
        """
        Create(requestUriString: str) -> WebRequest

            Initializes a new System.Net.WebRequest instance for the specified URI scheme.

            requestUriString: The URI that identifies the Internet resource.

            Returns: A System.Net.WebRequest descendant for the specific URI scheme.

        Create(requestUri: Uri) -> WebRequest

            Initializes a new System.Net.WebRequest instance for the specified URI scheme.

            requestUri: A System.Uri containing the URI of the requested resource.

            Returns: A System.Net.WebRequest descendant for the specified URI scheme.
        """
        ...

    @staticmethod
    def CreateDefault(requestUri):
        """
        CreateDefault(requestUri: Uri) -> WebRequest

            Initializes a new System.Net.WebRequest instance for the specified URI scheme.

            requestUri: A System.Uri containing the URI of the requested resource.

            Returns: A System.Net.WebRequest descendant for the specified URI scheme.
        """
        ...

    @staticmethod
    def CreateHttp(*__args):
        """
        CreateHttp(requestUriString: str) -> HttpWebRequest

            Initializes a new System.Net.HttpWebRequest instance for the specified URI string.

            requestUriString: A URI string that identifies the Internet resource.

            Returns: Returns System.Net.HttpWebRequest.An System.Net.HttpWebRequest  instance for the specific URI string.

        CreateHttp(requestUri: Uri) -> HttpWebRequest

            Initializes a new System.Net.HttpWebRequest instance for the specified URI.

            requestUri: A URI that identifies the Internet resource.

            Returns: Returns System.Net.HttpWebRequest.An System.Net.HttpWebRequest instance for the specific URI string.
        """
        ...

    def EndGetRequestStream(self, asyncResult):
        """
        EndGetRequestStream(self: WebRequest, asyncResult: IAsyncResult) -> Stream

            When overridden in a descendant class, returns a System.IO.Stream for writing data to the Internet resource.

            asyncResult: An System.IAsyncResult that references a pending request for a stream.

            Returns: A System.IO.Stream to write data to.
        """
        ...

    def EndGetResponse(self, asyncResult):
        """
        EndGetResponse(self: WebRequest, asyncResult: IAsyncResult) -> WebResponse

            When overridden in a descendant class, returns a System.Net.WebResponse.

            asyncResult: An System.IAsyncResult that references a pending request for a response.

            Returns: A System.Net.WebResponse that contains a response to the Internet request.
        """
        ...

    def GetRequestStream(self):
        """
        GetRequestStream(self: WebRequest) -> Stream

            When overridden in a descendant class, returns a System.IO.Stream for writing data to the Internet resource.

            Returns: A System.IO.Stream for writing data to the Internet resource.
        """
        ...

    def GetRequestStreamAsync(self):
        """
        GetRequestStreamAsync(self: WebRequest) -> Task[Stream]

            When overridden in a descendant class, returns a System.IO.Stream for writing data to the Internet resource as an asynchronous operation.

            Returns: Returns System.Threading.Tasks.Task.The task object representing the asynchronous operation.
        """
        ...

    def GetResponse(self):
        """
        GetResponse(self: WebRequest) -> WebResponse

            When overridden in a descendant class, returns a response to an Internet request.

            Returns: A System.Net.WebResponse containing the response to the Internet request.
        """
        ...

    def GetResponseAsync(self):
        """
        GetResponseAsync(self: WebRequest) -> Task[WebResponse]

            When overridden in a descendant class, returns a response to an Internet request as an asynchronous operation.

            Returns: Returns System.Threading.Tasks.Task.The task object representing the asynchronous operation.
        """
        ...

    @staticmethod
    def GetSystemWebProxy():
        """
        GetSystemWebProxy() -> IWebProxy

            Returns a proxy configured with the Internet Explorer settings of the currently impersonated user.

            Returns: An System.Net.IWebProxy used by every call to instances of System.Net.WebRequest.
        """
        ...

    @staticmethod
    def RegisterPortableWebRequestCreator(creator):
        """
        RegisterPortableWebRequestCreator(creator: IWebRequestCreate)

            Register an System.Net.IWebRequestCreate object.

            creator: The System.Net.IWebRequestCreate object to register.
        """
        ...

    @staticmethod
    def RegisterPrefix(prefix, creator):
        """
        RegisterPrefix(prefix: str, creator: IWebRequestCreate) -> bool

            Registers a System.Net.WebRequest descendant for the specified URI.

            prefix: The complete URI or URI prefix that the System.Net.WebRequest descendant services.

            creator: The create method that the System.Net.WebRequest calls to create the System.Net.WebRequest descendant.

            Returns: ue if registration is successful; otherwise, lse.
        """
        ...

    @staticmethod # known case of __new__
    def __new__(cls, *args): #cannot find CLR constructor
        """
        __new__(cls: type)

        __new__(cls: type, serializationInfo: SerializationInfo, streamingContext: StreamingContext)
        """
        ...

    @property
    def AuthenticationLevel(self):
        """
        Gets or sets values indicating the level of authentication and impersonation used for this request.

        Get: AuthenticationLevel(self: WebRequest) -> AuthenticationLevel

        Set: AuthenticationLevel(self: WebRequest) = value
        """
        ...

    @property
    def CachePolicy(self):
        """
        Gets or sets the cache policy for this request.

        Get: CachePolicy(self: WebRequest) -> RequestCachePolicy

        Set: CachePolicy(self: WebRequest) = value
        """
        ...

    @property
    def ConnectionGroupName(self):
        """
        When overridden in a descendant class, gets or sets the name of the connection group for the request.

        Get: ConnectionGroupName(self: WebRequest) -> str

        Set: ConnectionGroupName(self: WebRequest) = value
        """
        ...

    @property
    def ContentLength(self):
        """
        When overridden in a descendant class, gets or sets the content length of the request data being sent.

        Get: ContentLength(self: WebRequest) -> Int64

        Set: ContentLength(self: WebRequest) = value
        """
        ...

    @property
    def ContentType(self):
        """
        When overridden in a descendant class, gets or sets the content type of the request data being sent.

        Get: ContentType(self: WebRequest) -> str

        Set: ContentType(self: WebRequest) = value
        """
        ...

    @property
    def CreatorInstance(self):
        """
        When overridden in a descendant class, gets the factory object derived from the System.Net.IWebRequestCreate class used to create the System.Net.WebRequest instantiated for making the request to the specified URI.

        Get: CreatorInstance(self: WebRequest) -> IWebRequestCreate
        """
        ...

    @property
    def Credentials(self):
        """
        When overridden in a descendant class, gets or sets the network credentials used for authenticating the request with the Internet resource.

        Get: Credentials(self: WebRequest) -> ICredentials

        Set: Credentials(self: WebRequest) = value
        """
        ...

    @property
    def Headers(self):
        """
        When overridden in a descendant class, gets or sets the collection of header name/value pairs associated with the request.

        Get: Headers(self: WebRequest) -> WebHeaderCollection

        Set: Headers(self: WebRequest) = value
        """
        ...

    @property
    def ImpersonationLevel(self):
        """
        Gets or sets the impersonation level for the current request.

        Get: ImpersonationLevel(self: WebRequest) -> TokenImpersonationLevel

        Set: ImpersonationLevel(self: WebRequest) = value
        """
        ...

    @property
    def Method(self):
        """
        When overridden in a descendant class, gets or sets the protocol method to use in this request.

        Get: Method(self: WebRequest) -> str

        Set: Method(self: WebRequest) = value
        """
        ...

    @property
    def PreAuthenticate(self):
        """
        When overridden in a descendant class, indicates whether to pre-authenticate the request.

        Get: PreAuthenticate(self: WebRequest) -> bool

        Set: PreAuthenticate(self: WebRequest) = value
        """
        ...

    @property
    def Proxy(self):
        """
        When overridden in a descendant class, gets or sets the network proxy to use to access this Internet resource.

        Get: Proxy(self: WebRequest) -> IWebProxy

        Set: Proxy(self: WebRequest) = value
        """
        ...

    @property
    def RequestUri(self):
        """
        When overridden in a descendant class, gets the URI of the Internet resource associated with the request.

        Get: RequestUri(self: WebRequest) -> Uri
        """
        ...

    @property
    def Timeout(self):
        """
        Gets or sets the length of time, in milliseconds, before the request times out.

        Get: Timeout(self: WebRequest) -> int

        Set: Timeout(self: WebRequest) = value
        """
        ...

    @property
    def UseDefaultCredentials(self):
        """
        When overridden in a descendant class, gets or sets a System.Boolean value that controls whether System.Net.CredentialCache.DefaultCredentials are sent with requests.

        Get: UseDefaultCredentials(self: WebRequest) -> bool

        Set: UseDefaultCredentials(self: WebRequest) = value
        """
        ...


    DefaultCachePolicy = None
    DefaultWebProxy = None


class FileWebRequest(WebRequest): # skipped bases: <type 'ISerializable'>
    """ Provides a file system implementation of the System.Net.WebRequest class. """
    @property
    def ConnectionGroupName(self):
        """
        Gets or sets the name of the connection group for the request. This property is reserved for future use.

        Get: ConnectionGroupName(self: FileWebRequest) -> str

        Set: ConnectionGroupName(self: FileWebRequest) = value
        """
        ...

    @property
    def ContentLength(self):
        """
        Gets or sets the content length of the data being sent.

        Get: ContentLength(self: FileWebRequest) -> Int64

        Set: ContentLength(self: FileWebRequest) = value
        """
        ...

    @property
    def ContentType(self):
        """
        Gets or sets the content type of the data being sent. This property is reserved for future use.

        Get: ContentType(self: FileWebRequest) -> str

        Set: ContentType(self: FileWebRequest) = value
        """
        ...

    @property
    def Credentials(self):
        """
        Gets or sets the credentials that are associated with this request. This property is reserved for future use.

        Get: Credentials(self: FileWebRequest) -> ICredentials

        Set: Credentials(self: FileWebRequest) = value
        """
        ...

    @property
    def Headers(self):
        """
        Gets a collection of the name/value pairs that are associated with the request. This property is reserved for future use.

        Get: Headers(self: FileWebRequest) -> WebHeaderCollection
        """
        ...

    @property
    def Method(self):
        """
        Gets or sets the protocol method used for the request. This property is reserved for future use.

        Get: Method(self: FileWebRequest) -> str

        Set: Method(self: FileWebRequest) = value
        """
        ...

    @property
    def PreAuthenticate(self):
        """
        Gets or sets a value that indicates whether to preauthenticate a request. This property is reserved for future use.

        Get: PreAuthenticate(self: FileWebRequest) -> bool

        Set: PreAuthenticate(self: FileWebRequest) = value
        """
        ...

    @property
    def Proxy(self):
        """
        Gets or sets the network proxy to use for this request. This property is reserved for future use.

        Get: Proxy(self: FileWebRequest) -> IWebProxy

        Set: Proxy(self: FileWebRequest) = value
        """
        ...

    @property
    def RequestUri(self):
        """
        Gets the Uniform Resource Identifier (URI) of the request.

        Get: RequestUri(self: FileWebRequest) -> Uri
        """
        ...

    @property
    def Timeout(self):
        """
        Gets or sets the length of time until the request times out.

        Get: Timeout(self: FileWebRequest) -> int

        Set: Timeout(self: FileWebRequest) = value
        """
        ...

    @property
    def UseDefaultCredentials(self):
        """
        Always throws a System.NotSupportedException.

        Get: UseDefaultCredentials(self: FileWebRequest) -> bool

        Set: UseDefaultCredentials(self: FileWebRequest) = value
        """
        ...



class WebResponse(MarshalByRefObject, ISerializable, IDisposable):
    """ Provides a response from a Uniform Resource Identifier (URI). This is an stract class. """
    def Close(self):
        """
        Close(self: WebResponse)

            When overridden by a descendant class, closes the response stream.
        """
        ...

    def GetResponseStream(self):
        """
        GetResponseStream(self: WebResponse) -> Stream

            When overridden in a descendant class, returns the data stream from the Internet resource.

            Returns: An instance of the System.IO.Stream class for reading data from the Internet resource.
        """
        ...

    @staticmethod # known case of __new__
    def __new__(cls, *args): #cannot find CLR constructor
        """
        __new__(cls: type)

        __new__(cls: type, serializationInfo: SerializationInfo, streamingContext: StreamingContext)
        """
        ...

    @property
    def ContentLength(self):
        """
        When overridden in a descendant class, gets or sets the content length of data being received.

        Get: ContentLength(self: WebResponse) -> Int64

        Set: ContentLength(self: WebResponse) = value
        """
        ...

    @property
    def ContentType(self):
        """
        When overridden in a derived class, gets or sets the content type of the data being received.

        Get: ContentType(self: WebResponse) -> str

        Set: ContentType(self: WebResponse) = value
        """
        ...

    @property
    def Headers(self):
        """
        When overridden in a derived class, gets a collection of header name-value pairs associated with this request.

        Get: Headers(self: WebResponse) -> WebHeaderCollection
        """
        ...

    @property
    def IsFromCache(self):
        """
        Gets a System.Boolean value that indicates whether this response was obtained from the cache.

        Get: IsFromCache(self: WebResponse) -> bool
        """
        ...

    @property
    def IsMutuallyAuthenticated(self):
        """
        Gets a System.Boolean value that indicates whether mutual authentication occurred.

        Get: IsMutuallyAuthenticated(self: WebResponse) -> bool
        """
        ...

    @property
    def ResponseUri(self):
        """
        When overridden in a derived class, gets the URI of the Internet resource that actually responded to the request.

        Get: ResponseUri(self: WebResponse) -> Uri
        """
        ...

    @property
    def SupportsHeaders(self):
        """
        Gets a value that indicates if headers are supported.

        Get: SupportsHeaders(self: WebResponse) -> bool
        """
        ...



class FileWebResponse(WebResponse, ICloseEx): # skipped bases: <type 'IDisposable'>, <type 'ISerializable'>
    """ Provides a file system implementation of the System.Net.WebResponse class. """
    @property
    def ContentLength(self):
        """
        Gets the length of the content in the file system resource.

        Get: ContentLength(self: FileWebResponse) -> Int64
        """
        ...

    @property
    def ContentType(self):
        """
        Gets the content type of the file system resource.

        Get: ContentType(self: FileWebResponse) -> str
        """
        ...

    @property
    def Headers(self):
        """
        Gets a collection of header name/value pairs associated with the response.

        Get: Headers(self: FileWebResponse) -> WebHeaderCollection
        """
        ...

    @property
    def ResponseUri(self):
        """
        Gets the URI of the file system resource that provided the response.

        Get: ResponseUri(self: FileWebResponse) -> Uri
        """
        ...

    @property
    def SupportsHeaders(self):
        """
        Gets a value that indicates whether the System.Net.FileWebResponse.Headers property is supported by the System.Net.FileWebResponse instance.

        Get: SupportsHeaders(self: FileWebResponse) -> bool
        """
        ...



class FtpStatusCode(Enum): # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies the status codes returned for a File Transfer Protocol (FTP) operation.

    enum FtpStatusCode, values: AccountNeeded (532), ActionAbortedLocalProcessingError (451), ActionAbortedUnknownPageType (551), ActionNotTakenFilenameNotAllowed (553), ActionNotTakenFileUnavailable (550), ActionNotTakenFileUnavailableOrBusy (450), ActionNotTakenInsufficientSpace (452), ArgumentSyntaxError (501), BadCommandSequence (503), CantOpenData (425), ClosingControl (221), ClosingData (226), CommandExtraneous (202), CommandNotImplemented (502), CommandOK (200), CommandSyntaxError (500), ConnectionClosed (426), DataAlreadyOpen (125), DirectoryStatus (212), EnteringPassive (227), FileActionAborted (552), FileActionOK (250), FileCommandPending (350), FileStatus (213), LoggedInProceed (230), NeedLoginAccount (332), NotLoggedIn (530), OpeningData (150), PathnameCreated (257), RestartMarker (110), SendPasswordCommand (331), SendUserCommand (220), ServerWantsSecureSession (234), ServiceNotAvailable (421), ServiceTemporarilyNotAvailable (120), SystemType (215), Undefined (0)
    """
    AccountNeeded = None
    ActionAbortedLocalProcessingError = None
    ActionAbortedUnknownPageType = None
    ActionNotTakenFilenameNotAllowed = None
    ActionNotTakenFileUnavailable = None
    ActionNotTakenFileUnavailableOrBusy = None
    ActionNotTakenInsufficientSpace = None
    ArgumentSyntaxError = None
    BadCommandSequence = None
    CantOpenData = None
    ClosingControl = None
    ClosingData = None
    CommandExtraneous = None
    CommandNotImplemented = None
    CommandOK = None
    CommandSyntaxError = None
    ConnectionClosed = None
    DataAlreadyOpen = None
    DirectoryStatus = None
    EnteringPassive = None
    FileActionAborted = None
    FileActionOK = None
    FileCommandPending = None
    FileStatus = None
    LoggedInProceed = None
    NeedLoginAccount = None
    NotLoggedIn = None
    OpeningData = None
    PathnameCreated = None
    RestartMarker = None
    SendPasswordCommand = None
    SendUserCommand = None
    ServerWantsSecureSession = None
    ServiceNotAvailable = None
    ServiceTemporarilyNotAvailable = None
    SystemType = None
    Undefined = None
    value__ = None


class FtpWebRequest(WebRequest): # skipped bases: <type 'ISerializable'>
    """ Implements a File Transfer Protocol (FTP) client. """
    @property
    def ClientCertificates(self):
        """
        Gets or sets the certificates used for establishing an encrypted connection to the FTP server.

        Get: ClientCertificates(self: FtpWebRequest) -> X509CertificateCollection

        Set: ClientCertificates(self: FtpWebRequest) = value
        """
        ...

    @property
    def ConnectionGroupName(self):
        """
        Gets or sets the name of the connection group that contains the service point used to send the current request.

        Get: ConnectionGroupName(self: FtpWebRequest) -> str

        Set: ConnectionGroupName(self: FtpWebRequest) = value
        """
        ...

    @property
    def ContentLength(self):
        """
        Gets or sets a value that is ignored by the System.Net.FtpWebRequest class.

        Get: ContentLength(self: FtpWebRequest) -> Int64

        Set: ContentLength(self: FtpWebRequest) = value
        """
        ...

    @property
    def ContentOffset(self):
        """
        Gets or sets a byte offset into the file being downloaded by this request.

        Get: ContentOffset(self: FtpWebRequest) -> Int64

        Set: ContentOffset(self: FtpWebRequest) = value
        """
        ...

    @property
    def ContentType(self):
        """
        Always throws a System.NotSupportedException.

        Get: ContentType(self: FtpWebRequest) -> str

        Set: ContentType(self: FtpWebRequest) = value
        """
        ...

    @property
    def Credentials(self):
        """
        Gets or sets the credentials used to communicate with the FTP server.

        Get: Credentials(self: FtpWebRequest) -> ICredentials

        Set: Credentials(self: FtpWebRequest) = value
        """
        ...

    @property
    def EnableSsl(self):
        """
        Gets or sets a System.Boolean that specifies that an SSL connection should be used.

        Get: EnableSsl(self: FtpWebRequest) -> bool

        Set: EnableSsl(self: FtpWebRequest) = value
        """
        ...

    @property
    def Headers(self):
        """
        Gets an empty System.Net.WebHeaderCollection object.

        Get: Headers(self: FtpWebRequest) -> WebHeaderCollection

        Set: Headers(self: FtpWebRequest) = value
        """
        ...

    @property
    def KeepAlive(self):
        """
        Gets or sets a System.Boolean value that specifies whether the control connection to the FTP server is closed after the request completes.

        Get: KeepAlive(self: FtpWebRequest) -> bool

        Set: KeepAlive(self: FtpWebRequest) = value
        """
        ...

    @property
    def Method(self):
        """
        Gets or sets the command to send to the FTP server.

        Get: Method(self: FtpWebRequest) -> str

        Set: Method(self: FtpWebRequest) = value
        """
        ...

    @property
    def PreAuthenticate(self):
        """
        Always throws a System.NotSupportedException.

        Get: PreAuthenticate(self: FtpWebRequest) -> bool

        Set: PreAuthenticate(self: FtpWebRequest) = value
        """
        ...

    @property
    def Proxy(self):
        """
        Gets or sets the proxy used to communicate with the FTP server.

        Get: Proxy(self: FtpWebRequest) -> IWebProxy

        Set: Proxy(self: FtpWebRequest) = value
        """
        ...

    @property
    def ReadWriteTimeout(self):
        """
        Gets or sets a time-out when reading from or writing to a stream.

        Get: ReadWriteTimeout(self: FtpWebRequest) -> int

        Set: ReadWriteTimeout(self: FtpWebRequest) = value
        """
        ...

    @property
    def RenameTo(self):
        """
        Gets or sets the new name of a file being renamed.

        Get: RenameTo(self: FtpWebRequest) -> str

        Set: RenameTo(self: FtpWebRequest) = value
        """
        ...

    @property
    def RequestUri(self):
        """
        Gets the URI requested by this instance.

        Get: RequestUri(self: FtpWebRequest) -> Uri
        """
        ...

    @property
    def ServicePoint(self):
        """
        Gets the System.Net.ServicePoint object used to connect to the FTP server.

        Get: ServicePoint(self: FtpWebRequest) -> ServicePoint
        """
        ...

    @property
    def Timeout(self):
        """
        Gets or sets the number of milliseconds to wait for a request.

        Get: Timeout(self: FtpWebRequest) -> int

        Set: Timeout(self: FtpWebRequest) = value
        """
        ...

    @property
    def UseBinary(self):
        """
        Gets or sets a System.Boolean value that specifies the data type for file transfers.

        Get: UseBinary(self: FtpWebRequest) -> bool

        Set: UseBinary(self: FtpWebRequest) = value
        """
        ...

    @property
    def UseDefaultCredentials(self):
        """
        Always throws a System.NotSupportedException.

        Get: UseDefaultCredentials(self: FtpWebRequest) -> bool

        Set: UseDefaultCredentials(self: FtpWebRequest) = value
        """
        ...

    @property
    def UsePassive(self):
        """
        Gets or sets the behavior of a client application's data transfer process.

        Get: UsePassive(self: FtpWebRequest) -> bool

        Set: UsePassive(self: FtpWebRequest) = value
        """
        ...


    DefaultCachePolicy = None


class FtpWebResponse(WebResponse): # skipped bases: <type 'IDisposable'>, <type 'ISerializable'>
    """ Encapsulates a File Transfer Protocol (FTP) server's response to a request. """
    @property
    def BannerMessage(self):
        """
        Gets the message sent by the FTP server when a connection is established prior to logon.

        Get: BannerMessage(self: FtpWebResponse) -> str
        """
        ...

    @property
    def ContentLength(self):
        """
        Gets the length of the data received from the FTP server.

        Get: ContentLength(self: FtpWebResponse) -> Int64
        """
        ...

    @property
    def ExitMessage(self):
        """
        Gets the message sent by the server when the FTP session is ending.

        Get: ExitMessage(self: FtpWebResponse) -> str
        """
        ...

    @property
    def Headers(self):
        """
        Gets an empty System.Net.WebHeaderCollection object.

        Get: Headers(self: FtpWebResponse) -> WebHeaderCollection
        """
        ...

    @property
    def LastModified(self):
        """
        Gets the date and time that a file on an FTP server was last modified.

        Get: LastModified(self: FtpWebResponse) -> DateTime
        """
        ...

    @property
    def ResponseUri(self):
        """
        Gets the URI that sent the response to the request.

        Get: ResponseUri(self: FtpWebResponse) -> Uri
        """
        ...

    @property
    def StatusCode(self):
        """
        Gets the most recent status code sent from the FTP server.

        Get: StatusCode(self: FtpWebResponse) -> FtpStatusCode
        """
        ...

    @property
    def StatusDescription(self):
        """
        Gets text that describes a status code sent from the FTP server.

        Get: StatusDescription(self: FtpWebResponse) -> str
        """
        ...

    @property
    def SupportsHeaders(self):
        """
        Gets a value that indicates whether the System.Net.FtpWebResponse.Headers property is supported by the System.Net.FtpWebResponse instance.

        Get: SupportsHeaders(self: FtpWebResponse) -> bool
        """
        ...

    @property
    def WelcomeMessage(self):
        """
        Gets the message sent by the FTP server when authentication is complete.

        Get: WelcomeMessage(self: FtpWebResponse) -> str
        """
        ...



class GlobalProxySelection: # skipped bases: <type 'object'>
    """
    Contains a global default proxy instance for all HTTP requests.

    GlobalProxySelection()
    """
    @staticmethod
    def GetEmptyWebProxy():
        """
        GetEmptyWebProxy() -> IWebProxy

            Returns an empty proxy instance.

            Returns: An System.Net.IWebProxy that contains no information.
        """
        ...

    Select = None


class HttpContinueDelegate(MulticastDelegate): # skipped bases: <type 'ICloneable'>, <type 'ISerializable'>
    """
    Represents the method that notifies callers when a continue response is received by the client.

    HttpContinueDelegate(object: object, method: IntPtr)
    """
    def BeginInvoke(self, StatusCode, httpHeaders, callback, object):
        """ BeginInvoke(self: HttpContinueDelegate, StatusCode: int, httpHeaders: WebHeaderCollection, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result):
        """ EndInvoke(self: HttpContinueDelegate, result: IAsyncResult) """
        ...

    def Invoke(self, StatusCode, httpHeaders):
        """ Invoke(self: HttpContinueDelegate, StatusCode: int, httpHeaders: WebHeaderCollection) """
        ...


class HttpListener(object, IDisposable):
    """
    Provides a simple, programmatically controlled HTTP protocol listener. This class cannot be inherited.

    HttpListener()
    """
    def Abort(self):
        """
        Abort(self: HttpListener)

            Shuts down the System.Net.HttpListener object immediately, discarding all currently queued requests.
        """
        ...

    def BeginGetContext(self, callback, state):
        """
        BeginGetContext(self: HttpListener, callback: AsyncCallback, state: object) -> IAsyncResult

            Begins asynchronously retrieving an incoming request.

            callback: An System.AsyncCallback delegate that references the method to invoke when a client request is available.

            state: A user-defined object that contains information about the operation. This object is passed to the callback delegate when the operation completes.

            Returns: An System.IAsyncResult object that indicates the status of the asynchronous operation.
        """
        ...

    def Close(self):
        """
        Close(self: HttpListener)

            Shuts down the System.Net.HttpListener.
        """
        ...

    def EndGetContext(self, asyncResult):
        """
        EndGetContext(self: HttpListener, asyncResult: IAsyncResult) -> HttpListenerContext

            Completes an asynchronous operation to retrieve an incoming client request.

            asyncResult: An System.IAsyncResult object that was obtained when the asynchronous operation was started.

            Returns: An System.Net.HttpListenerContext object that represents the client request.
        """
        ...

    def ExtendedProtectionSelector(self, *args): #cannot find CLR method
        """ ExtendedProtectionSelector(object: object, method: IntPtr) """
        ...

    def GetContext(self):
        """
        GetContext(self: HttpListener) -> HttpListenerContext

            Waits for an incoming request and returns when one is received.

            Returns: An System.Net.HttpListenerContext object that represents a client request.
        """
        ...

    def GetContextAsync(self):
        """
        GetContextAsync(self: HttpListener) -> Task[HttpListenerContext]

            Waits for an incoming request as an asynchronous operation.

            Returns: Returns System.Threading.Tasks.Task.The task object representing the asynchronous operation. The System.Threading.Tasks.Task property on the task object returns an

             System.Net.HttpListenerContext object that represents a client request.
        """
        ...

    def Start(self):
        """
        Start(self: HttpListener)

            Allows this instance to receive incoming requests.
        """
        ...

    def Stop(self):
        """
        Stop(self: HttpListener)

            Causes this instance to stop receiving incoming requests.
        """
        ...

    @property
    def AuthenticationSchemes(self):
        """
        Gets or sets the scheme used to authenticate clients.

        Get: AuthenticationSchemes(self: HttpListener) -> AuthenticationSchemes

        Set: AuthenticationSchemes(self: HttpListener) = value
        """
        ...

    @property
    def AuthenticationSchemeSelectorDelegate(self):
        """
        Gets or sets the delegate called to determine the protocol used to authenticate clients.

        Get: AuthenticationSchemeSelectorDelegate(self: HttpListener) -> AuthenticationSchemeSelector

        Set: AuthenticationSchemeSelectorDelegate(self: HttpListener) = value
        """
        ...

    @property
    def DefaultServiceNames(self):
        """
        Gets a default list of Service Provider Names (SPNs) as determined by registered prefixes.

        Get: DefaultServiceNames(self: HttpListener) -> ServiceNameCollection
        """
        ...

    @property
    def ExtendedProtectionPolicy(self):
        """
        Get or set the System.Security.Authentication.ExtendedProtection.ExtendedProtectionPolicy to use for extended protection for a session.

        Get: ExtendedProtectionPolicy(self: HttpListener) -> ExtendedProtectionPolicy

        Set: ExtendedProtectionPolicy(self: HttpListener) = value
        """
        ...

    @property
    def ExtendedProtectionSelectorDelegate(self):
        """
        Get or set the delegate called to determine the System.Security.Authentication.ExtendedProtection.ExtendedProtectionPolicy to use for each request.

        Get: ExtendedProtectionSelectorDelegate(self: HttpListener) -> ExtendedProtectionSelector

        Set: ExtendedProtectionSelectorDelegate(self: HttpListener) = value
        """
        ...

    @property
    def IgnoreWriteExceptions(self):
        """
        Gets or sets a System.Boolean value that specifies whether your application receives exceptions that occur when an System.Net.HttpListener sends the response to the client.

        Get: IgnoreWriteExceptions(self: HttpListener) -> bool

        Set: IgnoreWriteExceptions(self: HttpListener) = value
        """
        ...

    @property
    def IsListening(self):
        """
        Gets a value that indicates whether System.Net.HttpListener has been started.

        Get: IsListening(self: HttpListener) -> bool
        """
        ...

    @property
    def Prefixes(self):
        """
        Gets the Uniform Resource Identifier (URI) prefixes handled by this System.Net.HttpListener object.

        Get: Prefixes(self: HttpListener) -> HttpListenerPrefixCollection
        """
        ...

    @property
    def Realm(self):
        """
        Gets or sets the realm, or resource partition, associated with this System.Net.HttpListener object.

        Get: Realm(self: HttpListener) -> str

        Set: Realm(self: HttpListener) = value
        """
        ...

    @property
    def TimeoutManager(self):
        """
        The timeout manager for this System.Net.HttpListener instance.

        Get: TimeoutManager(self: HttpListener) -> HttpListenerTimeoutManager
        """
        ...

    @property
    def UnsafeConnectionNtlmAuthentication(self):
        """
        Gets or sets a System.Boolean value that controls whether, when NTLM is used, additional requests using the same Transmission Control Protocol (TCP) connection are required to authenticate.

        Get: UnsafeConnectionNtlmAuthentication(self: HttpListener) -> bool

        Set: UnsafeConnectionNtlmAuthentication(self: HttpListener) = value
        """
        ...


    ExtendedProtectionSelector = None
    IsSupported = True


class HttpListenerBasicIdentity(GenericIdentity): # skipped bases: <type 'IIdentity'>
    """
    Holds the user name and password from a basic authentication request.

    HttpListenerBasicIdentity(username: str, password: str)
    """
    @property
    def CustomSerializationData(self):
        """  """
        ...

    @property
    def Password(self):
        """
        Indicates the password from a basic authentication attempt.

        Get: Password(self: HttpListenerBasicIdentity) -> str
        """
        ...



class HttpListenerContext: # skipped bases: <type 'object'>
    """ Provides access to the request and response objects used by the System.Net.HttpListener class. This class cannot be inherited. """
    def AcceptWebSocketAsync(self, subProtocol, *__args):
        """
        AcceptWebSocketAsync(self: HttpListenerContext, subProtocol: str) -> Task[HttpListenerWebSocketContext]

            Accept a WebSocket connection as an asynchronous operation.

            subProtocol: The supported WebSocket sub-protocol.

            Returns: Returns System.Threading.Tasks.Task.The task object representing the asynchronous operation. The System.Threading.Tasks.Task property on the task object returns an

             System.Net.WebSockets.HttpListenerWebSocketContext object.

        AcceptWebSocketAsync(self: HttpListenerContext, subProtocol: str, keepAliveInterval: TimeSpan) -> Task[HttpListenerWebSocketContext]

            Accept a WebSocket connection specifying the supported WebSocket sub-protocol  and WebSocket keep-alive interval as an asynchronous operation.

            subProtocol: The supported WebSocket sub-protocol.

            keepAliveInterval: The WebSocket protocol keep-alive interval in milliseconds.

            Returns: Returns System.Threading.Tasks.Task.The task object representing the asynchronous operation. The System.Threading.Tasks.Task property on the task object returns an

             System.Net.WebSockets.HttpListenerWebSocketContext object.

        AcceptWebSocketAsync(self: HttpListenerContext, subProtocol: str, receiveBufferSize: int, keepAliveInterval: TimeSpan) -> Task[HttpListenerWebSocketContext]

            Accept a WebSocket connection specifying the supported WebSocket sub-protocol, receive buffer size, and WebSocket keep-alive interval as an asynchronous operation.

            subProtocol: The supported WebSocket sub-protocol.

            receiveBufferSize: The receive buffer size in bytes.

            keepAliveInterval: The WebSocket protocol keep-alive interval in milliseconds.

            Returns: Returns System.Threading.Tasks.Task.The task object representing the asynchronous operation. The System.Threading.Tasks.Task property on the task object returns an

             System.Net.WebSockets.HttpListenerWebSocketContext object.

        AcceptWebSocketAsync(self: HttpListenerContext, subProtocol: str, receiveBufferSize: int, keepAliveInterval: TimeSpan, internalBuffer: ArraySegment[Byte]) -> Task[HttpListenerWebSocketContext]
        """
        ...

    @property
    def Request(self):
        """
        Gets the System.Net.HttpListenerRequest that represents a client's request for a resource.

        Get: Request(self: HttpListenerContext) -> HttpListenerRequest
        """
        ...

    @property
    def Response(self):
        """
        Gets the System.Net.HttpListenerResponse object that will be sent to the client in response to the client's request.

        Get: Response(self: HttpListenerContext) -> HttpListenerResponse
        """
        ...

    @property
    def User(self):
        """
        Gets an object used to obtain identity, authentication information, and security roles for the client whose request is represented by this System.Net.HttpListenerContext object.

        Get: User(self: HttpListenerContext) -> IPrincipal
        """
        ...



class HttpListenerException(Win32Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>
    """
    The exception that is thrown when an error occurs processing an HTTP request.

    HttpListenerException()

    HttpListenerException(errorCode: int)

    HttpListenerException(errorCode: int, message: str)
    """
    @property
    def ErrorCode(self):
        """
        Gets a value that identifies the error that occurred.

        Get: ErrorCode(self: HttpListenerException) -> int
        """
        ...


    SerializeObjectState = None


class HttpListenerPrefixCollection(object, ICollection[str]): # skipped bases: <type 'IEnumerable'>, <type 'IEnumerable[str]'>
    """ Represents the collection used to store Uniform Resource Identifier (URI) prefixes for System.Net.HttpListener objects. """
    def GetEnumerator(self):
        """
        GetEnumerator(self: HttpListenerPrefixCollection) -> IEnumerator[str]

            Returns an object that can be used to iterate through the collection.

            Returns: An object that implements the System.Collections.IEnumerator interface and provides access to the strings in this collection.
        """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...

    @property
    def Count(self):
        """
        Gets the number of prefixes contained in the collection.

        Get: Count(self: HttpListenerPrefixCollection) -> int
        """
        ...

    @property
    def IsReadOnly(self):
        """
        Gets a value that indicates whether access to the collection is read-only.

        Get: IsReadOnly(self: HttpListenerPrefixCollection) -> bool
        """
        ...

    @property
    def IsSynchronized(self):
        """
        Gets a value that indicates whether access to the collection is synchronized (thread-safe).

        Get: IsSynchronized(self: HttpListenerPrefixCollection) -> bool
        """
        ...



class HttpListenerRequest: # skipped bases: <type 'object'>
    """ Describes an incoming HTTP request to an System.Net.HttpListener object. This class cannot be inherited. """
    def BeginGetClientCertificate(self, requestCallback, state):
        """
        BeginGetClientCertificate(self: HttpListenerRequest, requestCallback: AsyncCallback, state: object) -> IAsyncResult

            Begins an asynchronous request for the client's X.509 v.3 certificate.

            requestCallback: An System.AsyncCallback delegate that references the method to invoke when the operation is complete.

            state: A user-defined object that contains information about the operation. This object is passed to the callback delegate when the operation completes.

            Returns: An System.IAsyncResult that indicates the status of the operation.
        """
        ...

    def EndGetClientCertificate(self, asyncResult):
        """
        EndGetClientCertificate(self: HttpListenerRequest, asyncResult: IAsyncResult) -> X509Certificate2

            Ends an asynchronous request for the client's X.509 v.3 certificate.

            asyncResult: The pending request for the certificate.

            Returns: The System.IAsyncResult object that is returned when the operation started.
        """
        ...

    def GetClientCertificate(self):
        """
        GetClientCertificate(self: HttpListenerRequest) -> X509Certificate2

            Retrieves the client's X.509 v.3 certificate.

            Returns: A System.Security.Cryptography.X509Certificates object that contains the client's X.509 v.3 certificate.
        """
        ...

    def GetClientCertificateAsync(self):
        """
        GetClientCertificateAsync(self: HttpListenerRequest) -> Task[X509Certificate2]

            Retrieves the client's X.509 v.3 certificate as an asynchronous operation.

            Returns: Returns System.Threading.Tasks.Task.The task object representing the asynchronous operation. The System.Threading.Tasks.Task property on the task object returns a

             System.Security.Cryptography.X509Certificates object that contains the client's X.509 v.3 certificate.
        """
        ...

    @property
    def AcceptTypes(self):
        """
        Gets the MIME types accepted by the client.

        Get: AcceptTypes(self: HttpListenerRequest) -> Array[str]
        """
        ...

    @property
    def ClientCertificateError(self):
        """
        Gets an error code that identifies a problem with the System.Security.Cryptography.X509Certificates.X509Certificate provided by the client.

        Get: ClientCertificateError(self: HttpListenerRequest) -> int
        """
        ...

    @property
    def ContentEncoding(self):
        """
        Gets the content encoding that can be used with data sent with the request

        Get: ContentEncoding(self: HttpListenerRequest) -> Encoding
        """
        ...

    @property
    def ContentLength64(self):
        """
        Gets the length of the body data included in the request.

        Get: ContentLength64(self: HttpListenerRequest) -> Int64
        """
        ...

    @property
    def ContentType(self):
        """
        Gets the MIME type of the body data included in the request.

        Get: ContentType(self: HttpListenerRequest) -> str
        """
        ...

    @property
    def Cookies(self):
        """
        Gets the cookies sent with the request.

        Get: Cookies(self: HttpListenerRequest) -> CookieCollection
        """
        ...

    @property
    def HasEntityBody(self):
        """
        Gets a System.Boolean value that indicates whether the request has associated body data.

        Get: HasEntityBody(self: HttpListenerRequest) -> bool
        """
        ...

    @property
    def Headers(self):
        """
        Gets the collection of header name/value pairs sent in the request.

        Get: Headers(self: HttpListenerRequest) -> NameValueCollection
        """
        ...

    @property
    def HttpMethod(self):
        """
        Gets the HTTP method specified by the client.

        Get: HttpMethod(self: HttpListenerRequest) -> str
        """
        ...

    @property
    def InputStream(self):
        """
        Gets a stream that contains the body data sent by the client.

        Get: InputStream(self: HttpListenerRequest) -> Stream
        """
        ...

    @property
    def IsAuthenticated(self):
        """
        Gets a System.Boolean value that indicates whether the client sending this request is authenticated.

        Get: IsAuthenticated(self: HttpListenerRequest) -> bool
        """
        ...

    @property
    def IsLocal(self):
        """
        Gets a System.Boolean value that indicates whether the request is sent from the local computer.

        Get: IsLocal(self: HttpListenerRequest) -> bool
        """
        ...

    @property
    def IsSecureConnection(self):
        """
        Gets a System.Boolean value that indicates whether the TCP connection used to send the request is using the Secure Sockets Layer (SSL) protocol.

        Get: IsSecureConnection(self: HttpListenerRequest) -> bool
        """
        ...

    @property
    def IsWebSocketRequest(self):
        """
        Gets a System.Boolean value that indicates whether the TCP connection was  a WebSocket request.

        Get: IsWebSocketRequest(self: HttpListenerRequest) -> bool
        """
        ...

    @property
    def KeepAlive(self):
        """
        Gets a System.Boolean value that indicates whether the client requests a persistent connection.

        Get: KeepAlive(self: HttpListenerRequest) -> bool
        """
        ...

    @property
    def LocalEndPoint(self):
        """
        Get the server IP address and port number to which the request is directed.

        Get: LocalEndPoint(self: HttpListenerRequest) -> IPEndPoint
        """
        ...

    @property
    def ProtocolVersion(self):
        """
        Gets the HTTP version used by the requesting client.

        Get: ProtocolVersion(self: HttpListenerRequest) -> Version
        """
        ...

    @property
    def QueryString(self):
        """
        Gets the query string included in the request.

        Get: QueryString(self: HttpListenerRequest) -> NameValueCollection
        """
        ...

    @property
    def RawUrl(self):
        """
        Gets the URL information (without the host and port) requested by the client.

        Get: RawUrl(self: HttpListenerRequest) -> str
        """
        ...

    @property
    def RemoteEndPoint(self):
        """
        Gets the client IP address and port number from which the request originated.

        Get: RemoteEndPoint(self: HttpListenerRequest) -> IPEndPoint
        """
        ...

    @property
    def RequestTraceIdentifier(self):
        """
        Gets the request identifier of the incoming HTTP request.

        Get: RequestTraceIdentifier(self: HttpListenerRequest) -> Guid
        """
        ...

    @property
    def ServiceName(self):
        """
        Gets the Service Provider Name (SPN) that the client sent on the request.

        Get: ServiceName(self: HttpListenerRequest) -> str
        """
        ...

    @property
    def TransportContext(self):
        """
        Gets the System.Net.TransportContext for the client request.

        Get: TransportContext(self: HttpListenerRequest) -> TransportContext
        """
        ...

    @property
    def Url(self):
        """
        Gets the System.Uri object requested by the client.

        Get: Url(self: HttpListenerRequest) -> Uri
        """
        ...

    @property
    def UrlReferrer(self):
        """
        Gets the Uniform Resource Identifier (URI) of the resource that referred the client to the server.

        Get: UrlReferrer(self: HttpListenerRequest) -> Uri
        """
        ...

    @property
    def UserAgent(self):
        """
        Gets the user agent presented by the client.

        Get: UserAgent(self: HttpListenerRequest) -> str
        """
        ...

    @property
    def UserHostAddress(self):
        """
        Gets the server IP address and port number to which the request is directed.

        Get: UserHostAddress(self: HttpListenerRequest) -> str
        """
        ...

    @property
    def UserHostName(self):
        """
        Gets the DNS name and, if provided, the port number specified by the client.

        Get: UserHostName(self: HttpListenerRequest) -> str
        """
        ...

    @property
    def UserLanguages(self):
        """
        Gets the natural languages that are preferred for the response.

        Get: UserLanguages(self: HttpListenerRequest) -> Array[str]
        """
        ...



class HttpListenerResponse(object, IDisposable):
    """ Represents a response to a request being handled by an System.Net.HttpListener object. """
    def Abort(self):
        """
        Abort(self: HttpListenerResponse)

            Closes the connection to the client without sending a response.
        """
        ...

    def AddHeader(self, name, value):
        """
        AddHeader(self: HttpListenerResponse, name: str, value: str)

            Adds the specified header and value to the HTTP headers for this response.

            name: The name of the HTTP header to set.

            value: The value for the name header.
        """
        ...

    def AppendCookie(self, cookie):
        """
        AppendCookie(self: HttpListenerResponse, cookie: Cookie)

            Adds the specified System.Net.Cookie to the collection of cookies for this response.

            cookie: The System.Net.Cookie to add to the collection to be sent with this response.
        """
        ...

    def AppendHeader(self, name, value):
        """
        AppendHeader(self: HttpListenerResponse, name: str, value: str)

            Appends a value to the specified HTTP header to be sent with this response.

            name: The name of the HTTP header to append value to.

            value: The value to append to the name header.
        """
        ...

    def Close(self, responseEntity=None, willBlock=None):
        """
        Close(self: HttpListenerResponse, responseEntity: Array[Byte], willBlock: bool)

            Returns the specified byte array to the client and releases the resources held by this System.Net.HttpListenerResponse instance.

            responseEntity: A System.Byte array that contains the response to send to the client.

            willBlock: ue to block execution while flushing the stream to the client; otherwise, lse.

        Close(self: HttpListenerResponse)

            Sends the response to the client and releases the resources held by this System.Net.HttpListenerResponse instance.
        """
        ...

    def CopyFrom(self, templateResponse):
        """
        CopyFrom(self: HttpListenerResponse, templateResponse: HttpListenerResponse)

            Copies properties from the specified System.Net.HttpListenerResponse to this response.

            templateResponse: The System.Net.HttpListenerResponse instance to copy.
        """
        ...

    def Redirect(self, url):
        """
        Redirect(self: HttpListenerResponse, url: str)

            Configures the response to redirect the client to the specified URL.

            url: The URL that the client should use to locate the requested resource.
        """
        ...

    def SetCookie(self, cookie):
        """
        SetCookie(self: HttpListenerResponse, cookie: Cookie)

            Adds or updates a System.Net.Cookie in the collection of cookies sent with this response.

            cookie: A System.Net.Cookie for this response.
        """
        ...

    @property
    def ContentEncoding(self):
        """
        Gets or sets the System.Text.Encoding for this response's System.Net.HttpListenerResponse.OutputStream.

        Get: ContentEncoding(self: HttpListenerResponse) -> Encoding

        Set: ContentEncoding(self: HttpListenerResponse) = value
        """
        ...

    @property
    def ContentLength64(self):
        """
        Gets or sets the number of bytes in the body data included in the response.

        Get: ContentLength64(self: HttpListenerResponse) -> Int64

        Set: ContentLength64(self: HttpListenerResponse) = value
        """
        ...

    @property
    def ContentType(self):
        """
        Gets or sets the MIME type of the content returned.

        Get: ContentType(self: HttpListenerResponse) -> str

        Set: ContentType(self: HttpListenerResponse) = value
        """
        ...

    @property
    def Cookies(self):
        """
        Gets or sets the collection of cookies returned with the response.

        Get: Cookies(self: HttpListenerResponse) -> CookieCollection

        Set: Cookies(self: HttpListenerResponse) = value
        """
        ...

    @property
    def Headers(self):
        """
        Gets or sets the collection of header name/value pairs returned by the server.

        Get: Headers(self: HttpListenerResponse) -> WebHeaderCollection

        Set: Headers(self: HttpListenerResponse) = value
        """
        ...

    @property
    def KeepAlive(self):
        """
        Gets or sets a value indicating whether the server requests a persistent connection.

        Get: KeepAlive(self: HttpListenerResponse) -> bool

        Set: KeepAlive(self: HttpListenerResponse) = value
        """
        ...

    @property
    def OutputStream(self):
        """
        Gets a System.IO.Stream object to which a response can be written.

        Get: OutputStream(self: HttpListenerResponse) -> Stream
        """
        ...

    @property
    def ProtocolVersion(self):
        """
        Gets or sets the HTTP version used for the response.

        Get: ProtocolVersion(self: HttpListenerResponse) -> Version

        Set: ProtocolVersion(self: HttpListenerResponse) = value
        """
        ...

    @property
    def RedirectLocation(self):
        """
        Gets or sets the value of the HTTP cation header in this response.

        Get: RedirectLocation(self: HttpListenerResponse) -> str

        Set: RedirectLocation(self: HttpListenerResponse) = value
        """
        ...

    @property
    def SendChunked(self):
        """
        Gets or sets whether the response uses chunked transfer encoding.

        Get: SendChunked(self: HttpListenerResponse) -> bool

        Set: SendChunked(self: HttpListenerResponse) = value
        """
        ...

    @property
    def StatusCode(self):
        """
        Gets or sets the HTTP status code to be returned to the client.

        Get: StatusCode(self: HttpListenerResponse) -> int

        Set: StatusCode(self: HttpListenerResponse) = value
        """
        ...

    @property
    def StatusDescription(self):
        """
        Gets or sets a text description of the HTTP status code returned to the client.

        Get: StatusDescription(self: HttpListenerResponse) -> str

        Set: StatusDescription(self: HttpListenerResponse) = value
        """
        ...



class HttpListenerTimeoutManager: # skipped bases: <type 'object'>
    """ The timeout manager to use for an System.Net.HttpListener object. """
    @property
    def DrainEntityBody(self):
        """
        Gets or sets the time, in seconds, allowed for the System.Net.HttpListener  to drain the entity body on a Keep-Alive connection.

        Get: DrainEntityBody(self: HttpListenerTimeoutManager) -> TimeSpan

        Set: DrainEntityBody(self: HttpListenerTimeoutManager) = value
        """
        ...

    @property
    def EntityBody(self):
        """
        Gets or sets the time, in seconds, allowed for the request entity body to arrive.

        Get: EntityBody(self: HttpListenerTimeoutManager) -> TimeSpan

        Set: EntityBody(self: HttpListenerTimeoutManager) = value
        """
        ...

    @property
    def HeaderWait(self):
        """
        Gets or sets the time, in seconds, allowed for the System.Net.HttpListener to parse the request header.

        Get: HeaderWait(self: HttpListenerTimeoutManager) -> TimeSpan

        Set: HeaderWait(self: HttpListenerTimeoutManager) = value
        """
        ...

    @property
    def IdleConnection(self):
        """
        Gets or sets the time, in seconds, allowed for an idle connection.

        Get: IdleConnection(self: HttpListenerTimeoutManager) -> TimeSpan

        Set: IdleConnection(self: HttpListenerTimeoutManager) = value
        """
        ...

    @property
    def MinSendBytesPerSecond(self):
        """
        Gets or sets the minimum send rate, in bytes-per-second, for the response.

        Get: MinSendBytesPerSecond(self: HttpListenerTimeoutManager) -> Int64

        Set: MinSendBytesPerSecond(self: HttpListenerTimeoutManager) = value
        """
        ...

    @property
    def RequestQueue(self):
        """
        Gets or sets the time, in seconds, allowed for the request to remain in the request queue before the System.Net.HttpListener picks it up.

        Get: RequestQueue(self: HttpListenerTimeoutManager) -> TimeSpan

        Set: RequestQueue(self: HttpListenerTimeoutManager) = value
        """
        ...



class HttpRequestHeader(Enum): # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    The HTTP headers that may be specified in a client request.

    enum HttpRequestHeader, values: Accept (20), AcceptCharset (21), AcceptEncoding (22), AcceptLanguage (23), Allow (10), Authorization (24), CacheControl (0), Connection (1), ContentEncoding (13), ContentLanguage (14), ContentLength (11), ContentLocation (15), ContentMd5 (16), ContentRange (17), ContentType (12), Cookie (25), Date (2), Expect (26), Expires (18), From (27), Host (28), IfMatch (29), IfModifiedSince (30), IfNoneMatch (31), IfRange (32), IfUnmodifiedSince (33), KeepAlive (3), LastModified (19), MaxForwards (34), Pragma (4), ProxyAuthorization (35), Range (37), Referer (36), Te (38), Trailer (5), TransferEncoding (6), Translate (39), Upgrade (7), UserAgent (40), Via (8), Warning (9)
    """
    Accept = None
    AcceptCharset = None
    AcceptEncoding = None
    AcceptLanguage = None
    Allow = None
    Authorization = None
    CacheControl = None
    Connection = None
    ContentEncoding = None
    ContentLanguage = None
    ContentLength = None
    ContentLocation = None
    ContentMd5 = None
    ContentRange = None
    ContentType = None
    Cookie = None
    Date = None
    Expect = None
    Expires = None
    From = None
    Host = None
    IfMatch = None
    IfModifiedSince = None
    IfNoneMatch = None
    IfRange = None
    IfUnmodifiedSince = None
    KeepAlive = None
    LastModified = None
    MaxForwards = None
    Pragma = None
    ProxyAuthorization = None
    Range = None
    Referer = None
    Te = None
    Trailer = None
    TransferEncoding = None
    Translate = None
    Upgrade = None
    UserAgent = None
    value__ = None
    Via = None
    Warning = None


class HttpResponseHeader(Enum): # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    The HTTP headers that can be specified in a server response.

    enum HttpResponseHeader, values: AcceptRanges (20), Age (21), Allow (10), CacheControl (0), Connection (1), ContentEncoding (13), ContentLanguage (14), ContentLength (11), ContentLocation (15), ContentMd5 (16), ContentRange (17), ContentType (12), Date (2), ETag (22), Expires (18), KeepAlive (3), LastModified (19), Location (23), Pragma (4), ProxyAuthenticate (24), RetryAfter (25), Server (26), SetCookie (27), Trailer (5), TransferEncoding (6), Upgrade (7), Vary (28), Via (8), Warning (9), WwwAuthenticate (29)
    """
    AcceptRanges = None
    Age = None
    Allow = None
    CacheControl = None
    Connection = None
    ContentEncoding = None
    ContentLanguage = None
    ContentLength = None
    ContentLocation = None
    ContentMd5 = None
    ContentRange = None
    ContentType = None
    Date = None
    ETag = None
    Expires = None
    KeepAlive = None
    LastModified = None
    Location = None
    Pragma = None
    ProxyAuthenticate = None
    RetryAfter = None
    Server = None
    SetCookie = None
    Trailer = None
    TransferEncoding = None
    Upgrade = None
    value__ = None
    Vary = None
    Via = None
    Warning = None
    WwwAuthenticate = None


class HttpStatusCode(Enum): # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Contains the values of status codes defined for HTTP.

    enum HttpStatusCode, values: Accepted (202), Ambiguous (300), BadGateway (502), BadRequest (400), Conflict (409), Continue (100), Created (201), ExpectationFailed (417), Forbidden (403), Found (302), GatewayTimeout (504), Gone (410), HttpVersionNotSupported (505), InternalServerError (500), LengthRequired (411), MethodNotAllowed (405), Moved (301), MovedPermanently (301), MultipleChoices (300), NoContent (204), NonAuthoritativeInformation (203), NotAcceptable (406), NotFound (404), NotImplemented (501), NotModified (304), OK (200), PartialContent (206), PaymentRequired (402), PreconditionFailed (412), ProxyAuthenticationRequired (407), Redirect (302), RedirectKeepVerb (307), RedirectMethod (303), RequestedRangeNotSatisfiable (416), RequestEntityTooLarge (413), RequestTimeout (408), RequestUriTooLong (414), ResetContent (205), SeeOther (303), ServiceUnavailable (503), SwitchingProtocols (101), TemporaryRedirect (307), Unauthorized (401), UnsupportedMediaType (415), Unused (306), UpgradeRequired (426), UseProxy (305)
    """
    Accepted = None
    Ambiguous = None
    BadGateway = None
    BadRequest = None
    Conflict = None
    Continue = None
    Created = None
    ExpectationFailed = None
    Forbidden = None
    Found = None
    GatewayTimeout = None
    Gone = None
    HttpVersionNotSupported = None
    InternalServerError = None
    LengthRequired = None
    MethodNotAllowed = None
    Moved = None
    MovedPermanently = None
    MultipleChoices = None
    NoContent = None
    NonAuthoritativeInformation = None
    NotAcceptable = None
    NotFound = None
    NotImplemented = None
    NotModified = None
    OK = None
    PartialContent = None
    PaymentRequired = None
    PreconditionFailed = None
    ProxyAuthenticationRequired = None
    Redirect = None
    RedirectKeepVerb = None
    RedirectMethod = None
    RequestedRangeNotSatisfiable = None
    RequestEntityTooLarge = None
    RequestTimeout = None
    RequestUriTooLong = None
    ResetContent = None
    SeeOther = None
    ServiceUnavailable = None
    SwitchingProtocols = None
    TemporaryRedirect = None
    Unauthorized = None
    UnsupportedMediaType = None
    Unused = None
    UpgradeRequired = None
    UseProxy = None
    value__ = None


class HttpVersion: # skipped bases: <type 'object'>
    """
    Defines the HTTP version numbers that are supported by the System.Net.HttpWebRequest and System.Net.HttpWebResponse classes.

    HttpVersion()
    """
    Version10 = None
    Version11 = None


class HttpWebRequest(WebRequest): # skipped bases: <type 'ISerializable'>
    """
    Provides an HTTP-specific implementation of the System.Net.WebRequest class.

    HttpWebRequest()
    """
    def AddRange(self, *__args):
        """
        AddRange(self: HttpWebRequest, from: int, to: int)

            Adds a byte range header to the request for a specified range.

            from: The position at which to start sending data.

            to: The position at which to stop sending data.

        AddRange(self: HttpWebRequest, from: Int64, to: Int64)

            Adds a byte range header to the request for a specified range.

            from: The position at which to start sending data.

            to: The position at which to stop sending data.

        AddRange(self: HttpWebRequest, range: int)

            Adds a byte range header to a request for a specific range from the beginning or end of the requested data.

            range: The starting or ending point of the range.

        AddRange(self: HttpWebRequest, range: Int64)

            Adds a byte range header to a request for a specific range from the beginning or end of the requested data.

            range: The starting or ending point of the range.

        AddRange(self: HttpWebRequest, rangeSpecifier: str, from: int, to: int)

            Adds a range header to a request for a specified range.

            rangeSpecifier: The description of the range.

            from: The position at which to start sending data.

            to: The position at which to stop sending data.

        AddRange(self: HttpWebRequest, rangeSpecifier: str, from: Int64, to: Int64)

            Adds a range header to a request for a specified range.

            rangeSpecifier: The description of the range.

            from: The position at which to start sending data.

            to: The position at which to stop sending data.

        AddRange(self: HttpWebRequest, rangeSpecifier: str, range: int)

            Adds a Range header to a request for a specific range from the beginning or end of the requested data.

            rangeSpecifier: The description of the range.

            range: The starting or ending point of the range.

        AddRange(self: HttpWebRequest, rangeSpecifier: str, range: Int64)

            Adds a Range header to a request for a specific range from the beginning or end of the requested data.

            rangeSpecifier: The description of the range.

            range: The starting or ending point of the range.
        """
        ...

    @property
    def Accept(self):
        """
        Gets or sets the value of the cept HTTP header.

        Get: Accept(self: HttpWebRequest) -> str

        Set: Accept(self: HttpWebRequest) = value
        """
        ...

    @property
    def Address(self):
        """
        Gets the Uniform Resource Identifier (URI) of the Internet resource that actually responds to the request.

        Get: Address(self: HttpWebRequest) -> Uri
        """
        ...

    @property
    def AllowAutoRedirect(self):
        """
        Gets or sets a value that indicates whether the request should follow redirection responses.

        Get: AllowAutoRedirect(self: HttpWebRequest) -> bool

        Set: AllowAutoRedirect(self: HttpWebRequest) = value
        """
        ...

    @property
    def AllowReadStreamBuffering(self):
        """
        Gets or sets a value that indicates whether to buffer the received from the Internet resource.

        Get: AllowReadStreamBuffering(self: HttpWebRequest) -> bool

        Set: AllowReadStreamBuffering(self: HttpWebRequest) = value
        """
        ...

    @property
    def AllowWriteStreamBuffering(self):
        """
        Gets or sets a value that indicates whether to buffer the data sent to the Internet resource.

        Get: AllowWriteStreamBuffering(self: HttpWebRequest) -> bool

        Set: AllowWriteStreamBuffering(self: HttpWebRequest) = value
        """
        ...

    @property
    def AutomaticDecompression(self):
        """
        Gets or sets the type of decompression that is used.

        Get: AutomaticDecompression(self: HttpWebRequest) -> DecompressionMethods

        Set: AutomaticDecompression(self: HttpWebRequest) = value
        """
        ...

    @property
    def ClientCertificates(self):
        """
        Gets or sets the collection of security certificates that are associated with this request.

        Get: ClientCertificates(self: HttpWebRequest) -> X509CertificateCollection

        Set: ClientCertificates(self: HttpWebRequest) = value
        """
        ...

    @property
    def Connection(self):
        """
        Gets or sets the value of the nnection HTTP header.

        Get: Connection(self: HttpWebRequest) -> str

        Set: Connection(self: HttpWebRequest) = value
        """
        ...

    @property
    def ConnectionGroupName(self):
        """
        Gets or sets the name of the connection group for the request.

        Get: ConnectionGroupName(self: HttpWebRequest) -> str

        Set: ConnectionGroupName(self: HttpWebRequest) = value
        """
        ...

    @property
    def ContentLength(self):
        """
        Gets or sets the ntent-length HTTP header.

        Get: ContentLength(self: HttpWebRequest) -> Int64

        Set: ContentLength(self: HttpWebRequest) = value
        """
        ...

    @property
    def ContentType(self):
        """
        Gets or sets the value of the ntent-type HTTP header.

        Get: ContentType(self: HttpWebRequest) -> str

        Set: ContentType(self: HttpWebRequest) = value
        """
        ...

    @property
    def ContinueDelegate(self):
        """
        Gets or sets the delegate method called when an HTTP 100-continue response is received from the Internet resource.

        Get: ContinueDelegate(self: HttpWebRequest) -> HttpContinueDelegate

        Set: ContinueDelegate(self: HttpWebRequest) = value
        """
        ...

    @property
    def ContinueTimeout(self):
        """
        Gets or sets a timeout, in milliseconds, to wait until the 100-Continue is received from the server.

        Get: ContinueTimeout(self: HttpWebRequest) -> int

        Set: ContinueTimeout(self: HttpWebRequest) = value
        """
        ...

    @property
    def CookieContainer(self):
        """
        Gets or sets the cookies associated with the request.

        Get: CookieContainer(self: HttpWebRequest) -> CookieContainer

        Set: CookieContainer(self: HttpWebRequest) = value
        """
        ...

    @property
    def Credentials(self):
        """
        Gets or sets authentication information for the request.

        Get: Credentials(self: HttpWebRequest) -> ICredentials

        Set: Credentials(self: HttpWebRequest) = value
        """
        ...

    @property
    def Date(self):
        """
        Get or set the te HTTP header value to use in an HTTP request.

        Get: Date(self: HttpWebRequest) -> DateTime

        Set: Date(self: HttpWebRequest) = value
        """
        ...

    @property
    def Expect(self):
        """
        Gets or sets the value of the pect HTTP header.

        Get: Expect(self: HttpWebRequest) -> str

        Set: Expect(self: HttpWebRequest) = value
        """
        ...

    @property
    def HaveResponse(self):
        """
        Gets a value that indicates whether a response has been received from an Internet resource.

        Get: HaveResponse(self: HttpWebRequest) -> bool
        """
        ...

    @property
    def Headers(self):
        """
        Specifies a collection of the name/value pairs that make up the HTTP headers.

        Get: Headers(self: HttpWebRequest) -> WebHeaderCollection

        Set: Headers(self: HttpWebRequest) = value
        """
        ...

    @property
    def Host(self):
        """
        Get or set the Host header value to use in an HTTP request independent from the request URI.

        Get: Host(self: HttpWebRequest) -> str

        Set: Host(self: HttpWebRequest) = value
        """
        ...

    @property
    def IfModifiedSince(self):
        """
        Gets or sets the value of the -Modified-Since HTTP header.

        Get: IfModifiedSince(self: HttpWebRequest) -> DateTime

        Set: IfModifiedSince(self: HttpWebRequest) = value
        """
        ...

    @property
    def KeepAlive(self):
        """
        Gets or sets a value that indicates whether to make a persistent connection to the Internet resource.

        Get: KeepAlive(self: HttpWebRequest) -> bool

        Set: KeepAlive(self: HttpWebRequest) = value
        """
        ...

    @property
    def MaximumAutomaticRedirections(self):
        """
        Gets or sets the maximum number of redirects that the request follows.

        Get: MaximumAutomaticRedirections(self: HttpWebRequest) -> int

        Set: MaximumAutomaticRedirections(self: HttpWebRequest) = value
        """
        ...

    @property
    def MaximumResponseHeadersLength(self):
        """
        Gets or sets the maximum allowed length of the response headers.

        Get: MaximumResponseHeadersLength(self: HttpWebRequest) -> int

        Set: MaximumResponseHeadersLength(self: HttpWebRequest) = value
        """
        ...

    @property
    def MediaType(self):
        """
        Gets or sets the media type of the request.

        Get: MediaType(self: HttpWebRequest) -> str

        Set: MediaType(self: HttpWebRequest) = value
        """
        ...

    @property
    def Method(self):
        """
        Gets or sets the method for the request.

        Get: Method(self: HttpWebRequest) -> str

        Set: Method(self: HttpWebRequest) = value
        """
        ...

    @property
    def Pipelined(self):
        """
        Gets or sets a value that indicates whether to pipeline the request to the Internet resource.

        Get: Pipelined(self: HttpWebRequest) -> bool

        Set: Pipelined(self: HttpWebRequest) = value
        """
        ...

    @property
    def PreAuthenticate(self):
        """
        Gets or sets a value that indicates whether to send an Authorization header with the request.

        Get: PreAuthenticate(self: HttpWebRequest) -> bool

        Set: PreAuthenticate(self: HttpWebRequest) = value
        """
        ...

    @property
    def ProtocolVersion(self):
        """
        Gets or sets the version of HTTP to use for the request.

        Get: ProtocolVersion(self: HttpWebRequest) -> Version

        Set: ProtocolVersion(self: HttpWebRequest) = value
        """
        ...

    @property
    def Proxy(self):
        """
        Gets or sets proxy information for the request.

        Get: Proxy(self: HttpWebRequest) -> IWebProxy

        Set: Proxy(self: HttpWebRequest) = value
        """
        ...

    @property
    def ReadWriteTimeout(self):
        """
        Gets or sets a time-out in milliseconds when writing to or reading from a stream.

        Get: ReadWriteTimeout(self: HttpWebRequest) -> int

        Set: ReadWriteTimeout(self: HttpWebRequest) = value
        """
        ...

    @property
    def Referer(self):
        """
        Gets or sets the value of the ferer HTTP header.

        Get: Referer(self: HttpWebRequest) -> str

        Set: Referer(self: HttpWebRequest) = value
        """
        ...

    @property
    def RequestUri(self):
        """
        Gets the original Uniform Resource Identifier (URI) of the request.

        Get: RequestUri(self: HttpWebRequest) -> Uri
        """
        ...

    @property
    def SendChunked(self):
        """
        Gets or sets a value that indicates whether to send data in segments to the Internet resource.

        Get: SendChunked(self: HttpWebRequest) -> bool

        Set: SendChunked(self: HttpWebRequest) = value
        """
        ...

    @property
    def ServerCertificateValidationCallback(self):
        """
        Gets or sets a callback function to validate the server certificate.

        Get: ServerCertificateValidationCallback(self: HttpWebRequest) -> RemoteCertificateValidationCallback

        Set: ServerCertificateValidationCallback(self: HttpWebRequest) = value
        """
        ...

    @property
    def ServicePoint(self):
        """
        Gets the service point to use for the request.

        Get: ServicePoint(self: HttpWebRequest) -> ServicePoint
        """
        ...

    @property
    def SupportsCookieContainer(self):
        """
        Gets a value that indicates whether the request provides support for a System.Net.CookieContainer.

        Get: SupportsCookieContainer(self: HttpWebRequest) -> bool
        """
        ...

    @property
    def Timeout(self):
        """
        Gets or sets the time-out value in milliseconds for the System.Net.HttpWebRequest.GetResponse and System.Net.HttpWebRequest.GetRequestStream methods.

        Get: Timeout(self: HttpWebRequest) -> int

        Set: Timeout(self: HttpWebRequest) = value
        """
        ...

    @property
    def TransferEncoding(self):
        """
        Gets or sets the value of the ansfer-encoding HTTP header.

        Get: TransferEncoding(self: HttpWebRequest) -> str

        Set: TransferEncoding(self: HttpWebRequest) = value
        """
        ...

    @property
    def UnsafeAuthenticatedConnectionSharing(self):
        """
        Gets or sets a value that indicates whether to allow high-speed NTLM-authenticated connection sharing.

        Get: UnsafeAuthenticatedConnectionSharing(self: HttpWebRequest) -> bool

        Set: UnsafeAuthenticatedConnectionSharing(self: HttpWebRequest) = value
        """
        ...

    @property
    def UseDefaultCredentials(self):
        """
        Gets or sets a System.Boolean value that controls whether default credentials are sent with requests.

        Get: UseDefaultCredentials(self: HttpWebRequest) -> bool

        Set: UseDefaultCredentials(self: HttpWebRequest) = value
        """
        ...

    @property
    def UserAgent(self):
        """
        Gets or sets the value of the er-agent HTTP header.

        Get: UserAgent(self: HttpWebRequest) -> str

        Set: UserAgent(self: HttpWebRequest) = value
        """
        ...


    DefaultCachePolicy = None
    DefaultMaximumErrorResponseLength = 64
    DefaultMaximumResponseHeadersLength = 64


class HttpWebResponse(WebResponse): # skipped bases: <type 'IDisposable'>, <type 'ISerializable'>
    """
    Provides an HTTP-specific implementation of the System.Net.WebResponse class.

    HttpWebResponse()
    """
    def GetResponseHeader(self, headerName):
        """
        GetResponseHeader(self: HttpWebResponse, headerName: str) -> str

            Gets the contents of a header that was returned with the response.

            headerName: The header value to return.

            Returns: The contents of the specified header.
        """
        ...

    @property
    def CharacterSet(self):
        """
        Gets the character set of the response.

        Get: CharacterSet(self: HttpWebResponse) -> str
        """
        ...

    @property
    def ContentEncoding(self):
        """
        Gets the method that is used to encode the body of the response.

        Get: ContentEncoding(self: HttpWebResponse) -> str
        """
        ...

    @property
    def ContentLength(self):
        """
        Gets the length of the content returned by the request.

        Get: ContentLength(self: HttpWebResponse) -> Int64
        """
        ...

    @property
    def ContentType(self):
        """
        Gets the content type of the response.

        Get: ContentType(self: HttpWebResponse) -> str
        """
        ...

    @property
    def Cookies(self):
        """
        Gets or sets the cookies that are associated with this response.

        Get: Cookies(self: HttpWebResponse) -> CookieCollection

        Set: Cookies(self: HttpWebResponse) = value
        """
        ...

    @property
    def Headers(self):
        """
        Gets the headers that are associated with this response from the server.

        Get: Headers(self: HttpWebResponse) -> WebHeaderCollection
        """
        ...

    @property
    def IsMutuallyAuthenticated(self):
        """
        Gets a System.Boolean value that indicates whether both client and server were authenticated.

        Get: IsMutuallyAuthenticated(self: HttpWebResponse) -> bool
        """
        ...

    @property
    def LastModified(self):
        """
        Gets the last date and time that the contents of the response were modified.

        Get: LastModified(self: HttpWebResponse) -> DateTime
        """
        ...

    @property
    def Method(self):
        """
        Gets the method that is used to return the response.

        Get: Method(self: HttpWebResponse) -> str
        """
        ...

    @property
    def ProtocolVersion(self):
        """
        Gets the version of the HTTP protocol that is used in the response.

        Get: ProtocolVersion(self: HttpWebResponse) -> Version
        """
        ...

    @property
    def ResponseUri(self):
        """
        Gets the URI of the Internet resource that responded to the request.

        Get: ResponseUri(self: HttpWebResponse) -> Uri
        """
        ...

    @property
    def Server(self):
        """
        Gets the name of the server that sent the response.

        Get: Server(self: HttpWebResponse) -> str
        """
        ...

    @property
    def StatusCode(self):
        """
        Gets the status of the response.

        Get: StatusCode(self: HttpWebResponse) -> HttpStatusCode
        """
        ...

    @property
    def StatusDescription(self):
        """
        Gets the status description returned with the response.

        Get: StatusDescription(self: HttpWebResponse) -> str
        """
        ...

    @property
    def SupportsHeaders(self):
        """
        Gets a value that indicates if headers are supported.

        Get: SupportsHeaders(self: HttpWebResponse) -> bool
        """
        ...



class IAuthenticationModule:
    """ Provides the base authentication interface for Web client authentication modules. """
    def Authenticate(self, challenge, request, credentials):
        """
        Authenticate(self: IAuthenticationModule, challenge: str, request: WebRequest, credentials: ICredentials) -> Authorization

            Returns an instance of the System.Net.Authorization class in respose to an authentication challenge from a server.

            challenge: The authentication challenge sent by the server.

            request: The System.Net.WebRequest instance associated with the challenge.

            credentials: The credentials associated with the challenge.

            Returns: An System.Net.Authorization instance containing the authorization message for the request, or ll if the challenge cannot be handled.
        """
        ...

    def PreAuthenticate(self, request, credentials):
        """
        PreAuthenticate(self: IAuthenticationModule, request: WebRequest, credentials: ICredentials) -> Authorization

            Returns an instance of the System.Net.Authorization class for an authentication request to a server.

            request: The System.Net.WebRequest instance associated with the authentication request.

            credentials: The credentials associated with the authentication request.

            Returns: An System.Net.Authorization instance containing the authorization message for the request.
        """
        ...

    @property
    def AuthenticationType(self):
        """
        Gets the authentication type provided by this authentication module.

        Get: AuthenticationType(self: IAuthenticationModule) -> str
        """
        ...

    @property
    def CanPreAuthenticate(self):
        """
        Gets a value indicating whether the authentication module supports preauthentication.

        Get: CanPreAuthenticate(self: IAuthenticationModule) -> bool
        """
        ...



class ICertificatePolicy:
    """ Validates a server certificate. """
    def CheckValidationResult(self, srvPoint, certificate, request, certificateProblem):
        """
        CheckValidationResult(self: ICertificatePolicy, srvPoint: ServicePoint, certificate: X509Certificate, request: WebRequest, certificateProblem: int) -> bool

            Validates a server certificate.

            srvPoint: The System.Net.ServicePoint that will use the certificate.

            certificate: The certificate to validate.

            request: The request that received the certificate.

            certificateProblem: The problem that was encountered when using the certificate.

            Returns: ue if the certificate should be honored; otherwise, lse.
        """
        ...


class ICredentialPolicy:
    """ Defines the credential policy to be used for resource requests that are made using System.Net.WebRequest and its derived classes. """
    def ShouldSendCredential(self, challengeUri, request, credential, authenticationModule):
        """
        ShouldSendCredential(self: ICredentialPolicy, challengeUri: Uri, request: WebRequest, credential: NetworkCredential, authenticationModule: IAuthenticationModule) -> bool

            Returns a System.Boolean that indicates whether the client's credentials are sent with a resource request made using an instance of the System.Net.WebRequest class.

            challengeUri: The System.Uri that will receive the request. For more information, see the Remarks section.

            request: The System.Net.WebRequest that represents the resource being requested.

            credential: The System.Net.NetworkCredential that will be sent with the request if this method returns ue.

            authenticationModule: The System.Net.IAuthenticationModule that will conduct the authentication, if authentication is required.

            Returns: ue if the credentials are sent with the request; otherwise, lse.
        """
        ...


class ICredentials:
    """ Provides the base authentication interface for retrieving credentials for Web client authentication. """
    def GetCredential(self, uri, authType):
        """
        GetCredential(self: ICredentials, uri: Uri, authType: str) -> NetworkCredential

            Returns a System.Net.NetworkCredential object that is associated with the specified URI, and authentication type.

            uri: The System.Uri that the client is providing authentication for.

            authType: The type of authentication, as defined in the System.Net.IAuthenticationModule.AuthenticationType property.

            Returns: The System.Net.NetworkCredential that is associated with the specified URI and authentication type, or, if no credentials are available, ll.
        """
        ...


class ICredentialsByHost:
    """ Provides the interface for retrieving credentials for a host, port, and authentication type. """
    def GetCredential(self, host, port, authenticationType):
        """
        GetCredential(self: ICredentialsByHost, host: str, port: int, authenticationType: str) -> NetworkCredential

            Returns the credential for the specified host, port, and authentication protocol.

            host: The host computer that is authenticating the client.

            port: The port on host that the client will communicate with.

            authenticationType: The authentication protocol.

            Returns: A System.Net.NetworkCredential for the specified host, port, and authentication protocol, or ll if there are no credentials available for the specified host, port, and

             authentication protocol.
        """
        ...


class IPAddress: # skipped bases: <type 'object'>
    """
    Provides an Internet Protocol (IP) address.

    IPAddress(newAddress: Int64)

    IPAddress(address: Array[Byte], scopeid: Int64)

    IPAddress(address: Array[Byte])
    """
    def Equals(self, comparand):
        """
        Equals(self: IPAddress, comparand: object) -> bool

            Compares two IP addresses.

            comparand: An System.Net.IPAddress instance to compare to the current instance.

            Returns: ue if the two addresses are equal; otherwise, lse.
        """
        ...

    def GetAddressBytes(self):
        """
        GetAddressBytes(self: IPAddress) -> Array[Byte]

            Provides a copy of the System.Net.IPAddress as an array of bytes.

            Returns: A System.Byte array.
        """
        ...

    def GetHashCode(self):
        """
        GetHashCode(self: IPAddress) -> int

            Returns a hash value for an IP address.

            Returns: An integer hash value.
        """
        ...

    @staticmethod
    def HostToNetworkOrder(host):
        """
        HostToNetworkOrder(host: Int64) -> Int64

            Converts a long value from host byte order to network byte order.

            host: The number to convert, expressed in host byte order.

            Returns: A long value, expressed in network byte order.

        HostToNetworkOrder(host: int) -> int

            Converts an integer value from host byte order to network byte order.

            host: The number to convert, expressed in host byte order.

            Returns: An integer value, expressed in network byte order.

        HostToNetworkOrder(host: Int16) -> Int16

            Converts a short value from host byte order to network byte order.

            host: The number to convert, expressed in host byte order.

            Returns: A short value, expressed in network byte order.
        """
        ...

    @staticmethod
    def IsLoopback(address):
        """
        IsLoopback(address: IPAddress) -> bool

            Indicates whether the specified IP address is the loopback address.

            address: An IP address.

            Returns: ue if address is the loopback address; otherwise, lse.
        """
        ...

    def MapToIPv4(self):
        """
        MapToIPv4(self: IPAddress) -> IPAddress

            Maps the System.Net.IPAddress object to an IPv4 address.

            Returns: Returns System.Net.IPAddress.An IPv4 address.
        """
        ...

    def MapToIPv6(self):
        """
        MapToIPv6(self: IPAddress) -> IPAddress

            Maps the System.Net.IPAddress object to an IPv6 address.

            Returns: Returns System.Net.IPAddress.An IPv6 address.
        """
        ...

    @staticmethod
    def NetworkToHostOrder(network):
        """
        NetworkToHostOrder(network: Int64) -> Int64

            Converts a long value from network byte order to host byte order.

            network: The number to convert, expressed in network byte order.

            Returns: A long value, expressed in host byte order.

        NetworkToHostOrder(network: int) -> int

            Converts an integer value from network byte order to host byte order.

            network: The number to convert, expressed in network byte order.

            Returns: An integer value, expressed in host byte order.

        NetworkToHostOrder(network: Int16) -> Int16

            Converts a short value from network byte order to host byte order.

            network: The number to convert, expressed in network byte order.

            Returns: A short value, expressed in host byte order.
        """
        ...

    @staticmethod
    def Parse(ipString):
        """
        Parse(ipString: str) -> IPAddress

            Converts an IP address string to an System.Net.IPAddress instance.

            ipString: A string that contains an IP address in dotted-quad notation for IPv4 and in colon-hexadecimal notation for IPv6.

            Returns: An System.Net.IPAddress instance.
        """
        ...

    def ToString(self):
        """
        ToString(self: IPAddress) -> str

            Converts an Internet address to its standard notation.

            Returns: A string that contains the IP address in either IPv4 dotted-quad or in IPv6 colon-hexadecimal notation.
        """
        ...

    @staticmethod
    def TryParse(ipString, address):
        """
        TryParse(ipString: str) -> (bool, IPAddress)

            Determines whether a string is a valid IP address.

            ipString: The string to validate.

            Returns: ue if ipString was able to be parsed as an IP address; otherwise, lse.
        """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    @property
    def Address(self):
        """
        An Internet Protocol (IP) address.

        Get: Address(self: IPAddress) -> Int64

        Set: Address(self: IPAddress) = value
        """
        ...

    @property
    def AddressFamily(self):
        """
        Gets the address family of the IP address.

        Get: AddressFamily(self: IPAddress) -> AddressFamily
        """
        ...

    @property
    def IsIPv4MappedToIPv6(self):
        """
        Gets whether the IP address is an IPv4-mapped IPv6 address.

        Get: IsIPv4MappedToIPv6(self: IPAddress) -> bool
        """
        ...

    @property
    def IsIPv6LinkLocal(self):
        """
        Gets whether the address is an IPv6 link local address.

        Get: IsIPv6LinkLocal(self: IPAddress) -> bool
        """
        ...

    @property
    def IsIPv6Multicast(self):
        """
        Gets whether the address is an IPv6 multicast global address.

        Get: IsIPv6Multicast(self: IPAddress) -> bool
        """
        ...

    @property
    def IsIPv6SiteLocal(self):
        """
        Gets whether the address is an IPv6 site local address.

        Get: IsIPv6SiteLocal(self: IPAddress) -> bool
        """
        ...

    @property
    def IsIPv6Teredo(self):
        """
        Gets whether the address is an IPv6 Teredo address.

        Get: IsIPv6Teredo(self: IPAddress) -> bool
        """
        ...

    @property
    def ScopeId(self):
        """
        Gets or sets the IPv6 address scope identifier.

        Get: ScopeId(self: IPAddress) -> Int64

        Set: ScopeId(self: IPAddress) = value
        """
        ...


    Any = None
    Broadcast = None
    IPv6Any = None
    IPv6Loopback = None
    IPv6None = None
    Loopback = None



class IPEndPoint(EndPoint):
    """
    Represents a network endpoint as an IP address and a port number.

    IPEndPoint(address: Int64, port: int)

    IPEndPoint(address: IPAddress, port: int)
    """
    def Equals(self, comparand):
        """
        Equals(self: IPEndPoint, comparand: object) -> bool

            Determines whether the specified System.Object is equal to the current System.Object.

            comparand: The System.Object to compare with the current System.Object.

            Returns: ue if the specified System.Object is equal to the current System.Object; otherwise, lse.
        """
        ...

    def GetHashCode(self):
        """
        GetHashCode(self: IPEndPoint) -> int

            Returns a hash value for a System.Net.IPEndPoint instance.

            Returns: An integer hash value.
        """
        ...

    def ToString(self):
        """
        ToString(self: IPEndPoint) -> str

            Returns the IP address and port number of the specified endpoint.

            Returns: A string containing the IP address and the port number of the specified endpoint (for example, 192.168.1.2:80).
        """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    @staticmethod # known case of __new__
    def __new__(cls, address, port):
        """
        __new__(cls: type, address: Int64, port: int)

        __new__(cls: type, address: IPAddress, port: int)
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    @property
    def Address(self):
        """
        Gets or sets the IP address of the endpoint.

        Get: Address(self: IPEndPoint) -> IPAddress

        Set: Address(self: IPEndPoint) = value
        """
        ...

    @property
    def AddressFamily(self):
        """
        Gets the Internet Protocol (IP) address family.

        Get: AddressFamily(self: IPEndPoint) -> AddressFamily
        """
        ...

    @property
    def Port(self):
        """
        Gets or sets the port number of the endpoint.

        Get: Port(self: IPEndPoint) -> int

        Set: Port(self: IPEndPoint) = value
        """
        ...


    MaxPort = 65535
    MinPort = 0


class IPHostEntry: # skipped bases: <type 'object'>
    """
    Provides a container class for Internet host address information.

    IPHostEntry()
    """
    @property
    def AddressList(self):
        """
        Gets or sets a list of IP addresses that are associated with a host.

        Get: AddressList(self: IPHostEntry) -> Array[IPAddress]

        Set: AddressList(self: IPHostEntry) = value
        """
        ...

    @property
    def Aliases(self):
        """
        Gets or sets a list of aliases that are associated with a host.

        Get: Aliases(self: IPHostEntry) -> Array[str]

        Set: Aliases(self: IPHostEntry) = value
        """
        ...

    @property
    def HostName(self):
        """
        Gets or sets the DNS name of the host.

        Get: HostName(self: IPHostEntry) -> str

        Set: HostName(self: IPHostEntry) = value
        """
        ...



class IWebProxy:
    """ Provides the base interface for implementation of proxy access for the System.Net.WebRequest class. """
    def GetProxy(self, destination):
        """
        GetProxy(self: IWebProxy, destination: Uri) -> Uri

            Returns the URI of a proxy.

            destination: A System.Uri that specifies the requested Internet resource.

            Returns: A System.Uri instance that contains the URI of the proxy used to contact destination.
        """
        ...

    def IsBypassed(self, host):
        """
        IsBypassed(self: IWebProxy, host: Uri) -> bool

            Indicates that the proxy should not be used for the specified host.

            host: The System.Uri of the host to check for proxy use.

            Returns: ue if the proxy server should not be used for host; otherwise, lse.
        """
        ...

    @property
    def Credentials(self):
        """
        The credentials to submit to the proxy server for authentication.

        Get: Credentials(self: IWebProxy) -> ICredentials

        Set: Credentials(self: IWebProxy) = value
        """
        ...



class IWebProxyScript:
    """ Provides the base interface to load and execute scripts for automatic proxy detection. """
    def Close(self):
        """
        Close(self: IWebProxyScript)

            Closes a script.
        """
        ...

    def Load(self, scriptLocation, script, helperType):
        """
        Load(self: IWebProxyScript, scriptLocation: Uri, script: str, helperType: Type) -> bool

            Loads a script.

            scriptLocation: Internal only.

            script: Internal only.

            helperType: Internal only.

            Returns: A System.Boolean indicating whether the script was successfully loaded.
        """
        ...

    def Run(self, url, host):
        """
        Run(self: IWebProxyScript, url: str, host: str) -> str

            Runs a script.

            url: Internal only.

            host: Internal only.

            Returns: A System.String.An internal-only value returned.
        """
        ...


class IWebRequestCreate:
    """ Provides the base interface for creating System.Net.WebRequest instances. """
    def Create(self, uri):
        """
        Create(self: IWebRequestCreate, uri: Uri) -> WebRequest

            Creates a System.Net.WebRequest instance.

            uri: The uniform resource identifier (URI) of the Web resource.

            Returns: A System.Net.WebRequest instance.
        """
        ...


class NetworkAccess(Enum): # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies network access permissions.

    enum (flags) NetworkAccess, values: Accept (128), Connect (64)
    """
    Accept = None
    Connect = None
    value__ = None


class NetworkCredential(object, ICredentials, ICredentialsByHost):
    """
    Provides credentials for password-based authentication schemes such as basic, digest, NTLM, and Kerberos authentication.

    NetworkCredential()

    NetworkCredential(userName: str, password: str)

    NetworkCredential(userName: str, password: SecureString)

    NetworkCredential(userName: str, password: str, domain: str)

    NetworkCredential(userName: str, password: SecureString, domain: str)
    """
    @property
    def Domain(self):
        """
        Gets or sets the domain or computer name that verifies the credentials.

        Get: Domain(self: NetworkCredential) -> str

        Set: Domain(self: NetworkCredential) = value
        """
        ...

    @property
    def Password(self):
        """
        Gets or sets the password for the user name associated with the credentials.

        Get: Password(self: NetworkCredential) -> str

        Set: Password(self: NetworkCredential) = value
        """
        ...

    @property
    def SecurePassword(self):
        """
        Gets or sets the password as a System.Security.SecureString instance.

        Get: SecurePassword(self: NetworkCredential) -> SecureString

        Set: SecurePassword(self: NetworkCredential) = value
        """
        ...

    @property
    def UserName(self):
        """
        Gets or sets the user name associated with the credentials.

        Get: UserName(self: NetworkCredential) -> str

        Set: UserName(self: NetworkCredential) = value
        """
        ...



class OpenReadCompletedEventArgs(AsyncCompletedEventArgs):
    """ Provides data for the System.Net.WebClient.OpenReadCompleted event. """
    @property
    def Result(self):
        """
        Gets a readable stream that contains data downloaded by a erload:System.Net.WebClient.DownloadDataAsync method.

        Get: Result(self: OpenReadCompletedEventArgs) -> Stream
        """
        ...



class OpenReadCompletedEventHandler(MulticastDelegate): # skipped bases: <type 'ICloneable'>, <type 'ISerializable'>
    """
    Represents the method that will handle the System.Net.WebClient.OpenReadCompleted event of a System.Net.WebClient.

    OpenReadCompletedEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: OpenReadCompletedEventHandler, sender: object, e: OpenReadCompletedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result):
        """ EndInvoke(self: OpenReadCompletedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender, e):
        """ Invoke(self: OpenReadCompletedEventHandler, sender: object, e: OpenReadCompletedEventArgs) """
        ...


class OpenWriteCompletedEventArgs(AsyncCompletedEventArgs):
    """ Provides data for the System.Net.WebClient.OpenWriteCompleted event. """
    @property
    def Result(self):
        """
        Gets a writable stream that is used to send data to a server.

        Get: Result(self: OpenWriteCompletedEventArgs) -> Stream
        """
        ...



class OpenWriteCompletedEventHandler(MulticastDelegate): # skipped bases: <type 'ICloneable'>, <type 'ISerializable'>
    """
    Represents the method that will handle the System.Net.WebClient.OpenWriteCompleted event of a System.Net.WebClient.

    OpenWriteCompletedEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: OpenWriteCompletedEventHandler, sender: object, e: OpenWriteCompletedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result):
        """ EndInvoke(self: OpenWriteCompletedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender, e):
        """ Invoke(self: OpenWriteCompletedEventHandler, sender: object, e: OpenWriteCompletedEventArgs) """
        ...


class ProtocolViolationException(InvalidOperationException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>
    """
    The exception that is thrown when an error is made while using a network protocol.

    ProtocolViolationException()

    ProtocolViolationException(message: str)
    """
    def GetObjectData(self, serializationInfo, streamingContext):
        """
        GetObjectData(self: ProtocolViolationException, serializationInfo: SerializationInfo, streamingContext: StreamingContext)

            Populates a System.Runtime.Serialization.SerializationInfo with the data required to serialize the target object.

            serializationInfo: The System.Runtime.Serialization.SerializationInfo to populate with data.

            streamingContext: A System.Runtime.Serialization.StreamingContext that specifies the destination for this serialization.
        """
        ...

    SerializeObjectState = None


class SecurityProtocolType(Enum): # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies the security protocols that are supported by the Schannel security package.

    enum (flags) SecurityProtocolType, values: Ssl3 (48), SystemDefault (0), Tls (192), Tls11 (768), Tls12 (3072), Tls13 (12288)
    """
    Ssl3 = None
    SystemDefault = None
    Tls = None
    Tls11 = None
    Tls12 = None
    Tls13 = None
    value__ = None


class ServicePoint: # skipped bases: <type 'object'>
    """ Provides connection management for HTTP connections. """
    def CloseConnectionGroup(self, connectionGroupName):
        """
        CloseConnectionGroup(self: ServicePoint, connectionGroupName: str) -> bool

            Removes the specified connection group from this System.Net.ServicePoint object.

            connectionGroupName: The name of the connection group that contains the connections to close and remove from this service point.

            Returns: A System.Boolean value that indicates whether the connection group was closed.
        """
        ...

    def SetTcpKeepAlive(self, enabled, keepAliveTime, keepAliveInterval):
        """
        SetTcpKeepAlive(self: ServicePoint, enabled: bool, keepAliveTime: int, keepAliveInterval: int)

            Enables or disables the keep-alive option on a TCP connection.

            enabled: If set to true, then the TCP keep-alive option on a TCP connection will be enabled using the specified keepAliveTime and keepAliveInterval values. If set to false,

             then the TCP keep-alive option is disabled and the remaining parameters are ignored.The default value is false.

            keepAliveTime: Specifies the timeout, in milliseconds, with no activity until the first keep-alive packet is sent. The value must be greater than 0.  If a value of less than or equal

             to zero is passed an System.ArgumentOutOfRangeException is thrown.

            keepAliveInterval: Specifies the interval, in milliseconds, between when successive keep-alive packets are sent if no acknowledgement is received.The value must be greater than 0.  If a

             value of less than or equal to zero is passed an System.ArgumentOutOfRangeException is thrown.
        """
        ...

    @property
    def Address(self):
        """
        Gets the Uniform Resource Identifier (URI) of the server that this System.Net.ServicePoint object connects to.

        Get: Address(self: ServicePoint) -> Uri
        """
        ...

    @property
    def BindIPEndPointDelegate(self):
        """
        Specifies the delegate to associate a local System.Net.IPEndPoint with a System.Net.ServicePoint.

        Get: BindIPEndPointDelegate(self: ServicePoint) -> BindIPEndPoint

        Set: BindIPEndPointDelegate(self: ServicePoint) = value
        """
        ...

    @property
    def Certificate(self):
        """
        Gets the certificate received for this System.Net.ServicePoint object.

        Get: Certificate(self: ServicePoint) -> X509Certificate
        """
        ...

    @property
    def ClientCertificate(self):
        """
        Gets the last client certificate sent to the server.

        Get: ClientCertificate(self: ServicePoint) -> X509Certificate
        """
        ...

    @property
    def ConnectionLeaseTimeout(self):
        """
        Gets or sets the number of milliseconds after which an active System.Net.ServicePoint connection is closed.

        Get: ConnectionLeaseTimeout(self: ServicePoint) -> int

        Set: ConnectionLeaseTimeout(self: ServicePoint) = value
        """
        ...

    @property
    def ConnectionLimit(self):
        """
        Gets or sets the maximum number of connections allowed on this System.Net.ServicePoint object.

        Get: ConnectionLimit(self: ServicePoint) -> int

        Set: ConnectionLimit(self: ServicePoint) = value
        """
        ...

    @property
    def ConnectionName(self):
        """
        Gets the connection name.

        Get: ConnectionName(self: ServicePoint) -> str
        """
        ...

    @property
    def CurrentConnections(self):
        """
        Gets the number of open connections associated with this System.Net.ServicePoint object.

        Get: CurrentConnections(self: ServicePoint) -> int
        """
        ...

    @property
    def Expect100Continue(self):
        """
        Gets or sets a System.Boolean value that determines whether 100-Continue behavior is used.

        Get: Expect100Continue(self: ServicePoint) -> bool

        Set: Expect100Continue(self: ServicePoint) = value
        """
        ...

    @property
    def IdleSince(self):
        """
        Gets the date and time that the System.Net.ServicePoint object was last connected to a host.

        Get: IdleSince(self: ServicePoint) -> DateTime
        """
        ...

    @property
    def MaxIdleTime(self):
        """
        Gets or sets the amount of time a connection associated with the System.Net.ServicePoint object can remain idle before the connection is closed.

        Get: MaxIdleTime(self: ServicePoint) -> int

        Set: MaxIdleTime(self: ServicePoint) = value
        """
        ...

    @property
    def ProtocolVersion(self):
        """
        Gets the version of the HTTP protocol that the System.Net.ServicePoint object uses.

        Get: ProtocolVersion(self: ServicePoint) -> Version
        """
        ...

    @property
    def ReceiveBufferSize(self):
        """
        Gets or sets the size of the receiving buffer for the socket used by this System.Net.ServicePoint.

        Get: ReceiveBufferSize(self: ServicePoint) -> int

        Set: ReceiveBufferSize(self: ServicePoint) = value
        """
        ...

    @property
    def SupportsPipelining(self):
        """
        Indicates whether the System.Net.ServicePoint object supports pipelined connections.

        Get: SupportsPipelining(self: ServicePoint) -> bool
        """
        ...

    @property
    def UseNagleAlgorithm(self):
        """
        Gets or sets a System.Boolean value that determines whether the Nagle algorithm is used on connections managed by this System.Net.ServicePoint object.

        Get: UseNagleAlgorithm(self: ServicePoint) -> bool

        Set: UseNagleAlgorithm(self: ServicePoint) = value
        """
        ...



class ServicePointManager: # skipped bases: <type 'object'>
    """ Manages the collection of System.Net.ServicePoint objects. """
    @staticmethod
    def FindServicePoint(*__args):
        """
        FindServicePoint(address: Uri) -> ServicePoint

            Finds an existing System.Net.ServicePoint object or creates a new System.Net.ServicePoint object to manage communications with the specified System.Uri object.

            address: The System.Uri object of the Internet resource to contact.

            Returns: The System.Net.ServicePoint object that manages communications for the request.

        FindServicePoint(uriString: str, proxy: IWebProxy) -> ServicePoint

            Finds an existing System.Net.ServicePoint object or creates a new System.Net.ServicePoint object to manage communications with the specified Uniform Resource

             Identifier (URI).

            uriString: The URI of the Internet resource to be contacted.

            proxy: The proxy data for this request.

            Returns: The System.Net.ServicePoint object that manages communications for the request.

        FindServicePoint(address: Uri, proxy: IWebProxy) -> ServicePoint

            Finds an existing System.Net.ServicePoint object or creates a new System.Net.ServicePoint object to manage communications with the specified System.Uri object.

            address: A System.Uri object that contains the address of the Internet resource to contact.

            proxy: The proxy data for this request.

            Returns: The System.Net.ServicePoint object that manages communications for the request.
        """
        ...

    @staticmethod
    def SetTcpKeepAlive(enabled, keepAliveTime, keepAliveInterval):
        """
        SetTcpKeepAlive(enabled: bool, keepAliveTime: int, keepAliveInterval: int)

            Enables or disables the keep-alive option on a TCP connection.

            enabled: If set to true, then the TCP keep-alive option on a TCP connection will be enabled using the specified keepAliveTime and keepAliveInterval values. If set to false,

             then the TCP keep-alive option is disabled and the remaining parameters are ignored.The default value is false.

            keepAliveTime: Specifies the timeout, in milliseconds, with no activity until the first keep-alive packet is sent.The value must be greater than 0.  If a value of less than or equal

             to zero is passed an System.ArgumentOutOfRangeException is thrown.

            keepAliveInterval: Specifies the interval, in milliseconds, between when successive keep-alive packets are sent if no acknowledgement is received.The value must be greater than 0.  If a

             value of less than or equal to zero is passed an System.ArgumentOutOfRangeException is thrown.
        """
        ...

    CertificatePolicy = None
    CheckCertificateRevocationList = False
    DefaultConnectionLimit = 2
    DefaultNonPersistentConnectionLimit = 4
    DefaultPersistentConnectionLimit = 2
    DnsRefreshTimeout = 120000
    EnableDnsRoundRobin = False
    EncryptionPolicy = None
    Expect100Continue = True
    MaxServicePointIdleTime = 100000
    MaxServicePoints = 0
    ReusePort = False
    SecurityProtocol = None
    ServerCertificateValidationCallback = None
    UseNagleAlgorithm = True


class SocketAddress: # skipped bases: <type 'object'>
    """
    Stores serialized information from System.Net.EndPoint derived classes.

    SocketAddress(family: AddressFamily)

    SocketAddress(family: AddressFamily, size: int)
    """
    def Equals(self, comparand):
        """
        Equals(self: SocketAddress, comparand: object) -> bool

            Determines whether the specified ject is equal to the current ject.

            comparand: The System.Object to compare with the current ject.

            Returns: ue if the specified ject is equal to the current ject; otherwise, lse.
        """
        ...

    def GetHashCode(self):
        """
        GetHashCode(self: SocketAddress) -> int

            Serves as a hash function for a particular type, suitable for use in hashing algorithms and data structures like a hash table.

            Returns: A hash code for the current System.Object.
        """
        ...

    def ToString(self):
        """
        ToString(self: SocketAddress) -> str

            Returns information about the socket address.

            Returns: A string that contains information about the System.Net.SocketAddress.
        """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...

    @property
    def Family(self):
        """
        Gets the System.Net.Sockets.AddressFamily enumerated value of the current System.Net.SocketAddress.

        Get: Family(self: SocketAddress) -> AddressFamily
        """
        ...

    @property
    def Size(self):
        """
        Gets the underlying buffer size of the System.Net.SocketAddress.

        Get: Size(self: SocketAddress) -> int
        """
        ...



class SocketPermission(CodeAccessPermission, IUnrestrictedPermission): # skipped bases: <type 'ISecurityEncodable'>, <type 'IPermission'>, <type 'IStackWalk'>
    """
    Controls rights to make or accept connections on a transport address.

    SocketPermission(state: PermissionState)

    SocketPermission(access: NetworkAccess, transport: TransportType, hostName: str, portNumber: int)
    """
    def AddPermission(self, access, transport, hostName, portNumber):
        """
        AddPermission(self: SocketPermission, access: NetworkAccess, transport: TransportType, hostName: str, portNumber: int)

            Adds a permission to the set of permissions for a transport address.

            access: One of the System.Net.NetworkAccess values.

            transport: One of the System.Net.TransportType values.

            hostName: The host name for the transport address.

            portNumber: The port number for the transport address.
        """
        ...

    @staticmethod # known case of __new__
    def __new__(cls, *__args):
        """
        __new__(cls: type, state: PermissionState)

        __new__(cls: type, access: NetworkAccess, transport: TransportType, hostName: str, portNumber: int)
        """
        ...

    @property
    def AcceptList(self):
        """
        Gets a list of System.Net.EndpointPermission instances that identifies the endpoints that can be accepted under this permission instance.

        Get: AcceptList(self: SocketPermission) -> IEnumerator
        """
        ...

    @property
    def ConnectList(self):
        """
        Gets a list of System.Net.EndpointPermission instances that identifies the endpoints that can be connected to under this permission instance.

        Get: ConnectList(self: SocketPermission) -> IEnumerator
        """
        ...


    AllPorts = -1


class SocketPermissionAttribute(CodeAccessSecurityAttribute): # skipped bases: <type '_Attribute'>
    """
    Specifies security actions to control System.Net.Sockets.Socket connections. This class cannot be inherited.

    SocketPermissionAttribute(action: SecurityAction)
    """
    def CreatePermission(self):
        """
        CreatePermission(self: SocketPermissionAttribute) -> IPermission

            Creates and returns a new instance of the System.Net.SocketPermission class.

            Returns: An instance of the System.Net.SocketPermission class that corresponds to the security declaration.
        """
        ...

    @property
    def Access(self):
        """
        Gets or sets the network access method that is allowed by this System.Net.SocketPermissionAttribute.

        Get: Access(self: SocketPermissionAttribute) -> str

        Set: Access(self: SocketPermissionAttribute) = value
        """
        ...

    @property
    def Host(self):
        """
        Gets or sets the DNS host name or IP address that is specified by this System.Net.SocketPermissionAttribute.

        Get: Host(self: SocketPermissionAttribute) -> str

        Set: Host(self: SocketPermissionAttribute) = value
        """
        ...

    @property
    def Port(self):
        """
        Gets or sets the port number that is associated with this System.Net.SocketPermissionAttribute.

        Get: Port(self: SocketPermissionAttribute) -> str

        Set: Port(self: SocketPermissionAttribute) = value
        """
        ...

    @property
    def Transport(self):
        """
        Gets or sets the System.Net.TransportType that is specified by this System.Net.SocketPermissionAttribute.

        Get: Transport(self: SocketPermissionAttribute) -> str

        Set: Transport(self: SocketPermissionAttribute) = value
        """
        ...



class TransportContext: # skipped bases: <type 'object'>
    """ The System.Net.TransportContext class provides additional context about the underlying transport layer. """
    def GetChannelBinding(self, kind):
        """
        GetChannelBinding(self: TransportContext, kind: ChannelBindingKind) -> ChannelBinding

            Retrieves the requested channel binding.

            kind: The type of channel binding to retrieve.

            Returns: The requested System.Security.Authentication.ExtendedProtection.ChannelBinding, or ll if the channel binding is not supported by the current transport or by the

             operating system.
        """
        ...

    def GetTlsTokenBindings(self):
        """
        GetTlsTokenBindings(self: TransportContext) -> IEnumerable[TokenBinding]

            Gets the transport security layer token bindings.

            Returns: The transport security layer token bindings.
        """
        ...


class TransportType(Enum): # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Defines transport types for the System.Net.SocketPermission and System.Net.Sockets.Socket classes.

    enum TransportType, values: All (3), Connectionless (1), ConnectionOriented (2), Tcp (2), Udp (1)
    """
    All = None
    Connectionless = None
    ConnectionOriented = None
    Tcp = None
    Udp = None
    value__ = None


class UploadDataCompletedEventArgs(AsyncCompletedEventArgs):
    """ Provides data for the System.Net.WebClient.UploadDataCompleted event. """
    @property
    def Result(self):
        """
        Gets the server reply to a data upload operation started by calling an erload:System.Net.WebClient.UploadDataAsync method.

        Get: Result(self: UploadDataCompletedEventArgs) -> Array[Byte]
        """
        ...



class UploadDataCompletedEventHandler(MulticastDelegate): # skipped bases: <type 'ICloneable'>, <type 'ISerializable'>
    """
    Represents the method that will handle the System.Net.WebClient.UploadDataCompleted event of a System.Net.WebClient.

    UploadDataCompletedEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: UploadDataCompletedEventHandler, sender: object, e: UploadDataCompletedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result):
        """ EndInvoke(self: UploadDataCompletedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender, e):
        """ Invoke(self: UploadDataCompletedEventHandler, sender: object, e: UploadDataCompletedEventArgs) """
        ...


class UploadFileCompletedEventArgs(AsyncCompletedEventArgs):
    """ Provides data for the System.Net.WebClient.UploadFileCompleted event. """
    @property
    def Result(self):
        """
        Gets the server reply to a data upload operation that is started by calling an erload:System.Net.WebClient.UploadFileAsync method.

        Get: Result(self: UploadFileCompletedEventArgs) -> Array[Byte]
        """
        ...



class UploadFileCompletedEventHandler(MulticastDelegate): # skipped bases: <type 'ICloneable'>, <type 'ISerializable'>
    """
    Represents the method that will handle the System.Net.WebClient.UploadFileCompleted event of a System.Net.WebClient.

    UploadFileCompletedEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: UploadFileCompletedEventHandler, sender: object, e: UploadFileCompletedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result):
        """ EndInvoke(self: UploadFileCompletedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender, e):
        """ Invoke(self: UploadFileCompletedEventHandler, sender: object, e: UploadFileCompletedEventArgs) """
        ...


class UploadProgressChangedEventArgs(ProgressChangedEventArgs):
    """ Provides data for the System.Net.WebClient.UploadProgressChanged event of a System.Net.WebClient. """
    @property
    def BytesReceived(self):
        """
        Gets the number of bytes received.

        Get: BytesReceived(self: UploadProgressChangedEventArgs) -> Int64
        """
        ...

    @property
    def BytesSent(self):
        """
        Gets the number of bytes sent.

        Get: BytesSent(self: UploadProgressChangedEventArgs) -> Int64
        """
        ...

    @property
    def TotalBytesToReceive(self):
        """
        Gets the total number of bytes in a System.Net.WebClient data upload operation.

        Get: TotalBytesToReceive(self: UploadProgressChangedEventArgs) -> Int64
        """
        ...

    @property
    def TotalBytesToSend(self):
        """
        Gets the total number of bytes to send.

        Get: TotalBytesToSend(self: UploadProgressChangedEventArgs) -> Int64
        """
        ...



class UploadProgressChangedEventHandler(MulticastDelegate): # skipped bases: <type 'ICloneable'>, <type 'ISerializable'>
    """
    Represents the method that will handle the System.Net.WebClient.UploadProgressChanged event of a System.Net.WebClient.

    UploadProgressChangedEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: UploadProgressChangedEventHandler, sender: object, e: UploadProgressChangedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result):
        """ EndInvoke(self: UploadProgressChangedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender, e):
        """ Invoke(self: UploadProgressChangedEventHandler, sender: object, e: UploadProgressChangedEventArgs) """
        ...


class UploadStringCompletedEventArgs(AsyncCompletedEventArgs):
    """ Provides data for the System.Net.WebClient.UploadStringCompleted event. """
    @property
    def Result(self):
        """
        Gets the server reply to a string upload operation that is started by calling an erload:System.Net.WebClient.UploadStringAsync method.

        Get: Result(self: UploadStringCompletedEventArgs) -> str
        """
        ...



class UploadStringCompletedEventHandler(MulticastDelegate): # skipped bases: <type 'ICloneable'>, <type 'ISerializable'>
    """
    Represents the method that will handle the System.Net.WebClient.UploadStringCompleted event of a System.Net.WebClient.

    UploadStringCompletedEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: UploadStringCompletedEventHandler, sender: object, e: UploadStringCompletedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result):
        """ EndInvoke(self: UploadStringCompletedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender, e):
        """ Invoke(self: UploadStringCompletedEventHandler, sender: object, e: UploadStringCompletedEventArgs) """
        ...


class UploadValuesCompletedEventArgs(AsyncCompletedEventArgs):
    """ Provides data for the System.Net.WebClient.UploadValuesCompleted event. """
    @property
    def Result(self):
        """
        Gets the server reply to a data upload operation started by calling an erload:System.Net.WebClient.UploadValuesAsync method.

        Get: Result(self: UploadValuesCompletedEventArgs) -> Array[Byte]
        """
        ...



class UploadValuesCompletedEventHandler(MulticastDelegate): # skipped bases: <type 'ICloneable'>, <type 'ISerializable'>
    """
    Represents the method that will handle the System.Net.WebClient.UploadValuesCompleted event of a System.Net.WebClient.

    UploadValuesCompletedEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: UploadValuesCompletedEventHandler, sender: object, e: UploadValuesCompletedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result):
        """ EndInvoke(self: UploadValuesCompletedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender, e):
        """ Invoke(self: UploadValuesCompletedEventHandler, sender: object, e: UploadValuesCompletedEventArgs) """
        ...


class WebClient(Component): # skipped bases: <type 'IComponent'>, <type 'IDisposable'>
    """
    Provides common methods for sending data to and receiving data from a resource identified by a URI.

    WebClient()
    """
    def CancelAsync(self):
        """
        CancelAsync(self: WebClient)

            Cancels a pending asynchronous operation.
        """
        ...

    def DownloadData(self, address):
        """
        DownloadData(self: WebClient, address: str) -> Array[Byte]

            Downloads the resource as a System.Byte array from the URI specified.

            address: The URI from which to download data.

            Returns: A System.Byte array containing the downloaded resource.

        DownloadData(self: WebClient, address: Uri) -> Array[Byte]

            Downloads the resource as a System.Byte array from the URI specified.

            address: The URI represented by the System.Uri  object, from which to download data.

            Returns: A System.Byte array containing the downloaded resource.
        """
        ...

    def DownloadDataAsync(self, address, userToken=None):
        """
        DownloadDataAsync(self: WebClient, address: Uri)

            Downloads the resource as a System.Byte array from the URI specified as an asynchronous operation.

            address: A System.Uri containing the URI to download.

        DownloadDataAsync(self: WebClient, address: Uri, userToken: object)

            Downloads the resource as a System.Byte array from the URI specified as an asynchronous operation.

            address: A System.Uri containing the URI to download.

            userToken: A user-defined object that is passed to the method invoked when the asynchronous operation completes.
        """
        ...

    def DownloadDataTaskAsync(self, address):
        """
        DownloadDataTaskAsync(self: WebClient, address: str) -> Task[Array[Byte]]

            Downloads the resource as a System.Byte array from the URI specified as an asynchronous operation using a task object.

            address: The URI of the resource to download.

            Returns: Returns System.Threading.Tasks.Task.The task object representing the asynchronous operation. The System.Threading.Tasks.Task property on the task object returns a

             System.Byte array containing the downloaded resource.

        DownloadDataTaskAsync(self: WebClient, address: Uri) -> Task[Array[Byte]]

            Downloads the resource as a System.Byte array from the URI specified as an asynchronous operation using a task object.

            address: The URI of the resource to download.

            Returns: Returns System.Threading.Tasks.Task.The task object representing the asynchronous operation. The System.Threading.Tasks.Task property on the task object returns a

             System.Byte array containing the downloaded resource.
        """
        ...

    def DownloadFile(self, address, fileName):
        """
        DownloadFile(self: WebClient, address: str, fileName: str)

            Downloads the resource with the specified URI to a local file.

            address: The URI from which to download data.

            fileName: The name of the local file that is to receive the data.

        DownloadFile(self: WebClient, address: Uri, fileName: str)

            Downloads the resource with the specified URI to a local file.

            address: The URI specified as a System.String, from which to download data.

            fileName: The name of the local file that is to receive the data.
        """
        ...

    def DownloadFileAsync(self, address, fileName, userToken=None):
        """
        DownloadFileAsync(self: WebClient, address: Uri, fileName: str)

            Downloads, to a local file, the resource with the specified URI. This method does not block the calling thread.

            address: The URI of the resource to download.

            fileName: The name of the file to be placed on the local computer.

        DownloadFileAsync(self: WebClient, address: Uri, fileName: str, userToken: object)

            Downloads, to a local file, the resource with the specified URI. This method does not block the calling thread.

            address: The URI of the resource to download.

            fileName: The name of the file to be placed on the local computer.

            userToken: A user-defined object that is passed to the method invoked when the asynchronous operation completes.
        """
        ...

    def DownloadFileTaskAsync(self, address, fileName):
        """
        DownloadFileTaskAsync(self: WebClient, address: str, fileName: str) -> Task

            Downloads the specified resource to a local file as an asynchronous operation using a task object.

            address: The URI of the resource to download.

            fileName: The name of the file to be placed on the local computer.

            Returns: Returns System.Threading.Tasks.Task.The task object representing the asynchronous operation.

        DownloadFileTaskAsync(self: WebClient, address: Uri, fileName: str) -> Task

            Downloads the specified resource to a local file as an asynchronous operation using a task object.

            address: The URI of the resource to download.

            fileName: The name of the file to be placed on the local computer.

            Returns: Returns System.Threading.Tasks.Task.The task object representing the asynchronous operation.
        """
        ...

    def DownloadString(self, address):
        """
        DownloadString(self: WebClient, address: str) -> str

            Downloads the requested resource as a System.String. The resource to download is specified as a System.String containing the URI.

            address: A System.String containing the URI to download.

            Returns: A System.String containing the requested resource.

        DownloadString(self: WebClient, address: Uri) -> str

            Downloads the requested resource as a System.String. The resource to download is specified as a System.Uri.

            address: A System.Uri object containing the URI to download.

            Returns: A System.String containing the requested resource.
        """
        ...

    def DownloadStringAsync(self, address, userToken=None):
        """
        DownloadStringAsync(self: WebClient, address: Uri)

            Downloads the resource specified as a System.Uri. This method does not block the calling thread.

            address: A System.Uri containing the URI to download.

        DownloadStringAsync(self: WebClient, address: Uri, userToken: object)

            Downloads the specified string to the specified resource. This method does not block the calling thread.

            address: A System.Uri containing the URI to download.

            userToken: A user-defined object that is passed to the method invoked when the asynchronous operation completes.
        """
        ...

    def DownloadStringTaskAsync(self, address):
        """
        DownloadStringTaskAsync(self: WebClient, address: str) -> Task[str]

            Downloads the resource as a System.String from the URI specified as an asynchronous operation using a task object.

            address: The URI of the resource to download.

            Returns: Returns System.Threading.Tasks.Task.The task object representing the asynchronous operation. The System.Threading.Tasks.Task property on the task object returns a

             System.Byte array containing the downloaded resource.

        DownloadStringTaskAsync(self: WebClient, address: Uri) -> Task[str]

            Downloads the resource as a System.String from the URI specified as an asynchronous operation using a task object.

            address: The URI of the resource to download.

            Returns: Returns System.Threading.Tasks.Task.The task object representing the asynchronous operation. The System.Threading.Tasks.Task property on the task object returns a

             System.Byte array containing the downloaded resource.
        """
        ...

    def GetWebRequest(self, *args): #cannot find CLR method
        """
        GetWebRequest(self: WebClient, address: Uri) -> WebRequest

            Returns a System.Net.WebRequest object for the specified resource.

            address: A System.Uri that identifies the resource to request.

            Returns: A new System.Net.WebRequest object for the specified resource.
        """
        ...

    def GetWebResponse(self, *args): #cannot find CLR method
        """
        GetWebResponse(self: WebClient, request: WebRequest) -> WebResponse

            Returns the System.Net.WebResponse for the specified System.Net.WebRequest.

            request: A System.Net.WebRequest that is used to obtain the response.

            Returns: A System.Net.WebResponse containing the response for the specified System.Net.WebRequest.

        GetWebResponse(self: WebClient, request: WebRequest, result: IAsyncResult) -> WebResponse

            Returns the System.Net.WebResponse for the specified System.Net.WebRequest using the specified System.IAsyncResult.

            request: A System.Net.WebRequest that is used to obtain the response.

            result: An System.IAsyncResult object obtained from a previous call to System.Net.WebRequest.BeginGetResponse(System.AsyncCallback,System.Object) .

            Returns: A System.Net.WebResponse containing the response for the specified System.Net.WebRequest.
        """
        ...

    def OnDownloadDataCompleted(self, *args): #cannot find CLR method
        """
        OnDownloadDataCompleted(self: WebClient, e: DownloadDataCompletedEventArgs)

            Raises the System.Net.WebClient.DownloadDataCompleted event.

            e: A System.Net.DownloadDataCompletedEventArgs object that contains event data.
        """
        ...

    def OnDownloadFileCompleted(self, *args): #cannot find CLR method
        """
        OnDownloadFileCompleted(self: WebClient, e: AsyncCompletedEventArgs)

            Raises the System.Net.WebClient.DownloadFileCompleted event.

            e: An System.ComponentModel.AsyncCompletedEventArgs object containing event data.
        """
        ...

    def OnDownloadProgressChanged(self, *args): #cannot find CLR method
        """
        OnDownloadProgressChanged(self: WebClient, e: DownloadProgressChangedEventArgs)

            Raises the System.Net.WebClient.DownloadProgressChanged event.

            e: A System.Net.DownloadProgressChangedEventArgs object containing event data.
        """
        ...

    def OnDownloadStringCompleted(self, *args): #cannot find CLR method
        """
        OnDownloadStringCompleted(self: WebClient, e: DownloadStringCompletedEventArgs)

            Raises the System.Net.WebClient.DownloadStringCompleted event.

            e: A System.Net.DownloadStringCompletedEventArgs object containing event data.
        """
        ...

    def OnOpenReadCompleted(self, *args): #cannot find CLR method
        """
        OnOpenReadCompleted(self: WebClient, e: OpenReadCompletedEventArgs)

            Raises the System.Net.WebClient.OpenReadCompleted event.

            e: A System.Net.OpenReadCompletedEventArgs  object containing event data.
        """
        ...

    def OnOpenWriteCompleted(self, *args): #cannot find CLR method
        """
        OnOpenWriteCompleted(self: WebClient, e: OpenWriteCompletedEventArgs)

            Raises the System.Net.WebClient.OpenWriteCompleted event.

            e: A System.Net.OpenWriteCompletedEventArgs object containing event data.
        """
        ...

    def OnUploadDataCompleted(self, *args): #cannot find CLR method
        """
        OnUploadDataCompleted(self: WebClient, e: UploadDataCompletedEventArgs)

            Raises the System.Net.WebClient.UploadDataCompleted event.

            e: A System.Net.UploadDataCompletedEventArgs  object containing event data.
        """
        ...

    def OnUploadFileCompleted(self, *args): #cannot find CLR method
        """
        OnUploadFileCompleted(self: WebClient, e: UploadFileCompletedEventArgs)

            Raises the System.Net.WebClient.UploadFileCompleted event.

            e: An System.Net.UploadFileCompletedEventArgs object containing event data.
        """
        ...

    def OnUploadProgressChanged(self, *args): #cannot find CLR method
        """
        OnUploadProgressChanged(self: WebClient, e: UploadProgressChangedEventArgs)

            Raises the System.Net.WebClient.UploadProgressChanged event.

            e: An System.Net.UploadProgressChangedEventArgs object containing event data.
        """
        ...

    def OnUploadStringCompleted(self, *args): #cannot find CLR method
        """
        OnUploadStringCompleted(self: WebClient, e: UploadStringCompletedEventArgs)

            Raises the System.Net.WebClient.UploadStringCompleted event.

            e: An System.Net.UploadStringCompletedEventArgs  object containing event data.
        """
        ...

    def OnUploadValuesCompleted(self, *args): #cannot find CLR method
        """
        OnUploadValuesCompleted(self: WebClient, e: UploadValuesCompletedEventArgs)

            Raises the System.Net.WebClient.UploadValuesCompleted event.

            e: A System.Net.UploadValuesCompletedEventArgs  object containing event data.
        """
        ...

    def OnWriteStreamClosed(self, *args): #cannot find CLR method
        """
        OnWriteStreamClosed(self: WebClient, e: WriteStreamClosedEventArgs)

            Raises the System.Net.WebClient.WriteStreamClosed event.

            e: A System.Net.WriteStreamClosedEventArgs  object containing event data.
        """
        ...

    def OpenRead(self, address):
        """
        OpenRead(self: WebClient, address: str) -> Stream

            Opens a readable stream for the data downloaded from a resource with the URI specified as a System.String.

            address: The URI specified as a System.String from which to download data.

            Returns: A System.IO.Stream used to read data from a resource.

        OpenRead(self: WebClient, address: Uri) -> Stream

            Opens a readable stream for the data downloaded from a resource with the URI specified as a System.Uri

            address: The URI specified as a System.Uri from which to download data.

            Returns: A System.IO.Stream used to read data from a resource.
        """
        ...

    def OpenReadAsync(self, address, userToken=None):
        """
        OpenReadAsync(self: WebClient, address: Uri)

            Opens a readable stream containing the specified resource. This method does not block the calling thread.

            address: The URI of the resource to retrieve.

        OpenReadAsync(self: WebClient, address: Uri, userToken: object)

            Opens a readable stream containing the specified resource. This method does not block the calling thread.

            address: The URI of the resource to retrieve.

            userToken: A user-defined object that is passed to the method invoked when the asynchronous operation completes.
        """
        ...

    def OpenReadTaskAsync(self, address):
        """
        OpenReadTaskAsync(self: WebClient, address: str) -> Task[Stream]

            Opens a readable stream containing the specified resource as an asynchronous operation using a task object.

            address: The URI of the resource to retrieve.

            Returns: Returns System.Threading.Tasks.Task.The task object representing the asynchronous operation. The System.Threading.Tasks.Task property on the task object returns a

             System.IO.Stream used to read data from a resource.

        OpenReadTaskAsync(self: WebClient, address: Uri) -> Task[Stream]

            Opens a readable stream containing the specified resource as an asynchronous operation using a task object.

            address: The URI of the resource to retrieve.

            Returns: Returns System.Threading.Tasks.Task.The task object representing the asynchronous operation. The System.Threading.Tasks.Task property on the task object returns a

             System.IO.Stream used to read data from a resource.
        """
        ...

    def OpenWrite(self, address, method=None):
        """
        OpenWrite(self: WebClient, address: str) -> Stream

            Opens a stream for writing data to the specified resource.

            address: The URI of the resource to receive the data.

            Returns: A System.IO.Stream used to write data to the resource.

        OpenWrite(self: WebClient, address: Uri) -> Stream

            Opens a stream for writing data to the specified resource.

            address: The URI of the resource to receive the data.

            Returns: A System.IO.Stream used to write data to the resource.

        OpenWrite(self: WebClient, address: str, method: str) -> Stream

            Opens a stream for writing data to the specified resource, using the specified method.

            address: The URI of the resource to receive the data.

            method: The method used to send the data to the resource. If null, the default is POST for http and STOR for ftp.

            Returns: A System.IO.Stream used to write data to the resource.

        OpenWrite(self: WebClient, address: Uri, method: str) -> Stream

            Opens a stream for writing data to the specified resource, by using the specified method.

            address: The URI of the resource to receive the data.

            method: The method used to send the data to the resource. If null, the default is POST for http and STOR for ftp.

            Returns: A System.IO.Stream used to write data to the resource.
        """
        ...

    def OpenWriteAsync(self, address, method=None, userToken=None):
        """
        OpenWriteAsync(self: WebClient, address: Uri)

            Opens a stream for writing data to the specified resource. This method does not block the calling thread.

            address: The URI of the resource to receive the data.

        OpenWriteAsync(self: WebClient, address: Uri, method: str)

            Opens a stream for writing data to the specified resource. This method does not block the calling thread.

            address: The URI of the resource to receive the data.

            method: The method used to send the data to the resource. If null, the default is POST for http and STOR for ftp.

        OpenWriteAsync(self: WebClient, address: Uri, method: str, userToken: object)

            Opens a stream for writing data to the specified resource, using the specified method. This method does not block the calling thread.

            address: The URI of the resource to receive the data.

            method: The method used to send the data to the resource. If null, the default is POST for http and STOR for ftp.

            userToken: A user-defined object that is passed to the method invoked when the asynchronous operation completes
        """
        ...

    def OpenWriteTaskAsync(self, address, method=None):
        """
        OpenWriteTaskAsync(self: WebClient, address: str) -> Task[Stream]

            Opens a stream for writing data to the specified resource as an asynchronous operation using a task object.

            address: The URI of the resource to receive the data.

            Returns: Returns System.Threading.Tasks.Task.The task object representing the asynchronous operation. The System.Threading.Tasks.Task property on the task object returns a

             System.IO.Stream used to write data to the resource.

        OpenWriteTaskAsync(self: WebClient, address: Uri) -> Task[Stream]

            Opens a stream for writing data to the specified resource as an asynchronous operation using a task object.

            address: The URI of the resource to receive the data.

            Returns: Returns System.Threading.Tasks.Task.The task object representing the asynchronous operation. The System.Threading.Tasks.Task property on the task object returns a

             System.IO.Stream used to write data to the resource.

        OpenWriteTaskAsync(self: WebClient, address: str, method: str) -> Task[Stream]

            Opens a stream for writing data to the specified resource as an asynchronous operation using a task object.

            address: The URI of the resource to receive the data.

            method: The method used to send the data to the resource. If null, the default is POST for http and STOR for ftp.

            Returns: Returns System.Threading.Tasks.Task.The task object representing the asynchronous operation. The System.Threading.Tasks.Task property on the task object returns a

             System.IO.Stream used to write data to the resource.

        OpenWriteTaskAsync(self: WebClient, address: Uri, method: str) -> Task[Stream]

            Opens a stream for writing data to the specified resource as an asynchronous operation using a task object.

            address: The URI of the resource to receive the data.

            method: The method used to send the data to the resource. If null, the default is POST for http and STOR for ftp.

            Returns: Returns System.Threading.Tasks.Task.The task object representing the asynchronous operation. The System.Threading.Tasks.Task property on the task object returns a

             System.IO.Stream used to write data to the resource.
        """
        ...

    def UploadData(self, address, *__args):
        """
        UploadData(self: WebClient, address: str, data: Array[Byte]) -> Array[Byte]

            Uploads a data buffer to a resource identified by a URI.

            address: The URI of the resource to receive the data.

            data: The data buffer to send to the resource.

            Returns: A System.Byte array containing the body of the response from the resource.

        UploadData(self: WebClient, address: Uri, data: Array[Byte]) -> Array[Byte]

            Uploads a data buffer to a resource identified by a URI.

            address: The URI of the resource to receive the data.

            data: The data buffer to send to the resource.

            Returns: A System.Byte array containing the body of the response from the resource.

        UploadData(self: WebClient, address: str, method: str, data: Array[Byte]) -> Array[Byte]

            Uploads a data buffer to the specified resource, using the specified method.

            address: The URI of the resource to receive the data.

            method: The HTTP method used to send the data to the resource. If null, the default is POST for http and STOR for ftp.

            data: The data buffer to send to the resource.

            Returns: A System.Byte array containing the body of the response from the resource.

        UploadData(self: WebClient, address: Uri, method: str, data: Array[Byte]) -> Array[Byte]

            Uploads a data buffer to the specified resource, using the specified method.

            address: The URI of the resource to receive the data.

            method: The HTTP method used to send the data to the resource. If null, the default is POST for http and STOR for ftp.

            data: The data buffer to send to the resource.

            Returns: A System.Byte array containing the body of the response from the resource.
        """
        ...

    def UploadDataAsync(self, address, *__args):
        """
        UploadDataAsync(self: WebClient, address: Uri, data: Array[Byte])

            Uploads a data buffer to a resource identified by a URI, using the POST method. This method does not block the calling thread.

            address: The URI of the resource to receive the data.

            data: The data buffer to send to the resource.

        UploadDataAsync(self: WebClient, address: Uri, method: str, data: Array[Byte])

            Uploads a data buffer to a resource identified by a URI, using the specified method. This method does not block the calling thread.

            address: The URI of the resource to receive the data.

            method: The method used to send the data to the resource. If ll, the default is POST for http and STOR for ftp.

            data: The data buffer to send to the resource.

        UploadDataAsync(self: WebClient, address: Uri, method: str, data: Array[Byte], userToken: object)

            Uploads a data buffer to a resource identified by a URI, using the specified method and identifying token.

            address: The URI of the resource to receive the data.

            method: The method used to send the data to the resource. If ll, the default is POST for http and STOR for ftp.

            data: The data buffer to send to the resource.

            userToken: A user-defined object that is passed to the method invoked when the asynchronous operation completes.
        """
        ...

    def UploadDataTaskAsync(self, address, *__args):
        """
        UploadDataTaskAsync(self: WebClient, address: str, data: Array[Byte]) -> Task[Array[Byte]]

            Uploads a data buffer that contains a System.Byte array to the URI specified as an asynchronous operation using a task object.

            address: The URI of the resource to receive the data.

            data: The data buffer to send to the resource.

            Returns: Returns System.Threading.Tasks.Task.The task object representing the asynchronous operation. The System.Threading.Tasks.Task property on the task object returns a

             System.Byte array containing the body of the response received from the resource when the data buffer was uploaded.

        UploadDataTaskAsync(self: WebClient, address: Uri, data: Array[Byte]) -> Task[Array[Byte]]

            Uploads a data buffer that contains a System.Byte array to the URI specified as an asynchronous operation using a task object.

            address: The URI of the resource to receive the data.

            data: The data buffer to send to the resource.

            Returns: Returns System.Threading.Tasks.Task.The task object representing the asynchronous operation. The System.Threading.Tasks.Task property on the task object returns a

             System.Byte array containing the body of the response received from the resource when the data buffer was uploaded.

        UploadDataTaskAsync(self: WebClient, address: str, method: str, data: Array[Byte]) -> Task[Array[Byte]]

            Uploads a data buffer that contains a System.Byte array to the URI specified as an asynchronous operation using a task object.

            address: The URI of the resource to receive the data.

            method: The method used to send the data to the resource. If ll, the default is POST for http and STOR for ftp.

            data: The data buffer to send to the resource.

            Returns: Returns System.Threading.Tasks.Task.The task object representing the asynchronous operation. The System.Threading.Tasks.Task property on the task object returns a

             System.Byte array containing the body of the response received from the resource when the data buffer was uploaded.

        UploadDataTaskAsync(self: WebClient, address: Uri, method: str, data: Array[Byte]) -> Task[Array[Byte]]

            Uploads a data buffer that contains a System.Byte array to the URI specified as an asynchronous operation using a task object.

            address: The URI of the resource to receive the data.

            method: The method used to send the data to the resource. If ll, the default is POST for http and STOR for ftp.

            data: The data buffer to send to the resource.

            Returns: Returns System.Threading.Tasks.Task.The task object representing the asynchronous operation. The System.Threading.Tasks.Task property on the task object returns a

             System.Byte array containing the body of the response received from the resource when the data buffer was uploaded.
        """
        ...

    def UploadFile(self, address, *__args):
        """
        UploadFile(self: WebClient, address: str, fileName: str) -> Array[Byte]

            Uploads the specified local file to a resource with the specified URI.

            address: The URI of the resource to receive the file. For example, ftp://localhost/samplefile.txt.

            fileName: The file to send to the resource. For example, "samplefile.txt".

            Returns: A System.Byte array containing the body of the response from the resource.

        UploadFile(self: WebClient, address: Uri, fileName: str) -> Array[Byte]

            Uploads the specified local file to a resource with the specified URI.

            address: The URI of the resource to receive the file. For example, ftp://localhost/samplefile.txt.

            fileName: The file to send to the resource. For example, "samplefile.txt".

            Returns: A System.Byte array containing the body of the response from the resource.

        UploadFile(self: WebClient, address: str, method: str, fileName: str) -> Array[Byte]

            Uploads the specified local file to the specified resource, using the specified method.

            address: The URI of the resource to receive the file.

            method: The method used to send the file to the resource. If ll, the default is POST for http and STOR for ftp.

            fileName: The file to send to the resource.

            Returns: A System.Byte array containing the body of the response from the resource.

        UploadFile(self: WebClient, address: Uri, method: str, fileName: str) -> Array[Byte]

            Uploads the specified local file to the specified resource, using the specified method.

            address: The URI of the resource to receive the file.

            method: The method used to send the file to the resource. If ll, the default is POST for http and STOR for ftp.

            fileName: The file to send to the resource.

            Returns: A System.Byte array containing the body of the response from the resource.
        """
        ...

    def UploadFileAsync(self, address, *__args):
        """
        UploadFileAsync(self: WebClient, address: Uri, fileName: str)

            Uploads the specified local file to the specified resource, using the POST method. This method does not block the calling thread.

            address: The URI of the resource to receive the file. For HTTP resources, this URI must identify a resource that can accept a request sent with the POST method, such as a

             script or ASP page.

            fileName: The file to send to the resource.

        UploadFileAsync(self: WebClient, address: Uri, method: str, fileName: str)

            Uploads the specified local file to the specified resource, using the POST method. This method does not block the calling thread.

            address: The URI of the resource to receive the file. For HTTP resources, this URI must identify a resource that can accept a request sent with the POST method, such as a

             script or ASP page.

            method: The method used to send the data to the resource. If ll, the default is POST for http and STOR for ftp.

            fileName: The file to send to the resource.

        UploadFileAsync(self: WebClient, address: Uri, method: str, fileName: str, userToken: object)

            Uploads the specified local file to the specified resource, using the POST method. This method does not block the calling thread.

            address: The URI of the resource to receive the file. For HTTP resources, this URI must identify a resource that can accept a request sent with the POST method, such as a

             script or ASP page.

            method: The method used to send the data to the resource. If ll, the default is POST for http and STOR for ftp.

            fileName: The file to send to the resource.

            userToken: A user-defined object that is passed to the method invoked when the asynchronous operation completes.
        """
        ...

    def UploadFileTaskAsync(self, address, *__args):
        """
        UploadFileTaskAsync(self: WebClient, address: str, fileName: str) -> Task[Array[Byte]]

            Uploads the specified local file to a resource as an asynchronous operation using a task object.

            address: The URI of the resource to receive the file. For HTTP resources, this URI must identify a resource that can accept a request sent with the POST method, such as a

             script or ASP page.

            fileName: The local file to send to the resource.

            Returns: Returns System.Threading.Tasks.Task.The task object representing the asynchronous operation. The System.Threading.Tasks.Task property on the task object returns a

             System.Byte array containing the body of the response received from the resource when the file was uploaded.

        UploadFileTaskAsync(self: WebClient, address: Uri, fileName: str) -> Task[Array[Byte]]

            Uploads the specified local file to a resource as an asynchronous operation using a task object.

            address: The URI of the resource to receive the file. For HTTP resources, this URI must identify a resource that can accept a request sent with the POST method, such as a

             script or ASP page.

            fileName: The local file to send to the resource.

            Returns: Returns System.Threading.Tasks.Task.The task object representing the asynchronous operation. The System.Threading.Tasks.Task property on the task object returns a

             System.Byte array containing the body of the response received from the resource when the file was uploaded.

        UploadFileTaskAsync(self: WebClient, address: str, method: str, fileName: str) -> Task[Array[Byte]]

            Uploads the specified local file to a resource as an asynchronous operation using a task object.

            address: The URI of the resource to receive the file. For HTTP resources, this URI must identify a resource that can accept a request sent with the POST method, such as a

             script or ASP page.

            method: The method used to send the data to the resource. If ll, the default is POST for http and STOR for ftp.

            fileName: The local file to send to the resource.

            Returns: Returns System.Threading.Tasks.Task.The task object representing the asynchronous operation. The System.Threading.Tasks.Task property on the task object returns a

             System.Byte array containing the body of the response received from the resource when the file was uploaded.

        UploadFileTaskAsync(self: WebClient, address: Uri, method: str, fileName: str) -> Task[Array[Byte]]

            Uploads the specified local file to a resource as an asynchronous operation using a task object.

            address: The URI of the resource to receive the file. For HTTP resources, this URI must identify a resource that can accept a request sent with the POST method, such as a

             script or ASP page.

            method: The method used to send the data to the resource. If ll, the default is POST for http and STOR for ftp.

            fileName: The local file to send to the resource.

            Returns: Returns System.Threading.Tasks.Task.The task object representing the asynchronous operation. The System.Threading.Tasks.Task property on the task object returns a

             System.Byte array containing the body of the response received from the resource when the file was uploaded.
        """
        ...

    def UploadString(self, address, *__args):
        """
        UploadString(self: WebClient, address: str, data: str) -> str

            Uploads the specified string to the specified resource, using the POST method.

            address: The URI of the resource to receive the string. For Http resources, this URI must identify a resource that can accept a request sent with the POST method, such as a

             script or ASP page.

            data: The string to be uploaded.

            Returns: A System.String containing the response sent by the server.

        UploadString(self: WebClient, address: Uri, data: str) -> str

            Uploads the specified string to the specified resource, using the POST method.

            address: The URI of the resource to receive the string. For Http resources, this URI must identify a resource that can accept a request sent with the POST method, such as a

             script or ASP page.

            data: The string to be uploaded.

            Returns: A System.String containing the response sent by the server.

        UploadString(self: WebClient, address: str, method: str, data: str) -> str

            Uploads the specified string to the specified resource, using the specified method.

            address: The URI of the resource to receive the string. This URI must identify a resource that can accept a request sent with the method method.

            method: The HTTP method used to send the string to the resource. If null, the default is POST for http and STOR for ftp.

            data: The string to be uploaded.

            Returns: A System.String containing the response sent by the server.

        UploadString(self: WebClient, address: Uri, method: str, data: str) -> str

            Uploads the specified string to the specified resource, using the specified method.

            address: The URI of the resource to receive the string. This URI must identify a resource that can accept a request sent with the method method.

            method: The HTTP method used to send the string to the resource. If null, the default is POST for http and STOR for ftp.

            data: The string to be uploaded.

            Returns: A System.String containing the response sent by the server.
        """
        ...

    def UploadStringAsync(self, address, *__args):
        """
        UploadStringAsync(self: WebClient, address: Uri, data: str)

            Uploads the specified string to the specified resource. This method does not block the calling thread.

            address: The URI of the resource to receive the string. For HTTP resources, this URI must identify a resource that can accept a request sent with the POST method, such as a

             script or ASP page.

            data: The string to be uploaded.

        UploadStringAsync(self: WebClient, address: Uri, method: str, data: str)

            Uploads the specified string to the specified resource. This method does not block the calling thread.

            address: The URI of the resource to receive the string. For HTTP resources, this URI must identify a resource that can accept a request sent with the POST method, such as a

             script or ASP page.

            method: The HTTP method used to send the file to the resource. If null, the default is POST for http and STOR for ftp.

            data: The string to be uploaded.

        UploadStringAsync(self: WebClient, address: Uri, method: str, data: str, userToken: object)

            Uploads the specified string to the specified resource. This method does not block the calling thread.

            address: The URI of the resource to receive the string. For HTTP resources, this URI must identify a resource that can accept a request sent with the POST method, such as a

             script or ASP page.

            method: The HTTP method used to send the file to the resource. If null, the default is POST for http and STOR for ftp.

            data: The string to be uploaded.

            userToken: A user-defined object that is passed to the method invoked when the asynchronous operation completes.
        """
        ...

    def UploadStringTaskAsync(self, address, *__args):
        """
        UploadStringTaskAsync(self: WebClient, address: str, data: str) -> Task[str]

            Uploads the specified string to the specified resource as an asynchronous operation using a task object.

            address: The URI of the resource to receive the string. For HTTP resources, this URI must identify a resource that can accept a request sent with the POST method, such as a

             script or ASP page.

            data: The string to be uploaded.

            Returns: Returns System.Threading.Tasks.Task.The task object representing the asynchronous operation. The System.Threading.Tasks.Task property on the task object returns a

             System.String containing the response sent by the server.

        UploadStringTaskAsync(self: WebClient, address: Uri, data: str) -> Task[str]

            Uploads the specified string to the specified resource as an asynchronous operation using a task object.

            address: The URI of the resource to receive the string. For HTTP resources, this URI must identify a resource that can accept a request sent with the POST method, such as a

             script or ASP page.

            data: The string to be uploaded.

            Returns: Returns System.Threading.Tasks.Task.The task object representing the asynchronous operation. The System.Threading.Tasks.Task property on the task object returns a

             System.String containing the response sent by the server.

        UploadStringTaskAsync(self: WebClient, address: str, method: str, data: str) -> Task[str]

            Uploads the specified string to the specified resource as an asynchronous operation using a task object.

            address: The URI of the resource to receive the string. For HTTP resources, this URI must identify a resource that can accept a request sent with the POST method, such as a

             script or ASP page.

            method: The HTTP method used to send the file to the resource. If null, the default is POST for http and STOR for ftp.

            data: The string to be uploaded.

            Returns: Returns System.Threading.Tasks.Task.The task object representing the asynchronous operation. The System.Threading.Tasks.Task property on the task object returns a

             System.String containing the response sent by the server.

        UploadStringTaskAsync(self: WebClient, address: Uri, method: str, data: str) -> Task[str]

            Uploads the specified string to the specified resource as an asynchronous operation using a task object.

            address: The URI of the resource to receive the string. For HTTP resources, this URI must identify a resource that can accept a request sent with the POST method, such as a

             script or ASP page.

            method: The HTTP method used to send the file to the resource. If null, the default is POST for http and STOR for ftp.

            data: The string to be uploaded.

            Returns: Returns System.Threading.Tasks.Task.The task object representing the asynchronous operation. The System.Threading.Tasks.Task property on the task object returns a

             System.String containing the response sent by the server.
        """
        ...

    def UploadValues(self, address, *__args):
        """
        UploadValues(self: WebClient, address: str, data: NameValueCollection) -> Array[Byte]

            Uploads the specified name/value collection to the resource identified by the specified URI.

            address: The URI of the resource to receive the collection.

            data: The System.Collections.Specialized.NameValueCollection to send to the resource.

            Returns: A System.Byte array containing the body of the response from the resource.

        UploadValues(self: WebClient, address: Uri, data: NameValueCollection) -> Array[Byte]

            Uploads the specified name/value collection to the resource identified by the specified URI.

            address: The URI of the resource to receive the collection.

            data: The System.Collections.Specialized.NameValueCollection to send to the resource.

            Returns: A System.Byte array containing the body of the response from the resource.

        UploadValues(self: WebClient, address: str, method: str, data: NameValueCollection) -> Array[Byte]

            Uploads the specified name/value collection to the resource identified by the specified URI, using the specified method.

            address: The URI of the resource to receive the collection.

            method: The HTTP method used to send the file to the resource. If null, the default is POST for http and STOR for ftp.

            data: The System.Collections.Specialized.NameValueCollection to send to the resource.

            Returns: A System.Byte array containing the body of the response from the resource.

        UploadValues(self: WebClient, address: Uri, method: str, data: NameValueCollection) -> Array[Byte]

            Uploads the specified name/value collection to the resource identified by the specified URI, using the specified method.

            address: The URI of the resource to receive the collection.

            method: The HTTP method used to send the file to the resource. If null, the default is POST for http and STOR for ftp.

            data: The System.Collections.Specialized.NameValueCollection to send to the resource.

            Returns: A System.Byte array containing the body of the response from the resource.
        """
        ...

    def UploadValuesAsync(self, address, *__args):
        """
        UploadValuesAsync(self: WebClient, address: Uri, data: NameValueCollection)

            Uploads the data in the specified name/value collection to the resource identified by the specified URI. This method does not block the calling thread.

            address: The URI of the resource to receive the collection. This URI must identify a resource that can accept a request sent with the default method. See remarks.

            data: The System.Collections.Specialized.NameValueCollection to send to the resource.

        UploadValuesAsync(self: WebClient, address: Uri, method: str, data: NameValueCollection)

            Uploads the data in the specified name/value collection to the resource identified by the specified URI, using the specified method. This method does not block the

             calling thread.

            address: The URI of the resource to receive the collection. This URI must identify a resource that can accept a request sent with the method method.

            method: The method used to send the string to the resource. If null, the default is POST for http and STOR for ftp.

            data: The System.Collections.Specialized.NameValueCollection to send to the resource.

        UploadValuesAsync(self: WebClient, address: Uri, method: str, data: NameValueCollection, userToken: object)

            Uploads the data in the specified name/value collection to the resource identified by the specified URI, using the specified method. This method does not block the

             calling thread, and allows the caller to pass an object to the method that is invoked when the operation completes.

            address: The URI of the resource to receive the collection. This URI must identify a resource that can accept a request sent with the method method.

            method: The HTTP method used to send the string to the resource. If null, the default is POST for http and STOR for ftp.

            data: The System.Collections.Specialized.NameValueCollection to send to the resource.

            userToken: A user-defined object that is passed to the method invoked when the asynchronous operation completes.
        """
        ...

    def UploadValuesTaskAsync(self, address, *__args):
        """
        UploadValuesTaskAsync(self: WebClient, address: str, data: NameValueCollection) -> Task[Array[Byte]]

            Uploads the specified name/value collection to the resource identified by the specified URI as an asynchronous operation using a task object.

            address: The URI of the resource to receive the collection.

            data: The System.Collections.Specialized.NameValueCollection to send to the resource.

            Returns: Returns System.Threading.Tasks.Task.The task object representing the asynchronous operation. The System.Threading.Tasks.Task property on the task object returns a

             System.Byte array containing the response sent by the server.

        UploadValuesTaskAsync(self: WebClient, address: str, method: str, data: NameValueCollection) -> Task[Array[Byte]]

            Uploads the specified name/value collection to the resource identified by the specified URI as an asynchronous operation using a task object.

            address: The URI of the resource to receive the collection.

            method: The HTTP method used to send the collection to the resource. If null, the default is POST for http and STOR for ftp.

            data: The System.Collections.Specialized.NameValueCollection to send to the resource.

            Returns: Returns System.Threading.Tasks.Task.The task object representing the asynchronous operation. The System.Threading.Tasks.Task property on the task object returns a

             System.Byte array containing the response sent by the server.

        UploadValuesTaskAsync(self: WebClient, address: Uri, data: NameValueCollection) -> Task[Array[Byte]]

            Uploads the specified name/value collection to the resource identified by the specified URI as an asynchronous operation using a task object.

            address: The URI of the resource to receive the collection.

            data: The System.Collections.Specialized.NameValueCollection to send to the resource.

            Returns: Returns System.Threading.Tasks.Task.The task object representing the asynchronous operation. The System.Threading.Tasks.Task property on the task object returns a

             System.Byte array containing the response sent by the server.

        UploadValuesTaskAsync(self: WebClient, address: Uri, method: str, data: NameValueCollection) -> Task[Array[Byte]]

            Uploads the specified name/value collection to the resource identified by the specified URI as an asynchronous operation using a task object.

            address: The URI of the resource to receive the collection.

            method: The HTTP method used to send the collection to the resource. If null, the default is POST for http and STOR for ftp.

            data: The System.Collections.Specialized.NameValueCollection to send to the resource.

            Returns: Returns System.Threading.Tasks.Task.The task object representing the asynchronous operation. The System.Threading.Tasks.Task property on the task object returns a

             System.Byte array containing the response sent by the server.
        """
        ...

    @property
    def AllowReadStreamBuffering(self):
        """
        Gets or sets a value that indicates whether to buffer the data read from the Internet resource for a System.Net.WebClient instance.

        Get: AllowReadStreamBuffering(self: WebClient) -> bool

        Set: AllowReadStreamBuffering(self: WebClient) = value
        """
        ...

    @property
    def AllowWriteStreamBuffering(self):
        """
        Gets or sets a value that indicates whether to buffer the data written to the Internet resource for a System.Net.WebClient instance.

        Get: AllowWriteStreamBuffering(self: WebClient) -> bool

        Set: AllowWriteStreamBuffering(self: WebClient) = value
        """
        ...

    @property
    def BaseAddress(self):
        """
        Gets or sets the base URI for requests made by a System.Net.WebClient.

        Get: BaseAddress(self: WebClient) -> str

        Set: BaseAddress(self: WebClient) = value
        """
        ...

    @property
    def CachePolicy(self):
        """
        Gets or sets the application's cache policy for any resources obtained by this WebClient instance using System.Net.WebRequest objects.

        Get: CachePolicy(self: WebClient) -> RequestCachePolicy

        Set: CachePolicy(self: WebClient) = value
        """
        ...

    @property
    def CanRaiseEvents(self):
        """ Gets a value indicating whether the component can raise an event. """
        ...

    @property
    def Credentials(self):
        """
        Gets or sets the network credentials that are sent to the host and used to authenticate the request.

        Get: Credentials(self: WebClient) -> ICredentials

        Set: Credentials(self: WebClient) = value
        """
        ...

    @property
    def DesignMode(self):
        """ Gets a value that indicates whether the System.ComponentModel.Component is currently in design mode. """
        ...

    @property
    def Encoding(self):
        """
        Gets and sets the System.Text.Encoding used to upload and download strings.

        Get: Encoding(self: WebClient) -> Encoding

        Set: Encoding(self: WebClient) = value
        """
        ...

    @property
    def Events(self):
        """ Gets the list of event handlers that are attached to this System.ComponentModel.Component. """
        ...

    @property
    def Headers(self):
        """
        Gets or sets a collection of header name/value pairs associated with the request.

        Get: Headers(self: WebClient) -> WebHeaderCollection

        Set: Headers(self: WebClient) = value
        """
        ...

    @property
    def IsBusy(self):
        """
        Gets whether a Web request is in progress.

        Get: IsBusy(self: WebClient) -> bool
        """
        ...

    @property
    def Proxy(self):
        """
        Gets or sets the proxy used by this System.Net.WebClient object.

        Get: Proxy(self: WebClient) -> IWebProxy

        Set: Proxy(self: WebClient) = value
        """
        ...

    @property
    def QueryString(self):
        """
        Gets or sets a collection of query name/value pairs associated with the request.

        Get: QueryString(self: WebClient) -> NameValueCollection

        Set: QueryString(self: WebClient) = value
        """
        ...

    @property
    def ResponseHeaders(self):
        """
        Gets a collection of header name/value pairs associated with the response.

        Get: ResponseHeaders(self: WebClient) -> WebHeaderCollection
        """
        ...

    @property
    def UseDefaultCredentials(self):
        """
        Gets or sets a System.Boolean value that controls whether the System.Net.CredentialCache.DefaultCredentials are sent with requests.

        Get: UseDefaultCredentials(self: WebClient) -> bool

        Set: UseDefaultCredentials(self: WebClient) = value
        """
        ...


    DownloadDataCompleted = None
    DownloadFileCompleted = None
    DownloadProgressChanged = None
    DownloadStringCompleted = None
    OpenReadCompleted = None
    OpenWriteCompleted = None
    UploadDataCompleted = None
    UploadFileCompleted = None
    UploadProgressChanged = None
    UploadStringCompleted = None
    UploadValuesCompleted = None
    WriteStreamClosed = None


class WebException(InvalidOperationException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>
    """
    The exception that is thrown when an error occurs while accessing the network through a pluggable protocol.

    WebException()

    WebException(message: str)

    WebException(message: str, innerException: Exception)

    WebException(message: str, status: WebExceptionStatus)

    WebException(message: str, innerException: Exception, status: WebExceptionStatus, response: WebResponse)
    """
    def GetObjectData(self, serializationInfo, streamingContext):
        """
        GetObjectData(self: WebException, serializationInfo: SerializationInfo, streamingContext: StreamingContext)

            Populates a System.Runtime.Serialization.SerializationInfo instance with the data needed to serialize the System.Net.WebException.

            serializationInfo: The System.Runtime.Serialization.SerializationInfo to be used.

            streamingContext: The System.Runtime.Serialization.StreamingContext to be used.
        """
        ...

    @property
    def Response(self):
        """
        Gets the response that the remote host returned.

        Get: Response(self: WebException) -> WebResponse
        """
        ...

    @property
    def Status(self):
        """
        Gets the status of the response.

        Get: Status(self: WebException) -> WebExceptionStatus
        """
        ...


    SerializeObjectState = None


class WebExceptionStatus(Enum): # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Defines status codes for the System.Net.WebException class.

    enum WebExceptionStatus, values: CacheEntryNotFound (18), ConnectFailure (2), ConnectionClosed (8), KeepAliveFailure (12), MessageLengthLimitExceeded (17), NameResolutionFailure (1), Pending (13), PipelineFailure (5), ProtocolError (7), ProxyNameResolutionFailure (15), ReceiveFailure (3), RequestCanceled (6), RequestProhibitedByCachePolicy (19), RequestProhibitedByProxy (20), SecureChannelFailure (10), SendFailure (4), ServerProtocolViolation (11), Success (0), Timeout (14), TrustFailure (9), UnknownError (16)
    """
    CacheEntryNotFound = None
    ConnectFailure = None
    ConnectionClosed = None
    KeepAliveFailure = None
    MessageLengthLimitExceeded = None
    NameResolutionFailure = None
    Pending = None
    PipelineFailure = None
    ProtocolError = None
    ProxyNameResolutionFailure = None
    ReceiveFailure = None
    RequestCanceled = None
    RequestProhibitedByCachePolicy = None
    RequestProhibitedByProxy = None
    SecureChannelFailure = None
    SendFailure = None
    ServerProtocolViolation = None
    Success = None
    Timeout = None
    TrustFailure = None
    UnknownError = None
    value__ = None


class WebHeaderCollection(NameValueCollection): # skipped bases: <type 'ICollection'>, <type 'IEnumerable'>, <type 'IDeserializationCallback'>, <type 'ISerializable'>
    """
    Contains protocol headers associated with a request or response.

    WebHeaderCollection()
    """
    def AddWithoutValidate(self, *args): #cannot find CLR method
        """
        AddWithoutValidate(self: WebHeaderCollection, headerName: str, headerValue: str)

            Inserts a header into the collection without checking whether the header is on the restricted header list.

            headerName: The header to add to the collection.

            headerValue: The content of the header.
        """
        ...

    def GetEnumerator(self):
        """
        GetEnumerator(self: WebHeaderCollection) -> IEnumerator

            Returns an enumerator that can iterate through the System.Net.WebHeaderCollection instance.

            Returns: An System.Collections.IEnumerator for the System.Net.WebHeaderCollection.
        """
        ...

    @staticmethod
    def IsRestricted(headerName, response=None):
        """
        IsRestricted(headerName: str) -> bool

            Tests whether the specified HTTP header can be set for the request.

            headerName: The header to test.

            Returns: ue if the header is restricted; otherwise lse.

        IsRestricted(headerName: str, response: bool) -> bool

            Tests whether the specified HTTP header can be set for the request or the response.

            headerName: The header to test.

            response: Does the Framework test the response or the request?

            Returns: ue if the header is restricted; otherwise, lse.
        """
        ...

    def ToByteArray(self):
        """
        ToByteArray(self: WebHeaderCollection) -> Array[Byte]

            Converts the System.Net.WebHeaderCollection to a byte array..

            Returns: A System.Byte array holding the header collection.
        """
        ...

    def ToString(self):
        """
        ToString(self: WebHeaderCollection) -> str

            This method is obsolete.

            Returns: The System.String representation of the collection.
        """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...

    @property
    def AllKeys(self):
        """
        Gets all header names (keys) in the collection.

        Get: AllKeys(self: WebHeaderCollection) -> Array[str]
        """
        ...

    @property
    def Count(self):
        """
        Gets the number of headers in the collection.

        Get: Count(self: WebHeaderCollection) -> int
        """
        ...

    @property
    def IsReadOnly(self):
        """ Gets or sets a value indicating whether the System.Collections.Specialized.NameObjectCollectionBase instance is read-only. """
        ...

    @property
    def Keys(self):
        """
        Gets the collection of header names (keys) in the collection.

        Get: Keys(self: WebHeaderCollection) -> KeysCollection
        """
        ...



class WebPermission(CodeAccessPermission, IUnrestrictedPermission): # skipped bases: <type 'ISecurityEncodable'>, <type 'IPermission'>, <type 'IStackWalk'>
    """
    Controls rights to access HTTP Internet resources.

    WebPermission(state: PermissionState)

    WebPermission()

    WebPermission(access: NetworkAccess, uriRegex: Regex)

    WebPermission(access: NetworkAccess, uriString: str)
    """
    def AddPermission(self, access, *__args):
        """
        AddPermission(self: WebPermission, access: NetworkAccess, uriString: str)

            Adds the specified URI string with the specified access rights to the current System.Net.WebPermission.

            access: A System.Net.NetworkAccess that specifies the access rights that are granted to the URI.

            uriString: A string that describes the URI to which access rights are granted.

        AddPermission(self: WebPermission, access: NetworkAccess, uriRegex: Regex)

            Adds the specified URI with the specified access rights to the current System.Net.WebPermission.

            access: A NetworkAccess that specifies the access rights that are granted to the URI.

            uriRegex: A regular expression that describes the set of URIs to which access rights are granted.
        """
        ...

    @staticmethod # known case of __new__
    def __new__(cls, *__args):
        """
        __new__(cls: type, state: PermissionState)

        __new__(cls: type)

        __new__(cls: type, access: NetworkAccess, uriRegex: Regex)

        __new__(cls: type, access: NetworkAccess, uriString: str)
        """
        ...

    @property
    def AcceptList(self):
        """
        This property returns an enumeration of a single accept permissions held by this System.Net.WebPermission. The possible objects types contained in the returned enumeration are System.String and System.Text.RegularExpressions.Regex.

        Get: AcceptList(self: WebPermission) -> IEnumerator
        """
        ...

    @property
    def ConnectList(self):
        """
        This property returns an enumeration of a single connect permissions held by this System.Net.WebPermission. The possible objects types contained in the returned enumeration are System.String and System.Text.RegularExpressions.Regex.

        Get: ConnectList(self: WebPermission) -> IEnumerator
        """
        ...



class WebPermissionAttribute(CodeAccessSecurityAttribute): # skipped bases: <type '_Attribute'>
    """
    Specifies permission to access Internet resources. This class cannot be inherited.

    WebPermissionAttribute(action: SecurityAction)
    """
    def CreatePermission(self):
        """
        CreatePermission(self: WebPermissionAttribute) -> IPermission

            Creates and returns a new instance of the System.Net.WebPermission class.

            Returns: A System.Net.WebPermission corresponding to the security declaration.
        """
        ...

    @property
    def Accept(self):
        """
        Gets or sets the URI string accepted by the current System.Net.WebPermissionAttribute.

        Get: Accept(self: WebPermissionAttribute) -> str

        Set: Accept(self: WebPermissionAttribute) = value
        """
        ...

    @property
    def AcceptPattern(self):
        """
        Gets or sets a regular expression pattern that describes the URI accepted by the current System.Net.WebPermissionAttribute.

        Get: AcceptPattern(self: WebPermissionAttribute) -> str

        Set: AcceptPattern(self: WebPermissionAttribute) = value
        """
        ...

    @property
    def Connect(self):
        """
        Gets or sets the URI connection string controlled by the current System.Net.WebPermissionAttribute.

        Get: Connect(self: WebPermissionAttribute) -> str

        Set: Connect(self: WebPermissionAttribute) = value
        """
        ...

    @property
    def ConnectPattern(self):
        """
        Gets or sets a regular expression pattern that describes the URI connection controlled by the current System.Net.WebPermissionAttribute.

        Get: ConnectPattern(self: WebPermissionAttribute) -> str

        Set: ConnectPattern(self: WebPermissionAttribute) = value
        """
        ...



class WebProxy(object, IAutoWebProxy, ISerializable): # skipped bases: <type 'IWebProxy'>
    """
    Contains HTTP proxy settings for the System.Net.WebRequest class.

    WebProxy()

    WebProxy(Address: Uri)

    WebProxy(Address: Uri, BypassOnLocal: bool)

    WebProxy(Address: Uri, BypassOnLocal: bool, BypassList: Array[str])

    WebProxy(Address: Uri, BypassOnLocal: bool, BypassList: Array[str], Credentials: ICredentials)

    WebProxy(Host: str, Port: int)

    WebProxy(Address: str)

    WebProxy(Address: str, BypassOnLocal: bool)

    WebProxy(Address: str, BypassOnLocal: bool, BypassList: Array[str])

    WebProxy(Address: str, BypassOnLocal: bool, BypassList: Array[str], Credentials: ICredentials)
    """
    @staticmethod
    def GetDefaultProxy():
        """
        GetDefaultProxy() -> WebProxy

            Reads the Internet Explorer nondynamic proxy settings.

            Returns: A System.Net.WebProxy instance that contains the nondynamic proxy settings from Internet Explorer 5.5 and later.
        """
        ...

    def GetProxy(self, destination):
        """
        GetProxy(self: WebProxy, destination: Uri) -> Uri

            Returns the proxied URI for a request.

            destination: The System.Uri instance of the requested Internet resource.

            Returns: The System.Uri instance of the Internet resource, if the resource is on the bypass list; otherwise, the System.Uri instance of the proxy.
        """
        ...

    def IsBypassed(self, host):
        """
        IsBypassed(self: WebProxy, host: Uri) -> bool

            Indicates whether to use the proxy server for the specified host.

            host: The System.Uri instance of the host to check for proxy use.

            Returns: ue if the proxy server should not be used for host; otherwise, lse.
        """
        ...

    @property
    def Address(self):
        """
        Gets or sets the address of the proxy server.

        Get: Address(self: WebProxy) -> Uri

        Set: Address(self: WebProxy) = value
        """
        ...

    @property
    def BypassArrayList(self):
        """
        Gets a list of addresses that do not use the proxy server.

        Get: BypassArrayList(self: WebProxy) -> ArrayList
        """
        ...

    @property
    def BypassList(self):
        """
        Gets or sets an array of addresses that do not use the proxy server.

        Get: BypassList(self: WebProxy) -> Array[str]

        Set: BypassList(self: WebProxy) = value
        """
        ...

    @property
    def BypassProxyOnLocal(self):
        """
        Gets or sets a value that indicates whether to bypass the proxy server for local addresses.

        Get: BypassProxyOnLocal(self: WebProxy) -> bool

        Set: BypassProxyOnLocal(self: WebProxy) = value
        """
        ...

    @property
    def Credentials(self):
        """
        Gets or sets the credentials to submit to the proxy server for authentication.

        Get: Credentials(self: WebProxy) -> ICredentials

        Set: Credentials(self: WebProxy) = value
        """
        ...

    @property
    def UseDefaultCredentials(self):
        """
        Gets or sets a System.Boolean value that controls whether the System.Net.CredentialCache.DefaultCredentials are sent with requests.

        Get: UseDefaultCredentials(self: WebProxy) -> bool

        Set: UseDefaultCredentials(self: WebProxy) = value
        """
        ...



class WebRequestMethods: # skipped bases: <type 'object'>
    """ Container class for System.Net.WebRequestMethods.Ftp, System.Net.WebRequestMethods.File, and System.Net.WebRequestMethods.Http classes. This class cannot be inherited """
    def File(self, *args): #cannot find CLR method
        # no doc
        ...

    def Ftp(self, *args): #cannot find CLR method
        # no doc
        ...

    def Http(self, *args): #cannot find CLR method
        # no doc
        ...

    File = None
    Ftp = None
    Http = None
    __all__ = [
        'File',
        'Ftp',
        'Http',
    ]


class WebUtility: # skipped bases: <type 'object'>
    """ Provides methods for encoding and decoding URLs when processing Web requests. """
    @staticmethod
    def HtmlDecode(value, output=None):
        """
        HtmlDecode(value: str) -> str

            Converts a string that has been HTML-encoded for HTTP transmission into a decoded string.

            value: The string to decode.

            Returns: A decoded string.

        HtmlDecode(value: str, output: TextWriter)

            Converts a string that has been HTML-encoded into a decoded string, and sends the decoded string to a System.IO.TextWriter output stream.

            value: The string to decode.

            output: A System.IO.TextWriter stream of output.
        """
        ...

    @staticmethod
    def HtmlEncode(value, output=None):
        """
        HtmlEncode(value: str) -> str

            Converts a string to an HTML-encoded string.

            value: The string to encode.

            Returns: An encoded string.

        HtmlEncode(value: str, output: TextWriter)

            Converts a string into an HTML-encoded string, and returns the output as a System.IO.TextWriter stream of output.

            value: The string to encode.

            output: A System.IO.TextWriter output stream.
        """
        ...

    @staticmethod
    def UrlDecode(encodedValue):
        """
        UrlDecode(encodedValue: str) -> str

            Converts a string that has been encoded for transmission in a URL into a decoded string.

            encodedValue: A URL-encoded string to decode.

            Returns: Returns System.String.A decoded string.
        """
        ...

    @staticmethod
    def UrlDecodeToBytes(encodedValue, offset, count):
        """
        UrlDecodeToBytes(encodedValue: Array[Byte], offset: int, count: int) -> Array[Byte]

            Converts an encoded byte array that has been encoded for transmission in a URL into a decoded byte array.

            encodedValue: A URL-encoded System.Byte array to decode.

            offset: The offset, in bytes, from the start of the System.Byte array to decode.

            count: The count, in bytes, to decode from the System.Byte array.

            Returns: Returns System.Byte.A decoded System.Byte array.
        """
        ...

    @staticmethod
    def UrlEncode(value):
        """
        UrlEncode(value: str) -> str

            Converts a text string into a URL-encoded string.

            value: The text to URL-encode.

            Returns: Returns System.String.A URL-encoded string.
        """
        ...

    @staticmethod
    def UrlEncodeToBytes(value, offset, count):
        """
        UrlEncodeToBytes(value: Array[Byte], offset: int, count: int) -> Array[Byte]

            Converts a byte array into a URL-encoded byte array.

            value: The System.Byte array to URL-encode.

            offset: The offset, in bytes, from the start of the System.Byte array to encode.

            count: The count, in bytes, to encode from the System.Byte array.

            Returns: Returns System.Byte.An encoded System.Byte array.
        """
        ...

    __all__ = [
        'HtmlDecode',
        'HtmlEncode',
        'UrlDecode',
        'UrlDecodeToBytes',
        'UrlEncode',
        'UrlEncodeToBytes',
    ]


class WriteStreamClosedEventArgs(EventArgs):
    """
    Provides data for the System.Net.WebClient.WriteStreamClosed event.

    WriteStreamClosedEventArgs()
    """
    @property
    def Error(self):
        """
        Gets the error value when a write stream is closed.

        Get: Error(self: WriteStreamClosedEventArgs) -> Exception
        """
        ...



class WriteStreamClosedEventHandler(MulticastDelegate): # skipped bases: <type 'ICloneable'>, <type 'ISerializable'>
    """
    Represents the method that will handle the System.Net.WebClient.WriteStreamClosed event of a System.Net.WebClient.

    WriteStreamClosedEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: WriteStreamClosedEventHandler, sender: object, e: WriteStreamClosedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result):
        """ EndInvoke(self: WriteStreamClosedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender, e):
        """ Invoke(self: WriteStreamClosedEventHandler, sender: object, e: WriteStreamClosedEventArgs) """
        ...


# variables with complex values
