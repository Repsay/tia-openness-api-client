# encoding: utf-8
# module System.IO calls itself IO
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
# no doc
# no imports

# no functions
# classes

from System import Enum, EventArgs, IDisposable, MarshalByRefObject, MulticastDelegate, SystemException
from System.ComponentModel import Component, DescriptionAttribute, ISupportInitialize

from Runtime.Serialization import ISerializable

class BinaryReader(IDisposable):
    """
    Reads primitive data types as binary values in a specific encoding.

    BinaryReader(input: Stream)

    BinaryReader(input: Stream, encoding: Encoding)

    BinaryReader(input: Stream, encoding: Encoding, leaveOpen: bool)
    """

    def Close(self):
        """
        Close(self: BinaryReader)

            Closes the current reader and the underlying stream.
        """
        ...
    def FillBuffer(self, *args):  # cannot find CLR method
        """
        FillBuffer(self: BinaryReader, numBytes: int)

            Fills the internal buffer with the specified number of bytes read from the stream.

            numBytes: The number of bytes to be read.
        """
        ...
    def PeekChar(self):
        """
        PeekChar(self: BinaryReader) -> int

            Returns the next available character and does not advance the byte or character position.

            Returns: The next available character, or -1 if no more characters are available or the stream does not support seeking.
        """
        ...
    def Read(self, buffer=None, index=None, count=None):
        """
        Read(self: BinaryReader) -> int

            Reads characters from the underlying stream and advances the current position of the stream in accordance with the coding used and the specific character being read

             from the stream.

            Returns: The next character from the input stream, or -1 if no characters are currently available.

        Read(self: BinaryReader, buffer: Array[Char], index: int, count: int) -> int

            Reads the specified number of characters from the stream, starting from a specified point in the character array.

            buffer: The buffer to read data into.

            index: The starting point in the buffer at which to begin reading into the buffer.

            count: The number of characters to read.

            Returns: The total number of characters read into the buffer. This might be less than the number of characters requested if that many characters are not currently available, or

             it might be zero if the end of the stream is reached.

        Read(self: BinaryReader, buffer: Array[Byte], index: int, count: int) -> int

            Reads the specified number of bytes from the stream, starting from a specified point in the byte array.

            buffer: The buffer to read data into.

            index: The starting point in the buffer at which to begin reading into the buffer.

            count: The number of bytes to read.

            Returns: The number of bytes read into buffer. This might be less than the number of bytes requested if that many bytes are not available, or it might be zero if the end of the

             stream is reached.
        """
        ...
    def Read7BitEncodedInt(self, *args):  # cannot find CLR method
        """
        Read7BitEncodedInt(self: BinaryReader) -> int

            Reads in a 32-bit integer in compressed format.

            Returns: A 32-bit integer in compressed format.
        """
        ...
    def ReadBoolean(self):
        """
        ReadBoolean(self: BinaryReader) -> bool

            Reads a olean value from the current stream and advances the current position of the stream by one byte.

            Returns: ue if the byte is nonzero; otherwise, lse.
        """
        ...
    def ReadByte(self):
        """
        ReadByte(self: BinaryReader) -> Byte

            Reads the next byte from the current stream and advances the current position of the stream by one byte.

            Returns: The next byte read from the current stream.
        """
        ...
    def ReadBytes(self, count):
        """
        ReadBytes(self: BinaryReader, count: int) -> Array[Byte]

            Reads the specified number of bytes from the current stream into a byte array and advances the current position by that number of bytes.

            count: The number of bytes to read. This value must be 0 or a non-negative number or an exception will occur.

            Returns: A byte array containing data read from the underlying stream. This might be less than the number of bytes requested if the end of the stream is reached.
        """
        ...
    def ReadChar(self):
        """
        ReadChar(self: BinaryReader) -> Char

            Reads the next character from the current stream and advances the current position of the stream in accordance with the coding used and the specific character being

             read from the stream.

            Returns: A character read from the current stream.
        """
        ...
    def ReadChars(self, count):
        """
        ReadChars(self: BinaryReader, count: int) -> Array[Char]

            Reads the specified number of characters from the current stream, returns the data in a character array, and advances the current position in accordance with the

             coding used and the specific character being read from the stream.

            count: The number of characters to read.

            Returns: A character array containing data read from the underlying stream. This might be less than the number of characters requested if the end of the stream is reached.
        """
        ...
    def ReadDecimal(self):
        """
        ReadDecimal(self: BinaryReader) -> Decimal

            Reads a decimal value from the current stream and advances the current position of the stream by sixteen bytes.

            Returns: A decimal value read from the current stream.
        """
        ...
    def ReadDouble(self):
        """
        ReadDouble(self: BinaryReader) -> float

            Reads an 8-byte floating point value from the current stream and advances the current position of the stream by eight bytes.

            Returns: An 8-byte floating point value read from the current stream.
        """
        ...
    def ReadInt16(self):
        """
        ReadInt16(self: BinaryReader) -> Int16

            Reads a 2-byte signed integer from the current stream and advances the current position of the stream by two bytes.

            Returns: A 2-byte signed integer read from the current stream.
        """
        ...
    def ReadInt32(self):
        """
        ReadInt32(self: BinaryReader) -> int

            Reads a 4-byte signed integer from the current stream and advances the current position of the stream by four bytes.

            Returns: A 4-byte signed integer read from the current stream.
        """
        ...
    def ReadInt64(self):
        """
        ReadInt64(self: BinaryReader) -> Int64

            Reads an 8-byte signed integer from the current stream and advances the current position of the stream by eight bytes.

            Returns: An 8-byte signed integer read from the current stream.
        """
        ...
    def ReadSByte(self):
        """
        ReadSByte(self: BinaryReader) -> SByte

            Reads a signed byte from this stream and advances the current position of the stream by one byte.

            Returns: A signed byte read from the current stream.
        """
        ...
    def ReadSingle(self):
        """
        ReadSingle(self: BinaryReader) -> Single

            Reads a 4-byte floating point value from the current stream and advances the current position of the stream by four bytes.

            Returns: A 4-byte floating point value read from the current stream.
        """
        ...
    def ReadString(self):
        """
        ReadString(self: BinaryReader) -> str

            Reads a string from the current stream. The string is prefixed with the length, encoded as an integer seven bits at a time.

            Returns: The string being read.
        """
        ...
    def ReadUInt16(self):
        """
        ReadUInt16(self: BinaryReader) -> UInt16

            Reads a 2-byte unsigned integer from the current stream using little-endian encoding and advances the position of the stream by two bytes.

            Returns: A 2-byte unsigned integer read from this stream.
        """
        ...
    def ReadUInt32(self):
        """
        ReadUInt32(self: BinaryReader) -> UInt32

            Reads a 4-byte unsigned integer from the current stream and advances the position of the stream by four bytes.

            Returns: A 4-byte unsigned integer read from this stream.
        """
        ...
    def ReadUInt64(self):
        """
        ReadUInt64(self: BinaryReader) -> UInt64

            Reads an 8-byte unsigned integer from the current stream and advances the position of the stream by eight bytes.

            Returns: An 8-byte unsigned integer read from this stream.
        """
        ...
    @property
    def BaseStream(self):
        """
        Exposes access to the underlying stream of the System.IO.BinaryReader.

        Get: BaseStream(self: BinaryReader) -> Stream
        """
        ...

class BinaryWriter(IDisposable):
    """
    Writes primitive types in binary to a stream and supports writing strings in a specific encoding.

    BinaryWriter(output: Stream)

    BinaryWriter(output: Stream, encoding: Encoding)

    BinaryWriter(output: Stream, encoding: Encoding, leaveOpen: bool)
    """

    def Close(self):
        """
        Close(self: BinaryWriter)

            Closes the current System.IO.BinaryWriter and the underlying stream.
        """
        ...
    def Flush(self):
        """
        Flush(self: BinaryWriter)

            Clears all buffers for the current writer and causes any buffered data to be written to the underlying device.
        """
        ...
    def Seek(self, offset, origin):
        """
        Seek(self: BinaryWriter, offset: int, origin: SeekOrigin) -> Int64

            Sets the position within the current stream.

            offset: A byte offset relative to origin.

            origin: A field of System.IO.SeekOrigin indicating the reference point from which the new position is to be obtained.

            Returns: The position with the current stream.
        """
        ...
    def Write(self, *__args):
        """
        Write(self: BinaryWriter, value: bool)

            Writes a one-byte olean value to the current stream, with 0 representing lse and 1 representing ue.

            value: The olean value to write (0 or 1).

        Write(self: BinaryWriter, value: UInt64)

            Writes an eight-byte unsigned integer to the current stream and advances the stream position by eight bytes.

            value: The eight-byte unsigned integer to write.

        Write(self: BinaryWriter, value: Int64)

            Writes an eight-byte signed integer to the current stream and advances the stream position by eight bytes.

            value: The eight-byte signed integer to write.

        Write(self: BinaryWriter, value: UInt32)

            Writes a four-byte unsigned integer to the current stream and advances the stream position by four bytes.

            value: The four-byte unsigned integer to write.

        Write(self: BinaryWriter, value: int)

            Writes a four-byte signed integer to the current stream and advances the stream position by four bytes.

            value: The four-byte signed integer to write.

        Write(self: BinaryWriter, value: UInt16)

            Writes a two-byte unsigned integer to the current stream and advances the stream position by two bytes.

            value: The two-byte unsigned integer to write.

        Write(self: BinaryWriter, value: Int16)

            Writes a two-byte signed integer to the current stream and advances the stream position by two bytes.

            value: The two-byte signed integer to write.

        Write(self: BinaryWriter, value: Decimal)

            Writes a decimal value to the current stream and advances the stream position by sixteen bytes.

            value: The decimal value to write.

        Write(self: BinaryWriter, value: float)

            Writes an eight-byte floating-point value to the current stream and advances the stream position by eight bytes.

            value: The eight-byte floating-point value to write.

        Write(self: BinaryWriter, chars: Array[Char], index: int, count: int)

            Writes a section of a character array to the current stream, and advances the current position of the stream in accordance with the coding used and perhaps the

             specific characters being written to the stream.

            chars: A character array containing the data to write.

            index: The starting point in chars from which to begin writing.

            count: The number of characters to write.

        Write(self: BinaryWriter, chars: Array[Char])

            Writes a character array to the current stream and advances the current position of the stream in accordance with the coding used and the specific characters being

             written to the stream.

            chars: A character array containing the data to write.

        Write(self: BinaryWriter, ch: Char)

            Writes a Unicode character to the current stream and advances the current position of the stream in accordance with the coding used and the specific characters being

             written to the stream.

            ch: The non-surrogate, Unicode character to write.

        Write(self: BinaryWriter, buffer: Array[Byte], index: int, count: int)

            Writes a region of a byte array to the current stream.

            buffer: A byte array containing the data to write.

            index: The starting point in buffer at which to begin writing.

            count: The number of bytes to write.

        Write(self: BinaryWriter, buffer: Array[Byte])

            Writes a byte array to the underlying stream.

            buffer: A byte array containing the data to write.

        Write(self: BinaryWriter, value: SByte)

            Writes a signed byte to the current stream and advances the stream position by one byte.

            value: The signed byte to write.

        Write(self: BinaryWriter, value: Byte)

            Writes an unsigned byte to the current stream and advances the stream position by one byte.

            value: The unsigned byte to write.

        Write(self: BinaryWriter, value: Single)

            Writes a four-byte floating-point value to the current stream and advances the stream position by four bytes.

            value: The four-byte floating-point value to write.

        Write(self: BinaryWriter, value: str)

            Writes a length-prefixed string to this stream in the current encoding of the System.IO.BinaryWriter, and advances the current position of the stream in accordance

             with the encoding used and the specific characters being written to the stream.

            value: The value to write.
        """
        ...
    def Write7BitEncodedInt(self, *args):  # cannot find CLR method
        """
        Write7BitEncodedInt(self: BinaryWriter, value: int)

            Writes a 32-bit integer in a compressed format.

            value: The 32-bit integer to be written.
        """
        ...
    @property
    def BaseStream(self):
        """
        Gets the underlying stream of the System.IO.BinaryWriter.

        Get: BaseStream(self: BinaryWriter) -> Stream
        """
        ...
    Null = None
    OutStream = None

class Stream(MarshalByRefObject, IDisposable):
    """Provides a generic view of a sequence of bytes. This is an abstract class.To browse the .NET Framework source code for this type, see the Reference Source."""

    def BeginRead(self, buffer, offset, count, callback, state):
        """
        BeginRead(self: Stream, buffer: Array[Byte], offset: int, count: int, callback: AsyncCallback, state: object) -> IAsyncResult

            Begins an asynchronous read operation. (Consider using System.IO.Stream.ReadAsync(System.Byte[],System.Int32,System.Int32) instead; see the Remarks section.)

            buffer: The buffer to read the data into.

            offset: The byte offset in buffer at which to begin writing data read from the stream.

            count: The maximum number of bytes to read.

            callback: An optional asynchronous callback, to be called when the read is complete.

            state: A user-provided object that distinguishes this particular asynchronous read request from other requests.

            Returns: An System.IAsyncResult that represents the asynchronous read, which could still be pending.
        """
        ...
    def BeginWrite(self, buffer, offset, count, callback, state):
        """
        BeginWrite(self: Stream, buffer: Array[Byte], offset: int, count: int, callback: AsyncCallback, state: object) -> IAsyncResult

            Begins an asynchronous write operation. (Consider using System.IO.Stream.WriteAsync(System.Byte[],System.Int32,System.Int32) instead; see the Remarks section.)

            buffer: The buffer to write data from.

            offset: The byte offset in buffer from which to begin writing.

            count: The maximum number of bytes to write.

            callback: An optional asynchronous callback, to be called when the write is complete.

            state: A user-provided object that distinguishes this particular asynchronous write request from other requests.

            Returns: An syncResult that represents the asynchronous write, which could still be pending.
        """
        ...
    def Close(self):
        """
        Close(self: Stream)

            Closes the current stream and releases any resources (such as sockets and file handles) associated with the current stream. Instead of calling this method, ensure that

             the stream is properly disposed.
        """
        ...
    def CopyTo(self, destination, bufferSize=None):
        """
        CopyTo(self: Stream, destination: Stream)

            Reads the bytes from the current stream and writes them to another stream.

            destination: The stream to which the contents of the current stream will be copied.

        CopyTo(self: Stream, destination: Stream, bufferSize: int)

            Reads the bytes from the current stream and writes them to another stream, using a specified buffer size.

            destination: The stream to which the contents of the current stream will be copied.

            bufferSize: The size of the buffer. This value must be greater than zero. The default size is 81920.
        """
        ...
    def CopyToAsync(self, destination, bufferSize=None, cancellationToken=None):
        """
        CopyToAsync(self: Stream, destination: Stream, bufferSize: int, cancellationToken: CancellationToken) -> Task

            Asynchronously reads the bytes from the current stream and writes them to another stream, using a specified buffer size and cancellation token.

            destination: The stream to which the contents of the current stream will be copied.

            bufferSize: The size, in bytes, of the buffer. This value must be greater than zero. The default size is 81920.

            cancellationToken: The token to monitor for cancellation requests. The default value is System.Threading.CancellationToken.None.

            Returns: A task that represents the asynchronous copy operation.

        CopyToAsync(self: Stream, destination: Stream) -> Task

            Asynchronously reads the bytes from the current stream and writes them to another stream.

            destination: The stream to which the contents of the current stream will be copied.

            Returns: A task that represents the asynchronous copy operation.

        CopyToAsync(self: Stream, destination: Stream, bufferSize: int) -> Task

            Asynchronously reads the bytes from the current stream and writes them to another stream, using a specified buffer size.

            destination: The stream to which the contents of the current stream will be copied.

            bufferSize: The size, in bytes, of the buffer. This value must be greater than zero. The default size is 81920.

            Returns: A task that represents the asynchronous copy operation.
        """
        ...
    def CreateWaitHandle(self, *args):  # cannot find CLR method
        """
        CreateWaitHandle(self: Stream) -> WaitHandle

            Allocates a System.Threading.WaitHandle object.

            Returns: A reference to the allocated itHandle.
        """
        ...
    def EndRead(self, asyncResult):
        """
        EndRead(self: Stream, asyncResult: IAsyncResult) -> int

            Waits for the pending asynchronous read to complete. (Consider using System.IO.Stream.ReadAsync(System.Byte[],System.Int32,System.Int32) instead; see the Remarks

             section.)

            asyncResult: The reference to the pending asynchronous request to finish.

            Returns: The number of bytes read from the stream, between zero (0) and the number of bytes you requested. Streams return zero (0) only at the end of the stream, otherwise,

             they should block until at least one byte is available.
        """
        ...
    def EndWrite(self, asyncResult):
        """
        EndWrite(self: Stream, asyncResult: IAsyncResult)

            Ends an asynchronous write operation. (Consider using System.IO.Stream.WriteAsync(System.Byte[],System.Int32,System.Int32) instead; see the Remarks section.)

            asyncResult: A reference to the outstanding asynchronous I/O request.
        """
        ...
    def Flush(self):
        """
        Flush(self: Stream)

            When overridden in a derived class, clears all buffers for this stream and causes any buffered data to be written to the underlying device.
        """
        ...
    def FlushAsync(self, cancellationToken=None):
        """
        FlushAsync(self: Stream) -> Task

            Asynchronously clears all buffers for this stream and causes any buffered data to be written to the underlying device.

            Returns: A task that represents the asynchronous flush operation.

        FlushAsync(self: Stream, cancellationToken: CancellationToken) -> Task

            Asynchronously clears all buffers for this stream, causes any buffered data to be written to the underlying device, and monitors cancellation requests.

            cancellationToken: The token to monitor for cancellation requests. The default value is System.Threading.CancellationToken.None.

            Returns: A task that represents the asynchronous flush operation.
        """
        ...
    def ObjectInvariant(self, *args):  # cannot find CLR method
        """
        ObjectInvariant(self: Stream)

            Provides support for a System.Diagnostics.Contracts.Contract.
        """
        ...
    def Read(self, buffer, offset, count):
        """
        Read(self: Stream, offset: int, count: int) -> (int, Array[Byte])

            When overridden in a derived class, reads a sequence of bytes from the current stream and advances the position within the stream by the number of bytes read.

            offset: The zero-based byte offset in buffer at which to begin storing the data read from the current stream.

            count: The maximum number of bytes to be read from the current stream.

            Returns: The total number of bytes read into the buffer. This can be less than the number of bytes requested if that many bytes are not currently available, or zero (0) if the

             end of the stream has been reached.
        """
        ...
    def ReadAsync(self, buffer, offset, count, cancellationToken=None):
        """
        ReadAsync(self: Stream, buffer: Array[Byte], offset: int, count: int, cancellationToken: CancellationToken) -> Task[int]

            Asynchronously reads a sequence of bytes from the current stream, advances the position within the stream by the number of bytes read, and monitors cancellation

             requests.

            buffer: The buffer to write the data into.

            offset: The byte offset in buffer at which to begin writing data from the stream.

            count: The maximum number of bytes to read.

            cancellationToken: The token to monitor for cancellation requests. The default value is System.Threading.CancellationToken.None.

            Returns: A task that represents the asynchronous read operation. The value of the TResult parameter contains the total number of bytes read into the buffer. The result value

             can be less than the number of bytes requested if the number of bytes currently available is less than the requested number, or it can be 0 (zero) if the end of the

             stream has been reached.

        ReadAsync(self: Stream, buffer: Array[Byte], offset: int, count: int) -> Task[int]

            Asynchronously reads a sequence of bytes from the current stream and advances the position within the stream by the number of bytes read.

            buffer: The buffer to write the data into.

            offset: The byte offset in buffer at which to begin writing data from the stream.

            count: The maximum number of bytes to read.

            Returns: A task that represents the asynchronous read operation. The value of the TResult parameter contains the total number of bytes read into the buffer. The result value

             can be less than the number of bytes requested if the number of bytes currently available is less than the requested number, or it can be 0 (zero) if the end of the

             stream has been reached.
        """
        ...
    def ReadByte(self):
        """
        ReadByte(self: Stream) -> int

            Reads a byte from the stream and advances the position within the stream by one byte, or returns -1 if at the end of the stream.

            Returns: The unsigned byte cast to an t32, or -1 if at the end of the stream.
        """
        ...
    def Seek(self, offset, origin):
        """
        Seek(self: Stream, offset: Int64, origin: SeekOrigin) -> Int64

            When overridden in a derived class, sets the position within the current stream.

            offset: A byte offset relative to the origin parameter.

            origin: A value of type System.IO.SeekOrigin indicating the reference point used to obtain the new position.

            Returns: The new position within the current stream.
        """
        ...
    def SetLength(self, value):
        """
        SetLength(self: Stream, value: Int64)

            When overridden in a derived class, sets the length of the current stream.

            value: The desired length of the current stream in bytes.
        """
        ...
    @staticmethod
    def Synchronized(stream):
        """
        Synchronized(stream: Stream) -> Stream

            Creates a thread-safe (synchronized) wrapper around the specified System.IO.Stream object.

            stream: The System.IO.Stream object to synchronize.

            Returns: A thread-safe System.IO.Stream object.
        """
        ...
    def Write(self, buffer, offset, count):
        """
        Write(self: Stream, buffer: Array[Byte], offset: int, count: int)

            When overridden in a derived class, writes a sequence of bytes to the current stream and advances the current position within this stream by the number of bytes

             written.

            buffer: An array of bytes. This method copies count bytes from buffer to the current stream.

            offset: The zero-based byte offset in buffer at which to begin copying bytes to the current stream.

            count: The number of bytes to be written to the current stream.
        """
        ...
    def WriteAsync(self, buffer, offset, count, cancellationToken=None):
        """
        WriteAsync(self: Stream, buffer: Array[Byte], offset: int, count: int, cancellationToken: CancellationToken) -> Task

            Asynchronously writes a sequence of bytes to the current stream, advances the current position within this stream by the number of bytes written, and monitors

             cancellation requests.

            buffer: The buffer to write data from.

            offset: The zero-based byte offset in buffer from which to begin copying bytes to the stream.

            count: The maximum number of bytes to write.

            cancellationToken: The token to monitor for cancellation requests. The default value is System.Threading.CancellationToken.None.

            Returns: A task that represents the asynchronous write operation.

        WriteAsync(self: Stream, buffer: Array[Byte], offset: int, count: int) -> Task

            Asynchronously writes a sequence of bytes to the current stream and advances the current position within this stream by the number of bytes written.

            buffer: The buffer to write data from.

            offset: The zero-based byte offset in buffer from which to begin copying bytes to the stream.

            count: The maximum number of bytes to write.

            Returns: A task that represents the asynchronous write operation.
        """
        ...
    def WriteByte(self, value):
        """
        WriteByte(self: Stream, value: Byte)

            Writes a byte to the current position in the stream and advances the position within the stream by one byte.

            value: The byte to write to the stream.
        """
        ...
    @property
    def CanRead(self):
        """
        When overridden in a derived class, gets a value indicating whether the current stream supports reading.

        Get: CanRead(self: Stream) -> bool
        """
        ...
    @property
    def CanSeek(self):
        """
        When overridden in a derived class, gets a value indicating whether the current stream supports seeking.

        Get: CanSeek(self: Stream) -> bool
        """
        ...
    @property
    def CanTimeout(self):
        """
        Gets a value that determines whether the current stream can time out.

        Get: CanTimeout(self: Stream) -> bool
        """
        ...
    @property
    def CanWrite(self):
        """
        When overridden in a derived class, gets a value indicating whether the current stream supports writing.

        Get: CanWrite(self: Stream) -> bool
        """
        ...
    @property
    def Length(self):
        """
        When overridden in a derived class, gets the length in bytes of the stream.

        Get: Length(self: Stream) -> Int64
        """
        ...
    @property
    def Position(self):
        """
        When overridden in a derived class, gets or sets the position within the current stream.

        Get: Position(self: Stream) -> Int64

        Set: Position(self: Stream) = value
        """
        ...
    @property
    def ReadTimeout(self):
        """
        Gets or sets a value, in miliseconds, that determines how long the stream will attempt to read before timing out.

        Get: ReadTimeout(self: Stream) -> int

        Set: ReadTimeout(self: Stream) = value
        """
        ...
    @property
    def WriteTimeout(self):
        """
        Gets or sets a value, in miliseconds, that determines how long the stream will attempt to write before timing out.

        Get: WriteTimeout(self: Stream) -> int

        Set: WriteTimeout(self: Stream) = value
        """
        ...
    Null = None

