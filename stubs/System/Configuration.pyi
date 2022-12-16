# encoding: utf-8
# module System.Configuration calls itself Configuration
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class SettingAttribute(Attribute):  # skipped bases: <type '_Attribute'>
    """
    Represents a custom settings attribute used to associate settings information with a settings property.

    SettingAttribute()
    """

    pass

class ApplicationScopedSettingAttribute(SettingAttribute):  # skipped bases: <type '_Attribute'>
    """
    Specifies that an application settings property has a common value for all users of an application. This class cannot be inherited.

    ApplicationScopedSettingAttribute()
    """

    pass

class SettingsBase:  # skipped bases: <type 'object'>
    """Provides the base class used to support user property settings."""

    def Initialize(self, context, properties, providers):
        """
        Initialize(self: SettingsBase, context: SettingsContext, properties: SettingsPropertyCollection, providers: SettingsProviderCollection)

            Initializes internal properties used by System.Configuration.SettingsBase object.

            context: The settings context related to the settings properties.

            properties: The settings properties that will be accessible from the System.Configuration.SettingsBase instance.

            providers: The initialized providers that should be used when loading and saving property values.
        """
        ...
    def Save(self):
        """
        Save(self: SettingsBase)

            Stores the current values of the settings properties.
        """
        ...
    @staticmethod
    def Synchronized(settingsBase):
        """
        Synchronized(settingsBase: SettingsBase) -> SettingsBase

            Provides a System.Configuration.SettingsBase class that is synchronized (thread safe).

            settingsBase: The class used to support user property settings.

            Returns: A System.Configuration.SettingsBase class that is synchronized.
        """
        ...
    def __getitem__(self, *args):  # cannot find CLR method
        """x.__getitem__(y) <==> x[y]"""
        ...
    def __setitem__(self, *args):  # cannot find CLR method
        """x.__setitem__(i, y) <==> x[i]="""
        ...
    @property
    def Context(self):
        """
        Gets the associated settings context.

        Get: Context(self: SettingsBase) -> SettingsContext
        """
        ...
    @property
    def IsSynchronized(self):
        """
        Gets a value indicating whether access to the object is synchronized (thread safe).

        Get: IsSynchronized(self: SettingsBase) -> bool
        """
        ...
    @property
    def Properties(self):
        """
        Gets the collection of settings properties.

        Get: Properties(self: SettingsBase) -> SettingsPropertyCollection
        """
        ...
    @property
    def PropertyValues(self):
        """
        Gets a collection of settings property values.

        Get: PropertyValues(self: SettingsBase) -> SettingsPropertyValueCollection
        """
        ...
    @property
    def Providers(self):
        """
        Gets a collection of settings providers.

        Get: Providers(self: SettingsBase) -> SettingsProviderCollection
        """
        ...

class ApplicationSettingsBase(SettingsBase, INotifyPropertyChanged):
    """Acts as a base class for deriving concrete wrapper classes to implement the application settings feature in Window Forms applications."""

    def GetPreviousVersion(self, propertyName):
        """
        GetPreviousVersion(self: ApplicationSettingsBase, propertyName: str) -> object

            Returns the value of the named settings property for the previous version of the same application.

            propertyName: A System.String containing the name of the settings property whose value is to be returned.

            Returns: An System.Object containing the value of the specified System.Configuration.SettingsProperty if found; otherwise, ll.
        """
        ...
    def OnPropertyChanged(self, *args):  # cannot find CLR method
        """
        OnPropertyChanged(self: ApplicationSettingsBase, sender: object, e: PropertyChangedEventArgs)

            Raises the System.Configuration.ApplicationSettingsBase.PropertyChanged event.

            sender: The source of the event.

            e: A System.ComponentModel.PropertyChangedEventArgs that contains the event data.
        """
        ...
    def OnSettingChanging(self, *args):  # cannot find CLR method
        """
        OnSettingChanging(self: ApplicationSettingsBase, sender: object, e: SettingChangingEventArgs)

            Raises the System.Configuration.ApplicationSettingsBase.SettingChanging event.

            sender: The source of the event.

            e: A System.Configuration.SettingChangingEventArgs that contains the event data.
        """
        ...
    def OnSettingsLoaded(self, *args):  # cannot find CLR method
        """
        OnSettingsLoaded(self: ApplicationSettingsBase, sender: object, e: SettingsLoadedEventArgs)

            Raises the System.Configuration.ApplicationSettingsBase.SettingsLoaded event.

            sender: The source of the event.

            e: A System.Configuration.SettingsLoadedEventArgs that contains the event data.
        """
        ...
    def OnSettingsSaving(self, *args):  # cannot find CLR method
        """
        OnSettingsSaving(self: ApplicationSettingsBase, sender: object, e: CancelEventArgs)

            Raises the System.Configuration.ApplicationSettingsBase.SettingsSaving event.

            sender: The source of the event.

            e: A System.ComponentModel.CancelEventArgs that contains the event data.
        """
        ...
    def Reload(self):
        """
        Reload(self: ApplicationSettingsBase)

            Refreshes the application settings property values from persistent storage.
        """
        ...
    def Reset(self):
        """
        Reset(self: ApplicationSettingsBase)

            Restores the persisted application settings values to their corresponding default properties.
        """
        ...
    def Upgrade(self):
        """
        Upgrade(self: ApplicationSettingsBase)

            Updates application settings to reflect a more recent installation of the application.
        """
        ...
    @staticmethod  # known case of __new__
    def __new__(cls, *args):  # cannot find CLR constructor
        """
        __new__(cls: type)

        __new__(cls: type, owner: IComponent)

        __new__(cls: type, settingsKey: str)

        __new__(cls: type, owner: IComponent, settingsKey: str)
        """
        ...
    @property
    def Context(self):
        """
        Gets the application settings context associated with the settings group.

        Get: Context(self: ApplicationSettingsBase) -> SettingsContext
        """
        ...
    @property
    def Properties(self):
        """
        Gets the collection of settings properties in the wrapper.

        Get: Properties(self: ApplicationSettingsBase) -> SettingsPropertyCollection
        """
        ...
    @property
    def PropertyValues(self):
        """
        Gets a collection of property values.

        Get: PropertyValues(self: ApplicationSettingsBase) -> SettingsPropertyValueCollection
        """
        ...
    @property
    def Providers(self):
        """
        Gets the collection of application settings providers used by the wrapper.

        Get: Providers(self: ApplicationSettingsBase) -> SettingsProviderCollection
        """
        ...
    @property
    def SettingsKey(self):
        """
        Gets or sets the settings key for the application settings group.

        Get: SettingsKey(self: ApplicationSettingsBase) -> str

        Set: SettingsKey(self: ApplicationSettingsBase) = value
        """
        ...
    PropertyChanged = None
    SettingChanging = None
    SettingsLoaded = None
    SettingsSaving = None

