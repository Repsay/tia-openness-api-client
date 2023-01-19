# encoding: utf-8
# module System.Net.Configuration calls itself Configuration
# from System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AuthenticationModuleElement(ConfigurationElement):
    """
    Represents the type information for an authentication module. This class cannot be inherited.

    AuthenticationModuleElement()

    AuthenticationModuleElement(typeName: str)
    """

    @staticmethod  # known case of __new__
    def __new__(cls, typeName=None):
        """
        __new__(cls: type)

        __new__(cls: type, typeName: str)
        """
        ...
    @property
    def ElementProperty(self):
        """Gets the System.Configuration.ConfigurationElementProperty object that represents the System.Configuration.ConfigurationElement object itself."""
        ...
    @property
    def EvaluationContext(self):
        """Gets the System.Configuration.ContextInformation object for the System.Configuration.ConfigurationElement object."""
        ...
    @property
    def HasContext(self):
        """Gets a value that indicates whether the System.Configuration.ConfigurationElement.CurrentConfiguration property is ll."""
        ...
    @property
    def Properties(self): ...
    @property
    def Type(self):
        """
        Gets or sets the type and assembly information for the current instance.

        Get: Type(self: AuthenticationModuleElement) -> str

        Set: Type(self: AuthenticationModuleElement) = value
        """
        ...

class AuthenticationModuleElementCollection(
    ConfigurationElementCollection
):  # skipped bases: <type 'ICollection'>, <type 'IEnumerable'>
    """
    Represents a container for authentication module configuration elements. This class cannot be inherited.

    AuthenticationModuleElementCollection()
    """

    def Add(self, element):
        """
        Add(self: AuthenticationModuleElementCollection, element: AuthenticationModuleElement)

            Adds an element to the collection.

            element: The System.Net.Configuration.AuthenticationModuleElement to add to the collection.
        """
        ...
    def Clear(self):
        """
        Clear(self: AuthenticationModuleElementCollection)

            Removes all elements from the collection.
        """
        ...
    def IndexOf(self, element):
        """
        IndexOf(self: AuthenticationModuleElementCollection, element: AuthenticationModuleElement) -> int

            Returns the index of the specified configuration element.

            element: A System.Net.Configuration.AuthenticationModuleElement.

            Returns: The zero-based index of element.
        """
        ...
    def Remove(self, *__args):
        """
        Remove(self: AuthenticationModuleElementCollection, element: AuthenticationModuleElement)

            Removes the specified configuration element from the collection.

            element: The System.Net.Configuration.AuthenticationModuleElement to remove.

        Remove(self: AuthenticationModuleElementCollection, name: str)

            Removes the element with the specified key.

            name: The key of the element to remove.
        """
        ...
    def RemoveAt(self, index):
        """
        RemoveAt(self: AuthenticationModuleElementCollection, index: int)

            Removes the element at the specified index.

            index: The zero-based index of the element to remove.
        """
        ...
    def __add__(self, *args):  # cannot find CLR method
        """x.__add__(y) <==> x+y"""
        ...
    def __getitem__(self, *args):  # cannot find CLR method
        """x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y]"""
        ...
    def __setitem__(self, *args):  # cannot find CLR method
        """x.__setitem__(i, y) <==> x[i]=x.__setitem__(i, y) <==> x[i]="""
        ...
    @property
    def AddElementName(self):
        """Gets or sets the name of the System.Configuration.ConfigurationElement to associate with the add operation in the System.Configuration.ConfigurationElementCollection when overridden in a derived class."""
        ...
    @property
    def ClearElementName(self):
        """Gets or sets the name for the System.Configuration.ConfigurationElement to associate with the clear operation in the System.Configuration.ConfigurationElementCollection when overridden in a derived class."""
        ...
    @property
    def ElementName(self):
        """Gets the name used to identify this collection of elements in the configuration file when overridden in a derived class."""
        ...
    @property
    def ElementProperty(self):
        """Gets the System.Configuration.ConfigurationElementProperty object that represents the System.Configuration.ConfigurationElement object itself."""
        ...
    @property
    def EvaluationContext(self):
        """Gets the System.Configuration.ContextInformation object for the System.Configuration.ConfigurationElement object."""
        ...
    @property
    def HasContext(self):
        """Gets a value that indicates whether the System.Configuration.ConfigurationElement.CurrentConfiguration property is ll."""
        ...
    @property
    def Properties(self):
        """Gets the collection of properties."""
        ...
    @property
    def RemoveElementName(self):
        """Gets or sets the name of the System.Configuration.ConfigurationElement to associate with the remove operation in the System.Configuration.ConfigurationElementCollection when overridden in a derived class."""
        ...
    @property
    def ThrowOnDuplicate(self):
        """Gets a value indicating whether an attempt to add a duplicate System.Configuration.ConfigurationElement to the System.Configuration.ConfigurationElementCollection will cause an exception to be thrown."""
        ...

class AuthenticationModulesSection(ConfigurationSection):
    """
    Represents the configuration section for authentication modules. This class cannot be inherited.

    AuthenticationModulesSection()
    """

    @property
    def AuthenticationModules(self):
        """
        Gets the collection of authentication modules in the section.

        Get: AuthenticationModules(self: AuthenticationModulesSection) -> AuthenticationModuleElementCollection
        """
        ...
    @property
    def ElementProperty(self):
        """Gets the System.Configuration.ConfigurationElementProperty object that represents the System.Configuration.ConfigurationElement object itself."""
        ...
    @property
    def EvaluationContext(self):
        """Gets the System.Configuration.ContextInformation object for the System.Configuration.ConfigurationElement object."""
        ...
    @property
    def HasContext(self):
        """Gets a value that indicates whether the System.Configuration.ConfigurationElement.CurrentConfiguration property is ll."""
        ...
    @property
    def Properties(self): ...

class BypassElement(ConfigurationElement):
    """
    Represents the address information for resources that are not retrieved using a proxy server. This class cannot be inherited.

    BypassElement()

    BypassElement(address: str)
    """

    @staticmethod  # known case of __new__
    def __new__(cls, address=None):
        """
        __new__(cls: type)

        __new__(cls: type, address: str)
        """
        ...
    @property
    def Address(self):
        """
        Gets or sets the addresses of resources that bypass the proxy server.

        Get: Address(self: BypassElement) -> str

        Set: Address(self: BypassElement) = value
        """
        ...
    @property
    def ElementProperty(self):
        """Gets the System.Configuration.ConfigurationElementProperty object that represents the System.Configuration.ConfigurationElement object itself."""
        ...
    @property
    def EvaluationContext(self):
        """Gets the System.Configuration.ContextInformation object for the System.Configuration.ConfigurationElement object."""
        ...
    @property
    def HasContext(self):
        """Gets a value that indicates whether the System.Configuration.ConfigurationElement.CurrentConfiguration property is ll."""
        ...
    @property
    def Properties(self): ...

