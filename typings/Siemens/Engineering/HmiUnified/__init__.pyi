# encoding: utf-8
# module Siemens.Engineering.HmiUnified calls itself HmiUnified
# from Siemens.Engineering, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

from Siemens.Engineering.HW import Software

class HmiSoftware(
    Software
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """Represents the software components of a Hmi"""

    @property
    def AlarmClasses(self):
        """
        AlarmClasses collection

        Get: AlarmClasses(self: HmiSoftware) -> HmiAlarmClassComposition
        """
        ...
    @property
    def AlarmLogs(self):
        """
        Specifies HmiAlarmLog collection

        Get: AlarmLogs(self: HmiSoftware) -> HmiAlarmLogComposition
        """
        ...
    @property
    def AnalogAlarms(self):
        """
        AnalogAlarm collection

        Get: AnalogAlarms(self: HmiSoftware) -> HmiAnalogAlarmComposition
        """
        ...
    @property
    def Connections(self):
        """
        HmiConnection Collection

        Get: Connections(self: HmiSoftware) -> HmiConnectionComposition
        """
        ...
    @property
    def DataLogs(self):
        """
        Specifies HmiDataLog collection

        Get: DataLogs(self: HmiSoftware) -> HmiDataLogComposition
        """
        ...
    @property
    def DiscreteAlarms(self):
        """
        DiscreteAlarms collection

        Get: DiscreteAlarms(self: HmiSoftware) -> HmiDiscreteAlarmComposition
        """
        ...
    @property
    def RuntimeSettings(self):
        """
        Runtime settings of the hmi device

        Get: RuntimeSettings(self: HmiSoftware) -> HmiRuntimeSetting
        """
        ...
    @property
    def SystemTags(self):
        """
        Hmi system tag collection

        Get: SystemTags(self: HmiSoftware) -> HmiSystemTagComposition
        """
        ...
    @property
    def Tags(self):
        """
        Hmi tag collection

        Get: Tags(self: HmiSoftware) -> HmiTagComposition
        """
        ...
    @property
    def TagTables(self):
        """
        Hmi tagtables

        Get: TagTables(self: HmiSoftware) -> HmiTagTableComposition
        """
        ...

# variables with complex values
