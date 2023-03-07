from __future__ import annotations
from typing import Any, Dict, List, Optional, TypeVar
from Siemens.Engineering.HW import (
    DeviceComposition,
    View,
    SubnetComposition,
    DeviceUserGroupComposition,
    DeviceSystemGroup,
)
from Siemens.Engineering.HW.Utilities import HardwareUtilityComposition
from Siemens.Engineering.Hmi.Globalization import MultiLingualGraphicComposition
from Siemens.Engineering.Library import ProjectLibrary, GlobalLibraryComposition
from Siemens.Engineering.Library.MasterCopies import IMasterCopyTarget
from Siemens.Engineering.Settings import TiaPortalSettingsFolderComposition
from System import (
    EventArgs,
    IDisposable,
    Enum,
    IServiceProvider,
    Object,
    IEquatable,
    DateTime,
    Int64,
    TimeSpan,
    AsyncCallback,
    IAsyncResult,
    MulticastDelegate,
)
from System.Collections import IEnumerable
from System.Globalization import CultureInfo
from System.IO import DirectoryInfo, FileInfo
from System.Security import SecureString

T = TypeVar("T")
U = TypeVar("U")

class AttachingEventArgs(EventArgs):
    """Attaching event arguments"""

    @property
    def AccessLevel(self) -> TiaPortalAccessLevel:
        """Gets access level argument of the attaching event."""
        ...
    @property
    def ProcessId(self) -> int:
        """Gets attaching process identifier."""
        ...
    @property
    def ProcessPath(self) -> str:
        """Gets attaching event process path."""
        ...
    @property
    def TrustAuthority(self) -> TiaPortalTrustAuthority:
        """Gets TIA-Portal trust authority of the attaching event."""
        ...
    @property
    def Version(self) -> str:
        """Gets version argument of the attaching event."""
        ...
    def GrantAccess(self) -> None:
        """Grants permission to the attaching Openness application to attach."""
        ...

class ConfirmationChoices(Enum):
    """The list of possible confirmation choices
    Options for the confirmation dialog box:
        None(0): No choice
        Ok(1): Ok
        Yes(2): Yes
        YesToAll(4): Yes to all
        No(64): No
        NoToAll(128): No to all
        Abort(8): Abort
        Retry(16): Retry
        Ignore(32): Ignore
        Cancel(256): Cancel
    """

    Abort = ...
    Cancel = ...
    Ignore = ...
    No = ...
    NoToAll = ...
    Ok = ...
    Retry = ...
    value__ = ...
    Yes = ...
    YesToAll = ...

class ConfirmationEventArgs(EventArgs):
    """Confirmation event arguments"""

    @property
    def Caption(self) -> str:
        """Gets the caption of the confirmation."""
        ...
    @property
    def Choices(self) -> ConfirmationChoices:
        """Gets the choices of the confirmation."""
        ...
    @property
    def DetailText(self) -> str:
        """Gets the detail text of the confirmation."""
        ...
    @property
    def Icon(self) -> ConfirmationIcon:
        """Gets the icon."""
        ...
    @property
    def IsHandled(self) -> bool:
        """Gets or sets if the confirmation is handled."""
        ...
    @property
    def Result(self) -> ConfirmationChoices:
        """Gets the result of the confirmation."""
        ...
    @property
    def Text(self) -> str:
        """Gets the text of the confirmation."""
        ...

class ConfirmationIcon(Enum):
    """The list of possible confirmation icons
    Options for the confirmation dialog box:
        General(0): General
        Critical(1): Critical
        Error(2): Error
    """

    Critical = ...
    Error = ...
    General = ...
    value__ = ...

class ConfirmationResult(Enum):
    """The list of possible confirmation results
    Options for the confirmation dialog box:
        None(0): No choice
        Ok(1): Ok
        Yes(2): Yes
        YesToAll(4): Yes to all
        No(64): No
        NoToAll(128): No to all
        Abort(8): Abort
        Retry(16): Retry
        Ignore(32): Ignore
        Cancel(256): Cancel
    """

    Abort = ...
    Cancel = ...
    Ignore = ...
    No = ...
    NoToAll = ...
    Ok = ...
    Retry = ...
    value__ = ...
    Yes = ...
    YesToAll = ...

class EngineeringAttributeAccessMode(Enum):
    """Flags enum that describes different access levels
    Options for the attribute access mode:
        None(0): No access
        Read(1): Read access
        Write(2): Write access
        ReadWrite(3): Read and write access
    """

    Read = ...
    ReadWrite = ...
    value__ = ...
    Write = ...

class EngineeringAttributeInfo:
    """Represents composition information."""

    @property
    def AccessMode(self) -> EngineeringAttributeAccessMode:
        """Gets the level of access supported by the attribute."""
        ...
    @property
    def CreateRelevance(self) -> EngineeringCreateRelevance:
        """Gets the relevance of the attribute when creating a new object."""
        ...
    @property
    def Name(self) -> str:
        """Gets the name of the attribute."""
        ...
    def ToString(self) -> str:
        """Generates a string representation of the object."""
        ...

class EngineeringCompositionInfo:
    """Represents composition information."""

    @property
    def Name(self) -> str:
        """Composition name."""
        ...
    def ToString(self) -> str:
        """Generates a string representation of the object."""
        ...

class EngineeringCreateRelevance(Enum):
    """Flags enum that describes different relevance levels
    Options for the attribute relevance:
        None(0): No relevance
        Relevant(1): Relevant
        Mandatory(2): Mandatory
    """

    Mandatory = ...
    Relevant = ...
    value__ = ...

class EngineeringCreationInfo:
    """Represents the necessary information required to create an object."""

    @property
    def ParameterInfos(self) -> List[EngineeringCreationParameterInfo]:
        """The parameters needed to create the object."""
        ...
    @property
    def Type(self) -> Any:
        """The type of the object that will be created."""
        ...
    def ToString(self) -> str:
        """Generates a string representation of the object."""
        ...