class BypassElementCollection(
    ConfigurationElementCollection
):  # skipped bases: <type 'ICollection'>, <type 'IEnumerable'>
    """
    Represents a container for the addresses of resources that bypass the proxy server. This class cannot be inherited.

    BypassElementCollection()
    """

    def Add(self, element):
        """
        Add(self: BypassElementCollection, element: BypassElement)

            Adds an element to the collection.

            element: The System.Net.Configuration.BypassElement to add to the collection.
        """
        ...
    def Clear(self):
        """
        Clear(self: BypassElementCollection)

            Removes all elements from the collection.
        """
        ...
    def IndexOf(self, element):
        """
        IndexOf(self: BypassElementCollection, element: BypassElement) -> int

            Returns the index of the specified configuration element.

            element: A System.Net.Configuration.BypassElement.

            Returns: The zero-based index of element.
        """
        ...
    def Remove(self, *__args):
        """
        Remove(self: BypassElementCollection, element: BypassElement)

            Removes the specified configuration element from the collection.

            element: The System.Net.Configuration.BypassElement to remove.

        Remove(self: BypassElementCollection, name: str)

            Removes the element with the specified key.

            name: The key of the element to remove.
        """
        ...
    def RemoveAt(self, index):
        """
        RemoveAt(self: BypassElementCollection, index: int)

            Removes the element at the specified index.

            index: The zero-based index of the element to remove.
        """
        ...
    def __add__(self, *args):  # cannot find CLR method
        """x.__add__(y) <==> x+y"""
        ...
    def __getitem__(self, *args):  # cannot find CLR method
        """x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y]"""
        ...
    def __setitem__(self, *args):  # cannot find CLR method
        """x.__setitem__(i, y) <==> x[i]=x.__setitem__(i, y) <==> x[i]="""
        ...
    @property
    def AddElementName(self):
        """Gets or sets the name of the System.Configuration.ConfigurationElement to associate with the add operation in the System.Configuration.ConfigurationElementCollection when overridden in a derived class."""
        ...
    @property
    def ClearElementName(self):
        """Gets or sets the name for the System.Configuration.ConfigurationElement to associate with the clear operation in the System.Configuration.ConfigurationElementCollection when overridden in a derived class."""
        ...
    @property
    def ElementName(self):
        """Gets the name used to identify this collection of elements in the configuration file when overridden in a derived class."""
        ...
    @property
    def ElementProperty(self):
        """Gets the System.Configuration.ConfigurationElementProperty object that represents the System.Configuration.ConfigurationElement object itself."""
        ...
    @property
    def EvaluationContext(self):
        """Gets the System.Configuration.ContextInformation object for the System.Configuration.ConfigurationElement object."""
        ...
    @property
    def HasContext(self):
        """Gets a value that indicates whether the System.Configuration.ConfigurationElement.CurrentConfiguration property is ll."""
        ...
    @property
    def Properties(self):
        """Gets the collection of properties."""
        ...
    @property
    def RemoveElementName(self):
        """Gets or sets the name of the System.Configuration.ConfigurationElement to associate with the remove operation in the System.Configuration.ConfigurationElementCollection when overridden in a derived class."""
        ...
    @property
    def ThrowOnDuplicate(self): ...

class ConnectionManagementElement(ConfigurationElement):
    """
    Represents the maximum number of connections to a remote computer. This class cannot be inherited.

    ConnectionManagementElement()

    ConnectionManagementElement(address: str, maxConnection: int)
    """

    @staticmethod  # known case of __new__
    def __new__(cls, address=None, maxConnection=None):
        """
        __new__(cls: type)

        __new__(cls: type, address: str, maxConnection: int)
        """
        ...
    @property
    def Address(self):
        """
        Gets or sets the address for remote computers.

        Get: Address(self: ConnectionManagementElement) -> str

        Set: Address(self: ConnectionManagementElement) = value
        """
        ...
    @property
    def ElementProperty(self):
        """Gets the System.Configuration.ConfigurationElementProperty object that represents the System.Configuration.ConfigurationElement object itself."""
        ...
    @property
    def EvaluationContext(self):
        """Gets the System.Configuration.ContextInformation object for the System.Configuration.ConfigurationElement object."""
        ...
    @property
    def HasContext(self):
        """Gets a value that indicates whether the System.Configuration.ConfigurationElement.CurrentConfiguration property is ll."""
        ...
    @property
    def MaxConnection(self):
        """
        Gets or sets the maximum number of connections that can be made to a remote computer.

        Get: MaxConnection(self: ConnectionManagementElement) -> int

        Set: MaxConnection(self: ConnectionManagementElement) = value
        """
        ...
    @property
    def Properties(self): ...

class ConnectionManagementElementCollection(
    ConfigurationElementCollection
):  # skipped bases: <type 'ICollection'>, <type 'IEnumerable'>
    """
    Represents a container for connection management configuration elements. This class cannot be inherited.

    ConnectionManagementElementCollection()
    """

    def Add(self, element):
        """
        Add(self: ConnectionManagementElementCollection, element: ConnectionManagementElement)

            Adds an element to the collection.

            element: The System.Net.Configuration.ConnectionManagementElement to add to the collection.
        """
        ...
    def Clear(self):
        """
        Clear(self: ConnectionManagementElementCollection)

            Removes all elements from the collection.
        """
        ...
    def IndexOf(self, element):
        """
        IndexOf(self: ConnectionManagementElementCollection, element: ConnectionManagementElement) -> int

            Returns the index of the specified configuration element.

            element: A System.Net.Configuration.ConnectionManagementElement.

            Returns: The zero-based index of element.
        """
        ...
    def Remove(self, *__args):
        """
        Remove(self: ConnectionManagementElementCollection, element: ConnectionManagementElement)

            Removes the specified configuration element from the collection.

            element: The System.Net.Configuration.ConnectionManagementElement to remove.

        Remove(self: ConnectionManagementElementCollection, name: str)

            Removes the element with the specified key.

            name: The key of the element to remove.
        """
        ...
    def RemoveAt(self, index):
        """
        RemoveAt(self: ConnectionManagementElementCollection, index: int)

            Removes the element at the specified index.

            index: The zero-based index of the element to remove.
        """
        ...
    def __add__(self, *args):  # cannot find CLR method
        """x.__add__(y) <==> x+y"""
        ...
    def __getitem__(self, *args):  # cannot find CLR method
        """x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y]"""
        ...
    def __setitem__(self, *args):  # cannot find CLR method
        """x.__setitem__(i, y) <==> x[i]=x.__setitem__(i, y) <==> x[i]="""
        ...
    @property
    def AddElementName(self):
        """Gets or sets the name of the System.Configuration.ConfigurationElement to associate with the add operation in the System.Configuration.ConfigurationElementCollection when overridden in a derived class."""
        ...
    @property
    def ClearElementName(self):
        """Gets or sets the name for the System.Configuration.ConfigurationElement to associate with the clear operation in the System.Configuration.ConfigurationElementCollection when overridden in a derived class."""
        ...
    @property
    def ElementName(self):
        """Gets the name used to identify this collection of elements in the configuration file when overridden in a derived class."""
        ...
    @property
    def ElementProperty(self):
        """Gets the System.Configuration.ConfigurationElementProperty object that represents the System.Configuration.ConfigurationElement object itself."""
        ...
    @property
    def EvaluationContext(self):
        """Gets the System.Configuration.ContextInformation object for the System.Configuration.ConfigurationElement object."""
        ...
    @property
    def HasContext(self):
        """Gets a value that indicates whether the System.Configuration.ConfigurationElement.CurrentConfiguration property is ll."""
        ...
    @property
    def Properties(self):
        """Gets the collection of properties."""
        ...
    @property
    def RemoveElementName(self):
        """Gets or sets the name of the System.Configuration.ConfigurationElement to associate with the remove operation in the System.Configuration.ConfigurationElementCollection when overridden in a derived class."""
        ...
    @property
    def ThrowOnDuplicate(self):
        """Gets a value indicating whether an attempt to add a duplicate System.Configuration.ConfigurationElement to the System.Configuration.ConfigurationElementCollection will cause an exception to be thrown."""
        ...

