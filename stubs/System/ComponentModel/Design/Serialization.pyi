# encoding: utf-8
# module System.ComponentModel.Design.Serialization calls itself Serialization
# from System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class ComponentSerializationService:  # skipped bases: <type 'object'>
    """Provides the base class for serializing a set of components or serializable objects into a serialization store."""

    def CreateStore(self):
        """
        CreateStore(self: ComponentSerializationService) -> SerializationStore

            Creates a new System.ComponentModel.Design.Serialization.SerializationStore.

            Returns: A new created serialization store.
        """
        ...
    def Deserialize(self, store, container=None):
        """
        Deserialize(self: ComponentSerializationService, store: SerializationStore) -> ICollection

            Deserializes the given store to produce a collection of objects.

            store: The System.ComponentModel.Design.Serialization.SerializationStore to deserialize.

            Returns: A collection of objects created according to the stored state.

        Deserialize(self: ComponentSerializationService, store: SerializationStore, container: IContainer) -> ICollection

            Deserializes the given store and populates the given System.ComponentModel.IContainer with deserialized System.ComponentModel.IComponent objects.

            store: The System.ComponentModel.Design.Serialization.SerializationStore to deserialize.

            container: The System.ComponentModel.IContainer to which System.ComponentModel.IComponent objects will be added.

            Returns: A collection of objects created according to the stored state.
        """
        ...
    def DeserializeTo(self, store, container, validateRecycledTypes=None, applyDefaults=None):
        """
        DeserializeTo(self: ComponentSerializationService, store: SerializationStore, container: IContainer)

            Deserializes the given System.ComponentModel.Design.Serialization.SerializationStore to the given container.

            store: The System.ComponentModel.Design.Serialization.SerializationStore to deserialize.

            container: The container to which System.ComponentModel.IComponent objects will be added.

        DeserializeTo(self: ComponentSerializationService, store: SerializationStore, container: IContainer, validateRecycledTypes: bool)

            Deserializes the given System.ComponentModel.Design.Serialization.SerializationStore to the given container, optionally validating recycled types.

            store: The System.ComponentModel.Design.Serialization.SerializationStore to deserialize.

            container: The container to which System.ComponentModel.IComponent objects will be added.

            validateRecycledTypes: ue to guarantee that the deserialization will only work if applied to an object of the same type.

        DeserializeTo(self: ComponentSerializationService, store: SerializationStore, container: IContainer, validateRecycledTypes: bool, applyDefaults: bool)

            Deserializes the given System.ComponentModel.Design.Serialization.SerializationStore to the given container, optionally applying default property values.

            store: The System.ComponentModel.Design.Serialization.SerializationStore to deserialize.

            container: The container to which System.ComponentModel.IComponent objects will be added.

            validateRecycledTypes: ue to guarantee that the deserialization will only work if applied to an object of the same type.

            applyDefaults: ue to indicate that the default property values should be applied.
        """
        ...
    def LoadStore(self, stream):
        """
        LoadStore(self: ComponentSerializationService, stream: Stream) -> SerializationStore

            Loads a System.ComponentModel.Design.Serialization.SerializationStore from a stream.

            stream: The System.IO.Stream from which the store will be loaded.

            Returns: A new System.ComponentModel.Design.Serialization.SerializationStore instance.
        """
        ...
    def Serialize(self, store, value):
        """
        Serialize(self: ComponentSerializationService, store: SerializationStore, value: object)

            Serializes the given object to the given System.ComponentModel.Design.Serialization.SerializationStore.

            store: The System.ComponentModel.Design.Serialization.SerializationStore to which the state of value will be written.

            value: The object to serialize.
        """
        ...
    def SerializeAbsolute(self, store, value):
        """
        SerializeAbsolute(self: ComponentSerializationService, store: SerializationStore, value: object)

            Serializes the given object, accounting for default property values.

            store: The System.ComponentModel.Design.Serialization.SerializationStore to which the state of value will be serialized.

            value: The object to serialize.
        """
        ...
    def SerializeMember(self, store, owningObject, member):
        """
        SerializeMember(self: ComponentSerializationService, store: SerializationStore, owningObject: object, member: MemberDescriptor)

            Serializes the given member on the given object.

            store: The System.ComponentModel.Design.Serialization.SerializationStore to which the state of member will be serialized.

            owningObject: The object to which member is attached.

            member: A System.ComponentModel.MemberDescriptor specifying the member to serialize.
        """
        ...
    def SerializeMemberAbsolute(self, store, owningObject, member):
        """
        SerializeMemberAbsolute(self: ComponentSerializationService, store: SerializationStore, owningObject: object, member: MemberDescriptor)

            Serializes the given member on the given object, accounting for the default property value.

            store: The System.ComponentModel.Design.Serialization.SerializationStore to which the state of member will be serialized.

            owningObject: The object to which member is attached.

            member: The member to serialize.
        """
        ...

