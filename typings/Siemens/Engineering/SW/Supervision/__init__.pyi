# encoding: utf-8
# module Siemens.Engineering.SW.Supervision calls itself Supervision
# from Siemens.Engineering, Version=17.0.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class SupervisionProvider(object, IEngineeringObject, IEngineeringService, IInternalObjectAccess, IEquatable[object]): # skipped bases: <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEngineeringCompositionOrObject'>
    """ prodiag global supervision provider of proDiagFB """
    @property
    def Parent(self):
        """
        EOM parent of this object
        Get: Parent(self: SupervisionProvider) -> IEngineeringObject
        """
        ...


    def ExportSupervisionsToXlsx(self, path):
        """
        ExportSupervisionsToXlsx(self: SupervisionProvider, path: FileInfo) -> SupervisionXlsxResult
            Export of prodiag global supervisions to xlsx file
            path: path for exported prodiag global supervisions
            Returns: Siemens.Engineering.SW.Supervision.SupervisionXlsxResult
        """
        ...

    def GetHashCode(self):
        """
        GetHashCode(self: SupervisionProvider) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ImportSupervisionSettingsFromXlsx(self, path, importOptions):
        """
        ImportSupervisionSettingsFromXlsx(self: SupervisionProvider, path: FileInfo, importOptions: ImportOptions) -> SupervisionXlsxResult
            Import of prodiag settings from xlsx file
            path: path of xlsx file
            importOptions: option to select type of import
            Returns: Siemens.Engineering.SW.Supervision.SupervisionXlsxResult
        """
        ...

    def ImportSupervisionsFromXlsx(self, path, importOptions):
        """
        ImportSupervisionsFromXlsx(self: SupervisionProvider, path: FileInfo, importOptions: ImportOptions) -> SupervisionXlsxResult
            Import of prodiag global supervisions from xlsx file
            path: path from where prodiag global supervisions gets imported
            importOptions: option to select type of import
            Returns: Siemens.Engineering.SW.Supervision.SupervisionXlsxResult
        """
        ...

    def ToString(self):
        """
        ToString(self: SupervisionProvider) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class SupervisionSettingsExportImportResult(object, IEngineeringObject, IInternalObjectAccess, IEquatable[object]): # skipped bases: <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEngineeringCompositionOrObject'>
    """ Represents supervision settings export/import final result. """
    @property
    def ErrorCount(self):
        """
        Error count after export/import of supervision settings
        Get: ErrorCount(self: SupervisionSettingsExportImportResult) -> int
        """
        ...

    @property
    def Messages(self):
        """
        List of supervision settings export/import messages
        Get: Messages(self: SupervisionSettingsExportImportResult) -> SupervisionSettingsExportImportResultMessageComposition
        """
        ...

    @property
    def Parent(self):
        """
        EOM parent of this object
        Get: Parent(self: SupervisionSettingsExportImportResult) -> IEngineeringObject
        """
        ...

    @property
    def State(self):
        """
        Final state of the supervision settings export/import result.
        Get: State(self: SupervisionSettingsExportImportResult) -> SupervisionSettingsExportImportResultState
        """
        ...

    @property
    def WarningCount(self):
        """
        Warning count after import of supervision settings
        Get: WarningCount(self: SupervisionSettingsExportImportResult) -> int
        """
        ...


    def GetHashCode(self):
        """
        GetHashCode(self: SupervisionSettingsExportImportResult) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self):
        """
        ToString(self: SupervisionSettingsExportImportResult) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class SupervisionSettingsExportImportResultMessage(object, IEngineeringObject, IInternalObjectAccess, IEquatable[object]): # skipped bases: <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEngineeringCompositionOrObject'>
    """ Represents supervision settings export/import final result message """
    @property
    def Message(self):
        """
        Final message text of supervision settings export/import result.
        Get: Message(self: SupervisionSettingsExportImportResultMessage) -> str
        """
        ...

    @property
    def Parent(self):
        """
        EOM parent of this object
        Get: Parent(self: SupervisionSettingsExportImportResultMessage) -> IEngineeringObject
        """
        ...


    def GetHashCode(self):
        """
        GetHashCode(self: SupervisionSettingsExportImportResultMessage) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self):
        """
        ToString(self: SupervisionSettingsExportImportResultMessage) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class SupervisionSettingsExportImportResultMessageComposition(object, IEngineeringComposition, IInternalCompositionAccess, IEnumerable[SupervisionSettingsExportImportResultMessage], IEquatable[object]): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEnumerable'>, <type 'IInternalBaseAccess'>, <type 'IInternalCollectionAccess'>, <type 'IEngineeringInstance'>, <type 'IEngineeringCompositionOrObject'>
    """ Composition of SupervisionSettingsExportImportResultMessage """
    @property
    def Parent(self):
        """
        Gets the parent.
        Get: Parent(self: SupervisionSettingsExportImportResultMessageComposition) -> IEngineeringObject
        """
        ...


    def GetHashCode(self):
        """
        GetHashCode(self: SupervisionSettingsExportImportResultMessageComposition) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self):
        """
        ToString(self: SupervisionSettingsExportImportResultMessageComposition) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[SupervisionSettingsExportImportResultMessage](enumerable: IEnumerable[SupervisionSettingsExportImportResultMessage], value: SupervisionSettingsExportImportResultMessage) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class SupervisionSettingsExportImportResultState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>
    """
    The state of supervision settings export/import result
    enum SupervisionSettingsExportImportResultState, values: ErrorRollback (1), Success (0)
    """
    ErrorRollback = None
    Success = None
    value__ = None