class ConnectionManagementSection(ConfigurationSection):
    """
    Represents the configuration section for connection management. This class cannot be inherited.

    ConnectionManagementSection()
    """

    @property
    def ConnectionManagement(self):
        """
        Gets the collection of connection management objects in the section.

        Get: ConnectionManagement(self: ConnectionManagementSection) -> ConnectionManagementElementCollection
        """
        ...
    @property
    def ElementProperty(self):
        """Gets the System.Configuration.ConfigurationElementProperty object that represents the System.Configuration.ConfigurationElement object itself."""
        ...
    @property
    def EvaluationContext(self):
        """Gets the System.Configuration.ContextInformation object for the System.Configuration.ConfigurationElement object."""
        ...
    @property
    def HasContext(self):
        """Gets a value that indicates whether the System.Configuration.ConfigurationElement.CurrentConfiguration property is ll."""
        ...
    @property
    def Properties(self): ...

class DefaultProxySection(ConfigurationSection):
    """
    Represents the configuration section for Web proxy server usage. This class cannot be inherited.

    DefaultProxySection()
    """

    @property
    def BypassList(self):
        """
        Gets the collection of resources that are not obtained using the Web proxy server.

        Get: BypassList(self: DefaultProxySection) -> BypassElementCollection
        """
        ...
    @property
    def ElementProperty(self):
        """Gets the System.Configuration.ConfigurationElementProperty object that represents the System.Configuration.ConfigurationElement object itself."""
        ...
    @property
    def Enabled(self):
        """
        Gets or sets whether a Web proxy is used.

        Get: Enabled(self: DefaultProxySection) -> bool

        Set: Enabled(self: DefaultProxySection) = value
        """
        ...
    @property
    def EvaluationContext(self):
        """Gets the System.Configuration.ContextInformation object for the System.Configuration.ConfigurationElement object."""
        ...
    @property
    def HasContext(self):
        """Gets a value that indicates whether the System.Configuration.ConfigurationElement.CurrentConfiguration property is ll."""
        ...
    @property
    def Module(self):
        """
        Gets the type information for a custom Web proxy implementation.

        Get: Module(self: DefaultProxySection) -> ModuleElement
        """
        ...
    @property
    def Properties(self): ...
    @property
    def Proxy(self):
        """
        Gets the URI that identifies the Web proxy server to use.

        Get: Proxy(self: DefaultProxySection) -> ProxyElement
        """
        ...
    @property
    def UseDefaultCredentials(self):
        """
        Gets or sets whether default credentials are to be used to access a Web proxy server.

        Get: UseDefaultCredentials(self: DefaultProxySection) -> bool

        Set: UseDefaultCredentials(self: DefaultProxySection) = value
        """
        ...

class FtpCachePolicyElement(ConfigurationElement):
    """
    Represents the default FTP cache policy for network resources. This class cannot be inherited.

    FtpCachePolicyElement()
    """

    @property
    def ElementProperty(self):
        """Gets the System.Configuration.ConfigurationElementProperty object that represents the System.Configuration.ConfigurationElement object itself."""
        ...
    @property
    def EvaluationContext(self):
        """Gets the System.Configuration.ContextInformation object for the System.Configuration.ConfigurationElement object."""
        ...
    @property
    def HasContext(self):
        """Gets a value that indicates whether the System.Configuration.ConfigurationElement.CurrentConfiguration property is ll."""
        ...
    @property
    def PolicyLevel(self):
        """
        Gets or sets FTP caching behavior for the local machine.

        Get: PolicyLevel(self: FtpCachePolicyElement) -> RequestCacheLevel

        Set: PolicyLevel(self: FtpCachePolicyElement) = value
        """
        ...
    @property
    def Properties(self): ...

class HttpCachePolicyElement(ConfigurationElement):
    """
    Represents the default HTTP cache policy for network resources. This class cannot be inherited.

    HttpCachePolicyElement()
    """

    @property
    def ElementProperty(self):
        """Gets the System.Configuration.ConfigurationElementProperty object that represents the System.Configuration.ConfigurationElement object itself."""
        ...
    @property
    def EvaluationContext(self):
        """Gets the System.Configuration.ContextInformation object for the System.Configuration.ConfigurationElement object."""
        ...
    @property
    def HasContext(self):
        """Gets a value that indicates whether the System.Configuration.ConfigurationElement.CurrentConfiguration property is ll."""
        ...
    @property
    def MaximumAge(self):
        """
        Gets or sets the maximum age permitted for a resource returned from the cache.

        Get: MaximumAge(self: HttpCachePolicyElement) -> TimeSpan

        Set: MaximumAge(self: HttpCachePolicyElement) = value
        """
        ...
    @property
    def MaximumStale(self):
        """
        Gets or sets the maximum staleness value permitted for a resource returned from the cache.

        Get: MaximumStale(self: HttpCachePolicyElement) -> TimeSpan

        Set: MaximumStale(self: HttpCachePolicyElement) = value
        """
        ...
    @property
    def MinimumFresh(self):
        """
        Gets or sets the minimum freshness permitted for a resource returned from the cache.

        Get: MinimumFresh(self: HttpCachePolicyElement) -> TimeSpan

        Set: MinimumFresh(self: HttpCachePolicyElement) = value
        """
        ...
    @property
    def PolicyLevel(self):
        """
        Gets or sets HTTP caching behavior for the local machine.

        Get: PolicyLevel(self: HttpCachePolicyElement) -> HttpRequestCacheLevel

        Set: PolicyLevel(self: HttpCachePolicyElement) = value
        """
        ...
    @property
    def Properties(self): ...

class HttpListenerElement(ConfigurationElement):
    """
    Represents the HttpListener element in the configuration file. This class cannot be inherited.

    HttpListenerElement()
    """

    @property
    def ElementProperty(self):
        """Gets the System.Configuration.ConfigurationElementProperty object that represents the System.Configuration.ConfigurationElement object itself."""
        ...
    @property
    def EvaluationContext(self):
        """Gets the System.Configuration.ContextInformation object for the System.Configuration.ConfigurationElement object."""
        ...
    @property
    def HasContext(self):
        """Gets a value that indicates whether the System.Configuration.ConfigurationElement.CurrentConfiguration property is ll."""
        ...
    @property
    def Properties(self): ...
    @property
    def Timeouts(self):
        """
        Gets the default timeout elements used for an System.Net.HttpListener object.

        Get: Timeouts(self: HttpListenerElement) -> HttpListenerTimeoutsElement
        """
        ...
    @property
    def UnescapeRequestUrl(self):
        """
        Gets a value that indicates if System.Net.HttpListener uses the raw unescaped URI instead of the converted URI.

        Get: UnescapeRequestUrl(self: HttpListenerElement) -> bool
        """
        ...

