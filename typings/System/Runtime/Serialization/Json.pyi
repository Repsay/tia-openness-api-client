# encoding: utf-8
# module System.Runtime.Serialization.Json calls itself Json
# from System.Runtime.Serialization, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class DataContractJsonSerializer(XmlObjectSerializer):
    """
    Serializes objects to the JavaScript Object Notation (JSON) and deserializes JSON data to objects. This class cannot be inherited.

    DataContractJsonSerializer(type: Type)

    DataContractJsonSerializer(type: Type, rootName: str)

    DataContractJsonSerializer(type: Type, rootName: XmlDictionaryString)

    DataContractJsonSerializer(type: Type, knownTypes: IEnumerable[Type])

    DataContractJsonSerializer(type: Type, rootName: str, knownTypes: IEnumerable[Type])

    DataContractJsonSerializer(type: Type, rootName: XmlDictionaryString, knownTypes: IEnumerable[Type])

    DataContractJsonSerializer(type: Type, knownTypes: IEnumerable[Type], maxItemsInObjectGraph: int, ignoreExtensionDataObject: bool, dataContractSurrogate: IDataContractSurrogate, alwaysEmitTypeInformation: bool)

    DataContractJsonSerializer(type: Type, rootName: str, knownTypes: IEnumerable[Type], maxItemsInObjectGraph: int, ignoreExtensionDataObject: bool, dataContractSurrogate: IDataContractSurrogate, alwaysEmitTypeInformation: bool)

    DataContractJsonSerializer(type: Type, rootName: XmlDictionaryString, knownTypes: IEnumerable[Type], maxItemsInObjectGraph: int, ignoreExtensionDataObject: bool, dataContractSurrogate: IDataContractSurrogate, alwaysEmitTypeInformation: bool)

    DataContractJsonSerializer(type: Type, settings: DataContractJsonSerializerSettings)
    """

    @staticmethod  # known case of __new__
    def __new__(cls, type, *__args):
        """
        __new__(cls: type, type: Type)

        __new__(cls: type, type: Type, rootName: str)

        __new__(cls: type, type: Type, rootName: XmlDictionaryString)

        __new__(cls: type, type: Type, knownTypes: IEnumerable[Type])

        __new__(cls: type, type: Type, rootName: str, knownTypes: IEnumerable[Type])

        __new__(cls: type, type: Type, rootName: XmlDictionaryString, knownTypes: IEnumerable[Type])

        __new__(cls: type, type: Type, knownTypes: IEnumerable[Type], maxItemsInObjectGraph: int, ignoreExtensionDataObject: bool, dataContractSurrogate: IDataContractSurrogate, alwaysEmitTypeInformation: bool)

        __new__(cls: type, type: Type, rootName: str, knownTypes: IEnumerable[Type], maxItemsInObjectGraph: int, ignoreExtensionDataObject: bool, dataContractSurrogate: IDataContractSurrogate, alwaysEmitTypeInformation: bool)

        __new__(cls: type, type: Type, rootName: XmlDictionaryString, knownTypes: IEnumerable[Type], maxItemsInObjectGraph: int, ignoreExtensionDataObject: bool, dataContractSurrogate: IDataContractSurrogate, alwaysEmitTypeInformation: bool)

        __new__(cls: type, type: Type, settings: DataContractJsonSerializerSettings)
        """
        ...
    @property
    def DataContractSurrogate(self):
        """
        Gets a surrogate type that is currently active for a given System.Runtime.Serialization.IDataContractSurrogate instance. Surrogates can extend the serialization or deserialization process.

        Get: DataContractSurrogate(self: DataContractJsonSerializer) -> IDataContractSurrogate
        """
        ...
    @property
    def DateTimeFormat(self):
        """
        Gets the format of the date and time type items in object graph.

        Get: DateTimeFormat(self: DataContractJsonSerializer) -> DateTimeFormat
        """
        ...
    @property
    def EmitTypeInformation(self):
        """
        Gets or sets the data contract JSON serializer settings to emit type information.

        Get: EmitTypeInformation(self: DataContractJsonSerializer) -> EmitTypeInformation
        """
        ...
    @property
    def IgnoreExtensionDataObject(self):
        """
        Gets a value that specifies whether unknown data is ignored on deserialization and whether the System.Runtime.Serialization.IExtensibleDataObject interface is ignored on serialization.

        Get: IgnoreExtensionDataObject(self: DataContractJsonSerializer) -> bool
        """
        ...
    @property
    def KnownTypes(self):
        """
        Gets a collection of types that may be present in the object graph serialized using this instance of the System.Runtime.Serialization.Json.DataContractJsonSerializer.

        Get: KnownTypes(self: DataContractJsonSerializer) -> ReadOnlyCollection[Type]
        """
        ...
    @property
    def MaxItemsInObjectGraph(self):
        """
        Gets the maximum number of items in an object graph that the serializer serializes or deserializes in one read or write call.

        Get: MaxItemsInObjectGraph(self: DataContractJsonSerializer) -> int
        """
        ...
    @property
    def SerializeReadOnlyTypes(self):
        """
        Gets or sets a value that specifies whether to serialize read only types.

        Get: SerializeReadOnlyTypes(self: DataContractJsonSerializer) -> bool
        """
        ...
    @property
    def UseSimpleDictionaryFormat(self):
        """
        Gets or sets a value that specifies whether to use a simple dictionary format.

        Get: UseSimpleDictionaryFormat(self: DataContractJsonSerializer) -> bool
        """
        ...