class ContextStack:  # skipped bases: <type 'object'>
    """
    Provides a stack object that can be used by a serializer to make information available to nested serializers.

    ContextStack()
    """

    def Append(self, context):
        """
        Append(self: ContextStack, context: object)

            Appends an object to the end of the stack, rather than pushing it onto the top of the stack.

            context: A context object to append to the stack.
        """
        ...
    def Pop(self):
        """
        Pop(self: ContextStack) -> object

            Removes the current object off of the stack, returning its value.

            Returns: The object removed from the stack; ll if no objects are on the stack.
        """
        ...
    def Push(self, context):
        """
        Push(self: ContextStack, context: object)

            Pushes, or places, the specified object onto the stack.

            context: The context object to push onto the stack.
        """
        ...
    def __getitem__(self, *args):  # cannot find CLR method
        """x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y]"""
        ...
    @property
    def Current(self):
        """
        Gets the current object on the stack.

        Get: Current(self: ContextStack) -> object
        """
        ...

class DefaultSerializationProviderAttribute(Attribute):  # skipped bases: <type '_Attribute'>
    """
    The System.ComponentModel.Design.Serialization.DefaultSerializationProviderAttribute attribute is placed on a serializer to indicate the class to use as a default provider of that type of serializer.

    DefaultSerializationProviderAttribute(providerType: Type)

    DefaultSerializationProviderAttribute(providerTypeName: str)
    """

    @staticmethod  # known case of __new__
    def __new__(cls, *__args):
        """
        __new__(cls: type, providerType: Type)

        __new__(cls: type, providerTypeName: str)
        """
        ...
    @property
    def ProviderTypeName(self):
        """
        Gets the type name of the serialization provider.

        Get: ProviderTypeName(self: DefaultSerializationProviderAttribute) -> str
        """
        ...

class DesignerLoader:  # skipped bases: <type 'object'>
    """Provides a basic designer loader interface that can be used to implement a custom designer loader."""

    def BeginLoad(self, host):
        """
        BeginLoad(self: DesignerLoader, host: IDesignerLoaderHost)

            Begins loading a designer.

            host: The loader host through which this loader loads components.
        """
        ...
    def Dispose(self):
        """
        Dispose(self: DesignerLoader)

            Releases all resources used by the System.ComponentModel.Design.Serialization.DesignerLoader.
        """
        ...
    def Flush(self):
        """
        Flush(self: DesignerLoader)

            Writes cached changes to the location that the designer was loaded from.
        """
        ...
    @property
    def Loading(self):
        """
        Gets a value indicating whether the loader is currently loading a document.

        Get: Loading(self: DesignerLoader) -> bool
        """
        ...

class DesignerSerializerAttribute(Attribute):  # skipped bases: <type '_Attribute'>
    """
    Indicates a serializer for the serialization manager to use to serialize the values of the type this attribute is applied to. This class cannot be inherited.

    DesignerSerializerAttribute(serializerType: Type, baseSerializerType: Type)

    DesignerSerializerAttribute(serializerTypeName: str, baseSerializerType: Type)

    DesignerSerializerAttribute(serializerTypeName: str, baseSerializerTypeName: str)
    """

    @staticmethod  # known case of __new__
    def __new__(cls, *__args):
        """
        __new__(cls: type, serializerType: Type, baseSerializerType: Type)

        __new__(cls: type, serializerTypeName: str, baseSerializerType: Type)

        __new__(cls: type, serializerTypeName: str, baseSerializerTypeName: str)
        """
        ...
    @property
    def SerializerBaseTypeName(self):
        """
        Gets the fully qualified type name of the serializer base type.

        Get: SerializerBaseTypeName(self: DesignerSerializerAttribute) -> str
        """
        ...
    @property
    def SerializerTypeName(self):
        """
        Gets the fully qualified type name of the serializer.

        Get: SerializerTypeName(self: DesignerSerializerAttribute) -> str
        """
        ...
    @property
    def TypeId(self):
        """
        Indicates a unique ID for this attribute type.

        Get: TypeId(self: DesignerSerializerAttribute) -> object
        """
        ...

