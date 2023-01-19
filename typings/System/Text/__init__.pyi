# encoding: utf-8
# module System.Text calls itself Text
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class Encoding(object, ICloneable):
    """Represents a character encoding.To browse the .NET Framework source code for this type, see the Reference Source."""

    @staticmethod
    def Convert(srcEncoding, dstEncoding, bytes, index=None, count=None):
        """
        Convert(srcEncoding: Encoding, dstEncoding: Encoding, bytes: Array[Byte]) -> Array[Byte]

            Converts an entire byte array from one encoding to another.

            srcEncoding: The encoding format of bytes.

            dstEncoding: The target encoding format.

            bytes: The bytes to convert.

            Returns: An array of type System.Byte containing the results of converting bytes from srcEncoding to dstEncoding.

        Convert(srcEncoding: Encoding, dstEncoding: Encoding, bytes: Array[Byte], index: int, count: int) -> Array[Byte]

            Converts a range of bytes in a byte array from one encoding to another.

            srcEncoding: The encoding of the source array, bytes.

            dstEncoding: The encoding of the output array.

            bytes: The array of bytes to convert.

            index: The index of the first element of bytes to convert.

            count: The number of bytes to convert.

            Returns: An array of type System.Byte containing the result of converting a range of bytes in bytes from srcEncoding to dstEncoding.
        """
        ...
    def Equals(self, value):
        """
        Equals(self: Encoding, value: object) -> bool

            Determines whether the specified System.Object is equal to the current instance.

            value: The System.Object to compare with the current instance.

            Returns: ue if value is an instance of System.Text.Encoding and is equal to the current instance; otherwise, lse.
        """
        ...
    def GetByteCount(self, *__args):
        """
        GetByteCount(self: Encoding, chars: Array[Char]) -> int

            When overridden in a derived class, calculates the number of bytes produced by encoding all the characters in the specified character array.

            chars: The character array containing the characters to encode.

            Returns: The number of bytes produced by encoding all the characters in the specified character array.

        GetByteCount(self: Encoding, s: str) -> int

            When overridden in a derived class, calculates the number of bytes produced by encoding the characters in the specified string.

            s: The string containing the set of characters to encode.

            Returns: The number of bytes produced by encoding the specified characters.

        GetByteCount(self: Encoding, chars: Char*, count: int) -> int

            When overridden in a derived class, calculates the number of bytes produced by encoding a set of characters starting at the specified character pointer.

            chars: A pointer to the first character to encode.

            count: The number of characters to encode.

            Returns: The number of bytes produced by encoding the specified characters.

        GetByteCount(self: Encoding, chars: Array[Char], index: int, count: int) -> int

            When overridden in a derived class, calculates the number of bytes produced by encoding a set of characters from the specified character array.

            chars: The character array containing the set of characters to encode.

            index: The index of the first character to encode.

            count: The number of characters to encode.

            Returns: The number of bytes produced by encoding the specified characters.
        """
        ...
    def GetBytes(self, *__args):
        """
        GetBytes(self: Encoding, chars: Array[Char]) -> Array[Byte]

            When overridden in a derived class, encodes all the characters in the specified character array into a sequence of bytes.

            chars: The character array containing the characters to encode.

            Returns: A byte array containing the results of encoding the specified set of characters.

        GetBytes(self: Encoding, chars: Array[Char], index: int, count: int) -> Array[Byte]

            When overridden in a derived class, encodes a set of characters from the specified character array into a sequence of bytes.

            chars: The character array containing the set of characters to encode.

            index: The index of the first character to encode.

            count: The number of characters to encode.

            Returns: A byte array containing the results of encoding the specified set of characters.

        GetBytes(self: Encoding, s: str) -> Array[Byte]

            When overridden in a derived class, encodes all the characters in the specified string into a sequence of bytes.

            s: The string containing the characters to encode.

            Returns: A byte array containing the results of encoding the specified set of characters.

        GetBytes(self: Encoding, s: str, charIndex: int, charCount: int, bytes: Array[Byte], byteIndex: int) -> int

            When overridden in a derived class, encodes a set of characters from the specified string into the specified byte array.

            s: The string containing the set of characters to encode.

            charIndex: The index of the first character to encode.

            charCount: The number of characters to encode.

            bytes: The byte array to contain the resulting sequence of bytes.

            byteIndex: The index at which to start writing the resulting sequence of bytes.

            Returns: The actual number of bytes written into bytes.

        GetBytes(self: Encoding, chars: Array[Char], charIndex: int, charCount: int, bytes: Array[Byte], byteIndex: int) -> int

            When overridden in a derived class, encodes a set of characters from the specified character array into the specified byte array.

            chars: The character array containing the set of characters to encode.

            charIndex: The index of the first character to encode.

            charCount: The number of characters to encode.

            bytes: The byte array to contain the resulting sequence of bytes.

            byteIndex: The index at which to start writing the resulting sequence of bytes.

            Returns: The actual number of bytes written into bytes.

        GetBytes(self: Encoding, chars: Char*, charCount: int, bytes: Byte*, byteCount: int) -> int

            When overridden in a derived class, encodes a set of characters starting at the specified character pointer into a sequence of bytes that are stored starting at the

             specified byte pointer.

            chars: A pointer to the first character to encode.

            charCount: The number of characters to encode.

            bytes: A pointer to the location at which to start writing the resulting sequence of bytes.

            byteCount: The maximum number of bytes to write.

            Returns: The actual number of bytes written at the location indicated by the bytes parameter.
        """
        ...
    def GetCharCount(self, bytes, *__args):
        """
        GetCharCount(self: Encoding, bytes: Array[Byte]) -> int

            When overridden in a derived class, calculates the number of characters produced by decoding all the bytes in the specified byte array.

            bytes: The byte array containing the sequence of bytes to decode.

            Returns: The number of characters produced by decoding the specified sequence of bytes.

        GetCharCount(self: Encoding, bytes: Byte*, count: int) -> int

            When overridden in a derived class, calculates the number of characters produced by decoding a sequence of bytes starting at the specified byte pointer.

            bytes: A pointer to the first byte to decode.

            count: The number of bytes to decode.

            Returns: The number of characters produced by decoding the specified sequence of bytes.

        GetCharCount(self: Encoding, bytes: Array[Byte], index: int, count: int) -> int

            When overridden in a derived class, calculates the number of characters produced by decoding a sequence of bytes from the specified byte array.

            bytes: The byte array containing the sequence of bytes to decode.

            index: The index of the first byte to decode.

            count: The number of bytes to decode.

            Returns: The number of characters produced by decoding the specified sequence of bytes.
        """
        ...
    def GetChars(self, bytes, *__args):
        """
        GetChars(self: Encoding, bytes: Array[Byte]) -> Array[Char]

            When overridden in a derived class, decodes all the bytes in the specified byte array into a set of characters.

            bytes: The byte array containing the sequence of bytes to decode.

            Returns: A character array containing the results of decoding the specified sequence of bytes.

        GetChars(self: Encoding, bytes: Array[Byte], index: int, count: int) -> Array[Char]

            When overridden in a derived class, decodes a sequence of bytes from the specified byte array into a set of characters.

            bytes: The byte array containing the sequence of bytes to decode.

            index: The index of the first byte to decode.

            count: The number of bytes to decode.

            Returns: A character array containing the results of decoding the specified sequence of bytes.

        GetChars(self: Encoding, bytes: Array[Byte], byteIndex: int, byteCount: int, chars: Array[Char], charIndex: int) -> int

            When overridden in a derived class, decodes a sequence of bytes from the specified byte array into the specified character array.

            bytes: The byte array containing the sequence of bytes to decode.

            byteIndex: The index of the first byte to decode.

            byteCount: The number of bytes to decode.

            chars: The character array to contain the resulting set of characters.

            charIndex: The index at which to start writing the resulting set of characters.

            Returns: The actual number of characters written into chars.

        GetChars(self: Encoding, bytes: Byte*, byteCount: int, chars: Char*, charCount: int) -> int

            When overridden in a derived class, decodes a sequence of bytes starting at the specified byte pointer into a set of characters that are stored starting at the

             specified character pointer.

            bytes: A pointer to the first byte to decode.

            byteCount: The number of bytes to decode.

            chars: A pointer to the location at which to start writing the resulting set of characters.

            charCount: The maximum number of characters to write.

            Returns: The actual number of characters written at the location indicated by the chars parameter.
        """
        ...
    def GetDecoder(self):
        """
        GetDecoder(self: Encoding) -> Decoder

            When overridden in a derived class, obtains a decoder that converts an encoded sequence of bytes into a sequence of characters.

            Returns: A System.Text.Decoder that converts an encoded sequence of bytes into a sequence of characters.
        """
        ...
    def GetEncoder(self):
        """
        GetEncoder(self: Encoding) -> Encoder

            When overridden in a derived class, obtains an encoder that converts a sequence of Unicode characters into an encoded sequence of bytes.

            Returns: A System.Text.Encoder that converts a sequence of Unicode characters into an encoded sequence of bytes.
        """
        ...
    @staticmethod
    def GetEncoding(*__args):
        """
        GetEncoding(codepage: int) -> Encoding

            Returns the encoding associated with the specified code page identifier.

            codepage: The code page identifier of the preferred encoding. Possible values are listed in the Code Page column of the table that appears in the System.Text.Encoding class

             topic.-or- 0 (zero), to use the default encoding.

            Returns: The encoding that is associated with the specified code page.

        GetEncoding(codepage: int, encoderFallback: EncoderFallback, decoderFallback: DecoderFallback) -> Encoding

            Returns the encoding associated with the specified code page identifier. Parameters specify an error handler for characters that cannot be encoded and byte sequences

             that cannot be decoded.

            codepage: The code page identifier of the preferred encoding. Possible values are listed in the Code Page column of the table that appears in the System.Text.Encoding class

             topic.-or- 0 (zero), to use the default encoding.

            encoderFallback: An object that provides an error-handling procedure when a character cannot be encoded with the current encoding.

            decoderFallback: An object that provides an error-handling procedure when a byte sequence cannot be decoded with the current encoding.

            Returns: The encoding that is associated with the specified code page.

        GetEncoding(name: str) -> Encoding

            Returns the encoding associated with the specified code page name.

            name: The code page name of the preferred encoding. Any value returned by the System.Text.Encoding.WebName property is valid. Possible values are listed in the Name column

             of the table that appears in the System.Text.Encoding class topic.

            Returns: The encoding  associated with the specified code page.

        GetEncoding(name: str, encoderFallback: EncoderFallback, decoderFallback: DecoderFallback) -> Encoding

            Returns the encoding associated with the specified code page name. Parameters specify an error handler for characters that cannot be encoded and byte sequences that

             cannot be decoded.

            name: The code page name of the preferred encoding. Any value returned by the System.Text.Encoding.WebName property is valid. Possible values are listed in the Name column

             of the table that appears in the System.Text.Encoding class topic.

            encoderFallback: An object that provides an error-handling procedure when a character cannot be encoded with the current encoding.

            decoderFallback: An object that provides an error-handling procedure when a byte sequence cannot be decoded with the current encoding.

            Returns: The encoding that is associated with the specified code page.
        """
        ...
    @staticmethod
    def GetEncodings():
        """
        GetEncodings() -> Array[EncodingInfo]

            Returns an array that contains all encodings.

            Returns: An array that contains all encodings.
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: Encoding) -> int

            Returns the hash code for the current instance.

            Returns: The hash code for the current instance.
        """
        ...
    def GetMaxByteCount(self, charCount):
        """
        GetMaxByteCount(self: Encoding, charCount: int) -> int

            When overridden in a derived class, calculates the maximum number of bytes produced by encoding the specified number of characters.

            charCount: The number of characters to encode.

            Returns: The maximum number of bytes produced by encoding the specified number of characters.
        """
        ...
    def GetMaxCharCount(self, byteCount):
        """
        GetMaxCharCount(self: Encoding, byteCount: int) -> int

            When overridden in a derived class, calculates the maximum number of characters produced by decoding the specified number of bytes.

            byteCount: The number of bytes to decode.

            Returns: The maximum number of characters produced by decoding the specified number of bytes.
        """
        ...
    def GetPreamble(self):
        """
        GetPreamble(self: Encoding) -> Array[Byte]

            When overridden in a derived class, returns a sequence of bytes that specifies the encoding used.

            Returns: A byte array containing a sequence of bytes that specifies the encoding used.-or- A byte array of length zero, if a preamble is not required.
        """
        ...
    def GetString(self, bytes, *__args):
        """
        GetString(self: Encoding, bytes: Array[Byte]) -> str

            When overridden in a derived class, decodes all the bytes in the specified byte array into a string.

            bytes: The byte array containing the sequence of bytes to decode.

            Returns: A string that contains the results of decoding the specified sequence of bytes.

        GetString(self: Encoding, bytes: Array[Byte], index: int, count: int) -> str

            When overridden in a derived class, decodes a sequence of bytes from the specified byte array into a string.

            bytes: The byte array containing the sequence of bytes to decode.

            index: The index of the first byte to decode.

            count: The number of bytes to decode.

            Returns: A string that contains the results of decoding the specified sequence of bytes.

        GetString(self: Encoding, bytes: Byte*, byteCount: int) -> str

            When overridden in a derived class, decodes a specified number of bytes starting at a specified address into a string.

            bytes: A pointer to a byte array.

            byteCount: The number of bytes to decode.

            Returns: A string that contains the results of decoding the specified sequence of bytes.
        """
        ...
    def IsAlwaysNormalized(self, form=None):
        """
        IsAlwaysNormalized(self: Encoding) -> bool

            Gets a value indicating whether the current encoding is always normalized, using the default normalization form.

            Returns: ue if the current System.Text.Encoding is always normalized; otherwise, lse. The default is lse.

        IsAlwaysNormalized(self: Encoding, form: NormalizationForm) -> bool

            When overridden in a derived class, gets a value indicating whether the current encoding is always normalized, using the specified normalization form.

            form: One of the System.Text.NormalizationForm values.

            Returns: ue if the current System.Text.Encoding object is always normalized using the specified System.Text.NormalizationForm value; otherwise, lse. The default is lse.
        """
        ...
    @staticmethod
    def RegisterProvider(provider):
        """
        RegisterProvider(provider: EncodingProvider)

            Registers an encoding provider.

            provider: A subclass of System.Text.EncodingProvider that provides access to additional character encodings.
        """
        ...
    def __eq__(self, *args):  # cannot find CLR method
        """x.__eq__(y) <==> x==y"""
        ...
    def __ne__(self, *args): ...
    @property
    def BodyName(self):
        """
        When overridden in a derived class, gets a name for the current encoding that can be used with mail agent body tags.

        Get: BodyName(self: Encoding) -> str
        """
        ...
    @property
    def CodePage(self):
        """
        When overridden in a derived class, gets the code page identifier of the current System.Text.Encoding.

        Get: CodePage(self: Encoding) -> int
        """
        ...
    @property
    def DecoderFallback(self):
        """
        Gets or sets the System.Text.DecoderFallback object for the current System.Text.Encoding object.

        Get: DecoderFallback(self: Encoding) -> DecoderFallback

        Set: DecoderFallback(self: Encoding) = value
        """
        ...
    @property
    def EncoderFallback(self):
        """
        Gets or sets the System.Text.EncoderFallback object for the current System.Text.Encoding object.

        Get: EncoderFallback(self: Encoding) -> EncoderFallback

        Set: EncoderFallback(self: Encoding) = value
        """
        ...
    @property
    def EncodingName(self):
        """
        When overridden in a derived class, gets the human-readable description of the current encoding.

        Get: EncodingName(self: Encoding) -> str
        """
        ...
    @property
    def HeaderName(self):
        """
        When overridden in a derived class, gets a name for the current encoding that can be used with mail agent header tags.

        Get: HeaderName(self: Encoding) -> str
        """
        ...
    @property
    def IsBrowserDisplay(self):
        """
        When overridden in a derived class, gets a value indicating whether the current encoding can be used by browser clients for displaying content.

        Get: IsBrowserDisplay(self: Encoding) -> bool
        """
        ...
    @property
    def IsBrowserSave(self):
        """
        When overridden in a derived class, gets a value indicating whether the current encoding can be used by browser clients for saving content.

        Get: IsBrowserSave(self: Encoding) -> bool
        """
        ...
    @property
    def IsMailNewsDisplay(self):
        """
        When overridden in a derived class, gets a value indicating whether the current encoding can be used by mail and news clients for displaying content.

        Get: IsMailNewsDisplay(self: Encoding) -> bool
        """
        ...
    @property
    def IsMailNewsSave(self):
        """
        When overridden in a derived class, gets a value indicating whether the current encoding can be used by mail and news clients for saving content.

        Get: IsMailNewsSave(self: Encoding) -> bool
        """
        ...
    @property
    def IsReadOnly(self):
        """
        When overridden in a derived class, gets a value indicating whether the current encoding is read-only.

        Get: IsReadOnly(self: Encoding) -> bool
        """
        ...
    @property
    def IsSingleByte(self):
        """
        When overridden in a derived class, gets a value indicating whether the current encoding uses single-byte code points.

        Get: IsSingleByte(self: Encoding) -> bool
        """
        ...
    @property
    def WebName(self):
        """
        When overridden in a derived class, gets the name registered with the Internet Assigned Numbers Authority (IANA) for the current encoding.

        Get: WebName(self: Encoding) -> str
        """
        ...
    @property
    def WindowsCodePage(self):
        """
        When overridden in a derived class, gets the Windows operating system code page that most closely corresponds to the current encoding.

        Get: WindowsCodePage(self: Encoding) -> int
        """
        ...
    ASCII = None
    BigEndianUnicode = None
    Default = None
    Unicode = None
    UTF32 = None
    UTF7 = None
    UTF8 = None

