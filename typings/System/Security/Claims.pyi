# encoding: utf-8
# module System.Security.Claims calls itself Claims
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class Claim: # skipped bases: <type 'object'>
    """
    Represents a claim.

    Claim(reader: BinaryReader)

    Claim(reader: BinaryReader, subject: ClaimsIdentity)

    Claim(type: str, value: str)

    Claim(type: str, value: str, valueType: str)

    Claim(type: str, value: str, valueType: str, issuer: str)

    Claim(type: str, value: str, valueType: str, issuer: str, originalIssuer: str)

    Claim(type: str, value: str, valueType: str, issuer: str, originalIssuer: str, subject: ClaimsIdentity)
    """
    def Clone(self, identity=None):
        """
        Clone(self: Claim) -> Claim

            Returns a new System.Security.Claims.Claim object copied from this object. The new claim does not have a subject.

            Returns: The new claim object.

        Clone(self: Claim, identity: ClaimsIdentity) -> Claim

            Returns a new System.Security.Claims.Claim object copied from this object. The subject of the new claim is set to the specified ClaimsIdentity.

            identity: The intended subject of the new claim.

            Returns: The new claim object.
        """
        ...

    def ToString(self):
        """
        ToString(self: Claim) -> str

            Returns a string representation of this System.Security.Claims.Claim object.

            Returns: The string representation of this System.Security.Claims.Claim object.
        """
        ...

    def WriteTo(self, writer):
        """ WriteTo(self: Claim, writer: BinaryWriter) """
        ...

    @property
    def CustomSerializationData(self):
        """  """
        ...

    @property
    def Issuer(self):
        """
        Gets the issuer of the claim.

        Get: Issuer(self: Claim) -> str
        """
        ...

    @property
    def OriginalIssuer(self):
        """
        Gets the original issuer of the claim.

        Get: OriginalIssuer(self: Claim) -> str
        """
        ...

    @property
    def Properties(self):
        """
        Gets a dictionary that contains additional properties associated with this claim.

        Get: Properties(self: Claim) -> IDictionary[str, str]
        """
        ...

    @property
    def Subject(self):
        """
        Gets the subject of the claim.

        Get: Subject(self: Claim) -> ClaimsIdentity
        """
        ...

    @property
    def Type(self):
        """
        Gets the claim type of the claim.

        Get: Type(self: Claim) -> str
        """
        ...

    @property
    def Value(self):
        """
        Gets the value of the claim.

        Get: Value(self: Claim) -> str
        """
        ...

    @property
    def ValueType(self):
        """
        Gets the value type of the claim.

        Get: ValueType(self: Claim) -> str
        """
        ...