class ApplicationSettingsGroup(ConfigurationSectionGroup):
    """
    Represents a grouping of related application settings sections within a configuration file. This class cannot be inherited.

    ApplicationSettingsGroup()
    """

    pass

class AppSettingsReader:  # skipped bases: <type 'object'>
    """
    Provides a method for reading values of a particular type from the configuration.

    AppSettingsReader()
    """

    def GetValue(self, key, type):
        """
        GetValue(self: AppSettingsReader, key: str, type: Type) -> object

            Gets the value for a specified key from the System.Configuration.ConfigurationSettings.AppSettings property and returns an object of the specified type containing the value from the configuration.

            key: The key for which to get the value.

            type: The type of the object to return.

            Returns: The value of the specified key.
        """
        ...

class ClientSettingsSection(ConfigurationSection):
    """
    Represents a group of user-scoped application settings in a configuration file.

    ClientSettingsSection()
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
    def Settings(self):
        """
        Gets the collection of client settings for the section.

        Get: Settings(self: ClientSettingsSection) -> SettingElementCollection
        """
        ...

class ConfigurationException(SystemException):  # skipped bases: <type '_Exception'>, <type 'ISerializable'>
    """
    The exception that is thrown when a configuration system error has occurred.

    ConfigurationException()

    ConfigurationException(message: str)

    ConfigurationException(message: str, inner: Exception)

    ConfigurationException(message: str, node: XmlNode)

    ConfigurationException(message: str, inner: Exception, node: XmlNode)

    ConfigurationException(message: str, filename: str, line: int)

    ConfigurationException(message: str, inner: Exception, filename: str, line: int)
    """

    @staticmethod
    def GetXmlNodeFilename(node):
        """
        GetXmlNodeFilename(node: XmlNode) -> str

            Gets the path to the configuration file from which the internal System.Xml.XmlNode object was loaded when this configuration exception was thrown.

            node: The System.Xml.XmlNode that caused this System.Configuration.ConfigurationException exception to be thrown.

            Returns: A ring representing the node file name.
        """
        ...
    @staticmethod
    def GetXmlNodeLineNumber(node):
        """
        GetXmlNodeLineNumber(node: XmlNode) -> int

            Gets the line number within the configuration file that the internal System.Xml.XmlNode object represented when this configuration exception was thrown.

            node: The System.Xml.XmlNode that caused this System.Configuration.ConfigurationException exception to be thrown.

            Returns: An t representing the node line number.
        """
        ...
    @property
    def BareMessage(self):
        """
        Gets a description of why this configuration exception was thrown.

        Get: BareMessage(self: ConfigurationException) -> str
        """
        ...
    @property
    def Filename(self):
        """
        Gets the path to the configuration file that caused this configuration exception to be thrown.

        Get: Filename(self: ConfigurationException) -> str
        """
        ...
    @property
    def Line(self):
        """
        Gets the line number within the configuration file at which this configuration exception was thrown.

        Get: Line(self: ConfigurationException) -> int
        """
        ...
    @property
    def Message(self):
        """
        Gets an extended description of why this configuration exception was thrown.

        Get: Message(self: ConfigurationException) -> str
        """
        ...
    SerializeObjectState = None

class ConfigurationSettings:  # skipped bases: <type 'object'>
    """Provides runtime versions 1.0 and 1.1 support for reading configuration sections and common configuration settings."""

    @staticmethod
    def GetConfig(sectionName):
        """
        GetConfig(sectionName: str) -> object

            Returns the System.Configuration.ConfigurationSection object for the passed configuration section name and path.

            sectionName: A configuration name and path, such as "system.net/settings".

            Returns: The System.Configuration.ConfigurationSection object for the passed configuration section name and path.The System.Configuration.ConfigurationSettings class provides backward compatibility only. You should use the

             System.Configuration.ConfigurationManager class or System.Web.Configuration.WebConfigurationManager class instead.
        """
        ...
    AppSettings = None

class ConfigXmlDocument(
    XmlDocument, IConfigErrorInfo
):  # skipped bases: <type 'IXPathNavigable'>, <type 'IEnumerable'>, <type 'ICloneable'>
    """
    Wraps the corresponding System.Xml.XmlDocument type and also carries the necessary information for reporting file-name and line numbers.

    ConfigXmlDocument()
    """

    def LoadSingleElement(self, filename, sourceReader):
        """
        LoadSingleElement(self: ConfigXmlDocument, filename: str, sourceReader: XmlTextReader)

            Loads a single configuration element.

            filename: The name of the file.

            sourceReader: The source for the reader.
        """
        ...
    @property
    def Filename(self):
        """
        Gets the configuration file name.

        Get: Filename(self: ConfigXmlDocument) -> str
        """
        ...
    @property
    def LineNumber(self):
        """
        Gets the current node line number.

        Get: LineNumber(self: ConfigXmlDocument) -> int
        """
        ...

class DefaultSettingValueAttribute(Attribute):  # skipped bases: <type '_Attribute'>
    """
    Specifies the default value for an application settings property.

    DefaultSettingValueAttribute(value: str)
    """

    @staticmethod  # known case of __new__
    def __new__(cls, value):
        """__new__(cls: type, value: str)"""
        ...
    @property
    def Value(self):
        """
        Gets the default value for the application settings property.

        Get: Value(self: DefaultSettingValueAttribute) -> str
        """
        ...

class DictionarySectionHandler(object, IConfigurationSectionHandler):
    """
    Provides key/value pair configuration information from a configuration section.

    DictionarySectionHandler()
    """

    @property
    def KeyAttributeName(self):
        """Gets the XML attribute name to use as the key in a key/value pair."""
        ...
    @property
    def ValueAttributeName(self):
        """Gets the XML attribute name to use as the value in a key/value pair."""
        ...

class IApplicationSettingsProvider:
    """Defines extended capabilities for client-based application settings providers."""

    def GetPreviousVersion(self, context, property):
        """
        GetPreviousVersion(self: IApplicationSettingsProvider, context: SettingsContext, property: SettingsProperty) -> SettingsPropertyValue

            Returns the value of the specified settings property for the previous version of the same application.

            context: A System.Configuration.SettingsContext describing the current application usage.

            property: The System.Configuration.SettingsProperty whose value is to be returned.

            Returns: A System.Configuration.SettingsPropertyValue containing the value of the specified property setting as it was last set in the previous version of the application; or ll if the setting cannot be found.
        """
        ...
    def Reset(self, context):
        """
        Reset(self: IApplicationSettingsProvider, context: SettingsContext)

            Resets the application settings associated with the specified application to their default values.

            context: A System.Configuration.SettingsContext describing the current application usage.
        """
        ...
    def Upgrade(self, context, properties):
        """
        Upgrade(self: IApplicationSettingsProvider, context: SettingsContext, properties: SettingsPropertyCollection)

            Indicates to the provider that the application has been upgraded. This offers the provider an opportunity to upgrade its stored settings as appropriate.

            context: A System.Configuration.SettingsContext describing the current application usage.

            properties: A System.Configuration.SettingsPropertyCollection containing the settings property group whose values are to be retrieved.
        """
        ...

class IConfigurationSectionHandler:
    """Handles the access to certain configuration sections."""

    def Create(self, parent, configContext, section):
        """
        Create(self: IConfigurationSectionHandler, parent: object, configContext: object, section: XmlNode) -> object

            Creates a configuration section handler.

            parent: Parent object.

            configContext: Configuration context object.

            section: Section XML node.

            Returns: The created section handler object.
        """
        ...

class IConfigurationSystem:
    """Provides standard configuration methods."""

    def GetConfig(self, configKey):
        """
        GetConfig(self: IConfigurationSystem, configKey: str) -> object

            Gets the specified configuration.

            configKey: The configuration key.

            Returns: The object representing the configuration.
        """
        ...
    def Init(self):
        """
        Init(self: IConfigurationSystem)

            Used for initialization.
        """
        ...

class IdnElement(ConfigurationElement):
    """
    Provides the configuration setting for International Domain Name (IDN) processing in the System.Uri class.

    IdnElement()
    """

    @property
    def ElementProperty(self):
        """Gets the System.Configuration.ConfigurationElementProperty object that represents the System.Configuration.ConfigurationElement object itself."""
        ...
    @property
    def Enabled(self):
        """
        Gets or sets the value of the System.Configuration.IdnElement configuration setting.

        Get: Enabled(self: IdnElement) -> UriIdnScope

        Set: Enabled(self: IdnElement) = value
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