class BufferedStream(Stream):  # skipped bases: <type 'IDisposable'>
    """
    Adds a buffering layer to read and write operations on another stream. This class cannot be inherited.

    BufferedStream(stream: Stream)

    BufferedStream(stream: Stream, bufferSize: int)
    """

    @staticmethod  # known case of __new__
    def __new__(cls, stream, bufferSize=None):
        """
        __new__(cls: type, stream: Stream)

        __new__(cls: type, stream: Stream, bufferSize: int)
        """
        ...
    @property
    def CanRead(self):
        """
        Gets a value indicating whether the current stream supports reading.

        Get: CanRead(self: BufferedStream) -> bool
        """
        ...
    @property
    def CanSeek(self):
        """
        Gets a value indicating whether the current stream supports seeking.

        Get: CanSeek(self: BufferedStream) -> bool
        """
        ...
    @property
    def CanWrite(self):
        """
        Gets a value indicating whether the current stream supports writing.

        Get: CanWrite(self: BufferedStream) -> bool
        """
        ...
    @property
    def Length(self):
        """
        Gets the stream length in bytes.

        Get: Length(self: BufferedStream) -> Int64
        """
        ...
    @property
    def Position(self):
        """
        Gets the position within the current stream.

        Get: Position(self: BufferedStream) -> Int64

        Set: Position(self: BufferedStream) = value
        """
        ...

class Directory:  # skipped bases: <type 'object'>
    """Exposes static methods for creating, moving, and enumerating through directories and subdirectories. This class cannot be inherited.To browse the .NET Framework source code for this type, see the Reference Source."""

    @staticmethod
    def CreateDirectory(path, directorySecurity=None):
        """
        CreateDirectory(path: str) -> DirectoryInfo

            Creates all directories and subdirectories in the specified path unless they already exist.

            path: The directory to create.

            Returns: An object that represents the directory at the specified path. This object is returned regardless of whether a directory at the specified path already exists.

        CreateDirectory(path: str, directorySecurity: DirectorySecurity) -> DirectoryInfo

            Creates all the directories in the specified path, unless the already exist, applying the specified Windows security.

            path: The directory to create.

            directorySecurity: The access control to apply to the directory.

            Returns: An object that represents the directory at the specified path. This object is returned regardless of whether a directory at the specified path already exists.
        """
        ...
    @staticmethod
    def Delete(path, recursive=None):
        """
        Delete(path: str)

            Deletes an empty directory from a specified path.

            path: The name of the empty directory to remove. This directory must be writable and empty.

        Delete(path: str, recursive: bool)

            Deletes the specified directory and, if indicated, any subdirectories and files in the directory.

            path: The name of the directory to remove.

            recursive: ue to remove directories, subdirectories, and files in path; otherwise, lse.
        """
        ...
    @staticmethod
    def EnumerateDirectories(path, searchPattern=None, searchOption=None):
        """
        EnumerateDirectories(path: str, searchPattern: str) -> IEnumerable[str]

            Returns an enumerable collection of directory names that match a search pattern in a specified path.

            path: The relative or absolute path to the directory to search. This string is not case-sensitive.

            searchPattern: The search string to match against the names of directories in path.  This parameter can contain a combination of valid literal path and wildcard (* and ?) characters

             (see Remarks), but doesn't support regular expressions.

            Returns: An enumerable collection of the full names (including paths) for the directories in the directory specified by path and that match the specified search pattern.

        EnumerateDirectories(path: str, searchPattern: str, searchOption: SearchOption) -> IEnumerable[str]

            Returns an enumerable collection of directory names that match a search pattern in a specified path, and optionally searches subdirectories.

            path: The relative or absolute path to the directory to search. This string is not case-sensitive.

            searchPattern: The search string to match against the names of directories in path.  This parameter can contain a combination of valid literal path and wildcard (* and ?) characters

             (see Remarks), but doesn't support regular expressions.

            searchOption: One of the enumeration values that specifies whether the search operation should include only the current directory or should include all subdirectories.The default

             value is System.IO.SearchOption.TopDirectoryOnly.

            Returns: An enumerable collection of the full names (including paths) for the directories in the directory specified by path and that match the specified search pattern and

             option.

        EnumerateDirectories(path: str) -> IEnumerable[str]

            Returns an enumerable collection of directory names in a specified path.

            path: The relative or absolute path to the directory to search. This string is not case-sensitive.

            Returns: An enumerable collection of the full names (including paths) for the directories in the directory specified by path.
        """
        ...
    @staticmethod
    def EnumerateFiles(path, searchPattern=None, searchOption=None):
        """
        EnumerateFiles(path: str, searchPattern: str) -> IEnumerable[str]

            Returns an enumerable collection of file names that match a search pattern in a specified path.

            path: The relative or absolute path to the directory to search. This string is not case-sensitive.

            searchPattern: The search string to match against the names of files in path.  This parameter can contain a combination of valid literal path and wildcard (* and ?) characters (see

             Remarks), but doesn't support regular expressions.

            Returns: An enumerable collection of the full names (including paths) for the files in the directory specified by path and that match the specified search pattern.

        EnumerateFiles(path: str, searchPattern: str, searchOption: SearchOption) -> IEnumerable[str]

            Returns an enumerable collection of file names that match a search pattern in a specified path, and optionally searches subdirectories.

            path: The relative or absolute path to the directory to search. This string is not case-sensitive.

            searchPattern: The search string to match against the names of files in path.  This parameter can contain a combination of valid literal path and wildcard (* and ?) characters (see

             Remarks), but doesn't support regular expressions.

            searchOption: One of the enumeration values that specifies whether the search operation should include only the current directory or should include all subdirectories.The default

             value is System.IO.SearchOption.TopDirectoryOnly.

            Returns: An enumerable collection of the full names (including paths) for the files in the directory specified by path and that match the specified search pattern and option.

        EnumerateFiles(path: str) -> IEnumerable[str]

            Returns an enumerable collection of file names in a specified path.

            path: The relative or absolute path to the directory to search. This string is not case-sensitive.

            Returns: An enumerable collection of the full names (including paths) for the files in the directory specified by path.
        """
        ...
    @staticmethod
    def EnumerateFileSystemEntries(path, searchPattern=None, searchOption=None):
        """
        EnumerateFileSystemEntries(path: str, searchPattern: str) -> IEnumerable[str]

            Returns an enumerable collection of file names and directory names that  match a search pattern in a specified path.

            path: The relative or absolute path to the directory to search. This string is not case-sensitive.

            searchPattern: The search string to match against the names of file-system entries in path.  This parameter can contain a combination of valid literal path and wildcard (* and ?)

             characters (see Remarks), but doesn't support regular expressions.

            Returns: An enumerable collection of file-system entries in the directory specified by path and that match the specified search pattern.

        EnumerateFileSystemEntries(path: str, searchPattern: str, searchOption: SearchOption) -> IEnumerable[str]

            Returns an enumerable collection of file names and directory names that match a search pattern in a specified path, and optionally searches subdirectories.

            path: The relative or absolute path to the directory to search. This string is not case-sensitive.

            searchPattern: The search string to match against file-system entries in path.  This parameter can contain a combination of valid literal path and wildcard (* and ?) characters (see

             Remarks), but doesn't support regular expressions.

            searchOption: One of the enumeration values  that specifies whether the search operation should include only the current directory or should include all subdirectories.The default

             value is System.IO.SearchOption.TopDirectoryOnly.

            Returns: An enumerable collection of file-system entries in the directory specified by path and that match the specified search pattern and option.

        EnumerateFileSystemEntries(path: str) -> IEnumerable[str]

            Returns an enumerable collection of file names and directory names in a specified path.

            path: The relative or absolute path to the directory to search. This string is not case-sensitive.

            Returns: An enumerable collection of file-system entries in the directory specified by path.
        """
        ...
    @staticmethod
    def Exists(path):
        """
        Exists(path: str) -> bool

            Determines whether the given path refers to an existing directory on disk.

            path: The path to test.

            Returns: ue if path refers to an existing directory; lse if the directory does not exist or an error occurs when trying to determine if the specified directory exists.
        """
        ...
    @staticmethod
    def GetAccessControl(path, includeSections=None):
        """
        GetAccessControl(path: str) -> DirectorySecurity

            Gets a System.Security.AccessControl.DirectorySecurity object that encapsulates the access control list (ACL) entries for a specified directory.

            path: The path to a directory containing a System.Security.AccessControl.DirectorySecurity object that describes the file's access control list (ACL) information.

            Returns: An object that encapsulates the access control rules for the file described by the path parameter.

        GetAccessControl(path: str, includeSections: AccessControlSections) -> DirectorySecurity

            Gets a System.Security.AccessControl.DirectorySecurity object that encapsulates the specified type of access control list (ACL) entries for a specified directory.

            path: The path to a directory containing a System.Security.AccessControl.DirectorySecurity object that describes the file's access control list (ACL) information.

            includeSections: One of the System.Security.AccessControl.AccessControlSections values that specifies the type of access control list (ACL) information to receive.

            Returns: An object that encapsulates the access control rules for the file described by the path parameter.
        """
        ...
    @staticmethod
    def GetCreationTime(path):
        """
        GetCreationTime(path: str) -> DateTime

            Gets the creation date and time of a directory.

            path: The path of the directory.

            Returns: A structure that is set to the creation date and time for the specified directory. This value is expressed in local time.
        """
        ...
    @staticmethod
    def GetCreationTimeUtc(path):
        """
        GetCreationTimeUtc(path: str) -> DateTime

            Gets the creation date and time, in Coordinated Universal Time (UTC) format, of a directory.

            path: The path of the directory.

            Returns: A structure that is set to the creation date and time for the specified directory. This value is expressed in UTC time.
        """
        ...
    @staticmethod
    def GetCurrentDirectory():
        """
        GetCurrentDirectory() -> str

            Gets the current working directory of the application.

            Returns: A string that contains the path of the current working directory, and does not end with a backslash (\\).
        """
        ...
    @staticmethod
    def GetDirectories(path, searchPattern=None, searchOption=None):
        """
        GetDirectories(path: str, searchPattern: str) -> Array[str]

            Returns the names of subdirectories (including their paths) that match the specified search pattern in the specified directory.

            path: The relative or absolute path to the directory to search. This string is not case-sensitive.

            searchPattern: The search string to match against the names of subdirectories in path. This parameter can contain a combination of valid literal and wildcard characters (see

             Remarks), but doesn't support regular expressions.

            Returns: An array of the full names (including paths) of the subdirectories that match the search pattern in the specified directory, or an empty array if no directories are

             found.

        GetDirectories(path: str, searchPattern: str, searchOption: SearchOption) -> Array[str]

            Returns the names of the subdirectories (including their paths) that match the specified search pattern in the specified directory, and optionally searches

             subdirectories.

            path: The relative or absolute path to the directory to search. This string is not case-sensitive.

            searchPattern: The search string to match against the names of subdirectories in path. This parameter can contain a combination of valid literal and wildcard characters (see

             Remarks), but doesn't support regular expressions.

            searchOption: One of the enumeration values that specifies whether the search operation should include all subdirectories or only the current directory.

            Returns: An array of the full names (including paths) of the subdirectories that match the specified criteria, or an empty array if no directories are found.

        GetDirectories(path: str) -> Array[str]

            Returns the names of subdirectories (including their paths) in the specified directory.

            path: The relative or absolute path to the directory to search. This string is not case-sensitive.

            Returns: An array of the full names (including paths) of subdirectories in the specified path, or an empty array if no directories are found.
        """
        ...
    @staticmethod
    def GetDirectoryRoot(path):
        """
        GetDirectoryRoot(path: str) -> str

            Returns the volume information, root information, or both for the specified path.

            path: The path of a file or directory.

            Returns: A string that contains the volume information, root information, or both for the specified path.
        """
        ...
    @staticmethod
    def GetFiles(path, searchPattern=None, searchOption=None):
        """
        GetFiles(path: str, searchPattern: str) -> Array[str]

            Returns the names of files (including their paths) that match the specified search pattern in the specified directory.

            path: The relative or absolute path to the directory to search. This string is not case-sensitive.

            searchPattern: The search string to match against the names of files in path.  This parameter can contain a combination of valid literal path and wildcard (* and ?) characters (see

             Remarks), but doesn't support regular expressions.

            Returns: An array of the full names (including paths) for the files in the specified directory that match the specified search pattern, or an empty array if no files are found.

        GetFiles(path: str, searchPattern: str, searchOption: SearchOption) -> Array[str]

            Returns the names of files (including their paths) that match the specified search pattern in the specified directory, using a value to determine whether to search

             subdirectories.

            path: The relative or absolute path to the directory to search. This string is not case-sensitive.

            searchPattern: The search string to match against the names of files in path.  This parameter can contain a combination of valid literal path and wildcard (* and ?) characters (see

             Remarks), but doesn't support regular expressions.

            searchOption: One of the enumeration values that specifies whether the search operation should include all subdirectories or only the current directory.

            Returns: An array of the full names (including paths) for the files in the specified directory that match the specified search pattern and option, or an empty array if no files

             are found.

        GetFiles(path: str) -> Array[str]

            Returns the names of files (including their paths) in the specified directory.

            path: The relative or absolute path to the directory to search. This string is not case-sensitive.

            Returns: An array of the full names (including paths) for the files in the specified directory, or an empty array if no files are found.
        """
        ...
    @staticmethod
    def GetFileSystemEntries(path, searchPattern=None, searchOption=None):
        """
        GetFileSystemEntries(path: str, searchPattern: str) -> Array[str]

            Returns an array of file names and directory names that that match a search pattern in a specified path.

            path: The relative or absolute path to the directory to search. This string is not case-sensitive.

            searchPattern: The search string to match against the names of file and directories in path.  This parameter can contain a combination of valid literal path and wildcard (* and ?)

             characters (see Remarks), but doesn't support regular expressions.

            Returns: An array of file names and directory names that match the specified search criteria, or an empty array if no files or directories are found.

        GetFileSystemEntries(path: str, searchPattern: str, searchOption: SearchOption) -> Array[str]

            Returns an array of all the file names and directory names that match a search pattern in a specified path, and optionally searches subdirectories.

            path: The relative or absolute path to the directory to search. This string is not case-sensitive.

            searchPattern: The search string to match against the names of files and directories in path.  This parameter can contain a combination of valid literal path and wildcard (* and ?)

             characters (see Remarks), but doesn't support regular expressions.

            searchOption: One of the enumeration values that specifies whether the search operation should include only the current directory or should include all subdirectories.The default

             value is System.IO.SearchOption.TopDirectoryOnly.

            Returns: An array of file the file names and directory names that match the specified search criteria, or an empty array if no files or directories are found.

        GetFileSystemEntries(path: str) -> Array[str]

            Returns the names of all files and subdirectories in a specified path.

            path: The relative or absolute path to the directory to search. This string is not case-sensitive.

            Returns: An array of the names of files and subdirectories in the specified directory, or an empty array if no files or subdirectories are found.
        """
        ...
    @staticmethod
    def GetLastAccessTime(path):
        """
        GetLastAccessTime(path: str) -> DateTime

            Returns the date and time the specified file or directory was last accessed.

            path: The file or directory for which to obtain access date and time information.

            Returns: A structure that is set to the date and time the specified file or directory was last accessed. This value is expressed in local time.
        """
        ...
    @staticmethod
    def GetLastAccessTimeUtc(path):
        """
        GetLastAccessTimeUtc(path: str) -> DateTime

            Returns the date and time, in Coordinated Universal Time (UTC) format, that the specified file or directory was last accessed.

            path: The file or directory for which to obtain access date and time information.

            Returns: A structure that is set to the date and time the specified file or directory was last accessed. This value is expressed in UTC time.
        """
        ...
    @staticmethod
    def GetLastWriteTime(path):
        """
        GetLastWriteTime(path: str) -> DateTime

            Returns the date and time the specified file or directory was last written to.

            path: The file or directory for which to obtain modification date and time information.

            Returns: A structure that is set to the date and time the specified file or directory was last written to. This value is expressed in local time.
        """
        ...
    @staticmethod
    def GetLastWriteTimeUtc(path):
        """
        GetLastWriteTimeUtc(path: str) -> DateTime

            Returns the date and time, in Coordinated Universal Time (UTC) format, that the specified file or directory was last written to.

            path: The file or directory for which to obtain modification date and time information.

            Returns: A structure that is set to the date and time the specified file or directory was last written to. This value is expressed in UTC time.
        """
        ...
    @staticmethod
    def GetLogicalDrives():
        """
        GetLogicalDrives() -> Array[str]

            Retrieves the names of the logical drives on this computer in the form "<drive letter>:\".

            Returns: The logical drives on this computer.
        """
        ...
    @staticmethod
    def GetParent(path):
        """
        GetParent(path: str) -> DirectoryInfo

            Retrieves the parent directory of the specified path, including both absolute and relative paths.

            path: The path for which to retrieve the parent directory.

            Returns: The parent directory, or ll if path is the root directory, including the root of a UNC server or share name.
        """
        ...
    @staticmethod
    def Move(sourceDirName, destDirName):
        """
        Move(sourceDirName: str, destDirName: str)

            Moves a file or a directory and its contents to a new location.

            sourceDirName: The path of the file or directory to move.

            destDirName: The path to the new location for sourceDirName. If sourceDirName is a file, then destDirName must also be a file name.
        """
        ...
    @staticmethod
    def SetAccessControl(path, directorySecurity):
        """
        SetAccessControl(path: str, directorySecurity: DirectorySecurity)

            Applies access control list (ACL) entries described by a System.Security.AccessControl.DirectorySecurity object to the specified directory.

            path: A directory to add or remove access control list (ACL) entries from.

            directorySecurity: A System.Security.AccessControl.DirectorySecurity object that describes an ACL entry to apply to the directory described by the path parameter.
        """
        ...
    @staticmethod
    def SetCreationTime(path, creationTime):
        """
        SetCreationTime(path: str, creationTime: DateTime)

            Sets the creation date and time for the specified file or directory.

            path: The file or directory for which to set the creation date and time information.

            creationTime: The date and time the file or directory was last written to. This value is expressed in local time.
        """
        ...
    @staticmethod
    def SetCreationTimeUtc(path, creationTimeUtc):
        """
        SetCreationTimeUtc(path: str, creationTimeUtc: DateTime)

            Sets the creation date and time, in Coordinated Universal Time (UTC) format, for the specified file or directory.

            path: The file or directory for which to set the creation date and time information.

            creationTimeUtc: The date and time the directory or file was created. This value is expressed in local time.
        """
        ...
    @staticmethod
    def SetCurrentDirectory(path):
        """
        SetCurrentDirectory(path: str)

            Sets the application's current working directory to the specified directory.

            path: The path to which the current working directory is set.
        """
        ...
    @staticmethod
    def SetLastAccessTime(path, lastAccessTime):
        """
        SetLastAccessTime(path: str, lastAccessTime: DateTime)

            Sets the date and time the specified file or directory was last accessed.

            path: The file or directory for which to set the access date and time information.

            lastAccessTime: An object that contains the value to set for the access date and time of path. This value is expressed in local time.
        """
        ...
    @staticmethod
    def SetLastAccessTimeUtc(path, lastAccessTimeUtc):
        """
        SetLastAccessTimeUtc(path: str, lastAccessTimeUtc: DateTime)

            Sets the date and time, in Coordinated Universal Time (UTC) format, that the specified file or directory was last accessed.

            path: The file or directory for which to set the access date and time information.

            lastAccessTimeUtc: An object that  contains the value to set for the access date and time of path. This value is expressed in UTC time.
        """
        ...
    @staticmethod
    def SetLastWriteTime(path, lastWriteTime):
        """
        SetLastWriteTime(path: str, lastWriteTime: DateTime)

            Sets the date and time a directory was last written to.

            path: The path of the directory.

            lastWriteTime: The date and time the directory was last written to. This value is expressed in local time.
        """
        ...
    @staticmethod
    def SetLastWriteTimeUtc(path, lastWriteTimeUtc):
        """
        SetLastWriteTimeUtc(path: str, lastWriteTimeUtc: DateTime)

            Sets the date and time, in Coordinated Universal Time (UTC) format, that a directory was last written to.

            path: The path of the directory.

            lastWriteTimeUtc: The date and time the directory was last written to. This value is expressed in UTC time.
        """
        ...
    __all__ = [
        "CreateDirectory",
        "Delete",
        "EnumerateDirectories",
        "EnumerateFiles",
        "EnumerateFileSystemEntries",
        "Exists",
        "GetAccessControl",
        "GetCreationTime",
        "GetCreationTimeUtc",
        "GetCurrentDirectory",
        "GetDirectories",
        "GetDirectoryRoot",
        "GetFiles",
        "GetFileSystemEntries",
        "GetLastAccessTime",
        "GetLastAccessTimeUtc",
        "GetLastWriteTime",
        "GetLastWriteTimeUtc",
        "GetLogicalDrives",
        "GetParent",
        "Move",
        "SetAccessControl",
        "SetCreationTime",
        "SetCreationTimeUtc",
        "SetCurrentDirectory",
        "SetLastAccessTime",
        "SetLastAccessTimeUtc",
        "SetLastWriteTime",
        "SetLastWriteTimeUtc",
    ]