class EngineeringCreationParameterInfo:
    """The parameter info"""

    @property
    def IsMandatory(self) -> bool:
        """Gets if the parameter is mandatory."""
        ...
    @property
    def Name(self) -> str:
        """Gets the name of the parameter."""
        ...
    def ToString(self) -> str:
        """Generates a string representation of the object."""
        ...

class EngineeringException(Exception):
    """The base class for all engineering exceptions."""

    @property
    def DetailMessageData(self) -> List[ExceptionMessageData]:
        """Gets the detail message data."""
        ...
    @property
    def MessageData(self) -> ExceptionMessageData:
        """Gets the message data."""
        ...
    SerializeObjectState = ...

class EngineeringTargetInvocationException(EngineeringException): ...
class EngineeringDelegateInvocationException(EngineeringTargetInvocationException): ...
class EngineeringNotSupportedException(EngineeringException): ...
class EngineeringObjectDisposedException(EngineeringException): ...
class EngineeringOutOfMemoryException(EngineeringException): ...
class EngineeringRuntimeException(EngineeringException): ...
class EngineeringSecurityException(EngineeringException): ...
class EngineeringUserAbortException(EngineeringTargetInvocationException): ...

class EngineeringInvocationInfo:
    """Represents an action info."""

    @property
    def Name(self) -> str:
        """Gets the name of the action."""
        ...
    @property
    def ParameterInfos(self) -> List[EngineeringInvocationParameterInfo]:
        """Gets the parameter info list."""
        ...
    def ToString(self) -> str:
        """Generates a string representation of the object."""
        ...

class EngineeringInvocationParameterInfo:
    """The parameter info"""

    @property
    def Name(self) -> str:
        """Gets the name of the parameter."""
        ...
    @property
    def Type(self) -> Any:
        """Gets the type of the parameter."""
        ...
    def ToString(self) -> str:
        """Generates a string representation of the object."""
        ...

class EngineeringServiceInfo:
    """Represents an action info."""

    @property
    def Type(self) -> Any:
        """Gets the name of the action."""
        ...
    def ToString(self) -> str:
        """Generates a string representation of the object."""
        ...

class ExceptionMessageData:
    """Exception Message Data structure."""

    @property
    def DetailText(self) -> str:
        """Gets the detail text."""
        ...
    @property
    def Text(self) -> str:
        """Gets the text."""
        ...
    def ToString(self) -> str:
        """Generates a string representation of the object."""
        ...

class IEngineeringInstance:
    """IEngineeringInstance"""

    @property
    def Parent(self) -> IEngineeringObject:
        """Gets the parent."""
        ...

class IEngineeringCompositionOrObject(IEngineeringInstance):
    """IEngineeringCompositionOrObject"""

    ...

class IEngineeringObject(IEngineeringCompositionOrObject):
    """IEngineeringObject"""

    def Create(self, compositionName: str, type: T, parameters: Dict[str, Any]) -> T:
        """Creates a new object in the composition.
        Parameters:
            compositionName (str): Name of the composition.
            type (T): Type of the object to create.
            parameters (Dict[str, Any]): The parameters.
        Returns:
            T:  The new object.
        """
        ...
    def GetAttribute(self, name: str) -> Any:
        """Gets an attribute with the given name.
        Parameters:
            name (str): The name of the attribute.
        Returns:
            Any: The attribute.
        """
        ...
    def GetAttributeInfos(self) -> List[EngineeringAttributeInfo]:
        """Gets a collection of EngineeringAttributeInfo objects describing the different attributes on this object.
        Returns:
            List[EngineeringAttributeInfo]: A collection of EngineeringAttributeInfo objects describing the different attributes on this object.
        """
        ...
    def GetAttributes(self, names: List[str]) -> List[Object]:
        """Gets a list of attributes with the given names.
        Parameters:
            names (List[str]): The names of the attributes.
        Returns:
            List[Object]: List of attributes.
        """
        ...
    def GetComposition(self, name: str) -> IEngineeringCompositionOrObject:
        """Gets an IEngineeringCompositionOrObject with the given name.
        Parameters:
            name (str): The name of the composition.
        Returns:
            IEngineeringCompositionOrObject: The composition which has the given name.
        """
        ...
    def GetCompositionInfos(self) -> List[EngineeringCompositionInfo]:
        """Gets the list of composition infos available for the object.
        Returns:
            List[EngineeringCompositionInfo]: The list of composition infos available for the object.
        """
        ...
    def GetCreationInfos(self, compositionName: str) -> List[EngineeringCreationInfo]:
        """Gets the list of creation infos available for the object.
        Parameters:
            compositionName (str): The name of the composition.
        Returns:
            List[EngineeringCreationInfo]: The list of creation infos available for the object.
        """
        ...
    def GetInvocationInfos(self) -> List[EngineeringInvocationInfo]:
        """Gets the list of invocation infos available for the object.
        Returns:
            List[EngineeringInvocationInfo]: The list of invocation infos available for the object.
        """
        ...
    def Invoke(self, name: str, parameters: Dict[Any, Object]) -> Object:
        """Invokes an action on the object.
        Parameters:
            name (str): The name of the action to invoke.
            parameters (Dict[Any, Object]): The parameters to pass to the action. The keys are the parameter Type and the values are objects.
        Returns:
            Object: The result of the action.
        """
        ...
    def SetAttribute(self, name: str, value: Object) -> None:
        """Sets an attribute with the given name to the given value value.
        Parameters:
            name (str): The name of the attribute to set with the given value.
            value : The value to set for the attribute with the given name.
        """
        ...
    def SetAttributes(self, attributes: Dict[str, Object]) -> None:
        """Sets a list of attributes with the given names to the given values.
        Parameters:
            attributes (Dict[str, Object]): The attributes to set. The keys are the attribute names and the values are the attribute values.
        """
        ...

