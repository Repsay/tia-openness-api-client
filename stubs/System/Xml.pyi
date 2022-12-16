# encoding: utf-8
# module System.Xml calls itself Xml
# from System.Runtime.Serialization, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class IFragmentCapableXmlDictionaryWriter:
    """ Contains properties and methods that when implemented by a System.Xml.XmlDictionaryWriter, allows processing of XML fragments. """
    def EndFragment(self):
        """
        EndFragment(self: IFragmentCapableXmlDictionaryWriter)

            Ends the processing of an XML fragment.
        """
        ...

    def StartFragment(self, stream, generateSelfContainedTextFragment):
        """
        StartFragment(self: IFragmentCapableXmlDictionaryWriter, stream: Stream, generateSelfContainedTextFragment: bool)

            Starts the processing of an XML fragment.

            stream: The stream to write to.

            generateSelfContainedTextFragment: If ue, any namespaces declared outside the fragment is declared again if used inside of it; if lse the namespaces are not declared again.
        """
        ...

    def WriteFragment(self, buffer, offset, count):
        """
        WriteFragment(self: IFragmentCapableXmlDictionaryWriter, buffer: Array[Byte], offset: int, count: int)

            Writes an XML fragment to the underlying stream of the writer.

            buffer: The buffer to write to.

            offset: The starting position from which to write in buffer.

            count: The number of bytes to be written to the buffer.
        """
        ...

    @property
    def CanFragment(self):
        """
        Gets a value that indicates whether this System.Xml.XmlDictionaryWriter can process XML fragments.

        Get: CanFragment(self: IFragmentCapableXmlDictionaryWriter) -> bool
        """
        ...



class IStreamProvider:
    """ Represents an interface that can be implemented by classes providing streams. """
    def GetStream(self):
        """
        GetStream(self: IStreamProvider) -> Stream

            Gets a stream.

            Returns: A System.IO.Stream object.
        """
        ...

    def ReleaseStream(self, stream):
        """
        ReleaseStream(self: IStreamProvider, stream: Stream)

            Releases a stream to output.

            stream: The stream being released.
        """
        ...


class IXmlBinaryReaderInitializer:
    """ Provides methods for reinitializing a binary reader to read a new document. """
    def SetInput(self, *__args):
        """
        SetInput(self: IXmlBinaryReaderInitializer, buffer: Array[Byte], offset: int, count: int, dictionary: IXmlDictionary, quotas: XmlDictionaryReaderQuotas, session: XmlBinaryReaderSession, onClose: OnXmlDictionaryReaderClose)

            Reinitializes the binary reader using the given input buffer.

            buffer: The buffer from which to read.

            offset: Starting position from which to read in buffer.

            count: Number of bytes that can be read from buffer.

            dictionary: System.Xml.XmlDictionary to use.

            quotas: System.Xml.XmlDictionaryReaderQuotas to apply.

            session: System.Xml.XmlBinaryReaderSession to use.

            onClose: Delegate to call when the reader is closed.

        SetInput(self: IXmlBinaryReaderInitializer, stream: Stream, dictionary: IXmlDictionary, quotas: XmlDictionaryReaderQuotas, session: XmlBinaryReaderSession, onClose: OnXmlDictionaryReaderClose)

            Reinitializes the binary reader using the given input stream.

            stream: The stream from which to read.

            dictionary: System.Xml.XmlDictionary to use.

            quotas: System.Xml.XmlDictionaryReaderQuotas to apply.

            session: System.Xml.XmlBinaryReaderSession to use.

            onClose: Delegate to call when the reader is closed.
        """
        ...


class IXmlBinaryWriterInitializer:
    """ Specifies implementation requirements for XML binary writers that derive from this interface. """
    def SetOutput(self, stream, dictionary, session, ownsStream):
        """
        SetOutput(self: IXmlBinaryWriterInitializer, stream: Stream, dictionary: IXmlDictionary, session: XmlBinaryWriterSession, ownsStream: bool)

            Specifies initialization requirements for XML binary writers that implement this method.

            stream: The stream to write to.

            dictionary: The System.Xml.XmlDictionary to use.

            session: The System.Xml.XmlBinaryWriterSession to use.

            ownsStream: If ue, stream is closed by the writer when done; otherwise lse.
        """
        ...


class IXmlDictionary:
    """ An terface that defines the contract that an Xml dictionary must implement to be used by System.Xml.XmlDictionaryReader and System.Xml.XmlDictionaryWriter implementations. """
    def TryLookup(self, *__args):
        """
        TryLookup(self: IXmlDictionary, value: str) -> (bool, XmlDictionaryString)

            Checks the dictionary for a specified string value.

            value: String value being checked for.

            Returns: ue if value is in the dictionary, otherwise lse.

        TryLookup(self: IXmlDictionary, key: int) -> (bool, XmlDictionaryString)

            Attempts to look up an entry in the dictionary.

            key: Key to look up.

            Returns: ue if key is in the dictionary, otherwise lse.

        TryLookup(self: IXmlDictionary, value: XmlDictionaryString) -> (bool, XmlDictionaryString)

            Checks the dictionary for a specified System.Xml.XmlDictionaryString.

            value: The System.Xml.XmlDictionaryString being checked for.

            Returns: ue if System.Xml.XmlDictionaryString is in the dictionary, otherwise lse.
        """
        ...


class IXmlMtomReaderInitializer:
    """ Specifies implementation requirements for XML MTOM readers that derive from this interface. """
    def SetInput(self, *__args):
        """
        SetInput(self: IXmlMtomReaderInitializer, buffer: Array[Byte], offset: int, count: int, encodings: Array[Encoding], contentType: str, quotas: XmlDictionaryReaderQuotas, maxBufferSize: int, onClose: OnXmlDictionaryReaderClose)

            Specifies initialization requirements for XML MTOM readers that read a buffer.

            buffer: The buffer from which to read.

            offset: The starting position from which to read in buffer.

            count: The number of bytes that can be read from buffer.

            encodings: The possible character encodings of the input.

            contentType: The Content-Type of the message. Can be ll if the MIME type is present in the document being read.

            quotas: The System.Xml.XmlDictionaryReaderQuotas to apply to the reader.

            maxBufferSize: The maximum allowed size of the buffer.

            onClose: The delegate to use when an Close event happens.

        SetInput(self: IXmlMtomReaderInitializer, stream: Stream, encodings: Array[Encoding], contentType: str, quotas: XmlDictionaryReaderQuotas, maxBufferSize: int, onClose: OnXmlDictionaryReaderClose)

            Specifies initialization requirements for XML MTOM readers that read a stream.

            stream: The stream from which to read.

            encodings: The possible character encodings of the stream.

            contentType: The Content-Type of the message. Can be ll if the MIME type is present in the document being read.

            quotas: The System.Xml.XmlDictionaryReaderQuotas to apply to the reader.

            maxBufferSize: The maximum allowed size of the buffer.

            onClose: The delegate to use when an Close event happens.
        """
        ...


class IXmlMtomWriterInitializer:
    """ When implemented by an MTOM writer, this interface ensures initialization for an MTOM writer. """
    def SetOutput(self, stream, encoding, maxSizeInBytes, startInfo, boundary, startUri, writeMessageHeaders, ownsStream):
        """
        SetOutput(self: IXmlMtomWriterInitializer, stream: Stream, encoding: Encoding, maxSizeInBytes: int, startInfo: str, boundary: str, startUri: str, writeMessageHeaders: bool, ownsStream: bool)

            When implemented by an MTOM writer, initializes an MTOM writer.

            stream: The stream to write to.

            encoding: The character encoding of the stream.

            maxSizeInBytes: The maximum number of bytes that are buffered in the writer.

            startInfo: An attribute in the ContentType SOAP header, set to "Application/soap+xml".

            boundary: The MIME boundary string.

            startUri: The URI for MIME section.

            writeMessageHeaders: If ue, write message headers.

            ownsStream: If ue, the stream is closed by the writer when done; otherwise lse.
        """
        ...


class IXmlTextReaderInitializer:
    """ Specifies implementation requirements for XML text readers that derive from this interface. """
    def SetInput(self, *__args):
        """
        SetInput(self: IXmlTextReaderInitializer, buffer: Array[Byte], offset: int, count: int, encoding: Encoding, quotas: XmlDictionaryReaderQuotas, onClose: OnXmlDictionaryReaderClose)

            Specifies initialization requirements for XML text readers that read a buffer.

            buffer: The buffer from which to read.

            offset: The starting position from which to read in buffer.

            count: The number of bytes that can be read from buffer.

            encoding: The character encoding of the stream.

            quotas: The System.Xml.XmlDictionaryReaderQuotas to apply.

            onClose: The delegate to be called when the reader is closed.

        SetInput(self: IXmlTextReaderInitializer, stream: Stream, encoding: Encoding, quotas: XmlDictionaryReaderQuotas, onClose: OnXmlDictionaryReaderClose)

            Specifies initialization requirements for XML text readers that read a stream.

            stream: The stream from which to read.

            encoding: The character encoding of the stream.

            quotas: The System.Xml.XmlDictionaryReaderQuotas to apply.

            onClose: The delegate to be called when the reader is closed.
        """
        ...


class IXmlTextWriterInitializer:
    """ Specifies implementation requirements for XML text writers that derive from this interface. """
    def SetOutput(self, stream, encoding, ownsStream):
        """
        SetOutput(self: IXmlTextWriterInitializer, stream: Stream, encoding: Encoding, ownsStream: bool)

            Specifies initialization requirements for XML text writers that implement this method.

            stream: The stream to write to.

            encoding: The character encoding of the stream.

            ownsStream: If ue, stream is closed by the writer when done; otherwise lse.
        """
        ...


