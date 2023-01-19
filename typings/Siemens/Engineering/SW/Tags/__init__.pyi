# encoding: utf-8
# module Siemens.Engineering.SW.Tags calls itself Tags
# from Siemens.Engineering, Version=17.0.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class PlcConstant(object, IEngineeringObject, IMasterCopySource, IInternalObjectAccess, IEquatable[object]): # skipped bases: <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEngineeringCompositionOrObject'>
    """ Represents a Plc constant """
    @property
    def DataTypeName(self):
        """
        Defines the data type of this constant
        Get: DataTypeName(self: PlcConstant) -> str
        """
        ...

    @property
    def Name(self):
        """
        The name of the Plc constant
        Get: Name(self: PlcConstant) -> str
        """
        ...

    @property
    def Parent(self):
        """
        EOM parent of this object
        Get: Parent(self: PlcConstant) -> IEngineeringObject
        """
        ...

    @property
    def Value(self):
        """
        Defines the value of this constant.
        Get: Value(self: PlcConstant) -> str
        """
        ...


    def GetHashCode(self):
        """
        GetHashCode(self: PlcConstant) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self):
        """
        ToString(self: PlcConstant) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class PlcSystemConstant(PlcConstant): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IEquatable[object]'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalObjectAccess'>, <type 'IEngineeringInstance'>, <type 'IMasterCopySource'>
    """ Represents a Plc system constant """
    pass