class IDesignerLoaderHost(IDesignerHost):  # skipped bases: <type 'IServiceProvider'>, <type 'IServiceContainer'>
    """Provides an interface that can extend a designer host to support loading from a serialized state."""

    def EndLoad(self, baseClassName, successful, errorCollection):
        """
        EndLoad(self: IDesignerLoaderHost, baseClassName: str, successful: bool, errorCollection: ICollection)

            Ends the designer loading operation.

            baseClassName: The fully qualified name of the base class of the document that this designer is designing.

            successful: ue if the designer is successfully loaded; otherwise, lse.

            errorCollection: A collection containing the errors encountered during load, if any. If no errors were encountered, pass either an empty collection or ll.
        """
        ...
    def Reload(self):
        """
        Reload(self: IDesignerLoaderHost)

            Reloads the design document.
        """
        ...

class IDesignerLoaderHost2(
    IDesignerLoaderHost
):  # skipped bases: <type 'IDesignerHost'>, <type 'IServiceProvider'>, <type 'IServiceContainer'>
    """Provides an interface that extends System.ComponentModel.Design.Serialization.IDesignerLoaderHost to specify whether errors are tolerated while loading a design document."""

    @property
    def CanReloadWithErrors(self):
        """
        Gets or sets a value indicating whether it is possible to reload with errors.

        Get: CanReloadWithErrors(self: IDesignerLoaderHost2) -> bool

        Set: CanReloadWithErrors(self: IDesignerLoaderHost2) = value
        """
        ...
    @property
    def IgnoreErrorsDuringReload(self):
        """
        Gets or sets a value indicating whether errors should be ignored when System.ComponentModel.Design.Serialization.IDesignerLoaderHost.Reload is called.

        Get: IgnoreErrorsDuringReload(self: IDesignerLoaderHost2) -> bool

        Set: IgnoreErrorsDuringReload(self: IDesignerLoaderHost2) = value
        """
        ...

class IDesignerLoaderService:
    """Provides an interface that can extend a designer loader to support asynchronous loading of external components."""

    def AddLoadDependency(self):
        """
        AddLoadDependency(self: IDesignerLoaderService)

            Registers an external component as part of the load process managed by this interface.
        """
        ...
    def DependentLoadComplete(self, successful, errorCollection):
        """
        DependentLoadComplete(self: IDesignerLoaderService, successful: bool, errorCollection: ICollection)

            Signals that a dependent load has finished.

            successful: ue if the load of the designer is successful; lse if errors prevented the load from finishing.

            errorCollection: A collection of errors that occurred during the load, if any. If no errors occurred, pass either an empty collection or ll.
        """
        ...
    def Reload(self):
        """
        Reload(self: IDesignerLoaderService) -> bool

            Reloads the design document.

            Returns: ue if the reload request is accepted, or lse if the loader does not allow the reload.
        """
        ...