class ASCIIEncoding(Encoding):  # skipped bases: <type 'ICloneable'>
    """
    Represents an ASCII character encoding of Unicode characters.

    ASCIIEncoding()
    """

    @property
    def IsSingleByte(self):
        """
        Gets a value indicating whether the current encoding uses single-byte code points.

        Get: IsSingleByte(self: ASCIIEncoding) -> bool
        """
        ...

class Decoder:  # skipped bases: <type 'object'>
    """Converts a sequence of encoded bytes into a set of characters."""

    def Convert(self, bytes, *__args):
        """
        Convert(self: Decoder, bytes: Array[Byte], byteIndex: int, byteCount: int, chars: Array[Char], charIndex: int, charCount: int, flush: bool) -> (int, int, bool)

            Converts an array of encoded bytes to UTF-16 encoded characters and stores the result in a character array.

            bytes: A byte array to convert.

            byteIndex: The first element of bytes to convert.

            byteCount: The number of elements of bytes to convert.

            chars: An array to store the converted characters.

            charIndex: The first element of chars in which data is stored.

            charCount: The maximum number of elements of chars to use in the conversion.

            flush: ue to indicate that no further data is to be converted; otherwise, lse.

        Convert(self: Decoder, bytes: Byte*, byteCount: int, chars: Char*, charCount: int, flush: bool) -> (int, int, bool)

            Converts a buffer of encoded bytes to UTF-16 encoded characters and stores the result in another buffer.

            bytes: The address of a buffer that contains the byte sequences to convert.

            byteCount: The number of bytes in bytes to convert.

            chars: The address of a buffer to store the converted characters.

            charCount: The maximum number of characters in chars to use in the conversion.

            flush: ue to indicate no further data is to be converted; otherwise, lse.
        """
        ...
    def GetCharCount(self, bytes, *__args):
        """
        GetCharCount(self: Decoder, bytes: Array[Byte], index: int, count: int, flush: bool) -> int

            When overridden in a derived class, calculates the number of characters produced by decoding a sequence of bytes from the specified byte array. A parameter indicates

             whether to clear the internal state of the decoder after the calculation.

            bytes: The byte array containing the sequence of bytes to decode.

            index: The index of the first byte to decode.

            count: The number of bytes to decode.

            flush: ue to simulate clearing the internal state of the encoder after the calculation; otherwise, lse.

            Returns: The number of characters produced by decoding the specified sequence of bytes and any bytes in the internal buffer.

        GetCharCount(self: Decoder, bytes: Byte*, count: int, flush: bool) -> int

            When overridden in a derived class, calculates the number of characters produced by decoding a sequence of bytes starting at the specified byte pointer. A parameter

             indicates whether to clear the internal state of the decoder after the calculation.

            bytes: A pointer to the first byte to decode.

            count: The number of bytes to decode.

            flush: ue to simulate clearing the internal state of the encoder after the calculation; otherwise, lse.

            Returns: The number of characters produced by decoding the specified sequence of bytes and any bytes in the internal buffer.

        GetCharCount(self: Decoder, bytes: Array[Byte], index: int, count: int) -> int

            When overridden in a derived class, calculates the number of characters produced by decoding a sequence of bytes from the specified byte array.

            bytes: The byte array containing the sequence of bytes to decode.

            index: The index of the first byte to decode.

            count: The number of bytes to decode.

            Returns: The number of characters produced by decoding the specified sequence of bytes and any bytes in the internal buffer.
        """
        ...
    def GetChars(self, bytes, *__args):
        """
        GetChars(self: Decoder, bytes: Array[Byte], byteIndex: int, byteCount: int, chars: Array[Char], charIndex: int, flush: bool) -> int

            When overridden in a derived class, decodes a sequence of bytes from the specified byte array and any bytes in the internal buffer into the specified character array.

             A parameter indicates whether to clear the internal state of the decoder after the conversion.

            bytes: The byte array containing the sequence of bytes to decode.

            byteIndex: The index of the first byte to decode.

            byteCount: The number of bytes to decode.

            chars: The character array to contain the resulting set of characters.

            charIndex: The index at which to start writing the resulting set of characters.

            flush: ue to clear the internal state of the decoder after the conversion; otherwise, lse.

            Returns: The actual number of characters written into the chars parameter.

        GetChars(self: Decoder, bytes: Array[Byte], byteIndex: int, byteCount: int, chars: Array[Char], charIndex: int) -> int

            When overridden in a derived class, decodes a sequence of bytes from the specified byte array and any bytes in the internal buffer into the specified character array.

            bytes: The byte array containing the sequence of bytes to decode.

            byteIndex: The index of the first byte to decode.

            byteCount: The number of bytes to decode.

            chars: The character array to contain the resulting set of characters.

            charIndex: The index at which to start writing the resulting set of characters.

            Returns: The actual number of characters written into chars.

        GetChars(self: Decoder, bytes: Byte*, byteCount: int, chars: Char*, charCount: int, flush: bool) -> int

            When overridden in a derived class, decodes a sequence of bytes starting at the specified byte pointer and any bytes in the internal buffer into a set of characters

             that are stored starting at the specified character pointer. A parameter indicates whether to clear the internal state of the decoder after the conversion.

            bytes: A pointer to the first byte to decode.

            byteCount: The number of bytes to decode.

            chars: A pointer to the location at which to start writing the resulting set of characters.

            charCount: The maximum number of characters to write.

            flush: ue to clear the internal state of the decoder after the conversion; otherwise, lse.

            Returns: The actual number of characters written at the location indicated by the chars parameter.
        """
        ...
    def Reset(self):
        """
        Reset(self: Decoder)

            When overridden in a derived class, sets the decoder back to its initial state.
        """
        ...
    @property
    def Fallback(self):
        """
        Gets or sets a System.Text.DecoderFallback object for the current System.Text.Decoder object.

        Get: Fallback(self: Decoder) -> DecoderFallback

        Set: Fallback(self: Decoder) = value
        """
        ...
    @property
    def FallbackBuffer(self):
        """
        Gets the System.Text.DecoderFallbackBuffer object associated with the current System.Text.Decoder object.

        Get: FallbackBuffer(self: Decoder) -> DecoderFallbackBuffer
        """
        ...

