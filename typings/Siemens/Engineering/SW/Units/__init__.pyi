# encoding: utf-8
# module Siemens.Engineering.SW.Units calls itself Units
# from Siemens.Engineering, Version=17.0.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class PlcUnit(object, IEngineeringObject, IMasterCopySource, IMasterCopyTarget, IInternalObjectAccess, IEngineeringServiceProvider, IEquatable[object]): # skipped bases: <type 'IServiceProvider'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEngineeringCompositionOrObject'>
    """ Represents a Plc unit """
    @property
    def Author(self):
        """
        The author of the Plc unit
        Get: Author(self: PlcUnit) -> str
        Set: Author(self: PlcUnit) = value
        """
        ...

    @property
    def BlockGroup(self):
        """
        Gets the Plc block system group
        Get: BlockGroup(self: PlcUnit) -> PlcBlockSystemGroup
        """
        ...

    @property
    def Comment(self):
        """
        The comment of the Plc unit
        Get: Comment(self: PlcUnit) -> MultilingualText
        """
        ...

    @property
    def ExternalSourceGroup(self):
        """
        Gets unit external source group
        Get: ExternalSourceGroup(self: PlcUnit) -> PlcExternalSourceSystemGroup
        """
        ...

    @property
    def Name(self):
        """
        The name of the Plc unit
        Get: Name(self: PlcUnit) -> str
        Set: Name(self: PlcUnit) = value
        """
        ...

    @property
    def Parent(self):
        """
        EOM parent of this object
        Get: Parent(self: PlcUnit) -> IEngineeringObject
        """
        ...

    @property
    def Relations(self):
        """
        Gets the unit relations
        Get: Relations(self: PlcUnit) -> PlcUnitRelationComposition
        """
        ...

    @property
    def TagTableGroup(self):
        """
        Gets the Plc tag table system group
        Get: TagTableGroup(self: PlcUnit) -> PlcTagTableSystemGroup
        """
        ...

    @property
    def TypeGroup(self):
        """
        Gets the Plc type system group
        Get: TypeGroup(self: PlcUnit) -> PlcTypeSystemGroup
        """
        ...


    def Delete(self):
        """
        Delete(self: PlcUnit)
            Deletes this instance.
        """
        ...

    def GetHashCode(self):
        """
        GetHashCode(self: PlcUnit) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self):
        """
        ToString(self: PlcUnit) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class PlcUnitComposition(object, IEngineeringComposition, IInternalCompositionAccess, IEnumerable[PlcUnit], IEquatable[object]): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEnumerable'>, <type 'IInternalBaseAccess'>, <type 'IInternalCollectionAccess'>, <type 'IEngineeringInstance'>, <type 'IEngineeringCompositionOrObject'>
    """ Composition of Plc units """
    @property
    def Parent(self):
        """
        Gets the parent.
        Get: Parent(self: PlcUnitComposition) -> IEngineeringObject
        """
        ...


    def CreateFrom(self, sourceMasterCopy):
        """
        CreateFrom(self: PlcUnitComposition, sourceMasterCopy: MasterCopy) -> PlcUnit
            Create a Plc unit from a master copy
            sourceMasterCopy: The source master copy
            Returns: Siemens.Engineering.SW.Units.PlcUnit
        """
        ...

    def Find(self, name):
        """
        Find(self: PlcUnitComposition, name: str) -> PlcUnit
            Find a Plc unit by name
            name: Name of Plc unit
            Returns: Siemens.Engineering.SW.Units.PlcUnit
        """
        ...

    def GetHashCode(self):
        """
        GetHashCode(self: PlcUnitComposition) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self):
        """
        ToString(self: PlcUnitComposition) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[PlcUnit](enumerable: IEnumerable[PlcUnit], value: PlcUnit) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class PlcUnitProvider(object, IEngineeringObject, IEngineeringService, IInternalObjectAccess, IEquatable[object]): # skipped bases: <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEngineeringCompositionOrObject'>
    """ Provides Plc units """
    @property
    def Parent(self):
        """
        EOM parent of this object
        Get: Parent(self: PlcUnitProvider) -> IEngineeringObject
        """
        ...

    @property
    def UnitGroup(self):
        """
        Gets the Plc unit system group
        Get: UnitGroup(self: PlcUnitProvider) -> PlcUnitSystemGroup
        """
        ...


    def GetHashCode(self):
        """
        GetHashCode(self: PlcUnitProvider) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self):
        """
        ToString(self: PlcUnitProvider) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class PlcUnitRelation(object, IEngineeringObject, IInternalObjectAccess, IEquatable[object]): # skipped bases: <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEngineeringCompositionOrObject'>
    """ Represents a unit relation """
    @property
    def Parent(self):
        """
        EOM parent of this object
        Get: Parent(self: PlcUnitRelation) -> IEngineeringObject
        """
        ...

    @property
    def RelatedObject(self):
        """
        Related object of the relation
        Get: RelatedObject(self: PlcUnitRelation) -> str
        Set: RelatedObject(self: PlcUnitRelation) = value
        """
        ...

    @property
    def RelationType(self):
        """
        Unit relation type which allowed to access
        Get: RelationType(self: PlcUnitRelation) -> UnitRelationType
        """
        ...


    def Delete(self):
        """
        Delete(self: PlcUnitRelation)
            Deletes this instance.
        """
        ...

    def GetHashCode(self):
        """
        GetHashCode(self: PlcUnitRelation) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self):
        """
        ToString(self: PlcUnitRelation) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class PlcUnitRelationComposition(object, IEngineeringComposition, IInternalCompositionAccess, IEnumerable[PlcUnitRelation], IEquatable[object]): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEnumerable'>, <type 'IInternalBaseAccess'>, <type 'IInternalCollectionAccess'>, <type 'IEngineeringInstance'>, <type 'IEngineeringCompositionOrObject'>
    """ Composition of Plc unit relations """
    @property
    def Parent(self):
        """
        Gets the parent.
        Get: Parent(self: PlcUnitRelationComposition) -> IEngineeringObject
        """
        ...


    def Find(self, relatedObject):
        """
        Find(self: PlcUnitRelationComposition, relatedObject: str) -> PlcUnitRelation
            Find a Plc unit relation by the name of the related object
            relatedObject: Name of the related object
            Returns: Siemens.Engineering.SW.Units.PlcUnitRelation
        """
        ...

    def GetHashCode(self):
        """
        GetHashCode(self: PlcUnitRelationComposition) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self):
        """
        ToString(self: PlcUnitRelationComposition) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[PlcUnitRelation](enumerable: IEnumerable[PlcUnitRelation], value: PlcUnitRelation) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class PlcUnitSystemGroup(object, IEngineeringObject, IMasterCopyTarget, IInternalObjectAccess, IEngineeringServiceProvider, IEquatable[object]): # skipped bases: <type 'IServiceProvider'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEngineeringCompositionOrObject'>
    """ System group containing Plc units """
    @property
    def Parent(self):
        """
        EOM parent of this object
        Get: Parent(self: PlcUnitSystemGroup) -> IEngineeringObject
        """
        ...

    @property
    def Units(self):
        """
        Composition of Plc units
        Get: Units(self: PlcUnitSystemGroup) -> PlcUnitComposition
        """
        ...


    def GetHashCode(self):
        """
        GetHashCode(self: PlcUnitSystemGroup) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self):
        """
        ToString(self: PlcUnitSystemGroup) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class UnitAccessType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>
    """
    Unit accessibility type
    enum UnitAccessType, values: Published (0), Unpublished (1)
    """
    Published = None
    Unpublished = None
    value__ = None


class UnitRelationType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>
    """
    Relation types in Unit relation editor
    enum UnitRelationType, values: NonUnitDB (1), SoftwareUnit (0), TODB (2)
    """
    NonUnitDB = None
    SoftwareUnit = None
    TODB = None
    value__ = None


