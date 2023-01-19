# encoding: utf-8
# module Siemens.Engineering.SW.OpcUa calls itself OpcUa
# from Siemens.Engineering, Version=17.0.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class OpcUaCommunicationGroup(object, IEngineeringObject, IInternalObjectAccess, IEquatable[object]): # skipped bases: <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEngineeringCompositionOrObject'>
    """ Top level OpcUa Communication folder """
    @property
    def Parent(self):
        """
        EOM parent of this object
        Get: Parent(self: OpcUaCommunicationGroup) -> IEngineeringObject
        """
        ...

    @property
    def ServerInterfaceGroup(self):
        """
        OPCUA Server Interface Folder
        Get: ServerInterfaceGroup(self: OpcUaCommunicationGroup) -> ServerInterfaceGroup
        """
        ...


    def GetHashCode(self):
        """
        GetHashCode(self: OpcUaCommunicationGroup) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self):
        """
        ToString(self: OpcUaCommunicationGroup) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class OpcUaProvider(object, IEngineeringObject, IEngineeringService, IInternalObjectAccess, IEquatable[object]): # skipped bases: <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEngineeringCompositionOrObject'>
    """ OpcUa Provider """
    @property
    def CommunicationGroup(self):
        """
        Access the OpcUa Communication Folder
        Get: CommunicationGroup(self: OpcUaProvider) -> OpcUaCommunicationGroup
        """
        ...

    @property
    def Parent(self):
        """
        EOM parent of this object
        Get: Parent(self: OpcUaProvider) -> IEngineeringObject
        """
        ...


    def GetHashCode(self):
        """
        GetHashCode(self: OpcUaProvider) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self):
        """
        ToString(self: OpcUaProvider) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ReferenceNamespace(object, IEngineeringObject, IInternalObjectAccess, IEquatable[object]): # skipped bases: <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEngineeringCompositionOrObject'>
    """ OpcUa Reference Namespace """
    @property
    def Author(self):
        """
        Author
        Get: Author(self: ReferenceNamespace) -> str
        Set: Author(self: ReferenceNamespace) = value
        """
        ...

    @property
    def Comment(self):
        """
        Comment
        Get: Comment(self: ReferenceNamespace) -> MultilingualText
        """
        ...

    @property
    def CreationTime(self):
        """
        Creation time
        Get: CreationTime(self: ReferenceNamespace) -> DateTime
        """
        ...

    @property
    def Enabled(self):
        """
        Enable reference namespace and download to PLC
        Get: Enabled(self: ReferenceNamespace) -> bool
        Set: Enabled(self: ReferenceNamespace) = value
        """
        ...

    @property
    def LastModified(self):
        """
        Last modified time
        Get: LastModified(self: ReferenceNamespace) -> DateTime
        """
        ...

    @property
    def Name(self):
        """
        Name
        Get: Name(self: ReferenceNamespace) -> str
        """
        ...

    @property
    def Parent(self):
        """
        EOM parent of this object
        Get: Parent(self: ReferenceNamespace) -> IEngineeringObject
        """
        ...


    def Delete(self):
        """
        Delete(self: ReferenceNamespace)
            Deletes this instance.
        """
        ...

    def Export(self, filePath):
        """
        Export(self: ReferenceNamespace, filePath: FileInfo)
            Exports the original XML File
            filePath: Path to the location to save
        """
        ...

    def GetHashCode(self):
        """
        GetHashCode(self: ReferenceNamespace) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def Import(self, filePath):
        """
        Import(self: ReferenceNamespace, filePath: FileInfo)
            Import file
            filePath: Path to file
        """
        ...

    def ToString(self):
        """
        ToString(self: ReferenceNamespace) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ReferenceNamespaceComposition(object, IEngineeringComposition, IInternalCompositionAccess, IEnumerable[ReferenceNamespace], IEquatable[object]): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEnumerable'>, <type 'IInternalBaseAccess'>, <type 'IInternalCollectionAccess'>, <type 'IEngineeringInstance'>, <type 'IEngineeringCompositionOrObject'>
    """ Composition of Reference Namespaces """
    @property
    def Parent(self):
        """
        Gets the parent.
        Get: Parent(self: ReferenceNamespaceComposition) -> IEngineeringObject
        """
        ...


    def GetHashCode(self):
        """
        GetHashCode(self: ReferenceNamespaceComposition) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self):
        """
        ToString(self: ReferenceNamespaceComposition) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[ReferenceNamespace](enumerable: IEnumerable[ReferenceNamespace], value: ReferenceNamespace) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ServerInterface(object, IEngineeringObject, IInternalObjectAccess, IEquatable[object]): # skipped bases: <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEngineeringCompositionOrObject'>
    """ OpcUa Server Interface """
    @property
    def Author(self):
        """
        Author
        Get: Author(self: ServerInterface) -> str
        Set: Author(self: ServerInterface) = value
        """
        ...

    @property
    def Comment(self):
        """
        Comment
        Get: Comment(self: ServerInterface) -> MultilingualText
        """
        ...

    @property
    def CreationTime(self):
        """
        Creation time
        Get: CreationTime(self: ServerInterface) -> DateTime
        """
        ...

    @property
    def Enabled(self):
        """
        Enable server interface and download to PLC
        Get: Enabled(self: ServerInterface) -> bool
        Set: Enabled(self: ServerInterface) = value
        """
        ...

    @property
    def LastModified(self):
        """
        Last modified time
        Get: LastModified(self: ServerInterface) -> DateTime
        """
        ...

    @property
    def Name(self):
        """
        Name
        Get: Name(self: ServerInterface) -> str
        """
        ...

    @property
    def Parent(self):
        """
        EOM parent of this object
        Get: Parent(self: ServerInterface) -> IEngineeringObject
        """
        ...


    def Delete(self):
        """
        Delete(self: ServerInterface)
            Deletes this instance.
        """
        ...

    def Export(self, filePath):
        """
        Export(self: ServerInterface, filePath: FileInfo)
            Exports the original XML File
            filePath: Path to the location to save
        """
        ...

    def GetHashCode(self):
        """
        GetHashCode(self: ServerInterface) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def Import(self, filePath):
        """
        Import(self: ServerInterface, filePath: FileInfo)
            Import file
            filePath: Path to file
        """
        ...

    def ToString(self):
        """
        ToString(self: ServerInterface) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ServerInterfaceComposition(object, IEngineeringComposition, IInternalCompositionAccess, IEnumerable[ServerInterface], IEquatable[object]): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEnumerable'>, <type 'IInternalBaseAccess'>, <type 'IInternalCollectionAccess'>, <type 'IEngineeringInstance'>, <type 'IEngineeringCompositionOrObject'>
    """ Composition of Server Interfaces """
    @property
    def Parent(self):
        """
        Gets the parent.
        Get: Parent(self: ServerInterfaceComposition) -> IEngineeringObject
        """
        ...


    def GetHashCode(self):
        """
        GetHashCode(self: ServerInterfaceComposition) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self):
        """
        ToString(self: ServerInterfaceComposition) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[ServerInterface](enumerable: IEnumerable[ServerInterface], value: ServerInterface) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ServerInterfaceGroup(object, IEngineeringObject, IInternalObjectAccess, IEquatable[object]): # skipped bases: <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEngineeringCompositionOrObject'>
    """ Contains Server Interfaces """
    @property
    def Parent(self):
        """
        EOM parent of this object
        Get: Parent(self: ServerInterfaceGroup) -> IEngineeringObject
        """
        ...

    @property
    def ReferenceNamespaces(self):
        """
        Returns a list of Server Interfaces
        Get: ReferenceNamespaces(self: ServerInterfaceGroup) -> ReferenceNamespaceComposition
        """
        ...

    @property
    def ServerInterfaces(self):
        """
        Returns a list of Server Interfaces
        Get: ServerInterfaces(self: ServerInterfaceGroup) -> ServerInterfaceComposition
        """
        ...

    @property
    def SimaticInterfaces(self):
        """
        Returns a list of Server Interfaces
        Get: SimaticInterfaces(self: ServerInterfaceGroup) -> SimaticInterfaceComposition
        """
        ...


    def GetHashCode(self):
        """
        GetHashCode(self: ServerInterfaceGroup) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self):
        """
        ToString(self: ServerInterfaceGroup) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class SimaticInterface(object, IEngineeringObject, IInternalObjectAccess, IEquatable[object]): # skipped bases: <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEngineeringCompositionOrObject'>
    """ OpcUa Simatic Interface """
    @property
    def Author(self):
        """
        Author
        Get: Author(self: SimaticInterface) -> str
        Set: Author(self: SimaticInterface) = value
        """
        ...

    @property
    def Comment(self):
        """
        Comment
        Get: Comment(self: SimaticInterface) -> MultilingualText
        """
        ...

    @property
    def CreationTime(self):
        """
        Creation time
        Get: CreationTime(self: SimaticInterface) -> DateTime
        """
        ...

    @property
    def Enabled(self):
        """
        Enable simatic interface and download to PLC
        Get: Enabled(self: SimaticInterface) -> bool
        Set: Enabled(self: SimaticInterface) = value
        """
        ...

    @property
    def LastModified(self):
        """
        Last modified time
        Get: LastModified(self: SimaticInterface) -> DateTime
        """
        ...

    @property
    def Name(self):
        """
        Name
        Get: Name(self: SimaticInterface) -> str
        """
        ...

    @property
    def Parent(self):
        """
        EOM parent of this object
        Get: Parent(self: SimaticInterface) -> IEngineeringObject
        """
        ...


    def Delete(self):
        """
        Delete(self: SimaticInterface)
            Deletes this instance.
        """
        ...

    def Export(self, filePath):
        """
        Export(self: SimaticInterface, filePath: FileInfo)
            Exports the original XML File
            filePath: Path to the location to save
        """
        ...

    def GetHashCode(self):
        """
        GetHashCode(self: SimaticInterface) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self):
        """
        ToString(self: SimaticInterface) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class SimaticInterfaceComposition(object, IEngineeringComposition, IInternalCompositionAccess, IEnumerable[SimaticInterface], IEquatable[object]): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEnumerable'>, <type 'IInternalBaseAccess'>, <type 'IInternalCollectionAccess'>, <type 'IEngineeringInstance'>, <type 'IEngineeringCompositionOrObject'>
    """ Composition of Simatic Interfaces """
    @property
    def Parent(self):
        """
        Gets the parent.
        Get: Parent(self: SimaticInterfaceComposition) -> IEngineeringObject
        """
        ...


    def GetHashCode(self):
        """
        GetHashCode(self: SimaticInterfaceComposition) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self):
        """
        ToString(self: SimaticInterfaceComposition) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[SimaticInterface](enumerable: IEnumerable[SimaticInterface], value: SimaticInterface) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


