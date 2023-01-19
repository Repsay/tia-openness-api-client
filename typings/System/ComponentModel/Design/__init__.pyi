# encoding: utf-8
# module System.ComponentModel.Design calls itself Design
# from System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class ActiveDesignerEventArgs(EventArgs):
    """
    Provides data for the System.ComponentModel.Design.IDesignerEventService.ActiveDesigner event.

    ActiveDesignerEventArgs(oldDesigner: IDesignerHost, newDesigner: IDesignerHost)
    """
    @property
    def NewDesigner(self):
        """
        Gets the document that is gaining activation.

        Get: NewDesigner(self: ActiveDesignerEventArgs) -> IDesignerHost
        """
        ...

    @property
    def OldDesigner(self):
        """
        Gets the document that is losing activation.

        Get: OldDesigner(self: ActiveDesignerEventArgs) -> IDesignerHost
        """
        ...


    @staticmethod # known case of __new__
    def __new__(cls, oldDesigner, newDesigner):
        """ __new__(cls: type, oldDesigner: IDesignerHost, newDesigner: IDesignerHost) """
        ...


class ActiveDesignerEventHandler(MulticastDelegate): # skipped bases: <type 'ICloneable'>, <type 'ISerializable'>
    """
    Represents the method that will handle the System.ComponentModel.Design.IDesignerEventService.ActiveDesignerChanged event.

    ActiveDesignerEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: ActiveDesignerEventHandler, sender: object, e: ActiveDesignerEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result):
        """ EndInvoke(self: ActiveDesignerEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender, e):
        """ Invoke(self: ActiveDesignerEventHandler, sender: object, e: ActiveDesignerEventArgs) """
        ...


class CheckoutException(ExternalException): # skipped bases: <type 'ISerializable'>, <type '_Exception'>
    """
    The exception that is thrown when an attempt to check out a file that is checked into a source code management program is canceled or fails.

    CheckoutException()

    CheckoutException(message: str)

    CheckoutException(message: str, errorCode: int)

    CheckoutException(message: str, innerException: Exception)
    """
    Canceled = None
    SerializeObjectState = None


class CommandID: # skipped bases: <type 'object'>
    """
    Represents a unique command identifier that consists of a numeric command ID and a GUID menu group identifier.

    CommandID(menuGroup: Guid, commandID: int)
    """
    @property
    def Guid(self):
        """
        Gets the GUID of the menu group that the menu command identified by this System.ComponentModel.Design.CommandID belongs to.

        Get: Guid(self: CommandID) -> Guid
        """
        ...

    @property
    def ID(self):
        """
        Gets the numeric command ID.

        Get: ID(self: CommandID) -> int
        """
        ...


    def Equals(self, obj):
        """
        Equals(self: CommandID, obj: object) -> bool

            Determines whether two System.ComponentModel.Design.CommandID instances are equal.

            obj: The object to compare.

            Returns: ue if the specified object is equivalent to this one; otherwise, lse.
        """
        ...

    def GetHashCode(self):
        """
        GetHashCode(self: CommandID) -> int

            Serves as a hash function for a particular type.

            Returns: A hash code for the current System.Object.
        """
        ...

    def ToString(self):
        """
        ToString(self: CommandID) -> str

            Returns a System.String that represents the current object.

            Returns: A string that contains the command ID information, both the GUID and integer identifier.
        """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ComponentChangedEventArgs(EventArgs):
    """
    Provides data for the System.ComponentModel.Design.IComponentChangeService.ComponentChanged event. This class cannot be inherited.

    ComponentChangedEventArgs(component: object, member: MemberDescriptor, oldValue: object, newValue: object)
    """
    @property
    def Component(self):
        """
        Gets the component that was modified.

        Get: Component(self: ComponentChangedEventArgs) -> object
        """
        ...

    @property
    def Member(self):
        """
        Gets the member that has been changed.

        Get: Member(self: ComponentChangedEventArgs) -> MemberDescriptor
        """
        ...

    @property
    def NewValue(self):
        """
        Gets the new value of the changed member.

        Get: NewValue(self: ComponentChangedEventArgs) -> object
        """
        ...

    @property
    def OldValue(self):
        """
        Gets the old value of the changed member.

        Get: OldValue(self: ComponentChangedEventArgs) -> object
        """
        ...


    @staticmethod # known case of __new__
    def __new__(cls, component, member, oldValue, newValue):
        """ __new__(cls: type, component: object, member: MemberDescriptor, oldValue: object, newValue: object) """
        ...


class ComponentChangedEventHandler(MulticastDelegate): # skipped bases: <type 'ICloneable'>, <type 'ISerializable'>
    """
    Represents the method that will handle a System.ComponentModel.Design.IComponentChangeService.ComponentChanged event.

    ComponentChangedEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: ComponentChangedEventHandler, sender: object, e: ComponentChangedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result):
        """ EndInvoke(self: ComponentChangedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender, e):
        """ Invoke(self: ComponentChangedEventHandler, sender: object, e: ComponentChangedEventArgs) """
        ...


class ComponentChangingEventArgs(EventArgs):
    """
    Provides data for the System.ComponentModel.Design.IComponentChangeService.ComponentChanging event. This class cannot be inherited.

    ComponentChangingEventArgs(component: object, member: MemberDescriptor)
    """
    @property
    def Component(self):
        """
        Gets the component that is about to be changed or the component that is the parent container of the member that is about to be changed.

        Get: Component(self: ComponentChangingEventArgs) -> object
        """
        ...

    @property
    def Member(self):
        """
        Gets the member that is about to be changed.

        Get: Member(self: ComponentChangingEventArgs) -> MemberDescriptor
        """
        ...


    @staticmethod # known case of __new__
    def __new__(cls, component, member):
        """ __new__(cls: type, component: object, member: MemberDescriptor) """
        ...


class ComponentChangingEventHandler(MulticastDelegate): # skipped bases: <type 'ICloneable'>, <type 'ISerializable'>
    """
    Represents the method that will handle a System.ComponentModel.Design.IComponentChangeService.ComponentChanging event.

    ComponentChangingEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: ComponentChangingEventHandler, sender: object, e: ComponentChangingEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result):
        """ EndInvoke(self: ComponentChangingEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender, e):
        """ Invoke(self: ComponentChangingEventHandler, sender: object, e: ComponentChangingEventArgs) """
        ...


class ComponentEventArgs(EventArgs):
    """
    Provides data for the System.ComponentModel.Design.IComponentChangeService.ComponentAdded, System.ComponentModel.Design.IComponentChangeService.ComponentAdding, System.ComponentModel.Design.IComponentChangeService.ComponentRemoved, and System.ComponentModel.Design.IComponentChangeService.ComponentRemoving events.

    ComponentEventArgs(component: IComponent)
    """
    @property
    def Component(self):
        """
        Gets the component associated with the event.

        Get: Component(self: ComponentEventArgs) -> IComponent
        """
        ...


    @staticmethod # known case of __new__
    def __new__(cls, component):
        """ __new__(cls: type, component: IComponent) """
        ...


class ComponentEventHandler(MulticastDelegate): # skipped bases: <type 'ICloneable'>, <type 'ISerializable'>
    """
    Represents the method that will handle the System.ComponentModel.Design.IComponentChangeService.ComponentAdding, System.ComponentModel.Design.IComponentChangeService.ComponentAdded, System.ComponentModel.Design.IComponentChangeService.ComponentRemoving, and System.ComponentModel.Design.IComponentChangeService.ComponentRemoved events raised for component-level events.

    ComponentEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: ComponentEventHandler, sender: object, e: ComponentEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result):
        """ EndInvoke(self: ComponentEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender, e):
        """ Invoke(self: ComponentEventHandler, sender: object, e: ComponentEventArgs) """
        ...


