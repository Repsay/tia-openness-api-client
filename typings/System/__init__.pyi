# encoding: utf-8
# module System
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
# no doc
# no imports

# no functions
# classes
import enum
from typing import Generic, Optional, TypeVar
from System.Collections import (IComparer, IEnumerator, IEqualityComparer,
                                IList, IStructuralComparable,
                                IStructuralEquatable)
from System.Collections.Generic import IReadOnlyList
from System.ComponentModel import TypeConverter
from System.Reflection import MemberInfo
from System.Runtime.InteropServices import (_Activator, _Attribute, _Exception, # type: ignore
                                            _Type) # type: ignore
from System.Runtime.Serialization import (IDeserializationCallback,
                                          ISerializable)

X = TypeVar('X', covariant=True)
T = TypeVar('T')

class Object:
    """
    Supports all classes in the .NET Framework class hierarchy and provides low-level services to derived classes. This is the ultimate base class of all classes in the .NET Framework; it is the root of the type hierarchy.To browse the .NET Framework source code for this type, see the Reference Source.

    object()
    """
    def __delattr__(self, *args): #cannot find CLR method
        """ __delattr__(self: object, name: str) """
        ...

    def __format__(self, *args): #cannot find CLR method
        """ __format__(self: object, formatSpec: str) -> str """
        ...

    def __getattribute__(self, *args): #cannot find CLR method
        """ __getattribute__(self: object, name: str) -> object """
        ...

    def __hash__(self, *args): #cannot find CLR method
        """ x.__hash__() <==> hash(x) """
        ...

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        ...

    @staticmethod # known case of __new__
    def __new__(cls):
        """
        __new__(cls: type) -> object

        __new__(cls: type, *args�: Array[object]) -> object

        __new__(cls: type, **kwargs�: dict, *args�: Array[object]) -> object
        """
        ...

    def __reduce_ex__(self, *args): #cannot find CLR method
        ...

    def __reduce__(self, *args): #cannot find CLR method
        """ helper for pickle """
        ...

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        ...

    def __setattr__(self, *args): #cannot find CLR method
        """ __setattr__(self: object, name: str, value: object) """
        ...

    def __sizeof__(self, *args): #cannot find CLR method
        """ __sizeof__(self: object) -> int """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...

    def __subclasshook__(self, *args): #cannot find CLR method
        """ __subclasshook__(*args: Array[object]) -> NotImplementedType """
        ...

    __class__ = ...


class Exception(ISerializable, _Exception):
    """
    Represents errors that occur during application execution.To browse the .NET Framework source code for this type, see the Reference Source.

    Exception()

    Exception(message: str)

    Exception(message: str, innerException: Exception)
    """
    @property
    def Data(self):
        """
        Gets a collection of key/value pairs that provide additional user-defined information about the exception.

        Get: Data(self: Exception) -> IDictionary
        """
        ...

    @property
    def HResult(self):
        """
        Gets or sets HRESULT, a coded numerical value that is assigned to a specific exception.

        Get: HResult(self: Exception) -> int
        """
        ...


    SerializeObjectState = None


class SystemException(Exception): # skipped bases: <type 'ISerializable'>, <type '_Exception'>
    """
    Serves as the base class for system exceptions namespace.

    SystemException()

    SystemException(message: str)

    SystemException(message: str, innerException: Exception)
    """
    SerializeObjectState = None


class AccessViolationException(SystemException): # skipped bases: <type 'ISerializable'>, <type '_Exception'>
    """
    The exception that is thrown when there is an attempt to read or write protected memory.

    AccessViolationException()

    AccessViolationException(message: str)

    AccessViolationException(message: str, innerException: Exception)
    """
    SerializeObjectState = None


class Action:
    """
    Encapsulates a method that has no parameters and does not return a value.

    Action(object: object, method: IntPtr)
    """
    def BeginInvoke(self, callback, object):
        """ BeginInvoke(self: Action, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

# Error generating skeleton for function CombineImpl: 'type' object has no attribute '__bases__'

# Error generating skeleton for function DynamicInvokeImpl: 'type' object has no attribute '__bases__'

    def EndInvoke(self, result):
        """ EndInvoke(self: Action, result: IAsyncResult) """
        ...

# Error generating skeleton for function GetMethodImpl: 'type' object has no attribute '__bases__'

    def Invoke(self):
        """ Invoke(self: Action) """
        ...

# Error generating skeleton for function RemoveImpl: 'type' object has no attribute '__bases__'

    @staticmethod # known case of __new__
    def __new__(cls, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        ...

# Error generating skeleton for function __reduce_ex__: 'type' object has no attribute '__bases__'


class IDisposable:
    """ Provides a mechanism for releasing unmanaged resources.To browse the .NET Framework source code for this type, see the Reference Source. """
    def Dispose(self) -> None:
        """ Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources. """
        ...


class ActivationContext(IDisposable, ISerializable):
    """ Identifies the activation context for the current application. This class cannot be inherited. """
    @property
    def ApplicationManifestBytes(self):
        """
        Gets the ClickOnce application manifest for the current application.

        Get: ApplicationManifestBytes(self: ActivationContext) -> Array[Byte]
        """
        ...

    @property
    def DeploymentManifestBytes(self):
        """
        Gets the ClickOnce deployment manifest for the current application.

        Get: DeploymentManifestBytes(self: ActivationContext) -> Array[Byte]
        """
        ...

    @property
    def Form(self):
        """
        Gets the form, or store context, for the current application.

        Get: Form(self: ActivationContext) -> ContextForm
        """
        ...

    @property
    def Identity(self):
        """
        Gets the application identity for the current application.

        Get: Identity(self: ActivationContext) -> ApplicationIdentity
        """
        ...


    def ContextForm(self, *args): #cannot find CLR method
        """ enum ContextForm, values: Loose (0), StoreBounded (1) """
        ...

    @staticmethod
    def CreatePartialActivationContext(identity, manifestPaths=...):
        """
        CreatePartialActivationContext(identity: ApplicationIdentity) -> ActivationContext

            Initializes a new instance of the System.ActivationContext class using the specified application identity.

            identity: An object that identifies an application.

            Returns: An object with the specified application identity.

        CreatePartialActivationContext(identity: ApplicationIdentity, manifestPaths: Array[str]) -> ActivationContext

            Initializes a new instance of the System.ActivationContext class using the specified application identity and array of manifest paths.

            identity: An object that identifies an application.

            manifestPaths: A string array of manifest paths for the application.

            Returns: An object with the specified application identity and array of manifest paths.
        """
        ...


class Activator(_Activator):
    """ Contains methods to create types of objects locally or remotely, or obtain references to existing remote objects. This class cannot be inherited. """
    @staticmethod
    def CreateComInstanceFrom(assemblyName, typeName, hashValue=..., hashAlgorithm=...):
        """
        CreateComInstanceFrom(assemblyName: str, typeName: str) -> ObjectHandle

            Creates an instance of the COM object whose name is specified, using the named assembly file and the default constructor.

            assemblyName: The name of a file that contains an assembly where the type named typeName is sought.

            typeName: The name of the preferred type.

            Returns: A handle that must be unwrapped to access the newly created instance.

        CreateComInstanceFrom(assemblyName: str, typeName: str, hashValue: Array[Byte], hashAlgorithm: AssemblyHashAlgorithm) -> ObjectHandle

            Creates an instance of the COM object whose name is specified, using the named assembly file and the default constructor.

            assemblyName: The name of a file that contains an assembly where the type named typeName is sought.

            typeName: The name of the preferred type.

            hashValue: The value of the computed hash code.

            hashAlgorithm: The hash algorithm used for hashing files and generating the strong name.

            Returns: A handle that must be unwrapped to access the newly created instance.
        """
        ...

    @staticmethod
    def CreateInstance(*__args):
        """
        CreateInstance(type: Type, bindingAttr: BindingFlags, binder: Binder, args: Array[object], culture: CultureInfo) -> object

            Creates an instance of the specified type using the constructor that best matches the specified parameters.

            type: The type of object to create.

            bindingAttr: A combination of zero or more bit flags that affect the search for the type constructor. If bindingAttr is zero, a case-sensitive search for public

             constructors is conducted.

            binder: An object that uses bindingAttr and args to seek and identify the type constructor. If binder is ll, the default binder is used.

            args: An array of arguments that match in number, order, and type the parameters of the constructor to invoke. If args is an empty array or ll, the

             constructor that takes no parameters (the default constructor) is invoked.

            culture: Culture-specific information that governs the coercion of args to the formal types declared for the type constructor. If culture is ll, the

             System.Globalization.CultureInfo for the current thread is used.

            Returns: A reference to the newly created object.

        CreateInstance(type: Type, bindingAttr: BindingFlags, binder: Binder, args: Array[object], culture: CultureInfo, activationAttributes: Array[object]) -> object

            Creates an instance of the specified type using the constructor that best matches the specified parameters.

            type: The type of object to create.

            bindingAttr: A combination of zero or more bit flags that affect the search for the type constructor. If bindingAttr is zero, a case-sensitive search for public

             constructors is conducted.

            binder: An object that uses bindingAttr and args to seek and identify the type constructor. If binder is ll, the default binder is used.

            args: An array of arguments that match in number, order, and type the parameters of the constructor to invoke. If args is an empty array or ll, the

             constructor that takes no parameters (the default constructor) is invoked.

            culture: Culture-specific information that governs the coercion of args to the formal types declared for the type constructor. If culture is ll, the

             System.Globalization.CultureInfo for the current thread is used.

            activationAttributes: An array of one or more attributes that can participate in activation. This is typically an array that contains a single

             System.Runtime.Remoting.Activation.UrlAttribute object that specifies the URL that is required to activate a remote object. This parameter is related

             to client-activated objects. Client activation is a legacy technology that is retained for backward compatibility but is not recommended for new

             development. Distributed applications should instead use Windows Communication Foundation.

            Returns: A reference to the newly created object.

        CreateInstance(type: Type, *args: Array[object]) -> object

            Creates an instance of the specified type using the constructor that best matches the specified parameters.

            type: The type of object to create.

            args: An array of arguments that match in number, order, and type the parameters of the constructor to invoke. If args is an empty array or ll, the

             constructor that takes no parameters (the default constructor) is invoked.

            Returns: A reference to the newly created object.

        CreateInstance(type: Type, args: Array[object], activationAttributes: Array[object]) -> object

            Creates an instance of the specified type using the constructor that best matches the specified parameters.

            type: The type of object to create.

            args: An array of arguments that match in number, order, and type the parameters of the constructor to invoke. If args is an empty array or ll, the

             constructor that takes no parameters (the default constructor) is invoked.

            activationAttributes: An array of one or more attributes that can participate in activation. This is typically an array that contains a single

             System.Runtime.Remoting.Activation.UrlAttribute object that specifies the URL that is required to activate a remote object. This parameter is related

             to client-activated objects. Client activation is a legacy technology that is retained for backward compatibility but is not recommended for new

             development. Distributed applications should instead use Windows Communication Foundation.

            Returns: A reference to the newly created object.

        CreateInstance(type: Type) -> object

            Creates an instance of the specified type using that type's default constructor.

            type: The type of object to create.

            Returns: A reference to the newly created object.

        CreateInstance(assemblyName: str, typeName: str) -> ObjectHandle

            Creates an instance of the type whose name is specified, using the named assembly and default constructor.

            assemblyName: The name of the assembly where the type named typeName is sought. For more information, see the Remarks section. If assemblyName is ll, the executing

             assembly is searched.

            typeName: The fully qualified name of the preferred type.

            Returns: A handle that must be unwrapped to access the newly created instance.

        CreateInstance(assemblyName: str, typeName: str, activationAttributes: Array[object]) -> ObjectHandle

            Creates an instance of the type whose name is specified, using the named assembly and default constructor.

            assemblyName: The name of the assembly where the type named typeName is sought. If assemblyName is ll, the executing assembly is searched.

            typeName: The fully qualified name of the preferred type.

            activationAttributes: An array of one or more attributes that can participate in activation. This is typically an array that contains a single

             System.Runtime.Remoting.Activation.UrlAttribute object that specifies the URL that is required to activate a remote object. This parameter is related

             to client-activated objects. Client activation is a legacy technology that is retained for backward compatibility but is not recommended for new

             development. Distributed applications should instead use Windows Communication Foundation.

            Returns: A handle that must be unwrapped to access the newly created instance.

        CreateInstance(type: Type, nonPublic: bool) -> object

            Creates an instance of the specified type using that type's default constructor.

            type: The type of object to create.

            nonPublic: ue if a public or nonpublic default constructor can match; lse if only a public default constructor can match.

            Returns: A reference to the newly created object.

        CreateInstance(assemblyName: str, typeName: str, ignoreCase: bool, bindingAttr: BindingFlags, binder: Binder, args: Array[object], culture: CultureInfo, activationAttributes: Array[object], securityInfo: Evidence) -> ObjectHandle

            Creates an instance of the type whose name is specified, using the named assembly and the constructor that best matches the specified parameters.

            assemblyName: The name of the assembly where the type named typeName is sought. If assemblyName is ll, the executing assembly is searched.

            typeName: The fully qualified name of the preferred type.

            ignoreCase: ue to specify that the search for typeName is not case-sensitive; lse to specify that the search is case-sensitive.

            bindingAttr: A combination of zero or more bit flags that affect the search for the typeName constructor. If bindingAttr is zero, a case-sensitive search for

             public constructors is conducted.

            binder: An object that uses bindingAttr and args to seek and identify the typeName constructor. If binder is ll, the default binder is used.

            args: An array of arguments that match in number, order, and type the parameters of the constructor to invoke. If args is an empty array or ll, the

             constructor that takes no parameters (the default constructor) is invoked.

            culture: Culture-specific information that governs the coercion of args to the formal types declared for the typeName constructor. If culture is ll, the

             System.Globalization.CultureInfo for the current thread is used.

            activationAttributes: An array of one or more attributes that can participate in activation. This is typically an array that contains a single

             System.Runtime.Remoting.Activation.UrlAttribute object that specifies the URL that is required to activate a remote object. This parameter is related

             to client-activated objects. Client activation is a legacy technology that is retained for backward compatibility but is not recommended for new

             development. Distributed applications should instead use Windows Communication Foundation.

            securityInfo: Information used to make security policy decisions and grant code permissions.

            Returns: A handle that must be unwrapped to access the newly created instance.

        CreateInstance(assemblyName: str, typeName: str, ignoreCase: bool, bindingAttr: BindingFlags, binder: Binder, args: Array[object], culture: CultureInfo, activationAttributes: Array[object]) -> ObjectHandle

            Creates an instance of the type whose name is specified, using the named assembly and the constructor that best matches the specified parameters.

            assemblyName: The name of the assembly where the type named typeName is sought. If assemblyName is ll, the executing assembly is searched.

            typeName: The fully qualified name of the preferred type.

            ignoreCase: ue to specify that the search for typeName is not case-sensitive; lse to specify that the search is case-sensitive.

            bindingAttr: A combination of zero or more bit flags that affect the search for the typeName constructor. If bindingAttr is zero, a case-sensitive search for

             public constructors is conducted.

            binder: An object that uses bindingAttr and args to seek and identify the typeName constructor. If binder is ll, the default binder is used.

            args: An array of arguments that match in number, order, and type the parameters of the constructor to invoke. If args is an empty array or ll, the

             constructor that takes no parameters (the default constructor) is invoked.

            culture: Culture-specific information that governs the coercion of args to the formal types declared for the typeName constructor. If culture is ll, the

             System.Globalization.CultureInfo for the current thread is used.

            activationAttributes: An array of one or more attributes that can participate in activation. This is typically an array that contains a single

             System.Runtime.Remoting.Activation.UrlAttribute object that specifies the URL that is required to activate a remote object. This parameter is related

             to client-activated objects. Client activation is a legacy technology that is retained for backward compatibility but is not recommended for new

             development. Distributed applications should instead use Windows Communication Foundation.

            Returns: A handle that must be unwrapped to access the newly created instance.

        CreateInstance(domain: AppDomain, assemblyName: str, typeName: str) -> ObjectHandle

            Creates an instance of the type whose name is specified in the specified remote domain, using the named assembly and default constructor.

            domain: The remote domain where the type named typeName is created.

            assemblyName: The name of the assembly where the type named typeName is sought. If assemblyName is ll, the executing assembly is searched.

            typeName: The fully qualified name of the preferred type.

            Returns: A handle that must be unwrapped to access the newly created instance.

        CreateInstance(domain: AppDomain, assemblyName: str, typeName: str, ignoreCase: bool, bindingAttr: BindingFlags, binder: Binder, args: Array[object], culture: CultureInfo, activationAttributes: Array[object], securityAttributes: Evidence) -> ObjectHandle

            Creates an instance of the type whose name is specified in the specified remote domain, using the named assembly and the constructor that best

             matches the specified parameters.

            domain: The domain where the type named typeName is created.

            assemblyName: The name of the assembly where the type named typeName is sought. If assemblyName is ll, the executing assembly is searched.

            typeName: The fully qualified name of the preferred type.

            ignoreCase: ue to specify that the search for typeName is not case-sensitive; lse to specify that the search is case-sensitive.

            bindingAttr: A combination of zero or more bit flags that affect the search for the typeName constructor. If bindingAttr is zero, a case-sensitive search for

             public constructors is conducted.

            binder: An object that uses bindingAttr and args to seek and identify the typeName constructor. If binder is ll, the default binder is used.

            args: An array of arguments that match in number, order, and type the parameters of the constructor to invoke. If args is an empty array or ll, the

             constructor that takes no parameters (the default constructor) is invoked.

            culture: Culture-specific information that governs the coercion of args to the formal types declared for the typeName constructor. If culture is ll, the

             System.Globalization.CultureInfo for the current thread is used.

            activationAttributes: An array of one or more attributes that can participate in activation. This is typically an array that contains a single

             System.Runtime.Remoting.Activation.UrlAttribute object. The System.Runtime.Remoting.Activation.UrlAttribute specifies the URL that is required to

             activate a remote object.

            securityAttributes: Information used to make security policy decisions and grant code permissions.

            Returns: A handle that must be unwrapped to access the newly created instance.

        CreateInstance(domain: AppDomain, assemblyName: str, typeName: str, ignoreCase: bool, bindingAttr: BindingFlags, binder: Binder, args: Array[object], culture: CultureInfo, activationAttributes: Array[object]) -> ObjectHandle

            Creates an instance of the type whose name is specified in the specified remote domain, using the named assembly and the constructor that best

             matches the specified parameters.

            domain: The domain where the type named typeName is created.

            assemblyName: The name of the assembly where the type named typeName is sought. If assemblyName is ll, the executing assembly is searched.

            typeName: The fully qualified name of the preferred type.

            ignoreCase: ue to specify that the search for typeName is not case-sensitive; lse to specify that the search is case-sensitive.

            bindingAttr: A combination of zero or more bit flags that affect the search for the typeName constructor. If bindingAttr is zero, a case-sensitive search for

             public constructors is conducted.

            binder: An object that uses bindingAttr and args to seek and identify the typeName constructor. If binder is ll, the default binder is used.

            args: An array of arguments that match in number, order, and type the parameters of the constructor to invoke. If args is an empty array or ll, the

             constructor that takes no parameters (the default constructor) is invoked.

            culture: Culture-specific information that governs the coercion of args to the formal types declared for the typeName constructor. If culture is ll, the

             System.Globalization.CultureInfo for the current thread is used.

            activationAttributes: An array of one or more attributes that can participate in activation. This is typically an array that contains a single

             System.Runtime.Remoting.Activation.UrlAttribute object that specifies the URL that is required to activate a remote object. This parameter is related

             to client-activated objects. Client activation is a legacy technology that is retained for backward compatibility but is not recommended for new

             development. Distributed applications should instead use Windows Communication Foundation.

            Returns: A handle that must be unwrapped to access the newly created instance.

        CreateInstance(activationContext: ActivationContext) -> ObjectHandle

            Creates an instance of the type designated by the specified System.ActivationContext object.

            activationContext: An activation context object that specifies the object to create.

            Returns: A handle that must be unwrapped to access the newly created object.

        CreateInstance(activationContext: ActivationContext, activationCustomData: Array[str]) -> ObjectHandle

            Creates an instance of the type that is designated by the specified System.ActivationContext object and activated with the specified custom

             activation data.

            activationContext: An activation context object that specifies the object to create.

            activationCustomData: An array of Unicode strings that contain custom activation data.

            Returns: A handle that must be unwrapped to access the newly created object.

        CreateInstance[T]() -> T
        """
        ...

    @staticmethod
    def CreateInstanceFrom(*__args):
        """
        CreateInstanceFrom(assemblyFile: str, typeName: str) -> ObjectHandle

            Creates an instance of the type whose name is specified, using the named assembly file and default constructor.

            assemblyFile: The name of a file that contains an assembly where the type named typeName is sought.

            typeName: The name of the preferred type.

            Returns: A handle that must be unwrapped to access the newly created instance.

        CreateInstanceFrom(assemblyFile: str, typeName: str, activationAttributes: Array[object]) -> ObjectHandle

            Creates an instance of the type whose name is specified, using the named assembly file and default constructor.

            assemblyFile: The name of a file that contains an assembly where the type named typeName is sought.

            typeName: The name of the preferred type.

            activationAttributes: An array of one or more attributes that can participate in activation. This is typically an array that contains a single

             System.Runtime.Remoting.Activation.UrlAttribute object that specifies the URL that is required to activate a remote object. This parameter is related

             to client-activated objects. Client activation is a legacy technology that is retained for backward compatibility but is not recommended for new

             development. Distributed applications should instead use Windows Communication Foundation.

            Returns: A handle that must be unwrapped to access the newly created instance.

        CreateInstanceFrom(assemblyFile: str, typeName: str, ignoreCase: bool, bindingAttr: BindingFlags, binder: Binder, args: Array[object], culture: CultureInfo, activationAttributes: Array[object], securityInfo: Evidence) -> ObjectHandle

            Creates an instance of the type whose name is specified, using the named assembly file and the constructor that best matches the specified parameters.

            assemblyFile: The name of a file that contains an assembly where the type named typeName is sought.

            typeName: The name of the preferred type.

            ignoreCase: ue to specify that the search for typeName is not case-sensitive; lse to specify that the search is case-sensitive.

            bindingAttr: A combination of zero or more bit flags that affect the search for the typeName constructor. If bindingAttr is zero, a case-sensitive search for

             public constructors is conducted.

            binder: An object that uses bindingAttr and args to seek and identify the typeName constructor. If binder is ll, the default binder is used.

            args: An array of arguments that match in number, order, and type the parameters of the constructor to invoke. If args is an empty array or ll, the

             constructor that takes no parameters (the default constructor) is invoked.

            culture: Culture-specific information that governs the coercion of args to the formal types declared for the typeName constructor. If culture is ll, the

             System.Globalization.CultureInfo for the current thread is used.

            activationAttributes: An array of one or more attributes that can participate in activation. This is typically an array that contains a single

             System.Runtime.Remoting.Activation.UrlAttribute object that specifies the URL that is required to activate a remote object. This parameter is related

             to client-activated objects. Client activation is a legacy technology that is retained for backward compatibility but is not recommended for new

             development. Distributed applications should instead use Windows Communication Foundation.

            securityInfo: Information used to make security policy decisions and grant code permissions.

            Returns: A handle that must be unwrapped to access the newly created instance.

        CreateInstanceFrom(assemblyFile: str, typeName: str, ignoreCase: bool, bindingAttr: BindingFlags, binder: Binder, args: Array[object], culture: CultureInfo, activationAttributes: Array[object]) -> ObjectHandle

            Creates an instance of the type whose name is specified, using the named assembly file and the constructor that best matches the specified parameters.

            assemblyFile: The name of a file that contains an assembly where the type named typeName is sought.

            typeName: The name of the preferred type.

            ignoreCase: ue to specify that the search for typeName is not case-sensitive; lse to specify that the search is case-sensitive.

            bindingAttr: A combination of zero or more bit flags that affect the search for the typeName constructor. If bindingAttr is zero, a case-sensitive search for

             public constructors is conducted.

            binder: An object that uses bindingAttr and args to seek and identify the typeName constructor. If binder is ll, the default binder is used.

            args: An array of arguments that match in number, order, and type the parameters of the constructor to invoke. If args is an empty array or ll, the

             constructor that takes no parameters (the default constructor) is invoked.

            culture: Culture-specific information that governs the coercion of args to the formal types declared for the typeName constructor. If culture is ll, the

             System.Globalization.CultureInfo for the current thread is used.

            activationAttributes: An array of one or more attributes that can participate in activation. This is typically an array that contains a single

             System.Runtime.Remoting.Activation.UrlAttribute object that specifies the URL that is required to activate a remote object. This parameter is related

             to client-activated objects. Client activation is a legacy technology that is retained for backward compatibility but is not recommended for new

             development. Distributed applications should instead use Windows Communication Foundation.

            Returns: A handle that must be unwrapped to access the newly created instance.

        CreateInstanceFrom(domain: AppDomain, assemblyFile: str, typeName: str) -> ObjectHandle

            Creates an instance of the type whose name is specified in the specified remote domain, using the named assembly file and default constructor.

            domain: The remote domain where the type named typeName is created.

            assemblyFile: The name of a file that contains an assembly where the type named typeName is sought.

            typeName: The name of the preferred type.

            Returns: A handle that must be unwrapped to access the newly created instance.

        CreateInstanceFrom(domain: AppDomain, assemblyFile: str, typeName: str, ignoreCase: bool, bindingAttr: BindingFlags, binder: Binder, args: Array[object], culture: CultureInfo, activationAttributes: Array[object], securityAttributes: Evidence) -> ObjectHandle

            Creates an instance of the type whose name is specified in the specified remote domain, using the named assembly file and the constructor that best

             matches the specified parameters.

            domain: The remote domain where the type named typeName is created.

            assemblyFile: The name of a file that contains an assembly where the type named typeName is sought.

            typeName: The name of the preferred type.

            ignoreCase: ue to specify that the search for typeName is not case-sensitive; lse to specify that the search is case-sensitive.

            bindingAttr: A combination of zero or more bit flags that affect the search for the typeName constructor. If bindingAttr is zero, a case-sensitive search for

             public constructors is conducted.

            binder: An object that uses bindingAttr and args to seek and identify the typeName constructor. If binder is ll, the default binder is used.

            args: An array of arguments that match in number, order, and type the parameters of the constructor to invoke. If args is an empty array or ll, the

             constructor that takes no parameters (the default constructor) is invoked.

            culture: Culture-specific information that governs the coercion of args to the formal types declared for the typeName constructor. If culture is ll, the

             System.Globalization.CultureInfo for the current thread is used.

            activationAttributes: An array of one or more attributes that can participate in activation. This is typically an array that contains a single

             System.Runtime.Remoting.Activation.UrlAttribute object that specifies the URL that is required to activate a remote object. This parameter is related

             to client-activated objects. Client activation is a legacy technology that is retained for backward compatibility but is not recommended for new

             development. Distributed applications should instead use Windows Communication Foundation.

            securityAttributes: Information used to make security policy decisions and grant code permissions.

            Returns: A handle that must be unwrapped to access the newly created instance.

        CreateInstanceFrom(domain: AppDomain, assemblyFile: str, typeName: str, ignoreCase: bool, bindingAttr: BindingFlags, binder: Binder, args: Array[object], culture: CultureInfo, activationAttributes: Array[object]) -> ObjectHandle

            Creates an instance of the type whose name is specified in the specified remote domain, using the named assembly file and the constructor that best

             matches the specified parameters.

            domain: The remote domain where the type named typeName is created.

            assemblyFile: The name of a file that contains an assembly where the type named typeName is sought.

            typeName: The name of the preferred type.

            ignoreCase: ue to specify that the search for typeName is not case-sensitive; lse to specify that the search is case-sensitive.

            bindingAttr: A combination of zero or more bit flags that affect the search for the typeName constructor. If bindingAttr is zero, a case-sensitive search for

             public constructors is conducted.

            binder: An object that uses bindingAttr and args to seek and identify the typeName constructor. If binder is ll, the default binder is used.

            args: An array of arguments that match in number, order, and type the parameters of the constructor to invoke. If args is an empty array or ll, the

             constructor that takes no parameters (the default constructor) is invoked.

            culture: Culture-specific information that governs the coercion of args to the formal types declared for the typeName constructor. If culture is ll, the

             System.Globalization.CultureInfo for the current thread is used.

            activationAttributes: An array of one or more attributes that can participate in activation. This is typically an array that contains a single

             System.Runtime.Remoting.Activation.UrlAttribute object that specifies the URL that is required to activate a remote object. This parameter is related

             to client-activated objects. Client activation is a legacy technology that is retained for backward compatibility but is not recommended for new

             development. Distributed applications should instead use Windows Communication Foundation.

            Returns: A handle that must be unwrapped to access the newly created instance.
        """
        ...

    @staticmethod
    def GetObject(type, url, state=...):
        """
        GetObject(type: Type, url: str) -> object

            Creates a proxy for the well-known object indicated by the specified type and URL.

            type: The type of the well-known object to which you want to connect.

            url: The URL of the well-known object.

            Returns: A proxy that points to an endpoint served by the requested well-known object.

        GetObject(type: Type, url: str, state: object) -> object

            Creates a proxy for the well-known object indicated by the specified type, URL, and channel data.

            type: The type of the well-known object to which you want to connect.

            url: The URL of the well-known object.

            state: Channel-specific data or ll.

            Returns: A proxy that points to an endpoint served by the requested well-known object.
        """
        ...


class AggregateException(Exception): # skipped bases: <type 'ISerializable'>, <type '_Exception'>
    """
    Represents one or more errors that occur during application execution.

    AggregateException()

    AggregateException(message: str)

    AggregateException(message: str, innerException: Exception)

    AggregateException(innerExceptions: IEnumerable[Exception])

    AggregateException(*innerExceptions: Array[Exception])

    AggregateException(message: str, innerExceptions: IEnumerable[Exception])

    AggregateException(message: str, *innerExceptions: Array[Exception])
    """
    @property
    def InnerExceptions(self):
        """
        Gets a read-only collection of the System.Exception instances that caused the current exception.

        Get: InnerExceptions(self: AggregateException) -> ReadOnlyCollection[Exception]
        """
        ...


    def Flatten(self):
        """
        Flatten(self: AggregateException) -> AggregateException

            Flattens an System.AggregateException instances into a single, new instance.

            Returns: A new, flattened System.AggregateException.
        """
        ...

    def Handle(self, predicate):
        """ Handle(self: AggregateException, predicate: Func[Exception, bool]) """
        ...

    SerializeObjectState = None


class AppContext: # skipped bases: <type 'object'>
    """ Provides members for setting and retrieving data about an application's context. """
    @property
    def BaseDirectory(self):
        """
        Gets the pathname of the base directory that the assembly resolver uses to probe for assemblies.

        Get: BaseDirectory() -> str
        """
        ...

    @property
    def TargetFrameworkName(self):
        """
        Gets the name of the framework version targeted by the current application.

        Get: TargetFrameworkName() -> str
        """
        ...


    @staticmethod
    def GetData(name):
        """
        GetData(name: str) -> object

            Returns the value of the named data element assigned to the current application domain.

            name: The name of the data element.

            Returns: The value of name, if name identifies a named value; otherwise, ll.
        """
        ...

    @staticmethod
    def SetSwitch(switchName, isEnabled):
        """
        SetSwitch(switchName: str, isEnabled: bool)

            Sets the value of a switch.

            switchName: The name of the switch.

            isEnabled: The value of the switch.
        """
        ...

    @staticmethod
    def TryGetSwitch(switchName, isEnabled):
        """
        TryGetSwitch(switchName: str) -> (bool, bool)

            Tries to get the value of a switch.

            switchName: The name of the switch.

            Returns: ue if switchName was set and the isEnabled argument contains the value of the switch; otherwise, lse.
        """
        ...

    __all__ = [
        'GetData',
        'SetSwitch',
        'TryGetSwitch',
    ]


class MarshalByRefObject: # skipped bases: <type 'object'>
    """ Enables access to objects across application domain boundaries in applications that support remoting. """
    def CreateObjRef(self, requestedType):
        """
        CreateObjRef(self: MarshalByRefObject, requestedType: Type) -> ObjRef

            Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object.

            requestedType: The System.Type of the object that the new System.Runtime.Remoting.ObjRef will reference.

            Returns: Information required to generate a proxy.
        """
        ...

    def GetLifetimeService(self):
        """
        GetLifetimeService(self: MarshalByRefObject) -> object

            Retrieves the current lifetime service object that controls the lifetime policy for this instance.

            Returns: An object of type System.Runtime.Remoting.Lifetime.ILease used to control the lifetime policy for this instance.
        """
        ...

    def InitializeLifetimeService(self):
        """
        InitializeLifetimeService(self: MarshalByRefObject) -> object

            Obtains a lifetime service object to control the lifetime policy for this instance.

            Returns: An object of type System.Runtime.Remoting.Lifetime.ILease used to control the lifetime policy for this instance. This is the current lifetime service

             object for this instance if one exists; otherwise, a new lifetime service object initialized to the value of the

             System.Runtime.Remoting.Lifetime.LifetimeServices.LeaseManagerPollTime property.
        """
        ...


class _AppDomain:
    """ Exposes the public members of the System.AppDomain class to unmanaged code. """
    @property
    def BaseDirectory(self):
        """
        Provides COM objects with version-independent access to the System.AppDomain.BaseDirectory property.

        Get: BaseDirectory(self: _AppDomain) -> str
        """
        ...

    @property
    def DynamicDirectory(self):
        """
        Provides COM objects with version-independent access to the System.AppDomain.DynamicDirectory property.

        Get: DynamicDirectory(self: _AppDomain) -> str
        """
        ...

    @property
    def Evidence(self):
        """
        Provides COM objects with version-independent access to the System.AppDomain.Evidence property.

        Get: Evidence(self: _AppDomain) -> Evidence
        """
        ...

    @property
    def FriendlyName(self):
        """
        Provides COM objects with version-independent access to the System.AppDomain.FriendlyName property.

        Get: FriendlyName(self: _AppDomain) -> str
        """
        ...

    @property
    def RelativeSearchPath(self):
        """
        Provides COM objects with version-independent access to the System.AppDomain.RelativeSearchPath property.

        Get: RelativeSearchPath(self: _AppDomain) -> str
        """
        ...

    @property
    def ShadowCopyFiles(self):
        """
        Provides COM objects with version-independent access to the System.AppDomain.ShadowCopyFiles property.

        Get: ShadowCopyFiles(self: _AppDomain) -> bool
        """
        ...


    def AppendPrivatePath(self, path):
        """
        AppendPrivatePath(self: _AppDomain, path: str)

            Provides COM objects with version-independent access to the System.AppDomain.AppendPrivatePath(System.String) method.

            path: The name of the directory to be appended to the private path.
        """
        ...

    def ClearPrivatePath(self):
        """
        ClearPrivatePath(self: _AppDomain)

            Provides COM objects with version-independent access to the System.AppDomain.ClearPrivatePath method.
        """
        ...

    def ClearShadowCopyPath(self):
        """
        ClearShadowCopyPath(self: _AppDomain)

            Provides COM objects with version-independent access to the System.AppDomain.ClearShadowCopyPath method.
        """
        ...

    def CreateInstance(self, assemblyName, typeName, *__args):
        """
        CreateInstance(self: _AppDomain, assemblyName: str, typeName: str) -> ObjectHandle

            Provides COM objects with version-independent access to the System.AppDomain.CreateInstance(System.String,System.String) method.

            assemblyName: The display name of the assembly. See System.Reflection.Assembly.FullName.

            typeName: The fully qualified name of the requested type, including the namespace but not the assembly, as returned by the System.Type.FullName property.

            Returns: An object that is a wrapper for the new instance specified by typeName. The return value needs to be unwrapped to access the real object.

        CreateInstance(self: _AppDomain, assemblyName: str, typeName: str, activationAttributes: Array[object]) -> ObjectHandle

            Provides COM objects with version-independent access to the System.AppDomain.CreateInstance(System.String,System.String,System.Object[]) method

             overload.

            assemblyName: The display name of the assembly. See System.Reflection.Assembly.FullName.

            typeName: The fully qualified name of the requested type, including the namespace but not the assembly, as returned by the System.Type.FullName property.

            activationAttributes: An array of one or more attributes that can participate in activation. Typically, an array that contains a single

             System.Runtime.Remoting.Activation.UrlAttribute object. The System.Runtime.Remoting.Activation.UrlAttribute specifies the URL that is required to

             activate a remote object.

            Returns: An object that is a wrapper for the new instance specified by typeName. The return value needs to be unwrapped to access the real object.

        CreateInstance(self: _AppDomain, assemblyName: str, typeName: str, ignoreCase: bool, bindingAttr: BindingFlags, binder: Binder, args: Array[object], culture: CultureInfo, activationAttributes: Array[object], securityAttributes: Evidence) -> ObjectHandle

            Provides COM objects with version-independent access to the

             System.AppDomain.CreateInstance(System.String,System.String,System.Boolean,System.Reflection.BindingFlags,System.Reflection.Binder,System.Object[],Sys

             tem.Globalization.CultureInfo,System.Object[],System.Security.Policy.Evidence) method overload.

            assemblyName: The display name of the assembly. See System.Reflection.Assembly.FullName.

            typeName: The fully qualified name of the requested type, including the namespace but not the assembly, as returned by the System.Type.FullName property.

            ignoreCase: A Boolean value specifying whether to perform a case-sensitive search or not.

            bindingAttr: A combination of zero or more bit flags that affect the search for the typeName constructor. If bindingAttr is zero, a case-sensitive search for

             public constructors is conducted.

            binder: An object that enables the binding, coercion of argument types, invocation of members, and retrieval of System.Reflection.MemberInfo objects using

             reflection. If binder is null, the default binder is used.

            args: The arguments to pass to the constructor. This array of arguments must match in number, order, and type the parameters of the constructor to invoke.

             If the default constructor is preferred, args must be an empty array or null.

            culture: Culture-specific information that governs the coercion of args to the formal types declared for the typeName constructor. If culture is ll, the

             System.Globalization.CultureInfo for the current thread is used.

            activationAttributes: An array of one or more attributes that can participate in activation. Typically, an array that contains a single

             System.Runtime.Remoting.Activation.UrlAttribute object. The System.Runtime.Remoting.Activation.UrlAttribute specifies the URL that is required to

             activate a remote object.

            securityAttributes: Information used to authorize creation of typeName.

            Returns: An object that is a wrapper for the new instance specified by typeName. The return value needs to be unwrapped to access the real object.
        """
        ...

    def CreateInstanceFrom(self, assemblyFile, typeName, *__args):
        """
        CreateInstanceFrom(self: _AppDomain, assemblyFile: str, typeName: str) -> ObjectHandle

            Provides COM objects with version-independent access to the System.AppDomain.CreateInstanceFrom(System.String,System.String) method overload.

            assemblyFile: The name, including the path, of a file that contains an assembly that defines the requested type. The assembly is loaded using the

             System.Reflection.Assembly.LoadFrom(System.String)  method.

            typeName: The fully qualified name of the requested type, including the namespace but not the assembly, as returned by the System.Type.FullName property.

            Returns: An object that is a wrapper for the new instance, or ll if typeName is not found. The return value needs to be unwrapped to access the real object.

        CreateInstanceFrom(self: _AppDomain, assemblyFile: str, typeName: str, activationAttributes: Array[object]) -> ObjectHandle

            Provides COM objects with version-independent access to the System.AppDomain.CreateInstanceFrom(System.String,System.String,System.Object[]) method

             overload.

            assemblyFile: The name, including the path, of a file that contains an assembly that defines the requested type. The assembly is loaded using the

             System.Reflection.Assembly.LoadFrom(System.String)  method.

            typeName: The fully qualified name of the requested type, including the namespace but not the assembly, as returned by the System.Type.FullName property.

            activationAttributes: An array of one or more attributes that can participate in activation. Typically, an array that contains a single

             System.Runtime.Remoting.Activation.UrlAttribute object. The System.Runtime.Remoting.Activation.UrlAttribute specifies the URL that is required to

             activate a remote object.

            Returns: An object that is a wrapper for the new instance, or ll if typeName is not found. The return value needs to be unwrapped to access the real object.

        CreateInstanceFrom(self: _AppDomain, assemblyFile: str, typeName: str, ignoreCase: bool, bindingAttr: BindingFlags, binder: Binder, args: Array[object], culture: CultureInfo, activationAttributes: Array[object], securityAttributes: Evidence) -> ObjectHandle

            Provides COM objects with version-independent access to the

             System.AppDomain.CreateInstanceFrom(System.String,System.String,System.Boolean,System.Reflection.BindingFlags,System.Reflection.Binder,System.Object[]

             ,System.Globalization.CultureInfo,System.Object[],System.Security.Policy.Evidence) method overload.

            assemblyFile: The name, including the path, of a file that contains an assembly that defines the requested type. The assembly is loaded using the

             System.Reflection.Assembly.LoadFrom(System.String)  method.

            typeName: The fully qualified name of the requested type, including the namespace but not the assembly, as returned by the System.Type.FullName property.

            ignoreCase: A Boolean value specifying whether to perform a case-sensitive search or not.

            bindingAttr: A combination of zero or more bit flags that affect the search for the typeName constructor. If bindingAttr is zero, a case-sensitive search for

             public constructors is conducted.

            binder: An object that enables the binding, coercion of argument types, invocation of members, and retrieval of System.Reflection.MemberInfo objects through

             reflection. If binder is null, the default binder is used.

            args: The arguments to pass to the constructor. This array of arguments must match in number, order, and type the parameters of the constructor to invoke.

             If the default constructor is preferred, args must be an empty array or null.

            culture: Culture-specific information that governs the coercion of args to the formal types declared for the typeName constructor. If culture is ll, the

             System.Globalization.CultureInfo for the current thread is used.

            activationAttributes: An array of one or more attributes that can participate in activation. Typically, an array that contains a single

             System.Runtime.Remoting.Activation.UrlAttribute object. The System.Runtime.Remoting.Activation.UrlAttribute specifies the URL that is required to

             activate a remote object.

            securityAttributes: Information used to authorize creation of typeName.

            Returns: An object that is a wrapper for the new instance, or ll if typeName is not found. The return value needs to be unwrapped to access the real object.
        """
        ...

    def DefineDynamicAssembly(self, name, access, *__args):
        """
        DefineDynamicAssembly(self: _AppDomain, name: AssemblyName, access: AssemblyBuilderAccess) -> AssemblyBuilder

            Provides COM objects with version-independent access to the

             System.AppDomain.DefineDynamicAssembly(System.Reflection.AssemblyName,System.Reflection.Emit.AssemblyBuilderAccess) method overload.

            name: The unique identity of the dynamic assembly.

            access: The access mode for the dynamic assembly.

            Returns: Represents the dynamic assembly created.

        DefineDynamicAssembly(self: _AppDomain, name: AssemblyName, access: AssemblyBuilderAccess, dir: str) -> AssemblyBuilder

            Provides COM objects with version-independent access to the

             System.AppDomain.DefineDynamicAssembly(System.Reflection.AssemblyName,System.Reflection.Emit.AssemblyBuilderAccess,System.String) method overload.

            name: The unique identity of the dynamic assembly.

            access: The mode in which the dynamic assembly will be accessed.

            dir: The name of the directory where the assembly will be saved. If dir is ll, the directory defaults to the current directory.

            Returns: Represents the dynamic assembly created.

        DefineDynamicAssembly(self: _AppDomain, name: AssemblyName, access: AssemblyBuilderAccess, evidence: Evidence) -> AssemblyBuilder

            Provides COM objects with version-independent access to the

             System.AppDomain.DefineDynamicAssembly(System.Reflection.AssemblyName,System.Reflection.Emit.AssemblyBuilderAccess,System.Security.Policy.Evidence)

             method overload.

            name: The unique identity of the dynamic assembly.

            access: The mode in which the dynamic assembly will be accessed.

            evidence: The evidence supplied for the dynamic assembly. The evidence is used unaltered as the final set of evidence used for policy resolution.

            Returns: Represents the dynamic assembly created.

        DefineDynamicAssembly(self: _AppDomain, name: AssemblyName, access: AssemblyBuilderAccess, requiredPermissions: PermissionSet, optionalPermissions: PermissionSet, refusedPermissions: PermissionSet) -> AssemblyBuilder

            Provides COM objects with version-independent access to the

             System.AppDomain.DefineDynamicAssembly(System.Reflection.AssemblyName,System.Reflection.Emit.AssemblyBuilderAccess,System.Security.PermissionSet,Syste

             m.Security.PermissionSet,System.Security.PermissionSet) method overload.

            name: The unique identity of the dynamic assembly.

            access: The mode in which the dynamic assembly will be accessed.

            requiredPermissions: The required permissions request.

            optionalPermissions: The optional permissions request.

            refusedPermissions: The refused permissions request.

            Returns: Represents the dynamic assembly created.

        DefineDynamicAssembly(self: _AppDomain, name: AssemblyName, access: AssemblyBuilderAccess, dir: str, evidence: Evidence) -> AssemblyBuilder

            Provides COM objects with version-independent access to the

             System.AppDomain.DefineDynamicAssembly(System.Reflection.AssemblyName,System.Reflection.Emit.AssemblyBuilderAccess,System.String,System.Security.Polic

             y.Evidence) method overload.

            name: The unique identity of the dynamic assembly.

            access: The mode in which the dynamic assembly will be accessed.

            dir: The name of the directory where the assembly will be saved. If dir is ll, the directory defaults to the current directory.

            evidence: The evidence supplied for the dynamic assembly. The evidence is used unaltered as the final set of evidence used for policy resolution.

            Returns: Represents the dynamic assembly created.

        DefineDynamicAssembly(self: _AppDomain, name: AssemblyName, access: AssemblyBuilderAccess, dir: str, requiredPermissions: PermissionSet, optionalPermissions: PermissionSet, refusedPermissions: PermissionSet) -> AssemblyBuilder

            Provides COM objects with version-independent access to the

             System.AppDomain.DefineDynamicAssembly(System.Reflection.AssemblyName,System.Reflection.Emit.AssemblyBuilderAccess,System.String,System.Security.Permi

             ssionSet,System.Security.PermissionSet,System.Security.PermissionSet) method overload.

            name: The unique identity of the dynamic assembly.

            access: The mode in which the dynamic assembly will be accessed.

            dir: The name of the directory where the assembly will be saved. If dir is ll, the directory defaults to the current directory.

            requiredPermissions: The required permissions request.

            optionalPermissions: The optional permissions request.

            refusedPermissions: The refused permissions request.

            Returns: Represents the dynamic assembly created.

        DefineDynamicAssembly(self: _AppDomain, name: AssemblyName, access: AssemblyBuilderAccess, evidence: Evidence, requiredPermissions: PermissionSet, optionalPermissions: PermissionSet, refusedPermissions: PermissionSet) -> AssemblyBuilder

            Provides COM objects with version-independent access to the

             System.AppDomain.DefineDynamicAssembly(System.Reflection.AssemblyName,System.Reflection.Emit.AssemblyBuilderAccess,System.Security.Policy.Evidence,Sys

             tem.Security.PermissionSet,System.Security.PermissionSet,System.Security.PermissionSet) method overload.

            name: The unique identity of the dynamic assembly.

            access: The mode in which the dynamic assembly will be accessed.

            evidence: The evidence supplied for the dynamic assembly. The evidence is used unaltered as the final set of evidence used for policy resolution.

            requiredPermissions: The required permissions request.

            optionalPermissions: The optional permissions request.

            refusedPermissions: The refused permissions request.

            Returns: Represents the dynamic assembly created.

        DefineDynamicAssembly(self: _AppDomain, name: AssemblyName, access: AssemblyBuilderAccess, dir: str, evidence: Evidence, requiredPermissions: PermissionSet, optionalPermissions: PermissionSet, refusedPermissions: PermissionSet) -> AssemblyBuilder

            Provides COM objects with version-independent access to the

             System.AppDomain.DefineDynamicAssembly(System.Reflection.AssemblyName,System.Reflection.Emit.AssemblyBuilderAccess,System.String,System.Security.Polic

             y.Evidence,System.Security.PermissionSet,System.Security.PermissionSet,System.Security.PermissionSet) method overload.

            name: The unique identity of the dynamic assembly.

            access: The mode in which the dynamic assembly will be accessed.

            dir: The name of the directory where the assembly will be saved. If dir is ll, the directory defaults to the current directory.

            evidence: The evidence supplied for the dynamic assembly. The evidence is used unaltered as the final set of evidence used for policy resolution.

            requiredPermissions: The required permissions request.

            optionalPermissions: The optional permissions request.

            refusedPermissions: The refused permissions request.

            Returns: Represents the dynamic assembly created.

        DefineDynamicAssembly(self: _AppDomain, name: AssemblyName, access: AssemblyBuilderAccess, dir: str, evidence: Evidence, requiredPermissions: PermissionSet, optionalPermissions: PermissionSet, refusedPermissions: PermissionSet, isSynchronized: bool) -> AssemblyBuilder

            Provides COM objects with version-independent access to the

             System.AppDomain.DefineDynamicAssembly(System.Reflection.AssemblyName,System.Reflection.Emit.AssemblyBuilderAccess,System.String,System.Security.Polic

             y.Evidence,System.Security.PermissionSet,System.Security.PermissionSet,System.Security.PermissionSet,System.Boolean) method overload.

            name: The unique identity of the dynamic assembly.

            access: The mode in which the dynamic assembly will be accessed.

            dir: The name of the directory where the dynamic assembly will be saved. If dir is ll, the directory defaults to the current directory.

            evidence: The evidence supplied for the dynamic assembly. The evidence is used unaltered as the final set of evidence used for policy resolution.

            requiredPermissions: The required permissions request.

            optionalPermissions: The optional permissions request.

            refusedPermissions: The refused permissions request.

            isSynchronized: ue to synchronize the creation of modules, types, and members in the dynamic assembly; otherwise, lse.

            Returns: Represents the dynamic assembly created.
        """
        ...

    def DoCallBack(self, theDelegate):
        """
        DoCallBack(self: _AppDomain, theDelegate: CrossAppDomainDelegate)

            Provides COM objects with version-independent access to the System.AppDomain.DoCallBack(System.CrossAppDomainDelegate) method.

            theDelegate: A delegate that specifies a method to call.
        """
        ...

    def Equals(self, other):
        """
        Equals(self: _AppDomain, other: object) -> bool

            Provides COM objects with version-independent access to the inherited System.Object.Equals(System.Object) method.

            other: The System.Object to compare to the current System.Object.

            Returns: ue if the specified System.Object is equal to the current System.Object; otherwise, lse.
        """
        ...

    def ExecuteAssembly(self, assemblyFile, assemblySecurity=..., args=...):
        """
        ExecuteAssembly(self: _AppDomain, assemblyFile: str, assemblySecurity: Evidence) -> int

            Provides COM objects with version-independent access to the System.AppDomain.ExecuteAssembly(System.String,System.Security.Policy.Evidence) method

             overload.

            assemblyFile: The name of the file that contains the assembly to execute.

            assemblySecurity: Evidence for loading the assembly.

            Returns: The value returned by the entry point of the assembly.

        ExecuteAssembly(self: _AppDomain, assemblyFile: str) -> int

            Provides COM objects with version-independent access to the System.AppDomain.ExecuteAssembly(System.String) method overload.

            assemblyFile: The name of the file that contains the assembly to execute.

            Returns: The value returned by the entry point of the assembly.

        ExecuteAssembly(self: _AppDomain, assemblyFile: str, assemblySecurity: Evidence, args: Array[str]) -> int

            Provides COM objects with version-independent access to the

             System.AppDomain.ExecuteAssembly(System.String,System.Security.Policy.Evidence,System.String[]) method overload.

            assemblyFile: The name of the file that contains the assembly to execute.

            assemblySecurity: The supplied evidence for the assembly.

            args: The arguments to the entry point of the assembly.

            Returns: The value returned by the entry point of the assembly.
        """
        ...

    def GetAssemblies(self):
        """
        GetAssemblies(self: _AppDomain) -> Array[Assembly]

            Provides COM objects with version-independent access to the System.AppDomain.GetAssemblies method.

            Returns: An array of assemblies in this application domain.
        """
        ...

    def GetData(self, name):
        """
        GetData(self: _AppDomain, name: str) -> object

            Provides COM objects with version-independent access to the System.AppDomain.GetData(System.String) method.

            name: The name of a predefined application domain property, or the name of an application domain property you have defined.

            Returns: The value of the name property.
        """
        ...

    def GetHashCode(self):
        """
        GetHashCode(self: _AppDomain) -> int

            Provides COM objects with version-independent access to the inherited System.Object.GetHashCode method.

            Returns: A hash code for the current System.Object.
        """
        ...

    def GetIDsOfNames(self, riid, rgszNames, cNames, lcid, rgDispId):
        """
        GetIDsOfNames(self: _AppDomain, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid

            Maps a set of names to a corresponding set of dispatch identifiers.

            riid: Reserved for future use. Must be IID_NULL.

            rgszNames: Passed-in array of names to be mapped.

            cNames: Count of the names to be mapped.

            lcid: The locale context in which to interpret the names.

            rgDispId: Caller-allocated array which receives the IDs corresponding to the names.
        """
        ...

    def GetLifetimeService(self):
        """
        GetLifetimeService(self: _AppDomain) -> object

            Provides COM objects with version-independent access to the inherited System.MarshalByRefObject.GetLifetimeService method.

            Returns: An object of type System.Runtime.Remoting.Lifetime.ILease used to control the lifetime policy for this instance.
        """
        ...

    def GetType(self):
        """
        GetType(self: _AppDomain) -> Type

            Provides COM objects with version-independent access to the System.AppDomain.GetType method.

            Returns: A System.Type representing the type of the current instance.
        """
        ...

    def GetTypeInfo(self, iTInfo, lcid, ppTInfo):
        """
        GetTypeInfo(self: _AppDomain, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr)

            Retrieves the type information for an object, which can then be used to get the type information for an interface.

            iTInfo: The type information to return.

            lcid: The locale identifier for the type information.

            ppTInfo: Receives a pointer to the requested type information object.
        """
        ...

    def GetTypeInfoCount(self, pcTInfo):
        """
        GetTypeInfoCount(self: _AppDomain) -> UInt32

            Retrieves the number of type information interfaces that an object provides (either 0 or 1).
        """
        ...

    def InitializeLifetimeService(self):
        """
        InitializeLifetimeService(self: _AppDomain) -> object

            Provides COM objects with version-independent access to the System.AppDomain.InitializeLifetimeService method.

            Returns: Always ll.
        """
        ...

    def Invoke(self, dispIdMember, riid, lcid, wFlags, pDispParams, pVarResult, pExcepInfo, puArgErr):
        """
        Invoke(self: _AppDomain, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid

            Provides access to properties and methods exposed by an object.

            dispIdMember: Identifies the member.

            riid: Reserved for future use. Must be IID_NULL.

            lcid: The locale context in which to interpret arguments.

            wFlags: Flags describing the context of the call.

            pDispParams: Pointer to a structure containing an array of arguments, an array of argument DISPIDs for named arguments, and counts for the number of elements in

             the arrays.

            pVarResult: Pointer to the location where the result is to be stored.

            pExcepInfo: Pointer to a structure that contains exception information.

            puArgErr: The index of the first argument that has an error.
        """
        ...

    def Load(self, *__args):
        """
        Load(self: _AppDomain, assemblyRef: AssemblyName) -> Assembly

            Provides COM objects with version-independent access to the System.AppDomain.Load(System.Reflection.AssemblyName) method overload.

            assemblyRef: An object that describes the assembly to load.

            Returns: The loaded assembly.

        Load(self: _AppDomain, assemblyString: str) -> Assembly

            Provides COM objects with version-independent access to the System.AppDomain.Load(System.String) method overload.

            assemblyString: The display name of the assembly. See System.Reflection.Assembly.FullName.

            Returns: The loaded assembly.

        Load(self: _AppDomain, rawAssembly: Array[Byte]) -> Assembly

            Provides COM objects with version-independent access to the System.AppDomain.Load(System.Byte[]) method overload.

            rawAssembly: An array of type te that is a COFF-based image containing an emitted assembly.

            Returns: The loaded assembly.

        Load(self: _AppDomain, rawAssembly: Array[Byte], rawSymbolStore: Array[Byte]) -> Assembly

            Provides COM objects with version-independent access to the System.AppDomain.Load(System.Byte[],System.Byte[]) method overload.

            rawAssembly: An array of type te that is a COFF-based image containing an emitted assembly.

            rawSymbolStore: An array of type te containing the raw bytes representing the symbols for the assembly.

            Returns: The loaded assembly.

        Load(self: _AppDomain, rawAssembly: Array[Byte], rawSymbolStore: Array[Byte], securityEvidence: Evidence) -> Assembly

            Provides COM objects with version-independent access to the System.AppDomain.Load(System.Byte[],System.Byte[],System.Security.Policy.Evidence) method

             overload.

            rawAssembly: An array of type te that is a COFF-based image containing an emitted assembly.

            rawSymbolStore: An array of type te containing the raw bytes representing the symbols for the assembly.

            securityEvidence: Evidence for loading the assembly.

            Returns: The loaded assembly.

        Load(self: _AppDomain, assemblyRef: AssemblyName, assemblySecurity: Evidence) -> Assembly

            Provides COM objects with version-independent access to the System.AppDomain.Load(System.Reflection.AssemblyName,System.Security.Policy.Evidence)

             method overload.

            assemblyRef: An object that describes the assembly to load.

            assemblySecurity: Evidence for loading the assembly.

            Returns: The loaded assembly.

        Load(self: _AppDomain, assemblyString: str, assemblySecurity: Evidence) -> Assembly

            Provides COM objects with version-independent access to the System.AppDomain.Load(System.String,System.Security.Policy.Evidence) method overload.

            assemblyString: The display name of the assembly. See System.Reflection.Assembly.FullName.

            assemblySecurity: Evidence for loading the assembly.

            Returns: The loaded assembly.
        """
        ...

    def SetAppDomainPolicy(self, domainPolicy):
        """
        SetAppDomainPolicy(self: _AppDomain, domainPolicy: PolicyLevel)

            Provides COM objects with version-independent access to the System.AppDomain.SetAppDomainPolicy(System.Security.Policy.PolicyLevel) method.

            domainPolicy: The security policy level.
        """
        ...

    def SetCachePath(self, s):
        """
        SetCachePath(self: _AppDomain, s: str)

            Provides COM objects with version-independent access to the System.AppDomain.SetCachePath(System.String) method.

            s: The fully qualified path to the shadow copy location.
        """
        ...

    def SetData(self, name, data):
        """
        SetData(self: _AppDomain, name: str, data: object)

            Provides COM objects with version-independent access to the System.AppDomain.SetData(System.String,System.Object) method.

            name: The name of a user-defined application domain property to create or change.

            data: The value of the property.
        """
        ...

    def SetPrincipalPolicy(self, policy):
        """
        SetPrincipalPolicy(self: _AppDomain, policy: PrincipalPolicy)

            Provides COM objects with version-independent access to the System.AppDomain.SetPrincipalPolicy(System.Security.Principal.PrincipalPolicy) method.

            policy: One of the System.Security.Principal.PrincipalPolicy values that specifies the type of the principal object to attach to threads.
        """
        ...

    def SetShadowCopyPath(self, s):
        """
        SetShadowCopyPath(self: _AppDomain, s: str)

            Provides COM objects with version-independent access to the System.AppDomain.SetShadowCopyPath(System.String) method.

            s: A list of directory names, where each name is separated by a semicolon.
        """
        ...

    def SetThreadPrincipal(self, principal):
        """
        SetThreadPrincipal(self: _AppDomain, principal: IPrincipal)

            Provides COM objects with version-independent access to the System.AppDomain.SetThreadPrincipal(System.Security.Principal.IPrincipal) method.

            principal: The principal object to attach to threads.
        """
        ...

    def ToString(self):
        """
        ToString(self: _AppDomain) -> str

            Provides COM objects with version-independent access to the System.AppDomain.ToString method.

            Returns: A string formed by concatenating the literal string "Name:", the friendly name of the application domain, and either string representations of the

             context policies or the string "There are no context policies."
        """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...

    AssemblyLoad = None
    AssemblyResolve = None
    DomainUnload = None
    ProcessExit = None
    ResourceResolve = None
    TypeResolve = None
    UnhandledException = None


class AppDomain(MarshalByRefObject, _AppDomain, IEvidenceFactory):
    """ Represents an application domain, which is an isolated environment where applications execute. This class cannot be inherited. """
    @property
    def ActivationContext(self):
        """
        Gets the activation context for the current application domain.

        Get: ActivationContext(self: AppDomain) -> ActivationContext
        """
        ...

    @property
    def ApplicationIdentity(self):
        """
        Gets the identity of the application in the application domain.

        Get: ApplicationIdentity(self: AppDomain) -> ApplicationIdentity
        """
        ...

    @property
    def ApplicationTrust(self):
        """
        Gets information describing permissions granted to an application and whether the application has a trust level that allows it to run.

        Get: ApplicationTrust(self: AppDomain) -> ApplicationTrust
        """
        ...

    @property
    def CurrentDomain(self):
        """
        Gets the current application domain for the current System.Threading.Thread.

        Get: CurrentDomain() -> AppDomain
        """
        ...

    @property
    def DomainManager(self):
        """
        Gets the domain manager that was provided by the host when the application domain was initialized.

        Get: DomainManager(self: AppDomain) -> AppDomainManager
        """
        ...

    @property
    def Id(self):
        """
        Gets an integer that uniquely identifies the application domain within the process.

        Get: Id(self: AppDomain) -> int
        """
        ...

    @property
    def IsFullyTrusted(self):
        """
        Gets a value that indicates whether assemblies that are loaded into the current application domain execute with full trust.

        Get: IsFullyTrusted(self: AppDomain) -> bool
        """
        ...

    @property
    def IsHomogenous(self):
        """
        Gets a value that indicates whether the current application domain has a set of permissions that is granted to all assemblies that are loaded into the application domain.

        Get: IsHomogenous(self: AppDomain) -> bool
        """
        ...

    @property
    def MonitoringIsEnabled(self):
        """
        Gets or sets a value that indicates whether CPU and memory monitoring of application domains is enabled for the current process. Once monitoring is enabled for a process, it cannot be disabled.

        Get: MonitoringIsEnabled() -> bool

        Set: MonitoringIsEnabled() = value
        """
        ...

    @property
    def MonitoringSurvivedMemorySize(self):
        """
        Gets the number of bytes that survived the last collection and that are known to be referenced by the current application domain.

        Get: MonitoringSurvivedMemorySize(self: AppDomain) -> Int64
        """
        ...

    @property
    def MonitoringSurvivedProcessMemorySize(self):
        """
        Gets the total bytes that survived from the last collection for all application domains in the process.

        Get: MonitoringSurvivedProcessMemorySize() -> Int64
        """
        ...

    @property
    def MonitoringTotalAllocatedMemorySize(self):
        """
        Gets the total size, in bytes, of all memory allocations that have been made by the application domain since it was created, without subtracting memory that has been collected.

        Get: MonitoringTotalAllocatedMemorySize(self: AppDomain) -> Int64
        """
        ...

    @property
    def MonitoringTotalProcessorTime(self):
        """
        Gets the total processor time that has been used by all threads while executing in the current application domain, since the process started.

        Get: MonitoringTotalProcessorTime(self: AppDomain) -> TimeSpan
        """
        ...

    @property
    def PermissionSet(self):
        """
        Gets the permission set of a sandboxed application domain.

        Get: PermissionSet(self: AppDomain) -> PermissionSet
        """
        ...

    @property
    def SetupInformation(self):
        """
        Gets the application domain configuration information for this instance.

        Get: SetupInformation(self: AppDomain) -> AppDomainSetup
        """
        ...


    def ApplyPolicy(self, assemblyName):
        """
        ApplyPolicy(self: AppDomain, assemblyName: str) -> str

            Returns the assembly display name after policy has been applied.

            assemblyName: The assembly display name, in the form provided by the System.Reflection.Assembly.FullName property.

            Returns: A string containing the assembly display name after policy has been applied.
        """
        ...

    def CreateComInstanceFrom(self, *__args):
        """
        CreateComInstanceFrom(self: AppDomain, assemblyName: str, typeName: str) -> ObjectHandle

            Creates a new instance of a specified COM type. Parameters specify the name of a file that contains an assembly containing the type and the name of

             the type.

            assemblyName: The name of a file containing an assembly that defines the requested type.

            typeName: The name of the requested type.

            Returns: An object that is a wrapper for the new instance specified by typeName. The return value needs to be unwrapped to access the real object.

        CreateComInstanceFrom(self: AppDomain, assemblyFile: str, typeName: str, hashValue: Array[Byte], hashAlgorithm: AssemblyHashAlgorithm) -> ObjectHandle

            Creates a new instance of a specified COM type. Parameters specify the name of a file that contains an assembly containing the type and the name of

             the type.

            assemblyFile: The name of a file containing an assembly that defines the requested type.

            typeName: The name of the requested type.

            hashValue: Represents the value of the computed hash code.

            hashAlgorithm: Represents the hash algorithm used by the assembly manifest.

            Returns: An object that is a wrapper for the new instance specified by typeName. The return value needs to be unwrapped to access the real object.
        """
        ...

    @staticmethod
    def CreateDomain(friendlyName, securityInfo=..., *__args):
        """
        CreateDomain(friendlyName: str, securityInfo: Evidence) -> AppDomain

            Creates a new application domain with the given name using the supplied evidence.

            friendlyName: The friendly name of the domain. This friendly name can be displayed in user interfaces to identify the domain. For more information, see

             System.AppDomain.FriendlyName.

            securityInfo: Evidence that establishes the identity of the code that runs in the application domain. Pass ll to use the evidence of the current application domain.

            Returns: The newly created application domain.

        CreateDomain(friendlyName: str) -> AppDomain

            Creates a new application domain with the specified name.

            friendlyName: The friendly name of the domain.

            Returns: The newly created application domain.

        CreateDomain(friendlyName: str, securityInfo: Evidence, info: AppDomainSetup) -> AppDomain

            Creates a new application domain using the specified name, evidence, and application domain setup information.

            friendlyName: The friendly name of the domain. This friendly name can be displayed in user interfaces to identify the domain. For more information, see

             System.AppDomain.FriendlyName.

            securityInfo: Evidence that establishes the identity of the code that runs in the application domain. Pass ll to use the evidence of the current application domain.

            info: An object that contains application domain initialization information.

            Returns: The newly created application domain.

        CreateDomain(friendlyName: str, securityInfo: Evidence, info: AppDomainSetup, grantSet: PermissionSet, *fullTrustAssemblies: Array[StrongName]) -> AppDomain

            Creates a new application domain using the specified name, evidence, application domain setup information, default permission set, and array of fully

             trusted assemblies.

            friendlyName: The friendly name of the domain. This friendly name can be displayed in user interfaces to identify the domain. For more information, see the

             description of System.AppDomain.FriendlyName.

            securityInfo: Evidence that establishes the identity of the code that runs in the application domain. Pass ll to use the evidence of the current application domain.

            info: An object that contains application domain initialization information.

            grantSet: A default permission set that is granted to all assemblies loaded into the new application domain that do not have specific grants.

            fullTrustAssemblies: An array of strong names representing assemblies to be considered fully trusted in the new application domain.

            Returns: The newly created application domain.

        CreateDomain(friendlyName: str, securityInfo: Evidence, appBasePath: str, appRelativeSearchPath: str, shadowCopyFiles: bool) -> AppDomain

            Creates a new application domain with the given name, using evidence, application base path, relative search path, and a parameter that specifies

             whether a shadow copy of an assembly is to be loaded into the application domain.

            friendlyName: The friendly name of the domain. This friendly name can be displayed in user interfaces to identify the domain. For more information, see

             System.AppDomain.FriendlyName.

            securityInfo: Evidence that establishes the identity of the code that runs in the application domain. Pass ll to use the evidence of the current application domain.

            appBasePath: The base directory that the assembly resolver uses to probe for assemblies. For more information, see System.AppDomain.BaseDirectory.

            appRelativeSearchPath: The path relative to the base directory where the assembly resolver should probe for private assemblies. For more information, see

             System.AppDomain.RelativeSearchPath.

            shadowCopyFiles: If ue, a shadow copy of an assembly is loaded into this application domain.

            Returns: The newly created application domain.

        CreateDomain(friendlyName: str, securityInfo: Evidence, appBasePath: str, appRelativeSearchPath: str, shadowCopyFiles: bool, adInit: AppDomainInitializer, adInitArgs: Array[str]) -> AppDomain

            Creates a new application domain with the given name, using evidence, application base path, relative search path, and a parameter that specifies

             whether a shadow copy of an assembly is to be loaded into the application domain. Specifies a callback method that is invoked when the application

             domain is initialized, and an array of string arguments to pass the callback method.

            friendlyName: The friendly name of the domain. This friendly name can be displayed in user interfaces to identify the domain. For more information, see

             System.AppDomain.FriendlyName.

            securityInfo: Evidence that establishes the identity of the code that runs in the application domain. Pass ll to use the evidence of the current application domain.

            appBasePath: The base directory that the assembly resolver uses to probe for assemblies. For more information, see System.AppDomain.BaseDirectory.

            appRelativeSearchPath: The path relative to the base directory where the assembly resolver should probe for private assemblies. For more information, see

             System.AppDomain.RelativeSearchPath.

            shadowCopyFiles: ue to load a shadow copy of an assembly into the application domain.

            adInit: An System.AppDomainInitializer delegate that represents a callback method to invoke when the new System.AppDomain object is initialized.

            adInitArgs: An array of string arguments to be passed to the callback represented by adInit, when the new System.AppDomain object is initialized.

            Returns: The newly created application domain.
        """
        ...

    def CreateInstanceAndUnwrap(self, assemblyName, typeName, *__args):
        """
        CreateInstanceAndUnwrap(self: AppDomain, assemblyName: str, typeName: str) -> object

            Creates a new instance of the specified type. Parameters specify the assembly where the type is defined, and the name of the type.

            assemblyName: The display name of the assembly. See System.Reflection.Assembly.FullName.

            typeName: The fully qualified name of the requested type, including the namespace but not the assembly, as returned by the System.Type.FullName property.

            Returns: An instance of the object specified by typeName.

        CreateInstanceAndUnwrap(self: AppDomain, assemblyName: str, typeName: str, activationAttributes: Array[object]) -> object

            Creates a new instance of the specified type. Parameters specify the assembly where the type is defined, the name of the type, and an array of

             activation attributes.

            assemblyName: The display name of the assembly. See System.Reflection.Assembly.FullName.

            typeName: The fully qualified name of the requested type, including the namespace but not the assembly, as returned by the System.Type.FullName property.

            activationAttributes: An array of one or more attributes that can participate in activation. Typically, an array that contains a single

             System.Runtime.Remoting.Activation.UrlAttribute object that specifies the URL that is required to activate a remote object. This parameter is related

             to client-activated objects.Client activation is a legacy technology that is retained for backward compatibility but is not recommended for new

             development. Distributed applications should instead use Windows Communication Foundation.

            Returns: An instance of the object specified by typeName.

        CreateInstanceAndUnwrap(self: AppDomain, assemblyName: str, typeName: str, ignoreCase: bool, bindingAttr: BindingFlags, binder: Binder, args: Array[object], culture: CultureInfo, activationAttributes: Array[object], securityAttributes: Evidence) -> object

            Creates a new instance of the specified type. Parameters specify the name of the type, and how it is found and created.

            assemblyName: The display name of the assembly. See System.Reflection.Assembly.FullName.

            typeName: The fully qualified name of the requested type, including the namespace but not the assembly, as returned by the System.Type.FullName property.

            ignoreCase: A Boolean value specifying whether to perform a case-sensitive search or not.

            bindingAttr: A combination of zero or more bit flags that affect the search for the typeName constructor. If bindingAttr is zero, a case-sensitive search for

             public constructors is conducted.

            binder: An object that enables the binding, coercion of argument types, invocation of members, and retrieval of System.Reflection.MemberInfo objects using

             reflection. If binder is null, the default binder is used.

            args: The arguments to pass to the constructor. This array of arguments must match in number, order, and type the parameters of the constructor to invoke.

             If the default constructor is preferred, args must be an empty array or null.

            culture: A culture-specific object used to govern the coercion of types. If culture is ll, the ltureInfo for the current thread is used.

            activationAttributes: An array of one or more attributes that can participate in activation. Typically, an array that contains a single

             System.Runtime.Remoting.Activation.UrlAttribute object that specifies the URL that is required to activate a remote object. This parameter is related

             to client-activated objects. Client activation is a legacy technology that is retained for backward compatibility but is not recommended for new

             development. Distributed applications should instead use Windows Communication Foundation.

            securityAttributes: Information used to authorize creation of typeName.

            Returns: An instance of the object specified by typeName.

        CreateInstanceAndUnwrap(self: AppDomain, assemblyName: str, typeName: str, ignoreCase: bool, bindingAttr: BindingFlags, binder: Binder, args: Array[object], culture: CultureInfo, activationAttributes: Array[object]) -> object

            Creates a new instance of the specified type defined in the specified assembly, specifying whether the case of the type name is ignored; the binding

             attributes and the binder that are used to select the type to be created; the arguments of the constructor; the culture; and the activation

             attributes.

            assemblyName: The display name of the assembly. See System.Reflection.Assembly.FullName.

            typeName: The fully qualified name of the requested type, including the namespace but not the assembly, as returned by the System.Type.FullName property.

            ignoreCase: A Boolean value specifying whether to perform a case-sensitive search or not.

            bindingAttr: A combination of zero or more bit flags that affect the search for the typeName constructor. If bindingAttr is zero, a case-sensitive search for

             public constructors is conducted.

            binder: An object that enables the binding, coercion of argument types, invocation of members, and retrieval of System.Reflection.MemberInfo objects using

             reflection. If binder is null, the default binder is used.

            args: The arguments to pass to the constructor. This array of arguments must match in number, order, and type the parameters of the constructor to invoke.

             If the default constructor is preferred, args must be an empty array or null.

            culture: A culture-specific object used to govern the coercion of types. If culture is ll, the ltureInfo for the current thread is used.

            activationAttributes: An array of one or more attributes that can participate in activation. Typically, an array that contains a single

             System.Runtime.Remoting.Activation.UrlAttribute object. that specifies the URL that is required to activate a remote object. This parameter is

             related to client-activated objects. Client activation is a legacy technology that is retained for backward compatibility but is not recommended for

             new development. Distributed applications should instead use Windows Communication Foundation.

            Returns: An instance of the object specified by typeName.
        """
        ...

    def CreateInstanceFromAndUnwrap(self, *__args):
        """
        CreateInstanceFromAndUnwrap(self: AppDomain, assemblyName: str, typeName: str) -> object

            Creates a new instance of the specified type defined in the specified assembly file.

            assemblyName: The file name and path of the assembly that defines the requested type.

            typeName: The fully qualified name of the requested type, including the namespace but not the assembly, as returned by the System.Type.FullName property.

            Returns: The requested object, or ll if typeName is not found.

        CreateInstanceFromAndUnwrap(self: AppDomain, assemblyName: str, typeName: str, activationAttributes: Array[object]) -> object

            Creates a new instance of the specified type defined in the specified assembly file.

            assemblyName: The file name and path of the assembly that defines the requested type.

            typeName: The fully qualified name of the requested type, including the namespace but not the assembly (see the System.Type.FullName property).

            activationAttributes: An array of one or more attributes that can participate in activation. Typically, an array that contains a single

             System.Runtime.Remoting.Activation.UrlAttribute object that specifies the URL that is required to activate a remote object. This parameter is related

             to client-activated objects.Client activation is a legacy technology that is retained for backward compatibility but is not recommended for new

             development. Distributed applications should instead use Windows Communication Foundation.

            Returns: The requested object, or ll if typeName is not found.

        CreateInstanceFromAndUnwrap(self: AppDomain, assemblyName: str, typeName: str, ignoreCase: bool, bindingAttr: BindingFlags, binder: Binder, args: Array[object], culture: CultureInfo, activationAttributes: Array[object], securityAttributes: Evidence) -> object

            Creates a new instance of the specified type defined in the specified assembly file.

            assemblyName: The file name and path of the assembly that defines the requested type.

            typeName: The fully qualified name of the requested type, including the namespace but not the assembly, as returned by the System.Type.FullName property.

            ignoreCase: A Boolean value specifying whether to perform a case-sensitive search or not.

            bindingAttr: A combination of zero or more bit flags that affect the search for the typeName constructor. If bindingAttr is zero, a case-sensitive search for

             public constructors is conducted.

            binder: An object that enables the binding, coercion of argument types, invocation of members, and retrieval of System.Reflection.MemberInfo objects through

             reflection. If binder is null, the default binder is used.

            args: The arguments to pass to the constructor. This array of arguments must match in number, order, and type the parameters of the constructor to invoke.

             If the default constructor is preferred, args must be an empty array or null.

            culture: Culture-specific information that governs the coercion of args to the formal types declared for the typeName constructor. If culture is ll, the

             System.Globalization.CultureInfo for the current thread is used.

            activationAttributes: An array of one or more attributes that can participate in activation. Typically, an array that contains a single

             System.Runtime.Remoting.Activation.UrlAttribute object that specifies the URL that is required to activate a remote object. This parameter is related

             to client-activated objects. Client activation is a legacy technology that is retained for backward compatibility but is not recommended for new

             development. Distributed applications should instead use Windows Communication Foundation.

            securityAttributes: Information used to authorize creation of typeName.

            Returns: The requested object, or ll if typeName is not found.

        CreateInstanceFromAndUnwrap(self: AppDomain, assemblyFile: str, typeName: str, ignoreCase: bool, bindingAttr: BindingFlags, binder: Binder, args: Array[object], culture: CultureInfo, activationAttributes: Array[object]) -> object

            Creates a new instance of the specified type defined in the specified assembly file, specifying whether the case of the type name is ignored; the

             binding attributes and the binder that are used to select the type to be created; the arguments of the constructor; the culture; and the activation

             attributes.

            assemblyFile: The file name and path of the assembly that defines the requested type.

            typeName: The fully qualified name of the requested type, including the namespace but not the assembly, as returned by the System.Type.FullName property.

            ignoreCase: A Boolean value specifying whether to perform a case-sensitive search or not.

            bindingAttr: A combination of zero or more bit flags that affect the search for the typeName constructor. If bindingAttr is zero, a case-sensitive search for

             public constructors is conducted.

            binder: An object that enables the binding, coercion of argument types, invocation of members, and retrieval of System.Reflection.MemberInfo objects through

             reflection. If binder is null, the default binder is used.

            args: The arguments to pass to the constructor. This array of arguments must match in number, order, and type the parameters of the constructor to invoke.

             If the default constructor is preferred, args must be an empty array or null.

            culture: Culture-specific information that governs the coercion of args to the formal types declared for the typeName constructor. If culture is ll, the

             System.Globalization.CultureInfo for the current thread is used.

            activationAttributes: An array of one or more attributes that can participate in activation. Typically, an array that contains a single

             System.Runtime.Remoting.Activation.UrlAttribute object that specifies the URL that is required to activate a remote object. This parameter is related

             to client-activated objects. Client activation is a legacy technology that is retained for backward compatibility but is not recommended for new

             development. Distributed applications should instead use Windows Communication Foundation.

            Returns: The requested object, or ll if typeName is not found.
        """
        ...

    def ExecuteAssemblyByName(self, assemblyName, *__args):
        """
        ExecuteAssemblyByName(self: AppDomain, assemblyName: str) -> int

            Executes an assembly given its display name.

            assemblyName: The display name of the assembly. See System.Reflection.Assembly.FullName.

            Returns: The value returned by the entry point of the assembly.

        ExecuteAssemblyByName(self: AppDomain, assemblyName: str, assemblySecurity: Evidence) -> int

            Executes an assembly given its display name, using the specified evidence.

            assemblyName: The display name of the assembly. See System.Reflection.Assembly.FullName.

            assemblySecurity: Evidence for loading the assembly.

            Returns: The value returned by the entry point of the assembly.

        ExecuteAssemblyByName(self: AppDomain, assemblyName: str, assemblySecurity: Evidence, *args: Array[str]) -> int

            Executes the assembly given its display name, using the specified evidence and arguments.

            assemblyName: The display name of the assembly. See System.Reflection.Assembly.FullName.

            assemblySecurity: Evidence for loading the assembly.

            args: Command-line arguments to pass when starting the process.

            Returns: The value returned by the entry point of the assembly.

        ExecuteAssemblyByName(self: AppDomain, assemblyName: str, *args: Array[str]) -> int

            Executes the assembly given its display name, using the specified arguments.

            assemblyName: The display name of the assembly. See System.Reflection.Assembly.FullName.

            args: Command-line arguments to pass when starting the process.

            Returns: The value that is returned by the entry point of the assembly.

        ExecuteAssemblyByName(self: AppDomain, assemblyName: AssemblyName, assemblySecurity: Evidence, *args: Array[str]) -> int

            Executes the assembly given an System.Reflection.AssemblyName, using the specified evidence and arguments.

            assemblyName: An System.Reflection.AssemblyName object representing the name of the assembly.

            assemblySecurity: Evidence for loading the assembly.

            args: Command-line arguments to pass when starting the process.

            Returns: The value returned by the entry point of the assembly.

        ExecuteAssemblyByName(self: AppDomain, assemblyName: AssemblyName, *args: Array[str]) -> int

            Executes the assembly given an System.Reflection.AssemblyName, using the specified arguments.

            assemblyName: An System.Reflection.AssemblyName object representing the name of the assembly.

            args: Command-line arguments to pass when starting the process.

            Returns: The value that is returned by the entry point of the assembly.
        """
        ...

    @staticmethod
    def GetCurrentThreadId():
        """
        GetCurrentThreadId() -> int

            Gets the current thread identifier.

            Returns: A 32-bit signed integer that is the identifier of the current thread.
        """
        ...

    def IsCompatibilitySwitchSet(self, value):
        """
        IsCompatibilitySwitchSet(self: AppDomain, value: str) -> Nullable[bool]

            Gets a nullable Boolean value that indicates whether any compatibility switches are set, and if so, whether the specified compatibility switch is set.

            value: The compatibility switch to test.

            Returns: A null reference (thing in Visual Basic) if no compatibility switches are set; otherwise, a Boolean value that indicates whether the compatibility

             switch that is specified by value is set.
        """
        ...

    def IsDefaultAppDomain(self):
        """
        IsDefaultAppDomain(self: AppDomain) -> bool

            Returns a value that indicates whether the application domain is the default application domain for the process.

            Returns: ue if the current System.AppDomain object represents the default application domain for the process; otherwise, lse.
        """
        ...

    def IsFinalizingForUnload(self):
        """
        IsFinalizingForUnload(self: AppDomain) -> bool

            Indicates whether this application domain is unloading, and the objects it contains are being finalized by the common language runtime.

            Returns: ue if this application domain is unloading and the common language runtime has started invoking finalizers; otherwise, lse.
        """
        ...

    def ReflectionOnlyGetAssemblies(self):
        """
        ReflectionOnlyGetAssemblies(self: AppDomain) -> Array[Assembly]

            Returns the assemblies that have been loaded into the reflection-only context of the application domain.

            Returns: An array of System.Reflection.Assembly objects that represent the assemblies loaded into the reflection-only context of the application domain.
        """
        ...

    def SetDynamicBase(self, path):
        """
        SetDynamicBase(self: AppDomain, path: str)

            Establishes the specified directory path as the base directory for subdirectories where dynamically generated files are stored and accessed.

            path: The fully qualified path that is the base directory for subdirectories where dynamic assemblies are stored.
        """
        ...

    def SetShadowCopyFiles(self):
        """
        SetShadowCopyFiles(self: AppDomain)

            Turns on shadow copying.
        """
        ...

    @staticmethod
    def Unload(domain):
        """
        Unload(domain: AppDomain)

            Unloads the specified application domain.

            domain: An application domain to unload.
        """
        ...

    AssemblyLoad = None
    AssemblyResolve = None
    DomainUnload = None
    FirstChanceException = None
    ProcessExit = None
    ReflectionOnlyAssemblyResolve = None
    ResourceResolve = None
    TypeResolve = None
    UnhandledException = None


class Delegate(ICloneable, ISerializable):
    """ Represents a delegate, which is a data structure that refers to a static method or to a class instance and an instance method of that class. """
    @property
    def Method(self):
        """
        Gets the method represented by the delegate.

        Get: Method(self: Delegate) -> MethodInfo
        """
        ...

    @property
    def Target(self):
        """
        Gets the class instance on which the current delegate invokes the instance method.

        Get: Target(self: Delegate) -> object
        """
        ...


    def Call(self, *args): #cannot find CLR method
        """
        Call(delegate: Delegate, *args: Array[object]) -> object

        Call(delegate: Delegate, **dict: dict, *args: Array[object]) -> object
        """
        ...

    @staticmethod
    def Combine(*__args):
        """
        Combine(a: Delegate, b: Delegate) -> Delegate

            Concatenates the invocation lists of two delegates.

            a: The delegate whose invocation list comes first.

            b: The delegate whose invocation list comes last.

            Returns: A new delegate with an invocation list that concatenates the invocation lists of a and b in that order. Returns a if b is ll, returns b if a is a

             null reference, and returns a null reference if both a and b are null references.

        Combine(*delegates: Array[Delegate]) -> Delegate

            Concatenates the invocation lists of an array of delegates.

            delegates: The array of delegates to combine.

            Returns: A new delegate with an invocation list that concatenates the invocation lists of the delegates in the delegates array. Returns ll if delegates is ll,

             if delegates contains zero elements, or if every entry in delegates is ll.
        """
        ...

    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: Delegate, d: Delegate) -> Delegate

            Concatenates the invocation lists of the specified multicast (combinable) delegate and the current multicast (combinable) delegate.

            d: The multicast (combinable) delegate whose invocation list to append to the end of the invocation list of the current multicast (combinable) delegate.

            Returns: A new multicast (combinable) delegate with an invocation list that concatenates the invocation list of the current multicast (combinable) delegate

             and the invocation list of d, or the current multicast (combinable) delegate if d is ll.
        """
        ...

    @staticmethod
    def CreateDelegate(type, *__args):
        """
        CreateDelegate(type: Type, target: object, method: str) -> Delegate

            Creates a delegate of the specified type that represents the specified instance method to invoke on the specified class instance.

            type: The System.Type of delegate to create.

            target: The class instance on which method is invoked.

            method: The name of the instance method that the delegate is to represent.

            Returns: A delegate of the specified type that represents the specified instance method to invoke on the specified class instance.

        CreateDelegate(type: Type, target: object, method: str, ignoreCase: bool) -> Delegate

            Creates a delegate of the specified type that represents the specified instance method to invoke on the specified class instance with the specified

             case-sensitivity.

            type: The System.Type of delegate to create.

            target: The class instance on which method is invoked.

            method: The name of the instance method that the delegate is to represent.

            ignoreCase: A Boolean indicating whether to ignore the case when comparing the name of the method.

            Returns: A delegate of the specified type that represents the specified instance method to invoke on the specified class instance.

        CreateDelegate(type: Type, target: object, method: str, ignoreCase: bool, throwOnBindFailure: bool) -> Delegate

            Creates a delegate of the specified type that represents the specified instance method to invoke on the specified class instance, with the specified

             case-sensitivity and the specified behavior on failure to bind.

            type: The System.Type of delegate to create.

            target: The class instance on which method is invoked.

            method: The name of the instance method that the delegate is to represent.

            ignoreCase: A Boolean indicating whether to ignore the case when comparing the name of the method.

            throwOnBindFailure: ue to throw an exception if method cannot be bound; otherwise, lse.

            Returns: A delegate of the specified type that represents the specified instance method to invoke on the specified class instance.

        CreateDelegate(type: Type, target: Type, method: str) -> Delegate

            Creates a delegate of the specified type that represents the specified static method of the specified class.

            type: The System.Type of delegate to create.

            target: The System.Type representing the class that implements method.

            method: The name of the static method that the delegate is to represent.

            Returns: A delegate of the specified type that represents the specified static method of the specified class.

        CreateDelegate(type: Type, target: Type, method: str, ignoreCase: bool) -> Delegate

            Creates a delegate of the specified type that represents the specified static method of the specified class, with the specified case-sensitivity.

            type: The System.Type of delegate to create.

            target: The System.Type representing the class that implements method.

            method: The name of the static method that the delegate is to represent.

            ignoreCase: A Boolean indicating whether to ignore the case when comparing the name of the method.

            Returns: A delegate of the specified type that represents the specified static method of the specified class.

        CreateDelegate(type: Type, target: Type, method: str, ignoreCase: bool, throwOnBindFailure: bool) -> Delegate

            Creates a delegate of the specified type that represents the specified static method of the specified class, with the specified case-sensitivity and

             the specified behavior on failure to bind.

            type: The System.Type of delegate to create.

            target: The System.Type representing the class that implements method.

            method: The name of the static method that the delegate is to represent.

            ignoreCase: A Boolean indicating whether to ignore the case when comparing the name of the method.

            throwOnBindFailure: ue to throw an exception if method cannot be bound; otherwise, lse.

            Returns: A delegate of the specified type that represents the specified static method of the specified class.

        CreateDelegate(type: Type, method: MethodInfo, throwOnBindFailure: bool) -> Delegate

            Creates a delegate of the specified type to represent the specified static method, with the specified behavior on failure to bind.

            type: The System.Type of delegate to create.

            method: The System.Reflection.MethodInfo describing the static or instance method the delegate is to represent.

            throwOnBindFailure: ue to throw an exception if method cannot be bound; otherwise, lse.

            Returns: A delegate of the specified type to represent the specified static method.

        CreateDelegate(type: Type, firstArgument: object, method: MethodInfo, throwOnBindFailure: bool) -> Delegate

            Creates a delegate of the specified type that represents the specified static or instance method, with the specified first argument and the specified

             behavior on failure to bind.

            type: A System.Type representing the type of delegate to create.

            firstArgument: An System.Object that is the first argument of the method the delegate represents. For instance methods, it must be compatible with the instance type.

            method: The System.Reflection.MethodInfo describing the static or instance method the delegate is to represent.

            throwOnBindFailure: ue to throw an exception if method cannot be bound; otherwise, lse.

            Returns: A delegate of the specified type that represents the specified static or instance method, or ll if throwOnBindFailure is lse and the delegate cannot

             be bound to method.

        CreateDelegate(type: Type, method: MethodInfo) -> Delegate

            Creates a delegate of the specified type to represent the specified static method.

            type: The System.Type of delegate to create.

            method: The System.Reflection.MethodInfo describing the static or instance method the delegate is to represent. Only static methods are supported in the .NET

             Framework version 1.0 and 1.1.

            Returns: A delegate of the specified type to represent the specified static method.

        CreateDelegate(type: Type, firstArgument: object, method: MethodInfo) -> Delegate

            Creates a delegate of the specified type that represents the specified static or instance method, with the specified first argument.

            type: The System.Type of delegate to create.

            firstArgument: The object to which the delegate is bound, or ll to treat method as atic (ared in Visual Basic).

            method: The System.Reflection.MethodInfo describing the static or instance method the delegate is to represent.

            Returns: A delegate of the specified type that represents the specified static or instance method.
        """
        ...

    def DynamicInvoke(self, args):
        """
        DynamicInvoke(self: Delegate, *args: Array[object]) -> object

            Dynamically invokes (late-bound) the method represented by the current delegate.

            args: An array of objects that are the arguments to pass to the method represented by the current delegate.-or-

                    ll, if the method represented

             by the current delegate does not require arguments.

            Returns: The object returned by the method represented by the delegate.
        """
        ...

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object

            Dynamically invokes (late-bound) the method represented by the current delegate.

            args: An array of objects that are the arguments to pass to the method represented by the current delegate.-or-

                    ll, if the method represented

             by the current delegate does not require arguments.

            Returns: The object returned by the method represented by the delegate.
        """
        ...

    def Equals(self, obj):
        """
        Equals(self: Delegate, obj: object) -> bool

            Determines whether the specified object and the current delegate are of the same type and share the same targets, methods, and invocation list.

            obj: The object to compare with the current delegate.

            Returns: ue if obj and the current delegate have the same targets, methods, and invocation list; otherwise, lse.
        """
        ...

    def GetHashCode(self):
        """
        GetHashCode(self: Delegate) -> int

            Returns a hash code for the delegate.

            Returns: A hash code for the delegate.
        """
        ...

    def GetInvocationList(self):
        """
        GetInvocationList(self: Delegate) -> Array[Delegate]

            Returns the invocation list of the delegate.

            Returns: An array of delegates representing the invocation list of the current delegate.
        """
        ...

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: Delegate) -> MethodInfo

            Gets the static method represented by the current delegate.

            Returns: A System.Reflection.MethodInfo describing the static method represented by the current delegate.
        """
        ...

    def InPlaceAdd(self, *args): #cannot find CLR method
        """ InPlaceAdd(self: Delegate, other: Delegate) -> Delegate """
        ...

    def InPlaceSubtract(self, *args): #cannot find CLR method
        """ InPlaceSubtract(self: Delegate, other: Delegate) -> Delegate """
        ...

    @staticmethod
    def Remove(source, value):
        """
        Remove(source: Delegate, value: Delegate) -> Delegate

            Removes the last occurrence of the invocation list of a delegate from the invocation list of another delegate.

            source: The delegate from which to remove the invocation list of value.

            value: The delegate that supplies the invocation list to remove from the invocation list of source.

            Returns: A new delegate with an invocation list formed by taking the invocation list of source and removing the last occurrence of the invocation list of

             value, if the invocation list of value is found within the invocation list of source. Returns source if value is ll or if the invocation list of

             value is not found within the invocation list of source. Returns a null reference if the invocation list of value is equal to the invocation list of

             source or if source is a null reference.
        """
        ...

    @staticmethod
    def RemoveAll(source, value):
        """
        RemoveAll(source: Delegate, value: Delegate) -> Delegate

            Removes all occurrences of the invocation list of a delegate from the invocation list of another delegate.

            source: The delegate from which to remove the invocation list of value.

            value: The delegate that supplies the invocation list to remove from the invocation list of source.

            Returns: A new delegate with an invocation list formed by taking the invocation list of source and removing all occurrences of the invocation list of value,

             if the invocation list of value is found within the invocation list of source. Returns source if value is ll or if the invocation list of value is

             not found within the invocation list of source. Returns a null reference if the invocation list of value is equal to the invocation list of source,

             if source contains only a series of invocation lists that are equal to the invocation list of value, or if source is a null reference.
        """
        ...

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: Delegate, d: Delegate) -> Delegate

            Removes the invocation list of a delegate from the invocation list of another delegate.

            d: The delegate that supplies the invocation list to remove from the invocation list of the current delegate.

            Returns: A new delegate with an invocation list formed by taking the invocation list of the current delegate and removing the invocation list of value, if the

             invocation list of value is found within the current delegate's invocation list. Returns the current delegate if value is ll or if the invocation

             list of value is not found within the current delegate's invocation list. Returns ll if the invocation list of value is equal to the current

             delegate's invocation list.
        """
        ...

    def __call__(self, *args): #cannot find CLR method
        """
        Call(delegate: Delegate, *args: Array[object]) -> object

        Call(delegate: Delegate, **dict: dict, *args: Array[object]) -> object
        """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __iadd__(self, *args): #cannot find CLR method
        """ __iadd__(self: Delegate, other: Delegate) -> Delegate """
        ...

    def __isub__(self, *args): #cannot find CLR method
        """ __isub__(self: Delegate, other: Delegate) -> Delegate """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class MulticastDelegate(Delegate): # skipped bases: <type 'ICloneable'>, <type 'ISerializable'>
    """ Represents a multicast delegate; that is, a delegate that can have more than one element in its invocation list. """
    pass

class AppDomainInitializer(MulticastDelegate): # skipped bases: <type 'ICloneable'>, <type 'ISerializable'>
    """
    Represents the callback method to invoke when the application domain is initialized.

    AppDomainInitializer(object: object, method: IntPtr)
    """
    def BeginInvoke(self, args, callback, object):
        """ BeginInvoke(self: AppDomainInitializer, args: Array[str], callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result):
        """ EndInvoke(self: AppDomainInitializer, result: IAsyncResult) """
        ...

    def Invoke(self, args):
        """ Invoke(self: AppDomainInitializer, args: Array[str]) """
        ...


class AppDomainManager(MarshalByRefObject):
    """
    Provides a managed equivalent of an unmanaged host.

    AppDomainManager()
    """
    @property
    def ApplicationActivator(self):
        """
        Gets the application activator that handles the activation of add-ins and manifest-based applications for the domain.

        Get: ApplicationActivator(self: AppDomainManager) -> ApplicationActivator
        """
        ...

    @property
    def EntryAssembly(self):
        """
        Gets the entry assembly for an application.

        Get: EntryAssembly(self: AppDomainManager) -> Assembly
        """
        ...

    @property
    def HostExecutionContextManager(self):
        """
        Gets the host execution context manager that manages the flow of the execution context.

        Get: HostExecutionContextManager(self: AppDomainManager) -> HostExecutionContextManager
        """
        ...

    @property
    def HostSecurityManager(self):
        """
        Gets the host security manager that participates in security decisions for the application domain.

        Get: HostSecurityManager(self: AppDomainManager) -> HostSecurityManager
        """
        ...

    @property
    def InitializationFlags(self):
        """
        Gets the initialization flags for custom application domain managers.

        Get: InitializationFlags(self: AppDomainManager) -> AppDomainManagerInitializationOptions

        Set: InitializationFlags(self: AppDomainManager) = value
        """
        ...


    def CheckSecuritySettings(self, state):
        """
        CheckSecuritySettings(self: AppDomainManager, state: SecurityState) -> bool

            Indicates whether the specified operation is allowed in the application domain.

            state: A subclass of System.Security.SecurityState that identifies the operation whose security status is requested.

            Returns: ue if the host allows the operation specified by state to be performed in the application domain; otherwise, lse.
        """
        ...

    def CreateDomain(self, friendlyName, securityInfo, appDomainInfo):
        """
        CreateDomain(self: AppDomainManager, friendlyName: str, securityInfo: Evidence, appDomainInfo: AppDomainSetup) -> AppDomain

            Returns a new or existing application domain.

            friendlyName: The friendly name of the domain.

            securityInfo: An object that contains evidence mapped through the security policy to establish a top-of-stack permission set.

            appDomainInfo: An object that contains application domain initialization information.

            Returns: A new or existing application domain.
        """
        ...

    def CreateDomainHelper(self, *args): #cannot find CLR method
        """
        CreateDomainHelper(friendlyName: str, securityInfo: Evidence, appDomainInfo: AppDomainSetup) -> AppDomain

            Provides a helper method to create an application domain.

            friendlyName: The friendly name of the domain.

            securityInfo: An object that contains evidence mapped through the security policy to establish a top-of-stack permission set.

            appDomainInfo: An object that contains application domain initialization information.

            Returns: A newly created application domain.
        """
        ...

    def InitializeNewDomain(self, appDomainInfo):
        """
        InitializeNewDomain(self: AppDomainManager, appDomainInfo: AppDomainSetup)

            Initializes the new application domain.

            appDomainInfo: An object that contains application domain initialization information.
        """
        ...


class IConvertible:
    """ Defines methods that convert the value of the implementing reference or value type to a common language runtime type that has an equivalent value. """
    def GetTypeCode(self):
        """
        GetTypeCode(self: IConvertible) -> TypeCode

            Returns the System.TypeCode for this instance.

            Returns: The enumerated constant that is the System.TypeCode of the class or value type that implements this interface.
        """
        ...

    def ToBoolean(self, provider):
        """
        ToBoolean(self: IConvertible, provider: IFormatProvider) -> bool

            Converts the value of this instance to an equivalent Boolean value using the specified culture-specific formatting information.

            provider: An System.IFormatProvider interface implementation that supplies culture-specific formatting information.

            Returns: A Boolean value equivalent to the value of this instance.
        """
        ...

    def ToByte(self, provider):
        """
        ToByte(self: IConvertible, provider: IFormatProvider) -> Byte

            Converts the value of this instance to an equivalent 8-bit unsigned integer using the specified culture-specific formatting information.

            provider: An System.IFormatProvider interface implementation that supplies culture-specific formatting information.

            Returns: An 8-bit unsigned integer equivalent to the value of this instance.
        """
        ...

    def ToChar(self, provider):
        """
        ToChar(self: IConvertible, provider: IFormatProvider) -> Char

            Converts the value of this instance to an equivalent Unicode character using the specified culture-specific formatting information.

            provider: An System.IFormatProvider interface implementation that supplies culture-specific formatting information.

            Returns: A Unicode character equivalent to the value of this instance.
        """
        ...

    def ToDateTime(self, provider):
        """
        ToDateTime(self: IConvertible, provider: IFormatProvider) -> DateTime

            Converts the value of this instance to an equivalent System.DateTime using the specified culture-specific formatting information.

            provider: An System.IFormatProvider interface implementation that supplies culture-specific formatting information.

            Returns: A System.DateTime instance equivalent to the value of this instance.
        """
        ...

    def ToDecimal(self, provider):
        """
        ToDecimal(self: IConvertible, provider: IFormatProvider) -> Decimal

            Converts the value of this instance to an equivalent System.Decimal number using the specified culture-specific formatting information.

            provider: An System.IFormatProvider interface implementation that supplies culture-specific formatting information.

            Returns: A System.Decimal number equivalent to the value of this instance.
        """
        ...

    def ToDouble(self, provider):
        """
        ToDouble(self: IConvertible, provider: IFormatProvider) -> float

            Converts the value of this instance to an equivalent double-precision floating-point number using the specified culture-specific formatting

             information.

            provider: An System.IFormatProvider interface implementation that supplies culture-specific formatting information.

            Returns: A double-precision floating-point number equivalent to the value of this instance.
        """
        ...

    def ToInt16(self, provider):
        """
        ToInt16(self: IConvertible, provider: IFormatProvider) -> Int16

            Converts the value of this instance to an equivalent 16-bit signed integer using the specified culture-specific formatting information.

            provider: An System.IFormatProvider interface implementation that supplies culture-specific formatting information.

            Returns: An 16-bit signed integer equivalent to the value of this instance.
        """
        ...

    def ToInt32(self, provider):
        """
        ToInt32(self: IConvertible, provider: IFormatProvider) -> int

            Converts the value of this instance to an equivalent 32-bit signed integer using the specified culture-specific formatting information.

            provider: An System.IFormatProvider interface implementation that supplies culture-specific formatting information.

            Returns: An 32-bit signed integer equivalent to the value of this instance.
        """
        ...

    def ToInt64(self, provider):
        """
        ToInt64(self: IConvertible, provider: IFormatProvider) -> Int64

            Converts the value of this instance to an equivalent 64-bit signed integer using the specified culture-specific formatting information.

            provider: An System.IFormatProvider interface implementation that supplies culture-specific formatting information.

            Returns: An 64-bit signed integer equivalent to the value of this instance.
        """
        ...

    def ToSByte(self, provider):
        """
        ToSByte(self: IConvertible, provider: IFormatProvider) -> SByte

            Converts the value of this instance to an equivalent 8-bit signed integer using the specified culture-specific formatting information.

            provider: An System.IFormatProvider interface implementation that supplies culture-specific formatting information.

            Returns: An 8-bit signed integer equivalent to the value of this instance.
        """
        ...

    def ToSingle(self, provider):
        """
        ToSingle(self: IConvertible, provider: IFormatProvider) -> Single

            Converts the value of this instance to an equivalent single-precision floating-point number using the specified culture-specific formatting

             information.

            provider: An System.IFormatProvider interface implementation that supplies culture-specific formatting information.

            Returns: A single-precision floating-point number equivalent to the value of this instance.
        """
        ...

    def ToString(self, provider):
        """
        ToString(self: IConvertible, provider: IFormatProvider) -> str

            Converts the value of this instance to an equivalent System.String using the specified culture-specific formatting information.

            provider: An System.IFormatProvider interface implementation that supplies culture-specific formatting information.

            Returns: A System.String instance equivalent to the value of this instance.
        """
        ...

    def ToType(self, conversionType, provider):
        """
        ToType(self: IConvertible, conversionType: Type, provider: IFormatProvider) -> object

            Converts the value of this instance to an System.Object of the specified System.Type that has an equivalent value, using the specified

             culture-specific formatting information.

            conversionType: The System.Type to which the value of this instance is converted.

            provider: An System.IFormatProvider interface implementation that supplies culture-specific formatting information.

            Returns: An System.Object instance of type conversionType whose value is equivalent to the value of this instance.
        """
        ...

    def ToUInt16(self, provider):
        """
        ToUInt16(self: IConvertible, provider: IFormatProvider) -> UInt16

            Converts the value of this instance to an equivalent 16-bit unsigned integer using the specified culture-specific formatting information.

            provider: An System.IFormatProvider interface implementation that supplies culture-specific formatting information.

            Returns: An 16-bit unsigned integer equivalent to the value of this instance.
        """
        ...

    def ToUInt32(self, provider):
        """
        ToUInt32(self: IConvertible, provider: IFormatProvider) -> UInt32

            Converts the value of this instance to an equivalent 32-bit unsigned integer using the specified culture-specific formatting information.

            provider: An System.IFormatProvider interface implementation that supplies culture-specific formatting information.

            Returns: An 32-bit unsigned integer equivalent to the value of this instance.
        """
        ...

    def ToUInt64(self, provider):
        """
        ToUInt64(self: IConvertible, provider: IFormatProvider) -> UInt64

            Converts the value of this instance to an equivalent 64-bit unsigned integer using the specified culture-specific formatting information.

            provider: An System.IFormatProvider interface implementation that supplies culture-specific formatting information.

            Returns: An 64-bit unsigned integer equivalent to the value of this instance.
        """
        ...


class IFormattable:
    """ Provides functionality to format the value of an object into a string representation. """
    def ToString(self, format, formatProvider):
        """
        ToString(self: IFormattable, format: str, formatProvider: IFormatProvider) -> str

            Formats the value of the current instance using the specified format.

            format: The format to use.-or- A null reference (thing in Visual Basic) to use the default format defined for the type of the System.IFormattable

             implementation.

            formatProvider: The provider to use to format the value.-or- A null reference (thing in Visual Basic) to obtain the numeric format information from the current

             locale setting of the operating system.

            Returns: The value of the current instance in the specified format.
        """
        ...

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        ...


class Enum(IComparable, IFormattable, IConvertible, enum.Enum):
    """ Provides the base class for enumerations. """

    def Equals(self, obj):
        """
        Equals(self: Enum, obj: object) -> bool

            Returns a value indicating whether this instance is equal to a specified object.

            obj: An object to compare with this instance, or ll.

            Returns: ue if obj is an enumeration value of the same type and with the same underlying value as this instance; otherwise, lse.
        """
        ...

    @staticmethod
    def Format(enumType, value, format):
        """
        Format(enumType: Type, value: object, format: str) -> str

            Converts the specified value of a specified enumerated type to its equivalent string representation according to the specified format.

            enumType: The enumeration type of the value to convert.

            value: The value to convert.

            format: The output format to use.

            Returns: A string representation of value.
        """
        ...

    def GetHashCode(self):
        """
        GetHashCode(self: Enum) -> int

            Returns the hash code for the value of this instance.

            Returns: A 32-bit signed integer hash code.
        """
        ...

    @staticmethod
    def GetName(enumType, value):
        """
        GetName(enumType: Type, value: object) -> str

            Retrieves the name of the constant in the specified enumeration that has the specified value.

            enumType: An enumeration type.

            value: The value of a particular enumerated constant in terms of its underlying type.

            Returns: A string containing the name of the enumerated constant in enumType whose value is value; or ll if no such constant is found.
        """
        ...

    @staticmethod
    def GetNames(enumType):
        """
        GetNames(enumType: Type) -> Array[str]

            Retrieves an array of the names of the constants in a specified enumeration.

            enumType: An enumeration type.

            Returns: A string array of the names of the constants in enumType.
        """
        ...

    @staticmethod
    def GetUnderlyingType(enumType):
        """
        GetUnderlyingType(enumType: Type) -> Type

            Returns the underlying type of the specified enumeration.

            enumType: The enumeration whose underlying type will be retrieved.

            Returns: The underlying type of enumType.
        """
        ...

    @staticmethod
    def GetValues(enumType):
        """
        GetValues(enumType: Type) -> Array

            Retrieves an array of the values of the constants in a specified enumeration.

            enumType: An enumeration type.

            Returns: An array that contains the values of the constants in enumType.
        """
        ...

    def HasFlag(self, flag):
        """
        HasFlag(self: Enum, flag: Enum) -> bool

            Determines whether one or more bit fields are set in the current instance.

            flag: An enumeration value.

            Returns: ue if the bit field or bit fields that are set in flag are also set in the current instance; otherwise, lse.
        """
        ...

    @staticmethod
    def IsDefined(enumType, value):
        """
        IsDefined(enumType: Type, value: object) -> bool

            Returns an indication whether a constant with a specified value exists in a specified enumeration.

            enumType: An enumeration type.

            value: The value or name of a constant in enumType.

            Returns: ue if a constant in enumType has a value equal to value; otherwise, lse.
        """
        ...

    @staticmethod
    def Parse(enumType, value, ignoreCase=...):
        """
        Parse(enumType: Type, value: str) -> object

            Converts the string representation of the name or numeric value of one or more enumerated constants to an equivalent enumerated object.

            enumType: An enumeration type.

            value: A string containing the name or value to convert.

            Returns: An object of type enumType whose value is represented by value.

        Parse(enumType: Type, value: str, ignoreCase: bool) -> object

            Converts the string representation of the name or numeric value of one or more enumerated constants to an equivalent enumerated object. A parameter

             specifies whether the operation is case-insensitive.

            enumType: An enumeration type.

            value: A string containing the name or value to convert.

            ignoreCase: ue to ignore case; lse to regard case.

            Returns: An object of type enumType whose value is represented by value.
        """
        ...

    @staticmethod
    def ToObject(enumType, value):
        """
        ToObject(enumType: Type, value: object) -> object

            Converts the specified object with an integer value to an enumeration member.

            enumType: The enumeration type to return.

            value: The value convert to an enumeration member.

            Returns: An enumeration object whose value is value.

        ToObject(enumType: Type, value: SByte) -> object

            Converts the specified 8-bit signed integer value to an enumeration member.

            enumType: The enumeration type to return.

            value: The value to convert to an enumeration member.

            Returns: An instance of the enumeration set to value.

        ToObject(enumType: Type, value: Int16) -> object

            Converts the specified 16-bit signed integer to an enumeration member.

            enumType: The enumeration type to return.

            value: The value to convert to an enumeration member.

            Returns: An instance of the enumeration set to value.

        ToObject(enumType: Type, value: int) -> object

            Converts the specified 32-bit signed integer to an enumeration member.

            enumType: The enumeration type to return.

            value: The value to convert to an enumeration member.

            Returns: An instance of the enumeration set to value.

        ToObject(enumType: Type, value: Byte) -> object

            Converts the specified 8-bit unsigned integer to an enumeration member.

            enumType: The enumeration type to return.

            value: The value to convert to an enumeration member.

            Returns: An instance of the enumeration set to value.

        ToObject(enumType: Type, value: UInt16) -> object

            Converts the specified 16-bit unsigned integer value to an enumeration member.

            enumType: The enumeration type to return.

            value: The value to convert to an enumeration member.

            Returns: An instance of the enumeration set to value.

        ToObject(enumType: Type, value: UInt32) -> object

            Converts the specified 32-bit unsigned integer value to an enumeration member.

            enumType: The enumeration type to return.

            value: The value to convert to an enumeration member.

            Returns: An instance of the enumeration set to value.

        ToObject(enumType: Type, value: Int64) -> object

            Converts the specified 64-bit signed integer to an enumeration member.

            enumType: The enumeration type to return.

            value: The value to convert to an enumeration member.

            Returns: An instance of the enumeration set to value.

        ToObject(enumType: Type, value: UInt64) -> object

            Converts the specified 64-bit unsigned integer value to an enumeration member.

            enumType: The enumeration type to return.

            value: The value to convert to an enumeration member.

            Returns: An instance of the enumeration set to value.
        """
        ...

    @staticmethod
    def TryParse(value, *__args):
        """
        TryParse[TEnum](value: str) -> (bool, TEnum)

        TryParse[TEnum](value: str, ignoreCase: bool) -> (bool, TEnum)
        """
        ...

    def __and__(self, *args): #cannot find CLR method
        """ __and__(self: object, other: object) -> object """
        ...

    def __invert__(self, *args): #cannot find CLR method
        """ __invert__(self: object) -> object """
        ...

    def __nonzero__(self, *args): #cannot find CLR method
        """ __nonzero__(self: object) -> bool """
        ...

    def __or__(self, *args): #cannot find CLR method
        """ __or__(self: object, other: object) -> object """
        ...

    def __rand__(self, *args): #cannot find CLR method
        """ __rand__(self: object, other: object) -> object """
        ...

    def __ror__(self, *args): #cannot find CLR method
        """ __ror__(self: object, other: object) -> object """
        ...

    def __rxor__(self, *args): #cannot find CLR method
        """ __rxor__(self: object, other: object) -> object """
        ...

    def __xor__(self, *args): #cannot find CLR method
        """ __xor__(self: object, other: object) -> object """
        ...


class AppDomainManagerInitializationOptions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>
    """
    Specifies the action that a custom application domain manager takes when initializing a new domain.

    enum (flags) AppDomainManagerInitializationOptions, values: None (0), RegisterWithHost (1)
    """

    RegisterWithHost = None
    value__ = None


class AppDomainSetup(IAppDomainSetup):
    """
    Represents assembly binding information that can be added to an instance of System.AppDomain.

    AppDomainSetup()

    AppDomainSetup(activationContext: ActivationContext)

    AppDomainSetup(activationArguments: ActivationArguments)
    """
    @property
    def ActivationArguments(self):
        """
        Gets or sets data about the activation of an application domain.

        Get: ActivationArguments(self: AppDomainSetup) -> ActivationArguments

        Set: ActivationArguments(self: AppDomainSetup) = value
        """
        ...

    @property
    def AppDomainInitializer(self):
        """
        Gets or sets the System.AppDomainInitializer delegate, which represents a callback method that is invoked when the application domain is initialized.

        Get: AppDomainInitializer(self: AppDomainSetup) -> AppDomainInitializer

        Set: AppDomainInitializer(self: AppDomainSetup) = value
        """
        ...

    @property
    def AppDomainInitializerArguments(self):
        """
        Gets or sets the arguments passed to the callback method represented by the System.AppDomainInitializer delegate. The callback method is invoked when the application domain is initialized.

        Get: AppDomainInitializerArguments(self: AppDomainSetup) -> Array[str]

        Set: AppDomainInitializerArguments(self: AppDomainSetup) = value
        """
        ...

    @property
    def AppDomainManagerAssembly(self):
        """
        Gets or sets the display name of the assembly that provides the type of the application domain manager for application domains created using this System.AppDomainSetup object.

        Get: AppDomainManagerAssembly(self: AppDomainSetup) -> str

        Set: AppDomainManagerAssembly(self: AppDomainSetup) = value
        """
        ...

    @property
    def AppDomainManagerType(self):
        """
        Gets or sets the full name of the type that provides the application domain manager for application domains created using this System.AppDomainSetup object.

        Get: AppDomainManagerType(self: AppDomainSetup) -> str

        Set: AppDomainManagerType(self: AppDomainSetup) = value
        """
        ...

    @property
    def ApplicationTrust(self):
        """
        Gets or sets an object containing security and trust information.

        Get: ApplicationTrust(self: AppDomainSetup) -> ApplicationTrust

        Set: ApplicationTrust(self: AppDomainSetup) = value
        """
        ...

    @property
    def DisallowApplicationBaseProbing(self):
        """
        Specifies whether the application base path and private binary path are probed when searching for assemblies to load.

        Get: DisallowApplicationBaseProbing(self: AppDomainSetup) -> bool

        Set: DisallowApplicationBaseProbing(self: AppDomainSetup) = value
        """
        ...

    @property
    def DisallowBindingRedirects(self):
        """
        Gets or sets a value that indicates whether an application domain allows assembly binding redirection.

        Get: DisallowBindingRedirects(self: AppDomainSetup) -> bool

        Set: DisallowBindingRedirects(self: AppDomainSetup) = value
        """
        ...

    @property
    def DisallowCodeDownload(self):
        """
        Gets or sets a value that indicates whether HTTP download of assemblies is allowed for an application domain.

        Get: DisallowCodeDownload(self: AppDomainSetup) -> bool

        Set: DisallowCodeDownload(self: AppDomainSetup) = value
        """
        ...

    @property
    def DisallowPublisherPolicy(self):
        """
        Gets or sets a value that indicates whether the <publisherPolicy> section of the configuration file is applied to an application domain.

        Get: DisallowPublisherPolicy(self: AppDomainSetup) -> bool

        Set: DisallowPublisherPolicy(self: AppDomainSetup) = value
        """
        ...

    @property
    def LoaderOptimization(self):
        """
        Specifies the optimization policy used to load an executable.

        Get: LoaderOptimization(self: AppDomainSetup) -> LoaderOptimization

        Set: LoaderOptimization(self: AppDomainSetup) = value
        """
        ...

    @property
    def PartialTrustVisibleAssemblies(self):
        """
        Gets or sets a list of assemblies marked with the System.Security.PartialTrustVisibilityLevel.NotVisibleByDefault flag that are made visible to partial-trust code running in a sandboxed application domain.

        Get: PartialTrustVisibleAssemblies(self: AppDomainSetup) -> Array[str]

        Set: PartialTrustVisibleAssemblies(self: AppDomainSetup) = value
        """
        ...

    @property
    def SandboxInterop(self):
        """
        Gets or sets a value that indicates whether interface caching is disabled for interop calls in the application domain, so that a QueryInterface is performed on each call.

        Get: SandboxInterop(self: AppDomainSetup) -> bool

        Set: SandboxInterop(self: AppDomainSetup) = value
        """
        ...

    @property
    def TargetFrameworkName(self):
        """
        Gets or sets a string that specifies the target version and profile of the .NET Framework for the application domain, in a format that can be parsed by the System.Runtime.Versioning.FrameworkName.#ctor(System.String) constructor.

        Get: TargetFrameworkName(self: AppDomainSetup) -> str

        Set: TargetFrameworkName(self: AppDomainSetup) = value
        """
        ...


    def GetConfigurationBytes(self):
        """
        GetConfigurationBytes(self: AppDomainSetup) -> Array[Byte]

            Returns the XML configuration information set by the System.AppDomainSetup.SetConfigurationBytes(System.Byte[]) method, which overrides the

             application's XML configuration information.

            Returns: An array that contains the XML configuration information that was set by the System.AppDomainSetup.SetConfigurationBytes(System.Byte[]) method, or ll

             if the System.AppDomainSetup.SetConfigurationBytes(System.Byte[]) method has not been called.
        """
        ...

    def SetCompatibilitySwitches(self, switches):
        """ SetCompatibilitySwitches(self: AppDomainSetup, switches: IEnumerable[str]) """
        ...

    def SetConfigurationBytes(self, value):
        """
        SetConfigurationBytes(self: AppDomainSetup, value: Array[Byte])

            Provides XML configuration information for the application domain, replacing the application's XML configuration information.

            value: An array that contains the XML configuration information to be used for the application domain.
        """
        ...

    def SetNativeFunction(self, functionName, functionVersion, functionPointer):
        """
        SetNativeFunction(self: AppDomainSetup, functionName: str, functionVersion: int, functionPointer: IntPtr)

            Provides the common language runtime with an alternate implementation of a string comparison function.

            functionName: The name of the string comparison function to override.

            functionVersion: The function version. For .NET Framework 4.5, its value must be 1 or greater.

            functionPointer: A pointer to the function that overrides functionName.
        """
        ...


class AppDomainUnloadedException(SystemException): # skipped bases: <type 'ISerializable'>, <type '_Exception'>
    """
    The exception that is thrown when an attempt is made to access an unloaded application domain.

    AppDomainUnloadedException()

    AppDomainUnloadedException(message: str)

    AppDomainUnloadedException(message: str, innerException: Exception)
    """
    SerializeObjectState = None


class ApplicationException(Exception): # skipped bases: <type 'ISerializable'>, <type '_Exception'>
    """
    Serves as the base class for application-defined exceptions.

    ApplicationException()

    ApplicationException(message: str)

    ApplicationException(message: str, innerException: Exception)
    """
    SerializeObjectState = None


class ApplicationId: # skipped bases: <type 'object'>
    """
    Contains information used to uniquely identify a manifest-based application. This class cannot be inherited.

    ApplicationId(publicKeyToken: Array[Byte], name: str, version: Version, processorArchitecture: str, culture: str)
    """
    @property
    def Culture(self):
        """
        Gets a string representing the culture information for the application.

        Get: Culture(self: ApplicationId) -> str
        """
        ...

    @property
    def Name(self):
        """
        Gets the name of the application.

        Get: Name(self: ApplicationId) -> str
        """
        ...

    @property
    def ProcessorArchitecture(self):
        """
        Gets the target processor architecture for the application.

        Get: ProcessorArchitecture(self: ApplicationId) -> str
        """
        ...

    @property
    def PublicKeyToken(self):
        """
        Gets the public key token for the application.

        Get: PublicKeyToken(self: ApplicationId) -> Array[Byte]
        """
        ...

    @property
    def Version(self):
        """
        Gets the version of the application.

        Get: Version(self: ApplicationId) -> Version
        """
        ...


    def Copy(self):
        """
        Copy(self: ApplicationId) -> ApplicationId

            Creates and returns an identical copy of the current application identity.

            Returns: An System.ApplicationId object that represents an exact copy of the original.
        """
        ...

    def Equals(self, o):
        """
        Equals(self: ApplicationId, o: object) -> bool

            Determines whether the specified System.ApplicationId object is equivalent to the current System.ApplicationId.

            o: The System.ApplicationId object to compare to the current System.ApplicationId.

            Returns: ue if the specified System.ApplicationId object is equivalent to the current System.ApplicationId; otherwise, lse.
        """
        ...

    def GetHashCode(self):
        """
        GetHashCode(self: ApplicationId) -> int

            Gets the hash code for the current application identity.

            Returns: The hash code for the current application identity.
        """
        ...

    def ToString(self):
        """
        ToString(self: ApplicationId) -> str

            Creates and returns a string representation of the application identity.

            Returns: A string representation of the application identity.
        """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ApplicationIdentity( ISerializable):
    """
    Provides the ability to uniquely identify a manifest-activated application. This class cannot be inherited.

    ApplicationIdentity(applicationIdentityFullName: str)
    """
    @property
    def CodeBase(self):
        """
        Gets the location of the deployment manifest as a URL.

        Get: CodeBase(self: ApplicationIdentity) -> str
        """
        ...

    @property
    def FullName(self):
        """
        Gets the full name of the application.

        Get: FullName(self: ApplicationIdentity) -> str
        """
        ...


    def ToString(self):
        """
        ToString(self: ApplicationIdentity) -> str

            Returns the full name of the manifest-activated application.

            Returns: The full name of the manifest-activated application.
        """
        ...


class ArgIterator: # skipped bases: <type 'object'>
    """
    Represents a variable-length argument list; that is, the parameters of a function that takes a variable number of arguments.

    ArgIterator(arglist: RuntimeArgumentHandle)

    ArgIterator(arglist: RuntimeArgumentHandle, ptr: Void*)
    """
    def End(self):
        """
        End(self: ArgIterator)

            Concludes processing of the variable-length argument list represented by this instance.
        """
        ...

    def Equals(self, o):
        """
        Equals(self: ArgIterator, o: object) -> bool

            This method is not supported, and always throws System.NotSupportedException.

            o: An object to be compared to this instance.

            Returns: This comparison is not supported. No value is returned.
        """
        ...

    def GetHashCode(self):
        """
        GetHashCode(self: ArgIterator) -> int

            Returns the hash code of this object.

            Returns: A 32-bit signed integer hash code.
        """
        ...

    def GetNextArg(self, rth=...):
        """
        GetNextArg(self: ArgIterator) -> TypedReference

            Returns the next argument in a variable-length argument list.

            Returns: The next argument as a System.TypedReference object.

        GetNextArg(self: ArgIterator, rth: RuntimeTypeHandle) -> TypedReference

            Returns the next argument in a variable-length argument list that has a specified type.

            rth: A runtime type handle that identifies the type of the argument to retrieve.

            Returns: The next argument as a System.TypedReference object.
        """
        ...

    def GetNextArgType(self):
        """
        GetNextArgType(self: ArgIterator) -> RuntimeTypeHandle

            Returns the type of the next argument.

            Returns: The type of the next argument.
        """
        ...

    def GetRemainingCount(self):
        """
        GetRemainingCount(self: ArgIterator) -> int

            Returns the number of arguments remaining in the argument list.

            Returns: The number of remaining arguments.
        """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ArgumentException(SystemException): # skipped bases: <type 'ISerializable'>, <type '_Exception'>
    """
    The exception that is thrown when one of the arguments provided to a method is not valid.

    ArgumentException()

    ArgumentException(message: str)

    ArgumentException(message: str, innerException: Exception)

    ArgumentException(message: str, paramName: str, innerException: Exception)

    ArgumentException(message: str, paramName: str)
    """
    @property
    def ParamName(self):
        """
        Gets the name of the parameter that causes this exception.

        Get: ParamName(self: ArgumentException) -> str
        """
        ...


    SerializeObjectState = None


class ArgumentNullException(ArgumentException): # skipped bases: <type 'ISerializable'>, <type '_Exception'>
    """
    The exception that is thrown when a null reference (thing in Visual Basic) is passed to a method that does not accept it as a valid argument.

    ArgumentNullException()

    ArgumentNullException(paramName: str)

    ArgumentNullException(message: str, innerException: Exception)

    ArgumentNullException(paramName: str, message: str)
    """
    SerializeObjectState = None


class ArgumentOutOfRangeException(ArgumentException): # skipped bases: <type 'ISerializable'>, <type '_Exception'>
    """
    The exception that is thrown when the value of an argument is outside the allowable range of values as defined by the invoked method.

    ArgumentOutOfRangeException()

    ArgumentOutOfRangeException(paramName: str)

    ArgumentOutOfRangeException(paramName: str, message: str)

    ArgumentOutOfRangeException(message: str, innerException: Exception)

    ArgumentOutOfRangeException(paramName: str, actualValue: object, message: str)
    """
    @property
    def ActualValue(self):
        """
        Gets the argument value that causes this exception.

        Get: ActualValue(self: ArgumentOutOfRangeException) -> object
        """
        ...


    SerializeObjectState = None


class ArithmeticException(SystemException): # skipped bases: <type 'ISerializable'>, <type '_Exception'>
    """
    The exception that is thrown for errors in an arithmetic, casting, or conversion operation.

    ArithmeticException()

    ArithmeticException(message: str)

    ArithmeticException(message: str, innerException: Exception)
    """
    SerializeObjectState = None


class ICloneable:
    """ Supports cloning, which creates a new instance of a class with the same value as an existing instance. """
    def Clone(self):
        """
        Clone(self: ICloneable) -> object

            Creates a new object that is a copy of the current instance.

            Returns: A new object that is a copy of this instance.
        """
        ...


class Array( ICloneable, IList, IStructuralComparable, IStructuralEquatable): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>
    """ Provides methods for creating, manipulating, searching, and sorting arrays, thereby serving as the base class for all arrays in the common language runtime.To browse the .NET Framework source code for this type, see the Reference Source. """
    @property
    def IsSynchronized(self):
        """
        Gets a value indicating whether access to the System.Array is synchronized (thread safe).

        Get: IsSynchronized(self: Array) -> bool
        """
        ...

    @property
    def Length(self):
        """
        Gets the total number of elements in all the dimensions of the System.Array.

        Get: Length(self: Array) -> int
        """
        ...

    @property
    def LongLength(self):
        """
        Gets a 64-bit integer that represents the total number of elements in all the dimensions of the System.Array.

        Get: LongLength(self: Array) -> Int64
        """
        ...

    @property
    def Rank(self):
        """
        Gets the rank (number of dimensions) of the System.Array. For example, a one-dimensional array returns 1, a two-dimensional array returns 2, and so on.

        Get: Rank(self: Array) -> int
        """
        ...

    @property
    def SyncRoot(self):
        """
        Gets an object that can be used to synchronize access to the System.Array.

        Get: SyncRoot(self: Array) -> object
        """
        ...


    @staticmethod
    def AsReadOnly(array):
        """ AsReadOnly[T](array: Array[T]) -> ReadOnlyCollection[T] """
        ...

    @staticmethod
    def BinarySearch(array, *__args):
        """
        BinarySearch(array: Array, value: object) -> int

            Searches an entire one-dimensional sorted array for a specific element, using the System.IComparable interface implemented by each element of the

             array and by the specified object.

            array: The sorted one-dimensional System.Array to search.

            value: The object to search for.

            Returns: The index of the specified value in the specified array, if value is found; otherwise, a negative number. If value is not found and value is less

             than one or more elements in array, the negative number returned is the bitwise complement of the index of the first element that is larger than

             value. If value is not found and value is greater than all elements in array, the negative number returned is the bitwise complement of (the index of

             the last element plus 1). If this method is called with a non-sorted array, the return value can be incorrect and a negative number could be

             returned, even if value is present in array.

        BinarySearch(array: Array, index: int, length: int, value: object) -> int

            Searches a range of elements in a one-dimensional sorted array for a value, using the System.IComparable interface implemented by each element of the

             array and by the specified value.

            array: The sorted one-dimensional System.Array to search.

            index: The starting index of the range to search.

            length: The length of the range to search.

            value: The object to search for.

            Returns: The index of the specified value in the specified array, if value is found; otherwise, a negative number. If value is not found and value is less

             than one or more elements in array, the negative number returned is the bitwise complement of the index of the first element that is larger than

             value. If value is not found and value is greater than all elements in array, the negative number returned is the bitwise complement of (the index of

             the last element plus 1). If this method is called with a non-sorted array, the return value can be incorrect and a negative number could be

             returned, even if value is present in array.

        BinarySearch(array: Array, value: object, comparer: IComparer) -> int

            Searches an entire one-dimensional sorted array for a value using the specified System.Collections.IComparer interface.

            array: The sorted one-dimensional System.Array to search.

            value: The object to search for.

            comparer: The System.Collections.IComparer implementation to use when comparing elements.-or-

                    ll to use the System.IComparable implementation of

             each element.

            Returns: The index of the specified value in the specified array, if value is found; otherwise, a negative number. If value is not found and value is less

             than one or more elements in array, the negative number returned is the bitwise complement of the index of the first element that is larger than

             value. If value is not found and value is greater than all elements in array, the negative number returned is the bitwise complement of (the index of

             the last element plus 1). If this method is called with a non-sorted array, the return value can be incorrect and a negative number could be

             returned, even if value is present in array.

        BinarySearch[T](array: Array[T], value: T) -> int

        BinarySearch[T](array: Array[T], value: T, comparer: IComparer[T]) -> int

        BinarySearch[T](array: Array[T], index: int, length: int, value: T) -> int

        BinarySearch[T](array: Array[T], index: int, length: int, value: T, comparer: IComparer[T]) -> int

        BinarySearch(array: Array, index: int, length: int, value: object, comparer: IComparer) -> int

            Searches a range of elements in a one-dimensional sorted array for a value, using the specified System.Collections.IComparer interface.

            array: The sorted one-dimensional System.Array to search.

            index: The starting index of the range to search.

            length: The length of the range to search.

            value: The object to search for.

            comparer: The System.Collections.IComparer implementation to use when comparing elements.-or-

                    ll to use the System.IComparable implementation of

             each element.

            Returns: The index of the specified value in the specified array, if value is found; otherwise, a negative number. If value is not found and value is less

             than one or more elements in array, the negative number returned is the bitwise complement of the index of the first element that is larger than

             value. If value is not found and value is greater than all elements in array, the negative number returned is the bitwise complement of (the index of

             the last element plus 1). If this method is called with a non-sorted array, the return value can be incorrect and a negative number could be

             returned, even if value is present in array.
        """
        ...

    @staticmethod
    def ConstrainedCopy(sourceArray, sourceIndex, destinationArray, destinationIndex, length):
        """
        ConstrainedCopy(sourceArray: Array, sourceIndex: int, destinationArray: Array, destinationIndex: int, length: int)

            Copies a range of elements from an System.Array starting at the specified source index and pastes them to another System.Array starting at the

             specified destination index.  Guarantees that all changes are undone if the copy does not succeed completely.

            sourceArray: The System.Array that contains the data to copy.

            sourceIndex: A 32-bit integer that represents the index in the sourceArray at which copying begins.

            destinationArray: The System.Array that receives the data.

            destinationIndex: A 32-bit integer that represents the index in the destinationArray at which storing begins.

            length: A 32-bit integer that represents the number of elements to copy.
        """
        ...

    @staticmethod
    def ConvertAll(array, converter):
        """ ConvertAll[(TInput, TOutput)](array: Array[TInput], converter: Converter[TInput, TOutput]) -> Array[TOutput] """
        ...

    @staticmethod
    def Copy(sourceArray, *__args):
        """
        Copy(sourceArray: Array, destinationArray: Array, length: int)

            Copies a range of elements from an System.Array starting at the first element and pastes them into another System.Array starting at the first

             element. The length is specified as a 32-bit integer.

            sourceArray: The System.Array that contains the data to copy.

            destinationArray: The System.Array that receives the data.

            length: A 32-bit integer that represents the number of elements to copy.

        Copy(sourceArray: Array, sourceIndex: int, destinationArray: Array, destinationIndex: int, length: int)

            Copies a range of elements from an System.Array starting at the specified source index and pastes them to another System.Array starting at the

             specified destination index. The length and the indexes are specified as 32-bit integers.

            sourceArray: The System.Array that contains the data to copy.

            sourceIndex: A 32-bit integer that represents the index in the sourceArray at which copying begins.

            destinationArray: The System.Array that receives the data.

            destinationIndex: A 32-bit integer that represents the index in the destinationArray at which storing begins.

            length: A 32-bit integer that represents the number of elements to copy.

        Copy(sourceArray: Array, destinationArray: Array, length: Int64)

            Copies a range of elements from an System.Array starting at the first element and pastes them into another System.Array starting at the first

             element. The length is specified as a 64-bit integer.

            sourceArray: The System.Array that contains the data to copy.

            destinationArray: The System.Array that receives the data.

            length: A 64-bit integer that represents the number of elements to copy. The integer must be between zero and System.Int32.MaxValue, inclusive.

        Copy(sourceArray: Array, sourceIndex: Int64, destinationArray: Array, destinationIndex: Int64, length: Int64)

            Copies a range of elements from an System.Array starting at the specified source index and pastes them to another System.Array starting at the

             specified destination index. The length and the indexes are specified as 64-bit integers.

            sourceArray: The System.Array that contains the data to copy.

            sourceIndex: A 64-bit integer that represents the index in the sourceArray at which copying begins.

            destinationArray: The System.Array that receives the data.

            destinationIndex: A 64-bit integer that represents the index in the destinationArray at which storing begins.

            length: A 64-bit integer that represents the number of elements to copy. The integer must be between zero and System.Int32.MaxValue, inclusive.
        """
        ...

    def CopyTo(self, array, index):
        """
        CopyTo(self: Array, array: Array, index: int)

            Copies all the elements of the current one-dimensional array to the specified one-dimensional array starting at the specified destination array

             index. The index is specified as a 32-bit integer.

            array: The one-dimensional array that is the destination of the elements copied from the current array.

            index: A 32-bit integer that represents the index in array at which copying begins.

        CopyTo(self: Array, array: Array, index: Int64)

            Copies all the elements of the current one-dimensional array to the specified one-dimensional array starting at the specified destination array

             index. The index is specified as a 64-bit integer.

            array: The one-dimensional array that is the destination of the elements copied from the current array.

            index: A 64-bit integer that represents the index in array at which copying begins.
        """
        ...

    @staticmethod
    def CreateInstance(elementType, *__args):
        """
        CreateInstance(elementType: Type, length: int) -> Array

            Creates a one-dimensional System.Array of the specified System.Type and length, with zero-based indexing.

            elementType: The System.Type of the System.Array to create.

            length: The size of the System.Array to create.

            Returns: A new one-dimensional System.Array of the specified System.Type with the specified length, using zero-based indexing.

        CreateInstance(elementType: Type, length1: int, length2: int, length3: int) -> Array

            Creates a three-dimensional System.Array of the specified System.Type and dimension lengths, with zero-based indexing.

            elementType: The System.Type of the System.Array to create.

            length1: The size of the first dimension of the System.Array to create.

            length2: The size of the second dimension of the System.Array to create.

            length3: The size of the third dimension of the System.Array to create.

            Returns: A new three-dimensional System.Array of the specified System.Type with the specified length for each dimension, using zero-based indexing.

        CreateInstance(elementType: Type, *lengths: Array[int]) -> Array

            Creates a multidimensional System.Array of the specified System.Type and dimension lengths, with zero-based indexing. The dimension lengths are

             specified in an array of 32-bit integers.

            elementType: The System.Type of the System.Array to create.

            lengths: An array of 32-bit integers that represent the size of each dimension of the System.Array to create.

            Returns: A new multidimensional System.Array of the specified System.Type with the specified length for each dimension, using zero-based indexing.

        CreateInstance(elementType: Type, *lengths: Array[Int64]) -> Array

            Creates a multidimensional System.Array of the specified System.Type and dimension lengths, with zero-based indexing. The dimension lengths are

             specified in an array of 64-bit integers.

            elementType: The System.Type of the System.Array to create.

            lengths: An array of 64-bit integers that represent the size of each dimension of the System.Array to create. Each integer in the array must be between zero

             and System.Int32.MaxValue, inclusive.

            Returns: A new multidimensional System.Array of the specified System.Type with the specified length for each dimension, using zero-based indexing.

        CreateInstance(elementType: Type, lengths: Array[int], lowerBounds: Array[int]) -> Array

            Creates a multidimensional System.Array of the specified System.Type and dimension lengths, with the specified lower bounds.

            elementType: The System.Type of the System.Array to create.

            lengths: A one-dimensional array that contains the size of each dimension of the System.Array to create.

            lowerBounds: A one-dimensional array that contains the lower bound (starting index) of each dimension of the System.Array to create.

            Returns: A new multidimensional System.Array of the specified System.Type with the specified length and lower bound for each dimension.

        CreateInstance(elementType: Type, length1: int, length2: int) -> Array

            Creates a two-dimensional System.Array of the specified System.Type and dimension lengths, with zero-based indexing.

            elementType: The System.Type of the System.Array to create.

            length1: The size of the first dimension of the System.Array to create.

            length2: The size of the second dimension of the System.Array to create.

            Returns: A new two-dimensional System.Array of the specified System.Type with the specified length for each dimension, using zero-based indexing.
        """
        ...

    @staticmethod
    def Empty():
        """ Empty[T]() -> Array[T] """
        ...

    @staticmethod
    def Exists(array, match):
        """ Exists[T](array: Array[T], match: Predicate[T]) -> bool """
        ...

    @staticmethod
    def Find(array, match):
        """ Find[T](array: Array[T], match: Predicate[T]) -> T """
        ...

    @staticmethod
    def FindAll(array, match):
        """ FindAll[T](array: Array[T], match: Predicate[T]) -> Array[T] """
        ...

    @staticmethod
    def FindIndex(array, *__args):
        """
        FindIndex[T](array: Array[T], match: Predicate[T]) -> int

        FindIndex[T](array: Array[T], startIndex: int, match: Predicate[T]) -> int

        FindIndex[T](array: Array[T], startIndex: int, count: int, match: Predicate[T]) -> int
        """
        ...

    @staticmethod
    def FindLast(array, match):
        """ FindLast[T](array: Array[T], match: Predicate[T]) -> T """
        ...

    @staticmethod
    def FindLastIndex(array, *__args):
        """
        FindLastIndex[T](array: Array[T], match: Predicate[T]) -> int

        FindLastIndex[T](array: Array[T], startIndex: int, match: Predicate[T]) -> int

        FindLastIndex[T](array: Array[T], startIndex: int, count: int, match: Predicate[T]) -> int
        """
        ...

    @staticmethod
    def ForEach(array, action):
        """ ForEach[T](array: Array[T], action: Action[T]) """
        ...

    def GetEnumerator(self):
        """
        GetEnumerator(self: Array) -> IEnumerator

            Returns an System.Collections.IEnumerator for the System.Array.

            Returns: An System.Collections.IEnumerator for the System.Array.
        """
        ...

    def GetLength(self, dimension):
        """
        GetLength(self: Array, dimension: int) -> int

            Gets a 32-bit integer that represents the number of elements in the specified dimension of the System.Array.

            dimension: A zero-based dimension of the System.Array whose length needs to be determined.

            Returns: A 32-bit integer that represents the number of elements in the specified dimension.
        """
        ...

    def GetLongLength(self, dimension):
        """
        GetLongLength(self: Array, dimension: int) -> Int64

            Gets a 64-bit integer that represents the number of elements in the specified dimension of the System.Array.

            dimension: A zero-based dimension of the System.Array whose length needs to be determined.

            Returns: A 64-bit integer that represents the number of elements in the specified dimension.
        """
        ...

    def GetLowerBound(self, dimension):
        """
        GetLowerBound(self: Array, dimension: int) -> int

            Gets the index of the first element of the specified dimension in the array.

            dimension: A zero-based dimension of the array whose starting index needs to be determined.

            Returns: The index of the first element of the specified dimension in the array.
        """
        ...

    def GetUpperBound(self, dimension):
        """
        GetUpperBound(self: Array, dimension: int) -> int

            Gets the index of the last element of the specified dimension in the array.

            dimension: A zero-based dimension of the array whose upper bound needs to be determined.

            Returns: The index of the last element of the specified dimension in the array, or -1 if the specified dimension is empty.
        """
        ...

    def GetValue(self, *__args):
        """
        GetValue(self: Array, *indices: Array[int]) -> object

            Gets the value at the specified position in the multidimensional System.Array. The indexes are specified as an array of 32-bit integers.

            indices: A one-dimensional array of 32-bit integers that represent the indexes specifying the position of the System.Array element to get.

            Returns: The value at the specified position in the multidimensional System.Array.

        GetValue(self: Array, index: int) -> object

            Gets the value at the specified position in the one-dimensional System.Array. The index is specified as a 32-bit integer.

            index: A 32-bit integer that represents the position of the System.Array element to get.

            Returns: The value at the specified position in the one-dimensional System.Array.

        GetValue(self: Array, index1: int, index2: int) -> object

            Gets the value at the specified position in the two-dimensional System.Array. The indexes are specified as 32-bit integers.

            index1: A 32-bit integer that represents the first-dimension index of the System.Array element to get.

            index2: A 32-bit integer that represents the second-dimension index of the System.Array element to get.

            Returns: The value at the specified position in the two-dimensional System.Array.

        GetValue(self: Array, index1: int, index2: int, index3: int) -> object

            Gets the value at the specified position in the three-dimensional System.Array. The indexes are specified as 32-bit integers.

            index1: A 32-bit integer that represents the first-dimension index of the System.Array element to get.

            index2: A 32-bit integer that represents the second-dimension index of the System.Array element to get.

            index3: A 32-bit integer that represents the third-dimension index of the System.Array element to get.

            Returns: The value at the specified position in the three-dimensional System.Array.

        GetValue(self: Array, index: Int64) -> object

            Gets the value at the specified position in the one-dimensional System.Array. The index is specified as a 64-bit integer.

            index: A 64-bit integer that represents the position of the System.Array element to get.

            Returns: The value at the specified position in the one-dimensional System.Array.

        GetValue(self: Array, index1: Int64, index2: Int64) -> object

            Gets the value at the specified position in the two-dimensional System.Array. The indexes are specified as 64-bit integers.

            index1: A 64-bit integer that represents the first-dimension index of the System.Array element to get.

            index2: A 64-bit integer that represents the second-dimension index of the System.Array element to get.

            Returns: The value at the specified position in the two-dimensional System.Array.

        GetValue(self: Array, index1: Int64, index2: Int64, index3: Int64) -> object

            Gets the value at the specified position in the three-dimensional System.Array. The indexes are specified as 64-bit integers.

            index1: A 64-bit integer that represents the first-dimension index of the System.Array element to get.

            index2: A 64-bit integer that represents the second-dimension index of the System.Array element to get.

            index3: A 64-bit integer that represents the third-dimension index of the System.Array element to get.

            Returns: The value at the specified position in the three-dimensional System.Array.

        GetValue(self: Array, *indices: Array[Int64]) -> object

            Gets the value at the specified position in the multidimensional System.Array. The indexes are specified as an array of 64-bit integers.

            indices: A one-dimensional array of 64-bit integers that represent the indexes specifying the position of the System.Array element to get.

            Returns: The value at the specified position in the multidimensional System.Array.
        """
        ...

    def Initialize(self):
        """
        Initialize(self: Array)

            Initializes every element of the value-type System.Array by calling the default constructor of the value type.
        """
        ...

    @staticmethod
    def LastIndexOf(array, value, startIndex=..., count=...):
        """
        LastIndexOf(array: Array, value: object) -> int

            Searches for the specified object and returns the index of the last occurrence within the entire one-dimensional System.Array.

            array: The one-dimensional System.Array to search.

            value: The object to locate in array.

            Returns: The index of the last occurrence of value within the entire array, if found; otherwise, the lower bound of the array minus 1.

        LastIndexOf(array: Array, value: object, startIndex: int) -> int

            Searches for the specified object and returns the index of the last occurrence within the range of elements in the one-dimensional System.Array that

             extends from the first element to the specified index.

            array: The one-dimensional System.Array to search.

            value: The object to locate in array.

            startIndex: The starting index of the backward search.

            Returns: The index of the last occurrence of value within the range of elements in array that extends from the first element to startIndex, if found;

             otherwise, the lower bound of the array minus 1.

        LastIndexOf(array: Array, value: object, startIndex: int, count: int) -> int

            Searches for the specified object and returns the index of the last occurrence within the range of elements in the one-dimensional System.Array that

             contains the specified number of elements and ends at the specified index.

            array: The one-dimensional System.Array to search.

            value: The object to locate in array.

            startIndex: The starting index of the backward search.

            count: The number of elements in the section to search.

            Returns: The index of the last occurrence of value within the range of elements in array that contains the number of elements specified in count and ends at

             startIndex, if found; otherwise, the lower bound of the array minus 1.

        LastIndexOf[T](array: Array[T], value: T) -> int

        LastIndexOf[T](array: Array[T], value: T, startIndex: int) -> int

        LastIndexOf[T](array: Array[T], value: T, startIndex: int, count: int) -> int
        """
        ...

    @staticmethod
    def Resize(array, newSize):
        """ Resize[T](array: Array[T], newSize: int) -> Array[T] """
        ...

    @staticmethod
    def Reverse(array, index=..., length=...):
        """
        Reverse(array: Array)

            Reverses the sequence of the elements in the entire one-dimensional System.Array.

            array: The one-dimensional System.Array to reverse.

        Reverse(array: Array, index: int, length: int)

            Reverses the sequence of the elements in a range of elements in the one-dimensional System.Array.

            array: The one-dimensional System.Array to reverse.

            index: The starting index of the section to reverse.

            length: The number of elements in the section to reverse.
        """
        ...

    def SetValue(self, value, *__args):
        """
        SetValue(self: Array, value: object, index: int)

            Sets a value to the element at the specified position in the one-dimensional System.Array. The index is specified as a 32-bit integer.

            value: The new value for the specified element.

            index: A 32-bit integer that represents the position of the System.Array element to set.

        SetValue(self: Array, value: object, index1: int, index2: int)

            Sets a value to the element at the specified position in the two-dimensional System.Array. The indexes are specified as 32-bit integers.

            value: The new value for the specified element.

            index1: A 32-bit integer that represents the first-dimension index of the System.Array element to set.

            index2: A 32-bit integer that represents the second-dimension index of the System.Array element to set.

        SetValue(self: Array, value: object, index1: int, index2: int, index3: int)

            Sets a value to the element at the specified position in the three-dimensional System.Array. The indexes are specified as 32-bit integers.

            value: The new value for the specified element.

            index1: A 32-bit integer that represents the first-dimension index of the System.Array element to set.

            index2: A 32-bit integer that represents the second-dimension index of the System.Array element to set.

            index3: A 32-bit integer that represents the third-dimension index of the System.Array element to set.

        SetValue(self: Array, value: object, *indices: Array[int])

            Sets a value to the element at the specified position in the multidimensional System.Array. The indexes are specified as an array of 32-bit integers.

            value: The new value for the specified element.

            indices: A one-dimensional array of 32-bit integers that represent the indexes specifying the position of the element to set.

        SetValue(self: Array, value: object, index: Int64)

            Sets a value to the element at the specified position in the one-dimensional System.Array. The index is specified as a 64-bit integer.

            value: The new value for the specified element.

            index: A 64-bit integer that represents the position of the System.Array element to set.

        SetValue(self: Array, value: object, index1: Int64, index2: Int64)

            Sets a value to the element at the specified position in the two-dimensional System.Array. The indexes are specified as 64-bit integers.

            value: The new value for the specified element.

            index1: A 64-bit integer that represents the first-dimension index of the System.Array element to set.

            index2: A 64-bit integer that represents the second-dimension index of the System.Array element to set.

        SetValue(self: Array, value: object, index1: Int64, index2: Int64, index3: Int64)

            Sets a value to the element at the specified position in the three-dimensional System.Array. The indexes are specified as 64-bit integers.

            value: The new value for the specified element.

            index1: A 64-bit integer that represents the first-dimension index of the System.Array element to set.

            index2: A 64-bit integer that represents the second-dimension index of the System.Array element to set.

            index3: A 64-bit integer that represents the third-dimension index of the System.Array element to set.

        SetValue(self: Array, value: object, *indices: Array[Int64])

            Sets a value to the element at the specified position in the multidimensional System.Array. The indexes are specified as an array of 64-bit integers.

            value: The new value for the specified element.

            indices: A one-dimensional array of 64-bit integers that represent the indexes specifying the position of the element to set.
        """
        ...

    @staticmethod
    def Sort(*__args):
        """
        Sort(array: Array)

            Sorts the elements in an entire one-dimensional System.Array using the System.IComparable implementation of each element of the System.Array.

            array: The one-dimensional System.Array to sort.

        Sort[(TKey, TValue)](keys: Array[TKey], items: Array[TValue], index: int, length: int, comparer: IComparer[TKey])Sort[T](array: Array[T], index: int, length: int, comparer: IComparer[T])Sort[(TKey, TValue)](keys: Array[TKey], items: Array[TValue], comparer: IComparer[TKey])Sort[T](array: Array[T], comparer: IComparer[T])Sort[(TKey, TValue)](keys: Array[TKey], items: Array[TValue], index: int, length: int)Sort[T](array: Array[T], index: int, length: int)Sort[T](array: Array[T], comparison: Comparison[T])Sort[(TKey, TValue)](keys: Array[TKey], items: Array[TValue])Sort(array: Array, index: int, length: int, comparer: IComparer)

            Sorts the elements in a range of elements in a one-dimensional System.Array using the specified System.Collections.IComparer.

            array: The one-dimensional System.Array to sort.

            index: The starting index of the range to sort.

            length: The number of elements in the range to sort.

            comparer: The System.Collections.IComparer implementation to use when comparing elements.-or-

                    ll to use the System.IComparable implementation of

             each element.

        Sort(keys: Array, items: Array, comparer: IComparer)

            Sorts a pair of one-dimensional System.Array objects (one contains the keys and the other contains the corresponding items) based on the keys in the

             first System.Array using the specified System.Collections.IComparer.

            keys: The one-dimensional System.Array that contains the keys to sort.

            items: The one-dimensional System.Array that contains the items that correspond to each of the keys in the keysSystem.Array.-or-

                    ll to sort

             only the keysSystem.Array.

            comparer: The System.Collections.IComparer implementation to use when comparing elements.-or-

                    ll to use the System.IComparable implementation of

             each element.

        Sort(array: Array, comparer: IComparer)

            Sorts the elements in a one-dimensional System.Array using the specified System.Collections.IComparer.

            array: The one-dimensional array to sort.

            comparer: The implementation to use when comparing elements.-or-

                    ll to use the System.IComparable implementation of each element.

        Sort(keys: Array, items: Array, index: int, length: int)

            Sorts a range of elements in a pair of one-dimensional System.Array objects (one contains the keys and the other contains the corresponding items)

             based on the keys in the first System.Array using the System.IComparable implementation of each key.

            keys: The one-dimensional System.Array that contains the keys to sort.

            items: The one-dimensional System.Array that contains the items that correspond to each of the keys in the keysSystem.Array.-or-

                    ll to sort

             only the keysSystem.Array.

            index: The starting index of the range to sort.

            length: The number of elements in the range to sort.

        Sort(array: Array, index: int, length: int)

            Sorts the elements in a range of elements in a one-dimensional System.Array using the System.IComparable implementation of each element of the

             System.Array.

            array: The one-dimensional System.Array to sort.

            index: The starting index of the range to sort.

            length: The number of elements in the range to sort.

        Sort(keys: Array, items: Array)

            Sorts a pair of one-dimensional System.Array objects (one contains the keys and the other contains the corresponding items) based on the keys in the

             first System.Array using the System.IComparable implementation of each key.

            keys: The one-dimensional System.Array that contains the keys to sort.

            items: The one-dimensional System.Array that contains the items that correspond to each of the keys in the keysSystem.Array.-or-

                    ll to sort

             only the keysSystem.Array.

        Sort[T](array: Array[T])Sort(keys: Array, items: Array, index: int, length: int, comparer: IComparer)

            Sorts a range of elements in a pair of one-dimensional System.Array objects (one contains the keys and the other contains the corresponding items)

             based on the keys in the first System.Array using the specified System.Collections.IComparer.

            keys: The one-dimensional System.Array that contains the keys to sort.

            items: The one-dimensional System.Array that contains the items that correspond to each of the keys in the keysSystem.Array.-or-

                    ll to sort

             only the keysSystem.Array.

            index: The starting index of the range to sort.

            length: The number of elements in the range to sort.

            comparer: The System.Collections.IComparer implementation to use when comparing elements.-or-

                    ll to use the System.IComparable implementation of

             each element.
        """
        ...

    @staticmethod
    def TrueForAll(array, match):
        """ TrueForAll[T](array: Array[T], match: Predicate[T]) -> bool """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """
        __contains__(self: IList, value: object) -> bool

            Determines whether the System.Collections.IList contains a specific value.

            value: The object to locate in the System.Collections.IList.

            Returns: ue if the System.Object is found in the System.Collections.IList; otherwise, lse.
        """
        ...

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*y """
        ...

    def __radd__(self, *args): #cannot find CLR method
        """ __radd__(data1: Array, data2: Array) -> Array """
        ...


class ArraySegment( IList, IReadOnlyList): # skipped bases: <type 'IEnumerable[T]'>, <type 'IEnumerable'>, <type 'ICollection[T]'>, <type 'IReadOnlyCollection[T]'>
    """
    ArraySegment[T](array: Array[T])

    ArraySegment[T](array: Array[T], offset: int, count: int)
    """
    @property
    def Array(self):
        """
        Gets the original array containing the range of elements that the array segment delimits.

        Get: Array(self: ArraySegment[T]) -> Array[T]
        """
        ...

    @property
    def Count(self):
        """
        Gets the number of elements in the range delimited by the array segment.

        Get: Count(self: ArraySegment[T]) -> int
        """
        ...

    @property
    def Offset(self):
        """
        Gets the position of the first element in the range delimited by the array segment, relative to the start of the original array.

        Get: Offset(self: ArraySegment[T]) -> int
        """
        ...


    def Equals(self, obj):
        """
        Equals(self: ArraySegment[T], obj: object) -> bool

            Determines whether the specified object is equal to the current instance.

            obj: The object to be compared with the current instance.

            Returns: ue if the specified object is a System.ArraySegment structure and is equal to the current instance; otherwise, lse.

        Equals(self: ArraySegment[T], obj: ArraySegment[T]) -> bool

            Determines whether the specified System.ArraySegment structure is equal to the current instance.

            obj: The structure to compare with the current instance.

            Returns: ue if the specified System.ArraySegment structure is equal to the current instance; otherwise, lse.
        """
        ...

    def GetHashCode(self):
        """
        GetHashCode(self: ArraySegment[T]) -> int

            Returns the hash code for the current instance.

            Returns: A 32-bit signed integer hash code.
        """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ArrayTypeMismatchException(SystemException): # skipped bases: <type 'ISerializable'>, <type '_Exception'>
    """
    The exception that is thrown when an attempt is made to store an element of the wrong type within an array.

    ArrayTypeMismatchException()

    ArrayTypeMismatchException(message: str)

    ArrayTypeMismatchException(message: str, innerException: Exception)
    """
    SerializeObjectState = None


class EventArgs: # skipped bases: <type 'object'>
    """
    Represents the base class for classes that contain event data, and provides a value to use for events that do not include event data.

    EventArgs()
    """
    Empty = None


class AssemblyLoadEventArgs(EventArgs):
    """
    Provides data for the System.AppDomain.AssemblyLoad event.

    AssemblyLoadEventArgs(loadedAssembly: Assembly)
    """
    @property
    def LoadedAssembly(self):
        """
        Gets an System.Reflection.Assembly that represents the currently loaded assembly.

        Get: LoadedAssembly(self: AssemblyLoadEventArgs) -> Assembly
        """
        ...


    @staticmethod # known case of __new__
    def __new__(cls, loadedAssembly):
        """ __new__(cls: type, loadedAssembly: Assembly) """
        ...


class AssemblyLoadEventHandler(MulticastDelegate): # skipped bases: <type 'ICloneable'>, <type 'ISerializable'>
    """
    Represents the method that handles the System.AppDomain.AssemblyLoad event of an System.AppDomain.

    AssemblyLoadEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, args, callback, object):
        """ BeginInvoke(self: AssemblyLoadEventHandler, sender: object, args: AssemblyLoadEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result):
        """ EndInvoke(self: AssemblyLoadEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender, args):
        """ Invoke(self: AssemblyLoadEventHandler, sender: object, args: AssemblyLoadEventArgs) """
        ...


class AsyncCallback(MulticastDelegate): # skipped bases: <type 'ICloneable'>, <type 'ISerializable'>
    """
    References a method to be called when a corresponding asynchronous operation completes.

    AsyncCallback(object: object, method: IntPtr)
    """
    def BeginInvoke(self, ar, callback, object):
        """ BeginInvoke(self: AsyncCallback, ar: IAsyncResult, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result):
        """ EndInvoke(self: AsyncCallback, result: IAsyncResult) """
        ...

    def Invoke(self, ar):
        """ Invoke(self: AsyncCallback, ar: IAsyncResult) """
        ...


class Attribute( _Attribute):
    """ Represents the base class for custom attributes. """
    @property
    def TypeId(self):
        """
        When implemented in a derived class, gets a unique identifier for this System.Attribute.

        Get: TypeId(self: Attribute) -> object
        """
        ...


    def Equals(self, obj):
        """
        Equals(self: Attribute, obj: object) -> bool

            Returns a value that indicates whether this instance is equal to a specified object.

            obj: An System.Object to compare with this instance or ll.

            Returns: ue if obj equals the type and value of this instance; otherwise, lse.
        """
        ...

    @staticmethod
    def GetCustomAttribute(element, attributeType, inherit=...):
        """
        GetCustomAttribute(element: MemberInfo, attributeType: Type) -> Attribute

            Retrieves a custom attribute applied to a member of a type. Parameters specify the member, and the type of the custom attribute to search for.

            element: An object derived from the System.Reflection.MemberInfo class that describes a constructor, event, field, method, or property member of a class.

            attributeType: The type, or a base type, of the custom attribute to search for.

            Returns: A reference to the single custom attribute of type attributeType that is applied to element, or ll if there is no such attribute.

        GetCustomAttribute(element: MemberInfo, attributeType: Type, inherit: bool) -> Attribute

            Retrieves a custom attribute applied to a member of a type. Parameters specify the member, the type of the custom attribute to search for, and

             whether to search ancestors of the member.

            element: An object derived from the System.Reflection.MemberInfo class that describes a constructor, event, field, method, or property member of a class.

            attributeType: The type, or a base type, of the custom attribute to search for.

            inherit: If ue, specifies to also search the ancestors of element for custom attributes.

            Returns: A reference to the single custom attribute of type attributeType that is applied to element, or ll if there is no such attribute.

        GetCustomAttribute(element: ParameterInfo, attributeType: Type) -> Attribute

            Retrieves a custom attribute applied to a method parameter. Parameters specify the method parameter, and the type of the custom attribute to search

             for.

            element: An object derived from the System.Reflection.ParameterInfo class that describes a parameter of a member of a class.

            attributeType: The type, or a base type, of the custom attribute to search for.

            Returns: A reference to the single custom attribute of type attributeType that is applied to element, or ll if there is no such attribute.

        GetCustomAttribute(element: ParameterInfo, attributeType: Type, inherit: bool) -> Attribute

            Retrieves a custom attribute applied to a method parameter. Parameters specify the method parameter, the type of the custom attribute to search for,

             and whether to search ancestors of the method parameter.

            element: An object derived from the System.Reflection.ParameterInfo class that describes a parameter of a member of a class.

            attributeType: The type, or a base type, of the custom attribute to search for.

            inherit: If ue, specifies to also search the ancestors of element for custom attributes.

            Returns: A reference to the single custom attribute of type attributeType that is applied to element, or ll if there is no such attribute.

        GetCustomAttribute(element: Module, attributeType: Type) -> Attribute

            Retrieves a custom attribute applied to a module. Parameters specify the module, and the type of the custom attribute to search for.

            element: An object derived from the System.Reflection.Module class that describes a portable executable file.

            attributeType: The type, or a base type, of the custom attribute to search for.

            Returns: A reference to the single custom attribute of type attributeType that is applied to element, or ll if there is no such attribute.

        GetCustomAttribute(element: Module, attributeType: Type, inherit: bool) -> Attribute

            Retrieves a custom attribute applied to a module. Parameters specify the module, the type of the custom attribute to search for, and an ignored

             search option.

            element: An object derived from the System.Reflection.Module class that describes a portable executable file.

            attributeType: The type, or a base type, of the custom attribute to search for.

            inherit: This parameter is ignored, and does not affect the operation of this method.

            Returns: A reference to the single custom attribute of type attributeType that is applied to element, or ll if there is no such attribute.

        GetCustomAttribute(element: Assembly, attributeType: Type) -> Attribute

            Retrieves a custom attribute applied to a specified assembly. Parameters specify the assembly and the type of the custom attribute to search for.

            element: An object derived from the System.Reflection.Assembly class that describes a reusable collection of modules.

            attributeType: The type, or a base type, of the custom attribute to search for.

            Returns: A reference to the single custom attribute of type attributeType that is applied to element, or ll if there is no such attribute.

        GetCustomAttribute(element: Assembly, attributeType: Type, inherit: bool) -> Attribute

            Retrieves a custom attribute applied to an assembly. Parameters specify the assembly, the type of the custom attribute to search for, and an ignored

             search option.

            element: An object derived from the System.Reflection.Assembly class that describes a reusable collection of modules.

            attributeType: The type, or a base type, of the custom attribute to search for.

            inherit: This parameter is ignored, and does not affect the operation of this method.

            Returns: A reference to the single custom attribute of type attributeType that is applied to element, or ll if there is no such attribute.
        """
        ...

    @staticmethod
    def GetCustomAttributes(element, *__args):
        """
        GetCustomAttributes(element: MemberInfo, type: Type) -> Array[Attribute]

            Retrieves an array of the custom attributes applied to a member of a type. Parameters specify the member, and the type of the custom attribute to

             search for.

            element: An object derived from the System.Reflection.MemberInfo class that describes a constructor, event, field, method, or property member of a class.

            type: The type, or a base type, of the custom attribute to search for.

            Returns: An System.Attribute array that contains the custom attributes of type type applied to element, or an empty array if no such custom attributes exist.

        GetCustomAttributes(element: MemberInfo, type: Type, inherit: bool) -> Array[Attribute]

            Retrieves an array of the custom attributes applied to a member of a type. Parameters specify the member, the type of the custom attribute to search

             for, and whether to search ancestors of the member.

            element: An object derived from the System.Reflection.MemberInfo class that describes a constructor, event, field, method, or property member of a class.

            type: The type, or a base type, of the custom attribute to search for.

            inherit: If ue, specifies to also search the ancestors of element for custom attributes.

            Returns: An System.Attribute array that contains the custom attributes of type type applied to element, or an empty array if no such custom attributes exist.

        GetCustomAttributes(element: MemberInfo) -> Array[Attribute]

            Retrieves an array of the custom attributes applied to a member of a type. A parameter specifies the member.

            element: An object derived from the System.Reflection.MemberInfo class that describes a constructor, event, field, method, or property member of a class.

            Returns: An System.Attribute array that contains the custom attributes applied to element, or an empty array if no such custom attributes exist.

        GetCustomAttributes(element: MemberInfo, inherit: bool) -> Array[Attribute]

            Retrieves an array of the custom attributes applied to a member of a type. Parameters specify the member, the type of the custom attribute to search

             for, and whether to search ancestors of the member.

            element: An object derived from the System.Reflection.MemberInfo class that describes a constructor, event, field, method, or property member of a class.

            inherit: If ue, specifies to also search the ancestors of element for custom attributes.

            Returns: An System.Attribute array that contains the custom attributes applied to element, or an empty array if no such custom attributes exist.

        GetCustomAttributes(element: ParameterInfo) -> Array[Attribute]

            Retrieves an array of the custom attributes applied to a method parameter. A parameter specifies the method parameter.

            element: An object derived from the System.Reflection.ParameterInfo class that describes a parameter of a member of a class.

            Returns: An System.Attribute array that contains the custom attributes applied to element, or an empty array if no such custom attributes exist.

        GetCustomAttributes(element: ParameterInfo, attributeType: Type) -> Array[Attribute]

            Retrieves an array of the custom attributes applied to a method parameter. Parameters specify the method parameter, and the type of the custom

             attribute to search for.

            element: An object derived from the System.Reflection.ParameterInfo class that describes a parameter of a member of a class.

            attributeType: The type, or a base type, of the custom attribute to search for.

            Returns: An System.Attribute array that contains the custom attributes of type attributeType applied to element, or an empty array if no such custom

             attributes exist.

        GetCustomAttributes(element: ParameterInfo, attributeType: Type, inherit: bool) -> Array[Attribute]

            Retrieves an array of the custom attributes applied to a method parameter. Parameters specify the method parameter, the type of the custom attribute

             to search for, and whether to search ancestors of the method parameter.

            element: An object derived from the System.Reflection.ParameterInfo class that describes a parameter of a member of a class.

            attributeType: The type, or a base type, of the custom attribute to search for.

            inherit: If ue, specifies to also search the ancestors of element for custom attributes.

            Returns: An System.Attribute array that contains the custom attributes of type attributeType applied to element, or an empty array if no such custom

             attributes exist.

        GetCustomAttributes(element: ParameterInfo, inherit: bool) -> Array[Attribute]

            Retrieves an array of the custom attributes applied to a method parameter. Parameters specify the method parameter, and whether to search ancestors

             of the method parameter.

            element: An object derived from the System.Reflection.ParameterInfo class that describes a parameter of a member of a class.

            inherit: If ue, specifies to also search the ancestors of element for custom attributes.

            Returns: An System.Attribute array that contains the custom attributes applied to element, or an empty array if no such custom attributes exist.

        GetCustomAttributes(element: Module, attributeType: Type) -> Array[Attribute]

            Retrieves an array of the custom attributes applied to a module. Parameters specify the module, and the type of the custom attribute to search for.

            element: An object derived from the System.Reflection.Module class that describes a portable executable file.

            attributeType: The type, or a base type, of the custom attribute to search for.

            Returns: An System.Attribute array that contains the custom attributes of type attributeType applied to element, or an empty array if no such custom

             attributes exist.

        GetCustomAttributes(element: Module) -> Array[Attribute]

            Retrieves an array of the custom attributes applied to a module. A parameter specifies the module.

            element: An object derived from the System.Reflection.Module class that describes a portable executable file.

            Returns: An System.Attribute array that contains the custom attributes applied to element, or an empty array if no such custom attributes exist.

        GetCustomAttributes(element: Module, inherit: bool) -> Array[Attribute]

            Retrieves an array of the custom attributes applied to a module. Parameters specify the module, and an ignored search option.

            element: An object derived from the System.Reflection.Module class that describes a portable executable file.

            inherit: This parameter is ignored, and does not affect the operation of this method.

            Returns: An System.Attribute array that contains the custom attributes applied to element, or an empty array if no such custom attributes exist.

        GetCustomAttributes(element: Module, attributeType: Type, inherit: bool) -> Array[Attribute]

            Retrieves an array of the custom attributes applied to a module. Parameters specify the module, the type of the custom attribute to search for, and

             an ignored search option.

            element: An object derived from the System.Reflection.Module class that describes a portable executable file.

            attributeType: The type, or a base type, of the custom attribute to search for.

            inherit: This parameter is ignored, and does not affect the operation of this method.

            Returns: An System.Attribute array that contains the custom attributes of type attributeType applied to element, or an empty array if no such custom

             attributes exist.

        GetCustomAttributes(element: Assembly, attributeType: Type) -> Array[Attribute]

            Retrieves an array of the custom attributes applied to an assembly. Parameters specify the assembly, and the type of the custom attribute to search

             for.

            element: An object derived from the System.Reflection.Assembly class that describes a reusable collection of modules.

            attributeType: The type, or a base type, of the custom attribute to search for.

            Returns: An System.Attribute array that contains the custom attributes of type attributeType applied to element, or an empty array if no such custom

             attributes exist.

        GetCustomAttributes(element: Assembly, attributeType: Type, inherit: bool) -> Array[Attribute]

            Retrieves an array of the custom attributes applied to an assembly. Parameters specify the assembly, the type of the custom attribute to search for,

             and an ignored search option.

            element: An object derived from the System.Reflection.Assembly class that describes a reusable collection of modules.

            attributeType: The type, or a base type, of the custom attribute to search for.

            inherit: This parameter is ignored, and does not affect the operation of this method.

            Returns: An System.Attribute array that contains the custom attributes of type attributeType applied to element, or an empty array if no such custom

             attributes exist.

        GetCustomAttributes(element: Assembly) -> Array[Attribute]

            Retrieves an array of the custom attributes applied to an assembly. A parameter specifies the assembly.

            element: An object derived from the System.Reflection.Assembly class that describes a reusable collection of modules.

            Returns: An System.Attribute array that contains the custom attributes applied to element, or an empty array if no such custom attributes exist.

        GetCustomAttributes(element: Assembly, inherit: bool) -> Array[Attribute]

            Retrieves an array of the custom attributes applied to an assembly. Parameters specify the assembly, and an ignored search option.

            element: An object derived from the System.Reflection.Assembly class that describes a reusable collection of modules.

            inherit: This parameter is ignored, and does not affect the operation of this method.

            Returns: An System.Attribute array that contains the custom attributes applied to element, or an empty array if no such custom attributes exist.
        """
        ...

    def GetHashCode(self):
        """
        GetHashCode(self: Attribute) -> int

            Returns the hash code for this instance.

            Returns: A 32-bit signed integer hash code.
        """
        ...

    def IsDefaultAttribute(self):
        """
        IsDefaultAttribute(self: Attribute) -> bool

            When overridden in a derived class, indicates whether the value of this instance is the default value for the derived class.

            Returns: ue if this instance is the default attribute for the class; otherwise, lse.
        """
        ...

    @staticmethod
    def IsDefined(element, attributeType, inherit=...):
        """
        IsDefined(element: MemberInfo, attributeType: Type) -> bool

            Determines whether any custom attributes are applied to a member of a type. Parameters specify the member, and the type of the custom attribute to

             search for.

            element: An object derived from the System.Reflection.MemberInfo class that describes a constructor, event, field, method, type, or property member of a class.

            attributeType: The type, or a base type, of the custom attribute to search for.

            Returns: ue if a custom attribute of type attributeType is applied to element; otherwise, lse.

        IsDefined(element: MemberInfo, attributeType: Type, inherit: bool) -> bool

            Determines whether any custom attributes are applied to a member of a type. Parameters specify the member, the type of the custom attribute to search

             for, and whether to search ancestors of the member.

            element: An object derived from the System.Reflection.MemberInfo class that describes a constructor, event, field, method, type, or property member of a class.

            attributeType: The type, or a base type, of the custom attribute to search for.

            inherit: If ue, specifies to also search the ancestors of element for custom attributes.

            Returns: ue if a custom attribute of type attributeType is applied to element; otherwise, lse.

        IsDefined(element: ParameterInfo, attributeType: Type) -> bool

            Determines whether any custom attributes are applied to a method parameter. Parameters specify the method parameter, and the type of the custom

             attribute to search for.

            element: An object derived from the System.Reflection.ParameterInfo class that describes a parameter of a member of a class.

            attributeType: The type, or a base type, of the custom attribute to search for.

            Returns: ue if a custom attribute of type attributeType is applied to element; otherwise, lse.

        IsDefined(element: ParameterInfo, attributeType: Type, inherit: bool) -> bool

            Determines whether any custom attributes are applied to a method parameter. Parameters specify the method parameter, the type of the custom attribute

             to search for, and whether to search ancestors of the method parameter.

            element: An object derived from the System.Reflection.ParameterInfo class that describes a parameter of a member of a class.

            attributeType: The type, or a base type, of the custom attribute to search for.

            inherit: If ue, specifies to also search the ancestors of element for custom attributes.

            Returns: ue if a custom attribute of type attributeType is applied to element; otherwise, lse.

        IsDefined(element: Module, attributeType: Type) -> bool

            Determines whether any custom attributes of a specified type are applied to a module. Parameters specify the module, and the type of the custom

             attribute to search for.

            element: An object derived from the System.Reflection.Module class that describes a portable executable file.

            attributeType: The type, or a base type, of the custom attribute to search for.

            Returns: ue if a custom attribute of type attributeType is applied to element; otherwise, lse.

        IsDefined(element: Module, attributeType: Type, inherit: bool) -> bool

            Determines whether any custom attributes are applied to a module. Parameters specify the module, the type of the custom attribute to search for, and

             an ignored search option.

            element: An object derived from the System.Reflection.Module class that describes a portable executable file.

            attributeType: The type, or a base type, of the custom attribute to search for.

            inherit: This parameter is ignored, and does not affect the operation of this method.

            Returns: ue if a custom attribute of type attributeType is applied to element; otherwise, lse.

        IsDefined(element: Assembly, attributeType: Type) -> bool

            Determines whether any custom attributes are applied to an assembly. Parameters specify the assembly, and the type of the custom attribute to search

             for.

            element: An object derived from the System.Reflection.Assembly class that describes a reusable collection of modules.

            attributeType: The type, or a base type, of the custom attribute to search for.

            Returns: ue if a custom attribute of type attributeType is applied to element; otherwise, lse.

        IsDefined(element: Assembly, attributeType: Type, inherit: bool) -> bool

            Determines whether any custom attributes are applied to an assembly. Parameters specify the assembly, the type of the custom attribute to search for,

             and an ignored search option.

            element: An object derived from the System.Reflection.Assembly class that describes a reusable collection of modules.

            attributeType: The type, or a base type, of the custom attribute to search for.

            inherit: This parameter is ignored, and does not affect the operation of this method.

            Returns: ue if a custom attribute of type attributeType is applied to element; otherwise, lse.
        """
        ...

    def Match(self, obj):
        """
        Match(self: Attribute, obj: object) -> bool

            When overridden in a derived class, returns a value that indicates whether this instance equals a specified object.

            obj: An System.Object to compare with this instance of System.Attribute.

            Returns: ue if this instance equals obj; otherwise, lse.
        """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class AttributeTargets(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>
    """
    Specifies the application elements on which it is valid to apply an attribute.

    enum (flags) AttributeTargets, values: All (32767), Assembly (1), Class (4), Constructor (32), Delegate (4096), Enum (16), Event (512), Field (256), GenericParameter (16384), Interface (1024), Method (64), Module (2), Parameter (2048), Property (128), ReturnValue (8192), Struct (8)
    """
    All = None
    Assembly = None
    Class = None
    Constructor = None
    Delegate = None
    Enum = None
    Event = None
    Field = None
    GenericParameter = None
    Interface = None
    Method = None
    Module = None
    Parameter = None
    Property = None
    ReturnValue = None
    Struct = None
    value__ = None


class AttributeUsageAttribute(Attribute): # skipped bases: <type '_Attribute'>
    """
    Specifies the usage of another attribute class. This class cannot be inherited.

    AttributeUsageAttribute(validOn: AttributeTargets)
    """
    @property
    def AllowMultiple(self):
        """
        Gets or sets a Boolean value indicating whether more than one instance of the indicated attribute can be specified for a single program element.

        Get: AllowMultiple(self: AttributeUsageAttribute) -> bool

        Set: AllowMultiple(self: AttributeUsageAttribute) = value
        """
        ...

    @property
    def Inherited(self):
        """
        Gets or sets a System.Boolean value that determines whether the indicated attribute is inherited by derived classes and overriding members.

        Get: Inherited(self: AttributeUsageAttribute) -> bool

        Set: Inherited(self: AttributeUsageAttribute) = value
        """
        ...

    @property
    def ValidOn(self):
        """
        Gets a set of values identifying which program elements that the indicated attribute can be applied to.

        Get: ValidOn(self: AttributeUsageAttribute) -> AttributeTargets
        """
        ...


    @staticmethod # known case of __new__
    def __new__(cls, validOn):
        """ __new__(cls: type, validOn: AttributeTargets) """
        ...


class BadImageFormatException(SystemException): # skipped bases: <type 'ISerializable'>, <type '_Exception'>
    """
    The exception that is thrown when the file image of a dynamic link library (DLL) or an executable program is invalid.

    BadImageFormatException()

    BadImageFormatException(message: str)

    BadImageFormatException(message: str, inner: Exception)

    BadImageFormatException(message: str, fileName: str)

    BadImageFormatException(message: str, fileName: str, inner: Exception)
    """
    @property
    def FileName(self):
        """
        Gets the name of the file that causes this exception.

        Get: FileName(self: BadImageFormatException) -> str
        """
        ...

    @property
    def FusionLog(self):
        """
        Gets the log file that describes why an assembly load failed.

        Get: FusionLog(self: BadImageFormatException) -> str
        """
        ...


    SerializeObjectState = None


class Base64FormattingOptions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>
    """
    Specifies whether relevant erload:System.Convert.ToBase64CharArray and erload:System.Convert.ToBase64String methods insert line breaks in their output.

    enum (flags) Base64FormattingOptions, values: InsertLineBreaks (1), None (0)
    """
    InsertLineBreaks = None

    value__ = None


class BitConverter: # skipped bases: <type 'object'>
    """ Converts base data types to an array of bytes, and an array of bytes to base data types. """
    @staticmethod
    def DoubleToInt64Bits(value):
        """
        DoubleToInt64Bits(value: float) -> Int64

            Converts the specified double-precision floating point number to a 64-bit signed integer.

            value: The number to convert.

            Returns: A 64-bit signed integer whose value is equivalent to value.
        """
        ...

    @staticmethod
    def GetBytes(value):
        """
        GetBytes(value: bool) -> Array[Byte]

            Returns the specified Boolean value as a byte array.

            value: A Boolean value.

            Returns: A byte array with length 1.

        GetBytes(value: Char) -> Array[Byte]

            Returns the specified Unicode character value as an array of bytes.

            value: A character to convert.

            Returns: An array of bytes with length 2.

        GetBytes(value: Int16) -> Array[Byte]

            Returns the specified 16-bit signed integer value as an array of bytes.

            value: The number to convert.

            Returns: An array of bytes with length 2.

        GetBytes(value: int) -> Array[Byte]

            Returns the specified 32-bit signed integer value as an array of bytes.

            value: The number to convert.

            Returns: An array of bytes with length 4.

        GetBytes(value: Int64) -> Array[Byte]

            Returns the specified 64-bit signed integer value as an array of bytes.

            value: The number to convert.

            Returns: An array of bytes with length 8.

        GetBytes(value: UInt16) -> Array[Byte]

            Returns the specified 16-bit unsigned integer value as an array of bytes.

            value: The number to convert.

            Returns: An array of bytes with length 2.

        GetBytes(value: UInt32) -> Array[Byte]

            Returns the specified 32-bit unsigned integer value as an array of bytes.

            value: The number to convert.

            Returns: An array of bytes with length 4.

        GetBytes(value: UInt64) -> Array[Byte]

            Returns the specified 64-bit unsigned integer value as an array of bytes.

            value: The number to convert.

            Returns: An array of bytes with length 8.

        GetBytes(value: Single) -> Array[Byte]

            Returns the specified single-precision floating point value as an array of bytes.

            value: The number to convert.

            Returns: An array of bytes with length 4.

        GetBytes(value: float) -> Array[Byte]

            Returns the specified double-precision floating point value as an array of bytes.

            value: The number to convert.

            Returns: An array of bytes with length 8.
        """
        ...

    @staticmethod
    def Int64BitsToDouble(value):
        """
        Int64BitsToDouble(value: Int64) -> float

            Converts the specified 64-bit signed integer to a double-precision floating point number.

            value: The number to convert.

            Returns: A double-precision floating point number whose value is equivalent to value.
        """
        ...

    @staticmethod
    def ToBoolean(value, startIndex):
        """
        ToBoolean(value: Array[Byte], startIndex: int) -> bool

            Returns a Boolean value converted from the byte at a specified position in a byte array.

            value: A byte array.

            startIndex: The index of the byte within value.

            Returns: ue if the byte at startIndex in value is nonzero; otherwise, lse.
        """
        ...

    @staticmethod
    def ToChar(value, startIndex):
        """
        ToChar(value: Array[Byte], startIndex: int) -> Char

            Returns a Unicode character converted from two bytes at a specified position in a byte array.

            value: An array.

            startIndex: The starting position within value.

            Returns: A character formed by two bytes beginning at startIndex.
        """
        ...

    @staticmethod
    def ToDouble(value, startIndex):
        """
        ToDouble(value: Array[Byte], startIndex: int) -> float

            Returns a double-precision floating point number converted from eight bytes at a specified position in a byte array.

            value: An array of bytes.

            startIndex: The starting position within value.

            Returns: A double precision floating point number formed by eight bytes beginning at startIndex.
        """
        ...

    @staticmethod
    def ToInt16(value, startIndex):
        """
        ToInt16(value: Array[Byte], startIndex: int) -> Int16

            Returns a 16-bit signed integer converted from two bytes at a specified position in a byte array.

            value: An array of bytes.

            startIndex: The starting position within value.

            Returns: A 16-bit signed integer formed by two bytes beginning at startIndex.
        """
        ...

    @staticmethod
    def ToInt32(value, startIndex):
        """
        ToInt32(value: Array[Byte], startIndex: int) -> int

            Returns a 32-bit signed integer converted from four bytes at a specified position in a byte array.

            value: An array of bytes.

            startIndex: The starting position within value.

            Returns: A 32-bit signed integer formed by four bytes beginning at startIndex.
        """
        ...

    @staticmethod
    def ToInt64(value, startIndex):
        """
        ToInt64(value: Array[Byte], startIndex: int) -> Int64

            Returns a 64-bit signed integer converted from eight bytes at a specified position in a byte array.

            value: An array of bytes.

            startIndex: The starting position within value.

            Returns: A 64-bit signed integer formed by eight bytes beginning at startIndex.
        """
        ...

    @staticmethod
    def ToSingle(value, startIndex):
        """
        ToSingle(value: Array[Byte], startIndex: int) -> Single

            Returns a single-precision floating point number converted from four bytes at a specified position in a byte array.

            value: An array of bytes.

            startIndex: The starting position within value.

            Returns: A single-precision floating point number formed by four bytes beginning at startIndex.
        """
        ...

    @staticmethod
    def ToString(value=..., startIndex=..., length=...):
        """
        ToString(value: Array[Byte], startIndex: int, length: int) -> str

            Converts the numeric value of each element of a specified subarray of bytes to its equivalent hexadecimal string representation.

            value: An array of bytes.

            startIndex: The starting position within value.

            length: The number of array elements in value to convert.

            Returns: A string of hexadecimal pairs separated by hyphens, where each pair represents the corresponding element in a subarray of value; for example,

             "7F-2C-4A-00".

        ToString(value: Array[Byte]) -> str

            Converts the numeric value of each element of a specified array of bytes to its equivalent hexadecimal string representation.

            value: An array of bytes.

            Returns: A string of hexadecimal pairs separated by hyphens, where each pair represents the corresponding element in value; for example, "7F-2C-4A-00".

        ToString(value: Array[Byte], startIndex: int) -> str

            Converts the numeric value of each element of a specified subarray of bytes to its equivalent hexadecimal string representation.

            value: An array of bytes.

            startIndex: The starting position within value.

            Returns: A string of hexadecimal pairs separated by hyphens, where each pair represents the corresponding element in a subarray of value; for example,

             "7F-2C-4A-00".
        """
        ...

    @staticmethod
    def ToUInt16(value, startIndex):
        """
        ToUInt16(value: Array[Byte], startIndex: int) -> UInt16

            Returns a 16-bit unsigned integer converted from two bytes at a specified position in a byte array.

            value: The array of bytes.

            startIndex: The starting position within value.

            Returns: A 16-bit unsigned integer formed by two bytes beginning at startIndex.
        """
        ...

    @staticmethod
    def ToUInt32(value, startIndex):
        """
        ToUInt32(value: Array[Byte], startIndex: int) -> UInt32

            Returns a 32-bit unsigned integer converted from four bytes at a specified position in a byte array.

            value: An array of bytes.

            startIndex: The starting position within value.

            Returns: A 32-bit unsigned integer formed by four bytes beginning at startIndex.
        """
        ...

    @staticmethod
    def ToUInt64(value, startIndex):
        """
        ToUInt64(value: Array[Byte], startIndex: int) -> UInt64

            Returns a 64-bit unsigned integer converted from eight bytes at a specified position in a byte array.

            value: An array of bytes.

            startIndex: The starting position within value.

            Returns: A 64-bit unsigned integer formed by the eight bytes beginning at startIndex.
        """
        ...

    IsLittleEndian = True
    __all__ = [
        'DoubleToInt64Bits',
        'GetBytes',
        'Int64BitsToDouble',
        'IsLittleEndian',
        'ToBoolean',
        'ToChar',
        'ToDouble',
        'ToInt16',
        'ToInt32',
        'ToInt64',
        'ToSingle',
        'ToString',
        'ToUInt16',
        'ToUInt32',
        'ToUInt64',
    ]


class Int32: # skipped bases: <type 'object'>
    """ Represents a 32-bit signed integer.To browse the .NET Framework source code for this type, see the Reference Source. """
    def bit_length(self, *args): #cannot find CLR method
        """ bit_length(value: int) -> int """
        ...

    def conjugate(self, *args): #cannot find CLR method
        """ conjugate(x: int) -> int """
        ...

    def __abs__(self, *args): #cannot find CLR method
        """ x.__abs__() <==> abs(x) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __and__(self, *args): #cannot find CLR method
        """ __and__(x: int, y: int) -> int """
        ...

    def __cmp__(self, *args): #cannot find CLR method
        """ x.__cmp__(y) <==> cmp(x,y) """
        ...

    def __coerce__(self, *args): #cannot find CLR method
        """ __coerce__(x: int, o: object) -> object """
        ...

    def __divmod__(self, *args): #cannot find CLR method
        """
        __divmod__(x: int, y: int) -> tuple

        __divmod__(x: int, y: object) -> object
        """
        ...

    def __div__(self, *args): #cannot find CLR method
        """ x.__div__(y) <==> x/y """
        ...

    def __float__(self, *args): #cannot find CLR method
        """ __float__(self: int) -> float """
        ...

    def __floordiv__(self, *args): #cannot find CLR method
        """ x.__floordiv__(y) <==> x//y """
        ...

    def __getnewargs__(self, *args): #cannot find CLR method
        """ __getnewargs__(self: int) -> object """
        ...

    def __hex__(self, *args): #cannot find CLR method
        """ __hex__(x: int) -> str """
        ...

    def __index__(self, *args): #cannot find CLR method
        """ __index__(x: int) -> int """
        ...

    def __int__(self, *args): #cannot find CLR method
        """ __int__(self: int) -> int """
        ...

    def __invert__(self, *args): #cannot find CLR method
        """ __invert__(x: int) -> int """
        ...

    def __long__(self, *args): #cannot find CLR method
        """ __long__(self: int) -> long """
        ...

    def __lshift__(self, *args): #cannot find CLR method
        """ x.__rshift__(y) <==> x<<yx.__rshift__(y) <==> x<<y """
        ...

    def __mod__(self, *args): #cannot find CLR method
        """ x.__mod__(y) <==> x%y """
        ...

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*y """
        ...

    def __neg__(self, *args): #cannot find CLR method
        """ x.__neg__() <==> -x """
        ...

    def __nonzero__(self, *args): #cannot find CLR method
        """ __nonzero__(x: int) -> bool """
        ...

    def __oct__(self, *args): #cannot find CLR method
        """ __oct__(x: int) -> str """
        ...

    def __or__(self, *args): #cannot find CLR method
        """ __or__(x: int, y: int) -> int """
        ...

    def __pos__(self, *args): #cannot find CLR method
        """ __pos__(x: int) -> int """
        ...

    def __pow__(self, *args): #cannot find CLR method
        """ x.__pow__(y[, z]) <==> pow(x, y[, z])x.__pow__(y[, z]) <==> pow(x, y[, z])x.__pow__(y[, z]) <==> pow(x, y[, z])x.__pow__(y[, z]) <==> pow(x, y[, z]) """
        ...

    def __radd__(self, *args): #cannot find CLR method
        """ __radd__(x: int, y: int) -> object """
        ...

    def __rand__(self, *args): #cannot find CLR method
        """ __rand__(x: int, y: int) -> int """
        ...

    def __rdivmod__(self, *args): #cannot find CLR method
        """ __rdivmod__(x: int, y: int) -> object """
        ...

    def __rdiv__(self, *args): #cannot find CLR method
        """ __rdiv__(x: int, y: int) -> object """
        ...

    def __rfloordiv__(self, *args): #cannot find CLR method
        """ __rfloordiv__(x: int, y: int) -> object """
        ...

    def __rlshift__(self, *args): #cannot find CLR method
        """ __rlshift__(x: int, y: int) -> object """
        ...

    def __rmod__(self, *args): #cannot find CLR method
        """ __rmod__(x: int, y: int) -> int """
        ...

    def __rmul__(self, *args): #cannot find CLR method
        """ __rmul__(x: int, y: int) -> object """
        ...

    def __ror__(self, *args): #cannot find CLR method
        """ __ror__(x: int, y: int) -> int """
        ...

    def __rpow__(self, *args): #cannot find CLR method
        """
        __rpow__(x: int, power: long, qmod: long) -> object

        __rpow__(x: int, power: float, qmod: float) -> object

        __rpow__(x: int, power: int, qmod: Nullable[int]) -> object

        __rpow__(x: int, power: int) -> object
        """
        ...

    def __rrshift__(self, *args): #cannot find CLR method
        """ __rrshift__(x: int, y: int) -> int """
        ...

    def __rshift__(self, *args): #cannot find CLR method
        """ x.__rshift__(y) <==> x>>yx.__rshift__(y) <==> x>>y """
        ...

    def __rsub__(self, *args): #cannot find CLR method
        """ __rsub__(x: int, y: int) -> object """
        ...

    def __rtruediv__(self, *args): #cannot find CLR method
        """ __rtruediv__(x: int, y: int) -> float """
        ...

    def __rxor__(self, *args): #cannot find CLR method
        """ __rxor__(x: int, y: int) -> int """
        ...

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        ...

    def __truediv__(self, *args): #cannot find CLR method
        """ x.__truediv__(y) <==> x/y """
        ...

    def __trunc__(self, *args): #cannot find CLR method
        """ __trunc__(x: int) -> int """
        ...

    def __xor__(self, *args): #cannot find CLR method
        """ __xor__(x: int, y: int) -> int """
        ...

    denominator = None
    imag = None
    numerator = None
    real = None


class Boolean(int):
    """ Represents a Boolean (ue or lse) value. """
    pass

class Buffer: # skipped bases: <type 'object'>
    """ Manipulates arrays of primitive types. """
    @staticmethod
    def BlockCopy(src, srcOffset, dst, dstOffset, count):
        """
        BlockCopy(src: Array, srcOffset: int, dst: Array, dstOffset: int, count: int)

            Copies a specified number of bytes from a source array starting at a particular offset to a destination array starting at a particular offset.

            src: The source buffer.

            srcOffset: The zero-based byte offset into src.

            dst: The destination buffer.

            dstOffset: The zero-based byte offset into dst.

            count: The number of bytes to copy.
        """
        ...

    @staticmethod
    def ByteLength(array):
        """
        ByteLength(array: Array) -> int

            Returns the number of bytes in the specified array.

            array: An array.

            Returns: The number of bytes in the array.
        """
        ...

    @staticmethod
    def GetByte(array, index):
        """
        GetByte(array: Array, index: int) -> Byte

            Retrieves the byte at a specified location in a specified array.

            array: An array.

            index: A location in the array.

            Returns: Returns the index byte in the array.
        """
        ...

    @staticmethod
    def MemoryCopy(source, destination, destinationSizeInBytes, sourceBytesToCopy):
        """
        MemoryCopy(source: Void*, destination: Void*, destinationSizeInBytes: Int64, sourceBytesToCopy: Int64)

            Copies a number of bytes specified as a long integer value from one address in memory to another. This API is not CLS-compliant.

            source: The address of the bytes to copy.

            destination: The target address.

            destinationSizeInBytes: The number of bytes available in the destination memory block.

            sourceBytesToCopy: The number of bytes to copy.

        MemoryCopy(source: Void*, destination: Void*, destinationSizeInBytes: UInt64, sourceBytesToCopy: UInt64)

            Copies a number of bytes specified as an unsigned long integer value from one address in memory to another. This API is not CLS-compliant.

            source: The address of the bytes to copy.

            destination: The target address.

            destinationSizeInBytes: The number of bytes available in the destination memory block.

            sourceBytesToCopy: The number of bytes to copy.
        """
        ...

    @staticmethod
    def SetByte(array, index, value):
        """
        SetByte(array: Array, index: int, value: Byte)

            Assigns a specified value to a byte at a particular location in a specified array.

            array: An array.

            index: A location in the array.

            value: A value to assign.
        """
        ...

    __all__ = [
        'BlockCopy',
        'ByteLength',
        'GetByte',
        'MemoryCopy',
        'SetByte',
    ]


class Byte( IComparable, IFormattable, IConvertible, IEquatable):
    """ Represents an 8-bit unsigned integer. """
    def bit_length(self, *args): #cannot find CLR method
        """ bit_length(value: Byte) -> int """
        ...

    def conjugate(self, *args): #cannot find CLR method
        """ conjugate(x: Byte) -> Byte """
        ...

    def GetHashCode(self):
        """
        GetHashCode(self: Byte) -> int

            Returns the hash code for this instance.

            Returns: A hash code for the current System.Byte.
        """
        ...

    @staticmethod
    def Parse(s, *__args):
        """
        Parse(s: str) -> Byte

            Converts the string representation of a number to its System.Byte equivalent.

            s: A string that contains a number to convert. The string is interpreted using the System.Globalization.NumberStyles.Integer style.

            Returns: A byte value that is equivalent to the number contained in s.

        Parse(s: str, style: NumberStyles) -> Byte

            Converts the string representation of a number in a specified style to its System.Byte equivalent.

            s: A string that contains a number to convert. The string is interpreted using the style specified by style.

            style: A bitwise combination of enumeration values that indicates the style elements that can be present in s. A typical value to specify is

             System.Globalization.NumberStyles.Integer.

            Returns: A byte value that is equivalent to the number contained in s.

        Parse(s: str, provider: IFormatProvider) -> Byte

            Converts the string representation of a number in a specified culture-specific format to its System.Byte equivalent.

            s: A string that contains a number to convert. The string is interpreted using the System.Globalization.NumberStyles.Integer style.

            provider: An object that supplies culture-specific parsing information about s. If provider is ll, the thread current culture is used.

            Returns: A byte value that is equivalent to the number contained in s.

        Parse(s: str, style: NumberStyles, provider: IFormatProvider) -> Byte

            Converts the string representation of a number in a specified style and culture-specific format to its System.Byte equivalent.

            s: A string that contains a number to convert. The string is interpreted using the style specified by style.

            style: A bitwise combination of enumeration values that indicates the style elements that can be present in s. A typical value to specify is

             System.Globalization.NumberStyles.Integer.

            provider: An object that supplies culture-specific information about the format of s. If provider is ll, the thread current culture is used.

            Returns: A byte value that is equivalent to the number contained in s.
        """
        ...

    @staticmethod
    def TryParse(s, *__args):
        """
        TryParse(s: str) -> (bool, Byte)

            Tries to convert the string representation of a number to its System.Byte equivalent, and returns a value that indicates whether the conversion

             succeeded.

            s: A string that contains a number to convert. The string is interpreted using the System.Globalization.NumberStyles.Integer style.

            Returns: ue if s was converted successfully; otherwise, lse.

        TryParse(s: str, style: NumberStyles, provider: IFormatProvider) -> (bool, Byte)

            Converts the string representation of a number in a specified style and culture-specific format to its System.Byte equivalent. A return value

             indicates whether the conversion succeeded or failed.

            s: A string containing a number to convert. The string is interpreted using the style specified by style.

            style: A bitwise combination of enumeration values that indicates the style elements that can be present in s. A typical value to specify is

             System.Globalization.NumberStyles.Integer.

            provider: An object that supplies culture-specific formatting information about s. If provider is ll, the thread current culture is used.

            Returns: ue if s was converted successfully; otherwise, lse.
        """
        ...

    def __abs__(self, *args): #cannot find CLR method
        """ x.__abs__() <==> abs(x) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        ...

    def __and__(self, *args): #cannot find CLR method
        """
        __and__(x: Byte, y: Byte) -> Byte

        __and__(x: Byte, y: SByte) -> Int16
        """
        ...

    def __cmp__(self, *args): #cannot find CLR method
        """ x.__cmp__(y) <==> cmp(x,y)x.__cmp__(y) <==> cmp(x,y) """
        ...

    def __div__(self, *args): #cannot find CLR method
        """ x.__div__(y) <==> x/yx.__div__(y) <==> x/y """
        ...

    def __float__(self, *args): #cannot find CLR method
        """ __float__(x: Byte) -> float """
        ...

    def __floordiv__(self, *args): #cannot find CLR method
        """ x.__floordiv__(y) <==> x//yx.__floordiv__(y) <==> x//y """
        ...

    def __hex__(self, *args): #cannot find CLR method
        """ __hex__(value: Byte) -> str """
        ...

    def __index__(self, *args): #cannot find CLR method
        """ __index__(x: Byte) -> int """
        ...

    def __int__(self, *args): #cannot find CLR method
        """ __int__(x: Byte) -> int """
        ...

    def __invert__(self, *args): #cannot find CLR method
        """ __invert__(x: Byte) -> object """
        ...

    def __lshift__(self, *args): #cannot find CLR method
        """ x.__rshift__(y) <==> x<<yx.__rshift__(y) <==> x<<y """
        ...

    def __mod__(self, *args): #cannot find CLR method
        """ x.__mod__(y) <==> x%yx.__mod__(y) <==> x%y """
        ...

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*yx.__mul__(y) <==> x*y """
        ...

    def __neg__(self, *args): #cannot find CLR method
        """ x.__neg__() <==> -x """
        ...

    def __nonzero__(self, *args): #cannot find CLR method
        """ __nonzero__(x: Byte) -> bool """
        ...

    def __or__(self, *args): #cannot find CLR method
        """
        __or__(x: Byte, y: Byte) -> Byte

        __or__(x: Byte, y: SByte) -> Int16
        """
        ...

    def __pos__(self, *args): #cannot find CLR method
        """ __pos__(x: Byte) -> Byte """
        ...

    def __pow__(self, *args): #cannot find CLR method
        """ x.__pow__(y[, z]) <==> pow(x, y[, z])x.__pow__(y[, z]) <==> pow(x, y[, z]) """
        ...

    def __radd__(self, *args): #cannot find CLR method
        """
        __radd__(x: Byte, y: Byte) -> object

        __radd__(x: SByte, y: Byte) -> object
        """
        ...

    def __rand__(self, *args): #cannot find CLR method
        """
        __rand__(x: Byte, y: Byte) -> Byte

        __rand__(x: SByte, y: Byte) -> Int16
        """
        ...

    def __rdiv__(self, *args): #cannot find CLR method
        """
        __rdiv__(x: Byte, y: Byte) -> object

        __rdiv__(x: SByte, y: Byte) -> object
        """
        ...

    def __rfloordiv__(self, *args): #cannot find CLR method
        """
        __rfloordiv__(x: Byte, y: Byte) -> Byte

        __rfloordiv__(x: SByte, y: Byte) -> object
        """
        ...

    def __rmod__(self, *args): #cannot find CLR method
        """
        __rmod__(x: Byte, y: Byte) -> Byte

        __rmod__(x: SByte, y: Byte) -> Int16
        """
        ...

    def __rmul__(self, *args): #cannot find CLR method
        """
        __rmul__(x: Byte, y: Byte) -> object

        __rmul__(x: SByte, y: Byte) -> object
        """
        ...

    def __ror__(self, *args): #cannot find CLR method
        """
        __ror__(x: Byte, y: Byte) -> Byte

        __ror__(x: SByte, y: Byte) -> Int16
        """
        ...

    def __rpow__(self, *args): #cannot find CLR method
        """
        __rpow__(x: Byte, y: Byte) -> object

        __rpow__(x: SByte, y: Byte) -> object
        """
        ...

    def __rshift__(self, *args): #cannot find CLR method
        """ x.__rshift__(y) <==> x>>yx.__rshift__(y) <==> x>>y """
        ...

    def __rsub__(self, *args): #cannot find CLR method
        """
        __rsub__(x: Byte, y: Byte) -> object

        __rsub__(x: SByte, y: Byte) -> object
        """
        ...

    def __rtruediv__(self, *args): #cannot find CLR method
        """
        __rtruediv__(x: Byte, y: Byte) -> float

        __rtruediv__(x: SByte, y: Byte) -> float
        """
        ...

    def __rxor__(self, *args): #cannot find CLR method
        """
        __rxor__(x: Byte, y: Byte) -> Byte

        __rxor__(x: SByte, y: Byte) -> Int16
        """
        ...

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-yx.__sub__(y) <==> x-y """
        ...

    def __truediv__(self, *args): #cannot find CLR method
        """ x.__truediv__(y) <==> x/yx.__truediv__(y) <==> x/y """
        ...

    def __trunc__(self, *args): #cannot find CLR method
        """ __trunc__(x: Byte) -> Byte """
        ...

    def __xor__(self, *args): #cannot find CLR method
        """
        __xor__(x: Byte, y: Byte) -> Byte

        __xor__(x: Byte, y: SByte) -> Int16
        """
        ...

    denominator = None
    imag = None
    MaxValue = None
    MinValue = None
    numerator = None
    real = None


class CannotUnloadAppDomainException(SystemException): # skipped bases: <type 'ISerializable'>, <type '_Exception'>
    """
    The exception that is thrown when an attempt to unload an application domain fails.

    CannotUnloadAppDomainException()

    CannotUnloadAppDomainException(message: str)

    CannotUnloadAppDomainException(message: str, innerException: Exception)
    """
    SerializeObjectState = None


class Char( IComparable, IConvertible, IEquatable):
    """ Represents a character as a UTF-16 code unit. """
    @staticmethod
    def ConvertFromUtf32(utf32):
        """
        ConvertFromUtf32(utf32: int) -> str

            Converts the specified Unicode code point into a UTF-16 encoded string.

            utf32: A 21-bit Unicode code point.

            Returns: A string consisting of one System.Char object or a surrogate pair of System.Char objects equivalent to the code point specified by the utf32

             parameter.
        """
        ...

    @staticmethod
    def ConvertToUtf32(*__args):
        """
        ConvertToUtf32(highSurrogate: Char, lowSurrogate: Char) -> int

            Converts the value of a UTF-16 encoded surrogate pair into a Unicode code point.

            highSurrogate: A high surrogate code unit (that is, a code unit ranging from U+D800 through U+DBFF).

            lowSurrogate: A low surrogate code unit (that is, a code unit ranging from U+DC00 through U+DFFF).

            Returns: The 21-bit Unicode code point represented by the highSurrogate and lowSurrogate parameters.

        ConvertToUtf32(s: str, index: int) -> int

            Converts the value of a UTF-16 encoded character or surrogate pair at a specified position in a string into a Unicode code point.

            s: A string that contains a character or surrogate pair.

            index: The index position of the character or surrogate pair in s.

            Returns: The 21-bit Unicode code point represented by the character or surrogate pair at the position in the s parameter specified by the index parameter.
        """
        ...

    def GetHashCode(self):
        """
        GetHashCode(self: Char) -> int

            Returns the hash code for this instance.

            Returns: A 32-bit signed integer hash code.
        """
        ...

    @staticmethod
    def GetNumericValue(*__args):
        """
        GetNumericValue(c: Char) -> float

            Converts the specified numeric Unicode character to a double-precision floating point number.

            c: The Unicode character to convert.

            Returns: The numeric value of c if that character represents a number; otherwise, -1.0.

        GetNumericValue(s: str, index: int) -> float

            Converts the numeric Unicode character at the specified position in a specified string to a double-precision floating point number.

            s: A System.String.

            index: The character position in s.

            Returns: The numeric value of the character at position index in s if that character represents a number; otherwise, -1.
        """
        ...

    @staticmethod
    def GetUnicodeCategory(*__args):
        """
        GetUnicodeCategory(c: Char) -> UnicodeCategory

            Categorizes a specified Unicode character into a group identified by one of the System.Globalization.UnicodeCategory values.

            c: The Unicode character to categorize.

            Returns: A System.Globalization.UnicodeCategory value that identifies the group that contains c.

        GetUnicodeCategory(s: str, index: int) -> UnicodeCategory

            Categorizes the character at the specified position in a specified string into a group identified by one of the System.Globalization.UnicodeCategory

             values.

            s: A System.String.

            index: The character position in s.

            Returns: A System.Globalization.UnicodeCategory enumerated constant that identifies the group that contains the character at position index in s.
        """
        ...

    @staticmethod
    def IsControl(*__args):
        """
        IsControl(c: Char) -> bool

            Indicates whether the specified Unicode character is categorized as a control character.

            c: The Unicode character to evaluate.

            Returns: ue if c is a control character; otherwise, lse.

        IsControl(s: str, index: int) -> bool

            Indicates whether the character at the specified position in a specified string is categorized as a control character.

            s: A string.

            index: The position of the character to evaluate in s.

            Returns: ue if the character at position index in s is a control character; otherwise, lse.
        """
        ...

    @staticmethod
    def IsDigit(*__args):
        """
        IsDigit(c: Char) -> bool

            Indicates whether the specified Unicode character is categorized as a decimal digit.

            c: The Unicode character to evaluate.

            Returns: ue if c is a decimal digit; otherwise, lse.

        IsDigit(s: str, index: int) -> bool

            Indicates whether the character at the specified position in a specified string is categorized as a decimal digit.

            s: A string.

            index: The position of the character to evaluate in s.

            Returns: ue if the character at position index in s is a decimal digit; otherwise, lse.
        """
        ...

    @staticmethod
    def IsHighSurrogate(*__args):
        """
        IsHighSurrogate(c: Char) -> bool

            Indicates whether the specified System.Char object is a high surrogate.

            c: The Unicode character to evaluate.

            Returns: ue if the numeric value of the c parameter ranges from U+D800 through U+DBFF; otherwise, lse.

        IsHighSurrogate(s: str, index: int) -> bool

            Indicates whether the System.Char object at the specified position in a string is a high surrogate.

            s: A string.

            index: The position of the character to evaluate in s.

            Returns: ue if the numeric value of the specified character in the s parameter ranges from U+D800 through U+DBFF; otherwise, lse.
        """
        ...

    @staticmethod
    def IsLetter(*__args):
        """
        IsLetter(c: Char) -> bool

            Indicates whether the specified Unicode character is categorized as a Unicode letter.

            c: The Unicode character to evaluate.

            Returns: ue if c is a letter; otherwise, lse.

        IsLetter(s: str, index: int) -> bool

            Indicates whether the character at the specified position in a specified string is categorized as a Unicode letter.

            s: A string.

            index: The position of the character to evaluate in s.

            Returns: ue if the character at position index in s is a letter; otherwise, lse.
        """
        ...

    @staticmethod
    def IsLetterOrDigit(*__args):
        """
        IsLetterOrDigit(c: Char) -> bool

            Indicates whether the specified Unicode character is categorized as a letter or a decimal digit.

            c: The Unicode character to evaluate.

            Returns: ue if c is a letter or a decimal digit; otherwise, lse.

        IsLetterOrDigit(s: str, index: int) -> bool

            Indicates whether the character at the specified position in a specified string is categorized as a letter or a decimal digit.

            s: A string.

            index: The position of the character to evaluate in s.

            Returns: ue if the character at position index in s is a letter or a decimal digit; otherwise, lse.
        """
        ...

    @staticmethod
    def IsLower(*__args):
        """
        IsLower(c: Char) -> bool

            Indicates whether the specified Unicode character is categorized as a lowercase letter.

            c: The Unicode character to evaluate.

            Returns: ue if c is a lowercase letter; otherwise, lse.

        IsLower(s: str, index: int) -> bool

            Indicates whether the character at the specified position in a specified string is categorized as a lowercase letter.

            s: A string.

            index: The position of the character to evaluate in s.

            Returns: ue if the character at position index in s is a lowercase letter; otherwise, lse.
        """
        ...

    @staticmethod
    def IsLowSurrogate(*__args):
        """
        IsLowSurrogate(c: Char) -> bool

            Indicates whether the specified System.Char object is a low surrogate.

            c: The character to evaluate.

            Returns: ue if the numeric value of the c parameter ranges from U+DC00 through U+DFFF; otherwise, lse.

        IsLowSurrogate(s: str, index: int) -> bool

            Indicates whether the System.Char object at the specified position in a string is a low surrogate.

            s: A string.

            index: The position of the character to evaluate in s.

            Returns: ue if the numeric value of the specified character in the s parameter ranges from U+DC00 through U+DFFF; otherwise, lse.
        """
        ...

    @staticmethod
    def IsNumber(*__args):
        """
        IsNumber(c: Char) -> bool

            Indicates whether the specified Unicode character is categorized as a number.

            c: The Unicode character to evaluate.

            Returns: ue if c is a number; otherwise, lse.

        IsNumber(s: str, index: int) -> bool

            Indicates whether the character at the specified position in a specified string is categorized as a number.

            s: A string.

            index: The position of the character to evaluate in s.

            Returns: ue if the character at position index in s is a number; otherwise, lse.
        """
        ...

    @staticmethod
    def IsPunctuation(*__args):
        """
        IsPunctuation(c: Char) -> bool

            Indicates whether the specified Unicode character is categorized as a punctuation mark.

            c: The Unicode character to evaluate.

            Returns: ue if c is a punctuation mark; otherwise, lse.

        IsPunctuation(s: str, index: int) -> bool

            Indicates whether the character at the specified position in a specified string is categorized as a punctuation mark.

            s: A string.

            index: The position of the character to evaluate in s.

            Returns: ue if the character at position index in s is a punctuation mark; otherwise, lse.
        """
        ...

    @staticmethod
    def IsSeparator(*__args):
        """
        IsSeparator(c: Char) -> bool

            Indicates whether the specified Unicode character is categorized as a separator character.

            c: The Unicode character to evaluate.

            Returns: ue if c is a separator character; otherwise, lse.

        IsSeparator(s: str, index: int) -> bool

            Indicates whether the character at the specified position in a specified string is categorized as a separator character.

            s: A string.

            index: The position of the character to evaluate in s.

            Returns: ue if the character at position index in s is a separator character; otherwise, lse.
        """
        ...

    @staticmethod
    def IsSurrogate(*__args):
        """
        IsSurrogate(c: Char) -> bool

            Indicates whether the specified character has a surrogate code unit.

            c: The Unicode character to evaluate.

            Returns: ue if c is either a high surrogate or a low surrogate; otherwise, lse.

        IsSurrogate(s: str, index: int) -> bool

            Indicates whether the character at the specified position in a specified string has a surrogate code unit.

            s: A string.

            index: The position of the character to evaluate in s.

            Returns: ue if the character at position index in s is a either a high surrogate or a low surrogate; otherwise, lse.
        """
        ...

    @staticmethod
    def IsSurrogatePair(*__args):
        """
        IsSurrogatePair(s: str, index: int) -> bool

            Indicates whether two adjacent System.Char objects at a specified position in a string form a surrogate pair.

            s: A string.

            index: The starting position of the pair of characters to evaluate within s.

            Returns: ue if the s parameter includes adjacent characters at positions index and index + 1, and the numeric value of the character at position index ranges

             from U+D800 through U+DBFF, and the numeric value of the character at position index+1 ranges from U+DC00 through U+DFFF; otherwise, lse.

        IsSurrogatePair(highSurrogate: Char, lowSurrogate: Char) -> bool

            Indicates whether the two specified System.Char objects form a surrogate pair.

            highSurrogate: The character to evaluate as the high surrogate of a surrogate pair.

            lowSurrogate: The character to evaluate as the low surrogate of a surrogate pair.

            Returns: ue if the numeric value of the highSurrogate parameter ranges from U+D800 through U+DBFF, and the numeric value of the lowSurrogate parameter ranges

             from U+DC00 through U+DFFF; otherwise, lse.
        """
        ...

    @staticmethod
    def IsSymbol(*__args):
        """
        IsSymbol(c: Char) -> bool

            Indicates whether the specified Unicode character is categorized as a symbol character.

            c: The Unicode character to evaluate.

            Returns: ue if c is a symbol character; otherwise, lse.

        IsSymbol(s: str, index: int) -> bool

            Indicates whether the character at the specified position in a specified string is categorized as a symbol character.

            s: A string.

            index: The position of the character to evaluate in s.

            Returns: ue if the character at position index in s is a symbol character; otherwise, lse.
        """
        ...

    @staticmethod
    def IsUpper(*__args):
        """
        IsUpper(c: Char) -> bool

            Indicates whether the specified Unicode character is categorized as an uppercase letter.

            c: The Unicode character to evaluate.

            Returns: ue if c is an uppercase letter; otherwise, lse.

        IsUpper(s: str, index: int) -> bool

            Indicates whether the character at the specified position in a specified string is categorized as an uppercase letter.

            s: A string.

            index: The position of the character to evaluate in s.

            Returns: ue if the character at position index in s is an uppercase letter; otherwise, lse.
        """
        ...

    @staticmethod
    def IsWhiteSpace(*__args):
        """
        IsWhiteSpace(c: Char) -> bool

            Indicates whether the specified Unicode character is categorized as white space.

            c: The Unicode character to evaluate.

            Returns: ue if c is white space; otherwise, lse.

        IsWhiteSpace(s: str, index: int) -> bool

            Indicates whether the character at the specified position in a specified string is categorized as white space.

            s: A string.

            index: The position of the character to evaluate in s.

            Returns: ue if the character at position index in s is white space; otherwise, lse.
        """
        ...

    @staticmethod
    def Parse(s):
        """
        Parse(s: str) -> Char

            Converts the value of the specified string to its equivalent Unicode character.

            s: A string that contains a single character, or ll.

            Returns: A Unicode character equivalent to the sole character in s.
        """
        ...

    @staticmethod
    def ToLower(c, culture=...):
        """
        ToLower(c: Char, culture: CultureInfo) -> Char

            Converts the value of a specified Unicode character to its lowercase equivalent using specified culture-specific formatting information.

            c: The Unicode character to convert.

            culture: An object that supplies culture-specific casing rules.

            Returns: The lowercase equivalent of c, modified according to culture, or the unchanged value of c, if c is already lowercase or not alphabetic.

        ToLower(c: Char) -> Char

            Converts the value of a Unicode character to its lowercase equivalent.

            c: The Unicode character to convert.

            Returns: The lowercase equivalent of c, or the unchanged value of c, if c is already lowercase or not alphabetic.
        """
        ...

    @staticmethod
    def ToLowerInvariant(c):
        """
        ToLowerInvariant(c: Char) -> Char

            Converts the value of a Unicode character to its lowercase equivalent using the casing rules of the invariant culture.

            c: The Unicode character to convert.

            Returns: The lowercase equivalent of the c parameter, or the unchanged value of c, if c is already lowercase or not alphabetic.
        """
        ...

    @staticmethod
    def ToUpper(c, culture=...):
        """
        ToUpper(c: Char, culture: CultureInfo) -> Char

            Converts the value of a specified Unicode character to its uppercase equivalent using specified culture-specific formatting information.

            c: The Unicode character to convert.

            culture: An object that supplies culture-specific casing rules.

            Returns: The uppercase equivalent of c, modified according to culture, or the unchanged value of c if c is already uppercase, has no uppercase equivalent, or

             is not alphabetic.

        ToUpper(c: Char) -> Char

            Converts the value of a Unicode character to its uppercase equivalent.

            c: The Unicode character to convert.

            Returns: The uppercase equivalent of c, or the unchanged value of c if c is already uppercase, has no uppercase equivalent, or is not alphabetic.
        """
        ...

    @staticmethod
    def ToUpperInvariant(c):
        """
        ToUpperInvariant(c: Char) -> Char

            Converts the value of a Unicode character to its uppercase equivalent using the casing rules of the invariant culture.

            c: The Unicode character to convert.

            Returns: The uppercase equivalent of the c parameter, or the unchanged value of c, if c is already uppercase or not alphabetic.
        """
        ...

    @staticmethod
    def TryParse(s, result):
        """
        TryParse(s: str) -> (bool, Char)

            Converts the value of the specified string to its equivalent Unicode character. A return code indicates whether the conversion succeeded or failed.

            s: A string that contains a single character, or ll.

            Returns: ue if the s parameter was converted successfully; otherwise, lse.
        """
        ...

    def __cmp__(self, *args): #cannot find CLR method
        """ x.__cmp__(y) <==> cmp(x,y) """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """
        __contains__(self: Char, other: Char) -> bool

        __contains__(self: Char, other: str) -> bool
        """
        ...

    def __index__(self, *args): #cannot find CLR method
        """ __index__(self: Char) -> int """
        ...

    MaxValue = None
    MinValue = None


class CharEnumerator(ICloneable, IEnumerator[Char]): # skipped bases: <type 'IEnumerator'>, <type 'IDisposable'>
    """ Supports iterating over a System.String object and reading its individual characters. This class cannot be inherited. """
    def Dispose(self):
        """
        Dispose(self: CharEnumerator)

            Releases all resources used by the current instance of the System.CharEnumerator class.
        """
        ...

    def MoveNext(self):
        """
        MoveNext(self: CharEnumerator) -> bool

            Increments the internal index of the current System.CharEnumerator object to the next character of the enumerated string.

            Returns: ue if the index is successfully incremented and within the enumerated string; otherwise, lse.
        """
        ...

    def Reset(self):
        """
        Reset(self: CharEnumerator)

            Initializes the index to a position logically before the first character of the enumerated string.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[Char](enumerator: IEnumerator[Char], value: Char) -> bool """
        ...


class CLSCompliantAttribute(Attribute): # skipped bases: <type '_Attribute'>
    """
    Indicates whether a program element is compliant with the Common Language Specification (CLS). This class cannot be inherited.

    CLSCompliantAttribute(isCompliant: bool)
    """
    @property
    def IsCompliant(self):
        """
        Gets the Boolean value indicating whether the indicated program element is CLS-compliant.

        Get: IsCompliant(self: CLSCompliantAttribute) -> bool
        """
        ...


    @staticmethod # known case of __new__
    def __new__(cls, isCompliant):
        """ __new__(cls: type, isCompliant: bool) """
        ...


class Comparison(MulticastDelegate): # skipped bases: <type 'ICloneable'>, <type 'ISerializable'>
    """ Comparison[T](object: object, method: IntPtr) """
    def BeginInvoke(self, x, y, callback, object):
        """ BeginInvoke(self: Comparison[T], x: T, y: T, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result):
        """ EndInvoke(self: Comparison[T], result: IAsyncResult) -> int """
        ...

    def Invoke(self, x, y):
        """ Invoke(self: Comparison[T], x: T, y: T) -> int """
        ...


class Console: # skipped bases: <type 'object'>
    """ Represents the standard input, output, and error streams for console applications. This class cannot be inherited.To browse the .NET Framework source code for this type, see the Reference Source. """
    @property
    def BackgroundColor(self):
        """
        Gets or sets the background color of the console.

        Get: BackgroundColor() -> ConsoleColor

        Set: BackgroundColor() = value
        """
        ...

    @property
    def BufferHeight(self):
        """
        Gets or sets the height of the buffer area.

        Get: BufferHeight() -> int

        Set: BufferHeight() = value
        """
        ...

    @property
    def BufferWidth(self):
        """
        Gets or sets the width of the buffer area.

        Get: BufferWidth() -> int

        Set: BufferWidth() = value
        """
        ...

    @property
    def CapsLock(self):
        """
        Gets a value indicating whether the CAPS LOCK keyboard toggle is turned on or turned off.

        Get: CapsLock() -> bool
        """
        ...

    @property
    def CursorLeft(self):
        """
        Gets or sets the column position of the cursor within the buffer area.

        Get: CursorLeft() -> int

        Set: CursorLeft() = value
        """
        ...

    @property
    def CursorSize(self):
        """
        Gets or sets the height of the cursor within a character cell.

        Get: CursorSize() -> int

        Set: CursorSize() = value
        """
        ...

    @property
    def CursorTop(self):
        """
        Gets or sets the row position of the cursor within the buffer area.

        Get: CursorTop() -> int

        Set: CursorTop() = value
        """
        ...

    @property
    def CursorVisible(self):
        """
        Gets or sets a value indicating whether the cursor is visible.

        Get: CursorVisible() -> bool

        Set: CursorVisible() = value
        """
        ...

    @property
    def Error(self):
        """
        Gets the standard error output stream.

        Get: Error() -> TextWriter
        """
        ...

    @property
    def ForegroundColor(self):
        """
        Gets or sets the foreground color of the console.

        Get: ForegroundColor() -> ConsoleColor

        Set: ForegroundColor() = value
        """
        ...

    @property
    def In(self):
        """
        Gets the standard input stream.

        Get: In() -> TextReader
        """
        ...

    @property
    def InputEncoding(self):
        """
        Gets or sets the encoding the console uses to read input.

        Get: InputEncoding() -> Encoding

        Set: InputEncoding() = value
        """
        ...

    @property
    def IsErrorRedirected(self):
        """
        Gets a value that indicates whether the error output stream has been redirected from the standard error stream.

        Get: IsErrorRedirected() -> bool
        """
        ...

    @property
    def IsInputRedirected(self):
        """
        Gets a value that indicates whether input has been redirected from the standard input stream.

        Get: IsInputRedirected() -> bool
        """
        ...

    @property
    def IsOutputRedirected(self):
        """
        Gets a value that indicates whether output has been redirected from the standard output stream.

        Get: IsOutputRedirected() -> bool
        """
        ...

    @property
    def KeyAvailable(self):
        """
        Gets a value indicating whether a key press is available in the input stream.

        Get: KeyAvailable() -> bool
        """
        ...

    @property
    def LargestWindowHeight(self):
        """
        Gets the largest possible number of console window rows, based on the current font and screen resolution.

        Get: LargestWindowHeight() -> int
        """
        ...

    @property
    def LargestWindowWidth(self):
        """
        Gets the largest possible number of console window columns, based on the current font and screen resolution.

        Get: LargestWindowWidth() -> int
        """
        ...

    @property
    def NumberLock(self):
        """
        Gets a value indicating whether the NUM LOCK keyboard toggle is turned on or turned off.

        Get: NumberLock() -> bool
        """
        ...

    @property
    def Out(self):
        """
        Gets the standard output stream.

        Get: Out() -> TextWriter
        """
        ...

    @property
    def OutputEncoding(self):
        """
        Gets or sets the encoding the console uses to write output.

        Get: OutputEncoding() -> Encoding

        Set: OutputEncoding() = value
        """
        ...

    @property
    def Title(self):
        """
        Gets or sets the title to display in the console title bar.

        Get: Title() -> str

        Set: Title() = value
        """
        ...

    @property
    def TreatControlCAsInput(self):
        """
        Gets or sets a value indicating whether the combination of the System.ConsoleModifiers.Control modifier key and System.ConsoleKey.C console key (Ctrl+C) is treated as ordinary input or as an interruption that is handled by the operating system.

        Get: TreatControlCAsInput() -> bool

        Set: TreatControlCAsInput() = value
        """
        ...

    @property
    def WindowHeight(self):
        """
        Gets or sets the height of the console window area.

        Get: WindowHeight() -> int

        Set: WindowHeight() = value
        """
        ...

    @property
    def WindowLeft(self):
        """
        Gets or sets the leftmost position of the console window area relative to the screen buffer.

        Get: WindowLeft() -> int

        Set: WindowLeft() = value
        """
        ...

    @property
    def WindowTop(self):
        """
        Gets or sets the top position of the console window area relative to the screen buffer.

        Get: WindowTop() -> int

        Set: WindowTop() = value
        """
        ...

    @property
    def WindowWidth(self):
        """
        Gets or sets the width of the console window.

        Get: WindowWidth() -> int

        Set: WindowWidth() = value
        """
        ...


    @staticmethod
    def Beep(frequency=..., duration=...):
        """
        Beep()

            Plays the sound of a beep through the console speaker.

        Beep(frequency: int, duration: int)

            Plays the sound of a beep of a specified frequency and duration through the console speaker.

            frequency: The frequency of the beep, ranging from 37 to 32767 hertz.

            duration: The duration of the beep measured in milliseconds.
        """
        ...

    @staticmethod
    def Clear():
        """
        Clear()

            Clears the console buffer and corresponding console window of display information.
        """
        ...

    @staticmethod
    def MoveBufferArea(sourceLeft, sourceTop, sourceWidth, sourceHeight, targetLeft, targetTop, sourceChar=..., sourceForeColor=..., sourceBackColor=...):
        """
        MoveBufferArea(sourceLeft: int, sourceTop: int, sourceWidth: int, sourceHeight: int, targetLeft: int, targetTop: int)

            Copies a specified source area of the screen buffer to a specified destination area.

            sourceLeft: The leftmost column of the source area.

            sourceTop: The topmost row of the source area.

            sourceWidth: The number of columns in the source area.

            sourceHeight: The number of rows in the source area.

            targetLeft: The leftmost column of the destination area.

            targetTop: The topmost row of the destination area.

        MoveBufferArea(sourceLeft: int, sourceTop: int, sourceWidth: int, sourceHeight: int, targetLeft: int, targetTop: int, sourceChar: Char, sourceForeColor: ConsoleColor, sourceBackColor: ConsoleColor)

            Copies a specified source area of the screen buffer to a specified destination area.

            sourceLeft: The leftmost column of the source area.

            sourceTop: The topmost row of the source area.

            sourceWidth: The number of columns in the source area.

            sourceHeight: The number of rows in the source area.

            targetLeft: The leftmost column of the destination area.

            targetTop: The topmost row of the destination area.

            sourceChar: The character used to fill the source area.

            sourceForeColor: The foreground color used to fill the source area.

            sourceBackColor: The background color used to fill the source area.
        """
        ...

    @staticmethod
    def OpenStandardError(bufferSize=...):
        """
        OpenStandardError() -> Stream

            Acquires the standard error stream.

            Returns: The standard error stream.

        OpenStandardError(bufferSize: int) -> Stream

            Acquires the standard error stream, which is set to a specified buffer size.

            bufferSize: The internal stream buffer size.

            Returns: The standard error stream.
        """
        ...

    @staticmethod
    def OpenStandardInput(bufferSize=...):
        """
        OpenStandardInput() -> Stream

            Acquires the standard input stream.

            Returns: The standard input stream.

        OpenStandardInput(bufferSize: int) -> Stream

            Acquires the standard input stream, which is set to a specified buffer size.

            bufferSize: The internal stream buffer size.

            Returns: The standard input stream.
        """
        ...

    @staticmethod
    def OpenStandardOutput(bufferSize=...):
        """
        OpenStandardOutput() -> Stream

            Acquires the standard output stream.

            Returns: The standard output stream.

        OpenStandardOutput(bufferSize: int) -> Stream

            Acquires the standard output stream, which is set to a specified buffer size.

            bufferSize: The internal stream buffer size.

            Returns: The standard output stream.
        """
        ...

    @staticmethod
    def Read():
        """
        Read() -> int

            Reads the next character from the standard input stream.

            Returns: The next character from the input stream, or negative one (-1) if there are currently no more characters to be read.
        """
        ...

    @staticmethod
    def ReadKey(intercept=...):
        """
        ReadKey() -> ConsoleKeyInfo

            Obtains the next character or function key pressed by the user. The pressed key is displayed in the console window.

            Returns: An object that describes the System.ConsoleKey constant and Unicode character, if any, that correspond to the pressed console key. The

             System.ConsoleKeyInfo object also describes, in a bitwise combination of System.ConsoleModifiers values, whether one or more Shift, Alt, or Ctrl

             modifier keys was pressed simultaneously with the console key.

        ReadKey(intercept: bool) -> ConsoleKeyInfo

            Obtains the next character or function key pressed by the user. The pressed key is optionally displayed in the console window.

            intercept: Determines whether to display the pressed key in the console window. ue to not display the pressed key; otherwise, lse.

            Returns: An object that describes the System.ConsoleKey constant and Unicode character, if any, that correspond to the pressed console key. The

             System.ConsoleKeyInfo object also describes, in a bitwise combination of System.ConsoleModifiers values, whether one or more Shift, Alt, or Ctrl

             modifier keys was pressed simultaneously with the console key.
        """
        ...

    @staticmethod
    def ReadLine():
        """
        ReadLine() -> str

            Reads the next line of characters from the standard input stream.

            Returns: The next line of characters from the input stream, or ll if no more lines are available.
        """
        ...

    @staticmethod
    def ResetColor():
        """
        ResetColor()

            Sets the foreground and background console colors to their defaults.
        """
        ...

    @staticmethod
    def SetBufferSize(width, height):
        """
        SetBufferSize(width: int, height: int)

            Sets the height and width of the screen buffer area to the specified values.

            width: The width of the buffer area measured in columns.

            height: The height of the buffer area measured in rows.
        """
        ...

    @staticmethod
    def SetCursorPosition(left, top):
        """
        SetCursorPosition(left: int, top: int)

            Sets the position of the cursor.

            left: The column position of the cursor. Columns are numbered from left to right starting at 0.

            top: The row position of the cursor. Rows are numbered from top to bottom starting at 0.
        """
        ...

    @staticmethod
    def SetError(newError):
        """
        SetError(newError: TextWriter)

            Sets the System.Console.Error property to the specified System.IO.TextWriter object.

            newError: A stream that is the new standard error output.
        """
        ...

    @staticmethod
    def SetIn(newIn):
        """
        SetIn(newIn: TextReader)

            Sets the System.Console.In property to the specified System.IO.TextReader object.

            newIn: A stream that is the new standard input.
        """
        ...

    @staticmethod
    def SetOut(newOut):
        """
        SetOut(newOut: TextWriter)

            Sets the System.Console.Out property to the specified System.IO.TextWriter object.

            newOut: A stream that is the new standard output.
        """
        ...

    @staticmethod
    def SetWindowPosition(left, top):
        """
        SetWindowPosition(left: int, top: int)

            Sets the position of the console window relative to the screen buffer.

            left: The column position of the upper left  corner of the console window.

            top: The row position of the upper left corner of the console window.
        """
        ...

    @staticmethod
    def SetWindowSize(width, height):
        """
        SetWindowSize(width: int, height: int)

            Sets the height and width of the console window to the specified values.

            width: The width of the console window measured in columns.

            height: The height of the console window measured in rows.
        """
        ...

    @staticmethod
    def Write(*__args):
        """
        Write(format: str, arg0: object)

            Writes the text representation of the specified object to the standard output stream using the specified format information.

            format: A composite format string (see Remarks).

            arg0: An object to write using format.

        Write(value: UInt64)

            Writes the text representation of the specified 64-bit unsigned integer value to the standard output stream.

            value: The value to write.

        Write(value: Int64)

            Writes the text representation of the specified 64-bit signed integer value to the standard output stream.

            value: The value to write.

        Write(value: UInt32)

            Writes the text representation of the specified 32-bit unsigned integer value to the standard output stream.

            value: The value to write.

        Write(value: int)

            Writes the text representation of the specified 32-bit signed integer value to the standard output stream.

            value: The value to write.

        Write(value: Single)

            Writes the text representation of the specified single-precision floating-point value to the standard output stream.

            value: The value to write.

        Write(value: Decimal)

            Writes the text representation of the specified System.Decimal value to the standard output stream.

            value: The value to write.

        Write(value: float)

            Writes the text representation of the specified double-precision floating-point value to the standard output stream.

            value: The value to write.

        Write(buffer: Array[Char], index: int, count: int)

            Writes the specified subarray of Unicode characters to the standard output stream.

            buffer: An array of Unicode characters.

            index: The starting position in buffer.

            count: The number of characters to write.

        Write(buffer: Array[Char])

            Writes the specified array of Unicode characters to the standard output stream.

            buffer: A Unicode character array.

        Write(value: Char)

            Writes the specified Unicode character value to the standard output stream.

            value: The value to write.

        Write(value: bool)

            Writes the text representation of the specified Boolean value to the standard output stream.

            value: The value to write.

        Write(format: str, *arg: Array[object])

            Writes the text representation of the specified array of objects to the standard output stream using the specified format information.

            format: A composite format string (see Remarks).

            arg: An array of objects to write using format.

        Write(format: str, arg0: object, arg1: object, arg2: object, arg3: object)

            Writes the text representation of the specified objects and variable-length parameter list to the standard output stream using the specified format

             information.

            format: A composite format string (see Remarks).

            arg0: The first object to write using format.

            arg1: The second object to write using format.

            arg2: The third object to write using format.

            arg3: The fourth object to write using format.

        Write(format: str, arg0: object, arg1: object, arg2: object)

            Writes the text representation of the specified objects to the standard output stream using the specified format information.

            format: A composite format string (see Remarks).

            arg0: The first object to write using format.

            arg1: The second object to write using format.

            arg2: The third object to write using format.

        Write(format: str, arg0: object, arg1: object)

            Writes the text representation of the specified objects to the standard output stream using the specified format information.

            format: A composite format string (see Remarks).

            arg0: The first object to write using format.

            arg1: The second object to write using format.

        Write(value: object)

            Writes the text representation of the specified object to the standard output stream.

            value: The value to write, or ll.

        Write(value: str)

            Writes the specified string value to the standard output stream.

            value: The value to write.
        """
        ...

    @staticmethod
    def WriteLine(*__args):
        """
        WriteLine()

            Writes the current line terminator to the standard output stream.

        WriteLine(format: str, arg0: object, arg1: object, arg2: object)

            Writes the text representation of the specified objects, followed by the current line terminator, to the standard output stream using the specified

             format information.

            format: A composite format string (see Remarks).

            arg0: The first object to write using format.

            arg1: The second object to write using format.

            arg2: The third object to write using format.

        WriteLine(format: str, arg0: object, arg1: object)

            Writes the text representation of the specified objects, followed by the current line terminator, to the standard output stream using the specified

             format information.

            format: A composite format string (see Remarks).

            arg0: The first object to write using format.

            arg1: The second object to write using format.

        WriteLine(format: str, arg0: object)

            Writes the text representation of the specified object, followed by the current line terminator, to the standard output stream using the specified

             format information.

            format: A composite format string (see Remarks).

            arg0: An object to write using format.

        WriteLine(value: str)

            Writes the specified string value, followed by the current line terminator, to the standard output stream.

            value: The value to write.

        WriteLine(value: object)

            Writes the text representation of the specified object, followed by the current line terminator, to the standard output stream.

            value: The value to write.

        WriteLine(value: UInt64)

            Writes the text representation of the specified 64-bit unsigned integer value, followed by the current line terminator, to the standard output stream.

            value: The value to write.

        WriteLine(value: Int64)

            Writes the text representation of the specified 64-bit signed integer value, followed by the current line terminator, to the standard output stream.

            value: The value to write.

        WriteLine(format: str, arg0: object, arg1: object, arg2: object, arg3: object)

            Writes the text representation of the specified objects and variable-length parameter list, followed by the current line terminator, to the standard

             output stream using the specified format information.

            format: A composite format string (see Remarks).

            arg0: The first object to write using format.

            arg1: The second object to write using format.

            arg2: The third object to write using format.

            arg3: The fourth object to write using format.

        WriteLine(value: UInt32)

            Writes the text representation of the specified 32-bit unsigned integer value, followed by the current line terminator, to the standard output stream.

            value: The value to write.

        WriteLine(value: Single)

            Writes the text representation of the specified single-precision floating-point value, followed by the current line terminator, to the standard

             output stream.

            value: The value to write.

        WriteLine(value: float)

            Writes the text representation of the specified double-precision floating-point value, followed by the current line terminator, to the standard

             output stream.

            value: The value to write.

        WriteLine(value: Decimal)

            Writes the text representation of the specified System.Decimal value, followed by the current line terminator, to the standard output stream.

            value: The value to write.

        WriteLine(buffer: Array[Char], index: int, count: int)

            Writes the specified subarray of Unicode characters, followed by the current line terminator, to the standard output stream.

            buffer: An array of Unicode characters.

            index: The starting position in buffer.

            count: The number of characters to write.

        WriteLine(buffer: Array[Char])

            Writes the specified array of Unicode characters, followed by the current line terminator, to the standard output stream.

            buffer: A Unicode character array.

        WriteLine(value: Char)

            Writes the specified Unicode character, followed by the current line terminator, value to the standard output stream.

            value: The value to write.

        WriteLine(value: bool)

            Writes the text representation of the specified Boolean value, followed by the current line terminator, to the standard output stream.

            value: The value to write.

        WriteLine(value: int)

            Writes the text representation of the specified 32-bit signed integer value, followed by the current line terminator, to the standard output stream.

            value: The value to write.

        WriteLine(format: str, *arg: Array[object])

            Writes the text representation of the specified array of objects, followed by the current line terminator, to the standard output stream using the

             specified format information.

            format: A composite format string (see Remarks).

            arg: An array of objects to write using format.
        """
        ...

    CancelKeyPress = None
    __all__ = [
        'Beep',
        'CancelKeyPress',
        'Clear',
        'MoveBufferArea',
        'OpenStandardError',
        'OpenStandardInput',
        'OpenStandardOutput',
        'Read',
        'ReadKey',
        'ReadLine',
        'ResetColor',
        'SetBufferSize',
        'SetCursorPosition',
        'SetError',
        'SetIn',
        'SetOut',
        'SetWindowPosition',
        'SetWindowSize',
        'Write',
        'WriteLine',
    ]


class ConsoleCancelEventArgs(EventArgs):
    """ Provides data for the System.Console.CancelKeyPress event. This class cannot be inherited. """
    @property
    def Cancel(self):
        """
        Gets or sets a value that indicates whether simultaneously pressing the System.ConsoleModifiers.Control modifier key and the System.ConsoleKey.C console key (Ctrl+C) or the Ctrl+Break keys terminates the current process. The default is lse, which terminates the current process.

        Get: Cancel(self: ConsoleCancelEventArgs) -> bool

        Set: Cancel(self: ConsoleCancelEventArgs) = value
        """
        ...

    @property
    def SpecialKey(self):
        """
        Gets the combination of modifier and console keys that interrupted the current process.

        Get: SpecialKey(self: ConsoleCancelEventArgs) -> ConsoleSpecialKey
        """
        ...



class ConsoleCancelEventHandler(MulticastDelegate): # skipped bases: <type 'ICloneable'>, <type 'ISerializable'>
    """
    Represents the method that will handle the System.Console.CancelKeyPress event of a System.Console.

    ConsoleCancelEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: ConsoleCancelEventHandler, sender: object, e: ConsoleCancelEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result):
        """ EndInvoke(self: ConsoleCancelEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender, e):
        """ Invoke(self: ConsoleCancelEventHandler, sender: object, e: ConsoleCancelEventArgs) """
        ...


class ConsoleColor(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>
    """
    Specifies constants that define foreground and background colors for the console.

    enum ConsoleColor, values: Black (0), Blue (9), Cyan (11), DarkBlue (1), DarkCyan (3), DarkGray (8), DarkGreen (2), DarkMagenta (5), DarkRed (4), DarkYellow (6), Gray (7), Green (10), Magenta (13), Red (12), White (15), Yellow (14)
    """
    Black = None
    Blue = None
    Cyan = None
    DarkBlue = None
    DarkCyan = None
    DarkGray = None
    DarkGreen = None
    DarkMagenta = None
    DarkRed = None
    DarkYellow = None
    Gray = None
    Green = None
    Magenta = None
    Red = None
    value__ = None
    White = None
    Yellow = None


class ConsoleKey(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>
    """
    Specifies the standard keys on a console.

    enum ConsoleKey, values: A (65), Add (107), Applications (93), Attention (246), B (66), Backspace (8), BrowserBack (166), BrowserFavorites (171), BrowserForward (167), BrowserHome (172), BrowserRefresh (168), BrowserSearch (170), BrowserStop (169), C (67), Clear (12), CrSel (247), D (68), D0 (48), D1 (49), D2 (50), D3 (51), D4 (52), D5 (53), D6 (54), D7 (55), D8 (56), D9 (57), Decimal (110), Delete (46), Divide (111), DownArrow (40), E (69), End (35), Enter (13), EraseEndOfFile (249), Escape (27), Execute (43), ExSel (248), F (70), F1 (112), F10 (121), F11 (122), F12 (123), F13 (124), F14 (125), F15 (126), F16 (127), F17 (128), F18 (129), F19 (130), F2 (113), F20 (131), F21 (132), F22 (133), F23 (134), F24 (135), F3 (114), F4 (115), F5 (116), F6 (117), F7 (118), F8 (119), F9 (120), G (71), H (72), Help (47), Home (36), I (73), Insert (45), J (74), K (75), L (76), LaunchApp1 (182), LaunchApp2 (183), LaunchMail (180), LaunchMediaSelect (181), LeftArrow (37), LeftWindows (91), M (77), MediaNext (176), MediaPlay (179), MediaPrevious (177), MediaStop (178), Multiply (106), N (78), NoName (252), NumPad0 (96), NumPad1 (97), NumPad2 (98), NumPad3 (99), NumPad4 (100), NumPad5 (101), NumPad6 (102), NumPad7 (103), NumPad8 (104), NumPad9 (105), O (79), Oem1 (186), Oem102 (226), Oem2 (191), Oem3 (192), Oem4 (219), Oem5 (220), Oem6 (221), Oem7 (222), Oem8 (223), OemClear (254), OemComma (188), OemMinus (189), OemPeriod (190), OemPlus (187), P (80), Pa1 (253), Packet (231), PageDown (34), PageUp (33), Pause (19), Play (250), Print (42), PrintScreen (44), Process (229), Q (81), R (82), RightArrow (39), RightWindows (92), S (83), Select (41), Separator (108), Sleep (95), Spacebar (32), Subtract (109), T (84), Tab (9), U (85), UpArrow (38), V (86), VolumeDown (174), VolumeMute (173), VolumeUp (175), W (87), X (88), Y (89), Z (90), Zoom (251)
    """
    A = None
    Add = None
    Applications = None
    Attention = None
    B = None
    Backspace = None
    BrowserBack = None
    BrowserFavorites = None
    BrowserForward = None
    BrowserHome = None
    BrowserRefresh = None
    BrowserSearch = None
    BrowserStop = None
    C = None
    Clear = None
    CrSel = None
    D = None
    D0 = None
    D1 = None
    D2 = None
    D3 = None
    D4 = None
    D5 = None
    D6 = None
    D7 = None
    D8 = None
    D9 = None
    Decimal = None
    Delete = None
    Divide = None
    DownArrow = None
    E = None
    End = None
    Enter = None
    EraseEndOfFile = None
    Escape = None
    Execute = None
    ExSel = None
    F = None
    F1 = None
    F10 = None
    F11 = None
    F12 = None
    F13 = None
    F14 = None
    F15 = None
    F16 = None
    F17 = None
    F18 = None
    F19 = None
    F2 = None
    F20 = None
    F21 = None
    F22 = None
    F23 = None
    F24 = None
    F3 = None
    F4 = None
    F5 = None
    F6 = None
    F7 = None
    F8 = None
    F9 = None
    G = None
    H = None
    Help = None
    Home = None
    I = None
    Insert = None
    J = None
    K = None
    L = None
    LaunchApp1 = None
    LaunchApp2 = None
    LaunchMail = None
    LaunchMediaSelect = None
    LeftArrow = None
    LeftWindows = None
    M = None
    MediaNext = None
    MediaPlay = None
    MediaPrevious = None
    MediaStop = None
    Multiply = None
    N = None
    NoName = None
    NumPad0 = None
    NumPad1 = None
    NumPad2 = None
    NumPad3 = None
    NumPad4 = None
    NumPad5 = None
    NumPad6 = None
    NumPad7 = None
    NumPad8 = None
    NumPad9 = None
    O = None
    Oem1 = None
    Oem102 = None
    Oem2 = None
    Oem3 = None
    Oem4 = None
    Oem5 = None
    Oem6 = None
    Oem7 = None
    Oem8 = None
    OemClear = None
    OemComma = None
    OemMinus = None
    OemPeriod = None
    OemPlus = None
    P = None
    Pa1 = None
    Packet = None
    PageDown = None
    PageUp = None
    Pause = None
    Play = None
    Print = None
    PrintScreen = None
    Process = None
    Q = None
    R = None
    RightArrow = None
    RightWindows = None
    S = None
    Select = None
    Separator = None
    Sleep = None
    Spacebar = None
    Subtract = None
    T = None
    Tab = None
    U = None
    UpArrow = None
    V = None
    value__ = None
    VolumeDown = None
    VolumeMute = None
    VolumeUp = None
    W = None
    X = None
    Y = None
    Z = None
    Zoom = None


class ConsoleKeyInfo: # skipped bases: <type 'object'>
    """
    Describes the console key that was pressed, including the character represented by the console key and the state of the SHIFT, ALT, and CTRL modifier keys.

    ConsoleKeyInfo(keyChar: Char, key: ConsoleKey, shift: bool, alt: bool, control: bool)
    """
    @property
    def Key(self):
        """
        Gets the console key represented by the current System.ConsoleKeyInfo object.

        Get: Key(self: ConsoleKeyInfo) -> ConsoleKey
        """
        ...

    @property
    def KeyChar(self):
        """
        Gets the Unicode character represented by the current System.ConsoleKeyInfo object.

        Get: KeyChar(self: ConsoleKeyInfo) -> Char
        """
        ...

    @property
    def Modifiers(self):
        """
        Gets a bitwise combination of System.ConsoleModifiers values that specifies one or more modifier keys pressed simultaneously with the console key.

        Get: Modifiers(self: ConsoleKeyInfo) -> ConsoleModifiers
        """
        ...


    def Equals(self, *__args):
        """
        Equals(self: ConsoleKeyInfo, value: object) -> bool

            Gets a value indicating whether the specified object is equal to the current System.ConsoleKeyInfo object.

            value: An object to compare to the current System.ConsoleKeyInfo object.

            Returns: ue if value is a System.ConsoleKeyInfo object and is equal to the current System.ConsoleKeyInfo object; otherwise, lse.

        Equals(self: ConsoleKeyInfo, obj: ConsoleKeyInfo) -> bool

            Gets a value indicating whether the specified System.ConsoleKeyInfo object is equal to the current System.ConsoleKeyInfo object.

            obj: An object to compare to the current System.ConsoleKeyInfo object.

            Returns: ue if obj is equal to the current System.ConsoleKeyInfo object; otherwise, lse.
        """
        ...

    def GetHashCode(self):
        """
        GetHashCode(self: ConsoleKeyInfo) -> int

            Returns the hash code for the current System.ConsoleKeyInfo object.

            Returns: A 32-bit signed integer hash code.
        """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ConsoleModifiers(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>
    """
    Represents the SHIFT, ALT, and CTRL modifier keys on a keyboard.

    enum (flags) ConsoleModifiers, values: Alt (1), Control (4), Shift (2)
    """
    Alt = None
    Control = None
    Shift = None
    value__ = None


class ConsoleSpecialKey(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>
    """
    Specifies combinations of modifier and console keys that can interrupt the current process.

    enum ConsoleSpecialKey, values: ControlBreak (1), ControlC (0)
    """
    ControlBreak = None
    ControlC = None
    value__ = None


class ContextBoundObject(MarshalByRefObject):
    """ Defines the base class for all context-bound classes. """
    pass

class ContextMarshalException(SystemException): # skipped bases: <type 'ISerializable'>, <type '_Exception'>
    """
    The exception that is thrown when an attempt to marshal an object across a context boundary fails.

    ContextMarshalException()

    ContextMarshalException(message: str)

    ContextMarshalException(message: str, inner: Exception)
    """
    SerializeObjectState = None


class ContextStaticAttribute(Attribute): # skipped bases: <type '_Attribute'>
    """
    Indicates that the value of a static field is unique for a particular context.

    ContextStaticAttribute()
    """
    pass

class Convert: # skipped bases: <type 'object'>
    """ Converts a base data type to another base data type. """
    @staticmethod
    def ChangeType(value, *__args):
        """
        ChangeType(value: object, typeCode: TypeCode) -> object

            Returns an object of the specified type whose value is equivalent to the specified object.

            value: An object that implements the System.IConvertible interface.

            typeCode: The type of object to return.

            Returns: An object whose underlying type is typeCode and whose value is equivalent to value.-or-A null reference (thing in Visual Basic), if value is ll and

             typeCode is System.TypeCode.Empty, System.TypeCode.String, or System.TypeCode.Object.

        ChangeType(value: object, typeCode: TypeCode, provider: IFormatProvider) -> object

            Returns an object of the specified type whose value is equivalent to the specified object. A parameter supplies culture-specific formatting

             information.

            value: An object that implements the System.IConvertible interface.

            typeCode: The type of object to return.

            provider: An object that supplies culture-specific formatting information.

            Returns: An object whose underlying type is typeCode and whose value is equivalent to value.-or- A null reference (thing in Visual Basic), if value is ll and

             typeCode is System.TypeCode.Empty, System.TypeCode.String, or System.TypeCode.Object.

        ChangeType(value: object, conversionType: Type) -> object

            Returns an object of the specified type and whose value is equivalent to the specified object.

            value: An object that implements the System.IConvertible interface.

            conversionType: The type of object to return.

            Returns: An object whose type is conversionType and whose value is equivalent to value.-or-A null reference (thing in Visual Basic), if value is ll and

             conversionType is not a value type.

        ChangeType(value: object, conversionType: Type, provider: IFormatProvider) -> object

            Returns an object of the specified type whose value is equivalent to the specified object. A parameter supplies culture-specific formatting

             information.

            value: An object that implements the System.IConvertible interface.

            conversionType: The type of object to return.

            provider: An object that supplies culture-specific formatting information.

            Returns: An object whose type is conversionType and whose value is equivalent to value.-or-

                  value, if the System.Type of value and conversionType

             are equal.-or- A null reference (thing in Visual Basic), if value is ll and conversionType is not a value type.
        """
        ...

    @staticmethod
    def FromBase64CharArray(inArray, offset, length):
        """
        FromBase64CharArray(inArray: Array[Char], offset: int, length: int) -> Array[Byte]

            Converts a subset of a Unicode character array, which encodes binary data as base-64 digits, to an equivalent 8-bit unsigned integer array.

             Parameters specify the subset in the input array and the number of elements to convert.

            inArray: A Unicode character array.

            offset: A position within inArray.

            length: The number of elements in inArray to convert.

            Returns: An array of 8-bit unsigned integers equivalent to length elements at position offset in inArray.
        """
        ...

    @staticmethod
    def FromBase64String(s):
        """
        FromBase64String(s: str) -> Array[Byte]

            Converts the specified string, which encodes binary data as base-64 digits, to an equivalent 8-bit unsigned integer array.

            s: The string to convert.

            Returns: An array of 8-bit unsigned integers that is equivalent to s.
        """
        ...

    @staticmethod
    def GetTypeCode(value):
        """
        GetTypeCode(value: object) -> TypeCode

            Returns the System.TypeCode for the specified object.

            value: An object that implements the System.IConvertible interface.

            Returns: The System.TypeCode for value, or System.TypeCode.Empty if value is ll.
        """
        ...

    @staticmethod
    def IsDBNull(value):
        """
        IsDBNull(value: object) -> bool

            Returns an indication whether the specified object is of type System.DBNull.

            value: An object.

            Returns: ue if value is of type System.DBNull; otherwise, lse.
        """
        ...

    @staticmethod
    def ToBase64CharArray(inArray, offsetIn, length, outArray, offsetOut, options=...):
        """
        ToBase64CharArray(inArray: Array[Byte], offsetIn: int, length: int, outArray: Array[Char], offsetOut: int) -> int

            Converts a subset of an 8-bit unsigned integer array to an equivalent subset of a Unicode character array encoded with base-64 digits. Parameters

             specify the subsets as offsets in the input and output arrays, and the number of elements in the input array to convert.

            inArray: An input array of 8-bit unsigned integers.

            offsetIn: A position within inArray.

            length: The number of elements of inArray to convert.

            outArray: An output array of Unicode characters.

            offsetOut: A position within outArray.

            Returns: A 32-bit signed integer containing the number of bytes in outArray.

        ToBase64CharArray(inArray: Array[Byte], offsetIn: int, length: int, outArray: Array[Char], offsetOut: int, options: Base64FormattingOptions) -> int

            Converts a subset of an 8-bit unsigned integer array to an equivalent subset of a Unicode character array encoded with base-64 digits. Parameters

             specify the subsets as offsets in the input and output arrays, the number of elements in the input array to convert, and whether line breaks are

             inserted in the output array.

            inArray: An input array of 8-bit unsigned integers.

            offsetIn: A position within inArray.

            length: The number of elements of inArray to convert.

            outArray: An output array of Unicode characters.

            offsetOut: A position within outArray.

            options: System.Base64FormattingOptions.InsertLineBreaks to insert a line break every 76 characters, or System.Base64FormattingOptions.None to not insert line

             breaks.

            Returns: A 32-bit signed integer containing the number of bytes in outArray.
        """
        ...

    @staticmethod
    def ToBase64String(inArray, *__args):
        """
        ToBase64String(inArray: Array[Byte]) -> str

            Converts an array of 8-bit unsigned integers to its equivalent string representation that is encoded with base-64 digits.

            inArray: An array of 8-bit unsigned integers.

            Returns: The string representation, in base 64, of the contents of inArray.

        ToBase64String(inArray: Array[Byte], options: Base64FormattingOptions) -> str

            Converts an array of 8-bit unsigned integers to its equivalent string representation that is encoded with base-64 digits. A parameter specifies

             whether to insert line breaks in the return value.

            inArray: An array of 8-bit unsigned integers.

            options: System.Base64FormattingOptions.InsertLineBreaks to insert a line break every 76 characters, or System.Base64FormattingOptions.None to not insert line

             breaks.

            Returns: The string representation in base 64 of the elements in inArray.

        ToBase64String(inArray: Array[Byte], offset: int, length: int) -> str

            Converts a subset of an array of 8-bit unsigned integers to its equivalent string representation that is encoded with base-64 digits. Parameters

             specify the subset as an offset in the input array, and the number of elements in the array to convert.

            inArray: An array of 8-bit unsigned integers.

            offset: An offset in inArray.

            length: The number of elements of inArray to convert.

            Returns: The string representation in base 64 of length elements of inArray, starting at position offset.

        ToBase64String(inArray: Array[Byte], offset: int, length: int, options: Base64FormattingOptions) -> str

            Converts a subset of an array of 8-bit unsigned integers to its equivalent string representation that is encoded with base-64 digits. Parameters

             specify the subset as an offset in the input array, the number of elements in the array to convert, and whether to insert line breaks in the return

             value.

            inArray: An array of 8-bit unsigned integers.

            offset: An offset in inArray.

            length: The number of elements of inArray to convert.

            options: System.Base64FormattingOptions.InsertLineBreaks to insert a line break every 76 characters, or System.Base64FormattingOptions.None to not insert line

             breaks.

            Returns: The string representation in base 64 of length elements of inArray, starting at position offset.
        """
        ...

    @staticmethod
    def ToBoolean(value, provider=...):
        """
        ToBoolean(value: object) -> bool

            Converts the value of a specified object to an equivalent Boolean value.

            value: An object that implements the System.IConvertible interface, or ll.

            Returns: ue or lse, which reflects the value returned by invoking the System.IConvertible.ToBoolean(System.IFormatProvider) method for the underlying type of

             value. If value is ll, the method returns lse.

        ToBoolean(value: float) -> bool

            Converts the value of the specified double-precision floating-point number to an equivalent Boolean value.

            value: The double-precision floating-point number to convert.

            Returns: ue if value is not zero; otherwise, lse.

        ToBoolean(value: Single) -> bool

            Converts the value of the specified single-precision floating-point number to an equivalent Boolean value.

            value: The single-precision floating-point number to convert.

            Returns: ue if value is not zero; otherwise, lse.

        ToBoolean(value: str, provider: IFormatProvider) -> bool

            Converts the specified string representation of a logical value to its Boolean equivalent, using the specified culture-specific formatting

             information.

            value: A string that contains the value of either System.Boolean.TrueString or System.Boolean.FalseString.

            provider: An object that supplies culture-specific formatting information. This parameter is ignored.

            Returns: ue if value equals System.Boolean.TrueString, or lse if value equals System.Boolean.FalseString or ll.

        ToBoolean(value: str) -> bool

            Converts the specified string representation of a logical value to its Boolean equivalent.

            value: A string that contains the value of either System.Boolean.TrueString or System.Boolean.FalseString.

            Returns: ue if value equals System.Boolean.TrueString, or lse if value equals System.Boolean.FalseString or ll.

        ToBoolean(value: UInt64) -> bool

            Converts the value of the specified 64-bit unsigned integer to an equivalent Boolean value.

            value: The 64-bit unsigned integer to convert.

            Returns: ue if value is not zero; otherwise, lse.

        ToBoolean(value: Int64) -> bool

            Converts the value of the specified 64-bit signed integer to an equivalent Boolean value.

            value: The 64-bit signed integer to convert.

            Returns: ue if value is not zero; otherwise, lse.

        ToBoolean(value: UInt32) -> bool

            Converts the value of the specified 32-bit unsigned integer to an equivalent Boolean value.

            value: The 32-bit unsigned integer to convert.

            Returns: ue if value is not zero; otherwise, lse.

        ToBoolean(value: int) -> bool

            Converts the value of the specified 32-bit signed integer to an equivalent Boolean value.

            value: The 32-bit signed integer to convert.

            Returns: ue if value is not zero; otherwise, lse.

        ToBoolean(value: UInt16) -> bool

            Converts the value of the specified 16-bit unsigned integer to an equivalent Boolean value.

            value: The 16-bit unsigned integer to convert.

            Returns: ue if value is not zero; otherwise, lse.

        ToBoolean(value: Int16) -> bool

            Converts the value of the specified 16-bit signed integer to an equivalent Boolean value.

            value: The 16-bit signed integer to convert.

            Returns: ue if value is not zero; otherwise, lse.

        ToBoolean(value: Byte) -> bool

            Converts the value of the specified 8-bit unsigned integer to an equivalent Boolean value.

            value: The 8-bit unsigned integer to convert.

            Returns: ue if value is not zero; otherwise, lse.

        ToBoolean(value: Char) -> bool

            Calling this method always throws System.InvalidCastException.

            value: The Unicode character to convert.

            Returns: This conversion is not supported. No value is returned.

        ToBoolean(value: SByte) -> bool

            Converts the value of the specified 8-bit signed integer to an equivalent Boolean value.

            value: The 8-bit signed integer to convert.

            Returns: ue if value is not zero; otherwise, lse.

        ToBoolean(value: bool) -> bool

            Returns the specified Boolean value; no actual conversion is performed.

            value: The Boolean value to return.

            Returns: value is returned unchanged.

        ToBoolean(value: object, provider: IFormatProvider) -> bool

            Converts the value of the specified object to an equivalent Boolean value, using the specified culture-specific formatting information.

            value: An object that implements the System.IConvertible interface, or ll.

            provider: An object that supplies culture-specific formatting information.

            Returns: ue or lse, which reflects the value returned by invoking the System.IConvertible.ToBoolean(System.IFormatProvider) method for the underlying type of

             value. If value is ll, the method returns lse.

        ToBoolean(value: Decimal) -> bool

            Converts the value of the specified decimal number to an equivalent Boolean value.

            value: The number to convert.

            Returns: ue if value is not zero; otherwise, lse.

        ToBoolean(value: DateTime) -> bool

            Calling this method always throws System.InvalidCastException.

            value: The date and time value to convert.

            Returns: This conversion is not supported. No value is returned.
        """
        ...

    @staticmethod
    def ToByte(value, *__args):
        """
        ToByte(value: object) -> Byte

            Converts the value of the specified object to an 8-bit unsigned integer.

            value: An object that implements the System.IConvertible interface, or ll.

            Returns: An 8-bit unsigned integer that is equivalent to value, or zero if value is ll.

        ToByte(value: str, provider: IFormatProvider) -> Byte

            Converts the specified string representation of a number to an equivalent 8-bit unsigned integer, using specified culture-specific formatting

             information.

            value: A string that contains the number to convert.

            provider: An object that supplies culture-specific formatting information.

            Returns: An 8-bit unsigned integer that is equivalent to value, or zero if value is ll.

        ToByte(value: str) -> Byte

            Converts the specified string representation of a number to an equivalent 8-bit unsigned integer.

            value: A string that contains the number to convert.

            Returns: An 8-bit unsigned integer that is equivalent to value, or zero if value is ll.

        ToByte(value: Decimal) -> Byte

            Converts the value of the specified decimal number to an equivalent 8-bit unsigned integer.

            value: The number to convert.

            Returns: value, rounded to the nearest 8-bit unsigned integer. If value is halfway between two whole numbers, the even number is returned; that is, 4.5 is

             converted to 4, and 5.5 is converted to 6.

        ToByte(value: float) -> Byte

            Converts the value of the specified double-precision floating-point number to an equivalent 8-bit unsigned integer.

            value: The double-precision floating-point number to convert.

            Returns: value, rounded to the nearest 8-bit unsigned integer. If value is halfway between two whole numbers, the even number is returned; that is, 4.5 is

             converted to 4, and 5.5 is converted to 6.

        ToByte(value: Single) -> Byte

            Converts the value of the specified single-precision floating-point number to an equivalent 8-bit unsigned integer.

            value: A single-precision floating-point number.

            Returns: value, rounded to the nearest 8-bit unsigned integer. If value is halfway between two whole numbers, the even number is returned; that is, 4.5 is

             converted to 4, and 5.5 is converted to 6.

        ToByte(value: UInt64) -> Byte

            Converts the value of the specified 64-bit unsigned integer to an equivalent 8-bit unsigned integer.

            value: The 64-bit unsigned integer to convert.

            Returns: An 8-bit unsigned integer that is equivalent to value.

        ToByte(value: Int64) -> Byte

            Converts the value of the specified 64-bit signed integer to an equivalent 8-bit unsigned integer.

            value: The 64-bit signed integer to convert.

            Returns: An 8-bit unsigned integer that is equivalent to value.

        ToByte(value: DateTime) -> Byte

            Calling this method always throws System.InvalidCastException.

            value: The date and time value to convert.

            Returns: This conversion is not supported. No value is returned.

        ToByte(value: UInt32) -> Byte

            Converts the value of the specified 32-bit unsigned integer to an equivalent 8-bit unsigned integer.

            value: The 32-bit unsigned integer to convert.

            Returns: An 8-bit unsigned integer that is equivalent to value.

        ToByte(value: UInt16) -> Byte

            Converts the value of the specified 16-bit unsigned integer to an equivalent 8-bit unsigned integer.

            value: The 16-bit unsigned integer to convert.

            Returns: An 8-bit unsigned integer that is equivalent to value.

        ToByte(value: Int16) -> Byte

            Converts the value of the specified 16-bit signed integer to an equivalent 8-bit unsigned integer.

            value: The 16-bit signed integer to convert.

            Returns: An 8-bit unsigned integer that is equivalent to value.

        ToByte(value: SByte) -> Byte

            Converts the value of the specified 8-bit signed integer to an equivalent 8-bit unsigned integer.

            value: The 8-bit signed integer to be converted.

            Returns: An 8-bit unsigned integer that is equivalent to value.

        ToByte(value: Char) -> Byte

            Converts the value of the specified Unicode character to the equivalent 8-bit unsigned integer.

            value: The Unicode character to convert.

            Returns: An 8-bit unsigned integer that is equivalent to value.

        ToByte(value: Byte) -> Byte

            Returns the specified 8-bit unsigned integer; no actual conversion is performed.

            value: The 8-bit unsigned integer to return.

            Returns: value is returned unchanged.

        ToByte(value: bool) -> Byte

            Converts the specified Boolean value to the equivalent 8-bit unsigned integer.

            value: The Boolean value to convert.

            Returns: The number 1 if value is ue; otherwise, 0.

        ToByte(value: object, provider: IFormatProvider) -> Byte

            Converts the value of the specified object to an 8-bit unsigned integer, using the specified culture-specific formatting information.

            value: An object that implements the System.IConvertible interface.

            provider: An object that supplies culture-specific formatting information.

            Returns: An 8-bit unsigned integer that is equivalent to value, or zero if value is ll.

        ToByte(value: int) -> Byte

            Converts the value of the specified 32-bit signed integer to an equivalent 8-bit unsigned integer.

            value: The 32-bit signed integer to convert.

            Returns: An 8-bit unsigned integer that is equivalent to value.

        ToByte(value: str, fromBase: int) -> Byte

            Converts the string representation of a number in a specified base to an equivalent 8-bit unsigned integer.

            value: A string that contains the number to convert.

            fromBase: The base of the number in value, which must be 2, 8, 10, or 16.

            Returns: An 8-bit unsigned integer that is equivalent to the number in value, or 0 (zero) if value is ll.
        """
        ...

    @staticmethod
    def ToChar(value, provider=...):
        """
        ToChar(value: object) -> Char

            Converts the value of the specified object to a Unicode character.

            value: An object that implements the System.IConvertible interface.

            Returns: A Unicode character that is equivalent to value, or System.Char.MinValue if value is ll.

        ToChar(value: float) -> Char

            Calling this method always throws System.InvalidCastException.

            value: The double-precision floating-point number to convert.

            Returns: This conversion is not supported. No value is returned.

        ToChar(value: Single) -> Char

            Calling this method always throws System.InvalidCastException.

            value: The single-precision floating-point number to convert.

            Returns: This conversion is not supported. No value is returned.

        ToChar(value: str, provider: IFormatProvider) -> Char

            Converts the first character of a specified string to a Unicode character, using specified culture-specific formatting information.

            value: A string of length 1 or ll.

            provider: An object that supplies culture-specific formatting information. This parameter is ignored.

            Returns: A Unicode character that is equivalent to the first and only character in value.

        ToChar(value: str) -> Char

            Converts the first character of a specified string to a Unicode character.

            value: A string of length 1.

            Returns: A Unicode character that is equivalent to the first and only character in value.

        ToChar(value: UInt64) -> Char

            Converts the value of the specified 64-bit unsigned integer to its equivalent Unicode character.

            value: The 64-bit unsigned integer to convert.

            Returns: A Unicode character that is equivalent to value.

        ToChar(value: Int64) -> Char

            Converts the value of the specified 64-bit signed integer to its equivalent Unicode character.

            value: The 64-bit signed integer to convert.

            Returns: A Unicode character that is equivalent to value.

        ToChar(value: UInt32) -> Char

            Converts the value of the specified 32-bit unsigned integer to its equivalent Unicode character.

            value: The 32-bit unsigned integer to convert.

            Returns: A Unicode character that is equivalent to value.

        ToChar(value: int) -> Char

            Converts the value of the specified 32-bit signed integer to its equivalent Unicode character.

            value: The 32-bit signed integer to convert.

            Returns: A Unicode character that is equivalent to value.

        ToChar(value: UInt16) -> Char

            Converts the value of the specified 16-bit unsigned integer to its equivalent Unicode character.

            value: The 16-bit unsigned integer to convert.

            Returns: A Unicode character that is equivalent to value.

        ToChar(value: Int16) -> Char

            Converts the value of the specified 16-bit signed integer to its equivalent Unicode character.

            value: The 16-bit signed integer to convert.

            Returns: A Unicode character that is equivalent to value.

        ToChar(value: Byte) -> Char

            Converts the value of the specified 8-bit unsigned integer to its equivalent Unicode character.

            value: The 8-bit unsigned integer to convert.

            Returns: A Unicode character that is equivalent to value.

        ToChar(value: SByte) -> Char

            Converts the value of the specified 8-bit signed integer to its equivalent Unicode character.

            value: The 8-bit signed integer to convert.

            Returns: A Unicode character that is equivalent to value.

        ToChar(value: Char) -> Char

            Returns the specified Unicode character value; no actual conversion is performed.

            value: The Unicode character to return.

            Returns: value is returned unchanged.

        ToChar(value: bool) -> Char

            Calling this method always throws System.InvalidCastException.

            value: The Boolean value to convert.

            Returns: This conversion is not supported. No value is returned.

        ToChar(value: object, provider: IFormatProvider) -> Char

            Converts the value of the specified object to its equivalent Unicode character, using the specified culture-specific formatting information.

            value: An object that implements the System.IConvertible interface.

            provider: An object that supplies culture-specific formatting information.

            Returns: A Unicode character that is equivalent to value, or System.Char.MinValue if value is ll.

        ToChar(value: Decimal) -> Char

            Calling this method always throws System.InvalidCastException.

            value: The decimal number to convert.

            Returns: This conversion is not supported. No value is returned.

        ToChar(value: DateTime) -> Char

            Calling this method always throws System.InvalidCastException.

            value: The date and time value to convert.

            Returns: This conversion is not supported. No value is returned.
        """
        ...

    @staticmethod
    def ToDateTime(value, provider=...):
        """
        ToDateTime(value: DateTime) -> DateTime

            Returns the specified System.DateTime object; no actual conversion is performed.

            value: A date and time value.

            Returns: value is returned unchanged.

        ToDateTime(value: Single) -> DateTime

            Calling this method always throws System.InvalidCastException.

            value: The single-precision floating-point value to convert.

            Returns: This conversion is not supported. No value is returned.

        ToDateTime(value: Char) -> DateTime

            Calling this method always throws System.InvalidCastException.

            value: The Unicode character to convert.

            Returns: This conversion is not supported. No value is returned.

        ToDateTime(value: bool) -> DateTime

            Calling this method always throws System.InvalidCastException.

            value: The Boolean value to convert.

            Returns: This conversion is not supported. No value is returned.

        ToDateTime(value: UInt64) -> DateTime

            Calling this method always throws System.InvalidCastException.

            value: The 64-bit unsigned integer to convert.

            Returns: This conversion is not supported. No value is returned.

        ToDateTime(value: Int64) -> DateTime

            Calling this method always throws System.InvalidCastException.

            value: The 64-bit signed integer to convert.

            Returns: This conversion is not supported. No value is returned.

        ToDateTime(value: UInt32) -> DateTime

            Calling this method always throws System.InvalidCastException.

            value: The 32-bit unsigned integer to convert.

            Returns: This conversion is not supported. No value is returned.

        ToDateTime(value: int) -> DateTime

            Calling this method always throws System.InvalidCastException.

            value: The 32-bit signed integer to convert.

            Returns: This conversion is not supported. No value is returned.

        ToDateTime(value: UInt16) -> DateTime

            Calling this method always throws System.InvalidCastException.

            value: The 16-bit unsigned integer to convert.

            Returns: This conversion is not supported. No value is returned.

        ToDateTime(value: Int16) -> DateTime

            Calling this method always throws System.InvalidCastException.

            value: The 16-bit signed integer to convert.

            Returns: This conversion is not supported. No value is returned.

        ToDateTime(value: Byte) -> DateTime

            Calling this method always throws System.InvalidCastException.

            value: The 8-bit unsigned integer to convert.

            Returns: This conversion is not supported. No value is returned.

        ToDateTime(value: SByte) -> DateTime

            Calling this method always throws System.InvalidCastException.

            value: The 8-bit signed integer to convert.

            Returns: This conversion is not supported. No value is returned.

        ToDateTime(value: str, provider: IFormatProvider) -> DateTime

            Converts the specified string representation of a number to an equivalent date and time, using the specified culture-specific formatting information.

            value: A string that contains a date and time to convert.

            provider: An object that supplies culture-specific formatting information.

            Returns: The date and time equivalent of the value of value, or the date and time equivalent of System.DateTime.MinValue if value is ll.

        ToDateTime(value: str) -> DateTime

            Converts the specified string representation of a date and time to an equivalent date and time value.

            value: The string representation of a date and time.

            Returns: The date and time equivalent of the value of value, or the date and time equivalent of System.DateTime.MinValue if value is ll.

        ToDateTime(value: object, provider: IFormatProvider) -> DateTime

            Converts the value of the specified object to a System.DateTime object, using the specified culture-specific formatting information.

            value: An object that implements the System.IConvertible interface.

            provider: An object that supplies culture-specific formatting information.

            Returns: The date and time equivalent of the value of value, or the date and time equivalent of System.DateTime.MinValue if value is ll.

        ToDateTime(value: object) -> DateTime

            Converts the value of the specified object to a System.DateTime object.

            value: An object that implements the System.IConvertible interface, or ll.

            Returns: The date and time equivalent of the value of value, or a date and time equivalent of System.DateTime.MinValue if value is ll.

        ToDateTime(value: float) -> DateTime

            Calling this method always throws System.InvalidCastException.

            value: The double-precision floating-point value to convert.

            Returns: This conversion is not supported. No value is returned.

        ToDateTime(value: Decimal) -> DateTime

            Calling this method always throws System.InvalidCastException.

            value: The number to convert.

            Returns: This conversion is not supported. No value is returned.
        """
        ...

    @staticmethod
    def ToDecimal(value, provider=...):
        """
        ToDecimal(value: object) -> Decimal

            Converts the value of the specified object to an equivalent decimal number.

            value: An object that implements the System.IConvertible interface, or ll.

            Returns: A decimal number that is equivalent to value, or 0 (zero) if value is ll.

        ToDecimal(value: Decimal) -> Decimal

            Returns the specified decimal number; no actual conversion is performed.

            value: A decimal number.

            Returns: value is returned unchanged.

        ToDecimal(value: str, provider: IFormatProvider) -> Decimal

            Converts the specified string representation of a number to an equivalent decimal number, using the specified culture-specific formatting information.

            value: A string that contains a number to convert.

            provider: An object that supplies culture-specific formatting information.

            Returns: A decimal number that is equivalent to the number in value, or 0 (zero) if value is ll.

        ToDecimal(value: str) -> Decimal

            Converts the specified string representation of a number to an equivalent decimal number.

            value: A string that contains a number to convert.

            Returns: A decimal number that is equivalent to the number in value, or 0 (zero) if value is ll.

        ToDecimal(value: float) -> Decimal

            Converts the value of the specified double-precision floating-point number to an equivalent decimal number.

            value: The double-precision floating-point number to convert.

            Returns: A decimal number that is equivalent to value.

        ToDecimal(value: Single) -> Decimal

            Converts the value of the specified single-precision floating-point number to the equivalent decimal number.

            value: The single-precision floating-point number to convert.

            Returns: A decimal number that is equivalent to value.

        ToDecimal(value: UInt64) -> Decimal

            Converts the value of the specified 64-bit unsigned integer to an equivalent decimal number.

            value: The 64-bit unsigned integer to convert.

            Returns: A decimal number that is equivalent to value.

        ToDecimal(value: Int64) -> Decimal

            Converts the value of the specified 64-bit signed integer to an equivalent decimal number.

            value: The 64-bit signed integer to convert.

            Returns: A decimal number that is equivalent to value.

        ToDecimal(value: UInt32) -> Decimal

            Converts the value of the specified 32-bit unsigned integer to an equivalent decimal number.

            value: The 32-bit unsigned integer to convert.

            Returns: A decimal number that is equivalent to value.

        ToDecimal(value: int) -> Decimal

            Converts the value of the specified 32-bit signed integer to an equivalent decimal number.

            value: The 32-bit signed integer to convert.

            Returns: A decimal number that is equivalent to value.

        ToDecimal(value: UInt16) -> Decimal

            Converts the value of the specified 16-bit unsigned integer to an equivalent decimal number.

            value: The 16-bit unsigned integer to convert.

            Returns: The decimal number that is equivalent to value.

        ToDecimal(value: Int16) -> Decimal

            Converts the value of the specified 16-bit signed integer to an equivalent decimal number.

            value: The 16-bit signed integer to convert.

            Returns: A decimal number that is equivalent to value.

        ToDecimal(value: Char) -> Decimal

            Calling this method always throws System.InvalidCastException.

            value: The Unicode character to convert.

            Returns: This conversion is not supported. No value is returned.

        ToDecimal(value: Byte) -> Decimal

            Converts the value of the specified 8-bit unsigned integer to the equivalent decimal number.

            value: The 8-bit unsigned integer to convert.

            Returns: The decimal number that is equivalent to value.

        ToDecimal(value: SByte) -> Decimal

            Converts the value of the specified 8-bit signed integer to the equivalent decimal number.

            value: The 8-bit signed integer to convert.

            Returns: A decimal number that is equivalent to value.

        ToDecimal(value: object, provider: IFormatProvider) -> Decimal

            Converts the value of the specified object to an equivalent decimal number, using the specified culture-specific formatting information.

            value: An object that implements the System.IConvertible interface.

            provider: An object that supplies culture-specific formatting information.

            Returns: A decimal number that is equivalent to value, or 0 (zero) if value is ll.

        ToDecimal(value: bool) -> Decimal

            Converts the specified Boolean value to the equivalent decimal number.

            value: The Boolean value to convert.

            Returns: The number 1 if value is ue; otherwise, 0.

        ToDecimal(value: DateTime) -> Decimal

            Calling this method always throws System.InvalidCastException.

            value: The date and time value to convert.

            Returns: This conversion is not supported. No value is returned.
        """
        ...

    @staticmethod
    def ToDouble(value, provider=...):
        """
        ToDouble(value: object) -> float

            Converts the value of the specified object to a double-precision floating-point number.

            value: An object that implements the System.IConvertible interface, or ll.

            Returns: A double-precision floating-point number that is equivalent to value, or zero if value is ll.

        ToDouble(value: str, provider: IFormatProvider) -> float

            Converts the specified string representation of a number to an equivalent double-precision floating-point number, using the specified

             culture-specific formatting information.

            value: A string that contains the number to convert.

            provider: An object that supplies culture-specific formatting information.

            Returns: A double-precision floating-point number that is equivalent to the number in value, or 0 (zero) if value is ll.

        ToDouble(value: str) -> float

            Converts the specified string representation of a number to an equivalent double-precision floating-point number.

            value: A string that contains the number to convert.

            Returns: A double-precision floating-point number that is equivalent to the number in value, or 0 (zero) if value is ll.

        ToDouble(value: Decimal) -> float

            Converts the value of the specified decimal number to an equivalent double-precision floating-point number.

            value: The decimal number to convert.

            Returns: A double-precision floating-point number that is equivalent to value.

        ToDouble(value: float) -> float

            Returns the specified double-precision floating-point number; no actual conversion is performed.

            value: The double-precision floating-point number to return.

            Returns: value is returned unchanged.

        ToDouble(value: Single) -> float

            Converts the value of the specified single-precision floating-point number to an equivalent double-precision floating-point number.

            value: The single-precision floating-point number.

            Returns: A double-precision floating-point number that is equivalent to value.

        ToDouble(value: UInt64) -> float

            Converts the value of the specified 64-bit unsigned integer to an equivalent double-precision floating-point number.

            value: The 64-bit unsigned integer to convert.

            Returns: A double-precision floating-point number that is equivalent to value.

        ToDouble(value: Int64) -> float

            Converts the value of the specified 64-bit signed integer to an equivalent double-precision floating-point number.

            value: The 64-bit signed integer to convert.

            Returns: A double-precision floating-point number that is equivalent to value.

        ToDouble(value: UInt32) -> float

            Converts the value of the specified 32-bit unsigned integer to an equivalent double-precision floating-point number.

            value: The 32-bit unsigned integer to convert.

            Returns: A double-precision floating-point number that is equivalent to value.

        ToDouble(value: int) -> float

            Converts the value of the specified 32-bit signed integer to an equivalent double-precision floating-point number.

            value: The 32-bit signed integer to convert.

            Returns: A double-precision floating-point number that is equivalent to value.

        ToDouble(value: UInt16) -> float

            Converts the value of the specified 16-bit unsigned integer to the equivalent double-precision floating-point number.

            value: The 16-bit unsigned integer to convert.

            Returns: A double-precision floating-point number that is equivalent to value.

        ToDouble(value: Char) -> float

            Calling this method always throws System.InvalidCastException.

            value: The Unicode character to convert.

            Returns: This conversion is not supported. No value is returned.

        ToDouble(value: Int16) -> float

            Converts the value of the specified 16-bit signed integer to an equivalent double-precision floating-point number.

            value: The 16-bit signed integer to convert.

            Returns: A double-precision floating-point number equivalent to value.

        ToDouble(value: Byte) -> float

            Converts the value of the specified 8-bit unsigned integer to the equivalent double-precision floating-point number.

            value: The 8-bit unsigned integer to convert.

            Returns: The double-precision floating-point number that is equivalent to value.

        ToDouble(value: SByte) -> float

            Converts the value of the specified 8-bit signed integer to the equivalent double-precision floating-point number.

            value: The 8-bit signed integer to convert.

            Returns: The 8-bit signed integer that is equivalent to value.

        ToDouble(value: object, provider: IFormatProvider) -> float

            Converts the value of the specified object to an double-precision floating-point number, using the specified culture-specific formatting information.

            value: An object that implements the System.IConvertible interface.

            provider: An object that supplies culture-specific formatting information.

            Returns: A double-precision floating-point number that is equivalent to value, or zero if value is ll.

        ToDouble(value: bool) -> float

            Converts the specified Boolean value to the equivalent double-precision floating-point number.

            value: The Boolean value to convert.

            Returns: The number 1 if value is ue; otherwise, 0.

        ToDouble(value: DateTime) -> float

            Calling this method always throws System.InvalidCastException.

            value: The date and time value to convert.

            Returns: This conversion is not supported. No value is returned.
        """
        ...

    @staticmethod
    def ToInt16(value, *__args):
        """
        ToInt16(value: object) -> Int16

            Converts the value of the specified object to a 16-bit signed integer.

            value: An object that implements the System.IConvertible interface, or ll.

            Returns: A 16-bit signed integer that is equivalent to value, or zero if value is ll.

        ToInt16(value: str, provider: IFormatProvider) -> Int16

            Converts the specified string representation of a number to an equivalent 16-bit signed integer, using the specified culture-specific formatting

             information.

            value: A string that contains the number to convert.

            provider: An object that supplies culture-specific formatting information.

            Returns: A 16-bit signed integer that is equivalent to the number in value, or 0 (zero) if value is ll.

        ToInt16(value: str) -> Int16

            Converts the specified string representation of a number to an equivalent 16-bit signed integer.

            value: A string that contains the number to convert.

            Returns: A 16-bit signed integer that is equivalent to the number in value, or 0 (zero) if value is ll.

        ToInt16(value: Decimal) -> Int16

            Converts the value of the specified decimal number to an equivalent 16-bit signed integer.

            value: The decimal number to convert.

            Returns: value, rounded to the nearest 16-bit signed integer. If value is halfway between two whole numbers, the even number is returned; that is, 4.5 is

             converted to 4, and 5.5 is converted to 6.

        ToInt16(value: float) -> Int16

            Converts the value of the specified double-precision floating-point number to an equivalent 16-bit signed integer.

            value: The double-precision floating-point number to convert.

            Returns: value, rounded to the nearest 16-bit signed integer. If value is halfway between two whole numbers, the even number is returned; that is, 4.5 is

             converted to 4, and 5.5 is converted to 6.

        ToInt16(value: Single) -> Int16

            Converts the value of the specified single-precision floating-point number to an equivalent 16-bit signed integer.

            value: The single-precision floating-point number to convert.

            Returns: value, rounded to the nearest 16-bit signed integer. If value is halfway between two whole numbers, the even number is returned; that is, 4.5 is

             converted to 4, and 5.5 is converted to 6.

        ToInt16(value: UInt64) -> Int16

            Converts the value of the specified 64-bit unsigned integer to an equivalent 16-bit signed integer.

            value: The 64-bit unsigned integer to convert.

            Returns: A 16-bit signed integer that is equivalent to value.

        ToInt16(value: Int64) -> Int16

            Converts the value of the specified 64-bit signed integer to an equivalent 16-bit signed integer.

            value: The 64-bit signed integer to convert.

            Returns: A 16-bit signed integer that is equivalent to value.

        ToInt16(value: DateTime) -> Int16

            Calling this method always throws System.InvalidCastException.

            value: The date and time value to convert.

            Returns: This conversion is not supported. No value is returned.

        ToInt16(value: Int16) -> Int16

            Returns the specified 16-bit signed integer; no actual conversion is performed.

            value: The 16-bit signed integer to return.

            Returns: value is returned unchanged.

        ToInt16(value: int) -> Int16

            Converts the value of the specified 32-bit signed integer to an equivalent 16-bit signed integer.

            value: The 32-bit signed integer to convert.

            Returns: The 16-bit signed integer equivalent of value.

        ToInt16(value: UInt16) -> Int16

            Converts the value of the specified 16-bit unsigned integer to the equivalent 16-bit signed integer.

            value: The 16-bit unsigned integer to convert.

            Returns: A 16-bit signed integer that is equivalent to value.

        ToInt16(value: Byte) -> Int16

            Converts the value of the specified 8-bit unsigned integer to the equivalent 16-bit signed integer.

            value: The 8-bit unsigned integer to convert.

            Returns: A 16-bit signed integer that is equivalent to value.

        ToInt16(value: SByte) -> Int16

            Converts the value of the specified 8-bit signed integer to the equivalent 16-bit signed integer.

            value: The 8-bit signed integer to convert.

            Returns: A 8-bit signed integer that is equivalent to value.

        ToInt16(value: Char) -> Int16

            Converts the value of the specified Unicode character to the equivalent 16-bit signed integer.

            value: The Unicode character to convert.

            Returns: A 16-bit signed integer that is equivalent to value.

        ToInt16(value: bool) -> Int16

            Converts the specified Boolean value to the equivalent 16-bit signed integer.

            value: The Boolean value to convert.

            Returns: The number 1 if value is ue; otherwise, 0.

        ToInt16(value: object, provider: IFormatProvider) -> Int16

            Converts the value of the specified object to a 16-bit signed integer, using the specified culture-specific formatting information.

            value: An object that implements the System.IConvertible interface.

            provider: An object that supplies culture-specific formatting information.

            Returns: A 16-bit signed integer that is equivalent to value, or zero if value is ll.

        ToInt16(value: UInt32) -> Int16

            Converts the value of the specified 32-bit unsigned integer to an equivalent 16-bit signed integer.

            value: The 32-bit unsigned integer to convert.

            Returns: A 16-bit signed integer that is equivalent to value.

        ToInt16(value: str, fromBase: int) -> Int16

            Converts the string representation of a number in a specified base to an equivalent 16-bit signed integer.

            value: A string that contains the number to convert.

            fromBase: The base of the number in value, which must be 2, 8, 10, or 16.

            Returns: A 16-bit signed integer that is equivalent to the number in value, or 0 (zero) if value is ll.
        """
        ...

    @staticmethod
    def ToInt32(value, *__args):
        """
        ToInt32(value: object) -> int

            Converts the value of the specified object to a 32-bit signed integer.

            value: An object that implements the System.IConvertible interface, or ll.

            Returns: A 32-bit signed integer equivalent to value, or zero if value is ll.

        ToInt32(value: str, provider: IFormatProvider) -> int

            Converts the specified string representation of a number to an equivalent 32-bit signed integer, using the specified culture-specific formatting

             information.

            value: A string that contains the number to convert.

            provider: An object that supplies culture-specific formatting information.

            Returns: A 32-bit signed integer that is equivalent to the number in value, or 0 (zero) if value is ll.

        ToInt32(value: str) -> int

            Converts the specified string representation of a number to an equivalent 32-bit signed integer.

            value: A string that contains the number to convert.

            Returns: A 32-bit signed integer that is equivalent to the number in value, or 0 (zero) if value is ll.

        ToInt32(value: Decimal) -> int

            Converts the value of the specified decimal number to an equivalent 32-bit signed integer.

            value: The decimal number to convert.

            Returns: value, rounded to the nearest 32-bit signed integer. If value is halfway between two whole numbers, the even number is returned; that is, 4.5 is

             converted to 4, and 5.5 is converted to 6.

        ToInt32(value: float) -> int

            Converts the value of the specified double-precision floating-point number to an equivalent 32-bit signed integer.

            value: The double-precision floating-point number to convert.

            Returns: value, rounded to the nearest 32-bit signed integer. If value is halfway between two whole numbers, the even number is returned; that is, 4.5 is

             converted to 4, and 5.5 is converted to 6.

        ToInt32(value: Single) -> int

            Converts the value of the specified single-precision floating-point number to an equivalent 32-bit signed integer.

            value: The single-precision floating-point number to convert.

            Returns: value, rounded to the nearest 32-bit signed integer. If value is halfway between two whole numbers, the even number is returned; that is, 4.5 is

             converted to 4, and 5.5 is converted to 6.

        ToInt32(value: UInt64) -> int

            Converts the value of the specified 64-bit unsigned integer to an equivalent 32-bit signed integer.

            value: The 64-bit unsigned integer to convert.

            Returns: A 32-bit signed integer that is equivalent to value.

        ToInt32(value: Int64) -> int

            Converts the value of the specified 64-bit signed integer to an equivalent 32-bit signed integer.

            value: The 64-bit signed integer to convert.

            Returns: A 32-bit signed integer that is equivalent to value.

        ToInt32(value: DateTime) -> int

            Calling this method always throws System.InvalidCastException.

            value: The date and time value to convert.

            Returns: This conversion is not supported. No value is returned.

        ToInt32(value: int) -> int

            Returns the specified 32-bit signed integer; no actual conversion is performed.

            value: The 32-bit signed integer to return.

            Returns: value is returned unchanged.

        ToInt32(value: UInt16) -> int

            Converts the value of the specified 16-bit unsigned integer to the equivalent 32-bit signed integer.

            value: The 16-bit unsigned integer to convert.

            Returns: A 32-bit signed integer that is equivalent to value.

        ToInt32(value: Int16) -> int

            Converts the value of the specified 16-bit signed integer to an equivalent 32-bit signed integer.

            value: The 16-bit signed integer to convert.

            Returns: A 32-bit signed integer that is equivalent to value.

        ToInt32(value: Byte) -> int

            Converts the value of the specified 8-bit unsigned integer to the equivalent 32-bit signed integer.

            value: The 8-bit unsigned integer to convert.

            Returns: A 32-bit signed integer that is equivalent to value.

        ToInt32(value: SByte) -> int

            Converts the value of the specified 8-bit signed integer to the equivalent 32-bit signed integer.

            value: The 8-bit signed integer to convert.

            Returns: A 8-bit signed integer that is equivalent to value.

        ToInt32(value: Char) -> int

            Converts the value of the specified Unicode character to the equivalent 32-bit signed integer.

            value: The Unicode character to convert.

            Returns: A 32-bit signed integer that is equivalent to value.

        ToInt32(value: bool) -> int

            Converts the specified Boolean value to the equivalent 32-bit signed integer.

            value: The Boolean value to convert.

            Returns: The number 1 if value is ue; otherwise, 0.

        ToInt32(value: object, provider: IFormatProvider) -> int

            Converts the value of the specified object to a 32-bit signed integer, using the specified culture-specific formatting information.

            value: An object that implements the System.IConvertible interface.

            provider: An object that supplies culture-specific formatting information.

            Returns: A 32-bit signed integer that is equivalent to value, or zero if value is ll.

        ToInt32(value: UInt32) -> int

            Converts the value of the specified 32-bit unsigned integer to an equivalent 32-bit signed integer.

            value: The 32-bit unsigned integer to convert.

            Returns: A 32-bit signed integer that is equivalent to value.

        ToInt32(value: str, fromBase: int) -> int

            Converts the string representation of a number in a specified base to an equivalent 32-bit signed integer.

            value: A string that contains the number to convert.

            fromBase: The base of the number in value, which must be 2, 8, 10, or 16.

            Returns: A 32-bit signed integer that is equivalent to the number in value, or 0 (zero) if value is ll.
        """
        ...

    @staticmethod
    def ToInt64(value, *__args):
        """
        ToInt64(value: object) -> Int64

            Converts the value of the specified object to a 64-bit signed integer.

            value: An object that implements the System.IConvertible interface, or ll.

            Returns: A 64-bit signed integer that is equivalent to value, or zero if value is ll.

        ToInt64(value: str, provider: IFormatProvider) -> Int64

            Converts the specified string representation of a number to an equivalent 64-bit signed integer, using the specified culture-specific formatting

             information.

            value: A string that contains the number to convert.

            provider: An object that supplies culture-specific formatting information.

            Returns: A 64-bit signed integer that is equivalent to the number in value, or 0 (zero) if value is ll.

        ToInt64(value: str) -> Int64

            Converts the specified string representation of a number to an equivalent 64-bit signed integer.

            value: A string that contains a number to convert.

            Returns: A 64-bit signed integer that is equivalent to the number in value, or 0 (zero) if value is ll.

        ToInt64(value: Decimal) -> Int64

            Converts the value of the specified decimal number to an equivalent 64-bit signed integer.

            value: The decimal number to convert.

            Returns: value, rounded to the nearest 64-bit signed integer. If value is halfway between two whole numbers, the even number is returned; that is, 4.5 is

             converted to 4, and 5.5 is converted to 6.

        ToInt64(value: float) -> Int64

            Converts the value of the specified double-precision floating-point number to an equivalent 64-bit signed integer.

            value: The double-precision floating-point number to convert.

            Returns: value, rounded to the nearest 64-bit signed integer. If value is halfway between two whole numbers, the even number is returned; that is, 4.5 is

             converted to 4, and 5.5 is converted to 6.

        ToInt64(value: Single) -> Int64

            Converts the value of the specified single-precision floating-point number to an equivalent 64-bit signed integer.

            value: The single-precision floating-point number to convert.

            Returns: value, rounded to the nearest 64-bit signed integer. If value is halfway between two whole numbers, the even number is returned; that is, 4.5 is

             converted to 4, and 5.5 is converted to 6.

        ToInt64(value: Int64) -> Int64

            Returns the specified 64-bit signed integer; no actual conversion is performed.

            value: A 64-bit signed integer.

            Returns: value is returned unchanged.

        ToInt64(value: UInt64) -> Int64

            Converts the value of the specified 64-bit unsigned integer to an equivalent 64-bit signed integer.

            value: The 64-bit unsigned integer to convert.

            Returns: A 64-bit signed integer that is equivalent to value.

        ToInt64(value: DateTime) -> Int64

            Calling this method always throws System.InvalidCastException.

            value: The date and time value to convert.

            Returns: This conversion is not supported. No value is returned.

        ToInt64(value: UInt32) -> Int64

            Converts the value of the specified 32-bit unsigned integer to an equivalent 64-bit signed integer.

            value: The 32-bit unsigned integer to convert.

            Returns: A 64-bit signed integer that is equivalent to value.

        ToInt64(value: UInt16) -> Int64

            Converts the value of the specified 16-bit unsigned integer to the equivalent 64-bit signed integer.

            value: The 16-bit unsigned integer to convert.

            Returns: A 64-bit signed integer that is equivalent to value.

        ToInt64(value: Int16) -> Int64

            Converts the value of the specified 16-bit signed integer to an equivalent 64-bit signed integer.

            value: The 16-bit signed integer to convert.

            Returns: A 64-bit signed integer that is equivalent to value.

        ToInt64(value: Byte) -> Int64

            Converts the value of the specified 8-bit unsigned integer to the equivalent 64-bit signed integer.

            value: The 8-bit unsigned integer to convert.

            Returns: A 64-bit signed integer that is equivalent to value.

        ToInt64(value: SByte) -> Int64

            Converts the value of the specified 8-bit signed integer to the equivalent 64-bit signed integer.

            value: The 8-bit signed integer to convert.

            Returns: A 64-bit signed integer that is equivalent to value.

        ToInt64(value: Char) -> Int64

            Converts the value of the specified Unicode character to the equivalent 64-bit signed integer.

            value: The Unicode character to convert.

            Returns: A 64-bit signed integer that is equivalent to value.

        ToInt64(value: bool) -> Int64

            Converts the specified Boolean value to the equivalent 64-bit signed integer.

            value: The Boolean value to convert.

            Returns: The number 1 if value is ue; otherwise, 0.

        ToInt64(value: object, provider: IFormatProvider) -> Int64

            Converts the value of the specified object to a 64-bit signed integer, using the specified culture-specific formatting information.

            value: An object that implements the System.IConvertible interface.

            provider: An object that supplies culture-specific formatting information.

            Returns: A 64-bit signed integer that is equivalent to value, or zero if value is ll.

        ToInt64(value: int) -> Int64

            Converts the value of the specified 32-bit signed integer to an equivalent 64-bit signed integer.

            value: The 32-bit signed integer to convert.

            Returns: A 64-bit signed integer that is equivalent to value.

        ToInt64(value: str, fromBase: int) -> Int64

            Converts the string representation of a number in a specified base to an equivalent 64-bit signed integer.

            value: A string that contains the number to convert.

            fromBase: The base of the number in value, which must be 2, 8, 10, or 16.

            Returns: A 64-bit signed integer that is equivalent to the number in value, or 0 (zero) if value is ll.
        """
        ...

    @staticmethod
    def ToSByte(value, *__args):
        """
        ToSByte(value: object) -> SByte

            Converts the value of the specified object to an 8-bit signed integer.

            value: An object that implements the System.IConvertible interface, or ll.

            Returns: An 8-bit signed integer that is equivalent to value, or zero if value is ll.

        ToSByte(value: str, provider: IFormatProvider) -> SByte

            Converts the specified string representation of a number to an equivalent 8-bit signed integer, using the specified culture-specific formatting

             information.

            value: A string that contains the number to convert.

            provider: An object that supplies culture-specific formatting information.

            Returns: An 8-bit signed integer that is equivalent to value.

        ToSByte(value: str) -> SByte

            Converts the specified string representation of a number to an equivalent 8-bit signed integer.

            value: A string that contains the number to convert.

            Returns: An 8-bit signed integer that is equivalent to the number in value, or 0 (zero) if value is ll.

        ToSByte(value: Decimal) -> SByte

            Converts the value of the specified decimal number to an equivalent 8-bit signed integer.

            value: The decimal number to convert.

            Returns: value, rounded to the nearest 8-bit signed integer. If value is halfway between two whole numbers, the even number is returned; that is, 4.5 is

             converted to 4, and 5.5 is converted to 6.

        ToSByte(value: float) -> SByte

            Converts the value of the specified double-precision floating-point number to an equivalent 8-bit signed integer.

            value: The double-precision floating-point number to convert.

            Returns: value, rounded to the nearest 8-bit signed integer. If value is halfway between two whole numbers, the even number is returned; that is, 4.5 is

             converted to 4, and 5.5 is converted to 6.

        ToSByte(value: Single) -> SByte

            Converts the value of the specified single-precision floating-point number to an equivalent 8-bit signed integer.

            value: The single-precision floating-point number to convert.

            Returns: value, rounded to the nearest 8-bit signed integer. If value is halfway between two whole numbers, the even number is returned; that is, 4.5 is

             converted to 4, and 5.5 is converted to 6.

        ToSByte(value: UInt64) -> SByte

            Converts the value of the specified 64-bit unsigned integer to an equivalent 8-bit signed integer.

            value: The 64-bit unsigned integer to convert.

            Returns: An 8-bit signed integer that is equivalent to value.

        ToSByte(value: Int64) -> SByte

            Converts the value of the specified 64-bit signed integer to an equivalent 8-bit signed integer.

            value: The 64-bit signed integer to convert.

            Returns: An 8-bit signed integer that is equivalent to value.

        ToSByte(value: DateTime) -> SByte

            Calling this method always throws System.InvalidCastException.

            value: The date and time value to convert.

            Returns: This conversion is not supported. No value is returned.

        ToSByte(value: UInt32) -> SByte

            Converts the value of the specified 32-bit unsigned integer to an equivalent 8-bit signed integer.

            value: The 32-bit unsigned integer to convert.

            Returns: An 8-bit signed integer that is equivalent to value.

        ToSByte(value: UInt16) -> SByte

            Converts the value of the specified 16-bit unsigned integer to the equivalent 8-bit signed integer.

            value: The 16-bit unsigned integer to convert.

            Returns: An 8-bit signed integer that is equivalent to value.

        ToSByte(value: Int16) -> SByte

            Converts the value of the specified 16-bit signed integer to the equivalent 8-bit signed integer.

            value: The 16-bit signed integer to convert.

            Returns: An 8-bit signed integer that is equivalent to value.

        ToSByte(value: Byte) -> SByte

            Converts the value of the specified 8-bit unsigned integer to the equivalent 8-bit signed integer.

            value: The 8-bit unsigned integer to convert.

            Returns: An 8-bit signed integer that is equivalent to value.

        ToSByte(value: Char) -> SByte

            Converts the value of the specified Unicode character to the equivalent 8-bit signed integer.

            value: The Unicode character to convert.

            Returns: An 8-bit signed integer that is equivalent to value.

        ToSByte(value: SByte) -> SByte

            Returns the specified 8-bit signed integer; no actual conversion is performed.

            value: The 8-bit signed integer to return.

            Returns: value is returned unchanged.

        ToSByte(value: bool) -> SByte

            Converts the specified Boolean value to the equivalent 8-bit signed integer.

            value: The Boolean value to convert.

            Returns: The number 1 if value is ue; otherwise, 0.

        ToSByte(value: object, provider: IFormatProvider) -> SByte

            Converts the value of the specified object to an 8-bit signed integer, using the specified culture-specific formatting information.

            value: An object that implements the System.IConvertible interface.

            provider: An object that supplies culture-specific formatting information.

            Returns: An 8-bit signed integer that is equivalent to value, or zero if value is ll.

        ToSByte(value: int) -> SByte

            Converts the value of the specified 32-bit signed integer to an equivalent 8-bit signed integer.

            value: The 32-bit signed integer to convert.

            Returns: An 8-bit signed integer that is equivalent to value.

        ToSByte(value: str, fromBase: int) -> SByte

            Converts the string representation of a number in a specified base to an equivalent 8-bit signed integer.

            value: A string that contains the number to convert.

            fromBase: The base of the number in value, which must be 2, 8, 10, or 16.

            Returns: An 8-bit signed integer that is equivalent to the number in value, or 0 (zero) if value is ll.
        """
        ...

    @staticmethod
    def ToSingle(value, provider=...):
        """
        ToSingle(value: object) -> Single

            Converts the value of the specified object to a single-precision floating-point number.

            value: An object that implements the System.IConvertible interface, or ll.

            Returns: A single-precision floating-point number that is equivalent to value, or zero if value is ll.

        ToSingle(value: str, provider: IFormatProvider) -> Single

            Converts the specified string representation of a number to an equivalent single-precision floating-point number, using the specified

             culture-specific formatting information.

            value: A string that contains the number to convert.

            provider: An object that supplies culture-specific formatting information.

            Returns: A single-precision floating-point number that is equivalent to the number in value, or 0 (zero) if value is ll.

        ToSingle(value: str) -> Single

            Converts the specified string representation of a number to an equivalent single-precision floating-point number.

            value: A string that contains the number to convert.

            Returns: A single-precision floating-point number that is equivalent to the number in value, or 0 (zero) if value is ll.

        ToSingle(value: Decimal) -> Single

            Converts the value of the specified decimal number to an equivalent single-precision floating-point number.

            value: The decimal number to convert.

            Returns: A single-precision floating-point number that is equivalent to value.

                  value is rounded using rounding to nearest. For example, when

             rounded to two decimals, the value 2.345 becomes 2.34 and the value 2.355 becomes 2.36.

        ToSingle(value: float) -> Single

            Converts the value of the specified double-precision floating-point number to an equivalent single-precision floating-point number.

            value: The double-precision floating-point number to convert.

            Returns: A single-precision floating-point number that is equivalent to value.

                  value is rounded using rounding to nearest. For example, when

             rounded to two decimals, the value 2.345 becomes 2.34 and the value 2.355 becomes 2.36.

        ToSingle(value: Single) -> Single

            Returns the specified single-precision floating-point number; no actual conversion is performed.

            value: The single-precision floating-point number to return.

            Returns: value is returned unchanged.

        ToSingle(value: UInt64) -> Single

            Converts the value of the specified 64-bit unsigned integer to an equivalent single-precision floating-point number.

            value: The 64-bit unsigned integer to convert.

            Returns: A single-precision floating-point number that is equivalent to value.

        ToSingle(value: Int64) -> Single

            Converts the value of the specified 64-bit signed integer to an equivalent single-precision floating-point number.

            value: The 64-bit signed integer to convert.

            Returns: A single-precision floating-point number that is equivalent to value.

        ToSingle(value: UInt32) -> Single

            Converts the value of the specified 32-bit unsigned integer to an equivalent single-precision floating-point number.

            value: The 32-bit unsigned integer to convert.

            Returns: A single-precision floating-point number that is equivalent to value.

        ToSingle(value: int) -> Single

            Converts the value of the specified 32-bit signed integer to an equivalent single-precision floating-point number.

            value: The 32-bit signed integer to convert.

            Returns: A single-precision floating-point number that is equivalent to value.

        ToSingle(value: UInt16) -> Single

            Converts the value of the specified 16-bit unsigned integer to the equivalent single-precision floating-point number.

            value: The 16-bit unsigned integer to convert.

            Returns: A single-precision floating-point number that is equivalent to value.

        ToSingle(value: Int16) -> Single

            Converts the value of the specified 16-bit signed integer to an equivalent single-precision floating-point number.

            value: The 16-bit signed integer to convert.

            Returns: A single-precision floating-point number that is equivalent to value.

        ToSingle(value: Char) -> Single

            Calling this method always throws System.InvalidCastException.

            value: The Unicode character to convert.

            Returns: This conversion is not supported. No value is returned.

        ToSingle(value: Byte) -> Single

            Converts the value of the specified 8-bit unsigned integer to the equivalent single-precision floating-point number.

            value: The 8-bit unsigned integer to convert.

            Returns: A single-precision floating-point number that is equivalent to value.

        ToSingle(value: SByte) -> Single

            Converts the value of the specified 8-bit signed integer to the equivalent single-precision floating-point number.

            value: The 8-bit signed integer to convert.

            Returns: An 8-bit signed integer that is equivalent to value.

        ToSingle(value: object, provider: IFormatProvider) -> Single

            Converts the value of the specified object to an single-precision floating-point number, using the specified culture-specific formatting information.

            value: An object that implements the System.IConvertible interface.

            provider: An object that supplies culture-specific formatting information.

            Returns: A single-precision floating-point number that is equivalent to value, or zero if value is ll.

        ToSingle(value: bool) -> Single

            Converts the specified Boolean value to the equivalent single-precision floating-point number.

            value: The Boolean value to convert.

            Returns: The number 1 if value is ue; otherwise, 0.

        ToSingle(value: DateTime) -> Single

            Calling this method always throws System.InvalidCastException.

            value: The date and time value to convert.

            Returns: This conversion is not supported. No value is returned.
        """
        ...

    @staticmethod
    def ToString(value=..., *__args):
        """
        ToString(value: object) -> str

            Converts the value of the specified object to its equivalent string representation.

            value: An object that supplies the value to convert, or ll.

            Returns: The string representation of value, or System.String.Empty if value is ll.

        ToString(value: Single) -> str

            Converts the value of the specified single-precision floating-point number to its equivalent string representation.

            value: The single-precision floating-point number to convert.

            Returns: The string representation of value.

        ToString(value: Single, provider: IFormatProvider) -> str

            Converts the value of the specified single-precision floating-point number to its equivalent string representation, using the specified

             culture-specific formatting information.

            value: The single-precision floating-point number to convert.

            provider: An object that supplies culture-specific formatting information.

            Returns: The string representation of value.

        ToString(value: float) -> str

            Converts the value of the specified double-precision floating-point number to its equivalent string representation.

            value: The double-precision floating-point number to convert.

            Returns: The string representation of value.

        ToString(value: float, provider: IFormatProvider) -> str

            Converts the value of the specified double-precision floating-point number to its equivalent string representation.

            value: The double-precision floating-point number to convert.

            provider: An object that supplies culture-specific formatting information.

            Returns: The string representation of value.

        ToString(value: Decimal) -> str

            Converts the value of the specified decimal number to its equivalent string representation.

            value: The decimal number to convert.

            Returns: The string representation of value.

        ToString(value: Decimal, provider: IFormatProvider) -> str

            Converts the value of the specified decimal number to its equivalent string representation, using the specified culture-specific formatting

             information.

            value: The decimal number to convert.

            provider: An object that supplies culture-specific formatting information.

            Returns: The string representation of value.

        ToString(value: UInt64, provider: IFormatProvider) -> str

            Converts the value of the specified 64-bit unsigned integer to its equivalent string representation, using the specified culture-specific formatting

             information.

            value: The 64-bit unsigned integer to convert.

            provider: An object that supplies culture-specific formatting information.

            Returns: The string representation of value.

        ToString(value: DateTime) -> str

            Converts the value of the specified System.DateTime to its equivalent string representation.

            value: The date and time value to convert.

            Returns: The string representation of value.

        ToString(value: str) -> str

            Returns the specified string instance; no actual conversion is performed.

            value: The string to return.

            Returns: value is returned unchanged.

        ToString(value: str, provider: IFormatProvider) -> str

            Returns the specified string instance; no actual conversion is performed.

            value: The string to return.

            provider: An object that supplies culture-specific formatting information. This parameter is ignored.

            Returns: value is returned unchanged.

        ToString(value: Byte, toBase: int) -> str

            Converts the value of an 8-bit unsigned integer to its equivalent string representation in a specified base.

            value: The 8-bit unsigned integer to convert.

            toBase: The base of the return value, which must be 2, 8, 10, or 16.

            Returns: The string representation of value in base toBase.

        ToString(value: Int16, toBase: int) -> str

            Converts the value of a 16-bit signed integer to its equivalent string representation in a specified base.

            value: The 16-bit signed integer to convert.

            toBase: The base of the return value, which must be 2, 8, 10, or 16.

            Returns: The string representation of value in base toBase.

        ToString(value: int, toBase: int) -> str

            Converts the value of a 32-bit signed integer to its equivalent string representation in a specified base.

            value: The 32-bit signed integer to convert.

            toBase: The base of the return value, which must be 2, 8, 10, or 16.

            Returns: The string representation of value in base toBase.

        ToString(value: Int64, toBase: int) -> str

            Converts the value of a 64-bit signed integer to its equivalent string representation in a specified base.

            value: The 64-bit signed integer to convert.

            toBase: The base of the return value, which must be 2, 8, 10, or 16.

            Returns: The string representation of value in base toBase.

        ToString(value: DateTime, provider: IFormatProvider) -> str

            Converts the value of the specified System.DateTime to its equivalent string representation, using the specified culture-specific formatting

             information.

            value: The date and time value to convert.

            provider: An object that supplies culture-specific formatting information.

            Returns: The string representation of value.

        ToString(value: UInt64) -> str

            Converts the value of the specified 64-bit unsigned integer to its equivalent string representation.

            value: The 64-bit unsigned integer to convert.

            Returns: The string representation of value.

        ToString(value: Int64, provider: IFormatProvider) -> str

            Converts the value of the specified 64-bit signed integer to its equivalent string representation, using the specified culture-specific formatting

             information.

            value: The 64-bit signed integer to convert.

            provider: An object that supplies culture-specific formatting information.

            Returns: The string representation of value.

        ToString(value: Int64) -> str

            Converts the value of the specified 64-bit signed integer to its equivalent string representation.

            value: The 64-bit signed integer to convert.

            Returns: The string representation of value.

        ToString(value: object, provider: IFormatProvider) -> str

            Converts the value of the specified object to its equivalent string representation using the specified culture-specific formatting information.

            value: An object that supplies the value to convert, or ll.

            provider: An object that supplies culture-specific formatting information.

            Returns: The string representation of value, or System.String.Empty if value is an object whose value is ll. If value is ll, the method returns ll.

        ToString(value: Char) -> str

            Converts the value of the specified Unicode character to its equivalent string representation.

            value: The Unicode character to convert.

            Returns: The string representation of value.

        ToString(value: Char, provider: IFormatProvider) -> str

            Converts the value of the specified Unicode character to its equivalent string representation, using the specified culture-specific formatting

             information.

            value: The Unicode character to convert.

            provider: An object that supplies culture-specific formatting information. This parameter is ignored.

            Returns: The string representation of value.

        ToString(value: SByte) -> str

            Converts the value of the specified 8-bit signed integer to its equivalent string representation.

            value: The 8-bit signed integer to convert.

            Returns: The string representation of value.

        ToString(value: SByte, provider: IFormatProvider) -> str

            Converts the value of the specified 8-bit signed integer to its equivalent string representation, using the specified culture-specific formatting

             information.

            value: The 8-bit signed integer to convert.

            provider: An object that supplies culture-specific formatting information.

            Returns: The string representation of value.

        ToString(value: Byte) -> str

            Converts the value of the specified 8-bit unsigned integer to its equivalent string representation.

            value: The 8-bit unsigned integer to convert.

            Returns: The string representation of value.

        ToString(value: Byte, provider: IFormatProvider) -> str

            Converts the value of the specified 8-bit unsigned integer to its equivalent string representation, using the specified culture-specific formatting

             information.

            value: The 8-bit unsigned integer to convert.

            provider: An object that supplies culture-specific formatting information.

            Returns: The string representation of value.

        ToString(value: Int16) -> str

            Converts the value of the specified 16-bit signed integer to its equivalent string representation.

            value: The 16-bit signed integer to convert.

            Returns: The string representation of value.

        ToString(value: Int16, provider: IFormatProvider) -> str

            Converts the value of the specified 16-bit signed integer to its equivalent string representation, using the specified culture-specific formatting

             information.

            value: The 16-bit signed integer to convert.

            provider: An object that supplies culture-specific formatting information.

            Returns: The string representation of value.

        ToString(value: UInt16) -> str

            Converts the value of the specified 16-bit unsigned integer to its equivalent string representation.

            value: The 16-bit unsigned integer to convert.

            Returns: The string representation of value.

        ToString(value: UInt16, provider: IFormatProvider) -> str

            Converts the value of the specified 16-bit unsigned integer to its equivalent string representation, using the specified culture-specific formatting

             information.

            value: The 16-bit unsigned integer to convert.

            provider: An object that supplies culture-specific formatting information.

            Returns: The string representation of value.

        ToString(value: int) -> str

            Converts the value of the specified 32-bit signed integer to its equivalent string representation.

            value: The 32-bit signed integer to convert.

            Returns: The string representation of value.

        ToString(value: int, provider: IFormatProvider) -> str

            Converts the value of the specified 32-bit signed integer to its equivalent string representation, using the specified culture-specific formatting

             information.

            value: The 32-bit signed integer to convert.

            provider: An object that supplies culture-specific formatting information.

            Returns: The string representation of value.

        ToString(value: UInt32) -> str

            Converts the value of the specified 32-bit unsigned integer to its equivalent string representation.

            value: The 32-bit unsigned integer to convert.

            Returns: The string representation of value.

        ToString(value: UInt32, provider: IFormatProvider) -> str

            Converts the value of the specified 32-bit unsigned integer to its equivalent string representation, using the specified culture-specific formatting

             information.

            value: The 32-bit unsigned integer to convert.

            provider: An object that supplies culture-specific formatting information.

            Returns: The string representation of value.

        ToString(value: bool) -> str

            Converts the specified Boolean value to its equivalent string representation.

            value: The Boolean value to convert.

            Returns: The string representation of value.

        ToString(value: bool, provider: IFormatProvider) -> str

            Converts the specified Boolean value to its equivalent string representation.

            value: The Boolean value to convert.

            provider: An instance of an object. This parameter is ignored.

            Returns: The string representation of value.
        """
        ...

    @staticmethod
    def ToUInt16(value, *__args):
        """
        ToUInt16(value: object) -> UInt16

            Converts the value of the specified object to a 16-bit unsigned integer.

            value: An object that implements the System.IConvertible interface, or ll.

            Returns: A 16-bit unsigned integer that is equivalent to value, or zero if value is ll.

        ToUInt16(value: str, provider: IFormatProvider) -> UInt16

            Converts the specified string representation of a number to an equivalent 16-bit unsigned integer, using the specified culture-specific formatting

             information.

            value: A string that contains the number to convert.

            provider: An object that supplies culture-specific formatting information.

            Returns: A 16-bit unsigned integer that is equivalent to the number in value, or 0 (zero) if value is ll.

        ToUInt16(value: str) -> UInt16

            Converts the specified string representation of a number to an equivalent 16-bit unsigned integer.

            value: A string that contains the number to convert.

            Returns: A 16-bit unsigned integer that is equivalent to the number in value, or 0 (zero) if value is ll.

        ToUInt16(value: Decimal) -> UInt16

            Converts the value of the specified decimal number to an equivalent 16-bit unsigned integer.

            value: The decimal number to convert.

            Returns: value, rounded to the nearest 16-bit unsigned integer. If value is halfway between two whole numbers, the even number is returned; that is, 4.5 is

             converted to 4, and 5.5 is converted to 6.

        ToUInt16(value: float) -> UInt16

            Converts the value of the specified double-precision floating-point number to an equivalent 16-bit unsigned integer.

            value: The double-precision floating-point number to convert.

            Returns: value, rounded to the nearest 16-bit unsigned integer. If value is halfway between two whole numbers, the even number is returned; that is, 4.5 is

             converted to 4, and 5.5 is converted to 6.

        ToUInt16(value: Single) -> UInt16

            Converts the value of the specified single-precision floating-point number to an equivalent 16-bit unsigned integer.

            value: The single-precision floating-point number to convert.

            Returns: value, rounded to the nearest 16-bit unsigned integer. If value is halfway between two whole numbers, the even number is returned; that is, 4.5 is

             converted to 4, and 5.5 is converted to 6.

        ToUInt16(value: UInt64) -> UInt16

            Converts the value of the specified 64-bit unsigned integer to an equivalent 16-bit unsigned integer.

            value: The 64-bit unsigned integer to convert.

            Returns: A 16-bit unsigned integer that is equivalent to value.

        ToUInt16(value: Int64) -> UInt16

            Converts the value of the specified 64-bit signed integer to an equivalent 16-bit unsigned integer.

            value: The 64-bit signed integer to convert.

            Returns: A 16-bit unsigned integer that is equivalent to value.

        ToUInt16(value: DateTime) -> UInt16

            Calling this method always throws System.InvalidCastException.

            value: The date and time value to convert.

            Returns: This conversion is not supported. No value is returned.

        ToUInt16(value: UInt32) -> UInt16

            Converts the value of the specified 32-bit unsigned integer to an equivalent 16-bit unsigned integer.

            value: The 32-bit unsigned integer to convert.

            Returns: A 16-bit unsigned integer that is equivalent to value.

        ToUInt16(value: int) -> UInt16

            Converts the value of the specified 32-bit signed integer to an equivalent 16-bit unsigned integer.

            value: The 32-bit signed integer to convert.

            Returns: A 16-bit unsigned integer that is equivalent to value.

        ToUInt16(value: Int16) -> UInt16

            Converts the value of the specified 16-bit signed integer to the equivalent 16-bit unsigned integer.

            value: The 16-bit signed integer to convert.

            Returns: A 16-bit unsigned integer that is equivalent to value.

        ToUInt16(value: Byte) -> UInt16

            Converts the value of the specified 8-bit unsigned integer to the equivalent 16-bit unsigned integer.

            value: The 8-bit unsigned integer to convert.

            Returns: A 16-bit unsigned integer that is equivalent to value.

        ToUInt16(value: SByte) -> UInt16

            Converts the value of the specified 8-bit signed integer to the equivalent 16-bit unsigned integer.

            value: The 8-bit signed integer to convert.

            Returns: A 16-bit unsigned integer that is equivalent to value.

        ToUInt16(value: Char) -> UInt16

            Converts the value of the specified Unicode character to the equivalent 16-bit unsigned integer.

            value: The Unicode character to convert.

            Returns: The 16-bit unsigned integer equivalent to value.

        ToUInt16(value: bool) -> UInt16

            Converts the specified Boolean value to the equivalent 16-bit unsigned integer.

            value: The Boolean value to convert.

            Returns: The number 1 if value is ue; otherwise, 0.

        ToUInt16(value: object, provider: IFormatProvider) -> UInt16

            Converts the value of the specified object to a 16-bit unsigned integer, using the specified culture-specific formatting information.

            value: An object that implements the System.IConvertible interface.

            provider: An object that supplies culture-specific formatting information.

            Returns: A 16-bit unsigned integer that is equivalent to value, or zero if value is ll.

        ToUInt16(value: UInt16) -> UInt16

            Returns the specified 16-bit unsigned integer; no actual conversion is performed.

            value: The 16-bit unsigned integer to return.

            Returns: value is returned unchanged.

        ToUInt16(value: str, fromBase: int) -> UInt16

            Converts the string representation of a number in a specified base to an equivalent 16-bit unsigned integer.

            value: A string that contains the number to convert.

            fromBase: The base of the number in value, which must be 2, 8, 10, or 16.

            Returns: A 16-bit unsigned integer that is equivalent to the number in value, or 0 (zero) if value is ll.
        """
        ...

    @staticmethod
    def ToUInt32(value, *__args):
        """
        ToUInt32(value: object) -> UInt32

            Converts the value of the specified object to a 32-bit unsigned integer.

            value: An object that implements the System.IConvertible interface, or ll.

            Returns: A 32-bit unsigned integer that is equivalent to value, or 0 (zero) if value is ll.

        ToUInt32(value: str, provider: IFormatProvider) -> UInt32

            Converts the specified string representation of a number to an equivalent 32-bit unsigned integer, using the specified culture-specific formatting

             information.

            value: A string that contains the number to convert.

            provider: An object that supplies culture-specific formatting information.

            Returns: A 32-bit unsigned integer that is equivalent to the number in value, or 0 (zero) if value is ll.

        ToUInt32(value: str) -> UInt32

            Converts the specified string representation of a number to an equivalent 32-bit unsigned integer.

            value: A string that contains the number to convert.

            Returns: A 32-bit unsigned integer that is equivalent to the number in value, or 0 (zero) if value is ll.

        ToUInt32(value: Decimal) -> UInt32

            Converts the value of the specified decimal number to an equivalent 32-bit unsigned integer.

            value: The decimal number to convert.

            Returns: value, rounded to the nearest 32-bit unsigned integer. If value is halfway between two whole numbers, the even number is returned; that is, 4.5 is

             converted to 4, and 5.5 is converted to 6.

        ToUInt32(value: float) -> UInt32

            Converts the value of the specified double-precision floating-point number to an equivalent 32-bit unsigned integer.

            value: The double-precision floating-point number to convert.

            Returns: value, rounded to the nearest 32-bit unsigned integer. If value is halfway between two whole numbers, the even number is returned; that is, 4.5 is

             converted to 4, and 5.5 is converted to 6.

        ToUInt32(value: Single) -> UInt32

            Converts the value of the specified single-precision floating-point number to an equivalent 32-bit unsigned integer.

            value: The single-precision floating-point number to convert.

            Returns: value, rounded to the nearest 32-bit unsigned integer. If value is halfway between two whole numbers, the even number is returned; that is, 4.5 is

             converted to 4, and 5.5 is converted to 6.

        ToUInt32(value: UInt64) -> UInt32

            Converts the value of the specified 64-bit unsigned integer to an equivalent 32-bit unsigned integer.

            value: The 64-bit unsigned integer to convert.

            Returns: A 32-bit unsigned integer that is equivalent to value.

        ToUInt32(value: Int64) -> UInt32

            Converts the value of the specified 64-bit signed integer to an equivalent 32-bit unsigned integer.

            value: The 64-bit signed integer to convert.

            Returns: A 32-bit unsigned integer that is equivalent to value.

        ToUInt32(value: DateTime) -> UInt32

            Calling this method always throws System.InvalidCastException.

            value: The date and time value to convert.

            Returns: This conversion is not supported. No value is returned.

        ToUInt32(value: UInt32) -> UInt32

            Returns the specified 32-bit unsigned integer; no actual conversion is performed.

            value: The 32-bit unsigned integer to return.

            Returns: value is returned unchanged.

        ToUInt32(value: UInt16) -> UInt32

            Converts the value of the specified 16-bit unsigned integer to the equivalent 32-bit unsigned integer.

            value: The 16-bit unsigned integer to convert.

            Returns: A 32-bit unsigned integer that is equivalent to value.

        ToUInt32(value: Int16) -> UInt32

            Converts the value of the specified 16-bit signed integer to the equivalent 32-bit unsigned integer.

            value: The 16-bit signed integer to convert.

            Returns: A 32-bit unsigned integer that is equivalent to value.

        ToUInt32(value: Byte) -> UInt32

            Converts the value of the specified 8-bit unsigned integer to the equivalent 32-bit unsigned integer.

            value: The 8-bit unsigned integer to convert.

            Returns: A 32-bit unsigned integer that is equivalent to value.

        ToUInt32(value: SByte) -> UInt32

            Converts the value of the specified 8-bit signed integer to the equivalent 32-bit unsigned integer.

            value: The 8-bit signed integer to convert.

            Returns: A 32-bit unsigned integer that is equivalent to value.

        ToUInt32(value: Char) -> UInt32

            Converts the value of the specified Unicode character to the equivalent 32-bit unsigned integer.

            value: The Unicode character to convert.

            Returns: A 32-bit unsigned integer that is equivalent to value.

        ToUInt32(value: bool) -> UInt32

            Converts the specified Boolean value to the equivalent 32-bit unsigned integer.

            value: The Boolean value to convert.

            Returns: The number 1 if value is ue; otherwise, 0.

        ToUInt32(value: object, provider: IFormatProvider) -> UInt32

            Converts the value of the specified object to a 32-bit unsigned integer, using the specified culture-specific formatting information.

            value: An object that implements the System.IConvertible interface.

            provider: An object that supplies culture-specific formatting information.

            Returns: A 32-bit unsigned integer that is equivalent to value, or zero if value is ll.

        ToUInt32(value: int) -> UInt32

            Converts the value of the specified 32-bit signed integer to an equivalent 32-bit unsigned integer.

            value: The 32-bit signed integer to convert.

            Returns: A 32-bit unsigned integer that is equivalent to value.

        ToUInt32(value: str, fromBase: int) -> UInt32

            Converts the string representation of a number in a specified base to an equivalent 32-bit unsigned integer.

            value: A string that contains the number to convert.

            fromBase: The base of the number in value, which must be 2, 8, 10, or 16.

            Returns: A 32-bit unsigned integer that is equivalent to the number in value, or 0 (zero) if value is ll.
        """
        ...

    @staticmethod
    def ToUInt64(value, *__args):
        """
        ToUInt64(value: object) -> UInt64

            Converts the value of the specified object to a 64-bit unsigned integer.

            value: An object that implements the System.IConvertible interface, or ll.

            Returns: A 64-bit unsigned integer that is equivalent to value, or zero if value is ll.

        ToUInt64(value: str, provider: IFormatProvider) -> UInt64

            Converts the specified string representation of a number to an equivalent 64-bit unsigned integer, using the specified culture-specific formatting

             information.

            value: A string that contains the number to convert.

            provider: An object that supplies culture-specific formatting information.

            Returns: A 64-bit unsigned integer that is equivalent to the number in value, or 0 (zero) if value is ll.

        ToUInt64(value: str) -> UInt64

            Converts the specified string representation of a number to an equivalent 64-bit unsigned integer.

            value: A string that contains the number to convert.

            Returns: A 64-bit signed integer that is equivalent to the number in value, or 0 (zero) if value is ll.

        ToUInt64(value: Decimal) -> UInt64

            Converts the value of the specified decimal number to an equivalent 64-bit unsigned integer.

            value: The decimal number to convert.

            Returns: value, rounded to the nearest 64-bit unsigned integer. If value is halfway between two whole numbers, the even number is returned; that is, 4.5 is

             converted to 4, and 5.5 is converted to 6.

        ToUInt64(value: float) -> UInt64

            Converts the value of the specified double-precision floating-point number to an equivalent 64-bit unsigned integer.

            value: The double-precision floating-point number to convert.

            Returns: value, rounded to the nearest 64-bit unsigned integer. If value is halfway between two whole numbers, the even number is returned; that is, 4.5 is

             converted to 4, and 5.5 is converted to 6.

        ToUInt64(value: Single) -> UInt64

            Converts the value of the specified single-precision floating-point number to an equivalent 64-bit unsigned integer.

            value: The single-precision floating-point number to convert.

            Returns: value, rounded to the nearest 64-bit unsigned integer. If value is halfway between two whole numbers, the even number is returned; that is, 4.5 is

             converted to 4, and 5.5 is converted to 6.

        ToUInt64(value: UInt64) -> UInt64

            Returns the specified 64-bit unsigned integer; no actual conversion is performed.

            value: The 64-bit unsigned integer to return.

            Returns: value is returned unchanged.

        ToUInt64(value: Int64) -> UInt64

            Converts the value of the specified 64-bit signed integer to an equivalent 64-bit unsigned integer.

            value: The 64-bit signed integer to convert.

            Returns: A 64-bit unsigned integer that is equivalent to value.

        ToUInt64(value: DateTime) -> UInt64

            Calling this method always throws System.InvalidCastException.

            value: The date and time value to convert.

            Returns: This conversion is not supported. No value is returned.

        ToUInt64(value: UInt32) -> UInt64

            Converts the value of the specified 32-bit unsigned integer to an equivalent 64-bit unsigned integer.

            value: The 32-bit unsigned integer to convert.

            Returns: A 64-bit unsigned integer that is equivalent to value.

        ToUInt64(value: UInt16) -> UInt64

            Converts the value of the specified 16-bit unsigned integer to the equivalent 64-bit unsigned integer.

            value: The 16-bit unsigned integer to convert.

            Returns: A 64-bit unsigned integer that is equivalent to value.

        ToUInt64(value: Int16) -> UInt64

            Converts the value of the specified 16-bit signed integer to the equivalent 64-bit unsigned integer.

            value: The 16-bit signed integer to convert.

            Returns: A 64-bit unsigned integer that is equivalent to value.

        ToUInt64(value: Byte) -> UInt64

            Converts the value of the specified 8-bit unsigned integer to the equivalent 64-bit unsigned integer.

            value: The 8-bit unsigned integer to convert.

            Returns: A 64-bit signed integer that is equivalent to value.

        ToUInt64(value: SByte) -> UInt64

            Converts the value of the specified 8-bit signed integer to the equivalent 64-bit unsigned integer.

            value: The 8-bit signed integer to convert.

            Returns: A 64-bit unsigned integer that is equivalent to value.

        ToUInt64(value: Char) -> UInt64

            Converts the value of the specified Unicode character to the equivalent 64-bit unsigned integer.

            value: The Unicode character to convert.

            Returns: A 64-bit unsigned integer that is equivalent to value.

        ToUInt64(value: bool) -> UInt64

            Converts the specified Boolean value to the equivalent 64-bit unsigned integer.

            value: The Boolean value to convert.

            Returns: The number 1 if value is ue; otherwise, 0.

        ToUInt64(value: object, provider: IFormatProvider) -> UInt64

            Converts the value of the specified object to a 64-bit unsigned integer, using the specified culture-specific formatting information.

            value: An object that implements the System.IConvertible interface.

            provider: An object that supplies culture-specific formatting information.

            Returns: A 64-bit unsigned integer that is equivalent to value, or zero if value is ll.

        ToUInt64(value: int) -> UInt64

            Converts the value of the specified 32-bit signed integer to an equivalent 64-bit unsigned integer.

            value: The 32-bit signed integer to convert.

            Returns: A 64-bit unsigned integer that is equivalent to value.

        ToUInt64(value: str, fromBase: int) -> UInt64

            Converts the string representation of a number in a specified base to an equivalent 64-bit unsigned integer.

            value: A string that contains the number to convert.

            fromBase: The base of the number in value, which must be 2, 8, 10, or 16.

            Returns: A 64-bit unsigned integer that is equivalent to the number in value, or 0 (zero) if value is ll.
        """
        ...

    DBNull = None
    __all__ = [
        'ChangeType',
        'DBNull',
        'FromBase64CharArray',
        'FromBase64String',
        'GetTypeCode',
        'IsDBNull',
        'ToBase64CharArray',
        'ToBase64String',
        'ToBoolean',
        'ToByte',
        'ToChar',
        'ToDateTime',
        'ToDecimal',
        'ToDouble',
        'ToInt16',
        'ToInt32',
        'ToInt64',
        'ToSByte',
        'ToSingle',
        'ToString',
        'ToUInt16',
        'ToUInt32',
        'ToUInt64',
    ]


class Converter(MulticastDelegate): # skipped bases: <type 'ICloneable'>, <type 'ISerializable'>
    """ Converter[TInput, TOutput](object: object, method: IntPtr) """
    def BeginInvoke(self, input, callback, object):
        """ BeginInvoke(self: Converter[TInput, TOutput], input: TInput, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result):
        """ EndInvoke(self: Converter[TInput, TOutput], result: IAsyncResult) -> TOutput """
        ...

    def Invoke(self, input):
        """ Invoke(self: Converter[TInput, TOutput], input: TInput) -> TOutput """
        ...


class CrossAppDomainDelegate(MulticastDelegate): # skipped bases: <type 'ICloneable'>, <type 'ISerializable'>
    """
    Used by System.AppDomain.DoCallBack(System.CrossAppDomainDelegate) for cross-application domain calls.

    CrossAppDomainDelegate(object: object, method: IntPtr)
    """
    def BeginInvoke(self, callback, object):
        """ BeginInvoke(self: CrossAppDomainDelegate, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result):
        """ EndInvoke(self: CrossAppDomainDelegate, result: IAsyncResult) """
        ...

    def Invoke(self):
        """ Invoke(self: CrossAppDomainDelegate) """
        ...


class DataMisalignedException(SystemException): # skipped bases: <type 'ISerializable'>, <type '_Exception'>
    """
    The exception that is thrown when a unit of data is read from or written to an address that is not a multiple of the data size. This class cannot be inherited.

    DataMisalignedException()

    DataMisalignedException(message: str)

    DataMisalignedException(message: str, innerException: Exception)
    """
    SerializeObjectState = None


class DateTime( IComparable, IFormattable, IConvertible, ISerializable, IEquatable):
    """
    Represents an instant in time, typically expressed as a date and time of day. To browse the .NET Framework source code for this type, see the Reference Source.

    DateTime(ticks: Int64)

    DateTime(ticks: Int64, kind: DateTimeKind)

    DateTime(year: int, month: int, day: int)

    DateTime(year: int, month: int, day: int, calendar: Calendar)

    DateTime(year: int, month: int, day: int, hour: int, minute: int, second: int)

    DateTime(year: int, month: int, day: int, hour: int, minute: int, second: int, kind: DateTimeKind)

    DateTime(year: int, month: int, day: int, hour: int, minute: int, second: int, calendar: Calendar)

    DateTime(year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int)

    DateTime(year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int, kind: DateTimeKind)

    DateTime(year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int, calendar: Calendar)

    DateTime(year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int, calendar: Calendar, kind: DateTimeKind)
    """
    @property
    def Date(self):
        """
        Gets the date component of this instance.

        Get: Date(self: DateTime) -> DateTime
        """
        ...

    @property
    def Day(self):
        """
        Gets the day of the month represented by this instance.

        Get: Day(self: DateTime) -> int
        """
        ...

    @property
    def DayOfWeek(self):
        """
        Gets the day of the week represented by this instance.

        Get: DayOfWeek(self: DateTime) -> DayOfWeek
        """
        ...

    @property
    def DayOfYear(self):
        """
        Gets the day of the year represented by this instance.

        Get: DayOfYear(self: DateTime) -> int
        """
        ...

    @property
    def Hour(self):
        """
        Gets the hour component of the date represented by this instance.

        Get: Hour(self: DateTime) -> int
        """
        ...

    @property
    def Kind(self):
        """
        Gets a value that indicates whether the time represented by this instance is based on local time, Coordinated Universal Time (UTC), or neither.

        Get: Kind(self: DateTime) -> DateTimeKind
        """
        ...

    @property
    def Millisecond(self):
        """
        Gets the milliseconds component of the date represented by this instance.

        Get: Millisecond(self: DateTime) -> int
        """
        ...

    @property
    def Minute(self):
        """
        Gets the minute component of the date represented by this instance.

        Get: Minute(self: DateTime) -> int
        """
        ...

    @property
    def Month(self):
        """
        Gets the month component of the date represented by this instance.

        Get: Month(self: DateTime) -> int
        """
        ...

    @property
    def Now(self):
        """
        Gets a System.DateTime object that is set to the current date and time on this computer, expressed as the local time.

        Get: Now() -> DateTime
        """
        ...

    @property
    def Second(self):
        """
        Gets the seconds component of the date represented by this instance.

        Get: Second(self: DateTime) -> int
        """
        ...

    @property
    def Ticks(self):
        """
        Gets the number of ticks that represent the date and time of this instance.

        Get: Ticks(self: DateTime) -> Int64
        """
        ...

    @property
    def TimeOfDay(self):
        """
        Gets the time of day for this instance.

        Get: TimeOfDay(self: DateTime) -> TimeSpan
        """
        ...

    @property
    def Today(self):
        """
        Gets the current date.

        Get: Today() -> DateTime
        """
        ...

    @property
    def UtcNow(self):
        """
        Gets a System.DateTime object that is set to the current date and time on this computer, expressed as the Coordinated Universal Time (UTC).

        Get: UtcNow() -> DateTime
        """
        ...

    @property
    def Year(self):
        """
        Gets the year component of the date represented by this instance.

        Get: Year(self: DateTime) -> int
        """
        ...


    def Add(self, value):
        """
        Add(self: DateTime, value: TimeSpan) -> DateTime

            Returns a new System.DateTime that adds the value of the specified System.TimeSpan to the value of this instance.

            value: A positive or negative time interval.

            Returns: An object whose value is the sum of the date and time represented by this instance and the time interval represented by value.
        """
        ...

    def AddDays(self, value):
        """
        AddDays(self: DateTime, value: float) -> DateTime

            Returns a new System.DateTime that adds the specified number of days to the value of this instance.

            value: A number of whole and fractional days. The value parameter can be negative or positive.

            Returns: An object whose value is the sum of the date and time represented by this instance and the number of days represented by value.
        """
        ...

    def AddHours(self, value):
        """
        AddHours(self: DateTime, value: float) -> DateTime

            Returns a new System.DateTime that adds the specified number of hours to the value of this instance.

            value: A number of whole and fractional hours. The value parameter can be negative or positive.

            Returns: An object whose value is the sum of the date and time represented by this instance and the number of hours represented by value.
        """
        ...

    def AddMilliseconds(self, value):
        """
        AddMilliseconds(self: DateTime, value: float) -> DateTime

            Returns a new System.DateTime that adds the specified number of milliseconds to the value of this instance.

            value: A number of whole and fractional milliseconds. The value parameter can be negative or positive. Note that this value is rounded to the nearest

             integer.

            Returns: An object whose value is the sum of the date and time represented by this instance and the number of milliseconds represented by value.
        """
        ...

    def AddMinutes(self, value):
        """
        AddMinutes(self: DateTime, value: float) -> DateTime

            Returns a new System.DateTime that adds the specified number of minutes to the value of this instance.

            value: A number of whole and fractional minutes. The value parameter can be negative or positive.

            Returns: An object whose value is the sum of the date and time represented by this instance and the number of minutes represented by value.
        """
        ...

    def AddMonths(self, months):
        """
        AddMonths(self: DateTime, months: int) -> DateTime

            Returns a new System.DateTime that adds the specified number of months to the value of this instance.

            months: A number of months. The months parameter can be negative or positive.

            Returns: An object whose value is the sum of the date and time represented by this instance and months.
        """
        ...

    def AddSeconds(self, value):
        """
        AddSeconds(self: DateTime, value: float) -> DateTime

            Returns a new System.DateTime that adds the specified number of seconds to the value of this instance.

            value: A number of whole and fractional seconds. The value parameter can be negative or positive.

            Returns: An object whose value is the sum of the date and time represented by this instance and the number of seconds represented by value.
        """
        ...

    def AddTicks(self, value):
        """
        AddTicks(self: DateTime, value: Int64) -> DateTime

            Returns a new System.DateTime that adds the specified number of ticks to the value of this instance.

            value: A number of 100-nanosecond ticks. The value parameter can be positive or negative.

            Returns: An object whose value is the sum of the date and time represented by this instance and the time represented by value.
        """
        ...

    def AddYears(self, value):
        """
        AddYears(self: DateTime, value: int) -> DateTime

            Returns a new System.DateTime that adds the specified number of years to the value of this instance.

            value: A number of years. The value parameter can be negative or positive.

            Returns: An object whose value is the sum of the date and time represented by this instance and the number of years represented by value.
        """
        ...

    @staticmethod
    def Compare(t1, t2):
        """
        Compare(t1: DateTime, t2: DateTime) -> int

            Compares two instances of System.DateTime and returns an integer that indicates whether the first instance is earlier than, the same as, or later

             than the second instance.

            t1: The first object to compare.

            t2: The second object to compare.

            Returns: A signed number indicating the relative values of t1 and t2.Value Type Condition Less than zero

                          t1 is earlier than t2. Zero

                           t1 is the same as t2. Greater than zero

                          t1 is later than t2.
        """
        ...

    @staticmethod
    def DaysInMonth(year, month):
        """
        DaysInMonth(year: int, month: int) -> int

            Returns the number of days in the specified month and year.

            year: The year.

            month: The month (a number ranging from 1 to 12).

            Returns: The number of days in month for the specified year.For example, if month equals 2 for February, the return value is 28 or 29 depending upon whether

             year is a leap year.
        """
        ...

    @staticmethod
    def FromBinary(dateData):
        """
        FromBinary(dateData: Int64) -> DateTime

            Deserializes a 64-bit binary value and recreates an original serialized System.DateTime object.

            dateData: A 64-bit signed integer that encodes the System.DateTime.Kind property in a 2-bit field and the System.DateTime.Ticks property in a 62-bit field.

            Returns: An object that is equivalent to the System.DateTime object that was serialized by the System.DateTime.ToBinary method.
        """
        ...

    @staticmethod
    def FromFileTime(fileTime):
        """
        FromFileTime(fileTime: Int64) -> DateTime

            Converts the specified Windows file time to an equivalent local time.

            fileTime: A Windows file time expressed in ticks.

            Returns: An object that represents the local time equivalent of the date and time represented by the fileTime parameter.
        """
        ...

    @staticmethod
    def FromFileTimeUtc(fileTime):
        """
        FromFileTimeUtc(fileTime: Int64) -> DateTime

            Converts the specified Windows file time to an equivalent UTC time.

            fileTime: A Windows file time expressed in ticks.

            Returns: An object that represents the UTC time equivalent of the date and time represented by the fileTime parameter.
        """
        ...

    @staticmethod
    def FromOADate(d):
        """
        FromOADate(d: float) -> DateTime

            Returns a System.DateTime equivalent to the specified OLE Automation Date.

            d: An OLE Automation Date value.

            Returns: An object that represents the same date and time as d.
        """
        ...

    def GetDateTimeFormats(self, *__args):
        """
        GetDateTimeFormats(self: DateTime) -> Array[str]

            Converts the value of this instance to all the string representations supported by the standard date and time format specifiers.

            Returns: A string array where each element is the representation of the value of this instance formatted with one of the standard date and time format

             specifiers.

        GetDateTimeFormats(self: DateTime, provider: IFormatProvider) -> Array[str]

            Converts the value of this instance to all the string representations supported by the standard date and time format specifiers and the specified

             culture-specific formatting information.

            provider: An object that supplies culture-specific formatting information about this instance.

            Returns: A string array where each element is the representation of the value of this instance formatted with one of the standard date and time format

             specifiers.

        GetDateTimeFormats(self: DateTime, format: Char) -> Array[str]

            Converts the value of this instance to all the string representations supported by the specified standard date and time format specifier.

            format: A standard date and time format string (see Remarks).

            Returns: A string array where each element is the representation of the value of this instance formatted with the format standard date and time format

             specifier.

        GetDateTimeFormats(self: DateTime, format: Char, provider: IFormatProvider) -> Array[str]

            Converts the value of this instance to all the string representations supported by the specified standard date and time format specifier and

             culture-specific formatting information.

            format: A date and time format string (see Remarks).

            provider: An object that supplies culture-specific formatting information about this instance.

            Returns: A string array where each element is the representation of the value of this instance formatted with one of the standard date and time format

             specifiers.
        """
        ...

    def GetHashCode(self):
        """
        GetHashCode(self: DateTime) -> int

            Returns the hash code for this instance.

            Returns: A 32-bit signed integer hash code.
        """
        ...

    def IsDaylightSavingTime(self):
        """
        IsDaylightSavingTime(self: DateTime) -> bool

            Indicates whether this instance of System.DateTime is within the daylight saving time range for the current time zone.

            Returns: ue if the value of the System.DateTime.Kind property is System.DateTimeKind.Local or System.DateTimeKind.Unspecified and the value of this instance

             of System.DateTime is within the daylight saving time range for the local time zone; lse if System.DateTime.Kind is System.DateTimeKind.Utc.
        """
        ...

    @staticmethod
    def IsLeapYear(year):
        """
        IsLeapYear(year: int) -> bool

            Returns an indication whether the specified year is a leap year.

            year: A 4-digit year.

            Returns: ue if year is a leap year; otherwise, lse.
        """
        ...

    @staticmethod
    def Parse(s, provider=..., styles=...):
        """
        Parse(s: str) -> DateTime

            Converts the string representation of a date and time to its System.DateTime equivalent.

            s: A string that contains a date and time to convert.

            Returns: An object that is equivalent to the date and time contained in s.

        Parse(s: str, provider: IFormatProvider) -> DateTime

            Converts the string representation of a date and time to its System.DateTime equivalent by using culture-specific format information.

            s: A string that contains a date and time to convert.

            provider: An object that supplies culture-specific format information about s.

            Returns: An object that is equivalent to the date and time contained in s as specified by provider.

        Parse(s: str, provider: IFormatProvider, styles: DateTimeStyles) -> DateTime

            Converts the string representation of a date and time to its System.DateTime equivalent by using culture-specific format information and formatting

             style.

            s: A string that contains a date and time to convert.

            provider: An object that supplies culture-specific formatting information about s.

            styles: A bitwise combination of the enumeration values that indicates the style elements that can be present in s for the parse operation to succeed, and

             that defines how to interpret the parsed date in relation to the current time zone or the current date. A typical value to specify is

             System.Globalization.DateTimeStyles.None.

            Returns: An object that is equivalent to the date and time contained in s, as specified by provider and styles.
        """
        ...

    @staticmethod
    def ParseExact(s, *__args):
        """
        ParseExact(s: str, format: str, provider: IFormatProvider) -> DateTime

            Converts the specified string representation of a date and time to its System.DateTime equivalent using the specified format and culture-specific

             format information. The format of the string representation must match the specified format exactly.

            s: A string that contains a date and time to convert.

            format: A format specifier that defines the required format of s. For more information, see the Remarks section.

            provider: An object that supplies culture-specific format information about s.

            Returns: An object that is equivalent to the date and time contained in s, as specified by format and provider.

        ParseExact(s: str, format: str, provider: IFormatProvider, style: DateTimeStyles) -> DateTime

            Converts the specified string representation of a date and time to its System.DateTime equivalent using the specified format, culture-specific format

             information, and style. The format of the string representation must match the specified format exactly or an exception is thrown.

            s: A string containing a date and time to convert.

            format: A format specifier that defines the required format of s. For more information, see the Remarks section.

            provider: An object that supplies culture-specific formatting information about s.

            style: A bitwise combination of the enumeration values that provides additional information about s, about style elements that may be present in s, or about

             the conversion from s to a System.DateTime value. A typical value to specify is System.Globalization.DateTimeStyles.None.

            Returns: An object that is equivalent to the date and time contained in s, as specified by format, provider, and style.

        ParseExact(s: str, formats: Array[str], provider: IFormatProvider, style: DateTimeStyles) -> DateTime

            Converts the specified string representation of a date and time to its System.DateTime equivalent using the specified array of formats,

             culture-specific format information, and style. The format of the string representation must match at least one of the specified formats exactly or

             an exception is thrown.

            s: A string that contains a date and time to convert.

            formats: An array of allowable formats of s. For more information, see the Remarks section.

            provider: An object that supplies culture-specific format information about s.

            style: A bitwise combination of enumeration values that indicates the permitted format of s. A typical value to specify is

             System.Globalization.DateTimeStyles.None.

            Returns: An object that is equivalent to the date and time contained in s, as specified by formats, provider, and style.
        """
        ...

    @staticmethod
    def SpecifyKind(value, kind):
        """
        SpecifyKind(value: DateTime, kind: DateTimeKind) -> DateTime

            Creates a new System.DateTime object that has the same number of ticks as the specified System.DateTime, but is designated as either local time,

             Coordinated Universal Time (UTC), or neither, as indicated by the specified System.DateTimeKind value.

            value: A date and time.

            kind: One of the enumeration values that indicates whether the new object represents local time, UTC, or neither.

            Returns: A new object that has the same number of ticks as the object represented by the value parameter and the System.DateTimeKind value specified by the

             kind parameter.
        """
        ...

    def Subtract(self, value):
        """
        Subtract(self: DateTime, value: DateTime) -> TimeSpan

            Subtracts the specified date and time from this instance.

            value: The date and time value to subtract.

            Returns: A time interval that is equal to the date and time represented by this instance minus the date and time represented by value.

        Subtract(self: DateTime, value: TimeSpan) -> DateTime

            Subtracts the specified duration from this instance.

            value: The time interval to subtract.

            Returns: An object that is equal to the date and time represented by this instance minus the time interval represented by value.
        """
        ...

    def ToBinary(self):
        """
        ToBinary(self: DateTime) -> Int64

            Serializes the current System.DateTime object to a 64-bit binary value that subsequently can be used to recreate the System.DateTime object.

            Returns: A 64-bit signed integer that encodes the System.DateTime.Kind and System.DateTime.Ticks properties.
        """
        ...

    def ToFileTime(self):
        """
        ToFileTime(self: DateTime) -> Int64

            Converts the value of the current System.DateTime object to a Windows file time.

            Returns: The value of the current System.DateTime object expressed as a Windows file time.
        """
        ...

    def ToFileTimeUtc(self):
        """
        ToFileTimeUtc(self: DateTime) -> Int64

            Converts the value of the current System.DateTime object to a Windows file time.

            Returns: The value of the current System.DateTime object expressed as a Windows file time.
        """
        ...

    def ToLocalTime(self):
        """
        ToLocalTime(self: DateTime) -> DateTime

            Converts the value of the current System.DateTime object to local time.

            Returns: An object whose System.DateTime.Kind property is System.DateTimeKind.Local, and whose value is the local time equivalent to the value of the current

             System.DateTime object, or System.DateTime.MaxValue if the converted value is too large to be represented by a System.DateTime object, or

             System.DateTime.MinValue if the converted value is too small to be represented as a System.DateTime object.
        """
        ...

    def ToLongDateString(self):
        """
        ToLongDateString(self: DateTime) -> str

            Converts the value of the current System.DateTime object to its equivalent long date string representation.

            Returns: A string that contains the long date string representation of the current System.DateTime object.
        """
        ...

    def ToLongTimeString(self):
        """
        ToLongTimeString(self: DateTime) -> str

            Converts the value of the current System.DateTime object to its equivalent long time string representation.

            Returns: A string that contains the long time string representation of the current System.DateTime object.
        """
        ...

    def ToOADate(self):
        """
        ToOADate(self: DateTime) -> float

            Converts the value of this instance to the equivalent OLE Automation date.

            Returns: A double-precision floating-point number that contains an OLE Automation date equivalent to the value of this instance.
        """
        ...

    def ToShortDateString(self):
        """
        ToShortDateString(self: DateTime) -> str

            Converts the value of the current System.DateTime object to its equivalent short date string representation.

            Returns: A string that contains the short date string representation of the current System.DateTime object.
        """
        ...

    def ToShortTimeString(self):
        """
        ToShortTimeString(self: DateTime) -> str

            Converts the value of the current System.DateTime object to its equivalent short time string representation.

            Returns: A string that contains the short time string representation of the current System.DateTime object.
        """
        ...

    def ToUniversalTime(self):
        """
        ToUniversalTime(self: DateTime) -> DateTime

            Converts the value of the current System.DateTime object to Coordinated Universal Time (UTC).

            Returns: An object whose System.DateTime.Kind property is System.DateTimeKind.Utc, and whose value is the UTC equivalent to the value of the current

             System.DateTime object, or System.DateTime.MaxValue if the converted value is too large to be represented by a System.DateTime object, or

             System.DateTime.MinValue if the converted value is too small to be represented by a System.DateTime object.
        """
        ...

    @staticmethod
    def TryParse(s, *__args):
        """
        TryParse(s: str) -> (bool, DateTime)

            Converts the specified string representation of a date and time to its System.DateTime equivalent and returns a value that indicates whether the

             conversion succeeded.

            s: A string containing a date and time to convert.

            Returns: ue if the s parameter was converted successfully; otherwise, lse.

        TryParse(s: str, provider: IFormatProvider, styles: DateTimeStyles) -> (bool, DateTime)

            Converts the specified string representation of a date and time to its System.DateTime equivalent using the specified culture-specific format

             information and formatting style, and returns a value that indicates whether the conversion succeeded.

            s: A string containing a date and time to convert.

            provider: An object that supplies culture-specific formatting information about s.

            styles: A bitwise combination of enumeration values that defines how to interpret the parsed date in relation to the current time zone or the current date. A

             typical value to specify is System.Globalization.DateTimeStyles.None.

            Returns: ue if the s parameter was converted successfully; otherwise, lse.
        """
        ...

    @staticmethod
    def TryParseExact(s, *__args):
        """
        TryParseExact(s: str, format: str, provider: IFormatProvider, style: DateTimeStyles) -> (bool, DateTime)

            Converts the specified string representation of a date and time to its System.DateTime equivalent using the specified format, culture-specific format

             information, and style. The format of the string representation must match the specified format exactly. The method returns a value that indicates

             whether the conversion succeeded.

            s: A string containing a date and time to convert.

            format: The required format of s. See the Remarks section for more information.

            provider: An object that supplies culture-specific formatting information about s.

            style: A bitwise combination of one or more enumeration values that indicate the permitted format of s.

            Returns: ue if s was converted successfully; otherwise, lse.

        TryParseExact(s: str, formats: Array[str], provider: IFormatProvider, style: DateTimeStyles) -> (bool, DateTime)

            Converts the specified string representation of a date and time to its System.DateTime equivalent using the specified array of formats,

             culture-specific format information, and style. The format of the string representation must match at least one of the specified formats exactly. The

             method returns a value that indicates whether the conversion succeeded.

            s: A string that contains a date and time to convert.

            formats: An array of allowable formats of s. See the Remarks section for more information.

            provider: An object that supplies culture-specific format information about s.

            style: A bitwise combination of enumeration values that indicates the permitted format of s. A typical value to specify is

             System.Globalization.DateTimeStyles.None.

            Returns: ue if the s parameter was converted successfully; otherwise, lse.
        """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __cmp__(self, *args): #cannot find CLR method
        """ x.__cmp__(y) <==> cmp(x,y) """
        ...

    def __rsub__(self, *args): #cannot find CLR method
        """
        __rsub__(d1: DateTime, d2: DateTime) -> TimeSpan

            Subtracts a specified date and time from another specified date and time and returns a time interval.

            d1: The date and time value to subtract from (the minuend).

            d2: The date and time value to subtract (the subtrahend).

            Returns: The time interval between d1 and d2; that is, d1 minus d2.
        """
        ...

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-yx.__sub__(y) <==> x-y """
        ...

    MaxValue = None
    MinValue = None


class DateTimeKind(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>
    """
    Specifies whether a System.DateTime object represents a local time, a Coordinated Universal Time (UTC), or is not specified as either local time or UTC.

    enum DateTimeKind, values: Local (2), Unspecified (0), Utc (1)
    """
    Local = None
    Unspecified = None
    Utc = None
    value__ = None


class DateTimeOffset( IComparable, IFormattable, ISerializable, IDeserializationCallback, IEquatable):
    """
    Represents a point in time, typically expressed as a date and time of day, relative to Coordinated Universal Time (UTC).

    DateTimeOffset(ticks: Int64, offset: TimeSpan)

    DateTimeOffset(dateTime: DateTime)

    DateTimeOffset(dateTime: DateTime, offset: TimeSpan)

    DateTimeOffset(year: int, month: int, day: int, hour: int, minute: int, second: int, offset: TimeSpan)

    DateTimeOffset(year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int, offset: TimeSpan)

    DateTimeOffset(year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int, calendar: Calendar, offset: TimeSpan)
    """
    @property
    def Date(self):
        """
        Gets a System.DateTime value that represents the date component of the current System.DateTimeOffset object.

        Get: Date(self: DateTimeOffset) -> DateTime
        """
        ...

    @property
    def DateTime(self):
        """
        Gets a System.DateTime value that represents the date and time of the current System.DateTimeOffset object.

        Get: DateTime(self: DateTimeOffset) -> DateTime
        """
        ...

    @property
    def Day(self):
        """
        Gets the day of the month represented by the current System.DateTimeOffset object.

        Get: Day(self: DateTimeOffset) -> int
        """
        ...

    @property
    def DayOfWeek(self):
        """
        Gets the day of the week represented by the current System.DateTimeOffset object.

        Get: DayOfWeek(self: DateTimeOffset) -> DayOfWeek
        """
        ...

    @property
    def DayOfYear(self):
        """
        Gets the day of the year represented by the current System.DateTimeOffset object.

        Get: DayOfYear(self: DateTimeOffset) -> int
        """
        ...

    @property
    def Hour(self):
        """
        Gets the hour component of the time represented by the current System.DateTimeOffset object.

        Get: Hour(self: DateTimeOffset) -> int
        """
        ...

    @property
    def LocalDateTime(self):
        """
        Gets a System.DateTime value that represents the local date and time of the current System.DateTimeOffset object.

        Get: LocalDateTime(self: DateTimeOffset) -> DateTime
        """
        ...

    @property
    def Millisecond(self):
        """
        Gets the millisecond component of the time represented by the current System.DateTimeOffset object.

        Get: Millisecond(self: DateTimeOffset) -> int
        """
        ...

    @property
    def Minute(self):
        """
        Gets the minute component of the time represented by the current System.DateTimeOffset object.

        Get: Minute(self: DateTimeOffset) -> int
        """
        ...

    @property
    def Month(self):
        """
        Gets the month component of the date represented by the current System.DateTimeOffset object.

        Get: Month(self: DateTimeOffset) -> int
        """
        ...

    @property
    def Now(self):
        """
        Gets a System.DateTimeOffset object that is set to the current date and time on the current computer, with the offset set to the local time's offset from Coordinated Universal Time (UTC).

        Get: Now() -> DateTimeOffset
        """
        ...

    @property
    def Offset(self):
        """
        Gets the time's offset from Coordinated Universal Time (UTC).

        Get: Offset(self: DateTimeOffset) -> TimeSpan
        """
        ...

    @property
    def Second(self):
        """
        Gets the second component of the clock time represented by the current System.DateTimeOffset object.

        Get: Second(self: DateTimeOffset) -> int
        """
        ...

    @property
    def Ticks(self):
        """
        Gets the number of ticks that represents the date and time of the current System.DateTimeOffset object in clock time.

        Get: Ticks(self: DateTimeOffset) -> Int64
        """
        ...

    @property
    def TimeOfDay(self):
        """
        Gets the time of day for the current System.DateTimeOffset object.

        Get: TimeOfDay(self: DateTimeOffset) -> TimeSpan
        """
        ...

    @property
    def UtcDateTime(self):
        """
        Gets a System.DateTime value that represents the Coordinated Universal Time (UTC) date and time of the current System.DateTimeOffset object.

        Get: UtcDateTime(self: DateTimeOffset) -> DateTime
        """
        ...

    @property
    def UtcNow(self):
        """
        Gets a System.DateTimeOffset object whose date and time are set to the current Coordinated Universal Time (UTC) date and time and whose offset is System.TimeSpan.Zero.

        Get: UtcNow() -> DateTimeOffset
        """
        ...

    @property
    def UtcTicks(self):
        """
        Gets the number of ticks that represents the date and time of the current System.DateTimeOffset object in Coordinated Universal Time (UTC).

        Get: UtcTicks(self: DateTimeOffset) -> Int64
        """
        ...

    @property
    def Year(self):
        """
        Gets the year component of the date represented by the current System.DateTimeOffset object.

        Get: Year(self: DateTimeOffset) -> int
        """
        ...


    def Add(self, timeSpan):
        """
        Add(self: DateTimeOffset, timeSpan: TimeSpan) -> DateTimeOffset

            Returns a new System.DateTimeOffset object that adds a specified time interval to the value of this instance.

            timeSpan: A System.TimeSpan object that represents a positive or a negative time interval.

            Returns: An object whose value is the sum of the date and time represented by the current System.DateTimeOffset object and the time interval represented by

             timeSpan.
        """
        ...

    def AddDays(self, days):
        """
        AddDays(self: DateTimeOffset, days: float) -> DateTimeOffset

            Returns a new System.DateTimeOffset object that adds a specified number of whole and fractional days to the value of this instance.

            days: A number of whole and fractional days. The number can be negative or positive.

            Returns: An object whose value is the sum of the date and time represented by the current System.DateTimeOffset object and the number of days represented by

             days.
        """
        ...

    def AddHours(self, hours):
        """
        AddHours(self: DateTimeOffset, hours: float) -> DateTimeOffset

            Returns a new System.DateTimeOffset object that adds a specified number of whole and fractional hours to the value of this instance.

            hours: A number of whole and fractional hours. The number can be negative or positive.

            Returns: An object whose value is the sum of the date and time represented by the current System.DateTimeOffset object and the number of hours represented by

             hours.
        """
        ...

    def AddMilliseconds(self, milliseconds):
        """
        AddMilliseconds(self: DateTimeOffset, milliseconds: float) -> DateTimeOffset

            Returns a new System.DateTimeOffset object that adds a specified number of milliseconds to the value of this instance.

            milliseconds: A number of whole and fractional milliseconds. The number can be negative or positive.

            Returns: An object whose value is the sum of the date and time represented by the current System.DateTimeOffset object and the number of whole milliseconds

             represented by milliseconds.
        """
        ...

    def AddMinutes(self, minutes):
        """
        AddMinutes(self: DateTimeOffset, minutes: float) -> DateTimeOffset

            Returns a new System.DateTimeOffset object that adds a specified number of whole and fractional minutes to the value of this instance.

            minutes: A number of whole and fractional minutes. The number can be negative or positive.

            Returns: An object whose value is the sum of the date and time represented by the current System.DateTimeOffset object and the number of minutes represented

             by minutes.
        """
        ...

    def AddMonths(self, months):
        """
        AddMonths(self: DateTimeOffset, months: int) -> DateTimeOffset

            Returns a new System.DateTimeOffset object that adds a specified number of months to the value of this instance.

            months: A number of whole months. The number can be negative or positive.

            Returns: An object whose value is the sum of the date and time represented by the current System.DateTimeOffset object and the number of months represented by

             months.
        """
        ...

    def AddSeconds(self, seconds):
        """
        AddSeconds(self: DateTimeOffset, seconds: float) -> DateTimeOffset

            Returns a new System.DateTimeOffset object that adds a specified number of whole and fractional seconds to the value of this instance.

            seconds: A number of whole and fractional seconds. The number can be negative or positive.

            Returns: An object whose value is the sum of the date and time represented by the current System.DateTimeOffset object and the number of seconds represented

             by seconds.
        """
        ...

    def AddTicks(self, ticks):
        """
        AddTicks(self: DateTimeOffset, ticks: Int64) -> DateTimeOffset

            Returns a new System.DateTimeOffset object that adds a specified number of ticks to the value of this instance.

            ticks: A number of 100-nanosecond ticks. The number can be negative or positive.

            Returns: An object whose value is the sum of the date and time represented by the current System.DateTimeOffset object and the number of ticks represented by

             ticks.
        """
        ...

    def AddYears(self, years):
        """
        AddYears(self: DateTimeOffset, years: int) -> DateTimeOffset

            Returns a new System.DateTimeOffset object that adds a specified number of years to the value of this instance.

            years: A number of years. The number can be negative or positive.

            Returns: An object whose value is the sum of the date and time represented by the current System.DateTimeOffset object and the number of years represented by

             years.
        """
        ...

    @staticmethod
    def Compare(first, second):
        """
        Compare(first: DateTimeOffset, second: DateTimeOffset) -> int

            Compares two System.DateTimeOffset objects and indicates whether the first is earlier than the second, equal to the second, or later than the second.

            first: The first object to compare.

            second: The second object to compare.

            Returns: A signed integer that indicates whether the value of the first parameter is earlier than, later than, or the same time as the value of the second

             parameter, as the following table shows.Return valueMeaningLess than zero

                          first is earlier than second.Zero

             first is equal to second.Greater than zero

                          first is later than second.
        """
        ...

    def EqualsExact(self, other):
        """
        EqualsExact(self: DateTimeOffset, other: DateTimeOffset) -> bool

            Determines whether the current System.DateTimeOffset object represents the same time and has the same offset as a specified System.DateTimeOffset

             object.

            other: The object to compare to the current System.DateTimeOffset object.

            Returns: ue if the current System.DateTimeOffset object and other have the same date and time value and the same System.DateTimeOffset.Offset value;

             otherwise, lse.
        """
        ...

    @staticmethod
    def FromFileTime(fileTime):
        """
        FromFileTime(fileTime: Int64) -> DateTimeOffset

            Converts the specified Windows file time to an equivalent local time.

            fileTime: A Windows file time, expressed in ticks.

            Returns: An object that represents the date and time of fileTime with the offset set to the local time offset.
        """
        ...

    @staticmethod
    def FromUnixTimeMilliseconds(milliseconds):
        """
        FromUnixTimeMilliseconds(milliseconds: Int64) -> DateTimeOffset

            Converts a Unix time expressed as the number of milliseconds that have elapsed since 1970-01-01T00:00:00Z to a System.DateTimeOffset value.

            milliseconds: A Unix time, expressed as the number of milliseconds that have elapsed since 1970-01-01T00:00:00Z (January 1, 1970, at 12:00 AM UTC). For Unix times

             before this date, its value is negative.

            Returns: A date and time value that represents the same moment in time as the Unix time.
        """
        ...

    @staticmethod
    def FromUnixTimeSeconds(seconds):
        """
        FromUnixTimeSeconds(seconds: Int64) -> DateTimeOffset

            Converts a Unix time expressed as the number of seconds that have elapsed since 1970-01-01T00:00:00Z to a System.DateTimeOffset value.

            seconds: A Unix time, expressed as the number of seconds that have elapsed since 1970-01-01T00:00:00Z (January 1, 1970, at 12:00 AM UTC). For Unix times

             before this date, its value is negative.

            Returns: A date and time value that represents the same moment in time as the Unix time.
        """
        ...

    def GetHashCode(self):
        """
        GetHashCode(self: DateTimeOffset) -> int

            Returns the hash code for the current System.DateTimeOffset object.

            Returns: A 32-bit signed integer hash code.
        """
        ...

    @staticmethod
    def Parse(input, formatProvider=..., styles=...):
        """
        Parse(input: str) -> DateTimeOffset

            Converts the specified string representation of a date, time, and offset to its System.DateTimeOffset equivalent.

            input: A string that contains a date and time to convert.

            Returns: An object that is equivalent to the date and time that is contained in input.

        Parse(input: str, formatProvider: IFormatProvider) -> DateTimeOffset

            Converts the specified string representation of a date and time to its System.DateTimeOffset equivalent using the specified culture-specific format

             information.

            input: A string that contains a date and time to convert.

            formatProvider: An object that provides culture-specific format information about input.

            Returns: An object that is equivalent to the date and time that is contained in input, as specified by formatProvider.

        Parse(input: str, formatProvider: IFormatProvider, styles: DateTimeStyles) -> DateTimeOffset

            Converts the specified string representation of a date and time to its System.DateTimeOffset equivalent using the specified culture-specific format

             information and formatting style.

            input: A string that contains a date and time to convert.

            formatProvider: An object that provides culture-specific format information about input.

            styles: A bitwise combination of enumeration values that indicates the permitted format of input. A typical value to specify is

             System.Globalization.DateTimeStyles.None.

            Returns: An object that is equivalent to the date and time that is contained in input as specified by formatProvider and styles.
        """
        ...

    @staticmethod
    def ParseExact(input, *__args):
        """
        ParseExact(input: str, format: str, formatProvider: IFormatProvider) -> DateTimeOffset

            Converts the specified string representation of a date and time to its System.DateTimeOffset equivalent using the specified format and

             culture-specific format information. The format of the string representation must match the specified format exactly.

            input: A string that contains a date and time to convert.

            format: A format specifier that defines the expected format of input.

            formatProvider: An object that supplies culture-specific formatting information about input.

            Returns: An object that is equivalent to the date and time that is contained in input as specified by format and formatProvider.

        ParseExact(input: str, format: str, formatProvider: IFormatProvider, styles: DateTimeStyles) -> DateTimeOffset

            Converts the specified string representation of a date and time to its System.DateTimeOffset equivalent using the specified format, culture-specific

             format information, and style. The format of the string representation must match the specified format exactly.

            input: A string that contains a date and time to convert.

            format: A format specifier that defines the expected format of input.

            formatProvider: An object that supplies culture-specific formatting information about input.

            styles: A bitwise combination of enumeration values that indicates the permitted format of input.

            Returns: An object that is equivalent to the date and time that is contained in the input parameter, as specified by the format, formatProvider, and styles

             parameters.

        ParseExact(input: str, formats: Array[str], formatProvider: IFormatProvider, styles: DateTimeStyles) -> DateTimeOffset

            Converts the specified string representation of a date and time to its System.DateTimeOffset equivalent using the specified formats, culture-specific

             format information, and style. The format of the string representation must match one of the specified formats exactly.

            input: A string that contains a date and time to convert.

            formats: An array of format specifiers that define the expected formats of input.

            formatProvider: An object that supplies culture-specific formatting information about input.

            styles: A bitwise combination of enumeration values that indicates the permitted format of input.

            Returns: An object that is equivalent to the date and time that is contained in the input parameter, as specified by the formats, formatProvider, and styles

             parameters.
        """
        ...

    def Subtract(self, value):
        """
        Subtract(self: DateTimeOffset, value: DateTimeOffset) -> TimeSpan

            Subtracts a System.DateTimeOffset value that represents a specific date and time from the current System.DateTimeOffset object.

            value: An object that represents the value to subtract.

            Returns: An object that specifies the interval between the two System.DateTimeOffset objects.

        Subtract(self: DateTimeOffset, value: TimeSpan) -> DateTimeOffset

            Subtracts a specified time interval from the current System.DateTimeOffset object.

            value: The time interval to subtract.

            Returns: An object that is equal to the date and time represented by the current System.DateTimeOffset object, minus the time interval represented by value.
        """
        ...

    def ToFileTime(self):
        """
        ToFileTime(self: DateTimeOffset) -> Int64

            Converts the value of the current System.DateTimeOffset object to a Windows file time.

            Returns: The value of the current System.DateTimeOffset object, expressed as a Windows file time.
        """
        ...

    def ToLocalTime(self):
        """
        ToLocalTime(self: DateTimeOffset) -> DateTimeOffset

            Converts the current System.DateTimeOffset object to a System.DateTimeOffset object that represents the local time.

            Returns: An object that represents the date and time of the current System.DateTimeOffset object converted to local time.
        """
        ...

    def ToOffset(self, offset):
        """
        ToOffset(self: DateTimeOffset, offset: TimeSpan) -> DateTimeOffset

            Converts the value of the current System.DateTimeOffset object to the date and time specified by an offset value.

            offset: The offset to convert the System.DateTimeOffset value to.

            Returns: An object that is equal to the original System.DateTimeOffset object (that is, their System.DateTimeOffset.ToUniversalTime methods return identical

             points in time) but whose System.DateTimeOffset.Offset property is set to offset.
        """
        ...

    def ToUniversalTime(self):
        """
        ToUniversalTime(self: DateTimeOffset) -> DateTimeOffset

            Converts the current System.DateTimeOffset object to a System.DateTimeOffset value that represents the Coordinated Universal Time (UTC).

            Returns: An object that represents the date and time of the current System.DateTimeOffset object converted to Coordinated Universal Time (UTC).
        """
        ...

    def ToUnixTimeMilliseconds(self):
        """
        ToUnixTimeMilliseconds(self: DateTimeOffset) -> Int64

            Returns the number of milliseconds that have elapsed since 1970-01-01T00:00:00.000Z.

            Returns: The number of milliseconds that have elapsed since 1970-01-01T00:00:00.000Z.
        """
        ...

    def ToUnixTimeSeconds(self):
        """
        ToUnixTimeSeconds(self: DateTimeOffset) -> Int64

            Returns the number of seconds that have elapsed since 1970-01-01T00:00:00Z.

            Returns: The number of seconds that have elapsed since 1970-01-01T00:00:00Z.
        """
        ...

    @staticmethod
    def TryParse(input, *__args):
        """
        TryParse(input: str) -> (bool, DateTimeOffset)

            Tries to converts a specified string representation of a date and time to its System.DateTimeOffset equivalent, and returns a value that indicates

             whether the conversion succeeded.

            input: A string that contains a date and time to convert.

            Returns: ue if the input parameter is successfully converted; otherwise, lse.

        TryParse(input: str, formatProvider: IFormatProvider, styles: DateTimeStyles) -> (bool, DateTimeOffset)

            Tries to convert a specified string representation of a date and time to its System.DateTimeOffset equivalent, and returns a value that indicates

             whether the conversion succeeded.

            input: A string that contains a date and time to convert.

            formatProvider: An object that provides culture-specific formatting information about input.

            styles: A bitwise combination of enumeration values that indicates the permitted format of input.

            Returns: ue if the input parameter is successfully converted; otherwise, lse.
        """
        ...

    @staticmethod
    def TryParseExact(input, *__args):
        """
        TryParseExact(input: str, format: str, formatProvider: IFormatProvider, styles: DateTimeStyles) -> (bool, DateTimeOffset)

            Converts the specified string representation of a date and time to its System.DateTimeOffset equivalent using the specified format, culture-specific

             format information, and style. The format of the string representation must match the specified format exactly.

            input: A string that contains a date and time to convert.

            format: A format specifier that defines the required format of input.

            formatProvider: An object that supplies culture-specific formatting information about input.

            styles: A bitwise combination of enumeration values that indicates the permitted format of input. A typical value to specify is ne.

            Returns: ue if the input parameter is successfully converted; otherwise, lse.

        TryParseExact(input: str, formats: Array[str], formatProvider: IFormatProvider, styles: DateTimeStyles) -> (bool, DateTimeOffset)

            Converts the specified string representation of a date and time to its System.DateTimeOffset equivalent using the specified array of formats,

             culture-specific format information, and style. The format of the string representation must match one of the specified formats exactly.

            input: A string that contains a date and time to convert.

            formats: An array that defines the expected formats of input.

            formatProvider: An object that supplies culture-specific formatting information about input.

            styles: A bitwise combination of enumeration values that indicates the permitted format of input. A typical value to specify is ne.

            Returns: ue if the input parameter is successfully converted; otherwise, lse.
        """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __cmp__(self, *args): #cannot find CLR method
        """ x.__cmp__(y) <==> cmp(x,y) """
        ...

    def __rsub__(self, *args): #cannot find CLR method
        """
        __rsub__(left: DateTimeOffset, right: DateTimeOffset) -> TimeSpan

            Subtracts one System.DateTimeOffset object from another and yields a time interval.

            left: The minuend.

            right: The subtrahend.

            Returns: An object that represents the difference between left and right.
        """
        ...

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-yx.__sub__(y) <==> x-y """
        ...

    MaxValue = None
    MinValue = None


class DayOfWeek(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>
    """
    Specifies the day of the week.

    enum DayOfWeek, values: Friday (5), Monday (1), Saturday (6), Sunday (0), Thursday (4), Tuesday (2), Wednesday (3)
    """
    Friday = None
    Monday = None
    Saturday = None
    Sunday = None
    Thursday = None
    Tuesday = None
    value__ = None
    Wednesday = None


class DBNull( ISerializable, IConvertible):
    """ Represents a nonexistent value. This class cannot be inherited. """
    def __nonzero__(self, *args): #cannot find CLR method
        """ __nonzero__(value: DBNull) -> bool """
        ...

    Value = None


class Decimal( IFormattable, IComparable, IConvertible, IDeserializationCallback, IEquatable):
    """
    Represents a decimal number.

    Decimal(value: int)

    Decimal(value: UInt32)

    Decimal(value: Int64)

    Decimal(value: UInt64)

    Decimal(value: Single)

    Decimal(value: float)

    Decimal(bits: Array[int])

    Decimal(lo: int, mid: int, hi: int, isNegative: bool, scale: Byte)
    """
    @staticmethod
    def Add(d1, d2):
        """
        Add(d1: Decimal, d2: Decimal) -> Decimal

            Adds two specified System.Decimal values.

            d1: The first value to add.

            d2: The second value to add.

            Returns: The sum of d1 and d2.
        """
        ...

    @staticmethod
    def Ceiling(d):
        """
        Ceiling(d: Decimal) -> Decimal

            Returns the smallest integral value that is greater than or equal to the specified decimal number.

            d: A decimal number.

            Returns: The smallest integral value that is greater than or equal to the d parameter. Note that this method returns a System.Decimal instead of an integral

             type.
        """
        ...

    @staticmethod
    def Compare(d1, d2):
        """
        Compare(d1: Decimal, d2: Decimal) -> int

            Compares two specified System.Decimal values.

            d1: The first value to compare.

            d2: The second value to compare.

            Returns: A signed number indicating the relative values of d1 and d2.Return value Meaning Less than zero

                          d1 is less than d2. Zero

                        d1 and d2 are equal. Greater than zero

                          d1 is greater than d2.
        """
        ...

    @staticmethod
    def Divide(d1, d2):
        """
        Divide(d1: Decimal, d2: Decimal) -> Decimal

            Divides two specified System.Decimal values.

            d1: The dividend.

            d2: The divisor.

            Returns: The result of dividing d1 by d2.
        """
        ...

    @staticmethod
    def Floor(d):
        """
        Floor(d: Decimal) -> Decimal

            Rounds a specified System.Decimal number to the closest integer toward negative infinity.

            d: The value to round.

            Returns: If d has a fractional part, the next whole System.Decimal number toward negative infinity that is less than d.-or- If d doesn't have a fractional

             part, d is returned unchanged. Note that the method returns an integral value of type System.Decimal.
        """
        ...

    @staticmethod
    def FromOACurrency(cy):
        """
        FromOACurrency(cy: Int64) -> Decimal

            Converts the specified 64-bit signed integer, which contains an OLE Automation Currency value, to the equivalent System.Decimal value.

            cy: An OLE Automation Currency value.

            Returns: A System.Decimal that contains the equivalent of cy.
        """
        ...

    @staticmethod
    def GetBits(d):
        """
        GetBits(d: Decimal) -> Array[int]

            Converts the value of a specified instance of System.Decimal to its equivalent binary representation.

            d: The value to convert.

            Returns: A 32-bit signed integer array with four elements that contain the binary representation of d.
        """
        ...

    def GetHashCode(self):
        """
        GetHashCode(self: Decimal) -> int

            Returns the hash code for this instance.

            Returns: A 32-bit signed integer hash code.
        """
        ...

    @staticmethod
    def Multiply(d1, d2):
        """
        Multiply(d1: Decimal, d2: Decimal) -> Decimal

            Multiplies two specified System.Decimal values.

            d1: The multiplicand.

            d2: The multiplier.

            Returns: The result of multiplying d1 and d2.
        """
        ...

    @staticmethod
    def Negate(d):
        """
        Negate(d: Decimal) -> Decimal

            Returns the result of multiplying the specified System.Decimal value by negative one.

            d: The value to negate.

            Returns: A decimal number with the value of d, but the opposite sign.-or- Zero, if d is zero.
        """
        ...

    @staticmethod
    def Parse(s, *__args):
        """
        Parse(s: str) -> Decimal

            Converts the string representation of a number to its System.Decimal equivalent.

            s: The string representation of the number to convert.

            Returns: The equivalent to the number contained in s.

        Parse(s: str, style: NumberStyles) -> Decimal

            Converts the string representation of a number in a specified style to its System.Decimal equivalent.

            s: The string representation of the number to convert.

            style: A bitwise combination of System.Globalization.NumberStyles values that indicates the style elements that can be present in s. A typical value to

             specify is System.Globalization.NumberStyles.Number.

            Returns: The System.Decimal number equivalent to the number contained in s as specified by style.

        Parse(s: str, provider: IFormatProvider) -> Decimal

            Converts the string representation of a number to its System.Decimal equivalent using the specified culture-specific format information.

            s: The string representation of the number to convert.

            provider: An System.IFormatProvider that supplies culture-specific parsing information about s.

            Returns: The System.Decimal number equivalent to the number contained in s as specified by provider.

        Parse(s: str, style: NumberStyles, provider: IFormatProvider) -> Decimal

            Converts the string representation of a number to its System.Decimal equivalent using the specified style and culture-specific format.

            s: The string representation of the number to convert.

            style: A bitwise combination of System.Globalization.NumberStyles values that indicates the style elements that can be present in s. A typical value to

             specify is System.Globalization.NumberStyles.Number.

            provider: An System.IFormatProvider object that supplies culture-specific information about the format of s.

            Returns: The System.Decimal number equivalent to the number contained in s as specified by style and provider.
        """
        ...

    @staticmethod
    def Remainder(d1, d2):
        """
        Remainder(d1: Decimal, d2: Decimal) -> Decimal

            Computes the remainder after dividing two System.Decimal values.

            d1: The dividend.

            d2: The divisor.

            Returns: The remainder after dividing d1 by d2.
        """
        ...

    @staticmethod
    def Round(d, *__args):
        """
        Round(d: Decimal) -> Decimal

            Rounds a decimal value to the nearest integer.

            d: A decimal number to round.

            Returns: The integer that is nearest to the d parameter. If d is halfway between two integers, one of which is even and the other odd, the even number is

             returned.

        Round(d: Decimal, decimals: int) -> Decimal

            Rounds a System.Decimal value to a specified number of decimal places.

            d: A decimal number to round.

            decimals: A value from 0 to 28 that specifies the number of decimal places to round to.

            Returns: The decimal number equivalent to d rounded to decimals number of decimal places.

        Round(d: Decimal, mode: MidpointRounding) -> Decimal

            Rounds a decimal value to the nearest integer. A parameter specifies how to round the value if it is midway between two other numbers.

            d: A decimal number to round.

            mode: A value that specifies how to round d if it is midway between two other numbers.

            Returns: The integer that is nearest to the d parameter. If d is halfway between two numbers, one of which is even and the other odd, the mode parameter

             determines which of the two numbers is returned.

        Round(d: Decimal, decimals: int, mode: MidpointRounding) -> Decimal

            Rounds a decimal value to a specified precision. A parameter specifies how to round the value if it is midway between two other numbers.

            d: A decimal number to round.

            decimals: The number of significant decimal places (precision) in the return value.

            mode: A value that specifies how to round d if it is midway between two other numbers.

            Returns: The number that is nearest to the d parameter with a precision equal to the decimals parameter. If d is halfway between two numbers, one of which is

             even and the other odd, the mode parameter determines which of the two numbers is returned. If the precision of d is less than decimals, d is

             returned unchanged.
        """
        ...

    @staticmethod
    def Subtract(d1, d2):
        """
        Subtract(d1: Decimal, d2: Decimal) -> Decimal

            Subtracts one specified System.Decimal value from another.

            d1: The minuend.

            d2: The subtrahend.

            Returns: The result of subtracting d2 from d1.
        """
        ...

    @staticmethod
    def ToOACurrency(value):
        """
        ToOACurrency(value: Decimal) -> Int64

            Converts the specified System.Decimal value to the equivalent OLE Automation Currency value, which is contained in a 64-bit signed integer.

            value: The decimal number to convert.

            Returns: A 64-bit signed integer that contains the OLE Automation equivalent of value.
        """
        ...

    @staticmethod
    def Truncate(d):
        """
        Truncate(d: Decimal) -> Decimal

            Returns the integral digits of the specified System.Decimal; any fractional digits are discarded.

            d: The decimal number to truncate.

            Returns: The result of d rounded toward zero, to the nearest whole number.
        """
        ...

    @staticmethod
    def TryParse(s, *__args):
        """
        TryParse(s: str) -> (bool, Decimal)

            Converts the string representation of a number to its System.Decimal equivalent. A return value indicates whether the conversion succeeded or failed.

            s: The string representation of the number to convert.

            Returns: ue if s was converted successfully; otherwise, lse.

        TryParse(s: str, style: NumberStyles, provider: IFormatProvider) -> (bool, Decimal)

            Converts the string representation of a number to its System.Decimal equivalent using the specified style and culture-specific format. A return value

             indicates whether the conversion succeeded or failed.

            s: The string representation of the number to convert.

            style: A bitwise combination of enumeration values that indicates the permitted format of s. A typical value to specify is

             System.Globalization.NumberStyles.Number.

            provider: An object that supplies culture-specific parsing information about s.

            Returns: ue if s was converted successfully; otherwise, lse.
        """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __cmp__(self, *args): #cannot find CLR method
        """ x.__cmp__(y) <==> cmp(x,y) """
        ...

    def __complex__(self, *args): #cannot find CLR method
        """ __complex__(value: Decimal) -> float """
        ...

    def __div__(self, *args): #cannot find CLR method
        """ x.__div__(y) <==> x/y """
        ...

    def __float__(self, *args): #cannot find CLR method
        """ __complex__(value: Decimal) -> float """
        ...

    def __int__(self, *args): #cannot find CLR method
        """ __int__(value: Decimal) -> int """
        ...

    def __long__(self, *args): #cannot find CLR method
        """ __int__(value: Decimal) -> int """
        ...

    def __mod__(self, *args): #cannot find CLR method
        """ x.__mod__(y) <==> x%y """
        ...

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*y """
        ...

    def __neg__(self, *args): #cannot find CLR method
        """ x.__neg__() <==> -x """
        ...

    def __nonzero__(self, *args): #cannot find CLR method
        """ __nonzero__(x: Decimal) -> bool """
        ...

    def __pos__(self, *args): #cannot find CLR method
        """
        __pos__(d: Decimal) -> Decimal

            Returns the value of the System.Decimal operand (the sign of the operand is unchanged).

            d: The operand to return.

            Returns: The value of the operand, d.
        """
        ...

    def __radd__(self, *args): #cannot find CLR method
        """
        __radd__(d1: Decimal, d2: Decimal) -> Decimal

            Adds two specified System.Decimal values.

            d1: The first value to add.

            d2: The second value to add.

            Returns: The result of adding d1 and d2.
        """
        ...

    def __rdiv__(self, *args): #cannot find CLR method
        """
        __rdiv__(d1: Decimal, d2: Decimal) -> Decimal

            Divides two specified System.Decimal values.

            d1: The dividend.

            d2: The divisor.

            Returns: The result of dividing d1 by d2.
        """
        ...

    def __rmod__(self, *args): #cannot find CLR method
        """
        __rmod__(d1: Decimal, d2: Decimal) -> Decimal

            Returns the remainder resulting from dividing two specified System.Decimal values.

            d1: The dividend.

            d2: The divisor.

            Returns: The remainder resulting from dividing d1 by d2.
        """
        ...

    def __rmul__(self, *args): #cannot find CLR method
        """
        __rmul__(d1: Decimal, d2: Decimal) -> Decimal

            Multiplies two specified System.Decimal values.

            d1: The first value to multiply.

            d2: The second value to multiply.

            Returns: The result of multiplying d1 by d2.
        """
        ...

    def __rsub__(self, *args): #cannot find CLR method
        """
        __rsub__(d1: Decimal, d2: Decimal) -> Decimal

            Subtracts two specified System.Decimal values.

            d1: The minuend.

            d2: The subtrahend.

            Returns: The result of subtracting d2 from d1.
        """
        ...

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        ...

    MaxValue = None
    MinusOne = None
    MinValue = None
    One = None
    Zero = None


class DivideByZeroException(ArithmeticException): # skipped bases: <type 'ISerializable'>, <type '_Exception'>
    """
    The exception that is thrown when there is an attempt to divide an integral or System.Decimal value by zero.

    DivideByZeroException()

    DivideByZeroException(message: str)

    DivideByZeroException(message: str, innerException: Exception)
    """
    SerializeObjectState = None


class TypeLoadException(SystemException): # skipped bases: <type 'ISerializable'>, <type '_Exception'>
    """
    The exception that is thrown when type-loading failures occur.

    TypeLoadException()

    TypeLoadException(message: str)

    TypeLoadException(message: str, inner: Exception)
    """
    @property
    def TypeName(self):
        """
        Gets the fully qualified name of the type that causes the exception.

        Get: TypeName(self: TypeLoadException) -> str
        """
        ...


    SerializeObjectState = None


class DllNotFoundException(TypeLoadException): # skipped bases: <type 'ISerializable'>, <type '_Exception'>
    """
    The exception that is thrown when a DLL specified in a DLL import cannot be found.

    DllNotFoundException()

    DllNotFoundException(message: str)

    DllNotFoundException(message: str, inner: Exception)
    """
    SerializeObjectState = None


class Double: # skipped bases: <type 'object'>
    """ Represents a double-precision floating-point number. """
    def as_integer_ratio(self, *args): #cannot find CLR method
        """ as_integer_ratio(self: float) -> tuple """
        ...

    def conjugate(self, *args): #cannot find CLR method
        """ conjugate(x: float) -> float """
        ...

    def hex(self, *args): #cannot find CLR method
        """ hex(self: float) -> str """
        ...

    def is_integer(self, *args): #cannot find CLR method
        """ is_integer(self: float) -> bool """
        ...

    def __abs__(self, *args): #cannot find CLR method
        """ x.__abs__() <==> abs(x) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __coerce__(self, *args): #cannot find CLR method
        """ __coerce__(x: float, o: object) -> tuple """
        ...

    def __divmod__(self, *args): #cannot find CLR method
        """ __divmod__(x: float, y: float) -> object """
        ...

    def __div__(self, *args): #cannot find CLR method
        """ x.__div__(y) <==> x/y """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        ...

    def __float__(self, *args): #cannot find CLR method
        """ __float__(self: float) -> float """
        ...

    def __floordiv__(self, *args): #cannot find CLR method
        """ x.__floordiv__(y) <==> x//y """
        ...

    def __getformat__(self, *args): #cannot find CLR method
        """ __getformat__(typestr: str) -> str """
        ...

    def __getnewargs__(self, *args): #cannot find CLR method
        """ __getnewargs__(self: float) -> object """
        ...

    def __ge__(self, *args): #cannot find CLR method
        ...

    def __gt__(self, *args): #cannot find CLR method
        ...

    def __int__(self, *args): #cannot find CLR method
        """ __int__(d: float) -> object """
        ...

    def __le__(self, *args): #cannot find CLR method
        ...

    def __long__(self, *args): #cannot find CLR method
        """ __long__(self: float) -> long """
        ...

    def __lt__(self, *args): #cannot find CLR method
        ...

    def __mod__(self, *args): #cannot find CLR method
        """ x.__mod__(y) <==> x%y """
        ...

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*y """
        ...

    def __neg__(self, *args): #cannot find CLR method
        """ x.__neg__() <==> -x """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    def __nonzero__(self, *args): #cannot find CLR method
        """ __nonzero__(x: float) -> bool """
        ...

    def __pos__(self, *args): #cannot find CLR method
        """ __pos__(x: float) -> float """
        ...

    def __pow__(self, *args): #cannot find CLR method
        """ x.__pow__(y[, z]) <==> pow(x, y[, z]) """
        ...

    def __radd__(self, *args): #cannot find CLR method
        """ __radd__(x: float, y: float) -> float """
        ...

    def __rdivmod__(self, *args): #cannot find CLR method
        """ __rdivmod__(x: float, y: float) -> object """
        ...

    def __rdiv__(self, *args): #cannot find CLR method
        """ __rdiv__(x: float, y: float) -> float """
        ...

    def __rfloordiv__(self, *args): #cannot find CLR method
        """ __rfloordiv__(x: float, y: float) -> float """
        ...

    def __rmod__(self, *args): #cannot find CLR method
        """ __rmod__(x: float, y: float) -> float """
        ...

    def __rmul__(self, *args): #cannot find CLR method
        """ __rmul__(x: float, y: float) -> float """
        ...

    def __rpow__(self, *args): #cannot find CLR method
        """ __rpow__(x: float, y: float) -> float """
        ...

    def __rsub__(self, *args): #cannot find CLR method
        """ __rsub__(x: float, y: float) -> float """
        ...

    def __rtruediv__(self, *args): #cannot find CLR method
        """ __rtruediv__(x: float, y: float) -> float """
        ...

    def __setformat__(self, *args): #cannot find CLR method
        """ __setformat__(typestr: str, fmt: str) """
        ...

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        ...

    def __truediv__(self, *args): #cannot find CLR method
        """ x.__truediv__(y) <==> x/y """
        ...

    def __trunc__(self, *args): #cannot find CLR method
        """ __trunc__(x: float) -> object """
        ...

    imag = None
    real = None


class DuplicateWaitObjectException(ArgumentException): # skipped bases: <type 'ISerializable'>, <type '_Exception'>
    """
    The exception that is thrown when an object appears more than once in an array of synchronization objects.

    DuplicateWaitObjectException()

    DuplicateWaitObjectException(parameterName: str)

    DuplicateWaitObjectException(parameterName: str, message: str)

    DuplicateWaitObjectException(message: str, innerException: Exception)
    """
    SerializeObjectState = None


class EntryPointNotFoundException(TypeLoadException): # skipped bases: <type 'ISerializable'>, <type '_Exception'>
    """
    The exception that is thrown when an attempt to load a class fails due to the absence of an entry method.

    EntryPointNotFoundException()

    EntryPointNotFoundException(message: str)

    EntryPointNotFoundException(message: str, inner: Exception)
    """
    SerializeObjectState = None


class Environment: # skipped bases: <type 'object'>
    """ Provides information about, and means to manipulate, the current environment and platform. This class cannot be inherited. """
    @property
    def CommandLine(self):
        """
        Gets the command line for this process.

        Get: CommandLine() -> str
        """
        ...

    @property
    def CurrentDirectory(self):
        """
        Gets or sets the fully qualified path of the current working directory.

        Get: CurrentDirectory() -> str

        Set: CurrentDirectory() = value
        """
        ...

    @property
    def CurrentManagedThreadId(self):
        """
        Gets a unique identifier for the current managed thread.

        Get: CurrentManagedThreadId() -> int
        """
        ...

    @property
    def ExitCode(self):
        """
        Gets or sets the exit code of the process.

        Get: ExitCode() -> int

        Set: ExitCode() = value
        """
        ...

    @property
    def HasShutdownStarted(self):
        """
        Gets a value that indicates whether the current application domain is being unloaded or the common language runtime (CLR) is shutting down.

        Get: HasShutdownStarted() -> bool
        """
        ...

    @property
    def Is64BitOperatingSystem(self):
        """
        Determines whether the current operating system is a 64-bit operating system.

        Get: Is64BitOperatingSystem() -> bool
        """
        ...

    @property
    def Is64BitProcess(self):
        """
        Determines whether the current process is a 64-bit process.

        Get: Is64BitProcess() -> bool
        """
        ...

    @property
    def MachineName(self):
        """
        Gets the NetBIOS name of this local computer.

        Get: MachineName() -> str
        """
        ...

    @property
    def NewLine(self):
        """
        Gets the newline string defined for this environment.

        Get: NewLine() -> str
        """
        ...

    @property
    def OSVersion(self):
        """
        Gets an System.OperatingSystem object that contains the current platform identifier and version number.

        Get: OSVersion() -> OperatingSystem
        """
        ...

    @property
    def ProcessorCount(self):
        """
        Gets the number of processors on the current machine.

        Get: ProcessorCount() -> int
        """
        ...

    @property
    def StackTrace(self):
        """
        Gets current stack trace information.

        Get: StackTrace() -> str
        """
        ...

    @property
    def SystemDirectory(self):
        """
        Gets the fully qualified path of the system directory.

        Get: SystemDirectory() -> str
        """
        ...

    @property
    def SystemPageSize(self):
        """
        Gets the number of bytes in the operating system's memory page.

        Get: SystemPageSize() -> int
        """
        ...

    @property
    def TickCount(self):
        """
        Gets the number of milliseconds elapsed since the system started.

        Get: TickCount() -> int
        """
        ...

    @property
    def UserDomainName(self):
        """
        Gets the network domain name associated with the current user.

        Get: UserDomainName() -> str
        """
        ...

    @property
    def UserInteractive(self):
        """
        Gets a value indicating whether the current process is running in user interactive mode.

        Get: UserInteractive() -> bool
        """
        ...

    @property
    def UserName(self):
        """
        Gets the user name of the person who is currently logged on to the Windows operating system.

        Get: UserName() -> str
        """
        ...

    @property
    def Version(self):
        """
        Gets a System.Version object that describes the major, minor, build, and revision numbers of the common language runtime.

        Get: Version() -> Version
        """
        ...

    @property
    def WorkingSet(self):
        """
        Gets the amount of physical memory mapped to the process context.

        Get: WorkingSet() -> Int64
        """
        ...


    @staticmethod
    def Exit(exitCode):
        """
        Exit(exitCode: int)

            Terminates this process and returns an exit code to the operating system.

            exitCode: The exit code to return to the operating system. Use 0 (zero) to indicate that the process completed successfully.
        """
        ...

    @staticmethod
    def ExpandEnvironmentVariables(name):
        """
        ExpandEnvironmentVariables(name: str) -> str

            Replaces the name of each environment variable embedded in the specified string with the string equivalent of the value of the variable, then returns

             the resulting string.

            name: A string containing the names of zero or more environment variables. Each environment variable is quoted with the percent sign character (%).

            Returns: A string with each environment variable replaced by its value.
        """
        ...

    @staticmethod
    def FailFast(message, exception=...):
        """
        FailFast(message: str)

            Immediately terminates a process after writing a message to the Windows Application event log, and then includes the message in error reporting to

             Microsoft.

            message: A message that explains why the process was terminated, or ll if no explanation is provided.

        FailFast(message: str, exception: Exception)

            Immediately terminates a process after writing a message to the Windows Application event log, and then includes the message and exception

             information in error reporting to Microsoft.

            message: A message that explains why the process was terminated, or ll if no explanation is provided.

            exception: An exception that represents the error that caused the termination. This is typically the exception in a tch block.
        """
        ...

    @staticmethod
    def GetCommandLineArgs():
        """
        GetCommandLineArgs() -> Array[str]

            Returns a string array containing the command-line arguments for the current process.

            Returns: An array of string where each element contains a command-line argument. The first element is the executable file name, and the following zero or more

             elements contain the remaining command-line arguments.
        """
        ...

    @staticmethod
    def GetEnvironmentVariable(variable, target=...):
        """
        GetEnvironmentVariable(variable: str) -> str

            Retrieves the value of an environment variable from the current process.

            variable: The name of the environment variable.

            Returns: The value of the environment variable specified by variable, or ll if the environment variable is not found.

        GetEnvironmentVariable(variable: str, target: EnvironmentVariableTarget) -> str

            Retrieves the value of an environment variable from the current process or from the Windows operating system registry key for the current user or

             local machine.

            variable: The name of an environment variable.

            target: One of the System.EnvironmentVariableTarget values.

            Returns: The value of the environment variable specified by the variable and target parameters, or ll if the environment variable is not found.
        """
        ...

    @staticmethod
    def GetEnvironmentVariables(target=...):
        """
        GetEnvironmentVariables() -> IDictionary

            Retrieves all environment variable names and their values from the current process.

            Returns: A dictionary that contains all environment variable names and their values; otherwise, an empty dictionary if no environment variables are found.

        GetEnvironmentVariables(target: EnvironmentVariableTarget) -> IDictionary

            Retrieves all environment variable names and their values from the current process, or from the Windows operating system registry key for the current

             user or local machine.

            target: One of the System.EnvironmentVariableTarget values.

            Returns: A dictionary that contains all environment variable names and their values from the source specified by the target parameter; otherwise, an empty

             dictionary if no environment variables are found.
        """
        ...

    @staticmethod
    def GetFolderPath(folder, option=...):
        """
        GetFolderPath(folder: SpecialFolder) -> str

        GetFolderPath(folder: SpecialFolder, option: SpecialFolderOption) -> str
        """
        ...

    @staticmethod
    def GetLogicalDrives():
        """
        GetLogicalDrives() -> Array[str]

            Returns an array of string containing the names of the logical drives on the current computer.

            Returns: An array of strings where each element contains the name of a logical drive. For example, if the computer's hard drive is the first logical drive,

             the first element returned is "C:\".
        """
        ...

    @staticmethod
    def SetEnvironmentVariable(variable, value, target=...):
        """
        SetEnvironmentVariable(variable: str, value: str)

            Creates, modifies, or deletes an environment variable stored in the current process.

            variable: The name of an environment variable.

            value: A value to assign to variable.

        SetEnvironmentVariable(variable: str, value: str, target: EnvironmentVariableTarget)

            Creates, modifies, or deletes an environment variable stored in the current process or in the Windows operating system registry key reserved for the

             current user or local machine.

            variable: The name of an environment variable.

            value: A value to assign to variable.

            target: One of the enumeration values that specifies the location of the environment variable.
        """
        ...

    def SpecialFolder(self, *args): #cannot find CLR method
        """ enum SpecialFolder, values: AdminTools (48), ApplicationData (26), CDBurning (59), CommonAdminTools (47), CommonApplicationData (35), CommonDesktopDirectory (25), CommonDocuments (46), CommonMusic (53), CommonOemLinks (58), CommonPictures (54), CommonProgramFiles (43), CommonProgramFilesX86 (44), CommonPrograms (23), CommonStartMenu (22), CommonStartup (24), CommonTemplates (45), CommonVideos (55), Cookies (33), Desktop (0), DesktopDirectory (16), Favorites (6), Fonts (20), History (34), InternetCache (32), LocalApplicationData (28), LocalizedResources (57), MyComputer (17), MyDocuments (5), MyMusic (13), MyPictures (39), MyVideos (14), NetworkShortcuts (19), Personal (5), PrinterShortcuts (27), ProgramFiles (38), ProgramFilesX86 (42), Programs (2), Recent (8), Resources (56), SendTo (9), StartMenu (11), Startup (7), System (37), SystemX86 (41), Templates (21), UserProfile (40), Windows (36) """
        ...

    def SpecialFolderOption(self, *args): #cannot find CLR method
        """ enum SpecialFolderOption, values: Create (32768), DoNotVerify (16384), None (0) """
        ...

    __all__ = [
        'Exit',
        'ExpandEnvironmentVariables',
        'FailFast',
        'GetCommandLineArgs',
        'GetEnvironmentVariable',
        'GetEnvironmentVariables',
        'GetFolderPath',
        'GetLogicalDrives',
        'SetEnvironmentVariable',
        'SpecialFolder',
        'SpecialFolderOption',
    ]


class EnvironmentVariableTarget(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>
    """
    Specifies the location where an environment variable is stored or retrieved in a set or get operation.

    enum EnvironmentVariableTarget, values: Machine (2), Process (0), User (1)
    """
    Machine = None
    Process = None
    User = None
    value__ = None


class EventHandler:
    """
    Represents the method that will handle an event that has no event data.

    EventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: EventHandler, sender: object, e: EventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

# Error generating skeleton for function CombineImpl: 'type' object has no attribute '__bases__'

# Error generating skeleton for function DynamicInvokeImpl: 'type' object has no attribute '__bases__'

    def EndInvoke(self, result):
        """ EndInvoke(self: EventHandler, result: IAsyncResult) """
        ...

# Error generating skeleton for function GetMethodImpl: 'type' object has no attribute '__bases__'

    def Invoke(self, sender, e):
        """ Invoke(self: EventHandler, sender: object, e: EventArgs) """
        ...

# Error generating skeleton for function RemoveImpl: 'type' object has no attribute '__bases__'

    @staticmethod # known case of __new__
    def __new__(cls, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        ...

# Error generating skeleton for function __reduce_ex__: 'type' object has no attribute '__bases__'


class ExecutionEngineException(SystemException): # skipped bases: <type 'ISerializable'>, <type '_Exception'>
    """
    The exception that is thrown when there is an internal error in the execution engine of the common language runtime. This class cannot be inherited.

    ExecutionEngineException()

    ExecutionEngineException(message: str)

    ExecutionEngineException(message: str, innerException: Exception)
    """
    SerializeObjectState = None


class MemberAccessException(SystemException): # skipped bases: <type 'ISerializable'>, <type '_Exception'>
    """
    The exception that is thrown when an attempt to access a class member fails.

    MemberAccessException()

    MemberAccessException(message: str)

    MemberAccessException(message: str, inner: Exception)
    """
    SerializeObjectState = None


class FieldAccessException(MemberAccessException): # skipped bases: <type 'ISerializable'>, <type '_Exception'>
    """
    The exception that is thrown when there is an invalid attempt to access a private or protected field inside a class.

    FieldAccessException()

    FieldAccessException(message: str)

    FieldAccessException(message: str, inner: Exception)
    """
    SerializeObjectState = None


class UriParser: # skipped bases: <type 'object'>
    """ Parses a new URI scheme. This is an abstract class. """
    def GetComponents(self, *args): #cannot find CLR method
        """
        GetComponents(self: UriParser, uri: Uri, components: UriComponents, format: UriFormat) -> str

            Gets the components from a URI.

            uri: The URI to parse.

            components: The System.UriComponents to retrieve from uri.

            format: One of the System.UriFormat values that controls how special characters are escaped.

            Returns: A string that contains the components.
        """
        ...

    def InitializeAndValidate(self, *args): #cannot find CLR method
        """
        InitializeAndValidate(self: UriParser, uri: Uri) -> UriFormatException

            Initialize the state of the parser and validate the URI.

            uri: The T:System.Uri to validate.
        """
        ...

    def IsBaseOf(self, *args): #cannot find CLR method
        """
        IsBaseOf(self: UriParser, baseUri: Uri, relativeUri: Uri) -> bool

            Determines whether baseUri is a base URI for relativeUri.

            baseUri: The base URI.

            relativeUri: The URI to test.

            Returns: ue if baseUri is a base URI for relativeUri; otherwise, lse.
        """
        ...

    @staticmethod
    def IsKnownScheme(schemeName):
        """
        IsKnownScheme(schemeName: str) -> bool

            Indicates whether the parser for a scheme is registered.

            schemeName: The scheme name to check.

            Returns: ue if schemeName has been registered; otherwise, lse.
        """
        ...

    def IsWellFormedOriginalString(self, *args): #cannot find CLR method
        """
        IsWellFormedOriginalString(self: UriParser, uri: Uri) -> bool

            Indicates whether a URI is well-formed.

            uri: The URI to check.

            Returns: ue if uri is well-formed; otherwise, lse.
        """
        ...

    def OnNewUri(self, *args): #cannot find CLR method
        """
        OnNewUri(self: UriParser) -> UriParser

            Invoked by a System.Uri constructor to get a System.UriParser instance

            Returns: A System.UriParser for the constructed System.Uri.
        """
        ...

    def OnRegister(self, *args): #cannot find CLR method
        """
        OnRegister(self: UriParser, schemeName: str, defaultPort: int)

            Invoked by the Framework when a System.UriParser method is registered.

            schemeName: The scheme that is associated with this System.UriParser.

            defaultPort: The port number of the scheme.
        """
        ...

    @staticmethod
    def Register(uriParser, schemeName, defaultPort):
        """
        Register(uriParser: UriParser, schemeName: str, defaultPort: int)

            Associates a scheme and port number with a System.UriParser.

            uriParser: The URI parser to register.

            schemeName: The name of the scheme that is associated with this parser.

            defaultPort: The default port number for the specified scheme.
        """
        ...

    def Resolve(self, *args): #cannot find CLR method
        """
        Resolve(self: UriParser, baseUri: Uri, relativeUri: Uri) -> (str, UriFormatException)

            Called by System.Uri constructors and erload:System.Uri.TryCreate to resolve a relative URI.

            baseUri: A base URI.

            relativeUri: A relative URI.

            Returns: The string of the resolved relative System.Uri.
        """
        ...


class FileStyleUriParser(UriParser):
    """
    A customizable parser based on the File scheme.

    FileStyleUriParser()
    """
    pass

class FlagsAttribute(Attribute): # skipped bases: <type '_Attribute'>
    """
    Indicates that an enumeration can be treated as a bit field; that is, a set of flags.

    FlagsAttribute()
    """
    pass

class FormatException(SystemException): # skipped bases: <type 'ISerializable'>, <type '_Exception'>
    """
    The exception that is thrown when the format of an argument is invalid, or when a composite format string is not well formed.

    FormatException()

    FormatException(message: str)

    FormatException(message: str, innerException: Exception)
    """
    SerializeObjectState = None


class FormattableString( IFormattable):
    """ Represents a composite format string, along with the arguments to be formatted. """
    @property
    def ArgumentCount(self):
        """
        Gets the number of arguments to be formatted.

        Get: ArgumentCount(self: FormattableString) -> int
        """
        ...

    @property
    def Format(self):
        """
        Returns the composite format string.

        Get: Format(self: FormattableString) -> str
        """
        ...


    def GetArgument(self, index):
        """
        GetArgument(self: FormattableString, index: int) -> object

            Returns the argument at the specified index position.

            index: The index of the argument. Its value can range from zero to one less than the value of System.FormattableString.ArgumentCount.

            Returns: The argument.
        """
        ...

    def GetArguments(self):
        """
        GetArguments(self: FormattableString) -> Array[object]

            Returns an object array that contains one or more objects to format.

            Returns: An object array that contains one or more objects to format.
        """
        ...

    @staticmethod
    def Invariant(formattable):
        """
        Invariant(formattable: FormattableString) -> str

            Returns a result string in which arguments are formatted by using the conventions of the invariant culture.

            formattable: The object to convert to a result string.

            Returns: The string that results from formatting the current instance by using the conventions of the invariant culture.
        """
        ...


class FtpStyleUriParser(UriParser):
    """
    A customizable parser based on the File Transfer Protocol (FTP) scheme.

    FtpStyleUriParser()
    """
    pass

class GC: # skipped bases: <type 'object'>
    """ Controls the system garbage collector, a service that automatically reclaims unused memory. """
    @property
    def MaxGeneration(self):
        """
        Gets the maximum number of generations that the system currently supports.

        Get: MaxGeneration() -> int
        """
        ...


    @staticmethod
    def AddMemoryPressure(bytesAllocated):
        """
        AddMemoryPressure(bytesAllocated: Int64)

            Informs the runtime of a large allocation of unmanaged memory that should be taken into account when scheduling garbage collection.

            bytesAllocated: The incremental amount of unmanaged memory that has been allocated.
        """
        ...

    @staticmethod
    def CancelFullGCNotification():
        """
        CancelFullGCNotification()

            Cancels the registration of a garbage collection notification.
        """
        ...

    @staticmethod
    def Collect(generation=..., mode=..., blocking=..., compacting=...):
        """
        Collect(generation: int)

            Forces an immediate garbage collection from generation 0 through a specified generation.

            generation: The number of the oldest generation to be garbage collected.

        Collect()

            Forces an immediate garbage collection of all generations.

        Collect(generation: int, mode: GCCollectionMode)

            Forces a garbage collection from generation 0 through a specified generation, at a time specified by a System.GCCollectionMode value.

            generation: The number of the oldest generation to be garbage collected.

            mode: An enumeration value that specifies whether the garbage collection is forced (System.GCCollectionMode.Default or System.GCCollectionMode.Forced) or

             optimized (System.GCCollectionMode.Optimized).

        Collect(generation: int, mode: GCCollectionMode, blocking: bool)

            Forces a garbage collection from generation 0 through a specified generation, at a time specified by a System.GCCollectionMode value, with a value

             specifying whether the collection should be blocking.

            generation: The number of the oldest generation to be garbage collected.

            mode: An enumeration value that specifies whether the garbage collection is forced (System.GCCollectionMode.Default or System.GCCollectionMode.Forced) or

             optimized (System.GCCollectionMode.Optimized).

            blocking: ue to perform a blocking garbage collection; lse to perform a background garbage collection where possible.

        Collect(generation: int, mode: GCCollectionMode, blocking: bool, compacting: bool)

            Forces a garbage collection from generation 0 through a specified generation, at a time specified by a System.GCCollectionMode value, with values

             that specify whether the collection should be blocking and compacting.

            generation: The number of the oldest generation to be garbage collected.

            mode: An enumeration value that specifies whether the garbage collection is forced (System.GCCollectionMode.Default or System.GCCollectionMode.Forced) or

             optimized (System.GCCollectionMode.Optimized).

            blocking: ue to perform a blocking garbage collection; lse to perform a background garbage collection where possible. See the Remarks section for more

             information.

            compacting: ue to compact the small object heap; lse to sweep only. See the Remarks section for more information.
        """
        ...

    @staticmethod
    def CollectionCount(generation):
        """
        CollectionCount(generation: int) -> int

            Returns the number of times garbage collection has occurred for the specified generation of objects.

            generation: The generation of objects for which the garbage collection count is to be determined.

            Returns: The number of times garbage collection has occurred for the specified generation since the process was started.
        """
        ...

    @staticmethod
    def EndNoGCRegion():
        """
        EndNoGCRegion()

            Ends the no GC region latency mode.
        """
        ...

    @staticmethod
    def GetAllocatedBytesForCurrentThread():
        """ GetAllocatedBytesForCurrentThread() -> Int64 """
        ...

    @staticmethod
    def GetGeneration(*__args):
        """
        GetGeneration(wo: WeakReference) -> int

            Returns the current generation number of the target of a specified weak reference.

            wo: A System.WeakReference that refers to the target object whose generation number is to be determined.

            Returns: The current generation number of the target of wo.

        GetGeneration(obj: object) -> int

            Returns the current generation number of the specified object.

            obj: The object that generation information is retrieved for.

            Returns: The current generation number of obj.
        """
        ...

    @staticmethod
    def GetTotalMemory(forceFullCollection):
        """
        GetTotalMemory(forceFullCollection: bool) -> Int64

            Retrieves the number of bytes currently thought to be allocated. A parameter indicates whether this method can wait a short interval before

             returning, to allow the system to collect garbage and finalize objects.

            forceFullCollection: ue to indicate that this method can wait for garbage collection to occur before returning; otherwise, lse.

            Returns: A number that is the best available approximation of the number of bytes currently allocated in managed memory.
        """
        ...

    @staticmethod
    def KeepAlive(obj):
        """
        KeepAlive(obj: object)

            References the specified object, which makes it ineligible for garbage collection from the start of the current routine to the point where this

             method is called.

            obj: The object to reference.
        """
        ...

    @staticmethod
    def RegisterForFullGCNotification(maxGenerationThreshold, largeObjectHeapThreshold):
        """
        RegisterForFullGCNotification(maxGenerationThreshold: int, largeObjectHeapThreshold: int)

            Specifies that a garbage collection notification should be raised when conditions favor full garbage collection and when the collection has been

             completed.

            maxGenerationThreshold: A number between 1 and 99 that specifies when the notification should be raised based on the objects allocated in generation 2.

            largeObjectHeapThreshold: A number between 1 and 99 that specifies when the notification should be raised based on objects allocated in the large object heap.
        """
        ...

    @staticmethod
    def RemoveMemoryPressure(bytesAllocated):
        """
        RemoveMemoryPressure(bytesAllocated: Int64)

            Informs the runtime that unmanaged memory has been released and no longer needs to be taken into account when scheduling garbage collection.

            bytesAllocated: The amount of unmanaged memory that has been released.
        """
        ...

    @staticmethod
    def ReRegisterForFinalize(obj):
        """
        ReRegisterForFinalize(obj: object)

            Requests that the system call the finalizer for the specified object for which System.GC.SuppressFinalize(System.Object) has previously been called.

            obj: The object that a finalizer must be called for.
        """
        ...

    @staticmethod
    def SuppressFinalize(obj):
        """
        SuppressFinalize(obj: object)

            Requests that the common language runtime not call the finalizer for the specified object.

            obj: The object whose finalizer must not be executed.
        """
        ...

    @staticmethod
    def TryStartNoGCRegion(totalSize, *__args):
        """
        TryStartNoGCRegion(totalSize: Int64) -> bool

            Attempts to disallow garbage collection during the execution of a critical path if a specified amount of memory is available.

            totalSize: The amount of memory in bytes to allocate without triggering a garbage collection. It must be less than or equal to the size of an ephemeral segment.

             For information on the size of an ephemeral segement, see the "Ephemeral generations and segments" section in the Fundamentals of Garbage Collection

             article.

            Returns: ue if the runtime was able to commit the required amount of memory and the garbage collector is able to enter no GC region latency mode; otherwise,

             lse.

        TryStartNoGCRegion(totalSize: Int64, lohSize: Int64) -> bool

            Attempts to disallow garbage collection during the execution of a critical path if a specified amount of memory is available for the large object

             heap and the small object heap.

                     ephemeral segment. For information on the size of an ephemeral segement, see the "Ephemeral generations and segments" section in the Fundamentals of

             Garbage Collection article.

            lohSize: The number of bytes in totalSize to use for large object heap (LOH) allocations.

            Returns: ue if the runtime was able to commit the required amount of memory and the garbage collector is able to enter no GC region latency mode; otherwise,

             lse.

        TryStartNoGCRegion(totalSize: Int64, disallowFullBlockingGC: bool) -> bool

            Attempts to disallow garbage collection during the execution of a critical path if a specified amount of memory is available, and controls whether

             the garbage collector does a full blocking garbage collection if not enough memory is initially available.

            totalSize: The amount of memory in bytes to allocate without triggering a garbage collection. It must be less than or equal to the size of an ephemeral segment.

             For information on the size of an ephemeral segement, see the "Ephemeral generations and segments" section in the Fundamentals of Garbage Collection

             article.

            disallowFullBlockingGC: ue to omit a full blocking garbage collection if the garbage collector is initially unable to allocate totalSize bytes; otherwise, lse.

            Returns: ue if the runtime was able to commit the required amount of memory and the garbage collector is able to enter no GC region latency mode; otherwise,

             lse.

        TryStartNoGCRegion(totalSize: Int64, lohSize: Int64, disallowFullBlockingGC: bool) -> bool

            Attempts to disallow garbage collection during the execution of a critical path if a specified amount of memory is available for the large object

             heap and the small object heap, and controls whether the garbage collector does a full blocking garbage collection if not enough memory is initially

             available.

                     ephemeral segment. For information on the size of an ephemeral segement, see the "Ephemeral generations and segments" section in the Fundamentals of

             Garbage Collection article.

            lohSize: The number of bytes in totalSize to use for large object heap (LOH) allocations.

            disallowFullBlockingGC: ue to omit a full blocking garbage collection if the garbage collector is initially unable to allocate the specified memory on the small object heap

             (SOH) and LOH; otherwise, lse.

            Returns: ue if the runtime was able to commit the required amount of memory and the garbage collector is able to enter no GC region latency mode; otherwise,

             lse.
        """
        ...

    @staticmethod
    def WaitForFullGCApproach(millisecondsTimeout=...):
        """
        WaitForFullGCApproach() -> GCNotificationStatus

            Returns the status of a registered notification for determining whether a full, blocking garbage collection by the common language runtime is

             imminent.

            Returns: The status of the registered garbage collection notification.

        WaitForFullGCApproach(millisecondsTimeout: int) -> GCNotificationStatus

            Returns, in a specified time-out period, the status of a registered notification for determining whether a full, blocking garbage collection by the

             common language runtime is imminent.

            millisecondsTimeout: The length of time to wait before a notification status can be obtained. Specify -1 to wait indefinitely.

            Returns: The status of the registered garbage collection notification.
        """
        ...

    @staticmethod
    def WaitForFullGCComplete(millisecondsTimeout=...):
        """
        WaitForFullGCComplete() -> GCNotificationStatus

            Returns the status of a registered notification for determining whether a full, blocking garbage collection by the common language runtime has

             completed.

            Returns: The status of the registered garbage collection notification.

        WaitForFullGCComplete(millisecondsTimeout: int) -> GCNotificationStatus

            Returns, in a specified time-out period, the status of a registered notification for determining whether a full, blocking garbage collection by

             common language the runtime has completed.

            millisecondsTimeout: The length of time to wait before a notification status can be obtained. Specify -1 to wait indefinitely.

            Returns: The status of the registered garbage collection notification.
        """
        ...

    @staticmethod
    def WaitForPendingFinalizers():
        """
        WaitForPendingFinalizers()

            Suspends the current thread until the thread that is processing the queue of finalizers has emptied that queue.
        """
        ...

    __all__ = [
        'AddMemoryPressure',
        'CancelFullGCNotification',
        'Collect',
        'CollectionCount',
        'EndNoGCRegion',
        'GetAllocatedBytesForCurrentThread',
        'GetGeneration',
        'GetTotalMemory',
        'KeepAlive',
        'RegisterForFullGCNotification',
        'RemoveMemoryPressure',
        'ReRegisterForFinalize',
        'SuppressFinalize',
        'TryStartNoGCRegion',
        'WaitForFullGCApproach',
        'WaitForFullGCComplete',
        'WaitForPendingFinalizers',
    ]


class GCCollectionMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>
    """
    Specifies the behavior for a forced garbage collection.

    enum GCCollectionMode, values: Default (0), Forced (1), Optimized (2)
    """
    Default = None
    Forced = None
    Optimized = None
    value__ = None


class GCNotificationStatus(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>
    """
    Provides information about the current registration for notification of the next full garbage collection.

    enum GCNotificationStatus, values: Canceled (2), Failed (1), NotApplicable (4), Succeeded (0), Timeout (3)
    """
    Canceled = None
    Failed = None
    NotApplicable = None
    Succeeded = None
    Timeout = None
    value__ = None


class GenericUriParser(UriParser):
    """
    A customizable parser for a hierarchical URI.

    GenericUriParser(options: GenericUriParserOptions)
    """
    @staticmethod # known case of __new__
    def __new__(cls, options):
        """ __new__(cls: type, options: GenericUriParserOptions) """
        ...


class GenericUriParserOptions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>
    """
    Specifies options for a System.UriParser.

    enum (flags) GenericUriParserOptions, values: AllowEmptyAuthority (2), Default (0), DontCompressPath (128), DontConvertPathBackslashes (64), DontUnescapePathDotsAndSlashes (256), GenericAuthority (1), Idn (512), IriParsing (1024), NoFragment (32), NoPort (8), NoQuery (16), NoUserInfo (4)
    """
    AllowEmptyAuthority = None
    Default = None
    DontCompressPath = None
    DontConvertPathBackslashes = None
    DontUnescapePathDotsAndSlashes = None
    GenericAuthority = None
    Idn = None
    IriParsing = None
    NoFragment = None
    NoPort = None
    NoQuery = None
    NoUserInfo = None
    value__ = None


class GopherStyleUriParser(UriParser):
    """
    A customizable parser based on the Gopher scheme.

    GopherStyleUriParser()
    """
    pass

class Guid( IFormattable, IComparable, IEquatable):
    """
    Represents a globally unique identifier (GUID).To browse the .NET Framework source code for this type, see the Reference Source.

    Guid(b: Array[Byte])

    Guid(a: UInt32, b: UInt16, c: UInt16, d: Byte, e: Byte, f: Byte, g: Byte, h: Byte, i: Byte, j: Byte, k: Byte)

    Guid(a: int, b: Int16, c: Int16, d: Array[Byte])

    Guid(a: int, b: Int16, c: Int16, d: Byte, e: Byte, f: Byte, g: Byte, h: Byte, i: Byte, j: Byte, k: Byte)

    Guid(g: str)
    """
    def GetHashCode(self):
        """
        GetHashCode(self: Guid) -> int

            Returns the hash code for this instance.

            Returns: The hash code for this instance.
        """
        ...

    @staticmethod
    def NewGuid():
        """
        NewGuid() -> Guid

            Initializes a new instance of the System.Guid structure.

            Returns: A new GUID object.
        """
        ...

    @staticmethod
    def Parse(input):
        """
        Parse(input: str) -> Guid

            Converts the string representation of a GUID to the equivalent System.Guid structure.

            input: The string to convert.

            Returns: A structure that contains the value that was parsed.
        """
        ...

    @staticmethod
    def ParseExact(input, format):
        """
        ParseExact(input: str, format: str) -> Guid

            Converts the string representation of a GUID to the equivalent System.Guid structure, provided that the string is in the specified format.

            input: The GUID to convert.

            format: One of the following specifiers that indicates the exact format to use when interpreting input: "N", "D", "B", "P", or "X".

            Returns: A structure that contains the value that was parsed.
        """
        ...

    def ToByteArray(self):
        """
        ToByteArray(self: Guid) -> Array[Byte]

            Returns a 16-element byte array that contains the value of this instance.

            Returns: A 16-element byte array.
        """
        ...

    @staticmethod
    def TryParse(input, result):
        """
        TryParse(input: str) -> (bool, Guid)

            Converts the string representation of a GUID to the equivalent System.Guid structure.

            input: The GUID to convert.

            Returns: ue if the parse operation was successful; otherwise, lse.
        """
        ...

    @staticmethod
    def TryParseExact(input, format, result):
        """
        TryParseExact(input: str, format: str) -> (bool, Guid)

            Converts the string representation of a GUID to the equivalent System.Guid structure, provided that the string is in the specified format.

            input: The GUID to convert.

            format: One of the following specifiers that indicates the exact format to use when interpreting input: "N", "D", "B", "P", or "X".

            Returns: ue if the parse operation was successful; otherwise, lse.
        """
        ...

    Empty = None


class HttpStyleUriParser(UriParser):
    """
    A customizable parser based on the HTTP scheme.

    HttpStyleUriParser()
    """
    pass

class IAppDomainSetup:
    """ Represents assembly binding information that can be added to an instance of System.AppDomain. """
    @property
    def ApplicationBase(self):
        """
        Gets or sets the name of the directory containing the application.

        Get: ApplicationBase(self: IAppDomainSetup) -> str

        Set: ApplicationBase(self: IAppDomainSetup) = value
        """
        ...

    @property
    def ApplicationName(self):
        """
        Gets or sets the name of the application.

        Get: ApplicationName(self: IAppDomainSetup) -> str

        Set: ApplicationName(self: IAppDomainSetup) = value
        """
        ...

    @property
    def CachePath(self):
        """
        Gets and sets the name of an area specific to the application where files are shadow copied.

        Get: CachePath(self: IAppDomainSetup) -> str

        Set: CachePath(self: IAppDomainSetup) = value
        """
        ...

    @property
    def ConfigurationFile(self):
        """
        Gets and sets the name of the configuration file for an application domain.

        Get: ConfigurationFile(self: IAppDomainSetup) -> str

        Set: ConfigurationFile(self: IAppDomainSetup) = value
        """
        ...

    @property
    def DynamicBase(self):
        """
        Gets or sets the directory where dynamically generated files are stored and accessed.

        Get: DynamicBase(self: IAppDomainSetup) -> str

        Set: DynamicBase(self: IAppDomainSetup) = value
        """
        ...

    @property
    def LicenseFile(self):
        """
        Gets or sets the location of the license file associated with this domain.

        Get: LicenseFile(self: IAppDomainSetup) -> str

        Set: LicenseFile(self: IAppDomainSetup) = value
        """
        ...

    @property
    def PrivateBinPath(self):
        """
        Gets or sets the list of directories that is combined with the System.AppDomainSetup.ApplicationBase directory to probe for private assemblies.

        Get: PrivateBinPath(self: IAppDomainSetup) -> str

        Set: PrivateBinPath(self: IAppDomainSetup) = value
        """
        ...

    @property
    def PrivateBinPathProbe(self):
        """
        Gets or sets the private binary directory path used to locate an application.

        Get: PrivateBinPathProbe(self: IAppDomainSetup) -> str

        Set: PrivateBinPathProbe(self: IAppDomainSetup) = value
        """
        ...

    @property
    def ShadowCopyDirectories(self):
        """
        Gets or sets the names of the directories containing assemblies to be shadow copied.

        Get: ShadowCopyDirectories(self: IAppDomainSetup) -> str

        Set: ShadowCopyDirectories(self: IAppDomainSetup) = value
        """
        ...

    @property
    def ShadowCopyFiles(self):
        """
        Gets or sets a string that indicates whether shadow copying is turned on or off.

        Get: ShadowCopyFiles(self: IAppDomainSetup) -> str

        Set: ShadowCopyFiles(self: IAppDomainSetup) = value
        """
        ...



class IAsyncResult:
    """ Represents the status of an asynchronous operation. """
    @property
    def AsyncState(self):
        """
        Gets a user-defined object that qualifies or contains information about an asynchronous operation.

        Get: AsyncState(self: IAsyncResult) -> object
        """
        ...

    @property
    def AsyncWaitHandle(self):
        """
        Gets a System.Threading.WaitHandle that is used to wait for an asynchronous operation to complete.

        Get: AsyncWaitHandle(self: IAsyncResult) -> WaitHandle
        """
        ...

    @property
    def CompletedSynchronously(self):
        """
        Gets a value that indicates whether the asynchronous operation completed synchronously.

        Get: CompletedSynchronously(self: IAsyncResult) -> bool
        """
        ...

    @property
    def IsCompleted(self):
        """
        Gets a value that indicates whether the asynchronous operation has completed.

        Get: IsCompleted(self: IAsyncResult) -> bool
        """
        ...



class IComparable:
    """ Defines a generalized type-specific comparison method that a value type or class implements to order or sort its instances. """
    def CompareTo(self, obj):
        """
        CompareTo(self: IComparable, obj: object) -> int

            Compares the current instance with another object of the same type and returns an integer that indicates whether the current instance precedes,

             follows, or occurs in the same position in the sort order as the other object.

            obj: An object to compare with this instance.

            Returns: A value that indicates the relative order of the objects being compared. The return value has these meanings: Value Meaning Less than zero This

             instance precedes obj in the sort order. Zero This instance occurs in the same position in the sort order as obj. Greater than zero This instance

             follows obj in the sort order.
        """
        ...

# Error generating skeleton for function __eq__: 'type' object has no attribute '__bases__'

# Error generating skeleton for function __ge__: 'type' object has no attribute '__bases__'

# Error generating skeleton for function __gt__: 'type' object has no attribute '__bases__'

# Error generating skeleton for function __le__: 'type' object has no attribute '__bases__'

# Error generating skeleton for function __lt__: 'type' object has no attribute '__bases__'

# Error generating skeleton for function __ne__: 'type' object has no attribute '__bases__'


class ICustomFormatter:
    """ Defines a method that supports custom formatting of the value of an object. """
    def Format(self, format, arg, formatProvider):
        """
        Format(self: ICustomFormatter, format: str, arg: object, formatProvider: IFormatProvider) -> str

            Converts the value of a specified object to an equivalent string representation using specified format and culture-specific formatting information.

            format: A format string containing formatting specifications.

            arg: An object to format.

            formatProvider: An object that supplies format information about the current instance.

            Returns: The string representation of the value of arg, formatted as specified by format and formatProvider.
        """
        ...


class IEquatable:
    # no doc
    def Equals(self, other):
        """
        Equals(self: IEquatable[T], other: T) -> bool

            Indicates whether the current object is equal to another object of the same type.

            other: An object to compare with this object.

            Returns: ue if the current object is equal to the other parameter; otherwise, lse.
        """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...


class IFormatProvider:
    """ Provides a mechanism for retrieving an object to control formatting. """
    def GetFormat(self, formatType):
        """
        GetFormat(self: IFormatProvider, formatType: Type) -> object

            Returns an object that provides formatting services for the specified type.

            formatType: An object that specifies the type of format object to return.

            Returns: An instance of the object specified by formatType, if the System.IFormatProvider implementation can supply that type of object; otherwise, ll.
        """
        ...


class IndexOutOfRangeException(SystemException): # skipped bases: <type 'ISerializable'>, <type '_Exception'>
    """
    The exception that is thrown when an attempt is made to access an element of an array or collection with an index that is outside its bounds.

    IndexOutOfRangeException()

    IndexOutOfRangeException(message: str)

    IndexOutOfRangeException(message: str, innerException: Exception)
    """
    SerializeObjectState = None


class InsufficientExecutionStackException(SystemException): # skipped bases: <type 'ISerializable'>, <type '_Exception'>
    """
    The exception that is thrown when there is insufficient execution stack available to allow most methods to execute.

    InsufficientExecutionStackException()

    InsufficientExecutionStackException(message: str)

    InsufficientExecutionStackException(message: str, innerException: Exception)
    """
    SerializeObjectState = None


class OutOfMemoryException(SystemException): # skipped bases: <type 'ISerializable'>, <type '_Exception'>
    """
    The exception that is thrown when there is not enough memory to continue the execution of a program.

    OutOfMemoryException()

    OutOfMemoryException(message: str)

    OutOfMemoryException(message: str, innerException: Exception)
    """
    SerializeObjectState = None


class InsufficientMemoryException(OutOfMemoryException): # skipped bases: <type 'ISerializable'>, <type '_Exception'>
    """
    The exception that is thrown when a check for sufficient available memory fails. This class cannot be inherited.

    InsufficientMemoryException()

    InsufficientMemoryException(message: str)

    InsufficientMemoryException(message: str, innerException: Exception)
    """
    SerializeObjectState = None


class Int16( IComparable, IFormattable, IConvertible, IEquatable):
    """ Represents a 16-bit signed integer. """
    def bit_length(self, *args): #cannot find CLR method
        """ bit_length(value: Int16) -> int """
        ...

    def conjugate(self, *args): #cannot find CLR method
        """ conjugate(x: Int16) -> Int16 """
        ...

    def GetHashCode(self):
        """
        GetHashCode(self: Int16) -> int

            Returns the hash code for this instance.

            Returns: A 32-bit signed integer hash code.
        """
        ...

    @staticmethod
    def Parse(s, *__args):
        """
        Parse(s: str) -> Int16

            Converts the string representation of a number to its 16-bit signed integer equivalent.

            s: A string containing a number to convert.

            Returns: A 16-bit signed integer equivalent to the number contained in s.

        Parse(s: str, style: NumberStyles) -> Int16

            Converts the string representation of a number in a specified style to its 16-bit signed integer equivalent.

            s: A string containing a number to convert.

            style: A bitwise combination of the enumeration values that indicates the style elements that can be present in s. A typical value to specify is

             System.Globalization.NumberStyles.Integer.

            Returns: A 16-bit signed integer equivalent to the number specified in s.

        Parse(s: str, provider: IFormatProvider) -> Int16

            Converts the string representation of a number in a specified culture-specific format to its 16-bit signed integer equivalent.

            s: A string containing a number to convert.

            provider: An System.IFormatProvider that supplies culture-specific formatting information about s.

            Returns: A 16-bit signed integer equivalent to the number specified in s.

        Parse(s: str, style: NumberStyles, provider: IFormatProvider) -> Int16

            Converts the string representation of a number in a specified style and culture-specific format to its 16-bit signed integer equivalent.

            s: A string containing a number to convert.

            style: A bitwise combination of enumeration values that indicates the style elements that can be present in s. A typical value to specify is

             System.Globalization.NumberStyles.Integer.

            provider: An System.IFormatProvider that supplies culture-specific formatting information about s.

            Returns: A 16-bit signed integer equivalent to the number specified in s.
        """
        ...

    @staticmethod
    def TryParse(s, *__args):
        """
        TryParse(s: str) -> (bool, Int16)

            Converts the string representation of a number to its 16-bit signed integer equivalent. A return value indicates whether the conversion succeeded or

             failed.

            s: A string containing a number to convert.

            Returns: ue if s was converted successfully; otherwise, lse.

        TryParse(s: str, style: NumberStyles, provider: IFormatProvider) -> (bool, Int16)

            Converts the string representation of a number in a specified style and culture-specific format to its 16-bit signed integer equivalent. A return

             value indicates whether the conversion succeeded or failed.

            s: A string containing a number to convert. The string is interpreted using the style specified by style.

            style: A bitwise combination of enumeration values that indicates the style elements that can be present in s. A typical value to specify is

             System.Globalization.NumberStyles.Integer.

            provider: An object that supplies culture-specific formatting information about s.

            Returns: ue if s was converted successfully; otherwise, lse.
        """
        ...

    def __abs__(self, *args): #cannot find CLR method
        """ x.__abs__() <==> abs(x) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __and__(self, *args): #cannot find CLR method
        """ __and__(x: Int16, y: Int16) -> Int16 """
        ...

    def __cmp__(self, *args): #cannot find CLR method
        """ x.__cmp__(y) <==> cmp(x,y) """
        ...

    def __div__(self, *args): #cannot find CLR method
        """ x.__div__(y) <==> x/y """
        ...

    def __float__(self, *args): #cannot find CLR method
        """ __float__(x: Int16) -> float """
        ...

    def __floordiv__(self, *args): #cannot find CLR method
        """ x.__floordiv__(y) <==> x//y """
        ...

    def __hex__(self, *args): #cannot find CLR method
        """ __hex__(value: Int16) -> str """
        ...

    def __index__(self, *args): #cannot find CLR method
        """ __index__(x: Int16) -> int """
        ...

    def __int__(self, *args): #cannot find CLR method
        """ __int__(x: Int16) -> int """
        ...

    def __invert__(self, *args): #cannot find CLR method
        """ __invert__(x: Int16) -> Int16 """
        ...

    def __lshift__(self, *args): #cannot find CLR method
        """ x.__rshift__(y) <==> x<<yx.__rshift__(y) <==> x<<y """
        ...

    def __mod__(self, *args): #cannot find CLR method
        """ x.__mod__(y) <==> x%y """
        ...

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*y """
        ...

    def __neg__(self, *args): #cannot find CLR method
        """ x.__neg__() <==> -x """
        ...

    def __nonzero__(self, *args): #cannot find CLR method
        """ __nonzero__(x: Int16) -> bool """
        ...

    def __or__(self, *args): #cannot find CLR method
        """ __or__(x: Int16, y: Int16) -> Int16 """
        ...

    def __pos__(self, *args): #cannot find CLR method
        """ __pos__(x: Int16) -> Int16 """
        ...

    def __pow__(self, *args): #cannot find CLR method
        """ x.__pow__(y[, z]) <==> pow(x, y[, z]) """
        ...

    def __radd__(self, *args): #cannot find CLR method
        """ __radd__(x: Int16, y: Int16) -> object """
        ...

    def __rand__(self, *args): #cannot find CLR method
        """ __rand__(x: Int16, y: Int16) -> Int16 """
        ...

    def __rdiv__(self, *args): #cannot find CLR method
        """ __rdiv__(x: Int16, y: Int16) -> object """
        ...

    def __rfloordiv__(self, *args): #cannot find CLR method
        """ __rfloordiv__(x: Int16, y: Int16) -> object """
        ...

    def __rmod__(self, *args): #cannot find CLR method
        """ __rmod__(x: Int16, y: Int16) -> Int16 """
        ...

    def __rmul__(self, *args): #cannot find CLR method
        """ __rmul__(x: Int16, y: Int16) -> object """
        ...

    def __ror__(self, *args): #cannot find CLR method
        """ __ror__(x: Int16, y: Int16) -> Int16 """
        ...

    def __rpow__(self, *args): #cannot find CLR method
        """ __rpow__(x: Int16, y: Int16) -> object """
        ...

    def __rshift__(self, *args): #cannot find CLR method
        """ x.__rshift__(y) <==> x>>yx.__rshift__(y) <==> x>>y """
        ...

    def __rsub__(self, *args): #cannot find CLR method
        """ __rsub__(x: Int16, y: Int16) -> object """
        ...

    def __rtruediv__(self, *args): #cannot find CLR method
        """ __rtruediv__(x: Int16, y: Int16) -> float """
        ...

    def __rxor__(self, *args): #cannot find CLR method
        """ __rxor__(x: Int16, y: Int16) -> Int16 """
        ...

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        ...

    def __truediv__(self, *args): #cannot find CLR method
        """ x.__truediv__(y) <==> x/y """
        ...

    def __trunc__(self, *args): #cannot find CLR method
        """ __trunc__(x: Int16) -> Int16 """
        ...

    def __xor__(self, *args): #cannot find CLR method
        """ __xor__(x: Int16, y: Int16) -> Int16 """
        ...

    denominator = None
    imag = None
    MaxValue = None
    MinValue = None
    numerator = None
    real = None


class Int64( IComparable, IFormattable, IConvertible, IEquatable):
    """ Represents a 64-bit signed integer. """
    def bit_length(self, *args): #cannot find CLR method
        """ bit_length(value: Int64) -> int """
        ...

    def conjugate(self, *args): #cannot find CLR method
        """ conjugate(x: Int64) -> Int64 """
        ...

    def GetHashCode(self):
        """
        GetHashCode(self: Int64) -> int

            Returns the hash code for this instance.

            Returns: A 32-bit signed integer hash code.
        """
        ...

    @staticmethod
    def Parse(s, *__args):
        """
        Parse(s: str) -> Int64

            Converts the string representation of a number to its 64-bit signed integer equivalent.

            s: A string containing a number to convert.

            Returns: A 64-bit signed integer equivalent to the number contained in s.

        Parse(s: str, style: NumberStyles) -> Int64

            Converts the string representation of a number in a specified style to its 64-bit signed integer equivalent.

            s: A string containing a number to convert.

            style: A bitwise combination of System.Globalization.NumberStyles values that indicates the permitted format of s. A typical value to specify is

             System.Globalization.NumberStyles.Integer.

            Returns: A 64-bit signed integer equivalent to the number specified in s.

        Parse(s: str, provider: IFormatProvider) -> Int64

            Converts the string representation of a number in a specified culture-specific format to its 64-bit signed integer equivalent.

            s: A string containing a number to convert.

            provider: An object that supplies culture-specific formatting information about s.

            Returns: A 64-bit signed integer equivalent to the number specified in s.

        Parse(s: str, style: NumberStyles, provider: IFormatProvider) -> Int64

            Converts the string representation of a number in a specified style and culture-specific format to its 64-bit signed integer equivalent.

            s: A string containing a number to convert.

            style: A bitwise combination of enumeration values that indicates the style elements that can be present in s. A typical value to specify is

             System.Globalization.NumberStyles.Integer.

            provider: An System.IFormatProvider that supplies culture-specific formatting information about s.

            Returns: A 64-bit signed integer equivalent to the number specified in s.
        """
        ...

    @staticmethod
    def TryParse(s, *__args):
        """
        TryParse(s: str) -> (bool, Int64)

            Converts the string representation of a number to its 64-bit signed integer equivalent. A return value indicates whether the conversion succeeded or

             failed.

            s: A string containing a number to convert.

            Returns: ue if s was converted successfully; otherwise, lse.

        TryParse(s: str, style: NumberStyles, provider: IFormatProvider) -> (bool, Int64)

            Converts the string representation of a number in a specified style and culture-specific format to its 64-bit signed integer equivalent. A return

             value indicates whether the conversion succeeded or failed.

            s: A string containing a number to convert. The string is interpreted using the style specified by style.

            style: A bitwise combination of enumeration values that indicates the style elements that can be present in s. A typical value to specify is

             System.Globalization.NumberStyles.Integer.

            provider: An object that supplies culture-specific formatting information about s.

            Returns: ue if s was converted successfully; otherwise, lse.
        """
        ...

    def __abs__(self, *args): #cannot find CLR method
        """ x.__abs__() <==> abs(x) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __and__(self, *args): #cannot find CLR method
        """ __and__(x: Int64, y: Int64) -> Int64 """
        ...

    def __cmp__(self, *args): #cannot find CLR method
        """ x.__cmp__(y) <==> cmp(x,y) """
        ...

    def __div__(self, *args): #cannot find CLR method
        """ x.__div__(y) <==> x/y """
        ...

    def __float__(self, *args): #cannot find CLR method
        """ __float__(x: Int64) -> float """
        ...

    def __floordiv__(self, *args): #cannot find CLR method
        """ x.__floordiv__(y) <==> x//y """
        ...

    def __hex__(self, *args): #cannot find CLR method
        """ __hex__(value: Int64) -> str """
        ...

    def __index__(self, *args): #cannot find CLR method
        """ __index__(x: Int64) -> long """
        ...

    def __int__(self, *args): #cannot find CLR method
        """ __int__(x: Int64) -> int """
        ...

    def __invert__(self, *args): #cannot find CLR method
        """ __invert__(x: Int64) -> Int64 """
        ...

    def __lshift__(self, *args): #cannot find CLR method
        """ x.__rshift__(y) <==> x<<y """
        ...

    def __mod__(self, *args): #cannot find CLR method
        """ x.__mod__(y) <==> x%y """
        ...

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*y """
        ...

    def __neg__(self, *args): #cannot find CLR method
        """ x.__neg__() <==> -x """
        ...

    def __nonzero__(self, *args): #cannot find CLR method
        """ __nonzero__(x: Int64) -> bool """
        ...

    def __or__(self, *args): #cannot find CLR method
        """ __or__(x: Int64, y: Int64) -> Int64 """
        ...

    def __pos__(self, *args): #cannot find CLR method
        """ __pos__(x: Int64) -> Int64 """
        ...

    def __pow__(self, *args): #cannot find CLR method
        """ x.__pow__(y[, z]) <==> pow(x, y[, z]) """
        ...

    def __radd__(self, *args): #cannot find CLR method
        """ __radd__(x: Int64, y: Int64) -> object """
        ...

    def __rand__(self, *args): #cannot find CLR method
        """ __rand__(x: Int64, y: Int64) -> Int64 """
        ...

    def __rdiv__(self, *args): #cannot find CLR method
        """ __rdiv__(x: Int64, y: Int64) -> object """
        ...

    def __rfloordiv__(self, *args): #cannot find CLR method
        """ __rfloordiv__(x: Int64, y: Int64) -> object """
        ...

    def __rmod__(self, *args): #cannot find CLR method
        """ __rmod__(x: Int64, y: Int64) -> Int64 """
        ...

    def __rmul__(self, *args): #cannot find CLR method
        """ __rmul__(x: Int64, y: Int64) -> object """
        ...

    def __ror__(self, *args): #cannot find CLR method
        """ __ror__(x: Int64, y: Int64) -> Int64 """
        ...

    def __rpow__(self, *args): #cannot find CLR method
        """ __rpow__(x: Int64, y: Int64) -> object """
        ...

    def __rshift__(self, *args): #cannot find CLR method
        """ x.__rshift__(y) <==> x>>y """
        ...

    def __rsub__(self, *args): #cannot find CLR method
        """ __rsub__(x: Int64, y: Int64) -> object """
        ...

    def __rtruediv__(self, *args): #cannot find CLR method
        """ __rtruediv__(x: Int64, y: Int64) -> float """
        ...

    def __rxor__(self, *args): #cannot find CLR method
        """ __rxor__(x: Int64, y: Int64) -> Int64 """
        ...

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        ...

    def __truediv__(self, *args): #cannot find CLR method
        """ x.__truediv__(y) <==> x/y """
        ...

    def __trunc__(self, *args): #cannot find CLR method
        """ __trunc__(x: Int64) -> Int64 """
        ...

    def __xor__(self, *args): #cannot find CLR method
        """ __xor__(x: Int64, y: Int64) -> Int64 """
        ...

    denominator = None
    imag = None
    MaxValue = None
    MinValue = None
    numerator = None
    real = None


class IntPtr( ISerializable):
    """
    A platform-specific type that is used to represent a pointer or a handle.

    IntPtr(value: int)

    IntPtr(value: Int64)

    IntPtr(value: Void*)
    """
    @property
    def Size(self):
        """
        Gets the size of this instance.

        Get: Size() -> int
        """
        ...


    @staticmethod
    def Add(pointer, offset):
        """
        Add(pointer: IntPtr, offset: int) -> IntPtr

            Adds an offset to the value of a pointer.

            pointer: The pointer to add the offset to.

            offset: The offset to add.

            Returns: A new pointer that reflects the addition of offset to pointer.
        """
        ...

    def Equals(self, obj):
        """
        Equals(self: IntPtr, obj: object) -> bool

            Returns a value indicating whether this instance is equal to a specified object.

            obj: An object to compare with this instance or ll.

            Returns: ue if obj is an instance of System.IntPtr and equals the value of this instance; otherwise, lse.
        """
        ...

    def GetHashCode(self):
        """
        GetHashCode(self: IntPtr) -> int

            Returns the hash code for this instance.

            Returns: A 32-bit signed integer hash code.
        """
        ...

    @staticmethod
    def Subtract(pointer, offset):
        """
        Subtract(pointer: IntPtr, offset: int) -> IntPtr

            Subtracts an offset from the value of a pointer.

            pointer: The pointer to subtract the offset from.

            offset: The offset to subtract.

            Returns: A new pointer that reflects the subtraction of offset from pointer.
        """
        ...

    def ToInt32(self):
        """
        ToInt32(self: IntPtr) -> int

            Converts the value of this instance to a 32-bit signed integer.

            Returns: A 32-bit signed integer equal to the value of this instance.
        """
        ...

    def ToInt64(self):
        """
        ToInt64(self: IntPtr) -> Int64

            Converts the value of this instance to a 64-bit signed integer.

            Returns: A 64-bit signed integer equal to the value of this instance.
        """
        ...

    def ToPointer(self):
        """
        ToPointer(self: IntPtr) -> Void*

            Converts the value of this instance to a pointer to an unspecified type.

            Returns: A pointer to System.Void; that is, a pointer to memory containing data of an unspecified type.
        """
        ...

    def ToString(self, format=...):
        """
        ToString(self: IntPtr) -> str

            Converts the numeric value of the current System.IntPtr object to its equivalent string representation.

            Returns: The string representation of the value of this instance.

        ToString(self: IntPtr, format: str) -> str

            Converts the numeric value of the current System.IntPtr object to its equivalent string representation.

            format: A format specification that governs how the current System.IntPtr object is converted.

            Returns: The string representation of the value of the current System.IntPtr object.
        """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __int__(self, *args): #cannot find CLR method
        """ __int__(value: IntPtr) -> int """
        ...

    def __long__(self, *args): #cannot find CLR method
        """ __int__(value: IntPtr) -> int """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        ...

    Zero = None


class InvalidCastException(SystemException): # skipped bases: <type 'ISerializable'>, <type '_Exception'>
    """
    The exception that is thrown for invalid casting or explicit conversion.

    InvalidCastException()

    InvalidCastException(message: str)

    InvalidCastException(message: str, innerException: Exception)

    InvalidCastException(message: str, errorCode: int)
    """
    SerializeObjectState = None


class InvalidOperationException(SystemException): # skipped bases: <type 'ISerializable'>, <type '_Exception'>
    """
    The exception that is thrown when a method call is invalid for the object's current state.

    InvalidOperationException()

    InvalidOperationException(message: str)

    InvalidOperationException(message: str, innerException: Exception)
    """
    SerializeObjectState = None


class InvalidProgramException(SystemException): # skipped bases: <type 'ISerializable'>, <type '_Exception'>
    """
    The exception that is thrown when a program contains invalid Microsoft intermediate language (MSIL) or metadata. Generally this indicates a bug in the compiler that generated the program.

    InvalidProgramException()

    InvalidProgramException(message: str)

    InvalidProgramException(message: str, inner: Exception)
    """
    SerializeObjectState = None


class InvalidTimeZoneException(Exception): # skipped bases: <type 'ISerializable'>, <type '_Exception'>
    """
    The exception that is thrown when time zone information is invalid.

    InvalidTimeZoneException(message: str)

    InvalidTimeZoneException(message: str, innerException: Exception)

    InvalidTimeZoneException()
    """
    SerializeObjectState = None


class IObservable:
    # no doc
    def Subscribe(self, observer):
        """
        Subscribe(self: IObservable[T], observer: IObserver[T]) -> IDisposable

            Notifies the provider that an observer is to receive notifications.

            observer: The object that is to receive notifications.

            Returns: A reference to an interface that allows observers to stop receiving notifications before the provider has finished sending them.
        """
        ...


class IObserver:
    # no doc
    def OnCompleted(self):
        """
        OnCompleted(self: IObserver[T])

            Notifies the observer that the provider has finished sending push-based notifications.
        """
        ...

    def OnError(self, error):
        """
        OnError(self: IObserver[T], error: Exception)

            Notifies the observer that the provider has experienced an error condition.

            error: An object that provides additional information about the error.
        """
        ...

    def OnNext(self, value):
        """
        OnNext(self: IObserver[T], value: T)

            Provides the observer with new data.

            value: The current notification information.
        """
        ...


class IProgress:
    # no doc
    def Report(self, value):
        """
        Report(self: IProgress[T], value: T)

            Reports a progress update.

            value: The value of the updated progress.
        """
        ...


class IServiceProvider:
    """ Defines a mechanism for retrieving a service object; that is, an object that provides custom support to other objects. """
    class GetService(Generic[X]):
        # no doc
        @classmethod
        def __new__(cls, *args) -> Optional[X]:
            ...

    # def GetService[X](self) -> Optional[X]:
    #     ...
class Lazy: # skipped bases: <type 'object'>
    """
    Lazy[T]()

    Lazy[T](valueFactory: Func[T])

    Lazy[T](isThreadSafe: bool)

    Lazy[T](mode: LazyThreadSafetyMode)

    Lazy[T](valueFactory: Func[T], isThreadSafe: bool)

    Lazy[T](valueFactory: Func[T], mode: LazyThreadSafetyMode)
    """
    @property
    def IsValueCreated(self):
        """
        Gets a value that indicates whether a value has been created for this System.Lazy instance.

        Get: IsValueCreated(self: Lazy[T]) -> bool
        """
        ...

    @property
    def Value(self):
        """
        Gets the lazily initialized value of the current System.Lazy instance.

        Get: Value(self: Lazy[T]) -> T
        """
        ...


    def ToString(self):
        """
        ToString(self: Lazy[T]) -> str

            Creates and returns a string representation of the System.Lazy property for this instance.

            Returns: The result of calling the System.Object.ToString method on the System.Lazy property for this instance, if the value has been created (that is, if the

             System.Lazy property returns ue). Otherwise, a string indicating that the value has not been created.
        """
        ...


class LdapStyleUriParser(UriParser):
    """
    A customizable parser based on the Lightweight Directory Access Protocol (LDAP) scheme.

    LdapStyleUriParser()
    """
    pass

class LoaderOptimization(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>
    """
    An enumeration used with the System.LoaderOptimizationAttribute class to specify loader optimizations for an executable.

    enum LoaderOptimization, values: DisallowBindings (4), DomainMask (3), MultiDomain (2), MultiDomainHost (3), NotSpecified (0), SingleDomain (1)
    """
    DisallowBindings = None
    DomainMask = None
    MultiDomain = None
    MultiDomainHost = None
    NotSpecified = None
    SingleDomain = None
    value__ = None


class LoaderOptimizationAttribute(Attribute): # skipped bases: <type '_Attribute'>
    """
    Used to set the default loader optimization policy for the main method of an executable application.

    LoaderOptimizationAttribute(value: Byte)

    LoaderOptimizationAttribute(value: LoaderOptimization)
    """
    @property
    def Value(self):
        """
        Gets the current System.LoaderOptimization value for this instance.

        Get: Value(self: LoaderOptimizationAttribute) -> LoaderOptimization
        """
        ...


    @staticmethod # known case of __new__
    def __new__(cls, value):
        """
        __new__(cls: type, value: Byte)

        __new__(cls: type, value: LoaderOptimization)
        """
        ...


class LocalDataStoreSlot: # skipped bases: <type 'object'>
    """ Encapsulates a memory slot to store local data. This class cannot be inherited. """
    pass

class Math: # skipped bases: <type 'object'>
    """ Provides constants and static methods for trigonometric, logarithmic, and other common mathematical functions.To browse the .NET Framework source code for this type, see the Reference Source. """
    @staticmethod
    def Abs(value):
        """
        Abs(value: SByte) -> SByte

            Returns the absolute value of an 8-bit signed integer.

            value: A number that is greater than System.SByte.MinValue, but less than or equal to System.SByte.MaxValue.

                Abs(value: Int16) -> Int16

            Returns the absolute value of a 16-bit signed integer.

            value: A number that is greater than System.Int16.MinValue, but less than or equal to System.Int16.MaxValue.

                Abs(value: int) -> int

            Returns the absolute value of a 32-bit signed integer.

            value: A number that is greater than System.Int32.MinValue, but less than or equal to System.Int32.MaxValue.

                Abs(value: Int64) -> Int64

            Returns the absolute value of a 64-bit signed integer.

            value: A number that is greater than System.Int64.MinValue, but less than or equal to System.Int64.MaxValue.

                Abs(value: Decimal) -> Decimal

            Returns the absolute value of a System.Decimal number.

            value: A number that is greater than or equal to System.Decimal.MinValue, but less than or equal to System.Decimal.MaxValue.

                Abs(value: Single) -> Single

            Returns the absolute value of a single-precision floating-point number.

            value: A number that is greater than or equal to System.Single.MinValue, but less than or equal to System.Single.MaxValue.

                Abs(value: float) -> float

            Returns the absolute value of a double-precision floating-point number.

            value: A number that is greater than or equal to System.Double.MinValue, but less than or equal to System.Double.MaxValue.

                """
        ...

    @staticmethod
    def Acos(d):
        """
        Acos(d: float) -> float

            Returns the angle whose cosine is the specified number.

            d: A number representing a cosine, where d must be greater than or equal to -1, but less than or equal to 1.

                          System.Double.NaN if d < -1 or d > 1 or d equals System.Double.NaN.
        """
        ...

    @staticmethod
    def Asin(d):
        """
        Asin(d: float) -> float

            Returns the angle whose sine is the specified number.

            d: A number representing a sine, where d must be greater than or equal to -1, but less than or equal to 1.

                          System.Double.NaN if d < -1 or d > 1 or d equals System.Double.NaN.
        """
        ...

    @staticmethod
    def Atan(d):
        """
        Atan(d: float) -> float

            Returns the angle whose tangent is the specified number.

            d: A number representing a tangent.

                                     System.Double.PositiveInfinity.
        """
        ...

    @staticmethod
    def Atan2(y, x):
        """
        Atan2(y: float, x: float) -> float

            Returns the angle whose tangent is the quotient of two specified numbers.

            y: The y coordinate of a point.

            x: The x coordinate of a point.

                                                     System.Double.NaN, or if x and y are either System.Double.PositiveInfinity or System.Double.NegativeInfinity, the method returns System.Double.NaN.
        """
        ...

    @staticmethod
    def BigMul(a, b):
        """
        BigMul(a: int, b: int) -> Int64

            Produces the full product of two 32-bit numbers.

            a: The first number to multiply.

            b: The second number to multiply.

            Returns: The number containing the product of the specified numbers.
        """
        ...

    @staticmethod
    def Ceiling(*__args):
        """
        Ceiling(d: Decimal) -> Decimal

            Returns the smallest integral value that is greater than or equal to the specified decimal number.

            d: A decimal number.

            Returns: The smallest integral value that is greater than or equal to d. Note that this method returns a System.Decimal instead of an integral type.

        Ceiling(a: float) -> float

            Returns the smallest integral value that is greater than or equal to the specified double-precision floating-point number.

            a: A double-precision floating-point number.

            Returns: The smallest integral value that is greater than or equal to a. If a is equal to System.Double.NaN, System.Double.NegativeInfinity, or

             System.Double.PositiveInfinity, that value is returned. Note that this method returns a System.Double instead of an integral type.
        """
        ...

    @staticmethod
    def Cos(d):
        """
        Cos(d: float) -> float

            Returns the cosine of the specified angle.

            d: An angle, measured in radians.

            Returns: The cosine of d. If d is equal to System.Double.NaN, System.Double.NegativeInfinity, or System.Double.PositiveInfinity, this method returns

             System.Double.NaN.
        """
        ...

    @staticmethod
    def Cosh(value):
        """
        Cosh(value: float) -> float

            Returns the hyperbolic cosine of the specified angle.

            value: An angle, measured in radians.

            Returns: The hyperbolic cosine of value. If value is equal to System.Double.NegativeInfinity or System.Double.PositiveInfinity, System.Double.PositiveInfinity

             is returned. If value is equal to System.Double.NaN, System.Double.NaN is returned.
        """
        ...

    @staticmethod
    def DivRem(a, b, result):
        """
        DivRem(a: int, b: int) -> (int, int)

            Calculates the quotient of two 32-bit signed integers and also returns the remainder in an output parameter.

            a: The dividend.

            b: The divisor.

            Returns: The quotient of the specified numbers.

        DivRem(a: Int64, b: Int64) -> (Int64, Int64)

            Calculates the quotient of two 64-bit signed integers and also returns the remainder in an output parameter.

            a: The dividend.

            b: The divisor.

            Returns: The quotient of the specified numbers.
        """
        ...

    @staticmethod
    def Exp(d):
        ...

    @staticmethod
    def Floor(d):
        """
        Floor(d: Decimal) -> Decimal

            Returns the largest integer less than or equal to the specified decimal number.

            d: A decimal number.

            Returns: The largest integer less than or equal to d.  Note that the method returns an integral value of type System.Math.

        Floor(d: float) -> float

            Returns the largest integer less than or equal to the specified double-precision floating-point number.

            d: A double-precision floating-point number.

            Returns: The largest integer less than or equal to d. If d is equal to System.Double.NaN, System.Double.NegativeInfinity, or System.Double.PositiveInfinity,

             that value is returned.
        """
        ...

    @staticmethod
    def IEEERemainder(x, y):
        """
        IEEERemainder(x: float, y: float) -> float

            Returns the remainder resulting from the division of a specified number by another specified number.

            x: A dividend.

            y: A divisor.

            Returns: A number equal to x - (y Q), where Q is the quotient of x / y rounded to the nearest integer (if x / y falls halfway between two integers, the even

             integer is returned).If x - (y Q) is zero, the value +0 is returned if x is positive, or -0 if x is negative.If y = 0, System.Double.NaN is returned.
        """
        ...

    @staticmethod
    def Log(*__args):
        ...

    @staticmethod
    def Log10(d):
        """
        Log10(d: float) -> float

            Returns the base 10 logarithm of a specified number.

            d: A number whose logarithm is to be found.

            Returns: One of the values in the following table.

                          d parameter Return value Positive The base 10 log of d; that is, log 10d. Zero

                        System.Double.NegativeInfinity

                        Negative

                          System.Double.NaN

                        Equal to

             System.Double.NaNSystem.Double.NaN

                        Equal to System.Double.PositiveInfinitySystem.Double.PositiveInfinity
        """
        ...

    @staticmethod
    def Max(val1, val2):
        """
        Max(val1: SByte, val2: SByte) -> SByte

            Returns the larger of two 8-bit signed integers.

            val1: The first of two 8-bit signed integers to compare.

            val2: The second of two 8-bit signed integers to compare.

            Returns: Parameter val1 or val2, whichever is larger.

        Max(val1: Byte, val2: Byte) -> Byte

            Returns the larger of two 8-bit unsigned integers.

            val1: The first of two 8-bit unsigned integers to compare.

            val2: The second of two 8-bit unsigned integers to compare.

            Returns: Parameter val1 or val2, whichever is larger.

        Max(val1: Int16, val2: Int16) -> Int16

            Returns the larger of two 16-bit signed integers.

            val1: The first of two 16-bit signed integers to compare.

            val2: The second of two 16-bit signed integers to compare.

            Returns: Parameter val1 or val2, whichever is larger.

        Max(val1: UInt16, val2: UInt16) -> UInt16

            Returns the larger of two 16-bit unsigned integers.

            val1: The first of two 16-bit unsigned integers to compare.

            val2: The second of two 16-bit unsigned integers to compare.

            Returns: Parameter val1 or val2, whichever is larger.

        Max(val1: int, val2: int) -> int

            Returns the larger of two 32-bit signed integers.

            val1: The first of two 32-bit signed integers to compare.

            val2: The second of two 32-bit signed integers to compare.

            Returns: Parameter val1 or val2, whichever is larger.

        Max(val1: UInt32, val2: UInt32) -> UInt32

            Returns the larger of two 32-bit unsigned integers.

            val1: The first of two 32-bit unsigned integers to compare.

            val2: The second of two 32-bit unsigned integers to compare.

            Returns: Parameter val1 or val2, whichever is larger.

        Max(val1: Int64, val2: Int64) -> Int64

            Returns the larger of two 64-bit signed integers.

            val1: The first of two 64-bit signed integers to compare.

            val2: The second of two 64-bit signed integers to compare.

            Returns: Parameter val1 or val2, whichever is larger.

        Max(val1: UInt64, val2: UInt64) -> UInt64

            Returns the larger of two 64-bit unsigned integers.

            val1: The first of two 64-bit unsigned integers to compare.

            val2: The second of two 64-bit unsigned integers to compare.

            Returns: Parameter val1 or val2, whichever is larger.

        Max(val1: Single, val2: Single) -> Single

            Returns the larger of two single-precision floating-point numbers.

            val1: The first of two single-precision floating-point numbers to compare.

            val2: The second of two single-precision floating-point numbers to compare.

            Returns: Parameter val1 or val2, whichever is larger. If val1, or val2, or both val1 and val2 are equal to System.Single.NaN, System.Single.NaN is returned.

        Max(val1: float, val2: float) -> float

            Returns the larger of two double-precision floating-point numbers.

            val1: The first of two double-precision floating-point numbers to compare.

            val2: The second of two double-precision floating-point numbers to compare.

            Returns: Parameter val1 or val2, whichever is larger. If val1, val2, or both val1 and val2 are equal to System.Double.NaN, System.Double.NaN is returned.

        Max(val1: Decimal, val2: Decimal) -> Decimal

            Returns the larger of two decimal numbers.

            val1: The first of two decimal numbers to compare.

            val2: The second of two decimal numbers to compare.

            Returns: Parameter val1 or val2, whichever is larger.
        """
        ...

    @staticmethod
    def Min(val1, val2):
        """
        Min(val1: SByte, val2: SByte) -> SByte

            Returns the smaller of two 8-bit signed integers.

            val1: The first of two 8-bit signed integers to compare.

            val2: The second of two 8-bit signed integers to compare.

            Returns: Parameter val1 or val2, whichever is smaller.

        Min(val1: Byte, val2: Byte) -> Byte

            Returns the smaller of two 8-bit unsigned integers.

            val1: The first of two 8-bit unsigned integers to compare.

            val2: The second of two 8-bit unsigned integers to compare.

            Returns: Parameter val1 or val2, whichever is smaller.

        Min(val1: Int16, val2: Int16) -> Int16

            Returns the smaller of two 16-bit signed integers.

            val1: The first of two 16-bit signed integers to compare.

            val2: The second of two 16-bit signed integers to compare.

            Returns: Parameter val1 or val2, whichever is smaller.

        Min(val1: UInt16, val2: UInt16) -> UInt16

            Returns the smaller of two 16-bit unsigned integers.

            val1: The first of two 16-bit unsigned integers to compare.

            val2: The second of two 16-bit unsigned integers to compare.

            Returns: Parameter val1 or val2, whichever is smaller.

        Min(val1: int, val2: int) -> int

            Returns the smaller of two 32-bit signed integers.

            val1: The first of two 32-bit signed integers to compare.

            val2: The second of two 32-bit signed integers to compare.

            Returns: Parameter val1 or val2, whichever is smaller.

        Min(val1: UInt32, val2: UInt32) -> UInt32

            Returns the smaller of two 32-bit unsigned integers.

            val1: The first of two 32-bit unsigned integers to compare.

            val2: The second of two 32-bit unsigned integers to compare.

            Returns: Parameter val1 or val2, whichever is smaller.

        Min(val1: Int64, val2: Int64) -> Int64

            Returns the smaller of two 64-bit signed integers.

            val1: The first of two 64-bit signed integers to compare.

            val2: The second of two 64-bit signed integers to compare.

            Returns: Parameter val1 or val2, whichever is smaller.

        Min(val1: UInt64, val2: UInt64) -> UInt64

            Returns the smaller of two 64-bit unsigned integers.

            val1: The first of two 64-bit unsigned integers to compare.

            val2: The second of two 64-bit unsigned integers to compare.

            Returns: Parameter val1 or val2, whichever is smaller.

        Min(val1: Single, val2: Single) -> Single

            Returns the smaller of two single-precision floating-point numbers.

            val1: The first of two single-precision floating-point numbers to compare.

            val2: The second of two single-precision floating-point numbers to compare.

            Returns: Parameter val1 or val2, whichever is smaller. If val1, val2, or both val1 and val2 are equal to System.Single.NaN, System.Single.NaN is returned.

        Min(val1: float, val2: float) -> float

            Returns the smaller of two double-precision floating-point numbers.

            val1: The first of two double-precision floating-point numbers to compare.

            val2: The second of two double-precision floating-point numbers to compare.

            Returns: Parameter val1 or val2, whichever is smaller. If val1, val2, or both val1 and val2 are equal to System.Double.NaN, System.Double.NaN is returned.

        Min(val1: Decimal, val2: Decimal) -> Decimal

            Returns the smaller of two decimal numbers.

            val1: The first of two decimal numbers to compare.

            val2: The second of two decimal numbers to compare.

            Returns: Parameter val1 or val2, whichever is smaller.
        """
        ...

    @staticmethod
    def Pow(x, y):
        """
        Pow(x: float, y: float) -> float

            Returns a specified number raised to the specified power.

            x: A double-precision floating-point number to be raised to a power.

            y: A double-precision floating-point number that specifies a power.

            Returns: The number x raised to the power y.
        """
        ...

    @staticmethod
    def Round(*__args):
        """
        Round(value: float, digits: int) -> float

            Rounds a double-precision floating-point value to a specified number of fractional digits.

            value: A double-precision floating-point number to be rounded.

            digits: The number of fractional digits in the return value.

            Returns: The number nearest to value that contains a number of fractional digits equal to digits.

        Round(value: float, mode: MidpointRounding) -> float

            Rounds a double-precision floating-point value to the nearest integer. A parameter specifies how to round the value if it is midway between two

             numbers.

            value: A double-precision floating-point number to be rounded.

            mode: Specification for how to round value if it is midway between two other numbers.

            Returns: The integer nearest value. If value is halfway between two integers, one of which is even and the other odd, then mode determines which of the two is

             returned.

        Round(value: float, digits: int, mode: MidpointRounding) -> float

            Rounds a double-precision floating-point value to a specified number of fractional digits. A parameter specifies how to round the value if it is

             midway between two numbers.

            value: A double-precision floating-point number to be rounded.

            digits: The number of fractional digits in the return value.

            mode: Specification for how to round value if it is midway between two other numbers.

            Returns: The number nearest to value that has a number of fractional digits equal to digits. If value has fewer fractional digits than digits, value is

             returned unchanged.

        Round(d: Decimal) -> Decimal

            Rounds a decimal value to the nearest integral value.

            d: A decimal number to be rounded.

            Returns: The integer nearest parameter d. If the fractional component of d is halfway between two integers, one of which is even and the other odd, the even

             number is returned. Note that this method returns a System.Decimal instead of an integral type.

        Round(d: Decimal, decimals: int) -> Decimal

            Rounds a decimal value to a specified number of fractional digits.

            d: A decimal number to be rounded.

            decimals: The number of decimal places in the return value.

            Returns: The number nearest to d that contains a number of fractional digits equal to decimals.

        Round(d: Decimal, mode: MidpointRounding) -> Decimal

            Rounds a decimal value to the nearest integer. A parameter specifies how to round the value if it is midway between two numbers.

            d: A decimal number to be rounded.

            mode: Specification for how to round d if it is midway between two other numbers.

            Returns: The integer nearest d. If d is halfway between two numbers, one of which is even and the other odd, then mode determines which of the two is returned.

        Round(d: Decimal, decimals: int, mode: MidpointRounding) -> Decimal

            Rounds a decimal value to a specified number of fractional digits. A parameter specifies how to round the value if it is midway between two numbers.

            d: A decimal number to be rounded.

            decimals: The number of decimal places in the return value.

            mode: Specification for how to round d if it is midway between two other numbers.

            Returns: The number nearest to d that contains a number of fractional digits equal to decimals. If d has fewer fractional digits than decimals, d is returned

             unchanged.

        Round(a: float) -> float

            Rounds a double-precision floating-point value to the nearest integral value.

            a: A double-precision floating-point number to be rounded.

            Returns: The integer nearest a. If the fractional component of a is halfway between two integers, one of which is even and the other odd, then the even number

             is returned. Note that this method returns a System.Double instead of an integral type.
        """
        ...

    @staticmethod
    def Sign(value):
        """
        Sign(value: SByte) -> int

            Returns an integer that indicates the sign of an 8-bit signed integer.

            value: A signed number.

            Returns: A number that indicates the sign of value, as shown in the following table.Return value Meaning -1

                          value is less than zero. 0

                             value is equal to zero. 1

                          value is greater than zero.

        Sign(value: Int16) -> int

            Returns an integer that indicates the sign of a 16-bit signed integer.

            value: A signed number.

            Returns: A number that indicates the sign of value, as shown in the following table.Return value Meaning -1

                          value is less than zero. 0

                             value is equal to zero. 1

                          value is greater than zero.

        Sign(value: int) -> int

            Returns an integer that indicates the sign of a 32-bit signed integer.

            value: A signed number.

            Returns: A number that indicates the sign of value, as shown in the following table.Return value Meaning -1

                          value is less than zero. 0

                             value is equal to zero. 1

                          value is greater than zero.

        Sign(value: Int64) -> int

            Returns an integer that indicates the sign of a 64-bit signed integer.

            value: A signed number.

            Returns: A number that indicates the sign of value, as shown in the following table.Return value Meaning -1

                          value is less than zero. 0

                             value is equal to zero. 1

                          value is greater than zero.

        Sign(value: Single) -> int

            Returns an integer that indicates the sign of a single-precision floating-point number.

            value: A signed number.

            Returns: A number that indicates the sign of value, as shown in the following table.Return value Meaning -1

                          value is less than zero. 0

                             value is equal to zero. 1

                          value is greater than zero.

        Sign(value: float) -> int

            Returns an integer that indicates the sign of a double-precision floating-point number.

            value: A signed number.

            Returns: A number that indicates the sign of value, as shown in the following table.Return value Meaning -1

                          value is less than zero. 0

                             value is equal to zero. 1

                          value is greater than zero.

        Sign(value: Decimal) -> int

            Returns an integer that indicates the sign of a decimal number.

            value: A signed decimal number.

            Returns: A number that indicates the sign of value, as shown in the following table.Return value Meaning -1

                          value is less than zero. 0

                             value is equal to zero. 1

                          value is greater than zero.
        """
        ...

    @staticmethod
    def Sin(a):
        """
        Sin(a: float) -> float

            Returns the sine of the specified angle.

            a: An angle, measured in radians.

            Returns: The sine of a. If a is equal to System.Double.NaN, System.Double.NegativeInfinity, or System.Double.PositiveInfinity, this method returns

             System.Double.NaN.
        """
        ...

    @staticmethod
    def Sinh(value):
        """
        Sinh(value: float) -> float

            Returns the hyperbolic sine of the specified angle.

            value: An angle, measured in radians.

            Returns: The hyperbolic sine of value. If value is equal to System.Double.NegativeInfinity, System.Double.PositiveInfinity, or System.Double.NaN, this method

             returns a System.Double equal to value.
        """
        ...

    @staticmethod
    def Sqrt(d):
        """
        Sqrt(d: float) -> float

            Returns the square root of a specified number.

            d: The number whose square root is to be found.

            Returns: One of the values in the following table.

                          d parameter Return value Zero or positive The positive square root of d. Negative

                           System.Double.NaN

                        Equals System.Double.NaNSystem.Double.NaN

                        Equals

             System.Double.PositiveInfinitySystem.Double.PositiveInfinity
        """
        ...

    @staticmethod
    def Tan(a):
        """
        Tan(a: float) -> float

            Returns the tangent of the specified angle.

            a: An angle, measured in radians.

            Returns: The tangent of a. If a is equal to System.Double.NaN, System.Double.NegativeInfinity, or System.Double.PositiveInfinity, this method returns

             System.Double.NaN.
        """
        ...

    @staticmethod
    def Tanh(value):
        """
        Tanh(value: float) -> float

            Returns the hyperbolic tangent of the specified angle.

            value: An angle, measured in radians.

            Returns: The hyperbolic tangent of value. If value is equal to System.Double.NegativeInfinity, this method returns -1. If value is equal to

             System.Double.PositiveInfinity, this method returns 1. If value is equal to System.Double.NaN, this method returns System.Double.NaN.
        """
        ...

    @staticmethod
    def Truncate(d):
        """
        Truncate(d: Decimal) -> Decimal

            Calculates the integral part of a specified decimal number.

            d: A number to truncate.

            Returns: The integral part of d; that is, the number that remains after any fractional digits have been discarded.

        Truncate(d: float) -> float

            Calculates the integral part of a specified double-precision floating-point number.

            d: A number to truncate.

            Returns: The integral part of d; that is, the number that remains after any fractional digits have been discarded, or one of the values listed in the

             following table.

                          d

                        Return value

             System.Double.NaNSystem.Double.NaNSystem.Double.NegativeInfinitySystem.Double.NegativeInfinitySystem.Double.PositiveInfinitySystem.Double.PositiveInfi

             nity
        """
        ...

    E = 2.7182818284590451
    PI = 3.1415926535897931
    __all__ = [
        'Abs',
        'Acos',
        'Asin',
        'Atan',
        'Atan2',
        'BigMul',
        'Ceiling',
        'Cos',
        'Cosh',
        'DivRem',
        'E',
        'Exp',
        'Floor',
        'IEEERemainder',
        'Log',
        'Log10',
        'Max',
        'Min',
        'PI',
        'Pow',
        'Round',
        'Sign',
        'Sin',
        'Sinh',
        'Sqrt',
        'Tan',
        'Tanh',
        'Truncate',
    ]


class MethodAccessException(MemberAccessException): # skipped bases: <type 'ISerializable'>, <type '_Exception'>
    """
    The exception that is thrown when there is an invalid attempt to access a method, such as accessing a private method from partially trusted code.

    MethodAccessException()

    MethodAccessException(message: str)

    MethodAccessException(message: str, inner: Exception)
    """
    SerializeObjectState = None


class MidpointRounding(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>
    """
    Specifies how mathematical rounding methods should process a number that is midway between two numbers.

    enum MidpointRounding, values: AwayFromZero (1), ToEven (0)
    """
    AwayFromZero = None
    ToEven = None
    value__ = None


class MissingMemberException(MemberAccessException): # skipped bases: <type 'ISerializable'>, <type '_Exception'>
    """
    The exception that is thrown when there is an attempt to dynamically access a class member that does not exist or that is not declared as public. If a member in a class library has been removed or renamed, recompile any assemblies that reference that library.

    MissingMemberException()

    MissingMemberException(message: str)

    MissingMemberException(message: str, inner: Exception)

    MissingMemberException(className: str, memberName: str)
    """
    @property
    def Message(self):
        """
        Gets the text string showing the class name, the member name, and the signature of the missing member.

        Get: Message(self: MissingMemberException) -> str
        """
        ...


    def GetObjectData(self, info, context):
        """
        GetObjectData(self: MissingMemberException, info: SerializationInfo, context: StreamingContext)

            Sets the System.Runtime.Serialization.SerializationInfo object with the class name, the member name, the signature of the missing member, and

             additional exception information.

            info: The object that holds the serialized object data.

            context: The contextual information about the source or destination.
        """
        ...

    ClassName = None
    MemberName = None
    SerializeObjectState = None
    Signature = None


class MissingFieldException(MissingMemberException): # skipped bases: <type 'ISerializable'>, <type '_Exception'>
    """
    The exception that is thrown when there is an attempt to dynamically access a field that does not exist. If a field in a class library has been removed or renamed, recompile any assemblies that reference that library.

    MissingFieldException()

    MissingFieldException(message: str)

    MissingFieldException(message: str, inner: Exception)

    MissingFieldException(className: str, fieldName: str)
    """
    ClassName = None
    MemberName = None
    SerializeObjectState = None
    Signature = None


class MissingMethodException(MissingMemberException): # skipped bases: <type 'ISerializable'>, <type '_Exception'>
    """
    The exception that is thrown when there is an attempt to dynamically access a method that does not exist.

    MissingMethodException()

    MissingMethodException(message: str)

    MissingMethodException(message: str, inner: Exception)

    MissingMethodException(className: str, methodName: str)
    """
    ClassName = None
    MemberName = None
    SerializeObjectState = None
    Signature = None


class ModuleHandle: # skipped bases: <type 'object'>
    """ Represents a runtime handle for a module. """
    @property
    def MDStreamVersion(self):
        """
        Gets the metadata stream version.

        Get: MDStreamVersion(self: ModuleHandle) -> int
        """
        ...


    def Equals(self, *__args):
        """
        Equals(self: ModuleHandle, obj: object) -> bool

            Returns a System.Boolean value indicating whether the specified object is a System.ModuleHandle structure, and equal to the current

             System.ModuleHandle.

            obj: The object to be compared with the current System.ModuleHandle structure.

            Returns: ue if obj is a System.ModuleHandle structure, and is equal to the current System.ModuleHandle structure; otherwise, lse.

        Equals(self: ModuleHandle, handle: ModuleHandle) -> bool

            Returns a System.Boolean value indicating whether the specified System.ModuleHandle structure is equal to the current System.ModuleHandle.

            handle: The System.ModuleHandle structure to be compared with the current System.ModuleHandle.

            Returns: ue if handle is equal to the current System.ModuleHandle structure; otherwise lse.
        """
        ...

    def GetHashCode(self):
        """
        GetHashCode(self: ModuleHandle) -> int

            Returns the hash code for this instance.

            Returns: A 32-bit signed integer that is the hash code for this instance.
        """
        ...

    def GetRuntimeFieldHandleFromMetadataToken(self, fieldToken):
        """
        GetRuntimeFieldHandleFromMetadataToken(self: ModuleHandle, fieldToken: int) -> RuntimeFieldHandle

            Returns a runtime handle for the field identified by the specified metadata token.

            fieldToken: A metadata token that identifies a field in the module.

            Returns: A System.RuntimeFieldHandle for the field identified by fieldToken.
        """
        ...

    def GetRuntimeMethodHandleFromMetadataToken(self, methodToken):
        """
        GetRuntimeMethodHandleFromMetadataToken(self: ModuleHandle, methodToken: int) -> RuntimeMethodHandle

            Returns a runtime method handle for the method or constructor identified by the specified metadata token.

            methodToken: A metadata token that identifies a method or constructor in the module.

            Returns: A System.RuntimeMethodHandle for the method or constructor identified by methodToken.
        """
        ...

    def GetRuntimeTypeHandleFromMetadataToken(self, typeToken):
        """
        GetRuntimeTypeHandleFromMetadataToken(self: ModuleHandle, typeToken: int) -> RuntimeTypeHandle

            Returns a runtime type handle for the type identified by the specified metadata token.

            typeToken: A metadata token that identifies a type in the module.

            Returns: A System.RuntimeTypeHandle for the type identified by typeToken.
        """
        ...

    def ResolveFieldHandle(self, fieldToken, typeInstantiationContext=..., methodInstantiationContext=...):
        """
        ResolveFieldHandle(self: ModuleHandle, fieldToken: int) -> RuntimeFieldHandle

            Returns a runtime handle for the field identified by the specified metadata token.

            fieldToken: A metadata token that identifies a field in the module.

            Returns: A System.RuntimeFieldHandle for the field identified by fieldToken.

        ResolveFieldHandle(self: ModuleHandle, fieldToken: int, typeInstantiationContext: Array[RuntimeTypeHandle], methodInstantiationContext: Array[RuntimeTypeHandle]) -> RuntimeFieldHandle

            Returns a runtime field handle for the field identified by the specified metadata token, specifying the generic type arguments of the type and method

             where the token is in scope.

            fieldToken: A metadata token that identifies a field in the module.

            typeInstantiationContext: An array of System.RuntimeTypeHandle structures representing the generic type arguments of the type where the token is in scope, or ll if that type

             is not generic.

            methodInstantiationContext: An array of System.RuntimeTypeHandle structures representing the generic type arguments of the method where the token is in scope, or ll if that

             method is not generic.

            Returns: A System.RuntimeFieldHandle for the field identified by fieldToken.
        """
        ...

    def ResolveMethodHandle(self, methodToken, typeInstantiationContext=..., methodInstantiationContext=...):
        """
        ResolveMethodHandle(self: ModuleHandle, methodToken: int) -> RuntimeMethodHandle

            Returns a runtime method handle for the method or constructor identified by the specified metadata token.

            methodToken: A metadata token that identifies a method or constructor in the module.

            Returns: A System.RuntimeMethodHandle for the method or constructor identified by methodToken.

        ResolveMethodHandle(self: ModuleHandle, methodToken: int, typeInstantiationContext: Array[RuntimeTypeHandle], methodInstantiationContext: Array[RuntimeTypeHandle]) -> RuntimeMethodHandle

            Returns a runtime method handle for the method or constructor identified by the specified metadata token, specifying the generic type arguments of

             the type and method where the token is in scope.

            methodToken: A metadata token that identifies a method or constructor in the module.

            typeInstantiationContext: An array of System.RuntimeTypeHandle structures representing the generic type arguments of the type where the token is in scope, or ll if that type

             is not generic.

            methodInstantiationContext: An array of System.RuntimeTypeHandle structures representing the generic type arguments of the method where the token is in scope, or ll if that

             method is not generic.

            Returns: A System.RuntimeMethodHandle for the method or constructor identified by methodToken.
        """
        ...

    def ResolveTypeHandle(self, typeToken, typeInstantiationContext=..., methodInstantiationContext=...):
        """
        ResolveTypeHandle(self: ModuleHandle, typeToken: int) -> RuntimeTypeHandle

            Returns a runtime type handle for the type identified by the specified metadata token.

            typeToken: A metadata token that identifies a type in the module.

            Returns: A System.RuntimeTypeHandle for the type identified by typeToken.

        ResolveTypeHandle(self: ModuleHandle, typeToken: int, typeInstantiationContext: Array[RuntimeTypeHandle], methodInstantiationContext: Array[RuntimeTypeHandle]) -> RuntimeTypeHandle

            Returns a runtime type handle for the type identified by the specified metadata token, specifying the generic type arguments of the type and method

             where the token is in scope.

            typeToken: A metadata token that identifies a type in the module.

            typeInstantiationContext: An array of System.RuntimeTypeHandle structures representing the generic type arguments of the type where the token is in scope, or ll if that type

             is not generic.

            methodInstantiationContext: An array of System.RuntimeTypeHandle structures objects representing the generic type arguments of the method where the token is in scope, or ll if

             that method is not generic.

            Returns: A System.RuntimeTypeHandle for the type identified by typeToken.
        """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    EmptyHandle = None


class MTAThreadAttribute(Attribute): # skipped bases: <type '_Attribute'>
    """
    Indicates that the COM threading model for an application is multithreaded apartment (MTA).

    MTAThreadAttribute()
    """
    pass

class MulticastNotSupportedException(SystemException): # skipped bases: <type 'ISerializable'>, <type '_Exception'>
    """
    The exception that is thrown when there is an attempt to combine two delegates based on the System.Delegate type instead of the System.MulticastDelegate type. This class cannot be inherited.

    MulticastNotSupportedException()

    MulticastNotSupportedException(message: str)

    MulticastNotSupportedException(message: str, inner: Exception)
    """
    SerializeObjectState = None


class NetPipeStyleUriParser(UriParser):
    """
    A parser based on the NetPipe scheme for the "Indigo" system.

    NetPipeStyleUriParser()
    """
    pass

class NetTcpStyleUriParser(UriParser):
    """
    A parser based on the NetTcp scheme for the "Indigo" system.

    NetTcpStyleUriParser()
    """
    pass

class NewsStyleUriParser(UriParser):
    """
    A customizable parser based on the news scheme using the Network News Transfer Protocol (NNTP).

    NewsStyleUriParser()
    """
    pass

class NonSerializedAttribute(Attribute): # skipped bases: <type '_Attribute'>
    """
    Indicates that a field of a serializable class should not be serialized. This class cannot be inherited.

    NonSerializedAttribute()
    """
    pass

class NotFiniteNumberException(ArithmeticException): # skipped bases: <type 'ISerializable'>, <type '_Exception'>
    """
    The exception that is thrown when a floating-point value is positive infinity, negative infinity, or Not-a-Number (NaN).

    NotFiniteNumberException()

    NotFiniteNumberException(offendingNumber: float)

    NotFiniteNumberException(message: str)

    NotFiniteNumberException(message: str, offendingNumber: float)

    NotFiniteNumberException(message: str, innerException: Exception)

    NotFiniteNumberException(message: str, offendingNumber: float, innerException: Exception)
    """
    @property
    def OffendingNumber(self):
        """
        Gets the invalid number that is a positive infinity, a negative infinity, or Not-a-Number (NaN).

        Get: OffendingNumber(self: NotFiniteNumberException) -> float
        """
        ...


    def GetObjectData(self, info, context):
        """
        GetObjectData(self: NotFiniteNumberException, info: SerializationInfo, context: StreamingContext)

            Sets the System.Runtime.Serialization.SerializationInfo object with the invalid number and additional exception information.

            info: The object that holds the serialized object data.

            context: The contextual information about the source or destination.
        """
        ...

    SerializeObjectState = None


class NotImplementedException(SystemException): # skipped bases: <type 'ISerializable'>, <type '_Exception'>
    """
    The exception that is thrown when a requested method or operation is not implemented.

    NotImplementedException()

    NotImplementedException(message: str)

    NotImplementedException(message: str, inner: Exception)
    """
    SerializeObjectState = None


class NotSupportedException(SystemException): # skipped bases: <type 'ISerializable'>, <type '_Exception'>
    """
    The exception that is thrown when an invoked method is not supported, or when there is an attempt to read, seek, or write to a stream that does not support the invoked functionality.

    NotSupportedException()

    NotSupportedException(message: str)

    NotSupportedException(message: str, innerException: Exception)
    """
    SerializeObjectState = None


class Nullable:
    """ Supports a value type that can be assigned ll. This class cannot be inherited. """
    @staticmethod
    def Compare(n1, n2):
        """ Compare[T](n1: Nullable[T], n2: Nullable[T]) -> int """
        ...

    @staticmethod
    def Equals(*__args):
        """ Equals[T](n1: Nullable[T], n2: Nullable[T]) -> bool """
        ...

    @staticmethod
    def GetUnderlyingType(nullableType):
        """
        GetUnderlyingType(nullableType: Type) -> Type

            Returns the underlying type argument of the specified nullable type.

            nullableType: A System.Type object that describes a closed generic nullable type.

            Returns: The type argument of the nullableType parameter, if the nullableType parameter is a closed generic nullable type; otherwise, ll.
        """
        ...

    __all__ = [
        'Compare',
        'Equals',
        'GetUnderlyingType',
    ]


class NullReferenceException(SystemException): # skipped bases: <type 'ISerializable'>, <type '_Exception'>
    """
    The exception that is thrown when there is an attempt to dereference a null object reference.

    NullReferenceException()

    NullReferenceException(message: str)

    NullReferenceException(message: str, innerException: Exception)
    """
    SerializeObjectState = None


class ObjectDisposedException(InvalidOperationException): # skipped bases: <type 'ISerializable'>, <type '_Exception'>
    """
    The exception that is thrown when an operation is performed on a disposed object.

    ObjectDisposedException(objectName: str)

    ObjectDisposedException(objectName: str, message: str)

    ObjectDisposedException(message: str, innerException: Exception)
    """
    @property
    def Message(self):
        """
        Gets the message that describes the error.

        Get: Message(self: ObjectDisposedException) -> str
        """
        ...

    @property
    def ObjectName(self):
        """
        Gets the name of the disposed object.

        Get: ObjectName(self: ObjectDisposedException) -> str
        """
        ...


    def GetObjectData(self, info, context):
        """
        GetObjectData(self: ObjectDisposedException, info: SerializationInfo, context: StreamingContext)

            Retrieves the System.Runtime.Serialization.SerializationInfo object with the parameter name and additional exception information.

            info: The System.Runtime.Serialization.SerializationInfo that holds the serialized object data about the exception being thrown.

            context: The System.Runtime.Serialization.StreamingContext that contains contextual information about the source or destination.
        """
        ...

    SerializeObjectState = None


class ObsoleteAttribute(Attribute): # skipped bases: <type '_Attribute'>
    """
    Marks the program elements that are no longer in use. This class cannot be inherited.

    ObsoleteAttribute()

    ObsoleteAttribute(message: str)

    ObsoleteAttribute(message: str, error: bool)
    """
    @property
    def IsError(self):
        """
        Gets a Boolean value indicating whether the compiler will treat usage of the obsolete program element as an error.

        Get: IsError(self: ObsoleteAttribute) -> bool
        """
        ...

    @property
    def Message(self):
        """
        Gets the workaround message, including a description of the alternative program elements.

        Get: Message(self: ObsoleteAttribute) -> str
        """
        ...


    @staticmethod # known case of __new__
    def __new__(cls, message=..., error=...):
        """
        __new__(cls: type)

        __new__(cls: type, message: str)

        __new__(cls: type, message: str, error: bool)
        """
        ...


class OperatingSystem( ICloneable, ISerializable):
    """
    Represents information about an operating system, such as the version and platform identifier. This class cannot be inherited.

    OperatingSystem(platform: PlatformID, version: Version)
    """
    @property
    def Platform(self):
        """
        Gets a System.PlatformID enumeration value that identifies the operating system platform.

        Get: Platform(self: OperatingSystem) -> PlatformID
        """
        ...

    @property
    def ServicePack(self):
        """
        Gets the service pack version represented by this System.OperatingSystem object.

        Get: ServicePack(self: OperatingSystem) -> str
        """
        ...

    @property
    def Version(self):
        """
        Gets a System.Version object that identifies the operating system.

        Get: Version(self: OperatingSystem) -> Version
        """
        ...

    @property
    def VersionString(self):
        """
        Gets the concatenated string representation of the platform identifier, version, and service pack that are currently installed on the operating system.

        Get: VersionString(self: OperatingSystem) -> str
        """
        ...


    def ToString(self):
        """
        ToString(self: OperatingSystem) -> str

            Converts the value of this System.OperatingSystem object to its equivalent string representation.

            Returns: The string representation of the values returned by the System.OperatingSystem.Platform, System.OperatingSystem.Version, and

             System.OperatingSystem.ServicePack properties.
        """
        ...


class OperationCanceledException(SystemException): # skipped bases: <type 'ISerializable'>, <type '_Exception'>
    """
    The exception that is thrown in a thread upon cancellation of an operation that the thread was executing.

    OperationCanceledException()

    OperationCanceledException(message: str)

    OperationCanceledException(message: str, innerException: Exception)

    OperationCanceledException(token: CancellationToken)

    OperationCanceledException(message: str, token: CancellationToken)

    OperationCanceledException(message: str, innerException: Exception, token: CancellationToken)
    """
    @property
    def CancellationToken(self):
        """
        Gets a token associated with the operation that was canceled.

        Get: CancellationToken(self: OperationCanceledException) -> CancellationToken
        """
        ...


    SerializeObjectState = None


class OverflowException(ArithmeticException): # skipped bases: <type 'ISerializable'>, <type '_Exception'>
    """
    The exception that is thrown when an arithmetic, casting, or conversion operation in a checked context results in an overflow.

    OverflowException()

    OverflowException(message: str)

    OverflowException(message: str, innerException: Exception)
    """
    SerializeObjectState = None


class ParamArrayAttribute(Attribute): # skipped bases: <type '_Attribute'>
    """
    Indicates that a method will allow a variable number of arguments in its invocation. This class cannot be inherited.

    ParamArrayAttribute()
    """
    pass

class PlatformID(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>
    """
    Identifies the operating system, or platform, supported by an assembly.

    enum PlatformID, values: MacOSX (6), Unix (4), Win32NT (2), Win32S (0), Win32Windows (1), WinCE (3), Xbox (5)
    """
    MacOSX = None
    Unix = None
    value__ = None
    Win32NT = None
    Win32S = None
    Win32Windows = None
    WinCE = None
    Xbox = None


class PlatformNotSupportedException(NotSupportedException): # skipped bases: <type 'ISerializable'>, <type '_Exception'>
    """
    The exception that is thrown when a feature does not run on a particular platform.

    PlatformNotSupportedException()

    PlatformNotSupportedException(message: str)

    PlatformNotSupportedException(message: str, inner: Exception)
    """
    SerializeObjectState = None


class Predicate(MulticastDelegate): # skipped bases: <type 'ICloneable'>, <type 'ISerializable'>
    """ Predicate[T](object: object, method: IntPtr) """
    def BeginInvoke(self, obj, callback, object):
        """ BeginInvoke(self: Predicate[T], obj: T, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result):
        """ EndInvoke(self: Predicate[T], result: IAsyncResult) -> bool """
        ...

    def Invoke(self, obj):
        """ Invoke(self: Predicate[T], obj: T) -> bool """
        ...


class Progress( IProgress):
    """
    Progress[T]()

    Progress[T](handler: Action[T])
    """
    def OnReport(self, *args): #cannot find CLR method
        """
        OnReport(self: Progress[T], value: T)

            Reports a progress change.

            value: The value of the updated progress.
        """
        ...

    ProgressChanged = None


class Random: # skipped bases: <type 'object'>
    """
    Represents a pseudo-random number generator, which is a device that produces a sequence of numbers that meet certain statistical requirements for randomness.To browse the .NET Framework source code for this type, see the Reference Source.

    Random()

    Random(Seed: int)
    """
    def Next(self, *__args):
        """
        Next(self: Random) -> int

            Returns a non-negative random integer.

            Returns: A 32-bit signed integer that is greater than or equal to 0 and less than System.Int32.MaxValue.

        Next(self: Random, minValue: int, maxValue: int) -> int

            Returns a random integer that is within a specified range.

            minValue: The inclusive lower bound of the random number returned.

            maxValue: The exclusive upper bound of the random number returned. maxValue must be greater than or equal to minValue.

            Returns: A 32-bit signed integer greater than or equal to minValue and less than maxValue; that is, the range of return values includes minValue but not

             maxValue. If minValue equals maxValue, minValue is returned.

        Next(self: Random, maxValue: int) -> int

            Returns a non-negative random integer that is less than the specified maximum.

            maxValue: The exclusive upper bound of the random number to be generated. maxValue must be greater than or equal to 0.

            Returns: A 32-bit signed integer that is greater than or equal to 0, and less than maxValue; that is, the range of return values ordinarily includes 0 but not

             maxValue. However, if maxValue equals 0, maxValue is returned.
        """
        ...

    def NextBytes(self, buffer):
        """
        NextBytes(self: Random, buffer: Array[Byte])

            Fills the elements of a specified array of bytes with random numbers.

            buffer: An array of bytes to contain random numbers.
        """
        ...

    def NextDouble(self):
        """
        NextDouble(self: Random) -> float

            Returns a random floating-point number that is greater than or equal to 0.0, and less than 1.0.

            Returns: A double-precision floating point number that is greater than or equal to 0.0, and less than 1.0.
        """
        ...

    def Sample(self, *args): #cannot find CLR method
        """
        Sample(self: Random) -> float

            Returns a random floating-point number between 0.0 and 1.0.

            Returns: A double-precision floating point number that is greater than or equal to 0.0, and less than 1.0.
        """
        ...


class RankException(SystemException): # skipped bases: <type 'ISerializable'>, <type '_Exception'>
    """
    The exception that is thrown when an array with the wrong number of dimensions is passed to a method.

    RankException()

    RankException(message: str)

    RankException(message: str, innerException: Exception)
    """
    SerializeObjectState = None


class ResolveEventArgs(EventArgs):
    """
    Provides data for loader resolution events, such as the System.AppDomain.TypeResolve, System.AppDomain.ResourceResolve, System.AppDomain.ReflectionOnlyAssemblyResolve, and System.AppDomain.AssemblyResolve events.

    ResolveEventArgs(name: str)

    ResolveEventArgs(name: str, requestingAssembly: Assembly)
    """
    @property
    def Name(self):
        """
        Gets the name of the item to resolve.

        Get: Name(self: ResolveEventArgs) -> str
        """
        ...

    @property
    def RequestingAssembly(self):
        """
        Gets the assembly whose dependency is being resolved.

        Get: RequestingAssembly(self: ResolveEventArgs) -> Assembly
        """
        ...


    @staticmethod # known case of __new__
    def __new__(cls, name, requestingAssembly=...):
        """
        __new__(cls: type, name: str)

        __new__(cls: type, name: str, requestingAssembly: Assembly)
        """
        ...


class ResolveEventHandler(MulticastDelegate): # skipped bases: <type 'ICloneable'>, <type 'ISerializable'>
    """
    Represents a method that handles the System.AppDomain.TypeResolve, System.AppDomain.ResourceResolve, or System.AppDomain.AssemblyResolve event of an System.AppDomain.

    ResolveEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, args, callback, object):
        """ BeginInvoke(self: ResolveEventHandler, sender: object, args: ResolveEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result):
        """ EndInvoke(self: ResolveEventHandler, result: IAsyncResult) -> Assembly """
        ...

    def Invoke(self, sender, args):
        """ Invoke(self: ResolveEventHandler, sender: object, args: ResolveEventArgs) -> Assembly """
        ...


class RuntimeArgumentHandle: # skipped bases: <type 'object'>
    """ References a variable-length argument list. """
    pass

class RuntimeFieldHandle( ISerializable):
    """ Represents a field using an internal metadata token. """
    @property
    def Value(self):
        """
        Gets a handle to the field represented by the current instance.

        Get: Value(self: RuntimeFieldHandle) -> IntPtr
        """
        ...


    def Equals(self, *__args):
        """
        Equals(self: RuntimeFieldHandle, obj: object) -> bool

            Indicates whether the current instance is equal to the specified object.

            obj: The object to compare to the current instance.

            Returns: ue if obj is a System.RuntimeFieldHandle and equal to the value of the current instance; otherwise, lse.

        Equals(self: RuntimeFieldHandle, handle: RuntimeFieldHandle) -> bool

            Indicates whether the current instance is equal to the specified System.RuntimeFieldHandle.

            handle: The System.RuntimeFieldHandle to compare to the current instance.

            Returns: ue if the value of handle is equal to the value of the current instance; otherwise, lse.
        """
        ...

    def GetHashCode(self):
        """
        GetHashCode(self: RuntimeFieldHandle) -> int

            Returns the hash code for this instance.

            Returns: A 32-bit signed integer that is the hash code for this instance.
        """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class RuntimeMethodHandle( ISerializable):
    """ System.RuntimeMethodHandle is a handle to the internal metadata representation of a method. """
    @property
    def Value(self):
        """
        Gets the value of this instance.

        Get: Value(self: RuntimeMethodHandle) -> IntPtr
        """
        ...


    def Equals(self, *__args):
        """
        Equals(self: RuntimeMethodHandle, obj: object) -> bool

            Indicates whether this instance is equal to a specified object.

            obj: A System.Object to compare to this instance.

            Returns: ue if obj is a System.RuntimeMethodHandle and equal to the value of this instance; otherwise, lse.

        Equals(self: RuntimeMethodHandle, handle: RuntimeMethodHandle) -> bool

            Indicates whether this instance is equal to a specified System.RuntimeMethodHandle.

            handle: A System.RuntimeMethodHandle to compare to this instance.

            Returns: ue if handle is equal to the value of this instance; otherwise, lse.
        """
        ...

    def GetFunctionPointer(self):
        """
        GetFunctionPointer(self: RuntimeMethodHandle) -> IntPtr

            Obtains a pointer to the method represented by this instance.

            Returns: A pointer to the method represented by this instance.
        """
        ...

    def GetHashCode(self):
        """
        GetHashCode(self: RuntimeMethodHandle) -> int

            Returns the hash code for this instance.

            Returns: A 32-bit signed integer hash code.
        """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class RuntimeTypeHandle( ISerializable):
    """ Represents a type using an internal metadata token. """
    @property
    def Value(self):
        """
        Gets a handle to the type represented by this instance.

        Get: Value(self: RuntimeTypeHandle) -> IntPtr
        """
        ...


    def Equals(self, *__args):
        """
        Equals(self: RuntimeTypeHandle, handle: RuntimeTypeHandle) -> bool

            Indicates whether the specified System.RuntimeTypeHandle structure is equal to the current System.RuntimeTypeHandle structure.

            handle: The System.RuntimeTypeHandle structure to compare to the current instance.

            Returns: ue if the value of handle is equal to the value of this instance; otherwise, lse.

        Equals(self: RuntimeTypeHandle, obj: object) -> bool

            Indicates whether the specified object is equal to the current System.RuntimeTypeHandle structure.

            obj: An object to compare to the current instance.

            Returns: ue if obj is a System.RuntimeTypeHandle structure and is equal to the value of this instance; otherwise, lse.
        """
        ...

    def GetHashCode(self):
        """
        GetHashCode(self: RuntimeTypeHandle) -> int

            Returns the hash code for the current instance.

            Returns: A 32-bit signed integer hash code.
        """
        ...

    def GetModuleHandle(self):
        """
        GetModuleHandle(self: RuntimeTypeHandle) -> ModuleHandle

            Gets a handle to the module that contains the type represented by the current instance.

            Returns: A System.ModuleHandle structure representing a handle to the module that contains the type represented by the current instance.
        """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class SByte(IComparable, IFormattable, IConvertible, IEquatable):
    """ Represents an 8-bit signed integer. """
    def bit_length(self, *args): #cannot find CLR method
        """ bit_length(value: SByte) -> int """
        ...

    def conjugate(self, *args): #cannot find CLR method
        """ conjugate(x: SByte) -> SByte """
        ...

    def GetHashCode(self):
        """
        GetHashCode(self: SByte) -> int

            Returns the hash code for this instance.

            Returns: A 32-bit signed integer hash code.
        """
        ...

    @staticmethod
    def Parse(s, *__args):
        """
        Parse(s: str) -> SByte

            Converts the string representation of a number to its 8-bit signed integer equivalent.

            s: A string that represents a number to convert. The string is interpreted using the System.Globalization.NumberStyles.Integer style.

            Returns: An 8-bit signed integer that is equivalent to the number contained in the s parameter.

        Parse(s: str, style: NumberStyles) -> SByte

            Converts the string representation of a number in a specified style to its 8-bit signed integer equivalent.

            s: A string that contains a number to convert. The string is interpreted using the style specified by style.

            style: A bitwise combination of the enumeration values that indicates the style elements that can be present in s. A typical value to specify is

             System.Globalization.NumberStyles.Integer.

            Returns: An 8-bit signed integer that is equivalent to the number specified in s.

        Parse(s: str, provider: IFormatProvider) -> SByte

            Converts the string representation of a number in a specified culture-specific format to its 8-bit signed integer equivalent.

            s: A string that represents a number to convert. The string is interpreted using the System.Globalization.NumberStyles.Integer style.

            provider: An object that supplies culture-specific formatting information about s. If provider is ll, the thread current culture is used.

            Returns: An 8-bit signed integer that is equivalent to the number specified in s.

        Parse(s: str, style: NumberStyles, provider: IFormatProvider) -> SByte

            Converts the string representation of a number that is in a specified style and culture-specific format to its 8-bit signed equivalent.

            s: A string that contains the number to convert. The string is interpreted by using the style specified by style.

            style: A bitwise combination of the enumeration values that indicates the style elements that can be present in s. A typical value to specify is

             System.Globalization.NumberStyles.Integer.

            provider: An object that supplies culture-specific formatting information about s. If provider is ll, the thread current culture is used.

            Returns: An 8-bit signed byte value that is equivalent to the number specified in the s parameter.
        """
        ...

    @staticmethod
    def TryParse(s, *__args):
        """
        TryParse(s: str) -> (bool, SByte)

            Tries to convert the string representation of a number to its System.SByte equivalent, and returns a value that indicates whether the conversion

             succeeded.

            s: A string that contains a number to convert.

            Returns: ue if s was converted successfully; otherwise, lse.

        TryParse(s: str, style: NumberStyles, provider: IFormatProvider) -> (bool, SByte)

            Tries to convert the string representation of a number in a specified style and culture-specific format to its System.SByte equivalent, and returns a

             value that indicates whether the conversion succeeded.

            s: A string representing a number to convert.

            style: A bitwise combination of enumeration values that indicates the permitted format of s. A typical value to specify is

             System.Globalization.NumberStyles.Integer.

            provider: An object that supplies culture-specific formatting information about s.

            Returns: ue if s was converted successfully; otherwise, lse.
        """
        ...

    def __abs__(self, *args): #cannot find CLR method
        """ x.__abs__() <==> abs(x) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __and__(self, *args): #cannot find CLR method
        """ __and__(x: SByte, y: SByte) -> SByte """
        ...

    def __cmp__(self, *args): #cannot find CLR method
        """ x.__cmp__(y) <==> cmp(x,y) """
        ...

    def __div__(self, *args): #cannot find CLR method
        """ x.__div__(y) <==> x/y """
        ...

    def __float__(self, *args): #cannot find CLR method
        """ __float__(x: SByte) -> float """
        ...

    def __floordiv__(self, *args): #cannot find CLR method
        """ x.__floordiv__(y) <==> x//y """
        ...

    def __hex__(self, *args): #cannot find CLR method
        """ __hex__(value: SByte) -> str """
        ...

    def __index__(self, *args): #cannot find CLR method
        """ __index__(x: SByte) -> int """
        ...

    def __int__(self, *args): #cannot find CLR method
        """ __int__(x: SByte) -> int """
        ...

    def __invert__(self, *args): #cannot find CLR method
        """ __invert__(x: SByte) -> SByte """
        ...

    def __lshift__(self, *args): #cannot find CLR method
        """ x.__rshift__(y) <==> x<<yx.__rshift__(y) <==> x<<y """
        ...

    def __mod__(self, *args): #cannot find CLR method
        """ x.__mod__(y) <==> x%y """
        ...

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*y """
        ...

    def __neg__(self, *args): #cannot find CLR method
        """ x.__neg__() <==> -x """
        ...

    def __nonzero__(self, *args): #cannot find CLR method
        """ __nonzero__(x: SByte) -> bool """
        ...

    def __or__(self, *args): #cannot find CLR method
        """ __or__(x: SByte, y: SByte) -> SByte """
        ...

    def __pos__(self, *args): #cannot find CLR method
        """ __pos__(x: SByte) -> SByte """
        ...

    def __pow__(self, *args): #cannot find CLR method
        """ x.__pow__(y[, z]) <==> pow(x, y[, z]) """
        ...

    def __radd__(self, *args): #cannot find CLR method
        """ __radd__(x: SByte, y: SByte) -> object """
        ...

    def __rand__(self, *args): #cannot find CLR method
        """ __rand__(x: SByte, y: SByte) -> SByte """
        ...

    def __rdiv__(self, *args): #cannot find CLR method
        """ __rdiv__(x: SByte, y: SByte) -> object """
        ...

    def __rfloordiv__(self, *args): #cannot find CLR method
        """ __rfloordiv__(x: SByte, y: SByte) -> object """
        ...

    def __rmod__(self, *args): #cannot find CLR method
        """ __rmod__(x: SByte, y: SByte) -> SByte """
        ...

    def __rmul__(self, *args): #cannot find CLR method
        """ __rmul__(x: SByte, y: SByte) -> object """
        ...

    def __ror__(self, *args): #cannot find CLR method
        """ __ror__(x: SByte, y: SByte) -> SByte """
        ...

    def __rpow__(self, *args): #cannot find CLR method
        """ __rpow__(x: SByte, y: SByte) -> object """
        ...

    def __rshift__(self, *args): #cannot find CLR method
        """ x.__rshift__(y) <==> x>>yx.__rshift__(y) <==> x>>y """
        ...

    def __rsub__(self, *args): #cannot find CLR method
        """ __rsub__(x: SByte, y: SByte) -> object """
        ...

    def __rtruediv__(self, *args): #cannot find CLR method
        """ __rtruediv__(x: SByte, y: SByte) -> float """
        ...

    def __rxor__(self, *args): #cannot find CLR method
        """ __rxor__(x: SByte, y: SByte) -> SByte """
        ...

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        ...

    def __truediv__(self, *args): #cannot find CLR method
        """ x.__truediv__(y) <==> x/y """
        ...

    def __trunc__(self, *args): #cannot find CLR method
        """ __trunc__(x: SByte) -> SByte """
        ...

    def __xor__(self, *args): #cannot find CLR method
        """ __xor__(x: SByte, y: SByte) -> SByte """
        ...

    denominator = None
    imag = None
    MaxValue = None
    MinValue = None
    numerator = None
    real = None


class SerializableAttribute(Attribute): # skipped bases: <type '_Attribute'>
    """
    Indicates that a class can be serialized. This class cannot be inherited.

    SerializableAttribute()
    """
    pass

class Single( IComparable, IFormattable, IConvertible, IEquatable):
    """ Represents a single-precision floating-point number. """
    def conjugate(self, *args): #cannot find CLR method
        """ conjugate(x: Single) -> Single """
        ...

    def GetHashCode(self):
        """
        GetHashCode(self: Single) -> int

            Returns the hash code for this instance.

            Returns: A 32-bit signed integer hash code.
        """
        ...

    @staticmethod
    def IsInfinity(f):
        """
        IsInfinity(f: Single) -> bool

            Returns a value indicating whether the specified number evaluates to negative or positive infinity.

            f: A single-precision floating-point number.

            Returns: ue if f evaluates to System.Single.PositiveInfinity or System.Single.NegativeInfinity; otherwise, lse.
        """
        ...

    @staticmethod
    def IsNaN(f):
        """
        IsNaN(f: Single) -> bool

            Returns a value that indicates whether the specified value is not a number (System.Single.NaN).

            f: A single-precision floating-point number.

            Returns: ue if f evaluates to not a number (System.Single.NaN); otherwise, lse.
        """
        ...

    @staticmethod
    def IsNegativeInfinity(f):
        """
        IsNegativeInfinity(f: Single) -> bool

            Returns a value indicating whether the specified number evaluates to negative infinity.

            f: A single-precision floating-point number.

            Returns: ue if f evaluates to System.Single.NegativeInfinity; otherwise, lse.
        """
        ...

    @staticmethod
    def IsPositiveInfinity(f):
        """
        IsPositiveInfinity(f: Single) -> bool

            Returns a value indicating whether the specified number evaluates to positive infinity.

            f: A single-precision floating-point number.

            Returns: ue if f evaluates to System.Single.PositiveInfinity; otherwise, lse.
        """
        ...

    @staticmethod
    def Parse(s, *__args):
        """
        Parse(s: str) -> Single

            Converts the string representation of a number to its single-precision floating-point number equivalent.

            s: A string that contains a number to convert.

            Returns: A single-precision floating-point number equivalent to the numeric value or symbol specified in s.

        Parse(s: str, style: NumberStyles) -> Single

            Converts the string representation of a number in a specified style to its single-precision floating-point number equivalent.

            s: A string that contains a number to convert.

            style: A bitwise combination of enumeration values that indicates the style elements that can be present in s. A typical value to specify is

             System.Globalization.NumberStyles.Float combined with System.Globalization.NumberStyles.AllowThousands.

            Returns: A single-precision floating-point number that is equivalent to the numeric value or symbol specified in s.

        Parse(s: str, provider: IFormatProvider) -> Single

            Converts the string representation of a number in a specified culture-specific format to its single-precision floating-point number equivalent.

            s: A string that contains a number to convert.

            provider: An object that supplies culture-specific formatting information about s.

            Returns: A single-precision floating-point number equivalent to the numeric value or symbol specified in s.

        Parse(s: str, style: NumberStyles, provider: IFormatProvider) -> Single

            Converts the string representation of a number in a specified style and culture-specific format to its single-precision floating-point number

             equivalent.

            s: A string that contains a number to convert.

            style: A bitwise combination of enumeration values that indicates the style elements that can be present in s. A typical value to specify is

             System.Globalization.NumberStyles.Float combined with System.Globalization.NumberStyles.AllowThousands.

            provider: An object that supplies culture-specific formatting information about s.

            Returns: A single-precision floating-point number equivalent to the numeric value or symbol specified in s.
        """
        ...

    @staticmethod
    def TryParse(s, *__args):
        """
        TryParse(s: str) -> (bool, Single)

            Converts the string representation of a number to its single-precision floating-point number equivalent. A return value indicates whether the

             conversion succeeded or failed.

            s: A string representing a number to convert.

            Returns: ue if s was converted successfully; otherwise, lse.

        TryParse(s: str, style: NumberStyles, provider: IFormatProvider) -> (bool, Single)

            Converts the string representation of a number in a specified style and culture-specific format to its single-precision floating-point number

             equivalent. A return value indicates whether the conversion succeeded or failed.

            s: A string representing a number to convert.

            style: A bitwise combination of enumeration values that indicates the permitted format of s. A typical value to specify is

             System.Globalization.NumberStyles.Float combined with System.Globalization.NumberStyles.AllowThousands.

            provider: An object that supplies culture-specific formatting information about s.

            Returns: ue if s was converted successfully; otherwise, lse.
        """
        ...

    def __abs__(self, *args): #cannot find CLR method
        """ x.__abs__() <==> abs(x) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __div__(self, *args): #cannot find CLR method
        """ x.__div__(y) <==> x/y """
        ...

    def __float__(self, *args): #cannot find CLR method
        """ __float__(x: Single) -> float """
        ...

    def __floordiv__(self, *args): #cannot find CLR method
        """ x.__floordiv__(y) <==> x//y """
        ...

    def __int__(self, *args): #cannot find CLR method
        """ __int__(x: Single) -> int """
        ...

    def __mod__(self, *args): #cannot find CLR method
        """ x.__mod__(y) <==> x%y """
        ...

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*y """
        ...

    def __neg__(self, *args): #cannot find CLR method
        """ x.__neg__() <==> -x """
        ...

    def __nonzero__(self, *args): #cannot find CLR method
        """ __nonzero__(x: Single) -> bool """
        ...

    def __pos__(self, *args): #cannot find CLR method
        """ __pos__(x: Single) -> Single """
        ...

    def __pow__(self, *args): #cannot find CLR method
        """ x.__pow__(y[, z]) <==> pow(x, y[, z]) """
        ...

    def __radd__(self, *args): #cannot find CLR method
        """ __radd__(x: Single, y: Single) -> Single """
        ...

    def __rdiv__(self, *args): #cannot find CLR method
        """ __rdiv__(x: Single, y: Single) -> Single """
        ...

    def __rfloordiv__(self, *args): #cannot find CLR method
        """ __rfloordiv__(x: Single, y: Single) -> Single """
        ...

    def __rmod__(self, *args): #cannot find CLR method
        """ __rmod__(x: Single, y: Single) -> Single """
        ...

    def __rmul__(self, *args): #cannot find CLR method
        """ __rmul__(x: Single, y: Single) -> Single """
        ...

    def __rpow__(self, *args): #cannot find CLR method
        """ __rpow__(x: Single, y: Single) -> Single """
        ...

    def __rsub__(self, *args): #cannot find CLR method
        """ __rsub__(x: Single, y: Single) -> Single """
        ...

    def __rtruediv__(self, *args): #cannot find CLR method
        """ __rtruediv__(x: Single, y: Single) -> Single """
        ...

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        ...

    def __truediv__(self, *args): #cannot find CLR method
        """ x.__truediv__(y) <==> x/y """
        ...

    def __trunc__(self, *args): #cannot find CLR method
        """ __trunc__(x: Single) -> object """
        ...

    Epsilon = None
    imag = None
    MaxValue = None
    MinValue = None
    NaN = None
    NegativeInfinity = None
    PositiveInfinity = None
    real = None


class StackOverflowException(SystemException): # skipped bases: <type 'ISerializable'>, <type '_Exception'>
    """
    The exception that is thrown when the execution stack overflows because it contains too many nested method calls. This class cannot be inherited.

    StackOverflowException()

    StackOverflowException(message: str)

    StackOverflowException(message: str, innerException: Exception)
    """
    SerializeObjectState = None


class STAThreadAttribute(Attribute): # skipped bases: <type '_Attribute'>
    """
    Indicates that the COM threading model for an application is single-threaded apartment (STA).

    STAThreadAttribute()
    """
    pass

class String: # skipped bases: <type 'object'>
    """
    Represents text as a sequence of UTF-16 code units.To browse the .NET Framework source code for this type, see the Reference Source.

    str(value: Char*)

    str(value: Char*, startIndex: int, length: int)

    str(value: SByte*)

    str(value: SByte*, startIndex: int, length: int)

    str(value: SByte*, startIndex: int, length: int, enc: Encoding)

    str(value: Array[Char], startIndex: int, length: int)

    str(value: Array[Char])

    str(c: Char, count: int)
    """
    def capitalize(self, *args): #cannot find CLR method
        """ capitalize(self: str) -> str """
        ...

    def center(self, *args): #cannot find CLR method
        """
        center(self: str, width: int) -> str

        center(self: str, width: int, fillchar: Char) -> str
        """
        ...

    def count(self, *args): #cannot find CLR method
        """
        count(self: str, sub: str) -> int

        count(self: str, sub: str, start: int) -> int

        count(self: str, ssub: str, start: int, end: int) -> int
        """
        ...

    def decode(self, *args): #cannot find CLR method
        """
        decode(s: str) -> str

        decode(s: str, encoding: object, errors: str) -> str
        """
        ...

    def encode(self, *args): #cannot find CLR method
        """ encode(s: str, encoding: object, errors: str) -> str """
        ...

    def endswith(self, *args): #cannot find CLR method
        """
        endswith(self: str, suffix: str) -> bool

        endswith(self: str, suffix: str, start: int) -> bool

        endswith(self: str, suffix: str, start: int, end: int) -> bool

        endswith(self: str, suffix: object) -> bool

        endswith(self: str, suffix: object, start: int) -> bool

        endswith(self: str, suffix: object, start: int, end: int) -> bool
        """
        ...

    def expandtabs(self, *args): #cannot find CLR method
        """
        expandtabs(self: str) -> str

        expandtabs(self: str, tabsize: int) -> str
        """
        ...

    def find(self, *args): #cannot find CLR method
        """
        find(self: str, sub: str) -> int

        find(self: str, sub: str, start: int) -> int

        find(self: str, sub: str, start: long) -> int

        find(self: str, sub: str, start: int, end: int) -> int

        find(self: str, sub: str, start: long, end: long) -> int

        find(self: str, sub: str, start: object, end: object) -> int
        """
        ...

    def format(self, *args): #cannot find CLR method
        """
        format(format_string: str, *args: Array[object]) -> str

        format(format_string�: str, **kwargs�: dict, *args�: Array[object]) -> str
        """
        ...

    def index(self, *args): #cannot find CLR method
        """
        index(self: str, sub: str) -> int

        index(self: str, sub: str, start: int) -> int

        index(self: str, sub: str, start: int, end: int) -> int

        index(self: str, sub: str, start: object, end: object) -> int
        """
        ...

    def isalnum(self, *args): #cannot find CLR method
        """ isalnum(self: str) -> bool """
        ...

    def isalpha(self, *args): #cannot find CLR method
        """ isalpha(self: str) -> bool """
        ...

    def isdecimal(self, *args): #cannot find CLR method
        """ isdecimal(self: str) -> bool """
        ...

    def isdigit(self, *args): #cannot find CLR method
        """ isdigit(self: str) -> bool """
        ...

    def islower(self, *args): #cannot find CLR method
        """ islower(self: str) -> bool """
        ...

    def isnumeric(self, *args): #cannot find CLR method
        """ isnumeric(self: str) -> bool """
        ...

    def isspace(self, *args): #cannot find CLR method
        """ isspace(self: str) -> bool """
        ...

    def istitle(self, *args): #cannot find CLR method
        """ istitle(self: str) -> bool """
        ...

    def isunicode(self, *args): #cannot find CLR method
        """ isunicode(self: str) -> bool """
        ...

    def isupper(self, *args): #cannot find CLR method
        """ isupper(self: str) -> bool """
        ...

    def join(self, *args): #cannot find CLR method
        """
        join(self: str, sequence: object) -> str

        join(self: str, sequence: list) -> str
        """
        ...

    def ljust(self, *args): #cannot find CLR method
        """
        ljust(self: str, width: int) -> str

        ljust(self: str, width: int, fillchar: Char) -> str
        """
        ...

    def lower(self, *args): #cannot find CLR method
        """ lower(self: str) -> str """
        ...

    def lstrip(self, *args): #cannot find CLR method
        """
        lstrip(self: str) -> str

        lstrip(self: str, chars: str) -> str
        """
        ...

    def partition(self, *args): #cannot find CLR method
        """ partition(self: str, sep: str) -> tuple (of str) """
        ...

    def replace(self, *args): #cannot find CLR method
        """ replace(self: str, old: str, new: str, count: int) -> str """
        ...

    def rfind(self, *args): #cannot find CLR method
        """
        rfind(self: str, sub: str) -> int

        rfind(self: str, sub: str, start: int) -> int

        rfind(self: str, sub: str, start: long) -> int

        rfind(self: str, sub: str, start: int, end: int) -> int

        rfind(self: str, sub: str, start: long, end: long) -> int

        rfind(self: str, sub: str, start: object, end: object) -> int
        """
        ...

    def rindex(self, *args): #cannot find CLR method
        """
        rindex(self: str, sub: str) -> int

        rindex(self: str, sub: str, start: int) -> int

        rindex(self: str, sub: str, start: int, end: int) -> int

        rindex(self: str, sub: str, start: object, end: object) -> int
        """
        ...

    def rjust(self, *args): #cannot find CLR method
        """
        rjust(self: str, width: int) -> str

        rjust(self: str, width: int, fillchar: Char) -> str
        """
        ...

    def rpartition(self, *args): #cannot find CLR method
        """ rpartition(self: str, sep: str) -> tuple (of str) """
        ...

    def rsplit(self, *args): #cannot find CLR method
        """
        rsplit(self: str) -> list

        rsplit(self: str, sep: str) -> list

        rsplit(self: str, sep: str, maxsplit: int) -> list
        """
        ...

    def rstrip(self, *args): #cannot find CLR method
        """
        rstrip(self: str) -> str

        rstrip(self: str, chars: str) -> str
        """
        ...

    def split(self, *args): #cannot find CLR method
        """
        split(self: str) -> list

        split(self: str, sep: str) -> list

        split(self: str, sep: str, maxsplit: int) -> list
        """
        ...

    def splitlines(self, *args): #cannot find CLR method
        """
        splitlines(self: str) -> list

        splitlines(self: str, keepends: bool) -> list
        """
        ...

    def startswith(self, *args): #cannot find CLR method
        """
        startswith(self: str, prefix: str) -> bool

        startswith(self: str, prefix: str, start: int) -> bool

        startswith(self: str, prefix: str, start: int, end: int) -> bool

        startswith(self: str, prefix: object) -> bool

        startswith(self: str, prefix: object, start: int) -> bool

        startswith(self: str, prefix: object, start: int, end: int) -> bool
        """
        ...

    def strip(self, *args): #cannot find CLR method
        """
        strip(self: str) -> str

        strip(self: str, chars: str) -> str
        """
        ...

    def swapcase(self, *args): #cannot find CLR method
        """ swapcase(self: str) -> str """
        ...

    def title(self, *args): #cannot find CLR method
        """ title(self: str) -> str """
        ...

    def translate(self, *args): #cannot find CLR method
        """
        translate(self: str, table: dict) -> str

        translate(self: str, table: str) -> str

        translate(self: str, table: str, deletechars: str) -> str
        """
        ...

    def upper(self, *args): #cannot find CLR method
        """ upper(self: str) -> str """
        ...

    def zfill(self, *args): #cannot find CLR method
        """ zfill(self: str, width: int) -> str """
        ...

    def _formatter_field_name_split(self, *args): #cannot find CLR method
        """ _formatter_field_name_split(self: str) -> tuple """
        ...

    def _formatter_parser(self, *args): #cannot find CLR method
        """ _formatter_parser(self: str) -> IEnumerable[tuple] """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """
        __contains__(s: str, item: str) -> bool

        __contains__(s: str, item: Char) -> bool
        """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __getnewargs__(self, *args): #cannot find CLR method
        """ __getnewargs__(self: str) -> object """
        ...

    def __getslice__(self, *args): #cannot find CLR method
        """ __getslice__(self: str, x: int, y: int) -> str """
        ...

    def __ge__(self, *args): #cannot find CLR method
        ...

    def __gt__(self, *args): #cannot find CLR method
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...

    def __le__(self, *args): #cannot find CLR method
        ...

    def __lt__(self, *args): #cannot find CLR method
        ...

    def __mod__(self, *args): #cannot find CLR method
        """ x.__mod__(y) <==> x%y """
        ...

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*yx.__mul__(y) <==> x*yx.__mul__(y) <==> x*y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    def __radd__(self, *args): #cannot find CLR method
        """
        __radd__(self: str, other: str) -> str

        __radd__(self: Char, other: str) -> str
        """
        ...

    def __rmod__(self, *args): #cannot find CLR method
        """ __rmod__(other: object, self: str) -> object """
        ...

    def __rmul__(self, *args): #cannot find CLR method
        """
        __rmul__(other: int, self: str) -> str

        __rmul__(count: Index, self: str) -> object

        __rmul__(count: object, self: str) -> object
        """
        ...


class StringComparer( IComparer, IEqualityComparer):
    """ Represents a string comparison operation that uses specific case and culture-based or ordinal comparison rules. """
    @property
    def CurrentCulture(self):
        """
        Gets a System.StringComparer object that performs a case-sensitive string comparison using the word comparison rules of the current culture.

        Get: CurrentCulture() -> StringComparer
        """
        ...

    @property
    def CurrentCultureIgnoreCase(self):
        """
        Gets a System.StringComparer object that performs case-insensitive string comparisons using the word comparison rules of the current culture.

        Get: CurrentCultureIgnoreCase() -> StringComparer
        """
        ...

    @property
    def InvariantCulture(self):
        """
        Gets a System.StringComparer object that performs a case-sensitive string comparison using the word comparison rules of the invariant culture.

        Get: InvariantCulture() -> StringComparer
        """
        ...

    @property
    def InvariantCultureIgnoreCase(self):
        """
        Gets a System.StringComparer object that performs a case-insensitive string comparison using the word comparison rules of the invariant culture.

        Get: InvariantCultureIgnoreCase() -> StringComparer
        """
        ...

    @property
    def Ordinal(self):
        """
        Gets a System.StringComparer object that performs a case-sensitive ordinal string comparison.

        Get: Ordinal() -> StringComparer
        """
        ...

    @property
    def OrdinalIgnoreCase(self):
        """
        Gets a System.StringComparer object that performs a case-insensitive ordinal string comparison.

        Get: OrdinalIgnoreCase() -> StringComparer
        """
        ...


    @staticmethod
    def Create(culture, ignoreCase):
        """
        Create(culture: CultureInfo, ignoreCase: bool) -> StringComparer

            Creates a System.StringComparer object that compares strings according to the rules of a specified culture.

            culture: A culture whose linguistic rules are used to perform a string comparison.

            ignoreCase: ue to specify that comparison operations be case-insensitive; lse to specify that comparison operations be case-sensitive.

            Returns: A new System.StringComparer object that performs string comparisons according to the comparison rules used by the culture parameter and the case rule

             specified by the ignoreCase parameter.
        """
        ...


class StringComparison(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>
    """
    Specifies the culture, case, and sort rules to be used by certain overloads of the System.String.Compare(System.String,System.String) and System.String.Equals(System.Object) methods.

    enum StringComparison, values: CurrentCulture (0), CurrentCultureIgnoreCase (1), InvariantCulture (2), InvariantCultureIgnoreCase (3), Ordinal (4), OrdinalIgnoreCase (5)
    """
    CurrentCulture = None
    CurrentCultureIgnoreCase = None
    InvariantCulture = None
    InvariantCultureIgnoreCase = None
    Ordinal = None
    OrdinalIgnoreCase = None
    value__ = None


class StringNormalizationExtensions: # skipped bases: <type 'object'>
    """ Provides extension methods to work with normalized strings. """
    @staticmethod
    def IsNormalized(value, normalizationForm=...):
        """
        IsNormalized(value: str) -> bool

            Indicates whether the specified string is in Unicode normalization form C.

            value: A string.

            Returns: ue if value is in normalization form C; otherwise, lse.

        IsNormalized(value: str, normalizationForm: NormalizationForm) -> bool

            Indicates whether a string is in a specified Unicode normalization form.

            value: A string.

            normalizationForm: A Unicode normalization form.

            Returns: ue if value is in normalization form normalizationForm; otherwise, lse.
        """
        ...

    @staticmethod
    def Normalize(value, normalizationForm=...):
        """
        Normalize(value: str) -> str

            Normalizes a string to a Unicode normalization form C.

            value: The string to normalize.

            Returns: A new string whose textual value is the same as value but whose binary representation is in Unicode normalization form C.

        Normalize(value: str, normalizationForm: NormalizationForm) -> str

            Normalizes a string to the specified Unicode normalization form.

            value: The string to normalize.

            normalizationForm: The Unicode normalization form.

            Returns: A new string whose textual value is the same as value but whose binary representation is in the normalizationForm normalization form.
        """
        ...

    __all__ = [
        'IsNormalized',
        'Normalize',
    ]


class StringSplitOptions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>
    """
    Specifies whether applicable erload:System.String.Split method overloads include or omit empty substrings from the return value.

    enum (flags) StringSplitOptions, values: None (0), RemoveEmptyEntries (1)
    """

    RemoveEmptyEntries = None
    value__ = None


class ThreadStaticAttribute(Attribute): # skipped bases: <type '_Attribute'>
    """
    Indicates that the value of a static field is unique for each thread.

    ThreadStaticAttribute()
    """
    pass

class TimeoutException(SystemException): # skipped bases: <type 'ISerializable'>, <type '_Exception'>
    """
    The exception that is thrown when the time allotted for a process or operation has expired.

    TimeoutException()

    TimeoutException(message: str)

    TimeoutException(message: str, innerException: Exception)
    """
    SerializeObjectState = None


class TimeSpan( IComparable, IEquatable, IFormattable):
    """
    Represents a time interval.To browse the .NET Framework source code for this type, see the Reference Source.

    TimeSpan(ticks: Int64)

    TimeSpan(hours: int, minutes: int, seconds: int)

    TimeSpan(days: int, hours: int, minutes: int, seconds: int)

    TimeSpan(days: int, hours: int, minutes: int, seconds: int, milliseconds: int)
    """
    @property
    def Days(self):
        """
        Gets the days component of the time interval represented by the current System.TimeSpan structure.

        Get: Days(self: TimeSpan) -> int
        """
        ...

    @property
    def Hours(self):
        """
        Gets the hours component of the time interval represented by the current System.TimeSpan structure.

        Get: Hours(self: TimeSpan) -> int
        """
        ...

    @property
    def Milliseconds(self):
        """
        Gets the milliseconds component of the time interval represented by the current System.TimeSpan structure.

        Get: Milliseconds(self: TimeSpan) -> int
        """
        ...

    @property
    def Minutes(self):
        """
        Gets the minutes component of the time interval represented by the current System.TimeSpan structure.

        Get: Minutes(self: TimeSpan) -> int
        """
        ...

    @property
    def Seconds(self):
        """
        Gets the seconds component of the time interval represented by the current System.TimeSpan structure.

        Get: Seconds(self: TimeSpan) -> int
        """
        ...

    @property
    def Ticks(self):
        """
        Gets the number of ticks that represent the value of the current System.TimeSpan structure.

        Get: Ticks(self: TimeSpan) -> Int64
        """
        ...

    @property
    def TotalDays(self):
        """
        Gets the value of the current System.TimeSpan structure expressed in whole and fractional days.

        Get: TotalDays(self: TimeSpan) -> float
        """
        ...

    @property
    def TotalHours(self):
        """
        Gets the value of the current System.TimeSpan structure expressed in whole and fractional hours.

        Get: TotalHours(self: TimeSpan) -> float
        """
        ...

    @property
    def TotalMilliseconds(self):
        """
        Gets the value of the current System.TimeSpan structure expressed in whole and fractional milliseconds.

        Get: TotalMilliseconds(self: TimeSpan) -> float
        """
        ...

    @property
    def TotalMinutes(self):
        """
        Gets the value of the current System.TimeSpan structure expressed in whole and fractional minutes.

        Get: TotalMinutes(self: TimeSpan) -> float
        """
        ...

    @property
    def TotalSeconds(self):
        """
        Gets the value of the current System.TimeSpan structure expressed in whole and fractional seconds.

        Get: TotalSeconds(self: TimeSpan) -> float
        """
        ...


    def Add(self, ts):
        """
        Add(self: TimeSpan, ts: TimeSpan) -> TimeSpan

            Returns a new System.TimeSpan object whose value is the sum of the specified System.TimeSpan object and this instance.

            ts: The time interval to add.

            Returns: A new object that represents the value of this instance plus the value of ts.
        """
        ...

    @staticmethod
    def Compare(t1, t2):
        """
        Compare(t1: TimeSpan, t2: TimeSpan) -> int

            Compares two System.TimeSpan values and returns an integer that indicates whether the first value is shorter than, equal to, or longer than the

             second value.

            t1: The first time interval to compare.

            t2: The second time interval to compare.

            Returns: One of the following values.Value Description -1

                          t1 is shorter than t2. 0

                          t1 is equal to t2. 1

                  t1 is longer than t2.
        """
        ...

    def Duration(self):
        """
        Duration(self: TimeSpan) -> TimeSpan

            Returns a new System.TimeSpan object whose value is the absolute value of the current System.TimeSpan object.

            Returns: A new object whose value is the absolute value of the current System.TimeSpan object.
        """
        ...

    @staticmethod
    def FromDays(value):
        """
        FromDays(value: float) -> TimeSpan

            Returns a System.TimeSpan that represents a specified number of days, where the specification is accurate to the nearest millisecond.

            value: A number of days, accurate to the nearest millisecond.

            Returns: An object that represents value.
        """
        ...

    @staticmethod
    def FromHours(value):
        """
        FromHours(value: float) -> TimeSpan

            Returns a System.TimeSpan that represents a specified number of hours, where the specification is accurate to the nearest millisecond.

            value: A number of hours accurate to the nearest millisecond.

            Returns: An object that represents value.
        """
        ...

    @staticmethod
    def FromMilliseconds(value):
        """
        FromMilliseconds(value: float) -> TimeSpan

            Returns a System.TimeSpan that represents a specified number of milliseconds.

            value: A number of milliseconds.

            Returns: An object that represents value.
        """
        ...

    @staticmethod
    def FromMinutes(value):
        """
        FromMinutes(value: float) -> TimeSpan

            Returns a System.TimeSpan that represents a specified number of minutes, where the specification is accurate to the nearest millisecond.

            value: A number of minutes, accurate to the nearest millisecond.

            Returns: An object that represents value.
        """
        ...

    @staticmethod
    def FromSeconds(value):
        """
        FromSeconds(value: float) -> TimeSpan

            Returns a System.TimeSpan that represents a specified number of seconds, where the specification is accurate to the nearest millisecond.

            value: A number of seconds, accurate to the nearest millisecond.

            Returns: An object that represents value.
        """
        ...

    @staticmethod
    def FromTicks(value):
        """
        FromTicks(value: Int64) -> TimeSpan

            Returns a System.TimeSpan that represents a specified time, where the specification is in units of ticks.

            value: A number of ticks that represent a time.

            Returns: An object that represents value.
        """
        ...

    def GetHashCode(self):
        """
        GetHashCode(self: TimeSpan) -> int

            Returns a hash code for this instance.

            Returns: A 32-bit signed integer hash code.
        """
        ...

    def Negate(self):
        """
        Negate(self: TimeSpan) -> TimeSpan

            Returns a new System.TimeSpan object whose value is the negated value of this instance.

            Returns: A new object with the same numeric value as this instance, but with the opposite sign.
        """
        ...

    @staticmethod
    def Parse(*__args):
        """
        Parse(s: str) -> TimeSpan

            Converts the string representation of a time interval to its System.TimeSpan equivalent.

            s: A string that specifies the time interval to convert.

            Returns: A time interval that corresponds to s.

        Parse(input: str, formatProvider: IFormatProvider) -> TimeSpan

            Converts the string representation of a time interval to its System.TimeSpan equivalent by using the specified culture-specific format information.

            input: A string that specifies the time interval to convert.

            formatProvider: An object that supplies culture-specific formatting information.

            Returns: A time interval that corresponds to input, as specified by formatProvider.
        """
        ...

    @staticmethod
    def ParseExact(input, *__args):
        """
        ParseExact(input: str, format: str, formatProvider: IFormatProvider) -> TimeSpan

            Converts the string representation of a time interval to its System.TimeSpan equivalent by using the specified format and culture-specific format

             information. The format of the string representation must match the specified format exactly.

            input: A string that specifies the time interval to convert.

            format: A standard or custom format string that defines the required format of input.

            formatProvider: An object that provides culture-specific formatting information.

            Returns: A time interval that corresponds to input, as specified by format and formatProvider.

        ParseExact(input: str, formats: Array[str], formatProvider: IFormatProvider) -> TimeSpan

            Converts the string representation of a time interval to its System.TimeSpan equivalent by using the specified array of format strings and

             culture-specific format information. The format of the string representation must match one of the specified formats exactly.

            input: A string that specifies the time interval to convert.

            formats: A array of standard or custom format strings that defines the required format of input.

            formatProvider: An object that provides culture-specific formatting information.

            Returns: A time interval that corresponds to input, as specified by formats and formatProvider.

        ParseExact(input: str, format: str, formatProvider: IFormatProvider, styles: TimeSpanStyles) -> TimeSpan

            Converts the string representation of a time interval to its System.TimeSpan equivalent by using the specified format, culture-specific format

             information, and styles. The format of the string representation must match the specified format exactly.

            input: A string that specifies the time interval to convert.

            format: A standard or custom format string that defines the required format of input.

            formatProvider: An object that provides culture-specific formatting information.

            styles: A bitwise combination of enumeration values that defines the style elements that may be present in input.

            Returns: A time interval that corresponds to input, as specified by format, formatProvider, and styles.

        ParseExact(input: str, formats: Array[str], formatProvider: IFormatProvider, styles: TimeSpanStyles) -> TimeSpan

            Converts the string representation of a time interval to its System.TimeSpan equivalent by using the specified formats, culture-specific format

             information, and styles. The format of the string representation must match one of the specified formats exactly.

            input: A string that specifies the time interval to convert.

            formats: A array of standard or custom format strings that define the required format of input.

            formatProvider: An object that provides culture-specific formatting information.

            styles: A bitwise combination of enumeration values that defines the style elements that may be present in input.

            Returns: A time interval that corresponds to input, as specified by formats, formatProvider, and styles.
        """
        ...

    def Subtract(self, ts):
        """
        Subtract(self: TimeSpan, ts: TimeSpan) -> TimeSpan

            Returns a new System.TimeSpan object whose value is the difference between the specified System.TimeSpan object and this instance.

            ts: The time interval to be subtracted.

            Returns: A new time interval whose value is the result of the value of this instance minus the value of ts.
        """
        ...

    @staticmethod
    def TryParse(*__args):
        """
        TryParse(s: str) -> (bool, TimeSpan)

            Converts the string representation of a time interval to its System.TimeSpan equivalent and returns a value that indicates whether the conversion

             succeeded.

            s: A string that specifies the time interval to convert.

            Returns: ue if s was converted successfully; otherwise, lse. This operation returns lse if the s parameter is ll or System.String.Empty, has an invalid

             format, represents a time interval that is less than System.TimeSpan.MinValue or greater than System.TimeSpan.MaxValue, or has at least one days,

             hours, minutes, or seconds component outside its valid range.

        TryParse(input: str, formatProvider: IFormatProvider) -> (bool, TimeSpan)

            Converts the string representation of a time interval to its System.TimeSpan equivalent by using the specified culture-specific formatting

             information, and returns a value that indicates whether the conversion succeeded.

            input: A string that specifies the time interval to convert.

            formatProvider: An object that supplies culture-specific formatting information.

            Returns: ue if input was converted successfully; otherwise, lse. This operation returns lse if the input parameter is ll or System.String.Empty, has an

             invalid format, represents a time interval that is less than System.TimeSpan.MinValue or greater than System.TimeSpan.MaxValue, or has at least one

             days, hours, minutes, or seconds component outside its valid range.
        """
        ...

    @staticmethod
    def TryParseExact(input, *__args):
        """
        TryParseExact(input: str, format: str, formatProvider: IFormatProvider) -> (bool, TimeSpan)

            Converts the string representation of a time interval to its System.TimeSpan equivalent by using the specified format and culture-specific format

             information, and returns a value that indicates whether the conversion succeeded. The format of the string representation must match the specified

             format exactly.

            input: A string that specifies the time interval to convert.

            format: A standard or custom format string that defines the required format of input.

            formatProvider: An object that supplies culture-specific formatting information.

            Returns: ue if input was converted successfully; otherwise, lse.

        TryParseExact(input: str, formats: Array[str], formatProvider: IFormatProvider) -> (bool, TimeSpan)

            Converts the specified string representation of a time interval to its System.TimeSpan equivalent by using the specified formats and culture-specific

             format information, and returns a value that indicates whether the conversion succeeded. The format of the string representation must match one of

             the specified formats exactly.

            input: A string that specifies the time interval to convert.

            formats: A array of standard or custom format strings that define the acceptable formats of input.

            formatProvider: An object that provides culture-specific formatting information.

            Returns: ue if input was converted successfully; otherwise, lse.

        TryParseExact(input: str, format: str, formatProvider: IFormatProvider, styles: TimeSpanStyles) -> (bool, TimeSpan)

            Converts the string representation of a time interval to its System.TimeSpan equivalent by using the specified format, culture-specific format

             information, and styles, and returns a value that indicates whether the conversion succeeded. The format of the string representation must match the

             specified format exactly.

            input: A string that specifies the time interval to convert.

            format: A standard or custom format string that defines the required format of input.

            formatProvider: An object that provides culture-specific formatting information.

            styles: One or more enumeration values that indicate the style of input.

            Returns: ue if input was converted successfully; otherwise, lse.

        TryParseExact(input: str, formats: Array[str], formatProvider: IFormatProvider, styles: TimeSpanStyles) -> (bool, TimeSpan)

            Converts the specified string representation of a time interval to its System.TimeSpan equivalent by using the specified formats, culture-specific

             format information, and styles, and returns a value that indicates whether the conversion succeeded. The format of the string representation must

             match one of the specified formats exactly.

            input: A string that specifies the time interval to convert.

            formats: A array of standard or custom format strings that define the acceptable formats of input.

            formatProvider: An object that supplies culture-specific formatting information.

            styles: One or more enumeration values that indicate the style of input.

            Returns: ue if input was converted successfully; otherwise, lse.
        """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __cmp__(self, *args): #cannot find CLR method
        """ x.__cmp__(y) <==> cmp(x,y) """
        ...

    def __neg__(self, *args): #cannot find CLR method
        """ x.__neg__() <==> -x """
        ...

    def __pos__(self, *args): #cannot find CLR method
        """
        __pos__(t: TimeSpan) -> TimeSpan

            Returns the specified instance of System.TimeSpan.

            t: The time interval to return.

            Returns: The time interval specified by t.
        """
        ...

    def __radd__(self, *args): #cannot find CLR method
        """
        __radd__(t1: TimeSpan, t2: TimeSpan) -> TimeSpan

            Adds two specified System.TimeSpan instances.

            t1: The first time interval to add.

            t2: The second time interval to add.

            Returns: An object whose value is the sum of the values of t1 and t2.
        """
        ...

    def __rsub__(self, *args): #cannot find CLR method
        """
        __rsub__(t1: TimeSpan, t2: TimeSpan) -> TimeSpan

            Subtracts a specified System.TimeSpan from another specified System.TimeSpan.

            t1: The minuend.

            t2: The subtrahend.

            Returns: An object whose value is the result of the value of t1 minus the value of t2.
        """
        ...

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        ...

    MaxValue = None
    MinValue = None
    TicksPerDay = None
    TicksPerHour = None
    TicksPerMillisecond = None
    TicksPerMinute = None
    TicksPerSecond = None
    Zero = None


class TimeZone: # skipped bases: <type 'object'>
    """ Represents a time zone. """
    @property
    def CurrentTimeZone(self):
        """
        Gets the time zone of the current computer.

        Get: CurrentTimeZone() -> TimeZone
        """
        ...

    @property
    def DaylightName(self):
        """
        Gets the daylight saving time zone name.

        Get: DaylightName(self: TimeZone) -> str
        """
        ...

    @property
    def StandardName(self):
        """
        Gets the standard time zone name.

        Get: StandardName(self: TimeZone) -> str
        """
        ...


    def GetDaylightChanges(self, year):
        """
        GetDaylightChanges(self: TimeZone, year: int) -> DaylightTime

            Returns the daylight saving time period for a particular year.

            year: The year that the daylight saving time period applies to.

            Returns: A System.Globalization.DaylightTime object that contains the start and end date for daylight saving time in year.
        """
        ...

    def GetUtcOffset(self, time):
        """
        GetUtcOffset(self: TimeZone, time: DateTime) -> TimeSpan

            Returns the Coordinated Universal Time (UTC) offset for the specified local time.

            time: A date and time value.

            Returns: The Coordinated Universal Time (UTC) offset from time.
        """
        ...

    def IsDaylightSavingTime(self, time, daylightTimes=...):
        """
        IsDaylightSavingTime(self: TimeZone, time: DateTime) -> bool

            Returns a value indicating whether the specified date and time is within a daylight saving time period.

            time: A date and time.

            Returns: ue if time is in a daylight saving time period; otherwise, lse.

        IsDaylightSavingTime(time: DateTime, daylightTimes: DaylightTime) -> bool

            Returns a value indicating whether the specified date and time is within the specified daylight saving time period.

            time: A date and time.

            daylightTimes: A daylight saving time period.

            Returns: ue if time is in daylightTimes; otherwise, lse.
        """
        ...

    def ToLocalTime(self, time):
        """
        ToLocalTime(self: TimeZone, time: DateTime) -> DateTime

            Returns the local time that corresponds to a specified date and time value.

            time: A Coordinated Universal Time (UTC) time.

            Returns: A System.DateTime object whose value is the local time that corresponds to time.
        """
        ...

    def ToUniversalTime(self, time):
        """
        ToUniversalTime(self: TimeZone, time: DateTime) -> DateTime

            Returns the Coordinated Universal Time (UTC) that corresponds to a specified time.

            time: A date and time.

            Returns: A System.DateTime object whose value is the Coordinated Universal Time (UTC) that corresponds to time.
        """
        ...



class TimeZoneInfo( IEquatable, ISerializable, IDeserializationCallback):
    """ Represents any time zone in the world. """
    @property
    def BaseUtcOffset(self):
        """
        Gets the time difference between the current time zone's standard time and Coordinated Universal Time (UTC).

        Get: BaseUtcOffset(self: TimeZoneInfo) -> TimeSpan
        """
        ...

    @property
    def DaylightName(self):
        """
        Gets the display name for the current time zone's daylight saving time.

        Get: DaylightName(self: TimeZoneInfo) -> str
        """
        ...

    @property
    def DisplayName(self):
        """
        Gets the general display name that represents the time zone.

        Get: DisplayName(self: TimeZoneInfo) -> str
        """
        ...

    @property
    def Id(self):
        """
        Gets the time zone identifier.

        Get: Id(self: TimeZoneInfo) -> str
        """
        ...

    @property
    def Local(self):
        """
        Gets a System.TimeZoneInfo object that represents the local time zone.

        Get: Local() -> TimeZoneInfo
        """
        ...

    @property
    def StandardName(self):
        """
        Gets the display name for the time zone's standard time.

        Get: StandardName(self: TimeZoneInfo) -> str
        """
        ...

    @property
    def SupportsDaylightSavingTime(self):
        """
        Gets a value indicating whether the time zone has any daylight saving time rules.

        Get: SupportsDaylightSavingTime(self: TimeZoneInfo) -> bool
        """
        ...

    @property
    def Utc(self):
        """
        Gets a System.TimeZoneInfo object that represents the Coordinated Universal Time (UTC) zone.

        Get: Utc() -> TimeZoneInfo
        """
        ...


    def AdjustmentRule(self, *args): #cannot find CLR method
        # no doc
        ...

    @staticmethod
    def ClearCachedData():
        """
        ClearCachedData()

            Clears cached time zone data.
        """
        ...

    @staticmethod
    def ConvertTime(*__args):
        """
        ConvertTime(dateTimeOffset: DateTimeOffset, destinationTimeZone: TimeZoneInfo) -> DateTimeOffset

            Converts a time to the time in a particular time zone.

            dateTimeOffset: The date and time to convert.

            destinationTimeZone: The time zone to convert dateTime to.

            Returns: The date and time in the destination time zone.

        ConvertTime(dateTime: DateTime, destinationTimeZone: TimeZoneInfo) -> DateTime

            Converts a time to the time in a particular time zone.

            dateTime: The date and time to convert.

            destinationTimeZone: The time zone to convert dateTime to.

            Returns: The date and time in the destination time zone.

        ConvertTime(dateTime: DateTime, sourceTimeZone: TimeZoneInfo, destinationTimeZone: TimeZoneInfo) -> DateTime

            Converts a time from one time zone to another.

            dateTime: The date and time to convert.

            sourceTimeZone: The time zone of dateTime.

            destinationTimeZone: The time zone to convert dateTime to.

            Returns: The date and time in the destination time zone that corresponds to the dateTime parameter in the source time zone.
        """
        ...

    @staticmethod
    def ConvertTimeBySystemTimeZoneId(*__args):
        """
        ConvertTimeBySystemTimeZoneId(dateTimeOffset: DateTimeOffset, destinationTimeZoneId: str) -> DateTimeOffset

            Converts a time to the time in another time zone based on the time zone's identifier.

            dateTimeOffset: The date and time to convert.

            destinationTimeZoneId: The identifier of the destination time zone.

            Returns: The date and time in the destination time zone.

        ConvertTimeBySystemTimeZoneId(dateTime: DateTime, destinationTimeZoneId: str) -> DateTime

            Converts a time to the time in another time zone based on the time zone's identifier.

            dateTime: The date and time to convert.

            destinationTimeZoneId: The identifier of the destination time zone.

            Returns: The date and time in the destination time zone.

        ConvertTimeBySystemTimeZoneId(dateTime: DateTime, sourceTimeZoneId: str, destinationTimeZoneId: str) -> DateTime

            Converts a time from one time zone to another based on time zone identifiers.

            dateTime: The date and time to convert.

            sourceTimeZoneId: The identifier of the source time zone.

            destinationTimeZoneId: The identifier of the destination time zone.

            Returns: The date and time in the destination time zone that corresponds to the dateTime parameter in the source time zone.
        """
        ...

    @staticmethod
    def ConvertTimeFromUtc(dateTime, destinationTimeZone):
        """
        ConvertTimeFromUtc(dateTime: DateTime, destinationTimeZone: TimeZoneInfo) -> DateTime

            Converts a Coordinated Universal Time (UTC) to the time in a specified time zone.

            dateTime: The Coordinated Universal Time (UTC).

            destinationTimeZone: The time zone to convert dateTime to.

            Returns: The date and time in the destination time zone. Its System.DateTime.Kind property is System.DateTimeKind.Utc if destinationTimeZone is

             System.TimeZoneInfo.Utc; otherwise, its System.DateTime.Kind property is System.DateTimeKind.Unspecified.
        """
        ...

    @staticmethod
    def ConvertTimeToUtc(dateTime, sourceTimeZone=...):
        """
        ConvertTimeToUtc(dateTime: DateTime) -> DateTime

            Converts the specified date and time to Coordinated Universal Time (UTC).

            dateTime: The date and time to convert.

            Returns: The Coordinated Universal Time (UTC) that corresponds to the dateTime parameter. The System.DateTime value's System.DateTime.Kind property is always

             set to System.DateTimeKind.Utc.

        ConvertTimeToUtc(dateTime: DateTime, sourceTimeZone: TimeZoneInfo) -> DateTime

            Converts the time in a specified time zone to Coordinated Universal Time (UTC).

            dateTime: The date and time to convert.

            sourceTimeZone: The time zone of dateTime.

            Returns: The Coordinated Universal Time (UTC) that corresponds to the dateTime parameter. The System.DateTime object's System.DateTime.Kind property is always

             set to System.DateTimeKind.Utc.
        """
        ...

    @staticmethod
    def CreateCustomTimeZone(id, baseUtcOffset, displayName, standardDisplayName, daylightDisplayName=..., adjustmentRules=..., disableDaylightSavingTime=...):
        """
        CreateCustomTimeZone(id: str, baseUtcOffset: TimeSpan, displayName: str, standardDisplayName: str) -> TimeZoneInfo

            Creates a custom time zone with a specified identifier, an offset from Coordinated Universal Time (UTC), a display name, and a standard time display

             name.

            id: The time zone's identifier.

            baseUtcOffset: An object that represents the time difference between this time zone and Coordinated Universal Time (UTC).

            displayName: The display name of the new time zone.

            standardDisplayName: The name of the new time zone's standard time.

            Returns: The new time zone.

        CreateCustomTimeZone(id: str, baseUtcOffset: TimeSpan, displayName: str, standardDisplayName: str, daylightDisplayName: str, adjustmentRules: Array[AdjustmentRule]) -> TimeZoneInfo

        CreateCustomTimeZone(id: str, baseUtcOffset: TimeSpan, displayName: str, standardDisplayName: str, daylightDisplayName: str, adjustmentRules: Array[AdjustmentRule], disableDaylightSavingTime: bool) -> TimeZoneInfo
        """
        ...

    @staticmethod
    def FindSystemTimeZoneById(id):
        """
        FindSystemTimeZoneById(id: str) -> TimeZoneInfo

            Retrieves a System.TimeZoneInfo object from the registry based on its identifier.

            id: The time zone identifier, which corresponds to the System.TimeZoneInfo.Id property.

            Returns: An object whose identifier is the value of the id parameter.
        """
        ...

    @staticmethod
    def FromSerializedString(source):
        """
        FromSerializedString(source: str) -> TimeZoneInfo

            Deserializes a string to re-create an original serialized System.TimeZoneInfo object.

            source: The string representation of the serialized System.TimeZoneInfo object.

            Returns: The original serialized object.
        """
        ...

    def GetAdjustmentRules(self):
        """
        GetAdjustmentRules(self: TimeZoneInfo) -> Array[AdjustmentRule]

            Retrieves an array of System.TimeZoneInfo.AdjustmentRule objects that apply to the current System.TimeZoneInfo object.

            Returns: An array of objects for this time zone.
        """
        ...

    def GetAmbiguousTimeOffsets(self, *__args):
        """
        GetAmbiguousTimeOffsets(self: TimeZoneInfo, dateTimeOffset: DateTimeOffset) -> Array[TimeSpan]

            Returns information about the possible dates and times that an ambiguous date and time can be mapped to.

            dateTimeOffset: A date and time.

            Returns: An array of objects that represents possible Coordinated Universal Time (UTC) offsets that a particular date and time can be mapped to.

        GetAmbiguousTimeOffsets(self: TimeZoneInfo, dateTime: DateTime) -> Array[TimeSpan]

            Returns information about the possible dates and times that an ambiguous date and time can be mapped to.

            dateTime: A date and time.

            Returns: An array of objects that represents possible Coordinated Universal Time (UTC) offsets that a particular date and time can be mapped to.
        """
        ...

    def GetHashCode(self):
        """
        GetHashCode(self: TimeZoneInfo) -> int

            Serves as a hash function for hashing algorithms and data structures such as hash tables.

            Returns: A 32-bit signed integer that serves as the hash code for this System.TimeZoneInfo object.
        """
        ...

    @staticmethod
    def GetSystemTimeZones():
        """
        GetSystemTimeZones() -> ReadOnlyCollection[TimeZoneInfo]

            Returns a sorted collection of all the time zones about which information is available on the local system.

            Returns: A read-only collection of System.TimeZoneInfo objects.
        """
        ...

    def GetUtcOffset(self, *__args):
        """
        GetUtcOffset(self: TimeZoneInfo, dateTimeOffset: DateTimeOffset) -> TimeSpan

            Calculates the offset or difference between the time in this time zone and Coordinated Universal Time (UTC) for a particular date and time.

            dateTimeOffset: The date and time to determine the offset for.

            Returns: An object that indicates the time difference between Coordinated Universal Time (UTC) and the current time zone.

        GetUtcOffset(self: TimeZoneInfo, dateTime: DateTime) -> TimeSpan

            Calculates the offset or difference between the time in this time zone and Coordinated Universal Time (UTC) for a particular date and time.

            dateTime: The date and time to determine the offset for.

            Returns: An object that indicates the time difference between the two time zones.
        """
        ...

    def HasSameRules(self, other):
        """
        HasSameRules(self: TimeZoneInfo, other: TimeZoneInfo) -> bool

            Indicates whether the current object and another System.TimeZoneInfo object have the same adjustment rules.

            other: A second object to compare with the current System.TimeZoneInfo object.

            Returns: ue if the two time zones have identical adjustment rules and an identical base offset; otherwise, lse.
        """
        ...

    def IsAmbiguousTime(self, *__args):
        """
        IsAmbiguousTime(self: TimeZoneInfo, dateTimeOffset: DateTimeOffset) -> bool

            Determines whether a particular date and time in a particular time zone is ambiguous and can be mapped to two or more Coordinated Universal Time

             (UTC) times.

            dateTimeOffset: A date and time.

            Returns: ue if the dateTimeOffset parameter is ambiguous in the current time zone; otherwise, lse.

        IsAmbiguousTime(self: TimeZoneInfo, dateTime: DateTime) -> bool

            Determines whether a particular date and time in a particular time zone is ambiguous and can be mapped to two or more Coordinated Universal Time

             (UTC) times.

            dateTime: A date and time value.

            Returns: ue if the dateTime parameter is ambiguous; otherwise, lse.
        """
        ...

    def IsDaylightSavingTime(self, *__args):
        """
        IsDaylightSavingTime(self: TimeZoneInfo, dateTimeOffset: DateTimeOffset) -> bool

            Indicates whether a specified date and time falls in the range of daylight saving time for the time zone of the current System.TimeZoneInfo object.

            dateTimeOffset: A date and time value.

            Returns: ue if the dateTimeOffset parameter is a daylight saving time; otherwise, lse.

        IsDaylightSavingTime(self: TimeZoneInfo, dateTime: DateTime) -> bool

            Indicates whether a specified date and time falls in the range of daylight saving time for the time zone of the current System.TimeZoneInfo object.

            dateTime: A date and time value.

            Returns: ue if the dateTime parameter is a daylight saving time; otherwise, lse.
        """
        ...

    def IsInvalidTime(self, dateTime):
        """
        IsInvalidTime(self: TimeZoneInfo, dateTime: DateTime) -> bool

            Indicates whether a particular date and time is invalid.

            dateTime: A date and time value.

            Returns: ue if dateTime is invalid; otherwise, lse.
        """
        ...

    def ToSerializedString(self):
        """
        ToSerializedString(self: TimeZoneInfo) -> str

            Converts the current System.TimeZoneInfo object to a serialized string.

            Returns: A string that represents the current System.TimeZoneInfo object.
        """
        ...

    def ToString(self):
        """
        ToString(self: TimeZoneInfo) -> str

            Returns the current System.TimeZoneInfo object's display name.

            Returns: The value of the System.TimeZoneInfo.DisplayName property of the current System.TimeZoneInfo object.
        """
        ...

    def TransitionTime(self, *args): #cannot find CLR method
        # no doc
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...



class TimeZoneNotFoundException(Exception): # skipped bases: <type 'ISerializable'>, <type '_Exception'>
    """
    The exception that is thrown when a time zone cannot be found.

    TimeZoneNotFoundException(message: str)

    TimeZoneNotFoundException(message: str, innerException: Exception)

    TimeZoneNotFoundException()
    """
    SerializeObjectState = None


class Tuple:
    """ Provides static methods for creating tuple objects. To browse the .NET Framework source code for this type, see the Reference Source. """
    @staticmethod
    def Create(item1, item2=..., item3=..., item4=..., item5=..., item6=..., item7=..., item8=...):
        """
        Create[(T1, T2)](item1: T1, item2: T2) -> Tuple[T1, T2]

        Create[(T1, T2, T3)](item1: T1, item2: T2, item3: T3) -> Tuple[T1, T2, T3]

        Create[T1](item1: T1) -> Tuple[T1]

        Create[(T1, T2, T3, T4)](item1: T1, item2: T2, item3: T3, item4: T4) -> Tuple[T1, T2, T3, T4]

        Create[(T1, T2, T3, T4, T5)](item1: T1, item2: T2, item3: T3, item4: T4, item5: T5) -> Tuple[T1, T2, T3, T4, T5]

        Create[(T1, T2, T3, T4, T5, T6)](item1: T1, item2: T2, item3: T3, item4: T4, item5: T5, item6: T6) -> Tuple[T1, T2, T3, T4, T5, T6]

        Create[(T1, T2, T3, T4, T5, T6, T7)](item1: T1, item2: T2, item3: T3, item4: T4, item5: T5, item6: T6, item7: T7) -> Tuple[T1, T2, T3, T4, T5, T6, T7]

        Create[(T1, T2, T3, T4, T5, T6, T7, T8)](item1: T1, item2: T2, item3: T3, item4: T4, item5: T5, item6: T6, item7: T7, item8: T8) -> Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8]]
        """
        ...

    __all__ = [
        'Create',
    ]


class TupleExtensions: # skipped bases: <type 'object'>
    """ Provides extension methods for tuples to interoperate with language support for tuples in C#. """
    @staticmethod
    def Deconstruct(value, item1, item2=..., item3=..., item4=..., item5=..., item6=..., item7=..., item8=..., item9=..., item10=..., item11=..., item12=..., item13=..., item14=..., item15=..., item16=..., item17=..., item18=..., item19=..., item20=..., item21=...):
        """
        Deconstruct[T1](value: Tuple[T1]) -> T1

        Deconstruct[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17, T18, T19)](value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13, T14, Tuple[T15, T16, T17, T18, T19]]]) -> (T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17, T18, T19)

        Deconstruct[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17, T18)](value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13, T14, Tuple[T15, T16, T17, T18]]]) -> (T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17, T18)

        Deconstruct[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17)](value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13, T14, Tuple[T15, T16, T17]]]) -> (T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17)

        Deconstruct[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16)](value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13, T14, Tuple[T15, T16]]]) -> (T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16)

        Deconstruct[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15)](value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13, T14, Tuple[T15]]]) -> (T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15)

        Deconstruct[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14)](value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13, T14]]) -> (T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14)

        Deconstruct[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13)](value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13]]) -> (T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13)

        Deconstruct[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12)](value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12]]) -> (T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12)

        Deconstruct[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17, T18, T19, T20)](value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13, T14, Tuple[T15, T16, T17, T18, T19, T20]]]) -> (T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17, T18, T19, T20)

        Deconstruct[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11)](value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11]]) -> (T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11)

        Deconstruct[(T1, T2, T3, T4, T5, T6, T7, T8, T9)](value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9]]) -> (T1, T2, T3, T4, T5, T6, T7, T8, T9)

        Deconstruct[(T1, T2, T3, T4, T5, T6, T7, T8)](value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8]]) -> (T1, T2, T3, T4, T5, T6, T7, T8)

        Deconstruct[(T1, T2, T3, T4, T5, T6, T7)](value: Tuple[T1, T2, T3, T4, T5, T6, T7]) -> (T1, T2, T3, T4, T5, T6, T7)

        Deconstruct[(T1, T2, T3, T4, T5, T6)](value: Tuple[T1, T2, T3, T4, T5, T6]) -> (T1, T2, T3, T4, T5, T6)

        Deconstruct[(T1, T2, T3, T4, T5)](value: Tuple[T1, T2, T3, T4, T5]) -> (T1, T2, T3, T4, T5)

        Deconstruct[(T1, T2, T3, T4)](value: Tuple[T1, T2, T3, T4]) -> (T1, T2, T3, T4)

        Deconstruct[(T1, T2, T3)](value: Tuple[T1, T2, T3]) -> (T1, T2, T3)

        Deconstruct[(T1, T2)](value: Tuple[T1, T2]) -> (T1, T2)

        Deconstruct[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10)](value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10]]) -> (T1, T2, T3, T4, T5, T6, T7, T8, T9, T10)

        Deconstruct[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17, T18, T19, T20, T21)](value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13, T14, Tuple[T15, T16, T17, T18, T19, T20, T21]]]) -> (T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17, T18, T19, T20, T21)
        """
        ...

    @staticmethod
    def ToTuple(value):
        """
        ToTuple[T1](value: ValueTuple[T1]) -> Tuple[T1]

        ToTuple[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17, T18, T19)](value: ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10, T11, T12, T13, T14, ValueTuple[T15, T16, T17, T18, T19]]]) -> Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13, T14, Tuple[T15, T16, T17, T18, T19]]]

        ToTuple[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17, T18)](value: ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10, T11, T12, T13, T14, ValueTuple[T15, T16, T17, T18]]]) -> Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13, T14, Tuple[T15, T16, T17, T18]]]

        ToTuple[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17)](value: ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10, T11, T12, T13, T14, ValueTuple[T15, T16, T17]]]) -> Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13, T14, Tuple[T15, T16, T17]]]

        ToTuple[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16)](value: ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10, T11, T12, T13, T14, ValueTuple[T15, T16]]]) -> Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13, T14, Tuple[T15, T16]]]

        ToTuple[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15)](value: ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10, T11, T12, T13, T14, ValueTuple[T15]]]) -> Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13, T14, Tuple[T15]]]

        ToTuple[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14)](value: ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10, T11, T12, T13, T14]]) -> Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13, T14]]

        ToTuple[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13)](value: ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10, T11, T12, T13]]) -> Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13]]

        ToTuple[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12)](value: ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10, T11, T12]]) -> Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12]]

        ToTuple[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17, T18, T19, T20)](value: ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10, T11, T12, T13, T14, ValueTuple[T15, T16, T17, T18, T19, T20]]]) -> Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13, T14, Tuple[T15, T16, T17, T18, T19, T20]]]

        ToTuple[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11)](value: ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10, T11]]) -> Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11]]

        ToTuple[(T1, T2, T3, T4, T5, T6, T7, T8, T9)](value: ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9]]) -> Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9]]

        ToTuple[(T1, T2, T3, T4, T5, T6, T7, T8)](value: ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8]]) -> Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8]]

        ToTuple[(T1, T2, T3, T4, T5, T6, T7)](value: ValueTuple[T1, T2, T3, T4, T5, T6, T7]) -> Tuple[T1, T2, T3, T4, T5, T6, T7]

        ToTuple[(T1, T2, T3, T4, T5, T6)](value: ValueTuple[T1, T2, T3, T4, T5, T6]) -> Tuple[T1, T2, T3, T4, T5, T6]

        ToTuple[(T1, T2, T3, T4, T5)](value: ValueTuple[T1, T2, T3, T4, T5]) -> Tuple[T1, T2, T3, T4, T5]

        ToTuple[(T1, T2, T3, T4)](value: ValueTuple[T1, T2, T3, T4]) -> Tuple[T1, T2, T3, T4]

        ToTuple[(T1, T2, T3)](value: ValueTuple[T1, T2, T3]) -> Tuple[T1, T2, T3]

        ToTuple[(T1, T2)](value: ValueTuple[T1, T2]) -> Tuple[T1, T2]

        ToTuple[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10)](value: ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10]]) -> Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10]]

        ToTuple[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17, T18, T19, T20, T21)](value: ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10, T11, T12, T13, T14, ValueTuple[T15, T16, T17, T18, T19, T20, T21]]]) -> Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13, T14, Tuple[T15, T16, T17, T18, T19, T20, T21]]]
        """
        ...

    @staticmethod
    def ToValueTuple(value):
        """
        ToValueTuple[T1](value: Tuple[T1]) -> ValueTuple[T1]

        ToValueTuple[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17, T18, T19)](value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13, T14, Tuple[T15, T16, T17, T18, T19]]]) -> ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10, T11, T12, T13, T14, ValueTuple[T15, T16, T17, T18, T19]]]

        ToValueTuple[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17, T18)](value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13, T14, Tuple[T15, T16, T17, T18]]]) -> ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10, T11, T12, T13, T14, ValueTuple[T15, T16, T17, T18]]]

        ToValueTuple[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17)](value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13, T14, Tuple[T15, T16, T17]]]) -> ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10, T11, T12, T13, T14, ValueTuple[T15, T16, T17]]]

        ToValueTuple[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16)](value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13, T14, Tuple[T15, T16]]]) -> ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10, T11, T12, T13, T14, ValueTuple[T15, T16]]]

        ToValueTuple[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15)](value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13, T14, Tuple[T15]]]) -> ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10, T11, T12, T13, T14, ValueTuple[T15]]]

        ToValueTuple[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14)](value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13, T14]]) -> ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10, T11, T12, T13, T14]]

        ToValueTuple[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13)](value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13]]) -> ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10, T11, T12, T13]]

        ToValueTuple[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12)](value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12]]) -> ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10, T11, T12]]

        ToValueTuple[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17, T18, T19, T20)](value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13, T14, Tuple[T15, T16, T17, T18, T19, T20]]]) -> ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10, T11, T12, T13, T14, ValueTuple[T15, T16, T17, T18, T19, T20]]]

        ToValueTuple[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11)](value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11]]) -> ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10, T11]]

        ToValueTuple[(T1, T2, T3, T4, T5, T6, T7, T8, T9)](value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9]]) -> ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9]]

        ToValueTuple[(T1, T2, T3, T4, T5, T6, T7, T8)](value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8]]) -> ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8]]

        ToValueTuple[(T1, T2, T3, T4, T5, T6, T7)](value: Tuple[T1, T2, T3, T4, T5, T6, T7]) -> ValueTuple[T1, T2, T3, T4, T5, T6, T7]

        ToValueTuple[(T1, T2, T3, T4, T5, T6)](value: Tuple[T1, T2, T3, T4, T5, T6]) -> ValueTuple[T1, T2, T3, T4, T5, T6]

        ToValueTuple[(T1, T2, T3, T4, T5)](value: Tuple[T1, T2, T3, T4, T5]) -> ValueTuple[T1, T2, T3, T4, T5]

        ToValueTuple[(T1, T2, T3, T4)](value: Tuple[T1, T2, T3, T4]) -> ValueTuple[T1, T2, T3, T4]

        ToValueTuple[(T1, T2, T3)](value: Tuple[T1, T2, T3]) -> ValueTuple[T1, T2, T3]

        ToValueTuple[(T1, T2)](value: Tuple[T1, T2]) -> ValueTuple[T1, T2]

        ToValueTuple[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10)](value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10]]) -> ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10]]

        ToValueTuple[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17, T18, T19, T20, T21)](value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13, T14, Tuple[T15, T16, T17, T18, T19, T20, T21]]]) -> ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10, T11, T12, T13, T14, ValueTuple[T15, T16, T17, T18, T19, T20, T21]]]
        """
        ...

    __all__ = [
        'Deconstruct',
        'ToTuple',
        'ToValueTuple',
    ]


class Type(MemberInfo, _Type, IReflect): #type: ignore # skipped bases: <type 'ICustomAttributeProvider'>, <type '_MemberInfo'>
    """ Represents type declarations: class types, interface types, array types, value types, enumeration types, type parameters, generic type definitions, and open or closed constructed generic types.To browse the .NET Framework source code for this type, see the Reference Source. """
    @property
    def ContainsGenericParameters(self):
        """
        Gets a value indicating whether the current System.Type object has type parameters that have not been replaced by specific types.

        Get: ContainsGenericParameters(self: Type) -> bool
        """
        ...

    @property
    def DeclaringMethod(self):
        """
        Gets a System.Reflection.MethodBase that represents the declaring method, if the current System.Type represents a type parameter of a generic method.

        Get: DeclaringMethod(self: Type) -> MethodBase
        """
        ...

    @property
    def DefaultBinder(self):
        """
        Gets a reference to the default binder, which implements internal rules for selecting the appropriate members to be called by System.Type.InvokeMember(System.String,System.Reflection.BindingFlags,System.Reflection.Binder,System.Object,System.Object[],System.Reflection.ParameterModifier[],System.Globalization.CultureInfo,System.String[]).

        Get: DefaultBinder() -> Binder
        """
        ...

    @property
    def GenericParameterAttributes(self):
        """
        Gets a combination of System.Reflection.GenericParameterAttributes flags that describe the covariance and special constraints of the current generic type parameter.

        Get: GenericParameterAttributes(self: Type) -> GenericParameterAttributes
        """
        ...

    @property
    def GenericParameterPosition(self):
        """
        Gets the position of the type parameter in the type parameter list of the generic type or method that declared the parameter, when the System.Type object represents a type parameter of a generic type or a generic method.

        Get: GenericParameterPosition(self: Type) -> int
        """
        ...

    @property
    def GenericTypeArguments(self):
        """
        Gets an array of the generic type arguments for this type.

        Get: GenericTypeArguments(self: Type) -> Array[Type]
        """
        ...

    @property
    def IsConstructedGenericType(self):
        """
        Gets a value that indicates whether this object represents a constructed generic type. You can create instances of a constructed generic type.

        Get: IsConstructedGenericType(self: Type) -> bool
        """
        ...

    @property
    def IsGenericParameter(self):
        """
        Gets a value indicating whether the current System.Type represents a type parameter in the definition of a generic type or method.

        Get: IsGenericParameter(self: Type) -> bool
        """
        ...

    @property
    def IsGenericType(self):
        """
        Gets a value indicating whether the current type is a generic type.

        Get: IsGenericType(self: Type) -> bool
        """
        ...

    @property
    def IsGenericTypeDefinition(self):
        """
        Gets a value indicating whether the current System.Type represents a generic type definition, from which other generic types can be constructed.

        Get: IsGenericTypeDefinition(self: Type) -> bool
        """
        ...

    @property
    def IsNested(self):
        """
        Gets a value indicating whether the current System.Type object represents a type whose definition is nested inside the definition of another type.

        Get: IsNested(self: Type) -> bool
        """
        ...

    @property
    def IsSecurityCritical(self):
        """
        Gets a value that indicates whether the current type is security-critical or security-safe-critical at the current trust level, and therefore can perform critical operations.

        Get: IsSecurityCritical(self: Type) -> bool
        """
        ...

    @property
    def IsSecuritySafeCritical(self):
        """
        Gets a value that indicates whether the current type is security-safe-critical at the current trust level; that is, whether it can perform critical operations and can be accessed by transparent code.

        Get: IsSecuritySafeCritical(self: Type) -> bool
        """
        ...

    @property
    def IsSecurityTransparent(self):
        """
        Gets a value that indicates whether the current type is transparent at the current trust level, and therefore cannot perform critical operations.

        Get: IsSecurityTransparent(self: Type) -> bool
        """
        ...

    @property
    def IsVisible(self):
        """
        Gets a value indicating whether the System.Type can be accessed by code outside the assembly.

        Get: IsVisible(self: Type) -> bool
        """
        ...

    @property
    def StructLayoutAttribute(self):
        """
        Gets a System.Runtime.InteropServices.StructLayoutAttribute that describes the layout of the current type.

        Get: StructLayoutAttribute(self: Type) -> StructLayoutAttribute
        """
        ...


    def GetAttributeFlagsImpl(self, *args): #cannot find CLR method
        """
        GetAttributeFlagsImpl(self: Type) -> TypeAttributes

            When overridden in a derived class, implements the System.Type.Attributes property and gets a bitmask indicating the attributes associated with the

             System.Type.

            Returns: A System.Reflection.TypeAttributes object representing the attribute set of the System.Type.
        """
        ...

    def GetConstructorImpl(self, *args): #cannot find CLR method
        """
        GetConstructorImpl(self: Type, bindingAttr: BindingFlags, binder: Binder, callConvention: CallingConventions, types: Array[Type], modifiers: Array[ParameterModifier]) -> ConstructorInfo

            When overridden in a derived class, searches for a constructor whose parameters match the specified argument types and modifiers, using the specified

             binding constraints and the specified calling convention.

            bindingAttr: A bitmask comprised of one or more System.Reflection.BindingFlags that specify how the search is conducted.-or- Zero, to return ll.

            binder: An object that defines a set of properties and enables binding, which can involve selection of an overloaded method, coercion of argument types, and

             invocation of a member through reflection.-or- A null reference (thing in Visual Basic), to use the System.Type.DefaultBinder.

            callConvention: The object that specifies the set of rules to use regarding the order and layout of arguments, how the return value is passed, what registers are

             used for arguments, and the stack is cleaned up.

            types: An array of System.Type objects representing the number, order, and type of the parameters for the constructor to get.-or- An empty array of the type

             System.Type (that is, Type[] types = new Type[0]) to get a constructor that takes no parameters.

            modifiers: An array of System.Reflection.ParameterModifier objects representing the attributes associated with the corresponding element in the types array. The

             default binder does not process this parameter.

            Returns: A System.Reflection.ConstructorInfo object representing the constructor that matches the specified requirements, if found; otherwise, ll.
        """
        ...

    def GetEnumName(self, value):
        """
        GetEnumName(self: Type, value: object) -> str

            Returns the name of the constant that has the specified value, for the current enumeration type.

            value: The value whose name is to be retrieved.

            Returns: The name of the member of the current enumeration type that has the specified value, or ll if no such constant is found.
        """
        ...

    def GetEnumNames(self):
        """
        GetEnumNames(self: Type) -> Array[str]

            Returns the names of the members of the current enumeration type.

            Returns: An array that contains the names of the members of the enumeration.
        """
        ...

    def GetEnumUnderlyingType(self):
        """
        GetEnumUnderlyingType(self: Type) -> Type

            Returns the underlying type of the current enumeration type.

            Returns: The underlying type of the current enumeration.
        """
        ...

    def GetEnumValues(self):
        """
        GetEnumValues(self: Type) -> Array

            Returns an array of the values of the constants in the current enumeration type.

            Returns: An array that contains the values. The elements of the array are sorted by the binary values (that is, the unsigned values) of the enumeration

             constants.
        """
        ...

    def GetGenericArguments(self):
        """
        GetGenericArguments(self: Type) -> Array[Type]

            Returns an array of System.Type objects that represent the type arguments of a closed generic type or the type parameters of a generic type

             definition.

            Returns: An array of System.Type objects that represent the type arguments of a generic type. Returns an empty array if the current type is not a generic type.
        """
        ...

    def GetGenericParameterConstraints(self):
        """
        GetGenericParameterConstraints(self: Type) -> Array[Type]

            Returns an array of System.Type objects that represent the constraints on the current generic type parameter.

            Returns: An array of System.Type objects that represent the constraints on the current generic type parameter.
        """
        ...

    def GetGenericTypeDefinition(self):
        """
        GetGenericTypeDefinition(self: Type) -> Type

            Returns a System.Type object that represents a generic type definition from which the current generic type can be constructed.

            Returns: A System.Type object representing a generic type from which the current type can be constructed.
        """
        ...

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: Type, name: str, bindingAttr: BindingFlags, binder: Binder, callConvention: CallingConventions, types: Array[Type], modifiers: Array[ParameterModifier]) -> MethodInfo

            When overridden in a derived class, searches for the specified method whose parameters match the specified argument types and modifiers, using the

             specified binding constraints and the specified calling convention.

            name: The string containing the name of the method to get.

            bindingAttr: A bitmask comprised of one or more System.Reflection.BindingFlags that specify how the search is conducted.-or- Zero, to return ll.

            binder: An object that defines a set of properties and enables binding, which can involve selection of an overloaded method, coercion of argument types, and

             invocation of a member through reflection.-or- A null reference (thing in Visual Basic), to use the System.Type.DefaultBinder.

            callConvention: The object that specifies the set of rules to use regarding the order and layout of arguments, how the return value is passed, what registers are

             used for arguments, and what process cleans up the stack.

            types: An array of System.Type objects representing the number, order, and type of the parameters for the method to get.-or- An empty array of the type

             System.Type (that is, Type[] types = new Type[0]) to get a method that takes no parameters.-or-

                    ll. If types is ll, arguments are not

             matched.

            modifiers: An array of System.Reflection.ParameterModifier objects representing the attributes associated with the corresponding element in the types array. The

             default binder does not process this parameter.

            Returns: An object representing the method that matches the specified requirements, if found; otherwise, ll.
        """
        ...

    def GetPropertyImpl(self, *args): #cannot find CLR method
        """
        GetPropertyImpl(self: Type, name: str, bindingAttr: BindingFlags, binder: Binder, returnType: Type, types: Array[Type], modifiers: Array[ParameterModifier]) -> PropertyInfo

            When overridden in a derived class, searches for the specified property whose parameters match the specified argument types and modifiers, using the

             specified binding constraints.

            name: The string containing the name of the property to get.

            bindingAttr: A bitmask comprised of one or more System.Reflection.BindingFlags that specify how the search is conducted.-or- Zero, to return ll.

            binder: An object that defines a set of properties and enables binding, which can involve selection of an overloaded member, coercion of argument types, and

             invocation of a member through reflection.-or- A null reference (thing in Visual Basic), to use the System.Type.DefaultBinder.

            returnType: The return type of the property.

            types: An array of System.Type objects representing the number, order, and type of the parameters for the indexed property to get.-or- An empty array of the

             type System.Type (that is, Type[] types = new Type[0]) to get a property that is not indexed.

            modifiers: An array of System.Reflection.ParameterModifier objects representing the attributes associated with the corresponding element in the types array. The

             default binder does not process this parameter.

            Returns: An object representing the property that matches the specified requirements, if found; otherwise, ll.
        """
        ...

    @staticmethod
    def GetTypeArray(args):
        """
        GetTypeArray(args: Array[object]) -> Array[Type]

            Gets the types of the objects in the specified array.

            args: An array of objects whose types to determine.

            Returns: An array of System.Type objects representing the types of the corresponding elements in args.
        """
        ...

    @staticmethod
    def GetTypeCode(type):
        """
        GetTypeCode(type: Type) -> TypeCode

            Gets the underlying type code of the specified System.Type.

            type: The type whose underlying type code to get.

            Returns: The code of the underlying type, or System.TypeCode.Empty if type is ll.
        """
        ...

    def GetTypeCodeImpl(self, *args): #cannot find CLR method
        """
        GetTypeCodeImpl(self: Type) -> TypeCode

            Returns the underlying type code of this System.Type instance.

            Returns: The type code of the underlying type.
        """
        ...

    @staticmethod
    def GetTypeFromCLSID(clsid, *__args):
        """
        GetTypeFromCLSID(clsid: Guid) -> Type

            Gets the type associated with the specified class identifier (CLSID).

            clsid: The CLSID of the type to get.

            Returns: stem.__ComObject regardless of whether the CLSID is valid.

        GetTypeFromCLSID(clsid: Guid, throwOnError: bool) -> Type

            Gets the type associated with the specified class identifier (CLSID), specifying whether to throw an exception if an error occurs while loading the

             type.

            clsid: The CLSID of the type to get.

            throwOnError: ue to throw any exception that occurs.-or-

                    lse to ignore any exception that occurs.

            Returns: stem.__ComObject regardless of whether the CLSID is valid.

        GetTypeFromCLSID(clsid: Guid, server: str) -> Type

            Gets the type associated with the specified class identifier (CLSID) from the specified server.

            clsid: The CLSID of the type to get.

            server: The server from which to load the type. If the server name is ll, this method automatically reverts to the local machine.

            Returns: stem.__ComObject regardless of whether the CLSID is valid.

        GetTypeFromCLSID(clsid: Guid, server: str, throwOnError: bool) -> Type

            Gets the type associated with the specified class identifier (CLSID) from the specified server, specifying whether to throw an exception if an error

             occurs while loading the type.

            clsid: The CLSID of the type to get.

            server: The server from which to load the type. If the server name is ll, this method automatically reverts to the local machine.

            throwOnError: ue to throw any exception that occurs.-or-

                    lse to ignore any exception that occurs.

            Returns: stem.__ComObject regardless of whether the CLSID is valid.
        """
        ...

    @staticmethod
    def GetTypeFromHandle(handle):
        """
        GetTypeFromHandle(handle: RuntimeTypeHandle) -> Type

            Gets the type referenced by the specified type handle.

            handle: The object that refers to the type.

            Returns: The type referenced by the specified System.RuntimeTypeHandle, or ll if the System.RuntimeTypeHandle.Value property of handle is ll.
        """
        ...

    @staticmethod
    def GetTypeFromProgID(progID, *__args):
        """
        GetTypeFromProgID(progID: str) -> Type

            Gets the type associated with the specified program identifier (ProgID), returning null if an error is encountered while loading the System.Type.

            progID: The ProgID of the type to get.

            Returns: The type associated with the specified ProgID, if progID is a valid entry in the registry and a type is associated with it; otherwise, ll.

        GetTypeFromProgID(progID: str, throwOnError: bool) -> Type

            Gets the type associated with the specified program identifier (ProgID), specifying whether to throw an exception if an error occurs while loading

             the type.

            progID: The ProgID of the type to get.

            throwOnError: ue to throw any exception that occurs.-or-

                    lse to ignore any exception that occurs.

            Returns: The type associated with the specified program identifier (ProgID), if progID is a valid entry in the registry and a type is associated with it;

             otherwise, ll.

        GetTypeFromProgID(progID: str, server: str) -> Type

            Gets the type associated with the specified program identifier (progID) from the specified server, returning null if an error is encountered while

             loading the type.

            progID: The progID of the type to get.

            server: The server from which to load the type. If the server name is ll, this method automatically reverts to the local machine.

            Returns: The type associated with the specified program identifier (progID), if progID is a valid entry in the registry and a type is associated with it;

             otherwise, ll.

        GetTypeFromProgID(progID: str, server: str, throwOnError: bool) -> Type

            Gets the type associated with the specified program identifier (progID) from the specified server, specifying whether to throw an exception if an

             error occurs while loading the type.

            progID: The progID of the System.Type to get.

            server: The server from which to load the type. If the server name is ll, this method automatically reverts to the local machine.

            throwOnError: ue to throw any exception that occurs.-or-

                    lse to ignore any exception that occurs.

            Returns: The type associated with the specified program identifier (progID), if progID is a valid entry in the registry and a type is associated with it;

             otherwise, ll.
        """
        ...

    @staticmethod
    def GetTypeHandle(o):
        """
        GetTypeHandle(o: object) -> RuntimeTypeHandle

            Gets the handle for the System.Type of a specified object.

            o: The object for which to get the type handle.

            Returns: The handle for the System.Type of the specified System.Object.
        """
        ...

    def HasElementTypeImpl(self, *args): #cannot find CLR method
        """
        HasElementTypeImpl(self: Type) -> bool

            When overridden in a derived class, implements the System.Type.HasElementType property and determines whether the current System.Type encompasses or

             refers to another type; that is, whether the current System.Type is an array, a pointer, or is passed by reference.

            Returns: ue if the System.Type is an array, a pointer, or is passed by reference; otherwise, lse.
        """
        ...

    def IsArrayImpl(self, *args): #cannot find CLR method
        """
        IsArrayImpl(self: Type) -> bool

            When overridden in a derived class, implements the System.Type.IsArray property and determines whether the System.Type is an array.

            Returns: ue if the System.Type is an array; otherwise, lse.
        """
        ...

    def IsByRefImpl(self, *args): #cannot find CLR method
        """
        IsByRefImpl(self: Type) -> bool

            When overridden in a derived class, implements the System.Type.IsByRef property and determines whether the System.Type is passed by reference.

            Returns: ue if the System.Type is passed by reference; otherwise, lse.
        """
        ...

    def IsCOMObjectImpl(self, *args): #cannot find CLR method
        """
        IsCOMObjectImpl(self: Type) -> bool

            When overridden in a derived class, implements the System.Type.IsCOMObject property and determines whether the System.Type is a COM object.

            Returns: ue if the System.Type is a COM object; otherwise, lse.
        """
        ...

    def IsContextfulImpl(self, *args): #cannot find CLR method
        """
        IsContextfulImpl(self: Type) -> bool

            Implements the System.Type.IsContextful property and determines whether the System.Type can be hosted in a context.

            Returns: ue if the System.Type can be hosted in a context; otherwise, lse.
        """
        ...

    def IsEnumDefined(self, value):
        """
        IsEnumDefined(self: Type, value: object) -> bool

            Returns a value that indicates whether the specified value exists in the current enumeration type.

            value: The value to be tested.

            Returns: ue if the specified value is a member of the current enumeration type; otherwise, lse.
        """
        ...

    def IsEquivalentTo(self, other):
        """
        IsEquivalentTo(self: Type, other: Type) -> bool

            Determines whether two COM types have the same identity and are eligible for type equivalence.

            other: The COM type that is tested for equivalence with the current type.

            Returns: ue if the COM types are equivalent; otherwise, lse. This method also returns lse if one type is in an assembly that is loaded for execution, and the

             other is in an assembly that is loaded into the reflection-only context.
        """
        ...

    def IsMarshalByRefImpl(self, *args): #cannot find CLR method
        """
        IsMarshalByRefImpl(self: Type) -> bool

            Implements the System.Type.IsMarshalByRef property and determines whether the System.Type is marshaled by reference.

            Returns: ue if the System.Type is marshaled by reference; otherwise, lse.
        """
        ...

    def IsPointerImpl(self, *args): #cannot find CLR method
        """
        IsPointerImpl(self: Type) -> bool

            When overridden in a derived class, implements the System.Type.IsPointer property and determines whether the System.Type is a pointer.

            Returns: ue if the System.Type is a pointer; otherwise, lse.
        """
        ...

    def IsPrimitiveImpl(self, *args): #cannot find CLR method
        """
        IsPrimitiveImpl(self: Type) -> bool

            When overridden in a derived class, implements the System.Type.IsPrimitive property and determines whether the System.Type is one of the primitive

             types.

            Returns: ue if the System.Type is one of the primitive types; otherwise, lse.
        """
        ...

    def IsValueTypeImpl(self, *args): #cannot find CLR method
        """
        IsValueTypeImpl(self: Type) -> bool

            Implements the System.Type.IsValueType property and determines whether the System.Type is a value type; that is, not a class or an interface.

            Returns: ue if the System.Type is a value type; otherwise, lse.
        """
        ...

    def MakeArrayType(self, rank=...):
        """
        MakeArrayType(self: Type) -> Type

            Returns a System.Type object representing a one-dimensional array of the current type, with a lower bound of zero.

            Returns: A System.Type object representing a one-dimensional array of the current type, with a lower bound of zero.

        MakeArrayType(self: Type, rank: int) -> Type

            Returns a System.Type object representing an array of the current type, with the specified number of dimensions.

            rank: The number of dimensions for the array. This number must be less than or equal to 32.

            Returns: An object representing an array of the current type, with the specified number of dimensions.
        """
        ...

    def MakeByRefType(self):
        """
        MakeByRefType(self: Type) -> Type

            Returns a System.Type object that represents the current type when passed as a f parameter (Ref parameter in Visual Basic).

            Returns: A System.Type object that represents the current type when passed as a f parameter (Ref parameter in Visual Basic).
        """
        ...

    def MakeGenericType(self, typeArguments):
        """
        MakeGenericType(self: Type, *typeArguments: Array[Type]) -> Type

            Substitutes the elements of an array of types for the type parameters of the current generic type definition and returns a System.Type object

             representing the resulting constructed type.

            typeArguments: An array of types to be substituted for the type parameters of the current generic type.

            Returns: A System.Type representing the constructed type formed by substituting the elements of typeArguments for the type parameters of the current generic

             type.
        """
        ...

    def MakePointerType(self):
        """
        MakePointerType(self: Type) -> Type

            Returns a System.Type object that represents a pointer to the current type.

            Returns: A System.Type object that represents a pointer to the current type.
        """
        ...

    @staticmethod
    def ReflectionOnlyGetType(typeName, throwIfNotFound, ignoreCase):
        """
        ReflectionOnlyGetType(typeName: str, throwIfNotFound: bool, ignoreCase: bool) -> Type

            Gets the System.Type with the specified name, specifying whether to perform a case-sensitive search and whether to throw an exception if the type is

             not found. The type is loaded for reflection only, not for execution.

            typeName: The assembly-qualified name of the System.Type to get.

            throwIfNotFound: ue to throw a System.TypeLoadException if the type cannot be found; lse to return ll if the type cannot be found. Specifying lse also suppresses some

             other exception conditions, but not all of them. See the Exceptions section.

            ignoreCase: ue to perform a case-insensitive search for typeName; lse to perform a case-sensitive search for typeName.

            Returns: The type with the specified name, if found; otherwise, ll. If the type is not found, the throwIfNotFound parameter specifies whether ll is returned

             or an exception is thrown. In some cases, an exception is thrown regardless of the value of throwIfNotFound. See the Exceptions section.
        """
        ...

    Delimiter = None
    EmptyTypes = None
    Missing = None


class TypeAccessException(TypeLoadException): # skipped bases: <type 'ISerializable'>, <type '_Exception'>
    """
    The exception that is thrown when a method attempts to use a type that it does not have access to.

    TypeAccessException()

    TypeAccessException(message: str)

    TypeAccessException(message: str, inner: Exception)
    """
    SerializeObjectState = None


class TypeCode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>
    """
    Specifies the type of an object.

    enum TypeCode, values: Boolean (3), Byte (6), Char (4), DateTime (16), DBNull (2), Decimal (15), Double (14), Empty (0), Int16 (7), Int32 (9), Int64 (11), Object (1), SByte (5), Single (13), String (18), UInt16 (8), UInt32 (10), UInt64 (12)
    """
    Boolean = None
    Byte = None
    Char = None
    DateTime = None
    DBNull = None
    Decimal = None
    Double = None
    Empty = None
    Int16 = None
    Int32 = None
    Int64 = None
    Object = None
    SByte = None
    Single = None
    String = None
    UInt16 = None
    UInt32 = None
    UInt64 = None
    value__ = None


class TypedReference: # skipped bases: <type 'object'>
    """ Describes objects that contain both a managed pointer to a location and a runtime representation of the type that may be stored at that location. """
    def Equals(self, o):
        """
        Equals(self: TypedReference, o: object) -> bool

            Checks if this object is equal to the specified object.

            o: The object with which to compare the current object.

            Returns: ue if this object is equal to the specified object; otherwise, lse.
        """
        ...

    def GetHashCode(self):
        """
        GetHashCode(self: TypedReference) -> int

            Returns the hash code of this object.

            Returns: The hash code of this object.
        """
        ...

    @staticmethod
    def GetTargetType(value):
        """
        GetTargetType(value: TypedReference) -> Type

            Returns the type of the target of the specified pedReference.

            value: The value whose target's type is to be returned.

            Returns: The type of the target of the specified pedReference.
        """
        ...

    @staticmethod
    def MakeTypedReference(target, flds):
        """
        MakeTypedReference(target: object, flds: Array[FieldInfo]) -> TypedReference

            Makes a pedReference for a field identified by a specified object and list of field descriptions.

            target: An object that contains the field described by the first element of flds.

            flds: A list of field descriptions where each element describes a field that contains the field described by the succeeding element. Each described field

             must be a value type. The field descriptions must be ntimeFieldInfo objects supplied by the type system.

            Returns: A System.TypedReference for the field described by the last element of flds.
        """
        ...

    @staticmethod
    def SetTypedReference(target, value):
        """
        SetTypedReference(target: TypedReference, value: object)

            Converts the specified value to a pedReference. This method is not supported.

            target: The target of the conversion.

            value: The value to be converted.
        """
        ...

    @staticmethod
    def TargetTypeToken(value):
        """
        TargetTypeToken(value: TypedReference) -> RuntimeTypeHandle

            Returns the internal metadata type handle for the specified pedReference.

            value: The pedReference for which the type handle is requested.

            Returns: The internal metadata type handle for the specified pedReference.
        """
        ...

    @staticmethod
    def ToObject(value):
        """
        ToObject(value: TypedReference) -> object

            Converts the specified pedReference to an ject.

            value: The pedReference to be converted.

            Returns: An System.Object converted from a pedReference.
        """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class TypeInitializationException(SystemException): # skipped bases: <type 'ISerializable'>, <type '_Exception'>
    """
    The exception that is thrown as a wrapper around the exception thrown by the class initializer. This class cannot be inherited.

    TypeInitializationException(fullTypeName: str, innerException: Exception)
    """
    @property
    def TypeName(self):
        """
        Gets the fully qualified name of the type that fails to initialize.

        Get: TypeName(self: TypeInitializationException) -> str
        """
        ...


    SerializeObjectState = None


class TypeUnloadedException(SystemException): # skipped bases: <type 'ISerializable'>, <type '_Exception'>
    """
    The exception that is thrown when there is an attempt to access an unloaded class.

    TypeUnloadedException()

    TypeUnloadedException(message: str)

    TypeUnloadedException(message: str, innerException: Exception)
    """
    SerializeObjectState = None


class UInt16( IComparable, IFormattable, IConvertible, IEquatable):
    """ Represents a 16-bit unsigned integer. """
    def bit_length(self, *args): #cannot find CLR method
        """ bit_length(value: UInt16) -> int """
        ...

    def conjugate(self, *args): #cannot find CLR method
        """ conjugate(x: UInt16) -> UInt16 """
        ...

    def GetHashCode(self):
        """
        GetHashCode(self: UInt16) -> int

            Returns the hash code for this instance.

            Returns: A 32-bit signed integer hash code.
        """
        ...

    @staticmethod
    def Parse(s, *__args):
        """
        Parse(s: str) -> UInt16

            Converts the string representation of a number to its 16-bit unsigned integer equivalent.

            s: A string that represents the number to convert.

            Returns: A 16-bit unsigned integer equivalent to the number contained in s.

        Parse(s: str, style: NumberStyles) -> UInt16

            Converts the string representation of a number in a specified style to its 16-bit unsigned integer equivalent.This method is not CLS-compliant. The

             CLS-compliant alternative is System.Int32.Parse(System.String,System.Globalization.NumberStyles).

            s: A string that represents the number to convert. The string is interpreted by using the style specified by the style parameter.

            style: A bitwise combination of the enumeration values that specify the permitted format of s. A typical value to specify is

             System.Globalization.NumberStyles.Integer.

            Returns: A 16-bit unsigned integer equivalent to the number specified in s.

        Parse(s: str, provider: IFormatProvider) -> UInt16

            Converts the string representation of a number in a specified culture-specific format to its 16-bit unsigned integer equivalent.

            s: A string that represents the number to convert.

            provider: An object that supplies culture-specific formatting information about s.

            Returns: A 16-bit unsigned integer equivalent to the number specified in s.

        Parse(s: str, style: NumberStyles, provider: IFormatProvider) -> UInt16

            Converts the string representation of a number in a specified style and culture-specific format to its 16-bit unsigned integer equivalent.

            s: A string that represents the number to convert. The string is interpreted by using the style specified by the style parameter.

            style: A bitwise combination of enumeration values that indicate the style elements that can be present in s. A typical value to specify is

             System.Globalization.NumberStyles.Integer.

            provider: An object that supplies culture-specific formatting information about s.

            Returns: A 16-bit unsigned integer equivalent to the number specified in s.
        """
        ...

    @staticmethod
    def TryParse(s, *__args):
        """
        TryParse(s: str) -> (bool, UInt16)

            Tries to convert the string representation of a number to its 16-bit unsigned integer equivalent. A return value indicates whether the conversion

             succeeded or failed.

            s: A string that represents the number to convert.

            Returns: ue if s was converted successfully; otherwise, lse.

        TryParse(s: str, style: NumberStyles, provider: IFormatProvider) -> (bool, UInt16)

            Tries to convert the string representation of a number in a specified style and culture-specific format to its 16-bit unsigned integer equivalent. A

             return value indicates whether the conversion succeeded or failed.

            s: A string that represents the number to convert. The string is interpreted by using the style specified by the style parameter.

            style: A bitwise combination of enumeration values that indicates the permitted format of s. A typical value to specify is

             System.Globalization.NumberStyles.Integer.

            provider: An object that supplies culture-specific formatting information about s.

            Returns: ue if s was converted successfully; otherwise, lse.
        """
        ...

    def __abs__(self, *args): #cannot find CLR method
        """ x.__abs__() <==> abs(x) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        ...

    def __and__(self, *args): #cannot find CLR method
        """
        __and__(x: UInt16, y: UInt16) -> UInt16

        __and__(x: UInt16, y: Int16) -> int
        """
        ...

    def __cmp__(self, *args): #cannot find CLR method
        """ x.__cmp__(y) <==> cmp(x,y)x.__cmp__(y) <==> cmp(x,y) """
        ...

    def __div__(self, *args): #cannot find CLR method
        """ x.__div__(y) <==> x/yx.__div__(y) <==> x/y """
        ...

    def __float__(self, *args): #cannot find CLR method
        """ __float__(x: UInt16) -> float """
        ...

    def __floordiv__(self, *args): #cannot find CLR method
        """ x.__floordiv__(y) <==> x//yx.__floordiv__(y) <==> x//y """
        ...

    def __hex__(self, *args): #cannot find CLR method
        """ __hex__(value: UInt16) -> str """
        ...

    def __index__(self, *args): #cannot find CLR method
        """ __index__(x: UInt16) -> int """
        ...

    def __int__(self, *args): #cannot find CLR method
        """ __int__(x: UInt16) -> int """
        ...

    def __invert__(self, *args): #cannot find CLR method
        """ __invert__(x: UInt16) -> object """
        ...

    def __lshift__(self, *args): #cannot find CLR method
        """ x.__rshift__(y) <==> x<<yx.__rshift__(y) <==> x<<y """
        ...

    def __mod__(self, *args): #cannot find CLR method
        """ x.__mod__(y) <==> x%yx.__mod__(y) <==> x%y """
        ...

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*yx.__mul__(y) <==> x*y """
        ...

    def __neg__(self, *args): #cannot find CLR method
        """ x.__neg__() <==> -x """
        ...

    def __nonzero__(self, *args): #cannot find CLR method
        """ __nonzero__(x: UInt16) -> bool """
        ...

    def __or__(self, *args): #cannot find CLR method
        """
        __or__(x: UInt16, y: UInt16) -> UInt16

        __or__(x: UInt16, y: Int16) -> int
        """
        ...

    def __pos__(self, *args): #cannot find CLR method
        """ __pos__(x: UInt16) -> UInt16 """
        ...

    def __pow__(self, *args): #cannot find CLR method
        """ x.__pow__(y[, z]) <==> pow(x, y[, z])x.__pow__(y[, z]) <==> pow(x, y[, z]) """
        ...

    def __radd__(self, *args): #cannot find CLR method
        """
        __radd__(x: UInt16, y: UInt16) -> object

        __radd__(x: Int16, y: UInt16) -> object
        """
        ...

    def __rand__(self, *args): #cannot find CLR method
        """
        __rand__(x: UInt16, y: UInt16) -> UInt16

        __rand__(x: Int16, y: UInt16) -> int
        """
        ...

    def __rdiv__(self, *args): #cannot find CLR method
        """
        __rdiv__(x: UInt16, y: UInt16) -> object

        __rdiv__(x: Int16, y: UInt16) -> object
        """
        ...

    def __rfloordiv__(self, *args): #cannot find CLR method
        """
        __rfloordiv__(x: UInt16, y: UInt16) -> UInt16

        __rfloordiv__(x: Int16, y: UInt16) -> object
        """
        ...

    def __rmod__(self, *args): #cannot find CLR method
        """
        __rmod__(x: UInt16, y: UInt16) -> UInt16

        __rmod__(x: Int16, y: UInt16) -> int
        """
        ...

    def __rmul__(self, *args): #cannot find CLR method
        """
        __rmul__(x: UInt16, y: UInt16) -> object

        __rmul__(x: Int16, y: UInt16) -> object
        """
        ...

    def __ror__(self, *args): #cannot find CLR method
        """
        __ror__(x: UInt16, y: UInt16) -> UInt16

        __ror__(x: Int16, y: UInt16) -> int
        """
        ...

    def __rpow__(self, *args): #cannot find CLR method
        """
        __rpow__(x: UInt16, y: UInt16) -> object

        __rpow__(x: Int16, y: UInt16) -> object
        """
        ...

    def __rshift__(self, *args): #cannot find CLR method
        """ x.__rshift__(y) <==> x>>yx.__rshift__(y) <==> x>>y """
        ...

    def __rsub__(self, *args): #cannot find CLR method
        """
        __rsub__(x: UInt16, y: UInt16) -> object

        __rsub__(x: Int16, y: UInt16) -> object
        """
        ...

    def __rtruediv__(self, *args): #cannot find CLR method
        """
        __rtruediv__(x: UInt16, y: UInt16) -> float

        __rtruediv__(x: Int16, y: UInt16) -> float
        """
        ...

    def __rxor__(self, *args): #cannot find CLR method
        """
        __rxor__(x: UInt16, y: UInt16) -> UInt16

        __rxor__(x: Int16, y: UInt16) -> int
        """
        ...

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-yx.__sub__(y) <==> x-y """
        ...

    def __truediv__(self, *args): #cannot find CLR method
        """ x.__truediv__(y) <==> x/yx.__truediv__(y) <==> x/y """
        ...

    def __trunc__(self, *args): #cannot find CLR method
        """ __trunc__(x: UInt16) -> UInt16 """
        ...

    def __xor__(self, *args): #cannot find CLR method
        """
        __xor__(x: UInt16, y: UInt16) -> UInt16

        __xor__(x: UInt16, y: Int16) -> int
        """
        ...

    denominator = None
    imag = None
    MaxValue = None
    MinValue = None
    numerator = None
    real = None


class UInt32( IComparable, IFormattable, IConvertible, IEquatable):
    """ Represents a 32-bit unsigned integer. """
    def bit_length(self, *args): #cannot find CLR method
        """ bit_length(value: UInt32) -> int """
        ...

    def conjugate(self, *args): #cannot find CLR method
        """ conjugate(x: UInt32) -> UInt32 """
        ...

    def GetHashCode(self):
        """
        GetHashCode(self: UInt32) -> int

            Returns the hash code for this instance.

            Returns: A 32-bit signed integer hash code.
        """
        ...

    @staticmethod
    def Parse(s, *__args):
        """
        Parse(s: str) -> UInt32

            Converts the string representation of a number to its 32-bit unsigned integer equivalent.

            s: A string representing the number to convert.

            Returns: A 32-bit unsigned integer equivalent to the number contained in s.

        Parse(s: str, style: NumberStyles) -> UInt32

            Converts the string representation of a number in a specified style to its 32-bit unsigned integer equivalent.

            s: A string representing the number to convert. The string is interpreted by using the style specified by the style parameter.

            style: A bitwise combination of the enumeration values that specify the permitted format of s. A typical value to specify is

             System.Globalization.NumberStyles.Integer.

            Returns: A 32-bit unsigned integer equivalent to the number specified in s.

        Parse(s: str, provider: IFormatProvider) -> UInt32

            Converts the string representation of a number in a specified culture-specific format to its 32-bit unsigned integer equivalent.

            s: A string that represents the number to convert.

            provider: An object that supplies culture-specific formatting information about s.

            Returns: A 32-bit unsigned integer equivalent to the number specified in s.

        Parse(s: str, style: NumberStyles, provider: IFormatProvider) -> UInt32

            Converts the string representation of a number in a specified style and culture-specific format to its 32-bit unsigned integer equivalent.

            s: A string representing the number to convert. The string is interpreted by using the style specified by the style parameter.

            style: A bitwise combination of enumeration values that indicates the style elements that can be present in s. A typical value to specify is

             System.Globalization.NumberStyles.Integer.

            provider: An object that supplies culture-specific formatting information about s.

            Returns: A 32-bit unsigned integer equivalent to the number specified in s.
        """
        ...

    @staticmethod
    def TryParse(s, *__args):
        """
        TryParse(s: str) -> (bool, UInt32)

            Tries to convert the string representation of a number to its 32-bit unsigned integer equivalent. A return value indicates whether the conversion

             succeeded or failed.

            s: A string that represents the number to convert.

            Returns: ue if s was converted successfully; otherwise, lse.

        TryParse(s: str, style: NumberStyles, provider: IFormatProvider) -> (bool, UInt32)

            Tries to convert the string representation of a number in a specified style and culture-specific format to its 32-bit unsigned integer equivalent. A

             return value indicates whether the conversion succeeded or failed.

            s: A string that represents the number to convert. The string is interpreted by using the style specified by the style parameter.

            style: A bitwise combination of enumeration values that indicates the permitted format of s. A typical value to specify is

             System.Globalization.NumberStyles.Integer.

            provider: An object that supplies culture-specific formatting information about s.

            Returns: ue if s was converted successfully; otherwise, lse.
        """
        ...

    def __abs__(self, *args): #cannot find CLR method
        """ x.__abs__() <==> abs(x) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        ...

    def __and__(self, *args): #cannot find CLR method
        """
        __and__(x: UInt32, y: UInt32) -> UInt32

        __and__(x: UInt32, y: int) -> Int64
        """
        ...

    def __cmp__(self, *args): #cannot find CLR method
        """ x.__cmp__(y) <==> cmp(x,y)x.__cmp__(y) <==> cmp(x,y) """
        ...

    def __div__(self, *args): #cannot find CLR method
        """ x.__div__(y) <==> x/yx.__div__(y) <==> x/y """
        ...

    def __float__(self, *args): #cannot find CLR method
        """ __float__(x: UInt32) -> float """
        ...

    def __floordiv__(self, *args): #cannot find CLR method
        """ x.__floordiv__(y) <==> x//yx.__floordiv__(y) <==> x//y """
        ...

    def __hex__(self, *args): #cannot find CLR method
        """ __hex__(value: UInt32) -> str """
        ...

    def __index__(self, *args): #cannot find CLR method
        """ __index__(x: UInt32) -> int """
        ...

    def __int__(self, *args): #cannot find CLR method
        """ __int__(x: UInt32) -> int """
        ...

    def __invert__(self, *args): #cannot find CLR method
        """ __invert__(x: UInt32) -> object """
        ...

    def __lshift__(self, *args): #cannot find CLR method
        """ x.__rshift__(y) <==> x<<y """
        ...

    def __mod__(self, *args): #cannot find CLR method
        """ x.__mod__(y) <==> x%yx.__mod__(y) <==> x%y """
        ...

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*yx.__mul__(y) <==> x*y """
        ...

    def __neg__(self, *args): #cannot find CLR method
        """ x.__neg__() <==> -x """
        ...

    def __nonzero__(self, *args): #cannot find CLR method
        """ __nonzero__(x: UInt32) -> bool """
        ...

    def __or__(self, *args): #cannot find CLR method
        """
        __or__(x: UInt32, y: UInt32) -> UInt32

        __or__(x: UInt32, y: int) -> Int64
        """
        ...

    def __pos__(self, *args): #cannot find CLR method
        """ __pos__(x: UInt32) -> UInt32 """
        ...

    def __pow__(self, *args): #cannot find CLR method
        """ x.__pow__(y[, z]) <==> pow(x, y[, z])x.__pow__(y[, z]) <==> pow(x, y[, z]) """
        ...

    def __radd__(self, *args): #cannot find CLR method
        """
        __radd__(x: UInt32, y: UInt32) -> object

        __radd__(x: int, y: UInt32) -> object
        """
        ...

    def __rand__(self, *args): #cannot find CLR method
        """
        __rand__(x: UInt32, y: UInt32) -> UInt32

        __rand__(x: int, y: UInt32) -> Int64
        """
        ...

    def __rdiv__(self, *args): #cannot find CLR method
        """
        __rdiv__(x: UInt32, y: UInt32) -> object

        __rdiv__(x: int, y: UInt32) -> object
        """
        ...

    def __rfloordiv__(self, *args): #cannot find CLR method
        """
        __rfloordiv__(x: UInt32, y: UInt32) -> UInt32

        __rfloordiv__(x: int, y: UInt32) -> object
        """
        ...

    def __rmod__(self, *args): #cannot find CLR method
        """
        __rmod__(x: UInt32, y: UInt32) -> UInt32

        __rmod__(x: int, y: UInt32) -> Int64
        """
        ...

    def __rmul__(self, *args): #cannot find CLR method
        """
        __rmul__(x: UInt32, y: UInt32) -> object

        __rmul__(x: int, y: UInt32) -> object
        """
        ...

    def __ror__(self, *args): #cannot find CLR method
        """
        __ror__(x: UInt32, y: UInt32) -> UInt32

        __ror__(x: int, y: UInt32) -> Int64
        """
        ...

    def __rpow__(self, *args): #cannot find CLR method
        """
        __rpow__(x: UInt32, y: UInt32) -> object

        __rpow__(x: int, y: UInt32) -> object
        """
        ...

    def __rshift__(self, *args): #cannot find CLR method
        """ x.__rshift__(y) <==> x>>y """
        ...

    def __rsub__(self, *args): #cannot find CLR method
        """
        __rsub__(x: UInt32, y: UInt32) -> object

        __rsub__(x: int, y: UInt32) -> object
        """
        ...

    def __rtruediv__(self, *args): #cannot find CLR method
        """
        __rtruediv__(x: UInt32, y: UInt32) -> float

        __rtruediv__(x: int, y: UInt32) -> float
        """
        ...

    def __rxor__(self, *args): #cannot find CLR method
        """
        __rxor__(x: UInt32, y: UInt32) -> UInt32

        __rxor__(x: int, y: UInt32) -> Int64
        """
        ...

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-yx.__sub__(y) <==> x-y """
        ...

    def __truediv__(self, *args): #cannot find CLR method
        """ x.__truediv__(y) <==> x/yx.__truediv__(y) <==> x/y """
        ...

    def __trunc__(self, *args): #cannot find CLR method
        """ __trunc__(x: UInt32) -> UInt32 """
        ...

    def __xor__(self, *args): #cannot find CLR method
        """
        __xor__(x: UInt32, y: UInt32) -> UInt32

        __xor__(x: UInt32, y: int) -> Int64
        """
        ...

    denominator = None
    imag = None
    MaxValue = None
    MinValue = None
    numerator = None
    real = None


class UInt64( IComparable, IFormattable, IConvertible, IEquatable):
    """ Represents a 64-bit unsigned integer. """
    def bit_length(self, *args): #cannot find CLR method
        """ bit_length(value: UInt64) -> int """
        ...

    def conjugate(self, *args): #cannot find CLR method
        """ conjugate(x: UInt64) -> UInt64 """
        ...

    def GetHashCode(self):
        """
        GetHashCode(self: UInt64) -> int

            Returns the hash code for this instance.

            Returns: A 32-bit signed integer hash code.
        """
        ...

    @staticmethod
    def Parse(s, *__args):
        """
        Parse(s: str) -> UInt64

            Converts the string representation of a number to its 64-bit unsigned integer equivalent.

            s: A string that represents the number to convert.

            Returns: A 64-bit unsigned integer equivalent to the number contained in s.

        Parse(s: str, style: NumberStyles) -> UInt64

            Converts the string representation of a number in a specified style to its 64-bit unsigned integer equivalent.

            s: A string that represents the number to convert. The string is interpreted by using the style specified by the style parameter.

            style: A bitwise combination of the enumeration values that specifies the permitted format of s. A typical value to specify is

             System.Globalization.NumberStyles.Integer.

            Returns: A 64-bit unsigned integer equivalent to the number specified in s.

        Parse(s: str, provider: IFormatProvider) -> UInt64

            Converts the string representation of a number in a specified culture-specific format to its 64-bit unsigned integer equivalent.

            s: A string that represents the number to convert.

            provider: An object that supplies culture-specific formatting information about s.

            Returns: A 64-bit unsigned integer equivalent to the number specified in s.

        Parse(s: str, style: NumberStyles, provider: IFormatProvider) -> UInt64

            Converts the string representation of a number in a specified style and culture-specific format to its 64-bit unsigned integer equivalent.

            s: A string that represents the number to convert. The string is interpreted by using the style specified by the style parameter.

            style: A bitwise combination of enumeration values that indicates the style elements that can be present in s. A typical value to specify is

             System.Globalization.NumberStyles.Integer.

            provider: An object that supplies culture-specific formatting information about s.

            Returns: A 64-bit unsigned integer equivalent to the number specified in s.
        """
        ...

    @staticmethod
    def TryParse(s, *__args):
        """
        TryParse(s: str) -> (bool, UInt64)

            Tries to convert the string representation of a number to its 64-bit unsigned integer equivalent. A return value indicates whether the conversion

             succeeded or failed.

            s: A string that represents the number to convert.

            Returns: ue if s was converted successfully; otherwise, lse.

        TryParse(s: str, style: NumberStyles, provider: IFormatProvider) -> (bool, UInt64)

            Tries to convert the string representation of a number in a specified style and culture-specific format to its 64-bit unsigned integer equivalent. A

             return value indicates whether the conversion succeeded or failed.

            s: A string that represents the number to convert. The string is interpreted by using the style specified by the style parameter.

            style: A bitwise combination of enumeration values that indicates the permitted format of s. A typical value to specify is

             System.Globalization.NumberStyles.Integer.

            provider: An object that supplies culture-specific formatting information about s.

            Returns: ue if s was converted successfully; otherwise, lse.
        """
        ...

    def __abs__(self, *args): #cannot find CLR method
        """ x.__abs__() <==> abs(x) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        ...

    def __and__(self, *args): #cannot find CLR method
        """
        __and__(x: UInt64, y: UInt64) -> UInt64

        __and__(x: UInt64, y: Int64) -> long
        """
        ...

    def __cmp__(self, *args): #cannot find CLR method
        """ x.__cmp__(y) <==> cmp(x,y)x.__cmp__(y) <==> cmp(x,y) """
        ...

    def __div__(self, *args): #cannot find CLR method
        """ x.__div__(y) <==> x/yx.__div__(y) <==> x/y """
        ...

    def __float__(self, *args): #cannot find CLR method
        """ __float__(x: UInt64) -> float """
        ...

    def __floordiv__(self, *args): #cannot find CLR method
        """ x.__floordiv__(y) <==> x//yx.__floordiv__(y) <==> x//y """
        ...

    def __hex__(self, *args): #cannot find CLR method
        """ __hex__(value: UInt64) -> str """
        ...

    def __index__(self, *args): #cannot find CLR method
        """ __index__(x: UInt64) -> long """
        ...

    def __int__(self, *args): #cannot find CLR method
        """ __int__(x: UInt64) -> int """
        ...

    def __invert__(self, *args): #cannot find CLR method
        """ __invert__(x: UInt64) -> object """
        ...

    def __lshift__(self, *args): #cannot find CLR method
        """ x.__rshift__(y) <==> x<<y """
        ...

    def __mod__(self, *args): #cannot find CLR method
        """ x.__mod__(y) <==> x%yx.__mod__(y) <==> x%y """
        ...

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*yx.__mul__(y) <==> x*y """
        ...

    def __neg__(self, *args): #cannot find CLR method
        """ x.__neg__() <==> -x """
        ...

    def __nonzero__(self, *args): #cannot find CLR method
        """ __nonzero__(x: UInt64) -> bool """
        ...

    def __or__(self, *args): #cannot find CLR method
        """
        __or__(x: UInt64, y: UInt64) -> UInt64

        __or__(x: UInt64, y: Int64) -> long
        """
        ...

    def __pos__(self, *args): #cannot find CLR method
        """ __pos__(x: UInt64) -> UInt64 """
        ...

    def __pow__(self, *args): #cannot find CLR method
        """ x.__pow__(y[, z]) <==> pow(x, y[, z])x.__pow__(y[, z]) <==> pow(x, y[, z]) """
        ...

    def __radd__(self, *args): #cannot find CLR method
        """
        __radd__(x: UInt64, y: UInt64) -> object

        __radd__(x: Int64, y: UInt64) -> object
        """
        ...

    def __rand__(self, *args): #cannot find CLR method
        """
        __rand__(x: UInt64, y: UInt64) -> UInt64

        __rand__(x: Int64, y: UInt64) -> long
        """
        ...

    def __rdiv__(self, *args): #cannot find CLR method
        """
        __rdiv__(x: UInt64, y: UInt64) -> object

        __rdiv__(x: Int64, y: UInt64) -> object
        """
        ...

    def __rfloordiv__(self, *args): #cannot find CLR method
        """
        __rfloordiv__(x: UInt64, y: UInt64) -> UInt64

        __rfloordiv__(x: Int64, y: UInt64) -> object
        """
        ...

    def __rmod__(self, *args): #cannot find CLR method
        """
        __rmod__(x: UInt64, y: UInt64) -> UInt64

        __rmod__(x: Int64, y: UInt64) -> long
        """
        ...

    def __rmul__(self, *args): #cannot find CLR method
        """
        __rmul__(x: UInt64, y: UInt64) -> object

        __rmul__(x: Int64, y: UInt64) -> object
        """
        ...

    def __ror__(self, *args): #cannot find CLR method
        """
        __ror__(x: UInt64, y: UInt64) -> UInt64

        __ror__(x: Int64, y: UInt64) -> long
        """
        ...

    def __rpow__(self, *args): #cannot find CLR method
        """
        __rpow__(x: UInt64, y: UInt64) -> object

        __rpow__(x: Int64, y: UInt64) -> object
        """
        ...

    def __rshift__(self, *args): #cannot find CLR method
        """ x.__rshift__(y) <==> x>>y """
        ...

    def __rsub__(self, *args): #cannot find CLR method
        """
        __rsub__(x: UInt64, y: UInt64) -> object

        __rsub__(x: Int64, y: UInt64) -> object
        """
        ...

    def __rtruediv__(self, *args): #cannot find CLR method
        """
        __rtruediv__(x: UInt64, y: UInt64) -> float

        __rtruediv__(x: Int64, y: UInt64) -> float
        """
        ...

    def __rxor__(self, *args): #cannot find CLR method
        """
        __rxor__(x: UInt64, y: UInt64) -> UInt64

        __rxor__(x: Int64, y: UInt64) -> long
        """
        ...

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-yx.__sub__(y) <==> x-y """
        ...

    def __truediv__(self, *args): #cannot find CLR method
        """ x.__truediv__(y) <==> x/yx.__truediv__(y) <==> x/y """
        ...

    def __trunc__(self, *args): #cannot find CLR method
        """ __trunc__(x: UInt64) -> UInt64 """
        ...

    def __xor__(self, *args): #cannot find CLR method
        """
        __xor__(x: UInt64, y: UInt64) -> UInt64

        __xor__(x: UInt64, y: Int64) -> long
        """
        ...

    denominator = None
    imag = None
    MaxValue = None
    MinValue = None
    numerator = None
    real = None


class UIntPtr( ISerializable):
    """
    A platform-specific type that is used to represent a pointer or a handle.

    UIntPtr(value: UInt32)

    UIntPtr(value: UInt64)

    UIntPtr(value: Void*)
    """
    @property
    def Size(self):
        """
        Gets the size of this instance.

        Get: Size() -> int
        """
        ...


    @staticmethod
    def Add(pointer, offset):
        """
        Add(pointer: UIntPtr, offset: int) -> UIntPtr

            Adds an offset to the value of an unsigned pointer.

            pointer: The unsigned pointer to add the offset to.

            offset: The offset to add.

            Returns: A new unsigned pointer that reflects the addition of offset to pointer.
        """
        ...

    def Equals(self, obj):
        """
        Equals(self: UIntPtr, obj: object) -> bool

            Returns a value indicating whether this instance is equal to a specified object.

            obj: An object to compare with this instance or ll.

            Returns: ue if obj is an instance of System.UIntPtr and equals the value of this instance; otherwise, lse.
        """
        ...

    def GetHashCode(self):
        """
        GetHashCode(self: UIntPtr) -> int

            Returns the hash code for this instance.

            Returns: A 32-bit signed integer hash code.
        """
        ...

    @staticmethod
    def Subtract(pointer, offset):
        """
        Subtract(pointer: UIntPtr, offset: int) -> UIntPtr

            Subtracts an offset from the value of an unsigned pointer.

            pointer: The unsigned pointer to subtract the offset from.

            offset: The offset to subtract.

            Returns: A new unsigned pointer that reflects the subtraction of offset from pointer.
        """
        ...

    def ToPointer(self):
        """
        ToPointer(self: UIntPtr) -> Void*

            Converts the value of this instance to a pointer to an unspecified type.

            Returns: A pointer to System.Void; that is, a pointer to memory containing data of an unspecified type.
        """
        ...

    def ToString(self):
        """
        ToString(self: UIntPtr) -> str

            Converts the numeric value of this instance to its equivalent string representation.

            Returns: The string representation of the value of this instance.
        """
        ...

    def ToUInt32(self):
        """
        ToUInt32(self: UIntPtr) -> UInt32

            Converts the value of this instance to a 32-bit unsigned integer.

            Returns: A 32-bit unsigned integer equal to the value of this instance.
        """
        ...

    def ToUInt64(self):
        """
        ToUInt64(self: UIntPtr) -> UInt64

            Converts the value of this instance to a 64-bit unsigned integer.

            Returns: A 64-bit unsigned integer equal to the value of this instance.
        """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        ...

    Zero = None


class UnauthorizedAccessException(SystemException): # skipped bases: <type 'ISerializable'>, <type '_Exception'>
    """
    The exception that is thrown when the operating system denies access because of an I/O error or a specific type of security error.

    UnauthorizedAccessException()

    UnauthorizedAccessException(message: str)

    UnauthorizedAccessException(message: str, inner: Exception)
    """
    SerializeObjectState = None


class UnhandledExceptionEventArgs(EventArgs):
    """
    Provides data for the event that is raised when there is an exception that is not handled in any application domain.

    UnhandledExceptionEventArgs(exception: object, isTerminating: bool)
    """
    @property
    def ExceptionObject(self):
        """
        Gets the unhandled exception object.

        Get: ExceptionObject(self: UnhandledExceptionEventArgs) -> object
        """
        ...

    @property
    def IsTerminating(self):
        """
        Indicates whether the common language runtime is terminating.

        Get: IsTerminating(self: UnhandledExceptionEventArgs) -> bool
        """
        ...


    @staticmethod # known case of __new__
    def __new__(cls, exception, isTerminating):
        """ __new__(cls: type, exception: object, isTerminating: bool) """
        ...


class UnhandledExceptionEventHandler(MulticastDelegate): # skipped bases: <type 'ICloneable'>, <type 'ISerializable'>
    """
    Represents the method that will handle the event raised by an exception that is not handled by the application domain.

    UnhandledExceptionEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: UnhandledExceptionEventHandler, sender: object, e: UnhandledExceptionEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result):
        """ EndInvoke(self: UnhandledExceptionEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender, e):
        """ Invoke(self: UnhandledExceptionEventHandler, sender: object, e: UnhandledExceptionEventArgs) """
        ...


class Uri( ISerializable):
    """
    Provides an object representation of a uniform resource identifier (URI) and easy access to the parts of the URI.

    Uri(uriString: str)

    Uri(uriString: str, dontEscape: bool)

    Uri(baseUri: Uri, relativeUri: str, dontEscape: bool)

    Uri(uriString: str, uriKind: UriKind)

    Uri(baseUri: Uri, relativeUri: str)

    Uri(baseUri: Uri, relativeUri: Uri)
    """
    @property
    def AbsolutePath(self):
        """
        Gets the absolute path of the URI.

        Get: AbsolutePath(self: Uri) -> str
        """
        ...

    @property
    def AbsoluteUri(self):
        """
        Gets the absolute URI.

        Get: AbsoluteUri(self: Uri) -> str
        """
        ...

    @property
    def Authority(self):
        """
        Gets the Domain Name System (DNS) host name or IP address and the port number for a server.

        Get: Authority(self: Uri) -> str
        """
        ...

    @property
    def DnsSafeHost(self):
        """
        Gets an unescaped host name that is safe to use for DNS resolution.

        Get: DnsSafeHost(self: Uri) -> str
        """
        ...

    @property
    def Fragment(self):
        """
        Gets the escaped URI fragment.

        Get: Fragment(self: Uri) -> str
        """
        ...

    @property
    def Host(self):
        """
        Gets the host component of this instance.

        Get: Host(self: Uri) -> str
        """
        ...

    @property
    def HostNameType(self):
        """
        Gets the type of the host name specified in the URI.

        Get: HostNameType(self: Uri) -> UriHostNameType
        """
        ...

    @property
    def IdnHost(self):
        """
        The RFC 3490 compliant International Domain Name of the host, using Punycode as appropriate.

        Get: IdnHost(self: Uri) -> str
        """
        ...

    @property
    def IsAbsoluteUri(self):
        """
        Gets whether the System.Uri instance is absolute.

        Get: IsAbsoluteUri(self: Uri) -> bool
        """
        ...

    @property
    def IsDefaultPort(self):
        """
        Gets whether the port value of the URI is the default for this scheme.

        Get: IsDefaultPort(self: Uri) -> bool
        """
        ...

    @property
    def IsFile(self):
        """
        Gets a value indicating whether the specified System.Uri is a file URI.

        Get: IsFile(self: Uri) -> bool
        """
        ...

    @property
    def IsLoopback(self):
        """
        Gets whether the specified System.Uri references the local host.

        Get: IsLoopback(self: Uri) -> bool
        """
        ...

    @property
    def IsUnc(self):
        """
        Gets whether the specified System.Uri is a universal naming convention (UNC) path.

        Get: IsUnc(self: Uri) -> bool
        """
        ...

    @property
    def LocalPath(self):
        """
        Gets a local operating-system representation of a file name.

        Get: LocalPath(self: Uri) -> str
        """
        ...

    @property
    def OriginalString(self):
        """
        Gets the original URI string that was passed to the System.Uri constructor.

        Get: OriginalString(self: Uri) -> str
        """
        ...

    @property
    def PathAndQuery(self):
        """
        Gets the System.Uri.AbsolutePath and System.Uri.Query properties separated by a question mark (?).

        Get: PathAndQuery(self: Uri) -> str
        """
        ...

    @property
    def Port(self):
        """
        Gets the port number of this URI.

        Get: Port(self: Uri) -> int
        """
        ...

    @property
    def Query(self):
        """
        Gets any query information included in the specified URI.

        Get: Query(self: Uri) -> str
        """
        ...

    @property
    def Scheme(self):
        """
        Gets the scheme name for this URI.

        Get: Scheme(self: Uri) -> str
        """
        ...

    @property
    def Segments(self):
        """
        Gets an array containing the path segments that make up the specified URI.

        Get: Segments(self: Uri) -> Array[str]
        """
        ...

    @property
    def UserEscaped(self):
        """
        Indicates that the URI string was completely escaped before the System.Uri instance was created.

        Get: UserEscaped(self: Uri) -> bool
        """
        ...

    @property
    def UserInfo(self):
        """
        Gets the user name, password, or other user-specific information associated with the specified URI.

        Get: UserInfo(self: Uri) -> str
        """
        ...


    def Canonicalize(self, *args): #cannot find CLR method
        """
        Canonicalize(self: Uri)

            Converts the internally stored URI to canonical form.
        """
        ...

    @staticmethod
    def CheckHostName(name):
        """
        CheckHostName(name: str) -> UriHostNameType

            Determines whether the specified host name is a valid DNS name.

            name: The host name to validate. This can be an IPv4 or IPv6 address or an Internet host name.

            Returns: A System.UriHostNameType that indicates the type of the host name. If the type of the host name cannot be determined or if the host name is ll or a

             zero-length string, this method returns System.UriHostNameType.Unknown.
        """
        ...

    @staticmethod
    def CheckSchemeName(schemeName):
        """
        CheckSchemeName(schemeName: str) -> bool

            Determines whether the specified scheme name is valid.

            schemeName: The scheme name to validate.

            Returns: A System.Boolean value that is ue if the scheme name is valid; otherwise, lse.
        """
        ...

    def CheckSecurity(self, *args): #cannot find CLR method
        """
        CheckSecurity(self: Uri)

            Calling this method has no effect.
        """
        ...

    @staticmethod
    def Compare(uri1, uri2, partsToCompare, compareFormat, comparisonType):
        """
        Compare(uri1: Uri, uri2: Uri, partsToCompare: UriComponents, compareFormat: UriFormat, comparisonType: StringComparison) -> int

            Compares the specified parts of two URIs using the specified comparison rules.

            uri1: The first System.Uri.

            uri2: The second System.Uri.

            partsToCompare: A bitwise combination of the System.UriComponents values that specifies the parts of uri1 and uri2 to compare.

            compareFormat: One of the System.UriFormat values that specifies the character escaping used when the URI components are compared.

            comparisonType: One of the System.StringComparison values.

            Returns: An System.Int32 value that indicates the lexical relationship between the compared System.Uri components.ValueMeaningLess than zero

              uri1 is less than uri2.Zero

                          uri1 equals uri2.Greater than zero

                          uri1 is greater than uri2.
        """
        ...

    def Equals(self, comparand):
        """
        Equals(self: Uri, comparand: object) -> bool

            Compares two System.Uri instances for equality.

            comparand: The System.Uri instance or a URI identifier to compare with the current instance.

            Returns: A System.Boolean value that is ue if the two instances represent the same URI; otherwise, lse.
        """
        ...

    def Escape(self, *args): #cannot find CLR method
        """
        Escape(self: Uri)

            Converts any unsafe or reserved characters in the path component to their hexadecimal character representations.
        """
        ...

    @staticmethod
    def EscapeDataString(stringToEscape):
        """
        EscapeDataString(stringToEscape: str) -> str

            Converts a string to its escaped representation.

            stringToEscape: The string to escape.

            Returns: A System.String that contains the escaped representation of stringToEscape.
        """
        ...

    def EscapeString(self, *args): #cannot find CLR method
        """
        EscapeString(str: str) -> str

            Converts a string to its escaped representation.

            str: The string to transform to its escaped representation.

            Returns: The escaped representation of the string.
        """
        ...

    @staticmethod
    def EscapeUriString(stringToEscape):
        """
        EscapeUriString(stringToEscape: str) -> str

            Converts a URI string to its escaped representation.

            stringToEscape: The string to escape.

            Returns: A System.String that contains the escaped representation of stringToEscape.
        """
        ...

    @staticmethod
    def FromHex(digit):
        """
        FromHex(digit: Char) -> int

            Gets the decimal value of a hexadecimal digit.

            digit: The hexadecimal digit (0-9, a-f, A-F) to convert.

            Returns: An System.Int32 value that contains a number from 0 to 15 that corresponds to the specified hexadecimal digit.
        """
        ...

    def GetComponents(self, components, format):
        """
        GetComponents(self: Uri, components: UriComponents, format: UriFormat) -> str

            Gets the specified components of the current instance using the specified escaping for special characters.

            components: A bitwise combination of the System.UriComponents values that specifies which parts of the current instance to return to the caller.

            format: One of the System.UriFormat values that controls how special characters are escaped.

            Returns: A System.String that contains the components.
        """
        ...

    def GetHashCode(self):
        """
        GetHashCode(self: Uri) -> int

            Gets the hash code for the URI.

            Returns: An System.Int32 containing the hash value generated for this URI.
        """
        ...

    def GetLeftPart(self, part):
        """
        GetLeftPart(self: Uri, part: UriPartial) -> str

            Gets the specified portion of a System.Uri instance.

            part: One of the System.UriPartial values that specifies the end of the URI portion to return.

            Returns: A System.String that contains the specified portion of the System.Uri instance.
        """
        ...

    @staticmethod
    def HexEscape(character):
        """
        HexEscape(character: Char) -> str

            Converts a specified character into its hexadecimal equivalent.

            character: The character to convert to hexadecimal representation.

            Returns: The hexadecimal representation of the specified character.
        """
        ...

    @staticmethod
    def HexUnescape(pattern, index):
        """
        HexUnescape(pattern: str, index: int) -> (Char, int)

            Converts a specified hexadecimal representation of a character to the character.

            pattern: The hexadecimal representation of a character.

            index: The location in pattern where the hexadecimal representation of a character begins.

            Returns: The character represented by the hexadecimal encoding at position index. If the character at index is not hexadecimal encoded, the character at index

             is returned. The value of index is incremented to point to the character following the one returned.
        """
        ...

    def IsBadFileSystemCharacter(self, *args): #cannot find CLR method
        """
        IsBadFileSystemCharacter(self: Uri, character: Char) -> bool

            Gets whether a character is invalid in a file system name.

            character: The System.Char to test.

            Returns: A System.Boolean value that is ue if the specified character is invalid; otherwise lse.
        """
        ...

    def IsBaseOf(self, uri):
        """
        IsBaseOf(self: Uri, uri: Uri) -> bool

            Determines whether the current System.Uri instance is a base of the specified System.Uri instance.

            uri: The specified System.Uri instance to test.

            Returns: ue if the current System.Uri instance is a base of uri; otherwise, lse.
        """
        ...

    def IsExcludedCharacter(self, *args): #cannot find CLR method
        """
        IsExcludedCharacter(character: Char) -> bool

            Gets whether the specified character should be escaped.

            character: The System.Char to test.

            Returns: A System.Boolean value that is ue if the specified character should be escaped; otherwise, lse.
        """
        ...

    @staticmethod
    def IsHexDigit(character):
        """
        IsHexDigit(character: Char) -> bool

            Determines whether a specified character is a valid hexadecimal digit.

            character: The character to validate.

            Returns: A System.Boolean value that is ue if the character is a valid hexadecimal digit; otherwise lse.
        """
        ...

    @staticmethod
    def IsHexEncoding(pattern, index):
        """
        IsHexEncoding(pattern: str, index: int) -> bool

            Determines whether a character in a string is hexadecimal encoded.

            pattern: The string to check.

            index: The location in pattern to check for hexadecimal encoding.

            Returns: A System.Boolean value that is ue if pattern is hexadecimal encoded at the specified location; otherwise, lse.
        """
        ...

    def IsReservedCharacter(self, *args): #cannot find CLR method
        """
        IsReservedCharacter(self: Uri, character: Char) -> bool

            Gets whether the specified character is a reserved character.

            character: The System.Char to test.

            Returns: A System.Boolean value that is ue if the specified character is a reserved character otherwise, lse.
        """
        ...

    def IsWellFormedOriginalString(self):
        """
        IsWellFormedOriginalString(self: Uri) -> bool

            Indicates whether the string used to construct this System.Uri was well-formed and is not required to be further escaped.

            Returns: A System.Boolean value that is ue if the string was well-formed; else lse.
        """
        ...

    @staticmethod
    def IsWellFormedUriString(uriString, uriKind):
        """
        IsWellFormedUriString(uriString: str, uriKind: UriKind) -> bool

            Indicates whether the string is well-formed by attempting to construct a URI with the string and ensures that the string does not require further

             escaping.

            uriString: The string used to attempt to construct a System.Uri.

            uriKind: The type of the System.Uri in uriString.

            Returns: A System.Boolean value that is ue if the string was well-formed; else lse.
        """
        ...

    def MakeRelative(self, toUri):
        """
        MakeRelative(self: Uri, toUri: Uri) -> str

            Determines the difference between two System.Uri instances.

            toUri: The URI to compare to the current URI.

            Returns: If the hostname and scheme of this URI instance and toUri are the same, then this method returns a System.String that represents a relative URI that,

             when appended to the current URI instance, yields the toUri parameter.If the hostname or scheme is different, then this method returns a

             System.String that represents the toUri parameter.
        """
        ...

    def MakeRelativeUri(self, uri):
        """
        MakeRelativeUri(self: Uri, uri: Uri) -> Uri

            Determines the difference between two System.Uri instances.

            uri: The URI to compare to the current URI.

            Returns: If the hostname and scheme of this URI instance and uri are the same, then this method returns a relative System.Uri that, when appended to the

             current URI instance, yields uri.If the hostname or scheme is different, then this method returns a System.Uri  that represents the uri parameter.
        """
        ...

    def Parse(self, *args): #cannot find CLR method
        """
        Parse(self: Uri)

            Parses the URI of the current instance to ensure it contains all the parts required for a valid URI.
        """
        ...

    def ToString(self):
        """
        ToString(self: Uri) -> str

            Gets a canonical string representation for the specified System.Uri instance.

            Returns: A System.String instance that contains the unescaped canonical representation of the System.Uri instance. All characters are unescaped except #, ?,

             and %.
        """
        ...

    @staticmethod
    def TryCreate(*__args):
        """
        TryCreate(uriString: str, uriKind: UriKind) -> (bool, Uri)

            Creates a new System.Uri using the specified System.String instance and a System.UriKind.

            uriString: The System.String representing the System.Uri.

            uriKind: The type of the Uri.

            Returns: A System.Boolean value that is ue if the System.Uri was successfully created; otherwise, lse.

        TryCreate(baseUri: Uri, relativeUri: str) -> (bool, Uri)

            Creates a new System.Uri using the specified base and relative System.String instances.

            baseUri: The base System.Uri.

            relativeUri: The relative System.Uri, represented as a System.String, to add to the base System.Uri.

            Returns: A System.Boolean value that is ue if the System.Uri was successfully created; otherwise, lse.

        TryCreate(baseUri: Uri, relativeUri: Uri) -> (bool, Uri)

            Creates a new System.Uri using the specified base and relative System.Uri instances.

            baseUri: The base System.Uri.

            relativeUri: The relative System.Uri to add to the base System.Uri.

            Returns: A System.Boolean value that is ue if the System.Uri was successfully created; otherwise, lse.
        """
        ...

    def Unescape(self, *args): #cannot find CLR method
        """
        Unescape(self: Uri, path: str) -> str

            Converts the specified string by replacing any escape sequences with their unescaped representation.

            path: The System.String to convert.

            Returns: A System.String that contains the unescaped value of the path parameter.
        """
        ...

    @staticmethod
    def UnescapeDataString(stringToUnescape):
        """
        UnescapeDataString(stringToUnescape: str) -> str

            Converts a string to its unescaped representation.

            stringToUnescape: The string to unescape.

            Returns: A System.String that contains the unescaped representation of stringToUnescape.
        """
        ...

    def __cmp__(self, *args): #cannot find CLR method
        """ x.__cmp__(y) <==> cmp(x,y) """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    SchemeDelimiter = '://'
    UriSchemeFile = 'file'
    UriSchemeFtp = 'ftp'
    UriSchemeGopher = 'gopher'
    UriSchemeHttp = 'http'
    UriSchemeHttps = 'https'
    UriSchemeMailto = 'mailto'
    UriSchemeNetPipe = 'net.pipe'
    UriSchemeNetTcp = 'net.tcp'
    UriSchemeNews = 'news'
    UriSchemeNntp = 'nntp'


class UriBuilder: # skipped bases: <type 'object'>
    """
    Provides a custom constructor for uniform resource identifiers (URIs) and modifies URIs for the System.Uri class.

    UriBuilder()

    UriBuilder(uri: str)

    UriBuilder(uri: Uri)

    UriBuilder(schemeName: str, hostName: str)

    UriBuilder(scheme: str, host: str, portNumber: int)

    UriBuilder(scheme: str, host: str, port: int, pathValue: str)

    UriBuilder(scheme: str, host: str, port: int, path: str, extraValue: str)
    """
    @property
    def Fragment(self):
        """
        Gets or sets the fragment portion of the URI.

        Get: Fragment(self: UriBuilder) -> str

        Set: Fragment(self: UriBuilder) = value
        """
        ...

    @property
    def Host(self):
        """
        Gets or sets the Domain Name System (DNS) host name or IP address of a server.

        Get: Host(self: UriBuilder) -> str

        Set: Host(self: UriBuilder) = value
        """
        ...

    @property
    def Password(self):
        """
        Gets or sets the password associated with the user that accesses the URI.

        Get: Password(self: UriBuilder) -> str

        Set: Password(self: UriBuilder) = value
        """
        ...

    @property
    def Path(self):
        """
        Gets or sets the path to the resource referenced by the URI.

        Get: Path(self: UriBuilder) -> str

        Set: Path(self: UriBuilder) = value
        """
        ...

    @property
    def Port(self):
        """
        Gets or sets the port number of the URI.

        Get: Port(self: UriBuilder) -> int

        Set: Port(self: UriBuilder) = value
        """
        ...

    @property
    def Query(self):
        """
        Gets or sets any query information included in the URI.

        Get: Query(self: UriBuilder) -> str

        Set: Query(self: UriBuilder) = value
        """
        ...

    @property
    def Scheme(self):
        """
        Gets or sets the scheme name of the URI.

        Get: Scheme(self: UriBuilder) -> str

        Set: Scheme(self: UriBuilder) = value
        """
        ...

    @property
    def Uri(self):
        """
        Gets the System.Uri instance constructed by the specified System.UriBuilder instance.

        Get: Uri(self: UriBuilder) -> Uri
        """
        ...

    @property
    def UserName(self):
        """
        The user name associated with the user that accesses the URI.

        Get: UserName(self: UriBuilder) -> str

        Set: UserName(self: UriBuilder) = value
        """
        ...


    def Equals(self, rparam):
        """
        Equals(self: UriBuilder, rparam: object) -> bool

            Compares an existing System.Uri instance with the contents of the System.UriBuilder for equality.

            rparam: The object to compare with the current instance.

            Returns: ue if rparam represents the same System.Uri as the System.Uri constructed by this System.UriBuilder instance; otherwise, lse.
        """
        ...

    def GetHashCode(self):
        """
        GetHashCode(self: UriBuilder) -> int

            Returns the hash code for the URI.

            Returns: The hash code generated for the URI.
        """
        ...

    def ToString(self):
        """
        ToString(self: UriBuilder) -> str

            Returns the display string for the specified System.UriBuilder instance.

            Returns: The string that contains the unescaped display string of the System.UriBuilder.
        """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class UriComponents(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>
    """
    Specifies the parts of a System.Uri.

    enum (flags) UriComponents, values: AbsoluteUri (127), Fragment (64), Host (4), HostAndPort (132), HttpRequestUrl (61), KeepDelimiter (1073741824), NormalizedHost (256), Path (16), PathAndQuery (48), Port (8), Query (32), Scheme (1), SchemeAndServer (13), SerializationInfoString (-2147483648), StrongAuthority (134), StrongPort (128), UserInfo (2)
    """
    AbsoluteUri = None
    Fragment = None
    Host = None
    HostAndPort = None
    HttpRequestUrl = None
    KeepDelimiter = None
    NormalizedHost = None
    Path = None
    PathAndQuery = None
    Port = None
    Query = None
    Scheme = None
    SchemeAndServer = None
    SerializationInfoString = None
    StrongAuthority = None
    StrongPort = None
    UserInfo = None
    value__ = None


class UriFormat(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>
    """
    Controls how URI information is escaped.

    enum UriFormat, values: SafeUnescaped (3), Unescaped (2), UriEscaped (1)
    """
    SafeUnescaped = None
    Unescaped = None
    UriEscaped = None
    value__ = None


class UriFormatException(FormatException): # skipped bases: <type 'ISerializable'>, <type '_Exception'>
    """
    The exception that is thrown when an invalid Uniform Resource Identifier (URI) is detected.

    UriFormatException()

    UriFormatException(textString: str)

    UriFormatException(textString: str, e: Exception)
    """
    SerializeObjectState = None


class UriHostNameType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>
    """
    Defines host name types for the System.Uri.CheckHostName(System.String) method.

    enum UriHostNameType, values: Basic (1), Dns (2), IPv4 (3), IPv6 (4), Unknown (0)
    """
    Basic = None
    Dns = None
    IPv4 = None
    IPv6 = None
    Unknown = None
    value__ = None


class UriIdnScope(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>
    """
    Provides the possible values for the configuration setting of the System.Configuration.IdnElement in the System.Configuration namespace.

    enum UriIdnScope, values: All (2), AllExceptIntranet (1), None (0)
    """
    All = None
    AllExceptIntranet = None

    value__ = None


class UriKind(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>
    """
    Defines the kinds of System.Uris for the System.Uri.IsWellFormedUriString(System.String,System.UriKind) and several erload:System.Uri.#ctor methods.

    enum UriKind, values: Absolute (1), Relative (2), RelativeOrAbsolute (0)
    """
    Absolute = None
    Relative = None
    RelativeOrAbsolute = None
    value__ = None


class UriPartial(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>
    """
    Defines the parts of a URI for the System.Uri.GetLeftPart(System.UriPartial) method.

    enum UriPartial, values: Authority (1), Path (2), Query (3), Scheme (0)
    """
    Authority = None
    Path = None
    Query = None
    Scheme = None
    value__ = None


class UriTypeConverter(TypeConverter):
    """
    Converts a System.String type to a System.Uri type, and vice versa.

    UriTypeConverter()
    """
    pass

class ValueTuple:
    """ Provides static methods for creating value tuples. """
    def CompareTo(self, other):
        """
        CompareTo(self: ValueTuple, other: ValueTuple) -> int

            Compares the current System.ValueTuple instance with a specified object.

            other: The object to compare with the current instance.

            Returns: Returns 0 if  other is a System.ValueTuple instance and 1 if other is ll.
        """
        ...

    @staticmethod
    def Create(item1=..., item2=..., item3=..., item4=..., item5=..., item6=..., item7=..., item8=...):
        """
        Create() -> ValueTuple

            Creates a new value tuple with zero components.

            Returns: A new value tuple with no components.

        Create[T1](item1: T1) -> ValueTuple[T1]

        Create[(T1, T2)](item1: T1, item2: T2) -> ValueTuple[T1, T2]

        Create[(T1, T2, T3)](item1: T1, item2: T2, item3: T3) -> ValueTuple[T1, T2, T3]

        Create[(T1, T2, T3, T4)](item1: T1, item2: T2, item3: T3, item4: T4) -> ValueTuple[T1, T2, T3, T4]

        Create[(T1, T2, T3, T4, T5)](item1: T1, item2: T2, item3: T3, item4: T4, item5: T5) -> ValueTuple[T1, T2, T3, T4, T5]

        Create[(T1, T2, T3, T4, T5, T6)](item1: T1, item2: T2, item3: T3, item4: T4, item5: T5, item6: T6) -> ValueTuple[T1, T2, T3, T4, T5, T6]

        Create[(T1, T2, T3, T4, T5, T6, T7)](item1: T1, item2: T2, item3: T3, item4: T4, item5: T5, item6: T6, item7: T7) -> ValueTuple[T1, T2, T3, T4, T5, T6, T7]

        Create[(T1, T2, T3, T4, T5, T6, T7, T8)](item1: T1, item2: T2, item3: T3, item4: T4, item5: T5, item6: T6, item7: T7, item8: T8) -> ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8]]
        """
        ...

    def Equals(self, *__args):
        """
        Equals(self: ValueTuple, obj: object) -> bool

            Returns a value that indicates whether the current System.ValueTuple instance is equal to a specified object.

            obj: The object to compare to the current instance.

            Returns: ue if obj is a System.ValueTuple instance; otherwise, lse.

        Equals(self: ValueTuple, other: ValueTuple) -> bool

            Determines whether two System.ValueTuple instances are equal. This method always returns ue.

            other: The value tuple to compare with the current instance.

            Returns: This method always returns ue.
        """
        ...

    def GetHashCode(self):
        """
        GetHashCode(self: ValueTuple) -> int

            Returns the hash code for the current System.ValueTuple instance.

            Returns: The hash code for the current System.ValueTuple instance.
        """
        ...

    def ToString(self):
        """
        ToString(self: ValueTuple) -> str

            Returns the string representation of this System.ValueTuple instance.

            Returns: This method always returns "()".
        """
        ...

# Error generating skeleton for function __eq__: 'type' object has no attribute '__bases__'

# Error generating skeleton for function __ge__: 'type' object has no attribute '__bases__'

# Error generating skeleton for function __gt__: 'type' object has no attribute '__bases__'

# Error generating skeleton for function __hash__: 'type' object has no attribute '__bases__'

# Error generating skeleton for function __le__: 'type' object has no attribute '__bases__'

# Error generating skeleton for function __lt__: 'type' object has no attribute '__bases__'

# Error generating skeleton for function __ne__: 'type' object has no attribute '__bases__'

# Error generating skeleton for function __reduce_ex__: 'type' object has no attribute '__bases__'

# Error generating skeleton for function __repr__: 'type' object has no attribute '__bases__'

# Error generating skeleton for function __str__: 'type' object has no attribute '__bases__'


class ValueType: # skipped bases: <type 'object'>
    """ Provides the base class for value types. """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class Version( ICloneable, IComparable, IEquatable):
    """
    Represents the version number of an assembly, operating system, or the common language runtime. This class cannot be inherited.

    Version(major: int, minor: int, build: int, revision: int)

    Version(major: int, minor: int, build: int)

    Version(major: int, minor: int)

    Version(version: str)

    Version()
    """
    @property
    def Build(self):
        """
        Gets the value of the build component of the version number for the current System.Version object.

        Get: Build(self: Version) -> int
        """
        ...

    @property
    def Major(self):
        """
        Gets the value of the major component of the version number for the current System.Version object.

        Get: Major(self: Version) -> int
        """
        ...

    @property
    def MajorRevision(self):
        """
        Gets the high 16 bits of the revision number.

        Get: MajorRevision(self: Version) -> Int16
        """
        ...

    @property
    def Minor(self):
        """
        Gets the value of the minor component of the version number for the current System.Version object.

        Get: Minor(self: Version) -> int
        """
        ...

    @property
    def MinorRevision(self):
        """
        Gets the low 16 bits of the revision number.

        Get: MinorRevision(self: Version) -> Int16
        """
        ...

    @property
    def Revision(self):
        """
        Gets the value of the revision component of the version number for the current System.Version object.

        Get: Revision(self: Version) -> int
        """
        ...


    def GetHashCode(self):
        """
        GetHashCode(self: Version) -> int

            Returns a hash code for the current System.Version object.

            Returns: A 32-bit signed integer hash code.
        """
        ...

    @staticmethod
    def Parse(input):
        """
        Parse(input: str) -> Version

            Converts the string representation of a version number to an equivalent System.Version object.

            input: A string that contains a version number to convert.

            Returns: An object that is equivalent to the version number specified in the input parameter.
        """
        ...

    def ToString(self, fieldCount=...):
        """
        ToString(self: Version) -> str

            Converts the value of the current System.Version object to its equivalent System.String representation.

            Returns: The System.String representation of the values of the major, minor, build, and revision components of the current System.Version object, as depicted

             in the following format. Each component is separated by a period character ('.'). Square brackets ('[' and ']') indicate a component that will not

             appear in the return value if the component is not defined: major.minor[.build[.revision]] For example, if you create a System.Version object using

             the constructor Version(1,1), the returned string is "1.1". If you create a System.Version object using the constructor Version(1,3,4,2), the

             returned string is "1.3.4.2".

        ToString(self: Version, fieldCount: int) -> str

            Converts the value of the current System.Version object to its equivalent System.String representation. A specified count indicates the number of

             components to return.

            fieldCount: The number of components to return. The fieldCount ranges from 0 to 4.

            Returns: The System.String representation of the values of the major, minor, build, and revision components of the current System.Version object, each

             separated by a period character ('.'). The fieldCount parameter determines how many components are returned.fieldCount Return Value 0 An empty string

             (""). 1 major 2 major.minor 3 major.minor.build 4 major.minor.build.revision For example, if you create System.Version object using the constructor

             Version(1,3,5), ToString(2) returns "1.3" and ToString(4) throws an exception.
        """
        ...

    @staticmethod
    def TryParse(input, result):
        """
        TryParse(input: str) -> (bool, Version)

            Tries to convert the string representation of a version number to an equivalent System.Version object, and returns a value that indicates whether the

             conversion succeeded.

            input: A string that contains a version number to convert.

            Returns: ue if the input parameter was converted successfully; otherwise, lse.
        """
        ...


class Void: # skipped bases: <type 'object'>
    """ Specifies a return value type for a method that does not return a value. """
    pass

class WeakReference:
    """
    Represents a weak reference, which references an object while still allowing that object to be reclaimed by garbage collection.

    WeakReference(target: object)

    WeakReference(target: object, trackResurrection: bool)
    """
    @property
    def IsAlive(self):
        """
        Gets an indication whether the object referenced by the current System.WeakReference object has been garbage collected.

        Get: IsAlive(self: WeakReference) -> bool
        """
        ...

    @property
    def Target(self):
        """
        Gets or sets the object (the target) referenced by the current System.WeakReference object.

        Get: Target(self: WeakReference) -> object

        Set: Target(self: WeakReference) = value
        """
        ...

    @property
    def TrackResurrection(self):
        """
        Gets an indication whether the object referenced by the current System.WeakReference object is tracked after it is finalized.

        Get: TrackResurrection(self: WeakReference) -> bool
        """
        ...


    def GetObjectData(self, info, context):
        """
        GetObjectData(self: WeakReference, info: SerializationInfo, context: StreamingContext)

            Populates a System.Runtime.Serialization.SerializationInfo object with all the data needed to serialize the current System.WeakReference object.

            info: An object that holds all the data needed to serialize or deserialize the current System.WeakReference object.

            context: (Reserved) The location where serialized data is stored and retrieved.
        """
        ...

    @staticmethod # known case of __new__
    def __new__(cls, target, trackResurrection=...):
        """
        __new__(cls: type, target: object)

        __new__(cls: type, target: object, trackResurrection: bool)

        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        ...

# Error generating skeleton for function __reduce_ex__: 'type' object has no attribute '__bases__'

# Error generating skeleton for function __repr__: 'type' object has no attribute '__bases__'


# variables with complex values