class ClaimsIdentity(object, IIdentity):
    """
    Represents a claims-based identity.

    ClaimsIdentity()

    ClaimsIdentity(identity: IIdentity)

    ClaimsIdentity(claims: IEnumerable[Claim])

    ClaimsIdentity(authenticationType: str)

    ClaimsIdentity(claims: IEnumerable[Claim], authenticationType: str)

    ClaimsIdentity(identity: IIdentity, claims: IEnumerable[Claim])

    ClaimsIdentity(authenticationType: str, nameType: str, roleType: str)

    ClaimsIdentity(claims: IEnumerable[Claim], authenticationType: str, nameType: str, roleType: str)

    ClaimsIdentity(identity: IIdentity, claims: IEnumerable[Claim], authenticationType: str, nameType: str, roleType: str)

    ClaimsIdentity(reader: BinaryReader)
    """
    def AddClaim(self, claim):
        """
        AddClaim(self: ClaimsIdentity, claim: Claim)

            Adds a single claim to this claims identity.

            claim: The claim to add.
        """
        ...

    def AddClaims(self, claims):
        """ AddClaims(self: ClaimsIdentity, claims: IEnumerable[Claim]) """
        ...

    def Clone(self):
        """
        Clone(self: ClaimsIdentity) -> ClaimsIdentity

            Returns a new System.Security.Claims.ClaimsIdentity copied from this claims identity.

            Returns: A copy of the current instance.
        """
        ...

    def CreateClaim(self, *args): #cannot find CLR method
        """ CreateClaim(self: ClaimsIdentity, reader: BinaryReader) -> Claim """
        ...

    def FindAll(self, *__args):
        """
        FindAll(self: ClaimsIdentity, match: Predicate[Claim]) -> IEnumerable[Claim]

        FindAll(self: ClaimsIdentity, type: str) -> IEnumerable[Claim]

            Retrieves all of the claims that have the specified claim type.

            type: The claim type against which to match claims.

            Returns: The matching claims. The list is read-only.
        """
        ...

    def FindFirst(self, *__args):
        """
        FindFirst(self: ClaimsIdentity, match: Predicate[Claim]) -> Claim

        FindFirst(self: ClaimsIdentity, type: str) -> Claim

            Retrieves the first claim with the specified claim type.

            type: The claim type to match.

            Returns: The first matching claim or ll if no match is found.
        """
        ...

    def GetObjectData(self, *args): #cannot find CLR method
        """
        GetObjectData(self: ClaimsIdentity, info: SerializationInfo, context: StreamingContext)

            Populates the System.Runtime.Serialization.SerializationInfo with data needed to serialize the current System.Security.Claims.ClaimsIdentity object.

            info: The object to populate with data.

            context: The destination for this serialization. Can be ll.
        """
        ...

    def HasClaim(self, *__args):
        """
        HasClaim(self: ClaimsIdentity, match: Predicate[Claim]) -> bool

        HasClaim(self: ClaimsIdentity, type: str, value: str) -> bool

            Determines whether this claims identity has a claim with the specified claim type and value.

            type: The type of the claim to match.

            value: The value of the claim to match.

            Returns: ue if a match is found; otherwise, lse.
        """
        ...

    def RemoveClaim(self, claim):
        """
        RemoveClaim(self: ClaimsIdentity, claim: Claim)

            Attempts to remove a claim from the claims identity.

            claim: The claim to remove.
        """
        ...

    def TryRemoveClaim(self, claim):
        """
        TryRemoveClaim(self: ClaimsIdentity, claim: Claim) -> bool

            Attempts to remove a claim from the claims identity.

            claim: The claim to remove.

            Returns: ue if the claim was successfully removed; otherwise, lse.
        """
        ...

    def WriteTo(self, writer):
        """ WriteTo(self: ClaimsIdentity, writer: BinaryWriter) """
        ...

    @property
    def Actor(self):
        """
        Gets or sets the identity of the calling party that was granted delegation rights.

        Get: Actor(self: ClaimsIdentity) -> ClaimsIdentity

        Set: Actor(self: ClaimsIdentity) = value
        """
        ...

    @property
    def AuthenticationType(self):
        """
        Gets the authentication type.

        Get: AuthenticationType(self: ClaimsIdentity) -> str
        """
        ...

    @property
    def BootstrapContext(self):
        """
        Gets or sets the token that was used to create this claims identity.

        Get: BootstrapContext(self: ClaimsIdentity) -> object

        Set: BootstrapContext(self: ClaimsIdentity) = value
        """
        ...

    @property
    def Claims(self):
        """
        Gets the claims associated with this claims identity.

        Get: Claims(self: ClaimsIdentity) -> IEnumerable[Claim]
        """
        ...

    @property
    def CustomSerializationData(self):
        """  """
        ...

    @property
    def IsAuthenticated(self):
        """
        Gets a value that indicates whether the identity has been authenticated.

        Get: IsAuthenticated(self: ClaimsIdentity) -> bool
        """
        ...

    @property
    def Label(self):
        """
        Gets or sets the label for this claims identity.

        Get: Label(self: ClaimsIdentity) -> str

        Set: Label(self: ClaimsIdentity) = value
        """
        ...

    @property
    def Name(self):
        """
        Gets the name of this claims identity.

        Get: Name(self: ClaimsIdentity) -> str
        """
        ...

    @property
    def NameClaimType(self):
        """
        Gets the claim type that is used to determine which claims provide the value for the System.Security.Claims.ClaimsIdentity.Name property of this claims identity.

        Get: NameClaimType(self: ClaimsIdentity) -> str
        """
        ...

    @property
    def RoleClaimType(self):
        """
        Gets the claim type that will be interpreted as a .NET Framework role among the claims in this claims identity.

        Get: RoleClaimType(self: ClaimsIdentity) -> str
        """
        ...


    DefaultIssuer = 'LOCAL AUTHORITY'
    DefaultNameClaimType = 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/name'
    DefaultRoleClaimType = 'http://schemas.microsoft.com/ws/2008/06/identity/claims/role'