class ComponentRenameEventArgs(EventArgs):
    """
    Provides data for the System.ComponentModel.Design.IComponentChangeService.ComponentRename event.

    ComponentRenameEventArgs(component: object, oldName: str, newName: str)
    """
    @property
    def Component(self):
        """
        Gets the component that is being renamed.

        Get: Component(self: ComponentRenameEventArgs) -> object
        """
        ...

    @property
    def NewName(self):
        """
        Gets the name of the component after the rename event.

        Get: NewName(self: ComponentRenameEventArgs) -> str
        """
        ...

    @property
    def OldName(self):
        """
        Gets the name of the component before the rename event.

        Get: OldName(self: ComponentRenameEventArgs) -> str
        """
        ...


    @staticmethod # known case of __new__
    def __new__(cls, component, oldName, newName):
        """ __new__(cls: type, component: object, oldName: str, newName: str) """
        ...


class ComponentRenameEventHandler(MulticastDelegate): # skipped bases: <type 'ICloneable'>, <type 'ISerializable'>
    """
    Represents the method that will handle a System.ComponentModel.Design.IComponentChangeService.ComponentRename event.

    ComponentRenameEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: ComponentRenameEventHandler, sender: object, e: ComponentRenameEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result):
        """ EndInvoke(self: ComponentRenameEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender, e):
        """ Invoke(self: ComponentRenameEventHandler, sender: object, e: ComponentRenameEventArgs) """
        ...


class DesignerCollection(object, ICollection): # skipped bases: <type 'IEnumerable'>
    """
    Represents a collection of designers.

    DesignerCollection(designers: Array[IDesignerHost])

    DesignerCollection(designers: IList)
    """
    def GetEnumerator(self):
        """
        GetEnumerator(self: DesignerCollection) -> IEnumerator

            Gets a new enumerator for this collection.

            Returns: An System.Collections.IEnumerator that enumerates the collection.
        """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...


class DesignerEventArgs(EventArgs):
    """
    Provides data for the System.ComponentModel.Design.IDesignerEventService.DesignerCreated and System.ComponentModel.Design.IDesignerEventService.DesignerDisposed events.

    DesignerEventArgs(host: IDesignerHost)
    """
    @property
    def Designer(self):
        """
        Gets the host of the document.

        Get: Designer(self: DesignerEventArgs) -> IDesignerHost
        """
        ...


    @staticmethod # known case of __new__
    def __new__(cls, host):
        """ __new__(cls: type, host: IDesignerHost) """
        ...


class DesignerEventHandler(MulticastDelegate): # skipped bases: <type 'ICloneable'>, <type 'ISerializable'>
    """
    Represents the method that will handle the System.ComponentModel.Design.IDesignerEventService.DesignerCreated and System.ComponentModel.Design.IDesignerEventService.DesignerDisposed events that are raised when a document is created or disposed of.

    DesignerEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: DesignerEventHandler, sender: object, e: DesignerEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result):
        """ EndInvoke(self: DesignerEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender, e):
        """ Invoke(self: DesignerEventHandler, sender: object, e: DesignerEventArgs) """
        ...


class IDesignerOptionService:
    """ Provides access to the designer options located on the Tools menu under the Options command in the Visual Studio development environment. """
    def GetOptionValue(self, pageName, valueName):
        """
        GetOptionValue(self: IDesignerOptionService, pageName: str, valueName: str) -> object

            Gets the value of the specified Windows Forms Designer option.

            pageName: The name of the page that defines the option.

            valueName: The name of the option property.

            Returns: The value of the specified option.
        """
        ...

    def SetOptionValue(self, pageName, valueName, value):
        """
        SetOptionValue(self: IDesignerOptionService, pageName: str, valueName: str, value: object)

            Sets the value of the specified Windows Forms Designer option.

            pageName: The name of the page that defines the option.

            valueName: The name of the option property.

            value: The new value.
        """
        ...


class DesignerOptionService(object, IDesignerOptionService):
    """ Provides a base class for getting and setting option values for a designer. """
    @property
    def Options(self):
        """
        Gets the options collection for this service.

        Get: Options(self: DesignerOptionService) -> DesignerOptionCollection
        """
        ...


    def CreateOptionCollection(self, *args): #cannot find CLR method
        """ CreateOptionCollection(self: DesignerOptionService, parent: DesignerOptionCollection, name: str, value: object) -> DesignerOptionCollection """
        ...

    def DesignerOptionCollection(self, *args): #cannot find CLR method
        # no doc
        ...

    def PopulateOptionCollection(self, *args): #cannot find CLR method
        """ PopulateOptionCollection(self: DesignerOptionService, options: DesignerOptionCollection) """
        ...

    def ShowDialog(self, *args): #cannot find CLR method
        """ ShowDialog(self: DesignerOptionService, options: DesignerOptionCollection, optionObject: object) -> bool """
        ...

    DesignerOptionCollection = None


class DesignerTransaction(object, IDisposable):
    """ Provides a way to group a series of design-time actions to improve performance and enable most types of changes to be undone. """
    @property
    def Canceled(self):
        """
        Gets a value indicating whether the transaction was canceled.

        Get: Canceled(self: DesignerTransaction) -> bool
        """
        ...

    @property
    def Committed(self):
        """
        Gets a value indicating whether the transaction was committed.

        Get: Committed(self: DesignerTransaction) -> bool
        """
        ...

    @property
    def Description(self):
        """
        Gets a description for the transaction.

        Get: Description(self: DesignerTransaction) -> str
        """
        ...


    def Cancel(self):
        """
        Cancel(self: DesignerTransaction)

            Cancels the transaction and attempts to roll back the changes made by the events of the transaction.
        """
        ...

    def Commit(self):
        """
        Commit(self: DesignerTransaction)

            Commits this transaction.
        """
        ...

    def OnCancel(self, *args): #cannot find CLR method
        """
        OnCancel(self: DesignerTransaction)

            Raises the ncel event.
        """
        ...

    def OnCommit(self, *args): #cannot find CLR method
        """
        OnCommit(self: DesignerTransaction)

            Performs the actual work of committing a transaction.
        """
        ...


class DesignerTransactionCloseEventArgs(EventArgs):
    """
    Provides data for the System.ComponentModel.Design.IDesignerHost.TransactionClosed and System.ComponentModel.Design.IDesignerHost.TransactionClosing events.

    DesignerTransactionCloseEventArgs(commit: bool)

    DesignerTransactionCloseEventArgs(commit: bool, lastTransaction: bool)
    """
    @property
    def LastTransaction(self):
        """
        Gets a value indicating whether this is the last transaction to close.

        Get: LastTransaction(self: DesignerTransactionCloseEventArgs) -> bool
        """
        ...

    @property
    def TransactionCommitted(self):
        """
        Indicates whether the designer called System.ComponentModel.Design.DesignerTransaction.Commit on the transaction.

        Get: TransactionCommitted(self: DesignerTransactionCloseEventArgs) -> bool
        """
        ...


    @staticmethod # known case of __new__
    def __new__(cls, commit, lastTransaction=None):
        """
        __new__(cls: type, commit: bool)

        __new__(cls: type, commit: bool, lastTransaction: bool)
        """
        ...


class DesignerTransactionCloseEventHandler(MulticastDelegate): # skipped bases: <type 'ICloneable'>, <type 'ISerializable'>
    """
    Represents the method that handles the System.ComponentModel.Design.IDesignerHost.TransactionClosed and System.ComponentModel.Design.IDesignerHost.TransactionClosing events of a designer.

    DesignerTransactionCloseEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: DesignerTransactionCloseEventHandler, sender: object, e: DesignerTransactionCloseEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result):
        """ EndInvoke(self: DesignerTransactionCloseEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender, e):
        """ Invoke(self: DesignerTransactionCloseEventHandler, sender: object, e: DesignerTransactionCloseEventArgs) """
        ...