class DecoderFallback:  # skipped bases: <type 'object'>
    """Provides a failure-handling mechanism, called a fallback, for an encoded input byte sequence that cannot be converted to an output character."""

    def CreateFallbackBuffer(self):
        """
        CreateFallbackBuffer(self: DecoderFallback) -> DecoderFallbackBuffer

            When overridden in a derived class, initializes a new instance of the System.Text.DecoderFallbackBuffer class.

            Returns: An object that provides a fallback buffer for a decoder.
        """
        ...
    @property
    def MaxCharCount(self):
        """
        When overridden in a derived class, gets the maximum number of characters the current System.Text.DecoderFallback object can return.

        Get: MaxCharCount(self: DecoderFallback) -> int
        """
        ...
    ExceptionFallback = None
    ReplacementFallback = None

class DecoderExceptionFallback(DecoderFallback):
    """
    Provides a failure-handling mechanism, called a fallback, for an encoded input byte sequence that cannot be converted to an input character. The fallback throws an exception instead of decoding the input byte sequence. This class cannot be inherited.

    DecoderExceptionFallback()
    """

    def Equals(self, value):
        """
        Equals(self: DecoderExceptionFallback, value: object) -> bool

            Indicates whether the current System.Text.DecoderExceptionFallback object and a specified object are equal.

            value: An object that derives from the System.Text.DecoderExceptionFallback class.

            Returns: ue if value is not ll and is a System.Text.DecoderExceptionFallback object; otherwise, lse.
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: DecoderExceptionFallback) -> int

            Retrieves the hash code for this instance.

            Returns: The return value is always the same arbitrary value, and has no special significance.
        """
        ...
    def __eq__(self, *args):  # cannot find CLR method
        """x.__eq__(y) <==> x==y"""
        ...
    def __ne__(self, *args): ...
    @property
    def MaxCharCount(self):
        """
        Gets the maximum number of characters this instance can return.

        Get: MaxCharCount(self: DecoderExceptionFallback) -> int
        """
        ...