class FileSystemInfo(MarshalByRefObject, ISerializable):
    """Provides the base class for both System.IO.FileInfo and System.IO.DirectoryInfo objects."""

    def Delete(self):
        """
        Delete(self: FileSystemInfo)

            Deletes a file or directory.
        """
        ...
    def Refresh(self):
        """
        Refresh(self: FileSystemInfo)

            Refreshes the state of the object.
        """
        ...
    @staticmethod  # known case of __new__
    def __new__(cls, *args):  # cannot find CLR constructor
        """
        __new__(cls: type)

        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        ...
    @property
    def Attributes(self):
        """
        Gets or sets the attributes for the current file or directory.

        Get: Attributes(self: FileSystemInfo) -> FileAttributes

        Set: Attributes(self: FileSystemInfo) = value
        """
        ...
    @property
    def CreationTime(self):
        """
        Gets or sets the creation time of the current file or directory.

        Get: CreationTime(self: FileSystemInfo) -> DateTime

        Set: CreationTime(self: FileSystemInfo) = value
        """
        ...
    @property
    def CreationTimeUtc(self):
        """
        Gets or sets the creation time, in coordinated universal time (UTC), of the current file or directory.

        Get: CreationTimeUtc(self: FileSystemInfo) -> DateTime

        Set: CreationTimeUtc(self: FileSystemInfo) = value
        """
        ...
    @property
    def Exists(self):
        """
        Gets a value indicating whether the file or directory exists.

        Get: Exists(self: FileSystemInfo) -> bool
        """
        ...
    @property
    def Extension(self):
        """
        Gets the string representing the extension part of the file.

        Get: Extension(self: FileSystemInfo) -> str
        """
        ...
    @property
    def FullName(self):
        """
        Gets the full path of the directory or file.

        Get: FullName(self: FileSystemInfo) -> str
        """
        ...
    @property
    def LastAccessTime(self):
        """
        Gets or sets the time the current file or directory was last accessed.

        Get: LastAccessTime(self: FileSystemInfo) -> DateTime

        Set: LastAccessTime(self: FileSystemInfo) = value
        """
        ...
    @property
    def LastAccessTimeUtc(self):
        """
        Gets or sets the time, in coordinated universal time (UTC), that the current file or directory was last accessed.

        Get: LastAccessTimeUtc(self: FileSystemInfo) -> DateTime

        Set: LastAccessTimeUtc(self: FileSystemInfo) = value
        """
        ...
    @property
    def LastWriteTime(self):
        """
        Gets or sets the time when the current file or directory was last written to.

        Get: LastWriteTime(self: FileSystemInfo) -> DateTime

        Set: LastWriteTime(self: FileSystemInfo) = value
        """
        ...
    @property
    def LastWriteTimeUtc(self):
        """
        Gets or sets the time, in coordinated universal time (UTC), when the current file or directory was last written to.

        Get: LastWriteTimeUtc(self: FileSystemInfo) -> DateTime

        Set: LastWriteTimeUtc(self: FileSystemInfo) = value
        """
        ...
    @property
    def Name(self):
        """
        For files, gets the name of the file. For directories, gets the name of the last directory in the hierarchy if a hierarchy exists. Otherwise, the me property gets the name of the directory.

        Get: Name(self: FileSystemInfo) -> str
        """
        ...
    FullPath = None
    OriginalPath = None

class DirectoryInfo(FileSystemInfo):  # skipped bases: <type 'ISerializable'>
    """
    Exposes instance methods for creating, moving, and enumerating through directories and subdirectories. This class cannot be inherited.To browse the .NET Framework source code for this type, see the Reference Source.

    DirectoryInfo(path: str)
    """

    @classmethod
    def __new__(cls, path: str) -> DirectoryInfo:
        """create a new instance of DirectoryInfo

        Parameters:
            path (str): The fully qualified name of the new directory, or the relative directory to create.

        Returns:
            DirectoryInfo: A DirectoryInfo object representing the directory specified by path.
        """
        ...
    def Create(self, directorySecurity=None):
        """
        Create(self: DirectoryInfo)

            Creates a directory.

        Create(self: DirectoryInfo, directorySecurity: DirectorySecurity)

            Creates a directory using a System.Security.AccessControl.DirectorySecurity object.

            directorySecurity: The access control to apply to the directory.
        """
        ...
    def CreateSubdirectory(self, path, directorySecurity=None):
        """
        CreateSubdirectory(self: DirectoryInfo, path: str) -> DirectoryInfo

            Creates a subdirectory or subdirectories on the specified path. The specified path can be relative to this instance of the System.IO.DirectoryInfo class.

            path: The specified path. This cannot be a different disk volume or Universal Naming Convention (UNC) name.

            Returns: The last directory specified in path.

        CreateSubdirectory(self: DirectoryInfo, path: str, directorySecurity: DirectorySecurity) -> DirectoryInfo

            Creates a subdirectory or subdirectories on the specified path with the specified security. The specified path can be relative to this instance of the

             System.IO.DirectoryInfo class.

            path: The specified path. This cannot be a different disk volume or Universal Naming Convention (UNC) name.

            directorySecurity: The security to apply.

            Returns: The last directory specified in path.
        """
        ...
    def EnumerateDirectories(self, searchPattern=None, searchOption=None):
        """
        EnumerateDirectories(self: DirectoryInfo) -> IEnumerable[DirectoryInfo]

            Returns an enumerable collection of directory information in the current directory.

            Returns: An enumerable collection of directories in the current directory.

        EnumerateDirectories(self: DirectoryInfo, searchPattern: str) -> IEnumerable[DirectoryInfo]

            Returns an enumerable collection of directory information that matches a specified search pattern.

            searchPattern: The search string to match against the names of directories.  This parameter can contain a combination of valid literal path and wildcard (* and ?) characters (see

             Remarks), but doesn't support regular expressions. The default pattern is "*", which returns all files.

            Returns: An enumerable collection of directories that matches searchPattern.

        EnumerateDirectories(self: DirectoryInfo, searchPattern: str, searchOption: SearchOption) -> IEnumerable[DirectoryInfo]

            Returns an enumerable collection of directory information that matches a specified search pattern and search subdirectory option.

            searchPattern: The search string to match against the names of directories.  This parameter can contain a combination of valid literal path and wildcard (* and ?) characters (see

             Remarks), but doesn't support regular expressions. The default pattern is "*", which returns all files.

            searchOption: One of the enumeration values that specifies whether the search operation should include only the current directory or all subdirectories. The default value is

             System.IO.SearchOption.TopDirectoryOnly.

            Returns: An enumerable collection of directories that matches searchPattern and searchOption.
        """
        ...
    def EnumerateFiles(self, searchPattern=None, searchOption=None):
        """
        EnumerateFiles(self: DirectoryInfo) -> IEnumerable[FileInfo]

            Returns an enumerable collection of file information in the current directory.

            Returns: An enumerable collection of the files in the current directory.

        EnumerateFiles(self: DirectoryInfo, searchPattern: str) -> IEnumerable[FileInfo]

            Returns an enumerable collection of file information that matches a search pattern.

            searchPattern: The search string to match against the names of files.  This parameter can contain a combination of valid literal path and wildcard (* and ?) characters (see Remarks),

             but doesn't support regular expressions. The default pattern is "*", which returns all files.

            Returns: An enumerable collection of files that matches searchPattern.

        EnumerateFiles(self: DirectoryInfo, searchPattern: str, searchOption: SearchOption) -> IEnumerable[FileInfo]

            Returns an enumerable collection of file information that matches a specified search pattern and search subdirectory option.

            searchPattern: The search string to match against the names of files.  This parameter can contain a combination of valid literal path and wildcard (* and ?) characters (see Remarks),

             but doesn't support regular expressions. The default pattern is "*", which returns all files.

            searchOption: One of the enumeration values that specifies whether the search operation should include only the current directory or all subdirectories. The default value is

             System.IO.SearchOption.TopDirectoryOnly.

            Returns: An enumerable collection of files that matches searchPattern and searchOption.
        """
        ...
    def EnumerateFileSystemInfos(self, searchPattern=None, searchOption=None):
        """
        EnumerateFileSystemInfos(self: DirectoryInfo) -> IEnumerable[FileSystemInfo]

            Returns an enumerable collection of file system information in the current directory.

            Returns: An enumerable collection of file system information in the current directory.

        EnumerateFileSystemInfos(self: DirectoryInfo, searchPattern: str) -> IEnumerable[FileSystemInfo]

            Returns an enumerable collection of file system information that matches a specified search pattern.

            searchPattern: The search string to match against the names of directories.  This parameter can contain a combination of valid literal path and wildcard (* and ?) characters (see

             Remarks), but doesn't support regular expressions. The default pattern is "*", which returns all files.

            Returns: An enumerable collection of file system information objects that matches searchPattern.

        EnumerateFileSystemInfos(self: DirectoryInfo, searchPattern: str, searchOption: SearchOption) -> IEnumerable[FileSystemInfo]

            Returns an enumerable collection of file system information that matches a specified search pattern and search subdirectory option.

            searchPattern: The search string to match against the names of directories.  This parameter can contain a combination of valid literal path and wildcard (* and ?) characters (see

             Remarks), but doesn't support regular expressions. The default pattern is "*", which returns all files.

            searchOption: One of the enumeration values that specifies whether the search operation should include only the current directory or all subdirectories. The default value is

             System.IO.SearchOption.TopDirectoryOnly.

            Returns: An enumerable collection of file system information objects that matches searchPattern and searchOption.
        """
        ...
    def GetAccessControl(self, includeSections=None):
        """
        GetAccessControl(self: DirectoryInfo) -> DirectorySecurity

            Gets a System.Security.AccessControl.DirectorySecurity object that encapsulates the access control list (ACL) entries for the directory described by the current

             System.IO.DirectoryInfo object.

            Returns: A System.Security.AccessControl.DirectorySecurity object that encapsulates the access control rules for the directory.

        GetAccessControl(self: DirectoryInfo, includeSections: AccessControlSections) -> DirectorySecurity

            Gets a System.Security.AccessControl.DirectorySecurity object that encapsulates the specified type of access control list (ACL) entries for the directory described by

             the current System.IO.DirectoryInfo object.

            includeSections: One of the System.Security.AccessControl.AccessControlSections values that specifies the type of access control list (ACL) information to receive.

            Returns: A System.Security.AccessControl.DirectorySecurity object that encapsulates the access control rules for the file described by the path parameter.ExceptionsException

             typeCondition

                          System.SystemException

                        The directory could not be found or modified.

             System.UnauthorizedAccessException

                        The current process does not have access to open the directory.

                          System.IO.IOException

                   An I/O error occurred while opening the directory.

                          System.PlatformNotSupportedException

                        The current operating system is not

             Microsoft Windows 2000 or later.

                          System.UnauthorizedAccessException

                        The directory is read-only.-or- This operation is not supported

             on the current platform.-or- The caller does not have the required permission.
        """
        ...
    def GetDirectories(self, searchPattern=None, searchOption=None):
        """
        GetDirectories(self: DirectoryInfo) -> Array[DirectoryInfo]

            Returns the subdirectories of the current directory.

            Returns: An array of System.IO.DirectoryInfo objects.

        GetDirectories(self: DirectoryInfo, searchPattern: str) -> Array[DirectoryInfo]

            Returns an array of directories in the current System.IO.DirectoryInfo matching the given search criteria.

            searchPattern: The search string to match against the names of directories.  This parameter can contain a combination of valid literal path and wildcard (* and ?) characters (see

             Remarks), but doesn't support regular expressions. The default pattern is "*", which returns all files.

            Returns: An array of type rectoryInfo matching searchPattern.

        GetDirectories(self: DirectoryInfo, searchPattern: str, searchOption: SearchOption) -> Array[DirectoryInfo]

            Returns an array of directories in the current System.IO.DirectoryInfo matching the given search criteria and using a value to determine whether to search

             subdirectories.

            searchPattern: The search string to match against the names of directories.  This parameter can contain a combination of valid literal path and wildcard (* and ?) characters (see

             Remarks), but doesn't support regular expressions. The default pattern is "*", which returns all files.

            searchOption: One of the enumeration values that specifies whether the search operation should include only the current directory or all subdirectories.

            Returns: An array of type rectoryInfo matching searchPattern.
        """
        ...
    def GetFiles(self, searchPattern=None, searchOption=None):
        """
        GetFiles(self: DirectoryInfo, searchPattern: str) -> Array[FileInfo]

            Returns a file list from the current directory matching the given search pattern.

            searchPattern: The search string to match against the names of files.  This parameter can contain a combination of valid literal path and wildcard (* and ?) characters (see Remarks),

             but doesn't support regular expressions. The default pattern is "*", which returns all files.

            Returns: An array of type System.IO.FileInfo.

        GetFiles(self: DirectoryInfo, searchPattern: str, searchOption: SearchOption) -> Array[FileInfo]

            Returns a file list from the current directory matching the given search pattern and using a value to determine whether to search subdirectories.

            searchPattern: The search string to match against the names of files.  This parameter can contain a combination of valid literal path and wildcard (* and ?) characters (see Remarks),

             but doesn't support regular expressions. The default pattern is "*", which returns all files.

            searchOption: One of the enumeration values that specifies whether the search operation should include only the current directory or all subdirectories.

            Returns: An array of type System.IO.FileInfo.

        GetFiles(self: DirectoryInfo) -> Array[FileInfo]

            Returns a file list from the current directory.

            Returns: An array of type System.IO.FileInfo.
        """
        ...
    def GetFileSystemInfos(self, searchPattern=None, searchOption=None):
        """
        GetFileSystemInfos(self: DirectoryInfo, searchPattern: str) -> Array[FileSystemInfo]

            Retrieves an array of strongly typed System.IO.FileSystemInfo objects representing the files and subdirectories that match the specified search criteria.

            searchPattern: The search string to match against the names of directories and files.  This parameter can contain a combination of valid literal path and wildcard (* and ?)

             characters (see Remarks), but doesn't support regular expressions. The default pattern is "*", which returns all files.

            Returns: An array of strongly typed leSystemInfo objects matching the search criteria.

        GetFileSystemInfos(self: DirectoryInfo, searchPattern: str, searchOption: SearchOption) -> Array[FileSystemInfo]

            Retrieves an array of System.IO.FileSystemInfo objects that represent the files and subdirectories matching the specified search criteria.

            searchPattern: The search string to match against the names of directories and filesa.  This parameter can contain a combination of valid literal path and wildcard (* and ?)

             characters (see Remarks), but doesn't support regular expressions. The default pattern is "*", which returns all files.

            searchOption: One of the enumeration values that specifies whether the search operation should include only the current directory or all subdirectories. The default value is

             System.IO.SearchOption.TopDirectoryOnly.

            Returns: An array of file system entries that match the search criteria.

        GetFileSystemInfos(self: DirectoryInfo) -> Array[FileSystemInfo]

            Returns an array of strongly typed System.IO.FileSystemInfo entries representing all the files and subdirectories in a directory.

            Returns: An array of strongly typed System.IO.FileSystemInfo entries.
        """
        ...
    def MoveTo(self, destDirName):
        """
        MoveTo(self: DirectoryInfo, destDirName: str)

            Moves a System.IO.DirectoryInfo instance and its contents to a new path.

            destDirName: The name and path to which to move this directory. The destination cannot be another disk volume or a directory with the identical name. It can be an existing

             directory to which you want to add this directory as a subdirectory.
        """
        ...
    def SetAccessControl(self, directorySecurity):
        """
        SetAccessControl(self: DirectoryInfo, directorySecurity: DirectorySecurity)

            Applies access control list (ACL) entries described by a System.Security.AccessControl.DirectorySecurity object to the directory described by the current

             System.IO.DirectoryInfo object.

            directorySecurity: An object that describes an ACL entry to apply to the directory described by the path parameter.
        """
        ...
    def ToString(self):
        """
        ToString(self: DirectoryInfo) -> str

            Returns the original path that was passed by the user.

            Returns: Returns the original path that was passed by the user.
        """
        ...
    def __str__(self, *args): ...
    @property
    def Exists(self):
        """
        Gets a value indicating whether the directory exists.

        Get: Exists(self: DirectoryInfo) -> bool
        """
        ...
    @property
    def FullName(self):
        """
        Gets the full path of the directory.

        Get: FullName(self: DirectoryInfo) -> str
        """
        ...
    @property
    def Name(self):
        """
        Gets the name of this System.IO.DirectoryInfo instance.

        Get: Name(self: DirectoryInfo) -> str
        """
        ...
    @property
    def Parent(self):
        """
        Gets the parent directory of a specified subdirectory.

        Get: Parent(self: DirectoryInfo) -> DirectoryInfo
        """
        ...
    @property
    def Root(self):
        """
        Gets the root portion of the directory.

        Get: Root(self: DirectoryInfo) -> DirectoryInfo
        """
        ...
    FullPath = None
    OriginalPath = None

class IOException(SystemException):  # skipped bases: <type '_Exception'>, <type 'ISerializable'>
    """
    The exception that is thrown when an I/O error occurs.

    IOException()

    IOException(message: str)

    IOException(message: str, hresult: int)

    IOException(message: str, innerException: Exception)
    """

    SerializeObjectState = None

class DirectoryNotFoundException(IOException):  # skipped bases: <type '_Exception'>, <type 'ISerializable'>
    """
    The exception that is thrown when part of a file or directory cannot be found.

    DirectoryNotFoundException()

    DirectoryNotFoundException(message: str)

    DirectoryNotFoundException(message: str, innerException: Exception)
    """

    SerializeObjectState = None

class DriveInfo(ISerializable):
    """
    Provides access to information on a drive.

    DriveInfo(driveName: str)
    """

    @staticmethod
    def GetDrives():
        """
        GetDrives() -> Array[DriveInfo]

            Retrieves the drive names of all logical drives on a computer.

            Returns: An array of type System.IO.DriveInfo that represents the logical drives on a computer.
        """
        ...
    def ToString(self):
        """
        ToString(self: DriveInfo) -> str

            Returns a drive name as a string.

            Returns: The name of the drive.
        """
        ...
    @property
    def AvailableFreeSpace(self):
        """
        Indicates the amount of available free space on a drive, in bytes.

        Get: AvailableFreeSpace(self: DriveInfo) -> Int64
        """
        ...
    @property
    def DriveFormat(self):
        """
        Gets the name of the file system, such as NTFS or FAT32.

        Get: DriveFormat(self: DriveInfo) -> str
        """
        ...
    @property
    def DriveType(self):
        """
        Gets the drive type, such as CD-ROM, removable, network, or fixed.

        Get: DriveType(self: DriveInfo) -> DriveType
        """
        ...
    @property
    def IsReady(self):
        """
        Gets a value that indicates whether a drive is ready.

        Get: IsReady(self: DriveInfo) -> bool
        """
        ...
    @property
    def Name(self):
        """
        Gets the name of a drive, such as C:\\.

        Get: Name(self: DriveInfo) -> str
        """
        ...
    @property
    def RootDirectory(self):
        """
        Gets the root directory of a drive.

        Get: RootDirectory(self: DriveInfo) -> DirectoryInfo
        """
        ...
    @property
    def TotalFreeSpace(self):
        """
        Gets the total amount of free space available on a drive, in bytes.

        Get: TotalFreeSpace(self: DriveInfo) -> Int64
        """
        ...
    @property
    def TotalSize(self):
        """
        Gets the total size of storage space on a drive, in bytes.

        Get: TotalSize(self: DriveInfo) -> Int64
        """
        ...
    @property
    def VolumeLabel(self):
        """
        Gets or sets the volume label of a drive.

        Get: VolumeLabel(self: DriveInfo) -> str

        Set: VolumeLabel(self: DriveInfo) = value
        """
        ...

class DriveNotFoundException(IOException):  # skipped bases: <type '_Exception'>, <type 'ISerializable'>
    """
    The exception that is thrown when trying to access a drive or share that is not available.

    DriveNotFoundException()

    DriveNotFoundException(message: str)

    DriveNotFoundException(message: str, innerException: Exception)
    """

    SerializeObjectState = None

class DriveType(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Defines constants for drive types, including CDRom, Fixed, Network, NoRootDirectory, Ram, Removable, and Unknown.

    enum DriveType, values: CDRom (5), Fixed (3), Network (4), NoRootDirectory (1), Ram (6), Removable (2), Unknown (0)
    """

    CDRom = None
    Fixed = None
    Network = None
    NoRootDirectory = None
    Ram = None
    Removable = None
    Unknown = None
    value__ = None

