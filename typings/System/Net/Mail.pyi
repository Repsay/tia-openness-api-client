# encoding: utf-8
# module System.Net.Mail calls itself Mail
# from System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AttachmentBase(object, IDisposable):
    """Base class that represents an email attachment. Classes System.Net.Mail.Attachment, System.Net.Mail.AlternateView, and System.Net.Mail.LinkedResource derive from this class."""

    @property
    def ContentId(self):
        """
        Gets or sets the MIME content ID for this attachment.

        Get: ContentId(self: AttachmentBase) -> str

        Set: ContentId(self: AttachmentBase) = value
        """
        ...
    @property
    def ContentStream(self):
        """
        Gets the content stream of this attachment.

        Get: ContentStream(self: AttachmentBase) -> Stream
        """
        ...
    @property
    def ContentType(self):
        """
        Gets the content type of this attachment.

        Get: ContentType(self: AttachmentBase) -> ContentType

        Set: ContentType(self: AttachmentBase) = value
        """
        ...
    @property
    def TransferEncoding(self):
        """
        Gets or sets the encoding of this attachment.

        Get: TransferEncoding(self: AttachmentBase) -> TransferEncoding

        Set: TransferEncoding(self: AttachmentBase) = value
        """
        ...

class AlternateView(AttachmentBase):  # skipped bases: <type 'IDisposable'>
    """
    Represents the format to view an email message.

    AlternateView(fileName: str)

    AlternateView(fileName: str, mediaType: str)

    AlternateView(fileName: str, contentType: ContentType)

    AlternateView(contentStream: Stream)

    AlternateView(contentStream: Stream, mediaType: str)

    AlternateView(contentStream: Stream, contentType: ContentType)
    """

    @staticmethod
    def CreateAlternateViewFromString(content, *__args):
        """
        CreateAlternateViewFromString(content: str) -> AlternateView

            Creates a System.Net.Mail.AlternateView of an email message using the content specified in a System.String.

            content: The System.String that contains the content of the email message.

            Returns: An System.Net.Mail.AlternateView object that represents an alternate view of an email message.

        CreateAlternateViewFromString(content: str, contentEncoding: Encoding, mediaType: str) -> AlternateView

            Creates an System.Net.Mail.AlternateView of an email message using the content specified in a System.String, the specified text encoding, and MIME media type of the

             content.

            content: A System.String that contains the content for this attachment.

            contentEncoding: An System.Text.Encoding. This value can be ll.

            mediaType: The MIME media type of the content.

            Returns: An System.Net.Mail.AlternateView object that represents an alternate view of an email message.

        CreateAlternateViewFromString(content: str, contentType: ContentType) -> AlternateView

            Creates an System.Net.Mail.AlternateView of an email message using the content specified in a System.String and the specified MIME media type of the content.

            content: A System.String that contains the content for this attachment.

            contentType: A System.Net.Mime.ContentType that describes the data in string.

            Returns: An System.Net.Mail.AlternateView object that represents an alternate view of an email message.
        """
        ...
    @property
    def BaseUri(self):
        """
        Gets or sets the base URI to use for resolving relative URIs in the System.Net.Mail.AlternateView.

        Get: BaseUri(self: AlternateView) -> Uri

        Set: BaseUri(self: AlternateView) = value
        """
        ...
    @property
    def LinkedResources(self):
        """
        Gets the set of embedded resources referred to by this attachment.

        Get: LinkedResources(self: AlternateView) -> LinkedResourceCollection
        """
        ...

class AlternateViewCollection(
    Collection[AlternateView], IDisposable
):  # skipped bases: <type 'IReadOnlyCollection[AlternateView]'>, <type 'IList[AlternateView]'>, <type 'IReadOnlyList[AlternateView]'>, <type 'IList'>, <type 'ICollection'>, <type 'IEnumerable'>, <type 'IEnumerable[AlternateView]'>, <type 'ICollection[AlternateView]'>
    """Represents a collection of System.Net.Mail.AlternateView objects."""

    @property
    def Items(self):
        """Gets a System.Collections.Generic.IList wrapper around the System.Collections.ObjectModel.Collection."""
        ...