class DecoderFallbackBuffer:  # skipped bases: <type 'object'>
    """Provides a buffer that allows a fallback handler to return an alternate string to a decoder when it cannot decode an input byte sequence."""

    def Fallback(self, bytesUnknown, index):
        """
        Fallback(self: DecoderFallbackBuffer, bytesUnknown: Array[Byte], index: int) -> bool

            When overridden in a derived class, prepares the fallback buffer to handle the specified input byte sequence.

            bytesUnknown: An input array of bytes.

            index: The index position of a byte in bytesUnknown.

            Returns: ue if the fallback buffer can process bytesUnknown; lse if the fallback buffer ignores bytesUnknown.
        """
        ...
    def GetNextChar(self):
        """
        GetNextChar(self: DecoderFallbackBuffer) -> Char

            When overridden in a derived class, retrieves the next character in the fallback buffer.

            Returns: The next character in the fallback buffer.
        """
        ...
    def MovePrevious(self):
        """
        MovePrevious(self: DecoderFallbackBuffer) -> bool

            When overridden in a derived class, causes the next call to the System.Text.DecoderFallbackBuffer.GetNextChar method to access the data buffer character position that

             is prior to the current character position.

            Returns: ue if the System.Text.DecoderFallbackBuffer.MovePrevious operation was successful; otherwise, lse.
        """
        ...
    def Reset(self):
        """
        Reset(self: DecoderFallbackBuffer)

            Initializes all data and state information pertaining to this fallback buffer.
        """
        ...
    @property
    def Remaining(self):
        """
        When overridden in a derived class, gets the number of characters in the current System.Text.DecoderFallbackBuffer object that remain to be processed.

        Get: Remaining(self: DecoderFallbackBuffer) -> int
        """
        ...

class DecoderExceptionFallbackBuffer(DecoderFallbackBuffer):
    """
    Throws System.Text.DecoderFallbackException when an encoded input byte sequence cannot be converted to a decoded output character. This class cannot be inherited.

    DecoderExceptionFallbackBuffer()
    """

    @property
    def Remaining(self):
        """
        Gets the number of characters in the current System.Text.DecoderExceptionFallbackBuffer object that remain to be processed.

        Get: Remaining(self: DecoderExceptionFallbackBuffer) -> int
        """
        ...

class DecoderFallbackException(ArgumentException):  # skipped bases: <type '_Exception'>, <type 'ISerializable'>
    """
    The exception that is thrown when a decoder fallback operation fails. This class cannot be inherited.

    DecoderFallbackException()

    DecoderFallbackException(message: str)

    DecoderFallbackException(message: str, innerException: Exception)

    DecoderFallbackException(message: str, bytesUnknown: Array[Byte], index: int)
    """

    @property
    def BytesUnknown(self):
        """
        Gets the input byte sequence that caused the exception.

        Get: BytesUnknown(self: DecoderFallbackException) -> Array[Byte]
        """
        ...
    @property
    def Index(self):
        """
        Gets the index position in the input byte sequence of the byte that caused the exception.

        Get: Index(self: DecoderFallbackException) -> int
        """
        ...
    SerializeObjectState = None

class DecoderReplacementFallback(DecoderFallback):
    """
    Provides a failure-handling mechanism, called a fallback, for an encoded input byte sequence that cannot be converted to an output character. The fallback emits a user-specified replacement string instead of a decoded input byte sequence. This class cannot be inherited.

    DecoderReplacementFallback()

    DecoderReplacementFallback(replacement: str)
    """

    def Equals(self, value):
        """
        Equals(self: DecoderReplacementFallback, value: object) -> bool

            Indicates whether the value of a specified object is equal to the System.Text.DecoderReplacementFallback object.

            value: A System.Text.DecoderReplacementFallback object.

            Returns: ue if value is a System.Text.DecoderReplacementFallback object having a System.Text.DecoderReplacementFallback.DefaultString property that is equal to the

             System.Text.DecoderReplacementFallback.DefaultString property of the current System.Text.DecoderReplacementFallback object; otherwise, lse.
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: DecoderReplacementFallback) -> int

            Retrieves the hash code for the value of the System.Text.DecoderReplacementFallback object.

            Returns: The hash code of the value of the object.
        """
        ...
    def __eq__(self, *args):  # cannot find CLR method
        """x.__eq__(y) <==> x==y"""
        ...
    @staticmethod  # known case of __new__
    def __new__(cls, replacement=None):
        """
        __new__(cls: type)

        __new__(cls: type, replacement: str)
        """
        ...
    def __ne__(self, *args): ...
    @property
    def DefaultString(self):
        """
        Gets the replacement string that is the value of the System.Text.DecoderReplacementFallback object.

        Get: DefaultString(self: DecoderReplacementFallback) -> str
        """
        ...
    @property
    def MaxCharCount(self):
        """
        Gets the number of characters in the replacement string for the System.Text.DecoderReplacementFallback object.

        Get: MaxCharCount(self: DecoderReplacementFallback) -> int
        """
        ...

class DecoderReplacementFallbackBuffer(DecoderFallbackBuffer):
    """
    Represents a substitute output string that is emitted when the original input byte sequence cannot be decoded. This class cannot be inherited.

    DecoderReplacementFallbackBuffer(fallback: DecoderReplacementFallback)
    """

    @staticmethod  # known case of __new__
    def __new__(cls, fallback):
        """__new__(cls: type, fallback: DecoderReplacementFallback)"""
        ...
    @property
    def Remaining(self):
        """
        Gets the number of characters in the replacement fallback buffer that remain to be processed.

        Get: Remaining(self: DecoderReplacementFallbackBuffer) -> int
        """
        ...

class Encoder:  # skipped bases: <type 'object'>
    """Converts a set of characters into a sequence of bytes."""

    def Convert(self, chars, *__args):
        """
        Convert(self: Encoder, chars: Array[Char], charIndex: int, charCount: int, bytes: Array[Byte], byteIndex: int, byteCount: int, flush: bool) -> (int, int, bool)

            Converts an array of Unicode characters to an encoded byte sequence and stores the result in an array of bytes.

            chars: An array of characters to convert.

            charIndex: The first element of chars to convert.

            charCount: The number of elements of chars to convert.

            bytes: An array where the converted bytes are stored.

            byteIndex: The first element of bytes in which data is stored.

            byteCount: The maximum number of elements of bytes to use in the conversion.

            flush: ue to indicate no further data is to be converted; otherwise, lse.

        Convert(self: Encoder, chars: Char*, charCount: int, bytes: Byte*, byteCount: int, flush: bool) -> (int, int, bool)

            Converts a buffer of Unicode characters to an encoded byte sequence and stores the result in another buffer.

            chars: The address of a string of UTF-16 encoded characters to convert.

            charCount: The number of characters in chars to convert.

            bytes: The address of a buffer to store the converted bytes.

            byteCount: The maximum number of bytes in bytes to use in the conversion.

            flush: ue to indicate no further data is to be converted; otherwise, lse.
        """
        ...
    def GetByteCount(self, chars, *__args):
        """
        GetByteCount(self: Encoder, chars: Char*, count: int, flush: bool) -> int

            When overridden in a derived class, calculates the number of bytes produced by encoding a set of characters starting at the specified character pointer. A parameter

             indicates whether to clear the internal state of the encoder after the calculation.

            chars: A pointer to the first character to encode.

            count: The number of characters to encode.

            flush: ue to simulate clearing the internal state of the encoder after the calculation; otherwise, lse.

            Returns: The number of bytes produced by encoding the specified characters and any characters in the internal buffer.

        GetByteCount(self: Encoder, chars: Array[Char], index: int, count: int, flush: bool) -> int

            When overridden in a derived class, calculates the number of bytes produced by encoding a set of characters from the specified character array. A parameter indicates

             whether to clear the internal state of the encoder after the calculation.

            chars: The character array containing the set of characters to encode.

            index: The index of the first character to encode.

            count: The number of characters to encode.

            flush: ue to simulate clearing the internal state of the encoder after the calculation; otherwise, lse.

            Returns: The number of bytes produced by encoding the specified characters and any characters in the internal buffer.
        """
        ...
    def GetBytes(self, chars, *__args):
        """
        GetBytes(self: Encoder, chars: Array[Char], charIndex: int, charCount: int, bytes: Array[Byte], byteIndex: int, flush: bool) -> int

            When overridden in a derived class, encodes a set of characters from the specified character array and any characters in the internal buffer into the specified byte

             array. A parameter indicates whether to clear the internal state of the encoder after the conversion.

            chars: The character array containing the set of characters to encode.

            charIndex: The index of the first character to encode.

            charCount: The number of characters to encode.

            bytes: The byte array to contain the resulting sequence of bytes.

            byteIndex: The index at which to start writing the resulting sequence of bytes.

            flush: ue to clear the internal state of the encoder after the conversion; otherwise, lse.

            Returns: The actual number of bytes written into bytes.

        GetBytes(self: Encoder, chars: Char*, charCount: int, bytes: Byte*, byteCount: int, flush: bool) -> int

            When overridden in a derived class, encodes a set of characters starting at the specified character pointer and any characters in the internal buffer into a sequence

             of bytes that are stored starting at the specified byte pointer. A parameter indicates whether to clear the internal state of the encoder after the conversion.

            chars: A pointer to the first character to encode.

            charCount: The number of characters to encode.

            bytes: A pointer to the location at which to start writing the resulting sequence of bytes.

            byteCount: The maximum number of bytes to write.

            flush: ue to clear the internal state of the encoder after the conversion; otherwise, lse.

            Returns: The actual number of bytes written at the location indicated by the bytes parameter.
        """
        ...
    def Reset(self):
        """
        Reset(self: Encoder)

            When overridden in a derived class, sets the encoder back to its initial state.
        """
        ...
    @property
    def Fallback(self):
        """
        Gets or sets a System.Text.EncoderFallback object for the current System.Text.Encoder object.

        Get: Fallback(self: Encoder) -> EncoderFallback

        Set: Fallback(self: Encoder) = value
        """
        ...
    @property
    def FallbackBuffer(self):
        """
        Gets the System.Text.EncoderFallbackBuffer object associated with the current System.Text.Encoder object.

        Get: FallbackBuffer(self: Encoder) -> EncoderFallbackBuffer
        """
        ...