class ClaimsPrincipal(object, IPrincipal):
    """
    An System.Security.Principal.IPrincipal implementation that supports multiple claims-based identities.

    ClaimsPrincipal()

    ClaimsPrincipal(identities: IEnumerable[ClaimsIdentity])

    ClaimsPrincipal(identity: IIdentity)

    ClaimsPrincipal(principal: IPrincipal)

    ClaimsPrincipal(reader: BinaryReader)
    """
    def AddIdentities(self, identities):
        """ AddIdentities(self: ClaimsPrincipal, identities: IEnumerable[ClaimsIdentity]) """
        ...

    def AddIdentity(self, identity):
        """
        AddIdentity(self: ClaimsPrincipal, identity: ClaimsIdentity)

            Adds the specified claims identity to this claims principal.

            identity: The claims identity to add.
        """
        ...

    def Clone(self):
        """
        Clone(self: ClaimsPrincipal) -> ClaimsPrincipal

            Returns a copy of this instance.

            Returns: A new copy of the System.Security.Claims.ClaimsPrincipal object.
        """
        ...

    def CreateClaimsIdentity(self, *args): #cannot find CLR method
        """
        CreateClaimsIdentity(self: ClaimsPrincipal, reader: BinaryReader) -> ClaimsIdentity

            Creates a new claims identity.

            reader: The binary reader.

            Returns: The created claims identity.
        """
        ...

    def FindAll(self, *__args):
        """
        FindAll(self: ClaimsPrincipal, match: Predicate[Claim]) -> IEnumerable[Claim]

        FindAll(self: ClaimsPrincipal, type: str) -> IEnumerable[Claim]

            Retrieves all or the claims that have the specified claim type.

            type: The claim type against which to match claims.

            Returns: The matching claims.
        """
        ...

    def FindFirst(self, *__args):
        """
        FindFirst(self: ClaimsPrincipal, match: Predicate[Claim]) -> Claim

        FindFirst(self: ClaimsPrincipal, type: str) -> Claim

            Retrieves the first claim with the specified claim type.

            type: The claim type to match.

            Returns: The first matching claim or ll if no match is found.
        """
        ...

    def GetObjectData(self, *args): #cannot find CLR method
        """
        GetObjectData(self: ClaimsPrincipal, info: SerializationInfo, context: StreamingContext)

            Populates the System.Runtime.Serialization.SerializationInfo with data needed to serialize the current System.Security.Claims.ClaimsPrincipal object.

            info: The object to populate with data.

            context: The destination for this serialization. Can be ll.
        """
        ...

    def HasClaim(self, *__args):
        """
        HasClaim(self: ClaimsPrincipal, match: Predicate[Claim]) -> bool

        HasClaim(self: ClaimsPrincipal, type: str, value: str) -> bool

            Determines whether any of the claims identities associated with this claims principal contains a claim with the specified claim type and value.

            type: The type of the claim to match.

            value: The value of the claim to match.

            Returns: ue if a matching claim exists; otherwise, lse.
        """
        ...

    def WriteTo(self, writer):
        """ WriteTo(self: ClaimsPrincipal, writer: BinaryWriter) """
        ...

    @property
    def Claims(self):
        """
        Gets a collection that contains all of the claims from all of the claims identities associated with this claims principal.

        Get: Claims(self: ClaimsPrincipal) -> IEnumerable[Claim]
        """
        ...

    @property
    def CustomSerializationData(self):
        """  """
        ...

    @property
    def Identities(self):
        """
        Gets a collection that contains all of the claims identities associated with this claims principal.

        Get: Identities(self: ClaimsPrincipal) -> IEnumerable[ClaimsIdentity]
        """
        ...

    @property
    def Identity(self):
        """
        Gets the primary claims identity associated with this claims principal.

        Get: Identity(self: ClaimsPrincipal) -> IIdentity
        """
        ...


    ClaimsPrincipalSelector = None
    Current = None


