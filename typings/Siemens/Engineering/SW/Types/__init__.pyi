# encoding: utf-8
# module Siemens.Engineering.SW.Types calls itself Types
# from Siemens.Engineering, Version=17.0.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class PlcType(object, IEngineeringObject, IMasterCopySource, IGenerateSource, IInternalObjectAccess, IEngineeringServiceProvider, IEquatable[object]): # skipped bases: <type 'IServiceProvider'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEngineeringCompositionOrObject'>
    """ Represents a Plc type """
    @property
    def CreationDate(self):
        """
        Creation date of this Plc type
        Get: CreationDate(self: PlcType) -> DateTime
        """
        ...

    @property
    def InterfaceModifiedDate(self):
        """
        Get last breakable interface change of the PLC data type
        Get: InterfaceModifiedDate(self: PlcType) -> DateTime
        """
        ...

    @property
    def IsConsistent(self):
        """
        True if block and used data is consistent
        Get: IsConsistent(self: PlcType) -> bool
        """
        ...

    @property
    def IsKnowHowProtected(self):
        """
        Gets the know-how protection status of the block
        Get: IsKnowHowProtected(self: PlcType) -> bool
        """
        ...

    @property
    def ModifiedDate(self):
        """
        Get the last non-breakable modification of the PLC data type
        Get: ModifiedDate(self: PlcType) -> DateTime
        """
        ...

    @property
    def Name(self):
        """
        The name of the Plc type
        Get: Name(self: PlcType) -> str
        Set: Name(self: PlcType) = value
        """
        ...

    @property
    def Parent(self):
        """
        EOM parent of this object
        Get: Parent(self: PlcType) -> IEngineeringObject
        """
        ...


    def Delete(self):
        """
        Delete(self: PlcType)
            Deletes this instance.
        """
        ...

    def Export(self, path, exportOptions):
        """
        Export(self: PlcType, path: FileInfo, exportOptions: ExportOptions)
            Simatic ML export of a Plc type
            path: Path to the Simatic ML file
            exportOptions: Option to use for export (default, readonly, etc.)
        """
        ...

    def GetHashCode(self):
        """
        GetHashCode(self: PlcType) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ShowInEditor(self):
        """
        ShowInEditor(self: PlcType)
            Show the indicated item in the Plc type editor
        """
        ...

    def ToString(self):
        """
        ToString(self: PlcType) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class PlcStruct(PlcType): # skipped bases: <type 'IMasterCopySource'>, <type 'IEquatable[object]'>, <type 'IInternalInstanceAccess'>, <type 'IServiceProvider'>, <type 'IGenerateSource'>, <type 'IEngineeringObject'>, <type 'IEngineeringServiceProvider'>, <type 'IInternalBaseAccess'>, <type 'IInternalObjectAccess'>, <type 'IEngineeringInstance'>, <type 'IEngineeringCompositionOrObject'>
    """ Represents a Plc struct """
    pass