class PlcSystemConstantComposition(object, IEngineeringComposition, IInternalCompositionAccess, IEnumerable[PlcSystemConstant], IEquatable[object]): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEnumerable'>, <type 'IInternalBaseAccess'>, <type 'IInternalCollectionAccess'>, <type 'IEngineeringInstance'>, <type 'IEngineeringCompositionOrObject'>
    """ Composition of PlcSystemConstants """
    @property
    def Parent(self):
        """
        Gets the parent.
        Get: Parent(self: PlcSystemConstantComposition) -> IEngineeringObject
        """
        ...


    def Find(self, name):
        """
        Find(self: PlcSystemConstantComposition, name: str) -> PlcSystemConstant
            Finds a given Plc system constant
            name: Name to find
            Returns: Siemens.Engineering.SW.Tags.PlcSystemConstant
        """
        ...

    def GetHashCode(self):
        """
        GetHashCode(self: PlcSystemConstantComposition) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self):
        """
        ToString(self: PlcSystemConstantComposition) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[PlcSystemConstant](enumerable: IEnumerable[PlcSystemConstant], value: PlcSystemConstant) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class PlcTag(object, IEngineeringObject, IMasterCopySource, IInternalObjectAccess, IEngineeringServiceProvider, IEquatable[object]): # skipped bases: <type 'IServiceProvider'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEngineeringCompositionOrObject'>
    """ Represents a Plc tag """
    @property
    def Comment(self):
        """
        The multilingual comment of the PlcTag
        Get: Comment(self: PlcTag) -> MultilingualText
        """
        ...

    @property
    def DataTypeName(self):
        """
        Defines the data type of this tag
        Get: DataTypeName(self: PlcTag) -> str
        Set: DataTypeName(self: PlcTag) = value
        """
        ...

    @property
    def ExternalAccessible(self):
        """
        Internal use only
        Get: ExternalAccessible(self: PlcTag) -> bool
        Set: ExternalAccessible(self: PlcTag) = value
        """
        ...

    @property
    def ExternalVisible(self):
        """
        Indicates whether this tag should be shown when browsing for tags from an HMI editor
        Get: ExternalVisible(self: PlcTag) -> bool
        Set: ExternalVisible(self: PlcTag) = value
        """
        ...

    @property
    def ExternalWritable(self):
        """
        Indicates whether this tag can be written to when browsing for tags from an HMI editor
        Get: ExternalWritable(self: PlcTag) -> bool
        Set: ExternalWritable(self: PlcTag) = value
        """
        ...

    @property
    def LogicalAddress(self):
        """
        The address in the PLC's address space
        Get: LogicalAddress(self: PlcTag) -> str
        Set: LogicalAddress(self: PlcTag) = value
        """
        ...

    @property
    def Name(self):
        """
        The name of the Plc tag
        Get: Name(self: PlcTag) -> str
        """
        ...

    @property
    def Parent(self):
        """
        EOM parent of this object
        Get: Parent(self: PlcTag) -> IEngineeringObject
        """
        ...


    def Delete(self):
        """
        Delete(self: PlcTag)
            Deletes this instance.
        """
        ...

    def Export(self, path, exportOptions):
        """
        Export(self: PlcTag, path: FileInfo, exportOptions: ExportOptions)
            Simatic ML export of a Plc tag
            path: Path to the Simatic ML file
            exportOptions: Option to use for export (default, readonly, etc.)
        """
        ...

    def GetHashCode(self):
        """
        GetHashCode(self: PlcTag) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self):
        """
        ToString(self: PlcTag) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class PlcTagComposition(object, IEngineeringComposition, IInternalCompositionAccess, IEnumerable[PlcTag], IEquatable[object]): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEnumerable'>, <type 'IInternalBaseAccess'>, <type 'IInternalCollectionAccess'>, <type 'IEngineeringInstance'>, <type 'IEngineeringCompositionOrObject'>
    """ Composition of PlcTags """
    @property
    def Parent(self):
        """
        Gets the parent.
        Get: Parent(self: PlcTagComposition) -> IEngineeringObject
        """
        ...


    def CreateFrom(self, sourceMasterCopy):
        """
        CreateFrom(self: PlcTagComposition, sourceMasterCopy: MasterCopy) -> PlcTag
            Create PlcTag from MasterCopy
            sourceMasterCopy: The source master copy
            Returns: Siemens.Engineering.SW.Tags.PlcTag
        """
        ...

    def Find(self, name):
        """
        Find(self: PlcTagComposition, name: str) -> PlcTag
            Finds a given Plc tag
            name: Name to find
            Returns: Siemens.Engineering.SW.Tags.PlcTag
        """
        ...

    def GetHashCode(self):
        """
        GetHashCode(self: PlcTagComposition) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def Import(self, path, importOptions):
        """
        Import(self: PlcTagComposition, path: FileInfo, importOptions: ImportOptions) -> IList[PlcTag]
            Simatic ML import of a Plc tag
            path: Path to the Simatic ML file
            importOptions: Options to use for Import
            Returns: System.Collections.Generic.IList<Siemens.Engineering.SW.Tags.PlcTag>
        """
        ...

    def ToString(self):
        """
        ToString(self: PlcTagComposition) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[PlcTag](enumerable: IEnumerable[PlcTag], value: PlcTag) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class PlcTagTable(object, IEngineeringObject, IShowable, IMasterCopySource, IMasterCopyTarget, IInternalObjectAccess, IEngineeringServiceProvider, IEquatable[object]): # skipped bases: <type 'IServiceProvider'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEngineeringCompositionOrObject'>
    """ Represents a Plc tag table """
    @property
    def IsDefault(self):
        """
        Indicates if this tag table is the default tag table
        Get: IsDefault(self: PlcTagTable) -> bool
        """
        ...

    @property
    def ModifiedTimeStamp(self):
        """
        Represents the last modified timestamp of this tag table
        Get: ModifiedTimeStamp(self: PlcTagTable) -> DateTime
        """
        ...

    @property
    def Name(self):
        """
        The name of the Plc tag table
        Get: Name(self: PlcTagTable) -> str
        """
        ...

    @property
    def Parent(self):
        """
        EOM parent of this object
        Get: Parent(self: PlcTagTable) -> IEngineeringObject
        """
        ...

    @property
    def SystemConstants(self):
        """
        Composition of Plc system constants
        Get: SystemConstants(self: PlcTagTable) -> PlcSystemConstantComposition
        """
        ...

    @property
    def Tags(self):
        """
        Composition of Plc tags
        Get: Tags(self: PlcTagTable) -> PlcTagComposition
        """
        ...

    @property
    def UserConstants(self):
        """
        Composition of Plc user constants
        Get: UserConstants(self: PlcTagTable) -> PlcUserConstantComposition
        """
        ...


    def Delete(self):
        """
        Delete(self: PlcTagTable)
            Deletes this instance.
        """
        ...

    def Export(self, path, exportOptions):
        """
        Export(self: PlcTagTable, path: FileInfo, exportOptions: ExportOptions)
            Simatic ML export of a Plc tag table
            path: Path to the Simatic ML file
            exportOptions: Option to use for export (default, readonly, etc.)
        """
        ...

    def GetHashCode(self):
        """
        GetHashCode(self: PlcTagTable) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self):
        """
        ToString(self: PlcTagTable) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class PlcTagTableComposition(object, IEngineeringComposition, IInternalCompositionAccess, IEnumerable[PlcTagTable], IEquatable[object]): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEnumerable'>, <type 'IInternalBaseAccess'>, <type 'IInternalCollectionAccess'>, <type 'IEngineeringInstance'>, <type 'IEngineeringCompositionOrObject'>
    """ Composition of PlcTagTables """
    @property
    def Parent(self):
        """
        Gets the parent.
        Get: Parent(self: PlcTagTableComposition) -> IEngineeringObject
        """
        ...


    def CreateFrom(self, sourceMasterCopy):
        """
        CreateFrom(self: PlcTagTableComposition, sourceMasterCopy: MasterCopy) -> PlcTagTable
            Create PlcTagTable from MasterCopy
            sourceMasterCopy: The source master copy
            Returns: Siemens.Engineering.SW.Tags.PlcTagTable
        """
        ...

    def Find(self, name):
        """
        Find(self: PlcTagTableComposition, name: str) -> PlcTagTable
            Finds a given Plc tag table
            name: Name to find
            Returns: Siemens.Engineering.SW.Tags.PlcTagTable
        """
        ...

    def GetHashCode(self):
        """
        GetHashCode(self: PlcTagTableComposition) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def Import(self, path, importOptions):
        """
        Import(self: PlcTagTableComposition, path: FileInfo, importOptions: ImportOptions) -> IList[PlcTagTable]
            Simatic ML import of a Plc tag table
            path: Path to the Simatic ML file
            importOptions: Options to use for Import
            Returns: System.Collections.Generic.IList<Siemens.Engineering.SW.Tags.PlcTagTable>
        """
        ...

    def ToString(self):
        """
        ToString(self: PlcTagTableComposition) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[PlcTagTable](enumerable: IEnumerable[PlcTagTable], value: PlcTagTable) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class PlcTagTableGroup(object, IEngineeringObject, IInternalObjectAccess, IEngineeringServiceProvider, IEquatable[object]): # skipped bases: <type 'IServiceProvider'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEngineeringCompositionOrObject'>
    """ Group containing Plc tag tables & Plc tag table user groups """
    @property
    def Groups(self):
        """
        Composition of Plc tag table user groups
        Get: Groups(self: PlcTagTableGroup) -> PlcTagTableUserGroupComposition
        """
        ...

    @property
    def Name(self):
        """
        The name of the Plc tag table group
        Get: Name(self: PlcTagTableGroup) -> str
        """
        ...

    @property
    def Parent(self):
        """
        EOM parent of this object
        Get: Parent(self: PlcTagTableGroup) -> IEngineeringObject
        """
        ...

    @property
    def TagTables(self):
        """
        Composition of Plc tag tables
        Get: TagTables(self: PlcTagTableGroup) -> PlcTagTableComposition
        """
        ...


    def GetHashCode(self):
        """
        GetHashCode(self: PlcTagTableGroup) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self):
        """
        ToString(self: PlcTagTableGroup) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class PlcTagTableSystemGroup(PlcTagTableGroup, IMasterCopyTarget): # skipped bases: <type 'IEquatable[object]'>, <type 'IInternalInstanceAccess'>, <type 'IServiceProvider'>, <type 'IEngineeringObject'>, <type 'IEngineeringServiceProvider'>, <type 'IInternalBaseAccess'>, <type 'IInternalObjectAccess'>, <type 'IEngineeringInstance'>, <type 'IEngineeringCompositionOrObject'>
    """ System group containing Plc tag tables & Plc tag table user groups """
    pass