class EncoderFallback:  # skipped bases: <type 'object'>
    """Provides a failure-handling mechanism, called a fallback, for an input character that cannot be converted to an encoded output byte sequence."""

    def CreateFallbackBuffer(self):
        """
        CreateFallbackBuffer(self: EncoderFallback) -> EncoderFallbackBuffer

            When overridden in a derived class, initializes a new instance of the System.Text.EncoderFallbackBuffer class.

            Returns: An object that provides a fallback buffer for an encoder.
        """
        ...
    @property
    def MaxCharCount(self):
        """
        When overridden in a derived class, gets the maximum number of characters the current System.Text.EncoderFallback object can return.

        Get: MaxCharCount(self: EncoderFallback) -> int
        """
        ...
    ExceptionFallback = None
    ReplacementFallback = None

class EncoderExceptionFallback(EncoderFallback):
    """
    Provides a failure-handling mechanism, called a fallback, for an input character that cannot be converted to an output byte sequence. The fallback throws an exception if an input character cannot be converted to an output byte sequence. This class cannot be inherited.

    EncoderExceptionFallback()
    """

    def Equals(self, value):
        """
        Equals(self: EncoderExceptionFallback, value: object) -> bool

            Indicates whether the current System.Text.EncoderExceptionFallback object and a specified object are equal.

            value: An object that derives from the System.Text.EncoderExceptionFallback class.

            Returns: ue if value is not ll (thing in Visual Basic .NET) and is a System.Text.EncoderExceptionFallback object; otherwise, lse.
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: EncoderExceptionFallback) -> int

            Retrieves the hash code for this instance.

            Returns: The return value is always the same arbitrary value, and has no special significance.
        """
        ...
    def __eq__(self, *args):  # cannot find CLR method
        """x.__eq__(y) <==> x==y"""
        ...
    def __ne__(self, *args): ...
    @property
    def MaxCharCount(self):
        """
        Gets the maximum number of characters this instance can return.

        Get: MaxCharCount(self: EncoderExceptionFallback) -> int
        """
        ...

class EncoderFallbackBuffer:  # skipped bases: <type 'object'>
    """Provides a buffer that allows a fallback handler to return an alternate string to an encoder when it cannot encode an input character."""

    def Fallback(self, *__args):
        """
        Fallback(self: EncoderFallbackBuffer, charUnknown: Char, index: int) -> bool

            When overridden in a derived class, prepares the fallback buffer to handle the specified input character.

            charUnknown: An input character.

            index: The index position of the character in the input buffer.

            Returns: ue if the fallback buffer can process charUnknown; lse if the fallback buffer ignores charUnknown.

        Fallback(self: EncoderFallbackBuffer, charUnknownHigh: Char, charUnknownLow: Char, index: int) -> bool

            When overridden in a derived class, prepares the fallback buffer to handle the specified surrogate pair.

            charUnknownHigh: The high surrogate of the input pair.

            charUnknownLow: The low surrogate of the input pair.

            index: The index position of the surrogate pair in the input buffer.

            Returns: ue if the fallback buffer can process charUnknownHigh and charUnknownLow; lse if the fallback buffer ignores the surrogate pair.
        """
        ...
    def GetNextChar(self):
        """
        GetNextChar(self: EncoderFallbackBuffer) -> Char

            When overridden in a derived class, retrieves the next character in the fallback buffer.

            Returns: The next character in the fallback buffer.
        """
        ...
    def MovePrevious(self):
        """
        MovePrevious(self: EncoderFallbackBuffer) -> bool

            When overridden in a derived class, causes the next call to the System.Text.EncoderFallbackBuffer.GetNextChar method to access the data buffer character position that

             is prior to the current character position.

            Returns: ue if the System.Text.EncoderFallbackBuffer.MovePrevious operation was successful; otherwise, lse.
        """
        ...
    def Reset(self):
        """
        Reset(self: EncoderFallbackBuffer)

            Initializes all data and state information pertaining to this fallback buffer.
        """
        ...
    @property
    def Remaining(self):
        """
        When overridden in a derived class, gets the number of characters in the current System.Text.EncoderFallbackBuffer object that remain to be processed.

        Get: Remaining(self: EncoderFallbackBuffer) -> int
        """
        ...

class EncoderExceptionFallbackBuffer(EncoderFallbackBuffer):
    """
    Throws System.Text.EncoderFallbackException when an input character cannot be converted to an encoded output byte sequence. This class cannot be inherited.

    EncoderExceptionFallbackBuffer()
    """

    @property
    def Remaining(self):
        """
        Gets the number of characters in the current System.Text.EncoderExceptionFallbackBuffer object that remain to be processed.

        Get: Remaining(self: EncoderExceptionFallbackBuffer) -> int
        """
        ...

class EncoderFallbackException(ArgumentException):  # skipped bases: <type '_Exception'>, <type 'ISerializable'>
    """
    The exception that is thrown when an encoder fallback operation fails. This class cannot be inherited.

    EncoderFallbackException()

    EncoderFallbackException(message: str)

    EncoderFallbackException(message: str, innerException: Exception)
    """

    def IsUnknownSurrogate(self):
        """
        IsUnknownSurrogate(self: EncoderFallbackException) -> bool

            Indicates whether the input that caused the exception is a surrogate pair.

            Returns: ue if the input was a surrogate pair; otherwise, lse.
        """
        ...
    @property
    def CharUnknown(self):
        """
        Gets the input character that caused the exception.

        Get: CharUnknown(self: EncoderFallbackException) -> Char
        """
        ...
    @property
    def CharUnknownHigh(self):
        """
        Gets the high component character of the surrogate pair that caused the exception.

        Get: CharUnknownHigh(self: EncoderFallbackException) -> Char
        """
        ...
    @property
    def CharUnknownLow(self):
        """
        Gets the low component character of the surrogate pair that caused the exception.

        Get: CharUnknownLow(self: EncoderFallbackException) -> Char
        """
        ...
    @property
    def Index(self):
        """
        Gets the index position in the input buffer of the character that caused the exception.

        Get: Index(self: EncoderFallbackException) -> int
        """
        ...
    SerializeObjectState = None

class EncoderReplacementFallback(EncoderFallback):
    """
    Provides a failure handling mechanism, called a fallback, for an input character that cannot be converted to an output byte sequence. The fallback uses a user-specified replacement string instead of the original input character. This class cannot be inherited.

    EncoderReplacementFallback()

    EncoderReplacementFallback(replacement: str)
    """

    def Equals(self, value):
        """
        Equals(self: EncoderReplacementFallback, value: object) -> bool

            Indicates whether the value of a specified object is equal to the System.Text.EncoderReplacementFallback object.

            value: A System.Text.EncoderReplacementFallback object.

            Returns: ue if the value parameter specifies an System.Text.EncoderReplacementFallback object and the replacement string of that object is equal to the replacement string of

             this System.Text.EncoderReplacementFallback object; otherwise, lse.
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: EncoderReplacementFallback) -> int

            Retrieves the hash code for the value of the System.Text.EncoderReplacementFallback object.

            Returns: The hash code of the value of the object.
        """
        ...
    def __eq__(self, *args):  # cannot find CLR method
        """x.__eq__(y) <==> x==y"""
        ...
    @staticmethod  # known case of __new__
    def __new__(cls, replacement=None):
        """
        __new__(cls: type)

        __new__(cls: type, replacement: str)
        """
        ...
    def __ne__(self, *args): ...
    @property
    def DefaultString(self):
        """
        Gets the replacement string that is the value of the System.Text.EncoderReplacementFallback object.

        Get: DefaultString(self: EncoderReplacementFallback) -> str
        """
        ...
    @property
    def MaxCharCount(self):
        """
        Gets the number of characters in the replacement string for the System.Text.EncoderReplacementFallback object.

        Get: MaxCharCount(self: EncoderReplacementFallback) -> int
        """
        ...