class IDesignerSerializationManager(IServiceProvider):
    """Provides an interface that can manage design-time serialization."""

    def AddSerializationProvider(self, provider):
        """
        AddSerializationProvider(self: IDesignerSerializationManager, provider: IDesignerSerializationProvider)

            Adds the specified serialization provider to the serialization manager.

            provider: The serialization provider to add.
        """
        ...
    def CreateInstance(self, type, arguments, name, addToContainer):
        """
        CreateInstance(self: IDesignerSerializationManager, type: Type, arguments: ICollection, name: str, addToContainer: bool) -> object

            Creates an instance of the specified type and adds it to a collection of named instances.

            type: The data type to create.

            arguments: The arguments to pass to the constructor for this type.

            name: The name of the object. This name can be used to access the object later through

             System.ComponentModel.Design.Serialization.IDesignerSerializationManager.GetInstance(System.String). If ll is passed, the object is still created but cannot be

             accessed by name.

            addToContainer: If ue, this object is added to the design container. The object must implement System.ComponentModel.IComponent for this to have any effect.

            Returns: The newly created object instance.
        """
        ...
    def GetInstance(self, name):
        """
        GetInstance(self: IDesignerSerializationManager, name: str) -> object

            Gets an instance of a created object of the specified name, or ll if that object does not exist.

            name: The name of the object to retrieve.

            Returns: An instance of the object with the given name, or ll if no object by that name can be found.
        """
        ...
    def GetName(self, value):
        """
        GetName(self: IDesignerSerializationManager, value: object) -> str

            Gets the name of the specified object, or ll if the object has no name.

            value: The object to retrieve the name for.

            Returns: The name of the object, or ll if the object is unnamed.
        """
        ...
    def GetSerializer(self, objectType, serializerType):
        """
        GetSerializer(self: IDesignerSerializationManager, objectType: Type, serializerType: Type) -> object

            Gets a serializer of the requested type for the specified object type.

            objectType: The type of the object to get the serializer for.

            serializerType: The type of the serializer to retrieve.

            Returns: An instance of the requested serializer, or ll if no appropriate serializer can be located.
        """
        ...
    def GetType(self, typeName):
        """
        GetType(self: IDesignerSerializationManager, typeName: str) -> Type

            Gets a type of the specified name.

            typeName: The fully qualified name of the type to load.

            Returns: An instance of the type, or ll if the type cannot be loaded.
        """
        ...
    def RemoveSerializationProvider(self, provider):
        """
        RemoveSerializationProvider(self: IDesignerSerializationManager, provider: IDesignerSerializationProvider)

            Removes a custom serialization provider from the serialization manager.

            provider: The provider to remove. This object must have been added using

             System.ComponentModel.Design.Serialization.IDesignerSerializationManager.AddSerializationProvider(System.ComponentModel.Design.Serialization.IDesignerSerializationProvi

             der).
        """
        ...
    def ReportError(self, errorInformation):
        """
        ReportError(self: IDesignerSerializationManager, errorInformation: object)

            Reports an error in serialization.

            errorInformation: The error to report. This information object can be of any object type. If it is an exception, the message of the exception is extracted and reported to the user. If

             it is any other type, System.Object.ToString is called to display the information to the user.
        """
        ...
    def SetName(self, instance, name):
        """
        SetName(self: IDesignerSerializationManager, instance: object, name: str)

            Sets the name of the specified existing object.

            instance: The object instance to name.

            name: The name to give the instance.
        """
        ...
    @property
    def Context(self):
        """
        Gets a stack-based, user-defined storage area that is useful for communication between serializers.

        Get: Context(self: IDesignerSerializationManager) -> ContextStack
        """
        ...
    @property
    def Properties(self):
        """
        Indicates custom properties that can be serializable with available serializers.

        Get: Properties(self: IDesignerSerializationManager) -> PropertyDescriptorCollection
        """
        ...
    ResolveName = None
    SerializationComplete = None

class IDesignerSerializationProvider:
    """Provides an interface that enables access to a serializer."""

    def GetSerializer(self, manager, currentSerializer, objectType, serializerType):
        """
        GetSerializer(self: IDesignerSerializationProvider, manager: IDesignerSerializationManager, currentSerializer: object, objectType: Type, serializerType: Type) -> object

            Gets a serializer using the specified attributes.

            manager: The serialization manager requesting the serializer.

            currentSerializer: An instance of the current serializer of the specified type. This can be ll if no serializer of the specified type exists.

            objectType: The data type of the object to serialize.

            serializerType: The data type of the serializer to create.

            Returns: An instance of a serializer of the type requested, or ll if the request cannot be satisfied.
        """
        ...

class IDesignerSerializationService:
    """Provides an interface that can invoke serialization and deserialization."""

    def Deserialize(self, serializationData):
        """
        Deserialize(self: IDesignerSerializationService, serializationData: object) -> ICollection

            Deserializes the specified serialization data object and returns a collection of objects represented by that data.

            serializationData: An object consisting of serialized data.

            Returns: An System.Collections.ICollection of objects rebuilt from the specified serialization data object.
        """
        ...
    def Serialize(self, objects):
        """
        Serialize(self: IDesignerSerializationService, objects: ICollection) -> object

            Serializes the specified collection of objects and stores them in a serialization data object.

            objects: A collection of objects to serialize.

            Returns: An object that contains the serialized state of the specified collection of objects.
        """
        ...