class PlcTagTableUserGroup(PlcTagTableGroup, IMasterCopySource, IMasterCopyTarget): # skipped bases: <type 'IEquatable[object]'>, <type 'IInternalInstanceAccess'>, <type 'IServiceProvider'>, <type 'IEngineeringObject'>, <type 'IEngineeringServiceProvider'>, <type 'IInternalBaseAccess'>, <type 'IInternalObjectAccess'>, <type 'IEngineeringInstance'>, <type 'IEngineeringCompositionOrObject'>
    """ User group containing Plc tag tables & Plc tag table user groups """
    def Delete(self):
        """
        Delete(self: PlcTagTableUserGroup)
            Deletes this instance.
        """
        ...


class PlcTagTableUserGroupComposition(object, IEngineeringComposition, IInternalCompositionAccess, IEnumerable[PlcTagTableUserGroup], IEquatable[object]): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEnumerable'>, <type 'IInternalBaseAccess'>, <type 'IInternalCollectionAccess'>, <type 'IEngineeringInstance'>, <type 'IEngineeringCompositionOrObject'>
    """ Composition of PlcTagTableUserGroups """
    @property
    def Parent(self):
        """
        Gets the parent.
        Get: Parent(self: PlcTagTableUserGroupComposition) -> IEngineeringObject
        """
        ...


    def CreateFrom(self, sourceMasterCopy):
        """
        CreateFrom(self: PlcTagTableUserGroupComposition, sourceMasterCopy: MasterCopy) -> PlcTagTableUserGroup
            Create PlcTagTableUserGroup from MasterCopy
            sourceMasterCopy: The source master copy
            Returns: Siemens.Engineering.SW.Tags.PlcTagTableUserGroup
        """
        ...

    def Find(self, name):
        """
        Find(self: PlcTagTableUserGroupComposition, name: str) -> PlcTagTableUserGroup
            Finds a given Plc tag table user group
            name: Name to find
            Returns: Siemens.Engineering.SW.Tags.PlcTagTableUserGroup
        """
        ...

    def GetHashCode(self):
        """
        GetHashCode(self: PlcTagTableUserGroupComposition) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self):
        """
        ToString(self: PlcTagTableUserGroupComposition) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[PlcTagTableUserGroup](enumerable: IEnumerable[PlcTagTableUserGroup], value: PlcTagTableUserGroup) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class PlcUserConstant(PlcConstant, IEngineeringServiceProvider): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IEquatable[object]'>, <type 'IInternalInstanceAccess'>, <type 'IServiceProvider'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalObjectAccess'>, <type 'IEngineeringInstance'>, <type 'IMasterCopySource'>
    """ Represents a Plc user constant """
    @property
    def Comment(self):
        """
        The comment of the user constant
        Get: Comment(self: PlcUserConstant) -> MultilingualText
        """
        ...


    def Delete(self):
        """
        Delete(self: PlcUserConstant)
            Deletes this instance.
        """
        ...

    def Export(self, path, exportOptions):
        """
        Export(self: PlcUserConstant, path: FileInfo, exportOptions: ExportOptions)
            Simatic ML export of a Plc constant
            path: Path to the Simatic ML file
            exportOptions: Option to use for export (default, readonly, etc.)
        """
        ...


