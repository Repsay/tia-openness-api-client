# encoding: utf-8
# module System.Web calls itself Web
# from System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AspNetHostingPermission(
    CodeAccessPermission, IUnrestrictedPermission
):  # skipped bases: <type 'IPermission'>, <type 'ISecurityEncodable'>, <type 'IStackWalk'>
    """
    Controls access permissions in ASP.NET hosted environments. This class cannot be inherited.

    AspNetHostingPermission(state: PermissionState)

    AspNetHostingPermission(level: AspNetHostingPermissionLevel)
    """

    @property
    def Level(self):
        """
        Gets or sets the current hosting permission level for an ASP.NET application.

        Get: Level(self: AspNetHostingPermission) -> AspNetHostingPermissionLevel

        Set: Level(self: AspNetHostingPermission) = value
        """
        ...
    @staticmethod  # known case of __new__
    def __new__(cls, *__args):
        """
        __new__(cls: type, state: PermissionState)

        __new__(cls: type, level: AspNetHostingPermissionLevel)
        """
        ...

class AspNetHostingPermissionAttribute(CodeAccessSecurityAttribute):  # skipped bases: <type '_Attribute'>
    """
    Allows security actions for System.Web.AspNetHostingPermission to be applied to code using declarative security. This class cannot be inherited.

    AspNetHostingPermissionAttribute(action: SecurityAction)
    """

    @property
    def Level(self):
        """
        Gets or sets the current hosting permission level.

        Get: Level(self: AspNetHostingPermissionAttribute) -> AspNetHostingPermissionLevel

        Set: Level(self: AspNetHostingPermissionAttribute) = value
        """
        ...
    def CreatePermission(self):
        """
        CreatePermission(self: AspNetHostingPermissionAttribute) -> IPermission

            Creates a new System.Web.AspNetHostingPermission with the permission level previously set by the System.Web.AspNetHostingPermissionAttribute.Level

             property.

            Returns: An System.Security.IPermission that is the new System.Web.AspNetHostingPermission.
        """
        ...

class AspNetHostingPermissionLevel(
    Enum
):  # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>
    """
    Specifies the trust level that is granted to an ASP.NET Web application.

    enum AspNetHostingPermissionLevel, values: High (500), Low (300), Medium (400), Minimal (200), None (100), Unrestricted (600)
    """

    High = None
    Low = None
    Medium = None
    Minimal = None

    Unrestricted = None
    value__ = None
