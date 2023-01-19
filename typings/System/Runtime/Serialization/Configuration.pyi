# encoding: utf-8
# module System.Runtime.Serialization.Configuration calls itself Configuration
# from System.Runtime.Serialization, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class DataContractSerializerSection(ConfigurationSection):
    """
    Handles the XML elements used to configure serialization by the System.Runtime.Serialization.DataContractSerializer.

    DataContractSerializerSection()
    """

    @property
    def DeclaredTypes(self):
        """
        Gets a collection of types added to the System.Runtime.Serialization.DataContractSerializer.KnownTypes property.

        Get: DeclaredTypes(self: DataContractSerializerSection) -> DeclaredTypeElementCollection
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

class DeclaredTypeElement(ConfigurationElement):
    """
    Handles the XML elements used to add known types that are used for serialization by the System.Runtime.Serialization.DataContractSerializer.

    DeclaredTypeElement()

    DeclaredTypeElement(typeName: str)
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
    def KnownTypes(self):
        """
        Gets the collection of known types.

        Get: KnownTypes(self: DeclaredTypeElement) -> TypeElementCollection
        """
        ...
    @property
    def Properties(self): ...
    @property
    def Type(self):
        """
        Gets or sets the name of the declared type that requires a collection of known types.

        Get: Type(self: DeclaredTypeElement) -> str

        Set: Type(self: DeclaredTypeElement) = value
        """
        ...

class DeclaredTypeElementCollection(
    ConfigurationElementCollection
):  # skipped bases: <type 'ICollection'>, <type 'IEnumerable'>
    """
    Handles the XML elements used to configure XML serialization using the System.Runtime.Serialization.DataContractSerializer.

    DeclaredTypeElementCollection()
    """

    def Add(self, element):
        """
        Add(self: DeclaredTypeElementCollection, element: DeclaredTypeElement)

            Adds a specified configuration element to the collection.

            element: The configuration element to add.
        """
        ...
    def Clear(self):
        """
        Clear(self: DeclaredTypeElementCollection)

            Removes all members of the collection.
        """
        ...
    def Contains(self, typeName):
        """
        Contains(self: DeclaredTypeElementCollection, typeName: str) -> bool

            Returns a value that specifies whether the element is in the collection.

            typeName: The name of the type to check for.

            Returns: ue if the element is in the collection; otherwise, lse.
        """
        ...
    def IndexOf(self, element):
        """
        IndexOf(self: DeclaredTypeElementCollection, element: DeclaredTypeElement) -> int

            Returns the position of the specified configuration element.

            element: The element to find in the collection.

            Returns: The index of the specified configuration element; otherwise, -1.
        """
        ...
    def Remove(self, *__args):
        """
        Remove(self: DeclaredTypeElementCollection, element: DeclaredTypeElement)

            Removes the specified configuration element from the collection.

            element: The System.Runtime.Serialization.Configuration.DeclaredTypeElement to remove.

        Remove(self: DeclaredTypeElementCollection, typeName: str)

            Removes the element specified by its key from the collection.

            typeName: The name of the type (which functions as a key) to remove from the collection.
        """
        ...
    def RemoveAt(self, index):
        """
        RemoveAt(self: DeclaredTypeElementCollection, index: int)

            Removes the configuration element found at the specified position.

            index: The position of the configuration element to remove.
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

class NetDataContractSerializerSection(ConfigurationSection):
    """
    Handles the XML elements used to configure serialization by the System.Runtime.Serialization.NetDataContractSerializer.

    NetDataContractSerializerSection()
    """

    @property
    def ElementProperty(self):
        """Gets the System.Configuration.ConfigurationElementProperty object that represents the System.Configuration.ConfigurationElement object itself."""
        ...
    @property
    def EnableUnsafeTypeForwarding(self):
        """
        Gets a value that indicates whether unsafe type forwarding is enabled.

        Get: EnableUnsafeTypeForwarding(self: NetDataContractSerializerSection) -> bool
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