class HttpListenerTimeoutsElement(ConfigurationElement):
    """
    Represents the System.Net.HttpListener timeouts element in the configuration file. This class cannot be inherited.

    HttpListenerTimeoutsElement()
    """

    @property
    def DrainEntityBody(self):
        """
        Gets the time, in seconds, allowed for the System.Net.HttpListener  to drain the entity body on a Keep-Alive connection.

        Get: DrainEntityBody(self: HttpListenerTimeoutsElement) -> TimeSpan
        """
        ...
    @property
    def ElementProperty(self):
        """Gets the System.Configuration.ConfigurationElementProperty object that represents the System.Configuration.ConfigurationElement object itself."""
        ...
    @property
    def EntityBody(self):
        """
        Gets the time, in seconds, allowed for the request entity body to arrive.

        Get: EntityBody(self: HttpListenerTimeoutsElement) -> TimeSpan
        """
        ...
    @property
    def EvaluationContext(self):
        """Gets the System.Configuration.ContextInformation object for the System.Configuration.ConfigurationElement object."""
        ...
    @property
    def HasContext(self):
        """Gets a value that indicates whether the System.Configuration.ConfigurationElement.CurrentConfiguration property is ll."""
        ...
    @property
    def HeaderWait(self):
        """
        Gets the time, in seconds, allowed for the System.Net.HttpListener to parse the request header.

        Get: HeaderWait(self: HttpListenerTimeoutsElement) -> TimeSpan
        """
        ...
    @property
    def IdleConnection(self):
        """
        Gets the time, in seconds, allowed for an idle connection.

        Get: IdleConnection(self: HttpListenerTimeoutsElement) -> TimeSpan
        """
        ...
    @property
    def MinSendBytesPerSecond(self):
        """
        Gets the minimum send rate, in bytes-per-second, for the response.

        Get: MinSendBytesPerSecond(self: HttpListenerTimeoutsElement) -> Int64
        """
        ...
    @property
    def Properties(self): ...
    @property
    def RequestQueue(self):
        """
        Gets the time, in seconds, allowed for the request to remain in the request queue before the System.Net.HttpListener picks it up.

        Get: RequestQueue(self: HttpListenerTimeoutsElement) -> TimeSpan
        """
        ...

class HttpWebRequestElement(ConfigurationElement):
    """
    Represents the maximum length for response headers. This class cannot be inherited.

    HttpWebRequestElement()
    """

    @property
    def ElementProperty(self):
        """Gets the System.Configuration.ConfigurationElementProperty object that represents the System.Configuration.ConfigurationElement object itself."""
        ...
    @property
    def EvaluationContext(self):
        """Gets the System.Configuration.ContextInformation object for the System.Configuration.ConfigurationElement object."""
        ...
    @property
    def HasContext(self):
        """Gets a value that indicates whether the System.Configuration.ConfigurationElement.CurrentConfiguration property is ll."""
        ...
    @property
    def MaximumErrorResponseLength(self):
        """
        Gets or sets the maximum allowed length of an error response.

        Get: MaximumErrorResponseLength(self: HttpWebRequestElement) -> int

        Set: MaximumErrorResponseLength(self: HttpWebRequestElement) = value
        """
        ...
    @property
    def MaximumResponseHeadersLength(self):
        """
        Gets or sets the maximum allowed length of the response headers.

        Get: MaximumResponseHeadersLength(self: HttpWebRequestElement) -> int

        Set: MaximumResponseHeadersLength(self: HttpWebRequestElement) = value
        """
        ...
    @property
    def MaximumUnauthorizedUploadLength(self):
        """
        Gets or sets the maximum length of an upload in response to an unauthorized error code.

        Get: MaximumUnauthorizedUploadLength(self: HttpWebRequestElement) -> int

        Set: MaximumUnauthorizedUploadLength(self: HttpWebRequestElement) = value
        """
        ...
    @property
    def Properties(self): ...
    @property
    def UseUnsafeHeaderParsing(self):
        """
        Setting this property ignores validation errors that occur during HTTP parsing.

        Get: UseUnsafeHeaderParsing(self: HttpWebRequestElement) -> bool

        Set: UseUnsafeHeaderParsing(self: HttpWebRequestElement) = value
        """
        ...

class Ipv6Element(ConfigurationElement):
    """
    Determines whether Internet Protocol version 6 is enabled on the local computer. This class cannot be inherited.

    Ipv6Element()
    """

    @property
    def ElementProperty(self):
        """Gets the System.Configuration.ConfigurationElementProperty object that represents the System.Configuration.ConfigurationElement object itself."""
        ...
    @property
    def Enabled(self):
        """
        Gets or sets a Boolean value that indicates whether Internet Protocol version 6 is enabled on the local computer.

        Get: Enabled(self: Ipv6Element) -> bool

        Set: Enabled(self: Ipv6Element) = value
        """
        ...
    @property
    def EvaluationContext(self):
        """Gets the System.Configuration.ContextInformation object for the System.Configuration.ConfigurationElement object."""
        ...
    @property
    def HasContext(self):
        """Gets a value that indicates whether the System.Configuration.ConfigurationElement.CurrentConfiguration property is ll."""
        ...
    @property
    def Properties(self): ...

class MailSettingsSectionGroup(ConfigurationSectionGroup):
    """
    Initializes a new instance of the System.Net.Configuration.MailSettingsSectionGroup class.

    MailSettingsSectionGroup()
    """

    @property
    def Smtp(self):
        """
        Gets the SMTP settings for the local computer.

        Get: Smtp(self: MailSettingsSectionGroup) -> SmtpSection
        """
        ...

class ModuleElement(ConfigurationElement):
    """
    Represents the type information for a custom System.Net.IWebProxy module. This class cannot be inherited.

    ModuleElement()
    """

    @property
    def ElementProperty(self):
        """Gets the System.Configuration.ConfigurationElementProperty object that represents the System.Configuration.ConfigurationElement object itself."""
        ...
    @property
    def EvaluationContext(self):
        """Gets the System.Configuration.ContextInformation object for the System.Configuration.ConfigurationElement object."""
        ...
    @property
    def HasContext(self):
        """Gets a value that indicates whether the System.Configuration.ConfigurationElement.CurrentConfiguration property is ll."""
        ...
    @property
    def Properties(self): ...
    @property
    def Type(self):
        """
        Gets or sets the type and assembly information for the current instance.

        Get: Type(self: ModuleElement) -> str

        Set: Type(self: ModuleElement) = value
        """
        ...

class NetSectionGroup(ConfigurationSectionGroup):
    """
    Gets the section group information for the networking namespaces. This class cannot be inherited.

    NetSectionGroup()
    """

    @staticmethod
    def GetSectionGroup(config):
        """
        GetSectionGroup(config: Configuration) -> NetSectionGroup

            Gets the stem.Net configuration section group from the specified configuration file.

            config: A System.Configuration.Configuration that represents a configuration file.

            Returns: A System.Net.Configuration.NetSectionGroup that represents the stem.Net settings in config.
        """
        ...
    @property
    def AuthenticationModules(self):
        """
        Gets the configuration section containing the authentication modules registered for the local computer.

        Get: AuthenticationModules(self: NetSectionGroup) -> AuthenticationModulesSection
        """
        ...
    @property
    def ConnectionManagement(self):
        """
        Gets the configuration section containing the connection management settings for the local computer.

        Get: ConnectionManagement(self: NetSectionGroup) -> ConnectionManagementSection
        """
        ...
    @property
    def DefaultProxy(self):
        """
        Gets the configuration section containing the default Web proxy server settings for the local computer.

        Get: DefaultProxy(self: NetSectionGroup) -> DefaultProxySection
        """
        ...
    @property
    def MailSettings(self):
        """
        Gets the configuration section containing the SMTP client e-mail settings for the local computer.

        Get: MailSettings(self: NetSectionGroup) -> MailSettingsSectionGroup
        """
        ...
    @property
    def RequestCaching(self):
        """
        Gets the configuration section containing the cache configuration settings for the local computer.

        Get: RequestCaching(self: NetSectionGroup) -> RequestCachingSection
        """
        ...
    @property
    def Settings(self):
        """
        Gets the configuration section containing the network settings for the local computer.

        Get: Settings(self: NetSectionGroup) -> SettingsSection
        """
        ...
    @property
    def WebRequestModules(self):
        """
        Gets the configuration section containing the modules registered for use with the System.Net.WebRequest class.

        Get: WebRequestModules(self: NetSectionGroup) -> WebRequestModulesSection
        """
        ...

