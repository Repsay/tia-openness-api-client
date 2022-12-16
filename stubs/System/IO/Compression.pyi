# encoding: utf-8
# module System.IO.Compression calls itself Compression
# from System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class CompressionLevel(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies values that indicate whether a compression operation emphasizes speed or compression size.

    enum CompressionLevel, values: Fastest (1), NoCompression (2), Optimal (0)
    """

    Fastest = None
    NoCompression = None
    Optimal = None
    value__ = None

class CompressionMode(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies whether to compress or decompress the underlying stream.

    enum CompressionMode, values: Compress (1), Decompress (0)
    """

    Compress = None
    Decompress = None
    value__ = None

class DeflateStream(Stream):  # skipped bases: <type 'IDisposable'>
    """
    Provides methods and properties for compressing and decompressing streams by using the Deflate algorithm.

    DeflateStream(stream: Stream, mode: CompressionMode)

    DeflateStream(stream: Stream, mode: CompressionMode, leaveOpen: bool)

    DeflateStream(stream: Stream, compressionLevel: CompressionLevel)

    DeflateStream(stream: Stream, compressionLevel: CompressionLevel, leaveOpen: bool)
    """

    @staticmethod  # known case of __new__
    def __new__(cls, stream, *__args):
        """
        __new__(cls: type, stream: Stream, mode: CompressionMode)

        __new__(cls: type, stream: Stream, mode: CompressionMode, leaveOpen: bool)

        __new__(cls: type, stream: Stream, compressionLevel: CompressionLevel)

        __new__(cls: type, stream: Stream, compressionLevel: CompressionLevel, leaveOpen: bool)
        """
        ...
    @property
    def BaseStream(self):
        """
        Gets a reference to the underlying stream.

        Get: BaseStream(self: DeflateStream) -> Stream
        """
        ...
    @property
    def CanRead(self):
        """
        Gets a value indicating whether the stream supports reading while decompressing a file.

        Get: CanRead(self: DeflateStream) -> bool
        """
        ...
    @property
    def CanSeek(self):
        """
        Gets a value indicating whether the stream supports seeking.

        Get: CanSeek(self: DeflateStream) -> bool
        """
        ...
    @property
    def CanWrite(self):
        """
        Gets a value indicating whether the stream supports writing.

        Get: CanWrite(self: DeflateStream) -> bool
        """
        ...
    @property
    def Length(self):
        """
        This property is not supported and always throws a System.NotSupportedException.

        Get: Length(self: DeflateStream) -> Int64
        """
        ...
    @property
    def Position(self):
        """
        This property is not supported and always throws a System.NotSupportedException.

        Get: Position(self: DeflateStream) -> Int64

        Set: Position(self: DeflateStream) = value
        """
        ...

class GZipStream(Stream):  # skipped bases: <type 'IDisposable'>
    """
    Provides methods and properties used to compress and decompress streams.

    GZipStream(stream: Stream, mode: CompressionMode)

    GZipStream(stream: Stream, mode: CompressionMode, leaveOpen: bool)

    GZipStream(stream: Stream, compressionLevel: CompressionLevel)

    GZipStream(stream: Stream, compressionLevel: CompressionLevel, leaveOpen: bool)
    """

    @staticmethod  # known case of __new__
    def __new__(cls, stream, *__args):
        """
        __new__(cls: type, stream: Stream, mode: CompressionMode)

        __new__(cls: type, stream: Stream, mode: CompressionMode, leaveOpen: bool)

        __new__(cls: type, stream: Stream, compressionLevel: CompressionLevel)

        __new__(cls: type, stream: Stream, compressionLevel: CompressionLevel, leaveOpen: bool)
        """
        ...
    @property
    def BaseStream(self):
        """
        Gets a reference to the underlying stream.

        Get: BaseStream(self: GZipStream) -> Stream
        """
        ...
    @property
    def CanRead(self):
        """
        Gets a value indicating whether the stream supports reading while decompressing a file.

        Get: CanRead(self: GZipStream) -> bool
        """
        ...
    @property
    def CanSeek(self):
        """
        Gets a value indicating whether the stream supports seeking.

        Get: CanSeek(self: GZipStream) -> bool
        """
        ...
    @property
    def CanWrite(self):
        """
        Gets a value indicating whether the stream supports writing.

        Get: CanWrite(self: GZipStream) -> bool
        """
        ...
    @property
    def Length(self):
        """
        This property is not supported and always throws a System.NotSupportedException.

        Get: Length(self: GZipStream) -> Int64
        """
        ...
    @property
    def Position(self):
        """
        This property is not supported and always throws a System.NotSupportedException.

        Get: Position(self: GZipStream) -> Int64

        Set: Position(self: GZipStream) = value
        """
        ...