class ExclusiveAccess(
    IEngineeringObject,
    IDisposable,
    IInternalObjectAccess,  # type: ignore
    IEquatable,
):
    """The class representing an exclusive access session to the TIA Portal"""

    @property
    def IsCancellationRequested(self) -> bool:
        """Gets a value indicating whether the cancellation of the exclusive access session has been requested."""
        ...
    @property
    def Parent(self) -> IEngineeringObject:
        """Gets the parent object."""
        ...
    @property
    def Text(self) -> str:
        """The information to display while an exclusive access session is active."""
        ...
    def GetHashCode(self) -> int:
        """Returns a hash code for this instance.
        Returns:
            int: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self) -> str:
        """Returns a System.String that represents the current System.Object.
        Returns:
            str: A System.String that represents the current System.Object.
        """
        ...
    def Transaction(self, peristence: ITransactionSupport, undoDescription: str) -> Transaction:
        """Acquires a transaction instance from the active exclusive access session
        Parameters:
            peristence (ITransactionSupport): The persistence where the transaction is to be created
            undoDescription (str): The description of the undo unit that is created for the open transaction
        Returns:
            Transaction: The transaction instance.
        """
        ...

class ExportOptions(Enum):
    """The list of possible scenarios supported by export action parameterization
    Options for the export action parameterization:
        None(0): No export options
        WithDefaults(1): Export with default values
        WithReadOnly(2): Export with read-only values
    """

    def __init__(self, value: int) -> None: ...

    value__ = ...
    WithDefaults = ...
    WithReadOnly = ...

class HistoryEntry(
    IEngineeringObject,
    IInternalObjectAccess,  # type: ignore
    IEquatable,
):
    """Represents a TIAP project history event"""

    @property
    def DateTime(self) -> DateTime:
        """The time when the event occurred"""
        ...
    @property
    def Parent(self) -> IEngineeringObject:
        """EOM parent of this object"""
        ...
    @property
    def Text(self) -> str:
        """The event description"""
        ...
    def GetHashCode(self) -> int:
        """Returns a hash code for this instance.
        Returns:
            int: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self) -> str:
        """Returns a System.String that represents the current System.Object.
        Returns:
            str: A System.String that represents the current System.Object.
        """
        ...

class IEngineeringComposition(IEngineeringCompositionOrObject, IEnumerable[U]):
    """IEngineeringComposition"""

    @property
    def Count(self) -> int:
        """Gets the number of elements contained in the IEngineeringComposition."""
        ...
    @property
    def IsReadOnly(self) -> bool:
        """Gets a value indicating whether this Composition was instantiated as ReadOnly."""
        ...
    def Contains(self, item: U) -> bool:
        """Determines if item is contained within.
        Parameters:
            item (IEngineeringObject): The item being sought.
        Returns:
            bool: true if item is contained within; otherwise false.
        """
        ...
    def Create(self, type: Optional[T], parameters: Optional[Dict[str, Object]]) -> T:
        """Creates an object of the given type with the given parameters.
        Parameters:
            type (T): The type of the object to create.
            parameters (Dict[str, Object]): The parameters to use for the creation of the object.
        Returns:
            T: The created object.
        """
        ...
    def GetCreationInfos(self) -> List[EngineeringCreationInfo]:
        """Returns a collection of EngineeringCreationInfo objects describing the different types of objects that can be created on this object.
        Returns:
            List[EngineeringCreationInfo]: A collection of EngineeringCreationInfo objects describing the different types of objects that can be created on this object.
        """
        ...
    def GetInvocationInfos(self) -> List[EngineeringInvocationInfo]:
        """Returns a collection of EngineeringInvocationInfo objects describing the different actions on this object.
        Returns:
            List[EngineeringInvocationInfo]: A collection of EngineeringInvocationInfo objects describing the different actions on this object.
        """
        ...
    def IndexOf(self, item: U) -> int:
        """Searches for item and returns the zero-based index of the first occurrence within.
        Parameters:
            item (IEngineeringObject): The item for which an index is sought.
        Returns:
            int: The element at the specified item.
        """
        ...
    def Invoke(self, name: str, parameters: Dict[Any, Object]) -> Object:
        """Invokes the action with the given name and parameters.
        Parameters:
            name (str): The name of the action to invoke.
            parameters (Dict[Any, Object]): The parameters to use for the invocation of the action.
        Returns:
            Object: The result of the invocation.
        """
        ...
    def __getitem__(self, *args): ...

class HistoryEntryComposition(
    IEngineeringComposition[HistoryEntry],
    IInternalCompositionAccess,  # type: ignore
    IEquatable,
):
    """Composition of HistoryEntries"""

    @property
    def Parent(self) -> IEngineeringObject:
        """EOM parent of this object"""
        ...
    def GetHashCode(self) -> int:
        """Returns a hash code for this instance.
        Returns:
            int: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self) -> str:
        """Returns a System.String that represents the current System.Object.
        Returns:
            str: A System.String that represents the current System.Object.
        """
        ...

class IEngineeringAssociation(IEngineeringInstance, IEnumerable[U]):
    """IEngineeringAssociation"""

    @property
    def Count(self) -> int:
        """Gets the number of elements contained in the IEngineeringAssociation."""
        ...
    @property
    def IsReadOnly(self) -> bool:
        """Gets a value indicating whether this Association was instantiated as ReadOnly."""
        ...
    def Contains(self, item: U) -> bool:
        """Determines if item is contained within.
        Parameters:
            item (IEngineeringObject): The item being sought.
        Returns:
            bool: true if item is contained within; otherwise false.
        """
        ...
    def GetInvocationInfos(self) -> List[EngineeringInvocationInfo]:
        """Returns a collection of EngineeringInvocationInfo objects describing the different actions on this object.
        Returns:
            List[EngineeringInvocationInfo]: A collection of EngineeringInvocationInfo objects describing the different actions on this object.
        """
        ...
    def IndexOf(self, item: U) -> int:
        """Searches for item and returns the zero-based index of the first occurrence within.
        Parameters:
            item (IEngineeringObject): The item for which an index is sought.
        Returns:
            int: The element at the specified item.
        """
        ...
    def Invoke(self, name: str, parameters: Dict[Any, Object]) -> Object:
        """Invokes the action with the given name and parameters.
        Parameters:
            name (str): The name of the action to invoke.
            parameters (Dict[Any, Object]): The parameters to use for the invocation of the action.
        Returns:
            Object: The result of the invocation.
        """
        ...
    def __getitem__(self, *args): ...

class IEngineeringObjectAssociation(
    IEngineeringAssociation[IEngineeringObject],
    IInternalAssociationAccess,  # type: ignore
    IEquatable,
):
    """Associated engineering objects"""

    @property
    def Parent(self) -> IEngineeringObject:
        """EOM parent of this object"""
        ...
    def GetHashCode(self) -> int:
        """Returns a hash code for this instance.
        Returns:
            int: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self) -> str:
        """Returns a System.String that represents the current System.Object.
        Returns:
            str: A System.String that represents the current System.Object.
        """
        ...

