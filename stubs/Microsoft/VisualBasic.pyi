# encoding: utf-8
# module Microsoft.VisualBasic calls itself VisualBasic
# from System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
# no doc
# no imports

# no functions
# classes

from System.CodeDom.Compiler import CodeDomProvider

class VBCodeProvider(CodeDomProvider):  # skipped bases: <type 'IDisposable'>, <type 'IComponent'>
    """
    Provides access to instances of the Visual Basic code generator and code compiler.

    VBCodeProvider()

    VBCodeProvider(providerOptions: IDictionary[str, str])
    """

    @staticmethod  # known case of __new__
    def __new__(cls, providerOptions=None):
        """
        __new__(cls: type)

        __new__(cls: type, providerOptions: IDictionary[str, str])
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
    def Events(self):
        """Gets the list of event handlers that are attached to this System.ComponentModel.Component."""
        ...
    @property
    def FileExtension(self):
        """
        Gets the file name extension to use when creating source code files.

        Get: FileExtension(self: VBCodeProvider) -> str
        """
        ...
    @property
    def LanguageOptions(self):
        """
        Gets a language features identifier.

        Get: LanguageOptions(self: VBCodeProvider) -> LanguageOptions
        """
        ...