class ClaimTypes: # skipped bases: <type 'object'>
    """ Defines constants for the well-known claim types that can be assigned to a subject. This class cannot be inherited. """
    Actor = 'http://schemas.xmlsoap.org/ws/2009/09/identity/claims/actor'
    Anonymous = 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/anonymous'
    Authentication = 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/authentication'
    AuthenticationInstant = 'http://schemas.microsoft.com/ws/2008/06/identity/claims/authenticationinstant'
    AuthenticationMethod = 'http://schemas.microsoft.com/ws/2008/06/identity/claims/authenticationmethod'
    AuthorizationDecision = 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/authorizationdecision'
    CookiePath = 'http://schemas.microsoft.com/ws/2008/06/identity/claims/cookiepath'
    Country = 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/country'
    DateOfBirth = 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/dateofbirth'
    DenyOnlyPrimaryGroupSid = 'http://schemas.microsoft.com/ws/2008/06/identity/claims/denyonlyprimarygroupsid'
    DenyOnlyPrimarySid = 'http://schemas.microsoft.com/ws/2008/06/identity/claims/denyonlyprimarysid'
    DenyOnlySid = 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/denyonlysid'
    DenyOnlyWindowsDeviceGroup = 'http://schemas.microsoft.com/ws/2008/06/identity/claims/denyonlywindowsdevicegroup'
    Dns = 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/dns'
    Dsa = 'http://schemas.microsoft.com/ws/2008/06/identity/claims/dsa'
    Email = 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress'
    Expiration = 'http://schemas.microsoft.com/ws/2008/06/identity/claims/expiration'
    Expired = 'http://schemas.microsoft.com/ws/2008/06/identity/claims/expired'
    Gender = 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/gender'
    GivenName = 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/givenname'
    GroupSid = 'http://schemas.microsoft.com/ws/2008/06/identity/claims/groupsid'
    Hash = 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/hash'
    HomePhone = 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/homephone'
    IsPersistent = 'http://schemas.microsoft.com/ws/2008/06/identity/claims/ispersistent'
    Locality = 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/locality'
    MobilePhone = 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/mobilephone'
    Name = 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/name'
    NameIdentifier = 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/nameidentifier'
    OtherPhone = 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/otherphone'
    PostalCode = 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/postalcode'
    PrimaryGroupSid = 'http://schemas.microsoft.com/ws/2008/06/identity/claims/primarygroupsid'
    PrimarySid = 'http://schemas.microsoft.com/ws/2008/06/identity/claims/primarysid'
    Role = 'http://schemas.microsoft.com/ws/2008/06/identity/claims/role'
    Rsa = 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/rsa'
    SerialNumber = 'http://schemas.microsoft.com/ws/2008/06/identity/claims/serialnumber'
    Sid = 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/sid'
    Spn = 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/spn'
    StateOrProvince = 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/stateorprovince'
    StreetAddress = 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/streetaddress'
    Surname = 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/surname'
    System = 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/system'
    Thumbprint = 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/thumbprint'
    Upn = 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/upn'
    Uri = 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/uri'
    UserData = 'http://schemas.microsoft.com/ws/2008/06/identity/claims/userdata'
    Version = 'http://schemas.microsoft.com/ws/2008/06/identity/claims/version'
    Webpage = 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/webpage'
    WindowsAccountName = 'http://schemas.microsoft.com/ws/2008/06/identity/claims/windowsaccountname'
    WindowsDeviceClaim = 'http://schemas.microsoft.com/ws/2008/06/identity/claims/windowsdeviceclaim'
    WindowsDeviceGroup = 'http://schemas.microsoft.com/ws/2008/06/identity/claims/windowsdevicegroup'
    WindowsFqbnVersion = 'http://schemas.microsoft.com/ws/2008/06/identity/claims/windowsfqbnversion'
    WindowsSubAuthority = 'http://schemas.microsoft.com/ws/2008/06/identity/claims/windowssubauthority'
    WindowsUserClaim = 'http://schemas.microsoft.com/ws/2008/06/identity/claims/windowsuserclaim'
    X500DistinguishedName = 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/x500distinguishedname'
    __all__ = [
        'Actor',
        'Anonymous',
        'Authentication',
        'AuthenticationInstant',
        'AuthenticationMethod',
        'AuthorizationDecision',
        'CookiePath',
        'Country',
        'DateOfBirth',
        'DenyOnlyPrimaryGroupSid',
        'DenyOnlyPrimarySid',
        'DenyOnlySid',
        'DenyOnlyWindowsDeviceGroup',
        'Dns',
        'Dsa',
        'Email',
        'Expiration',
        'Expired',
        'Gender',
        'GivenName',
        'GroupSid',
        'Hash',
        'HomePhone',
        'IsPersistent',
        'Locality',
        'MobilePhone',
        'Name',
        'NameIdentifier',
        'OtherPhone',
        'PostalCode',
        'PrimaryGroupSid',
        'PrimarySid',
        'Role',
        'Rsa',
        'SerialNumber',
        'Sid',
        'Spn',
        'StateOrProvince',
        'StreetAddress',
        'Surname',
        'System',
        'Thumbprint',
        'Upn',
        'Uri',
        'UserData',
        'Version',
        'Webpage',
        'WindowsAccountName',
        'WindowsDeviceClaim',
        'WindowsDeviceGroup',
        'WindowsFqbnVersion',
        'WindowsSubAuthority',
        'WindowsUserClaim',
        'X500DistinguishedName',
    ]