class IEngineeringRoot(IEngineeringObject):
    """IEngineeringRoot"""

    ...

class IEngineeringService:
    """The interface representing an engineering service"""

    ...

class IEngineeringServiceProvider(IServiceProvider):
    """IEngineeringServiceProvider"""

    def GetServiceInfos(self) -> List[EngineeringServiceInfo]:
        """Returns a collection of EngineeringServiceInfo objects describing the different services on this object.
        Returns:
            List[EngineeringServiceInfo]: A collection of EngineeringServiceInfo objects describing the different services on this object.
        """
        ...

class ImportOptions(Enum):
    """The list of possible options for Import
    Options for Import:
        None (0): No options
        Override (1): Override existing objects
    """

    Override = ...
    value__ = ...

class IShowable:
    """Access to Showable attributes"""

    def ShowInEditor(self) -> None:
        """Shows the object in the editor."""
        ...

class ISystemObject:
    """Access to SystemObject attributes"""

    @property
    def IsSystemObject(self) -> bool:
        """Indicates if this instance is a system object"""
        ...

class ITransactionSupport:
    """An interface indication that the item supports transactions"""

    ...

class Language(
    IEngineeringObject,
    IInternalObjectAccess,  # type: ignore
    IEquatable,
):
    """Represents a language that can be enabled in this Project"""

    @property
    def Culture(self) -> CultureInfo:
        """The culture info object"""
        ...
    @property
    def Parent(self) -> IEngineeringObject:
        """EOM parent of this object"""
        ...
    def GetHashCode(self) -> int:
        """Gives a hash code for this instance.
        Returns:
            int: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self) -> str:
        """Returns a System.String that represents the current System.Object.
        Returns:
            str: A System.String that represents the current System.Object.
        """
        ...

class LanguageAssociation(
    IEngineeringAssociation[Language],
    IEngineeringInstance,
    IInternalAssociationAccess,  # type: ignore
    IEquatable,
):
    """Collection of Languages."""

    @property
    def Parent(self) -> IEngineeringObject:
        """EOM parent of this object"""
        ...
    def Add(self, item: Language) -> None:
        """Adds an item to the collection.
        Parameters:
            item (Language): The item to add.
        """
        ...
    def Find(self, culture: CultureInfo) -> Language:
        """Searches for a language by a given culture.
        Parameters:
            culture (CultureInfo): The culture to search for.
        Returns:
            Language: The language with the given culture, or None if not found.
        """
        ...
    def GetHashCode(self) -> int:
        """Returns a hash code for this instance.
        Returns:
            int: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def Remove(self, item: Language) -> bool:
        """Removes an item.
        Parameters:
            item (Language): The item to be removed.
        Returns:
            bool: true if the item was removed; otherwise false.
        """
        ...
    def ToString(self) -> str:
        """Returns a System.String that represents the current System.Object.
        Returns:
            str: A System.String that represents the current System.Object.
        """
        ...

class LanguageComposition(
    IEngineeringComposition[Language],
    IInternalCompositionAccess,  # type: ignore
    IEquatable,
):
    """Composition of Languages"""

    @property
    def Parent(self) -> IEngineeringObject:
        """EOM parent of this object"""
        ...
    def Find(self, culture: CultureInfo) -> Language:
        """Searches for a language by a given culture.
        Parameters:
            culture (CultureInfo): The culture to search for.
        Returns:
            Language: The language with the given culture, or None if not found.
        """
        ...
    def GetHashCode(self) -> int:
        """Returns a hash code for this instance.
        Returns:
            int: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self) -> str:
        """Returns a System.String that represents the current System.Object.
        Returns:
            str: A System.String that represents the current System.Object.
        """
        ...

class LanguageSettings(
    IEngineeringObject,
    IInternalObjectAccess,  # type: ignore
    IEquatable,
):
    """Represents a language settings object."""

    @property
    def ActiveLanguages(self) -> LanguageAssociation:
        """The collection of active languages."""
        ...
    @property
    def EditingLanguage(self) -> Language:
        """The editing language."""
        ...
    @property
    def Languages(self) -> LanguageComposition:
        """The collection of languages."""
        ...
    @property
    def Parent(self) -> IEngineeringObject:
        """EOM parent of this object"""
        ...
    @property
    def ReferenceLanguage(self) -> Language:
        """The reference language."""
        ...
    def GetHashCode(self) -> int:
        """Returns a hash code for this instance.
        Returns:
            int: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self) -> str:
        """Returns a System.String that represents the current System.Object.
        Returns:
            str: A System.String that represents the current System.Object.
        """
        ...

class MultilingualText(
    IEngineeringObject,
    IInternalObjectAccess,  # type: ignore
    IEquatable,
):
    """Represents a String in multiple language translations"""

    @property
    def Items(self) -> MultilingualTextItemComposition:
        """Contains a collection of multilingual text items."""
        ...
    @property
    def Parent(self) -> IEngineeringObject:
        """EOM parent of this object"""
        ...
    def GetHashCode(self) -> int:
        """Returns a hash code for this instance.
        Returns:
            int: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self) -> str:
        """Returns a System.String that represents the current System.Object.
        Returns:
            str: A System.String that represents the current System.Object.
        """
        ...

class MultilingualTextItem(
    IEngineeringObject,
    IInternalObjectAccess,  # type: ignore
    IEquatable,
):
    """Multilingual text item."""

    @property
    def Language(self) -> Language:
        """Represents language of this item."""
        ...
    @property
    def Parent(self) -> IEngineeringObject:
        """EOM parent of this object"""
        ...
    @property
    def Text(self) -> str:
        """Represents text of this item."""
        ...
    def GetHashCode(self) -> int:
        """Returns a hash code for this instance.
        Returns:
            int: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self) -> str:
        """Returns a System.String that represents the current System.Object.
        Returns:
            str: A System.String that represents the current System.Object.
        """
        ...

