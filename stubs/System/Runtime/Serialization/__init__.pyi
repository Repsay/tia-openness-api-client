# encoding: utf-8
# module System.Runtime.Serialization calls itself Serialization
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.Runtime.Serialization, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class CollectionDataContractAttribute(Attribute):  # skipped bases: <type '_Attribute'>
    """
    When applied to a collection type, enables custom specification of the collection item elements. This attribute can be applied only to types that are recognized by the System.Runtime.Serialization.DataContractSerializer as valid, serializable collections.

    CollectionDataContractAttribute()
    """

    @property
    def IsItemNameSetExplicitly(self):
        """
        Gets whether System.Runtime.Serialization.CollectionDataContractAttribute.ItemName has been explicitly set.

        Get: IsItemNameSetExplicitly(self: CollectionDataContractAttribute) -> bool
        """
        ...
    @property
    def IsKeyNameSetExplicitly(self):
        """
        Gets whether System.Runtime.Serialization.CollectionDataContractAttribute.KeyName has been explicitly set.

        Get: IsKeyNameSetExplicitly(self: CollectionDataContractAttribute) -> bool
        """
        ...
    @property
    def IsNameSetExplicitly(self):
        """
        Gets whether System.Runtime.Serialization.CollectionDataContractAttribute.Name has been explicitly set.

        Get: IsNameSetExplicitly(self: CollectionDataContractAttribute) -> bool
        """
        ...
    @property
    def IsNamespaceSetExplicitly(self):
        """
        Gets whether System.Runtime.Serialization.CollectionDataContractAttribute.Namespace has been explicitly set.

        Get: IsNamespaceSetExplicitly(self: CollectionDataContractAttribute) -> bool
        """
        ...
    @property
    def IsReference(self):
        """
        Gets or sets a value that indicates whether to preserve object reference data.

        Get: IsReference(self: CollectionDataContractAttribute) -> bool

        Set: IsReference(self: CollectionDataContractAttribute) = value
        """
        ...
    @property
    def IsReferenceSetExplicitly(self):
        """
        Gets whether reference has been explicitly set.

        Get: IsReferenceSetExplicitly(self: CollectionDataContractAttribute) -> bool
        """
        ...
    @property
    def IsValueNameSetExplicitly(self):
        """
        Gets whether System.Runtime.Serialization.CollectionDataContractAttribute.ValueName has been explicitly set.

        Get: IsValueNameSetExplicitly(self: CollectionDataContractAttribute) -> bool
        """
        ...
    @property
    def ItemName(self):
        """
        Gets or sets a custom name for a collection element.

        Get: ItemName(self: CollectionDataContractAttribute) -> str

        Set: ItemName(self: CollectionDataContractAttribute) = value
        """
        ...
    @property
    def KeyName(self):
        """
        Gets or sets the custom name for a dictionary key name.

        Get: KeyName(self: CollectionDataContractAttribute) -> str

        Set: KeyName(self: CollectionDataContractAttribute) = value
        """
        ...
    @property
    def Name(self):
        """
        Gets or sets the data contract name for the collection type.

        Get: Name(self: CollectionDataContractAttribute) -> str

        Set: Name(self: CollectionDataContractAttribute) = value
        """
        ...
    @property
    def Namespace(self):
        """
        Gets or sets the namespace for the data contract.

        Get: Namespace(self: CollectionDataContractAttribute) -> str

        Set: Namespace(self: CollectionDataContractAttribute) = value
        """
        ...
    @property
    def ValueName(self):
        """
        Gets or sets the custom name for a dictionary value name.

        Get: ValueName(self: CollectionDataContractAttribute) -> str

        Set: ValueName(self: CollectionDataContractAttribute) = value
        """
        ...

class ContractNamespaceAttribute(Attribute):  # skipped bases: <type '_Attribute'>
    """
    Specifies the CLR namespace and XML namespace of the data contract.

    ContractNamespaceAttribute(contractNamespace: str)
    """

    @staticmethod  # known case of __new__
    def __new__(cls, contractNamespace):
        """__new__(cls: type, contractNamespace: str)"""
        ...
    @property
    def ClrNamespace(self):
        """
        Gets or sets the CLR namespace of the data contract type.

        Get: ClrNamespace(self: ContractNamespaceAttribute) -> str

        Set: ClrNamespace(self: ContractNamespaceAttribute) = value
        """
        ...
    @property
    def ContractNamespace(self):
        """
        Gets the namespace of the data contract members.

        Get: ContractNamespace(self: ContractNamespaceAttribute) -> str
        """
        ...

class DataContractAttribute(Attribute):  # skipped bases: <type '_Attribute'>
    """
    Specifies that the type defines or implements a data contract and is serializable by a serializer, such as the System.Runtime.Serialization.DataContractSerializer. To make their type serializable, type authors must define a data contract for their type.

    DataContractAttribute()
    """

    @property
    def IsNameSetExplicitly(self):
        """
        Gets whether System.Runtime.Serialization.DataContractAttribute.Name has been explicitly set.

        Get: IsNameSetExplicitly(self: DataContractAttribute) -> bool
        """
        ...
    @property
    def IsNamespaceSetExplicitly(self):
        """
        Gets whether System.Runtime.Serialization.DataContractAttribute.Namespace has been explicitly set.

        Get: IsNamespaceSetExplicitly(self: DataContractAttribute) -> bool
        """
        ...
    @property
    def IsReference(self):
        """
        Gets or sets a value that indicates whether to preserve object reference data.

        Get: IsReference(self: DataContractAttribute) -> bool

        Set: IsReference(self: DataContractAttribute) = value
        """
        ...
    @property
    def IsReferenceSetExplicitly(self):
        """
        Gets whether System.Runtime.Serialization.DataContractAttribute.IsReference has been explicitly set.

        Get: IsReferenceSetExplicitly(self: DataContractAttribute) -> bool
        """
        ...
    @property
    def Name(self):
        """
        Gets or sets the name of the data contract for the type.

        Get: Name(self: DataContractAttribute) -> str

        Set: Name(self: DataContractAttribute) = value
        """
        ...
    @property
    def Namespace(self):
        """
        Gets or sets the namespace for the data contract for the type.

        Get: Namespace(self: DataContractAttribute) -> str

        Set: Namespace(self: DataContractAttribute) = value
        """
        ...

class DataContractResolver:  # skipped bases: <type 'object'>
    """Provides a mechanism for dynamically mapping types to and from i:type representations during serialization and deserialization."""

    def ResolveName(self, typeName, typeNamespace, declaredType, knownTypeResolver):
        """
        ResolveName(self: DataContractResolver, typeName: str, typeNamespace: str, declaredType: Type, knownTypeResolver: DataContractResolver) -> Type

            Override this method to map the specified i:type name and namespace to a data contract type during deserialization.

            typeName: The i:type name to map.

            typeNamespace: The i:type namespace to map.

            declaredType: The type declared in the data contract.

            knownTypeResolver: The known type resolver.

            Returns: The type the i:type name and namespace is mapped to.
        """
        ...
    def TryResolveType(self, type, declaredType, knownTypeResolver, typeName, typeNamespace):
        """
        TryResolveType(self: DataContractResolver, type: Type, declaredType: Type, knownTypeResolver: DataContractResolver) -> (bool, XmlDictionaryString, XmlDictionaryString)

            Override this method to map a data contract type to an i:type name and namespace during serialization.

            type: The type to map.

            declaredType: The type declared in the data contract.

            knownTypeResolver: The known type resolver.

            Returns: ue if mapping succeeded; otherwise, lse.
        """
        ...

class XmlObjectSerializer:  # skipped bases: <type 'object'>
    """Provides the base class used to serialize objects as XML streams or documents. This class is abstract."""

    def IsStartObject(self, reader):
        """
        IsStartObject(self: XmlObjectSerializer, reader: XmlReader) -> bool

            Gets a value that specifies whether the System.Xml.XmlReader is positioned over an XML element that can be read.

            reader: An System.Xml.XmlReader used to read the XML stream or document.

            Returns: ue if the reader is positioned over the starting element; otherwise, lse.

        IsStartObject(self: XmlObjectSerializer, reader: XmlDictionaryReader) -> bool

            Gets a value that specifies whether the System.Xml.XmlDictionaryReader is positioned over an XML element that can be read.

            reader: An System.Xml.XmlDictionaryReader used to read the XML stream or document.

            Returns: ue if the reader can read the data; otherwise, lse.
        """
        ...
    def ReadObject(self, *__args):
        """
        ReadObject(self: XmlObjectSerializer, reader: XmlDictionaryReader) -> object

            Reads the XML document or stream with an System.Xml.XmlDictionaryReader and returns the deserialized object.

            reader: An System.Xml.XmlDictionaryReader used to read the XML document.

            Returns: The deserialized object.

        ReadObject(self: XmlObjectSerializer, stream: Stream) -> object

            Reads the XML stream or document with a System.IO.Stream and returns the deserialized object.

            stream: A System.IO.Stream used to read the XML stream or document.

            Returns: The deserialized object.

        ReadObject(self: XmlObjectSerializer, reader: XmlReader) -> object

            Reads the XML document or stream with an System.Xml.XmlReader and returns the deserialized object.

            reader: An System.Xml.XmlReader used to read the XML stream or document.

            Returns: The deserialized object.

        ReadObject(self: XmlObjectSerializer, reader: XmlReader, verifyObjectName: bool) -> object

            Reads the XML document or stream with an System.Xml.XmlReader and returns the deserialized object; it also enables you to specify whether the serializer can read the

             data before attempting to read it.

            reader: An System.Xml.XmlReader used to read the XML document or stream.

            verifyObjectName: ue to check whether the enclosing XML element name and namespace correspond to the root name and root namespace; lse to skip the verification.

            Returns: The deserialized object.

        ReadObject(self: XmlObjectSerializer, reader: XmlDictionaryReader, verifyObjectName: bool) -> object

            Reads the XML stream or document with an System.Xml.XmlDictionaryReader and returns the deserialized object; it also enables you to specify whether the serializer can

             read the data before attempting to read it.

            reader: An System.Xml.XmlDictionaryReader used to read the XML document.

            verifyObjectName: ue to check whether the enclosing XML element name and namespace correspond to the root name and root namespace; otherwise, lse to skip the verification.

            Returns: The deserialized object.
        """
        ...
    def WriteEndObject(self, writer):
        """
        WriteEndObject(self: XmlObjectSerializer, writer: XmlDictionaryWriter)

            Writes the end of the object data as a closing XML element to the XML document or stream with an System.Xml.XmlDictionaryWriter.

            writer: An System.Xml.XmlDictionaryWriter used to write the XML document or stream.

        WriteEndObject(self: XmlObjectSerializer, writer: XmlWriter)

            Writes the end of the object data as a closing XML element to the XML document or stream with an System.Xml.XmlWriter.

            writer: An System.Xml.XmlWriter used to write the XML document or stream.
        """
        ...
    def WriteObject(self, *__args):
        """
        WriteObject(self: XmlObjectSerializer, writer: XmlDictionaryWriter, graph: object)

            Writes the complete content (start, content, and end) of the object to the XML document or stream with the specified System.Xml.XmlDictionaryWriter.

            writer: An System.Xml.XmlDictionaryWriter used to write the content to the XML document or stream.

            graph: The object that contains the content to write.

        WriteObject(self: XmlObjectSerializer, stream: Stream, graph: object)

            Writes the complete content (start, content, and end) of the object to the XML document or stream with the specified System.IO.Stream.

            stream: A System.IO.Stream used to write the XML document or stream.

            graph: The object that contains the data to write to the stream.

        WriteObject(self: XmlObjectSerializer, writer: XmlWriter, graph: object)

            Writes the complete content (start, content, and end) of the object to the XML document or stream with the specified System.Xml.XmlWriter.

            writer: An System.Xml.XmlWriter used to write the XML document or stream.

            graph: The object that contains the content to write.
        """
        ...
    def WriteObjectContent(self, writer, graph):
        """
        WriteObjectContent(self: XmlObjectSerializer, writer: XmlDictionaryWriter, graph: object)

            Writes only the content of the object to the XML document or stream using the specified System.Xml.XmlDictionaryWriter.

            writer: An System.Xml.XmlDictionaryWriter used to write the XML document or stream.

            graph: The object that contains the content to write.

        WriteObjectContent(self: XmlObjectSerializer, writer: XmlWriter, graph: object)

            Writes only the content of the object to the XML document or stream with the specified System.Xml.XmlWriter.

            writer: An System.Xml.XmlWriter used to write the XML document or stream.

            graph: The object that contains the content to write.
        """
        ...
    def WriteStartObject(self, writer, graph):
        """
        WriteStartObject(self: XmlObjectSerializer, writer: XmlDictionaryWriter, graph: object)

            Writes the start of the object's data as an opening XML element using the specified System.Xml.XmlDictionaryWriter.

            writer: An System.Xml.XmlDictionaryWriter used to write the XML document.

            graph: The object to serialize.

        WriteStartObject(self: XmlObjectSerializer, writer: XmlWriter, graph: object)

            Writes the start of the object's data as an opening XML element using the specified System.Xml.XmlWriter.

            writer: An System.Xml.XmlWriter used to write the XML document.

            graph: The object to serialize.
        """
        ...

