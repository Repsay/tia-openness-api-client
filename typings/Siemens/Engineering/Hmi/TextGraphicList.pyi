# encoding: utf-8
# module Siemens.Engineering.Hmi.TextGraphicList calls itself TextGraphicList
# from Siemens.Engineering, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

from Siemens.Engineering import IEngineeringComposition, IEngineeringObject
from System import IEquatable

class GraphicList(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Represents a graphic list"""

    @property
    def Name(self):
        """
        The name of the graphic list

        Get: Name(self: GraphicList) -> str
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: GraphicList) -> IEngineeringObject
        """
        ...
    def Delete(self):
        """
        Delete(self: GraphicList)

            Deletes this instance.
        """
        ...
    def Export(self, path, exportOptions):
        """
        Export(self: GraphicList, path: FileInfo, exportOptions: ExportOptions)

            Simatic ML export of a graphic list

            path: Path to the Simatic ML file

            exportOptions: Option to use for export (default, readonly, etc.)
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: GraphicList) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: GraphicList) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class GraphicListComposition(
    IEngineeringComposition, IInternalCompositionAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """Composition of GraphicLists"""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: GraphicListComposition) -> IEngineeringObject
        """
        ...
    def Find(self, name):
        """
        Find(self: GraphicListComposition, name: str) -> GraphicList

            Finds a given graphic list

            name: Name to find

            Returns: Siemens.Engineering.Hmi.TextGraphicList.GraphicList
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: GraphicListComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def Import(self, path, importOptions):
        """
        Import(self: GraphicListComposition, path: FileInfo, importOptions: ImportOptions) -> IList[GraphicList]

            Simatic ML import of a graphic list

            path: Path to the Simatic ML file

            importOptions: Options to use for Import

            Returns: System.Collections.Generic.IList<Siemens.Engineering.Hmi.TextGraphicList.GraphicList>
        """
        ...
    def ToString(self):
        """
        ToString(self: GraphicListComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[GraphicList](enumerable:  value: GraphicList) -> bool"""
        ...
    def __ne__(self, *args): ...

class TextList(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Represents a text list"""

    @property
    def Name(self):
        """
        The name of the text list

        Get: Name(self: TextList) -> str
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: TextList) -> IEngineeringObject
        """
        ...
    def Delete(self):
        """
        Delete(self: TextList)

            Deletes this instance.
        """
        ...
    def Export(self, path, exportOptions):
        """
        Export(self: TextList, path: FileInfo, exportOptions: ExportOptions)

            Simatic ML export of a text list

            path: Path to the Simatic ML file

            exportOptions: Option to use for export (default, readonly, etc.)
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: TextList) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: TextList) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class TextListComposition(
    IEngineeringComposition, IInternalCompositionAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """Composition of TextLists"""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: TextListComposition) -> IEngineeringObject
        """
        ...
    def Find(self, name):
        """
        Find(self: TextListComposition, name: str) -> TextList

            Finds a given text list

            name: Name to find

            Returns: Siemens.Engineering.Hmi.TextGraphicList.TextList
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: TextListComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def Import(self, path, importOptions):
        """
        Import(self: TextListComposition, path: FileInfo, importOptions: ImportOptions) -> IList[TextList]

            Simatic ML import of a text list

            path: Path to the Simatic ML file

            importOptions: Options to use for Import

            Returns: System.Collections.Generic.IList<Siemens.Engineering.Hmi.TextGraphicList.TextList>
        """
        ...
    def ToString(self):
        """
        ToString(self: TextListComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[TextList](enumerable:  value: TextList) -> bool"""
        ...
    def __ne__(self, *args): ...