class Attachment(AttachmentBase):  # skipped bases: <type 'IDisposable'>
    """
    Represents an attachment to an e-mail.

    Attachment(fileName: str)

    Attachment(fileName: str, mediaType: str)

    Attachment(fileName: str, contentType: ContentType)

    Attachment(contentStream: Stream, name: str)

    Attachment(contentStream: Stream, name: str, mediaType: str)

    Attachment(contentStream: Stream, contentType: ContentType)
    """

    @staticmethod
    def CreateAttachmentFromString(content, *__args):
        """
        CreateAttachmentFromString(content: str, name: str) -> Attachment

            Creates a mail attachment using the content from the specified string, and the specified MIME content type name.

            content: A System.String that contains the content for this attachment.

            name: The MIME content type name value in the content type associated with this attachment.

            Returns: An object of type System.Net.Mail.Attachment.

        CreateAttachmentFromString(content: str, name: str, contentEncoding: Encoding, mediaType: str) -> Attachment

            Creates a mail attachment using the content from the specified string, the specified MIME content type name, character encoding, and MIME header information for the

             attachment.

            content: A System.String that contains the content for this attachment.

            name: The MIME content type name value in the content type associated with this attachment.

            contentEncoding: An System.Text.Encoding. This value can be ll.

            mediaType: A System.String that contains the MIME Content-Header information for this attachment. This value can be ll.

            Returns: An object of type System.Net.Mail.Attachment.

        CreateAttachmentFromString(content: str, contentType: ContentType) -> Attachment

            Creates a mail attachment using the content from the specified string, and the specified System.Net.Mime.ContentType.

            content: A System.String that contains the content for this attachment.

            contentType: A System.Net.Mime.ContentType object that represents the Multipurpose Internet Mail Exchange (MIME) protocol Content-Type header to be used.

            Returns: An object of type System.Net.Mail.Attachment.
        """
        ...
    @property
    def ContentDisposition(self):
        """
        Gets the MIME content disposition for this attachment.

        Get: ContentDisposition(self: Attachment) -> ContentDisposition
        """
        ...
    @property
    def Name(self):
        """
        Gets or sets the MIME content type name value in the content type associated with this attachment.

        Get: Name(self: Attachment) -> str

        Set: Name(self: Attachment) = value
        """
        ...
    @property
    def NameEncoding(self):
        """
        Specifies the encoding for the System.Net.Mail.AttachmentSystem.Net.Mail.Attachment.Name.

        Get: NameEncoding(self: Attachment) -> Encoding

        Set: NameEncoding(self: Attachment) = value
        """
        ...

class AttachmentCollection(
    Collection[Attachment], IDisposable
):  # skipped bases: <type 'IReadOnlyCollection[Attachment]'>, <type 'ICollection[Attachment]'>, <type 'IReadOnlyList[Attachment]'>, <type 'IList[Attachment]'>, <type 'IEnumerable[Attachment]'>, <type 'IList'>, <type 'ICollection'>, <type 'IEnumerable'>
    """Stores attachments to be sent as part of an e-mail message."""

    @property
    def Items(self):
        """Gets a System.Collections.Generic.IList wrapper around the System.Collections.ObjectModel.Collection."""
        ...