class DataContractSerializer(XmlObjectSerializer):
    """
    Serializes and deserializes an instance of a type into an XML stream or document using a supplied data contract. This class cannot be inherited.

    DataContractSerializer(type: Type)

    DataContractSerializer(type: Type, knownTypes: IEnumerable[Type])

    DataContractSerializer(type: Type, knownTypes: IEnumerable[Type], maxItemsInObjectGraph: int, ignoreExtensionDataObject: bool, preserveObjectReferences: bool, dataContractSurrogate: IDataContractSurrogate)

    DataContractSerializer(type: Type, knownTypes: IEnumerable[Type], maxItemsInObjectGraph: int, ignoreExtensionDataObject: bool, preserveObjectReferences: bool, dataContractSurrogate: IDataContractSurrogate, dataContractResolver: DataContractResolver)

    DataContractSerializer(type: Type, rootName: str, rootNamespace: str)

    DataContractSerializer(type: Type, rootName: str, rootNamespace: str, knownTypes: IEnumerable[Type])

    DataContractSerializer(type: Type, rootName: str, rootNamespace: str, knownTypes: IEnumerable[Type], maxItemsInObjectGraph: int, ignoreExtensionDataObject: bool, preserveObjectReferences: bool, dataContractSurrogate: IDataContractSurrogate)

    DataContractSerializer(type: Type, rootName: str, rootNamespace: str, knownTypes: IEnumerable[Type], maxItemsInObjectGraph: int, ignoreExtensionDataObject: bool, preserveObjectReferences: bool, dataContractSurrogate: IDataContractSurrogate, dataContractResolver: DataContractResolver)

    DataContractSerializer(type: Type, rootName: XmlDictionaryString, rootNamespace: XmlDictionaryString)

    DataContractSerializer(type: Type, rootName: XmlDictionaryString, rootNamespace: XmlDictionaryString, knownTypes: IEnumerable[Type])

    DataContractSerializer(type: Type, rootName: XmlDictionaryString, rootNamespace: XmlDictionaryString, knownTypes: IEnumerable[Type], maxItemsInObjectGraph: int, ignoreExtensionDataObject: bool, preserveObjectReferences: bool, dataContractSurrogate: IDataContractSurrogate)

    DataContractSerializer(type: Type, rootName: XmlDictionaryString, rootNamespace: XmlDictionaryString, knownTypes: IEnumerable[Type], maxItemsInObjectGraph: int, ignoreExtensionDataObject: bool, preserveObjectReferences: bool, dataContractSurrogate: IDataContractSurrogate, dataContractResolver: DataContractResolver)

    DataContractSerializer(type: Type, settings: DataContractSerializerSettings)
    """

    @staticmethod  # known case of __new__
    def __new__(cls, type, *__args):
        """
        __new__(cls: type, type: Type)

        __new__(cls: type, type: Type, knownTypes: IEnumerable[Type])

        __new__(cls: type, type: Type, knownTypes: IEnumerable[Type], maxItemsInObjectGraph: int, ignoreExtensionDataObject: bool, preserveObjectReferences: bool, dataContractSurrogate: IDataContractSurrogate)

        __new__(cls: type, type: Type, knownTypes: IEnumerable[Type], maxItemsInObjectGraph: int, ignoreExtensionDataObject: bool, preserveObjectReferences: bool, dataContractSurrogate: IDataContractSurrogate, dataContractResolver: DataContractResolver)

        __new__(cls: type, type: Type, rootName: str, rootNamespace: str)

        __new__(cls: type, type: Type, rootName: str, rootNamespace: str, knownTypes: IEnumerable[Type])

        __new__(cls: type, type: Type, rootName: str, rootNamespace: str, knownTypes: IEnumerable[Type], maxItemsInObjectGraph: int, ignoreExtensionDataObject: bool, preserveObjectReferences: bool, dataContractSurrogate: IDataContractSurrogate)

        __new__(cls: type, type: Type, rootName: str, rootNamespace: str, knownTypes: IEnumerable[Type], maxItemsInObjectGraph: int, ignoreExtensionDataObject: bool, preserveObjectReferences: bool, dataContractSurrogate: IDataContractSurrogate, dataContractResolver: DataContractResolver)

        __new__(cls: type, type: Type, rootName: XmlDictionaryString, rootNamespace: XmlDictionaryString)

        __new__(cls: type, type: Type, rootName: XmlDictionaryString, rootNamespace: XmlDictionaryString, knownTypes: IEnumerable[Type])

        __new__(cls: type, type: Type, rootName: XmlDictionaryString, rootNamespace: XmlDictionaryString, knownTypes: IEnumerable[Type], maxItemsInObjectGraph: int, ignoreExtensionDataObject: bool, preserveObjectReferences: bool, dataContractSurrogate: IDataContractSurrogate)

        __new__(cls: type, type: Type, rootName: XmlDictionaryString, rootNamespace: XmlDictionaryString, knownTypes: IEnumerable[Type], maxItemsInObjectGraph: int, ignoreExtensionDataObject: bool, preserveObjectReferences: bool, dataContractSurrogate: IDataContractSurrogate, dataContractResolver: DataContractResolver)

        __new__(cls: type, type: Type, settings: DataContractSerializerSettings)
        """
        ...
    @property
    def DataContractResolver(self):
        """
        Gets the component used to dynamically map i:type declarations to known contract types.

        Get: DataContractResolver(self: DataContractSerializer) -> DataContractResolver
        """
        ...
    @property
    def DataContractSurrogate(self):
        """
        Gets a surrogate type that can extend the serialization or deserialization process.

        Get: DataContractSurrogate(self: DataContractSerializer) -> IDataContractSurrogate
        """
        ...
    @property
    def IgnoreExtensionDataObject(self):
        """
        Gets a value that specifies whether to ignore data supplied by an extension of the class when the class is being serialized or deserialized.

        Get: IgnoreExtensionDataObject(self: DataContractSerializer) -> bool
        """
        ...
    @property
    def KnownTypes(self):
        """
        Gets a collection of types that may be present in the object graph serialized using this instance of the System.Runtime.Serialization.DataContractSerializer.

        Get: KnownTypes(self: DataContractSerializer) -> ReadOnlyCollection[Type]
        """
        ...
    @property
    def MaxItemsInObjectGraph(self):
        """
        Gets the maximum number of items in an object graph to serialize or deserialize.

        Get: MaxItemsInObjectGraph(self: DataContractSerializer) -> int
        """
        ...
    @property
    def PreserveObjectReferences(self):
        """
        Gets a value that specifies whether to use non-standard XML constructs to preserve object reference data.

        Get: PreserveObjectReferences(self: DataContractSerializer) -> bool
        """
        ...
    @property
    def SerializeReadOnlyTypes(self):
        """
        Gets a value that specifies whether read-only types are serialized.

        Get: SerializeReadOnlyTypes(self: DataContractSerializer) -> bool
        """
        ...

class DataContractSerializerExtensions:  # skipped bases: <type 'object'>
    """Extends the System.Runtime.Serialization.DataContractSerializer class by providing methods for setting and getting an System.Runtime.Serialization.ISerializationSurrogateProvider."""

    @staticmethod
    def GetSerializationSurrogateProvider(serializer):
        """
        GetSerializationSurrogateProvider(serializer: DataContractSerializer) -> ISerializationSurrogateProvider

            Returns the surrogate serialization provider for this serializer.

            serializer: The serializer which is being surrogated.

            Returns: The surrogate serializer.
        """
        ...
    @staticmethod
    def SetSerializationSurrogateProvider(serializer, provider):
        """
        SetSerializationSurrogateProvider(serializer: DataContractSerializer, provider: ISerializationSurrogateProvider)

            Specifies a surrogate serialization provider for this System.Runtime.Serialization.DataContractSerializer.

            serializer: The serializer which is being surrogated.

            provider: The surrogate serialization provider.
        """
        ...
    __all__ = [
        "GetSerializationSurrogateProvider",
        "SetSerializationSurrogateProvider",
    ]

class DataContractSerializerSettings:  # skipped bases: <type 'object'>
    """
    Specifies data contract serializer settings.

    DataContractSerializerSettings()
    """

    @property
    def DataContractResolver(self):
        """
        Gets or sets the component used to dynamically map xsi:type declarations to known contract types.

        Get: DataContractResolver(self: DataContractSerializerSettings) -> DataContractResolver

        Set: DataContractResolver(self: DataContractSerializerSettings) = value
        """
        ...
    @property
    def DataContractSurrogate(self):
        """
        Gets or sets a serialization surrogate.

        Get: DataContractSurrogate(self: DataContractSerializerSettings) -> IDataContractSurrogate

        Set: DataContractSurrogate(self: DataContractSerializerSettings) = value
        """
        ...
    @property
    def IgnoreExtensionDataObject(self):
        """
        Gets or sets a value that specifies whether to ignore data supplied by an extension of the class when the class is being serialized or deserialized.

        Get: IgnoreExtensionDataObject(self: DataContractSerializerSettings) -> bool

        Set: IgnoreExtensionDataObject(self: DataContractSerializerSettings) = value
        """
        ...
    @property
    def KnownTypes(self):
        """
        Gets or sets a collection of types that may be present in the object graph serialized using this instance of the DataContractSerializerSettings.

        Get: KnownTypes(self: DataContractSerializerSettings) -> IEnumerable[Type]

        Set: KnownTypes(self: DataContractSerializerSettings) = value
        """
        ...
    @property
    def MaxItemsInObjectGraph(self):
        """
        Gets or sets the maximum number of items in an object graph to serialize or deserialize.

        Get: MaxItemsInObjectGraph(self: DataContractSerializerSettings) -> int

        Set: MaxItemsInObjectGraph(self: DataContractSerializerSettings) = value
        """
        ...
    @property
    def PreserveObjectReferences(self):
        """
        Gets or sets a value that specifies whether to use non-standard XML constructs to preserve object reference data.

        Get: PreserveObjectReferences(self: DataContractSerializerSettings) -> bool

        Set: PreserveObjectReferences(self: DataContractSerializerSettings) = value
        """
        ...
    @property
    def RootName(self):
        """
        Gets or sets the root name of the selected object.

        Get: RootName(self: DataContractSerializerSettings) -> XmlDictionaryString

        Set: RootName(self: DataContractSerializerSettings) = value
        """
        ...
    @property
    def RootNamespace(self):
        """
        Gets or sets the root namespace for the specified object.

        Get: RootNamespace(self: DataContractSerializerSettings) -> XmlDictionaryString

        Set: RootNamespace(self: DataContractSerializerSettings) = value
        """
        ...
    @property
    def SerializeReadOnlyTypes(self):
        """
        Gets or sets a value that specifies whether to serialize read only types.

        Get: SerializeReadOnlyTypes(self: DataContractSerializerSettings) -> bool

        Set: SerializeReadOnlyTypes(self: DataContractSerializerSettings) = value
        """
        ...

class DataMemberAttribute(Attribute):  # skipped bases: <type '_Attribute'>
    """
    When applied to the member of a type, specifies that the member is part of a data contract and is serializable by the System.Runtime.Serialization.DataContractSerializer.

    DataMemberAttribute()
    """

    @property
    def EmitDefaultValue(self):
        """
        Gets or sets a value that specifies whether to serialize the default value for a field or property being serialized.

        Get: EmitDefaultValue(self: DataMemberAttribute) -> bool

        Set: EmitDefaultValue(self: DataMemberAttribute) = value
        """
        ...
    @property
    def IsNameSetExplicitly(self):
        """
        Gets whether System.Runtime.Serialization.DataMemberAttribute.Name has been explicitly set.

        Get: IsNameSetExplicitly(self: DataMemberAttribute) -> bool
        """
        ...
    @property
    def IsRequired(self):
        """
        Gets or sets a value that instructs the serialization engine that the member must be present when reading or deserializing.

        Get: IsRequired(self: DataMemberAttribute) -> bool

        Set: IsRequired(self: DataMemberAttribute) = value
        """
        ...
    @property
    def Name(self):
        """
        Gets or sets a data member name.

        Get: Name(self: DataMemberAttribute) -> str

        Set: Name(self: DataMemberAttribute) = value
        """
        ...
    @property
    def Order(self):
        """
        Gets or sets the order of serialization and deserialization of a member.

        Get: Order(self: DataMemberAttribute) -> int

        Set: Order(self: DataMemberAttribute) = value
        """
        ...