class MenuCommand: # skipped bases: <type 'object'>
    """
    Represents a Windows menu or toolbar command item.

    MenuCommand(handler: EventHandler, command: CommandID)
    """
    @property
    def Checked(self):
        """
        Gets or sets a value indicating whether this menu item is checked.

        Get: Checked(self: MenuCommand) -> bool

        Set: Checked(self: MenuCommand) = value
        """
        ...

    @property
    def CommandID(self):
        """
        Gets the System.ComponentModel.Design.CommandID associated with this menu command.

        Get: CommandID(self: MenuCommand) -> CommandID
        """
        ...

    @property
    def Enabled(self):
        """
        Gets a value indicating whether this menu item is available.

        Get: Enabled(self: MenuCommand) -> bool

        Set: Enabled(self: MenuCommand) = value
        """
        ...

    @property
    def OleStatus(self):
        """
        Gets the OLE command status code for this menu item.

        Get: OleStatus(self: MenuCommand) -> int
        """
        ...

    @property
    def Properties(self):
        """
        Gets the public properties associated with the System.ComponentModel.Design.MenuCommand.

        Get: Properties(self: MenuCommand) -> IDictionary
        """
        ...

    @property
    def Supported(self):
        """
        Gets or sets a value indicating whether this menu item is supported.

        Get: Supported(self: MenuCommand) -> bool

        Set: Supported(self: MenuCommand) = value
        """
        ...

    @property
    def Visible(self):
        """
        Gets or sets a value indicating whether this menu item is visible.

        Get: Visible(self: MenuCommand) -> bool

        Set: Visible(self: MenuCommand) = value
        """
        ...


    def Invoke(self, arg=None):
        """
        Invoke(self: MenuCommand)

            Invokes the command.

        Invoke(self: MenuCommand, arg: object)

            Invokes the command with the given parameter.

            arg: An optional argument for use by the command.
        """
        ...

    def OnCommandChanged(self, *args): #cannot find CLR method
        """
        OnCommandChanged(self: MenuCommand, e: EventArgs)

            Raises the System.ComponentModel.Design.MenuCommand.CommandChanged event.

            e: An System.EventArgs that contains the event data.
        """
        ...

    def ToString(self):
        """
        ToString(self: MenuCommand) -> str

            Returns a string representation of this menu command.

            Returns: A string containing the value of the System.ComponentModel.Design.MenuCommand.CommandID property appended with the names of any flags that are set,

             separated by pipe bars (|). These flag properties include System.ComponentModel.Design.MenuCommand.Checked,

             System.ComponentModel.Design.MenuCommand.Enabled, System.ComponentModel.Design.MenuCommand.Supported, and

             System.ComponentModel.Design.MenuCommand.Visible.
        """
        ...

    CommandChanged = None


class DesignerVerb(MenuCommand):
    """
    Represents a verb that can be invoked from a designer.

    DesignerVerb(text: str, handler: EventHandler)

    DesignerVerb(text: str, handler: EventHandler, startCommandID: CommandID)
    """
    @property
    def Description(self):
        """
        Gets or sets the description of the menu item for the verb.

        Get: Description(self: DesignerVerb) -> str

        Set: Description(self: DesignerVerb) = value
        """
        ...

    @property
    def Text(self):
        """
        Gets the text description for the verb command on the menu.

        Get: Text(self: DesignerVerb) -> str
        """
        ...



