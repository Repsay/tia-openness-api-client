""" This module contains all exceptions used in the tia_portal package. The exceptions are just wrappers for the exceptions raised by the TIA Portal API. The exceptions are used to make the API more user-friendly. The exceptions are grouped by the module they are used in."""


class LibraryImportError(Exception):
    pass


class LibraryDLLNotFound(Exception):
    pass


class InvalidTIASession(Exception):
    pass


class ProjectAlreadyExists(Exception):
    pass


class ProjectNotFound(Exception):
    pass


class InvalidProject(Exception):
    pass


class InvalidDeviceComposition(Exception):
    pass


class InvalidDevice(Exception):
    pass


class InvalidDeviceItemComposition(Exception):
    pass


class InvalidDeviceItem(Exception):
    pass


class DeviceAlreadyExists(Exception):
    pass


class InvalidSoftwareType(Exception):
    pass


class InvalidSoftware(Exception):
    pass


class InvalidSystemBlockGroupComposition(Exception):
    pass


class InvalidSystemBlockGroup(Exception):
    pass


class InvalidUserBlockGroupComposition(Exception):
    pass


class InvalidUserBlockGroup(Exception):
    pass


class InvalidBlockComposition(Exception):
    pass


class InvalidBlockType(Exception):
    pass


class InvalidBlock(Exception):
    pass


class InvalidGlobalLibraryComposition(Exception):
    pass


class InvalidGlobalLibrary(Exception):
    pass


class InvalidTypeFolder(Exception):
    pass


class InvalidTypeUserFolderComposition(Exception):
    pass


class InvalidUserTypeFolder(Exception):
    pass


class InvalidTypeUserFolder(Exception):
    pass


class InvalidTypeComposition(Exception):
    pass


class InvalidMasterCopyFolder(Exception):
    pass


class InvalidMasterCopyUserFolderComposition(Exception):
    pass


class InvalidUserMasterCopyFolder(Exception):
    pass


class InvalidMasterCopyComposition(Exception):
    pass


class InvalidMasterCopy(Exception):
    pass


class InvalidPath(Exception):
    pass


class TIALibraryNotFound(Exception):
    pass


class TIAProjectNotFound(Exception):
    pass


class TIAProjectAlreadyExists(Exception):
    pass


class TIAInvalidProject(Exception):
    pass


class TIAProjectAlreadyOpen(Exception):
    pass


class TIAInvalidSession(Exception):
    pass


class TIADeviceNotFound(Exception):
    pass


class TIADeviceAlreadyExists(Exception):
    pass


class TIADeviceItemNotFound(Exception):
    pass


class TIAGroupNotFound(Exception):
    pass


class TIAInvalidProperty(Exception):
    pass


class TIABlockNotFound(Exception):
    pass


class TIAInconsistentBlock(Exception):
    pass


class TIAGlobalLibraryNotFound(Exception):
    pass