class DateTimeFormat:  # skipped bases: <type 'object'>
    """
    Specifies date-time format options.

    DateTimeFormat(formatString: str)

    DateTimeFormat(formatString: str, formatProvider: IFormatProvider)
    """

    @property
    def DateTimeStyles(self):
        """
        Gets or sets the formatting options that customize string parsing for some date and time parsing methods.

        Get: DateTimeStyles(self: DateTimeFormat) -> DateTimeStyles

        Set: DateTimeStyles(self: DateTimeFormat) = value
        """
        ...
    @property
    def FormatProvider(self):
        """
        Gets an object that controls formatting.

        Get: FormatProvider(self: DateTimeFormat) -> IFormatProvider
        """
        ...
    @property
    def FormatString(self):
        """
        Gets the format strings to control the formatting produced when a date or time is represented as a string.

        Get: FormatString(self: DateTimeFormat) -> str
        """
        ...

class EmitTypeInformation(Enum):  # skipped bases: <type 'IComparable'>, <type 'IFormattable'>, <type 'IConvertible'>
    """
    Specifies how often to emit type information.

    enum EmitTypeInformation, values: Always (1), AsNeeded (0), Never (2)
    """

    Always = None
    AsNeeded = None
    Never = None
    value__ = None

class EnumMemberAttribute(Attribute):  # skipped bases: <type '_Attribute'>
    """
    Specifies that the field is an enumeration member and should be serialized.

    EnumMemberAttribute()
    """

    @property
    def IsValueSetExplicitly(self):
        """
        Gets whether the System.Runtime.Serialization.EnumMemberAttribute.Value has been explicitly set.

        Get: IsValueSetExplicitly(self: EnumMemberAttribute) -> bool
        """
        ...
    @property
    def Value(self):
        """
        Gets or sets the value associated with the enumeration member the attribute is applied to.

        Get: Value(self: EnumMemberAttribute) -> str

        Set: Value(self: EnumMemberAttribute) = value
        """
        ...

class ExportOptions:  # skipped bases: <type 'object'>
    """
    Represents the options that can be set for an System.Runtime.Serialization.XsdDataContractExporter.

    ExportOptions()
    """

    @property
    def DataContractSurrogate(self):
        """
        Gets or sets a serialization surrogate.

        Get: DataContractSurrogate(self: ExportOptions) -> IDataContractSurrogate

        Set: DataContractSurrogate(self: ExportOptions) = value
        """
        ...
    @property
    def KnownTypes(self):
        """
        Gets the collection of types that may be encountered during serialization or deserialization.

        Get: KnownTypes(self: ExportOptions) -> Collection[Type]
        """
        ...

class ExtensionDataObject:  # skipped bases: <type 'object'>
    """Stores data from a versioned data contract that has been extended by adding new members."""

    pass

class Formatter(object, IFormatter):
    """Provides base functionality for the common language runtime serialization formatters."""

    def GetNext(self, *args):  # cannot find CLR method
        """
        GetNext(self: Formatter) -> (object, Int64)

            Returns the next object to serialize, from the formatter's internal work queue.

            Returns: The next object to serialize.
        """
        ...
    def Schedule(self, *args):  # cannot find CLR method
        """
        Schedule(self: Formatter, obj: object) -> Int64

            Schedules an object for later serialization.

            obj: The object to schedule for serialization.

            Returns: The object ID assigned to the object.
        """
        ...
    def WriteArray(self, *args):  # cannot find CLR method
        """
        WriteArray(self: Formatter, obj: object, name: str, memberType: Type)

            When overridden in a derived class, writes an array to the stream already attached to the formatter.

            obj: The array to write.

            name: The name of the array.

            memberType: The type of elements that the array holds.
        """
        ...
    def WriteBoolean(self, *args):  # cannot find CLR method
        """
        WriteBoolean(self: Formatter, val: bool, name: str)

            When overridden in a derived class, writes a Boolean value to the stream already attached to the formatter.

            val: The value to write.

            name: The name of the member.
        """
        ...
    def WriteByte(self, *args):  # cannot find CLR method
        """
        WriteByte(self: Formatter, val: Byte, name: str)

            When overridden in a derived class, writes an 8-bit unsigned integer to the stream already attached to the formatter.

            val: The value to write.

            name: The name of the member.
        """
        ...
    def WriteChar(self, *args):  # cannot find CLR method
        """
        WriteChar(self: Formatter, val: Char, name: str)

            When overridden in a derived class, writes a Unicode character to the stream already attached to the formatter.

            val: The value to write.

            name: The name of the member.
        """
        ...
    def WriteDateTime(self, *args):  # cannot find CLR method
        """
        WriteDateTime(self: Formatter, val: DateTime, name: str)

            When overridden in a derived class, writes a System.DateTime value to the stream already attached to the formatter.

            val: The value to write.

            name: The name of the member.
        """
        ...
    def WriteDecimal(self, *args):  # cannot find CLR method
        """
        WriteDecimal(self: Formatter, val: Decimal, name: str)

            When overridden in a derived class, writes a System.Decimal value to the stream already attached to the formatter.

            val: The value to write.

            name: The name of the member.
        """
        ...
    def WriteDouble(self, *args):  # cannot find CLR method
        """
        WriteDouble(self: Formatter, val: float, name: str)

            When overridden in a derived class, writes a double-precision floating-point number to the stream already attached to the formatter.

            val: The value to write.

            name: The name of the member.
        """
        ...
    def WriteInt16(self, *args):  # cannot find CLR method
        """
        WriteInt16(self: Formatter, val: Int16, name: str)

            When overridden in a derived class, writes a 16-bit signed integer to the stream already attached to the formatter.

            val: The value to write.

            name: The name of the member.
        """
        ...
    def WriteInt32(self, *args):  # cannot find CLR method
        """
        WriteInt32(self: Formatter, val: int, name: str)

            When overridden in a derived class, writes a 32-bit signed integer to the stream.

            val: The value to write.

            name: The name of the member.
        """
        ...
    def WriteInt64(self, *args):  # cannot find CLR method
        """
        WriteInt64(self: Formatter, val: Int64, name: str)

            When overridden in a derived class, writes a 64-bit signed integer to the stream.

            val: The value to write.

            name: The name of the member.
        """
        ...
    def WriteMember(self, *args):  # cannot find CLR method
        """
        WriteMember(self: Formatter, memberName: str, data: object)

            Inspects the type of data received, and calls the appropriate ite method to perform the write to the stream already attached to the formatter.

            memberName: The name of the member to serialize.

            data: The object to write to the stream attached to the formatter.
        """
        ...
    def WriteObjectRef(self, *args):  # cannot find CLR method
        """
        WriteObjectRef(self: Formatter, obj: object, name: str, memberType: Type)

            When overridden in a derived class, writes an object reference to the stream already attached to the formatter.

            obj: The object reference to write.

            name: The name of the member.

            memberType: The type of object the reference points to.
        """
        ...
    def WriteSByte(self, *args):  # cannot find CLR method
        """
        WriteSByte(self: Formatter, val: SByte, name: str)

            When overridden in a derived class, writes an 8-bit signed integer to the stream already attached to the formatter.

            val: The value to write.

            name: The name of the member.
        """
        ...
    def WriteSingle(self, *args):  # cannot find CLR method
        """
        WriteSingle(self: Formatter, val: Single, name: str)

            When overridden in a derived class, writes a single-precision floating-point number to the stream already attached to the formatter.

            val: The value to write.

            name: The name of the member.
        """
        ...
    def WriteTimeSpan(self, *args):  # cannot find CLR method
        """
        WriteTimeSpan(self: Formatter, val: TimeSpan, name: str)

            When overridden in a derived class, writes a System.TimeSpan value to the stream already attached to the formatter.

            val: The value to write.

            name: The name of the member.
        """
        ...
    def WriteUInt16(self, *args):  # cannot find CLR method
        """
        WriteUInt16(self: Formatter, val: UInt16, name: str)

            When overridden in a derived class, writes a 16-bit unsigned integer to the stream already attached to the formatter.

            val: The value to write.

            name: The name of the member.
        """
        ...
    def WriteUInt32(self, *args):  # cannot find CLR method
        """
        WriteUInt32(self: Formatter, val: UInt32, name: str)

            When overridden in a derived class, writes a 32-bit unsigned integer to the stream already attached to the formatter.

            val: The value to write.

            name: The name of the member.
        """
        ...
    def WriteUInt64(self, *args):  # cannot find CLR method
        """
        WriteUInt64(self: Formatter, val: UInt64, name: str)

            When overridden in a derived class, writes a 64-bit unsigned integer to the stream already attached to the formatter.

            val: The value to write.

            name: The name of the member.
        """
        ...
    def WriteValueType(self, *args):  # cannot find CLR method
        """
        WriteValueType(self: Formatter, obj: object, name: str, memberType: Type)

            When overridden in a derived class, writes a value of the given type to the stream already attached to the formatter.

            obj: The object representing the value type.

            name: The name of the member.

            memberType: The System.Type of the value type.
        """
        ...
    @property
    def Binder(self):
        """
        When overridden in a derived class, gets or sets the System.Runtime.Serialization.SerializationBinder used with the current formatter.

        Get: Binder(self: Formatter) -> SerializationBinder

        Set: Binder(self: Formatter) = value
        """
        ...
    @property
    def Context(self):
        """
        When overridden in a derived class, gets or sets the System.Runtime.Serialization.StreamingContext used for the current serialization.

        Get: Context(self: Formatter) -> StreamingContext

        Set: Context(self: Formatter) = value
        """
        ...
    @property
    def SurrogateSelector(self):
        """
        When overridden in a derived class, gets or sets the System.Runtime.Serialization.ISurrogateSelector used with the current formatter.

        Get: SurrogateSelector(self: Formatter) -> ISurrogateSelector

        Set: SurrogateSelector(self: Formatter) = value
        """
        ...
    m_idGenerator = None
    m_objectQueue = None

class FormatterConverter(object, IFormatterConverter):
    """
    Represents a base implementation of the System.Runtime.Serialization.IFormatterConverter interface that uses the System.Convert class and the System.IConvertible interface.

    FormatterConverter()
    """

    pass

class FormatterServices:  # skipped bases: <type 'object'>
    """Provides static methods to aid with the implementation of a System.Runtime.Serialization.Formatter for serialization. This class cannot be inherited."""

    @staticmethod
    def CheckTypeSecurity(t, securityLevel):
        """
        CheckTypeSecurity(t: Type, securityLevel: TypeFilterLevel)

            Determines whether the specified System.Type can be deserialized with the System.Runtime.Serialization.Formatters.TypeFilterLevel property set to w.

            t: The System.Type to check for the ability to deserialize.

            securityLevel: The System.Runtime.Serialization.Formatters.TypeFilterLevel property value.
        """
        ...
    @staticmethod
    def GetObjectData(obj, members):
        """
        GetObjectData(obj: object, members: Array[MemberInfo]) -> Array[object]

            Extracts the data from the specified object and returns it as an array of objects.

            obj: The object to write to the formatter.

            members: The members to extract from the object.

            Returns: An array of System.Object that contains data stored in members and associated with obj.
        """
        ...
    @staticmethod
    def GetSafeUninitializedObject(type):
        """
        GetSafeUninitializedObject(type: Type) -> object

            Creates a new instance of the specified object type.

            type: The type of object to create.

            Returns: A zeroed object of the specified type.
        """
        ...
    @staticmethod
    def GetSerializableMembers(type, context=None):
        """
        GetSerializableMembers(type: Type, context: StreamingContext) -> Array[MemberInfo]

            Gets all the serializable members for a class of the specified System.Type and in the provided System.Runtime.Serialization.StreamingContext.

            type: The type being serialized or cloned.

            context: The context where the serialization occurs.

            Returns: An array of type System.Reflection.MemberInfo of the non-transient, non-static members.

        GetSerializableMembers(type: Type) -> Array[MemberInfo]

            Gets all the serializable members for a class of the specified System.Type.

            type: The type being serialized.

            Returns: An array of type System.Reflection.MemberInfo of the non-transient, non-static members.
        """
        ...
    @staticmethod
    def GetSurrogateForCyclicalReference(innerSurrogate):
        """
        GetSurrogateForCyclicalReference(innerSurrogate: ISerializationSurrogate) -> ISerializationSurrogate

            Returns a serialization surrogate for the specified System.Runtime.Serialization.ISerializationSurrogate.

            innerSurrogate: The specified surrogate.

            Returns: An System.Runtime.Serialization.ISerializationSurrogate for the specified innerSurrogate.
        """
        ...
    @staticmethod
    def GetTypeFromAssembly(assem, name):
        """
        GetTypeFromAssembly(assem: Assembly, name: str) -> Type

            Looks up the System.Type of the specified object in the provided System.Reflection.Assembly.

            assem: The assembly where you want to look up the object.

            name: The name of the object.

            Returns: The System.Type of the named object.
        """
        ...
    @staticmethod
    def GetUninitializedObject(type):
        """
        GetUninitializedObject(type: Type) -> object

            Creates a new instance of the specified object type.

            type: The type of object to create.

            Returns: A zeroed object of the specified type.
        """
        ...
    @staticmethod
    def PopulateObjectMembers(obj, members, data):
        """
        PopulateObjectMembers(obj: object, members: Array[MemberInfo], data: Array[object]) -> object

            Populates the specified object with values for each field drawn from the data array of objects.

            obj: The object to populate.

            members: An array of System.Reflection.MemberInfo that describes which fields and properties to populate.

            data: An array of System.Object that specifies the values for each field and property to populate.

            Returns: The newly populated object.
        """
        ...
    __all__ = [
        "CheckTypeSecurity",
        "GetObjectData",
        "GetSafeUninitializedObject",
        "GetSerializableMembers",
        "GetSurrogateForCyclicalReference",
        "GetTypeFromAssembly",
        "GetUninitializedObject",
        "PopulateObjectMembers",
    ]

