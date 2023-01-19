# encoding: utf-8
# module Siemens.Engineering.SW.WatchAndForceTables calls itself WatchAndForceTables
# from Siemens.Engineering, Version=17.0.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class PlcForceTable(object, IEngineeringObject, IShowable, IInternalObjectAccess, IEquatable[object]): # skipped bases: <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEngineeringCompositionOrObject'>
    """ Represents a Plc force table """
    @property
    def Entries(self):
        """
        Composition of ForceTable Entries
        Get: Entries(self: PlcForceTable) -> PlcTableCommentEntryComposition
        """
        ...

    @property
    def IsConsistent(self):
        """
        Table is consistent or not
        Get: IsConsistent(self: PlcForceTable) -> bool
        """
        ...

    @property
    def Name(self):
        """
        Name of the ForceTable
        Get: Name(self: PlcForceTable) -> str
        """
        ...

    @property
    def Parent(self):
        """
        EOM parent of this object
        Get: Parent(self: PlcForceTable) -> IEngineeringObject
        """
        ...


    def Export(self, path, exportOptions):
        """
        Export(self: PlcForceTable, path: FileInfo, exportOptions: ExportOptions)
            Simatic ML export of a Plc force table
            path: Path to the Simatic ML file
            exportOptions: Option to use for export (default, readonly, etc.)
        """
        ...

    def GetHashCode(self):
        """
        GetHashCode(self: PlcForceTable) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self):
        """
        ToString(self: PlcForceTable) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class PlcForceTableComposition(object, IEngineeringComposition, IInternalCompositionAccess, IEnumerable[PlcForceTable], IEquatable[object]): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEnumerable'>, <type 'IInternalBaseAccess'>, <type 'IInternalCollectionAccess'>, <type 'IEngineeringInstance'>, <type 'IEngineeringCompositionOrObject'>
    """ Composition of PlcForceTables """
    @property
    def Parent(self):
        """
        Gets the parent.
        Get: Parent(self: PlcForceTableComposition) -> IEngineeringObject
        """
        ...


    def Find(self, name):
        """
        Find(self: PlcForceTableComposition, name: str) -> PlcForceTable
            Find force table by name
            name: Name of the force table
            Returns: Siemens.Engineering.SW.WatchAndForceTables.PlcForceTable
        """
        ...

    def GetHashCode(self):
        """
        GetHashCode(self: PlcForceTableComposition) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def Import(self, path, importOptions):
        """
        Import(self: PlcForceTableComposition, path: FileInfo, importOptions: ImportOptions) -> IList[PlcForceTable]
            Import Plc force table from Simatic ML
            path: Path of the Simatic ML which will be imported
            importOptions: Options to use for import from Simatic ML
            Returns: System.Collections.Generic.IList<Siemens.Engineering.SW.WatchAndForceTables.PlcForceTable>
        """
        ...

    def ToString(self):
        """
        ToString(self: PlcForceTableComposition) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[PlcForceTable](enumerable: IEnumerable[PlcForceTable], value: PlcForceTable) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class PlcTableCommentEntry(object, IEngineeringObject, IInternalObjectAccess, IEquatable[object]): # skipped bases: <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEngineeringCompositionOrObject'>
    """ Represents a Plc Force\Watch table comment entry """
    @property
    def Parent(self):
        """
        EOM parent of this object
        Get: Parent(self: PlcTableCommentEntry) -> IEngineeringObject
        """
        ...


    def Delete(self):
        """
        Delete(self: PlcTableCommentEntry)
            Deletes this instance.
        """
        ...

    def GetHashCode(self):
        """
        GetHashCode(self: PlcTableCommentEntry) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self):
        """
        ToString(self: PlcTableCommentEntry) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class PlcForceTableEntry(PlcTableCommentEntry): # skipped bases: <type 'IEquatable[object]'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalObjectAccess'>, <type 'IEngineeringInstance'>, <type 'IEngineeringCompositionOrObject'>
    """ Represents a Plc force table entry """
    @property
    def Address(self):
        """
        Address information of the tag
        Get: Address(self: PlcForceTableEntry) -> str
        """
        ...

    @property
    def DisplayFormat(self):
        """
        DisplayFormat
        Get: DisplayFormat(self: PlcForceTableEntry) -> PlcWatchAndForceTableDisplayFormat
        """
        ...

    @property
    def ForceIntention(self):
        """
        Force intention of the user
        Get: ForceIntention(self: PlcForceTableEntry) -> bool
        """
        ...

    @property
    def ForceValue(self):
        """
        The value that shall be forced
        Get: ForceValue(self: PlcForceTableEntry) -> str
        """
        ...

    @property
    def MonitorTrigger(self):
        """
        The trigger used for monitoring
        Get: MonitorTrigger(self: PlcForceTableEntry) -> PlcWatchAndForceTablePreDefinedTrigger
        """
        ...

    @property
    def Name(self):
        """
        Name of the tag
        Get: Name(self: PlcForceTableEntry) -> str
        """
        ...



