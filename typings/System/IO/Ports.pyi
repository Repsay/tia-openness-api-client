# encoding: utf-8
# module System.IO.Ports calls itself Ports
# from System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class Handshake(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies the control protocol used in establishing a serial port communication for a System.IO.Ports.SerialPort object.

    enum Handshake, values: None (0), RequestToSend (2), RequestToSendXOnXOff (3), XOnXOff (1)
    """

    RequestToSend = None
    RequestToSendXOnXOff = None
    value__ = None
    XOnXOff = None

class Parity(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies the parity bit for a System.IO.Ports.SerialPort object.

    enum Parity, values: Even (2), Mark (3), None (0), Odd (1), Space (4)
    """

    Even = None
    Mark = None

    Odd = None
    Space = None
    value__ = None

class SerialData(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies the type of character that was received on the serial port of the System.IO.Ports.SerialPort object.

    enum SerialData, values: Chars (1), Eof (2)
    """

    Chars = None
    Eof = None
    value__ = None

class SerialDataReceivedEventArgs(EventArgs):
    """Provides data for the System.IO.Ports.SerialPort.DataReceived event."""

    @property
    def EventType(self):
        """
        Gets or sets the event type.

        Get: EventType(self: SerialDataReceivedEventArgs) -> SerialData
        """
        ...

class SerialDataReceivedEventHandler(MulticastDelegate):  # skipped bases: <type 'ICloneable'>, <type 'ISerializable'>
    """
    Represents the method that will handle the System.IO.Ports.SerialPort.DataReceived event of a System.IO.Ports.SerialPort object.

    SerialDataReceivedEventHandler(object: object, method: IntPtr)
    """

    def BeginInvoke(self, sender, e, callback, object):
        """BeginInvoke(self: SerialDataReceivedEventHandler, sender: object, e: SerialDataReceivedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult"""
        ...
    def EndInvoke(self, result):
        """EndInvoke(self: SerialDataReceivedEventHandler, result: IAsyncResult)"""
        ...
    def Invoke(self, sender, e):
        """Invoke(self: SerialDataReceivedEventHandler, sender: object, e: SerialDataReceivedEventArgs)"""
        ...

class SerialError(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies errors that occur on the System.IO.Ports.SerialPort object.

    enum SerialError, values: Frame (8), Overrun (2), RXOver (1), RXParity (4), TXFull (256)
    """

    Frame = None
    Overrun = None
    RXOver = None
    RXParity = None
    TXFull = None
    value__ = None

class SerialErrorReceivedEventArgs(EventArgs):
    """Prepares data for the System.IO.Ports.SerialPort.ErrorReceived event."""

    @property
    def EventType(self):
        """
        Gets or sets the event type.

        Get: EventType(self: SerialErrorReceivedEventArgs) -> SerialError
        """
        ...

class SerialErrorReceivedEventHandler(MulticastDelegate):  # skipped bases: <type 'ICloneable'>, <type 'ISerializable'>
    """
    Represents the method that will handle the System.IO.Ports.SerialPort.ErrorReceived event of a System.IO.Ports.SerialPort object.

    SerialErrorReceivedEventHandler(object: object, method: IntPtr)
    """

    def BeginInvoke(self, sender, e, callback, object):
        """BeginInvoke(self: SerialErrorReceivedEventHandler, sender: object, e: SerialErrorReceivedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult"""
        ...
    def EndInvoke(self, result):
        """EndInvoke(self: SerialErrorReceivedEventHandler, result: IAsyncResult)"""
        ...
    def Invoke(self, sender, e):
        """Invoke(self: SerialErrorReceivedEventHandler, sender: object, e: SerialErrorReceivedEventArgs)"""
        ...

class SerialPinChange(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies the type of change that occurred on the System.IO.Ports.SerialPort object.

    enum SerialPinChange, values: Break (64), CDChanged (32), CtsChanged (8), DsrChanged (16), Ring (256)
    """

    Break = None
    CDChanged = None
    CtsChanged = None
    DsrChanged = None
    Ring = None
    value__ = None

class SerialPinChangedEventArgs(EventArgs):
    """Provides data for the System.IO.Ports.SerialPort.PinChanged event."""

    @property
    def EventType(self):
        """
        Gets or sets the event type.

        Get: EventType(self: SerialPinChangedEventArgs) -> SerialPinChange
        """
        ...

class SerialPinChangedEventHandler(MulticastDelegate):  # skipped bases: <type 'ICloneable'>, <type 'ISerializable'>
    """
    Represents the method that will handle the System.IO.Ports.SerialPort.PinChanged event of a System.IO.Ports.SerialPort object.

    SerialPinChangedEventHandler(object: object, method: IntPtr)
    """

    def BeginInvoke(self, sender, e, callback, object):
        """BeginInvoke(self: SerialPinChangedEventHandler, sender: object, e: SerialPinChangedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult"""
        ...
    def EndInvoke(self, result):
        """EndInvoke(self: SerialPinChangedEventHandler, result: IAsyncResult)"""
        ...
    def Invoke(self, sender, e):
        """Invoke(self: SerialPinChangedEventHandler, sender: object, e: SerialPinChangedEventArgs)"""
        ...

class SerialPort(Component):  # skipped bases: <type 'IComponent'>, <type 'IDisposable'>
    """
    Represents a serial port resource.To browse the .NET Framework source code for this type, see the Reference Source.

    SerialPort(container: IContainer)

    SerialPort()

    SerialPort(portName: str)

    SerialPort(portName: str, baudRate: int)

    SerialPort(portName: str, baudRate: int, parity: Parity)

    SerialPort(portName: str, baudRate: int, parity: Parity, dataBits: int)

    SerialPort(portName: str, baudRate: int, parity: Parity, dataBits: int, stopBits: StopBits)
    """

    def Close(self):
        """
        Close(self: SerialPort)

            Closes the port connection, sets the System.IO.Ports.SerialPort.IsOpen property to lse, and disposes of the internal System.IO.Stream object.
        """
        ...
    def DiscardInBuffer(self):
        """
        DiscardInBuffer(self: SerialPort)

            Discards data from the serial driver's receive buffer.
        """
        ...
    def DiscardOutBuffer(self):
        """
        DiscardOutBuffer(self: SerialPort)

            Discards data from the serial driver's transmit buffer.
        """
        ...
    @staticmethod
    def GetPortNames():
        """
        GetPortNames() -> Array[str]

            Gets an array of serial port names for the current computer.

            Returns: An array of serial port names for the current computer.
        """
        ...
    def Open(self):
        """
        Open(self: SerialPort)

            Opens a new serial port connection.
        """
        ...
    def Read(self, buffer, offset, count):
        """
        Read(self: SerialPort, buffer: Array[Byte], offset: int, count: int) -> int

            Reads a number of bytes from the System.IO.Ports.SerialPort input buffer and writes those bytes into a byte array at the specified offset.

            buffer: The byte array to write the input to.

            offset: The offset in buffer at which to write the bytes.

            count: The maximum number of bytes to read. Fewer bytes are read if count is greater than the number of bytes in the input buffer.

            Returns: The number of bytes read.

        Read(self: SerialPort, buffer: Array[Char], offset: int, count: int) -> int

            Reads a number of characters from the System.IO.Ports.SerialPort input buffer and writes them into an array of characters at a given offset.

            buffer: The character array to write the input to.

            offset: The offset in buffer at which to write the characters.

            count: The maximum number of characters to read. Fewer characters are read if count is greater than the number of characters in the input buffer.

            Returns: The number of characters read.
        """
        ...
    def ReadByte(self):
        """
        ReadByte(self: SerialPort) -> int

            Synchronously reads one byte from the System.IO.Ports.SerialPort input buffer.

            Returns: The byte, cast to an System.Int32, or -1 if the end of the stream has been read.
        """
        ...
    def ReadChar(self):
        """
        ReadChar(self: SerialPort) -> int

            Synchronously reads one character from the System.IO.Ports.SerialPort input buffer.

            Returns: The character that was read.
        """
        ...
    def ReadExisting(self):
        """
        ReadExisting(self: SerialPort) -> str

            Reads all immediately available bytes, based on the encoding, in both the stream and the input buffer of the System.IO.Ports.SerialPort object.

            Returns: The contents of the stream and the input buffer of the System.IO.Ports.SerialPort object.
        """
        ...
    def ReadLine(self):
        """
        ReadLine(self: SerialPort) -> str

            Reads up to the System.IO.Ports.SerialPort.NewLine value in the input buffer.

            Returns: The contents of the input buffer up to the first occurrence of a System.IO.Ports.SerialPort.NewLine value.
        """
        ...
    def ReadTo(self, value):
        """
        ReadTo(self: SerialPort, value: str) -> str

            Reads a string up to the specified value in the input buffer.

            value: A value that indicates where the read operation stops.

            Returns: The contents of the input buffer up to the specified value.
        """
        ...
    def Write(self, *__args):
        """
        Write(self: SerialPort, text: str)

            Writes the specified string to the serial port.

            text: The string for output.

        Write(self: SerialPort, buffer: Array[Char], offset: int, count: int)

            Writes a specified number of characters to the serial port using data from a buffer.

            buffer: The character array that contains the data to write to the port.

            offset: The zero-based byte offset in the buffer parameter at which to begin copying bytes to the port.

            count: The number of characters to write.

        Write(self: SerialPort, buffer: Array[Byte], offset: int, count: int)

            Writes a specified number of bytes to the serial port using data from a buffer.

            buffer: The byte array that contains the data to write to the port.

            offset: The zero-based byte offset in the buffer parameter at which to begin copying bytes to the port.

            count: The number of bytes to write.
        """
        ...
    def WriteLine(self, text):
        """
        WriteLine(self: SerialPort, text: str)

            Writes the specified string and the System.IO.Ports.SerialPort.NewLine value to the output buffer.

            text: The string to write to the output buffer.
        """
        ...
    @staticmethod  # known case of __new__
    def __new__(cls, *__args):
        """
        __new__(cls: type, container: IContainer)

        __new__(cls: type)

        __new__(cls: type, portName: str)

        __new__(cls: type, portName: str, baudRate: int)

        __new__(cls: type, portName: str, baudRate: int, parity: Parity)

        __new__(cls: type, portName: str, baudRate: int, parity: Parity, dataBits: int)

        __new__(cls: type, portName: str, baudRate: int, parity: Parity, dataBits: int, stopBits: StopBits)
        """
        ...
    @property
    def BaseStream(self):
        """
        Gets the underlying System.IO.Stream object for a System.IO.Ports.SerialPort object.

        Get: BaseStream(self: SerialPort) -> Stream
        """
        ...
    @property
    def BaudRate(self):
        """
        Gets or sets the serial baud rate.

        Get: BaudRate(self: SerialPort) -> int

        Set: BaudRate(self: SerialPort) = value
        """
        ...
    @property
    def BreakState(self):
        """
        Gets or sets the break signal state.

        Get: BreakState(self: SerialPort) -> bool

        Set: BreakState(self: SerialPort) = value
        """
        ...
    @property
    def BytesToRead(self):
        """
        Gets the number of bytes of data in the receive buffer.

        Get: BytesToRead(self: SerialPort) -> int
        """
        ...
    @property
    def BytesToWrite(self):
        """
        Gets the number of bytes of data in the send buffer.

        Get: BytesToWrite(self: SerialPort) -> int
        """
        ...
    @property
    def CanRaiseEvents(self):
        """Gets a value indicating whether the component can raise an event."""
        ...
    @property
    def CDHolding(self):
        """
        Gets the state of the Carrier Detect line for the port.

        Get: CDHolding(self: SerialPort) -> bool
        """
        ...
    @property
    def CtsHolding(self):
        """
        Gets the state of the Clear-to-Send line.

        Get: CtsHolding(self: SerialPort) -> bool
        """
        ...
    @property
    def DataBits(self):
        """
        Gets or sets the standard length of data bits per byte.

        Get: DataBits(self: SerialPort) -> int

        Set: DataBits(self: SerialPort) = value
        """
        ...
    @property
    def DesignMode(self):
        """Gets a value that indicates whether the System.ComponentModel.Component is currently in design mode."""
        ...
    @property
    def DiscardNull(self):
        """
        Gets or sets a value indicating whether null bytes are ignored when transmitted between the port and the receive buffer.

        Get: DiscardNull(self: SerialPort) -> bool

        Set: DiscardNull(self: SerialPort) = value
        """
        ...
    @property
    def DsrHolding(self):
        """
        Gets the state of the Data Set Ready (DSR) signal.

        Get: DsrHolding(self: SerialPort) -> bool
        """
        ...
    @property
    def DtrEnable(self):
        """
        Gets or sets a value that enables the Data Terminal Ready (DTR) signal during serial communication.

        Get: DtrEnable(self: SerialPort) -> bool

        Set: DtrEnable(self: SerialPort) = value
        """
        ...
    @property
    def Encoding(self):
        """
        Gets or sets the byte encoding for pre- and post-transmission conversion of text.

        Get: Encoding(self: SerialPort) -> Encoding

        Set: Encoding(self: SerialPort) = value
        """
        ...
    @property
    def Events(self):
        """Gets the list of event handlers that are attached to this System.ComponentModel.Component."""
        ...
    @property
    def Handshake(self):
        """
        Gets or sets the handshaking protocol for serial port transmission of data using a value from System.IO.Ports.Handshake.

        Get: Handshake(self: SerialPort) -> Handshake

        Set: Handshake(self: SerialPort) = value
        """
        ...
    @property
    def IsOpen(self):
        """
        Gets a value indicating the open or closed status of the System.IO.Ports.SerialPort object.

        Get: IsOpen(self: SerialPort) -> bool
        """
        ...
    @property
    def NewLine(self):
        """
        Gets or sets the value used to interpret the end of a call to the System.IO.Ports.SerialPort.ReadLine and System.IO.Ports.SerialPort.WriteLine(System.String) methods.

        Get: NewLine(self: SerialPort) -> str

        Set: NewLine(self: SerialPort) = value
        """
        ...
    @property
    def Parity(self):
        """
        Gets or sets the parity-checking protocol.

        Get: Parity(self: SerialPort) -> Parity

        Set: Parity(self: SerialPort) = value
        """
        ...
    @property
    def ParityReplace(self):
        """
        Gets or sets the byte that replaces invalid bytes in a data stream when a parity error occurs.

        Get: ParityReplace(self: SerialPort) -> Byte

        Set: ParityReplace(self: SerialPort) = value
        """
        ...
    @property
    def PortName(self):
        """
        Gets or sets the port for communications, including but not limited to all available COM ports.

        Get: PortName(self: SerialPort) -> str

        Set: PortName(self: SerialPort) = value
        """
        ...
    @property
    def ReadBufferSize(self):
        """
        Gets or sets the size of the System.IO.Ports.SerialPort input buffer.

        Get: ReadBufferSize(self: SerialPort) -> int

        Set: ReadBufferSize(self: SerialPort) = value
        """
        ...
    @property
    def ReadTimeout(self):
        """
        Gets or sets the number of milliseconds before a time-out occurs when a read operation does not finish.

        Get: ReadTimeout(self: SerialPort) -> int

        Set: ReadTimeout(self: SerialPort) = value
        """
        ...
    @property
    def ReceivedBytesThreshold(self):
        """
        Gets or sets the number of bytes in the internal input buffer before a System.IO.Ports.SerialPort.DataReceived event occurs.

        Get: ReceivedBytesThreshold(self: SerialPort) -> int

        Set: ReceivedBytesThreshold(self: SerialPort) = value
        """
        ...
    @property
    def RtsEnable(self):
        """
        Gets or sets a value indicating whether the Request to Send (RTS) signal is enabled during serial communication.

        Get: RtsEnable(self: SerialPort) -> bool

        Set: RtsEnable(self: SerialPort) = value
        """
        ...
    @property
    def StopBits(self):
        """
        Gets or sets the standard number of stopbits per byte.

        Get: StopBits(self: SerialPort) -> StopBits

        Set: StopBits(self: SerialPort) = value
        """
        ...
    @property
    def WriteBufferSize(self):
        """
        Gets or sets the size of the serial port output buffer.

        Get: WriteBufferSize(self: SerialPort) -> int

        Set: WriteBufferSize(self: SerialPort) = value
        """
        ...
    @property
    def WriteTimeout(self):
        """
        Gets or sets the number of milliseconds before a time-out occurs when a write operation does not finish.

        Get: WriteTimeout(self: SerialPort) -> int

        Set: WriteTimeout(self: SerialPort) = value
        """
        ...
    DataReceived = None
    ErrorReceived = None
    InfiniteTimeout = -1
    PinChanged = None

class StopBits(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies the number of stop bits used on the System.IO.Ports.SerialPort object.

    enum StopBits, values: None (0), One (1), OnePointFive (3), Two (2)
    """

    One = None
    OnePointFive = None
    Two = None
    value__ = None