class EndOfStreamException(IOException):  # skipped bases: <type '_Exception'>, <type 'ISerializable'>
    """
    The exception that is thrown when reading is attempted past the end of a stream.

    EndOfStreamException()

    EndOfStreamException(message: str)

    EndOfStreamException(message: str, innerException: Exception)
    """

    SerializeObjectState = None

class ErrorEventArgs(EventArgs):
    """
    Provides data for the System.IO.FileSystemWatcher.Error event.

    ErrorEventArgs(exception: Exception)
    """

    def GetException(self):
        """
        GetException(self: ErrorEventArgs) -> Exception

            Gets the System.Exception that represents the error that occurred.

            Returns: An System.Exception that represents the error that occurred.
        """
        ...
    @staticmethod  # known case of __new__
    def __new__(cls, exception):
        """__new__(cls: type, exception: Exception)"""
        ...

class ErrorEventHandler(MulticastDelegate):  # skipped bases: <type 'ICloneable'>, <type 'ISerializable'>
    """
    Represents the method that will handle the System.IO.FileSystemWatcher.Error event of a System.IO.FileSystemWatcher object.

    ErrorEventHandler(object: object, method: IntPtr)
    """

    def BeginInvoke(self, sender, e, callback, object):
        """BeginInvoke(self: ErrorEventHandler, sender: object, e: ErrorEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult"""
        ...
    def EndInvoke(self, result):
        """EndInvoke(self: ErrorEventHandler, result: IAsyncResult)"""
        ...
    def Invoke(self, sender, e):
        """Invoke(self: ErrorEventHandler, sender: object, e: ErrorEventArgs)"""
        ...

class File:  # skipped bases: <type 'object'>
    """Provides static methods for the creation, copying, deletion, moving, and opening of a single file, and aids in the creation of System.IO.FileStream objects.To browse the .NET Framework source code for this type, see the Reference Source."""

    @staticmethod
    def AppendAllLines(path, contents, encoding=None):
        """AppendAllLines(path: str, contents: IEnumerable[str])AppendAllLines(path: str, contents: IEnumerable[str], encoding: Encoding)"""
        ...
    @staticmethod
    def AppendAllText(path, contents, encoding=None):
        """
        AppendAllText(path: str, contents: str)

            Opens a file, appends the specified string to the file, and then closes the file. If the file does not exist, this method creates a file, writes the specified string

             to the file, then closes the file.

            path: The file to append the specified string to.

            contents: The string to append to the file.

        AppendAllText(path: str, contents: str, encoding: Encoding)

            Appends the specified string to the file, creating the file if it does not already exist.

            path: The file to append the specified string to.

            contents: The string to append to the file.

            encoding: The character encoding to use.
        """
        ...
    @staticmethod
    def AppendText(path):
        """
        AppendText(path: str) -> StreamWriter

            Creates a System.IO.StreamWriter that appends UTF-8 encoded text to an existing file, or to a new file if the specified file does not exist.

            path: The path to the file to append to.

            Returns: A stream writer that appends UTF-8 encoded text to the specified file or to a new file.
        """
        ...
    @staticmethod
    def Copy(sourceFileName, destFileName, overwrite=None):
        """
        Copy(sourceFileName: str, destFileName: str)

            Copies an existing file to a new file. Overwriting a file of the same name is not allowed.

            sourceFileName: The file to copy.

            destFileName: The name of the destination file. This cannot be a directory or an existing file.

        Copy(sourceFileName: str, destFileName: str, overwrite: bool)

            Copies an existing file to a new file. Overwriting a file of the same name is allowed.

            sourceFileName: The file to copy.

            destFileName: The name of the destination file. This cannot be a directory.

            overwrite: ue if the destination file can be overwritten; otherwise, lse.
        """
        ...
    @staticmethod
    def Create(path, bufferSize=None, options=None, fileSecurity=None):
        """
        Create(path: str) -> FileStream

            Creates or overwrites a file in the specified path.

            path: The path and name of the file to create.

            Returns: A System.IO.FileStream that provides read/write access to the file specified in path.

        Create(path: str, bufferSize: int) -> FileStream

            Creates or overwrites the specified file.

            path: The name of the file.

            bufferSize: The number of bytes buffered for reads and writes to the file.

            Returns: A System.IO.FileStream with the specified buffer size that provides read/write access to the file specified in path.

        Create(path: str, bufferSize: int, options: FileOptions) -> FileStream

            Creates or overwrites the specified file, specifying a buffer size and a System.IO.FileOptions value that describes how to create or overwrite the file.

            path: The name of the file.

            bufferSize: The number of bytes buffered for reads and writes to the file.

            options: One of the System.IO.FileOptions values that describes how to create or overwrite the file.

            Returns: A new file with the specified buffer size.

        Create(path: str, bufferSize: int, options: FileOptions, fileSecurity: FileSecurity) -> FileStream

            Creates or overwrites the specified file with the specified buffer size, file options, and file security.

            path: The name of the file.

            bufferSize: The number of bytes buffered for reads and writes to the file.

            options: One of the System.IO.FileOptions values that describes how to create or overwrite the file.

            fileSecurity: One of the System.Security.AccessControl.FileSecurity values that determines the access control and audit security for the file.

            Returns: A new file with the specified buffer size, file options, and file security.
        """
        ...
    @staticmethod
    def CreateText(path):
        """
        CreateText(path: str) -> StreamWriter

            Creates or opens a file for writing UTF-8 encoded text.

            path: The file to be opened for writing.

            Returns: A System.IO.StreamWriter that writes to the specified file using UTF-8 encoding.
        """
        ...
    @staticmethod
    def Decrypt(path):
        """
        Decrypt(path: str)

            Decrypts a file that was encrypted by the current account using the System.IO.File.Encrypt(System.String) method.

            path: A path that describes a file to decrypt.
        """
        ...
    @staticmethod
    def Delete(path):
        """
        Delete(path: str)

            Deletes the specified file.

            path: The name of the file to be deleted. Wildcard characters are not supported.
        """
        ...
    @staticmethod
    def Encrypt(path):
        """
        Encrypt(path: str)

            Encrypts a file so that only the account used to encrypt the file can decrypt it.

            path: A path that describes a file to encrypt.
        """
        ...
    @staticmethod
    def Exists(path):
        """
        Exists(path: str) -> bool

            Determines whether the specified file exists.

            path: The file to check.

            Returns: ue if the caller has the required permissions and path contains the name of an existing file; otherwise, lse. This method also returns lse if path is ll, an invalid

             path, or a zero-length string. If the caller does not have sufficient permissions to read the specified file, no exception is thrown and the method returns lse

             regardless of the existence of path.
        """
        ...
    @staticmethod
    def GetAccessControl(path, includeSections=None):
        """
        GetAccessControl(path: str) -> FileSecurity

            Gets a System.Security.AccessControl.FileSecurity object that encapsulates the access control list (ACL) entries for a specified file.

            path: The path to a file containing a System.Security.AccessControl.FileSecurity object that describes the file's access control list (ACL) information.

            Returns: A System.Security.AccessControl.FileSecurity object that encapsulates the access control rules for the file described by the path parameter.

        GetAccessControl(path: str, includeSections: AccessControlSections) -> FileSecurity

            Gets a System.Security.AccessControl.FileSecurity object that encapsulates the specified type of access control list (ACL) entries for a particular file.

            path: The path to a file containing a System.Security.AccessControl.FileSecurity object that describes the file's access control list (ACL) information.

            includeSections: One of the System.Security.AccessControl.AccessControlSections values that specifies the type of access control list (ACL) information to receive.

            Returns: A System.Security.AccessControl.FileSecurity object that encapsulates the access control rules for the file described by the path parameter.
        """
        ...
    @staticmethod
    def GetAttributes(path):
        """
        GetAttributes(path: str) -> FileAttributes

            Gets the System.IO.FileAttributes of the file on the path.

            path: The path to the file.

            Returns: The System.IO.FileAttributes of the file on the path.
        """
        ...
    @staticmethod
    def GetCreationTime(path):
        """
        GetCreationTime(path: str) -> DateTime

            Returns the creation date and time of the specified file or directory.

            path: The file or directory for which to obtain creation date and time information.

            Returns: A System.DateTime structure set to the creation date and time for the specified file or directory. This value is expressed in local time.
        """
        ...
    @staticmethod
    def GetCreationTimeUtc(path):
        """
        GetCreationTimeUtc(path: str) -> DateTime

            Returns the creation date and time, in coordinated universal time (UTC), of the specified file or directory.

            path: The file or directory for which to obtain creation date and time information.

            Returns: A System.DateTime structure set to the creation date and time for the specified file or directory. This value is expressed in UTC time.
        """
        ...
    @staticmethod
    def GetLastAccessTime(path):
        """
        GetLastAccessTime(path: str) -> DateTime

            Returns the date and time the specified file or directory was last accessed.

            path: The file or directory for which to obtain access date and time information.

            Returns: A System.DateTime structure set to the date and time that the specified file or directory was last accessed. This value is expressed in local time.
        """
        ...
    @staticmethod
    def GetLastAccessTimeUtc(path):
        """
        GetLastAccessTimeUtc(path: str) -> DateTime

            Returns the date and time, in coordinated universal time (UTC), that the specified file or directory was last accessed.

            path: The file or directory for which to obtain access date and time information.

            Returns: A System.DateTime structure set to the date and time that the specified file or directory was last accessed. This value is expressed in UTC time.
        """
        ...
    @staticmethod
    def GetLastWriteTime(path):
        """
        GetLastWriteTime(path: str) -> DateTime

            Returns the date and time the specified file or directory was last written to.

            path: The file or directory for which to obtain write date and time information.

            Returns: A System.DateTime structure set to the date and time that the specified file or directory was last written to. This value is expressed in local time.
        """
        ...
    @staticmethod
    def GetLastWriteTimeUtc(path):
        """
        GetLastWriteTimeUtc(path: str) -> DateTime

            Returns the date and time, in coordinated universal time (UTC), that the specified file or directory was last written to.

            path: The file or directory for which to obtain write date and time information.

            Returns: A System.DateTime structure set to the date and time that the specified file or directory was last written to. This value is expressed in UTC time.
        """
        ...
    @staticmethod
    def Move(sourceFileName, destFileName):
        """
        Move(sourceFileName: str, destFileName: str)

            Moves a specified file to a new location, providing the option to specify a new file name.

            sourceFileName: The name of the file to move. Can include a relative or absolute path.

            destFileName: The new path and name for the file.
        """
        ...
    @staticmethod
    def Open(path, mode, access=None, share=None):
        """
        Open(path: str, mode: FileMode) -> FileStream

            Opens a System.IO.FileStream on the specified path with read/write access.

            path: The file to open.

            mode: A System.IO.FileMode value that specifies whether a file is created if one does not exist, and determines whether the contents of existing files are retained or

             overwritten.

            Returns: A System.IO.FileStream opened in the specified mode and path, with read/write access and not shared.

        Open(path: str, mode: FileMode, access: FileAccess) -> FileStream

            Opens a System.IO.FileStream on the specified path, with the specified mode and access.

            path: The file to open.

            mode: A System.IO.FileMode value that specifies whether a file is created if one does not exist, and determines whether the contents of existing files are retained or

             overwritten.

            access: A System.IO.FileAccess value that specifies the operations that can be performed on the file.

            Returns: An unshared System.IO.FileStream that provides access to the specified file, with the specified mode and access.

        Open(path: str, mode: FileMode, access: FileAccess, share: FileShare) -> FileStream

            Opens a System.IO.FileStream on the specified path, having the specified mode with read, write, or read/write access and the specified sharing option.

            path: The file to open.

            mode: A System.IO.FileMode value that specifies whether a file is created if one does not exist, and determines whether the contents of existing files are retained or

             overwritten.

            access: A System.IO.FileAccess value that specifies the operations that can be performed on the file.

            share: A System.IO.FileShare value specifying the type of access other threads have to the file.

            Returns: A System.IO.FileStream on the specified path, having the specified mode with read, write, or read/write access and the specified sharing option.
        """
        ...
    @staticmethod
    def OpenRead(path):
        """
        OpenRead(path: str) -> FileStream

            Opens an existing file for reading.

            path: The file to be opened for reading.

            Returns: A read-only System.IO.FileStream on the specified path.
        """
        ...
    @staticmethod
    def OpenText(path):
        """
        OpenText(path: str) -> StreamReader

            Opens an existing UTF-8 encoded text file for reading.

            path: The file to be opened for reading.

            Returns: A System.IO.StreamReader on the specified path.
        """
        ...
    @staticmethod
    def OpenWrite(path):
        """
        OpenWrite(path: str) -> FileStream

            Opens an existing file or creates a new file for writing.

            path: The file to be opened for writing.

            Returns: An unshared System.IO.FileStream object on the specified path with System.IO.FileAccess.Write access.
        """
        ...
    @staticmethod
    def ReadAllBytes(path):
        """
        ReadAllBytes(path: str) -> Array[Byte]

            Opens a binary file, reads the contents of the file into a byte array, and then closes the file.

            path: The file to open for reading.

            Returns: A byte array containing the contents of the file.
        """
        ...
    @staticmethod
    def ReadAllLines(path, encoding=None):
        """
        ReadAllLines(path: str) -> Array[str]

            Opens a text file, reads all lines of the file, and then closes the file.

            path: The file to open for reading.

            Returns: A string array containing all lines of the file.

        ReadAllLines(path: str, encoding: Encoding) -> Array[str]

            Opens a file, reads all lines of the file with the specified encoding, and then closes the file.

            path: The file to open for reading.

            encoding: The encoding applied to the contents of the file.

            Returns: A string array containing all lines of the file.
        """
        ...
    @staticmethod
    def ReadAllText(path, encoding=None):
        """
        ReadAllText(path: str) -> str

            Opens a text file, reads all lines of the file, and then closes the file.

            path: The file to open for reading.

            Returns: A string containing all lines of the file.

        ReadAllText(path: str, encoding: Encoding) -> str

            Opens a file, reads all lines of the file with the specified encoding, and then closes the file.

            path: The file to open for reading.

            encoding: The encoding applied to the contents of the file.

            Returns: A string containing all lines of the file.
        """
        ...
    @staticmethod
    def ReadLines(path, encoding=None):
        """
        ReadLines(path: str) -> IEnumerable[str]

            Reads the lines of a file.

            path: The file to read.

            Returns: All the lines of the file, or the lines that are the result of a query.

        ReadLines(path: str, encoding: Encoding) -> IEnumerable[str]

            Read the lines of a file that has a specified encoding.

            path: The file to read.

            encoding: The encoding that is applied to the contents of the file.

            Returns: All the lines of the file, or the lines that are the result of a query.
        """
        ...
    @staticmethod
    def Replace(sourceFileName, destinationFileName, destinationBackupFileName, ignoreMetadataErrors=None):
        """
        Replace(sourceFileName: str, destinationFileName: str, destinationBackupFileName: str)

            Replaces the contents of a specified file with the contents of another file, deleting the original file, and creating a backup of the replaced file.

            sourceFileName: The name of a file that replaces the file specified by destinationFileName.

            destinationFileName: The name of the file being replaced.

            destinationBackupFileName: The name of the backup file.

        Replace(sourceFileName: str, destinationFileName: str, destinationBackupFileName: str, ignoreMetadataErrors: bool)

            Replaces the contents of a specified file with the contents of another file, deleting the original file, and creating a backup of the replaced file and optionally

             ignores merge errors.

            sourceFileName: The name of a file that replaces the file specified by destinationFileName.

            destinationFileName: The name of the file being replaced.

            destinationBackupFileName: The name of the backup file.

            ignoreMetadataErrors: ue to ignore merge errors (such as attributes and access control lists (ACLs)) from the replaced file to the replacement file; otherwise, lse.
        """
        ...
    @staticmethod
    def SetAccessControl(path, fileSecurity):
        """
        SetAccessControl(path: str, fileSecurity: FileSecurity)

            Applies access control list (ACL) entries described by a System.Security.AccessControl.FileSecurity object to the specified file.

            path: A file to add or remove access control list (ACL) entries from.

            fileSecurity: A System.Security.AccessControl.FileSecurity object that describes an ACL entry to apply to the file described by the path parameter.
        """
        ...
    @staticmethod
    def SetAttributes(path, fileAttributes):
        """
        SetAttributes(path: str, fileAttributes: FileAttributes)

            Sets the specified System.IO.FileAttributes of the file on the specified path.

            path: The path to the file.

            fileAttributes: A bitwise combination of the enumeration values.
        """
        ...
    @staticmethod
    def SetCreationTime(path, creationTime):
        """
        SetCreationTime(path: str, creationTime: DateTime)

            Sets the date and time the file was created.

            path: The file for which to set the creation date and time information.

            creationTime: A System.DateTime containing the value to set for the creation date and time of path. This value is expressed in local time.
        """
        ...
    @staticmethod
    def SetCreationTimeUtc(path, creationTimeUtc):
        """
        SetCreationTimeUtc(path: str, creationTimeUtc: DateTime)

            Sets the date and time, in coordinated universal time (UTC), that the file was created.

            path: The file for which to set the creation date and time information.

            creationTimeUtc: A System.DateTime containing the value to set for the creation date and time of path. This value is expressed in UTC time.
        """
        ...
    @staticmethod
    def SetLastAccessTime(path, lastAccessTime):
        """
        SetLastAccessTime(path: str, lastAccessTime: DateTime)

            Sets the date and time the specified file was last accessed.

            path: The file for which to set the access date and time information.

            lastAccessTime: A System.DateTime containing the value to set for the last access date and time of path. This value is expressed in local time.
        """
        ...
    @staticmethod
    def SetLastAccessTimeUtc(path, lastAccessTimeUtc):
        """
        SetLastAccessTimeUtc(path: str, lastAccessTimeUtc: DateTime)

            Sets the date and time, in coordinated universal time (UTC), that the specified file was last accessed.

            path: The file for which to set the access date and time information.

            lastAccessTimeUtc: A System.DateTime containing the value to set for the last access date and time of path. This value is expressed in UTC time.
        """
        ...
    @staticmethod
    def SetLastWriteTime(path, lastWriteTime):
        """
        SetLastWriteTime(path: str, lastWriteTime: DateTime)

            Sets the date and time that the specified file was last written to.

            path: The file for which to set the date and time information.

            lastWriteTime: A System.DateTime containing the value to set for the last write date and time of path. This value is expressed in local time.
        """
        ...
    @staticmethod
    def SetLastWriteTimeUtc(path, lastWriteTimeUtc):
        """
        SetLastWriteTimeUtc(path: str, lastWriteTimeUtc: DateTime)

            Sets the date and time, in coordinated universal time (UTC), that the specified file was last written to.

            path: The file for which to set the date and time information.

            lastWriteTimeUtc: A System.DateTime containing the value to set for the last write date and time of path. This value is expressed in UTC time.
        """
        ...
    @staticmethod
    def WriteAllBytes(path, bytes):
        """
        WriteAllBytes(path: str, bytes: Array[Byte])

            Creates a new file, writes the specified byte array to the file, and then closes the file. If the target file already exists, it is overwritten.

            path: The file to write to.

            bytes: The bytes to write to the file.
        """
        ...
    @staticmethod
    def WriteAllLines(path, contents, encoding=None):
        """
        WriteAllLines(path: str, contents: Array[str])

            Creates a new file, write the specified string array to the file, and then closes the file.

            path: The file to write to.

            contents: The string array to write to the file.

        WriteAllLines(path: str, contents: Array[str], encoding: Encoding)

            Creates a new file, writes the specified string array to the file by using the specified encoding, and then closes the file.

            path: The file to write to.

            contents: The string array to write to the file.

            encoding: An System.Text.Encoding object that represents the character encoding applied to the string array.

        WriteAllLines(path: str, contents: IEnumerable[str])WriteAllLines(path: str, contents: IEnumerable[str], encoding: Encoding)
        """
        ...
    @staticmethod
    def WriteAllText(path, contents, encoding=None):
        """
        WriteAllText(path: str, contents: str)

            Creates a new file, writes the specified string to the file, and then closes the file. If the target file already exists, it is overwritten.

            path: The file to write to.

            contents: The string to write to the file.

        WriteAllText(path: str, contents: str, encoding: Encoding)

            Creates a new file, writes the specified string to the file using the specified encoding, and then closes the file. If the target file already exists, it is

             overwritten.

            path: The file to write to.

            contents: The string to write to the file.

            encoding: The encoding to apply to the string.
        """
        ...
    __all__ = [
        "AppendAllLines",
        "AppendAllText",
        "AppendText",
        "Copy",
        "Create",
        "CreateText",
        "Decrypt",
        "Delete",
        "Encrypt",
        "Exists",
        "GetAccessControl",
        "GetAttributes",
        "GetCreationTime",
        "GetCreationTimeUtc",
        "GetLastAccessTime",
        "GetLastAccessTimeUtc",
        "GetLastWriteTime",
        "GetLastWriteTimeUtc",
        "Move",
        "Open",
        "OpenRead",
        "OpenText",
        "OpenWrite",
        "ReadAllBytes",
        "ReadAllLines",
        "ReadAllText",
        "ReadLines",
        "Replace",
        "SetAccessControl",
        "SetAttributes",
        "SetCreationTime",
        "SetCreationTimeUtc",
        "SetLastAccessTime",
        "SetLastAccessTimeUtc",
        "SetLastWriteTime",
        "SetLastWriteTimeUtc",
        "WriteAllBytes",
        "WriteAllLines",
        "WriteAllText",
    ]

