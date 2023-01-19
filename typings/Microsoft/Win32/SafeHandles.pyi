# encoding: utf-8
# module Microsoft.Win32.SafeHandles calls itself SafeHandles
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
# no doc
# no imports

# no functions
# classes

from System.Runtime.InteropServices import CriticalHandle, SafeHandle

class CriticalHandleMinusOneIsInvalid(CriticalHandle):  # skipped bases: <type 'IDisposable'>
    """Provides a base class for Win32 critical handle implementations in which the value of -1 indicates an invalid handle."""

    handle = None

class CriticalHandleZeroOrMinusOneIsInvalid(CriticalHandle):  # skipped bases: <type 'IDisposable'>
    """Provides a base class for Win32 critical handle implementations in which the value of either 0 or -1 indicates an invalid handle."""

    handle = None

class SafeAccessTokenHandle(SafeHandle):  # skipped bases: <type 'IDisposable'>
    """
    Provides a safe handle to a Windows thread or process access token. For more information see Access Tokens

    SafeAccessTokenHandle(handle: IntPtr)
    """

    @property
    def InvalidHandle(self):
        """
        Returns an invalid handle by instantiating a Microsoft.Win32.SafeHandles.SafeAccessTokenHandle object with System.IntPtr.Zero.

        Get: InvalidHandle() -> SafeAccessTokenHandle
        """
        ...
    handle = None

class SafeHandleZeroOrMinusOneIsInvalid(SafeHandle):  # skipped bases: <type 'IDisposable'>
    """Provides a base class for Win32 safe handle implementations in which the value of either 0 or -1 indicates an invalid handle."""

    handle = None

class SafeFileHandle(SafeHandleZeroOrMinusOneIsInvalid):  # skipped bases: <type 'IDisposable'>
    """
    Represents a wrapper class for a file handle.

    SafeFileHandle(preexistingHandle: IntPtr, ownsHandle: bool)
    """

    handle = None

class SafeHandleMinusOneIsInvalid(SafeHandle):  # skipped bases: <type 'IDisposable'>
    """Provides a base class for Win32 safe handle implementations in which the value of -1 indicates an invalid handle."""

    handle = None

class SafeProcessHandle(SafeHandleZeroOrMinusOneIsInvalid):  # skipped bases: <type 'IDisposable'>
    """
    Provides a managed wrapper for a process handle.

    SafeProcessHandle(existingHandle: IntPtr, ownsHandle: bool)
    """

    handle = None

class SafeRegistryHandle(SafeHandleZeroOrMinusOneIsInvalid):  # skipped bases: <type 'IDisposable'>
    """
    Represents a safe handle to the Windows registry.

    SafeRegistryHandle(preexistingHandle: IntPtr, ownsHandle: bool)
    """

    handle = None

class SafeWaitHandle(SafeHandleZeroOrMinusOneIsInvalid):  # skipped bases: <type 'IDisposable'>
    """
    Represents a wrapper class for a wait handle.

    SafeWaitHandle(existingHandle: IntPtr, ownsHandle: bool)
    """

    handle = None

class SafeX509ChainHandle(SafeHandleZeroOrMinusOneIsInvalid):  # skipped bases: <type 'IDisposable'>
    """Provides a wrapper class that represents the handle of an X.509 chain object. For more information, see System.Security.Cryptography.X509Certificates.X509Chain."""

    handle = None