class MultilingualTextItemComposition(
    IEngineeringComposition[MultilingualTextItem],
    IInternalCompositionAccess,  # type: ignore
    IEquatable,
):
    """Collection of multilingual text items."""

    @property
    def Parent(self) -> IEngineeringObject:
        """EOM parent of this object"""
        ...
    def Find(self, language: Language) -> MultilingualTextItem:
        """Searches multilingual text item by language.
        Parameters:
            language (Language): Language to find.
        Returns:
            MultilingualTextItem: Siemens.Engineering.MultilingualTextItem
        """
        ...
    def GetHashCode(self) -> int:
        """Returns a hash code for this instance.
        Returns:
            int: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self) -> str:
        """Returns a System.String that represents the current System.Object.
        Returns:
            str: A System.String that represents the current System.Object.
        """
        ...

class NonRecoverableException(Exception):
    """NonRecoverableException"""

    @property
    def DetailMessageData(self) -> List[ExceptionMessageData]:
        """Gets the detail message data."""
        ...
    @property
    def MessageData(self) -> ExceptionMessageData:
        """Gets the message data."""
        ...
    SerializeObjectState = ...

class NotificationEventArgs(EventArgs):
    """Notification event arguments"""

    @property
    def Caption(self) -> str:
        """Caption of the notification event arguments"""
        ...
    @property
    def DetailText(self) -> str:
        """Detail text of the notification event arguments"""
        ...
    @property
    def Icon(self) -> NotificationIcon:
        """Icon of the notification event arguments"""
        ...
    @property
    def IsHandled(self) -> bool:
        """IsHandled of the notification event arguments"""
        ...
    @property
    def Text(self) -> str:
        """Text of the notification event arguments"""
        ...

class NotificationIcon(Enum):
    """The list of possible notification icons
    Options:
        Success (0): Success
        Information (1): Information
        Warning (2): Warning
        Error (3): Error
    """

    Error = ...
    Information = ...
    Success = ...
    value__ = ...
    Warning = ...

class OpenMode(Enum):
    """The modification state of an item being opened.
    Options:
        ReadOnly (0): ReadOnly
        ReadWrite (1): ReadWrite
    """

    ReadOnly = ...
    ReadWrite = ...
    value__ = ...

class Project(
    IEngineeringObject,
    ITransactionSupport,
    IMasterCopyTarget,
    IInternalObjectAccess,  # type: ignore
    IEngineeringServiceProvider,
    IEquatable,
):
    """Represents a project"""

    @property
    def Author(self) -> str:
        """Gets or sets the author of the project"""
        ...
    @property
    def Comment(self) -> MultilingualText:
        """Gets or sets the comment of the project"""
        ...
    @property
    def Copyright(self) -> str:
        """Gets or sets the copyright of the project"""
        ...
    @property
    def CreationDate(self) -> DateTime:
        """Gets the creation date of the project"""
        ...
    @property
    def DeviceGroups(self) -> DeviceUserGroupComposition:
        """Gets the device groups of the project"""
        ...
    @property
    def Devices(self) -> DeviceComposition:
        """Gets the devices of the project"""
        ...
    @property
    def Family(self) -> str:
        """Gets or sets the family of the project"""
        ...
    @property
    def Graphics(self) -> MultiLingualGraphicComposition:
        """Gets the graphics of the project"""
        ...
    @property
    def HistoryEntries(self) -> HistoryEntryComposition:
        """Gets the history entries of the project"""
        ...
    @property
    def HwUtilities(self) -> HardwareUtilityComposition:
        """Gets the hardware utilities of the project"""
        ...
    @property
    def IsModified(self) -> bool:
        """Gets a value indicating whether the project has unsaved changes"""
        ...
    @property
    def IsPrimary(self) -> bool:
        """Gets a value indicating whether the project is the primary project"""
        ...
    @property
    def LanguageSettings(self) -> LanguageSettings:
        """Gets the language settings of the project"""
        ...
    @property
    def LastModified(self) -> DateTime:
        """Gets the last modified date of the project"""
        ...
    @property
    def LastModifiedBy(self) -> str:
        """Gets the last modified by of the project"""
        ...
    @property
    def Name(self) -> str:
        """Gets or sets the name of the project"""
        ...
    @property
    def Parent(self) -> IEngineeringObject:
        """Gets the parent of the project"""
        ...
    @property
    def Path(self) -> FileInfo:
        """Gets the path of the project"""
        ...
    @property
    def ProjectLibrary(self) -> ProjectLibrary:
        """Gets the project library of the project"""
        ...
    @property
    def Size(self) -> Int64:
        """Gets the size of the project"""
        ...
    @property
    def Subnets(self) -> SubnetComposition:
        """Gets the subnets of the project"""
        ...
    @property
    def UngroupedDevicesGroup(self) -> DeviceSystemGroup:
        """Gets the ungrouped devices system group of the project"""
        ...
    @property
    def UsedProducts(self) -> UsedProductComposition:
        """Gets the used products of the project"""
        ...
    @property
    def Version(self) -> str:
        """Gets the version of the project"""
        ...
    def Archive(self, targetDirectory: DirectoryInfo, targetName: str, archivationMode: ProjectArchivationMode) -> None:
        """Archives the current project
        Parameters:
            targetDirectory (DirectoryInfo): Directory where the project to be archived
            targetName (str): File name for the archived file
            archivationMode (ProjectArchivationMode): Archivation mode
        """
        ...
    def Close(self) -> None:
        """Closes the project"""
        ...
    def ExportProjectTexts(self, path: FileInfo, sourceLanguage: CultureInfo, targetLanguage: CultureInfo) -> None:
        """Export project text to an xlsx file
        Parameters:
            path (FileInfo): Path to the xlsx file
            sourceLanguage (CultureInfo): The source language to use for the export of project texts
            targetLanguage (CultureInfo): The target language to use for the export of project texts
        """
        ...
    def GetHashCode(self) -> int:
        """Returns a hash code for this instance.
        Returns:
            int: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ImportProjectTexts(self, path: FileInfo, updateSourceLanguage: bool) -> ProjectTextResult:
        """Import project text from an import file
        Parameters:
            path (FileInfo): Path to the xlsx file
            updateSourceLanguage (bool): True if the source language is to be updated
        Returns:
            ProjectTextResult: Siemens.Engineering.ProjectTextResult
        """
        ...
    def Save(self) -> None:
        """Saves all changes of the project"""
        ...
    def SaveAs(self, targetFolderPath: DirectoryInfo) -> None:
        """Saves all changes of the project to a new location
        Parameters:
            targetFolderPath (DirectoryInfo): Target location for newly SavedAs project
        """
        ...
    def ShowHwEditor(self, view: View) -> None:
        """Show the indicated item in the HW editor of the attached TIA Portal
        Parameters:
            view (View): Which view of the HW editor to show
        """
        ...
    def ToString(self) -> str:
        """Returns a System.String that represents the current System.Object.
        Returns:
            str: A System.String that represents the current System.Object.
        """
        ...

