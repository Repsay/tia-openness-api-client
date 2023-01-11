# encoding: utf-8
# module System.Security.Cryptography.X509Certificates calls itself X509Certificates
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class OpenFlags(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies the way to open the X.509 certificate store.

    enum (flags) OpenFlags, values: IncludeArchived (8), MaxAllowed (2), OpenExistingOnly (4), ReadOnly (0), ReadWrite (1)
    """

    IncludeArchived = None
    MaxAllowed = None
    OpenExistingOnly = None
    ReadOnly = None
    ReadWrite = None
    value__ = None

class PublicKey:  # skipped bases: <type 'object'>
    """
    Represents a certificate's public key information. This class cannot be inherited.

    PublicKey(oid: Oid, parameters: AsnEncodedData, keyValue: AsnEncodedData)
    """

    @property
    def EncodedKeyValue(self):
        """
        Gets the ASN.1-encoded representation of the public key value.

        Get: EncodedKeyValue(self: PublicKey) -> AsnEncodedData
        """
        ...
    @property
    def EncodedParameters(self):
        """
        Gets the ASN.1-encoded representation of the public key parameters.

        Get: EncodedParameters(self: PublicKey) -> AsnEncodedData
        """
        ...
    @property
    def Key(self):
        """
        Gets an System.Security.Cryptography.RSACryptoServiceProvider or System.Security.Cryptography.DSACryptoServiceProvider object representing the public key.

        Get: Key(self: PublicKey) -> AsymmetricAlgorithm
        """
        ...
    @property
    def Oid(self):
        """
        Gets an object identifier (OID) object of the public key.

        Get: Oid(self: PublicKey) -> Oid
        """
        ...

class StoreLocation(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies the location of the X.509 certificate store.

    enum StoreLocation, values: CurrentUser (1), LocalMachine (2)
    """

    CurrentUser = None
    LocalMachine = None
    value__ = None

class StoreName(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies the name of the X.509 certificate store to open.

    enum StoreName, values: AddressBook (1), AuthRoot (2), CertificateAuthority (3), Disallowed (4), My (5), Root (6), TrustedPeople (7), TrustedPublisher (8)
    """

    AddressBook = None
    AuthRoot = None
    CertificateAuthority = None
    Disallowed = None
    My = None
    Root = None
    TrustedPeople = None
    TrustedPublisher = None
    value__ = None

class X500DistinguishedName(AsnEncodedData):
    """
    Represents the distinguished name of an X509 certificate. This class cannot be inherited.

    X500DistinguishedName(encodedDistinguishedName: Array[Byte])

    X500DistinguishedName(encodedDistinguishedName: AsnEncodedData)

    X500DistinguishedName(distinguishedName: X500DistinguishedName)

    X500DistinguishedName(distinguishedName: str)

    X500DistinguishedName(distinguishedName: str, flag: X500DistinguishedNameFlags)
    """

    def Decode(self, flag):
        """
        Decode(self: X500DistinguishedName, flag: X500DistinguishedNameFlags) -> str

            Decodes a distinguished name using the characteristics specified by the flag parameter.

            flag: A bitwise combination of the enumeration values that specify the characteristics of the distinguished name.

            Returns: The decoded distinguished name.
        """
        ...
    @property
    def Name(self):
        """
        Gets the comma-delimited distinguished name from an X500 certificate.

        Get: Name(self: X500DistinguishedName) -> str
        """
        ...

class X500DistinguishedNameFlags(
    Enum
):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies characteristics of the X.500 distinguished name.

    enum (flags) X500DistinguishedNameFlags, values: DoNotUsePlusSign (32), DoNotUseQuotes (64), ForceUTF8Encoding (16384), None (0), Reversed (1), UseCommas (128), UseNewLines (256), UseSemicolons (16), UseT61Encoding (8192), UseUTF8Encoding (4096)
    """

    DoNotUsePlusSign = None
    DoNotUseQuotes = None
    ForceUTF8Encoding = None

    Reversed = None
    UseCommas = None
    UseNewLines = None
    UseSemicolons = None
    UseT61Encoding = None
    UseUTF8Encoding = None
    value__ = None

class X509Extension(AsnEncodedData):
    """
    Represents an X509 extension.

    X509Extension(oid: str, rawData: Array[Byte], critical: bool)

    X509Extension(encodedExtension: AsnEncodedData, critical: bool)

    X509Extension(oid: Oid, rawData: Array[Byte], critical: bool)
    """

    @property
    def Critical(self):
        """
        Gets a Boolean value indicating whether the extension is critical.

        Get: Critical(self: X509Extension) -> bool

        Set: Critical(self: X509Extension) = value
        """
        ...

class X509BasicConstraintsExtension(X509Extension):
    """
    Defines the constraints set on a certificate. This class cannot be inherited.

    X509BasicConstraintsExtension()

    X509BasicConstraintsExtension(certificateAuthority: bool, hasPathLengthConstraint: bool, pathLengthConstraint: int, critical: bool)

    X509BasicConstraintsExtension(encodedBasicConstraints: AsnEncodedData, critical: bool)
    """

    @property
    def CertificateAuthority(self):
        """
        Gets a value indicating whether a certificate is a certificate authority (CA) certificate.

        Get: CertificateAuthority(self: X509BasicConstraintsExtension) -> bool
        """
        ...
    @property
    def HasPathLengthConstraint(self):
        """
        Gets a value indicating whether a certificate has a restriction on the number of path levels it allows.

        Get: HasPathLengthConstraint(self: X509BasicConstraintsExtension) -> bool
        """
        ...
    @property
    def PathLengthConstraint(self):
        """
        Gets the number of levels allowed in a certificate's path.

        Get: PathLengthConstraint(self: X509BasicConstraintsExtension) -> int
        """
        ...

class X509Certificate(object, IDisposable, IDeserializationCallback, ISerializable):
    """
    Provides methods that help you use X.509 v.3 certificates.

    X509Certificate()

    X509Certificate(data: Array[Byte])

    X509Certificate(rawData: Array[Byte], password: str)

    X509Certificate(rawData: Array[Byte], password: SecureString)

    X509Certificate(rawData: Array[Byte], password: str, keyStorageFlags: X509KeyStorageFlags)

    X509Certificate(rawData: Array[Byte], password: SecureString, keyStorageFlags: X509KeyStorageFlags)

    X509Certificate(fileName: str)

    X509Certificate(fileName: str, password: str)

    X509Certificate(fileName: str, password: SecureString)

    X509Certificate(fileName: str, password: str, keyStorageFlags: X509KeyStorageFlags)

    X509Certificate(fileName: str, password: SecureString, keyStorageFlags: X509KeyStorageFlags)

    X509Certificate(handle: IntPtr)

    X509Certificate(cert: X509Certificate)

    X509Certificate(info: SerializationInfo, context: StreamingContext)
    """

    @staticmethod
    def CreateFromCertFile(filename):
        """
        CreateFromCertFile(filename: str) -> X509Certificate

            Creates an X.509v3 certificate from the specified PKCS7 signed file.

            filename: The path of the PKCS7 signed file from which to create the X.509 certificate.

            Returns: The newly created X.509 certificate.
        """
        ...
    @staticmethod
    def CreateFromSignedFile(filename):
        """
        CreateFromSignedFile(filename: str) -> X509Certificate

            Creates an X.509v3 certificate from the specified signed file.

            filename: The path of the signed file from which to create the X.509 certificate.

            Returns: The newly created X.509 certificate.
        """
        ...
    def Equals(self, *__args):
        """
        Equals(self: X509Certificate, obj: object) -> bool

            Compares two System.Security.Cryptography.X509Certificates.X509Certificate objects for equality.

            obj: An System.Security.Cryptography.X509Certificates.X509Certificate object to compare to the current object.

            Returns: ue if the current System.Security.Cryptography.X509Certificates.X509Certificate object is equal to the object specified by the other parameter; otherwise, lse.

        Equals(self: X509Certificate, other: X509Certificate) -> bool

            Compares two System.Security.Cryptography.X509Certificates.X509Certificate objects for equality.

            other: An System.Security.Cryptography.X509Certificates.X509Certificate object to compare to the current object.

            Returns: ue if the current System.Security.Cryptography.X509Certificates.X509Certificate object is equal to the object specified by the other parameter; otherwise, lse.
        """
        ...
    def Export(self, contentType, password=None):
        """
        Export(self: X509Certificate, contentType: X509ContentType) -> Array[Byte]

            Exports the current System.Security.Cryptography.X509Certificates.X509Certificate object to a byte array in a format described by one of the

             System.Security.Cryptography.X509Certificates.X509ContentType values.

            contentType: One of the System.Security.Cryptography.X509Certificates.X509ContentType values that describes how to format the output data.

            Returns: An array of bytes that represents the current System.Security.Cryptography.X509Certificates.X509Certificate object.

        Export(self: X509Certificate, contentType: X509ContentType, password: str) -> Array[Byte]

            Exports the current System.Security.Cryptography.X509Certificates.X509Certificate object to a byte array in a format described by one of the

             System.Security.Cryptography.X509Certificates.X509ContentType values, and using the specified password.

            contentType: One of the System.Security.Cryptography.X509Certificates.X509ContentType values that describes how to format the output data.

            password: The password required to access the X.509 certificate data.

            Returns: An array of bytes that represents the current System.Security.Cryptography.X509Certificates.X509Certificate object.

        Export(self: X509Certificate, contentType: X509ContentType, password: SecureString) -> Array[Byte]

            Exports the current System.Security.Cryptography.X509Certificates.X509Certificate object to a byte array using the specified format and a password.

            contentType: One of the System.Security.Cryptography.X509Certificates.X509ContentType values that describes how to format the output data.

            password: The password required to access the X.509 certificate data.

            Returns: A byte array that represents the current System.Security.Cryptography.X509Certificates.X509Certificate object.
        """
        ...
    def FormatDate(self, *args):  # cannot find CLR method
        """
        FormatDate(date: DateTime) -> str

            Converts the specified date and time to a string.

            date: The date and time to convert.

            Returns: A string representation of the value of the System.DateTime object.
        """
        ...
    def GetCertHash(self, hashAlgorithm=None):
        """
        GetCertHash(self: X509Certificate) -> Array[Byte]

            Returns the hash value for the X.509v3 certificate as an array of bytes.

            Returns: The hash value for the X.509 certificate.

        GetCertHash(self: X509Certificate, hashAlgorithm: HashAlgorithmName) -> Array[Byte]
        """
        ...
    def GetCertHashString(self, hashAlgorithm=None):
        """
        GetCertHashString(self: X509Certificate) -> str

            Returns the SHA1 hash value for the X.509v3 certificate as a hexadecimal string.

            Returns: The hexadecimal string representation of the X.509 certificate hash value.

        GetCertHashString(self: X509Certificate, hashAlgorithm: HashAlgorithmName) -> str
        """
        ...
    def GetEffectiveDateString(self):
        """
        GetEffectiveDateString(self: X509Certificate) -> str

            Returns the effective date of this X.509v3 certificate.

            Returns: The effective date for this X.509 certificate.
        """
        ...
    def GetExpirationDateString(self):
        """
        GetExpirationDateString(self: X509Certificate) -> str

            Returns the expiration date of this X.509v3 certificate.

            Returns: The expiration date for this X.509 certificate.
        """
        ...
    def GetFormat(self):
        """
        GetFormat(self: X509Certificate) -> str

            Returns the name of the format of this X.509v3 certificate.

            Returns: The format of this X.509 certificate.
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: X509Certificate) -> int

            Returns the hash code for the X.509v3 certificate as an integer.

            Returns: The hash code for the X.509 certificate as an integer.
        """
        ...
    def GetIssuerName(self):
        """
        GetIssuerName(self: X509Certificate) -> str

            Returns the name of the certification authority that issued the X.509v3 certificate.

            Returns: The name of the certification authority that issued the X.509 certificate.
        """
        ...
    def GetKeyAlgorithm(self):
        """
        GetKeyAlgorithm(self: X509Certificate) -> str

            Returns the key algorithm information for this X.509v3 certificate as a string.

            Returns: The key algorithm information for this X.509 certificate as a string.
        """
        ...
    def GetKeyAlgorithmParameters(self):
        """
        GetKeyAlgorithmParameters(self: X509Certificate) -> Array[Byte]

            Returns the key algorithm parameters for the X.509v3 certificate as an array of bytes.

            Returns: The key algorithm parameters for the X.509 certificate as an array of bytes.
        """
        ...
    def GetKeyAlgorithmParametersString(self):
        """
        GetKeyAlgorithmParametersString(self: X509Certificate) -> str

            Returns the key algorithm parameters for the X.509v3 certificate as a hexadecimal string.

            Returns: The key algorithm parameters for the X.509 certificate as a hexadecimal string.
        """
        ...
    def GetName(self):
        """
        GetName(self: X509Certificate) -> str

            Returns the name of the principal to which the certificate was issued.

            Returns: The name of the principal to which the certificate was issued.
        """
        ...
    def GetPublicKey(self):
        """
        GetPublicKey(self: X509Certificate) -> Array[Byte]

            Returns the public key for the X.509v3 certificate as an array of bytes.

            Returns: The public key for the X.509 certificate as an array of bytes.
        """
        ...
    def GetPublicKeyString(self):
        """
        GetPublicKeyString(self: X509Certificate) -> str

            Returns the public key for the X.509v3 certificate as a hexadecimal string.

            Returns: The public key for the X.509 certificate as a hexadecimal string.
        """
        ...
    def GetRawCertData(self):
        """
        GetRawCertData(self: X509Certificate) -> Array[Byte]

            Returns the raw data for the entire X.509v3 certificate as an array of bytes.

            Returns: A byte array containing the X.509 certificate data.
        """
        ...
    def GetRawCertDataString(self):
        """
        GetRawCertDataString(self: X509Certificate) -> str

            Returns the raw data for the entire X.509v3 certificate as a hexadecimal string.

            Returns: The X.509 certificate data as a hexadecimal string.
        """
        ...
    def GetSerialNumber(self):
        """
        GetSerialNumber(self: X509Certificate) -> Array[Byte]

            Returns the serial number of the X.509v3 certificate as an array of bytes.

            Returns: The serial number of the X.509 certificate as an array of bytes.
        """
        ...
    def GetSerialNumberString(self):
        """
        GetSerialNumberString(self: X509Certificate) -> str

            Returns the serial number of the X.509v3 certificate as a hexadecimal string.

            Returns: The serial number of the X.509 certificate as a hexadecimal string.
        """
        ...
    def Import(self, *__args):
        """
        Import(self: X509Certificate, rawData: Array[Byte])

            Populates the System.Security.Cryptography.X509Certificates.X509Certificate object with data from a byte array.

            rawData: A byte array containing data from an X.509 certificate.

        Import(self: X509Certificate, rawData: Array[Byte], password: str, keyStorageFlags: X509KeyStorageFlags)

            Populates the System.Security.Cryptography.X509Certificates.X509Certificate object using data from a byte array, a password, and flags for determining how the private

             key is imported.

            rawData: A byte array containing data from an X.509 certificate.

            password: The password required to access the X.509 certificate data.

            keyStorageFlags: A bitwise combination of the enumeration values that control where and how to import the certificate.

        Import(self: X509Certificate, rawData: Array[Byte], password: SecureString, keyStorageFlags: X509KeyStorageFlags)

            Populates an System.Security.Cryptography.X509Certificates.X509Certificate object using data from a byte array, a password, and a key storage flag.

            rawData: A byte array that contains data from an X.509 certificate.

            password: The password required to access the X.509 certificate data.

            keyStorageFlags: A bitwise combination of the enumeration values that control where and how to import the certificate.

        Import(self: X509Certificate, fileName: str)

            Populates the System.Security.Cryptography.X509Certificates.X509Certificate object with information from a certificate file.

            fileName: The name of a certificate file represented as a string.

        Import(self: X509Certificate, fileName: str, password: str, keyStorageFlags: X509KeyStorageFlags)

            Populates the System.Security.Cryptography.X509Certificates.X509Certificate object with information from a certificate file, a password, and a

             System.Security.Cryptography.X509Certificates.X509KeyStorageFlags value.

            fileName: The name of a certificate file represented as a string.

            password: The password required to access the X.509 certificate data.

            keyStorageFlags: A bitwise combination of the enumeration values that control where and how to import the certificate.

        Import(self: X509Certificate, fileName: str, password: SecureString, keyStorageFlags: X509KeyStorageFlags)

            Populates an System.Security.Cryptography.X509Certificates.X509Certificate object with information from a certificate file, a password, and a key storage flag.

            fileName: The name of a certificate file.

            password: The password required to access the X.509 certificate data.

            keyStorageFlags: A bitwise combination of the enumeration values that control where and how to import the certificate.
        """
        ...
    def Reset(self):
        """
        Reset(self: X509Certificate)

            Resets the state of the System.Security.Cryptography.X509Certificates.X509Certificate2 object.
        """
        ...
    def ToString(self, fVerbose=None):
        """
        ToString(self: X509Certificate) -> str

            Returns a string representation of the current System.Security.Cryptography.X509Certificates.X509Certificate object.

            Returns: A string representation of the current System.Security.Cryptography.X509Certificates.X509Certificate object.

        ToString(self: X509Certificate, fVerbose: bool) -> str

            Returns a string representation of the current System.Security.Cryptography.X509Certificates.X509Certificate object, with extra information, if specified.

            fVerbose: ue to produce the verbose form of the string representation; otherwise, lse.

            Returns: A string representation of the current System.Security.Cryptography.X509Certificates.X509Certificate object.
        """
        ...
    def __eq__(self, *args):  # cannot find CLR method
        """x.__eq__(y) <==> x==yx.__eq__(y) <==> x==y"""
        ...
    def __ne__(self, *args): ...
    @property
    def Handle(self):
        """
        Gets a handle to a Microsoft Cryptographic API certificate context described by an unmanaged CERT_CONTEXT structure.

        Get: Handle(self: X509Certificate) -> IntPtr
        """
        ...
    @property
    def Issuer(self):
        """
        Gets the name of the certificate authority that issued the X.509v3 certificate.

        Get: Issuer(self: X509Certificate) -> str
        """
        ...
    @property
    def Subject(self):
        """
        Gets the subject distinguished name from the certificate.

        Get: Subject(self: X509Certificate) -> str
        """
        ...

class X509Certificate2(
    X509Certificate
):  # skipped bases: <type 'ISerializable'>, <type 'IDeserializationCallback'>, <type 'IDisposable'>
    """
    Represents an X.509 certificate.

    X509Certificate2()

    X509Certificate2(rawData: Array[Byte])

    X509Certificate2(rawData: Array[Byte], password: str)

    X509Certificate2(rawData: Array[Byte], password: SecureString)

    X509Certificate2(rawData: Array[Byte], password: str, keyStorageFlags: X509KeyStorageFlags)

    X509Certificate2(rawData: Array[Byte], password: SecureString, keyStorageFlags: X509KeyStorageFlags)

    X509Certificate2(fileName: str)

    X509Certificate2(fileName: str, password: str)

    X509Certificate2(fileName: str, password: SecureString)

    X509Certificate2(fileName: str, password: str, keyStorageFlags: X509KeyStorageFlags)

    X509Certificate2(fileName: str, password: SecureString, keyStorageFlags: X509KeyStorageFlags)

    X509Certificate2(handle: IntPtr)

    X509Certificate2(certificate: X509Certificate)
    """

    @staticmethod
    def GetCertContentType(*__args):
        """
        GetCertContentType(rawData: Array[Byte]) -> X509ContentType

            Indicates the type of certificate contained in a byte array.

            rawData: A byte array containing data from an X.509 certificate.

            Returns: An System.Security.Cryptography.X509Certificates.X509ContentType object.

        GetCertContentType(fileName: str) -> X509ContentType

            Indicates the type of certificate contained in a file.

            fileName: The name of a certificate file.

            Returns: An System.Security.Cryptography.X509Certificates.X509ContentType object.
        """
        ...
    def GetNameInfo(self, nameType, forIssuer):
        """
        GetNameInfo(self: X509Certificate2, nameType: X509NameType, forIssuer: bool) -> str

            Gets the subject and issuer names from a certificate.

            nameType: The System.Security.Cryptography.X509Certificates.X509NameType value for the subject.

            forIssuer: ue to include the issuer name; otherwise, lse.

            Returns: The name of the certificate.
        """
        ...
    def Verify(self):
        """
        Verify(self: X509Certificate2) -> bool

            Performs a X.509 chain validation using basic validation policy.

            Returns: ue if the validation succeeds; lse if the validation fails.
        """
        ...
    @property
    def Archived(self):
        """
        Gets or sets a value indicating that an X.509 certificate is archived.

        Get: Archived(self: X509Certificate2) -> bool

        Set: Archived(self: X509Certificate2) = value
        """
        ...
    @property
    def Extensions(self):
        """
        Gets a collection of System.Security.Cryptography.X509Certificates.X509Extension objects.

        Get: Extensions(self: X509Certificate2) -> X509ExtensionCollection
        """
        ...
    @property
    def FriendlyName(self):
        """
        Gets or sets the associated alias for a certificate.

        Get: FriendlyName(self: X509Certificate2) -> str

        Set: FriendlyName(self: X509Certificate2) = value
        """
        ...
    @property
    def HasPrivateKey(self):
        """
        Gets a value that indicates whether an System.Security.Cryptography.X509Certificates.X509Certificate2 object contains a private key.

        Get: HasPrivateKey(self: X509Certificate2) -> bool
        """
        ...
    @property
    def IssuerName(self):
        """
        Gets the distinguished name of the certificate issuer.

        Get: IssuerName(self: X509Certificate2) -> X500DistinguishedName
        """
        ...
    @property
    def NotAfter(self):
        """
        Gets the date in local time after which a certificate is no longer valid.

        Get: NotAfter(self: X509Certificate2) -> DateTime
        """
        ...
    @property
    def NotBefore(self):
        """
        Gets the date in local time on which a certificate becomes valid.

        Get: NotBefore(self: X509Certificate2) -> DateTime
        """
        ...
    @property
    def PrivateKey(self):
        """
        Gets or sets the System.Security.Cryptography.AsymmetricAlgorithm object that represents the private key associated with a certificate.

        Get: PrivateKey(self: X509Certificate2) -> AsymmetricAlgorithm

        Set: PrivateKey(self: X509Certificate2) = value
        """
        ...
    @property
    def PublicKey(self):
        """
        Gets a System.Security.Cryptography.X509Certificates.X509Certificate2.PublicKey object associated with a certificate.

        Get: PublicKey(self: X509Certificate2) -> PublicKey
        """
        ...
    @property
    def RawData(self):
        """
        Gets the raw data of a certificate.

        Get: RawData(self: X509Certificate2) -> Array[Byte]
        """
        ...
    @property
    def SerialNumber(self):
        """
        Gets the serial number of a certificate.

        Get: SerialNumber(self: X509Certificate2) -> str
        """
        ...
    @property
    def SignatureAlgorithm(self):
        """
        Gets the algorithm used to create the signature of a certificate.

        Get: SignatureAlgorithm(self: X509Certificate2) -> Oid
        """
        ...
    @property
    def SubjectName(self):
        """
        Gets the subject distinguished name from a certificate.

        Get: SubjectName(self: X509Certificate2) -> X500DistinguishedName
        """
        ...
    @property
    def Thumbprint(self):
        """
        Gets the thumbprint of a certificate.

        Get: Thumbprint(self: X509Certificate2) -> str
        """
        ...
    @property
    def Version(self):
        """
        Gets the X.509 format version of a certificate.

        Get: Version(self: X509Certificate2) -> int
        """
        ...

class X509CertificateCollection(
    CollectionBase
):  # skipped bases: <type 'IList'>, <type 'ICollection'>, <type 'IEnumerable'>
    """
    Defines a collection that stores System.Security.Cryptography.X509Certificates.X509Certificate objects.

    X509CertificateCollection()

    X509CertificateCollection(value: X509CertificateCollection)

    X509CertificateCollection(value: Array[X509Certificate])
    """

    def Add(self, value):
        """
        Add(self: X509CertificateCollection, value: X509Certificate) -> int

            Adds an System.Security.Cryptography.X509Certificates.X509Certificate with the specified value to the current

             System.Security.Cryptography.X509Certificates.X509CertificateCollection.

            value: The System.Security.Cryptography.X509Certificates.X509Certificate to add to the current System.Security.Cryptography.X509Certificates.X509CertificateCollection.

            Returns: The index into the current System.Security.Cryptography.X509Certificates.X509CertificateCollection at which the new

             System.Security.Cryptography.X509Certificates.X509Certificate was inserted.
        """
        ...
    def AddRange(self, value):
        """
        AddRange(self: X509CertificateCollection, value: Array[X509Certificate])

            Copies the elements of an array of type System.Security.Cryptography.X509Certificates.X509Certificate to the end of the current

             System.Security.Cryptography.X509Certificates.X509CertificateCollection.

            value: The array of type System.Security.Cryptography.X509Certificates.X509Certificate containing the objects to add to the current

             System.Security.Cryptography.X509Certificates.X509CertificateCollection.

        AddRange(self: X509CertificateCollection, value: X509CertificateCollection)

            Copies the elements of the specified System.Security.Cryptography.X509Certificates.X509CertificateCollection to the end of the current

             System.Security.Cryptography.X509Certificates.X509CertificateCollection.

            value: The System.Security.Cryptography.X509Certificates.X509CertificateCollection containing the objects to add to the collection.
        """
        ...
    def Contains(self, value):
        """
        Contains(self: X509CertificateCollection, value: X509Certificate) -> bool

            Gets a value indicating whether the current System.Security.Cryptography.X509Certificates.X509CertificateCollection contains the specified

             System.Security.Cryptography.X509Certificates.X509Certificate.

            value: The System.Security.Cryptography.X509Certificates.X509Certificate to locate.

            Returns: ue if the System.Security.Cryptography.X509Certificates.X509Certificate is contained in this collection; otherwise, lse.
        """
        ...
    def CopyTo(self, array, index):
        """
        CopyTo(self: X509CertificateCollection, array: Array[X509Certificate], index: int)

            Copies the System.Security.Cryptography.X509Certificates.X509Certificate values in the current System.Security.Cryptography.X509Certificates.X509CertificateCollection

             to a one-dimensional System.Array instance at the specified index.

            array: The one-dimensional System.Array that is the destination of the values copied from System.Security.Cryptography.X509Certificates.X509CertificateCollection.

            index: The index into array to begin copying.
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: X509CertificateCollection) -> int

            Builds a hash value based on all values contained in the current System.Security.Cryptography.X509Certificates.X509CertificateCollection.

            Returns: A hash value based on all values contained in the current System.Security.Cryptography.X509Certificates.X509CertificateCollection.
        """
        ...
    def IndexOf(self, value):
        """
        IndexOf(self: X509CertificateCollection, value: X509Certificate) -> int

            Returns the index of the specified System.Security.Cryptography.X509Certificates.X509Certificate in the current

             System.Security.Cryptography.X509Certificates.X509CertificateCollection.

            value: The System.Security.Cryptography.X509Certificates.X509Certificate to locate.

            Returns: The index of the System.Security.Cryptography.X509Certificates.X509Certificate specified by the value parameter in the

             System.Security.Cryptography.X509Certificates.X509CertificateCollection, if found; otherwise, -1.
        """
        ...
    def Insert(self, index, value):
        """
        Insert(self: X509CertificateCollection, index: int, value: X509Certificate)

            Inserts a System.Security.Cryptography.X509Certificates.X509Certificate into the current System.Security.Cryptography.X509Certificates.X509CertificateCollection at the

             specified index.

            index: The zero-based index where value should be inserted.

            value: The System.Security.Cryptography.X509Certificates.X509Certificate to insert.
        """
        ...
    def Remove(self, value):
        """
        Remove(self: X509CertificateCollection, value: X509Certificate)

            Removes a specific System.Security.Cryptography.X509Certificates.X509Certificate from the current

             System.Security.Cryptography.X509Certificates.X509CertificateCollection.

            value: The System.Security.Cryptography.X509Certificates.X509Certificate to remove from the current System.Security.Cryptography.X509Certificates.X509CertificateCollection.
        """
        ...
    def X509CertificateEnumerator(self, *args):  # cannot find CLR method
        """X509CertificateEnumerator(mappings: X509CertificateCollection)"""
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
    def InnerList(self):
        """Gets an System.Collections.ArrayList containing the list of elements in the System.Collections.CollectionBase instance."""
        ...
    @property
    def List(self):
        """Gets an System.Collections.IList containing the list of elements in the System.Collections.CollectionBase instance."""
        ...
    X509CertificateEnumerator = None

class X509Certificate2Collection(
    X509CertificateCollection
):  # skipped bases: <type 'IList'>, <type 'ICollection'>, <type 'IEnumerable'>
    """
    Represents a collection of System.Security.Cryptography.X509Certificates.X509Certificate2 objects. This class cannot be inherited.

    X509Certificate2Collection()

    X509Certificate2Collection(certificate: X509Certificate2)

    X509Certificate2Collection(certificates: X509Certificate2Collection)

    X509Certificate2Collection(certificates: Array[X509Certificate2])
    """

    def Export(self, contentType, password=None):
        """
        Export(self: X509Certificate2Collection, contentType: X509ContentType) -> Array[Byte]

            Exports X.509 certificate information into a byte array.

            contentType: A supported System.Security.Cryptography.X509Certificates.X509ContentType object.

            Returns: X.509 certificate information in a byte array.

        Export(self: X509Certificate2Collection, contentType: X509ContentType, password: str) -> Array[Byte]

            Exports X.509 certificate information into a byte array using a password.

            contentType: A supported System.Security.Cryptography.X509Certificates.X509ContentType object.

            password: A string used to protect the byte array.

            Returns: X.509 certificate information in a byte array.
        """
        ...
    def Find(self, findType, findValue, validOnly):
        """
        Find(self: X509Certificate2Collection, findType: X509FindType, findValue: object, validOnly: bool) -> X509Certificate2Collection

            Searches an System.Security.Cryptography.X509Certificates.X509Certificate2Collection object using the search criteria specified by the

             System.Security.Cryptography.X509Certificates.X509FindType enumeration and the findValue object.

            findType: One of the System.Security.Cryptography.X509Certificates.X509FindType  values.

            findValue: The search criteria as an object.

            validOnly: ue to allow only valid certificates to be returned from the search; otherwise, lse.

            Returns: An System.Security.Cryptography.X509Certificates.X509Certificate2Collection object.
        """
        ...
    def Import(self, *__args):
        """
        Import(self: X509Certificate2Collection, rawData: Array[Byte])

            Imports a certificate in the form of a byte array into a System.Security.Cryptography.X509Certificates.X509Certificate2Collection object.

            rawData: A byte array containing data from an X.509 certificate.

        Import(self: X509Certificate2Collection, fileName: str)

            Imports a certificate file into a System.Security.Cryptography.X509Certificates.X509Certificate2Collection object.

            fileName: The name of the file containing the certificate information.

        Import(self: X509Certificate2Collection, rawData: Array[Byte], password: str, keyStorageFlags: X509KeyStorageFlags)

            Imports a certificate, in the form of a byte array that requires a password to access the certificate, into a

             System.Security.Cryptography.X509Certificates.X509Certificate2Collection object.

            rawData: A byte array containing data from an System.Security.Cryptography.X509Certificates.X509Certificate2 object.

            password: The password required to access the certificate information.

            keyStorageFlags: A bitwise combination of the enumeration values that control how and where the certificate is imported.

        Import(self: X509Certificate2Collection, fileName: str, password: str, keyStorageFlags: X509KeyStorageFlags)

            Imports a certificate file that requires a password into a System.Security.Cryptography.X509Certificates.X509Certificate2Collection object.

            fileName: The name of the file containing the certificate information.

            password: The password required to access the certificate information.

            keyStorageFlags: A bitwise combination of the enumeration values that control how and where the certificate is imported.
        """
        ...
    def RemoveRange(self, certificates):
        """
        RemoveRange(self: X509Certificate2Collection, certificates: Array[X509Certificate2])

            Removes multiple System.Security.Cryptography.X509Certificates.X509Certificate2 objects in an array from an

             System.Security.Cryptography.X509Certificates.X509Certificate2Collection object.

            certificates: An array of System.Security.Cryptography.X509Certificates.X509Certificate2 objects.

        RemoveRange(self: X509Certificate2Collection, certificates: X509Certificate2Collection)

            Removes multiple System.Security.Cryptography.X509Certificates.X509Certificate2 objects in an System.Security.Cryptography.X509Certificates.X509Certificate2Collection

             object from another System.Security.Cryptography.X509Certificates.X509Certificate2Collection object.

            certificates: An System.Security.Cryptography.X509Certificates.X509Certificate2Collection object.
        """
        ...
    @property
    def InnerList(self):
        """Gets an System.Collections.ArrayList containing the list of elements in the System.Collections.CollectionBase instance."""
        ...
    @property
    def List(self):
        """Gets an System.Collections.IList containing the list of elements in the System.Collections.CollectionBase instance."""
        ...

class X509Certificate2Enumerator(object, IEnumerator):
    """Supports a simple iteration over a System.Security.Cryptography.X509Certificates.X509Certificate2Collection object. This class cannot be inherited."""

    @property
    def Current(self):
        """
        Gets the current element in the System.Security.Cryptography.X509Certificates.X509Certificate2Collection object.

        Get: Current(self: X509Certificate2Enumerator) -> X509Certificate2
        """
        ...

class X509Chain(object, IDisposable):
    """
    Represents a chain-building engine for System.Security.Cryptography.X509Certificates.X509Certificate2 certificates.

    X509Chain()

    X509Chain(useMachineContext: bool)

    X509Chain(chainContext: IntPtr)
    """

    def Build(self, certificate):
        """
        Build(self: X509Chain, certificate: X509Certificate2) -> bool

            Builds an X.509 chain using the policy specified in System.Security.Cryptography.X509Certificates.X509ChainPolicy.

            certificate: An System.Security.Cryptography.X509Certificates.X509Certificate2 object.

            Returns: ue if the X.509 certificate is valid; otherwise, lse.
        """
        ...
    @staticmethod
    def Create():
        """
        Create() -> X509Chain

            Creates an System.Security.Cryptography.X509Certificates.X509Chain object after querying for the mapping defined in the CryptoConfig file, and maps the chain to that

             mapping.

            Returns: An System.Security.Cryptography.X509Certificates.X509Chain object.
        """
        ...
    def Reset(self):
        """
        Reset(self: X509Chain)

            Clears the current System.Security.Cryptography.X509Certificates.X509Chain object.
        """
        ...
    @property
    def ChainContext(self):
        """
        Gets a handle to an X.509 chain.

        Get: ChainContext(self: X509Chain) -> IntPtr
        """
        ...
    @property
    def ChainElements(self):
        """
        Gets a collection of System.Security.Cryptography.X509Certificates.X509ChainElement objects.

        Get: ChainElements(self: X509Chain) -> X509ChainElementCollection
        """
        ...
    @property
    def ChainPolicy(self):
        """
        Gets or sets the System.Security.Cryptography.X509Certificates.X509ChainPolicy to use when building an X.509 certificate chain.

        Get: ChainPolicy(self: X509Chain) -> X509ChainPolicy

        Set: ChainPolicy(self: X509Chain) = value
        """
        ...
    @property
    def ChainStatus(self):
        """
        Gets the status of each element in an System.Security.Cryptography.X509Certificates.X509Chain object.

        Get: ChainStatus(self: X509Chain) -> Array[X509ChainStatus]
        """
        ...
    @property
    def SafeHandle(self):
        """
        Gets a safe handle for this System.Security.Cryptography.X509Certificates.X509Chain instance.

        Get: SafeHandle(self: X509Chain) -> SafeX509ChainHandle
        """
        ...

class X509ChainElement:  # skipped bases: <type 'object'>
    """Represents an element of an X.509 chain."""

    @property
    def Certificate(self):
        """
        Gets the X.509 certificate at a particular chain element.

        Get: Certificate(self: X509ChainElement) -> X509Certificate2
        """
        ...
    @property
    def ChainElementStatus(self):
        """
        Gets the error status of the current X.509 certificate in a chain.

        Get: ChainElementStatus(self: X509ChainElement) -> Array[X509ChainStatus]
        """
        ...
    @property
    def Information(self):
        """
        Gets additional error information from an unmanaged certificate chain structure.

        Get: Information(self: X509ChainElement) -> str
        """
        ...

class X509ChainElementCollection(object, ICollection):  # skipped bases: <type 'IEnumerable'>
    """Represents a collection of System.Security.Cryptography.X509Certificates.X509ChainElement objects. This class cannot be inherited."""

    def GetEnumerator(self):
        """
        GetEnumerator(self: X509ChainElementCollection) -> X509ChainElementEnumerator

            Gets an System.Security.Cryptography.X509Certificates.X509ChainElementEnumerator object that can be used to navigate through a collection of chain elements.

            Returns: An System.Security.Cryptography.X509Certificates.X509ChainElementEnumerator object.
        """
        ...
    def __getitem__(self, *args):  # cannot find CLR method
        """x.__getitem__(y) <==> x[y]"""
        ...
    def __len__(self, *args):  # cannot find CLR method
        """x.__len__() <==> len(x)"""
        ...
    @property
    def Count(self):
        """
        Gets the number of elements in the collection.

        Get: Count(self: X509ChainElementCollection) -> int
        """
        ...
    @property
    def IsSynchronized(self):
        """
        Gets a value indicating whether the collection of chain elements is synchronized.

        Get: IsSynchronized(self: X509ChainElementCollection) -> bool
        """
        ...
    @property
    def SyncRoot(self):
        """
        Gets an object that can be used to synchronize access to an System.Security.Cryptography.X509Certificates.X509ChainElementCollection object.

        Get: SyncRoot(self: X509ChainElementCollection) -> object
        """
        ...

class X509ChainElementEnumerator(object, IEnumerator):
    """Supports a simple iteration over an System.Security.Cryptography.X509Certificates.X509ChainElementCollection. This class cannot be inherited."""

    @property
    def Current(self):
        """
        Gets the current element in the System.Security.Cryptography.X509Certificates.X509ChainElementCollection.

        Get: Current(self: X509ChainElementEnumerator) -> X509ChainElement
        """
        ...

class X509ChainPolicy:  # skipped bases: <type 'object'>
    """
    Represents the chain policy to be applied when building an X509 certificate chain. This class cannot be inherited.

    X509ChainPolicy()
    """

    def Reset(self):
        """
        Reset(self: X509ChainPolicy)

            Resets the System.Security.Cryptography.X509Certificates.X509ChainPolicy members to their default values.
        """
        ...
    @property
    def ApplicationPolicy(self):
        """
        Gets a collection of object identifiers (OIDs) specifying which application policies or enhanced key usages (EKUs) the certificate supports.

        Get: ApplicationPolicy(self: X509ChainPolicy) -> OidCollection
        """
        ...
    @property
    def CertificatePolicy(self):
        """
        Gets a collection of object identifiers (OIDs) specifying which certificate policies the certificate supports.

        Get: CertificatePolicy(self: X509ChainPolicy) -> OidCollection
        """
        ...
    @property
    def ExtraStore(self):
        """
        Represents an additional collection of certificates that can be searched by the chaining engine when validating a certificate chain.

        Get: ExtraStore(self: X509ChainPolicy) -> X509Certificate2Collection
        """
        ...
    @property
    def RevocationFlag(self):
        """
        Gets or sets values for X509 revocation flags.

        Get: RevocationFlag(self: X509ChainPolicy) -> X509RevocationFlag

        Set: RevocationFlag(self: X509ChainPolicy) = value
        """
        ...
    @property
    def RevocationMode(self):
        """
        Gets or sets values for X509 certificate revocation mode.

        Get: RevocationMode(self: X509ChainPolicy) -> X509RevocationMode

        Set: RevocationMode(self: X509ChainPolicy) = value
        """
        ...
    @property
    def UrlRetrievalTimeout(self):
        """
        Gets the time span that elapsed during online revocation verification or downloading the certificate revocation list (CRL).

        Get: UrlRetrievalTimeout(self: X509ChainPolicy) -> TimeSpan

        Set: UrlRetrievalTimeout(self: X509ChainPolicy) = value
        """
        ...
    @property
    def VerificationFlags(self):
        """
        Gets verification flags for the certificate.

        Get: VerificationFlags(self: X509ChainPolicy) -> X509VerificationFlags

        Set: VerificationFlags(self: X509ChainPolicy) = value
        """
        ...
    @property
    def VerificationTime(self):
        """
        The time that the certificate was verified expressed in local time.

        Get: VerificationTime(self: X509ChainPolicy) -> DateTime

        Set: VerificationTime(self: X509ChainPolicy) = value
        """
        ...

class X509ChainStatus:  # skipped bases: <type 'object'>
    """Provides a simple structure for storing X509 chain status and error information."""

    @property
    def Status(self):
        """
        Specifies the status of the X509 chain.

        Get: Status(self: X509ChainStatus) -> X509ChainStatusFlags

        Set: Status(self: X509ChainStatus) = value
        """
        ...
    @property
    def StatusInformation(self):
        """
        Specifies a description of the System.Security.Cryptography.X509Certificates.X509Chain.ChainStatus value.

        Get: StatusInformation(self: X509ChainStatus) -> str

        Set: StatusInformation(self: X509ChainStatus) = value
        """
        ...

class X509ChainStatusFlags(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Defines the status of an X509 chain.

    enum (flags) X509ChainStatusFlags, values: CtlNotSignatureValid (262144), CtlNotTimeValid (131072), CtlNotValidForUsage (524288), Cyclic (128), ExplicitDistrust (67108864), HasExcludedNameConstraint (32768), HasNotDefinedNameConstraint (8192), HasNotPermittedNameConstraint (16384), HasNotSupportedCriticalExtension (134217728), HasNotSupportedNameConstraint (4096), HasWeakSignature (1048576), InvalidBasicConstraints (1024), InvalidExtension (256), InvalidNameConstraints (2048), InvalidPolicyConstraints (512), NoError (0), NoIssuanceChainPolicy (33554432), NotSignatureValid (8), NotTimeNested (2), NotTimeValid (1), NotValidForUsage (16), OfflineRevocation (16777216), PartialChain (65536), RevocationStatusUnknown (64), Revoked (4), UntrustedRoot (32)
    """

    CtlNotSignatureValid = None
    CtlNotTimeValid = None
    CtlNotValidForUsage = None
    Cyclic = None
    ExplicitDistrust = None
    HasExcludedNameConstraint = None
    HasNotDefinedNameConstraint = None
    HasNotPermittedNameConstraint = None
    HasNotSupportedCriticalExtension = None
    HasNotSupportedNameConstraint = None
    HasWeakSignature = None
    InvalidBasicConstraints = None
    InvalidExtension = None
    InvalidNameConstraints = None
    InvalidPolicyConstraints = None
    NoError = None
    NoIssuanceChainPolicy = None
    NotSignatureValid = None
    NotTimeNested = None
    NotTimeValid = None
    NotValidForUsage = None
    OfflineRevocation = None
    PartialChain = None
    RevocationStatusUnknown = None
    Revoked = None
    UntrustedRoot = None
    value__ = None

class X509ContentType(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies the format of an X.509 certificate.

    enum X509ContentType, values: Authenticode (6), Cert (1), Pfx (3), Pkcs12 (3), Pkcs7 (5), SerializedCert (2), SerializedStore (4), Unknown (0)
    """

    Authenticode = None
    Cert = None
    Pfx = None
    Pkcs12 = None
    Pkcs7 = None
    SerializedCert = None
    SerializedStore = None
    Unknown = None
    value__ = None

class X509EnhancedKeyUsageExtension(X509Extension):
    """
    Defines the collection of object identifiers (OIDs) that indicates the applications that use the key. This class cannot be inherited.

    X509EnhancedKeyUsageExtension()

    X509EnhancedKeyUsageExtension(enhancedKeyUsages: OidCollection, critical: bool)

    X509EnhancedKeyUsageExtension(encodedEnhancedKeyUsages: AsnEncodedData, critical: bool)
    """

    @property
    def EnhancedKeyUsages(self):
        """
        Gets the collection of object identifiers (OIDs) that indicate the applications that use the key.

        Get: EnhancedKeyUsages(self: X509EnhancedKeyUsageExtension) -> OidCollection
        """
        ...

class X509ExtensionCollection(object, ICollection):  # skipped bases: <type 'IEnumerable'>
    """
    Represents a collection of System.Security.Cryptography.X509Certificates.X509Extension objects. This class cannot be inherited.

    X509ExtensionCollection()
    """

    def Add(self, extension):
        """
        Add(self: X509ExtensionCollection, extension: X509Extension) -> int

            Adds an System.Security.Cryptography.X509Certificates.X509Extension object to an System.Security.Cryptography.X509Certificates.X509ExtensionCollection object.

            extension: An System.Security.Cryptography.X509Certificates.X509Extension  object to add to the System.Security.Cryptography.X509Certificates.X509ExtensionCollection object.

            Returns: The index at which the extension parameter was added.
        """
        ...
    def GetEnumerator(self):
        """
        GetEnumerator(self: X509ExtensionCollection) -> X509ExtensionEnumerator

            Returns an enumerator that can iterate through an System.Security.Cryptography.X509Certificates.X509ExtensionCollection object.

            Returns: An System.Security.Cryptography.X509Certificates.X509ExtensionEnumerator object to use to iterate through the

             System.Security.Cryptography.X509Certificates.X509ExtensionCollection object.
        """
        ...
    def __add__(self, *args):  # cannot find CLR method
        """x.__add__(y) <==> x+y"""
        ...
    def __getitem__(self, *args):  # cannot find CLR method
        """x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y]"""
        ...
    def __len__(self, *args):  # cannot find CLR method
        """x.__len__() <==> len(x)"""
        ...
    @property
    def Count(self):
        """
        Gets the number of System.Security.Cryptography.X509Certificates.X509Extension objects in a System.Security.Cryptography.X509Certificates.X509ExtensionCollection object.

        Get: Count(self: X509ExtensionCollection) -> int
        """
        ...
    @property
    def IsSynchronized(self):
        """
        Gets a value indicating whether the collection is guaranteed to be thread safe.

        Get: IsSynchronized(self: X509ExtensionCollection) -> bool
        """
        ...
    @property
    def SyncRoot(self):
        """
        Gets an object that you can use to synchronize access to the System.Security.Cryptography.X509Certificates.X509ExtensionCollection object.

        Get: SyncRoot(self: X509ExtensionCollection) -> object
        """
        ...

class X509ExtensionEnumerator(object, IEnumerator):
    """Supports a simple iteration over a System.Security.Cryptography.X509Certificates.X509ExtensionCollection. This class cannot be inherited."""

    @property
    def Current(self):
        """
        Gets the current element in the System.Security.Cryptography.X509Certificates.X509ExtensionCollection.

        Get: Current(self: X509ExtensionEnumerator) -> X509Extension
        """
        ...

class X509FindType(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies the type of value the System.Security.Cryptography.X509Certificates.X509Certificate2Collection.Find(System.Security.Cryptography.X509Certificates.X509FindType,System.Object,System.Boolean) method searches for.

    enum X509FindType, values: FindByApplicationPolicy (10), FindByCertificatePolicy (11), FindByExtension (12), FindByIssuerDistinguishedName (4), FindByIssuerName (3), FindByKeyUsage (13), FindBySerialNumber (5), FindBySubjectDistinguishedName (2), FindBySubjectKeyIdentifier (14), FindBySubjectName (1), FindByTemplateName (9), FindByThumbprint (0), FindByTimeExpired (8), FindByTimeNotYetValid (7), FindByTimeValid (6)
    """

    FindByApplicationPolicy = None
    FindByCertificatePolicy = None
    FindByExtension = None
    FindByIssuerDistinguishedName = None
    FindByIssuerName = None
    FindByKeyUsage = None
    FindBySerialNumber = None
    FindBySubjectDistinguishedName = None
    FindBySubjectKeyIdentifier = None
    FindBySubjectName = None
    FindByTemplateName = None
    FindByThumbprint = None
    FindByTimeExpired = None
    FindByTimeNotYetValid = None
    FindByTimeValid = None
    value__ = None

class X509IncludeOption(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies how much of the X.509 certificate chain should be included in the X.509 data.

    enum X509IncludeOption, values: EndCertOnly (2), ExcludeRoot (1), None (0), WholeChain (3)
    """

    EndCertOnly = None
    ExcludeRoot = None

    value__ = None
    WholeChain = None

class X509KeyStorageFlags(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Defines where and how to import the private key of an X.509 certificate.

    enum (flags) X509KeyStorageFlags, values: DefaultKeySet (0), EphemeralKeySet (32), Exportable (4), MachineKeySet (2), PersistKeySet (16), UserKeySet (1), UserProtected (8)
    """

    DefaultKeySet = None
    EphemeralKeySet = None
    Exportable = None
    MachineKeySet = None
    PersistKeySet = None
    UserKeySet = None
    UserProtected = None
    value__ = None

class X509KeyUsageExtension(X509Extension):
    """
    Defines the usage of a key contained within an X.509 certificate.  This class cannot be inherited.

    X509KeyUsageExtension()

    X509KeyUsageExtension(keyUsages: X509KeyUsageFlags, critical: bool)

    X509KeyUsageExtension(encodedKeyUsage: AsnEncodedData, critical: bool)
    """

    @property
    def KeyUsages(self):
        """
        Gets the key usage flag associated with the certificate.

        Get: KeyUsages(self: X509KeyUsageExtension) -> X509KeyUsageFlags
        """
        ...

class X509KeyUsageFlags(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Defines how the certificate key can be used. If this value is not defined, the key can be used for any purpose.

    enum (flags) X509KeyUsageFlags, values: CrlSign (2), DataEncipherment (16), DecipherOnly (32768), DigitalSignature (128), EncipherOnly (1), KeyAgreement (8), KeyCertSign (4), KeyEncipherment (32), None (0), NonRepudiation (64)
    """

    CrlSign = None
    DataEncipherment = None
    DecipherOnly = None
    DigitalSignature = None
    EncipherOnly = None
    KeyAgreement = None
    KeyCertSign = None
    KeyEncipherment = None

    NonRepudiation = None
    value__ = None

class X509NameType(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies the type of name the X509 certificate contains.

    enum X509NameType, values: DnsFromAlternativeName (4), DnsName (3), EmailName (1), SimpleName (0), UpnName (2), UrlName (5)
    """

    DnsFromAlternativeName = None
    DnsName = None
    EmailName = None
    SimpleName = None
    UpnName = None
    UrlName = None
    value__ = None

class X509RevocationFlag(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies which X509 certificates in the chain should be checked for revocation.

    enum X509RevocationFlag, values: EndCertificateOnly (0), EntireChain (1), ExcludeRoot (2)
    """

    EndCertificateOnly = None
    EntireChain = None
    ExcludeRoot = None
    value__ = None

class X509RevocationMode(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies the mode used to check for X509 certificate revocation.

    enum X509RevocationMode, values: NoCheck (0), Offline (2), Online (1)
    """

    NoCheck = None
    Offline = None
    Online = None
    value__ = None

class X509Store(object, IDisposable):
    """
    Represents an X.509 store, which is a physical store where certificates are persisted and managed. This class cannot be inherited.

    X509Store()

    X509Store(storeName: str)

    X509Store(storeName: StoreName)

    X509Store(storeLocation: StoreLocation)

    X509Store(storeName: StoreName, storeLocation: StoreLocation)

    X509Store(storeName: str, storeLocation: StoreLocation)

    X509Store(storeHandle: IntPtr)
    """

    def Add(self, certificate):
        """
        Add(self: X509Store, certificate: X509Certificate2)

            Adds a certificate to an X.509 certificate store.

            certificate: The certificate to add.
        """
        ...
    def AddRange(self, certificates):
        """
        AddRange(self: X509Store, certificates: X509Certificate2Collection)

            Adds a collection of certificates to an X.509 certificate store.

            certificates: The collection of certificates to add.
        """
        ...
    def Close(self):
        """
        Close(self: X509Store)

            Closes an X.509 certificate store.
        """
        ...
    def Open(self, flags):
        """
        Open(self: X509Store, flags: OpenFlags)

            Opens an X.509 certificate store or creates a new store, depending on System.Security.Cryptography.X509Certificates.OpenFlags flag settings.

            flags: A bitwise combination of enumeration values that specifies the way to open the X.509 certificate store.
        """
        ...
    def Remove(self, certificate):
        """
        Remove(self: X509Store, certificate: X509Certificate2)

            Removes a certificate from an X.509 certificate store.

            certificate: The certificate to remove.
        """
        ...
    def RemoveRange(self, certificates):
        """
        RemoveRange(self: X509Store, certificates: X509Certificate2Collection)

            Removes a range of certificates from an X.509 certificate store.

            certificates: A range of certificates to remove.
        """
        ...
    def __add__(self, *args):  # cannot find CLR method
        """x.__add__(y) <==> x+y"""
        ...
    @property
    def Certificates(self):
        """
        Returns a collection of certificates located in an X.509 certificate store.

        Get: Certificates(self: X509Store) -> X509Certificate2Collection
        """
        ...
    @property
    def Location(self):
        """
        Gets the location of the X.509 certificate store.

        Get: Location(self: X509Store) -> StoreLocation
        """
        ...
    @property
    def Name(self):
        """
        Gets the name of the X.509 certificate store.

        Get: Name(self: X509Store) -> str
        """
        ...
    @property
    def StoreHandle(self):
        """
        Gets an System.IntPtr handle to an ERTSTORE store.

        Get: StoreHandle(self: X509Store) -> IntPtr
        """
        ...

class X509SubjectKeyIdentifierExtension(X509Extension):
    """
    Defines a string that identifies a certificate's subject key identifier (SKI). This class cannot be inherited.

    X509SubjectKeyIdentifierExtension()

    X509SubjectKeyIdentifierExtension(subjectKeyIdentifier: str, critical: bool)

    X509SubjectKeyIdentifierExtension(subjectKeyIdentifier: Array[Byte], critical: bool)

    X509SubjectKeyIdentifierExtension(encodedSubjectKeyIdentifier: AsnEncodedData, critical: bool)

    X509SubjectKeyIdentifierExtension(key: PublicKey, critical: bool)

    X509SubjectKeyIdentifierExtension(key: PublicKey, algorithm: X509SubjectKeyIdentifierHashAlgorithm, critical: bool)
    """

    @property
    def SubjectKeyIdentifier(self):
        """
        Gets a string that represents the subject key identifier (SKI) for a certificate.

        Get: SubjectKeyIdentifier(self: X509SubjectKeyIdentifierExtension) -> str
        """
        ...

class X509SubjectKeyIdentifierHashAlgorithm(
    Enum
):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Defines the type of hash algorithm to use with the System.Security.Cryptography.X509Certificates.X509SubjectKeyIdentifierExtension class.

    enum X509SubjectKeyIdentifierHashAlgorithm, values: CapiSha1 (2), Sha1 (0), ShortSha1 (1)
    """

    CapiSha1 = None
    Sha1 = None
    ShortSha1 = None
    value__ = None

class X509VerificationFlags(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies conditions under which verification of certificates in the X509 chain should be conducted.

    enum (flags) X509VerificationFlags, values: AllFlags (4095), AllowUnknownCertificateAuthority (16), IgnoreCertificateAuthorityRevocationUnknown (1024), IgnoreCtlNotTimeValid (2), IgnoreCtlSignerRevocationUnknown (512), IgnoreEndRevocationUnknown (256), IgnoreInvalidBasicConstraints (8), IgnoreInvalidName (64), IgnoreInvalidPolicy (128), IgnoreNotTimeNested (4), IgnoreNotTimeValid (1), IgnoreRootRevocationUnknown (2048), IgnoreWrongUsage (32), NoFlag (0)
    """

    AllFlags = None
    AllowUnknownCertificateAuthority = None
    IgnoreCertificateAuthorityRevocationUnknown = None
    IgnoreCtlNotTimeValid = None
    IgnoreCtlSignerRevocationUnknown = None
    IgnoreEndRevocationUnknown = None
    IgnoreInvalidBasicConstraints = None
    IgnoreInvalidName = None
    IgnoreInvalidPolicy = None
    IgnoreNotTimeNested = None
    IgnoreNotTimeValid = None
    IgnoreRootRevocationUnknown = None
    IgnoreWrongUsage = None
    NoFlag = None
    value__ = None