class IDataContractSurrogate:
    """Provides the methods needed to substitute one type for another by the System.Runtime.Serialization.DataContractSerializer during serialization, deserialization, and export and import of XML schema documents (XSD)."""

    def GetCustomDataToExport(self, *__args):
        """
        GetCustomDataToExport(self: IDataContractSurrogate, memberInfo: MemberInfo, dataContractType: Type) -> object

            During schema export operations, inserts annotations into the schema for non-null return values.

            memberInfo: A System.Reflection.MemberInfo that describes the member.

            dataContractType: A System.Type.

            Returns: An object that represents the annotation to be inserted into the XML schema definition.

        GetCustomDataToExport(self: IDataContractSurrogate, clrType: Type, dataContractType: Type) -> object

            During schema export operations, inserts annotations into the schema for non-null return values.

            clrType: The CLR type to be replaced.

            dataContractType: The data contract type to be annotated.

            Returns: An object that represents the annotation to be inserted into the XML schema definition.
        """
        ...
    def GetDataContractType(self, type):
        """
        GetDataContractType(self: IDataContractSurrogate, type: Type) -> Type

            During serialization, deserialization, and schema import and export, returns a data contract type that substitutes the specified type.

            type: The CLR type System.Type to substitute.

            Returns: The System.Type to substitute for the type value. This type must be serializable by the System.Runtime.Serialization.DataContractSerializer. For example, it must be

             marked with the System.Runtime.Serialization.DataContractAttribute attribute or other mechanisms that the serializer recognizes.
        """
        ...
    def GetDeserializedObject(self, obj, targetType):
        """
        GetDeserializedObject(self: IDataContractSurrogate, obj: object, targetType: Type) -> object

            During deserialization, returns an object that is a substitute for the specified object.

            obj: The deserialized object to be substituted.

            targetType: The System.Type that the substituted object should be assigned to.

            Returns: The substituted deserialized object. This object must be of a type that is serializable by the System.Runtime.Serialization.DataContractSerializer. For example, it

             must be marked with the System.Runtime.Serialization.DataContractAttribute attribute or other mechanisms that the serializer recognizes.
        """
        ...
    def GetKnownCustomDataTypes(self, customDataTypes):
        """GetKnownCustomDataTypes(self: IDataContractSurrogate, customDataTypes: Collection[Type])"""
        ...
    def GetObjectToSerialize(self, obj, targetType):
        """
        GetObjectToSerialize(self: IDataContractSurrogate, obj: object, targetType: Type) -> object

            During serialization, returns an object that substitutes the specified object.

            obj: The object to substitute.

            targetType: The System.Type that the substituted object should be assigned to.

            Returns: The substituted object that will be serialized. The object must be serializable by the System.Runtime.Serialization.DataContractSerializer. For example, it must be

             marked with the System.Runtime.Serialization.DataContractAttribute attribute or other mechanisms that the serializer recognizes.
        """
        ...
    def GetReferencedTypeOnImport(self, typeName, typeNamespace, customData):
        """
        GetReferencedTypeOnImport(self: IDataContractSurrogate, typeName: str, typeNamespace: str, customData: object) -> Type

            During schema import, returns the type referenced by the schema.

            typeName: The name of the type in schema.

            typeNamespace: The namespace of the type in schema.

            customData: The object that represents the annotation inserted into the XML schema definition, which is data that can be used for finding the referenced type.

            Returns: The System.Type to use for the referenced type.
        """
        ...
    def ProcessImportedType(self, typeDeclaration, compileUnit):
        """
        ProcessImportedType(self: IDataContractSurrogate, typeDeclaration: CodeTypeDeclaration, compileUnit: CodeCompileUnit) -> CodeTypeDeclaration

            Processes the type that has been generated from the imported schema.

            typeDeclaration: A System.CodeDom.CodeTypeDeclaration to process that represents the type declaration generated during schema import.

            compileUnit: The System.CodeDom.CodeCompileUnit that contains the other code generated during schema import.

            Returns: A System.CodeDom.CodeTypeDeclaration that contains the processed type.
        """
        ...

class IDeserializationCallback:
    """Indicates that a class is to be notified when deserialization of the entire object graph has been completed. Note that this interface is not called when deserializing with the XmlSerializer (System.Xml.Serialization.XmlSerializer)."""

    def OnDeserialization(self, sender):
        """
        OnDeserialization(self: IDeserializationCallback, sender: object)

            Runs when the entire object graph has been deserialized.

            sender: The object that initiated the callback. The functionality for this parameter is not currently implemented.
        """
        ...

class IExtensibleDataObject:
    """Provides a data structure to store extra data encountered by the System.Runtime.Serialization.XmlObjectSerializer during deserialization of a type marked with the System.Runtime.Serialization.DataContractAttribute attribute."""

    @property
    def ExtensionData(self):
        """
        Gets or sets the structure that contains extra data.

        Get: ExtensionData(self: IExtensibleDataObject) -> ExtensionDataObject

        Set: ExtensionData(self: IExtensibleDataObject) = value
        """
        ...

class IFormatter:
    """Provides functionality for formatting serialized objects."""

    def Deserialize(self, serializationStream):
        """
        Deserialize(self: IFormatter, serializationStream: Stream) -> object

            Deserializes the data on the provided stream and reconstitutes the graph of objects.

            serializationStream: The stream that contains the data to deserialize.

            Returns: The top object of the deserialized graph.
        """
        ...
    def Serialize(self, serializationStream, graph):
        """
        Serialize(self: IFormatter, serializationStream: Stream, graph: object)

            Serializes an object, or graph of objects with the given root to the provided stream.

            serializationStream: The stream where the formatter puts the serialized data. This stream can reference a variety of backing stores (such as files, network, memory, and so on).

            graph: The object, or root of the object graph, to serialize. All child objects of this root object are automatically serialized.
        """
        ...
    @property
    def Binder(self):
        """
        Gets or sets the System.Runtime.Serialization.SerializationBinder that performs type lookups during deserialization.

        Get: Binder(self: IFormatter) -> SerializationBinder

        Set: Binder(self: IFormatter) = value
        """
        ...
    @property
    def Context(self):
        """
        Gets or sets the System.Runtime.Serialization.StreamingContext used for serialization and deserialization.

        Get: Context(self: IFormatter) -> StreamingContext

        Set: Context(self: IFormatter) = value
        """
        ...
    @property
    def SurrogateSelector(self):
        """
        Gets or sets the System.Runtime.Serialization.SurrogateSelector used by the current formatter.

        Get: SurrogateSelector(self: IFormatter) -> ISurrogateSelector

        Set: SurrogateSelector(self: IFormatter) = value
        """
        ...

class IFormatterConverter:
    """Provides the connection between an instance of System.Runtime.Serialization.SerializationInfo and the formatter-provided class best suited to parse the data inside the System.Runtime.Serialization.SerializationInfo."""

    def Convert(self, value, *__args):
        """
        Convert(self: IFormatterConverter, value: object, type: Type) -> object

            Converts a value to the given System.Type.

            value: The object to be converted.

            type: The System.Type into which value is to be converted.

            Returns: The converted value.

        Convert(self: IFormatterConverter, value: object, typeCode: TypeCode) -> object

            Converts a value to the given System.TypeCode.

            value: The object to be converted.

            typeCode: The System.TypeCode into which value is to be converted.

            Returns: The converted value.
        """
        ...
    def ToBoolean(self, value):
        """
        ToBoolean(self: IFormatterConverter, value: object) -> bool

            Converts a value to a System.Boolean.

            value: The object to be converted.

            Returns: The converted value.
        """
        ...
    def ToByte(self, value):
        """
        ToByte(self: IFormatterConverter, value: object) -> Byte

            Converts a value to an 8-bit unsigned integer.

            value: The object to be converted.

            Returns: The converted value.
        """
        ...
    def ToChar(self, value):
        """
        ToChar(self: IFormatterConverter, value: object) -> Char

            Converts a value to a Unicode character.

            value: The object to be converted.

            Returns: The converted value.
        """
        ...
    def ToDateTime(self, value):
        """
        ToDateTime(self: IFormatterConverter, value: object) -> DateTime

            Converts a value to a System.DateTime.

            value: The object to be converted.

            Returns: The converted value.
        """
        ...
    def ToDecimal(self, value):
        """
        ToDecimal(self: IFormatterConverter, value: object) -> Decimal

            Converts a value to a System.Decimal.

            value: The object to be converted.

            Returns: The converted value.
        """
        ...
    def ToDouble(self, value):
        """
        ToDouble(self: IFormatterConverter, value: object) -> float

            Converts a value to a double-precision floating-point number.

            value: The object to be converted.

            Returns: The converted value.
        """
        ...
    def ToInt16(self, value):
        """
        ToInt16(self: IFormatterConverter, value: object) -> Int16

            Converts a value to a 16-bit signed integer.

            value: The object to be converted.

            Returns: The converted value.
        """
        ...
    def ToInt32(self, value):
        """
        ToInt32(self: IFormatterConverter, value: object) -> int

            Converts a value to a 32-bit signed integer.

            value: The object to be converted.

            Returns: The converted value.
        """
        ...
    def ToInt64(self, value):
        """
        ToInt64(self: IFormatterConverter, value: object) -> Int64

            Converts a value to a 64-bit signed integer.

            value: The object to be converted.

            Returns: The converted value.
        """
        ...
    def ToSByte(self, value):
        """
        ToSByte(self: IFormatterConverter, value: object) -> SByte

            Converts a value to a System.SByte.

            value: The object to be converted.

            Returns: The converted value.
        """
        ...
    def ToSingle(self, value):
        """
        ToSingle(self: IFormatterConverter, value: object) -> Single

            Converts a value to a single-precision floating-point number.

            value: The object to be converted.

            Returns: The converted value.
        """
        ...
    def ToString(self, value):
        """
        ToString(self: IFormatterConverter, value: object) -> str

            Converts a value to a System.String.

            value: The object to be converted.

            Returns: The converted value.
        """
        ...
    def ToUInt16(self, value):
        """
        ToUInt16(self: IFormatterConverter, value: object) -> UInt16

            Converts a value to a 16-bit unsigned integer.

            value: The object to be converted.

            Returns: The converted value.
        """
        ...
    def ToUInt32(self, value):
        """
        ToUInt32(self: IFormatterConverter, value: object) -> UInt32

            Converts a value to a 32-bit unsigned integer.

            value: The object to be converted.

            Returns: The converted value.
        """
        ...
    def ToUInt64(self, value):
        """
        ToUInt64(self: IFormatterConverter, value: object) -> UInt64

            Converts a value to a 64-bit unsigned integer.

            value: The object to be converted.

            Returns: The converted value.
        """
        ...

class IgnoreDataMemberAttribute(Attribute):  # skipped bases: <type '_Attribute'>
    """
    When applied to the member of a type, specifies that the member is not part of a data contract and is not serialized.

    IgnoreDataMemberAttribute()
    """

    pass