class PlcSystemTypeGroup(object, IEngineeringObject, IInternalObjectAccess, IEquatable[object]): # skipped bases: <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEngineeringCompositionOrObject'>
    """ Group containing Plc system types """
    @property
    def Name(self):
        """
        The name of the Plc system type group
        Get: Name(self: PlcSystemTypeGroup) -> str
        """
        ...

    @property
    def Parent(self):
        """
        EOM parent of this object
        Get: Parent(self: PlcSystemTypeGroup) -> IEngineeringObject
        """
        ...

    @property
    def Types(self):
        """
        Composition of Plc system types
        Get: Types(self: PlcSystemTypeGroup) -> PlcTypeComposition
        """
        ...


    def GetHashCode(self):
        """
        GetHashCode(self: PlcSystemTypeGroup) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self):
        """
        ToString(self: PlcSystemTypeGroup) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class PlcSystemTypeGroupComposition(object, IEngineeringComposition, IInternalCompositionAccess, IEnumerable[PlcSystemTypeGroup], IEquatable[object]): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEnumerable'>, <type 'IInternalBaseAccess'>, <type 'IInternalCollectionAccess'>, <type 'IEngineeringInstance'>, <type 'IEngineeringCompositionOrObject'>
    """ Composition of PlcSystemTypeGroups """
    @property
    def Parent(self):
        """
        Gets the parent.
        Get: Parent(self: PlcSystemTypeGroupComposition) -> IEngineeringObject
        """
        ...


    def GetHashCode(self):
        """
        GetHashCode(self: PlcSystemTypeGroupComposition) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self):
        """
        ToString(self: PlcSystemTypeGroupComposition) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[PlcSystemTypeGroup](enumerable: IEnumerable[PlcSystemTypeGroup], value: PlcSystemTypeGroup) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class PlcTypeComposition(object, IEngineeringComposition, IInternalCompositionAccess, IEnumerable[PlcType], IEquatable[object]): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEnumerable'>, <type 'IInternalBaseAccess'>, <type 'IInternalCollectionAccess'>, <type 'IEngineeringInstance'>, <type 'IEngineeringCompositionOrObject'>
    """ Composition of PlcTypes """
    @property
    def Parent(self):
        """
        Gets the parent.
        Get: Parent(self: PlcTypeComposition) -> IEngineeringObject
        """
        ...


    def CreateFrom(self, *__args):
        """
        CreateFrom(self: PlcTypeComposition, sourceMasterCopy: MasterCopy) -> PlcType
            Create PlcType from MasterCopy
            sourceMasterCopy: The source master copy
            Returns: Siemens.Engineering.SW.Types.PlcType
        CreateFrom(self: PlcTypeComposition, libraryTypeVersion: PlcTypeLibraryTypeVersion) -> PlcType
            Create plc type from type version
            libraryTypeVersion: Library type version
            Returns: Siemens.Engineering.SW.Types.PlcType
        """
        ...

    def Find(self, name):
        """
        Find(self: PlcTypeComposition, name: str) -> PlcType
            Finds a given Plc type
            name: Name to find
            Returns: Siemens.Engineering.SW.Types.PlcType
        """
        ...

    def GetHashCode(self):
        """
        GetHashCode(self: PlcTypeComposition) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def Import(self, path, importOptions, swImportOptions=None):
        """
        Import(self: PlcTypeComposition, path: FileInfo, importOptions: ImportOptions) -> IList[PlcType]
            Simatic ML import of a Plc type
            path: Path to the Simatic ML file
            importOptions: Options to use for Import
            Returns: System.Collections.Generic.IList<Siemens.Engineering.SW.Types.PlcType>
        Import(self: PlcTypeComposition, path: FileInfo, importOptions: ImportOptions, swImportOptions: SWImportOptions) -> IList[PlcType]
            Simatic ML import of a Plc type
            path: Path to the Simatic ML file
            importOptions: Options to use for Import
            swImportOptions: Sw import options to use for Import
            Returns: System.Collections.Generic.IList<Siemens.Engineering.SW.Types.PlcType>
        """
        ...

    def ToString(self):
        """
        ToString(self: PlcTypeComposition) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[PlcType](enumerable: IEnumerable[PlcType], value: PlcType) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class PlcTypeGroup(object, IEngineeringObject, IInternalObjectAccess, IEngineeringServiceProvider, IEquatable[object]): # skipped bases: <type 'IServiceProvider'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEngineeringCompositionOrObject'>
    """ Group containing Plc types & Plc type user groups """
    @property
    def Groups(self):
        """
        Composition of Plc type user groups
        Get: Groups(self: PlcTypeGroup) -> PlcTypeUserGroupComposition
        """
        ...

    @property
    def Name(self):
        """
        The name of the Plc type group
        Get: Name(self: PlcTypeGroup) -> str
        """
        ...

    @property
    def Parent(self):
        """
        EOM parent of this object
        Get: Parent(self: PlcTypeGroup) -> IEngineeringObject
        """
        ...

    @property
    def Types(self):
        """
        Composition of Plc types
        Get: Types(self: PlcTypeGroup) -> PlcTypeComposition
        """
        ...


    def GetHashCode(self):
        """
        GetHashCode(self: PlcTypeGroup) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self):
        """
        ToString(self: PlcTypeGroup) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class PlcTypeLibraryType(LibraryType): # skipped bases: <type 'IEquatable[object]'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'ILibraryTypeOrFolderSelection'>, <type 'IInternalBaseAccess'>, <type 'IInternalObjectAccess'>, <type 'IEngineeringInstance'>, <type 'IEngineeringCompositionOrObject'>
    """ Represents a library type made from a Plc type """
    pass