class DataContractJsonSerializerSettings:  # skipped bases: <type 'object'>
    """
    Specifies System.Runtime.Serialization.Json.DataContractJsonSerializer settings.

    DataContractJsonSerializerSettings()
    """

    @property
    def DataContractSurrogate(self):
        """
        Gets or sets a surrogate type that is currently active for given IDataContractSurrogate instance.

        Get: DataContractSurrogate(self: DataContractJsonSerializerSettings) -> IDataContractSurrogate

        Set: DataContractSurrogate(self: DataContractJsonSerializerSettings) = value
        """
        ...
    @property
    def DateTimeFormat(self):
        """
        Gets or sets a DateTimeFormat that defines the culturally appropriate format of displaying dates and times.

        Get: DateTimeFormat(self: DataContractJsonSerializerSettings) -> DateTimeFormat

        Set: DateTimeFormat(self: DataContractJsonSerializerSettings) = value
        """
        ...
    @property
    def EmitTypeInformation(self):
        """
        Gets or sets the data contract JSON serializer settings to emit type information.

        Get: EmitTypeInformation(self: DataContractJsonSerializerSettings) -> EmitTypeInformation

        Set: EmitTypeInformation(self: DataContractJsonSerializerSettings) = value
        """
        ...
    @property
    def IgnoreExtensionDataObject(self):
        """
        Gets or sets a value that specifies whether to ignore data supplied by an extension of the class when the class is being serialized or deserialized.

        Get: IgnoreExtensionDataObject(self: DataContractJsonSerializerSettings) -> bool

        Set: IgnoreExtensionDataObject(self: DataContractJsonSerializerSettings) = value
        """
        ...
    @property
    def KnownTypes(self):
        """
        Gets or sets a collection of types that may be present in the object graph serialized using this instance the DataContractJsonSerializerSettings.

        Get: KnownTypes(self: DataContractJsonSerializerSettings) -> IEnumerable[Type]

        Set: KnownTypes(self: DataContractJsonSerializerSettings) = value
        """
        ...
    @property
    def MaxItemsInObjectGraph(self):
        """
        Gets or sets the maximum number of items in an object graph to serialize or deserialize.

        Get: MaxItemsInObjectGraph(self: DataContractJsonSerializerSettings) -> int

        Set: MaxItemsInObjectGraph(self: DataContractJsonSerializerSettings) = value
        """
        ...
    @property
    def RootName(self):
        """
        Gets or sets the root name of the selected object.

        Get: RootName(self: DataContractJsonSerializerSettings) -> str

        Set: RootName(self: DataContractJsonSerializerSettings) = value
        """
        ...
    @property
    def SerializeReadOnlyTypes(self):
        """
        Gets or sets a value that specifies whether to serialize read only types.

        Get: SerializeReadOnlyTypes(self: DataContractJsonSerializerSettings) -> bool

        Set: SerializeReadOnlyTypes(self: DataContractJsonSerializerSettings) = value
        """
        ...
    @property
    def UseSimpleDictionaryFormat(self):
        """
        Gets or sets a value that specifies whether to use a simple dictionary format.

        Get: UseSimpleDictionaryFormat(self: DataContractJsonSerializerSettings) -> bool

        Set: UseSimpleDictionaryFormat(self: DataContractJsonSerializerSettings) = value
        """
        ...