class DeliveryNotificationOptions(
    Enum
):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Describes the delivery notification options for e-mail.

    enum (flags) DeliveryNotificationOptions, values: Delay (4), Never (134217728), None (0), OnFailure (2), OnSuccess (1)
    """

    Delay = None
    Never = None

    OnFailure = None
    OnSuccess = None
    value__ = None

class LinkedResource(AttachmentBase):  # skipped bases: <type 'IDisposable'>
    """
    Represents an embedded external resource in an email attachment, such as an image in an HTML attachment.

    LinkedResource(fileName: str)

    LinkedResource(fileName: str, mediaType: str)

    LinkedResource(fileName: str, contentType: ContentType)

    LinkedResource(contentStream: Stream)

    LinkedResource(contentStream: Stream, mediaType: str)

    LinkedResource(contentStream: Stream, contentType: ContentType)
    """

    @staticmethod
    def CreateLinkedResourceFromString(content, *__args):
        """
        CreateLinkedResourceFromString(content: str) -> LinkedResource

            Creates a System.Net.Mail.LinkedResource object from a string to be included in an email attachment as an embedded resource. The default media type is plain text, and

             the default content type is ASCII.

            content: A string that contains the embedded resource to be included in the email attachment.

            Returns: A System.Net.Mail.LinkedResource object that contains the embedded resource to be included in the email attachment.

        CreateLinkedResourceFromString(content: str, contentEncoding: Encoding, mediaType: str) -> LinkedResource

            Creates a System.Net.Mail.LinkedResource object from a string to be included in an email attachment as an embedded resource, with the specified content type, and media

             type.

            content: A string that contains the embedded resource to be included in the email attachment.

            contentEncoding: The type of the content.

            mediaType: The MIME media type of the content.

            Returns: A System.Net.Mail.LinkedResource object that contains the embedded resource to be included in the email attachment.

        CreateLinkedResourceFromString(content: str, contentType: ContentType) -> LinkedResource

            Creates a System.Net.Mail.LinkedResource object from a string to be included in an email attachment as an embedded resource, with the specified content type, and media

             type as plain text.

            content: A string that contains the embedded resource to be included in the email attachment.

            contentType: The type of the content.

            Returns: A System.Net.Mail.LinkedResource object that contains the embedded resource to be included in the email attachment.
        """
        ...
    @property
    def ContentLink(self):
        """
        Gets or sets a URI that the resource must match.

        Get: ContentLink(self: LinkedResource) -> Uri

        Set: ContentLink(self: LinkedResource) = value
        """
        ...

class LinkedResourceCollection(
    Collection[LinkedResource], IDisposable
):  # skipped bases: <type 'IEnumerable[LinkedResource]'>, <type 'IReadOnlyList[LinkedResource]'>, <type 'ICollection[LinkedResource]'>, <type 'IReadOnlyCollection[LinkedResource]'>, <type 'IList[LinkedResource]'>, <type 'ICollection'>, <type 'IEnumerable'>, <type 'IList'>
    """Stores linked resources to be sent as part of an e-mail message."""

    @property
    def Items(self):
        """Gets a System.Collections.Generic.IList wrapper around the System.Collections.ObjectModel.Collection."""
        ...

class MailAddress:  # skipped bases: <type 'object'>
    """
    Represents the address of an electronic mail sender or recipient.

    MailAddress(address: str)

    MailAddress(address: str, displayName: str)

    MailAddress(address: str, displayName: str, displayNameEncoding: Encoding)
    """

    def Equals(self, value):
        """
        Equals(self: MailAddress, value: object) -> bool

            Compares two mail addresses.

            value: A System.Net.Mail.MailAddress instance to compare to the current instance.

            Returns: ue if the two mail addresses are equal; otherwise, lse.
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: MailAddress) -> int

            Returns a hash value for a mail address.

            Returns: An integer hash value.
        """
        ...
    def ToString(self):
        """
        ToString(self: MailAddress) -> str

            Returns a string representation of this instance.

            Returns: A System.String that contains the contents of this System.Net.Mail.MailAddress.
        """
        ...
    def __eq__(self, *args):  # cannot find CLR method
        """x.__eq__(y) <==> x==y"""
        ...
    def __ne__(self, *args): ...
    @property
    def Address(self):
        """
        Gets the e-mail address specified when this instance was created.

        Get: Address(self: MailAddress) -> str
        """
        ...
    @property
    def DisplayName(self):
        """
        Gets the display name composed from the display name and address information specified when this instance was created.

        Get: DisplayName(self: MailAddress) -> str
        """
        ...
    @property
    def Host(self):
        """
        Gets the host portion of the address specified when this instance was created.

        Get: Host(self: MailAddress) -> str
        """
        ...
    @property
    def User(self):
        """
        Gets the user information from the address specified when this instance was created.

        Get: User(self: MailAddress) -> str
        """
        ...

class MailAddressCollection(
    Collection[MailAddress]
):  # skipped bases: <type 'IEnumerable[MailAddress]'>, <type 'ICollection[MailAddress]'>, <type 'IReadOnlyList[MailAddress]'>, <type 'IList'>, <type 'ICollection'>, <type 'IEnumerable'>, <type 'IList[MailAddress]'>, <type 'IReadOnlyCollection[MailAddress]'>
    """
    Store e-mail addresses that are associated with an e-mail message.

    MailAddressCollection()
    """

    def ToString(self):
        """
        ToString(self: MailAddressCollection) -> str

            Returns a string representation of the e-mail addresses in this System.Net.Mail.MailAddressCollection object.

            Returns: A System.String containing the e-mail addresses in this collection.
        """
        ...
    def __str__(self, *args): ...
    @property
    def Items(self):
        """Gets a System.Collections.Generic.IList wrapper around the System.Collections.ObjectModel.Collection."""
        ...

class MailMessage(object, IDisposable):
    """
    Represents an e-mail message that can be sent using the System.Net.Mail.SmtpClient class.

    MailMessage()

    MailMessage(from: str, to: str)

    MailMessage(from: str, to: str, subject: str, body: str)

    MailMessage(from: MailAddress, to: MailAddress)
    """

    @property
    def AlternateViews(self):
        """
        Gets the attachment collection used to store alternate forms of the message body.

        Get: AlternateViews(self: MailMessage) -> AlternateViewCollection
        """
        ...
    @property
    def Attachments(self):
        """
        Gets the attachment collection used to store data attached to this e-mail message.

        Get: Attachments(self: MailMessage) -> AttachmentCollection
        """
        ...
    @property
    def Bcc(self):
        """
        Gets the address collection that contains the blind carbon copy (BCC) recipients for this e-mail message.

        Get: Bcc(self: MailMessage) -> MailAddressCollection
        """
        ...
    @property
    def Body(self):
        """
        Gets or sets the message body.

        Get: Body(self: MailMessage) -> str

        Set: Body(self: MailMessage) = value
        """
        ...
    @property
    def BodyEncoding(self):
        """
        Gets or sets the encoding used to encode the message body.

        Get: BodyEncoding(self: MailMessage) -> Encoding

        Set: BodyEncoding(self: MailMessage) = value
        """
        ...
    @property
    def BodyTransferEncoding(self):
        """
        Gets or sets the transfer encoding used to encode the message body.

        Get: BodyTransferEncoding(self: MailMessage) -> TransferEncoding

        Set: BodyTransferEncoding(self: MailMessage) = value
        """
        ...
    @property
    def CC(self):
        """
        Gets the address collection that contains the carbon copy (CC) recipients for this e-mail message.

        Get: CC(self: MailMessage) -> MailAddressCollection
        """
        ...
    @property
    def DeliveryNotificationOptions(self):
        """
        Gets or sets the delivery notifications for this e-mail message.

        Get: DeliveryNotificationOptions(self: MailMessage) -> DeliveryNotificationOptions

        Set: DeliveryNotificationOptions(self: MailMessage) = value
        """
        ...
    @property
    def From(self):
        """
        Gets or sets the from address for this e-mail message.

        Get: From(self: MailMessage) -> MailAddress

        Set: From(self: MailMessage) = value
        """
        ...
    @property
    def Headers(self):
        """
        Gets the e-mail headers that are transmitted with this e-mail message.

        Get: Headers(self: MailMessage) -> NameValueCollection
        """
        ...
    @property
    def HeadersEncoding(self):
        """
        Gets or sets the encoding used for the user-defined custom headers for this e-mail message.

        Get: HeadersEncoding(self: MailMessage) -> Encoding

        Set: HeadersEncoding(self: MailMessage) = value
        """
        ...
    @property
    def IsBodyHtml(self):
        """
        Gets or sets a value indicating whether the mail message body is in Html.

        Get: IsBodyHtml(self: MailMessage) -> bool

        Set: IsBodyHtml(self: MailMessage) = value
        """
        ...
    @property
    def Priority(self):
        """
        Gets or sets the priority of this e-mail message.

        Get: Priority(self: MailMessage) -> MailPriority

        Set: Priority(self: MailMessage) = value
        """
        ...
    @property
    def ReplyTo(self):
        """
        Gets or sets the ReplyTo address for the mail message.

        Get: ReplyTo(self: MailMessage) -> MailAddress

        Set: ReplyTo(self: MailMessage) = value
        """
        ...
    @property
    def ReplyToList(self):
        """
        Gets or sets the list of addresses to reply to for the mail message.

        Get: ReplyToList(self: MailMessage) -> MailAddressCollection
        """
        ...
    @property
    def Sender(self):
        """
        Gets or sets the sender's address for this e-mail message.

        Get: Sender(self: MailMessage) -> MailAddress

        Set: Sender(self: MailMessage) = value
        """
        ...
    @property
    def Subject(self):
        """
        Gets or sets the subject line for this e-mail message.

        Get: Subject(self: MailMessage) -> str

        Set: Subject(self: MailMessage) = value
        """
        ...
    @property
    def SubjectEncoding(self):
        """
        Gets or sets the encoding used for the subject content for this e-mail message.

        Get: SubjectEncoding(self: MailMessage) -> Encoding

        Set: SubjectEncoding(self: MailMessage) = value
        """
        ...
    @property
    def To(self):
        """
        Gets the address collection that contains the recipients of this e-mail message.

        Get: To(self: MailMessage) -> MailAddressCollection
        """
        ...

class MailPriority(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies the priority of a System.Net.Mail.MailMessage.

    enum MailPriority, values: High (2), Low (1), Normal (0)
    """

    High = None
    Low = None
    Normal = None
    value__ = None