class ImportOptions:  # skipped bases: <type 'object'>
    """
    Represents the options that can be set on an System.Runtime.Serialization.XsdDataContractImporter.

    ImportOptions()
    """

    @property
    def CodeProvider(self):
        """
        Gets or sets a System.CodeDom.Compiler.CodeDomProvider instance that provides the means to check whether particular options for a target language are supported.

        Get: CodeProvider(self: ImportOptions) -> CodeDomProvider

        Set: CodeProvider(self: ImportOptions) = value
        """
        ...
    @property
    def DataContractSurrogate(self):
        """
        Gets or sets a data contract surrogate that can be used to modify the code generated during an import operation.

        Get: DataContractSurrogate(self: ImportOptions) -> IDataContractSurrogate

        Set: DataContractSurrogate(self: ImportOptions) = value
        """
        ...
    @property
    def EnableDataBinding(self):
        """
        Gets or sets a value that specifies whether types in generated code should implement the System.ComponentModel.INotifyPropertyChanged interface.

        Get: EnableDataBinding(self: ImportOptions) -> bool

        Set: EnableDataBinding(self: ImportOptions) = value
        """
        ...
    @property
    def GenerateInternal(self):
        """
        Gets or sets a value that specifies whether generated code will be marked internal or public.

        Get: GenerateInternal(self: ImportOptions) -> bool

        Set: GenerateInternal(self: ImportOptions) = value
        """
        ...
    @property
    def GenerateSerializable(self):
        """
        Gets or sets a value that specifies whether generated data contract classes will be marked with the System.SerializableAttribute attribute in addition to the System.Runtime.Serialization.DataContractAttribute attribute.

        Get: GenerateSerializable(self: ImportOptions) -> bool

        Set: GenerateSerializable(self: ImportOptions) = value
        """
        ...
    @property
    def ImportXmlType(self):
        """
        Gets or sets a value that determines whether all XML schema types, even those that do not conform to a data contract schema, will be imported.

        Get: ImportXmlType(self: ImportOptions) -> bool

        Set: ImportXmlType(self: ImportOptions) = value
        """
        ...
    @property
    def Namespaces(self):
        """
        Gets a dictionary that contains the mapping of data contract namespaces to the CLR namespaces that must be used to generate code during an import operation.

        Get: Namespaces(self: ImportOptions) -> IDictionary[str, str]
        """
        ...
    @property
    def ReferencedCollectionTypes(self):
        """
        Gets a collection of types that represents data contract collections that should be referenced when generating code for collections, such as lists or dictionaries of items.

        Get: ReferencedCollectionTypes(self: ImportOptions) -> ICollection[Type]
        """
        ...
    @property
    def ReferencedTypes(self):
        """
        Gets a System.Collections.Generic.IList containing types referenced in generated code.

        Get: ReferencedTypes(self: ImportOptions) -> ICollection[Type]
        """
        ...

class InvalidDataContractException(Exception):  # skipped bases: <type '_Exception'>, <type 'ISerializable'>
    """
    The exception that is thrown when the System.Runtime.Serialization.DataContractSerializer or System.Runtime.Serialization.NetDataContractSerializer encounters an invalid data contract during serialization and deserialization.

    InvalidDataContractException()

    InvalidDataContractException(message: str)

    InvalidDataContractException(message: str, innerException: Exception)
    """

    SerializeObjectState = None

class IObjectReference:
    """Indicates that the current interface implementer is a reference to another object."""

    def GetRealObject(self, context):
        """
        GetRealObject(self: IObjectReference, context: StreamingContext) -> object

            Returns the real object that should be deserialized, rather than the object that the serialized stream specifies.

            context: The System.Runtime.Serialization.StreamingContext from which the current object is deserialized.

            Returns: Returns the actual object that is put into the graph.
        """
        ...

class ISafeSerializationData:
    """Enables serialization of custom exception data in security-transparent code."""

    def CompleteDeserialization(self, deserialized):
        """
        CompleteDeserialization(self: ISafeSerializationData, deserialized: object)

            This method is called when the instance is deserialized.

            deserialized: An object that contains the state of the instance.
        """
        ...

class ISerializable:
    """Allows an object to control its own serialization and deserialization."""

    def GetObjectData(self, info, context):
        """
        GetObjectData(self: ISerializable, info: SerializationInfo, context: StreamingContext)

            Populates a System.Runtime.Serialization.SerializationInfo with the data needed to serialize the target object.

            info: The System.Runtime.Serialization.SerializationInfo to populate with data.

            context: The destination (see System.Runtime.Serialization.StreamingContext) for this serialization.
        """
        ...

class ISerializationSurrogate:
    """Implements a serialization surrogate selector that allows one object to perform serialization and deserialization of another."""

    def GetObjectData(self, obj, info, context):
        """
        GetObjectData(self: ISerializationSurrogate, obj: object, info: SerializationInfo, context: StreamingContext)

            Populates the provided System.Runtime.Serialization.SerializationInfo with the data needed to serialize the object.

            obj: The object to serialize.

            info: The System.Runtime.Serialization.SerializationInfo to populate with data.

            context: The destination (see System.Runtime.Serialization.StreamingContext) for this serialization.
        """
        ...
    def SetObjectData(self, obj, info, context, selector):
        """
        SetObjectData(self: ISerializationSurrogate, obj: object, info: SerializationInfo, context: StreamingContext, selector: ISurrogateSelector) -> object

            Populates the object using the information in the System.Runtime.Serialization.SerializationInfo.

            obj: The object to populate.

            info: The information to populate the object.

            context: The source from which the object is deserialized.

            selector: The surrogate selector where the search for a compatible surrogate begins.

            Returns: The populated deserialized object.
        """
        ...

class ISerializationSurrogateProvider:
    """Provides the methods needed to construct a serialization surrogate that extends the System.Runtime.Serialization.DataContractSerializer. A serialization surrogate is used during serialization and deserialization to substitute one type for another."""

    def GetDeserializedObject(self, obj, targetType):
        """
        GetDeserializedObject(self: ISerializationSurrogateProvider, obj: object, targetType: Type) -> object

            During deserialization, returns an object that is a substitute for the specified object.

            obj: The deserialized object to be substituted.

            targetType: The System.Type that the substituted object should be assigned to.

            Returns: The substituted deserialized object.
        """
        ...
    def GetObjectToSerialize(self, obj, targetType):
        """
        GetObjectToSerialize(self: ISerializationSurrogateProvider, obj: object, targetType: Type) -> object

            During serialization, returns an object that substitutes the specified object.

            obj: The object to substitute.

            targetType: The System.Type that the substituted object should be assigned to.

            Returns: The substituted object that will be serialized.
        """
        ...
    def GetSurrogateType(self, type):
        """
        GetSurrogateType(self: ISerializationSurrogateProvider, type: Type) -> Type

            During serialization, deserialization, and schema import and export, returns a data contract type that substitutes the specified type.

            type: The type to substitute.

            Returns: The System.Type to substitute for the type value.
        """
        ...

class ISurrogateSelector:
    """Indicates a serialization surrogate selector class."""

    def ChainSelector(self, selector):
        """
        ChainSelector(self: ISurrogateSelector, selector: ISurrogateSelector)

            Specifies the next System.Runtime.Serialization.ISurrogateSelector for surrogates to examine if the current instance does not have a surrogate for the specified type

             and assembly in the specified context.

            selector: The next surrogate selector to examine.
        """
        ...
    def GetNextSelector(self):
        """
        GetNextSelector(self: ISurrogateSelector) -> ISurrogateSelector

            Returns the next surrogate selector in the chain.

            Returns: The next surrogate selector in the chain or ll.
        """
        ...
    def GetSurrogate(self, type, context, selector):
        """
        GetSurrogate(self: ISurrogateSelector, type: Type, context: StreamingContext) -> (ISerializationSurrogate, ISurrogateSelector)

            Finds the surrogate that represents the specified object's type, starting with the specified surrogate selector for the specified serialization context.

            type: The System.Type of object (class) that needs a surrogate.

            context: The source or destination context for the current serialization.

            Returns: The appropriate surrogate for the given type in the given context.
        """
        ...

class KnownTypeAttribute(Attribute):  # skipped bases: <type '_Attribute'>
    """
    Specifies types that should be recognized by the System.Runtime.Serialization.DataContractSerializer when serializing or deserializing a given type.

    KnownTypeAttribute(type: Type)

    KnownTypeAttribute(methodName: str)
    """

    @staticmethod  # known case of __new__
    def __new__(cls, *__args):
        """
        __new__(cls: type, type: Type)

        __new__(cls: type, methodName: str)
        """
        ...
    @property
    def MethodName(self):
        """
        Gets the name of a method that will return a list of types that should be recognized during serialization or deserialization.

        Get: MethodName(self: KnownTypeAttribute) -> str
        """
        ...
    @property
    def Type(self):
        """
        Gets the type that should be recognized during serialization or deserialization by the System.Runtime.Serialization.DataContractSerializer.

        Get: Type(self: KnownTypeAttribute) -> Type
        """
        ...

class NetDataContractSerializer(XmlObjectSerializer, IFormatter):
    """
    Serializes and deserializes an instance of a type into XML stream or document using the supplied .NET Framework types. This class cannot be inherited.

    NetDataContractSerializer()

    NetDataContractSerializer(context: StreamingContext)

    NetDataContractSerializer(context: StreamingContext, maxItemsInObjectGraph: int, ignoreExtensionDataObject: bool, assemblyFormat: FormatterAssemblyStyle, surrogateSelector: ISurrogateSelector)

    NetDataContractSerializer(rootName: str, rootNamespace: str)

    NetDataContractSerializer(rootName: str, rootNamespace: str, context: StreamingContext, maxItemsInObjectGraph: int, ignoreExtensionDataObject: bool, assemblyFormat: FormatterAssemblyStyle, surrogateSelector: ISurrogateSelector)

    NetDataContractSerializer(rootName: XmlDictionaryString, rootNamespace: XmlDictionaryString)

    NetDataContractSerializer(rootName: XmlDictionaryString, rootNamespace: XmlDictionaryString, context: StreamingContext, maxItemsInObjectGraph: int, ignoreExtensionDataObject: bool, assemblyFormat: FormatterAssemblyStyle, surrogateSelector: ISurrogateSelector)
    """

    @staticmethod  # known case of __new__
    def __new__(cls, *__args):
        """
        __new__(cls: type)

        __new__(cls: type, context: StreamingContext)

        __new__(cls: type, context: StreamingContext, maxItemsInObjectGraph: int, ignoreExtensionDataObject: bool, assemblyFormat: FormatterAssemblyStyle, surrogateSelector: ISurrogateSelector)

        __new__(cls: type, rootName: str, rootNamespace: str)

        __new__(cls: type, rootName: str, rootNamespace: str, context: StreamingContext, maxItemsInObjectGraph: int, ignoreExtensionDataObject: bool, assemblyFormat: FormatterAssemblyStyle, surrogateSelector: ISurrogateSelector)

        __new__(cls: type, rootName: XmlDictionaryString, rootNamespace: XmlDictionaryString)

        __new__(cls: type, rootName: XmlDictionaryString, rootNamespace: XmlDictionaryString, context: StreamingContext, maxItemsInObjectGraph: int, ignoreExtensionDataObject: bool, assemblyFormat: FormatterAssemblyStyle, surrogateSelector: ISurrogateSelector)
        """
        ...
    @property
    def AssemblyFormat(self):
        """
        Gets a value that specifies a method for locating and loading assemblies.

        Get: AssemblyFormat(self: NetDataContractSerializer) -> FormatterAssemblyStyle

        Set: AssemblyFormat(self: NetDataContractSerializer) = value
        """
        ...
    @property
    def Binder(self):
        """
        Gets or sets an object that controls class loading.

        Get: Binder(self: NetDataContractSerializer) -> SerializationBinder

        Set: Binder(self: NetDataContractSerializer) = value
        """
        ...
    @property
    def Context(self):
        """
        Gets or sets the object that enables the passing of context data that is useful while serializing or deserializing.

        Get: Context(self: NetDataContractSerializer) -> StreamingContext

        Set: Context(self: NetDataContractSerializer) = value
        """
        ...
    @property
    def IgnoreExtensionDataObject(self):
        """
        Gets a value that specifies whether data supplied by an extension of the object is ignored.

        Get: IgnoreExtensionDataObject(self: NetDataContractSerializer) -> bool
        """
        ...
    @property
    def MaxItemsInObjectGraph(self):
        """
        Gets the maximum number of items allowed in the object to be serialized.

        Get: MaxItemsInObjectGraph(self: NetDataContractSerializer) -> int
        """
        ...
    @property
    def SurrogateSelector(self):
        """
        Gets or sets an object that assists the formatter when selecting a surrogate for serialization.

        Get: SurrogateSelector(self: NetDataContractSerializer) -> ISurrogateSelector

        Set: SurrogateSelector(self: NetDataContractSerializer) = value
        """
        ...

