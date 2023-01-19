# encoding: utf-8
# module System.Runtime calls itself Runtime
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AssemblyTargetedPatchBandAttribute(Attribute):  # skipped bases: <type '_Attribute'>
    """
    Specifies patch band information for targeted patching of the .NET Framework.

    AssemblyTargetedPatchBandAttribute(targetedPatchBand: str)
    """

    @staticmethod  # known case of __new__
    def __new__(cls, targetedPatchBand):
        """__new__(cls: type, targetedPatchBand: str)"""
        ...
    @property
    def TargetedPatchBand(self):
        """
        Gets the patch band.

        Get: TargetedPatchBand(self: AssemblyTargetedPatchBandAttribute) -> str
        """
        ...

class GCLargeObjectHeapCompactionMode(
    Enum
):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    [Supported in the .NET Framework 4.5.1 and later versions] Indicates whether the next blocking garbage collection compacts the large object heap (LOH).

    enum GCLargeObjectHeapCompactionMode, values: CompactOnce (2), Default (1)
    """

    CompactOnce = None
    Default = None
    value__ = None

class GCLatencyMode(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Adjusts the time that the garbage collector intrudes in your application.

    enum GCLatencyMode, values: Batch (0), Interactive (1), LowLatency (2), NoGCRegion (4), SustainedLowLatency (3)
    """

    Batch = None
    Interactive = None
    LowLatency = None
    NoGCRegion = None
    SustainedLowLatency = None
    value__ = None

class GCSettings:  # skipped bases: <type 'object'>
    """Specifies the garbage collection settings for the current process."""

    IsServerGC = False
    LargeObjectHeapCompactionMode = None
    LatencyMode = None
    __all__ = []

class MemoryFailPoint(CriticalFinalizerObject, IDisposable):
    """
    Checks for sufficient memory resources before executing an operation. This class cannot be inherited.

    MemoryFailPoint(sizeInMegabytes: int)
    """

    @staticmethod  # known case of __new__
    def __new__(cls, sizeInMegabytes):
        """__new__(cls: type, sizeInMegabytes: int)"""
        ...

class ProfileOptimization:  # skipped bases: <type 'object'>
    """Improves the startup performance of application domains in applications that require the just-in-time (JIT) compiler by performing background compilation of methods that are likely to be executed, based on profiles created during previous compilations."""

    @staticmethod
    def SetProfileRoot(directoryPath):
        """
        SetProfileRoot(directoryPath: str)

            Enables optimization profiling for the current application domain, and sets the folder where the optimization profile files are stored. On a single-core computer, the

             method is ignored.

            directoryPath: The full path to the folder where profile files are stored for the current application domain.
        """
        ...
    @staticmethod
    def StartProfile(profile):
        """
        StartProfile(profile: str)

            Starts just-in-time (JIT) compilation of the methods that were previously recorded in the specified profile file, on a background thread. Starts the process of

             recording current method use, which later overwrites the specified profile file.

            profile: The file name of the profile to use.
        """
        ...
    __all__ = [
        "SetProfileRoot",
        "StartProfile",
    ]

class TargetedPatchingOptOutAttribute(Attribute):  # skipped bases: <type '_Attribute'>
    """
    Indicates that the .NET Framework class library method to which this attribute is applied is unlikely to be affected by servicing releases, and therefore is eligible to be inlined across Native Image Generator (NGen) images.

    TargetedPatchingOptOutAttribute(reason: str)
    """

    @staticmethod  # known case of __new__
    def __new__(cls, reason):
        """__new__(cls: type, reason: str)"""
        ...
    @property
    def Reason(self):
        """
        Gets the reason why the method to which this attribute is applied is considered to be eligible for inlining across Native Image Generator (NGen) images.

        Get: Reason(self: TargetedPatchingOptOutAttribute) -> str
        """
        ...

# variables with complex values