class IXmlJsonReaderInitializer:
    """Specifies the interface for initializing a JavaScript Object Notation (JSON) reader when reusing them to read from a particular stream or buffer."""

    def SetInput(self, *__args):
        """
        SetInput(self: IXmlJsonReaderInitializer, buffer: Array[Byte], offset: int, count: int, encoding: Encoding, quotas: XmlDictionaryReaderQuotas, onClose: OnXmlDictionaryReaderClose)

            Reinitializes a JavaScript Object Notation (JSON) enabled reader to a specified buffer that contains JSON-encoded data.

            buffer: The input System.Byte buffer array from which to read.

            offset: The starting position from which to read in buffer.

            count: The number of bytes that can be read from buffer.

            encoding: The System.Text.Encoding used by the reader.

            quotas: The System.Xml.XmlDictionaryReaderQuotas to apply.

            onClose: The System.Xml.OnXmlDictionaryReaderClose delegate to call when the reader is closed.

        SetInput(self: IXmlJsonReaderInitializer, stream: Stream, encoding: Encoding, quotas: XmlDictionaryReaderQuotas, onClose: OnXmlDictionaryReaderClose)

            Reinitializes a JavaScript Object Notation (JSON) enabled reader to a specified stream that contains JSON-encoded data.

            stream: The input System.IO.Stream from which to read.

            encoding: The System.Text.Encoding used by the reader.

            quotas: System.Xml.XmlDictionaryReaderQuotas to apply.

            onClose: Delegate to call when the reader is closed.
        """
        ...

class IXmlJsonWriterInitializer:
    """Specifies the interface for initializing a JavaScript Object Notation (JSON) writer when reusing them to write to a particular output stream."""

    def SetOutput(self, stream, encoding, ownsStream):
        """
        SetOutput(self: IXmlJsonWriterInitializer, stream: Stream, encoding: Encoding, ownsStream: bool)

            Initializes (or reinitializes) a JavaScript Object Notation (JSON) writer to a specified output stream with specified character encoding.

            stream: The output System.IO.Stream to which the writer writes.

            encoding: The System.Text.Encoding that specifies the character encoding of the output stream.

            ownsStream: If ue, the output stream is closed by the writer when done; otherwise lse.
        """
        ...