class PlcTableCommentEntryComposition(object, IEngineeringComposition, IInternalCompositionAccess, IEnumerable[PlcTableCommentEntry], IEquatable[object]): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEnumerable'>, <type 'IInternalBaseAccess'>, <type 'IInternalCollectionAccess'>, <type 'IEngineeringInstance'>, <type 'IEngineeringCompositionOrObject'>
    """ Represents a Plc Force\Watch table comment entries """
    @property
    def Parent(self):
        """
        Gets the parent.
        Get: Parent(self: PlcTableCommentEntryComposition) -> IEngineeringObject
        """
        ...


    def GetHashCode(self):
        """
        GetHashCode(self: PlcTableCommentEntryComposition) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self):
        """
        ToString(self: PlcTableCommentEntryComposition) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[PlcTableCommentEntry](enumerable: IEnumerable[PlcTableCommentEntry], value: PlcTableCommentEntry) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class PlcWatchAndForceTableDisplayFormat(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>
    """
    Enum for DisplayFormat
    enum PlcWatchAndForceTableDisplayFormat, values: Any_pointer (1), BCD (2), Bin (3), Block_number (13), Bool (4), Character (5), Character_sequence (6), Counter (17), Date (7), DATE_AND_TIME (8), DEC_sequence (9), DEC_signed (10), DEC_unsigned (11), Float (16), Hex (12), Octal (14), Pointer (15), SIMATIC_Time (18), String (19), Time (20), TIME_OF_DAY (21), Undef (0), Unicode_character (22), Unicode_character_sequence (23), Unicode_string (24)
    """
    Any_pointer = None
    BCD = None
    Bin = None
    Block_number = None
    Bool = None
    Character = None
    Character_sequence = None
    Counter = None
    Date = None
    DATE_AND_TIME = None
    DEC_sequence = None
    DEC_signed = None
    DEC_unsigned = None
    Float = None
    Hex = None
    Octal = None
    Pointer = None
    SIMATIC_Time = None
    String = None
    Time = None
    TIME_OF_DAY = None
    Undef = None
    Unicode_character = None
    Unicode_character_sequence = None
    Unicode_string = None
    value__ = None


class PlcWatchAndForceTableGroup(object, IEngineeringObject, IInternalObjectAccess, IEquatable[object]): # skipped bases: <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEngineeringCompositionOrObject'>
    """ Group contatining Plc watch tables """
    @property
    def ForceTables(self):
        """
        Composition of PlcWatchTables
        Get: ForceTables(self: PlcWatchAndForceTableGroup) -> PlcForceTableComposition
        """
        ...

    @property
    def Groups(self):
        """
        Composition of User Groups
        Get: Groups(self: PlcWatchAndForceTableGroup) -> PlcWatchAndForceTableUserGroupComposition
        """
        ...

    @property
    def Name(self):
        """
        The name of the Plc watch table group
        Get: Name(self: PlcWatchAndForceTableGroup) -> str
        """
        ...

    @property
    def Parent(self):
        """
        EOM parent of this object
        Get: Parent(self: PlcWatchAndForceTableGroup) -> IEngineeringObject
        """
        ...

    @property
    def WatchTables(self):
        """
        Composition of PlcWatchTables
        Get: WatchTables(self: PlcWatchAndForceTableGroup) -> PlcWatchTableComposition
        """
        ...


    def GetHashCode(self):
        """
        GetHashCode(self: PlcWatchAndForceTableGroup) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self):
        """
        ToString(self: PlcWatchAndForceTableGroup) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class PlcWatchAndForceTablePreDefinedTrigger(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>
    """
    Enum for PreDefinedTrigger
    enum PlcWatchAndForceTablePreDefinedTrigger, values: OnceOnlyAtEnd (4), OnceOnlyAtStart (2), OnceOnlyAtStop (6), Permanent (0), PermanentAtEnd (3), PermanentAtStart (1), PermanentAtStop (5), Undef (7)
    """
    OnceOnlyAtEnd = None
    OnceOnlyAtStart = None
    OnceOnlyAtStop = None
    Permanent = None
    PermanentAtEnd = None
    PermanentAtStart = None
    PermanentAtStop = None
    Undef = None
    value__ = None


class PlcWatchAndForceTableSystemGroup(PlcWatchAndForceTableGroup): # skipped bases: <type 'IEquatable[object]'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalObjectAccess'>, <type 'IEngineeringInstance'>, <type 'IEngineeringCompositionOrObject'>
    """ System group containing Plc watch tables and Plc force tables and user group containing these """
    pass

class PlcWatchAndForceTableUserGroup(PlcWatchAndForceTableGroup): # skipped bases: <type 'IEquatable[object]'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalObjectAccess'>, <type 'IEngineeringInstance'>, <type 'IEngineeringCompositionOrObject'>
    """ User group containing Plc watch tables """
    def Delete(self):
        """
        Delete(self: PlcWatchAndForceTableUserGroup)
            Deletes this instance.
        """
        ...


class PlcWatchAndForceTableUserGroupComposition(object, IEngineeringComposition, IInternalCompositionAccess, IEnumerable[PlcWatchAndForceTableUserGroup], IEquatable[object]): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEnumerable'>, <type 'IInternalBaseAccess'>, <type 'IInternalCollectionAccess'>, <type 'IEngineeringInstance'>, <type 'IEngineeringCompositionOrObject'>
    """ Composition of PlcWatchTableUserGroups """
    @property
    def Parent(self):
        """
        Gets the parent.
        Get: Parent(self: PlcWatchAndForceTableUserGroupComposition) -> IEngineeringObject
        """
        ...


    def CreateFrom(self, sourceMasterCopy):
        """
        CreateFrom(self: PlcWatchAndForceTableUserGroupComposition, sourceMasterCopy: MasterCopy) -> PlcWatchAndForceTableUserGroup
            Create PlcBlockUserGroup from MasterCopy
            sourceMasterCopy: The source master copy
            Returns: Siemens.Engineering.SW.WatchAndForceTables.PlcWatchAndForceTableUserGroup
        """
        ...

    def Find(self, name):
        """
        Find(self: PlcWatchAndForceTableUserGroupComposition, name: str) -> PlcWatchAndForceTableUserGroup
            Finds given Plc watch table user group
            name: Name of the Plcwatchtable group to search for
            Returns: Siemens.Engineering.SW.WatchAndForceTables.PlcWatchAndForceTableUserGroup
        """
        ...

    def GetHashCode(self):
        """
        GetHashCode(self: PlcWatchAndForceTableUserGroupComposition) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self):
        """
        ToString(self: PlcWatchAndForceTableUserGroupComposition) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[PlcWatchAndForceTableUserGroup](enumerable: IEnumerable[PlcWatchAndForceTableUserGroup], value: PlcWatchAndForceTableUserGroup) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class PlcWatchTable(object, IEngineeringObject, IShowable, IInternalObjectAccess, IEquatable[object]): # skipped bases: <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEngineeringCompositionOrObject'>
    """ Represents a Plc watch table """
    @property
    def Entries(self):
        """
        Composition of WatchTable Entries
        Get: Entries(self: PlcWatchTable) -> PlcTableCommentEntryComposition
        """
        ...

    @property
    def IsConsistent(self):
        """
        Table is consistent or not
        Get: IsConsistent(self: PlcWatchTable) -> bool
        """
        ...

    @property
    def Name(self):
        """
        Name of the WatchTable
        Get: Name(self: PlcWatchTable) -> str
        """
        ...

    @property
    def Parent(self):
        """
        EOM parent of this object
        Get: Parent(self: PlcWatchTable) -> IEngineeringObject
        """
        ...


    def Delete(self):
        """
        Delete(self: PlcWatchTable)
            Deletes this instance.
        """
        ...

    def Export(self, path, exportOptions):
        """
        Export(self: PlcWatchTable, path: FileInfo, exportOptions: ExportOptions)
            Simatic ML export of a Plc watch table
            path: Path to the Simatic ML file
            exportOptions: Option to use for export (default, readonly, etc.)
        """
        ...

    def GetHashCode(self):
        """
        GetHashCode(self: PlcWatchTable) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self):
        """
        ToString(self: PlcWatchTable) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class PlcWatchTableComposition(object, IEngineeringComposition, IInternalCompositionAccess, IEnumerable[PlcWatchTable], IEquatable[object]): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEnumerable'>, <type 'IInternalBaseAccess'>, <type 'IInternalCollectionAccess'>, <type 'IEngineeringInstance'>, <type 'IEngineeringCompositionOrObject'>
    """ Composition of PlcWatchTables """
    @property
    def Parent(self):
        """
        Gets the parent.
        Get: Parent(self: PlcWatchTableComposition) -> IEngineeringObject
        """
        ...


    def Find(self, name):
        """
        Find(self: PlcWatchTableComposition, name: str) -> PlcWatchTable
            Finds a given Plc watch table
            name: The name of the WatchTable
            Returns: Siemens.Engineering.SW.WatchAndForceTables.PlcWatchTable
        """
        ...

    def GetHashCode(self):
        """
        GetHashCode(self: PlcWatchTableComposition) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def Import(self, path, importOptions):
        """
        Import(self: PlcWatchTableComposition, path: FileInfo, importOptions: ImportOptions) -> IList[PlcWatchTable]
            Import Plc watch table from Simatic ML
            path: Path of the Simatic ML which will be imported
            importOptions: Options to use for import from Simatic ML
            Returns: System.Collections.Generic.IList<Siemens.Engineering.SW.WatchAndForceTables.PlcWatchTable>
        """
        ...

    def ToString(self):
        """
        ToString(self: PlcWatchTableComposition) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[PlcWatchTable](enumerable: IEnumerable[PlcWatchTable], value: PlcWatchTable) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class PlcWatchTableEntry(PlcTableCommentEntry): # skipped bases: <type 'IEquatable[object]'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalObjectAccess'>, <type 'IEngineeringInstance'>, <type 'IEngineeringCompositionOrObject'>
    """ Represents a Plc watch table entry """
    @property
    def Address(self):
        """
        Address
        Get: Address(self: PlcWatchTableEntry) -> str
        """
        ...

    @property
    def DisplayFormat(self):
        """
        DisplayFormat
        Get: DisplayFormat(self: PlcWatchTableEntry) -> PlcWatchAndForceTableDisplayFormat
        """
        ...

    @property
    def ModifyIntention(self):
        """
        The user's modify intention
        Get: ModifyIntention(self: PlcWatchTableEntry) -> bool
        """
        ...

    @property
    def ModifyTrigger(self):
        """
        The trigger used for modify
        Get: ModifyTrigger(self: PlcWatchTableEntry) -> PlcWatchAndForceTablePreDefinedTrigger
        """
        ...

    @property
    def ModifyValue(self):
        """
        The value that shall be used for modify.
        Get: ModifyValue(self: PlcWatchTableEntry) -> str
        """
        ...

    @property
    def MonitorTrigger(self):
        """
        The trigger used for monitoring.
        Get: MonitorTrigger(self: PlcWatchTableEntry) -> PlcWatchAndForceTablePreDefinedTrigger
        """
        ...

    @property
    def Name(self):
        """
        Name
        Get: Name(self: PlcWatchTableEntry) -> str
        """
        ...