class PlcUserConstantComposition(object, IEngineeringComposition, IInternalCompositionAccess, IEnumerable[PlcUserConstant], IEquatable[object]): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEnumerable'>, <type 'IInternalBaseAccess'>, <type 'IInternalCollectionAccess'>, <type 'IEngineeringInstance'>, <type 'IEngineeringCompositionOrObject'>
    """ Composition of PlcUserConstants """
    @property
    def Parent(self):
        """
        Gets the parent.
        Get: Parent(self: PlcUserConstantComposition) -> IEngineeringObject
        """
        ...


    def CreateFrom(self, sourceMasterCopy):
        """
        CreateFrom(self: PlcUserConstantComposition, sourceMasterCopy: MasterCopy) -> PlcUserConstant
            Create PlcUserConstant from MasterCopy
            sourceMasterCopy: The source master copy
            Returns: Siemens.Engineering.SW.Tags.PlcUserConstant
        """
        ...

    def Find(self, name):
        """
        Find(self: PlcUserConstantComposition, name: str) -> PlcUserConstant
            Finds a given Plc user constant
            name: Name to find
            Returns: Siemens.Engineering.SW.Tags.PlcUserConstant
        """
        ...

    def GetHashCode(self):
        """
        GetHashCode(self: PlcUserConstantComposition) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def Import(self, path, importOptions):
        """
        Import(self: PlcUserConstantComposition, path: FileInfo, importOptions: ImportOptions) -> IList[PlcUserConstant]
            Simatic ML import of a Plc constant
            path: Path to the Simatic ML file
            importOptions: Options to use for Import
            Returns: System.Collections.Generic.IList<Siemens.Engineering.SW.Tags.PlcUserConstant>
        """
        ...

    def ToString(self):
        """
        ToString(self: PlcUserConstantComposition) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[PlcUserConstant](enumerable: IEnumerable[PlcUserConstant], value: PlcUserConstant) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