class ParameterElement(ConfigurationElement):
    """
    Handles the XML elements used to configure XML serialization by the System.Runtime.Serialization.DataContractSerializer.

    ParameterElement()

    ParameterElement(typeName: str)

    ParameterElement(index: int)
    """

    @staticmethod  # known case of __new__
    def __new__(cls, *__args):
        """
        __new__(cls: type)

        __new__(cls: type, typeName: str)

        __new__(cls: type, index: int)
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
    def Index(self):
        """
        Gets or sets the position of the generic known type.

        Get: Index(self: ParameterElement) -> int

        Set: Index(self: ParameterElement) = value
        """
        ...
    @property
    def Parameters(self):
        """
        Gets the collection of parameters.

        Get: Parameters(self: ParameterElement) -> ParameterElementCollection
        """
        ...
    @property
    def Properties(self): ...
    @property
    def Type(self):
        """
        Gets or sets the type name of the parameter of the generic known type.

        Get: Type(self: ParameterElement) -> str

        Set: Type(self: ParameterElement) = value
        """
        ...

class ParameterElementCollection(
    ConfigurationElementCollection
):  # skipped bases: <type 'ICollection'>, <type 'IEnumerable'>
    """
    Handles the XML elements used to configure serialization by the System.Runtime.Serialization.DataContractSerializer.

    ParameterElementCollection()
    """

    def Add(self, element):
        """
        Add(self: ParameterElementCollection, element: ParameterElement)

            Adds an element to the collection of parameter elements.

            element: The System.Runtime.Serialization.Configuration.ParameterElement element to add to the collection.
        """
        ...
    def Clear(self):
        """
        Clear(self: ParameterElementCollection)

            Removes all members of the collection.
        """
        ...
    def Contains(self, typeName):
        """
        Contains(self: ParameterElementCollection, typeName: str) -> bool

            Gets or sets a value specifying whether the named type is found in the collection.

            typeName: The name of the type to find.

            Returns: ue if the element is present; otherwise, lse.
        """
        ...
    def IndexOf(self, element):
        """
        IndexOf(self: ParameterElementCollection, element: ParameterElement) -> int

            Gets the position of the specified element in the collection.

            element: The System.Runtime.Serialization.Configuration.ParameterElement element to find.

            Returns: The position of the specified element.
        """
        ...
    def Remove(self, element):
        """
        Remove(self: ParameterElementCollection, element: ParameterElement)

            Removes the specified element from the collection.

            element: The System.Runtime.Serialization.Configuration.ParameterElement to remove.
        """
        ...
    def RemoveAt(self, index):
        """
        RemoveAt(self: ParameterElementCollection, index: int)

            Removes the element at the specified position.

            index: The position of the element to remove.
        """
        ...
    def __add__(self, *args):  # cannot find CLR method
        """x.__add__(y) <==> x+y"""
        ...
    def __getitem__(self, *args):  # cannot find CLR method
        """x.__getitem__(y) <==> x[y]"""
        ...
    def __setitem__(self, *args):  # cannot find CLR method
        """x.__setitem__(i, y) <==> x[i]="""
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
        Gets the type of the parameters collection in configuration.

        Get: CollectionType(self: ParameterElementCollection) -> ConfigurationElementCollectionType
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

class SerializationSectionGroup(ConfigurationSectionGroup):
    """
    Handles the XML elements used to configure serialization by the System.Runtime.Serialization.DataContractSerializer.

    SerializationSectionGroup()
    """

    @staticmethod
    def GetSectionGroup(config):
        """
        GetSectionGroup(config: Configuration) -> SerializationSectionGroup

            Gets the serialization configuration section for the specified configuration.

            config: A System.Configuration.Configuration that represents the configuration to retrieve.

            Returns: A System.Runtime.Serialization.Configuration.SerializationSectionGroup that represents the configuration section.
        """
        ...
    @property
    def DataContractSerializer(self):
        """
        Gets the System.Runtime.Serialization.Configuration.DataContractSerializerSection used to set up the known types collection.

        Get: DataContractSerializer(self: SerializationSectionGroup) -> DataContractSerializerSection
        """
        ...
    @property
    def NetDataContractSerializer(self):
        """
        Gets the System.Runtime.Serialization.Configuration.NetDataContractSerializerSection used to set up the known types collection.

        Get: NetDataContractSerializer(self: SerializationSectionGroup) -> NetDataContractSerializerSection
        """
        ...

class TypeElement(ConfigurationElement):
    """
    Handles the XML elements used to configure serialization by the System.Runtime.Serialization.DataContractSerializer.

    TypeElement()

    TypeElement(typeName: str)
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
    def Index(self):
        """
        Gets or sets the position of the element.

        Get: Index(self: TypeElement) -> int

        Set: Index(self: TypeElement) = value
        """
        ...
    @property
    def Parameters(self):
        """
        Gets a collection of parameters.

        Get: Parameters(self: TypeElement) -> ParameterElementCollection
        """
        ...
    @property
    def Properties(self): ...
    @property
    def Type(self):
        """
        Gets or sets the name of the type.

        Get: Type(self: TypeElement) -> str

        Set: Type(self: TypeElement) = value
        """
        ...

class TypeElementCollection(
    ConfigurationElementCollection
):  # skipped bases: <type 'ICollection'>, <type 'IEnumerable'>
    """
    Handles the XML elements used to configure the known types used for serialization by the System.Runtime.Serialization.DataContractSerializer.

    TypeElementCollection()
    """

    def Add(self, element):
        """
        Add(self: TypeElementCollection, element: TypeElement)

            Adds the specified element to the collection.

            element: A System.Runtime.Serialization.Configuration.TypeElement that represents the known type to add.
        """
        ...
    def Clear(self):
        """
        Clear(self: TypeElementCollection)

            Removes all members of the collection.
        """
        ...
    def IndexOf(self, element):
        """
        IndexOf(self: TypeElementCollection, element: TypeElement) -> int

            Returns the position of the specified element.

            element: The System.Runtime.Serialization.Configuration.TypeElement to find in the collection.

            Returns: The position of the specified element.
        """
        ...
    def Remove(self, element):
        """
        Remove(self: TypeElementCollection, element: TypeElement)

            Removes the specified element from the collection.

            element: The System.Runtime.Serialization.Configuration.TypeElement to remove.
        """
        ...
    def RemoveAt(self, index):
        """
        RemoveAt(self: TypeElementCollection, index: int)

            Removes the element at the specified position.

            index: The position in the collection from which to remove the element.
        """
        ...
    def __add__(self, *args):  # cannot find CLR method
        """x.__add__(y) <==> x+y"""
        ...
    def __getitem__(self, *args):  # cannot find CLR method
        """x.__getitem__(y) <==> x[y]"""
        ...
    def __setitem__(self, *args):  # cannot find CLR method
        """x.__setitem__(i, y) <==> x[i]="""
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
        Gets the collection of elements that represents the types using known types.

        Get: CollectionType(self: TypeElementCollection) -> ConfigurationElementCollectionType
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