class ClaimValueTypes: # skipped bases: <type 'object'>
    """ Defines claim value types according to the type URIs defined by W3C and OASIS. This class cannot be inherited. """
    Base64Binary = 'http://www.w3.org/2001/XMLSchema#base64Binary'
    Base64Octet = 'http://www.w3.org/2001/XMLSchema#base64Octet'
    Boolean = 'http://www.w3.org/2001/XMLSchema#boolean'
    Date = 'http://www.w3.org/2001/XMLSchema#date'
    DateTime = 'http://www.w3.org/2001/XMLSchema#dateTime'
    DaytimeDuration = 'http://www.w3.org/TR/2002/WD-xquery-operators-20020816#dayTimeDuration'
    DnsName = 'http://schemas.xmlsoap.org/claims/dns'
    Double = 'http://www.w3.org/2001/XMLSchema#double'
    DsaKeyValue = 'http://www.w3.org/2000/09/xmldsig#DSAKeyValue'
    Email = 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress'
    Fqbn = 'http://www.w3.org/2001/XMLSchema#fqbn'
    HexBinary = 'http://www.w3.org/2001/XMLSchema#hexBinary'
    Integer = 'http://www.w3.org/2001/XMLSchema#integer'
    Integer32 = 'http://www.w3.org/2001/XMLSchema#integer32'
    Integer64 = 'http://www.w3.org/2001/XMLSchema#integer64'
    KeyInfo = 'http://www.w3.org/2000/09/xmldsig#KeyInfo'
    Rfc822Name = 'urn:oasis:names:tc:xacml:1.0:data-type:rfc822Name'
    Rsa = 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/rsa'
    RsaKeyValue = 'http://www.w3.org/2000/09/xmldsig#RSAKeyValue'
    Sid = 'http://www.w3.org/2001/XMLSchema#sid'
    String = 'http://www.w3.org/2001/XMLSchema#string'
    Time = 'http://www.w3.org/2001/XMLSchema#time'
    UInteger32 = 'http://www.w3.org/2001/XMLSchema#uinteger32'
    UInteger64 = 'http://www.w3.org/2001/XMLSchema#uinteger64'
    UpnName = 'http://schemas.xmlsoap.org/claims/UPN'
    X500Name = 'urn:oasis:names:tc:xacml:1.0:data-type:x500Name'
    YearMonthDuration = 'http://www.w3.org/TR/2002/WD-xquery-operators-20020816#yearMonthDuration'
    __all__ = [
        'Base64Binary',
        'Base64Octet',
        'Boolean',
        'Date',
        'DateTime',
        'DaytimeDuration',
        'DnsName',
        'Double',
        'DsaKeyValue',
        'Email',
        'Fqbn',
        'HexBinary',
        'Integer',
        'Integer32',
        'Integer64',
        'KeyInfo',
        'Rfc822Name',
        'Rsa',
        'RsaKeyValue',
        'Sid',
        'String',
        'Time',
        'UInteger32',
        'UInteger64',
        'UpnName',
        'X500Name',
        'YearMonthDuration',
    ]


class DynamicRoleClaimProvider: # skipped bases: <type 'object'>
    """ The single method, System.Security.Claims.DynamicRoleClaimProvider.AddDynamicRoleClaims(System.Security.Claims.ClaimsIdentity,System.Collections.Generic.IEnumerable{System.Security.Claims.Claim}), exposed by this class is obsolete. You can use a System.Security.Claims.ClaimsAuthenticationManager object to add claims to a System.Security.Claims.ClaimsIdentity object. """
    @staticmethod
    def AddDynamicRoleClaims(claimsIdentity, claims):
        """ AddDynamicRoleClaims(claimsIdentity: ClaimsIdentity, claims: IEnumerable[Claim]) """
        ...

    __all__ = [
        'AddDynamicRoleClaims',
    ]