class IgnoreSectionHandler(object, IConfigurationSectionHandler):
    """
    Provides a legacy section-handler definition for configuration sections that are not handled by the System.Configuration types.

    IgnoreSectionHandler()
    """

    pass

class IPersistComponentSettings:
    """Defines standard functionality for controls or libraries that store and retrieve application settings."""

    def LoadComponentSettings(self):
        """
        LoadComponentSettings(self: IPersistComponentSettings)

            Reads the control's application settings into their corresponding properties and updates the control's state.
        """
        ...
    def ResetComponentSettings(self):
        """
        ResetComponentSettings(self: IPersistComponentSettings)

            Resets the control's application settings properties to their default values.
        """
        ...
    def SaveComponentSettings(self):
        """
        SaveComponentSettings(self: IPersistComponentSettings)

            Persists the control's application settings properties.
        """
        ...
    @property
    def SaveSettings(self):
        """
        Gets or sets a value indicating whether the control should automatically persist its application settings properties.

        Get: SaveSettings(self: IPersistComponentSettings) -> bool

        Set: SaveSettings(self: IPersistComponentSettings) = value
        """
        ...
    @property
    def SettingsKey(self):
        """
        Gets or sets the value of the application settings key for the current instance of the control.

        Get: SettingsKey(self: IPersistComponentSettings) -> str

        Set: SettingsKey(self: IPersistComponentSettings) = value
        """
        ...

