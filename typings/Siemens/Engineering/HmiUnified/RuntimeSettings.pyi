# encoding: utf-8
# module Siemens.Engineering.HmiUnified.RuntimeSettings calls itself RuntimeSettings
# from Siemens.Engineering, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

from Siemens.Engineering import IEngineeringAssociation, IEngineeringObject
from Siemens.Engineering.HmiUnified.Common import IValidator
from System import IEquatable

class HmiLanguageAndFont(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Language and font"""

    @property
    def Enable(self):
        """
        Enables language and font

        Get: Enable(self: HmiLanguageAndFont) -> bool

        Set: Enable(self: HmiLanguageAndFont) = value
        """
        ...
    @property
    def EnableForLogging(self):
        """
        Enables the language and font for logging

        Get: EnableForLogging(self: HmiLanguageAndFont) -> bool

        Set: EnableForLogging(self: HmiLanguageAndFont) = value
        """
        ...
    @property
    def FixedFont1(self):
        """
        Fixed font 1

        Get: FixedFont1(self: HmiLanguageAndFont) -> str
        """
        ...
    @property
    def FixedFont2(self):
        """
        Fixed font 2

        Get: FixedFont2(self: HmiLanguageAndFont) -> str
        """
        ...
    @property
    def FixedFont3(self):
        """
        Fixed font 3

        Get: FixedFont3(self: HmiLanguageAndFont) -> str
        """
        ...
    @property
    def FixedFont4(self):
        """
        Fixed font 4

        Get: FixedFont4(self: HmiLanguageAndFont) -> str
        """
        ...
    @property
    def Language(self):
        """
        Language name

        Get: Language(self: HmiLanguageAndFont) -> str
        """
        ...
    @property
    def Order(self):
        """
        Order of language and font entry

        Get: Order(self: HmiLanguageAndFont) -> Int16
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: HmiLanguageAndFont) -> IEngineeringObject
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: HmiLanguageAndFont) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: HmiLanguageAndFont) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class HmiLanguageAndFontAssociation(
    IEngineeringAssociation, IInternalAssociationAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalCollectionAccess'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>
    """Language and font list"""

    @property
    def Parent(self):
        """
        Gets the parent..

        Get: Parent(self: HmiLanguageAndFontAssociation) -> IEngineeringObject
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: HmiLanguageAndFontAssociation) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: HmiLanguageAndFontAssociation) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[HmiLanguageAndFont](enumerable:  value: HmiLanguageAndFont) -> bool"""
        ...
    def __ne__(self, *args): ...

class HmiRuntimeSetting(
    IValidator, IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Runtime settings of hmi device"""

    @property
    def LanguageAndFonts(self):
        """
        List of language and font entries

        Get: LanguageAndFonts(self: HmiRuntimeSetting) -> HmiLanguageAndFontAssociation
        """
        ...
    @property
    def OperateAsOpcServer(self):
        """
        Specifies whether hmi device should operate as opc server

        Get: OperateAsOpcServer(self: HmiRuntimeSetting) -> bool

        Set: OperateAsOpcServer(self: HmiRuntimeSetting) = value
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: HmiRuntimeSetting) -> IEngineeringObject
        """
        ...
    @property
    def StartScreen(self):
        """
        Name of the start up screen for hmi device

        Get: StartScreen(self: HmiRuntimeSetting) -> str

        Set: StartScreen(self: HmiRuntimeSetting) = value
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: HmiRuntimeSetting) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: HmiRuntimeSetting) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...
