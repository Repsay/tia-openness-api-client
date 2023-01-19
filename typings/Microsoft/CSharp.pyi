# encoding: utf-8
# module Microsoft.CSharp calls itself CSharp
# from System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
# no doc
# no imports

# no functions
# classes

from System.CodeDom.Compiler import CodeDomProvider

class CSharpCodeProvider(CodeDomProvider):  # skipped bases: <type 'IComponent'>, <type 'IDisposable'>
    """
    Provides access to instances of the C# code generator and code compiler.

    CSharpCodeProvider()

    CSharpCodeProvider(providerOptions: IDictionary[str, str])
    """

    @staticmethod  # known case of __new__
    def __new__(cls, providerOptions=None):
        """
        __new__(cls: type)

        __new__(cls: type, providerOptions: IDictionary[str, str])
        """
        ...
