# encoding: utf-8
# module System.Net.Mime calls itself Mime
# from System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class ContentDisposition: # skipped bases: <type 'object'>
    """
    Represents a MIME protocol Content-Disposition header.

    ContentDisposition()

    ContentDisposition(disposition: str)
    """
    def Equals(self, rparam):
        """
        Equals(self: ContentDisposition, rparam: object) -> bool

            Determines whether the content-disposition header of the specified System.Net.Mime.ContentDisposition object is equal to the content-disposition header of this object.

            rparam: The System.Net.Mime.ContentDisposition object to compare with this object.

            Returns: ue if the content-disposition headers are the same; otherwise lse.
        """
        ...

    def GetHashCode(self):
        """
        GetHashCode(self: ContentDisposition) -> int

            Determines the hash code of the specified System.Net.Mime.ContentDisposition object

            Returns: An integer hash value.
        """
        ...

    def ToString(self):
        """
        ToString(self: ContentDisposition) -> str

            Returns a System.String representation of this instance.

            Returns: A System.String that contains the property values for this instance.
        """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    @property
    def CreationDate(self):
        """
        Gets or sets the creation date for a file attachment.

        Get: CreationDate(self: ContentDisposition) -> DateTime

        Set: CreationDate(self: ContentDisposition) = value
        """
        ...

    @property
    def DispositionType(self):
        """
        Gets or sets the disposition type for an e-mail attachment.

        Get: DispositionType(self: ContentDisposition) -> str

        Set: DispositionType(self: ContentDisposition) = value
        """
        ...

    @property
    def FileName(self):
        """
        Gets or sets the suggested file name for an e-mail attachment.

        Get: FileName(self: ContentDisposition) -> str

        Set: FileName(self: ContentDisposition) = value
        """
        ...

    @property
    def Inline(self):
        """
        Gets or sets a System.Boolean value that determines the disposition type (Inline or Attachment) for an e-mail attachment.

        Get: Inline(self: ContentDisposition) -> bool

        Set: Inline(self: ContentDisposition) = value
        """
        ...

    @property
    def ModificationDate(self):
        """
        Gets or sets the modification date for a file attachment.

        Get: ModificationDate(self: ContentDisposition) -> DateTime

        Set: ModificationDate(self: ContentDisposition) = value
        """
        ...

    @property
    def Parameters(self):
        """
        Gets the parameters included in the Content-Disposition header represented by this instance.

        Get: Parameters(self: ContentDisposition) -> StringDictionary
        """
        ...

    @property
    def ReadDate(self):
        """
        Gets or sets the read date for a file attachment.

        Get: ReadDate(self: ContentDisposition) -> DateTime

        Set: ReadDate(self: ContentDisposition) = value
        """
        ...

    @property
    def Size(self):
        """
        Gets or sets the size of a file attachment.

        Get: Size(self: ContentDisposition) -> Int64

        Set: Size(self: ContentDisposition) = value
        """
        ...



class ContentType: # skipped bases: <type 'object'>
    """
    Represents a MIME protocol Content-Type header.

    ContentType()

    ContentType(contentType: str)
    """
    def Equals(self, rparam):
        """
        Equals(self: ContentType, rparam: object) -> bool

            Determines whether the content-type header of the specified System.Net.Mime.ContentType object is equal to the content-type header of this object.

            rparam: The System.Net.Mime.ContentType object to compare with this object.

            Returns: ue if the content-type headers are the same; otherwise lse.
        """
        ...

    def GetHashCode(self):
        """
        GetHashCode(self: ContentType) -> int

            Determines the hash code of the specified System.Net.Mime.ContentType object

            Returns: An integer hash value.
        """
        ...

    def ToString(self):
        """
        ToString(self: ContentType) -> str

            Returns a string representation of this System.Net.Mime.ContentType object.

            Returns: A System.String that contains the current settings for this System.Net.Mime.ContentType.
        """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    @property
    def Boundary(self):
        """
        Gets or sets the value of the boundary parameter included in the Content-Type header represented by this instance.

        Get: Boundary(self: ContentType) -> str

        Set: Boundary(self: ContentType) = value
        """
        ...

    @property
    def CharSet(self):
        """
        Gets or sets the value of the charset parameter included in the Content-Type header represented by this instance.

        Get: CharSet(self: ContentType) -> str

        Set: CharSet(self: ContentType) = value
        """
        ...

    @property
    def MediaType(self):
        """
        Gets or sets the media type value included in the Content-Type header represented by this instance.

        Get: MediaType(self: ContentType) -> str

        Set: MediaType(self: ContentType) = value
        """
        ...

    @property
    def Name(self):
        """
        Gets or sets the value of the name parameter included in the Content-Type header represented by this instance.

        Get: Name(self: ContentType) -> str

        Set: Name(self: ContentType) = value
        """
        ...

    @property
    def Parameters(self):
        """
        Gets the dictionary that contains the parameters included in the Content-Type header represented by this instance.

        Get: Parameters(self: ContentType) -> StringDictionary
        """
        ...



class DispositionTypeNames: # skipped bases: <type 'object'>
    """ Supplies the strings used to specify the disposition type for an e-mail attachment. """
    Attachment = 'attachment'
    Inline = 'inline'
    __all__ = [
        'Attachment',
        'Inline',
    ]


class MediaTypeNames: # skipped bases: <type 'object'>
    """ Specifies the media type information for an e-mail message attachment. """
    def Application(self, *args): #cannot find CLR method
        # no doc
        ...

    def Image(self, *args): #cannot find CLR method
        # no doc
        ...

    def Text(self, *args): #cannot find CLR method
        # no doc
        ...

    Application = None
    Image = None
    Text = None
    __all__ = [
        'Application',
        'Image',
        'Text',
    ]


class TransferEncoding(Enum): # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies the Content-Transfer-Encoding header information for an e-mail message attachment.

    enum TransferEncoding, values: Base64 (1), EightBit (3), QuotedPrintable (0), SevenBit (2), Unknown (-1)
    """
    Base64 = None
    EightBit = None
    QuotedPrintable = None
    SevenBit = None
    Unknown = None
    value__ = None