class DesignerVerbCollection(CollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>
    """
    Represents a collection of System.ComponentModel.Design.DesignerVerb objects.

    DesignerVerbCollection()

    DesignerVerbCollection(value: Array[DesignerVerb])
    """
    def Add(self, value):
        """
        Add(self: DesignerVerbCollection, value: DesignerVerb) -> int

            Adds the specified System.ComponentModel.Design.DesignerVerb to the collection.

            value: The System.ComponentModel.Design.DesignerVerb to add to the collection.

            Returns: The index in the collection at which the verb was added.
        """
        ...

    def AddRange(self, value):
        """
        AddRange(self: DesignerVerbCollection, value: Array[DesignerVerb])

            Adds the specified set of designer verbs to the collection.

            value: An array of System.ComponentModel.Design.DesignerVerb objects to add to the collection.

        AddRange(self: DesignerVerbCollection, value: DesignerVerbCollection)

            Adds the specified collection of designer verbs to the collection.

            value: A System.ComponentModel.Design.DesignerVerbCollection to add to the collection.
        """
        ...

    def Contains(self, value):
        """
        Contains(self: DesignerVerbCollection, value: DesignerVerb) -> bool

            Gets a value indicating whether the specified System.ComponentModel.Design.DesignerVerb exists in the collection.

            value: The System.ComponentModel.Design.DesignerVerb to search for in the collection.

            Returns: ue if the specified object exists in the collection; otherwise, lse.
        """
        ...

    def CopyTo(self, array, index):
        """
        CopyTo(self: DesignerVerbCollection, array: Array[DesignerVerb], index: int)

            Copies the collection members to the specified System.ComponentModel.Design.DesignerVerb array beginning at the specified destination index.

            array: The array to copy collection members to.

            index: The destination index to begin copying to.
        """
        ...

    def IndexOf(self, value):
        """
        IndexOf(self: DesignerVerbCollection, value: DesignerVerb) -> int

            Gets the index of the specified System.ComponentModel.Design.DesignerVerb.

            value: The System.ComponentModel.Design.DesignerVerb whose index to get in the collection.

            Returns: The index of the specified object if it is found in the list; otherwise, -1.
        """
        ...

    def Insert(self, index, value):
        """
        Insert(self: DesignerVerbCollection, index: int, value: DesignerVerb)

            Inserts the specified System.ComponentModel.Design.DesignerVerb at the specified index.

            index: The index in the collection at which to insert the verb.

            value: The System.ComponentModel.Design.DesignerVerb to insert in the collection.
        """
        ...

    def Remove(self, value):
        """
        Remove(self: DesignerVerbCollection, value: DesignerVerb)

            Removes the specified System.ComponentModel.Design.DesignerVerb from the collection.

            value: The System.ComponentModel.Design.DesignerVerb to remove from the collection.
        """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class DesigntimeLicenseContext(LicenseContext): # skipped bases: <type 'IServiceProvider'>
    """
    Represents a design-time license context that can support a license provider at design time.

    DesigntimeLicenseContext()
    """
    pass

class DesigntimeLicenseContextSerializer: # skipped bases: <type 'object'>
    """ Provides support for design-time license context serialization. """
    @staticmethod
    def Serialize(o, cryptoKey, context):
        """
        Serialize(o: Stream, cryptoKey: str, context: DesigntimeLicenseContext)

            Serializes the licenses within the specified design-time license context using the specified key and output stream.

            o: The stream to output to.

            cryptoKey: The key to use for encryption.

            context: A System.ComponentModel.Design.DesigntimeLicenseContext indicating the license context.
        """
        ...


class HelpContextType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>
    """
    Defines identifiers that indicate information about the context in which a request for Help information originated.

    enum HelpContextType, values: Ambient (0), Selection (2), ToolWindowSelection (3), Window (1)
    """
    Ambient = None
    Selection = None
    ToolWindowSelection = None
    value__ = None
    Window = None


class HelpKeywordAttribute(Attribute): # skipped bases: <type '_Attribute'>
    """
    Specifies the context keyword for a class or member. This class cannot be inherited.

    HelpKeywordAttribute()

    HelpKeywordAttribute(keyword: str)

    HelpKeywordAttribute(t: Type)
    """
    @property
    def HelpKeyword(self):
        """
        Gets the Help keyword supplied by this attribute.

        Get: HelpKeyword(self: HelpKeywordAttribute) -> str
        """
        ...


    @staticmethod # known case of __new__
    def __new__(cls, *__args):
        """
        __new__(cls: type)

        __new__(cls: type, keyword: str)

        __new__(cls: type, t: Type)
        """
        ...

    Default = None


class HelpKeywordType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>
    """
    Defines identifiers that indicate the type of a Help keyword.

    enum HelpKeywordType, values: F1Keyword (0), FilterKeyword (2), GeneralKeyword (1)
    """
    F1Keyword = None
    FilterKeyword = None
    GeneralKeyword = None
    value__ = None


class IComponentChangeService:
    """ Provides an interface to add and remove the event handlers for events that add, change, remove or rename components, and provides methods to raise a System.ComponentModel.Design.IComponentChangeService.ComponentChanged or System.ComponentModel.Design.IComponentChangeService.ComponentChanging event. """
    def OnComponentChanged(self, component, member, oldValue, newValue):
        """
        OnComponentChanged(self: IComponentChangeService, component: object, member: MemberDescriptor, oldValue: object, newValue: object)

            Announces to the component change service that a particular component has changed.

            component: The component that has changed.

            member: The member that has changed. This is ll if this change is not related to a single member.

            oldValue: The old value of the member. This is valid only if the member is not ll.

            newValue: The new value of the member. This is valid only if the member is not ll.
        """
        ...

    def OnComponentChanging(self, component, member):
        """
        OnComponentChanging(self: IComponentChangeService, component: object, member: MemberDescriptor)

            Announces to the component change service that a particular component is changing.

            component: The component that is about to change.

            member: The member that is changing. This is ll if this change is not related to a single member.
        """
        ...

    ComponentAdded = None
    ComponentAdding = None
    ComponentChanged = None
    ComponentChanging = None
    ComponentRemoved = None
    ComponentRemoving = None
    ComponentRename = None


class IComponentDiscoveryService:
    """ Enables enumeration of components at design time. """
    def GetComponentTypes(self, designerHost, baseType):
        """
        GetComponentTypes(self: IComponentDiscoveryService, designerHost: IDesignerHost, baseType: Type) -> ICollection

            Gets the list of available component types.

            designerHost: The designer host providing design-time services. Can be ll.

            baseType: The base type specifying the components to retrieve. Can be ll.

            Returns: The list of available component types.
        """
        ...


class IComponentInitializer:
    """ Provides a set of recommended default values during component creation. """
    def InitializeExistingComponent(self, defaultValues):
        """
        InitializeExistingComponent(self: IComponentInitializer, defaultValues: IDictionary)

            Restores an instance of a component to its default state.

            defaultValues: A dictionary of default property values, which are name/value pairs, with which to reset the component's state.
        """
        ...

    def InitializeNewComponent(self, defaultValues):
        """
        InitializeNewComponent(self: IComponentInitializer, defaultValues: IDictionary)

            Initializes a new component using a set of recommended values.

            defaultValues: A dictionary of default property values, which are name/value pairs, with which to initialize the component's state.
        """
        ...


class IDesigner(IDisposable):
    """ Provides the basic framework for building a custom designer. """
    @property
    def Component(self):
        """
        Gets the base component that this designer is designing.

        Get: Component(self: IDesigner) -> IComponent
        """
        ...

    @property
    def Verbs(self):
        """
        Gets a collection of the design-time verbs supported by the designer.

        Get: Verbs(self: IDesigner) -> DesignerVerbCollection
        """
        ...


    def DoDefaultAction(self):
        """
        DoDefaultAction(self: IDesigner)

            Performs the default action for this designer.
        """
        ...

    def Initialize(self, component):
        """
        Initialize(self: IDesigner, component: IComponent)

            Initializes the designer with the specified component.

            component: The component to associate with this designer.
        """
        ...


class IDesignerEventService:
    """ Provides event notifications when root designers are added and removed, when a selected component changes, and when the current root designer changes. """
    @property
    def ActiveDesigner(self):
        """
        Gets the root designer for the currently active document.

        Get: ActiveDesigner(self: IDesignerEventService) -> IDesignerHost
        """
        ...

    @property
    def Designers(self):
        """
        Gets a collection of root designers for design documents that are currently active in the development environment.

        Get: Designers(self: IDesignerEventService) -> DesignerCollection
        """
        ...


    ActiveDesignerChanged = None
    DesignerCreated = None
    DesignerDisposed = None
    SelectionChanged = None


class IDesignerFilter:
    """ Provides an interface that enables a designer to access and filter the dictionaries of a System.ComponentModel.TypeDescriptor that stores the property, attribute, and event descriptors that a component designer can expose to the design-time environment. """
    def PostFilterAttributes(self, attributes):
        """
        PostFilterAttributes(self: IDesignerFilter, attributes: IDictionary)

            When overridden in a derived class, allows a designer to change or remove items from the set of attributes that it exposes through a

             System.ComponentModel.TypeDescriptor.

            attributes: The System.Attribute objects for the class of the component. The keys in the dictionary of attributes are the System.Attribute.TypeId values of the

             attributes.
        """
        ...

    def PostFilterEvents(self, events):
        """
        PostFilterEvents(self: IDesignerFilter, events: IDictionary)

            When overridden in a derived class, allows a designer to change or remove items from the set of events that it exposes through a

             System.ComponentModel.TypeDescriptor.

            events: The System.ComponentModel.EventDescriptor objects that represent the events of the class of the component. The keys in the dictionary of events are

             event names.
        """
        ...

    def PostFilterProperties(self, properties):
        """
        PostFilterProperties(self: IDesignerFilter, properties: IDictionary)

            When overridden in a derived class, allows a designer to change or remove items from the set of properties that it exposes through a

             System.ComponentModel.TypeDescriptor.

            properties: The System.ComponentModel.PropertyDescriptor objects that represent the properties of the class of the component. The keys in the dictionary of

             properties are property names.
        """
        ...

    def PreFilterAttributes(self, attributes):
        """
        PreFilterAttributes(self: IDesignerFilter, attributes: IDictionary)

            When overridden in a derived class, allows a designer to add items to the set of attributes that it exposes through a

             System.ComponentModel.TypeDescriptor.

            attributes: The System.Attribute objects for the class of the component. The keys in the dictionary of attributes are the System.Attribute.TypeId values of the

             attributes.
        """
        ...

    def PreFilterEvents(self, events):
        """
        PreFilterEvents(self: IDesignerFilter, events: IDictionary)

            When overridden in a derived class, allows a designer to add items to the set of events that it exposes through a

             System.ComponentModel.TypeDescriptor.

            events: The System.ComponentModel.EventDescriptor objects that represent the events of the class of the component. The keys in the dictionary of events are

             event names.
        """
        ...

    def PreFilterProperties(self, properties):
        """
        PreFilterProperties(self: IDesignerFilter, properties: IDictionary)

            When overridden in a derived class, allows a designer to add items to the set of properties that it exposes through a

             System.ComponentModel.TypeDescriptor.

            properties: The System.ComponentModel.PropertyDescriptor objects that represent the properties of the class of the component. The keys in the dictionary of

             properties are property names.
        """
        ...


class IServiceContainer(IServiceProvider):
    """ Provides a container for services. """
    def AddService(self, serviceType, *__args):
        """
        AddService(self: IServiceContainer, serviceType: Type, serviceInstance: object)

            Adds the specified service to the service container.

            serviceType: The type of service to add.

            serviceInstance: An instance of the service type to add. This object must implement or inherit from the type indicated by the serviceType parameter.

        AddService(self: IServiceContainer, serviceType: Type, serviceInstance: object, promote: bool)

            Adds the specified service to the service container, and optionally promotes the service to any parent service containers.

            serviceType: The type of service to add.

            serviceInstance: An instance of the service type to add. This object must implement or inherit from the type indicated by the serviceType parameter.

            promote: ue to promote this request to any parent service containers; otherwise, lse.

        AddService(self: IServiceContainer, serviceType: Type, callback: ServiceCreatorCallback)

            Adds the specified service to the service container.

            serviceType: The type of service to add.

            callback: A callback object that is used to create the service. This allows a service to be declared as available, but delays the creation of the object until

             the service is requested.

        AddService(self: IServiceContainer, serviceType: Type, callback: ServiceCreatorCallback, promote: bool)

            Adds the specified service to the service container, and optionally promotes the service to parent service containers.

            serviceType: The type of service to add.

            callback: A callback object that is used to create the service. This allows a service to be declared as available, but delays the creation of the object until

             the service is requested.

            promote: ue to promote this request to any parent service containers; otherwise, lse.
        """
        ...

    def RemoveService(self, serviceType, promote=None):
        """
        RemoveService(self: IServiceContainer, serviceType: Type)

            Removes the specified service type from the service container.

            serviceType: The type of service to remove.

        RemoveService(self: IServiceContainer, serviceType: Type, promote: bool)

            Removes the specified service type from the service container, and optionally promotes the service to parent service containers.

            serviceType: The type of service to remove.

            promote: ue to promote this request to any parent service containers; otherwise, lse.
        """
        ...


class IDesignerHost(IServiceContainer): # skipped bases: <type 'IServiceProvider'>
    """ Provides an interface for managing designer transactions and components. """
    @property
    def Container(self):
        """
        Gets the container for this designer host.

        Get: Container(self: IDesignerHost) -> IContainer
        """
        ...

    @property
    def InTransaction(self):
        """
        Gets a value indicating whether the designer host is currently in a transaction.

        Get: InTransaction(self: IDesignerHost) -> bool
        """
        ...

    @property
    def Loading(self):
        """
        Gets a value indicating whether the designer host is currently loading the document.

        Get: Loading(self: IDesignerHost) -> bool
        """
        ...

    @property
    def RootComponent(self):
        """
        Gets the instance of the base class used as the root component for the current design.

        Get: RootComponent(self: IDesignerHost) -> IComponent
        """
        ...

    @property
    def RootComponentClassName(self):
        """
        Gets the fully qualified name of the class being designed.

        Get: RootComponentClassName(self: IDesignerHost) -> str
        """
        ...

    @property
    def TransactionDescription(self):
        """
        Gets the description of the current transaction.

        Get: TransactionDescription(self: IDesignerHost) -> str
        """
        ...


    def Activate(self):
        """
        Activate(self: IDesignerHost)

            Activates the designer that this host is hosting.
        """
        ...

    def CreateComponent(self, componentClass, name=None):
        """
        CreateComponent(self: IDesignerHost, componentClass: Type) -> IComponent

            Creates a component of the specified type and adds it to the design document.

            componentClass: The type of the component to create.

            Returns: The newly created component.

        CreateComponent(self: IDesignerHost, componentClass: Type, name: str) -> IComponent

            Creates a component of the specified type and name, and adds it to the design document.

            componentClass: The type of the component to create.

            name: The name for the component.

            Returns: The newly created component.
        """
        ...

    def CreateTransaction(self, description=None):
        """
        CreateTransaction(self: IDesignerHost) -> DesignerTransaction

            Creates a System.ComponentModel.Design.DesignerTransaction that can encapsulate event sequences to improve performance and enable undo and redo

             support functionality.

            Returns: A new instance of System.ComponentModel.Design.DesignerTransaction. When you complete the steps in your transaction, you should call

             System.ComponentModel.Design.DesignerTransaction.Commit on this object.

        CreateTransaction(self: IDesignerHost, description: str) -> DesignerTransaction

            Creates a System.ComponentModel.Design.DesignerTransaction that can encapsulate event sequences to improve performance and enable undo and redo

             support functionality, using the specified transaction description.

            description: A title or description for the newly created transaction.

            Returns: A new System.ComponentModel.Design.DesignerTransaction. When you have completed the steps in your transaction, you should call

             System.ComponentModel.Design.DesignerTransaction.Commit on this object.
        """
        ...

    def DestroyComponent(self, component):
        """
        DestroyComponent(self: IDesignerHost, component: IComponent)

            Destroys the specified component and removes it from the designer container.

            component: The component to destroy.
        """
        ...

    def GetDesigner(self, component):
        """
        GetDesigner(self: IDesignerHost, component: IComponent) -> IDesigner

            Gets the designer instance that contains the specified component.

            component: The System.ComponentModel.IComponent to retrieve the designer for.

            Returns: An System.ComponentModel.Design.IDesigner, or ll if there is no designer for the specified component.
        """
        ...

    def GetType(self, typeName):
        """
        GetType(self: IDesignerHost, typeName: str) -> Type

            Gets an instance of the specified, fully qualified type name.

            typeName: The name of the type to load.

            Returns: The type object for the specified type name, or ll if the type cannot be found.
        """
        ...

    Activated = None
    Deactivated = None
    LoadComplete = None
    TransactionClosed = None
    TransactionClosing = None
    TransactionOpened = None
    TransactionOpening = None


class IDesignerHostTransactionState:
    """ Specifies methods for the designer host to report on the state of transactions. """
    @property
    def IsClosingTransaction(self):
        """
        Gets a value indicating whether the designer host is closing a transaction.

        Get: IsClosingTransaction(self: IDesignerHostTransactionState) -> bool
        """
        ...



class IDictionaryService:
    """ Provides a basic, component site-specific, key-value pair dictionary through a service that a designer can use to store user-defined data. """
    def GetKey(self, value):
        """
        GetKey(self: IDictionaryService, value: object) -> object

            Gets the key corresponding to the specified value.

            value: The value to look up in the dictionary.

            Returns: The associated key, or ll if no key exists.
        """
        ...

    def GetValue(self, key):
        """
        GetValue(self: IDictionaryService, key: object) -> object

            Gets the value corresponding to the specified key.

            key: The key to look up the value for.

            Returns: The associated value, or ll if no value exists.
        """
        ...

    def SetValue(self, key, value):
        """
        SetValue(self: IDictionaryService, key: object, value: object)

            Sets the specified key-value pair.

            key: An object to use as the key to associate the value with.

            value: The value to store.
        """
        ...


class IEventBindingService:
    """ Provides a service for registering event handlers for component events. """
    def CreateUniqueMethodName(self, component, e):
        """
        CreateUniqueMethodName(self: IEventBindingService, component: IComponent, e: EventDescriptor) -> str

            Creates a unique name for an event-handler method for the specified component and event.

            component: The component instance the event is connected to.

            e: The event to create a name for.

            Returns: The recommended name for the event-handler method for this event.
        """
        ...

    def GetCompatibleMethods(self, e):
        """
        GetCompatibleMethods(self: IEventBindingService, e: EventDescriptor) -> ICollection

            Gets a collection of event-handler methods that have a method signature compatible with the specified event.

            e: The event to get the compatible event-handler methods for.

            Returns: A collection of strings.
        """
        ...

    def GetEvent(self, property):
        """
        GetEvent(self: IEventBindingService, property: PropertyDescriptor) -> EventDescriptor

            Gets an System.ComponentModel.EventDescriptor for the event that the specified property descriptor represents, if it represents an event.

            property: The property that represents an event.

            Returns: An System.ComponentModel.EventDescriptor for the event that the property represents, or ll if the property does not represent an event.
        """
        ...

    def GetEventProperties(self, events):
        """
        GetEventProperties(self: IEventBindingService, events: EventDescriptorCollection) -> PropertyDescriptorCollection

            Converts a set of event descriptors to a set of property descriptors.

            events: The events to convert to properties.

            Returns: An array of System.ComponentModel.PropertyDescriptor objects that describe the event set.
        """
        ...

    def GetEventProperty(self, e):
        """
        GetEventProperty(self: IEventBindingService, e: EventDescriptor) -> PropertyDescriptor

            Converts a single event descriptor to a property descriptor.

            e: The event to convert.

            Returns: A System.ComponentModel.PropertyDescriptor that describes the event.
        """
        ...

    def ShowCode(self, *__args):
        """
        ShowCode(self: IEventBindingService) -> bool

            Displays the user code for the designer.

            Returns: ue if the code is displayed; otherwise, lse.

        ShowCode(self: IEventBindingService, lineNumber: int) -> bool

            Displays the user code for the designer at the specified line.

            lineNumber: The line number to place the caret on.

            Returns: ue if the code is displayed; otherwise, lse.

        ShowCode(self: IEventBindingService, component: IComponent, e: EventDescriptor) -> bool

            Displays the user code for the specified event.

            component: The component that the event is connected to.

            e: The event to display.

            Returns: ue if the code is displayed; otherwise, lse.
        """
        ...


class IExtenderListService:
    """ Provides an interface that can list extender providers. """
    def GetExtenderProviders(self):
        """
        GetExtenderProviders(self: IExtenderListService) -> Array[IExtenderProvider]

            Gets the set of extender providers for the component.

            Returns: An array of type System.ComponentModel.IExtenderProvider that lists the active extender providers. If there are no providers, an empty array is

             returned.
        """
        ...


class IExtenderProviderService:
    """ Provides an interface for adding and removing extender providers at design time. """
    def AddExtenderProvider(self, provider):
        """
        AddExtenderProvider(self: IExtenderProviderService, provider: IExtenderProvider)

            Adds the specified extender provider.

            provider: The extender provider to add.
        """
        ...

    def RemoveExtenderProvider(self, provider):
        """
        RemoveExtenderProvider(self: IExtenderProviderService, provider: IExtenderProvider)

            Removes the specified extender provider.

            provider: The extender provider to remove.
        """
        ...


class IHelpService:
    """ Provides methods for showing Help topics and adding and removing Help keywords at design time. """
    def AddContextAttribute(self, name, value, keywordType):
        """
        AddContextAttribute(self: IHelpService, name: str, value: str, keywordType: HelpKeywordType)

            Adds a context attribute to the document.

            name: The name of the attribute to add.

            value: The value of the attribute.

            keywordType: The type of the keyword, from the enumeration System.ComponentModel.Design.HelpKeywordType.
        """
        ...

    def ClearContextAttributes(self):
        """
        ClearContextAttributes(self: IHelpService)

            Removes all existing context attributes from the document.
        """
        ...

    def CreateLocalContext(self, contextType):
        """
        CreateLocalContext(self: IHelpService, contextType: HelpContextType) -> IHelpService

            Creates a local System.ComponentModel.Design.IHelpService to manage subcontexts.

            contextType: The priority type of the subcontext to add.

            Returns: The newly created System.ComponentModel.Design.IHelpService.
        """
        ...

    def RemoveContextAttribute(self, name, value):
        """
        RemoveContextAttribute(self: IHelpService, name: str, value: str)

            Removes a previously added context attribute.

            name: The name of the attribute to remove.

            value: The value of the attribute to remove.
        """
        ...

    def RemoveLocalContext(self, localContext):
        """
        RemoveLocalContext(self: IHelpService, localContext: IHelpService)

            Removes a context created with System.ComponentModel.Design.IHelpService.CreateLocalContext(System.ComponentModel.Design.HelpContextType).

            localContext: The local context System.ComponentModel.Design.IHelpService to remove.
        """
        ...

    def ShowHelpFromKeyword(self, helpKeyword):
        """
        ShowHelpFromKeyword(self: IHelpService, helpKeyword: str)

            Shows the Help topic that corresponds to the specified keyword.

            helpKeyword: The keyword of the Help topic to display.
        """
        ...

    def ShowHelpFromUrl(self, helpUrl):
        """
        ShowHelpFromUrl(self: IHelpService, helpUrl: str)

            Shows the Help topic that corresponds to the specified URL.

            helpUrl: The URL of the Help topic to display.
        """
        ...


class IInheritanceService:
    """ Provides methods for identifying the components of a component. """
    def AddInheritedComponents(self, component, container):
        """
        AddInheritedComponents(self: IInheritanceService, component: IComponent, container: IContainer)

            Searches the specified component for fields that implement the System.ComponentModel.IComponent interface and adds each to the specified container,

             storing the inheritance level of each which can be retrieved using the

             System.ComponentModel.Design.IInheritanceService.GetInheritanceAttribute(System.ComponentModel.IComponent) method.

            component: The System.ComponentModel.IComponent to search. Searching begins with this component.

            container: The System.ComponentModel.IContainer to add components to.
        """
        ...

    def GetInheritanceAttribute(self, component):
        """
        GetInheritanceAttribute(self: IInheritanceService, component: IComponent) -> InheritanceAttribute

            Gets the inheritance attribute for the specified component.

            component: The System.ComponentModel.IComponent for which to retrieve the inheritance attribute.

            Returns: An instance of System.ComponentModel.InheritanceAttribute that describes the level of inheritance of the specified component.
        """
        ...


class IMenuCommandService:
    """ Provides methods to manage the global designer verbs and menu commands available in design mode, and to show some types of shortcut menus. """
    @property
    def Verbs(self):
        """
        Gets a collection of the designer verbs that are currently available.

        Get: Verbs(self: IMenuCommandService) -> DesignerVerbCollection
        """
        ...


    def AddCommand(self, command):
        """
        AddCommand(self: IMenuCommandService, command: MenuCommand)

            Adds the specified standard menu command to the menu.

            command: The System.ComponentModel.Design.MenuCommand to add.
        """
        ...

    def AddVerb(self, verb):
        """
        AddVerb(self: IMenuCommandService, verb: DesignerVerb)

            Adds the specified designer verb to the set of global designer verbs.

            verb: The System.ComponentModel.Design.DesignerVerb to add.
        """
        ...

    def FindCommand(self, commandID):
        """
        FindCommand(self: IMenuCommandService, commandID: CommandID) -> MenuCommand

            Searches for the specified command ID and returns the menu command associated with it.

            commandID: The System.ComponentModel.Design.CommandID to search for.

            Returns: The System.ComponentModel.Design.MenuCommand associated with the command ID, or ll if no command is found.
        """
        ...

    def GlobalInvoke(self, commandID):
        """
        GlobalInvoke(self: IMenuCommandService, commandID: CommandID) -> bool

            Invokes a menu or designer verb command matching the specified command ID.

            commandID: The System.ComponentModel.Design.CommandID of the command to search for and execute.

            Returns: ue if the command was found and invoked successfully; otherwise, lse.
        """
        ...

    def RemoveCommand(self, command):
        """
        RemoveCommand(self: IMenuCommandService, command: MenuCommand)

            Removes the specified standard menu command from the menu.

            command: The System.ComponentModel.Design.MenuCommand to remove.
        """
        ...

    def RemoveVerb(self, verb):
        """
        RemoveVerb(self: IMenuCommandService, verb: DesignerVerb)

            Removes the specified designer verb from the collection of global designer verbs.

            verb: The System.ComponentModel.Design.DesignerVerb to remove.
        """
        ...

    def ShowContextMenu(self, menuID, x, y):
        """
        ShowContextMenu(self: IMenuCommandService, menuID: CommandID, x: int, y: int)

            Shows the specified shortcut menu at the specified location.

            menuID: The System.ComponentModel.Design.CommandID for the shortcut menu to show.

            x: The x-coordinate at which to display the menu, in screen coordinates.

            y: The y-coordinate at which to display the menu, in screen coordinates.
        """
        ...


class IReferenceService:
    """ Provides an interface for obtaining references to objects within a project by name or type, obtaining the name of a specified object, and for locating the parent of a specified object within a designer project. """
    def GetComponent(self, reference):
        """
        GetComponent(self: IReferenceService, reference: object) -> IComponent

            Gets the component that contains the specified component.

            reference: The object to retrieve the parent component for.

            Returns: The base System.ComponentModel.IComponent that contains the specified object, or ll if no parent component exists.
        """
        ...

    def GetName(self, reference):
        """
        GetName(self: IReferenceService, reference: object) -> str

            Gets the name of the specified component.

            reference: The object to return the name of.

            Returns: The name of the object referenced, or ll if the object reference is not valid.
        """
        ...

    def GetReference(self, name):
        """
        GetReference(self: IReferenceService, name: str) -> object

            Gets a reference to the component whose name matches the specified name.

            name: The name of the component to return a reference to.

            Returns: An object the specified name refers to, or ll if no reference is found.
        """
        ...

    def GetReferences(self, baseType=None):
        """
        GetReferences(self: IReferenceService) -> Array[object]

            Gets all available references to project components.

            Returns: An array of all objects with references available to the System.ComponentModel.Design.IReferenceService.

        GetReferences(self: IReferenceService, baseType: Type) -> Array[object]

            Gets all available references to components of the specified type.

            baseType: The type of object to return references to instances of.

            Returns: An array of all available objects of the specified type.
        """
        ...


class IResourceService:
    """ Provides an interface for designers to access resource readers and writers for specific System.Globalization.CultureInfo resource types. """
    def GetResourceReader(self, info):
        """
        GetResourceReader(self: IResourceService, info: CultureInfo) -> IResourceReader

            Locates the resource reader for the specified culture and returns it.

            info: The System.Globalization.CultureInfo of the resource for which to retrieve a resource reader.

            Returns: An System.Resources.IResourceReader interface that contains the resources for the culture, or ll if no resources for the culture exist.
        """
        ...

    def GetResourceWriter(self, info):
        """
        GetResourceWriter(self: IResourceService, info: CultureInfo) -> IResourceWriter

            Locates the resource writer for the specified culture and returns it.

            info: The System.Globalization.CultureInfo of the resource for which to create a resource writer.

            Returns: An System.Resources.IResourceWriter interface for the specified culture.
        """
        ...


class IRootDesigner(IDesigner): # skipped bases: <type 'IDisposable'>
    """ Provides support for root-level designer view technologies. """
    @property
    def SupportedTechnologies(self):
        """
        Gets the set of technologies that this designer can support for its display.

        Get: SupportedTechnologies(self: IRootDesigner) -> Array[ViewTechnology]
        """
        ...


    def GetView(self, technology):
        """
        GetView(self: IRootDesigner, technology: ViewTechnology) -> object

            Gets a view object for the specified view technology.

            technology: A System.ComponentModel.Design.ViewTechnology that indicates a particular view technology.

            Returns: An object that represents the view for this designer.
        """
        ...


class ISelectionService:
    """ Provides an interface for a designer to select components. """
    @property
    def PrimarySelection(self):
        """
        Gets the object that is currently the primary selected object.

        Get: PrimarySelection(self: ISelectionService) -> object
        """
        ...

    @property
    def SelectionCount(self):
        """
        Gets the count of selected objects.

        Get: SelectionCount(self: ISelectionService) -> int
        """
        ...


    def GetComponentSelected(self, component):
        """
        GetComponentSelected(self: ISelectionService, component: object) -> bool

            Gets a value indicating whether the specified component is currently selected.

            component: The component to test.

            Returns: ue if the component is part of the user's current selection; otherwise, lse.
        """
        ...

    def GetSelectedComponents(self):
        """
        GetSelectedComponents(self: ISelectionService) -> ICollection

            Gets a collection of components that are currently selected.

            Returns: A collection that represents the current set of components that are selected.
        """
        ...

    def SetSelectedComponents(self, components, selectionType=None):
        """
        SetSelectedComponents(self: ISelectionService, components: ICollection)

            Selects the specified collection of components.

            components: The collection of components to select.

        SetSelectedComponents(self: ISelectionService, components: ICollection, selectionType: SelectionTypes)

            Selects the components from within the specified collection of components that match the specified selection type.

            components: The collection of components to select.

            selectionType: A value from the System.ComponentModel.Design.SelectionTypes enumeration. The default is System.ComponentModel.Design.SelectionTypes.Normal.
        """
        ...

    SelectionChanged = None
    SelectionChanging = None


class ITreeDesigner(IDesigner): # skipped bases: <type 'IDisposable'>
    """ Provides support for building a set of related custom designers. """
    @property
    def Children(self):
        """
        Gets a collection of child designers.

        Get: Children(self: ITreeDesigner) -> ICollection
        """
        ...

    @property
    def Parent(self):
        """
        Gets the parent designer.

        Get: Parent(self: ITreeDesigner) -> IDesigner
        """
        ...



class ITypeDescriptorFilterService:
    """ Provides an interface to modify the set of member descriptors for a component in design mode. """
    def FilterAttributes(self, component, attributes):
        """
        FilterAttributes(self: ITypeDescriptorFilterService, component: IComponent, attributes: IDictionary) -> bool

            Filters the attributes that a component exposes through a System.ComponentModel.TypeDescriptor.

            component: The component to filter the attributes of.

            attributes: A dictionary of attributes that can be modified.

            Returns: ue if the set of filtered attributes is to be cached; lse if the filter service must query again.
        """
        ...

    def FilterEvents(self, component, events):
        """
        FilterEvents(self: ITypeDescriptorFilterService, component: IComponent, events: IDictionary) -> bool

            Filters the events that a component exposes through a System.ComponentModel.TypeDescriptor.

            component: The component to filter events for.

            events: A dictionary of events that can be modified.

            Returns: ue if the set of filtered events is to be cached; lse if the filter service must query again.
        """
        ...

    def FilterProperties(self, component, properties):
        """
        FilterProperties(self: ITypeDescriptorFilterService, component: IComponent, properties: IDictionary) -> bool

            Filters the properties that a component exposes through a System.ComponentModel.TypeDescriptor.

            component: The component to filter properties for.

            properties: A dictionary of properties that can be modified.

            Returns: ue if the set of filtered properties is to be cached; lse if the filter service must query again.
        """
        ...


class ITypeDiscoveryService:
    """ Discovers available types at design time. """
    def GetTypes(self, baseType, excludeGlobalTypes):
        """
        GetTypes(self: ITypeDiscoveryService, baseType: Type, excludeGlobalTypes: bool) -> ICollection

            Retrieves the list of available types.

            baseType: The base type to match. Can be ll.

            excludeGlobalTypes: Indicates whether types from all referenced assemblies should be checked.

            Returns: A collection of types that match the criteria specified by baseType and excludeGlobalTypes.
        """
        ...


class ITypeResolutionService:
    """ Provides an interface to retrieve an assembly or type by name. """
    def GetAssembly(self, name, throwOnError=None):
        """
        GetAssembly(self: ITypeResolutionService, name: AssemblyName) -> Assembly

            Gets the requested assembly.

            name: The name of the assembly to retrieve.

            Returns: An instance of the requested assembly, or ll if no assembly can be located.

        GetAssembly(self: ITypeResolutionService, name: AssemblyName, throwOnError: bool) -> Assembly

            Gets the requested assembly.

            name: The name of the assembly to retrieve.

            throwOnError: ue if this method should throw an exception if the assembly cannot be located; otherwise, lse, and this method returns ll if the assembly cannot be

             located.

            Returns: An instance of the requested assembly, or ll if no assembly can be located.
        """
        ...

    def GetPathOfAssembly(self, name):
        """
        GetPathOfAssembly(self: ITypeResolutionService, name: AssemblyName) -> str

            Gets the path to the file from which the assembly was loaded.

            name: The name of the assembly.

            Returns: The path to the file from which the assembly was loaded.
        """
        ...

    def GetType(self, name, throwOnError=None, ignoreCase=None):
        """
        GetType(self: ITypeResolutionService, name: str) -> Type

            Loads a type with the specified name.

            name: The name of the type. If the type name is not a fully qualified name that indicates an assembly, this service will search its internal set of

             referenced assemblies.

            Returns: An instance of System.Type that corresponds to the specified name, or ll if no type can be found.

        GetType(self: ITypeResolutionService, name: str, throwOnError: bool) -> Type

            Loads a type with the specified name.

            name: The name of the type. If the type name is not a fully qualified name that indicates an assembly, this service will search its internal set of

             referenced assemblies.

            throwOnError: ue if this method should throw an exception if the assembly cannot be located; otherwise, lse, and this method returns ll if the assembly cannot be

             located.

            Returns: An instance of System.Type that corresponds to the specified name, or ll if no type can be found.

        GetType(self: ITypeResolutionService, name: str, throwOnError: bool, ignoreCase: bool) -> Type

            Loads a type with the specified name.

            name: The name of the type. If the type name is not a fully qualified name that indicates an assembly, this service will search its internal set of

             referenced assemblies.

            throwOnError: ue if this method should throw an exception if the assembly cannot be located; otherwise, lse, and this method returns ll if the assembly cannot be

             located.

            ignoreCase: ue to ignore case when searching for types; otherwise, lse.

            Returns: An instance of System.Type that corresponds to the specified name, or ll if no type can be found.
        """
        ...

    def ReferenceAssembly(self, name):
        """
        ReferenceAssembly(self: ITypeResolutionService, name: AssemblyName)

            Adds a reference to the specified assembly.

            name: An System.Reflection.AssemblyName that indicates the assembly to reference.
        """
        ...


class SelectionTypes(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>
    """
    Defines identifiers that indicate the type of a selection.

    enum (flags) SelectionTypes, values: Add (64), Auto (1), Click (16), MouseDown (4), MouseUp (8), Normal (1), Primary (16), Remove (128), Replace (2), Toggle (32), Valid (31)
    """
    Add = None
    Auto = None
    Click = None
    MouseDown = None
    MouseUp = None
    Normal = None
    Primary = None
    Remove = None
    Replace = None
    Toggle = None
    Valid = None
    value__ = None


class ServiceContainer(object, IServiceContainer, IDisposable): # skipped bases: <type 'IServiceProvider'>
    """
    Provides a simple implementation of the System.ComponentModel.Design.IServiceContainer interface. This class cannot be inherited.

    ServiceContainer()

    ServiceContainer(parentProvider: IServiceProvider)
    """
    @property
    def DefaultServices(self):
        """ Gets the default services implemented directly by System.ComponentModel.Design.ServiceContainer. """
        ...


    def GetService(self, serviceType):
        """
        GetService(self: ServiceContainer, serviceType: Type) -> object

            Gets the requested service.

            serviceType: The type of service to retrieve.

            Returns: An instance of the service if it could be found, or ll if it could not be found.
        """
        ...


class ServiceCreatorCallback(MulticastDelegate): # skipped bases: <type 'ICloneable'>, <type 'ISerializable'>
    """
    Provides a callback mechanism that can create an instance of a service on demand.

    ServiceCreatorCallback(object: object, method: IntPtr)
    """
    def BeginInvoke(self, container, serviceType, callback, object):
        """ BeginInvoke(self: ServiceCreatorCallback, container: IServiceContainer, serviceType: Type, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result):
        """ EndInvoke(self: ServiceCreatorCallback, result: IAsyncResult) -> object """
        ...

    def Invoke(self, container, serviceType):
        """ Invoke(self: ServiceCreatorCallback, container: IServiceContainer, serviceType: Type) -> object """
        ...


class StandardCommands: # skipped bases: <type 'object'>
    """
    Defines identifiers for the standard set of commands that are available to most applications.

    StandardCommands()
    """
    AlignBottom = None
    AlignHorizontalCenters = None
    AlignLeft = None
    AlignRight = None
    AlignToGrid = None
    AlignTop = None
    AlignVerticalCenters = None
    ArrangeBottom = None
    ArrangeIcons = None
    ArrangeRight = None
    BringForward = None
    BringToFront = None
    CenterHorizontally = None
    CenterVertically = None
    Copy = None
    Cut = None
    Delete = None
    DocumentOutline = None
    F1Help = None
    Group = None
    HorizSpaceConcatenate = None
    HorizSpaceDecrease = None
    HorizSpaceIncrease = None
    HorizSpaceMakeEqual = None
    LineupIcons = None
    LockControls = None
    MultiLevelRedo = None
    MultiLevelUndo = None
    Paste = None
    Properties = None
    PropertiesWindow = None
    Redo = None
    Replace = None
    SelectAll = None
    SendBackward = None
    SendToBack = None
    ShowGrid = None
    ShowLargeIcons = None
    SizeToControl = None
    SizeToControlHeight = None
    SizeToControlWidth = None
    SizeToFit = None
    SizeToGrid = None
    SnapToGrid = None
    TabOrder = None
    Undo = None
    Ungroup = None
    VerbFirst = None
    VerbLast = None
    VertSpaceConcatenate = None
    VertSpaceDecrease = None
    VertSpaceIncrease = None
    VertSpaceMakeEqual = None
    ViewCode = None
    ViewGrid = None


class StandardToolWindows: # skipped bases: <type 'object'>
    """
    Defines GUID identifiers that correspond to the standard set of tool windows that are available in the design environment.

    StandardToolWindows()
    """
    ObjectBrowser = None
    OutputWindow = None
    ProjectExplorer = None
    PropertyBrowser = None
    RelatedLinks = None
    ServerExplorer = None
    TaskList = None
    Toolbox = None


class TypeDescriptionProviderService: # skipped bases: <type 'object'>
    """ Provides a type description provider for a specified type. """
    def GetProvider(self, *__args):
        """
        GetProvider(self: TypeDescriptionProviderService, instance: object) -> TypeDescriptionProvider

            Gets a type description provider for the specified object.

            instance: The object to get a type description provider for.

            Returns: A System.ComponentModel.TypeDescriptionProvider that corresponds with instance.

        GetProvider(self: TypeDescriptionProviderService, type: Type) -> TypeDescriptionProvider

            Gets a type description provider for the specified type.

            type: The type to get a type description provider for.

            Returns: A System.ComponentModel.TypeDescriptionProvider that corresponds with type.
        """
        ...


class ViewTechnology(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>
    """
    Defines identifiers for a set of technologies that designer hosts support.

    enum ViewTechnology, values: Default (2), Passthrough (0), WindowsForms (1)
    """
    Default = None
    Passthrough = None
    value__ = None
    WindowsForms = None


# variables with complex values