class SupervisionSettingsProvider(object, IEngineeringObject, IEngineeringService, IInternalObjectAccess, IEquatable[object]): # skipped bases: <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEngineeringCompositionOrObject'>
    """ Provider for supervision settings """
    @property
    def Parent(self):
        """
        EOM parent of this object
        Get: Parent(self: SupervisionSettingsProvider) -> IEngineeringObject
        """
        ...


    def Export(self, filePath):
        """
        Export(self: SupervisionSettingsProvider, filePath: FileInfo) -> SupervisionSettingsExportImportResult
            Exports supervision settings in DAT file format
            filePath: File path where file having .dat extension is exported
            Returns: Siemens.Engineering.SW.Supervision.SupervisionSettingsExportImportResult
        """
        ...

    def GetHashCode(self):
        """
        GetHashCode(self: SupervisionSettingsProvider) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def Import(self, filePath):
        """
        Import(self: SupervisionSettingsProvider, filePath: FileInfo) -> SupervisionSettingsExportImportResult
            Imports supervision settings from DAT file
            filePath: File path where file having .dat extension is imported
            Returns: Siemens.Engineering.SW.Supervision.SupervisionSettingsExportImportResult
        """
        ...

    def ToString(self):
        """
        ToString(self: SupervisionSettingsProvider) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class SupervisionXlsxResult(object, IEngineeringObject, IInternalObjectAccess, IEquatable[object]): # skipped bases: <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEngineeringCompositionOrObject'>
    """ Represents a supervision export or import result. """
    @property
    def LogFilePath(self):
        """
        Path to the log file.
        Get: LogFilePath(self: SupervisionXlsxResult) -> FileInfo
        """
        ...

    @property
    def Parent(self):
        """
        EOM parent of this object
        Get: Parent(self: SupervisionXlsxResult) -> IEngineeringObject
        """
        ...

    @property
    def State(self):
        """
        Final state of the supervision export or import result.
        Get: State(self: SupervisionXlsxResult) -> SupervisionXlsxResultState
        """
        ...


    def GetHashCode(self):
        """
        GetHashCode(self: SupervisionXlsxResult) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self):
        """
        ToString(self: SupervisionXlsxResult) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class SupervisionXlsxResultState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>
    """
    Supervision import/export result state
    enum SupervisionXlsxResultState, values: Failure (1), Success (0)
    """
    Failure = None
    Success = None
    value__ = None