class PlcTypeLibraryTypeVersion(LibraryTypeVersion): # skipped bases: <type 'IEquatable[object]'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalObjectAccess'>, <type 'IEngineeringInstance'>, <type 'IEngineeringCompositionOrObject'>
    """ Represents a library type version made from a Plc type """
    pass

class PlcTypeSystemGroup(PlcTypeGroup, IMasterCopyTarget, ILibraryTypeInstantiationTarget): # skipped bases: <type 'IEquatable[object]'>, <type 'IInternalInstanceAccess'>, <type 'IServiceProvider'>, <type 'IEngineeringObject'>, <type 'IEngineeringServiceProvider'>, <type 'IInternalBaseAccess'>, <type 'IInternalObjectAccess'>, <type 'IEngineeringInstance'>, <type 'IEngineeringCompositionOrObject'>
    """ System group containing Plc types & Plc type user groups """
    @property
    def SystemTypeGroups(self):
        """
        Composition of system data types
        Get: SystemTypeGroups(self: PlcTypeSystemGroup) -> PlcSystemTypeGroupComposition
        """
        ...



class PlcTypeUserGroup(PlcTypeGroup, IMasterCopySource, IMasterCopyTarget, ILibraryTypeInstantiationTarget): # skipped bases: <type 'IEquatable[object]'>, <type 'IInternalInstanceAccess'>, <type 'IServiceProvider'>, <type 'IEngineeringObject'>, <type 'IEngineeringServiceProvider'>, <type 'IInternalBaseAccess'>, <type 'IInternalObjectAccess'>, <type 'IEngineeringInstance'>, <type 'IEngineeringCompositionOrObject'>
    """ User group containing Plc types & Plc type user groups """
    def Delete(self):
        """
        Delete(self: PlcTypeUserGroup)
            Deletes this instance.
        """
        ...


class PlcTypeUserGroupComposition(object, IEngineeringComposition, IInternalCompositionAccess, IEnumerable[PlcTypeUserGroup], IEquatable[object]): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEnumerable'>, <type 'IInternalBaseAccess'>, <type 'IInternalCollectionAccess'>, <type 'IEngineeringInstance'>, <type 'IEngineeringCompositionOrObject'>
    """ Composition of PlcTypeUserGroups """
    @property
    def Parent(self):
        """
        Gets the parent.
        Get: Parent(self: PlcTypeUserGroupComposition) -> IEngineeringObject
        """
        ...


    def CreateFrom(self, sourceMasterCopy):
        """
        CreateFrom(self: PlcTypeUserGroupComposition, sourceMasterCopy: MasterCopy) -> PlcTypeUserGroup
            Create PlcTypeUserGroup from MasterCopy
            sourceMasterCopy: The source master copy
            Returns: Siemens.Engineering.SW.Types.PlcTypeUserGroup
        """
        ...

    def Find(self, name):
        """
        Find(self: PlcTypeUserGroupComposition, name: str) -> PlcTypeUserGroup
            Finds a given Plc type user group
            name: Name to find
            Returns: Siemens.Engineering.SW.Types.PlcTypeUserGroup
        """
        ...

    def GetHashCode(self):
        """
        GetHashCode(self: PlcTypeUserGroupComposition) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self):
        """
        ToString(self: PlcTypeUserGroupComposition) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[PlcTypeUserGroup](enumerable: IEnumerable[PlcTypeUserGroup], value: PlcTypeUserGroup) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