class INameCreationService:
    """Provides a service that can generate unique names for objects."""

    def CreateName(self, container, dataType):
        """
        CreateName(self: INameCreationService, container: IContainer, dataType: Type) -> str

            Creates a new name that is unique to all components in the specified container.

            container: The container where the new object is added.

            dataType: The data type of the object that receives the name.

            Returns: A unique name for the data type.
        """
        ...
    def IsValidName(self, name):
        """
        IsValidName(self: INameCreationService, name: str) -> bool

            Gets a value indicating whether the specified name is valid.

            name: The name to validate.

            Returns: ue if the name is valid; otherwise, lse.
        """
        ...
    def ValidateName(self, name):
        """
        ValidateName(self: INameCreationService, name: str)

            Gets a value indicating whether the specified name is valid.

            name: The name to validate.
        """
        ...

class InstanceDescriptor:  # skipped bases: <type 'object'>
    """
    Provides the information necessary to create an instance of an object. This class cannot be inherited.

    InstanceDescriptor(member: MemberInfo, arguments: ICollection)

    InstanceDescriptor(member: MemberInfo, arguments: ICollection, isComplete: bool)
    """

    def Invoke(self):
        """
        Invoke(self: InstanceDescriptor) -> object

            Invokes this instance descriptor and returns the object the descriptor describes.

            Returns: The object this instance descriptor describes.
        """
        ...
    @property
    def Arguments(self):
        """
        Gets the collection of arguments that can be used to reconstruct an instance of the object that this instance descriptor represents.

        Get: Arguments(self: InstanceDescriptor) -> ICollection
        """
        ...
    @property
    def IsComplete(self):
        """
        Gets a value indicating whether the contents of this System.ComponentModel.Design.Serialization.InstanceDescriptor completely identify the instance.

        Get: IsComplete(self: InstanceDescriptor) -> bool
        """
        ...
    @property
    def MemberInfo(self):
        """
        Gets the member information that describes the instance this descriptor is associated with.

        Get: MemberInfo(self: InstanceDescriptor) -> MemberInfo
        """
        ...

class MemberRelationship:  # skipped bases: <type 'object'>
    """
    Represents a single relationship between an object and a member.

    MemberRelationship(owner: object, member: MemberDescriptor)
    """

    def Equals(self, obj):
        """
        Equals(self: MemberRelationship, obj: object) -> bool

            Determines whether two System.ComponentModel.Design.Serialization.MemberRelationship instances are equal.

            obj: The System.ComponentModel.Design.Serialization.MemberRelationship to compare with the current System.ComponentModel.Design.Serialization.MemberRelationship.

            Returns: ue if the specified System.ComponentModel.Design.Serialization.MemberRelationship is equal to the current

             System.ComponentModel.Design.Serialization.MemberRelationship; otherwise, lse.
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: MemberRelationship) -> int

            Returns the hash code for this instance.

            Returns: A hash code for the current System.ComponentModel.Design.Serialization.MemberRelationship.
        """
        ...
    def __eq__(self, *args):  # cannot find CLR method
        """x.__eq__(y) <==> x==y"""
        ...
    def __ne__(self, *args): ...
    @property
    def IsEmpty(self):
        """
        Gets a value indicating whether this relationship is equal to the System.ComponentModel.Design.Serialization.MemberRelationship.Empty relationship.

        Get: IsEmpty(self: MemberRelationship) -> bool
        """
        ...
    @property
    def Member(self):
        """
        Gets the related member.

        Get: Member(self: MemberRelationship) -> MemberDescriptor
        """
        ...
    @property
    def Owner(self):
        """
        Gets the owning object.

        Get: Owner(self: MemberRelationship) -> object
        """
        ...
    Empty = None

class MemberRelationshipService:  # skipped bases: <type 'object'>
    """Provides the base class for relating one member to another."""

    def GetRelationship(self, *args):  # cannot find CLR method
        """
        GetRelationship(self: MemberRelationshipService, source: MemberRelationship) -> MemberRelationship

            Gets a relationship to the given source relationship.

            source: The source relationship.

            Returns: A relationship to source, or System.ComponentModel.Design.Serialization.MemberRelationship.Empty if no relationship exists.
        """
        ...
    def SetRelationship(self, *args):  # cannot find CLR method
        """
        SetRelationship(self: MemberRelationshipService, source: MemberRelationship, relationship: MemberRelationship)

            Creates a relationship between the source object and target relationship.

            source: The source relationship.

            relationship: The relationship to set into the source.
        """
        ...
    def SupportsRelationship(self, source, relationship):
        """
        SupportsRelationship(self: MemberRelationshipService, source: MemberRelationship, relationship: MemberRelationship) -> bool

            Gets a value indicating whether the given relationship is supported.

            source: The source relationship.

            relationship: The relationship to set into the source.

            Returns: ue if a relationship between the given two objects is supported; otherwise, lse.
        """
        ...
    def __getitem__(self, *args):  # cannot find CLR method
        """x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y]"""
        ...
    def __setitem__(self, *args):  # cannot find CLR method
        """x.__setitem__(i, y) <==> x[i]=x.__setitem__(i, y) <==> x[i]="""
        ...