class ObjectIDGenerator:  # skipped bases: <type 'object'>
    """
    Generates IDs for objects.

    ObjectIDGenerator()
    """

    def GetId(self, obj, firstTime):
        """
        GetId(self: ObjectIDGenerator, obj: object) -> (Int64, bool)

            Returns the ID for the specified object, generating a new ID if the specified object has not already been identified by the

             System.Runtime.Serialization.ObjectIDGenerator.

            obj: The object you want an ID for.

            Returns: The object's ID is used for serialization. firstTime is set to ue if this is the first time the object has been identified; otherwise, it is set to lse.
        """
        ...
    def HasId(self, obj, firstTime):
        """
        HasId(self: ObjectIDGenerator, obj: object) -> (Int64, bool)

            Determines whether an object has already been assigned an ID.

            obj: The object you are asking for.

            Returns: The object ID of obj if previously known to the System.Runtime.Serialization.ObjectIDGenerator; otherwise, zero.
        """
        ...

class ObjectManager:  # skipped bases: <type 'object'>
    """
    Keeps track of objects as they are deserialized.

    ObjectManager(selector: ISurrogateSelector, context: StreamingContext)
    """

    def DoFixups(self):
        """
        DoFixups(self: ObjectManager)

            Performs all the recorded fixups.
        """
        ...
    def GetObject(self, objectID):
        """
        GetObject(self: ObjectManager, objectID: Int64) -> object

            Returns the object with the specified object ID.

            objectID: The ID of the requested object.

            Returns: The object with the specified object ID if it has been previously stored or ll if no such object has been registered.
        """
        ...
    def RaiseDeserializationEvent(self):
        """
        RaiseDeserializationEvent(self: ObjectManager)

            Raises the deserialization event to any registered object that implements System.Runtime.Serialization.IDeserializationCallback.
        """
        ...
    def RaiseOnDeserializingEvent(self, obj):
        """
        RaiseOnDeserializingEvent(self: ObjectManager, obj: object)

            Invokes the method marked with the System.Runtime.Serialization.OnDeserializingAttribute.

            obj: The instance of the type that contains the method to be invoked.
        """
        ...
    def RecordArrayElementFixup(self, arrayToBeFixed, *__args):
        """
        RecordArrayElementFixup(self: ObjectManager, arrayToBeFixed: Int64, index: int, objectRequired: Int64)

            Records a fixup for one element in an array.

            arrayToBeFixed: The ID of the array used to record a fixup.

            index: The index within arrayFixup that a fixup is requested for.

            objectRequired: The ID of the object that the current array element will point to after fixup is completed.

        RecordArrayElementFixup(self: ObjectManager, arrayToBeFixed: Int64, indices: Array[int], objectRequired: Int64)

            Records fixups for the specified elements in an array, to be executed later.

            arrayToBeFixed: The ID of the array used to record a fixup.

            indices: The indexes within the multidimensional array that a fixup is requested for.

            objectRequired: The ID of the object the array elements will point to after fixup is completed.
        """
        ...
    def RecordDelayedFixup(self, objectToBeFixed, memberName, objectRequired):
        """
        RecordDelayedFixup(self: ObjectManager, objectToBeFixed: Int64, memberName: str, objectRequired: Int64)

            Records a fixup for an object member, to be executed later.

            objectToBeFixed: The ID of the object that needs the reference to objectRequired.

            memberName: The member name of objectToBeFixed where the fixup will be performed.

            objectRequired: The ID of the object required by objectToBeFixed.
        """
        ...
    def RecordFixup(self, objectToBeFixed, member, objectRequired):
        """
        RecordFixup(self: ObjectManager, objectToBeFixed: Int64, member: MemberInfo, objectRequired: Int64)

            Records a fixup for a member of an object, to be executed later.

            objectToBeFixed: The ID of the object that needs the reference to the objectRequired object.

            member: The member of objectToBeFixed where the fixup will be performed.

            objectRequired: The ID of the object required by objectToBeFixed.
        """
        ...
    def RegisterObject(self, obj, objectID, info=None, idOfContainingObj=None, member=None, arrayIndex=None):
        """
        RegisterObject(self: ObjectManager, obj: object, objectID: Int64)

            Registers an object as it is deserialized, associating it with objectID.

            obj: The object to register.

            objectID: The ID of the object to register.

        RegisterObject(self: ObjectManager, obj: object, objectID: Int64, info: SerializationInfo)

            Registers an object as it is deserialized, associating it with objectID, and recording the System.Runtime.Serialization.SerializationInfo used with it.

            obj: The object to register.

            objectID: The ID of the object to register.

            info: The System.Runtime.Serialization.SerializationInfo used if obj implements System.Runtime.Serialization.ISerializable or has a

             System.Runtime.Serialization.ISerializationSurrogate. info will be completed with any required fixup information and then passed to the required object when that

             object is completed.

        RegisterObject(self: ObjectManager, obj: object, objectID: Int64, info: SerializationInfo, idOfContainingObj: Int64, member: MemberInfo)

            Registers a member of an object as it is deserialized, associating it with objectID, and recording the System.Runtime.Serialization.SerializationInfo.

            obj: The object to register.

            objectID: The ID of the object to register.

            info: The System.Runtime.Serialization.SerializationInfo used if obj implements System.Runtime.Serialization.ISerializable or has a

             System.Runtime.Serialization.ISerializationSurrogate. info will be completed with any required fixup information and then passed to the required object when that

             object is completed.

            idOfContainingObj: The ID of the object that contains obj. This parameter is required only if obj is a value type.

            member: The field in the containing object where obj exists. This parameter has meaning only if obj is a value type.

        RegisterObject(self: ObjectManager, obj: object, objectID: Int64, info: SerializationInfo, idOfContainingObj: Int64, member: MemberInfo, arrayIndex: Array[int])

            Registers a member of an array contained in an object while it is deserialized, associating it with objectID, and recording the

             System.Runtime.Serialization.SerializationInfo.

            obj: The object to register.

            objectID: The ID of the object to register.

            info: The System.Runtime.Serialization.SerializationInfo used if obj implements System.Runtime.Serialization.ISerializable or has a

             System.Runtime.Serialization.ISerializationSurrogate. info will be completed with any required fixup information and then passed to the required object when that

             object is completed.

            idOfContainingObj: The ID of the object that contains obj. This parameter is required only if obj is a value type.

            member: The field in the containing object where obj exists. This parameter has meaning only if obj is a value type.

            arrayIndex: If obj is a System.ValueType and a member of an array, arrayIndex contains the index within that array where obj exists. arrayIndex is ignored if obj is not both a

             System.ValueType and a member of an array.
        """
        ...

class OnDeserializedAttribute(Attribute):  # skipped bases: <type '_Attribute'>
    """
    When applied to a method, specifies that the method is called immediately after deserialization of an object in an object graph. The order of deserialization relative to other objects in the graph is non-deterministic.

    OnDeserializedAttribute()
    """

    pass

class OnDeserializingAttribute(Attribute):  # skipped bases: <type '_Attribute'>
    """
    When applied to a method, specifies that the method is called during deserialization of an object in an object graph. The order of deserialization relative to other objects in the graph is non-deterministic.

    OnDeserializingAttribute()
    """

    pass

class OnSerializedAttribute(Attribute):  # skipped bases: <type '_Attribute'>
    """
    When applied to a method, specifies that the method is called after serialization of an object in an object graph. The order of serialization relative to other objects in the graph is non-deterministic.

    OnSerializedAttribute()
    """

    pass

class OnSerializingAttribute(Attribute):  # skipped bases: <type '_Attribute'>
    """
    When applied to a method, specifies that the method is during serialization of an object in an object graph. The order of serialization relative to other objects in the graph is non-deterministic.

    OnSerializingAttribute()
    """

    pass

class OptionalFieldAttribute(Attribute):  # skipped bases: <type '_Attribute'>
    """
    Specifies that a field can be missing from a serialization stream so that the System.Runtime.Serialization.Formatters.Binary.BinaryFormatter and the System.Runtime.Serialization.Formatters.Soap.SoapFormatter does not throw an exception.

    OptionalFieldAttribute()
    """

    @property
    def VersionAdded(self):
        """
        This property is unused and is reserved.

        Get: VersionAdded(self: OptionalFieldAttribute) -> int

        Set: VersionAdded(self: OptionalFieldAttribute) = value
        """
        ...

class SafeSerializationEventArgs(EventArgs):
    """Provides data for the System.Exception.SerializeObjectState event."""

    def AddSerializedState(self, serializedState):
        """
        AddSerializedState(self: SafeSerializationEventArgs, serializedState: ISafeSerializationData)

            Stores the state of the exception.

            serializedState: A state object that is serialized with the instance.
        """
        ...
    @property
    def StreamingContext(self):
        """
        Gets or sets an object that describes the source and destination of a serialized stream.

        Get: StreamingContext(self: SafeSerializationEventArgs) -> StreamingContext
        """
        ...

class SerializationBinder:  # skipped bases: <type 'object'>
    """Allows users to control class loading and mandate what class to load."""

    def BindToName(self, serializedType, assemblyName, typeName):
        """
        BindToName(self: SerializationBinder, serializedType: Type) -> (str, str)

            When overridden in a derived class, controls the binding of a serialized object to a type.

            serializedType: The type of the object the formatter creates a new instance of.
        """
        ...
    def BindToType(self, assemblyName, typeName):
        """
        BindToType(self: SerializationBinder, assemblyName: str, typeName: str) -> Type

            When overridden in a derived class, controls the binding of a serialized object to a type.

            assemblyName: Specifies the System.Reflection.Assembly name of the serialized object.

            typeName: Specifies the System.Type name of the serialized object.

            Returns: The type of the object the formatter creates a new instance of.
        """
        ...

class SerializationEntry:  # skipped bases: <type 'object'>
    """Holds the value, System.Type, and name of a serialized object."""

    @property
    def Name(self):
        """
        Gets the name of the object.

        Get: Name(self: SerializationEntry) -> str
        """
        ...
    @property
    def ObjectType(self):
        """
        Gets the System.Type of the object.

        Get: ObjectType(self: SerializationEntry) -> Type
        """
        ...
    @property
    def Value(self):
        """
        Gets the value contained in the object.

        Get: Value(self: SerializationEntry) -> object
        """
        ...

class SerializationException(SystemException):  # skipped bases: <type '_Exception'>, <type 'ISerializable'>
    """
    The exception thrown when an error occurs during serialization or deserialization.

    SerializationException()

    SerializationException(message: str)

    SerializationException(message: str, innerException: Exception)
    """

    SerializeObjectState = None