class ProjectArchivationMode(Enum):
    """
    ProjectArchivationMode enum
        Options for archivation mode:
            None(0): No archivation
            Compressed(1): Compressed archivation
            DiscardRestorableData(2): Discard restorable data
            DiscardRestorableDataAndCompressed(3): Discard restorable data and compressed
    """

    Compressed = ...
    DiscardRestorableData = ...
    DiscardRestorableDataAndCompressed = ...
    value__ = ...

class ProjectComposition(
    IEngineeringComposition[Project],
    IInternalCompositionAccess,  # type: ignore
    IEquatable,
):
    """Composition of Projects"""

    @property
    def Parent(self) -> IEngineeringObject:
        """Gets the parent of the composition"""
        ...
    def Create(self, path: DirectoryInfo, name: str) -> Project:
        """Creates a new project
        Parameters:
            path (DirectoryInfo): Path to the project
            name (str): Name of the project
        """
        ...
    def GetHashCode(self) -> int:
        """Returns a hash code for this instance.
        Returns:
            int: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def Open(
        self,
        path: FileInfo,
        umacDelegate: Optional[UmacDelegate] = ...,
        projectOpenMode: Optional[ProjectOpenMode] = ...,
    ) -> Project:
        """Open a project from the specified path.
        Parameters:
            path (FileInfo): Path to the Tia Portal project file.
            umacDelegate (UmacDelegate, optional): Delegate that will be called if user authentication with UMAC is necessary. Defaults to None.
            projectOpenMode (ProjectOpenMode, optional): The mode in which the project will be opened. Defaults to ProjectOpenMode.Primary.
        Returns:
            Project: The opened project.
        """
        ...
    def OpenWithUpgrade(
        self,
        path: FileInfo,
        umacDelegate: Optional[UmacDelegate] = ...,
        projectOpenMode: Optional[ProjectOpenMode] = ...,
    ) -> Project:
        """Open a project from the specified path. If the project is not compatible with the current version of TIA Portal, it will be upgraded.
        Parameters:
            path (FileInfo): Path to the Tia Portal project file.
            umacDelegate (Optional[UmacDelegate], optional): Delegate that will be called if user authentication with UMAC is necessary. Defaults to None.
            projectOpenMode (Optional[ProjectOpenMode], optional): The mode in which the project will be opened. Defaults to ProjectOpenMode.Primary.
        Returns:
            Project: The opened project.
        """
        ...
    def Retrieve(
        self,
        sourcePath: FileInfo,
        targetDirectory: DirectoryInfo,
        umacDelegate: Optional[UmacDelegate] = ...,
        projectOpenMode: Optional[ProjectOpenMode] = ...,
    ) -> Project:
        """Retrieves an archived project with or without UMAC
        Parameters:
            sourcePath (FileInfo): The path of the archived project file
            targetDirectory (DirectoryInfo): The path to the folder where project would be retrieved.
            umacDelegate (Optional[UmacDelegate], optional): Delegate will be called if the project is protected and user authentication is required. If the project is not protected, this parameter is ignored. Defaults to None.
            projectOpenMode (Optional[ProjectOpenMode], optional): The mode in which the project will be opened. Defaults to ProjectOpenMode.Primary.
        Returns:
            Project: The retrieved project.
        """
        ...
    def RetrieveWithUpgrade(
        self,
        sourcePath: FileInfo,
        targetDirectory: DirectoryInfo,
        umacDelegate: Optional[UmacDelegate] = ...,
        projectOpenMode: Optional[ProjectOpenMode] = ...,
    ) -> Project:
        """Retrieves a project from an archive and upgrades it to the current version with umac
        Parameters:
            sourcePath (FileInfo): The path of the archived project file
            targetDirectory (DirectoryInfo): The path to the folder where project would be retrieved.
            umacDelegate (Optional[UmacDelegate], optional): Delegate will be called if the project is protected and user authentication is required. If the project is not protected, this parameter is ignored. Defaults to None.
            projectOpenMode (Optional[ProjectOpenMode], optional): The mode in which the project will be opened. Defaults to ProjectOpenMode.Primary.
        Returns:
            Project: The retrieved project.
        """
        ...
    def ToString(self) -> str:
        """Returns a System.String that represents the current System.Object.
        Returns:
            str: A System.String that represents the current System.Object.
        """
        ...

class ProjectOpenMode(Enum):
    """
    Project open mode
    Options for opening a project:
        Primary(0): Open the project in primary mode. This is the default mode.
        Secondary(1): Open the project in secondary mode.
    """

    Primary = ...
    Secondary = ...
    value__ = ...

class ProjectTextResult(
    IEngineeringObject,
    IInternalObjectAccess,  # type: ignore
    IInternalInstanceAccess,  # type: ignore
    IInternalBaseAccess,  # type: ignore
    IEquatable,
):
    """Represents a project text result"""

    @property
    def Path(self) -> FileInfo:
        """Path to the project text result file"""
        ...
    @property
    def State(self) -> ProjectTextResultState:
        """State of the project text result"""
        ...
    @property
    def Parent(self) -> IEngineeringObject:
        """EOM parent of this object"""
        ...
    def GetHashCode(self) -> int:
        """Returns a hash code for this instance.
        Returns:
            int: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self) -> str:
        """Returns a System.String that represents the current System.Object.
        Returns:
            str: A System.String that represents the current System.Object.
        """
        ...