class OnXmlDictionaryReaderClose(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>
    """
    legate for a callback method when closing the reader.

    OnXmlDictionaryReaderClose(object: object, method: IntPtr)
    """
    def BeginInvoke(self, reader, callback, object):
        """ BeginInvoke(self: OnXmlDictionaryReaderClose, reader: XmlDictionaryReader, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result):
        """ EndInvoke(self: OnXmlDictionaryReaderClose, result: IAsyncResult) """
        ...

    def Invoke(self, reader):
        """ Invoke(self: OnXmlDictionaryReaderClose, reader: XmlDictionaryReader) """
        ...


class UniqueId: # skipped bases: <type 'object'>
    """
    A unique identifier optimized for Guids.

    UniqueId()

    UniqueId(guid: Guid)

    UniqueId(guid: Array[Byte])

    UniqueId(guid: Array[Byte], offset: int)

    UniqueId(value: str)

    UniqueId(chars: Array[Char], offset: int, count: int)
    """
    def Equals(self, obj):
        """
        Equals(self: UniqueId, obj: object) -> bool

            Tests whether an object equals this System.Xml.UniqueId.

            obj: The object to compare.

            Returns: ue if the object equals this System.Xml.UniqueId; otherwise lse.
        """
        ...

    def GetHashCode(self):
        """
        GetHashCode(self: UniqueId) -> int

            Creates a hash-code representation of this System.Xml.UniqueId.

            Returns: An integer hash-code representation of this System.Xml.UniqueId.
        """
        ...

    def ToCharArray(self, chars, offset):
        """
        ToCharArray(self: UniqueId, chars: Array[Char], offset: int) -> int

            Puts the System.Xml.UniqueId value into a ar array.

            chars: The ar array.

            offset: Position in the ar array to start inserting the System.Xml.UniqueId value.

            Returns: Number of entries in the ar array filled by the System.Xml.UniqueId value.
        """
        ...

    def ToString(self):
        """
        ToString(self: UniqueId) -> str

            Displays the System.Xml.UniqueId value in string format.

            Returns: A string representation of the System.Xml.UniqueId value.
        """
        ...

    def TryGetGuid(self, *__args):
        """
        TryGetGuid(self: UniqueId, buffer: Array[Byte], offset: int) -> bool

            Tries to get the value of the System.Xml.UniqueId as a System.Guid and store it in the given byte array at the specified offest.

            buffer: te array that will contain the System.Guid.

            offset: Position in the te array to start inserting the System.Guid value.

            Returns: ue if the value stored in this instance of System.Xml.UniqueId is a System.Guid; otherwise lse.

        TryGetGuid(self: UniqueId) -> (bool, Guid)

            Tries to get the value of the System.Xml.UniqueId as a System.Guid.

            Returns: ue if the UniqueId represents a System.Guid; otherwise lse.
        """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    @property
    def CharArrayLength(self):
        """
        Gets the length of the string representation of the System.Xml.UniqueId.

        Get: CharArrayLength(self: UniqueId) -> int
        """
        ...

    @property
    def IsGuid(self):
        """
        Indicates whether the System.Xml.UniqueId is a System.Guid.

        Get: IsGuid(self: UniqueId) -> bool
        """
        ...



class XmlBinaryReaderSession(object, IXmlDictionary):
    """
    Enables optimized strings to be managed in a dynamic way.

    XmlBinaryReaderSession()
    """
    def Add(self, id, value):
        """
        Add(self: XmlBinaryReaderSession, id: int, value: str) -> XmlDictionaryString

            Creates an System.Xml.XmlDictionaryString from the input parameters and adds it to an internal collection.

            id: The key value.

            value: The value.

            Returns: The newly created System.Xml.XmlDictionaryString that is added to an internal collection.
        """
        ...

    def Clear(self):
        """
        Clear(self: XmlBinaryReaderSession)

            Clears the internal collection of all contents.
        """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...


class XmlBinaryWriterSession: # skipped bases: <type 'object'>
    """
    Enables using a dynamic dictionary to compress common strings that appear in a message and maintain state.

    XmlBinaryWriterSession()
    """
    def Reset(self):
        """
        Reset(self: XmlBinaryWriterSession)

            Clears out the internal collections.
        """
        ...

    def TryAdd(self, value, key):
        """
        TryAdd(self: XmlBinaryWriterSession, value: XmlDictionaryString) -> (bool, int)

            Tries to add an System.Xml.XmlDictionaryString to the internal collection.

            value: The System.Xml.XmlDictionaryString to add.

            Returns: ue if the string could be added; otherwise, lse.
        """
        ...


class XmlDictionary(object, IXmlDictionary):
    """
    Implements a dictionary used to optimize Windows Communication Foundation (WCF)'s XML reader/writer implementations.

    XmlDictionary()

    XmlDictionary(capacity: int)
    """
    def Add(self, value):
        """
        Add(self: XmlDictionary, value: str) -> XmlDictionaryString

            Adds a string to the System.Xml.XmlDictionary.

            value: String to add to the dictionary.

            Returns: The System.Xml.XmlDictionaryString that was added.
        """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    Empty = None


class XmlDictionaryReader(XmlReader): # skipped bases: <type 'IDisposable'>
    """ An stract class that the Windows Communication Foundation (WCF) derives from System.Xml.XmlReader to do serialization and deserialization. """
    @staticmethod
    def CreateBinaryReader(*__args):
        """
        CreateBinaryReader(buffer: Array[Byte], quotas: XmlDictionaryReaderQuotas) -> XmlDictionaryReader

            Creates an instance of System.Xml.XmlDictionaryReader that can read .NET Binary XML Format.

            buffer: The buffer from which to read.

            quotas: The quotas that apply to this operation.

            Returns: An instance of System.Xml.XmlDictionaryReader.

        CreateBinaryReader(buffer: Array[Byte], offset: int, count: int, quotas: XmlDictionaryReaderQuotas) -> XmlDictionaryReader

            Creates an instance of System.Xml.XmlDictionaryReader that can read .NET Binary XML Format.

            buffer: The buffer from which to read.

            offset: The starting position from which to read in buffer.

            count: The number of bytes that can be read from buffer.

            quotas: The quotas that apply to this operation.

            Returns: An instance of System.Xml.XmlDictionaryReader.

        CreateBinaryReader(buffer: Array[Byte], offset: int, count: int, dictionary: IXmlDictionary, quotas: XmlDictionaryReaderQuotas) -> XmlDictionaryReader

            Creates an instance of System.Xml.XmlDictionaryReader that can read .NET Binary XML Format.

            buffer: The buffer from which to read.

            offset: The starting position from which to read in buffer.

            count: The number of bytes that can be read from buffer.

            dictionary: System.Xml.XmlDictionary to use.

            quotas: The quotas that apply to this operation.

            Returns: An instance of System.Xml.XmlDictionaryReader.

        CreateBinaryReader(buffer: Array[Byte], offset: int, count: int, dictionary: IXmlDictionary, quotas: XmlDictionaryReaderQuotas, session: XmlBinaryReaderSession) -> XmlDictionaryReader

            Creates an instance of System.Xml.XmlDictionaryReader that can read .NET Binary XML Format.

            buffer: The buffer from which to read.

            offset: The starting position from which to read in buffer.

            count: The number of bytes that can be read from buffer.

            dictionary: The System.Xml.XmlDictionary to use.

            quotas: The System.Xml.XmlDictionaryReaderQuotas to apply.

            session: The System.Xml.XmlBinaryReaderSession to use.

            Returns: An instance of System.Xml.XmlDictionaryReader.

        CreateBinaryReader(buffer: Array[Byte], offset: int, count: int, dictionary: IXmlDictionary, quotas: XmlDictionaryReaderQuotas, session: XmlBinaryReaderSession, onClose: OnXmlDictionaryReaderClose) -> XmlDictionaryReader

            Creates an instance of System.Xml.XmlDictionaryReader that can read .NET Binary XML Format.

            buffer: The buffer from which to read.

            offset: The starting position from which to read in buffer.

            count: The number of bytes that can be read from buffer.

            dictionary: The System.Xml.XmlDictionary to use.

            quotas: The System.Xml.XmlDictionaryReaderQuotas to apply.

            session: The System.Xml.XmlBinaryReaderSession to use.

            onClose: Delegate to be called when the reader is closed.

            Returns: An instance of System.Xml.XmlDictionaryReader.

        CreateBinaryReader(stream: Stream, quotas: XmlDictionaryReaderQuotas) -> XmlDictionaryReader

            Creates an instance of System.Xml.XmlDictionaryReader that can read .NET Binary XML Format.

            stream: The stream from which to read.

            quotas: The quotas that apply to this operation.

            Returns: An instance of System.Xml.XmlDictionaryReader.

        CreateBinaryReader(stream: Stream, dictionary: IXmlDictionary, quotas: XmlDictionaryReaderQuotas) -> XmlDictionaryReader

            Creates an instance of System.Xml.XmlDictionaryReader that can read .NET Binary XML Format.

            stream: The stream from which to read.

            dictionary: System.Xml.XmlDictionary to use.

            quotas: The quotas that apply to this operation.

            Returns: An instance of System.Xml.XmlDictionaryReader.

        CreateBinaryReader(stream: Stream, dictionary: IXmlDictionary, quotas: XmlDictionaryReaderQuotas, session: XmlBinaryReaderSession) -> XmlDictionaryReader

            Creates an instance of System.Xml.XmlDictionaryReader that can read .NET Binary XML Format.

            stream: The stream from which to read.

            dictionary: System.Xml.XmlDictionary to use.

            quotas: The quotas that apply to this operation.

            session: System.Xml.XmlBinaryReaderSession to use.

            Returns: An instance of System.Xml.XmlDictionaryReader.

        CreateBinaryReader(stream: Stream, dictionary: IXmlDictionary, quotas: XmlDictionaryReaderQuotas, session: XmlBinaryReaderSession, onClose: OnXmlDictionaryReaderClose) -> XmlDictionaryReader

            Creates an instance of System.Xml.XmlDictionaryReader that can read .NET Binary XML Format.

            stream: The stream from which to read.

            dictionary: System.Xml.XmlDictionary to use.

            quotas: System.Xml.XmlDictionaryReaderQuotas to apply.

            session: System.Xml.XmlBinaryReaderSession to use.

            onClose: Delegate to be called when the reader is closed.

            Returns: An instance of System.Xml.XmlDictionaryReader.
        """
        ...

    @staticmethod
    def CreateDictionaryReader(reader):
        """
        CreateDictionaryReader(reader: XmlReader) -> XmlDictionaryReader

            Creates an instance of System.Xml.XmlDictionaryReader from an existing System.Xml.XmlReader.

            reader: An instance of System.Xml.XmlReader.

            Returns: An instance of System.Xml.XmlDictionaryReader.
        """
        ...

    @staticmethod
    def CreateMtomReader(*__args):
        """
        CreateMtomReader(stream: Stream, encoding: Encoding, quotas: XmlDictionaryReaderQuotas) -> XmlDictionaryReader

            Creates an instance of System.Xml.XmlDictionaryReader that reads XML in the MTOM format.

            stream: The stream from which to read.

            encoding: The possible character encoding of the stream.

            quotas: The quotas to apply to this reader.

            Returns: An instance of System.Xml.XmlDictionaryReader.

        CreateMtomReader(stream: Stream, encodings: Array[Encoding], quotas: XmlDictionaryReaderQuotas) -> XmlDictionaryReader

            Creates an instance of System.Xml.XmlDictionaryReader that reads XML in the MTOM format.

            stream: The stream from which to read.

            encodings: The possible character encodings of the stream.

            quotas: The quotas to apply to this reader.

            Returns: An instance of System.Xml.XmlDictionaryReader.

        CreateMtomReader(stream: Stream, encodings: Array[Encoding], contentType: str, quotas: XmlDictionaryReaderQuotas) -> XmlDictionaryReader

            Creates an instance of System.Xml.XmlDictionaryReader that reads XML in the MTOM format.

            stream: The stream from which to read.

            encodings: The possible character encodings of the stream.

            contentType: The Content-Type MIME type of the message.

            quotas: The quotas to apply to this reader.

            Returns: An instance of System.Xml.XmlDictionaryReader.

        CreateMtomReader(stream: Stream, encodings: Array[Encoding], contentType: str, quotas: XmlDictionaryReaderQuotas, maxBufferSize: int, onClose: OnXmlDictionaryReaderClose) -> XmlDictionaryReader

            Creates an instance of System.Xml.XmlDictionaryReader that reads XML in the MTOM format.

            stream: The stream from which to read.

            encodings: The possible character encodings of the stream.

            contentType: The Content-Type MIME type of the message.

            quotas: The MIME type of the message.

            maxBufferSize: The System.Xml.XmlDictionaryReaderQuotas to apply to the reader.

            onClose: The delegate to be called when the reader is closed.

            Returns: An instance of System.Xml.XmlDictionaryReader.

        CreateMtomReader(buffer: Array[Byte], offset: int, count: int, encoding: Encoding, quotas: XmlDictionaryReaderQuotas) -> XmlDictionaryReader

            Creates an instance of System.Xml.XmlDictionaryReader that reads XML in the MTOM format.

            buffer: The buffer from which to read.

            offset: The starting position from which to read in buffer.

            count: The number of bytes that can be read from buffer.

            encoding: The possible character encoding of the input.

            quotas: The quotas to apply to this reader.

            Returns: An instance of System.Xml.XmlDictionaryReader.

        CreateMtomReader(buffer: Array[Byte], offset: int, count: int, encodings: Array[Encoding], quotas: XmlDictionaryReaderQuotas) -> XmlDictionaryReader

            Creates an instance of System.Xml.XmlDictionaryReader that reads XML in the MTOM format.

            buffer: The buffer from which to read.

            offset: The starting position from which to read in buffer.

            count: The number of bytes that can be read from buffer.

            encodings: The possible character encodings of the input.

            quotas: The quotas to apply to this reader.

            Returns: An instance of System.Xml.XmlDictionaryReader.

        CreateMtomReader(buffer: Array[Byte], offset: int, count: int, encodings: Array[Encoding], contentType: str, quotas: XmlDictionaryReaderQuotas) -> XmlDictionaryReader

            Creates an instance of System.Xml.XmlDictionaryReader that reads XML in the MTOM format.

            buffer: The buffer from which to read.

            offset: The starting position from which to read in buffer.

            count: The number of bytes that can be read from buffer.

            encodings: The possible character encodings of the input.

            contentType: The Content-Type MIME type of the message.

            quotas: The quotas to apply to this reader.

            Returns: An instance of System.Xml.XmlDictionaryReader.

        CreateMtomReader(buffer: Array[Byte], offset: int, count: int, encodings: Array[Encoding], contentType: str, quotas: XmlDictionaryReaderQuotas, maxBufferSize: int, onClose: OnXmlDictionaryReaderClose) -> XmlDictionaryReader

            Creates an instance of System.Xml.XmlDictionaryReader that reads XML in the MTOM format.

            buffer: The buffer from which to read.

            offset: The starting position from which to read in buffer.

            count: The number of bytes that can be read from buffer.

            encodings: The possible character encodings of the input.

            contentType: The Content-Type MIME type of the message.

            quotas: The System.Xml.XmlDictionaryReaderQuotas to apply to the reader.

            maxBufferSize: The maximum allowed size of the buffer.

            onClose: The delegate to be called when the reader is closed.

            Returns: An instance of System.Xml.XmlDictionaryReader.
        """
        ...

    @staticmethod
    def CreateTextReader(*__args):
        """
        CreateTextReader(buffer: Array[Byte], quotas: XmlDictionaryReaderQuotas) -> XmlDictionaryReader

            Creates an instance of System.Xml.XmlDictionaryReader.

            buffer: The buffer from which to read.

            quotas: The quotas applied to the reader.

            Returns: An instance of System.Xml.XmlDictionaryReader.

        CreateTextReader(buffer: Array[Byte], offset: int, count: int, quotas: XmlDictionaryReaderQuotas) -> XmlDictionaryReader

            Creates an instance of System.Xml.XmlDictionaryReader.

            buffer: The buffer from which to read.

            offset: The starting position from which to read in buffer.

            count: The number of bytes that can be read from buffer.

            quotas: The quotas applied to the reader.

            Returns: An instance of System.Xml.XmlDictionaryReader.

        CreateTextReader(buffer: Array[Byte], offset: int, count: int, encoding: Encoding, quotas: XmlDictionaryReaderQuotas, onClose: OnXmlDictionaryReaderClose) -> XmlDictionaryReader

            Creates an instance of System.Xml.XmlDictionaryReader.

            buffer: The buffer from which to read.

            offset: The starting position from which to read in buffer.

            count: The number of bytes that can be read from buffer.

            encoding: The System.Text.Encoding object that specifies the encoding properties to apply.

            quotas: The System.Xml.XmlDictionaryReaderQuotas to apply.

            onClose: The delegate to be called when the reader is closed.

            Returns: An instance of System.Xml.XmlDictionaryReader.

        CreateTextReader(stream: Stream, quotas: XmlDictionaryReaderQuotas) -> XmlDictionaryReader

            Creates an instance of System.Xml.XmlDictionaryReader.

            stream: The stream from which to read.

            quotas: The quotas applied to the reader.

            Returns: An instance of System.Xml.XmlDictionaryReader.

        CreateTextReader(stream: Stream, encoding: Encoding, quotas: XmlDictionaryReaderQuotas, onClose: OnXmlDictionaryReaderClose) -> XmlDictionaryReader

            Creates an instance of System.Xml.XmlDictionaryReader.

            stream: The stream from which to read.

            encoding: The System.Text.Encoding object that specifies the encoding properties to apply.

            quotas: The System.Xml.XmlDictionaryReaderQuotas to apply.

            onClose: The delegate to be called when the reader is closed.

            Returns: An instance of System.Xml.XmlDictionaryReader.
        """
        ...

    def EndCanonicalization(self):
        """
        EndCanonicalization(self: XmlDictionaryReader)

            This method is not yet implemented.
        """
        ...

    def GetNonAtomizedNames(self, localName, namespaceUri):
        """
        GetNonAtomizedNames(self: XmlDictionaryReader) -> (str, str)

            Gets non-atomized names.
        """
        ...

    def IndexOfLocalName(self, localNames, namespaceUri):
        """
        IndexOfLocalName(self: XmlDictionaryReader, localNames: Array[str], namespaceUri: str) -> int

            Gets the index of the local name of the current node within an array of names.

            localNames: The string array of local names to be searched.

            namespaceUri: The namespace of current node.

            Returns: The index of the local name of the current node within an array of names.

        IndexOfLocalName(self: XmlDictionaryReader, localNames: Array[XmlDictionaryString], namespaceUri: XmlDictionaryString) -> int

            Gets the index of the local name of the current node within an array of names.

            localNames: The System.Xml.XmlDictionaryString array of local names to be searched.

            namespaceUri: The namespace of current node.

            Returns: The index of the local name of the current node within an array of names.
        """
        ...

    def IsLocalName(self, localName):
        """
        IsLocalName(self: XmlDictionaryReader, localName: str) -> bool

            Checks whether the parameter, localName, is the local name of the current node.

            localName: The local name of the current node.

            Returns: ue if localName matches local name of the current node; otherwise lse.

        IsLocalName(self: XmlDictionaryReader, localName: XmlDictionaryString) -> bool

            Checks whether the parameter, localName, is the local name of the current node.

            localName: An System.Xml.XmlDictionaryString that represents the local name of the current node.

            Returns: ue if localName matches local name of the current node; otherwise lse.
        """
        ...

    def IsNamespaceUri(self, namespaceUri):
        """
        IsNamespaceUri(self: XmlDictionaryReader, namespaceUri: str) -> bool

            Checks whether the parameter, namespaceUri, is the namespace of the current node.

            namespaceUri: The namespace of current node.

            Returns: ue if namespaceUri matches namespace of the current node; otherwise lse.

        IsNamespaceUri(self: XmlDictionaryReader, namespaceUri: XmlDictionaryString) -> bool

            Checks whether the parameter, namespaceUri, is the namespace of the current node.

            namespaceUri: Namespace of current node.

            Returns: ue if namespaceUri matches namespace of the current node; otherwise lse.
        """
        ...

    def IsStartArray(self, type):
        """
        IsStartArray(self: XmlDictionaryReader) -> (bool, Type)

            Checks whether the reader is positioned at the start of an array. This class returns lse, but derived classes that have the concept of arrays might return ue.

            Returns: ue if the reader is positioned at the start of an array node; otherwise lse.
        """
        ...

    def IsTextNode(self, *args): #cannot find CLR method
        """
        IsTextNode(self: XmlDictionaryReader, nodeType: XmlNodeType) -> bool

            Tests whether the current node is a text node.

            nodeType: Type of the node being tested.

            Returns: ue if the node type is System.Xml.XmlNodeType.Text, System.Xml.XmlNodeType.Whitespace, System.Xml.XmlNodeType.SignificantWhitespace, System.Xml.XmlNodeType.CDATA, or 

             System.Xml.XmlNodeType.Attribute; otherwise lse.
        """
        ...

    def MoveToStartElement(self, *__args):
        """
        MoveToStartElement(self: XmlDictionaryReader)

            Tests whether the current content node is a start element or an empty element.

        MoveToStartElement(self: XmlDictionaryReader, name: str)

            Tests whether the current content node is a start element or an empty element and if the System.Xml.XmlReader.Name property of the element matches the given argument.

            name: The System.Xml.XmlReader.Name property of the element.

        MoveToStartElement(self: XmlDictionaryReader, localName: str, namespaceUri: str)

            Tests whether the current content node is a start element or an empty element and if the System.Xml.XmlReader.LocalName and System.Xml.XmlReader.NamespaceURI 

             properties of the element matches the given arguments.

            localName: The local name of the element.

            namespaceUri: The namespace URI of the element.

        MoveToStartElement(self: XmlDictionaryReader, localName: XmlDictionaryString, namespaceUri: XmlDictionaryString)

            Tests whether the current content node is a start element or an empty element and if the System.Xml.XmlReader.LocalName and System.Xml.XmlReader.NamespaceURI 

             properties of the element matches the given argument.

            localName: The local name of the element.

            namespaceUri: The namespace URI of the element.
        """
        ...

    def ReadArray(self, localName, namespaceUri, array, offset, count):
        """
        ReadArray(self: XmlDictionaryReader, localName: str, namespaceUri: str, array: Array[bool], offset: int, count: int) -> int

            Reads repeated occurrences of System.Boolean nodes into a typed array.

            localName: The local name of the element.

            namespaceUri: The local name of the element.

            array: The array into which the nodes are put.

            offset: The starting index in the array.

            count: The number of nodes to put in the array.

            Returns: The number of nodes put in the array.

        ReadArray(self: XmlDictionaryReader, localName: XmlDictionaryString, namespaceUri: XmlDictionaryString, array: Array[Guid], offset: int, count: int) -> int

            Reads repeated occurrences of System.Guid nodes into a typed array.

            localName: The local name of the element.

            namespaceUri: The namespace URI of the element.

            array: The array into which the nodes are put.

            offset: The starting index in the array.

            count: The number of nodes to put in the array.

            Returns: The number of nodes put in the array.

        ReadArray(self: XmlDictionaryReader, localName: str, namespaceUri: str, array: Array[Guid], offset: int, count: int) -> int

            Reads repeated occurrences of System.Guid nodes into a typed array.

            localName: The local name of the element.

            namespaceUri: The namespace URI of the element.

            array: The array into which the nodes are put.

            offset: The starting index in the array.

            count: The number of nodes to put in the array.

            Returns: The number of nodes put in the array.

        ReadArray(self: XmlDictionaryReader, localName: XmlDictionaryString, namespaceUri: XmlDictionaryString, array: Array[DateTime], offset: int, count: int) -> int

            Reads repeated occurrences of System.DateTime nodes into a typed array.

            localName: The local name of the element.

            namespaceUri: The namespace URI of the element.

            array: The array into which the nodes are put.

            offset: The starting index in the array.

            count: The number of nodes to put in the array.

            Returns: The number of nodes put in the array.

        ReadArray(self: XmlDictionaryReader, localName: str, namespaceUri: str, array: Array[DateTime], offset: int, count: int) -> int

            Reads repeated occurrences of System.DateTime nodes into a typed array.

            localName: The local name of the element.

            namespaceUri: The namespace URI of the element.

            array: The array into which the nodes are put.

            offset: The starting index in the array.

            count: The number of nodes to put in the array.

            Returns: The number of nodes put in the array.

        ReadArray(self: XmlDictionaryReader, localName: XmlDictionaryString, namespaceUri: XmlDictionaryString, array: Array[Decimal], offset: int, count: int) -> int

            Reads repeated occurrences of System.Decimal nodes into a typed array.

            localName: The local name of the element.

            namespaceUri: The namespace URI of the element.

            array: The array into which the nodes are put.

            offset: The starting index in the array.

            count: The number of nodes to put in the array.

            Returns: The number of nodes put in the array.

        ReadArray(self: XmlDictionaryReader, localName: str, namespaceUri: str, array: Array[Decimal], offset: int, count: int) -> int

            Reads repeated occurrences of System.Decimal nodes into a typed array.

            localName: The local name of the element.

            namespaceUri: The namespace URI of the element.

            array: The array into which the nodes are put.

            offset: The starting index in the array.

            count: The number of nodes to put in the array.

            Returns: The number of nodes put in the array.

        ReadArray(self: XmlDictionaryReader, localName: XmlDictionaryString, namespaceUri: XmlDictionaryString, array: Array[float], offset: int, count: int) -> int

            Reads repeated occurrences of System.Double nodes type into a typed array.

            localName: The local name of the element.

            namespaceUri: The namespace URI of the element.

            array: The array into which the nodes are put.

            offset: The starting index in the array.

            count: The number of nodes to put in the array.

            Returns: The number of nodes put in the array.

        ReadArray(self: XmlDictionaryReader, localName: str, namespaceUri: str, array: Array[float], offset: int, count: int) -> int

            Reads repeated occurrences of System.Double nodes into a typed array.

            localName: The local name of the element.

            namespaceUri: The namespace URI of the element.

            array: The array into which the nodes are put.

            offset: The starting index in the array.

            count: The number of nodes to put in the array.

            Returns: The number of nodes put in the array.

        ReadArray(self: XmlDictionaryReader, localName: XmlDictionaryString, namespaceUri: XmlDictionaryString, array: Array[Single], offset: int, count: int) -> int

            Reads repeated occurrences of oat numbers into a typed array.

            localName: The local name of the element.

            namespaceUri: The namespace URI of the element.

            array: The array into which the float numbers are put.

            offset: The starting index in the array.

            count: The number of float numbers to put in the array.

            Returns: The number of float numbers put in the array.

        ReadArray(self: XmlDictionaryReader, localName: str, namespaceUri: str, array: Array[Single], offset: int, count: int) -> int

            Reads repeated occurrences of oat numbers into a typed array.

            localName: The local name of the element.

            namespaceUri: The namespace URI of the element.

            array: The array into which the float numbers are put.

            offset: The starting index in the array.

            count: The number of float numbers to put in the array.

            Returns: The umber of float numbers put in the array.

        ReadArray(self: XmlDictionaryReader, localName: XmlDictionaryString, namespaceUri: XmlDictionaryString, array: Array[Int64], offset: int, count: int) -> int

            Reads repeated occurrences of ng integers into a typed array.

            localName: The local name of the element.

            namespaceUri: The namespace URI of the element.

            array: The array into which the integers are put.

            offset: The starting index in the array.

            count: The number of integers to put in the array.

            Returns: The number of integers put in the array.

        ReadArray(self: XmlDictionaryReader, localName: str, namespaceUri: str, array: Array[Int64], offset: int, count: int) -> int

            Reads repeated occurrences of ng integers into a typed array.

            localName: The local name of the element.

            namespaceUri: The namespace URI of the element.

            array: The array into which the integers are put.

            offset: The starting index in the array.

            count: The number of integers to put in the array.

            Returns: The number of integers put in the array.

        ReadArray(self: XmlDictionaryReader, localName: XmlDictionaryString, namespaceUri: XmlDictionaryString, array: Array[int], offset: int, count: int) -> int

            Reads repeated occurrences of integers into a typed array.

            localName: The local name of the element.

            namespaceUri: The namespace URI of the element.

            array: The array into which the integers are put.

            offset: The starting index in the array.

            count: The number of integers to put in the array.

            Returns: The number of integers put in the array.

        ReadArray(self: XmlDictionaryReader, localName: str, namespaceUri: str, array: Array[int], offset: int, count: int) -> int

            Reads repeated occurrences of integers into a typed array.

            localName: The local name of the element.

            namespaceUri: The namespace URI of the element.

            array: The array into which the integers are put.

            offset: The starting index in the array.

            count: The number of integers to put in the array.

            Returns: The number of integers put in the array.

        ReadArray(self: XmlDictionaryReader, localName: XmlDictionaryString, namespaceUri: XmlDictionaryString, array: Array[Int16], offset: int, count: int) -> int

            Reads repeated occurrences of ort integers into a typed array.

            localName: The local name of the element.

            namespaceUri: The namespace URI of the element.

            array: The array into which the integers are put.

            offset: The starting index in the array.

            count: The number of integers to put in the array.

            Returns: The number of integers put in the array.

        ReadArray(self: XmlDictionaryReader, localName: str, namespaceUri: str, array: Array[Int16], offset: int, count: int) -> int

            Reads repeated occurrences of ort integers into a typed array.

            localName: The local name of the element.

            namespaceUri: The namespace URI of the element.

            array: The array into which the integers are put.

            offset: The starting index in the array.

            count: The number of integers to put in the array.

            Returns: The number of integers put in the array.

        ReadArray(self: XmlDictionaryReader, localName: XmlDictionaryString, namespaceUri: XmlDictionaryString, array: Array[bool], offset: int, count: int) -> int

            Reads repeated occurrences of System.Boolean nodes into a typed array.

            localName: The local name of the element.

            namespaceUri: The namespace URI of the element.

            array: The array into which the nodes are put.

            offset: The starting index in the array.

            count: The number of nodes to put in the array.

            Returns: The number of nodes put in the array.

        ReadArray(self: XmlDictionaryReader, localName: str, namespaceUri: str, array: Array[TimeSpan], offset: int, count: int) -> int

            Reads repeated occurrences of System.TimeSpan nodes into a typed array.

            localName: The local name of the element.

            namespaceUri: The namespace URI of the element.

            array: The array into which the nodes are put.

            offset: The starting index in the array.

            count: The number of nodes to put in the array.

            Returns: The number of nodes put in the array.

        ReadArray(self: XmlDictionaryReader, localName: XmlDictionaryString, namespaceUri: XmlDictionaryString, array: Array[TimeSpan], offset: int, count: int) -> int

            Reads repeated occurrences of System.TimeSpan nodes into a typed array.

            localName: The local name of the element.

            namespaceUri: The namespace URI of the element.

            array: The array into which the nodes are put.

            offset: The starting index in the array.

            count: The number of nodes to put in the array.

            Returns: The number of nodes put in the array.
        """
        ...

    def ReadBooleanArray(self, localName, namespaceUri):
        """
        ReadBooleanArray(self: XmlDictionaryReader, localName: str, namespaceUri: str) -> Array[bool]

            Reads repeated occurrences of System.Boolean nodes into a typed array.

            localName: The local name of the element.

            namespaceUri: The namespace URI of the element.

            Returns: A System.Boolean array of the System.Boolean nodes.

        ReadBooleanArray(self: XmlDictionaryReader, localName: XmlDictionaryString, namespaceUri: XmlDictionaryString) -> Array[bool]

            Reads repeated occurrences of System.Boolean nodes into a typed array.

            localName: The local name of the element.

            namespaceUri: The namespace URI of the element.

            Returns: A System.Boolean array of the System.Boolean nodes.
        """
        ...

    def ReadContentAsChars(self, chars, offset, count):
        """
        ReadContentAsChars(self: XmlDictionaryReader, chars: Array[Char], offset: int, count: int) -> int

            Reads the content into a ar array.

            chars: The array into which the characters are put.

            offset: The starting index in the array.

            count: The number of characters to put in the array.

            Returns: Number of characters read.
        """
        ...

    def ReadContentAsGuid(self):
        """
        ReadContentAsGuid(self: XmlDictionaryReader) -> Guid

            Converts a node's content to id.

            Returns: The id representation of node's content.
        """
        ...

    def ReadContentAsQualifiedName(self, localName, namespaceUri):
        """
        ReadContentAsQualifiedName(self: XmlDictionaryReader) -> (str, str)

            Converts a node's content to a qualified name representation.
        """
        ...

    def ReadContentAsTimeSpan(self):
        """
        ReadContentAsTimeSpan(self: XmlDictionaryReader) -> TimeSpan

            Converts a node's content to System.TimeSpan.

            Returns: System.TimeSpan representation of node's content.
        """
        ...

    def ReadContentAsUniqueId(self):
        """
        ReadContentAsUniqueId(self: XmlDictionaryReader) -> UniqueId

            Converts a node's content to a unique identifier.

            Returns: The node's content represented as a unique identifier.
        """
        ...

    def ReadDateTimeArray(self, localName, namespaceUri):
        """
        ReadDateTimeArray(self: XmlDictionaryReader, localName: str, namespaceUri: str) -> Array[DateTime]

            Converts a node's content to a System.DateTime array.

            localName: The local name of the element.

            namespaceUri: The namespace URI of the element.

            Returns: The node's content represented as a System.DateTime array.

        ReadDateTimeArray(self: XmlDictionaryReader, localName: XmlDictionaryString, namespaceUri: XmlDictionaryString) -> Array[DateTime]

            Converts a node's content to a System.DateTime array.

            localName: The local name of the element.

            namespaceUri: The namespace URI of the element.

            Returns: The node's content represented as a System.DateTime array.
        """
        ...

    def ReadDecimalArray(self, localName, namespaceUri):
        """
        ReadDecimalArray(self: XmlDictionaryReader, localName: str, namespaceUri: str) -> Array[Decimal]

            Converts a node's content to a System.Decimal array.

            localName: The local name of the element.

            namespaceUri: The namespace URI of the element.

            Returns: The node's content represented as a System.Decimal array.

        ReadDecimalArray(self: XmlDictionaryReader, localName: XmlDictionaryString, namespaceUri: XmlDictionaryString) -> Array[Decimal]

            Converts a node's content to a System.Decimal array.

            localName: The local name of the element.

            namespaceUri: The namespace URI of the element.

            Returns: The node's content represented as a System.Decimal array.
        """
        ...

    def ReadDoubleArray(self, localName, namespaceUri):
        """
        ReadDoubleArray(self: XmlDictionaryReader, localName: str, namespaceUri: str) -> Array[float]

            Converts a node's content to a System.Double array.

            localName: The local name of the element.

            namespaceUri: The namespace URI of the element.

            Returns: The node's content represented as a System.Double array.

        ReadDoubleArray(self: XmlDictionaryReader, localName: XmlDictionaryString, namespaceUri: XmlDictionaryString) -> Array[float]

            Converts a node's content to a System.Double array.

            localName: The local name of the element.

            namespaceUri: The namespace URI of the element.

            Returns: The node's content represented as a System.Double array.
        """
        ...

    def ReadElementContentAsGuid(self):
        """
        ReadElementContentAsGuid(self: XmlDictionaryReader) -> Guid

            Converts an element's content to a System.Guid.

            Returns: The node's content represented as a System.Guid.
        """
        ...

    def ReadElementContentAsTimeSpan(self):
        """
        ReadElementContentAsTimeSpan(self: XmlDictionaryReader) -> TimeSpan

            Converts an element's content to a System.TimeSpan.

            Returns: The node's content represented as a System.TimeSpan.
        """
        ...

    def ReadElementContentAsUniqueId(self):
        """
        ReadElementContentAsUniqueId(self: XmlDictionaryReader) -> UniqueId

            Converts an element's content to a unique identifier.

            Returns: The node's content represented as a unique identifier.
        """
        ...

    def ReadFullStartElement(self, *__args):
        """
        ReadFullStartElement(self: XmlDictionaryReader)

            Checks whether the current node is an element and advances the reader to the next node.

        ReadFullStartElement(self: XmlDictionaryReader, name: str)

            Checks whether the current node is an element with the given name and advances the reader to the next node.

            name: The qualified name of the element.

        ReadFullStartElement(self: XmlDictionaryReader, localName: str, namespaceUri: str)

            Checks whether the current node is an element with the given localName and namespaceUri and advances the reader to the next node.

            localName: The local name of the element.

            namespaceUri: The namespace URI of the element.

        ReadFullStartElement(self: XmlDictionaryReader, localName: XmlDictionaryString, namespaceUri: XmlDictionaryString)

            Checks whether the current node is an element with the given localName and namespaceUri and advances the reader to the next node.

            localName: The local name of the element.

            namespaceUri: The namespace URI of the element.
        """
        ...

    def ReadGuidArray(self, localName, namespaceUri):
        """
        ReadGuidArray(self: XmlDictionaryReader, localName: str, namespaceUri: str) -> Array[Guid]

            Reads the contents of a series of nodes with the given localName and namespaceUri into an array of System.Guid.

            localName: The local name of the element.

            namespaceUri: The namespace URI of the element.

            Returns: An array of System.Guid.

        ReadGuidArray(self: XmlDictionaryReader, localName: XmlDictionaryString, namespaceUri: XmlDictionaryString) -> Array[Guid]

            Reads the contents of a series of nodes with the given localName and namespaceUri into an array of System.Guid.

            localName: The local name of the element.

            namespaceUri: The namespace URI of the element.

            Returns: An array of System.Guid.
        """
        ...

    def ReadInt16Array(self, localName, namespaceUri):
        """
        ReadInt16Array(self: XmlDictionaryReader, localName: str, namespaceUri: str) -> Array[Int16]

            Reads the contents of a series of nodes with the given localName and namespaceUri into an array of ort integers (System.Int16).

            localName: The local name of the element.

            namespaceUri: The namespace URI of the element.

            Returns: An array of ort integers (System.Int16).

        ReadInt16Array(self: XmlDictionaryReader, localName: XmlDictionaryString, namespaceUri: XmlDictionaryString) -> Array[Int16]

            Reads the contents of a series of nodes with the given localName and namespaceUri into an array of ort integers (System.Int16).

            localName: The local name of the element.

            namespaceUri: The namespace URI of the element.

            Returns: An array of ort integers (System.Int16).
        """
        ...

    def ReadInt32Array(self, localName, namespaceUri):
        """
        ReadInt32Array(self: XmlDictionaryReader, localName: str, namespaceUri: str) -> Array[int]

            Reads the contents of a series of nodes with the given localName and namespaceUri into an array of integers (System.Int32).

            localName: The local name of the element.

            namespaceUri: The namespace URI of the element.

            Returns: An array of integers (System.Int32).

        ReadInt32Array(self: XmlDictionaryReader, localName: XmlDictionaryString, namespaceUri: XmlDictionaryString) -> Array[int]

            Reads the contents of a series of nodes with the given localName and namespaceUri into an array of integers (System.Int32).

            localName: The local name of the element.

            namespaceUri: The namespace URI of the element.

            Returns: An array of integers (System.Int32).
        """
        ...

    def ReadInt64Array(self, localName, namespaceUri):
        """
        ReadInt64Array(self: XmlDictionaryReader, localName: str, namespaceUri: str) -> Array[Int64]

            Reads the contents of a series of nodes with the given localName and namespaceUri into an array of ng integers (System.Int64).

            localName: The local name of the element.

            namespaceUri: The namespace URI of the element.

            Returns: An array of ng integers (System.Int64).

        ReadInt64Array(self: XmlDictionaryReader, localName: XmlDictionaryString, namespaceUri: XmlDictionaryString) -> Array[Int64]

            Reads the contents of a series of nodes with the given localName and namespaceUri into an array of ng integers (System.Int64).

            localName: The local name of the element.

            namespaceUri: The namespace URI of the element.

            Returns: An array of ng integers (System.Int64).
        """
        ...

    def ReadSingleArray(self, localName, namespaceUri):
        """
        ReadSingleArray(self: XmlDictionaryReader, localName: str, namespaceUri: str) -> Array[Single]

            Reads the contents of a series of nodes with the given localName and namespaceUri into an array of oat numbers (System.Single).

            localName: The local name of the element.

            namespaceUri: The namespace URI of the element.

            Returns: An array of oat numbers (System.Single).

        ReadSingleArray(self: XmlDictionaryReader, localName: XmlDictionaryString, namespaceUri: XmlDictionaryString) -> Array[Single]

            Reads the contents of a series of nodes with the given localName and namespaceUri into an array of oat numbers (System.Single).

            localName: The local name of the element.

            namespaceUri: The namespace URI of the element.

            Returns: An array of oat numbers (System.Single).
        """
        ...

    def ReadTimeSpanArray(self, localName, namespaceUri):
        """
        ReadTimeSpanArray(self: XmlDictionaryReader, localName: str, namespaceUri: str) -> Array[TimeSpan]

            Reads the contents of a series of nodes with the given localName and namespaceUri into a System.TimeSpan array.

            localName: The local name of the element.

            namespaceUri: The namespace URI of the element.

            Returns: A System.TimeSpan array.

        ReadTimeSpanArray(self: XmlDictionaryReader, localName: XmlDictionaryString, namespaceUri: XmlDictionaryString) -> Array[TimeSpan]

            Reads the contents of a series of nodes with the given localName and namespaceUri into a System.TimeSpan array.

            localName: The local name of the element.

            namespaceUri: The namespace URI of the element.

            Returns: A System.TimeSpan array.
        """
        ...

    def ReadValueAsBase64(self, buffer, offset, count):
        """
        ReadValueAsBase64(self: XmlDictionaryReader, buffer: Array[Byte], offset: int, count: int) -> int

            Not implemented.

            buffer: The buffer from which to read.

            offset: The starting position from which to read in buffer.

            count: The number of bytes that can be read from buffer.

            Returns: Not implemented.
        """
        ...

    def StartCanonicalization(self, stream, includeComments, inclusivePrefixes):
        """
        StartCanonicalization(self: XmlDictionaryReader, stream: Stream, includeComments: bool, inclusivePrefixes: Array[str])

            This method is not yet implemented.

            stream: The stream to read from.

            includeComments: Determines whether comments are included.

            inclusivePrefixes: The prefixes to be included.
        """
        ...

    def TryGetArrayLength(self, count):
        """
        TryGetArrayLength(self: XmlDictionaryReader) -> (bool, int)

            Not implemented in this class (it always returns lse). May be overridden in derived classes.

            Returns: lse, unless overridden in a derived class.
        """
        ...

    def TryGetBase64ContentLength(self, length):
        """
        TryGetBase64ContentLength(self: XmlDictionaryReader) -> (bool, int)

            Not implemented in this class (it always returns lse). May be overridden in derived classes.

            Returns: lse, unless overridden in a derived class.
        """
        ...

    def TryGetLocalNameAsDictionaryString(self, localName):
        """
        TryGetLocalNameAsDictionaryString(self: XmlDictionaryReader) -> (bool, XmlDictionaryString)

            Not implemented in this class (it always returns lse). May be overridden in derived classes.

            Returns: lse, unless overridden in a derived class.
        """
        ...

    def TryGetNamespaceUriAsDictionaryString(self, namespaceUri):
        """
        TryGetNamespaceUriAsDictionaryString(self: XmlDictionaryReader) -> (bool, XmlDictionaryString)

            Not implemented in this class (it always returns lse). May be overridden in derived classes.

            Returns: lse, unless overridden in a derived class.
        """
        ...

    def TryGetValueAsDictionaryString(self, value):
        """
        TryGetValueAsDictionaryString(self: XmlDictionaryReader) -> (bool, XmlDictionaryString)

            Not implemented in this class (it always returns lse). May be overridden in derived classes.

            Returns: lse, unless overridden in a derived class.
        """
        ...

    @property
    def CanCanonicalize(self):
        """
        This property always returns lse. Its derived classes can override to return ue if they support canonicalization.

        Get: CanCanonicalize(self: XmlDictionaryReader) -> bool
        """
        ...

    @property
    def Quotas(self):
        """
        Gets the quota values that apply to the current instance of this class.

        Get: Quotas(self: XmlDictionaryReader) -> XmlDictionaryReaderQuotas
        """
        ...



class XmlDictionaryReaderQuotas: # skipped bases: <type 'object'>
    """
    Contains configurable quota values for XmlDictionaryReaders.

    XmlDictionaryReaderQuotas()
    """
    def CopyTo(self, quotas):
        """
        CopyTo(self: XmlDictionaryReaderQuotas, quotas: XmlDictionaryReaderQuotas)

            Sets the properties on a passed-in quotas instance, based on the values in this instance.

            quotas: The System.Xml.XmlDictionaryReaderQuotas instance to which to copy values.
        """
        ...

    @property
    def MaxArrayLength(self):
        """
        Gets and sets the maximum allowed array length.

        Get: MaxArrayLength(self: XmlDictionaryReaderQuotas) -> int

        Set: MaxArrayLength(self: XmlDictionaryReaderQuotas) = value
        """
        ...

    @property
    def MaxBytesPerRead(self):
        """
        Gets and sets the maximum allowed bytes returned for each read.

        Get: MaxBytesPerRead(self: XmlDictionaryReaderQuotas) -> int

        Set: MaxBytesPerRead(self: XmlDictionaryReaderQuotas) = value
        """
        ...

    @property
    def MaxDepth(self):
        """
        Gets and sets the maximum nested node depth.

        Get: MaxDepth(self: XmlDictionaryReaderQuotas) -> int

        Set: MaxDepth(self: XmlDictionaryReaderQuotas) = value
        """
        ...

    @property
    def MaxNameTableCharCount(self):
        """
        Gets and sets the maximum characters allowed in a table name.

        Get: MaxNameTableCharCount(self: XmlDictionaryReaderQuotas) -> int

        Set: MaxNameTableCharCount(self: XmlDictionaryReaderQuotas) = value
        """
        ...

    @property
    def MaxStringContentLength(self):
        """
        Gets and sets the maximum string length returned by the reader.

        Get: MaxStringContentLength(self: XmlDictionaryReaderQuotas) -> int

        Set: MaxStringContentLength(self: XmlDictionaryReaderQuotas) = value
        """
        ...

    @property
    def ModifiedQuotas(self):
        """
        Gets the modified quotas for the System.Xml.XmlDictionaryReaderQuotas.

        Get: ModifiedQuotas(self: XmlDictionaryReaderQuotas) -> XmlDictionaryReaderQuotaTypes
        """
        ...


    Max = None


class XmlDictionaryReaderQuotaTypes(Enum): # skipped bases: <type 'IComparable'>, <type 'IFormattable'>, <type 'IConvertible'>
    """
    Enumerates the configurable quota values for XmlDictionaryReaders.

    enum (flags) XmlDictionaryReaderQuotaTypes, values: MaxArrayLength (4), MaxBytesPerRead (8), MaxDepth (1), MaxNameTableCharCount (16), MaxStringContentLength (2)
    """
    MaxArrayLength = None
    MaxBytesPerRead = None
    MaxDepth = None
    MaxNameTableCharCount = None
    MaxStringContentLength = None
    value__ = None


class XmlDictionaryString: # skipped bases: <type 'object'>
    """
    Represents an entry stored in a System.Xml.XmlDictionary.

    XmlDictionaryString(dictionary: IXmlDictionary, value: str, key: int)
    """
    def ToString(self):
        """
        ToString(self: XmlDictionaryString) -> str

            Displays a text representation of this object.

            Returns: The string value for this instance of the class.
        """
        ...

    @property
    def Dictionary(self):
        """
        Represents the System.Xml.IXmlDictionary passed to the constructor of this instance of System.Xml.XmlDictionaryString.

        Get: Dictionary(self: XmlDictionaryString) -> IXmlDictionary
        """
        ...

    @property
    def Key(self):
        """
        Gets the integer key for this instance of the class.

        Get: Key(self: XmlDictionaryString) -> int
        """
        ...

    @property
    def Value(self):
        """
        Gets the string value for this instance of the class.

        Get: Value(self: XmlDictionaryString) -> str
        """
        ...


    Empty = None


class XmlDictionaryWriter(XmlWriter): # skipped bases: <type 'IDisposable'>
    """ Represents an abstract class that Windows Communication Foundation (WCF) derives from System.Xml.XmlWriter to do serialization and deserialization. """
    @staticmethod
    def CreateBinaryWriter(stream, dictionary=None, session=None, ownsStream=None):
        """
        CreateBinaryWriter(stream: Stream) -> XmlDictionaryWriter

            Creates an instance of System.Xml.XmlDictionaryWriter that writes WCF binary XML format.

            stream: The stream to write to.

            Returns: An instance of System.Xml.XmlDictionaryWriter.

        CreateBinaryWriter(stream: Stream, dictionary: IXmlDictionary) -> XmlDictionaryWriter

            Creates an instance of System.Xml.XmlDictionaryWriter that writes WCF binary XML format.

            stream: The stream to write to.

            dictionary: The System.Xml.XmlDictionary to use as the shared dictionary.

            Returns: An instance of System.Xml.XmlDictionaryWriter.

        CreateBinaryWriter(stream: Stream, dictionary: IXmlDictionary, session: XmlBinaryWriterSession) -> XmlDictionaryWriter

            Creates an instance of System.Xml.XmlDictionaryWriter that writes WCF binary XML format.

            stream: The stream to write to.

            dictionary: The System.Xml.XmlDictionary to use as the shared dictionary.

            session: The System.Xml.XmlBinaryWriterSession to use.

            Returns: An instance of System.Xml.XmlDictionaryWriter.

        CreateBinaryWriter(stream: Stream, dictionary: IXmlDictionary, session: XmlBinaryWriterSession, ownsStream: bool) -> XmlDictionaryWriter

            Creates an instance of System.Xml.XmlDictionaryWriter that writes WCF binary XML format.

            stream: The stream from which to read.

            dictionary: The System.Xml.XmlDictionary to use as the shared dictionary.

            session: The System.Xml.XmlBinaryWriterSession to use.

            ownsStream: ue to indicate that the stream is closed by the writer when done; otherwise lse.

            Returns: An instance of System.Xml.XmlDictionaryWriter.
        """
        ...

    @staticmethod
    def CreateDictionaryWriter(writer):
        """
        CreateDictionaryWriter(writer: XmlWriter) -> XmlDictionaryWriter

            Creates an instance of System.Xml.XmlDictionaryWriter from an existing System.Xml.XmlWriter.

            writer: An instance of System.Xml.XmlWriter.

            Returns: An instance of System.Xml.XmlDictionaryWriter.
        """
        ...

    @staticmethod
    def CreateMtomWriter(stream, encoding, maxSizeInBytes, startInfo, boundary=None, startUri=None, writeMessageHeaders=None, ownsStream=None):
        """
        CreateMtomWriter(stream: Stream, encoding: Encoding, maxSizeInBytes: int, startInfo: str) -> XmlDictionaryWriter

            Creates an instance of System.Xml.XmlDictionaryWriter that writes XML in the MTOM format.

            stream: The stream to write to.

            encoding: The character encoding of the stream.

            maxSizeInBytes: The maximum number of bytes that are buffered in the writer.

            startInfo: An attribute in the ContentType SOAP header.

            Returns: An instance of System.Xml.XmlDictionaryWriter.

        CreateMtomWriter(stream: Stream, encoding: Encoding, maxSizeInBytes: int, startInfo: str, boundary: str, startUri: str, writeMessageHeaders: bool, ownsStream: bool) -> XmlDictionaryWriter

            Creates an instance of System.Xml.XmlDictionaryWriter that writes XML in the MTOM format.

            stream: The stream to write to.

            encoding: The character encoding of the stream.

            maxSizeInBytes: The maximum number of bytes that are buffered in the writer.

            startInfo: The content-type of the MIME part that contains the Infoset.

            boundary: The MIME boundary in the message.

            startUri: The content-id URI of the MIME part that contains the Infoset.

            writeMessageHeaders: ue to write message headers.

            ownsStream: ue to indicate that the stream is closed by the writer when done; otherwise lse.

            Returns: An instance of System.Xml.XmlDictionaryWriter.
        """
        ...

    @staticmethod
    def CreateTextWriter(stream, encoding=None, ownsStream=None):
        """
        CreateTextWriter(stream: Stream) -> XmlDictionaryWriter

            Creates an instance of System.Xml.XmlDictionaryWriter that writes text XML.

            stream: The stream to write to.

            Returns: An instance of System.Xml.XmlDictionaryWriter.

        CreateTextWriter(stream: Stream, encoding: Encoding) -> XmlDictionaryWriter

            Creates an instance of System.Xml.XmlDictionaryWriter that writes text XML.

            stream: The stream to write to.

            encoding: The character encoding of the output.

            Returns: An instance of System.Xml.XmlDictionaryWriter.

        CreateTextWriter(stream: Stream, encoding: Encoding, ownsStream: bool) -> XmlDictionaryWriter

            Creates an instance of System.Xml.XmlDictionaryWriter that writes text XML.

            stream: The stream to write to.

            encoding: The character encoding of the stream.

            ownsStream: ue to indicate that the stream is closed by the writer when done; otherwise lse.

            Returns: An instance of System.Xml.XmlDictionaryWriter.
        """
        ...

    def EndCanonicalization(self):
        """
        EndCanonicalization(self: XmlDictionaryWriter)

            When implemented by a derived class, it stops the canonicalization started by the matching 

             System.Xml.XmlDictionaryWriter.StartCanonicalization(System.IO.Stream,System.Boolean,System.String[]) call.
        """
        ...

    def StartCanonicalization(self, stream, includeComments, inclusivePrefixes):
        """
        StartCanonicalization(self: XmlDictionaryWriter, stream: Stream, includeComments: bool, inclusivePrefixes: Array[str])

            When implemented by a derived class, it starts the canonicalization.

            stream: The stream to write to.

            includeComments: ue to include comments; otherwise, lse.

            inclusivePrefixes: The prefixes to be included.
        """
        ...

    def WriteArray(self, prefix, localName, namespaceUri, array, offset, count):
        """
        WriteArray(self: XmlDictionaryWriter, prefix: str, localName: str, namespaceUri: str, array: Array[bool], offset: int, count: int)

            Writes nodes from a System.Boolean array.

            prefix: The namespace prefix.

            localName: The local name of the element.

            namespaceUri: The namespace URI of the element.

            array: The array that contains the data.

            offset: The starting index in the array.

            count: The number of values to write from the array.

        WriteArray(self: XmlDictionaryWriter, prefix: str, localName: XmlDictionaryString, namespaceUri: XmlDictionaryString, array: Array[Guid], offset: int, count: int)

            Writes nodes from a System.Guid array.

            prefix: The namespace prefix.

            localName: The local name of the element.

            namespaceUri: The namespace URI of the element.

            array: The array that contains the nodes.

            offset: The starting index in the array.

            count: The number of nodes to get from the array.

        WriteArray(self: XmlDictionaryWriter, prefix: str, localName: str, namespaceUri: str, array: Array[Guid], offset: int, count: int)

            Writes nodes from a System.Guid array.

            prefix: The namespace prefix.

            localName: The local name of the element.

            namespaceUri: The namespace URI of the element.

            array: The array that contains the nodes.

            offset: The starting index in the array.

            count: The number of nodes to get from the array.

        WriteArray(self: XmlDictionaryWriter, prefix: str, localName: XmlDictionaryString, namespaceUri: XmlDictionaryString, array: Array[DateTime], offset: int, count: int)

            Writes nodes from a System.DateTime array.

            prefix: The namespace prefix.

            localName: The local name of the element.

            namespaceUri: The namespace URI of the element.

            array: The array that contains the nodes.

            offset: The starting index in the array.

            count: The number of nodes to get from the array.

        WriteArray(self: XmlDictionaryWriter, prefix: str, localName: str, namespaceUri: str, array: Array[DateTime], offset: int, count: int)

            Writes nodes from a System.DateTime array.

            prefix: The namespace prefix.

            localName: The local name of the element.

            namespaceUri: The namespace URI of the element.

            array: The array that contains the nodes.

            offset: The starting index in the array.

            count: The number of nodes to get from the array.

        WriteArray(self: XmlDictionaryWriter, prefix: str, localName: XmlDictionaryString, namespaceUri: XmlDictionaryString, array: Array[Decimal], offset: int, count: int)

            Writes nodes from a System.Decimal array.

            prefix: The namespace prefix.

            localName: The local name of the element.

            namespaceUri: The namespace URI of the element.

            array: The array that contains the nodes.

            offset: The starting index in the array.

            count: The number of nodes to get from the array.

        WriteArray(self: XmlDictionaryWriter, prefix: str, localName: str, namespaceUri: str, array: Array[Decimal], offset: int, count: int)

            Writes nodes from a System.Decimal array.

            prefix: The namespace prefix.

            localName: The local name of the element.

            namespaceUri: The namespace URI of the element.

            array: The array that contains the nodes.

            offset: The starting index in the array.

            count: The number of nodes to get from the array.

        WriteArray(self: XmlDictionaryWriter, prefix: str, localName: XmlDictionaryString, namespaceUri: XmlDictionaryString, array: Array[float], offset: int, count: int)

            Writes nodes from a System.Double array.

            prefix: The namespace prefix.

            localName: The local name of the element.

            namespaceUri: The namespace URI of the element.

            array: The array that contains the nodes.

            offset: The starting index in the array.

            count: The number of nodes to get from the array.

        WriteArray(self: XmlDictionaryWriter, prefix: str, localName: str, namespaceUri: str, array: Array[float], offset: int, count: int)

            Writes nodes from a System.Double array.

            prefix: The namespace prefix.

            localName: The local name of the element.

            namespaceUri: The namespace URI of the element.

            array: The array that contains the nodes.

            offset: The starting index in the array.

            count: The number of nodes to get from the array.

        WriteArray(self: XmlDictionaryWriter, prefix: str, localName: XmlDictionaryString, namespaceUri: XmlDictionaryString, array: Array[Single], offset: int, count: int)

            Writes nodes from a System.Single array.

            prefix: The namespace prefix.

            localName: The local name of the element.

            namespaceUri: The namespace URI of the element.

            array: The array that contains the nodes.

            offset: The starting index in the array.

            count: The number of nodes to get from the array.

        WriteArray(self: XmlDictionaryWriter, prefix: str, localName: str, namespaceUri: str, array: Array[Single], offset: int, count: int)

            Writes nodes from a System.Single array.

            prefix: The namespace prefix.

            localName: The local name of the element.

            namespaceUri: The namespace URI of the element.

            array: The array that contains the nodes.

            offset: The starting index in the array.

            count: The number of nodes to get from the array.

        WriteArray(self: XmlDictionaryWriter, prefix: str, localName: XmlDictionaryString, namespaceUri: XmlDictionaryString, array: Array[Int64], offset: int, count: int)

            Writes nodes from a System.Int64 array.

            prefix: The namespace prefix.

            localName: The local name of the element.

            namespaceUri: The namespace URI of the element.

            array: The array that contains the nodes.

            offset: The starting index in the array.

            count: The number of nodes to get from the array.

        WriteArray(self: XmlDictionaryWriter, prefix: str, localName: str, namespaceUri: str, array: Array[Int64], offset: int, count: int)

            Writes nodes from a System.Int64 array.

            prefix: The namespace prefix.

            localName: The local name of the element.

            namespaceUri: The namespace URI of the element.

            array: The array that contains the nodes.

            offset: The starting index in the array.

            count: The number of nodes to get from the array.

        WriteArray(self: XmlDictionaryWriter, prefix: str, localName: XmlDictionaryString, namespaceUri: XmlDictionaryString, array: Array[int], offset: int, count: int)

            Writes nodes from a System.Int32 array.

            prefix: The namespace prefix.

            localName: The local name of the element.

            namespaceUri: The namespace URI of the element.

            array: The array that contains the nodes.

            offset: The starting index in the array.

            count: The number of nodes to get from the array.

        WriteArray(self: XmlDictionaryWriter, prefix: str, localName: str, namespaceUri: str, array: Array[int], offset: int, count: int)

            Writes nodes from a System.Int32 array.

            prefix: The namespace prefix.

            localName: The local name of the element.

            namespaceUri: The namespace URI of the element.

            array: The array that contains the nodes.

            offset: The starting index in the array.

            count: The number of nodes to get from the array.

        WriteArray(self: XmlDictionaryWriter, prefix: str, localName: XmlDictionaryString, namespaceUri: XmlDictionaryString, array: Array[Int16], offset: int, count: int)

            Writes nodes from a System.Int16 array.

            prefix: The namespace prefix.

            localName: The local name of the element.

            namespaceUri: The namespace URI of the element.

            array: The array that contains the nodes.

            offset: The starting index in the array.

            count: The number of nodes to get from the array.

        WriteArray(self: XmlDictionaryWriter, prefix: str, localName: str, namespaceUri: str, array: Array[Int16], offset: int, count: int)

            Writes nodes from a System.Int16 array.

            prefix: The namespace prefix.

            localName: The local name of the element.

            namespaceUri: The namespace URI of the element.

            array: The array that contains the nodes.

            offset: The starting index in the array.

            count: The number of nodes to get from the array.

        WriteArray(self: XmlDictionaryWriter, prefix: str, localName: XmlDictionaryString, namespaceUri: XmlDictionaryString, array: Array[bool], offset: int, count: int)

            Writes nodes from a System.Boolean array.

            prefix: The namespace prefix.

            localName: The local name of the element.

            namespaceUri: The namespace URI of the element.

            array: The array that contains the nodes.

            offset: The starting index in the array.

            count: The number of nodes to get from the array.

        WriteArray(self: XmlDictionaryWriter, prefix: str, localName: str, namespaceUri: str, array: Array[TimeSpan], offset: int, count: int)

            Writes nodes from a System.TimeSpan array.

            prefix: The namespace prefix.

            localName: The local name of the element.

            namespaceUri: The namespace URI of the element.

            array: The array that contains the nodes.

            offset: The starting index in the array.

            count: The number of nodes to get from the array.

        WriteArray(self: XmlDictionaryWriter, prefix: str, localName: XmlDictionaryString, namespaceUri: XmlDictionaryString, array: Array[TimeSpan], offset: int, count: int)

            Writes nodes from a System.TimeSpan array.

            prefix: The namespace prefix.

            localName: The local name of the element.

            namespaceUri: The namespace URI of the element.

            array: The array that contains the nodes.

            offset: The starting index in the array.

            count: The number of nodes to get from the array.
        """
        ...

    def WriteTextNode(self, *args): #cannot find CLR method
        """
        WriteTextNode(self: XmlDictionaryWriter, reader: XmlDictionaryReader, isAttribute: bool)

            Writes the text node that an System.Xml.XmlDictionaryReader is currently positioned on.

            reader: The System.Xml.XmlDictionaryReader to get the text value from.

            isAttribute: ue to indicate that the reader is positioned on an attribute value or element content; otherwise, lse.
        """
        ...

    def WriteValueAsync(self, value):
        """
        WriteValueAsync(self: XmlDictionaryWriter, value: IStreamProvider) -> Task

            Asynchronously writes a value from an System.Xml.IStreamProvider.

            value: The System.Xml.IStreamProvider value to write.

            Returns: The task that represents the asynchronous iteValue operation.
        """
        ...

    def WriteXmlAttribute(self, localName, value):
        """
        WriteXmlAttribute(self: XmlDictionaryWriter, localName: str, value: str)

            Writes a standard XML attribute in the current node.

            localName: The local name of the attribute.

            value: The value of the attribute.

        WriteXmlAttribute(self: XmlDictionaryWriter, localName: XmlDictionaryString, value: XmlDictionaryString)

            Writes an XML attribute in the current node.

            localName: The local name of the attribute.

            value: The value of the attribute.
        """
        ...

    def WriteXmlnsAttribute(self, prefix, namespaceUri):
        """
        WriteXmlnsAttribute(self: XmlDictionaryWriter, prefix: str, namespaceUri: str)

            Writes a namespace declaration attribute.

            prefix: The prefix that is bound to the given namespace.

            namespaceUri: The namespace to which the prefix is bound.

        WriteXmlnsAttribute(self: XmlDictionaryWriter, prefix: str, namespaceUri: XmlDictionaryString)

            Writes a namespace declaration attribute.

            prefix: The prefix that is bound to the given namespace.

            namespaceUri: The namespace to which the prefix is bound.
        """
        ...

    @property
    def CanCanonicalize(self):
        """
        This property always returns lse. Its derived classes can override to return ue if they support canonicalization.

        Get: CanCanonicalize(self: XmlDictionaryWriter) -> bool
        """
        ...