class IriParsingElement(ConfigurationElement):
    """
    Provides the configuration setting for International Resource Identifier (IRI) processing in the System.Uri class.

    IriParsingElement()
    """

    @property
    def ElementProperty(self):
        """Gets the System.Configuration.ConfigurationElementProperty object that represents the System.Configuration.ConfigurationElement object itself."""
        ...
    @property
    def Enabled(self):
        """
        Gets or sets the value of the System.Configuration.IriParsingElement configuration setting.

        Get: Enabled(self: IriParsingElement) -> bool

        Set: Enabled(self: IriParsingElement) = value
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

class ISettingsProviderService:
    """Provides an interface for defining an alternate application settings provider."""

    def GetSettingsProvider(self, property):
        """
        GetSettingsProvider(self: ISettingsProviderService, property: SettingsProperty) -> SettingsProvider

            Returns the settings provider compatible with the specified settings property.

            property: The System.Configuration.SettingsProperty that requires serialization.

            Returns: If found, the System.Configuration.SettingsProvider that can persist the specified settings property; otherwise, ll.
        """
        ...

class SettingsProvider(ProviderBase):
    """Acts as a base class for deriving custom settings providers in the application settings architecture."""

    def GetPropertyValues(self, context, collection):
        """
        GetPropertyValues(self: SettingsProvider, context: SettingsContext, collection: SettingsPropertyCollection) -> SettingsPropertyValueCollection

            Returns the collection of settings property values for the specified application instance and settings property group.

            context: A System.Configuration.SettingsContext describing the current application use.

            collection: A System.Configuration.SettingsPropertyCollection containing the settings property group whose values are to be retrieved.

            Returns: A System.Configuration.SettingsPropertyValueCollection containing the values for the specified settings property group.
        """
        ...
    def SetPropertyValues(self, context, collection):
        """
        SetPropertyValues(self: SettingsProvider, context: SettingsContext, collection: SettingsPropertyValueCollection)

            Sets the values of the specified group of property settings.

            context: A System.Configuration.SettingsContext describing the current application usage.

            collection: A System.Configuration.SettingsPropertyValueCollection representing the group of property settings to set.
        """
        ...
    @property
    def ApplicationName(self):
        """
        Gets or sets the name of the currently running application.

        Get: ApplicationName(self: SettingsProvider) -> str

        Set: ApplicationName(self: SettingsProvider) = value
        """
        ...

class LocalFileSettingsProvider(SettingsProvider, IApplicationSettingsProvider):
    """
    Provides persistence for application settings classes.

    LocalFileSettingsProvider()
    """

    def Initialize(self, name, values):
        """
        Initialize(self: LocalFileSettingsProvider, name: str, values: NameValueCollection)

            Initializes the provider.

            name: The friendly name of the provider.

            values: A collection of the name/value pairs representing the provider-specific attributes specified in the configuration for this provider.
        """
        ...
    @property
    def ApplicationName(self):
        """
        Gets or sets the name of the currently running application.

        Get: ApplicationName(self: LocalFileSettingsProvider) -> str

        Set: ApplicationName(self: LocalFileSettingsProvider) = value
        """
        ...

class NameValueFileSectionHandler(object, IConfigurationSectionHandler):
    """
    Provides access to a configuration file. This type supports the .NET Framework configuration infrastructure and is not intended to be used directly from your code.

    NameValueFileSectionHandler()
    """

    pass

class NameValueSectionHandler(object, IConfigurationSectionHandler):
    """
    Provides name/value-pair configuration information from a configuration section.

    NameValueSectionHandler()
    """

    @property
    def KeyAttributeName(self):
        """Gets the XML attribute name to use as the key in a key/value pair."""
        ...
    @property
    def ValueAttributeName(self):
        """Gets the XML attribute name to use as the value in a key/value pair."""
        ...

class NoSettingsVersionUpgradeAttribute(Attribute):  # skipped bases: <type '_Attribute'>
    """
    Specifies that a settings provider should disable any logic that gets invoked when an application upgrade is detected. This class cannot be inherited.

    NoSettingsVersionUpgradeAttribute()
    """

    pass

class SchemeSettingElement(ConfigurationElement):
    """
    Represents an element in a System.Configuration.SchemeSettingElementCollection class.

    SchemeSettingElement()
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
    def GenericUriParserOptions(self):
        """
        Gets the value of the GenericUriParserOptions entry from a System.Configuration.SchemeSettingElement instance.

        Get: GenericUriParserOptions(self: SchemeSettingElement) -> GenericUriParserOptions
        """
        ...
    @property
    def HasContext(self):
        """Gets a value that indicates whether the System.Configuration.ConfigurationElement.CurrentConfiguration property is ll."""
        ...
    @property
    def Name(self):
        """
        Gets the value of the Name entry from a System.Configuration.SchemeSettingElement instance.

        Get: Name(self: SchemeSettingElement) -> str
        """
        ...
    @property
    def Properties(self): ...

class SchemeSettingElementCollection(
    ConfigurationElementCollection
):  # skipped bases: <type 'ICollection'>, <type 'IEnumerable'>
    """
    Represents a collection of System.Configuration.SchemeSettingElement objects.

    SchemeSettingElementCollection()
    """

    def IndexOf(self, element):
        """
        IndexOf(self: SchemeSettingElementCollection, element: SchemeSettingElement) -> int

            The index of the specified System.Configuration.SchemeSettingElement.

            element: The System.Configuration.SchemeSettingElement for the specified index location.

            Returns: The index of the specified System.Configuration.SchemeSettingElement; otherwise, -1.
        """
        ...
    def __getitem__(self, *args):  # cannot find CLR method
        """x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y]"""
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
    def CollectionType(self):
        """
        Gets the default collection type of System.Configuration.SchemeSettingElementCollection.

        Get: CollectionType(self: SchemeSettingElementCollection) -> ConfigurationElementCollectionType
        """
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

class SettingChangingEventArgs(CancelEventArgs):
    """
    Provides data for the System.Configuration.ApplicationSettingsBase.SettingChanging event.

    SettingChangingEventArgs(settingName: str, settingClass: str, settingKey: str, newValue: object, cancel: bool)
    """

    @property
    def NewValue(self):
        """
        Gets the new value being assigned to the application settings property.

        Get: NewValue(self: SettingChangingEventArgs) -> object
        """
        ...
    @property
    def SettingClass(self):
        """
        Gets the application settings property category.

        Get: SettingClass(self: SettingChangingEventArgs) -> str
        """
        ...
    @property
    def SettingKey(self):
        """
        Gets the application settings key associated with the property.

        Get: SettingKey(self: SettingChangingEventArgs) -> str
        """
        ...
    @property
    def SettingName(self):
        """
        Gets the name of the application setting associated with the application settings property.

        Get: SettingName(self: SettingChangingEventArgs) -> str
        """
        ...

class SettingChangingEventHandler(MulticastDelegate):  # skipped bases: <type 'ICloneable'>, <type 'ISerializable'>
    """
    Represents the method that will handle the System.Configuration.ApplicationSettingsBase.SettingChanging event.

    SettingChangingEventHandler(object: object, method: IntPtr)
    """

    def BeginInvoke(self, sender, e, callback, object):
        """BeginInvoke(self: SettingChangingEventHandler, sender: object, e: SettingChangingEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult"""
        ...
    def EndInvoke(self, result):
        """EndInvoke(self: SettingChangingEventHandler, result: IAsyncResult)"""
        ...
    def Invoke(self, sender, e):
        """Invoke(self: SettingChangingEventHandler, sender: object, e: SettingChangingEventArgs)"""
        ...