class SerializationInfo:  # skipped bases: <type 'object'>
    """
    Stores all the data needed to serialize or deserialize an object. This class cannot be inherited.

    SerializationInfo(type: Type, converter: IFormatterConverter)

    SerializationInfo(type: Type, converter: IFormatterConverter, requireSameTokenInPartialTrust: bool)
    """

    def AddValue(self, name, value, type=None):
        """
        AddValue(self: SerializationInfo, name: str, value: object, type: Type)

            Adds a value into the System.Runtime.Serialization.SerializationInfo store, where value is associated with name and is serialized as being of System.Typetype.

            name: The name to associate with the value, so it can be deserialized later.

            value: The value to be serialized. Any children of this object will automatically be serialized.

            type: The System.Type to associate with the current object. This parameter must always be the type of the object itself or of one of its base classes.

        AddValue(self: SerializationInfo, name: str, value: object)

            Adds the specified object into the System.Runtime.Serialization.SerializationInfo store, where it is associated with a specified name.

            name: The name to associate with the value, so it can be deserialized later.

            value: The value to be serialized. Any children of this object will automatically be serialized.

        AddValue(self: SerializationInfo, name: str, value: bool)

            Adds a Boolean value into the System.Runtime.Serialization.SerializationInfo store.

            name: The name to associate with the value, so it can be deserialized later.

            value: The Boolean value to serialize.

        AddValue(self: SerializationInfo, name: str, value: Char)

            Adds a Unicode character value into the System.Runtime.Serialization.SerializationInfo store.

            name: The name to associate with the value, so it can be deserialized later.

            value: The character value to serialize.

        AddValue(self: SerializationInfo, name: str, value: SByte)

            Adds an 8-bit signed integer value into the System.Runtime.Serialization.SerializationInfo store.

            name: The name to associate with the value, so it can be deserialized later.

            value: The yte value to serialize.

        AddValue(self: SerializationInfo, name: str, value: Byte)

            Adds an 8-bit unsigned integer value into the System.Runtime.Serialization.SerializationInfo store.

            name: The name to associate with the value, so it can be deserialized later.

            value: The byte value to serialize.

        AddValue(self: SerializationInfo, name: str, value: Int16)

            Adds a 16-bit signed integer value into the System.Runtime.Serialization.SerializationInfo store.

            name: The name to associate with the value, so it can be deserialized later.

            value: The t16 value to serialize.

        AddValue(self: SerializationInfo, name: str, value: UInt16)

            Adds a 16-bit unsigned integer value into the System.Runtime.Serialization.SerializationInfo store.

            name: The name to associate with the value, so it can be deserialized later.

            value: The nt16 value to serialize.

        AddValue(self: SerializationInfo, name: str, value: int)

            Adds a 32-bit signed integer value into the System.Runtime.Serialization.SerializationInfo store.

            name: The name to associate with the value, so it can be deserialized later.

            value: The t32 value to serialize.

        AddValue(self: SerializationInfo, name: str, value: UInt32)

            Adds a 32-bit unsigned integer value into the System.Runtime.Serialization.SerializationInfo store.

            name: The name to associate with the value, so it can be deserialized later.

            value: The nt32 value to serialize.

        AddValue(self: SerializationInfo, name: str, value: Int64)

            Adds a 64-bit signed integer value into the System.Runtime.Serialization.SerializationInfo store.

            name: The name to associate with the value, so it can be deserialized later.

            value: The Int64 value to serialize.

        AddValue(self: SerializationInfo, name: str, value: UInt64)

            Adds a 64-bit unsigned integer value into the System.Runtime.Serialization.SerializationInfo store.

            name: The name to associate with the value, so it can be deserialized later.

            value: The nt64 value to serialize.

        AddValue(self: SerializationInfo, name: str, value: Single)

            Adds a single-precision floating-point value into the System.Runtime.Serialization.SerializationInfo store.

            name: The name to associate with the value, so it can be deserialized later.

            value: The single value to serialize.

        AddValue(self: SerializationInfo, name: str, value: float)

            Adds a double-precision floating-point value into the System.Runtime.Serialization.SerializationInfo store.

            name: The name to associate with the value, so it can be deserialized later.

            value: The double value to serialize.

        AddValue(self: SerializationInfo, name: str, value: Decimal)

            Adds a decimal value into the System.Runtime.Serialization.SerializationInfo store.

            name: The name to associate with the value, so it can be deserialized later.

            value: The decimal value to serialize.

        AddValue(self: SerializationInfo, name: str, value: DateTime)

            Adds a System.DateTime value into the System.Runtime.Serialization.SerializationInfo store.

            name: The name to associate with the value, so it can be deserialized later.

            value: The System.DateTime value to serialize.
        """
        ...
    def GetBoolean(self, name):
        """
        GetBoolean(self: SerializationInfo, name: str) -> bool

            Retrieves a Boolean value from the System.Runtime.Serialization.SerializationInfo store.

            name: The name associated with the value to retrieve.

            Returns: The Boolean value associated with name.
        """
        ...
    def GetByte(self, name):
        """
        GetByte(self: SerializationInfo, name: str) -> Byte

            Retrieves an 8-bit unsigned integer value from the System.Runtime.Serialization.SerializationInfo store.

            name: The name associated with the value to retrieve.

            Returns: The 8-bit unsigned integer associated with name.
        """
        ...
    def GetChar(self, name):
        """
        GetChar(self: SerializationInfo, name: str) -> Char

            Retrieves a Unicode character value from the System.Runtime.Serialization.SerializationInfo store.

            name: The name associated with the value to retrieve.

            Returns: The Unicode character associated with name.
        """
        ...
    def GetDateTime(self, name):
        """
        GetDateTime(self: SerializationInfo, name: str) -> DateTime

            Retrieves a System.DateTime value from the System.Runtime.Serialization.SerializationInfo store.

            name: The name associated with the value to retrieve.

            Returns: The System.DateTime value associated with name.
        """
        ...
    def GetDecimal(self, name):
        """
        GetDecimal(self: SerializationInfo, name: str) -> Decimal

            Retrieves a decimal value from the System.Runtime.Serialization.SerializationInfo store.

            name: The name associated with the value to retrieve.

            Returns: A decimal value from the System.Runtime.Serialization.SerializationInfo.
        """
        ...
    def GetDouble(self, name):
        """
        GetDouble(self: SerializationInfo, name: str) -> float

            Retrieves a double-precision floating-point value from the System.Runtime.Serialization.SerializationInfo store.

            name: The name associated with the value to retrieve.

            Returns: The double-precision floating-point value associated with name.
        """
        ...
    def GetEnumerator(self):
        """
        GetEnumerator(self: SerializationInfo) -> SerializationInfoEnumerator

            Returns a System.Runtime.Serialization.SerializationInfoEnumerator used to iterate through the name-value pairs in the System.Runtime.Serialization.SerializationInfo

             store.

            Returns: A System.Runtime.Serialization.SerializationInfoEnumerator for parsing the name-value pairs contained in the System.Runtime.Serialization.SerializationInfo store.
        """
        ...
    def GetInt16(self, name):
        """
        GetInt16(self: SerializationInfo, name: str) -> Int16

            Retrieves a 16-bit signed integer value from the System.Runtime.Serialization.SerializationInfo store.

            name: The name associated with the value to retrieve.

            Returns: The 16-bit signed integer associated with name.
        """
        ...
    def GetInt32(self, name):
        """
        GetInt32(self: SerializationInfo, name: str) -> int

            Retrieves a 32-bit signed integer value from the System.Runtime.Serialization.SerializationInfo store.

            name: The name of the value to retrieve.

            Returns: The 32-bit signed integer associated with name.
        """
        ...
    def GetInt64(self, name):
        """
        GetInt64(self: SerializationInfo, name: str) -> Int64

            Retrieves a 64-bit signed integer value from the System.Runtime.Serialization.SerializationInfo store.

            name: The name associated with the value to retrieve.

            Returns: The 64-bit signed integer associated with name.
        """
        ...
    def GetSByte(self, name):
        """
        GetSByte(self: SerializationInfo, name: str) -> SByte

            Retrieves an 8-bit signed integer value from the System.Runtime.Serialization.SerializationInfo store.

            name: The name associated with the value to retrieve.

            Returns: The 8-bit signed integer associated with name.
        """
        ...
    def GetSingle(self, name):
        """
        GetSingle(self: SerializationInfo, name: str) -> Single

            Retrieves a single-precision floating-point value from the System.Runtime.Serialization.SerializationInfo store.

            name: The name of the value to retrieve.

            Returns: The single-precision floating-point value associated with name.
        """
        ...
    def GetString(self, name):
        """
        GetString(self: SerializationInfo, name: str) -> str

            Retrieves a System.String value from the System.Runtime.Serialization.SerializationInfo store.

            name: The name associated with the value to retrieve.

            Returns: The System.String associated with name.
        """
        ...
    def GetUInt16(self, name):
        """
        GetUInt16(self: SerializationInfo, name: str) -> UInt16

            Retrieves a 16-bit unsigned integer value from the System.Runtime.Serialization.SerializationInfo store.

            name: The name associated with the value to retrieve.

            Returns: The 16-bit unsigned integer associated with name.
        """
        ...
    def GetUInt32(self, name):
        """
        GetUInt32(self: SerializationInfo, name: str) -> UInt32

            Retrieves a 32-bit unsigned integer value from the System.Runtime.Serialization.SerializationInfo store.

            name: The name associated with the value to retrieve.

            Returns: The 32-bit unsigned integer associated with name.
        """
        ...
    def GetUInt64(self, name):
        """
        GetUInt64(self: SerializationInfo, name: str) -> UInt64

            Retrieves a 64-bit unsigned integer value from the System.Runtime.Serialization.SerializationInfo store.

            name: The name associated with the value to retrieve.

            Returns: The 64-bit unsigned integer associated with name.
        """
        ...
    def GetValue(self, name, type):
        """
        GetValue(self: SerializationInfo, name: str, type: Type) -> object

            Retrieves a value from the System.Runtime.Serialization.SerializationInfo store.

            name: The name associated with the value to retrieve.

            type: The System.Type of the value to retrieve. If the stored value cannot be converted to this type, the system will throw a System.InvalidCastException.

            Returns: The object of the specified System.Type associated with name.
        """
        ...
    def SetType(self, type):
        """
        SetType(self: SerializationInfo, type: Type)

            Sets the System.Type of the object to serialize.

            type: The System.Type of the object to serialize.
        """
        ...
    @property
    def AssemblyName(self):
        """
        Gets or sets the assembly name of the type to serialize during serialization only.

        Get: AssemblyName(self: SerializationInfo) -> str

        Set: AssemblyName(self: SerializationInfo) = value
        """
        ...
    @property
    def FullTypeName(self):
        """
        Gets or sets the full name of the System.Type to serialize.

        Get: FullTypeName(self: SerializationInfo) -> str

        Set: FullTypeName(self: SerializationInfo) = value
        """
        ...
    @property
    def IsAssemblyNameSetExplicit(self):
        """
        Gets whether the assembly name has been explicitly set.

        Get: IsAssemblyNameSetExplicit(self: SerializationInfo) -> bool
        """
        ...
    @property
    def IsFullTypeNameSetExplicit(self):
        """
        Gets whether the full type name has been explicitly set.

        Get: IsFullTypeNameSetExplicit(self: SerializationInfo) -> bool
        """
        ...
    @property
    def MemberCount(self):
        """
        Gets the number of members that have been added to the System.Runtime.Serialization.SerializationInfo store.

        Get: MemberCount(self: SerializationInfo) -> int
        """
        ...
    @property
    def ObjectType(self):
        """
        Returns the type of the object to be serialized.

        Get: ObjectType(self: SerializationInfo) -> Type
        """
        ...

class SerializationInfoEnumerator(object, IEnumerator):
    """Provides a formatter-friendly mechanism for parsing the data in System.Runtime.Serialization.SerializationInfo. This class cannot be inherited."""

    @property
    def Current(self):
        """
        Gets the item currently being examined.

        Get: Current(self: SerializationInfoEnumerator) -> SerializationEntry
        """
        ...
    @property
    def Name(self):
        """
        Gets the name for the item currently being examined.

        Get: Name(self: SerializationInfoEnumerator) -> str
        """
        ...
    @property
    def ObjectType(self):
        """
        Gets the type of the item currently being examined.

        Get: ObjectType(self: SerializationInfoEnumerator) -> Type
        """
        ...
    @property
    def Value(self):
        """
        Gets the value of the item currently being examined.

        Get: Value(self: SerializationInfoEnumerator) -> object
        """
        ...

class SerializationObjectManager:  # skipped bases: <type 'object'>
    """
    Manages serialization processes at run time. This class cannot be inherited.

    SerializationObjectManager(context: StreamingContext)
    """

    def RaiseOnSerializedEvent(self):
        """
        RaiseOnSerializedEvent(self: SerializationObjectManager)

            Invokes the OnSerializing callback event if the type of the object has one; and registers the object for raising the OnSerialized event if the type of the object has

             one.
        """
        ...
    def RegisterObject(self, obj):
        """
        RegisterObject(self: SerializationObjectManager, obj: object)

            Registers the object upon which events will be raised.

            obj: The object to register.
        """
        ...

class StreamingContext:  # skipped bases: <type 'object'>
    """
    Describes the source and destination of a given serialized stream, and provides an additional caller-defined context.

    StreamingContext(state: StreamingContextStates)

    StreamingContext(state: StreamingContextStates, additional: object)
    """

    def Equals(self, obj):
        """
        Equals(self: StreamingContext, obj: object) -> bool

            Determines whether two System.Runtime.Serialization.StreamingContext instances contain the same values.

            obj: An object to compare with the current instance.

            Returns: ue if the specified object is an instance of System.Runtime.Serialization.StreamingContext and equals the value of the current instance; otherwise, lse.
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: StreamingContext) -> int

            Returns a hash code of this object.

            Returns: The System.Runtime.Serialization.StreamingContextStates value that contains the source or destination of the serialization for this

             System.Runtime.Serialization.StreamingContext.
        """
        ...
    def __eq__(self, *args):  # cannot find CLR method
        """x.__eq__(y) <==> x==y"""
        ...
    def __ne__(self, *args): ...
    @property
    def Context(self):
        """
        Gets context specified as part of the additional context.

        Get: Context(self: StreamingContext) -> object
        """
        ...
    @property
    def State(self):
        """
        Gets the source or destination of the transmitted data.

        Get: State(self: StreamingContext) -> StreamingContextStates
        """
        ...