class ProjectTextResultState(Enum):
    """
    The state of project text result
    Options for the state of project text result:
        Info(0): The project text result is an info.
        Warning(1): The project text result is a warning.
        Error(2): The project text result is an error.
    """

    Error = ...
    Info = ...
    value__ = ...
    Warning = ...

class TiaPortal(
    IApplicationEntryPoint,  # type: ignore
    IInternalApplicationAccess,  # type: ignore
    IEngineeringRoot,
    IEquatable,
    IDisposable,
):
    """Represents a connection to the TIA Portal.
    Parameters:
        tiaPortalMode(TiaPortalMode): The TIA Portal mode to connect to.
    """

    @property
    def GlobalLibraries(self) -> GlobalLibraryComposition:
        """The global libraries of the TIA Portal"""
        ...
    @property
    def Projects(self) -> ProjectComposition:
        """The projects of the TIA Portal"""
        ...
    @property
    def SettingsFolders(self) -> TiaPortalSettingsFolderComposition:
        """The settings folders of the TIA Portal"""
        ...
    Confirmation = ...
    Disposed = ...
    Notification = ...

    def ExclusiveAccess(self, text: Optional[str] = ...) -> ExclusiveAccess:
        """Acquire an exclusive access session to the TIA Portal
        Parameters:
            text (Optional[str], optional): The text to present to the interactive user while an exclusive access session is active. Defaults to None.
        Returns:
            ExclusiveAccess: Siemens.Engineering.ExclusiveAccess
        """
        ...
    def GetCurrentProcess(self) -> TiaPortalProcess:
        """Gets the information of connected TIA-Portal.
        Returns:
            TiaPortalProcess: The connected TIA-Portal.
        """
        ...
    @staticmethod
    def GetProcess(processId: int, *__args) -> TiaPortalProcess:
        """Gets the information of the running TIA-Portal.
        Parameters:
            processId (int): TIA-Portal's process id.
            timeout (Optional[TimeSpan], optional): An optional parameter that provides the ability to set a timeout. Defaults to None.
            millisecondsTimeout (Optional[int], optional): An optional parameter that provides the ability to set a timeout. Defaults to None.
        Returns:
            TiaPortalProcess: The running TIA-Portal.
        """
        ...
    @staticmethod
    def GetProcesses() -> List[TiaPortalProcess]:
        """Gets the information of all running TIA-Portals.
        Returns:
            List[TiaPortalProcess]: The running TIA-Portals.
        """
        ...

class TiaPortalAccessLevel(Enum):
    """
    The access level of the associated TIA Portal
    Options for the access level of the associated TIA Portal:
        None(0): No access level.
        NoLicense(1): No license.
        Trusted(2): Trusted.
        Modify(4): Modify.
        Published(8): Published.
        Pilot(32): Pilot.
        Elevated(256): Elevated.
    """

    Elevated = ...
    Modify = ...
    NoLicense = ...
    Pilot = ...
    Published = ...
    Trusted = ...
    value__ = ...

class TiaPortalMode(Enum):
    """
    Mode how to start the TIA-Portal.
    Options:
        WithoutUserInterface(0): Start the TIA-Portal without user interface.
        WithUserInterface(1): Start the TIA-Portal with user interface.
    """

    value__ = ...
    WithoutUserInterface = ...
    WithUserInterface = ...

class TiaPortalProcess(IDisposable):
    """TiaPortalProcess"""

    @property
    def AcquisitionTime(self) -> DateTime:
        """Gets the time when the TiaPortalProcess object was acquired."""
        ...
    @property
    def AttachedSessions(self) -> List[TiaPortalProcess]:
        """Gets the attached TIA-Portal processes."""
        ...
    @property
    def Id(self) -> int:
        """Gets the process id of the TIA-Portal."""
        ...
    @property
    def InstalledSoftware(self) -> List[TiaPortalProduct]:
        """Gets the installed software of the TIA-Portal."""
        ...
    @property
    def Mode(self) -> TiaPortalMode:
        """Gets the mode of the TIA-Portal."""
        ...
    @property
    def Path(self) -> FileInfo:
        """Gets the path of the executable of the TIA-Portal."""
        ...
    @property
    def ProjectPath(self) -> FileInfo:
        """Gets the path of any project currently open in the attached TIA-Portal."""
        ...
    Attaching = ...
    def Attach(self) -> TiaPortal:
        """Gets an additional instance of a TIA-Portal that is attached to the TIA-Portal process."""
        ...

class TiaPortalProduct:
    """TiaPortalProduct"""

    @property
    def Name(self) -> str:
        """Gets the product name."""
        ...
    @property
    def Options(self) -> List[TiaPortalProduct]:
        """Gets a list of installed options of the TIA-Portal process."""
        ...
    @property
    def Version(self) -> str:
        """Gets the product version."""
        ...