class PerformanceCountersElement(ConfigurationElement):
    """
    Represents the performance counter element in the stem.Net configuration file that determines whether networking performance counters are enabled. This class cannot be inherited.

    PerformanceCountersElement()
    """

    @property
    def ElementProperty(self):
        """Gets the System.Configuration.ConfigurationElementProperty object that represents the System.Configuration.ConfigurationElement object itself."""
        ...
    @property
    def Enabled(self):
        """
        Gets or sets whether performance counters are enabled.

        Get: Enabled(self: PerformanceCountersElement) -> bool

        Set: Enabled(self: PerformanceCountersElement) = value
        """
        ...
    @property
    def EvaluationContext(self):
        """Gets the System.Configuration.ContextInformation object for the System.Configuration.ConfigurationElement object."""
        ...
    @property
    def HasContext(self):
        """Gets a value that indicates whether the System.Configuration.ConfigurationElement.CurrentConfiguration property is ll."""
        ...
    @property
    def Properties(self): ...

class ProxyElement(ConfigurationElement):
    """
    Identifies the configuration settings for Web proxy server. This class cannot be inherited.

    ProxyElement()
    """

    def AutoDetectValues(self, *args):  # cannot find CLR method
        """enum AutoDetectValues, values: False (0), True (1), Unspecified (-1)"""
        ...
    def BypassOnLocalValues(self, *args):  # cannot find CLR method
        """enum BypassOnLocalValues, values: False (0), True (1), Unspecified (-1)"""
        ...
    def UseSystemDefaultValues(self, *args):  # cannot find CLR method
        """enum UseSystemDefaultValues, values: False (0), True (1), Unspecified (-1)"""
        ...
    @property
    def AutoDetect(self):
        """
        Gets or sets an System.Net.Configuration.ProxyElement.AutoDetectValues value that controls whether the Web proxy is automatically detected.

        Get: AutoDetect(self: ProxyElement) -> AutoDetectValues

        Set: AutoDetect(self: ProxyElement) = value
        """
        ...
    @property
    def BypassOnLocal(self):
        """
        Gets or sets a value that indicates whether local resources are retrieved by using a Web proxy server.

        Get: BypassOnLocal(self: ProxyElement) -> BypassOnLocalValues

        Set: BypassOnLocal(self: ProxyElement) = value
        """
        ...
    @property
    def ElementProperty(self):
        """Gets the System.Configuration.ConfigurationElementProperty object that represents the System.Configuration.ConfigurationElement object itself."""
        ...
    @property
    def EvaluationContext(self):
        """Gets the System.Configuration.ContextInformation object for the System.Configuration.ConfigurationElement object."""
        ...
    @property
    def HasContext(self):
        """Gets a value that indicates whether the System.Configuration.ConfigurationElement.CurrentConfiguration property is ll."""
        ...
    @property
    def Properties(self): ...
    @property
    def ProxyAddress(self):
        """
        Gets or sets the URI that identifies the Web proxy server to use.

        Get: ProxyAddress(self: ProxyElement) -> Uri

        Set: ProxyAddress(self: ProxyElement) = value
        """
        ...
    @property
    def ScriptLocation(self):
        """
        Gets or sets an System.Uri value that specifies the location of the automatic proxy detection script.

        Get: ScriptLocation(self: ProxyElement) -> Uri

        Set: ScriptLocation(self: ProxyElement) = value
        """
        ...
    @property
    def UseSystemDefault(self):
        """
        Gets or sets a System.Boolean value that controls whether the Internet Explorer Web proxy settings are used.

        Get: UseSystemDefault(self: ProxyElement) -> UseSystemDefaultValues

        Set: UseSystemDefault(self: ProxyElement) = value
        """
        ...
    AutoDetectValues = None
    BypassOnLocalValues = None
    UseSystemDefaultValues = None

class RequestCachingSection(ConfigurationSection):
    """
    Represents the configuration section for cache behavior. This class cannot be inherited.

    RequestCachingSection()
    """

    @property
    def DefaultFtpCachePolicy(self):
        """
        Gets the default FTP caching behavior for the local computer.

        Get: DefaultFtpCachePolicy(self: RequestCachingSection) -> FtpCachePolicyElement
        """
        ...
    @property
    def DefaultHttpCachePolicy(self):
        """
        Gets the default caching behavior for the local computer.

        Get: DefaultHttpCachePolicy(self: RequestCachingSection) -> HttpCachePolicyElement
        """
        ...
    @property
    def DefaultPolicyLevel(self):
        """
        Gets or sets the default cache policy level.

        Get: DefaultPolicyLevel(self: RequestCachingSection) -> RequestCacheLevel

        Set: DefaultPolicyLevel(self: RequestCachingSection) = value
        """
        ...
    @property
    def DisableAllCaching(self):
        """
        Gets or sets a Boolean value that enables caching on the local computer.

        Get: DisableAllCaching(self: RequestCachingSection) -> bool

        Set: DisableAllCaching(self: RequestCachingSection) = value
        """
        ...
    @property
    def ElementProperty(self):
        """Gets the System.Configuration.ConfigurationElementProperty object that represents the System.Configuration.ConfigurationElement object itself."""
        ...
    @property
    def EvaluationContext(self):
        """Gets the System.Configuration.ContextInformation object for the System.Configuration.ConfigurationElement object."""
        ...
    @property
    def HasContext(self):
        """Gets a value that indicates whether the System.Configuration.ConfigurationElement.CurrentConfiguration property is ll."""
        ...
    @property
    def IsPrivateCache(self):
        """
        Gets or sets a Boolean value that indicates whether the local computer cache is private.

        Get: IsPrivateCache(self: RequestCachingSection) -> bool

        Set: IsPrivateCache(self: RequestCachingSection) = value
        """
        ...
    @property
    def Properties(self): ...
    @property
    def UnspecifiedMaximumAge(self):
        """
        Gets or sets a value used as the maximum age for cached resources that do not have expiration information.

        Get: UnspecifiedMaximumAge(self: RequestCachingSection) -> TimeSpan

        Set: UnspecifiedMaximumAge(self: RequestCachingSection) = value
        """
        ...