class StreamingContextStates(Enum):  # skipped bases: <type 'IComparable'>, <type 'IFormattable'>, <type 'IConvertible'>
    """
    Defines a set of flags that specifies the source or destination context for the stream during serialization.

    enum (flags) StreamingContextStates, values: All (255), Clone (64), CrossAppDomain (128), CrossMachine (2), CrossProcess (1), File (4), Other (32), Persistence (8), Remoting (16)
    """

    All = None
    Clone = None
    CrossAppDomain = None
    CrossMachine = None
    CrossProcess = None
    File = None
    Other = None
    Persistence = None
    Remoting = None
    value__ = None

class SurrogateSelector(object, ISurrogateSelector):
    """
    Assists formatters in selection of the serialization surrogate to delegate the serialization or deserialization process to.

    SurrogateSelector()
    """

    def AddSurrogate(self, type, context, surrogate):
        """
        AddSurrogate(self: SurrogateSelector, type: Type, context: StreamingContext, surrogate: ISerializationSurrogate)

            Adds a surrogate to the list of checked surrogates.

            type: The System.Type for which the surrogate is required.

            context: The context-specific data.

            surrogate: The surrogate to call for this type.
        """
        ...
    def RemoveSurrogate(self, type, context):
        """
        RemoveSurrogate(self: SurrogateSelector, type: Type, context: StreamingContext)

            Removes the surrogate associated with a given type.

            type: The System.Type for which to remove the surrogate.

            context: The System.Runtime.Serialization.StreamingContext for the current surrogate.
        """
        ...

class XmlSerializableServices:  # skipped bases: <type 'object'>
    """Contains methods for reading and writing XML."""

    @staticmethod
    def AddDefaultSchema(schemas, typeQName):
        """
        AddDefaultSchema(schemas: XmlSchemaSet, typeQName: XmlQualifiedName)

            Generates a default schema type given the specified type name and adds it to the specified schema set.

            schemas: An System.Xml.Schema.XmlSchemaSet to add the generated schema type to.

            typeQName: An System.Xml.XmlQualifiedName that specifies the type name to assign the schema to.
        """
        ...
    @staticmethod
    def ReadNodes(xmlReader):
        """
        ReadNodes(xmlReader: XmlReader) -> Array[XmlNode]

            Reads a set of XML nodes from the specified reader and returns the result.

            xmlReader: An System.Xml.XmlReader used for reading.

            Returns: An array of type System.Xml.XmlNode.
        """
        ...
    @staticmethod
    def WriteNodes(xmlWriter, nodes):
        """
        WriteNodes(xmlWriter: XmlWriter, nodes: Array[XmlNode])

            Writes the supplied nodes using the specified writer.

            xmlWriter: An System.Xml.XmlWriter used for writing.

            nodes: An array of type System.Xml.XmlNode to write.
        """
        ...
    __all__ = [
        "AddDefaultSchema",
        "ReadNodes",
        "WriteNodes",
    ]

class XPathQueryGenerator:  # skipped bases: <type 'object'>
    """When given a class representing a data contract, and metadata representing a member of the contract, produces an XPath query for the member."""

    @staticmethod
    def CreateFromDataContractSerializer(type, pathToMember, *__args):
        """
        CreateFromDataContractSerializer(type: Type, pathToMember: Array[MemberInfo]) -> (str, XmlNamespaceManager)

            Creates an XPath from a data contract using the specified data contract type, array of metadata elements, and namespaces..

            type: The type that represents a data contract.

            pathToMember: The metadata, generated using the erload:System.Type.GetMember method of the System.Type class, that points to the specific data member used to generate the query.

            Returns: System.String

                The XPath generated from the type and member data.

        CreateFromDataContractSerializer(type: Type, pathToMember: Array[MemberInfo], rootElementXpath: StringBuilder) -> (str, XmlNamespaceManager)

            Creates an XPath from a data contract using the specified contract data type, array of metadata elements, the top level element, and namespaces.

            type: The type that represents a data contract.

            pathToMember: The metadata, generated using the erload:System.Type.GetMember method of the System.Type class, that points to the specific data member used to generate the query.

            rootElementXpath: The top level element in the xpath.

            Returns: System.String

                The XPath generated from the type and member data.
        """
        ...
    __all__ = [
        "CreateFromDataContractSerializer",
    ]

class XsdDataContractExporter:  # skipped bases: <type 'object'>
    """
    Allows the transformation of a set of .NET Framework types that are used in data contracts into an XML schema file (.xsd).

    XsdDataContractExporter()

    XsdDataContractExporter(schemas: XmlSchemaSet)
    """

    def CanExport(self, *__args):
        """
        CanExport(self: XsdDataContractExporter, assemblies: ICollection[Assembly]) -> bool

        CanExport(self: XsdDataContractExporter, types: ICollection[Type]) -> bool

        CanExport(self: XsdDataContractExporter, type: Type) -> bool

            Gets a value that indicates whether the specified common language runtime (CLR) type can be exported.

            type: The System.Type to export.

            Returns: ue if the type can be exported; otherwise, lse.
        """
        ...
    def Export(self, *__args):
        """
        Export(self: XsdDataContractExporter, assemblies: ICollection[Assembly])Export(self: XsdDataContractExporter, types: ICollection[Type])Export(self: XsdDataContractExporter, type: Type)

            Transforms the specified .NET Framework type into an XML schema definition language (XSD) schema.

            type: The System.Type to transform into an XML schema.
        """
        ...
    def GetRootElementName(self, type):
        """
        GetRootElementName(self: XsdDataContractExporter, type: Type) -> XmlQualifiedName

            Returns the top-level name and namespace for the System.Type.

            type: The System.Type to query.

            Returns: The System.Xml.XmlQualifiedName that represents the top-level name and namespace for this System.Type, which is written to the stream when writing this object.
        """
        ...
    def GetSchemaType(self, type):
        """
        GetSchemaType(self: XsdDataContractExporter, type: Type) -> XmlSchemaType

            Returns the XML schema type for the specified type.

            type: The type to return a schema for.

            Returns: An System.Xml.Schema.XmlSchemaType that contains the XML schema.
        """
        ...
    def GetSchemaTypeName(self, type):
        """
        GetSchemaTypeName(self: XsdDataContractExporter, type: Type) -> XmlQualifiedName

            Returns the contract name and contract namespace for the System.Type.

            type: The System.Type that was exported.

            Returns: An System.Xml.XmlQualifiedName that represents the contract name of the type and its namespace.
        """
        ...
    @property
    def Options(self):
        """
        Gets or sets an System.Runtime.Serialization.ExportOptions that contains options that can be set for the export operation.

        Get: Options(self: XsdDataContractExporter) -> ExportOptions

        Set: Options(self: XsdDataContractExporter) = value
        """
        ...
    @property
    def Schemas(self):
        """
        Gets the collection of exported XML schemas.

        Get: Schemas(self: XsdDataContractExporter) -> XmlSchemaSet
        """
        ...

class XsdDataContractImporter:  # skipped bases: <type 'object'>
    """
    Allows the transformation of a set of XML schema files (.xsd) into common language runtime (CLR) types.

    XsdDataContractImporter()

    XsdDataContractImporter(codeCompileUnit: CodeCompileUnit)
    """

    def CanImport(self, schemas, *__args):
        """
        CanImport(self: XsdDataContractImporter, schemas: XmlSchemaSet) -> bool

            Gets a value that indicates whether the schemas contained in an System.Xml.Schema.XmlSchemaSet can be transformed into a System.CodeDom.CodeCompileUnit.

            schemas: A System.Xml.Schema.XmlSchemaSet that contains the schemas to transform.

            Returns: ue if the schemas can be transformed to data contract types; otherwise, lse.

        CanImport(self: XsdDataContractImporter, schemas: XmlSchemaSet, typeNames: ICollection[XmlQualifiedName]) -> bool

        CanImport(self: XsdDataContractImporter, schemas: XmlSchemaSet, typeName: XmlQualifiedName) -> bool

            Gets a value that indicates whether the schemas contained in an System.Xml.Schema.XmlSchemaSet can be transformed into a System.CodeDom.CodeCompileUnit.

            schemas: A System.Xml.Schema.XmlSchemaSet that contains the schema representations.

            typeName: An System.Collections.IList of System.Xml.XmlQualifiedName that specifies the names of the schema types that need to be imported from the

             System.Xml.Schema.XmlSchemaSet.

            Returns: ue if the schemas can be transformed to data contract types; otherwise, lse.

        CanImport(self: XsdDataContractImporter, schemas: XmlSchemaSet, element: XmlSchemaElement) -> bool

            Gets a value that indicates whether a specific schema element contained in an System.Xml.Schema.XmlSchemaSet can be imported.

            schemas: An System.Xml.Schema.XmlSchemaSet to import.

            element: A specific System.Xml.Schema.XmlSchemaElement to check in the set of schemas.

            Returns: ue if the element can be imported; otherwise, lse.
        """
        ...
    def GetCodeTypeReference(self, typeName, element=None):
        """
        GetCodeTypeReference(self: XsdDataContractImporter, typeName: XmlQualifiedName) -> CodeTypeReference

            Returns a System.CodeDom.CodeTypeReference to the CLR type generated for the schema type with the specified System.Xml.XmlQualifiedName.

            typeName: The System.Xml.XmlQualifiedName that specifies the schema type to look up.

            Returns: A System.CodeDom.CodeTypeReference reference to the CLR type generated for the schema type with the typeName specified.

        GetCodeTypeReference(self: XsdDataContractImporter, typeName: XmlQualifiedName, element: XmlSchemaElement) -> CodeTypeReference

            Returns a System.CodeDom.CodeTypeReference for the specified XML qualified element and schema element.

            typeName: An System.Xml.XmlQualifiedName that specifies the XML qualified name of the schema type to look up.

            element: An System.Xml.Schema.XmlSchemaElement that specifies an element in an XML schema.

            Returns: A System.CodeDom.CodeTypeReference that represents the type that was generated for the specified schema type.
        """
        ...
    def GetKnownTypeReferences(self, typeName):
        """
        GetKnownTypeReferences(self: XsdDataContractImporter, typeName: XmlQualifiedName) -> ICollection[CodeTypeReference]

            Returns a list of System.CodeDom.CodeTypeReference objects that represents the known types generated when generating code for the specified schema type.

            typeName: An System.Xml.XmlQualifiedName that represents the schema type to look up known types for.

            Returns: A System.Collections.Generic.IList of type System.CodeDom.CodeTypeReference.
        """
        ...
    def Import(self, schemas, *__args):
        """
        Import(self: XsdDataContractImporter, schemas: XmlSchemaSet)

            Transforms the specified set of XML schemas contained in an System.Xml.Schema.XmlSchemaSet into a System.CodeDom.CodeCompileUnit.

            schemas: A System.Xml.Schema.XmlSchemaSet that contains the schema representations to generate CLR types for.

        Import(self: XsdDataContractImporter, schemas: XmlSchemaSet, typeNames: ICollection[XmlQualifiedName])Import(self: XsdDataContractImporter, schemas: XmlSchemaSet, typeName: XmlQualifiedName)

            Transforms the specified XML schema type contained in an System.Xml.Schema.XmlSchemaSet into a System.CodeDom.CodeCompileUnit.

            schemas: A System.Xml.Schema.XmlSchemaSet that contains the schema representations.

            typeName: A System.Xml.XmlQualifiedName that represents a specific schema type to import.

        Import(self: XsdDataContractImporter, schemas: XmlSchemaSet, element: XmlSchemaElement) -> XmlQualifiedName

            Transforms the specified schema element in the set of specified XML schemas into a System.CodeDom.CodeCompileUnit and returns an System.Xml.XmlQualifiedName that

             represents the data contract name for the specified element.

            schemas: An System.Xml.Schema.XmlSchemaSet that contains the schemas to transform.

            element: An System.Xml.Schema.XmlSchemaElement that represents the specific schema element to transform.

            Returns: An System.Xml.XmlQualifiedName that represents the specified element.
        """
        ...
    @property
    def CodeCompileUnit(self):
        """
        Gets a System.CodeDom.CodeCompileUnit used for storing the CLR types generated.

        Get: CodeCompileUnit(self: XsdDataContractImporter) -> CodeCompileUnit
        """
        ...
    @property
    def Options(self):
        """
        Gets or sets an System.Runtime.Serialization.ImportOptions that contains settable options for the import operation.

        Get: Options(self: XsdDataContractImporter) -> ImportOptions

        Set: Options(self: XsdDataContractImporter) = value
        """
        ...

# variables with complex values