class FileAccess(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Defines constants for read, write, or read/write access to a file.

    enum (flags) FileAccess, values: Read (1), ReadWrite (3), Write (2)
    """

    Read = None
    ReadWrite = None
    value__ = None
    Write = None

class FileAttributes(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Provides attributes for files and directories.

    enum (flags) FileAttributes, values: Archive (32), Compressed (2048), Device (64), Directory (16), Encrypted (16384), Hidden (2), IntegrityStream (32768), Normal (128), NoScrubData (131072), NotContentIndexed (8192), Offline (4096), ReadOnly (1), ReparsePoint (1024), SparseFile (512), System (4), Temporary (256)
    """

    Archive = None
    Compressed = None
    Device = None
    Directory = None
    Encrypted = None
    Hidden = None
    IntegrityStream = None
    Normal = None
    NoScrubData = None
    NotContentIndexed = None
    Offline = None
    ReadOnly = None
    ReparsePoint = None
    SparseFile = None
    System = None
    Temporary = None
    value__ = None

class FileInfo(FileSystemInfo):  # skipped bases: <type 'ISerializable'>
    """
    Provides properties and instance methods for the creation, copying, deletion, moving, and opening of files, and aids in the creation of System.IO.FileStream objects. This class cannot be inherited.To browse the .NET Framework source code for this type, see the Reference Source.

    FileInfo(fileName: str)
    """

    @classmethod
    def __new__(cls, fileName: str) -> FileInfo:
        """create a new instance for the creation, copying, deletion, moving, and opening of files, and aids in the creation of System.IO.FileStream objects. This class cannot be inherited.To browse the .NET Framework source code for this type, see the Reference Source.

        Parameters:
            fileName (str): The fully qualified name of the new file, or the relative file name.
        """
    def AppendText(self):
        """
        AppendText(self: FileInfo) -> StreamWriter

            Creates a System.IO.StreamWriter that appends text to the file represented by this instance of the System.IO.FileInfo.

            Returns: A new reamWriter.
        """
        ...
    def CopyTo(self, destFileName, overwrite=None):
        """
        CopyTo(self: FileInfo, destFileName: str) -> FileInfo

            Copies an existing file to a new file, disallowing the overwriting of an existing file.

            destFileName: The name of the new file to copy to.

            Returns: A new file with a fully qualified path.

        CopyTo(self: FileInfo, destFileName: str, overwrite: bool) -> FileInfo

            Copies an existing file to a new file, allowing the overwriting of an existing file.

            destFileName: The name of the new file to copy to.

            overwrite: ue to allow an existing file to be overwritten; otherwise, lse.

            Returns: A new file, or an overwrite of an existing file if overwrite is ue. If the file exists and overwrite is lse, an System.IO.IOException is thrown.
        """
        ...
    def Create(self):
        """
        Create(self: FileInfo) -> FileStream

            Creates a file.

            Returns: A new file.
        """
        ...
    def CreateText(self):
        """
        CreateText(self: FileInfo) -> StreamWriter

            Creates a System.IO.StreamWriter that writes a new text file.

            Returns: A new reamWriter.
        """
        ...
    def Decrypt(self):
        """
        Decrypt(self: FileInfo)

            Decrypts a file that was encrypted by the current account using the System.IO.FileInfo.Encrypt method.
        """
        ...
    def Encrypt(self):
        """
        Encrypt(self: FileInfo)

            Encrypts a file so that only the account used to encrypt the file can decrypt it.
        """
        ...
    def GetAccessControl(self, includeSections=None):
        """
        GetAccessControl(self: FileInfo) -> FileSecurity

            Gets a System.Security.AccessControl.FileSecurity object that encapsulates the access control list (ACL) entries for the file described by the current

             System.IO.FileInfo object.

            Returns: A System.Security.AccessControl.FileSecurity object that encapsulates the access control rules for the current file.

        GetAccessControl(self: FileInfo, includeSections: AccessControlSections) -> FileSecurity

            Gets a System.Security.AccessControl.FileSecurity object that encapsulates the specified type of access control list (ACL) entries for the file described by the

             current System.IO.FileInfo object.

            includeSections: One of the System.Security.AccessControl.AccessControlSections values that specifies which group of access control entries to retrieve.

            Returns: A System.Security.AccessControl.FileSecurity object that encapsulates the access control rules for the current file.
        """
        ...
    def MoveTo(self, destFileName):
        """
        MoveTo(self: FileInfo, destFileName: str)

            Moves a specified file to a new location, providing the option to specify a new file name.

            destFileName: The path to move the file to, which can specify a different file name.
        """
        ...
    def Open(self, mode, access=None, share=None):
        """
        Open(self: FileInfo, mode: FileMode) -> FileStream

            Opens a file in the specified mode.

            mode: A System.IO.FileMode constant specifying the mode (for example, en or pend) in which to open the file.

            Returns: A file opened in the specified mode, with read/write access and unshared.

        Open(self: FileInfo, mode: FileMode, access: FileAccess) -> FileStream

            Opens a file in the specified mode with read, write, or read/write access.

            mode: A System.IO.FileMode constant specifying the mode (for example, en or pend) in which to open the file.

            access: A System.IO.FileAccess constant specifying whether to open the file with ad, ite, or adWrite file access.

            Returns: A System.IO.FileStream object opened in the specified mode and access, and unshared.

        Open(self: FileInfo, mode: FileMode, access: FileAccess, share: FileShare) -> FileStream

            Opens a file in the specified mode with read, write, or read/write access and the specified sharing option.

            mode: A System.IO.FileMode constant specifying the mode (for example, en or pend) in which to open the file.

            access: A System.IO.FileAccess constant specifying whether to open the file with ad, ite, or adWrite file access.

            share: A System.IO.FileShare constant specifying the type of access other leStream objects have to this file.

            Returns: A System.IO.FileStream object opened with the specified mode, access, and sharing options.
        """
        ...
    def OpenRead(self):
        """
        OpenRead(self: FileInfo) -> FileStream

            Creates a read-only System.IO.FileStream.

            Returns: A new read-only System.IO.FileStream object.
        """
        ...
    def OpenText(self):
        """
        OpenText(self: FileInfo) -> StreamReader

            Creates a System.IO.StreamReader with UTF8 encoding that reads from an existing text file.

            Returns: A new reamReader with UTF8 encoding.
        """
        ...
    def OpenWrite(self):
        """
        OpenWrite(self: FileInfo) -> FileStream

            Creates a write-only System.IO.FileStream.

            Returns: A write-only unshared System.IO.FileStream object for a new or existing file.
        """
        ...
    def Replace(self, destinationFileName, destinationBackupFileName, ignoreMetadataErrors=None):
        """
        Replace(self: FileInfo, destinationFileName: str, destinationBackupFileName: str) -> FileInfo

            Replaces the contents of a specified file with the file described by the current System.IO.FileInfo object, deleting the original file, and creating a backup of the

             replaced file.

            destinationFileName: The name of a file to replace with the current file.

            destinationBackupFileName: The name of a file with which to create a backup of the file described by the destFileName parameter.

            Returns: A System.IO.FileInfo object that encapsulates information about the file described by the destFileName parameter.

        Replace(self: FileInfo, destinationFileName: str, destinationBackupFileName: str, ignoreMetadataErrors: bool) -> FileInfo

            Replaces the contents of a specified file with the file described by the current System.IO.FileInfo object, deleting the original file, and creating a backup of the

             replaced file.  Also specifies whether to ignore merge errors.

            destinationFileName: The name of a file to replace with the current file.

            destinationBackupFileName: The name of a file with which to create a backup of the file described by the destFileName parameter.

            ignoreMetadataErrors: ue to ignore merge errors (such as attributes and ACLs) from the replaced file to the replacement file; otherwise lse.

            Returns: A System.IO.FileInfo object that encapsulates information about the file described by the destFileName parameter.
        """
        ...
    def SetAccessControl(self, fileSecurity):
        """
        SetAccessControl(self: FileInfo, fileSecurity: FileSecurity)

            Applies access control list (ACL) entries described by a System.Security.AccessControl.FileSecurity object to the file described by the current System.IO.FileInfo

             object.

            fileSecurity: A System.Security.AccessControl.FileSecurity object that describes an access control list (ACL) entry to apply to the current file.
        """
        ...
    def ToString(self):
        """
        ToString(self: FileInfo) -> str

            Returns the path as a string.

            Returns: A string representing the path.
        """
        ...
    def __str__(self, *args): ...
    @property
    def Directory(self):
        """
        Gets an instance of the parent directory.

        Get: Directory(self: FileInfo) -> DirectoryInfo
        """
        ...
    @property
    def DirectoryName(self):
        """
        Gets a string representing the directory's full path.

        Get: DirectoryName(self: FileInfo) -> str
        """
        ...
    @property
    def Exists(self):
        """
        Gets a value indicating whether a file exists.

        Get: Exists(self: FileInfo) -> bool
        """
        ...
    @property
    def IsReadOnly(self):
        """
        Gets or sets a value that determines if the current file is read only.

        Get: IsReadOnly(self: FileInfo) -> bool

        Set: IsReadOnly(self: FileInfo) = value
        """
        ...
    @property
    def Length(self):
        """
        Gets the size, in bytes, of the current file.

        Get: Length(self: FileInfo) -> Int64
        """
        ...
    @property
    def Name(self) -> str:
        """Gets the name of the file."""
        ...
    FullPath = None
    OriginalPath = None

class FileLoadException(IOException):  # skipped bases: <type '_Exception'>, <type 'ISerializable'>
    """
    The exception that is thrown when a managed assembly is found but cannot be loaded.

    FileLoadException()

    FileLoadException(message: str)

    FileLoadException(message: str, inner: Exception)

    FileLoadException(message: str, fileName: str)

    FileLoadException(message: str, fileName: str, inner: Exception)
    """

    def GetObjectData(self, info, context):
        """
        GetObjectData(self: FileLoadException, info: SerializationInfo, context: StreamingContext)

            Sets the System.Runtime.Serialization.SerializationInfo with the file name and additional exception information.

            info: The System.Runtime.Serialization.SerializationInfo that holds the serialized object data about the exception being thrown.

            context: The System.Runtime.Serialization.StreamingContext that contains contextual information about the source or destination.
        """
        ...
    def ToString(self):
        """
        ToString(self: FileLoadException) -> str

            Returns the fully qualified name of the current exception, and possibly the error message, the name of the inner exception, and the stack trace.

            Returns: A string containing the fully qualified name of this exception, and possibly the error message, the name of the inner exception, and the stack trace, depending on

             which System.IO.FileLoadException constructor is used.
        """
        ...
    @property
    def FileName(self):
        """
        Gets the name of the file that causes this exception.

        Get: FileName(self: FileLoadException) -> str
        """
        ...
    @property
    def FusionLog(self):
        """
        Gets the log file that describes why an assembly load failed.

        Get: FusionLog(self: FileLoadException) -> str
        """
        ...
    @property
    def Message(self):
        """
        Gets the error message and the name of the file that caused this exception.

        Get: Message(self: FileLoadException) -> str
        """
        ...
    SerializeObjectState = None

class FileMode(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies how the operating system should open a file.

    enum FileMode, values: Append (6), Create (2), CreateNew (1), Open (3), OpenOrCreate (4), Truncate (5)
    """

    Append = None
    Create = None
    CreateNew = None
    Open = None
    OpenOrCreate = None
    Truncate = None
    value__ = None

class FileNotFoundException(IOException):  # skipped bases: <type '_Exception'>, <type 'ISerializable'>
    """
    The exception that is thrown when an attempt to access a file that does not exist on disk fails.

    FileNotFoundException()

    FileNotFoundException(message: str)

    FileNotFoundException(message: str, innerException: Exception)

    FileNotFoundException(message: str, fileName: str)

    FileNotFoundException(message: str, fileName: str, innerException: Exception)
    """

    def GetObjectData(self, info, context):
        """
        GetObjectData(self: FileNotFoundException, info: SerializationInfo, context: StreamingContext)

            Sets the System.Runtime.Serialization.SerializationInfo object with the file name and additional exception information.

            info: The object that holds the serialized object data about the exception being thrown.

            context: The object that contains contextual information about the source or destination.
        """
        ...
    def ToString(self):
        """
        ToString(self: FileNotFoundException) -> str

            Returns the fully qualified name of this exception and possibly the error message, the name of the inner exception, and the stack trace.

            Returns: The fully qualified name of this exception and possibly the error message, the name of the inner exception, and the stack trace.
        """
        ...
    @property
    def FileName(self):
        """
        Gets the name of the file that cannot be found.

        Get: FileName(self: FileNotFoundException) -> str
        """
        ...
    @property
    def FusionLog(self):
        """
        Gets the log file that describes why loading of an assembly failed.

        Get: FusionLog(self: FileNotFoundException) -> str
        """
        ...
    @property
    def Message(self):
        """
        Gets the error message that explains the reason for the exception.

        Get: Message(self: FileNotFoundException) -> str
        """
        ...
    SerializeObjectState = None

class FileOptions(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Represents advanced options for creating a System.IO.FileStream object.

    enum (flags) FileOptions, values: Asynchronous (1073741824), DeleteOnClose (67108864), Encrypted (16384), None (0), RandomAccess (268435456), SequentialScan (134217728), WriteThrough (-2147483648)
    """

    Asynchronous = None
    DeleteOnClose = None
    Encrypted = None

    RandomAccess = None
    SequentialScan = None
    value__ = None
    WriteThrough = None

class FileShare(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Contains constants for controlling the kind of access other System.IO.FileStream objects can have to the same file.

    enum (flags) FileShare, values: Delete (4), Inheritable (16), None (0), Read (1), ReadWrite (3), Write (2)
    """

    Delete = None
    Inheritable = None

    Read = None
    ReadWrite = None
    value__ = None
    Write = None

class FileStream(Stream):  # skipped bases: <type 'IDisposable'>
    """
    Provides a System.IO.Stream for a file, supporting both synchronous and asynchronous read and write operations.To browse the .NET Framework source code for this type, see the Reference Source.

    FileStream(path: str, mode: FileMode)

    FileStream(path: str, mode: FileMode, access: FileAccess)

    FileStream(path: str, mode: FileMode, access: FileAccess, share: FileShare)

    FileStream(path: str, mode: FileMode, access: FileAccess, share: FileShare, bufferSize: int)

    FileStream(path: str, mode: FileMode, access: FileAccess, share: FileShare, bufferSize: int, options: FileOptions)

    FileStream(path: str, mode: FileMode, access: FileAccess, share: FileShare, bufferSize: int, useAsync: bool)

    FileStream(path: str, mode: FileMode, rights: FileSystemRights, share: FileShare, bufferSize: int, options: FileOptions, fileSecurity: FileSecurity)

    FileStream(path: str, mode: FileMode, rights: FileSystemRights, share: FileShare, bufferSize: int, options: FileOptions)

    FileStream(handle: IntPtr, access: FileAccess)

    FileStream(handle: IntPtr, access: FileAccess, ownsHandle: bool)

    FileStream(handle: IntPtr, access: FileAccess, ownsHandle: bool, bufferSize: int)

    FileStream(handle: IntPtr, access: FileAccess, ownsHandle: bool, bufferSize: int, isAsync: bool)

    FileStream(handle: SafeFileHandle, access: FileAccess)

    FileStream(handle: SafeFileHandle, access: FileAccess, bufferSize: int)

    FileStream(handle: SafeFileHandle, access: FileAccess, bufferSize: int, isAsync: bool)
    """

    def GetAccessControl(self):
        """
        GetAccessControl(self: FileStream) -> FileSecurity

            Gets a System.Security.AccessControl.FileSecurity object that encapsulates the access control list (ACL) entries for the file described by the current

             System.IO.FileStream object.

            Returns: An object that encapsulates the access control settings for the file described by the current System.IO.FileStream object.
        """
        ...
    def Lock(self, position, length):
        """
        Lock(self: FileStream, position: Int64, length: Int64)

            Prevents other processes from reading from or writing to the System.IO.FileStream.

            position: The beginning of the range to lock. The value of this parameter must be equal to or greater than zero (0).

            length: The range to be locked.
        """
        ...
    def SetAccessControl(self, fileSecurity):
        """
        SetAccessControl(self: FileStream, fileSecurity: FileSecurity)

            Applies access control list (ACL) entries described by a System.Security.AccessControl.FileSecurity object to the file described by the current System.IO.FileStream

             object.

            fileSecurity: An object that describes an ACL entry to apply to the current file.
        """
        ...
    def Unlock(self, position, length):
        """
        Unlock(self: FileStream, position: Int64, length: Int64)

            Allows access by other processes to all or part of a file that was previously locked.

            position: The beginning of the range to unlock.

            length: The range to be unlocked.
        """
        ...
    @staticmethod  # known case of __new__
    def __new__(cls, *__args):
        """
        __new__(cls: type, path: str, mode: FileMode)

        __new__(cls: type, path: str, mode: FileMode, access: FileAccess)

        __new__(cls: type, path: str, mode: FileMode, access: FileAccess, share: FileShare)

        __new__(cls: type, path: str, mode: FileMode, access: FileAccess, share: FileShare, bufferSize: int)

        __new__(cls: type, path: str, mode: FileMode, access: FileAccess, share: FileShare, bufferSize: int, options: FileOptions)

        __new__(cls: type, path: str, mode: FileMode, access: FileAccess, share: FileShare, bufferSize: int, useAsync: bool)

        __new__(cls: type, path: str, mode: FileMode, rights: FileSystemRights, share: FileShare, bufferSize: int, options: FileOptions, fileSecurity: FileSecurity)

        __new__(cls: type, path: str, mode: FileMode, rights: FileSystemRights, share: FileShare, bufferSize: int, options: FileOptions)

        __new__(cls: type, handle: IntPtr, access: FileAccess)

        __new__(cls: type, handle: IntPtr, access: FileAccess, ownsHandle: bool)

        __new__(cls: type, handle: IntPtr, access: FileAccess, ownsHandle: bool, bufferSize: int)

        __new__(cls: type, handle: IntPtr, access: FileAccess, ownsHandle: bool, bufferSize: int, isAsync: bool)

        __new__(cls: type, handle: SafeFileHandle, access: FileAccess)

        __new__(cls: type, handle: SafeFileHandle, access: FileAccess, bufferSize: int)

        __new__(cls: type, handle: SafeFileHandle, access: FileAccess, bufferSize: int, isAsync: bool)
        """
        ...
    @property
    def CanRead(self):
        """
        Gets a value indicating whether the current stream supports reading.

        Get: CanRead(self: FileStream) -> bool
        """
        ...
    @property
    def CanSeek(self):
        """
        Gets a value indicating whether the current stream supports seeking.

        Get: CanSeek(self: FileStream) -> bool
        """
        ...
    @property
    def CanWrite(self):
        """
        Gets a value indicating whether the current stream supports writing.

        Get: CanWrite(self: FileStream) -> bool
        """
        ...
    @property
    def Handle(self):
        """
        Gets the operating system file handle for the file that the current leStream object encapsulates.

        Get: Handle(self: FileStream) -> IntPtr
        """
        ...
    @property
    def IsAsync(self):
        """
        Gets a value indicating whether the leStream was opened asynchronously or synchronously.

        Get: IsAsync(self: FileStream) -> bool
        """
        ...
    @property
    def Length(self):
        """
        Gets the length in bytes of the stream.

        Get: Length(self: FileStream) -> Int64
        """
        ...
    @property
    def Name(self):
        """
        Gets the name of the leStream that was passed to the constructor.

        Get: Name(self: FileStream) -> str
        """
        ...
    @property
    def Position(self):
        """
        Gets or sets the current position of this stream.

        Get: Position(self: FileStream) -> Int64

        Set: Position(self: FileStream) = value
        """
        ...
    @property
    def SafeFileHandle(self):
        """
        Gets a Microsoft.Win32.SafeHandles.SafeFileHandle object that represents the operating system file handle for the file that the current System.IO.FileStream object encapsulates.

        Get: SafeFileHandle(self: FileStream) -> SafeFileHandle
        """
        ...

class FileSystemEventArgs(EventArgs):
    """
    Provides data for the directory events: System.IO.FileSystemWatcher.Changed, System.IO.FileSystemWatcher.Created, System.IO.FileSystemWatcher.Deleted.

    FileSystemEventArgs(changeType: WatcherChangeTypes, directory: str, name: str)
    """

    @staticmethod  # known case of __new__
    def __new__(cls, changeType, directory, name):
        """__new__(cls: type, changeType: WatcherChangeTypes, directory: str, name: str)"""
        ...
    @property
    def ChangeType(self):
        """
        Gets the type of directory event that occurred.

        Get: ChangeType(self: FileSystemEventArgs) -> WatcherChangeTypes
        """
        ...
    @property
    def FullPath(self):
        """
        Gets the fully qualifed path of the affected file or directory.

        Get: FullPath(self: FileSystemEventArgs) -> str
        """
        ...
    @property
    def Name(self):
        """
        Gets the name of the affected file or directory.

        Get: Name(self: FileSystemEventArgs) -> str
        """
        ...

class FileSystemEventHandler(MulticastDelegate):  # skipped bases: <type 'ICloneable'>, <type 'ISerializable'>
    """
    Represents the method that will handle the System.IO.FileSystemWatcher.Changed, System.IO.FileSystemWatcher.Created, or System.IO.FileSystemWatcher.Deleted event of a System.IO.FileSystemWatcher class.

    FileSystemEventHandler(object: object, method: IntPtr)
    """

    def BeginInvoke(self, sender, e, callback, object):
        """BeginInvoke(self: FileSystemEventHandler, sender: object, e: FileSystemEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult"""
        ...
    def EndInvoke(self, result):
        """EndInvoke(self: FileSystemEventHandler, result: IAsyncResult)"""
        ...
    def Invoke(self, sender, e):
        """Invoke(self: FileSystemEventHandler, sender: object, e: FileSystemEventArgs)"""
        ...

class FileSystemWatcher(Component, ISupportInitialize):  # skipped bases: <type 'IComponent'>, <type 'IDisposable'>
    """
    Listens to the file system change notifications and raises events when a directory, or file in a directory, changes.To browse the .NET Framework source code for this type, see the Reference Source.

    FileSystemWatcher()

    FileSystemWatcher(path: str)

    FileSystemWatcher(path: str, filter: str)
    """

    def OnChanged(self, *args):  # cannot find CLR method
        """
        OnChanged(self: FileSystemWatcher, e: FileSystemEventArgs)

            Raises the System.IO.FileSystemWatcher.Changed event.

            e: A System.IO.FileSystemEventArgs that contains the event data.
        """
        ...
    def OnCreated(self, *args):  # cannot find CLR method
        """
        OnCreated(self: FileSystemWatcher, e: FileSystemEventArgs)

            Raises the System.IO.FileSystemWatcher.Created event.

            e: A System.IO.FileSystemEventArgs that contains the event data.
        """
        ...
    def OnDeleted(self, *args):  # cannot find CLR method
        """
        OnDeleted(self: FileSystemWatcher, e: FileSystemEventArgs)

            Raises the System.IO.FileSystemWatcher.Deleted event.

            e: A System.IO.FileSystemEventArgs that contains the event data.
        """
        ...
    def OnError(self, *args):  # cannot find CLR method
        """
        OnError(self: FileSystemWatcher, e: ErrorEventArgs)

            Raises the System.IO.FileSystemWatcher.Error event.

            e: An System.IO.ErrorEventArgs that contains the event data.
        """
        ...
    def OnRenamed(self, *args):  # cannot find CLR method
        """
        OnRenamed(self: FileSystemWatcher, e: RenamedEventArgs)

            Raises the System.IO.FileSystemWatcher.Renamed event.

            e: A System.IO.RenamedEventArgs that contains the event data.
        """
        ...
    def WaitForChanged(self, changeType, timeout=None):
        """
        WaitForChanged(self: FileSystemWatcher, changeType: WatcherChangeTypes) -> WaitForChangedResult

            A synchronous method that returns a structure that contains specific information on the change that occurred, given the type of change you want to monitor.

            changeType: The System.IO.WatcherChangeTypes to watch for.

            Returns: A System.IO.WaitForChangedResult that contains specific information on the change that occurred.

        WaitForChanged(self: FileSystemWatcher, changeType: WatcherChangeTypes, timeout: int) -> WaitForChangedResult

            A synchronous method that returns a structure that contains specific information on the change that occurred, given the type of change you want to monitor and the time

             (in milliseconds) to wait before timing out.

            changeType: The System.IO.WatcherChangeTypes to watch for.

            timeout: The time (in milliseconds) to wait before timing out.

            Returns: A System.IO.WaitForChangedResult that contains specific information on the change that occurred.
        """
        ...
    @staticmethod  # known case of __new__
    def __new__(cls, path=None, filter=None):
        """
        __new__(cls: type)

        __new__(cls: type, path: str)

        __new__(cls: type, path: str, filter: str)
        """
        ...
    @property
    def CanRaiseEvents(self):
        """Gets a value indicating whether the component can raise an event."""
        ...
    @property
    def DesignMode(self):
        """Gets a value that indicates whether the System.ComponentModel.Component is currently in design mode."""
        ...
    @property
    def EnableRaisingEvents(self):
        """
        Gets or sets a value indicating whether the component is enabled.

        Get: EnableRaisingEvents(self: FileSystemWatcher) -> bool

        Set: EnableRaisingEvents(self: FileSystemWatcher) = value
        """
        ...
    @property
    def Events(self):
        """Gets the list of event handlers that are attached to this System.ComponentModel.Component."""
        ...
    @property
    def Filter(self):
        """
        Gets or sets the filter string used to determine what files are monitored in a directory.

        Get: Filter(self: FileSystemWatcher) -> str

        Set: Filter(self: FileSystemWatcher) = value
        """
        ...
    @property
    def IncludeSubdirectories(self):
        """
        Gets or sets a value indicating whether subdirectories within the specified path should be monitored.

        Get: IncludeSubdirectories(self: FileSystemWatcher) -> bool

        Set: IncludeSubdirectories(self: FileSystemWatcher) = value
        """
        ...
    @property
    def InternalBufferSize(self):
        """
        Gets or sets the size (in bytes) of the internal buffer.

        Get: InternalBufferSize(self: FileSystemWatcher) -> int

        Set: InternalBufferSize(self: FileSystemWatcher) = value
        """
        ...
    @property
    def NotifyFilter(self):
        """
        Gets or sets the type of changes to watch for.

        Get: NotifyFilter(self: FileSystemWatcher) -> NotifyFilters

        Set: NotifyFilter(self: FileSystemWatcher) = value
        """
        ...
    @property
    def Path(self):
        """
        Gets or sets the path of the directory to watch.

        Get: Path(self: FileSystemWatcher) -> str

        Set: Path(self: FileSystemWatcher) = value
        """
        ...
    @property
    def Site(self):
        """
        Gets or sets an System.ComponentModel.ISite for the System.IO.FileSystemWatcher.

        Get: Site(self: FileSystemWatcher) -> ISite

        Set: Site(self: FileSystemWatcher) = value
        """
        ...
    @property
    def SynchronizingObject(self):
        """
        Gets or sets the object used to marshal the event handler calls issued as a result of a directory change.

        Get: SynchronizingObject(self: FileSystemWatcher) -> ISynchronizeInvoke

        Set: SynchronizingObject(self: FileSystemWatcher) = value
        """
        ...
    Changed = None
    Created = None
    Deleted = None
    Error = None
    Renamed = None

class InternalBufferOverflowException(SystemException):  # skipped bases: <type '_Exception'>, <type 'ISerializable'>
    """
    The exception thrown when the internal buffer overflows.

    InternalBufferOverflowException()

    InternalBufferOverflowException(message: str)

    InternalBufferOverflowException(message: str, inner: Exception)
    """

    SerializeObjectState = None

class InvalidDataException(SystemException):  # skipped bases: <type '_Exception'>, <type 'ISerializable'>
    """
    The exception that is thrown when a data stream is in an invalid format.

    InvalidDataException()

    InvalidDataException(message: str)

    InvalidDataException(message: str, innerException: Exception)
    """

    SerializeObjectState = None

class IODescriptionAttribute(DescriptionAttribute):  # skipped bases: <type '_Attribute'>
    """
    Sets the description visual designers can display when referencing an event, extender, or property.

    IODescriptionAttribute(description: str)
    """

    @property
    def Description(self):
        """
        Gets the description.

        Get: Description(self: IODescriptionAttribute) -> str
        """
        ...
    @property
    def DescriptionValue(self):
        """Gets or sets the string stored as the description."""
        ...

class MemoryStream(Stream):  # skipped bases: <type 'IDisposable'>
    """
    Creates a stream whose backing store is memory.To browse the .NET Framework source code for this type, see the Reference Source.

    MemoryStream()

    MemoryStream(capacity: int)

    MemoryStream(buffer: Array[Byte])

    MemoryStream(buffer: Array[Byte], writable: bool)

    MemoryStream(buffer: Array[Byte], index: int, count: int)

    MemoryStream(buffer: Array[Byte], index: int, count: int, writable: bool)

    MemoryStream(buffer: Array[Byte], index: int, count: int, writable: bool, publiclyVisible: bool)
    """

    def GetBuffer(self):
        """
        GetBuffer(self: MemoryStream) -> Array[Byte]

            Returns the array of unsigned bytes from which this stream was created.

            Returns: The byte array from which this stream was created, or the underlying array if a byte array was not provided to the System.IO.MemoryStream constructor during

             construction of the current instance.
        """
        ...
    def ToArray(self):
        """
        ToArray(self: MemoryStream) -> Array[Byte]

            Writes the stream contents to a byte array, regardless of the System.IO.MemoryStream.Position property.

            Returns: A new byte array.
        """
        ...
    def TryGetBuffer(self, buffer):
        """TryGetBuffer(self: MemoryStream) -> (bool, ArraySegment[Byte])"""
        ...
    def WriteTo(self, stream):
        """
        WriteTo(self: MemoryStream, stream: Stream)

            Writes the entire contents of this memory stream to another stream.

            stream: The stream to write this memory stream to.
        """
        ...
    @staticmethod  # known case of __new__
    def __new__(cls, *__args):
        """
        __new__(cls: type)

        __new__(cls: type, capacity: int)

        __new__(cls: type, buffer: Array[Byte])

        __new__(cls: type, buffer: Array[Byte], writable: bool)

        __new__(cls: type, buffer: Array[Byte], index: int, count: int)

        __new__(cls: type, buffer: Array[Byte], index: int, count: int, writable: bool)

        __new__(cls: type, buffer: Array[Byte], index: int, count: int, writable: bool, publiclyVisible: bool)
        """
        ...
    @property
    def CanRead(self):
        """
        Gets a value indicating whether the current stream supports reading.

        Get: CanRead(self: MemoryStream) -> bool
        """
        ...
    @property
    def CanSeek(self):
        """
        Gets a value indicating whether the current stream supports seeking.

        Get: CanSeek(self: MemoryStream) -> bool
        """
        ...
    @property
    def CanWrite(self):
        """
        Gets a value indicating whether the current stream supports writing.

        Get: CanWrite(self: MemoryStream) -> bool
        """
        ...
    @property
    def Capacity(self):
        """
        Gets or sets the number of bytes allocated for this stream.

        Get: Capacity(self: MemoryStream) -> int

        Set: Capacity(self: MemoryStream) = value
        """
        ...
    @property
    def Length(self):
        """
        Gets the length of the stream in bytes.

        Get: Length(self: MemoryStream) -> Int64
        """
        ...
    @property
    def Position(self):
        """
        Gets or sets the current position within the stream.

        Get: Position(self: MemoryStream) -> Int64

        Set: Position(self: MemoryStream) = value
        """
        ...

class NotifyFilters(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies changes to watch for in a file or folder.

    enum (flags) NotifyFilters, values: Attributes (4), CreationTime (64), DirectoryName (2), FileName (1), LastAccess (32), LastWrite (16), Security (256), Size (8)
    """

    Attributes = None
    CreationTime = None
    DirectoryName = None
    FileName = None
    LastAccess = None
    LastWrite = None
    Security = None
    Size = None
    value__ = None

class Path:  # skipped bases: <type 'object'>
    """Performs operations on System.String instances that contain file or directory path information. These operations are performed in a cross-platform manner.To browse the .NET Framework source code for this type, see the Reference Source."""

    @staticmethod
    def ChangeExtension(path, extension):
        """
        ChangeExtension(path: str, extension: str) -> str

            Changes the extension of a path string.

            path: The path information to modify. The path cannot contain any of the characters defined in System.IO.Path.GetInvalidPathChars.

            extension: The new extension (with or without a leading period). Specify ll to remove an existing extension from path.

            Returns: The modified path information.On Windows-based desktop platforms, if path is ll or an empty string (""), the path information is returned unmodified. If extension is

             ll, the returned string contains the specified path with its extension removed. If path has no extension, and extension is not ll, the returned path string contains

             extension appended to the end of path.
        """
        ...
    @staticmethod
    def Combine(*__args):
        """
        Combine(*paths: Array[str]) -> str

            Combines an array of strings into a path.

            paths: An array of parts of the path.

            Returns: The combined paths.

        Combine(path1: str, path2: str, path3: str) -> str

            Combines three strings into a path.

            path1: The first path to combine.

            path2: The second path to combine.

            path3: The third path to combine.

            Returns: The combined paths.

        Combine(path1: str, path2: str, path3: str, path4: str) -> str

            Combines four strings into a path.

            path1: The first path to combine.

            path2: The second path to combine.

            path3: The third path to combine.

            path4: The fourth path to combine.

            Returns: The combined paths.

        Combine(path1: str, path2: str) -> str

            Combines two strings into a path.

            path1: The first path to combine.

            path2: The second path to combine.

            Returns: The combined paths. If one of the specified paths is a zero-length string, this method returns the other path. If path2 contains an absolute path, this method returns

             path2.
        """
        ...
    @staticmethod
    def GetDirectoryName(path):
        """
        GetDirectoryName(path: str) -> str

            Returns the directory information for the specified path string.

            path: The path of a file or directory.

            Returns: Directory information for path, or ll if path denotes a root directory or is null. Returns System.String.Empty if path does not contain directory information.
        """
        ...
    @staticmethod
    def GetExtension(path):
        """
        GetExtension(path: str) -> str

            Returns the extension of the specified path string.

            path: The path string from which to get the extension.

            Returns: The extension of the specified path (including the period "."), or ll, or System.String.Empty. If path is ll, System.IO.Path.GetExtension(System.String) returns ll. If

             path does not have extension information, System.IO.Path.GetExtension(System.String) returns System.String.Empty.
        """
        ...
    @staticmethod
    def GetFileName(path):
        """
        GetFileName(path: str) -> str

            Returns the file name and extension of the specified path string.

            path: The path string from which to obtain the file name and extension.

            Returns: The characters after the last directory character in path. If the last character of path is a directory or volume separator character, this method returns

             System.String.Empty. If path is ll, this method returns ll.
        """
        ...
    @staticmethod
    def GetFileNameWithoutExtension(path):
        """
        GetFileNameWithoutExtension(path: str) -> str

            Returns the file name of the specified path string without the extension.

            path: The path of the file.

            Returns: The string returned by System.IO.Path.GetFileName(System.String), minus the last period (.) and all characters following it.
        """
        ...
    @staticmethod
    def GetFullPath(path):
        """
        GetFullPath(path: str) -> str

            Returns the absolute path for the specified path string.

            path: The file or directory for which to obtain absolute path information.

            Returns: The fully qualified location of path, such as "C:\\MyFile.txt".
        """
        ...
    @staticmethod
    def GetInvalidFileNameChars():
        """
        GetInvalidFileNameChars() -> Array[Char]

            Gets an array containing the characters that are not allowed in file names.

            Returns: An array containing the characters that are not allowed in file names.
        """
        ...
    @staticmethod
    def GetInvalidPathChars():
        """
        GetInvalidPathChars() -> Array[Char]

            Gets an array containing the characters that are not allowed in path names.

            Returns: An array containing the characters that are not allowed in path names.
        """
        ...
    @staticmethod
    def GetPathRoot(path):
        """
        GetPathRoot(path: str) -> str

            Gets the root directory information of the specified path.

            path: The path from which to obtain root directory information.

            Returns: The root directory of path, such as "C:\", or ll if path is ll, or an empty string if path does not contain root directory information.
        """
        ...
    @staticmethod
    def GetRandomFileName():
        """
        GetRandomFileName() -> str

            Returns a random folder name or file name.

            Returns: A random folder name or file name.
        """
        ...
    @staticmethod
    def GetTempFileName():
        """
        GetTempFileName() -> str

            Creates a uniquely named, zero-byte temporary file on disk and returns the full path of that file.

            Returns: The full path of the temporary file.
        """
        ...
    @staticmethod
    def GetTempPath():
        """
        GetTempPath() -> str

            Returns the path of the current user's temporary folder.

            Returns: The path to the temporary folder, ending with a backslash.
        """
        ...
    @staticmethod
    def HasExtension(path):
        """
        HasExtension(path: str) -> bool

            Determines whether a path includes a file name extension.

            path: The path to search for an extension.

            Returns: ue if the characters that follow the last directory separator (\\ or /) or volume separator (:) in the path include a period (.) followed by one or more characters;

             otherwise, lse.
        """
        ...
    @staticmethod
    def IsPathRooted(path):
        """
        IsPathRooted(path: str) -> bool

            Gets a value indicating whether the specified path string contains a root.

            path: The path to test.

            Returns: ue if path contains a root; otherwise, lse.
        """
        ...
    AltDirectorySeparatorChar = None
    DirectorySeparatorChar = None
    InvalidPathChars = None
    PathSeparator = None
    VolumeSeparatorChar = None
    __all__ = [
        "AltDirectorySeparatorChar",
        "ChangeExtension",
        "Combine",
        "DirectorySeparatorChar",
        "GetDirectoryName",
        "GetExtension",
        "GetFileName",
        "GetFileNameWithoutExtension",
        "GetFullPath",
        "GetInvalidFileNameChars",
        "GetInvalidPathChars",
        "GetPathRoot",
        "GetRandomFileName",
        "GetTempFileName",
        "GetTempPath",
        "HasExtension",
        "InvalidPathChars",
        "IsPathRooted",
        "PathSeparator",
        "VolumeSeparatorChar",
    ]

class PathTooLongException(IOException):  # skipped bases: <type '_Exception'>, <type 'ISerializable'>
    """
    The exception that is thrown when a path or fully qualified file name is longer than the system-defined maximum length.

    PathTooLongException()

    PathTooLongException(message: str)

    PathTooLongException(message: str, innerException: Exception)
    """

    SerializeObjectState = None

class RenamedEventArgs(FileSystemEventArgs):
    """
    Provides data for the System.IO.FileSystemWatcher.Renamed event.

    RenamedEventArgs(changeType: WatcherChangeTypes, directory: str, name: str, oldName: str)
    """

    @property
    def OldFullPath(self):
        """
        Gets the previous fully qualified path of the affected file or directory.

        Get: OldFullPath(self: RenamedEventArgs) -> str
        """
        ...
    @property
    def OldName(self):
        """
        Gets the old name of the affected file or directory.

        Get: OldName(self: RenamedEventArgs) -> str
        """
        ...

class RenamedEventHandler(MulticastDelegate):  # skipped bases: <type 'ICloneable'>, <type 'ISerializable'>
    """
    Represents the method that will handle the System.IO.FileSystemWatcher.Renamed event of a System.IO.FileSystemWatcher class.

    RenamedEventHandler(object: object, method: IntPtr)
    """

    def BeginInvoke(self, sender, e, callback, object):
        """BeginInvoke(self: RenamedEventHandler, sender: object, e: RenamedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult"""
        ...
    def EndInvoke(self, result):
        """EndInvoke(self: RenamedEventHandler, result: IAsyncResult)"""
        ...
    def Invoke(self, sender, e):
        """Invoke(self: RenamedEventHandler, sender: object, e: RenamedEventArgs)"""
        ...

class SearchOption(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies whether to search the current directory, or the current directory and all subdirectories.

    enum SearchOption, values: AllDirectories (1), TopDirectoryOnly (0)
    """

    AllDirectories = None
    TopDirectoryOnly = None
    value__ = None

class SeekOrigin(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies the position in a stream to use for seeking.

    enum SeekOrigin, values: Begin (0), Current (1), End (2)
    """

    Begin = None
    Current = None
    End = None
    value__ = None

class TextReader(MarshalByRefObject, IDisposable):
    """Represents a reader that can read a sequential series of characters."""

    def Close(self):
        """
        Close(self: TextReader)

            Closes the System.IO.TextReader and releases any system resources associated with the xtReader.
        """
        ...
    def Peek(self):
        """
        Peek(self: TextReader) -> int

            Reads the next character without changing the state of the reader or the character source. Returns the next available character without actually reading it from the

             reader.

            Returns: An integer representing the next character to be read, or -1 if no more characters are available or the reader does not support seeking.
        """
        ...
    def Read(self, buffer=None, index=None, count=None):
        """
        Read(self: TextReader) -> int

            Reads the next character from the text reader and advances the character position by one character.

            Returns: The next character from the text reader, or -1 if no more characters are available. The default implementation returns -1.

        Read(self: TextReader, index: int, count: int) -> (int, Array[Char])

            Reads a specified maximum number of characters from the current reader and writes the data to a buffer, beginning at the specified index.

            index: The position in buffer at which to begin writing.

            count: The maximum number of characters to read. If the end of the reader is reached before the specified number of characters is read into the buffer, the method returns.

            Returns: The number of characters that have been read. The number will be less than or equal to count, depending on whether the data is available within the reader. This method

             returns 0 (zero) if it is called when no more characters are left to read.
        """
        ...
    def ReadAsync(self, buffer, index, count):
        """
        ReadAsync(self: TextReader, buffer: Array[Char], index: int, count: int) -> Task[int]

            Reads a specified maximum number of characters from the current text reader asynchronously and writes the data to a buffer, beginning at the specified index.

            buffer: When this method returns, contains the specified character array with the values between index and (index + count - 1) replaced by the characters read from the current

             source.

            index: The position in buffer at which to begin writing.

            count: The maximum number of characters to read. If the end of the text is reached before the specified number of characters is read into the buffer, the current method

             returns.

            Returns: A task that represents the asynchronous read operation. The value of the TResult parameter contains the total number of bytes read into the buffer. The result value

             can be less than the number of bytes requested if the number of bytes currently available is less than the requested number, or it can be 0 (zero) if the end of the

             text has been reached.
        """
        ...
    def ReadBlock(self, buffer, index, count):
        """
        ReadBlock(self: TextReader, index: int, count: int) -> (int, Array[Char])

            Reads a specified maximum number of characters from the current text reader and writes the data to a buffer, beginning at the specified index.

            index: The position in buffer at which to begin writing.

            count: The maximum number of characters to read.

            Returns: The number of characters that have been read. The number will be less than or equal to count, depending on whether all input characters have been read.
        """
        ...
    def ReadBlockAsync(self, buffer, index, count):
        """
        ReadBlockAsync(self: TextReader, buffer: Array[Char], index: int, count: int) -> Task[int]

            Reads a specified maximum number of characters from the current text reader asynchronously and writes the data to a buffer, beginning at the specified index.

            buffer: When this method returns, contains the specified character array with the values between index and (index + count - 1) replaced by the characters read from the current

             source.

            index: The position in buffer at which to begin writing.

            count: The maximum number of characters to read. If the end of the text is reached before the specified number of characters is read into the buffer, the current method

             returns.

            Returns: A task that represents the asynchronous read operation. The value of the TResult parameter contains the total number of bytes read into the buffer. The result value

             can be less than the number of bytes requested if the number of bytes currently available is less than the requested number, or it can be 0 (zero) if the end of the

             text has been reached.
        """
        ...
    def ReadLine(self):
        """
        ReadLine(self: TextReader) -> str

            Reads a line of characters from the text reader and returns the data as a string.

            Returns: The next line from the reader, or ll if all characters have been read.
        """
        ...
    def ReadLineAsync(self):
        """
        ReadLineAsync(self: TextReader) -> Task[str]

            Reads a line of characters asynchronously and returns the data as a string.

            Returns: A task that represents the asynchronous read operation. The value of the TResult parameter contains the next line from the text reader, or is ll if all of the

             characters have been read.
        """
        ...
    def ReadToEnd(self):
        """
        ReadToEnd(self: TextReader) -> str

            Reads all characters from the current position to the end of the text reader and returns them as one string.

            Returns: A string that contains all characters from the current position to the end of the text reader.
        """
        ...
    def ReadToEndAsync(self):
        """
        ReadToEndAsync(self: TextReader) -> Task[str]

            Reads all characters from the current position to the end of the text reader asynchronously and returns them as one string.

            Returns: A task that represents the asynchronous read operation. The value of the TResult parameter contains a string with the characters from the current position to the end

             of the text reader.
        """
        ...
    @staticmethod
    def Synchronized(reader):
        """
        Synchronized(reader: TextReader) -> TextReader

            Creates a thread-safe wrapper around the specified xtReader.

            reader: The xtReader to synchronize.

            Returns: A thread-safe System.IO.TextReader.
        """
        ...
    Null = None

class StreamReader(TextReader):  # skipped bases: <type 'IDisposable'>
    """
    Implements a System.IO.TextReader that reads characters from a byte stream in a particular encoding.To browse the .NET Framework source code for this type, see the Reference Source.

    StreamReader(stream: Stream)

    StreamReader(stream: Stream, detectEncodingFromByteOrderMarks: bool)

    StreamReader(stream: Stream, encoding: Encoding)

    StreamReader(stream: Stream, encoding: Encoding, detectEncodingFromByteOrderMarks: bool)

    StreamReader(stream: Stream, encoding: Encoding, detectEncodingFromByteOrderMarks: bool, bufferSize: int)

    StreamReader(stream: Stream, encoding: Encoding, detectEncodingFromByteOrderMarks: bool, bufferSize: int, leaveOpen: bool)

    StreamReader(path: str)

    StreamReader(path: str, detectEncodingFromByteOrderMarks: bool)

    StreamReader(path: str, encoding: Encoding)

    StreamReader(path: str, encoding: Encoding, detectEncodingFromByteOrderMarks: bool)

    StreamReader(path: str, encoding: Encoding, detectEncodingFromByteOrderMarks: bool, bufferSize: int)
    """

    def DiscardBufferedData(self):
        """
        DiscardBufferedData(self: StreamReader)

            Clears the internal buffer.
        """
        ...
    @staticmethod  # known case of __new__
    def __new__(cls, *__args):
        """
        __new__(cls: type, stream: Stream)

        __new__(cls: type, stream: Stream, detectEncodingFromByteOrderMarks: bool)

        __new__(cls: type, stream: Stream, encoding: Encoding)

        __new__(cls: type, stream: Stream, encoding: Encoding, detectEncodingFromByteOrderMarks: bool)

        __new__(cls: type, stream: Stream, encoding: Encoding, detectEncodingFromByteOrderMarks: bool, bufferSize: int)

        __new__(cls: type, stream: Stream, encoding: Encoding, detectEncodingFromByteOrderMarks: bool, bufferSize: int, leaveOpen: bool)

        __new__(cls: type, path: str)

        __new__(cls: type, path: str, detectEncodingFromByteOrderMarks: bool)

        __new__(cls: type, path: str, encoding: Encoding)

        __new__(cls: type, path: str, encoding: Encoding, detectEncodingFromByteOrderMarks: bool)

        __new__(cls: type, path: str, encoding: Encoding, detectEncodingFromByteOrderMarks: bool, bufferSize: int)
        """
        ...
    @property
    def BaseStream(self):
        """
        Returns the underlying stream.

        Get: BaseStream(self: StreamReader) -> Stream
        """
        ...
    @property
    def CurrentEncoding(self):
        """
        Gets the current character encoding that the current System.IO.StreamReader object is using.

        Get: CurrentEncoding(self: StreamReader) -> Encoding
        """
        ...
    @property
    def EndOfStream(self):
        """
        Gets a value that indicates whether the current stream position is at the end of the stream.

        Get: EndOfStream(self: StreamReader) -> bool
        """
        ...
    Null = None

class TextWriter(MarshalByRefObject, IDisposable):
    """Represents a writer that can write a sequential series of characters. This class is abstract."""

    def Close(self):
        """
        Close(self: TextWriter)

            Closes the current writer and releases any system resources associated with the writer.
        """
        ...
    def Flush(self):
        """
        Flush(self: TextWriter)

            Clears all buffers for the current writer and causes any buffered data to be written to the underlying device.
        """
        ...
    def FlushAsync(self):
        """
        FlushAsync(self: TextWriter) -> Task

            Asynchronously clears all buffers for the current writer and causes any buffered data to be written to the underlying device.

            Returns: A task that represents the asynchronous flush operation.
        """
        ...
    @staticmethod
    def Synchronized(writer):
        """
        Synchronized(writer: TextWriter) -> TextWriter

            Creates a thread-safe wrapper around the specified xtWriter.

            writer: The xtWriter to synchronize.

            Returns: A thread-safe wrapper.
        """
        ...
    def Write(self, *__args):
        """
        Write(self: TextWriter, value: Char)

            Writes a character to the text string or stream.

            value: The character to write to the text stream.

        Write(self: TextWriter, format: str, arg0: object, arg1: object, arg2: object)

            Writes a formatted string to the text string or stream, using the same semantics as the System.String.Format(System.String,System.Object,System.Object,System.Object)

             method.

            format: A composite format string (see Remarks).

            arg0: The first object to format and write.

            arg1: The second object to format and write.

            arg2: The third object to format and write.

        Write(self: TextWriter, format: str, arg0: object, arg1: object)

            Writes a formatted string to the text string or stream, using the same semantics as the System.String.Format(System.String,System.Object,System.Object) method.

            format: A composite format string (see Remarks).

            arg0: The first object to format and write.

            arg1: The second object to format and write.

        Write(self: TextWriter, format: str, arg0: object)

            Writes a formatted string to the text string or stream, using the same semantics as the System.String.Format(System.String,System.Object) method.

            format: A composite format string (see Remarks).

            arg0: The object to format and write.

        Write(self: TextWriter, value: object)

            Writes the text representation of an object to the text string or stream by calling the String method on that object.

            value: The object to write.

        Write(self: TextWriter, value: str)

            Writes a string to the text string or stream.

            value: The string to write.

        Write(self: TextWriter, value: Decimal)

            Writes the text representation of a decimal value to the text string or stream.

            value: The decimal value to write.

        Write(self: TextWriter, format: str, *arg: Array[object])

            Writes a formatted string to the text string or stream, using the same semantics as the System.String.Format(System.String,System.Object[]) method.

            format: A composite format string (see Remarks).

            arg: An object array that contains zero or more objects to format and write.

        Write(self: TextWriter, value: float)

            Writes the text representation of an 8-byte floating-point value to the text string or stream.

            value: The 8-byte floating-point value to write.

        Write(self: TextWriter, value: UInt64)

            Writes the text representation of an 8-byte unsigned integer to the text string or stream.

            value: The 8-byte unsigned integer to write.

        Write(self: TextWriter, value: Int64)

            Writes the text representation of an 8-byte signed integer to the text string or stream.

            value: The 8-byte signed integer to write.

        Write(self: TextWriter, value: UInt32)

            Writes the text representation of a 4-byte unsigned integer to the text string or stream.

            value: The 4-byte unsigned integer to write.

        Write(self: TextWriter, value: int)

            Writes the text representation of a 4-byte signed integer to the text string or stream.

            value: The 4-byte signed integer to write.

        Write(self: TextWriter, buffer: Array[Char], index: int, count: int)

            Writes a subarray of characters to the text string or stream.

            buffer: The character array to write data from.

            index: The character position in the buffer at which to start retrieving data.

            count: The number of characters to write.

        Write(self: TextWriter, buffer: Array[Char])

            Writes a character array to the text string or stream.

            buffer: The character array to write to the text stream.

        Write(self: TextWriter, value: Single)

            Writes the text representation of a 4-byte floating-point value to the text string or stream.

            value: The 4-byte floating-point value to write.

        Write(self: TextWriter, value: bool)

            Writes the text representation of a olean value to the text string or stream.

            value: The olean value to write.
        """
        ...
    def WriteAsync(self, *__args):
        """
        WriteAsync(self: TextWriter, value: Char) -> Task

            Writes a character to the text string or stream asynchronously.

            value: The character to write to the text stream.

            Returns: A task that represents the asynchronous write operation.

        WriteAsync(self: TextWriter, value: str) -> Task

            Writes a string to the text string or stream asynchronously.

            value: The string to write. If value is ll, nothing is written to the text stream.

            Returns: A task that represents the asynchronous write operation.

        WriteAsync(self: TextWriter, buffer: Array[Char], index: int, count: int) -> Task

            Writes a subarray of characters to the text string or stream asynchronously.

            buffer: The character array to write data from.

            index: The character position in the buffer at which to start retrieving data.

            count: The number of characters to write.

            Returns: A task that represents the asynchronous write operation.

        WriteAsync(self: TextWriter, buffer: Array[Char]) -> Task

            Writes a character array to the text string or stream asynchronously.

            buffer: The character array to write to the text stream. If buffer is ll, nothing is written.

            Returns: A task that represents the asynchronous write operation.
        """
        ...
    def WriteLine(self, *__args):
        """
        WriteLine(self: TextWriter)

            Writes a line terminator to the text string or stream.

        WriteLine(self: TextWriter, format: str, arg0: object, arg1: object)

            Writes a formatted string and a new line to the text string or stream, using the same semantics as the System.String.Format(System.String,System.Object,System.Object)

             method.

            format: A composite format string (see Remarks).

            arg0: The first object to format and write.

            arg1: The second object to format and write.

        WriteLine(self: TextWriter, format: str, arg0: object)

            Writes a formatted string and a new line to the text string or stream, using the same semantics as the System.String.Format(System.String,System.Object) method.

            format: A composite format string (see Remarks).

            arg0: The object to format and write.

        WriteLine(self: TextWriter, value: object)

            Writes the text representation of an object by calling the String method on that object, followed by a line terminator to the text string or stream.

            value: The object to write. If value is ll, only the line terminator is written.

        WriteLine(self: TextWriter, value: str)

            Writes a string followed by a line terminator to the text string or stream.

            value: The string to write. If value is ll, only the line terminator is written.

        WriteLine(self: TextWriter, value: Decimal)

            Writes the text representation of a decimal value followed by a line terminator to the text string or stream.

            value: The decimal value to write.

        WriteLine(self: TextWriter, value: float)

            Writes the text representation of a 8-byte floating-point value followed by a line terminator to the text string or stream.

            value: The 8-byte floating-point value to write.

        WriteLine(self: TextWriter, value: Single)

            Writes the text representation of a 4-byte floating-point value followed by a line terminator to the text string or stream.

            value: The 4-byte floating-point value to write.

        WriteLine(self: TextWriter, value: UInt64)

            Writes the text representation of an 8-byte unsigned integer followed by a line terminator to the text string or stream.

            value: The 8-byte unsigned integer to write.

        WriteLine(self: TextWriter, value: Int64)

            Writes the text representation of an 8-byte signed integer followed by a line terminator to the text string or stream.

            value: The 8-byte signed integer to write.

        WriteLine(self: TextWriter, value: UInt32)

            Writes the text representation of a 4-byte unsigned integer followed by a line terminator to the text string or stream.

            value: The 4-byte unsigned integer to write.

        WriteLine(self: TextWriter, value: int)

            Writes the text representation of a 4-byte signed integer followed by a line terminator to the text string or stream.

            value: The 4-byte signed integer to write.

        WriteLine(self: TextWriter, value: bool)

            Writes the text representation of a olean value followed by a line terminator to the text string or stream.

            value: The olean value to write.

        WriteLine(self: TextWriter, buffer: Array[Char], index: int, count: int)

            Writes a subarray of characters followed by a line terminator to the text string or stream.

            buffer: The character array from which data is read.

            index: The character position in buffer at which to start reading data.

            count: The maximum number of characters to write.

        WriteLine(self: TextWriter, buffer: Array[Char])

            Writes an array of characters followed by a line terminator to the text string or stream.

            buffer: The character array from which data is read.

        WriteLine(self: TextWriter, value: Char)

            Writes a character followed by a line terminator to the text string or stream.

            value: The character to write to the text stream.

        WriteLine(self: TextWriter, format: str, arg0: object, arg1: object, arg2: object)

            Writes out a formatted string and a new line, using the same semantics as System.String.Format(System.String,System.Object).

            format: A composite format string (see Remarks).

            arg0: The first object to format and write.

            arg1: The second object to format and write.

            arg2: The third object to format and write.

        WriteLine(self: TextWriter, format: str, *arg: Array[object])

            Writes out a formatted string and a new line, using the same semantics as System.String.Format(System.String,System.Object).

            format: A composite format string (see Remarks).

            arg: An object array that contains zero or more objects to format and write.
        """
        ...
    def WriteLineAsync(self, *__args):
        """
        WriteLineAsync(self: TextWriter, value: Char) -> Task

            Writes a character followed by a line terminator asynchronously to the text string or stream.

            value: The character to write to the text stream.

            Returns: A task that represents the asynchronous write operation.

        WriteLineAsync(self: TextWriter, value: str) -> Task

            Writes a string followed by a line terminator asynchronously to the text string or stream.

            value: The string to write. If the value is ll, only a line terminator is written.

            Returns: A task that represents the asynchronous write operation.

        WriteLineAsync(self: TextWriter, buffer: Array[Char], index: int, count: int) -> Task

            Writes a subarray of characters followed by a line terminator asynchronously to the text string or stream.

            buffer: The character array to write data from.

            index: The character position in the buffer at which to start retrieving data.

            count: The number of characters to write.

            Returns: A task that represents the asynchronous write operation.

        WriteLineAsync(self: TextWriter) -> Task

            Writes a line terminator asynchronously to the text string or stream.

            Returns: A task that represents the asynchronous write operation.

        WriteLineAsync(self: TextWriter, buffer: Array[Char]) -> Task

            Writes an array of characters followed by a line terminator asynchronously to the text string or stream.

            buffer: The character array to write to the text stream. If the character array is ll, only the line terminator is written.

            Returns: A task that represents the asynchronous write operation.
        """
        ...
    @staticmethod  # known case of __new__
    def __new__(cls, *args):  # cannot find CLR constructor
        """
        __new__(cls: type)

        __new__(cls: type, formatProvider: IFormatProvider)
        """
        ...
    @property
    def Encoding(self):
        """
        When overridden in a derived class, returns the character encoding in which the output is written.

        Get: Encoding(self: TextWriter) -> Encoding
        """
        ...
    @property
    def FormatProvider(self):
        """
        Gets an object that controls formatting.

        Get: FormatProvider(self: TextWriter) -> IFormatProvider
        """
        ...
    @property
    def NewLine(self):
        """
        Gets or sets the line terminator string used by the current xtWriter.

        Get: NewLine(self: TextWriter) -> str

        Set: NewLine(self: TextWriter) = value
        """
        ...
    CoreNewLine = None
    Null = None

class StreamWriter(TextWriter):  # skipped bases: <type 'IDisposable'>
    """
    Implements a System.IO.TextWriter for writing characters to a stream in a particular encoding.To browse the .NET Framework source code for this type, see the Reference Source.

    StreamWriter(stream: Stream)

    StreamWriter(stream: Stream, encoding: Encoding)

    StreamWriter(stream: Stream, encoding: Encoding, bufferSize: int)

    StreamWriter(stream: Stream, encoding: Encoding, bufferSize: int, leaveOpen: bool)

    StreamWriter(path: str)

    StreamWriter(path: str, append: bool)

    StreamWriter(path: str, append: bool, encoding: Encoding)

    StreamWriter(path: str, append: bool, encoding: Encoding, bufferSize: int)
    """

    @property
    def AutoFlush(self):
        """
        Gets or sets a value indicating whether the System.IO.StreamWriter will flush its buffer to the underlying stream after every call to System.IO.StreamWriter.Write(System.Char).

        Get: AutoFlush(self: StreamWriter) -> bool

        Set: AutoFlush(self: StreamWriter) = value
        """
        ...
    @property
    def BaseStream(self):
        """
        Gets the underlying stream that interfaces with a backing store.

        Get: BaseStream(self: StreamWriter) -> Stream
        """
        ...
    @property
    def Encoding(self):
        """
        Gets the System.Text.Encoding in which the output is written.

        Get: Encoding(self: StreamWriter) -> Encoding
        """
        ...
    CoreNewLine = None
    Null = None

class StringReader(TextReader):  # skipped bases: <type 'IDisposable'>
    """
    Implements a System.IO.TextReader that reads from a string.

    StringReader(s: str)
    """

    @staticmethod  # known case of __new__
    def __new__(cls, s):
        """__new__(cls: type, s: str)"""
        ...

class StringWriter(TextWriter):  # skipped bases: <type 'IDisposable'>
    """
    Implements a System.IO.TextWriter for writing information to a string. The information is stored in an underlying System.Text.StringBuilder.

    StringWriter()

    StringWriter(formatProvider: IFormatProvider)

    StringWriter(sb: StringBuilder)

    StringWriter(sb: StringBuilder, formatProvider: IFormatProvider)
    """

    def GetStringBuilder(self):
        """
        GetStringBuilder(self: StringWriter) -> StringBuilder

            Returns the underlying System.Text.StringBuilder.

            Returns: The underlying ringBuilder.
        """
        ...
    def ToString(self):
        """
        ToString(self: StringWriter) -> str

            Returns a string containing the characters written to the current ringWriter so far.

            Returns: The string containing the characters written to the current ringWriter.
        """
        ...
    def __str__(self, *args): ...
    @property
    def Encoding(self):
        """
        Gets the System.Text.Encoding in which the output is written.

        Get: Encoding(self: StringWriter) -> Encoding
        """
        ...
    CoreNewLine = None

class UnmanagedMemoryAccessor(IDisposable):
    """
    Provides random access to unmanaged blocks of memory from managed code.

    UnmanagedMemoryAccessor(buffer: SafeBuffer, offset: Int64, capacity: Int64)

    UnmanagedMemoryAccessor(buffer: SafeBuffer, offset: Int64, capacity: Int64, access: FileAccess)
    """

    def Initialize(self, *args):  # cannot find CLR method
        """
        Initialize(self: UnmanagedMemoryAccessor, buffer: SafeBuffer, offset: Int64, capacity: Int64, access: FileAccess)

            Sets the initial values for the accessor.

            buffer: The buffer to contain the accessor.

            offset: The byte at which to start the accessor.

            capacity: The size, in bytes, of memory to allocate.

            access: The type of access allowed to the memory. The default is System.IO.MemoryMappedFiles.MemoryMappedFileAccess.ReadWrite.
        """
        ...
    def Read(self, position, structure):
        """Read[T](self: UnmanagedMemoryAccessor, position: Int64) -> T"""
        ...
    def ReadArray(self, position, array, offset, count):
        """ReadArray[T](self: UnmanagedMemoryAccessor, position: Int64, array: Array[T], offset: int, count: int) -> int"""
        ...
    def ReadBoolean(self, position):
        """
        ReadBoolean(self: UnmanagedMemoryAccessor, position: Int64) -> bool

            Reads a Boolean value from the accessor.

            position: The number of bytes into the accessor at which to begin reading.

            Returns: ue or lse.
        """
        ...
    def ReadByte(self, position):
        """
        ReadByte(self: UnmanagedMemoryAccessor, position: Int64) -> Byte

            Reads a byte value from the accessor.

            position: The number of bytes into the accessor at which to begin reading.

            Returns: The value that was read.
        """
        ...
    def ReadChar(self, position):
        """
        ReadChar(self: UnmanagedMemoryAccessor, position: Int64) -> Char

            Reads a character from the accessor.

            position: The number of bytes into the accessor at which to begin reading.

            Returns: The value that was read.
        """
        ...
    def ReadDecimal(self, position):
        """
        ReadDecimal(self: UnmanagedMemoryAccessor, position: Int64) -> Decimal

            Reads a decimal value from the accessor.

            position: The number of bytes into the accessor at which to begin reading.

            Returns: The value that was read.
        """
        ...
    def ReadDouble(self, position):
        """
        ReadDouble(self: UnmanagedMemoryAccessor, position: Int64) -> float

            Reads a double-precision floating-point value from the accessor.

            position: The number of bytes into the accessor at which to begin reading.

            Returns: The value that was read.
        """
        ...
    def ReadInt16(self, position):
        """
        ReadInt16(self: UnmanagedMemoryAccessor, position: Int64) -> Int16

            Reads a 16-bit integer from the accessor.

            position: The number of bytes into the accessor at which to begin reading.

            Returns: The value that was read.
        """
        ...
    def ReadInt32(self, position):
        """
        ReadInt32(self: UnmanagedMemoryAccessor, position: Int64) -> int

            Reads a 32-bit integer from the accessor.

            position: The number of bytes into the accessor at which to begin reading.

            Returns: The value that was read.
        """
        ...
    def ReadInt64(self, position):
        """
        ReadInt64(self: UnmanagedMemoryAccessor, position: Int64) -> Int64

            Reads a 64-bit integer from the accessor.

            position: The number of bytes into the accessor at which to begin reading.

            Returns: The value that was read.
        """
        ...
    def ReadSByte(self, position):
        """
        ReadSByte(self: UnmanagedMemoryAccessor, position: Int64) -> SByte

            Reads an 8-bit signed integer from the accessor.

            position: The number of bytes into the accessor at which to begin reading.

            Returns: The value that was read.
        """
        ...
    def ReadSingle(self, position):
        """
        ReadSingle(self: UnmanagedMemoryAccessor, position: Int64) -> Single

            Reads a single-precision floating-point value from the accessor.

            position: The number of bytes into the accessor at which to begin reading.

            Returns: The value that was read.
        """
        ...
    def ReadUInt16(self, position):
        """
        ReadUInt16(self: UnmanagedMemoryAccessor, position: Int64) -> UInt16

            Reads an unsigned 16-bit integer from the accessor.

            position: The number of bytes into the accessor at which to begin reading.

            Returns: The value that was read.
        """
        ...
    def ReadUInt32(self, position):
        """
        ReadUInt32(self: UnmanagedMemoryAccessor, position: Int64) -> UInt32

            Reads an unsigned 32-bit integer from the accessor.

            position: The number of bytes into the accessor at which to begin reading.

            Returns: The value that was read.
        """
        ...
    def ReadUInt64(self, position):
        """
        ReadUInt64(self: UnmanagedMemoryAccessor, position: Int64) -> UInt64

            Reads an unsigned 64-bit integer from the accessor.

            position: The number of bytes into the accessor at which to begin reading.

            Returns: The value that was read.
        """
        ...
    def Write(self, position, *__args):
        """
        Write(self: UnmanagedMemoryAccessor, position: Int64, value: bool)

            Writes a Boolean value into the accessor.

            position: The number of bytes into the accessor at which to begin writing.

            value: The value to write.

        Write(self: UnmanagedMemoryAccessor, position: Int64, value: Byte)

            Writes a byte value into the accessor.

            position: The number of bytes into the accessor at which to begin writing.

            value: The value to write.

        Write(self: UnmanagedMemoryAccessor, position: Int64, value: Decimal)

            Writes a decimal value into the accessor.

            position: The number of bytes into the accessor at which to begin writing.

            value: The value to write.

        Write(self: UnmanagedMemoryAccessor, position: Int64, value: Char)

            Writes a character into the accessor.

            position: The number of bytes into the accessor at which to begin writing.

            value: The value to write.

        Write(self: UnmanagedMemoryAccessor, position: Int64, value: Int16)

            Writes a 16-bit integer into the accessor.

            position: The number of bytes into the accessor at which to begin writing.

            value: The value to write.

        Write(self: UnmanagedMemoryAccessor, position: Int64, value: int)

            Writes a 32-bit integer into the accessor.

            position: The number of bytes into the accessor at which to begin writing.

            value: The value to write.

        Write(self: UnmanagedMemoryAccessor, position: Int64, value: Int64)

            Writes a 64-bit integer into the accessor.

            position: The number of bytes into the accessor at which to begin writing.

            value: The value to write.

        Write(self: UnmanagedMemoryAccessor, position: Int64, value: Single)

            Writes a ngle into the accessor.

            position: The number of bytes into the accessor at which to begin writing.

            value: The value to write.

        Write(self: UnmanagedMemoryAccessor, position: Int64, value: float)

            Writes a uble value into the accessor.

            position: The number of bytes into the accessor at which to begin writing.

            value: The value to write.

        Write(self: UnmanagedMemoryAccessor, position: Int64, value: SByte)

            Writes an 8-bit integer into the accessor.

            position: The number of bytes into the accessor at which to begin writing.

            value: The value to write.

        Write(self: UnmanagedMemoryAccessor, position: Int64, value: UInt16)

            Writes an unsigned 16-bit integer into the accessor.

            position: The number of bytes into the accessor at which to begin writing.

            value: The value to write.

        Write(self: UnmanagedMemoryAccessor, position: Int64, value: UInt32)

            Writes an unsigned 32-bit integer into the accessor.

            position: The number of bytes into the accessor at which to begin writing.

            value: The value to write.

        Write(self: UnmanagedMemoryAccessor, position: Int64, value: UInt64)

            Writes an unsigned 64-bit integer into the accessor.

            position: The number of bytes into the accessor at which to begin writing.

            value: The value to write.

        Write[T](self: UnmanagedMemoryAccessor, position: Int64, structure: T) -> T
        """
        ...
    def WriteArray(self, position, array, offset, count):
        """WriteArray[T](self: UnmanagedMemoryAccessor, position: Int64, array: Array[T], offset: int, count: int)"""
        ...
    @property
    def CanRead(self):
        """
        Determines whether the accessor is readable.

        Get: CanRead(self: UnmanagedMemoryAccessor) -> bool
        """
        ...
    @property
    def CanWrite(self):
        """
        Determines whether the accessory is writable.

        Get: CanWrite(self: UnmanagedMemoryAccessor) -> bool
        """
        ...
    @property
    def Capacity(self):
        """
        Gets the capacity of the accessor.

        Get: Capacity(self: UnmanagedMemoryAccessor) -> Int64
        """
        ...
    @property
    def IsOpen(self):
        """Determines whether the accessor is currently open by a process."""
        ...

class UnmanagedMemoryStream(Stream):  # skipped bases: <type 'IDisposable'>
    """
    Provides access to unmanaged blocks of memory from managed code.

    UnmanagedMemoryStream(buffer: SafeBuffer, offset: Int64, length: Int64)

    UnmanagedMemoryStream(buffer: SafeBuffer, offset: Int64, length: Int64, access: FileAccess)

    UnmanagedMemoryStream(pointer: Byte*, length: Int64)

    UnmanagedMemoryStream(pointer: Byte*, length: Int64, capacity: Int64, access: FileAccess)
    """

    def Initialize(self, *args):  # cannot find CLR method
        """
        Initialize(self: UnmanagedMemoryStream, pointer: Byte*, length: Int64, capacity: Int64, access: FileAccess)

            Initializes a new instance of the System.IO.UnmanagedMemoryStream class by using a pointer to an unmanaged memory location.

            pointer: A pointer to an unmanaged memory location.

            length: The length of the memory to use.

            capacity: The total amount of memory assigned to the stream.

            access: One of the System.IO.FileAccess values.

        Initialize(self: UnmanagedMemoryStream, buffer: SafeBuffer, offset: Int64, length: Int64, access: FileAccess)

            Initializes a new instance of the System.IO.UnmanagedMemoryStream class in a safe buffer with a specified offset, length, and file access.

            buffer: The buffer to contain the unmanaged memory stream.

            offset: The byte position in the buffer at which to start the unmanaged memory stream.

            length: The length of the unmanaged memory stream.

            access: The mode of file access to the unmanaged memory stream.
        """
        ...
    @staticmethod  # known case of __new__
    def __new__(cls, *__args):
        """
        __new__(cls: type)

        __new__(cls: type, buffer: SafeBuffer, offset: Int64, length: Int64)

        __new__(cls: type, buffer: SafeBuffer, offset: Int64, length: Int64, access: FileAccess)

        __new__(cls: type, pointer: Byte*, length: Int64)

        __new__(cls: type, pointer: Byte*, length: Int64, capacity: Int64, access: FileAccess)
        """
        ...
    @property
    def CanRead(self):
        """
        Gets a value indicating whether a stream supports reading.

        Get: CanRead(self: UnmanagedMemoryStream) -> bool
        """
        ...
    @property
    def CanSeek(self):
        """
        Gets a value indicating whether a stream supports seeking.

        Get: CanSeek(self: UnmanagedMemoryStream) -> bool
        """
        ...
    @property
    def CanWrite(self):
        """
        Gets a value indicating whether a stream supports writing.

        Get: CanWrite(self: UnmanagedMemoryStream) -> bool
        """
        ...
    @property
    def Capacity(self):
        """
        Gets the stream length (size) or the total amount of memory assigned to a stream (capacity).

        Get: Capacity(self: UnmanagedMemoryStream) -> Int64
        """
        ...
    @property
    def Length(self):
        """
        Gets the length of the data in a stream.

        Get: Length(self: UnmanagedMemoryStream) -> Int64
        """
        ...
    @property
    def Position(self):
        """
        Gets or sets the current position in a stream.

        Get: Position(self: UnmanagedMemoryStream) -> Int64

        Set: Position(self: UnmanagedMemoryStream) = value
        """
        ...
    @property
    def PositionPointer(self):
        """
        Gets or sets a byte pointer to a stream based on the current position in the stream.

        Get: PositionPointer(self: UnmanagedMemoryStream) -> Byte*

        Set: PositionPointer(self: UnmanagedMemoryStream) = value
        """
        ...

class WaitForChangedResult:  # skipped bases: <type 'object'>
    """Contains information on the change that occurred."""

    @property
    def ChangeType(self):
        """
        Gets or sets the type of change that occurred.

        Get: ChangeType(self: WaitForChangedResult) -> WatcherChangeTypes

        Set: ChangeType(self: WaitForChangedResult) = value
        """
        ...
    @property
    def Name(self):
        """
        Gets or sets the name of the file or directory that changed.

        Get: Name(self: WaitForChangedResult) -> str

        Set: Name(self: WaitForChangedResult) = value
        """
        ...
    @property
    def OldName(self):
        """
        Gets or sets the original name of the file or directory that was renamed.

        Get: OldName(self: WaitForChangedResult) -> str

        Set: OldName(self: WaitForChangedResult) = value
        """
        ...
    @property
    def TimedOut(self):
        """
        Gets or sets a value indicating whether the wait operation timed out.

        Get: TimedOut(self: WaitForChangedResult) -> bool

        Set: TimedOut(self: WaitForChangedResult) = value
        """
        ...

class WatcherChangeTypes(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Changes that might occur to a file or directory.

    enum (flags) WatcherChangeTypes, values: All (15), Changed (4), Created (1), Deleted (2), Renamed (8)
    """

    All = None
    Changed = None
    Created = None
    Deleted = None
    Renamed = None
    value__ = None

# variables with complex values