class ServicePointManagerElement(ConfigurationElement):
    """
    Represents the default settings used to create connections to a remote computer. This class cannot be inherited.

    ServicePointManagerElement()
    """

    @property
    def CheckCertificateName(self):
        """
        Gets or sets a Boolean value that controls checking host name information in an X509 certificate.

        Get: CheckCertificateName(self: ServicePointManagerElement) -> bool

        Set: CheckCertificateName(self: ServicePointManagerElement) = value
        """
        ...
    @property
    def CheckCertificateRevocationList(self):
        """
        Gets or sets a Boolean value that indicates whether the certificate is checked against the certificate authority revocation list.

        Get: CheckCertificateRevocationList(self: ServicePointManagerElement) -> bool

        Set: CheckCertificateRevocationList(self: ServicePointManagerElement) = value
        """
        ...
    @property
    def DnsRefreshTimeout(self):
        """
        Gets or sets the amount of time after which address information is refreshed.

        Get: DnsRefreshTimeout(self: ServicePointManagerElement) -> int

        Set: DnsRefreshTimeout(self: ServicePointManagerElement) = value
        """
        ...
    @property
    def ElementProperty(self):
        """Gets the System.Configuration.ConfigurationElementProperty object that represents the System.Configuration.ConfigurationElement object itself."""
        ...
    @property
    def EnableDnsRoundRobin(self):
        """
        Gets or sets a Boolean value that controls using different IP addresses on connections to the same server.

        Get: EnableDnsRoundRobin(self: ServicePointManagerElement) -> bool

        Set: EnableDnsRoundRobin(self: ServicePointManagerElement) = value
        """
        ...
    @property
    def EncryptionPolicy(self):
        """
        Gets or sets the System.Net.Security.EncryptionPolicy to use.

        Get: EncryptionPolicy(self: ServicePointManagerElement) -> EncryptionPolicy

        Set: EncryptionPolicy(self: ServicePointManagerElement) = value
        """
        ...
    @property
    def EvaluationContext(self):
        """Gets the System.Configuration.ContextInformation object for the System.Configuration.ConfigurationElement object."""
        ...
    @property
    def Expect100Continue(self):
        """
        Gets or sets a Boolean value that determines whether 100-Continue behavior is used.

        Get: Expect100Continue(self: ServicePointManagerElement) -> bool

        Set: Expect100Continue(self: ServicePointManagerElement) = value
        """
        ...
    @property
    def HasContext(self):
        """Gets a value that indicates whether the System.Configuration.ConfigurationElement.CurrentConfiguration property is ll."""
        ...
    @property
    def Properties(self): ...
    @property
    def UseNagleAlgorithm(self):
        """
        Gets or sets a Boolean value that determines whether the Nagle algorithm is used.

        Get: UseNagleAlgorithm(self: ServicePointManagerElement) -> bool

        Set: UseNagleAlgorithm(self: ServicePointManagerElement) = value
        """
        ...

class SettingsSection(ConfigurationSection):
    """
    Represents the configuration section for sockets, IPv6, response headers, and service points. This class cannot be inherited.

    SettingsSection()
    """

    @property
    def ElementProperty(self):
        """Gets the System.Configuration.ConfigurationElementProperty object that represents the System.Configuration.ConfigurationElement object itself."""
        ...
    @property
    def EvaluationContext(self):
        """Gets the System.Configuration.ContextInformation object for the System.Configuration.ConfigurationElement object."""
        ...
    @property
    def HasContext(self):
        """Gets a value that indicates whether the System.Configuration.ConfigurationElement.CurrentConfiguration property is ll."""
        ...
    @property
    def HttpListener(self):
        """
        Gets the configuration element that controls the settings used by an System.Net.HttpListener object.

        Get: HttpListener(self: SettingsSection) -> HttpListenerElement
        """
        ...
    @property
    def HttpWebRequest(self):
        """
        Gets the configuration element that controls the settings used by an System.Net.HttpWebRequest object.

        Get: HttpWebRequest(self: SettingsSection) -> HttpWebRequestElement
        """
        ...
    @property
    def Ipv6(self):
        """
        Gets the configuration element that enables Internet Protocol version 6 (IPv6).

        Get: Ipv6(self: SettingsSection) -> Ipv6Element
        """
        ...
    @property
    def PerformanceCounters(self):
        """
        Gets the configuration element that controls whether network performance counters are enabled.

        Get: PerformanceCounters(self: SettingsSection) -> PerformanceCountersElement
        """
        ...
    @property
    def Properties(self): ...
    @property
    def ServicePointManager(self):
        """
        Gets the configuration element that controls settings for connections to remote host computers.

        Get: ServicePointManager(self: SettingsSection) -> ServicePointManagerElement
        """
        ...
    @property
    def Socket(self):
        """
        Gets the configuration element that controls settings for sockets.

        Get: Socket(self: SettingsSection) -> SocketElement
        """
        ...
    @property
    def WebProxyScript(self):
        """
        Gets the configuration element that controls the execution timeout and download timeout of Web proxy scripts.

        Get: WebProxyScript(self: SettingsSection) -> WebProxyScriptElement
        """
        ...
    @property
    def WebUtility(self):
        """
        Gets the configuration element that controls the settings used by an System.Net.WebUtility object.

        Get: WebUtility(self: SettingsSection) -> WebUtilityElement
        """
        ...
    @property
    def WindowsAuthentication(self):
        """Get: WindowsAuthentication(self: SettingsSection) -> WindowsAuthenticationElement"""
        ...

class SmtpNetworkElement(ConfigurationElement):
    """
    Represents the network element in the SMTP configuration file. This class cannot be inherited.

    SmtpNetworkElement()
    """

    @property
    def ClientDomain(self):
        """
        Gets or sets the client domain name used in the initial SMTP protocol request to connect to an SMTP mail server.

        Get: ClientDomain(self: SmtpNetworkElement) -> str

        Set: ClientDomain(self: SmtpNetworkElement) = value
        """
        ...
    @property
    def DefaultCredentials(self):
        """
        Determines whether or not default user credentials are used to access an SMTP server. The default value is lse.

        Get: DefaultCredentials(self: SmtpNetworkElement) -> bool

        Set: DefaultCredentials(self: SmtpNetworkElement) = value
        """
        ...
    @property
    def ElementProperty(self):
        """Gets the System.Configuration.ConfigurationElementProperty object that represents the System.Configuration.ConfigurationElement object itself."""
        ...
    @property
    def EnableSsl(self):
        """
        Gets or sets whether SSL is used to access an SMTP mail server. The default value is lse.

        Get: EnableSsl(self: SmtpNetworkElement) -> bool

        Set: EnableSsl(self: SmtpNetworkElement) = value
        """
        ...
    @property
    def EvaluationContext(self):
        """Gets the System.Configuration.ContextInformation object for the System.Configuration.ConfigurationElement object."""
        ...
    @property
    def HasContext(self):
        """Gets a value that indicates whether the System.Configuration.ConfigurationElement.CurrentConfiguration property is ll."""
        ...
    @property
    def Host(self):
        """
        Gets or sets the name of the SMTP server.

        Get: Host(self: SmtpNetworkElement) -> str

        Set: Host(self: SmtpNetworkElement) = value
        """
        ...
    @property
    def Password(self):
        """
        Gets or sets the user password to use to connect to an SMTP mail server.

        Get: Password(self: SmtpNetworkElement) -> str

        Set: Password(self: SmtpNetworkElement) = value
        """
        ...
    @property
    def Port(self):
        """
        Gets or sets the port that SMTP clients use to connect to an SMTP mail server. The default value is 25.

        Get: Port(self: SmtpNetworkElement) -> int

        Set: Port(self: SmtpNetworkElement) = value
        """
        ...
    @property
    def Properties(self): ...
    @property
    def TargetName(self):
        """
        Gets or sets the Service Provider Name (SPN) to use for authentication when using extended protection to connect to an SMTP mail server.

        Get: TargetName(self: SmtpNetworkElement) -> str

        Set: TargetName(self: SmtpNetworkElement) = value
        """
        ...
    @property
    def UserName(self):
        """
        Gets or sets the user name to connect to an SMTP mail server.

        Get: UserName(self: SmtpNetworkElement) -> str

        Set: UserName(self: SmtpNetworkElement) = value
        """
        ...