class TiaPortalSession(IDisposable):
    """TiaPortalSession"""

    @property
    def AccessLevel(self) -> TiaPortalAccessLevel:
        """Gets the access level of the process."""
        ...
    @property
    def AttachTime(self) -> DateTime:
        """Gets the attached session date and time."""
        ...
    @property
    def Id(self) -> int:
        """Gets the attached session identifier."""
        ...
    @property
    def IsActive(self) -> bool:
        """Gets a value describing whether the TIA-Portal is in the middle of processing a call from this session."""
        ...
    @property
    def ProcessId(self) -> int:
        """Gets the process id of the TIA-Portal."""
        ...
    @property
    def ProcessPath(self) -> FileInfo:
        """Gets the path to where the executable of the attached process lives."""
        ...
    @property
    def TrustAuthority(self) -> bool:
        """Indicates if the current session was started by a process that was signed,and if so,if it is an Openness certificate or not."""
        ...
    @property
    def UtilizationTime(self) -> TimeSpan:
        """Gets the attached session utilization time."""
        ...
    @property
    def Version(self) -> str:
        """Gets the version of the TIA-Portal."""
        ...

class TiaPortalTrustAuthority(Enum):
    """
    The trust authority of the associated TIA Portal
    Options for the trust authority of the associated TIA Portal:
        None(0): No trust authority.
        Signed(1): Signed.
        Certified(2): Certified.
        CertifiedWithExpiration(256): Certified with expiration.
        FeatureTokens(512): Feature tokens.
    """

    Certified = ...
    CertifiedWithExpiration = ...
    FeatureTokens = ...
    Signed = ...
    value__ = ...

class Transaction(
    IEngineeringObject,
    IDisposable,
    IInternalObjectAccess,  # type: ignore
    IEquatable,
):
    """Represents an open transaction in a persistence (i.e. single unit of work)"""

    @property
    def CanCommit(self) -> bool:
        """Gets a value indicating whether the transaction can be committed."""
        ...
    @property
    def CommitRequested(self) -> bool:
        """Gets a value indicating whether the transaction has been requested to be committed."""
        ...
    @property
    def Parent(self) -> IEngineeringObject:
        """Gets the parent object of the transaction."""
        ...
    def CommitOnDispose(self):
        """Commit transaction when disposed"""
        ...
    def GetHashCode(self) -> int:
        """Returns a hash code for this instance
        Returns:
            int: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self) -> str:
        """Returns a System.String that represents the current System.Object.
        Returns:
            str: A System.String that represents the current System.Object.
        """
        ...

class UmacCredentials(
    IEngineeringObject,
    IInternalObjectAccess,  # type: ignore
    IEquatable,
):
    """Object that is used to authenticate user."""

    @property
    def Name(self) -> str:
        """Gets or sets the name of the UmacCredentials object."""
        ...
    @property
    def Type(self) -> UmacUserType:
        """Gets or sets the type of the UmacCredentials object."""
        ...
    @property
    def Parent(self) -> IEngineeringObject:
        """Gets the parent object of the UmacCredentials object."""
        ...
    def GetHashCode(self) -> int:
        """Returns a hash code for this instance.
        Returns:
            int: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def SetPassword(self, password: SecureString) -> None:
        """Sets the password of the UmacCredentials object.
        Parameters:
            password (SecureString): The password to set.
        """
        ...
    def ToString(self) -> str:
        """Returns a System.String that represents the current System.Object.
        Returns:
            str: A System.String that represents the current System.Object.
        """
        ...

class UmacDelegate(MulticastDelegate):
    """
    The delegate that will called back for user credetials if project is protected.
    """

    def BeginInvoke(self, umacCredentials: UmacCredentials, callback: AsyncCallback, object: Object) -> IAsyncResult:
        """Starts an asynchronous invocation of the delegate.
        Parameters:
            umacCredentials (UmacCredentials): Credentials to be used for authentication.
            callback (AsyncCallback): The method to be called when the asynchronous operation completes.
            object : The object to pass to the callback method.
        Returns:
            IAsyncResult: An System.IAsyncResult that references the asynchronous invocation.
        """
        ...
    def EndInvoke(self, result: IAsyncResult) -> None:
        """Ends an asynchronous invocation of the delegate.
        Parameters:
            result (IAsyncResult): The System.IAsyncResult returned by a call
        """
        ...
    def Invoke(self, umacCredentials: UmacCredentials):
        """Invokes the delegate.
        Parameters:
            umacCredentials (UmacCredentials): Credentials to be used for authentication.
        """
        ...

class UmacUserType(Enum):
    """
    User type.
    Options:
        Project (0): Project user.
        Global (1): Global user.
    """

    Global = ...
    Project = ...
    value__ = ...

class UsedProduct(
    IEngineeringObject,
    IInternalObjectAccess,  # type: ignore
    IEquatable,
):
    """Represents a product used by a project"""

    @property
    def Name(self) -> str:
        """Gets or sets the name of the UsedProduct object."""
        ...
    @property
    def Parent(self) -> IEngineeringObject:
        """Gets the parent object of the UsedProduct object."""
        ...
    @property
    def Version(self) -> str:
        """Gets the version of the UsedProduct object."""
        ...
    def GetHashCode(self) -> int:
        """Returns a hash code for this instance.
        Returns:
            int: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self) -> str:
        """Returns a System.String that represents the current System.Object.
        Returns:
            str: A System.String that represents the current System.Object.
        """
        ...

class UsedProductComposition(
    IEngineeringComposition[UsedProduct],
    IEngineeringCompositionOrObject,
    IEngineeringInstance,
    IEnumerable[UsedProduct],
    IInternalCompositionAccess,  # type: ignore
    IInternalCollectionAccess,  # type: ignore
    IInternalInstanceAccess,  # type: ignore
    IInternalBaseAccess,  # type: ignore
    IEquatable,
):
    """Composition of UsedProducts"""

    @property
    def Parent(self) -> IEngineeringObject:
        """Gets the parent object of the UsedProductComposition object."""
        ...
    def GetHashCode(self) -> int:
        """Returns a hash code for this instance.
        Returns:
            int: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self) -> str:
        """Returns a System.String that represents the current System.Object.
        Returns:
            str: A System.String that represents the current System.Object.
        """
        ...