class JsonReaderWriterFactory:  # skipped bases: <type 'object'>
    """Produces instances of System.Xml.XmlDictionaryReader that can read data encoded with JavaScript Object Notation (JSON) from a stream or buffer and map it to an XML Infoset and instances of System.Xml.XmlDictionaryWriter that can map an XML Infoset to JSON and write JSON-encoded data to a stream."""

    @staticmethod
    def CreateJsonReader(*__args):
        """
        CreateJsonReader(stream: Stream, quotas: XmlDictionaryReaderQuotas) -> XmlDictionaryReader

            Creates an System.Xml.XmlDictionaryReader that can map streams encoded with JavaScript Object Notation (JSON) to an XML Infoset.

            stream: The input System.IO.Stream from which to read.

            quotas: The System.Xml.XmlDictionaryReaderQuotas used to prevent Denial of Service attacks when reading untrusted data.

            Returns: An System.Xml.XmlDictionaryReader that can read JavaScript Object Notation (JSON).

        CreateJsonReader(buffer: Array[Byte], quotas: XmlDictionaryReaderQuotas) -> XmlDictionaryReader

            Creates an System.Xml.XmlDictionaryReader that can map buffers encoded with JavaScript Object Notation (JSON) to an XML Infoset.

            buffer: The input System.Byte buffer array from which to read.

            quotas: The System.Xml.XmlDictionaryReaderQuotas used to prevent Denial of Service attacks when reading untrusted data.

            Returns: An System.Xml.XmlDictionaryReader that can process JavaScript Object Notation (JSON) data.

        CreateJsonReader(stream: Stream, encoding: Encoding, quotas: XmlDictionaryReaderQuotas, onClose: OnXmlDictionaryReaderClose) -> XmlDictionaryReader

            Creates an System.Xml.XmlDictionaryReader that can map streams encoded with JavaScript Object Notation (JSON), of a specified size and offset, to an XML Infoset.

            stream: The input System.IO.Stream from which to read.

            encoding: The System.Text.Encoding that specifies the character encoding used by the reader. If ll is specified as the value, the reader attempts to auto-detect the encoding.

            quotas: The System.Xml.XmlDictionaryReaderQuotas used to prevent Denial of Service attacks when reading untrusted data.

            onClose: The System.Xml.OnXmlDictionaryReaderClose delegate to call when the reader is closed.

            Returns: An System.Xml.XmlDictionaryReader that can read JavaScript Object Notation (JSON).

        CreateJsonReader(buffer: Array[Byte], offset: int, count: int, quotas: XmlDictionaryReaderQuotas) -> XmlDictionaryReader

            Creates an System.Xml.XmlDictionaryReader that can map buffers encoded with JavaScript Object Notation (JSON), of a specified size and offset, to an XML Infoset.

            buffer: The input System.Byte buffer array from which to read.

            offset: Starting position from which to read in buffer.

            count: Number of bytes that can be read from buffer.

            quotas: The System.Xml.XmlDictionaryReaderQuotas used to prevent Denial of Service attacks when reading untrusted data.

            Returns: An System.Xml.XmlDictionaryReader that can read JavaScript Object Notation (JSON).

        CreateJsonReader(buffer: Array[Byte], offset: int, count: int, encoding: Encoding, quotas: XmlDictionaryReaderQuotas, onClose: OnXmlDictionaryReaderClose) -> XmlDictionaryReader

            Creates an System.Xml.XmlDictionaryReader that can map buffers encoded with JavaScript Object Notation (JSON), with a specified size and offset and character encoding,

             to an XML Infoset.

            buffer: The input System.Byte buffer array from which to read.

            offset: Starting position from which to read in buffer.

            count: Number of bytes that can be read from buffer.

            encoding: The System.Text.Encoding that specifies the character encoding used by the reader. If ll is specified as the value, the reader attempts to auto-detect the encoding.

            quotas: The System.Xml.XmlDictionaryReaderQuotas used to prevent Denial of Service attacks when reading untrusted data.

            onClose: The System.Xml.OnXmlDictionaryReaderClose delegate to call when the reader is closed. The default value is ll.

            Returns: An System.Xml.XmlDictionaryReader that can read JavaScript Object Notation (JSON).
        """
        ...
    @staticmethod
    def CreateJsonWriter(stream, encoding=None, ownsStream=None, indent=None, indentChars=None):
        """
        CreateJsonWriter(stream: Stream) -> XmlDictionaryWriter

            Creates an System.Xml.XmlDictionaryWriter that writes data encoded with JSON to a stream.

            stream: The output System.IO.Stream for the JSON writer.

            Returns: An System.Xml.XmlDictionaryWriter that writes data encoded with JSON to the stream based on an XML Infoset.

        CreateJsonWriter(stream: Stream, encoding: Encoding) -> XmlDictionaryWriter

            Creates an System.Xml.XmlDictionaryWriter that writes data encoded with JSON to a stream with a specified character encoding.

            stream: The output System.IO.Stream for the JSON writer.

            encoding: The System.Text.Encoding that specifies the character encoding used by the writer. The default encoding is UTF-8.

            Returns: An System.Xml.XmlDictionaryWriter that writes data encoded with JSON to the stream based on an XML Infoset.

        CreateJsonWriter(stream: Stream, encoding: Encoding, ownsStream: bool) -> XmlDictionaryWriter

            Creates an System.Xml.XmlDictionaryWriter that writes data encoded with JSON to a stream with a specified character encoding.

            stream: The output System.IO.Stream for the JSON writer.

            encoding: The System.Text.Encoding that specifies the character encoding used by the writer. The default encoding is UTF-8.

            ownsStream: If ue, the output stream is closed by the writer when done; otherwise lse. The default value is ue.

            Returns: An System.Xml.XmlDictionaryWriter that writes data encoded with JSON to the stream based on an XML Infoset.

        CreateJsonWriter(stream: Stream, encoding: Encoding, ownsStream: bool, indent: bool) -> XmlDictionaryWriter

            Creates an System.Xml.XmlDictionaryWriter that writes data encoded with JSON to a stream with a specified character.

            stream: The output System.IO.Stream for the JSON writer.

            encoding: The System.Text.Encoding that specifies the character encoding used by the writer. The default encoding is UTF-8.

            ownsStream: If ue, the output stream is closed by the writer when done; otherwise lse. The default value is ue.

            indent: If ue, the output uses multiline format, indenting each level properly; otherwise, lse.

            Returns: An System.Xml.XmlDictionaryWriter that writes data encoded with JSON to the stream based on an XML Infoset.

        CreateJsonWriter(stream: Stream, encoding: Encoding, ownsStream: bool, indent: bool, indentChars: str) -> XmlDictionaryWriter

            Creates an System.Xml.XmlDictionaryWriter that writes data encoded with JSON to a stream with a specified character.

            stream: The output System.IO.Stream for the JSON writer.

            encoding: The System.Text.Encoding that specifies the character encoding used by the writer. The default encoding is UTF-8.

            ownsStream: If ue, the output stream is closed by the writer when done; otherwise lse. The default value is ue.

            indent: If ue, the output uses multiline format, indenting each level properly; otherwise, lse.

            indentChars: The string used to indent each level.

            Returns: An System.Xml.XmlDictionaryWriter that writes data encoded with JSON to the stream based on an XML Infoset.
        """
        ...
    __all__ = [
        "CreateJsonReader",
        "CreateJsonWriter",
    ]