class SmtpSection(ConfigurationSection):
    """
    Represents the SMTP section in the stem.Net configuration file.

    SmtpSection()
    """

    @property
    def DeliveryFormat(self):
        """
        Gets or sets the delivery format to use for sending outgoing e-mail using the Simple Mail Transport Protocol (SMTP).

        Get: DeliveryFormat(self: SmtpSection) -> SmtpDeliveryFormat

        Set: DeliveryFormat(self: SmtpSection) = value
        """
        ...
    @property
    def DeliveryMethod(self):
        """
        Gets or sets the Simple Mail Transport Protocol (SMTP) delivery method. The default delivery method is System.Net.Mail.SmtpDeliveryMethod.Network.

        Get: DeliveryMethod(self: SmtpSection) -> SmtpDeliveryMethod

        Set: DeliveryMethod(self: SmtpSection) = value
        """
        ...
    @property
    def ElementProperty(self):
        """Gets the System.Configuration.ConfigurationElementProperty object that represents the System.Configuration.ConfigurationElement object itself."""
        ...
    @property
    def EvaluationContext(self):
        """Gets the System.Configuration.ContextInformation object for the System.Configuration.ConfigurationElement object."""
        ...
    @property
    def From(self):
        """
        Gets or sets the default value that indicates who the email message is from.

        Get: From(self: SmtpSection) -> str

        Set: From(self: SmtpSection) = value
        """
        ...
    @property
    def HasContext(self):
        """Gets a value that indicates whether the System.Configuration.ConfigurationElement.CurrentConfiguration property is ll."""
        ...
    @property
    def Network(self):
        """
        Gets the configuration element that controls the network settings used by the Simple Mail Transport Protocol (SMTP). file.System.Net.Configuration.SmtpNetworkElement.

        Get: Network(self: SmtpSection) -> SmtpNetworkElement
        """
        ...
    @property
    def Properties(self): ...
    @property
    def SpecifiedPickupDirectory(self):
        """
        Gets the pickup directory that will be used by the SMPT client.

        Get: SpecifiedPickupDirectory(self: SmtpSection) -> SmtpSpecifiedPickupDirectoryElement
        """
        ...

class SmtpSpecifiedPickupDirectoryElement(ConfigurationElement):
    """
    Represents an SMTP pickup directory configuration element.

    SmtpSpecifiedPickupDirectoryElement()
    """

    @property
    def ElementProperty(self):
        """Gets the System.Configuration.ConfigurationElementProperty object that represents the System.Configuration.ConfigurationElement object itself."""
        ...
    @property
    def EvaluationContext(self):
        """Gets the System.Configuration.ContextInformation object for the System.Configuration.ConfigurationElement object."""
        ...
    @property
    def HasContext(self):
        """Gets a value that indicates whether the System.Configuration.ConfigurationElement.CurrentConfiguration property is ll."""
        ...
    @property
    def PickupDirectoryLocation(self):
        """
        Gets or sets the folder where applications save mail messages to be processed by the SMTP server.

        Get: PickupDirectoryLocation(self: SmtpSpecifiedPickupDirectoryElement) -> str

        Set: PickupDirectoryLocation(self: SmtpSpecifiedPickupDirectoryElement) = value
        """
        ...
    @property
    def Properties(self): ...

class SocketElement(ConfigurationElement):
    """
    Represents information used to configure System.Net.Sockets.Socket objects. This class cannot be inherited.

    SocketElement()
    """

    @property
    def AlwaysUseCompletionPortsForAccept(self):
        """
        Gets or sets a Boolean value that specifies whether completion ports are used when accepting connections.

        Get: AlwaysUseCompletionPortsForAccept(self: SocketElement) -> bool

        Set: AlwaysUseCompletionPortsForAccept(self: SocketElement) = value
        """
        ...
    @property
    def AlwaysUseCompletionPortsForConnect(self):
        """
        Gets or sets a Boolean value that specifies whether completion ports are used when making connections.

        Get: AlwaysUseCompletionPortsForConnect(self: SocketElement) -> bool

        Set: AlwaysUseCompletionPortsForConnect(self: SocketElement) = value
        """
        ...
    @property
    def ElementProperty(self):
        """Gets the System.Configuration.ConfigurationElementProperty object that represents the System.Configuration.ConfigurationElement object itself."""
        ...
    @property
    def EvaluationContext(self):
        """Gets the System.Configuration.ContextInformation object for the System.Configuration.ConfigurationElement object."""
        ...
    @property
    def HasContext(self):
        """Gets a value that indicates whether the System.Configuration.ConfigurationElement.CurrentConfiguration property is ll."""
        ...
    @property
    def IPProtectionLevel(self):
        """
        Gets or sets a value that specifies the default System.Net.Sockets.IPProtectionLevel to use for a socket.

        Get: IPProtectionLevel(self: SocketElement) -> IPProtectionLevel

        Set: IPProtectionLevel(self: SocketElement) = value
        """
        ...
    @property
    def Properties(self): ...

class UnicodeDecodingConformance(
    Enum
):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Controls how Unicode characters are interpreted by the erload:System.Net.WebUtility.HtmlDecode methods.

    enum UnicodeDecodingConformance, values: Auto (0), Compat (2), Loose (3), Strict (1)
    """

    Auto = None
    Compat = None
    Loose = None
    Strict = None
    value__ = None

class UnicodeEncodingConformance(
    Enum
):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Controls how Unicode characters are output by the erload:System.Net.WebUtility.HtmlEncode methods.

    enum UnicodeEncodingConformance, values: Auto (0), Compat (2), Strict (1)
    """

    Auto = None
    Compat = None
    Strict = None
    value__ = None

class WebProxyScriptElement(ConfigurationElement):
    """
    Represents information used to configure Web proxy scripts. This class cannot be inherited.

    WebProxyScriptElement()
    """

    @property
    def AutoConfigUrlRetryInterval(self):
        """
        Get: AutoConfigUrlRetryInterval(self: WebProxyScriptElement) -> int

        Set: AutoConfigUrlRetryInterval(self: WebProxyScriptElement) = value
        """
        ...
    @property
    def DownloadTimeout(self):
        """
        Gets or sets the Web proxy script download timeout using the format hours:minutes:seconds.

        Get: DownloadTimeout(self: WebProxyScriptElement) -> TimeSpan

        Set: DownloadTimeout(self: WebProxyScriptElement) = value
        """
        ...
    @property
    def ElementProperty(self):
        """Gets the System.Configuration.ConfigurationElementProperty object that represents the System.Configuration.ConfigurationElement object itself."""
        ...
    @property
    def EvaluationContext(self):
        """Gets the System.Configuration.ContextInformation object for the System.Configuration.ConfigurationElement object."""
        ...
    @property
    def HasContext(self):
        """Gets a value that indicates whether the System.Configuration.ConfigurationElement.CurrentConfiguration property is ll."""
        ...
    @property
    def Properties(self): ...

class WebRequestModuleElement(ConfigurationElement):
    """
    Represents a URI prefix and the associated class that handles creating Web requests for the prefix. This class cannot be inherited.

    WebRequestModuleElement()

    WebRequestModuleElement(prefix: str, type: str)

    WebRequestModuleElement(prefix: str, type: Type)
    """

    @staticmethod  # known case of __new__
    def __new__(cls, prefix=None, type=None):
        """
        __new__(cls: type)

        __new__(cls: type, prefix: str, type: str)

        __new__(cls: type, prefix: str, type: Type)
        """
        ...
    @property
    def ElementProperty(self):
        """Gets the System.Configuration.ConfigurationElementProperty object that represents the System.Configuration.ConfigurationElement object itself."""
        ...
    @property
    def EvaluationContext(self):
        """Gets the System.Configuration.ContextInformation object for the System.Configuration.ConfigurationElement object."""
        ...
    @property
    def HasContext(self):
        """Gets a value that indicates whether the System.Configuration.ConfigurationElement.CurrentConfiguration property is ll."""
        ...
    @property
    def Prefix(self):
        """
        Gets or sets the URI prefix for the current Web request module.

        Get: Prefix(self: WebRequestModuleElement) -> str

        Set: Prefix(self: WebRequestModuleElement) = value
        """
        ...
    @property
    def Properties(self): ...
    @property
    def Type(self):
        """
        Gets or sets a class that creates Web requests.

        Get: Type(self: WebRequestModuleElement) -> Type

        Set: Type(self: WebRequestModuleElement) = value
        """
        ...

