# encoding: utf-8
# module System.Diagnostics.CodeAnalysis calls itself CodeAnalysis
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class ExcludeFromCodeCoverageAttribute(Attribute):  # skipped bases: <type '_Attribute'>
    """
    Specifies that the attributed code should be excluded from code coverage information.

    ExcludeFromCodeCoverageAttribute()
    """

    pass

class SuppressMessageAttribute(Attribute):  # skipped bases: <type '_Attribute'>
    """
    Suppresses reporting of a specific static analysis tool rule violation, allowing multiple suppressions on a single code artifact.

    SuppressMessageAttribute(category: str, checkId: str)
    """

    @property
    def Category(self):
        """
        Gets the category identifying the classification of the attribute.

        Get: Category(self: SuppressMessageAttribute) -> str
        """
        ...
    @property
    def CheckId(self):
        """
        Gets the identifier of the static analysis tool rule to be suppressed.

        Get: CheckId(self: SuppressMessageAttribute) -> str
        """
        ...
    @property
    def Justification(self):
        """
        Gets or sets the justification for suppressing the code analysis message.

        Get: Justification(self: SuppressMessageAttribute) -> str

        Set: Justification(self: SuppressMessageAttribute) = value
        """
        ...
    @property
    def MessageId(self):
        """
        Gets or sets an optional argument expanding on exclusion criteria.

        Get: MessageId(self: SuppressMessageAttribute) -> str

        Set: MessageId(self: SuppressMessageAttribute) = value
        """
        ...
    @property
    def Scope(self):
        """
        Gets or sets the scope of the code that is relevant for the attribute.

        Get: Scope(self: SuppressMessageAttribute) -> str

        Set: Scope(self: SuppressMessageAttribute) = value
        """
        ...
    @property
    def Target(self):
        """
        Gets or sets a fully qualified path that represents the target of the attribute.

        Get: Target(self: SuppressMessageAttribute) -> str

        Set: Target(self: SuppressMessageAttribute) = value
        """
        ...
    @staticmethod  # known case of __new__
    def __new__(cls, category, checkId):
        """__new__(cls: type, category: str, checkId: str)"""
        ...
