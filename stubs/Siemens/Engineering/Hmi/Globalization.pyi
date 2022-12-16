# encoding: utf-8
# module Siemens.Engineering.Hmi.Globalization calls itself Globalization
# from Siemens.Engineering, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

from Siemens.Engineering import IEngineeringObject, IEngineeringComposition
from System import IEquatable

class MultiLingualGraphic(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Represents a multilingual graphic object of the project"""

    @property
    def Name(self):
        """
        The name of the multilingual graphic

        Get: Name(self: MultiLingualGraphic) -> str
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: MultiLingualGraphic) -> IEngineeringObject
        """
        ...
    def Delete(self):
        """
        Delete(self: MultiLingualGraphic)

            Deletes this instance.
        """
        ...
    def Export(self, path, exportOptions):
        """
        Export(self: MultiLingualGraphic, path: FileInfo, exportOptions: ExportOptions)

            Simatic ML export of a multilingual graphic

            path: Path to the Simatic ML file

            exportOptions: Option to use for export (default, readonly, etc.)
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: MultiLingualGraphic) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: MultiLingualGraphic) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class MultiLingualGraphicComposition(
    IEngineeringComposition, IInternalCompositionAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """Composition of MultiLingualGraphics"""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: MultiLingualGraphicComposition) -> IEngineeringObject
        """
        ...
    def Find(self, name):
        """
        Find(self: MultiLingualGraphicComposition, name: str) -> MultiLingualGraphic

            Finds a given multilingual graphic

            name: Name to find

            Returns: Siemens.Engineering.Hmi.Globalization.MultiLingualGraphic
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: MultiLingualGraphicComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def Import(self, path, importOptions):
        """
        Import(self: MultiLingualGraphicComposition, path: FileInfo, importOptions: ImportOptions) -> IList[MultiLingualGraphic]

            Simatic ML import of a multilingual graphic

            path: Path to the Simatic ML file

            importOptions: Options to use for Import

            Returns: System.Collections.Generic.IList<Siemens.Engineering.Hmi.Globalization.MultiLingualGraphic>
        """
        ...
    def ToString(self):
        """
        ToString(self: MultiLingualGraphicComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[MultiLingualGraphic](enumerable:  value: MultiLingualGraphic) -> bool"""
        ...
    def __ne__(self, *args): ...