class SendCompletedEventHandler(MulticastDelegate):  # skipped bases: <type 'ICloneable'>, <type 'ISerializable'>
    """
    Represents the method that will handle the System.Net.Mail.SmtpClient.SendCompleted event.

    SendCompletedEventHandler(object: object, method: IntPtr)
    """

    def BeginInvoke(self, sender, e, callback, object):
        """BeginInvoke(self: SendCompletedEventHandler, sender: object, e: AsyncCompletedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult"""
        ...
    def EndInvoke(self, result):
        """EndInvoke(self: SendCompletedEventHandler, result: IAsyncResult)"""
        ...
    def Invoke(self, sender, e):
        """Invoke(self: SendCompletedEventHandler, sender: object, e: AsyncCompletedEventArgs)"""
        ...

class SmtpAccess(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies the level of access allowed to a Simple Mail Transport Protocol (SMTP) server.

    enum SmtpAccess, values: Connect (1), ConnectToUnrestrictedPort (2), None (0)
    """

    Connect = None
    ConnectToUnrestrictedPort = None

    value__ = None

class SmtpClient(object, IDisposable):
    """
    Allows applications to send e-mail by using the Simple Mail Transfer Protocol (SMTP).

    SmtpClient()

    SmtpClient(host: str)

    SmtpClient(host: str, port: int)
    """

    def OnSendCompleted(self, *args):  # cannot find CLR method
        """
        OnSendCompleted(self: SmtpClient, e: AsyncCompletedEventArgs)

            Raises the System.Net.Mail.SmtpClient.SendCompleted event.

            e: An System.ComponentModel.AsyncCompletedEventArgs that contains event data.
        """
        ...
    def Send(self, *__args):
        """
        Send(self: SmtpClient, from: str, recipients: str, subject: str, body: str)

            Sends the specified e-mail message to an SMTP server for delivery. The message sender, recipients, subject, and message body are specified using System.String objects.

            from: A System.String that contains the address information of the message sender.

            recipients: A System.String that contains the addresses that the message is sent to.

            subject: A System.String that contains the subject line for the message.

            body: A System.String that contains the message body.

        Send(self: SmtpClient, message: MailMessage)

            Sends the specified message to an SMTP server for delivery.

            message: A System.Net.Mail.MailMessage that contains the message to send.
        """
        ...
    def SendAsync(self, *__args):
        """
        SendAsync(self: SmtpClient, from: str, recipients: str, subject: str, body: str, userToken: object)

            Sends an e-mail message to an SMTP server for delivery. The message sender, recipients, subject, and message body are specified using System.String objects. This

             method does not block the calling thread and allows the caller to pass an object to the method that is invoked when the operation completes.

            from: A System.String that contains the address information of the message sender.

            recipients: A System.String that contains the address that the message is sent to.

            subject: A System.String that contains the subject line for the message.

            body: A System.String that contains the message body.

            userToken: A user-defined object that is passed to the method invoked when the asynchronous operation completes.

        SendAsync(self: SmtpClient, message: MailMessage, userToken: object)

            Sends the specified e-mail message to an SMTP server for delivery. This method does not block the calling thread and allows the caller to pass an object to the method

             that is invoked when the operation completes.

            message: A System.Net.Mail.MailMessage that contains the message to send.

            userToken: A user-defined object that is passed to the method invoked when the asynchronous operation completes.
        """
        ...
    def SendAsyncCancel(self):
        """
        SendAsyncCancel(self: SmtpClient)

            Cancels an asynchronous operation to send an e-mail message.
        """
        ...
    def SendMailAsync(self, *__args):
        """
        SendMailAsync(self: SmtpClient, from: str, recipients: str, subject: str, body: str) -> Task

            Sends the specified message to an SMTP server for delivery as an asynchronous operation. . The message sender, recipients, subject, and message body are specified

             using System.String objects.

            from: A System.String that contains the address information of the message sender.

            recipients: A System.String that contains the addresses that the message is sent to.

            subject: A System.String that contains the subject line for the message.

            body: A System.String that contains the message body.

            Returns: Returns System.Threading.Tasks.Task.The task object representing the asynchronous operation.

        SendMailAsync(self: SmtpClient, message: MailMessage) -> Task

            Sends the specified message to an SMTP server for delivery as an asynchronous operation.

            message: A System.Net.Mail.MailMessage that contains the message to send.

            Returns: Returns System.Threading.Tasks.Task.The task object representing the asynchronous operation.
        """
        ...
    @property
    def ClientCertificates(self):
        """
        Specify which certificates should be used to establish the Secure Sockets Layer (SSL) connection.

        Get: ClientCertificates(self: SmtpClient) -> X509CertificateCollection
        """
        ...
    @property
    def Credentials(self):
        """
        Gets or sets the credentials used to authenticate the sender.

        Get: Credentials(self: SmtpClient) -> ICredentialsByHost

        Set: Credentials(self: SmtpClient) = value
        """
        ...
    @property
    def DeliveryFormat(self):
        """
        Gets or sets the delivery format used by System.Net.Mail.SmtpClient to send e-mail.

        Get: DeliveryFormat(self: SmtpClient) -> SmtpDeliveryFormat

        Set: DeliveryFormat(self: SmtpClient) = value
        """
        ...
    @property
    def DeliveryMethod(self):
        """
        Specifies how outgoing email messages will be handled.

        Get: DeliveryMethod(self: SmtpClient) -> SmtpDeliveryMethod

        Set: DeliveryMethod(self: SmtpClient) = value
        """
        ...
    @property
    def EnableSsl(self):
        """
        Specify whether the System.Net.Mail.SmtpClient uses Secure Sockets Layer (SSL) to encrypt the connection.

        Get: EnableSsl(self: SmtpClient) -> bool

        Set: EnableSsl(self: SmtpClient) = value
        """
        ...
    @property
    def Host(self):
        """
        Gets or sets the name or IP address of the host used for SMTP transactions.

        Get: Host(self: SmtpClient) -> str

        Set: Host(self: SmtpClient) = value
        """
        ...
    @property
    def PickupDirectoryLocation(self):
        """
        Gets or sets the folder where applications save mail messages to be processed by the local SMTP server.

        Get: PickupDirectoryLocation(self: SmtpClient) -> str

        Set: PickupDirectoryLocation(self: SmtpClient) = value
        """
        ...
    @property
    def Port(self):
        """
        Gets or sets the port used for SMTP transactions.

        Get: Port(self: SmtpClient) -> int

        Set: Port(self: SmtpClient) = value
        """
        ...
    @property
    def ServicePoint(self):
        """
        Gets the network connection used to transmit the e-mail message.

        Get: ServicePoint(self: SmtpClient) -> ServicePoint
        """
        ...
    @property
    def TargetName(self):
        """
        Gets or sets the Service Provider Name (SPN) to use for authentication when using extended protection.

        Get: TargetName(self: SmtpClient) -> str

        Set: TargetName(self: SmtpClient) = value
        """
        ...
    @property
    def Timeout(self):
        """
        Gets or sets a value that specifies the amount of time after which a synchronous erload:System.Net.Mail.SmtpClient.Send call times out.

        Get: Timeout(self: SmtpClient) -> int

        Set: Timeout(self: SmtpClient) = value
        """
        ...
    @property
    def UseDefaultCredentials(self):
        """
        Gets or sets a System.Boolean value that controls whether the System.Net.CredentialCache.DefaultCredentials are sent with requests.

        Get: UseDefaultCredentials(self: SmtpClient) -> bool

        Set: UseDefaultCredentials(self: SmtpClient) = value
        """
        ...
    SendCompleted = None

class SmtpDeliveryFormat(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    The delivery format to use for sending outgoing e-mail using the Simple Mail Transport Protocol (SMTP).

    enum SmtpDeliveryFormat, values: International (1), SevenBit (0)
    """

    International = None
    SevenBit = None
    value__ = None

class SmtpDeliveryMethod(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies how email messages are delivered.

    enum SmtpDeliveryMethod, values: Network (0), PickupDirectoryFromIis (2), SpecifiedPickupDirectory (1)
    """

    Network = None
    PickupDirectoryFromIis = None
    SpecifiedPickupDirectory = None
    value__ = None

class SmtpException(Exception):  # skipped bases: <type '_Exception'>, <type 'ISerializable'>
    """
    Represents the exception that is thrown when the System.Net.Mail.SmtpClient is not able to complete a erload:System.Net.Mail.SmtpClient.Send or erload:System.Net.Mail.SmtpClient.SendAsync operation.

    SmtpException(statusCode: SmtpStatusCode)

    SmtpException(statusCode: SmtpStatusCode, message: str)

    SmtpException()

    SmtpException(message: str)

    SmtpException(message: str, innerException: Exception)
    """

    @property
    def StatusCode(self):
        """
        Gets the status code returned by an SMTP server when an e-mail message is transmitted.

        Get: StatusCode(self: SmtpException) -> SmtpStatusCode

        Set: StatusCode(self: SmtpException) = value
        """
        ...
    SerializeObjectState = None

class SmtpFailedRecipientException(SmtpException):  # skipped bases: <type '_Exception'>, <type 'ISerializable'>
    """
    Represents the exception that is thrown when the System.Net.Mail.SmtpClient is not able to complete a erload:System.Net.Mail.SmtpClient.Send or erload:System.Net.Mail.SmtpClient.SendAsync operation to a particular recipient.

    SmtpFailedRecipientException()

    SmtpFailedRecipientException(message: str)

    SmtpFailedRecipientException(message: str, innerException: Exception)

    SmtpFailedRecipientException(statusCode: SmtpStatusCode, failedRecipient: str)

    SmtpFailedRecipientException(statusCode: SmtpStatusCode, failedRecipient: str, serverResponse: str)

    SmtpFailedRecipientException(message: str, failedRecipient: str, innerException: Exception)
    """

    @property
    def FailedRecipient(self):
        """
        Indicates the e-mail address with delivery difficulties.

        Get: FailedRecipient(self: SmtpFailedRecipientException) -> str
        """
        ...
    SerializeObjectState = None

class SmtpFailedRecipientsException(
    SmtpFailedRecipientException
):  # skipped bases: <type '_Exception'>, <type 'ISerializable'>
    """
    The exception that is thrown when e-mail is sent using an System.Net.Mail.SmtpClient and cannot be delivered to all recipients.

    SmtpFailedRecipientsException()

    SmtpFailedRecipientsException(message: str)

    SmtpFailedRecipientsException(message: str, innerException: Exception)

    SmtpFailedRecipientsException(message: str, innerExceptions: Array[SmtpFailedRecipientException])
    """

    @property
    def InnerExceptions(self):
        """
        Gets one or more System.Net.Mail.SmtpFailedRecipientExceptions that indicate the e-mail recipients with SMTP delivery errors.

        Get: InnerExceptions(self: SmtpFailedRecipientsException) -> Array[SmtpFailedRecipientException]
        """
        ...
    SerializeObjectState = None

class SmtpPermission(
    CodeAccessPermission, IUnrestrictedPermission
):  # skipped bases: <type 'ISecurityEncodable'>, <type 'IPermission'>, <type 'IStackWalk'>
    """
    Controls access to Simple Mail Transport Protocol (SMTP) servers.

    SmtpPermission(state: PermissionState)

    SmtpPermission(unrestricted: bool)

    SmtpPermission(access: SmtpAccess)
    """

    def AddPermission(self, access):
        """
        AddPermission(self: SmtpPermission, access: SmtpAccess)

            Adds the specified access level value to the permission.

            access: One of the System.Net.Mail.SmtpAccess values.
        """
        ...
    @staticmethod  # known case of __new__
    def __new__(cls, *__args):
        """
        __new__(cls: type, state: PermissionState)

        __new__(cls: type, unrestricted: bool)

        __new__(cls: type, access: SmtpAccess)
        """
        ...
    @property
    def Access(self):
        """
        Gets the level of access to SMTP servers controlled by the permission.

        Get: Access(self: SmtpPermission) -> SmtpAccess
        """
        ...

class SmtpPermissionAttribute(CodeAccessSecurityAttribute):  # skipped bases: <type '_Attribute'>
    """
    Controls access to Simple Mail Transport Protocol (SMTP) servers.

    SmtpPermissionAttribute(action: SecurityAction)
    """

    def CreatePermission(self):
        """
        CreatePermission(self: SmtpPermissionAttribute) -> IPermission

            Creates a permission object that can be stored with the System.Security.Permissions.SecurityAction in an assembly's metadata.

            Returns: An System.Net.Mail.SmtpPermission instance.
        """
        ...
    @property
    def Access(self):
        """
        Gets or sets the level of access to SMTP servers controlled by the attribute.

        Get: Access(self: SmtpPermissionAttribute) -> str

        Set: Access(self: SmtpPermissionAttribute) = value
        """
        ...

class SmtpStatusCode(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies the outcome of sending e-mail by using the System.Net.Mail.SmtpClient class.

    enum SmtpStatusCode, values: BadCommandSequence (503), CannotVerifyUserWillAttemptDelivery (252), ClientNotPermitted (454), CommandNotImplemented (502), CommandParameterNotImplemented (504), CommandUnrecognized (500), ExceededStorageAllocation (552), GeneralFailure (-1), HelpMessage (214), InsufficientStorage (452), LocalErrorInProcessing (451), MailboxBusy (450), MailboxNameNotAllowed (553), MailboxUnavailable (550), MustIssueStartTlsFirst (530), Ok (250), ServiceClosingTransmissionChannel (221), ServiceNotAvailable (421), ServiceReady (220), StartMailInput (354), SyntaxError (501), SystemStatus (211), TransactionFailed (554), UserNotLocalTryAlternatePath (551), UserNotLocalWillForward (251)
    """

    BadCommandSequence = None
    CannotVerifyUserWillAttemptDelivery = None
    ClientNotPermitted = None
    CommandNotImplemented = None
    CommandParameterNotImplemented = None
    CommandUnrecognized = None
    ExceededStorageAllocation = None
    GeneralFailure = None
    HelpMessage = None
    InsufficientStorage = None
    LocalErrorInProcessing = None
    MailboxBusy = None
    MailboxNameNotAllowed = None
    MailboxUnavailable = None
    MustIssueStartTlsFirst = None
    Ok = None
    ServiceClosingTransmissionChannel = None
    ServiceNotAvailable = None
    ServiceReady = None
    StartMailInput = None
    SyntaxError = None
    SystemStatus = None
    TransactionFailed = None
    UserNotLocalTryAlternatePath = None
    UserNotLocalWillForward = None
    value__ = None