class EncoderReplacementFallbackBuffer(EncoderFallbackBuffer):
    """
    Represents a substitute input string that is used when the original input character cannot be encoded. This class cannot be inherited.

    EncoderReplacementFallbackBuffer(fallback: EncoderReplacementFallback)
    """

    @staticmethod  # known case of __new__
    def __new__(cls, fallback):
        """__new__(cls: type, fallback: EncoderReplacementFallback)"""
        ...
    @property
    def Remaining(self):
        """
        Gets the number of characters in the replacement fallback buffer that remain to be processed.

        Get: Remaining(self: EncoderReplacementFallbackBuffer) -> int
        """
        ...

class EncodingInfo:  # skipped bases: <type 'object'>
    """Provides basic information about an encoding."""

    def Equals(self, value):
        """
        Equals(self: EncodingInfo, value: object) -> bool

            Gets a value indicating whether the specified object is equal to the current System.Text.EncodingInfo object.

            value: An object to compare to the current System.Text.EncodingInfo object.

            Returns: ue if value is a System.Text.EncodingInfo object and is equal to the current System.Text.EncodingInfo object; otherwise, lse.
        """
        ...
    def GetEncoding(self):
        """
        GetEncoding(self: EncodingInfo) -> Encoding

            Returns a System.Text.Encoding object that corresponds to the current System.Text.EncodingInfo object.

            Returns: A System.Text.Encoding object that corresponds to the current System.Text.EncodingInfo object.
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: EncodingInfo) -> int

            Returns the hash code for the current System.Text.EncodingInfo object.

            Returns: A 32-bit signed integer hash code.
        """
        ...
    def __eq__(self, *args):  # cannot find CLR method
        """x.__eq__(y) <==> x==y"""
        ...
    def __ne__(self, *args): ...
    @property
    def CodePage(self):
        """
        Gets the code page identifier of the encoding.

        Get: CodePage(self: EncodingInfo) -> int
        """
        ...
    @property
    def DisplayName(self):
        """
        Gets the human-readable description of the encoding.

        Get: DisplayName(self: EncodingInfo) -> str
        """
        ...
    @property
    def Name(self):
        """
        Gets the name registered with the Internet Assigned Numbers Authority (IANA) for the encoding.

        Get: Name(self: EncodingInfo) -> str
        """
        ...

class EncodingProvider:  # skipped bases: <type 'object'>
    """
    Provides the base class for an encoding provider, which supplies encodings that are unavailable on a particular platform.

    EncodingProvider()
    """

    def GetEncoding(self, *__args):
        """
        GetEncoding(self: EncodingProvider, name: str, encoderFallback: EncoderFallback, decoderFallback: DecoderFallback) -> Encoding

            Returns the encoding associated with the specified name. Parameters specify an error handler for characters that cannot be encoded and byte sequences that cannot be

             decoded.

            name: The name of the preferred encoding.

            encoderFallback: An object that provides an error-handling procedure when a character cannot be encoded with this encoding.

            decoderFallback: An object that provides an error-handling procedure when a byte sequence cannot be decoded with the current encoding.

            Returns: The encoding that is associated with the specified name, or ll if this System.Text.EncodingProvider cannot return a valid encoding that corresponds to name.

        GetEncoding(self: EncodingProvider, codepage: int, encoderFallback: EncoderFallback, decoderFallback: DecoderFallback) -> Encoding

            Returns the encoding associated with the specified code page identifier. Parameters specify an error handler for characters that cannot be encoded and byte sequences

             that cannot be decoded.

            codepage: The code page identifier of the requested encoding.

            encoderFallback: An object that provides an error-handling procedure when a character cannot be encoded with this encoding.

            decoderFallback: An object that provides an error-handling procedure when a byte sequence cannot be decoded with this encoding.

            Returns: The encoding that is associated with the specified code page, or ll if this System.Text.EncodingProvider cannot return a valid encoding that corresponds to codepage.

        GetEncoding(self: EncodingProvider, name: str) -> Encoding

            Returns the encoding with the specified name.

            name: The name of the requested encoding.

            Returns: The encoding that is associated with the specified name, or ll if this System.Text.EncodingProvider cannot return a valid encoding that corresponds to name.

        GetEncoding(self: EncodingProvider, codepage: int) -> Encoding

            Returns the encoding associated with the specified code page identifier.

            codepage: The code page identifier of the requested encoding.

            Returns: The encoding that is associated with the specified code page, or ll if this System.Text.EncodingProvider cannot return a valid encoding that corresponds to codepage.
        """
        ...