class WebRequestModuleElementCollection(
    ConfigurationElementCollection
):  # skipped bases: <type 'ICollection'>, <type 'IEnumerable'>
    """
    Represents a container for Web request module configuration elements. This class cannot be inherited.

    WebRequestModuleElementCollection()
    """

    def Add(self, element):
        """
        Add(self: WebRequestModuleElementCollection, element: WebRequestModuleElement)

            Adds an element to the collection.

            element: The System.Net.Configuration.WebRequestModuleElement to add to the collection.
        """
        ...
    def Clear(self):
        """
        Clear(self: WebRequestModuleElementCollection)

            Removes all elements from the collection.
        """
        ...
    def IndexOf(self, element):
        """
        IndexOf(self: WebRequestModuleElementCollection, element: WebRequestModuleElement) -> int

            Returns the index of the specified configuration element.

            element: A System.Net.Configuration.WebRequestModuleElement.

            Returns: The zero-based index of element.
        """
        ...
    def Remove(self, *__args):
        """
        Remove(self: WebRequestModuleElementCollection, element: WebRequestModuleElement)

            Removes the specified configuration element from the collection.

            element: The System.Net.Configuration.WebRequestModuleElement to remove.

        Remove(self: WebRequestModuleElementCollection, name: str)

            Removes the element with the specified key.

            name: The key of the element to remove.
        """
        ...
    def RemoveAt(self, index):
        """
        RemoveAt(self: WebRequestModuleElementCollection, index: int)

            Removes the element at the specified index.

            index: The zero-based index of the element to remove.
        """
        ...
    def __add__(self, *args):  # cannot find CLR method
        """x.__add__(y) <==> x+y"""
        ...
    def __getitem__(self, *args):  # cannot find CLR method
        """x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y]"""
        ...
    def __setitem__(self, *args):  # cannot find CLR method
        """x.__setitem__(i, y) <==> x[i]=x.__setitem__(i, y) <==> x[i]="""
        ...
    @property
    def AddElementName(self):
        """Gets or sets the name of the System.Configuration.ConfigurationElement to associate with the add operation in the System.Configuration.ConfigurationElementCollection when overridden in a derived class."""
        ...
    @property
    def ClearElementName(self):
        """Gets or sets the name for the System.Configuration.ConfigurationElement to associate with the clear operation in the System.Configuration.ConfigurationElementCollection when overridden in a derived class."""
        ...
    @property
    def ElementName(self):
        """Gets the name used to identify this collection of elements in the configuration file when overridden in a derived class."""
        ...
    @property
    def ElementProperty(self):
        """Gets the System.Configuration.ConfigurationElementProperty object that represents the System.Configuration.ConfigurationElement object itself."""
        ...
    @property
    def EvaluationContext(self):
        """Gets the System.Configuration.ContextInformation object for the System.Configuration.ConfigurationElement object."""
        ...
    @property
    def HasContext(self):
        """Gets a value that indicates whether the System.Configuration.ConfigurationElement.CurrentConfiguration property is ll."""
        ...
    @property
    def Properties(self):
        """Gets the collection of properties."""
        ...
    @property
    def RemoveElementName(self):
        """Gets or sets the name of the System.Configuration.ConfigurationElement to associate with the remove operation in the System.Configuration.ConfigurationElementCollection when overridden in a derived class."""
        ...
    @property
    def ThrowOnDuplicate(self):
        """Gets a value indicating whether an attempt to add a duplicate System.Configuration.ConfigurationElement to the System.Configuration.ConfigurationElementCollection will cause an exception to be thrown."""
        ...

class WebRequestModulesSection(ConfigurationSection):
    """
    Represents the configuration section for Web request modules. This class cannot be inherited.

    WebRequestModulesSection()
    """

    @property
    def ElementProperty(self):
        """Gets the System.Configuration.ConfigurationElementProperty object that represents the System.Configuration.ConfigurationElement object itself."""
        ...
    @property
    def EvaluationContext(self):
        """Gets the System.Configuration.ContextInformation object for the System.Configuration.ConfigurationElement object."""
        ...
    @property
    def HasContext(self):
        """Gets a value that indicates whether the System.Configuration.ConfigurationElement.CurrentConfiguration property is ll."""
        ...
    @property
    def Properties(self): ...
    @property
    def WebRequestModules(self):
        """
        Gets the collection of Web request modules in the section.

        Get: WebRequestModules(self: WebRequestModulesSection) -> WebRequestModuleElementCollection
        """
        ...

class WebUtilityElement(ConfigurationElement):
    """
    Represents the WebUtility element in the configuration file.

    WebUtilityElement()
    """

    @property
    def ElementProperty(self):
        """Gets the System.Configuration.ConfigurationElementProperty object that represents the System.Configuration.ConfigurationElement object itself."""
        ...
    @property
    def EvaluationContext(self):
        """Gets the System.Configuration.ContextInformation object for the System.Configuration.ConfigurationElement object."""
        ...
    @property
    def HasContext(self):
        """Gets a value that indicates whether the System.Configuration.ConfigurationElement.CurrentConfiguration property is ll."""
        ...
    @property
    def Properties(self): ...
    @property
    def UnicodeDecodingConformance(self):
        """
        Gets the default Unicode decoding conformance behavior used for an System.Net.WebUtility object.

        Get: UnicodeDecodingConformance(self: WebUtilityElement) -> UnicodeDecodingConformance

        Set: UnicodeDecodingConformance(self: WebUtilityElement) = value
        """
        ...
    @property
    def UnicodeEncodingConformance(self):
        """
        Gets the default Unicode encoding conformance behavior used for an System.Net.WebUtility object.

        Get: UnicodeEncodingConformance(self: WebUtilityElement) -> UnicodeEncodingConformance

        Set: UnicodeEncodingConformance(self: WebUtilityElement) = value
        """
        ...

class WindowsAuthenticationElement(ConfigurationElement):
    """WindowsAuthenticationElement()"""

    @property
    def DefaultCredentialsHandleCacheSize(self):
        """
        Get: DefaultCredentialsHandleCacheSize(self: WindowsAuthenticationElement) -> int

        Set: DefaultCredentialsHandleCacheSize(self: WindowsAuthenticationElement) = value
        """
        ...
    @property
    def ElementProperty(self):
        """Gets the System.Configuration.ConfigurationElementProperty object that represents the System.Configuration.ConfigurationElement object itself."""
        ...
    @property
    def EvaluationContext(self):
        """Gets the System.Configuration.ContextInformation object for the System.Configuration.ConfigurationElement object."""
        ...
    @property
    def HasContext(self):
        """Gets a value that indicates whether the System.Configuration.ConfigurationElement.CurrentConfiguration property is ll."""
        ...
    @property
    def Properties(self): ...
