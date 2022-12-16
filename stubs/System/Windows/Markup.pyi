# encoding: utf-8
# module System.Windows.Markup calls itself Markup
# from System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class ValueSerializerAttribute(Attribute):  # skipped bases: <type '_Attribute'>
    """
    Identifies the System.Windows.Markup.ValueSerializer class that a type or property should use when it is serialized.

    ValueSerializerAttribute(valueSerializerType: Type)

    ValueSerializerAttribute(valueSerializerTypeName: str)
    """

    @staticmethod  # known case of __new__
    def __new__(cls, *__args):
        """
        __new__(cls: type, valueSerializerType: Type)

        __new__(cls: type, valueSerializerTypeName: str)
        """
        ...
    @property
    def ValueSerializerType(self):
        """
        Gets the type of the System.Windows.Markup.ValueSerializer class reported by this attribute.

        Get: ValueSerializerType(self: ValueSerializerAttribute) -> Type
        """
        ...
    @property
    def ValueSerializerTypeName(self):
        """
        Gets the assembly qualified name of the System.Windows.Markup.ValueSerializer type for this type or property.

        Get: ValueSerializerTypeName(self: ValueSerializerAttribute) -> str
        """
        ...