class NormalizationForm(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Defines the type of normalization to perform.

    enum NormalizationForm, values: FormC (1), FormD (2), FormKC (5), FormKD (6)
    """

    FormC = None
    FormD = None
    FormKC = None
    FormKD = None
    value__ = None

class StringBuilder(object, ISerializable):
    """
    Represents a mutable string of characters. This class cannot be inherited.To browse the .NET Framework source code for this type, see the Reference Source.

    StringBuilder()

    StringBuilder(capacity: int)

    StringBuilder(value: str)

    StringBuilder(value: str, capacity: int)

    StringBuilder(value: str, startIndex: int, length: int, capacity: int)

    StringBuilder(capacity: int, maxCapacity: int)
    """

    def Append(self, value, *__args):
        """
        Append(self: StringBuilder, value: Char, repeatCount: int) -> StringBuilder

            Appends a specified number of copies of the string representation of a Unicode character to this instance.

            value: The character to append.

            repeatCount: The number of times to append value.

            Returns: A reference to this instance after the append operation has completed.

        Append(self: StringBuilder, value: Array[Char]) -> StringBuilder

            Appends the string representation of the Unicode characters in a specified array to this instance.

            value: The array of characters to append.

            Returns: A reference to this instance after the append operation has completed.

        Append(self: StringBuilder, value: object) -> StringBuilder

            Appends the string representation of a specified object to this instance.

            value: The object to append.

            Returns: A reference to this instance after the append operation has completed.

        Append(self: StringBuilder, value: UInt64) -> StringBuilder

            Appends the string representation of a specified 64-bit unsigned integer to this instance.

            value: The value to append.

            Returns: A reference to this instance after the append operation has completed.

        Append(self: StringBuilder, value: UInt32) -> StringBuilder

            Appends the string representation of a specified 32-bit unsigned integer to this instance.

            value: The value to append.

            Returns: A reference to this instance after the append operation has completed.

        Append(self: StringBuilder, value: UInt16) -> StringBuilder

            Appends the string representation of a specified 16-bit unsigned integer to this instance.

            value: The value to append.

            Returns: A reference to this instance after the append operation has completed.

        Append(self: StringBuilder, value: Decimal) -> StringBuilder

            Appends the string representation of a specified decimal number to this instance.

            value: The value to append.

            Returns: A reference to this instance after the append operation has completed.

        Append(self: StringBuilder, value: float) -> StringBuilder

            Appends the string representation of a specified double-precision floating-point number to this instance.

            value: The value to append.

            Returns: A reference to this instance after the append operation has completed.

        Append(self: StringBuilder, value: Single) -> StringBuilder

            Appends the string representation of a specified single-precision floating-point number to this instance.

            value: The value to append.

            Returns: A reference to this instance after the append operation has completed.

        Append(self: StringBuilder, value: Int64) -> StringBuilder

            Appends the string representation of a specified 64-bit signed integer to this instance.

            value: The value to append.

            Returns: A reference to this instance after the append operation has completed.

        Append(self: StringBuilder, value: int) -> StringBuilder

            Appends the string representation of a specified 32-bit signed integer to this instance.

            value: The value to append.

            Returns: A reference to this instance after the append operation has completed.

        Append(self: StringBuilder, value: Int16) -> StringBuilder

            Appends the string representation of a specified 16-bit signed integer to this instance.

            value: The value to append.

            Returns: A reference to this instance after the append operation has completed.

        Append(self: StringBuilder, value: Char) -> StringBuilder

            Appends the string representation of a specified System.Char object to this instance.

            value: The UTF-16-encoded code unit to append.

            Returns: A reference to this instance after the append operation has completed.

        Append(self: StringBuilder, value: Byte) -> StringBuilder

            Appends the string representation of a specified 8-bit unsigned integer to this instance.

            value: The value to append.

            Returns: A reference to this instance after the append operation has completed.

        Append(self: StringBuilder, value: SByte) -> StringBuilder

            Appends the string representation of a specified 8-bit signed integer to this instance.

            value: The value to append.

            Returns: A reference to this instance after the append operation has completed.

        Append(self: StringBuilder, value: str, startIndex: int, count: int) -> StringBuilder

            Appends a copy of a specified substring to this instance.

            value: The string that contains the substring to append.

            startIndex: The starting position of the substring within value.

            count: The number of characters in value to append.

            Returns: A reference to this instance after the append operation has completed.

        Append(self: StringBuilder, value: str) -> StringBuilder

            Appends a copy of the specified string to this instance.

            value: The string to append.

            Returns: A reference to this instance after the append operation has completed.

        Append(self: StringBuilder, value: Array[Char], startIndex: int, charCount: int) -> StringBuilder

            Appends the string representation of a specified subarray of Unicode characters to this instance.

            value: A character array.

            startIndex: The starting position in value.

            charCount: The number of characters to append.

            Returns: A reference to this instance after the append operation has completed.

        Append(self: StringBuilder, value: Char*, valueCount: int) -> StringBuilder

            Appends an array of Unicode characters starting at a specified address to this instance.

            value: A pointer to an array of characters.

            valueCount: The number of characters in the array.

            Returns: A reference to this instance after the append operation has completed.

        Append(self: StringBuilder, value: bool) -> StringBuilder

            Appends the string representation of a specified Boolean value to this instance.

            value: The Boolean value to append.

            Returns: A reference to this instance after the append operation has completed.
        """
        ...
    def AppendFormat(self, *__args):
        """
        AppendFormat(self: StringBuilder, format: str, arg0: object) -> StringBuilder

            Appends the string returned by processing a composite format string, which contains zero or more format items, to this instance. Each format item is replaced by the

             string representation of a single argument.

            format: A composite format string (see Remarks).

            arg0: An object to format.

            Returns: A reference to this instance with format appended. Each format item in format is replaced by the string representation of arg0.

        AppendFormat(self: StringBuilder, format: str, arg0: object, arg1: object) -> StringBuilder

            Appends the string returned by processing a composite format string, which contains zero or more format items, to this instance. Each format item is replaced by the

             string representation of either of two arguments.

            format: A composite format string (see Remarks).

            arg0: The first object to format.

            arg1: The second object to format.

            Returns: A reference to this instance with format appended. Each format item in format is replaced by the string representation of the corresponding object argument.

        AppendFormat(self: StringBuilder, format: str, arg0: object, arg1: object, arg2: object) -> StringBuilder

            Appends the string returned by processing a composite format string, which contains zero or more format items, to this instance. Each format item is replaced by the

             string representation of either of three arguments.

            format: A composite format string (see Remarks).

            arg0: The first object to format.

            arg1: The second object to format.

            arg2: The third object to format.

            Returns: A reference to this instance with format appended. Each format item in format is replaced by the string representation of the corresponding object argument.

        AppendFormat(self: StringBuilder, provider: IFormatProvider, format: str, arg0: object) -> StringBuilder

            Appends the string returned by processing a composite format string, which contains zero or more format items, to this instance. Each format item is replaced by the

             string representation of a single argument using a specified format provider.

            provider: An object that supplies culture-specific formatting information.

            format: A composite format string (see Remarks).

            arg0: The object to format.

            Returns: A reference to this instance after the append operation has completed. After the append operation, this instance contains any data that existed before the operation,

             suffixed by a copy of format in which any format specification is replaced by the string representation of arg0.

        AppendFormat(self: StringBuilder, provider: IFormatProvider, format: str, arg0: object, arg1: object) -> StringBuilder

            Appends the string returned by processing a composite format string, which contains zero or more format items, to this instance. Each format item is replaced by the

             string representation of either of two arguments using a specified format provider.

            provider: An object that supplies culture-specific formatting information.

            format: A composite format string (see Remarks).

            arg0: The first object to format.

            arg1: The second object to format.

            Returns: A reference to this instance after the append operation has completed. After the append operation, this instance contains any data that existed before the operation,

             suffixed by a copy of format where any format specification is replaced by the string representation of the corresponding object argument.

        AppendFormat(self: StringBuilder, provider: IFormatProvider, format: str, arg0: object, arg1: object, arg2: object) -> StringBuilder

            Appends the string returned by processing a composite format string, which contains zero or more format items, to this instance. Each format item is replaced by the

             string representation of either of three arguments using a specified format provider.

            provider: An object that supplies culture-specific formatting information.

            format: A composite format string (see Remarks).

            arg0: The first object to format.

            arg1: The second object to format.

            arg2: The third object to format.

            Returns: A reference to this instance after the append operation has completed. After the append operation, this instance contains any data that existed before the operation,

             suffixed by a copy of format where any format specification is replaced by the string representation of the corresponding object argument.

        AppendFormat(self: StringBuilder, format: str, *args: Array[object]) -> StringBuilder

            Appends the string returned by processing a composite format string, which contains zero or more format items, to this instance. Each format item is replaced by the

             string representation of a corresponding argument in a parameter array.

            format: A composite format string (see Remarks).

            args: An array of objects to format.

            Returns: A reference to this instance with format appended. Each format item in format is replaced by the string representation of the corresponding object argument.

        AppendFormat(self: StringBuilder, provider: IFormatProvider, format: str, *args: Array[object]) -> StringBuilder

            Appends the string returned by processing a composite format string, which contains zero or more format items, to this instance. Each format item is replaced by the

             string representation of a corresponding argument in a parameter array using a specified format provider.

            provider: An object that supplies culture-specific formatting information.

            format: A composite format string (see Remarks).

            args: An array of objects to format.

            Returns: A reference to this instance after the append operation has completed. After the append operation, this instance contains any data that existed before the operation,

             suffixed by a copy of format where any format specification is replaced by the string representation of the corresponding object argument.
        """
        ...
    def AppendLine(self, value=None):
        """
        AppendLine(self: StringBuilder) -> StringBuilder

            Appends the default line terminator to the end of the current System.Text.StringBuilder object.

            Returns: A reference to this instance after the append operation has completed.

        AppendLine(self: StringBuilder, value: str) -> StringBuilder

            Appends a copy of the specified string followed by the default line terminator to the end of the current System.Text.StringBuilder object.

            value: The string to append.

            Returns: A reference to this instance after the append operation has completed.
        """
        ...
    def Clear(self):
        """
        Clear(self: StringBuilder) -> StringBuilder

            Removes all characters from the current System.Text.StringBuilder instance.

            Returns: An object whose System.Text.StringBuilder.Length is 0 (zero).
        """
        ...
    def CopyTo(self, sourceIndex, destination, destinationIndex, count):
        """
        CopyTo(self: StringBuilder, sourceIndex: int, destination: Array[Char], destinationIndex: int, count: int)

            Copies the characters from a specified segment of this instance to a specified segment of a destination System.Char array.

            sourceIndex: The starting position in this instance where characters will be copied from. The index is zero-based.

            destination: The array where characters will be copied.

            destinationIndex: The starting position in destination where characters will be copied. The index is zero-based.

            count: The number of characters to be copied.
        """
        ...
    def EnsureCapacity(self, capacity):
        """
        EnsureCapacity(self: StringBuilder, capacity: int) -> int

            Ensures that the capacity of this instance of System.Text.StringBuilder is at least the specified value.

            capacity: The minimum capacity to ensure.

            Returns: The new capacity of this instance.
        """
        ...
    def Equals(self, *__args):
        """
        Equals(self: StringBuilder, sb: StringBuilder) -> bool

            Returns a value indicating whether this instance is equal to a specified object.

            sb: An object to compare with this instance, or ll.

            Returns: ue if this instance and sb have equal string, System.Text.StringBuilder.Capacity, and System.Text.StringBuilder.MaxCapacity values; otherwise, lse.
        """
        ...
    def Insert(self, index, value, *__args):
        """
        Insert(self: StringBuilder, index: int, value: str, count: int) -> StringBuilder

            Inserts one or more copies of a specified string into this instance at the specified character position.

            index: The position in this instance where insertion begins.

            value: The string to insert.

            count: The number of times to insert value.

            Returns: A reference to this instance after insertion has completed.

        Insert(self: StringBuilder, index: int, value: UInt64) -> StringBuilder

            Inserts the string representation of a 64-bit unsigned integer into this instance at the specified character position.

            index: The position in this instance where insertion begins.

            value: The value to insert.

            Returns: A reference to this instance after the insert operation has completed.

        Insert(self: StringBuilder, index: int, value: UInt32) -> StringBuilder

            Inserts the string representation of a 32-bit unsigned integer into this instance at the specified character position.

            index: The position in this instance where insertion begins.

            value: The value to insert.

            Returns: A reference to this instance after the insert operation has completed.

        Insert(self: StringBuilder, index: int, value: UInt16) -> StringBuilder

            Inserts the string representation of a 16-bit unsigned integer into this instance at the specified character position.

            index: The position in this instance where insertion begins.

            value: The value to insert.

            Returns: A reference to this instance after the insert operation has completed.

        Insert(self: StringBuilder, index: int, value: Decimal) -> StringBuilder

            Inserts the string representation of a decimal number into this instance at the specified character position.

            index: The position in this instance where insertion begins.

            value: The value to insert.

            Returns: A reference to this instance after the insert operation has completed.

        Insert(self: StringBuilder, index: int, value: float) -> StringBuilder

            Inserts the string representation of a double-precision floating-point number into this instance at the specified character position.

            index: The position in this instance where insertion begins.

            value: The value to insert.

            Returns: A reference to this instance after the insert operation has completed.

        Insert(self: StringBuilder, index: int, value: Single) -> StringBuilder

            Inserts the string representation of a single-precision floating point number into this instance at the specified character position.

            index: The position in this instance where insertion begins.

            value: The value to insert.

            Returns: A reference to this instance after the insert operation has completed.

        Insert(self: StringBuilder, index: int, value: Int64) -> StringBuilder

            Inserts the string representation of a 64-bit signed integer into this instance at the specified character position.

            index: The position in this instance where insertion begins.

            value: The value to insert.

            Returns: A reference to this instance after the insert operation has completed.

        Insert(self: StringBuilder, index: int, value: int) -> StringBuilder

            Inserts the string representation of a specified 32-bit signed integer into this instance at the specified character position.

            index: The position in this instance where insertion begins.

            value: The value to insert.

            Returns: A reference to this instance after the insert operation has completed.

        Insert(self: StringBuilder, index: int, value: Array[Char], startIndex: int, charCount: int) -> StringBuilder

            Inserts the string representation of a specified subarray of Unicode characters into this instance at the specified character position.

            index: The position in this instance where insertion begins.

            value: A character array.

            startIndex: The starting index within value.

            charCount: The number of characters to insert.

            Returns: A reference to this instance after the insert operation has completed.

        Insert(self: StringBuilder, index: int, value: Array[Char]) -> StringBuilder

            Inserts the string representation of a specified array of Unicode characters into this instance at the specified character position.

            index: The position in this instance where insertion begins.

            value: The character array to insert.

            Returns: A reference to this instance after the insert operation has completed.

        Insert(self: StringBuilder, index: int, value: Char) -> StringBuilder

            Inserts the string representation of a specified Unicode character into this instance at the specified character position.

            index: The position in this instance where insertion begins.

            value: The value to insert.

            Returns: A reference to this instance after the insert operation has completed.

        Insert(self: StringBuilder, index: int, value: Int16) -> StringBuilder

            Inserts the string representation of a specified 16-bit signed integer into this instance at the specified character position.

            index: The position in this instance where insertion begins.

            value: The value to insert.

            Returns: A reference to this instance after the insert operation has completed.

        Insert(self: StringBuilder, index: int, value: Byte) -> StringBuilder

            Inserts the string representation of a specified 8-bit unsigned integer into this instance at the specified character position.

            index: The position in this instance where insertion begins.

            value: The value to insert.

            Returns: A reference to this instance after the insert operation has completed.

        Insert(self: StringBuilder, index: int, value: SByte) -> StringBuilder

            Inserts the string representation of a specified 8-bit signed integer into this instance at the specified character position.

            index: The position in this instance where insertion begins.

            value: The value to insert.

            Returns: A reference to this instance after the insert operation has completed.

        Insert(self: StringBuilder, index: int, value: str) -> StringBuilder

            Inserts a string into this instance at the specified character position.

            index: The position in this instance where insertion begins.

            value: The string to insert.

            Returns: A reference to this instance after the insert operation has completed.

        Insert(self: StringBuilder, index: int, value: object) -> StringBuilder

            Inserts the string representation of an object into this instance at the specified character position.

            index: The position in this instance where insertion begins.

            value: The object to insert, or ll.

            Returns: A reference to this instance after the insert operation has completed.

        Insert(self: StringBuilder, index: int, value: bool) -> StringBuilder

            Inserts the string representation of a Boolean value into this instance at the specified character position.

            index: The position in this instance where insertion begins.

            value: The value to insert.

            Returns: A reference to this instance after the insert operation has completed.
        """
        ...
    def Remove(self, startIndex, length):
        """
        Remove(self: StringBuilder, startIndex: int, length: int) -> StringBuilder

            Removes the specified range of characters from this instance.

            startIndex: The zero-based position in this instance where removal begins.

            length: The number of characters to remove.

            Returns: A reference to this instance after the excise operation has completed.
        """
        ...
    def Replace(self, *__args):
        """
        Replace(self: StringBuilder, oldValue: str, newValue: str) -> StringBuilder

            Replaces all occurrences of a specified string in this instance with another specified string.

            oldValue: The string to replace.

            newValue: The string that replaces oldValue, or ll.

            Returns: A reference to this instance with all instances of oldValue replaced by newValue.

        Replace(self: StringBuilder, oldValue: str, newValue: str, startIndex: int, count: int) -> StringBuilder

            Replaces, within a substring of this instance, all occurrences of a specified string with another specified string.

            oldValue: The string to replace.

            newValue: The string that replaces oldValue, or ll.

            startIndex: The position in this instance where the substring begins.

            count: The length of the substring.

            Returns: A reference to this instance with all instances of oldValue replaced by newValue in the range from startIndex to startIndex + count - 1.

        Replace(self: StringBuilder, oldChar: Char, newChar: Char) -> StringBuilder

            Replaces all occurrences of a specified character in this instance with another specified character.

            oldChar: The character to replace.

            newChar: The character that replaces oldChar.

            Returns: A reference to this instance with oldChar replaced by newChar.

        Replace(self: StringBuilder, oldChar: Char, newChar: Char, startIndex: int, count: int) -> StringBuilder

            Replaces, within a substring of this instance, all occurrences of a specified character with another specified character.

            oldChar: The character to replace.

            newChar: The character that replaces oldChar.

            startIndex: The position in this instance where the substring begins.

            count: The length of the substring.

            Returns: A reference to this instance with oldChar replaced by newChar in the range from startIndex to startIndex + count -1.
        """
        ...
    def ToString(self, startIndex=None, length=None):
        """
        ToString(self: StringBuilder) -> str

            Converts the value of this instance to a System.String.

            Returns: A string whose value is the same as this instance.

        ToString(self: StringBuilder, startIndex: int, length: int) -> str

            Converts the value of a substring of this instance to a System.String.

            startIndex: The starting position of the substring in this instance.

            length: The length of the substring.

            Returns: A string whose value is the same as the specified substring of this instance.
        """
        ...
    def __eq__(self, *args):  # cannot find CLR method
        """x.__eq__(y) <==> x==y"""
        ...
    def __getitem__(self, *args):  # cannot find CLR method
        """x.__getitem__(y) <==> x[y]"""
        ...
    def __setitem__(self, *args):  # cannot find CLR method
        """x.__setitem__(i, y) <==> x[i]="""
        ...
    @property
    def Capacity(self):
        """
        Gets or sets the maximum number of characters that can be contained in the memory allocated by the current instance.

        Get: Capacity(self: StringBuilder) -> int

        Set: Capacity(self: StringBuilder) = value
        """
        ...
    @property
    def Length(self):
        """
        Gets or sets the length of the current System.Text.StringBuilder object.

        Get: Length(self: StringBuilder) -> int

        Set: Length(self: StringBuilder) = value
        """
        ...
    @property
    def MaxCapacity(self):
        """
        Gets the maximum capacity of this instance.

        Get: MaxCapacity(self: StringBuilder) -> int
        """
        ...

class UnicodeEncoding(Encoding):  # skipped bases: <type 'ICloneable'>
    """
    Represents a UTF-16 encoding of Unicode characters.

    UnicodeEncoding()

    UnicodeEncoding(bigEndian: bool, byteOrderMark: bool)

    UnicodeEncoding(bigEndian: bool, byteOrderMark: bool, throwOnInvalidBytes: bool)
    """

    CharSize = 2

class UTF32Encoding(Encoding):  # skipped bases: <type 'ICloneable'>
    """
    Represents a UTF-32 encoding of Unicode characters.

    UTF32Encoding()

    UTF32Encoding(bigEndian: bool, byteOrderMark: bool)

    UTF32Encoding(bigEndian: bool, byteOrderMark: bool, throwOnInvalidCharacters: bool)
    """

    pass

class UTF7Encoding(Encoding):  # skipped bases: <type 'ICloneable'>
    """
    Represents a UTF-7 encoding of Unicode characters.

    UTF7Encoding()

    UTF7Encoding(allowOptionals: bool)
    """

    pass

class UTF8Encoding(Encoding):  # skipped bases: <type 'ICloneable'>
    """
    Represents a UTF-8 encoding of Unicode characters.

    UTF8Encoding()

    UTF8Encoding(encoderShouldEmitUTF8Identifier: bool)

    UTF8Encoding(encoderShouldEmitUTF8Identifier: bool, throwOnInvalidBytes: bool)
    """

    pass

# variables with complex values