class SettingElement(ConfigurationElement):
    """
    Represents a simplified configuration element used for updating elements in the configuration. This class cannot be inherited.

    SettingElement()

    SettingElement(name: str, serializeAs: SettingsSerializeAs)
    """

    @staticmethod  # known case of __new__
    def __new__(cls, name=None, serializeAs=None):
        """
        __new__(cls: type)

        __new__(cls: type, name: str, serializeAs: SettingsSerializeAs)
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
    def Name(self):
        """
        Gets or sets the name of the System.Configuration.SettingElement object.

        Get: Name(self: SettingElement) -> str

        Set: Name(self: SettingElement) = value
        """
        ...
    @property
    def Properties(self): ...
    @property
    def SerializeAs(self):
        """
        Gets or sets the serialization mechanism used to persist the values of the System.Configuration.SettingElement object.

        Get: SerializeAs(self: SettingElement) -> SettingsSerializeAs

        Set: SerializeAs(self: SettingElement) = value
        """
        ...
    @property
    def Value(self):
        """
        Gets or sets the value of a System.Configuration.SettingElement object by using a System.Configuration.SettingValueElement object.

        Get: Value(self: SettingElement) -> SettingValueElement

        Set: Value(self: SettingElement) = value
        """
        ...

class SettingElementCollection(
    ConfigurationElementCollection
):  # skipped bases: <type 'ICollection'>, <type 'IEnumerable'>
    """
    Contains a collection of System.Configuration.SettingElement objects. This class cannot be inherited.

    SettingElementCollection()
    """

    def Add(self, element):
        """
        Add(self: SettingElementCollection, element: SettingElement)

            Adds a System.Configuration.SettingElement object to the collection.

            element: The System.Configuration.SettingElement object to add to the collection.
        """
        ...
    def Clear(self):
        """
        Clear(self: SettingElementCollection)

            Removes all System.Configuration.SettingElement objects from the collection.
        """
        ...
    def Get(self, elementKey):
        """
        Get(self: SettingElementCollection, elementKey: str) -> SettingElement

            Gets a System.Configuration.SettingElement object from the collection.

            elementKey: A string value representing the System.Configuration.SettingElement object in the collection.

            Returns: A System.Configuration.SettingElement object.
        """
        ...
    def Remove(self, element):
        """
        Remove(self: SettingElementCollection, element: SettingElement)

            Removes a System.Configuration.SettingElement object from the collection.

            element: A System.Configuration.SettingElement object.
        """
        ...
    def __add__(self, *args):  # cannot find CLR method
        """x.__add__(y) <==> x+y"""
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
    def CollectionType(self):
        """
        Gets the type of the configuration collection.

        Get: CollectionType(self: SettingElementCollection) -> ConfigurationElementCollectionType
        """
        ...
    @property
    def ElementName(self): ...
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

class SettingsAttributeDictionary(
    Hashtable
):  # skipped bases: <type 'IDictionary'>, <type 'ICollection'>, <type 'IEnumerable'>, <type 'IDeserializationCallback'>, <type 'ICloneable'>, <type 'ISerializable'>
    """
    Represents a collection of key/value pairs used to describe a configuration object as well as a System.Configuration.SettingsProperty object.

    SettingsAttributeDictionary()

    SettingsAttributeDictionary(attributes: SettingsAttributeDictionary)
    """

    @property
    def comparer(self):
        """Gets or sets the System.Collections.IComparer to use for the System.Collections.Hashtable."""
        ...
    @property
    def EqualityComparer(self):
        """Gets the System.Collections.IEqualityComparer to use for the System.Collections.Hashtable."""
        ...
    @property
    def hcp(self):
        """Gets or sets the object that can dispense hash codes."""
        ...

class SettingsContext(
    Hashtable
):  # skipped bases: <type 'IDictionary'>, <type 'ICollection'>, <type 'IEnumerable'>, <type 'IDeserializationCallback'>, <type 'ICloneable'>, <type 'ISerializable'>
    """
    Provides contextual information that the provider can use when persisting settings.

    SettingsContext()
    """

    @property
    def comparer(self):
        """Gets or sets the System.Collections.IComparer to use for the System.Collections.Hashtable."""
        ...
    @property
    def EqualityComparer(self):
        """Gets the System.Collections.IEqualityComparer to use for the System.Collections.Hashtable."""
        ...
    @property
    def hcp(self):
        """Gets or sets the object that can dispense hash codes."""
        ...

class SettingsDescriptionAttribute(Attribute):  # skipped bases: <type '_Attribute'>
    """
    Provides a string that describes an individual configuration property. This class cannot be inherited.

    SettingsDescriptionAttribute(description: str)
    """

    @staticmethod  # known case of __new__
    def __new__(cls, description):
        """__new__(cls: type, description: str)"""
        ...
    @property
    def Description(self):
        """
        Gets the descriptive text for the associated configuration property.

        Get: Description(self: SettingsDescriptionAttribute) -> str
        """
        ...

class SettingsGroupDescriptionAttribute(Attribute):  # skipped bases: <type '_Attribute'>
    """
    Provides a string that describes an application settings property group. This class cannot be inherited.

    SettingsGroupDescriptionAttribute(description: str)
    """

    @staticmethod  # known case of __new__
    def __new__(cls, description):
        """__new__(cls: type, description: str)"""
        ...
    @property
    def Description(self):
        """
        The descriptive text for the application settings properties group.

        Get: Description(self: SettingsGroupDescriptionAttribute) -> str
        """
        ...

class SettingsGroupNameAttribute(Attribute):  # skipped bases: <type '_Attribute'>
    """
    Specifies a name for application settings property group. This class cannot be inherited.

    SettingsGroupNameAttribute(groupName: str)
    """

    @staticmethod  # known case of __new__
    def __new__(cls, groupName):
        """__new__(cls: type, groupName: str)"""
        ...
    @property
    def GroupName(self):
        """
        Gets the name of the application settings property group.

        Get: GroupName(self: SettingsGroupNameAttribute) -> str
        """
        ...

class SettingsLoadedEventArgs(EventArgs):
    """
    Provides data for the System.Configuration.ApplicationSettingsBase.SettingsLoaded event.

    SettingsLoadedEventArgs(provider: SettingsProvider)
    """

    @staticmethod  # known case of __new__
    def __new__(cls, provider):
        """__new__(cls: type, provider: SettingsProvider)"""
        ...
    @property
    def Provider(self):
        """
        Gets the settings provider used to store configuration settings.

        Get: Provider(self: SettingsLoadedEventArgs) -> SettingsProvider
        """
        ...

class SettingsLoadedEventHandler(MulticastDelegate):  # skipped bases: <type 'ICloneable'>, <type 'ISerializable'>
    """
    Represents the method that will handle the System.Configuration.ApplicationSettingsBase.SettingsLoaded event.

    SettingsLoadedEventHandler(object: object, method: IntPtr)
    """

    def BeginInvoke(self, sender, e, callback, object):
        """BeginInvoke(self: SettingsLoadedEventHandler, sender: object, e: SettingsLoadedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult"""
        ...
    def EndInvoke(self, result):
        """EndInvoke(self: SettingsLoadedEventHandler, result: IAsyncResult)"""
        ...
    def Invoke(self, sender, e):
        """Invoke(self: SettingsLoadedEventHandler, sender: object, e: SettingsLoadedEventArgs)"""
        ...

class SettingsManageability(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Provides values to indicate which services should be made available to application settings.

    enum SettingsManageability, values: Roaming (0)
    """

    Roaming = None
    value__ = None

class SettingsManageabilityAttribute(Attribute):  # skipped bases: <type '_Attribute'>
    """
    Specifies special services for application settings properties. This class cannot be inherited.

    SettingsManageabilityAttribute(manageability: SettingsManageability)
    """

    @staticmethod  # known case of __new__
    def __new__(cls, manageability):
        """__new__(cls: type, manageability: SettingsManageability)"""
        ...
    @property
    def Manageability(self):
        """
        Gets the set of special services that have been requested.

        Get: Manageability(self: SettingsManageabilityAttribute) -> SettingsManageability
        """
        ...

class SettingsProperty:  # skipped bases: <type 'object'>
    """
    Used internally as the class that represents metadata about an individual configuration property.

    SettingsProperty(name: str)

    SettingsProperty(name: str, propertyType: Type, provider: SettingsProvider, isReadOnly: bool, defaultValue: object, serializeAs: SettingsSerializeAs, attributes: SettingsAttributeDictionary, throwOnErrorDeserializing: bool, throwOnErrorSerializing: bool)

    SettingsProperty(propertyToCopy: SettingsProperty)
    """

    @property
    def Attributes(self):
        """
        Gets a System.Configuration.SettingsAttributeDictionary object containing the attributes of the System.Configuration.SettingsProperty object.

        Get: Attributes(self: SettingsProperty) -> SettingsAttributeDictionary
        """
        ...
    @property
    def DefaultValue(self):
        """
        Gets or sets the default value of the System.Configuration.SettingsProperty object.

        Get: DefaultValue(self: SettingsProperty) -> object

        Set: DefaultValue(self: SettingsProperty) = value
        """
        ...
    @property
    def IsReadOnly(self):
        """
        Gets or sets a value specifying whether a System.Configuration.SettingsProperty object is read-only.

        Get: IsReadOnly(self: SettingsProperty) -> bool

        Set: IsReadOnly(self: SettingsProperty) = value
        """
        ...
    @property
    def Name(self):
        """
        Gets or sets the name of the System.Configuration.SettingsProperty.

        Get: Name(self: SettingsProperty) -> str

        Set: Name(self: SettingsProperty) = value
        """
        ...
    @property
    def PropertyType(self):
        """
        Gets or sets the type for the System.Configuration.SettingsProperty.

        Get: PropertyType(self: SettingsProperty) -> Type

        Set: PropertyType(self: SettingsProperty) = value
        """
        ...
    @property
    def Provider(self):
        """
        Gets or sets the provider for the System.Configuration.SettingsProperty.

        Get: Provider(self: SettingsProperty) -> SettingsProvider

        Set: Provider(self: SettingsProperty) = value
        """
        ...
    @property
    def SerializeAs(self):
        """
        Gets or sets a System.Configuration.SettingsSerializeAs object for the System.Configuration.SettingsProperty.

        Get: SerializeAs(self: SettingsProperty) -> SettingsSerializeAs

        Set: SerializeAs(self: SettingsProperty) = value
        """
        ...
    @property
    def ThrowOnErrorDeserializing(self):
        """
        Gets or sets a value specifying whether an error will be thrown when the property is unsuccessfully deserialized.

        Get: ThrowOnErrorDeserializing(self: SettingsProperty) -> bool

        Set: ThrowOnErrorDeserializing(self: SettingsProperty) = value
        """
        ...
    @property
    def ThrowOnErrorSerializing(self):
        """
        Gets or sets a value specifying whether an error will be thrown when the property is unsuccessfully serialized.

        Get: ThrowOnErrorSerializing(self: SettingsProperty) -> bool

        Set: ThrowOnErrorSerializing(self: SettingsProperty) = value
        """
        ...

class SettingsPropertyCollection(object, ICloneable, ICollection):  # skipped bases: <type 'IEnumerable'>
    """
    Contains a collection of System.Configuration.SettingsProperty objects.

    SettingsPropertyCollection()
    """

    def Add(self, property):
        """
        Add(self: SettingsPropertyCollection, property: SettingsProperty)

            Adds a System.Configuration.SettingsProperty object to the collection.

            property: A System.Configuration.SettingsProperty object.
        """
        ...
    def Clear(self):
        """
        Clear(self: SettingsPropertyCollection)

            Removes all System.Configuration.SettingsProperty objects from the collection.
        """
        ...
    def GetEnumerator(self):
        """
        GetEnumerator(self: SettingsPropertyCollection) -> IEnumerator

            Gets the System.Collections.IEnumerator object as it applies to the collection.

            Returns: The System.Collections.IEnumerator object as it applies to the collection.
        """
        ...
    def OnAdd(self, *args):  # cannot find CLR method
        """
        OnAdd(self: SettingsPropertyCollection, property: SettingsProperty)

            Performs additional, custom processing when adding to the contents of the System.Configuration.SettingsPropertyCollection instance.

            property: A System.Configuration.SettingsProperty object.
        """
        ...
    def OnAddComplete(self, *args):  # cannot find CLR method
        """
        OnAddComplete(self: SettingsPropertyCollection, property: SettingsProperty)

            Performs additional, custom processing after adding to the contents of the System.Configuration.SettingsPropertyCollection instance.

            property: A System.Configuration.SettingsProperty object.
        """
        ...
    def OnClear(self, *args):  # cannot find CLR method
        """
        OnClear(self: SettingsPropertyCollection)

            Performs additional, custom processing when clearing the contents of the System.Configuration.SettingsPropertyCollection instance.
        """
        ...
    def OnClearComplete(self, *args):  # cannot find CLR method
        """
        OnClearComplete(self: SettingsPropertyCollection)

            Performs additional, custom processing after clearing the contents of the System.Configuration.SettingsPropertyCollection instance.
        """
        ...
    def OnRemove(self, *args):  # cannot find CLR method
        """
        OnRemove(self: SettingsPropertyCollection, property: SettingsProperty)

            Performs additional, custom processing when removing the contents of the System.Configuration.SettingsPropertyCollection instance.

            property: A System.Configuration.SettingsProperty object.
        """
        ...
    def OnRemoveComplete(self, *args):  # cannot find CLR method
        """
        OnRemoveComplete(self: SettingsPropertyCollection, property: SettingsProperty)

            Performs additional, custom processing after removing the contents of the System.Configuration.SettingsPropertyCollection instance.

            property: A System.Configuration.SettingsProperty object.
        """
        ...
    def Remove(self, name):
        """
        Remove(self: SettingsPropertyCollection, name: str)

            Removes a System.Configuration.SettingsProperty object from the collection.

            name: The name of the System.Configuration.SettingsProperty object.
        """
        ...
    def SetReadOnly(self):
        """
        SetReadOnly(self: SettingsPropertyCollection)

            Sets the collection to be read-only.
        """
        ...
    def __add__(self, *args):  # cannot find CLR method
        """x.__add__(y) <==> x+y"""
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
        Gets a value that specifies the number of System.Configuration.SettingsProperty objects in the collection.

        Get: Count(self: SettingsPropertyCollection) -> int
        """
        ...
    @property
    def IsSynchronized(self):
        """
        Gets a value that indicates whether access to the collection is synchronized (thread safe).

        Get: IsSynchronized(self: SettingsPropertyCollection) -> bool
        """
        ...
    @property
    def SyncRoot(self):
        """
        Gets the object to synchronize access to the collection.

        Get: SyncRoot(self: SettingsPropertyCollection) -> object
        """
        ...

class SettingsPropertyIsReadOnlyException(Exception):  # skipped bases: <type '_Exception'>, <type 'ISerializable'>
    """
    Provides an exception for read-only System.Configuration.SettingsProperty objects.

    SettingsPropertyIsReadOnlyException(message: str)

    SettingsPropertyIsReadOnlyException(message: str, innerException: Exception)

    SettingsPropertyIsReadOnlyException()
    """

    SerializeObjectState = None

class SettingsPropertyNotFoundException(Exception):  # skipped bases: <type '_Exception'>, <type 'ISerializable'>
    """
    Provides an exception for System.Configuration.SettingsProperty objects that are not found.

    SettingsPropertyNotFoundException(message: str)

    SettingsPropertyNotFoundException(message: str, innerException: Exception)

    SettingsPropertyNotFoundException()
    """

    SerializeObjectState = None

class SettingsPropertyValue:  # skipped bases: <type 'object'>
    """
    Contains the value of a settings property that can be loaded and stored by an instance of System.Configuration.SettingsBase.

    SettingsPropertyValue(property: SettingsProperty)
    """

    @property
    def Deserialized(self):
        """
        Gets or sets whether the value of a System.Configuration.SettingsProperty object has been deserialized.

        Get: Deserialized(self: SettingsPropertyValue) -> bool

        Set: Deserialized(self: SettingsPropertyValue) = value
        """
        ...
    @property
    def IsDirty(self):
        """
        Gets or sets whether the value of a System.Configuration.SettingsProperty object has changed.

        Get: IsDirty(self: SettingsPropertyValue) -> bool

        Set: IsDirty(self: SettingsPropertyValue) = value
        """
        ...
    @property
    def Name(self):
        """
        Gets the name of the property from the associated System.Configuration.SettingsProperty object.

        Get: Name(self: SettingsPropertyValue) -> str
        """
        ...
    @property
    def Property(self):
        """
        Gets the System.Configuration.SettingsProperty object.

        Get: Property(self: SettingsPropertyValue) -> SettingsProperty
        """
        ...
    @property
    def PropertyValue(self):
        """
        Gets or sets the value of the System.Configuration.SettingsProperty object.

        Get: PropertyValue(self: SettingsPropertyValue) -> object

        Set: PropertyValue(self: SettingsPropertyValue) = value
        """
        ...
    @property
    def SerializedValue(self):
        """
        Gets or sets the serialized value of the System.Configuration.SettingsProperty object.

        Get: SerializedValue(self: SettingsPropertyValue) -> object

        Set: SerializedValue(self: SettingsPropertyValue) = value
        """
        ...
    @property
    def UsingDefaultValue(self):
        """
        Gets a Boolean value specifying whether the value of the System.Configuration.SettingsPropertyValue object is the default value as defined by the System.Configuration.SettingsProperty.DefaultValue property value on the associated System.Configuration.SettingsProperty object.

        Get: UsingDefaultValue(self: SettingsPropertyValue) -> bool
        """
        ...

class SettingsPropertyValueCollection(object, ICloneable, ICollection):  # skipped bases: <type 'IEnumerable'>
    """
    Contains a collection of settings property values that map System.Configuration.SettingsProperty objects to System.Configuration.SettingsPropertyValue objects.

    SettingsPropertyValueCollection()
    """

    def Add(self, property):
        """
        Add(self: SettingsPropertyValueCollection, property: SettingsPropertyValue)

            Adds a System.Configuration.SettingsPropertyValue object to the collection.

            property: A System.Configuration.SettingsPropertyValue object.
        """
        ...
    def Clear(self):
        """
        Clear(self: SettingsPropertyValueCollection)

            Removes all System.Configuration.SettingsPropertyValue objects from the collection.
        """
        ...
    def GetEnumerator(self):
        """
        GetEnumerator(self: SettingsPropertyValueCollection) -> IEnumerator

            Gets the System.Collections.IEnumerator object as it applies to the collection.

            Returns: The System.Collections.IEnumerator object as it applies to the collection.
        """
        ...
    def Remove(self, name):
        """
        Remove(self: SettingsPropertyValueCollection, name: str)

            Removes a System.Configuration.SettingsPropertyValue object from the collection.

            name: The name of the System.Configuration.SettingsPropertyValue object.
        """
        ...
    def SetReadOnly(self):
        """
        SetReadOnly(self: SettingsPropertyValueCollection)

            Sets the collection to be read-only.
        """
        ...
    def __add__(self, *args):  # cannot find CLR method
        """x.__add__(y) <==> x+y"""
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
        Gets a value that specifies the number of System.Configuration.SettingsPropertyValue objects in the collection.

        Get: Count(self: SettingsPropertyValueCollection) -> int
        """
        ...
    @property
    def IsSynchronized(self):
        """
        Gets a value that indicates whether access to the collection is synchronized (thread safe).

        Get: IsSynchronized(self: SettingsPropertyValueCollection) -> bool
        """
        ...
    @property
    def SyncRoot(self):
        """
        Gets the object to synchronize access to the collection.

        Get: SyncRoot(self: SettingsPropertyValueCollection) -> object
        """
        ...

class SettingsPropertyWrongTypeException(Exception):  # skipped bases: <type '_Exception'>, <type 'ISerializable'>
    """
    Provides an exception that is thrown when an invalid type is used with a System.Configuration.SettingsProperty object.

    SettingsPropertyWrongTypeException(message: str)

    SettingsPropertyWrongTypeException(message: str, innerException: Exception)

    SettingsPropertyWrongTypeException()
    """

    SerializeObjectState = None

class SettingsProviderAttribute(Attribute):  # skipped bases: <type '_Attribute'>
    """
    Specifies the settings provider used to provide storage for the current application settings class or property. This class cannot be inherited.

    SettingsProviderAttribute(providerTypeName: str)

    SettingsProviderAttribute(providerType: Type)
    """

    @staticmethod  # known case of __new__
    def __new__(cls, *__args):
        """
        __new__(cls: type, providerTypeName: str)

        __new__(cls: type, providerType: Type)
        """
        ...
    @property
    def ProviderTypeName(self):
        """
        Gets the type name of the settings provider.

        Get: ProviderTypeName(self: SettingsProviderAttribute) -> str
        """
        ...

class SettingsProviderCollection(ProviderCollection):  # skipped bases: <type 'ICollection'>, <type 'IEnumerable'>
    """
    Represents a collection of application settings providers.

    SettingsProviderCollection()
    """

    pass

class SettingsSavingEventHandler(MulticastDelegate):  # skipped bases: <type 'ICloneable'>, <type 'ISerializable'>
    """
    Represents the method that will handle the System.Configuration.ApplicationSettingsBase.SettingsSaving event.

    SettingsSavingEventHandler(object: object, method: IntPtr)
    """

    def BeginInvoke(self, sender, e, callback, object):
        """BeginInvoke(self: SettingsSavingEventHandler, sender: object, e: CancelEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult"""
        ...
    def EndInvoke(self, result):
        """EndInvoke(self: SettingsSavingEventHandler, result: IAsyncResult)"""
        ...
    def Invoke(self, sender, e):
        """Invoke(self: SettingsSavingEventHandler, sender: object, e: CancelEventArgs)"""
        ...

class SettingsSerializeAs(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Determines the serialization scheme used to store application settings.

    enum SettingsSerializeAs, values: Binary (2), ProviderSpecific (3), String (0), Xml (1)
    """

    Binary = None
    ProviderSpecific = None
    String = None
    value__ = None
    Xml = None

class SettingsSerializeAsAttribute(Attribute):  # skipped bases: <type '_Attribute'>
    """
    Specifies the serialization mechanism that the settings provider should use. This class cannot be inherited.

    SettingsSerializeAsAttribute(serializeAs: SettingsSerializeAs)
    """

    @staticmethod  # known case of __new__
    def __new__(cls, serializeAs):
        """__new__(cls: type, serializeAs: SettingsSerializeAs)"""
        ...
    @property
    def SerializeAs(self):
        """
        Gets the System.Configuration.SettingsSerializeAs enumeration value that specifies the serialization scheme.

        Get: SerializeAs(self: SettingsSerializeAsAttribute) -> SettingsSerializeAs
        """
        ...

class SettingValueElement(ConfigurationElement):
    """
    Contains the XML representing the serialized value of the setting. This class cannot be inherited.

    SettingValueElement()
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
    def ValueXml(self):
        """
        Gets or sets the value of a System.Configuration.SettingValueElement object by using an System.Xml.XmlNode object.

        Get: ValueXml(self: SettingValueElement) -> XmlNode

        Set: ValueXml(self: SettingValueElement) = value
        """
        ...

class SingleTagSectionHandler(object, IConfigurationSectionHandler):
    """
    Handles configuration sections that are represented by a single XML tag in the .config file.

    SingleTagSectionHandler()
    """

    pass

class SpecialSetting(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies the special setting category of a application settings property.

    enum SpecialSetting, values: ConnectionString (0), WebServiceUrl (1)
    """

    ConnectionString = None
    value__ = None
    WebServiceUrl = None

class SpecialSettingAttribute(Attribute):  # skipped bases: <type '_Attribute'>
    """
    Indicates that an application settings property has a special significance. This class cannot be inherited.

    SpecialSettingAttribute(specialSetting: SpecialSetting)
    """

    @staticmethod  # known case of __new__
    def __new__(cls, specialSetting):
        """__new__(cls: type, specialSetting: SpecialSetting)"""
        ...
    @property
    def SpecialSetting(self):
        """
        Gets the value describing the special setting category of the application settings property.

        Get: SpecialSetting(self: SpecialSettingAttribute) -> SpecialSetting
        """
        ...

class UriSection(ConfigurationSection):
    """
    Represents the Uri section within a configuration file.

    UriSection()
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
    def Idn(self):
        """
        Gets an System.Configuration.IdnElement object that contains the configuration setting for International Domain Name (IDN) processing in the System.Uri class.

        Get: Idn(self: UriSection) -> IdnElement
        """
        ...
    @property
    def IriParsing(self):
        """
        Gets an System.Configuration.IriParsingElement object that contains the configuration setting for International Resource Identifiers (IRI) parsing in the System.Uri class.

        Get: IriParsing(self: UriSection) -> IriParsingElement
        """
        ...
    @property
    def Properties(self): ...
    @property
    def SchemeSettings(self):
        """
        Gets a System.Configuration.SchemeSettingElementCollection object that contains the configuration settings for scheme parsing in the System.Uri class.

        Get: SchemeSettings(self: UriSection) -> SchemeSettingElementCollection
        """
        ...

class UserScopedSettingAttribute(SettingAttribute):  # skipped bases: <type '_Attribute'>
    """
    Specifies that an application settings group or property contains distinct values for each user of an application. This class cannot be inherited.

    UserScopedSettingAttribute()
    """

    pass

class UserSettingsGroup(ConfigurationSectionGroup):
    """
    Represents a grouping of related user settings sections within a configuration file. This class cannot be inherited.

    UserSettingsGroup()
    """

    pass

# variables with complex values