class ResolveNameEventArgs(EventArgs):
    """
    Provides data for the System.ComponentModel.Design.Serialization.IDesignerSerializationManager.ResolveName event.

    ResolveNameEventArgs(name: str)
    """

    @staticmethod  # known case of __new__
    def __new__(cls, name):
        """__new__(cls: type, name: str)"""
        ...
    @property
    def Name(self):
        """
        Gets the name of the object to resolve.

        Get: Name(self: ResolveNameEventArgs) -> str
        """
        ...
    @property
    def Value(self):
        """
        Gets or sets the object that matches the name.

        Get: Value(self: ResolveNameEventArgs) -> object

        Set: Value(self: ResolveNameEventArgs) = value
        """
        ...

class ResolveNameEventHandler(MulticastDelegate):  # skipped bases: <type 'ICloneable'>, <type 'ISerializable'>
    """
    Represents the method that handles the System.ComponentModel.Design.Serialization.IDesignerSerializationManager.ResolveName event of a serialization manager.

    ResolveNameEventHandler(object: object, method: IntPtr)
    """

    def BeginInvoke(self, sender, e, callback, object):
        """BeginInvoke(self: ResolveNameEventHandler, sender: object, e: ResolveNameEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult"""
        ...
    def EndInvoke(self, result):
        """EndInvoke(self: ResolveNameEventHandler, result: IAsyncResult)"""
        ...
    def Invoke(self, sender, e):
        """Invoke(self: ResolveNameEventHandler, sender: object, e: ResolveNameEventArgs)"""
        ...

class RootDesignerSerializerAttribute(Attribute):  # skipped bases: <type '_Attribute'>
    """
    Indicates the base serializer to use for a root designer object. This class cannot be inherited.

    RootDesignerSerializerAttribute(serializerType: Type, baseSerializerType: Type, reloadable: bool)

    RootDesignerSerializerAttribute(serializerTypeName: str, baseSerializerType: Type, reloadable: bool)

    RootDesignerSerializerAttribute(serializerTypeName: str, baseSerializerTypeName: str, reloadable: bool)
    """

    @staticmethod  # known case of __new__
    def __new__(cls, *__args):
        """
        __new__(cls: type, serializerType: Type, baseSerializerType: Type, reloadable: bool)

        __new__(cls: type, serializerTypeName: str, baseSerializerType: Type, reloadable: bool)

        __new__(cls: type, serializerTypeName: str, baseSerializerTypeName: str, reloadable: bool)
        """
        ...
    @property
    def Reloadable(self):
        """
        Gets a value indicating whether the root serializer supports reloading of the design document without first disposing the designer host.

        Get: Reloadable(self: RootDesignerSerializerAttribute) -> bool
        """
        ...
    @property
    def SerializerBaseTypeName(self):
        """
        Gets the fully qualified type name of the base type of the serializer.

        Get: SerializerBaseTypeName(self: RootDesignerSerializerAttribute) -> str
        """
        ...
    @property
    def SerializerTypeName(self):
        """
        Gets the fully qualified type name of the serializer.

        Get: SerializerTypeName(self: RootDesignerSerializerAttribute) -> str
        """
        ...
    @property
    def TypeId(self):
        """
        Gets a unique ID for this attribute type.

        Get: TypeId(self: RootDesignerSerializerAttribute) -> object
        """
        ...

class SerializationStore(object, IDisposable):
    """Provides the base class for storing serialization data for the System.ComponentModel.Design.Serialization.ComponentSerializationService."""

    def Close(self):
        """
        Close(self: SerializationStore)

            Closes the serialization store.
        """
        ...
    def Save(self, stream):
        """
        Save(self: SerializationStore, stream: Stream)

            Saves the store to the given stream.

            stream: The stream to which the store will be serialized.
        """
        ...
    @property
    def Errors(self):
        """
        Gets a collection of errors that occurred during serialization or deserialization.

        Get: Errors(self: SerializationStore) -> ICollection
        """
        ...
