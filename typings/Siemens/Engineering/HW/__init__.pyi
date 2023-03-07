# encoding: utf-8
# module Siemens.Engineering.HW calls itself HW
# from Siemens.Engineering, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

from typing import Optional
from Siemens.Engineering import (
    IEngineeringAssociation,
    IEngineeringComposition,
    IEngineeringObject,
    IEngineeringServiceProvider,
)
from Siemens.Engineering.Library.MasterCopies import IMasterCopySource, IMasterCopyTarget
from System import Enum, IEquatable

class Address(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """The object holding the address data"""

    @property
    def AddressControllers(self):
        """
        Address's associated AddressControllers

        Get: AddressControllers(self: Address) -> AddressControllerAssociation
        """
        ...
    @property
    def IoType(self):
        """
        The IO type of the address

        Get: IoType(self: Address) -> AddressIoType
        """
        ...
    @property
    def Length(self):
        """
        Length of the address

        Get: Length(self: Address) -> int

        Set: Length(self: Address) = value
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: Address) -> IEngineeringObject
        """
        ...
    @property
    def StartAddress(self):
        """
        The start address of this address

        Get: StartAddress(self: Address) -> int

        Set: StartAddress(self: Address) = value
        """
        ...
    def AssignProcessImageToOrganizationBlock(self, organizationBlock):
        """
        AssignProcessImageToOrganizationBlock(self: Address, organizationBlock: OB)

            Assign the current process image to the OB.

            organizationBlock: The organizational block to assign.
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: Address) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: Address) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class AddressAssociation(
    IEngineeringAssociation, IInternalAssociationAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalCollectionAccess'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>
    """Associated addresses"""

    @property
    def Parent(self):
        """
        Gets the parent..

        Get: Parent(self: AddressAssociation) -> IEngineeringObject
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: AddressAssociation) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: AddressAssociation) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[Address](enumerable:  value: Address) -> bool"""
        ...
    def __ne__(self, *args): ...

class AddressComposition(
    IEngineeringComposition, IInternalCompositionAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """Composition of Addresses"""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: AddressComposition) -> IEngineeringObject
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: AddressComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: AddressComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[Address](enumerable:  value: Address) -> bool"""
        ...
    def __ne__(self, *args): ...

class AddressContext(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    AddressContext of an address

    enum AddressContext, values: Device (1), Head (2), None (0)
    """

    Device = None
    Head = None
    value__ = None

class AddressIoType(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Address IO type

    enum AddressIoType, values: Diagnosis (64), Input (1), None (0), Output (2), Substitute (16)
    """

    Diagnosis = None
    Input = None
    Output = None
    Substitute = None
    value__ = None

class ApplicationControlFunction(
    Enum
):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Possible values for property ApplicationControlFunction

    enum ApplicationControlFunction, values: DahlanderReversingStarter (49), DahlanderStarter (48), DirectStarter (16), MoldedCaseCircuitBreaker (18), OverloadRelay (0), PoleChangingReversingStarter (65), PoleChangingStarter (64), Positioner1 (96), Positioner2 (97), Positioner3 (98), Positioner4 (99), Positioner5 (100), ReversingStarter (17), SoftStarter (112), SoftStarterWithReversingContactor (113), SolenoidValve (80), StarDeltaReversingStarter (33), StarDeltaStarter (32)
    """

    DahlanderReversingStarter = None
    DahlanderStarter = None
    DirectStarter = None
    MoldedCaseCircuitBreaker = None
    OverloadRelay = None
    PoleChangingReversingStarter = None
    PoleChangingStarter = None
    Positioner1 = None
    Positioner2 = None
    Positioner3 = None
    Positioner4 = None
    Positioner5 = None
    ReversingStarter = None
    SoftStarter = None
    SoftStarterWithReversingContactor = None
    SolenoidValve = None
    StarDeltaReversingStarter = None
    StarDeltaStarter = None
    value__ = None

class BasicType(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Possible values for property BasicType

    enum BasicType, values: None (0), Value1 (1), Value2 (2), Value3 (3)
    """

    Value1 = None
    Value2 = None
    Value3 = None
    value__ = None

class BaudRate(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Devices baud rate

    enum BaudRate, values: Baud12000000 (10), Baud1500000 (7), Baud187500 (5), Baud19200 (2), Baud3000000 (8), Baud45450 (3), Baud500000 (6), Baud6000000 (9), Baud93750 (4), Baud9600 (1), None (0)
    """

    Baud12000000 = None
    Baud1500000 = None
    Baud187500 = None
    Baud19200 = None
    Baud3000000 = None
    Baud45450 = None
    Baud500000 = None
    Baud6000000 = None
    Baud93750 = None
    Baud9600 = None
    value__ = None

class BusProfile(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    BusProfile

    enum BusProfile, values: Dp (1), None (0), Standard (2), Universal (3), UserDefined (4)
    """

    Dp = None
    Standard = None
    Universal = None
    UserDefined = None
    value__ = None

class CableLength(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Possible values for property CableLength

    enum CableLength, values: Length1000m (6000), Length100m (600), Length20m (120), Length3000m (18000), Length50m (300), None (0)
    """

    Length1000m = None
    Length100m = None
    Length20m = None
    Length3000m = None
    Length50m = None
    value__ = None

class CableName(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Cable Name

    enum CableName, values: Flexible_FO_Cable_62_5 (12884901890), Flexible_FO_Cable_9 (4294967298), FO_Ground_Cable (8589934595), FO_Standard_Cable_62_5 (12884901889), FO_Standard_Cable_9 (4294967297), FO_Standard_Cable_GP_50 (8589934593), FO_Trailing_Cable_GP (8589934594), GI_PCF_Standard_Cable (34359738369), GI_PCF_Trailing_Cable (34359738370), GI_POF_Standard_Cable (30064771073), GI_POF_Trailing_Cable (30064771074), None (0), PCF_Standard_Cable_GP (21474836481), PCF_Trailing_Cable_GP (21474836482), POF_Standard_Cable_GP (17179869185), POF_Trailing_Cable (17179869186)
    """

    Flexible_FO_Cable_62_5 = None
    Flexible_FO_Cable_9 = None
    FO_Ground_Cable = None
    FO_Standard_Cable_62_5 = None
    FO_Standard_Cable_9 = None
    FO_Standard_Cable_GP_50 = None
    FO_Trailing_Cable_GP = None
    GI_PCF_Standard_Cable = None
    GI_PCF_Trailing_Cable = None
    GI_POF_Standard_Cable = None
    GI_POF_Trailing_Cable = None
    PCF_Standard_Cable_GP = None
    PCF_Trailing_Cable_GP = None
    POF_Standard_Cable_GP = None
    POF_Trailing_Cable = None
    value__ = None

class Channel(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Class representing a channel"""

    @property
    def IoType(self):
        """
        The IO type of the channel

        Get: IoType(self: Channel) -> ChannelIoType
        """
        ...
    @property
    def Number(self):
        """
        The number of this channel

        Get: Number(self: Channel) -> int
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: Channel) -> IEngineeringObject
        """
        ...
    @property
    def Type(self):
        """
        The type of this channel

        Get: Type(self: Channel) -> ChannelType
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: Channel) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: Channel) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class ChannelComposition(
    IEngineeringComposition, IInternalCompositionAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """Composition of Channels"""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: ChannelComposition) -> IEngineeringObject
        """
        ...
    def Find(self, type, ioType, number):
        """
        Find(self: ChannelComposition, type: ChannelType, ioType: ChannelIoType, number: int) -> Channel

            Finds a given channel

            type: Type to find

            ioType: IoType to find

            number: Number to find

            Returns: Siemens.Engineering.HW.Channel
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: ChannelComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: ChannelComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[Channel](enumerable:  value: Channel) -> bool"""
        ...
    def __ne__(self, *args): ...

class ChannelIoType(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Channel IO type

    enum ChannelIoType, values: Complex (3), Input (1), None (0), Output (2)
    """

    Complex = None
    Input = None
    Output = None
    value__ = None

class ChannelType(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Channel type

    enum ChannelType, values: Analog (1), Digital (2), None (0), Technology (3)
    """

    Analog = None
    Digital = None
    Technology = None
    value__ = None

class Classification(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Possible values for property Classification

    enum Classification, values: CPU (1), HM (2), None (0)
    """

    CPU = None
    HM = None
    value__ = None

class CommunicationLoad(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Profibus Communication Load

    enum CommunicationLoad, values: High (3), Low (1), Medium (2), None (0)
    """

    High = None
    Low = None
    Medium = None
    value__ = None

class ConfigurationDQOrDIGroup2(
    Enum
):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Possible values for property ConfigurationDQOrDIGroup2

    enum ConfigurationDQOrDIGroup2, values: IncrementalEncoderABPhaseShifted (2), TimerDi2WithEnableInputDi3 (1), TimerDq2WithEnableInputDi2 (3), TimerDqWithEnableInput (4), UseInputOrOutputIndividually (0)
    """

    IncrementalEncoderABPhaseShifted = None
    TimerDi2WithEnableInputDi3 = None
    TimerDq2WithEnableInputDi2 = None
    TimerDqWithEnableInput = None
    UseInputOrOutputIndividually = None
    value__ = None

class ControlFunctionCurrentMeasuringModuleInstalled(
    Enum
):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Possible values for property ControlFunctionCurrentMeasuringModuleInstalled

    enum ControlFunctionCurrentMeasuringModuleInstalled, values: Delta (0), IncomingCable (1)
    """

    Delta = None
    IncomingCable = None
    value__ = None

class ControlFunctionFeedbackCLOSEDFC(
    Enum
):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Possible values for property ControlFunctionFeedbackCLOSEDFC

    enum ControlFunctionFeedbackCLOSEDFC, values: AcyclicReceiveBit00 (40), AcyclicReceiveBit01 (41), AcyclicReceiveBit02 (42), AcyclicReceiveBit03 (43), AcyclicReceiveBit04 (44), AcyclicReceiveBit05 (45), AcyclicReceiveBit06 (46), AcyclicReceiveBit07 (47), AcyclicReceiveBit10 (48), AcyclicReceiveBit11 (49), AcyclicReceiveBit12 (50), AcyclicReceiveBit13 (51), AcyclicReceiveBit14 (52), AcyclicReceiveBit15 (53), AcyclicReceiveBit16 (54), AcyclicReceiveBit17 (55), BUInput1 (9), BUInput2 (10), BUInput3 (11), BUInput4 (12), BUTestResetButton (8), ContactorControl1QE1 (80), ContactorControl2QE2 (81), ContactorControl3QE3 (82), ContactorControl4QE4 (83), ContactorControl5QE5 (84), Counter1Output (236), Counter2Output (237), Counter3Output (238), Counter4Output (239), Counter5Output (228), Counter6Output (229), CyclicReceiveBit00 (56), CyclicReceiveBit01 (57), CyclicReceiveBit02 (58), CyclicReceiveBit03 (59), CyclicReceiveBit04 (60), CyclicReceiveBit05 (61), CyclicReceiveBit06 (62), CyclicReceiveBit07 (63), CyclicReceiveBit10 (64), CyclicReceiveBit11 (65), CyclicReceiveBit12 (66), CyclicReceiveBit13 (67), CyclicReceiveBit14 (68), CyclicReceiveBit15 (69), CyclicReceiveBit16 (70), CyclicReceiveBit17 (71), DisplayQLAOff (90), DisplayQLEForward (91), DisplayQLEForwardFast (92), DisplayQLEReverse (89), DisplayQLEReverseFast (88), DisplayQLSFault (93), DM1Input1 (16), DM1Input2 (17), DM1Input3 (18), DM1Input4 (19), DM1SensorChannel1 (24), DM1SensorChannel2 (25), DM2Input1 (20), DM2Input2 (21), DM2Input3 (22), DM2Input4 (23), EnabledControlCommandOff (74), EnabledControlCommandOnForward (75), EnabledControlCommandOnForwardFast (76), EnabledControlCommandOnReverse (73), EnabledControlCommandOnReverseFast (72), EventAM1OpenCircuit (180), EventAM1TripLevel0420mAGt (158), EventAM1TripLevel0420mALt (159), EventAM1WarningLevel0420mAGt (150), EventAM1WarningLevel0420mALt (151), EventAM2OpenCircuit (179), EventAM2TripLevel0420mAGt (6), EventAM2TripLevel0420mALt (7), EventAM2WarningLevel0420mAGt (4), EventAM2WarningLevel0420mALt (5), EventConfiguredOperatorPanelMissing (188), EventDMFLOCALOk (186), EventExternalFault1 (172), EventExternalFault2 (173), EventExternalFault3 (174), EventExternalFault4 (175), EventExternalFault5 (176), EventExternalFault6 (177), EventExternalGroundFault (133), EventExternalGroundFaultWarning (134), EventInternalGroundFault (132), EventJustOneStartPossible (165), EventLimitMonitor1 (168), EventLimitMonitor2 (169), EventLimitMonitor3 (170), EventLimitMonitor4 (171), EventLimitMonitor5 (38), EventLimitMonitor6 (39), EventMonitoringPeriodForMandatoryTestingTestRequirement (182), EventMotorOperatingHoursGt (166), EventNoStartPermitted (163), EventNumberOfStartsGt (164), EventOverload (130), EventOverloadAndPhaseFailure (131), EventPrewarningOverload (128), EventPROFIsafeActive (187), EventSafetyrelatedTripping (181), EventStalledRotor (160), EventStopTimeGt (167), EventThermistorOpenCircuit (137), EventThermistorShortCircuit (136), EventThermistorTripLevel (135), EventTimestampfctActiveAndOk (184), EventTM1OutOfRange (141), EventTM1SensorFault (140), EventTM1TripLevelTGt (139), EventTM1WarningLevelTGt (138), EventTM2OutOfRange (29), EventTM2SensorFault (28), EventTM2TripLevelTGt (31), EventTM2WarningLevelTGt (30), EventTripLevelCosPhiLt (156), EventTripLevelIGt (152), EventTripLevelILt (153), EventTripLevelPGt (154), EventTripLevelPLt (155), EventTripLevelULt (157), EventUnbalance (129), EventWarningLevelCosPhiLt (148), EventWarningLevelIGt (144), EventWarningLevelILt (145), EventWarningLevelPGt (146), EventWarningLevelPLt (147), EventWarningLevelULt (149), FaultAntivalence (208), FaultBus (197), FaultConfigurationError (195), FaultDouble0 (205), FaultDouble1 (206), FaultEndPosition (207), FaultExecutionOnCommand (200), FaultExecutionSTOPCommand (201), FaultFeedbackOff (203), FaultFeedbackOn (202), FaultHardwareFaultBasicUnit (192), FaultModuleFault (193), FaultOperationalProtectionOff (211), FaultParameterization (196), FaultPLCPCS (198), FaultPowerFailure (210), FaultStalledPositioner (204), FaultTemporaryComponents (194), FaultTestPositionFeedback (209), FixedLevel0 (1), FixedLevel1 (2), Flashing1Output (248), Flashing2Output (249), Flashing3Output (250), Flicker1Output (251), Flicker2Output (252), Flicker3Output (253), NonvolatileElement1Output (244), NonvolatileElement2Output (245), NonvolatileElement3Output (246), NonvolatileElement4Output (247), NotConnected (0), OPButton1 (33), OPButton2 (34), OPButton3 (35), OPButton4 (36), OPTestResetButton (32), PWMOutput (254), SignalConditioning1Output (240), SignalConditioning2Output (241), SignalConditioning3Output (242), SignalConditioning4Output (243), SignalConditioning5Output (214), SignalConditioning6Output (215), StatusBusOk (99), StatusChangeoverPauseActive (111), StatusCoolingDownPeriodActive (122), StatusCurrentFlowing (101), StatusDeviceOk (98), StatusDeviceTestActive (124), StatusEmergencyStartExecuted (121), StatusEnablingCircuitClosed (127), StatusFeedbackCLOSED (114), StatusFeedbackOPEN (115), StatusGroupFault (96), StatusGroupWarning (97), StatusInterlockingTimeActive (110), StatusOff (106), StatusOnForward (107), StatusOnForwardFast (108), StatusOnReverse (105), StatusOnReverseFast (104), StatusOperationalProtectionOff (119), StatusPauseTimeActive (123), StatusPhaseSequence123 (125), StatusPhaseSequence321 (126), StatusPLCPCSInRun (100), StatusPositionerRunsInCLOSEDDirection (113), StatusPositionerRunsInOPENDirection (112), StatusPROFIenergyCommandStartPausePending (102), StatusRemoteMode (120), StatusStartActive (109), StatusTestPosition (118), StatusTorqueCLOSED (116), StatusTorqueOPEN (117), Timer1Output (232), Timer2Output (233), Timer3Output (234), Timer4Output (235), Timer5Output (230), Timer6Output (231), TruthTable10Output (226), TruthTable11Output (227), TruthTable1Output (216), TruthTable2Output (217), TruthTable3Output (218), TruthTable4Output (219), TruthTable5Output (220), TruthTable6Output (221), TruthTable7Output (222), TruthTable8Output (223), TruthTable9Output1 (224), TruthTable9Output2 (225), WarningFeedbackCircuit (190), WarningSimultaneity (191)
    """

    AcyclicReceiveBit00 = None
    AcyclicReceiveBit01 = None
    AcyclicReceiveBit02 = None
    AcyclicReceiveBit03 = None
    AcyclicReceiveBit04 = None
    AcyclicReceiveBit05 = None
    AcyclicReceiveBit06 = None
    AcyclicReceiveBit07 = None
    AcyclicReceiveBit10 = None
    AcyclicReceiveBit11 = None
    AcyclicReceiveBit12 = None
    AcyclicReceiveBit13 = None
    AcyclicReceiveBit14 = None
    AcyclicReceiveBit15 = None
    AcyclicReceiveBit16 = None
    AcyclicReceiveBit17 = None
    BUInput1 = None
    BUInput2 = None
    BUInput3 = None
    BUInput4 = None
    BUTestResetButton = None
    ContactorControl1QE1 = None
    ContactorControl2QE2 = None
    ContactorControl3QE3 = None
    ContactorControl4QE4 = None
    ContactorControl5QE5 = None
    Counter1Output = None
    Counter2Output = None
    Counter3Output = None
    Counter4Output = None
    Counter5Output = None
    Counter6Output = None
    CyclicReceiveBit00 = None
    CyclicReceiveBit01 = None
    CyclicReceiveBit02 = None
    CyclicReceiveBit03 = None
    CyclicReceiveBit04 = None
    CyclicReceiveBit05 = None
    CyclicReceiveBit06 = None
    CyclicReceiveBit07 = None
    CyclicReceiveBit10 = None
    CyclicReceiveBit11 = None
    CyclicReceiveBit12 = None
    CyclicReceiveBit13 = None
    CyclicReceiveBit14 = None
    CyclicReceiveBit15 = None
    CyclicReceiveBit16 = None
    CyclicReceiveBit17 = None
    DisplayQLAOff = None
    DisplayQLEForward = None
    DisplayQLEForwardFast = None
    DisplayQLEReverse = None
    DisplayQLEReverseFast = None
    DisplayQLSFault = None
    DM1Input1 = None
    DM1Input2 = None
    DM1Input3 = None
    DM1Input4 = None
    DM1SensorChannel1 = None
    DM1SensorChannel2 = None
    DM2Input1 = None
    DM2Input2 = None
    DM2Input3 = None
    DM2Input4 = None
    EnabledControlCommandOff = None
    EnabledControlCommandOnForward = None
    EnabledControlCommandOnForwardFast = None
    EnabledControlCommandOnReverse = None
    EnabledControlCommandOnReverseFast = None
    EventAM1OpenCircuit = None
    EventAM1TripLevel0420mAGt = None
    EventAM1TripLevel0420mALt = None
    EventAM1WarningLevel0420mAGt = None
    EventAM1WarningLevel0420mALt = None
    EventAM2OpenCircuit = None
    EventAM2TripLevel0420mAGt = None
    EventAM2TripLevel0420mALt = None
    EventAM2WarningLevel0420mAGt = None
    EventAM2WarningLevel0420mALt = None
    EventConfiguredOperatorPanelMissing = None
    EventDMFLOCALOk = None
    EventExternalFault1 = None
    EventExternalFault2 = None
    EventExternalFault3 = None
    EventExternalFault4 = None
    EventExternalFault5 = None
    EventExternalFault6 = None
    EventExternalGroundFault = None
    EventExternalGroundFaultWarning = None
    EventInternalGroundFault = None
    EventJustOneStartPossible = None
    EventLimitMonitor1 = None
    EventLimitMonitor2 = None
    EventLimitMonitor3 = None
    EventLimitMonitor4 = None
    EventLimitMonitor5 = None
    EventLimitMonitor6 = None
    EventMonitoringPeriodForMandatoryTestingTestRequirement = None
    EventMotorOperatingHoursGt = None
    EventNoStartPermitted = None
    EventNumberOfStartsGt = None
    EventOverload = None
    EventOverloadAndPhaseFailure = None
    EventPrewarningOverload = None
    EventPROFIsafeActive = None
    EventSafetyrelatedTripping = None
    EventStalledRotor = None
    EventStopTimeGt = None
    EventThermistorOpenCircuit = None
    EventThermistorShortCircuit = None
    EventThermistorTripLevel = None
    EventTimestampfctActiveAndOk = None
    EventTM1OutOfRange = None
    EventTM1SensorFault = None
    EventTM1TripLevelTGt = None
    EventTM1WarningLevelTGt = None
    EventTM2OutOfRange = None
    EventTM2SensorFault = None
    EventTM2TripLevelTGt = None
    EventTM2WarningLevelTGt = None
    EventTripLevelCosPhiLt = None
    EventTripLevelIGt = None
    EventTripLevelILt = None
    EventTripLevelPGt = None
    EventTripLevelPLt = None
    EventTripLevelULt = None
    EventUnbalance = None
    EventWarningLevelCosPhiLt = None
    EventWarningLevelIGt = None
    EventWarningLevelILt = None
    EventWarningLevelPGt = None
    EventWarningLevelPLt = None
    EventWarningLevelULt = None
    FaultAntivalence = None
    FaultBus = None
    FaultConfigurationError = None
    FaultDouble0 = None
    FaultDouble1 = None
    FaultEndPosition = None
    FaultExecutionOnCommand = None
    FaultExecutionSTOPCommand = None
    FaultFeedbackOff = None
    FaultFeedbackOn = None
    FaultHardwareFaultBasicUnit = None
    FaultModuleFault = None
    FaultOperationalProtectionOff = None
    FaultParameterization = None
    FaultPLCPCS = None
    FaultPowerFailure = None
    FaultStalledPositioner = None
    FaultTemporaryComponents = None
    FaultTestPositionFeedback = None
    FixedLevel0 = None
    FixedLevel1 = None
    Flashing1Output = None
    Flashing2Output = None
    Flashing3Output = None
    Flicker1Output = None
    Flicker2Output = None
    Flicker3Output = None
    NonvolatileElement1Output = None
    NonvolatileElement2Output = None
    NonvolatileElement3Output = None
    NonvolatileElement4Output = None
    NotConnected = None
    OPButton1 = None
    OPButton2 = None
    OPButton3 = None
    OPButton4 = None
    OPTestResetButton = None
    PWMOutput = None
    SignalConditioning1Output = None
    SignalConditioning2Output = None
    SignalConditioning3Output = None
    SignalConditioning4Output = None
    SignalConditioning5Output = None
    SignalConditioning6Output = None
    StatusBusOk = None
    StatusChangeoverPauseActive = None
    StatusCoolingDownPeriodActive = None
    StatusCurrentFlowing = None
    StatusDeviceOk = None
    StatusDeviceTestActive = None
    StatusEmergencyStartExecuted = None
    StatusEnablingCircuitClosed = None
    StatusFeedbackCLOSED = None
    StatusFeedbackOPEN = None
    StatusGroupFault = None
    StatusGroupWarning = None
    StatusInterlockingTimeActive = None
    StatusOff = None
    StatusOnForward = None
    StatusOnForwardFast = None
    StatusOnReverse = None
    StatusOnReverseFast = None
    StatusOperationalProtectionOff = None
    StatusPauseTimeActive = None
    StatusPhaseSequence123 = None
    StatusPhaseSequence321 = None
    StatusPLCPCSInRun = None
    StatusPositionerRunsInCLOSEDDirection = None
    StatusPositionerRunsInOPENDirection = None
    StatusPROFIenergyCommandStartPausePending = None
    StatusRemoteMode = None
    StatusStartActive = None
    StatusTestPosition = None
    StatusTorqueCLOSED = None
    StatusTorqueOPEN = None
    Timer1Output = None
    Timer2Output = None
    Timer3Output = None
    Timer4Output = None
    Timer5Output = None
    Timer6Output = None
    TruthTable10Output = None
    TruthTable11Output = None
    TruthTable1Output = None
    TruthTable2Output = None
    TruthTable3Output = None
    TruthTable4Output = None
    TruthTable5Output = None
    TruthTable6Output = None
    TruthTable7Output = None
    TruthTable8Output = None
    TruthTable9Output1 = None
    TruthTable9Output2 = None
    value__ = None
    WarningFeedbackCircuit = None
    WarningSimultaneity = None

class ControlFunctionFeedbackON(
    Enum
):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Possible values for property ControlFunctionFeedbackON

    enum ControlFunctionFeedbackON, values: AcyclicReceiveBit00 (40), AcyclicReceiveBit01 (41), AcyclicReceiveBit02 (42), AcyclicReceiveBit03 (43), AcyclicReceiveBit04 (44), AcyclicReceiveBit05 (45), AcyclicReceiveBit06 (46), AcyclicReceiveBit07 (47), AcyclicReceiveBit10 (48), AcyclicReceiveBit11 (49), AcyclicReceiveBit12 (50), AcyclicReceiveBit13 (51), AcyclicReceiveBit14 (52), AcyclicReceiveBit15 (53), AcyclicReceiveBit16 (54), AcyclicReceiveBit17 (55), BUInput1 (9), BUInput2 (10), BUInput3 (11), BUInput4 (12), BUTestResetButton (8), ContactorControl1QE1 (80), ContactorControl2QE2 (81), ContactorControl3QE3 (82), ContactorControl4QE4 (83), ContactorControl5QE5 (84), Counter1Output (236), Counter2Output (237), Counter3Output (238), Counter4Output (239), Counter5Output (228), Counter6Output (229), CyclicReceiveBit00 (56), CyclicReceiveBit01 (57), CyclicReceiveBit02 (58), CyclicReceiveBit03 (59), CyclicReceiveBit04 (60), CyclicReceiveBit05 (61), CyclicReceiveBit06 (62), CyclicReceiveBit07 (63), CyclicReceiveBit10 (64), CyclicReceiveBit11 (65), CyclicReceiveBit12 (66), CyclicReceiveBit13 (67), CyclicReceiveBit14 (68), CyclicReceiveBit15 (69), CyclicReceiveBit16 (70), CyclicReceiveBit17 (71), DisplayQLAOff (90), DisplayQLEForward (91), DisplayQLEForwardFast (92), DisplayQLEReverse (89), DisplayQLEReverseFast (88), DisplayQLSFault (93), DM1Input1 (16), DM1Input2 (17), DM1Input3 (18), DM1Input4 (19), DM1SensorChannel1 (24), DM1SensorChannel2 (25), DM2Input1 (20), DM2Input2 (21), DM2Input3 (22), DM2Input4 (23), EnabledControlCommandOff (74), EnabledControlCommandOnForward (75), EnabledControlCommandOnForwardFast (76), EnabledControlCommandOnReverse (73), EnabledControlCommandOnReverseFast (72), EventAM1OpenCircuit (180), EventAM1TripLevel0420mAGt (158), EventAM1TripLevel0420mALt (159), EventAM1WarningLevel0420mAGt (150), EventAM1WarningLevel0420mALt (151), EventAM2OpenCircuit (179), EventAM2TripLevel0420mAGt (6), EventAM2TripLevel0420mALt (7), EventAM2WarningLevel0420mAGt (4), EventAM2WarningLevel0420mALt (5), EventConfiguredOperatorPanelMissing (188), EventDMFLOCALOk (186), EventExternalFault1 (172), EventExternalFault2 (173), EventExternalFault3 (174), EventExternalFault4 (175), EventExternalFault5 (176), EventExternalFault6 (177), EventExternalGroundFault (133), EventExternalGroundFaultWarning (134), EventInternalGroundFault (132), EventJustOneStartPossible (165), EventLimitMonitor1 (168), EventLimitMonitor2 (169), EventLimitMonitor3 (170), EventLimitMonitor4 (171), EventLimitMonitor5 (38), EventLimitMonitor6 (39), EventMonitoringPeriodForMandatoryTestingTestRequirement (182), EventMotorOperatingHoursGt (166), EventNoStartPermitted (163), EventNumberOfStartsGt (164), EventOverload (130), EventOverloadAndPhaseFailure (131), EventPrewarningOverload (128), EventPROFIsafeActive (187), EventSafetyrelatedTripping (181), EventStalledRotor (160), EventStopTimeGt (167), EventThermistorOpenCircuit (137), EventThermistorShortCircuit (136), EventThermistorTripLevel (135), EventTimestampfctActiveAndOk (184), EventTM1OutOfRange (141), EventTM1SensorFault (140), EventTM1TripLevelTGt (139), EventTM1WarningLevelTGt (138), EventTM2OutOfRange (29), EventTM2SensorFault (28), EventTM2TripLevelTGt (31), EventTM2WarningLevelTGt (30), EventTripLevelCosPhiLt (156), EventTripLevelIGt (152), EventTripLevelILt (153), EventTripLevelPGt (154), EventTripLevelPLt (155), EventTripLevelULt (157), EventUnbalance (129), EventWarningLevelCosPhiLt (148), EventWarningLevelIGt (144), EventWarningLevelILt (145), EventWarningLevelPGt (146), EventWarningLevelPLt (147), EventWarningLevelULt (149), FaultAntivalence (208), FaultBus (197), FaultConfigurationError (195), FaultDouble0 (205), FaultDouble1 (206), FaultEndPosition (207), FaultExecutionOnCommand (200), FaultExecutionSTOPCommand (201), FaultFeedbackOff (203), FaultFeedbackOn (202), FaultHardwareFaultBasicUnit (192), FaultModuleFault (193), FaultOperationalProtectionOff (211), FaultParameterization (196), FaultPLCPCS (198), FaultPowerFailure (210), FaultStalledPositioner (204), FaultTemporaryComponents (194), FaultTestPositionFeedback (209), FixedLevel0 (1), FixedLevel1 (2), Flashing1Output (248), Flashing2Output (249), Flashing3Output (250), Flicker1Output (251), Flicker2Output (252), Flicker3Output (253), NonvolatileElement1Output (244), NonvolatileElement2Output (245), NonvolatileElement3Output (246), NonvolatileElement4Output (247), NotConnected (0), OPButton1 (33), OPButton2 (34), OPButton3 (35), OPButton4 (36), OPTestResetButton (32), PWMOutput (254), SignalConditioning1Output (240), SignalConditioning2Output (241), SignalConditioning3Output (242), SignalConditioning4Output (243), SignalConditioning5Output (214), SignalConditioning6Output (215), StatusBusOk (99), StatusChangeoverPauseActive (111), StatusCoolingDownPeriodActive (122), StatusCurrentFlowing (101), StatusDeviceOk (98), StatusDeviceTestActive (124), StatusEmergencyStartExecuted (121), StatusEnablingCircuitClosed (127), StatusFeedbackCLOSED (114), StatusFeedbackOPEN (115), StatusGroupFault (96), StatusGroupWarning (97), StatusInterlockingTimeActive (110), StatusOff (106), StatusOnForward (107), StatusOnForwardFast (108), StatusOnReverse (105), StatusOnReverseFast (104), StatusOperationalProtectionOff (119), StatusPauseTimeActive (123), StatusPhaseSequence123 (125), StatusPhaseSequence321 (126), StatusPLCPCSInRun (100), StatusPositionerRunsInCLOSEDDirection (113), StatusPositionerRunsInOPENDirection (112), StatusPROFIenergyCommandStartPausePending (102), StatusRemoteMode (120), StatusStartActive (109), StatusTestPosition (118), StatusTorqueCLOSED (116), StatusTorqueOPEN (117), Timer1Output (232), Timer2Output (233), Timer3Output (234), Timer4Output (235), Timer5Output (230), Timer6Output (231), TruthTable10Output (226), TruthTable11Output (227), TruthTable1Output (216), TruthTable2Output (217), TruthTable3Output (218), TruthTable4Output (219), TruthTable5Output (220), TruthTable6Output (221), TruthTable7Output (222), TruthTable8Output (223), TruthTable9Output1 (224), TruthTable9Output2 (225), WarningFeedbackCircuit (190), WarningSimultaneity (191)
    """

    AcyclicReceiveBit00 = None
    AcyclicReceiveBit01 = None
    AcyclicReceiveBit02 = None
    AcyclicReceiveBit03 = None
    AcyclicReceiveBit04 = None
    AcyclicReceiveBit05 = None
    AcyclicReceiveBit06 = None
    AcyclicReceiveBit07 = None
    AcyclicReceiveBit10 = None
    AcyclicReceiveBit11 = None
    AcyclicReceiveBit12 = None
    AcyclicReceiveBit13 = None
    AcyclicReceiveBit14 = None
    AcyclicReceiveBit15 = None
    AcyclicReceiveBit16 = None
    AcyclicReceiveBit17 = None
    BUInput1 = None
    BUInput2 = None
    BUInput3 = None
    BUInput4 = None
    BUTestResetButton = None
    ContactorControl1QE1 = None
    ContactorControl2QE2 = None
    ContactorControl3QE3 = None
    ContactorControl4QE4 = None
    ContactorControl5QE5 = None
    Counter1Output = None
    Counter2Output = None
    Counter3Output = None
    Counter4Output = None
    Counter5Output = None
    Counter6Output = None
    CyclicReceiveBit00 = None
    CyclicReceiveBit01 = None
    CyclicReceiveBit02 = None
    CyclicReceiveBit03 = None
    CyclicReceiveBit04 = None
    CyclicReceiveBit05 = None
    CyclicReceiveBit06 = None
    CyclicReceiveBit07 = None
    CyclicReceiveBit10 = None
    CyclicReceiveBit11 = None
    CyclicReceiveBit12 = None
    CyclicReceiveBit13 = None
    CyclicReceiveBit14 = None
    CyclicReceiveBit15 = None
    CyclicReceiveBit16 = None
    CyclicReceiveBit17 = None
    DisplayQLAOff = None
    DisplayQLEForward = None
    DisplayQLEForwardFast = None
    DisplayQLEReverse = None
    DisplayQLEReverseFast = None
    DisplayQLSFault = None
    DM1Input1 = None
    DM1Input2 = None
    DM1Input3 = None
    DM1Input4 = None
    DM1SensorChannel1 = None
    DM1SensorChannel2 = None
    DM2Input1 = None
    DM2Input2 = None
    DM2Input3 = None
    DM2Input4 = None
    EnabledControlCommandOff = None
    EnabledControlCommandOnForward = None
    EnabledControlCommandOnForwardFast = None
    EnabledControlCommandOnReverse = None
    EnabledControlCommandOnReverseFast = None
    EventAM1OpenCircuit = None
    EventAM1TripLevel0420mAGt = None
    EventAM1TripLevel0420mALt = None
    EventAM1WarningLevel0420mAGt = None
    EventAM1WarningLevel0420mALt = None
    EventAM2OpenCircuit = None
    EventAM2TripLevel0420mAGt = None
    EventAM2TripLevel0420mALt = None
    EventAM2WarningLevel0420mAGt = None
    EventAM2WarningLevel0420mALt = None
    EventConfiguredOperatorPanelMissing = None
    EventDMFLOCALOk = None
    EventExternalFault1 = None
    EventExternalFault2 = None
    EventExternalFault3 = None
    EventExternalFault4 = None
    EventExternalFault5 = None
    EventExternalFault6 = None
    EventExternalGroundFault = None
    EventExternalGroundFaultWarning = None
    EventInternalGroundFault = None
    EventJustOneStartPossible = None
    EventLimitMonitor1 = None
    EventLimitMonitor2 = None
    EventLimitMonitor3 = None
    EventLimitMonitor4 = None
    EventLimitMonitor5 = None
    EventLimitMonitor6 = None
    EventMonitoringPeriodForMandatoryTestingTestRequirement = None
    EventMotorOperatingHoursGt = None
    EventNoStartPermitted = None
    EventNumberOfStartsGt = None
    EventOverload = None
    EventOverloadAndPhaseFailure = None
    EventPrewarningOverload = None
    EventPROFIsafeActive = None
    EventSafetyrelatedTripping = None
    EventStalledRotor = None
    EventStopTimeGt = None
    EventThermistorOpenCircuit = None
    EventThermistorShortCircuit = None
    EventThermistorTripLevel = None
    EventTimestampfctActiveAndOk = None
    EventTM1OutOfRange = None
    EventTM1SensorFault = None
    EventTM1TripLevelTGt = None
    EventTM1WarningLevelTGt = None
    EventTM2OutOfRange = None
    EventTM2SensorFault = None
    EventTM2TripLevelTGt = None
    EventTM2WarningLevelTGt = None
    EventTripLevelCosPhiLt = None
    EventTripLevelIGt = None
    EventTripLevelILt = None
    EventTripLevelPGt = None
    EventTripLevelPLt = None
    EventTripLevelULt = None
    EventUnbalance = None
    EventWarningLevelCosPhiLt = None
    EventWarningLevelIGt = None
    EventWarningLevelILt = None
    EventWarningLevelPGt = None
    EventWarningLevelPLt = None
    EventWarningLevelULt = None
    FaultAntivalence = None
    FaultBus = None
    FaultConfigurationError = None
    FaultDouble0 = None
    FaultDouble1 = None
    FaultEndPosition = None
    FaultExecutionOnCommand = None
    FaultExecutionSTOPCommand = None
    FaultFeedbackOff = None
    FaultFeedbackOn = None
    FaultHardwareFaultBasicUnit = None
    FaultModuleFault = None
    FaultOperationalProtectionOff = None
    FaultParameterization = None
    FaultPLCPCS = None
    FaultPowerFailure = None
    FaultStalledPositioner = None
    FaultTemporaryComponents = None
    FaultTestPositionFeedback = None
    FixedLevel0 = None
    FixedLevel1 = None
    Flashing1Output = None
    Flashing2Output = None
    Flashing3Output = None
    Flicker1Output = None
    Flicker2Output = None
    Flicker3Output = None
    NonvolatileElement1Output = None
    NonvolatileElement2Output = None
    NonvolatileElement3Output = None
    NonvolatileElement4Output = None
    NotConnected = None
    OPButton1 = None
    OPButton2 = None
    OPButton3 = None
    OPButton4 = None
    OPTestResetButton = None
    PWMOutput = None
    SignalConditioning1Output = None
    SignalConditioning2Output = None
    SignalConditioning3Output = None
    SignalConditioning4Output = None
    SignalConditioning5Output = None
    SignalConditioning6Output = None
    StatusBusOk = None
    StatusChangeoverPauseActive = None
    StatusCoolingDownPeriodActive = None
    StatusCurrentFlowing = None
    StatusDeviceOk = None
    StatusDeviceTestActive = None
    StatusEmergencyStartExecuted = None
    StatusEnablingCircuitClosed = None
    StatusFeedbackCLOSED = None
    StatusFeedbackOPEN = None
    StatusGroupFault = None
    StatusGroupWarning = None
    StatusInterlockingTimeActive = None
    StatusOff = None
    StatusOnForward = None
    StatusOnForwardFast = None
    StatusOnReverse = None
    StatusOnReverseFast = None
    StatusOperationalProtectionOff = None
    StatusPauseTimeActive = None
    StatusPhaseSequence123 = None
    StatusPhaseSequence321 = None
    StatusPLCPCSInRun = None
    StatusPositionerRunsInCLOSEDDirection = None
    StatusPositionerRunsInOPENDirection = None
    StatusPROFIenergyCommandStartPausePending = None
    StatusRemoteMode = None
    StatusStartActive = None
    StatusTestPosition = None
    StatusTorqueCLOSED = None
    StatusTorqueOPEN = None
    Timer1Output = None
    Timer2Output = None
    Timer3Output = None
    Timer4Output = None
    Timer5Output = None
    Timer6Output = None
    TruthTable10Output = None
    TruthTable11Output = None
    TruthTable1Output = None
    TruthTable2Output = None
    TruthTable3Output = None
    TruthTable4Output = None
    TruthTable5Output = None
    TruthTable6Output = None
    TruthTable7Output = None
    TruthTable8Output = None
    TruthTable9Output1 = None
    TruthTable9Output2 = None
    value__ = None
    WarningFeedbackCircuit = None
    WarningSimultaneity = None

class ControlFunctionFeedbackOPENFO(
    Enum
):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Possible values for property ControlFunctionFeedbackOPENFO

    enum ControlFunctionFeedbackOPENFO, values: AcyclicReceiveBit00 (40), AcyclicReceiveBit01 (41), AcyclicReceiveBit02 (42), AcyclicReceiveBit03 (43), AcyclicReceiveBit04 (44), AcyclicReceiveBit05 (45), AcyclicReceiveBit06 (46), AcyclicReceiveBit07 (47), AcyclicReceiveBit10 (48), AcyclicReceiveBit11 (49), AcyclicReceiveBit12 (50), AcyclicReceiveBit13 (51), AcyclicReceiveBit14 (52), AcyclicReceiveBit15 (53), AcyclicReceiveBit16 (54), AcyclicReceiveBit17 (55), BUInput1 (9), BUInput2 (10), BUInput3 (11), BUInput4 (12), BUTestResetButton (8), ContactorControl1QE1 (80), ContactorControl2QE2 (81), ContactorControl3QE3 (82), ContactorControl4QE4 (83), ContactorControl5QE5 (84), Counter1Output (236), Counter2Output (237), Counter3Output (238), Counter4Output (239), Counter5Output (228), Counter6Output (229), CyclicReceiveBit00 (56), CyclicReceiveBit01 (57), CyclicReceiveBit02 (58), CyclicReceiveBit03 (59), CyclicReceiveBit04 (60), CyclicReceiveBit05 (61), CyclicReceiveBit06 (62), CyclicReceiveBit07 (63), CyclicReceiveBit10 (64), CyclicReceiveBit11 (65), CyclicReceiveBit12 (66), CyclicReceiveBit13 (67), CyclicReceiveBit14 (68), CyclicReceiveBit15 (69), CyclicReceiveBit16 (70), CyclicReceiveBit17 (71), DisplayQLAOff (90), DisplayQLEForward (91), DisplayQLEForwardFast (92), DisplayQLEReverse (89), DisplayQLEReverseFast (88), DisplayQLSFault (93), DM1Input1 (16), DM1Input2 (17), DM1Input3 (18), DM1Input4 (19), DM1SensorChannel1 (24), DM1SensorChannel2 (25), DM2Input1 (20), DM2Input2 (21), DM2Input3 (22), DM2Input4 (23), EnabledControlCommandOff (74), EnabledControlCommandOnForward (75), EnabledControlCommandOnForwardFast (76), EnabledControlCommandOnReverse (73), EnabledControlCommandOnReverseFast (72), EventAM1OpenCircuit (180), EventAM1TripLevel0420mAGt (158), EventAM1TripLevel0420mALt (159), EventAM1WarningLevel0420mAGt (150), EventAM1WarningLevel0420mALt (151), EventAM2OpenCircuit (179), EventAM2TripLevel0420mAGt (6), EventAM2TripLevel0420mALt (7), EventAM2WarningLevel0420mAGt (4), EventAM2WarningLevel0420mALt (5), EventConfiguredOperatorPanelMissing (188), EventDMFLOCALOk (186), EventExternalFault1 (172), EventExternalFault2 (173), EventExternalFault3 (174), EventExternalFault4 (175), EventExternalFault5 (176), EventExternalFault6 (177), EventExternalGroundFault (133), EventExternalGroundFaultWarning (134), EventInternalGroundFault (132), EventJustOneStartPossible (165), EventLimitMonitor1 (168), EventLimitMonitor2 (169), EventLimitMonitor3 (170), EventLimitMonitor4 (171), EventLimitMonitor5 (38), EventLimitMonitor6 (39), EventMonitoringPeriodForMandatoryTestingTestRequirement (182), EventMotorOperatingHoursGt (166), EventNoStartPermitted (163), EventNumberOfStartsGt (164), EventOverload (130), EventOverloadAndPhaseFailure (131), EventPrewarningOverload (128), EventPROFIsafeActive (187), EventSafetyrelatedTripping (181), EventStalledRotor (160), EventStopTimeGt (167), EventThermistorOpenCircuit (137), EventThermistorShortCircuit (136), EventThermistorTripLevel (135), EventTimestampfctActiveAndOk (184), EventTM1OutOfRange (141), EventTM1SensorFault (140), EventTM1TripLevelTGt (139), EventTM1WarningLevelTGt (138), EventTM2OutOfRange (29), EventTM2SensorFault (28), EventTM2TripLevelTGt (31), EventTM2WarningLevelTGt (30), EventTripLevelCosPhiLt (156), EventTripLevelIGt (152), EventTripLevelILt (153), EventTripLevelPGt (154), EventTripLevelPLt (155), EventTripLevelULt (157), EventUnbalance (129), EventWarningLevelCosPhiLt (148), EventWarningLevelIGt (144), EventWarningLevelILt (145), EventWarningLevelPGt (146), EventWarningLevelPLt (147), EventWarningLevelULt (149), FaultAntivalence (208), FaultBus (197), FaultConfigurationError (195), FaultDouble0 (205), FaultDouble1 (206), FaultEndPosition (207), FaultExecutionOnCommand (200), FaultExecutionSTOPCommand (201), FaultFeedbackOff (203), FaultFeedbackOn (202), FaultHardwareFaultBasicUnit (192), FaultModuleFault (193), FaultOperationalProtectionOff (211), FaultParameterization (196), FaultPLCPCS (198), FaultPowerFailure (210), FaultStalledPositioner (204), FaultTemporaryComponents (194), FaultTestPositionFeedback (209), FixedLevel0 (1), FixedLevel1 (2), Flashing1Output (248), Flashing2Output (249), Flashing3Output (250), Flicker1Output (251), Flicker2Output (252), Flicker3Output (253), NonvolatileElement1Output (244), NonvolatileElement2Output (245), NonvolatileElement3Output (246), NonvolatileElement4Output (247), NotConnected (0), OPButton1 (33), OPButton2 (34), OPButton3 (35), OPButton4 (36), OPTestResetButton (32), PWMOutput (254), SignalConditioning1Output (240), SignalConditioning2Output (241), SignalConditioning3Output (242), SignalConditioning4Output (243), SignalConditioning5Output (214), SignalConditioning6Output (215), StatusBusOk (99), StatusChangeoverPauseActive (111), StatusCoolingDownPeriodActive (122), StatusCurrentFlowing (101), StatusDeviceOk (98), StatusDeviceTestActive (124), StatusEmergencyStartExecuted (121), StatusEnablingCircuitClosed (127), StatusFeedbackCLOSED (114), StatusFeedbackOPEN (115), StatusGroupFault (96), StatusGroupWarning (97), StatusInterlockingTimeActive (110), StatusOff (106), StatusOnForward (107), StatusOnForwardFast (108), StatusOnReverse (105), StatusOnReverseFast (104), StatusOperationalProtectionOff (119), StatusPauseTimeActive (123), StatusPhaseSequence123 (125), StatusPhaseSequence321 (126), StatusPLCPCSInRun (100), StatusPositionerRunsInCLOSEDDirection (113), StatusPositionerRunsInOPENDirection (112), StatusPROFIenergyCommandStartPausePending (102), StatusRemoteMode (120), StatusStartActive (109), StatusTestPosition (118), StatusTorqueCLOSED (116), StatusTorqueOPEN (117), Timer1Output (232), Timer2Output (233), Timer3Output (234), Timer4Output (235), Timer5Output (230), Timer6Output (231), TruthTable10Output (226), TruthTable11Output (227), TruthTable1Output (216), TruthTable2Output (217), TruthTable3Output (218), TruthTable4Output (219), TruthTable5Output (220), TruthTable6Output (221), TruthTable7Output (222), TruthTable8Output (223), TruthTable9Output1 (224), TruthTable9Output2 (225), WarningFeedbackCircuit (190), WarningSimultaneity (191)
    """

    AcyclicReceiveBit00 = None
    AcyclicReceiveBit01 = None
    AcyclicReceiveBit02 = None
    AcyclicReceiveBit03 = None
    AcyclicReceiveBit04 = None
    AcyclicReceiveBit05 = None
    AcyclicReceiveBit06 = None
    AcyclicReceiveBit07 = None
    AcyclicReceiveBit10 = None
    AcyclicReceiveBit11 = None
    AcyclicReceiveBit12 = None
    AcyclicReceiveBit13 = None
    AcyclicReceiveBit14 = None
    AcyclicReceiveBit15 = None
    AcyclicReceiveBit16 = None
    AcyclicReceiveBit17 = None
    BUInput1 = None
    BUInput2 = None
    BUInput3 = None
    BUInput4 = None
    BUTestResetButton = None
    ContactorControl1QE1 = None
    ContactorControl2QE2 = None
    ContactorControl3QE3 = None
    ContactorControl4QE4 = None
    ContactorControl5QE5 = None
    Counter1Output = None
    Counter2Output = None
    Counter3Output = None
    Counter4Output = None
    Counter5Output = None
    Counter6Output = None
    CyclicReceiveBit00 = None
    CyclicReceiveBit01 = None
    CyclicReceiveBit02 = None
    CyclicReceiveBit03 = None
    CyclicReceiveBit04 = None
    CyclicReceiveBit05 = None
    CyclicReceiveBit06 = None
    CyclicReceiveBit07 = None
    CyclicReceiveBit10 = None
    CyclicReceiveBit11 = None
    CyclicReceiveBit12 = None
    CyclicReceiveBit13 = None
    CyclicReceiveBit14 = None
    CyclicReceiveBit15 = None
    CyclicReceiveBit16 = None
    CyclicReceiveBit17 = None
    DisplayQLAOff = None
    DisplayQLEForward = None
    DisplayQLEForwardFast = None
    DisplayQLEReverse = None
    DisplayQLEReverseFast = None
    DisplayQLSFault = None
    DM1Input1 = None
    DM1Input2 = None
    DM1Input3 = None
    DM1Input4 = None
    DM1SensorChannel1 = None
    DM1SensorChannel2 = None
    DM2Input1 = None
    DM2Input2 = None
    DM2Input3 = None
    DM2Input4 = None
    EnabledControlCommandOff = None
    EnabledControlCommandOnForward = None
    EnabledControlCommandOnForwardFast = None
    EnabledControlCommandOnReverse = None
    EnabledControlCommandOnReverseFast = None
    EventAM1OpenCircuit = None
    EventAM1TripLevel0420mAGt = None
    EventAM1TripLevel0420mALt = None
    EventAM1WarningLevel0420mAGt = None
    EventAM1WarningLevel0420mALt = None
    EventAM2OpenCircuit = None
    EventAM2TripLevel0420mAGt = None
    EventAM2TripLevel0420mALt = None
    EventAM2WarningLevel0420mAGt = None
    EventAM2WarningLevel0420mALt = None
    EventConfiguredOperatorPanelMissing = None
    EventDMFLOCALOk = None
    EventExternalFault1 = None
    EventExternalFault2 = None
    EventExternalFault3 = None
    EventExternalFault4 = None
    EventExternalFault5 = None
    EventExternalFault6 = None
    EventExternalGroundFault = None
    EventExternalGroundFaultWarning = None
    EventInternalGroundFault = None
    EventJustOneStartPossible = None
    EventLimitMonitor1 = None
    EventLimitMonitor2 = None
    EventLimitMonitor3 = None
    EventLimitMonitor4 = None
    EventLimitMonitor5 = None
    EventLimitMonitor6 = None
    EventMonitoringPeriodForMandatoryTestingTestRequirement = None
    EventMotorOperatingHoursGt = None
    EventNoStartPermitted = None
    EventNumberOfStartsGt = None
    EventOverload = None
    EventOverloadAndPhaseFailure = None
    EventPrewarningOverload = None
    EventPROFIsafeActive = None
    EventSafetyrelatedTripping = None
    EventStalledRotor = None
    EventStopTimeGt = None
    EventThermistorOpenCircuit = None
    EventThermistorShortCircuit = None
    EventThermistorTripLevel = None
    EventTimestampfctActiveAndOk = None
    EventTM1OutOfRange = None
    EventTM1SensorFault = None
    EventTM1TripLevelTGt = None
    EventTM1WarningLevelTGt = None
    EventTM2OutOfRange = None
    EventTM2SensorFault = None
    EventTM2TripLevelTGt = None
    EventTM2WarningLevelTGt = None
    EventTripLevelCosPhiLt = None
    EventTripLevelIGt = None
    EventTripLevelILt = None
    EventTripLevelPGt = None
    EventTripLevelPLt = None
    EventTripLevelULt = None
    EventUnbalance = None
    EventWarningLevelCosPhiLt = None
    EventWarningLevelIGt = None
    EventWarningLevelILt = None
    EventWarningLevelPGt = None
    EventWarningLevelPLt = None
    EventWarningLevelULt = None
    FaultAntivalence = None
    FaultBus = None
    FaultConfigurationError = None
    FaultDouble0 = None
    FaultDouble1 = None
    FaultEndPosition = None
    FaultExecutionOnCommand = None
    FaultExecutionSTOPCommand = None
    FaultFeedbackOff = None
    FaultFeedbackOn = None
    FaultHardwareFaultBasicUnit = None
    FaultModuleFault = None
    FaultOperationalProtectionOff = None
    FaultParameterization = None
    FaultPLCPCS = None
    FaultPowerFailure = None
    FaultStalledPositioner = None
    FaultTemporaryComponents = None
    FaultTestPositionFeedback = None
    FixedLevel0 = None
    FixedLevel1 = None
    Flashing1Output = None
    Flashing2Output = None
    Flashing3Output = None
    Flicker1Output = None
    Flicker2Output = None
    Flicker3Output = None
    NonvolatileElement1Output = None
    NonvolatileElement2Output = None
    NonvolatileElement3Output = None
    NonvolatileElement4Output = None
    NotConnected = None
    OPButton1 = None
    OPButton2 = None
    OPButton3 = None
    OPButton4 = None
    OPTestResetButton = None
    PWMOutput = None
    SignalConditioning1Output = None
    SignalConditioning2Output = None
    SignalConditioning3Output = None
    SignalConditioning4Output = None
    SignalConditioning5Output = None
    SignalConditioning6Output = None
    StatusBusOk = None
    StatusChangeoverPauseActive = None
    StatusCoolingDownPeriodActive = None
    StatusCurrentFlowing = None
    StatusDeviceOk = None
    StatusDeviceTestActive = None
    StatusEmergencyStartExecuted = None
    StatusEnablingCircuitClosed = None
    StatusFeedbackCLOSED = None
    StatusFeedbackOPEN = None
    StatusGroupFault = None
    StatusGroupWarning = None
    StatusInterlockingTimeActive = None
    StatusOff = None
    StatusOnForward = None
    StatusOnForwardFast = None
    StatusOnReverse = None
    StatusOnReverseFast = None
    StatusOperationalProtectionOff = None
    StatusPauseTimeActive = None
    StatusPhaseSequence123 = None
    StatusPhaseSequence321 = None
    StatusPLCPCSInRun = None
    StatusPositionerRunsInCLOSEDDirection = None
    StatusPositionerRunsInOPENDirection = None
    StatusPROFIenergyCommandStartPausePending = None
    StatusRemoteMode = None
    StatusStartActive = None
    StatusTestPosition = None
    StatusTorqueCLOSED = None
    StatusTorqueOPEN = None
    Timer1Output = None
    Timer2Output = None
    Timer3Output = None
    Timer4Output = None
    Timer5Output = None
    Timer6Output = None
    TruthTable10Output = None
    TruthTable11Output = None
    TruthTable1Output = None
    TruthTable2Output = None
    TruthTable3Output = None
    TruthTable4Output = None
    TruthTable5Output = None
    TruthTable6Output = None
    TruthTable7Output = None
    TruthTable8Output = None
    TruthTable9Output1 = None
    TruthTable9Output2 = None
    value__ = None
    WarningFeedbackCircuit = None
    WarningSimultaneity = None

class ControlFunctionForward(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Possible values for property ControlFunctionForward

    enum ControlFunctionForward, values: AcyclicReceiveBit00 (40), AcyclicReceiveBit01 (41), AcyclicReceiveBit02 (42), AcyclicReceiveBit03 (43), AcyclicReceiveBit04 (44), AcyclicReceiveBit05 (45), AcyclicReceiveBit06 (46), AcyclicReceiveBit07 (47), AcyclicReceiveBit10 (48), AcyclicReceiveBit11 (49), AcyclicReceiveBit12 (50), AcyclicReceiveBit13 (51), AcyclicReceiveBit14 (52), AcyclicReceiveBit15 (53), AcyclicReceiveBit16 (54), AcyclicReceiveBit17 (55), BUInput1 (9), BUInput2 (10), BUInput3 (11), BUInput4 (12), BUTestResetButton (8), ContactorControl1QE1 (80), ContactorControl2QE2 (81), ContactorControl3QE3 (82), ContactorControl4QE4 (83), ContactorControl5QE5 (84), Counter1Output (236), Counter2Output (237), Counter3Output (238), Counter4Output (239), Counter5Output (228), Counter6Output (229), CyclicReceiveBit00 (56), CyclicReceiveBit01 (57), CyclicReceiveBit02 (58), CyclicReceiveBit03 (59), CyclicReceiveBit04 (60), CyclicReceiveBit05 (61), CyclicReceiveBit06 (62), CyclicReceiveBit07 (63), CyclicReceiveBit10 (64), CyclicReceiveBit11 (65), CyclicReceiveBit12 (66), CyclicReceiveBit13 (67), CyclicReceiveBit14 (68), CyclicReceiveBit15 (69), CyclicReceiveBit16 (70), CyclicReceiveBit17 (71), DisplayQLAOff (90), DisplayQLEForward (91), DisplayQLEForwardFast (92), DisplayQLEReverse (89), DisplayQLEReverseFast (88), DisplayQLSFault (93), DM1Input1 (16), DM1Input2 (17), DM1Input3 (18), DM1Input4 (19), DM1SensorChannel1 (24), DM1SensorChannel2 (25), DM2Input1 (20), DM2Input2 (21), DM2Input3 (22), DM2Input4 (23), EnabledControlCommandOff (74), EnabledControlCommandOnForward (75), EnabledControlCommandOnForwardFast (76), EnabledControlCommandOnReverse (73), EnabledControlCommandOnReverseFast (72), EventAM1OpenCircuit (180), EventAM1TripLevel0420mAGt (158), EventAM1TripLevel0420mALt (159), EventAM1WarningLevel0420mAGt (150), EventAM1WarningLevel0420mALt (151), EventAM2OpenCircuit (179), EventAM2TripLevel0420mAGt (6), EventAM2TripLevel0420mALt (7), EventAM2WarningLevel0420mAGt (4), EventAM2WarningLevel0420mALt (5), EventConfiguredOperatorPanelMissing (188), EventDMFLOCALOk (186), EventExternalFault1 (172), EventExternalFault2 (173), EventExternalFault3 (174), EventExternalFault4 (175), EventExternalFault5 (176), EventExternalFault6 (177), EventExternalGroundFault (133), EventExternalGroundFaultWarning (134), EventInternalGroundFault (132), EventJustOneStartPossible (165), EventLimitMonitor1 (168), EventLimitMonitor2 (169), EventLimitMonitor3 (170), EventLimitMonitor4 (171), EventLimitMonitor5 (38), EventLimitMonitor6 (39), EventMonitoringPeriodForMandatoryTestingTestRequirement (182), EventMotorOperatingHoursGt (166), EventNoStartPermitted (163), EventNumberOfStartsGt (164), EventOverload (130), EventOverloadAndPhaseFailure (131), EventPrewarningOverload (128), EventPROFIsafeActive (187), EventSafetyrelatedTripping (181), EventStalledRotor (160), EventStopTimeGt (167), EventThermistorOpenCircuit (137), EventThermistorShortCircuit (136), EventThermistorTripLevel (135), EventTimestampfctActiveAndOk (184), EventTM1OutOfRange (141), EventTM1SensorFault (140), EventTM1TripLevelTGt (139), EventTM1WarningLevelTGt (138), EventTM2OutOfRange (29), EventTM2SensorFault (28), EventTM2TripLevelTGt (31), EventTM2WarningLevelTGt (30), EventTripLevelCosPhiLt (156), EventTripLevelIGt (152), EventTripLevelILt (153), EventTripLevelPGt (154), EventTripLevelPLt (155), EventTripLevelULt (157), EventUnbalance (129), EventWarningLevelCosPhiLt (148), EventWarningLevelIGt (144), EventWarningLevelILt (145), EventWarningLevelPGt (146), EventWarningLevelPLt (147), EventWarningLevelULt (149), FaultAntivalence (208), FaultBus (197), FaultConfigurationError (195), FaultDouble0 (205), FaultDouble1 (206), FaultEndPosition (207), FaultExecutionOnCommand (200), FaultExecutionSTOPCommand (201), FaultFeedbackOff (203), FaultFeedbackOn (202), FaultHardwareFaultBasicUnit (192), FaultModuleFault (193), FaultOperationalProtectionOff (211), FaultParameterization (196), FaultPLCPCS (198), FaultPowerFailure (210), FaultStalledPositioner (204), FaultTemporaryComponents (194), FaultTestPositionFeedback (209), FixedLevel0 (1), FixedLevel1 (2), Flashing1Output (248), Flashing2Output (249), Flashing3Output (250), Flicker1Output (251), Flicker2Output (252), Flicker3Output (253), NonvolatileElement1Output (244), NonvolatileElement2Output (245), NonvolatileElement3Output (246), NonvolatileElement4Output (247), NotConnected (0), OPButton1 (33), OPButton2 (34), OPButton3 (35), OPButton4 (36), OPTestResetButton (32), PWMOutput (254), SignalConditioning1Output (240), SignalConditioning2Output (241), SignalConditioning3Output (242), SignalConditioning4Output (243), SignalConditioning5Output (214), SignalConditioning6Output (215), StatusBusOk (99), StatusChangeoverPauseActive (111), StatusCoolingDownPeriodActive (122), StatusCurrentFlowing (101), StatusDeviceOk (98), StatusDeviceTestActive (124), StatusEmergencyStartExecuted (121), StatusEnablingCircuitClosed (127), StatusFeedbackCLOSED (114), StatusFeedbackOPEN (115), StatusGroupFault (96), StatusGroupWarning (97), StatusInterlockingTimeActive (110), StatusOff (106), StatusOnForward (107), StatusOnForwardFast (108), StatusOnReverse (105), StatusOnReverseFast (104), StatusOperationalProtectionOff (119), StatusPauseTimeActive (123), StatusPhaseSequence123 (125), StatusPhaseSequence321 (126), StatusPLCPCSInRun (100), StatusPositionerRunsInCLOSEDDirection (113), StatusPositionerRunsInOPENDirection (112), StatusPROFIenergyCommandStartPausePending (102), StatusRemoteMode (120), StatusStartActive (109), StatusTestPosition (118), StatusTorqueCLOSED (116), StatusTorqueOPEN (117), Timer1Output (232), Timer2Output (233), Timer3Output (234), Timer4Output (235), Timer5Output (230), Timer6Output (231), TruthTable10Output (226), TruthTable11Output (227), TruthTable1Output (216), TruthTable2Output (217), TruthTable3Output (218), TruthTable4Output (219), TruthTable5Output (220), TruthTable6Output (221), TruthTable7Output (222), TruthTable8Output (223), TruthTable9Output1 (224), TruthTable9Output2 (225), WarningFeedbackCircuit (190), WarningSimultaneity (191)
    """

    AcyclicReceiveBit00 = None
    AcyclicReceiveBit01 = None
    AcyclicReceiveBit02 = None
    AcyclicReceiveBit03 = None
    AcyclicReceiveBit04 = None
    AcyclicReceiveBit05 = None
    AcyclicReceiveBit06 = None
    AcyclicReceiveBit07 = None
    AcyclicReceiveBit10 = None
    AcyclicReceiveBit11 = None
    AcyclicReceiveBit12 = None
    AcyclicReceiveBit13 = None
    AcyclicReceiveBit14 = None
    AcyclicReceiveBit15 = None
    AcyclicReceiveBit16 = None
    AcyclicReceiveBit17 = None
    BUInput1 = None
    BUInput2 = None
    BUInput3 = None
    BUInput4 = None
    BUTestResetButton = None
    ContactorControl1QE1 = None
    ContactorControl2QE2 = None
    ContactorControl3QE3 = None
    ContactorControl4QE4 = None
    ContactorControl5QE5 = None
    Counter1Output = None
    Counter2Output = None
    Counter3Output = None
    Counter4Output = None
    Counter5Output = None
    Counter6Output = None
    CyclicReceiveBit00 = None
    CyclicReceiveBit01 = None
    CyclicReceiveBit02 = None
    CyclicReceiveBit03 = None
    CyclicReceiveBit04 = None
    CyclicReceiveBit05 = None
    CyclicReceiveBit06 = None
    CyclicReceiveBit07 = None
    CyclicReceiveBit10 = None
    CyclicReceiveBit11 = None
    CyclicReceiveBit12 = None
    CyclicReceiveBit13 = None
    CyclicReceiveBit14 = None
    CyclicReceiveBit15 = None
    CyclicReceiveBit16 = None
    CyclicReceiveBit17 = None
    DisplayQLAOff = None
    DisplayQLEForward = None
    DisplayQLEForwardFast = None
    DisplayQLEReverse = None
    DisplayQLEReverseFast = None
    DisplayQLSFault = None
    DM1Input1 = None
    DM1Input2 = None
    DM1Input3 = None
    DM1Input4 = None
    DM1SensorChannel1 = None
    DM1SensorChannel2 = None
    DM2Input1 = None
    DM2Input2 = None
    DM2Input3 = None
    DM2Input4 = None
    EnabledControlCommandOff = None
    EnabledControlCommandOnForward = None
    EnabledControlCommandOnForwardFast = None
    EnabledControlCommandOnReverse = None
    EnabledControlCommandOnReverseFast = None
    EventAM1OpenCircuit = None
    EventAM1TripLevel0420mAGt = None
    EventAM1TripLevel0420mALt = None
    EventAM1WarningLevel0420mAGt = None
    EventAM1WarningLevel0420mALt = None
    EventAM2OpenCircuit = None
    EventAM2TripLevel0420mAGt = None
    EventAM2TripLevel0420mALt = None
    EventAM2WarningLevel0420mAGt = None
    EventAM2WarningLevel0420mALt = None
    EventConfiguredOperatorPanelMissing = None
    EventDMFLOCALOk = None
    EventExternalFault1 = None
    EventExternalFault2 = None
    EventExternalFault3 = None
    EventExternalFault4 = None
    EventExternalFault5 = None
    EventExternalFault6 = None
    EventExternalGroundFault = None
    EventExternalGroundFaultWarning = None
    EventInternalGroundFault = None
    EventJustOneStartPossible = None
    EventLimitMonitor1 = None
    EventLimitMonitor2 = None
    EventLimitMonitor3 = None
    EventLimitMonitor4 = None
    EventLimitMonitor5 = None
    EventLimitMonitor6 = None
    EventMonitoringPeriodForMandatoryTestingTestRequirement = None
    EventMotorOperatingHoursGt = None
    EventNoStartPermitted = None
    EventNumberOfStartsGt = None
    EventOverload = None
    EventOverloadAndPhaseFailure = None
    EventPrewarningOverload = None
    EventPROFIsafeActive = None
    EventSafetyrelatedTripping = None
    EventStalledRotor = None
    EventStopTimeGt = None
    EventThermistorOpenCircuit = None
    EventThermistorShortCircuit = None
    EventThermistorTripLevel = None
    EventTimestampfctActiveAndOk = None
    EventTM1OutOfRange = None
    EventTM1SensorFault = None
    EventTM1TripLevelTGt = None
    EventTM1WarningLevelTGt = None
    EventTM2OutOfRange = None
    EventTM2SensorFault = None
    EventTM2TripLevelTGt = None
    EventTM2WarningLevelTGt = None
    EventTripLevelCosPhiLt = None
    EventTripLevelIGt = None
    EventTripLevelILt = None
    EventTripLevelPGt = None
    EventTripLevelPLt = None
    EventTripLevelULt = None
    EventUnbalance = None
    EventWarningLevelCosPhiLt = None
    EventWarningLevelIGt = None
    EventWarningLevelILt = None
    EventWarningLevelPGt = None
    EventWarningLevelPLt = None
    EventWarningLevelULt = None
    FaultAntivalence = None
    FaultBus = None
    FaultConfigurationError = None
    FaultDouble0 = None
    FaultDouble1 = None
    FaultEndPosition = None
    FaultExecutionOnCommand = None
    FaultExecutionSTOPCommand = None
    FaultFeedbackOff = None
    FaultFeedbackOn = None
    FaultHardwareFaultBasicUnit = None
    FaultModuleFault = None
    FaultOperationalProtectionOff = None
    FaultParameterization = None
    FaultPLCPCS = None
    FaultPowerFailure = None
    FaultStalledPositioner = None
    FaultTemporaryComponents = None
    FaultTestPositionFeedback = None
    FixedLevel0 = None
    FixedLevel1 = None
    Flashing1Output = None
    Flashing2Output = None
    Flashing3Output = None
    Flicker1Output = None
    Flicker2Output = None
    Flicker3Output = None
    NonvolatileElement1Output = None
    NonvolatileElement2Output = None
    NonvolatileElement3Output = None
    NonvolatileElement4Output = None
    NotConnected = None
    OPButton1 = None
    OPButton2 = None
    OPButton3 = None
    OPButton4 = None
    OPTestResetButton = None
    PWMOutput = None
    SignalConditioning1Output = None
    SignalConditioning2Output = None
    SignalConditioning3Output = None
    SignalConditioning4Output = None
    SignalConditioning5Output = None
    SignalConditioning6Output = None
    StatusBusOk = None
    StatusChangeoverPauseActive = None
    StatusCoolingDownPeriodActive = None
    StatusCurrentFlowing = None
    StatusDeviceOk = None
    StatusDeviceTestActive = None
    StatusEmergencyStartExecuted = None
    StatusEnablingCircuitClosed = None
    StatusFeedbackCLOSED = None
    StatusFeedbackOPEN = None
    StatusGroupFault = None
    StatusGroupWarning = None
    StatusInterlockingTimeActive = None
    StatusOff = None
    StatusOnForward = None
    StatusOnForwardFast = None
    StatusOnReverse = None
    StatusOnReverseFast = None
    StatusOperationalProtectionOff = None
    StatusPauseTimeActive = None
    StatusPhaseSequence123 = None
    StatusPhaseSequence321 = None
    StatusPLCPCSInRun = None
    StatusPositionerRunsInCLOSEDDirection = None
    StatusPositionerRunsInOPENDirection = None
    StatusPROFIenergyCommandStartPausePending = None
    StatusRemoteMode = None
    StatusStartActive = None
    StatusTestPosition = None
    StatusTorqueCLOSED = None
    StatusTorqueOPEN = None
    Timer1Output = None
    Timer2Output = None
    Timer3Output = None
    Timer4Output = None
    Timer5Output = None
    Timer6Output = None
    TruthTable10Output = None
    TruthTable11Output = None
    TruthTable1Output = None
    TruthTable2Output = None
    TruthTable3Output = None
    TruthTable4Output = None
    TruthTable5Output = None
    TruthTable6Output = None
    TruthTable7Output = None
    TruthTable8Output = None
    TruthTable9Output1 = None
    TruthTable9Output2 = None
    value__ = None
    WarningFeedbackCircuit = None
    WarningSimultaneity = None

class ControlFunctionForwardFast(
    Enum
):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Possible values for property ControlFunctionForwardFast

    enum ControlFunctionForwardFast, values: AcyclicReceiveBit00 (40), AcyclicReceiveBit01 (41), AcyclicReceiveBit02 (42), AcyclicReceiveBit03 (43), AcyclicReceiveBit04 (44), AcyclicReceiveBit05 (45), AcyclicReceiveBit06 (46), AcyclicReceiveBit07 (47), AcyclicReceiveBit10 (48), AcyclicReceiveBit11 (49), AcyclicReceiveBit12 (50), AcyclicReceiveBit13 (51), AcyclicReceiveBit14 (52), AcyclicReceiveBit15 (53), AcyclicReceiveBit16 (54), AcyclicReceiveBit17 (55), BUInput1 (9), BUInput2 (10), BUInput3 (11), BUInput4 (12), BUTestResetButton (8), ContactorControl1QE1 (80), ContactorControl2QE2 (81), ContactorControl3QE3 (82), ContactorControl4QE4 (83), ContactorControl5QE5 (84), Counter1Output (236), Counter2Output (237), Counter3Output (238), Counter4Output (239), Counter5Output (228), Counter6Output (229), CyclicReceiveBit00 (56), CyclicReceiveBit01 (57), CyclicReceiveBit02 (58), CyclicReceiveBit03 (59), CyclicReceiveBit04 (60), CyclicReceiveBit05 (61), CyclicReceiveBit06 (62), CyclicReceiveBit07 (63), CyclicReceiveBit10 (64), CyclicReceiveBit11 (65), CyclicReceiveBit12 (66), CyclicReceiveBit13 (67), CyclicReceiveBit14 (68), CyclicReceiveBit15 (69), CyclicReceiveBit16 (70), CyclicReceiveBit17 (71), DisplayQLAOff (90), DisplayQLEForward (91), DisplayQLEForwardFast (92), DisplayQLEReverse (89), DisplayQLEReverseFast (88), DisplayQLSFault (93), DM1Input1 (16), DM1Input2 (17), DM1Input3 (18), DM1Input4 (19), DM1SensorChannel1 (24), DM1SensorChannel2 (25), DM2Input1 (20), DM2Input2 (21), DM2Input3 (22), DM2Input4 (23), EnabledControlCommandOff (74), EnabledControlCommandOnForward (75), EnabledControlCommandOnForwardFast (76), EnabledControlCommandOnReverse (73), EnabledControlCommandOnReverseFast (72), EventAM1OpenCircuit (180), EventAM1TripLevel0420mAGt (158), EventAM1TripLevel0420mALt (159), EventAM1WarningLevel0420mAGt (150), EventAM1WarningLevel0420mALt (151), EventAM2OpenCircuit (179), EventAM2TripLevel0420mAGt (6), EventAM2TripLevel0420mALt (7), EventAM2WarningLevel0420mAGt (4), EventAM2WarningLevel0420mALt (5), EventConfiguredOperatorPanelMissing (188), EventDMFLOCALOk (186), EventExternalFault1 (172), EventExternalFault2 (173), EventExternalFault3 (174), EventExternalFault4 (175), EventExternalFault5 (176), EventExternalFault6 (177), EventExternalGroundFault (133), EventExternalGroundFaultWarning (134), EventInternalGroundFault (132), EventJustOneStartPossible (165), EventLimitMonitor1 (168), EventLimitMonitor2 (169), EventLimitMonitor3 (170), EventLimitMonitor4 (171), EventLimitMonitor5 (38), EventLimitMonitor6 (39), EventMonitoringPeriodForMandatoryTestingTestRequirement (182), EventMotorOperatingHoursGt (166), EventNoStartPermitted (163), EventNumberOfStartsGt (164), EventOverload (130), EventOverloadAndPhaseFailure (131), EventPrewarningOverload (128), EventPROFIsafeActive (187), EventSafetyrelatedTripping (181), EventStalledRotor (160), EventStopTimeGt (167), EventThermistorOpenCircuit (137), EventThermistorShortCircuit (136), EventThermistorTripLevel (135), EventTimestampfctActiveAndOk (184), EventTM1OutOfRange (141), EventTM1SensorFault (140), EventTM1TripLevelTGt (139), EventTM1WarningLevelTGt (138), EventTM2OutOfRange (29), EventTM2SensorFault (28), EventTM2TripLevelTGt (31), EventTM2WarningLevelTGt (30), EventTripLevelCosPhiLt (156), EventTripLevelIGt (152), EventTripLevelILt (153), EventTripLevelPGt (154), EventTripLevelPLt (155), EventTripLevelULt (157), EventUnbalance (129), EventWarningLevelCosPhiLt (148), EventWarningLevelIGt (144), EventWarningLevelILt (145), EventWarningLevelPGt (146), EventWarningLevelPLt (147), EventWarningLevelULt (149), FaultAntivalence (208), FaultBus (197), FaultConfigurationError (195), FaultDouble0 (205), FaultDouble1 (206), FaultEndPosition (207), FaultExecutionOnCommand (200), FaultExecutionSTOPCommand (201), FaultFeedbackOff (203), FaultFeedbackOn (202), FaultHardwareFaultBasicUnit (192), FaultModuleFault (193), FaultOperationalProtectionOff (211), FaultParameterization (196), FaultPLCPCS (198), FaultPowerFailure (210), FaultStalledPositioner (204), FaultTemporaryComponents (194), FaultTestPositionFeedback (209), FixedLevel0 (1), FixedLevel1 (2), Flashing1Output (248), Flashing2Output (249), Flashing3Output (250), Flicker1Output (251), Flicker2Output (252), Flicker3Output (253), NonvolatileElement1Output (244), NonvolatileElement2Output (245), NonvolatileElement3Output (246), NonvolatileElement4Output (247), NotConnected (0), OPButton1 (33), OPButton2 (34), OPButton3 (35), OPButton4 (36), OPTestResetButton (32), PWMOutput (254), SignalConditioning1Output (240), SignalConditioning2Output (241), SignalConditioning3Output (242), SignalConditioning4Output (243), SignalConditioning5Output (214), SignalConditioning6Output (215), StatusBusOk (99), StatusChangeoverPauseActive (111), StatusCoolingDownPeriodActive (122), StatusCurrentFlowing (101), StatusDeviceOk (98), StatusDeviceTestActive (124), StatusEmergencyStartExecuted (121), StatusEnablingCircuitClosed (127), StatusFeedbackCLOSED (114), StatusFeedbackOPEN (115), StatusGroupFault (96), StatusGroupWarning (97), StatusInterlockingTimeActive (110), StatusOff (106), StatusOnForward (107), StatusOnForwardFast (108), StatusOnReverse (105), StatusOnReverseFast (104), StatusOperationalProtectionOff (119), StatusPauseTimeActive (123), StatusPhaseSequence123 (125), StatusPhaseSequence321 (126), StatusPLCPCSInRun (100), StatusPositionerRunsInCLOSEDDirection (113), StatusPositionerRunsInOPENDirection (112), StatusPROFIenergyCommandStartPausePending (102), StatusRemoteMode (120), StatusStartActive (109), StatusTestPosition (118), StatusTorqueCLOSED (116), StatusTorqueOPEN (117), Timer1Output (232), Timer2Output (233), Timer3Output (234), Timer4Output (235), Timer5Output (230), Timer6Output (231), TruthTable10Output (226), TruthTable11Output (227), TruthTable1Output (216), TruthTable2Output (217), TruthTable3Output (218), TruthTable4Output (219), TruthTable5Output (220), TruthTable6Output (221), TruthTable7Output (222), TruthTable8Output (223), TruthTable9Output1 (224), TruthTable9Output2 (225), WarningFeedbackCircuit (190), WarningSimultaneity (191)
    """

    AcyclicReceiveBit00 = None
    AcyclicReceiveBit01 = None
    AcyclicReceiveBit02 = None
    AcyclicReceiveBit03 = None
    AcyclicReceiveBit04 = None
    AcyclicReceiveBit05 = None
    AcyclicReceiveBit06 = None
    AcyclicReceiveBit07 = None
    AcyclicReceiveBit10 = None
    AcyclicReceiveBit11 = None
    AcyclicReceiveBit12 = None
    AcyclicReceiveBit13 = None
    AcyclicReceiveBit14 = None
    AcyclicReceiveBit15 = None
    AcyclicReceiveBit16 = None
    AcyclicReceiveBit17 = None
    BUInput1 = None
    BUInput2 = None
    BUInput3 = None
    BUInput4 = None
    BUTestResetButton = None
    ContactorControl1QE1 = None
    ContactorControl2QE2 = None
    ContactorControl3QE3 = None
    ContactorControl4QE4 = None
    ContactorControl5QE5 = None
    Counter1Output = None
    Counter2Output = None
    Counter3Output = None
    Counter4Output = None
    Counter5Output = None
    Counter6Output = None
    CyclicReceiveBit00 = None
    CyclicReceiveBit01 = None
    CyclicReceiveBit02 = None
    CyclicReceiveBit03 = None
    CyclicReceiveBit04 = None
    CyclicReceiveBit05 = None
    CyclicReceiveBit06 = None
    CyclicReceiveBit07 = None
    CyclicReceiveBit10 = None
    CyclicReceiveBit11 = None
    CyclicReceiveBit12 = None
    CyclicReceiveBit13 = None
    CyclicReceiveBit14 = None
    CyclicReceiveBit15 = None
    CyclicReceiveBit16 = None
    CyclicReceiveBit17 = None
    DisplayQLAOff = None
    DisplayQLEForward = None
    DisplayQLEForwardFast = None
    DisplayQLEReverse = None
    DisplayQLEReverseFast = None
    DisplayQLSFault = None
    DM1Input1 = None
    DM1Input2 = None
    DM1Input3 = None
    DM1Input4 = None
    DM1SensorChannel1 = None
    DM1SensorChannel2 = None
    DM2Input1 = None
    DM2Input2 = None
    DM2Input3 = None
    DM2Input4 = None
    EnabledControlCommandOff = None
    EnabledControlCommandOnForward = None
    EnabledControlCommandOnForwardFast = None
    EnabledControlCommandOnReverse = None
    EnabledControlCommandOnReverseFast = None
    EventAM1OpenCircuit = None
    EventAM1TripLevel0420mAGt = None
    EventAM1TripLevel0420mALt = None
    EventAM1WarningLevel0420mAGt = None
    EventAM1WarningLevel0420mALt = None
    EventAM2OpenCircuit = None
    EventAM2TripLevel0420mAGt = None
    EventAM2TripLevel0420mALt = None
    EventAM2WarningLevel0420mAGt = None
    EventAM2WarningLevel0420mALt = None
    EventConfiguredOperatorPanelMissing = None
    EventDMFLOCALOk = None
    EventExternalFault1 = None
    EventExternalFault2 = None
    EventExternalFault3 = None
    EventExternalFault4 = None
    EventExternalFault5 = None
    EventExternalFault6 = None
    EventExternalGroundFault = None
    EventExternalGroundFaultWarning = None
    EventInternalGroundFault = None
    EventJustOneStartPossible = None
    EventLimitMonitor1 = None
    EventLimitMonitor2 = None
    EventLimitMonitor3 = None
    EventLimitMonitor4 = None
    EventLimitMonitor5 = None
    EventLimitMonitor6 = None
    EventMonitoringPeriodForMandatoryTestingTestRequirement = None
    EventMotorOperatingHoursGt = None
    EventNoStartPermitted = None
    EventNumberOfStartsGt = None
    EventOverload = None
    EventOverloadAndPhaseFailure = None
    EventPrewarningOverload = None
    EventPROFIsafeActive = None
    EventSafetyrelatedTripping = None
    EventStalledRotor = None
    EventStopTimeGt = None
    EventThermistorOpenCircuit = None
    EventThermistorShortCircuit = None
    EventThermistorTripLevel = None
    EventTimestampfctActiveAndOk = None
    EventTM1OutOfRange = None
    EventTM1SensorFault = None
    EventTM1TripLevelTGt = None
    EventTM1WarningLevelTGt = None
    EventTM2OutOfRange = None
    EventTM2SensorFault = None
    EventTM2TripLevelTGt = None
    EventTM2WarningLevelTGt = None
    EventTripLevelCosPhiLt = None
    EventTripLevelIGt = None
    EventTripLevelILt = None
    EventTripLevelPGt = None
    EventTripLevelPLt = None
    EventTripLevelULt = None
    EventUnbalance = None
    EventWarningLevelCosPhiLt = None
    EventWarningLevelIGt = None
    EventWarningLevelILt = None
    EventWarningLevelPGt = None
    EventWarningLevelPLt = None
    EventWarningLevelULt = None
    FaultAntivalence = None
    FaultBus = None
    FaultConfigurationError = None
    FaultDouble0 = None
    FaultDouble1 = None
    FaultEndPosition = None
    FaultExecutionOnCommand = None
    FaultExecutionSTOPCommand = None
    FaultFeedbackOff = None
    FaultFeedbackOn = None
    FaultHardwareFaultBasicUnit = None
    FaultModuleFault = None
    FaultOperationalProtectionOff = None
    FaultParameterization = None
    FaultPLCPCS = None
    FaultPowerFailure = None
    FaultStalledPositioner = None
    FaultTemporaryComponents = None
    FaultTestPositionFeedback = None
    FixedLevel0 = None
    FixedLevel1 = None
    Flashing1Output = None
    Flashing2Output = None
    Flashing3Output = None
    Flicker1Output = None
    Flicker2Output = None
    Flicker3Output = None
    NonvolatileElement1Output = None
    NonvolatileElement2Output = None
    NonvolatileElement3Output = None
    NonvolatileElement4Output = None
    NotConnected = None
    OPButton1 = None
    OPButton2 = None
    OPButton3 = None
    OPButton4 = None
    OPTestResetButton = None
    PWMOutput = None
    SignalConditioning1Output = None
    SignalConditioning2Output = None
    SignalConditioning3Output = None
    SignalConditioning4Output = None
    SignalConditioning5Output = None
    SignalConditioning6Output = None
    StatusBusOk = None
    StatusChangeoverPauseActive = None
    StatusCoolingDownPeriodActive = None
    StatusCurrentFlowing = None
    StatusDeviceOk = None
    StatusDeviceTestActive = None
    StatusEmergencyStartExecuted = None
    StatusEnablingCircuitClosed = None
    StatusFeedbackCLOSED = None
    StatusFeedbackOPEN = None
    StatusGroupFault = None
    StatusGroupWarning = None
    StatusInterlockingTimeActive = None
    StatusOff = None
    StatusOnForward = None
    StatusOnForwardFast = None
    StatusOnReverse = None
    StatusOnReverseFast = None
    StatusOperationalProtectionOff = None
    StatusPauseTimeActive = None
    StatusPhaseSequence123 = None
    StatusPhaseSequence321 = None
    StatusPLCPCSInRun = None
    StatusPositionerRunsInCLOSEDDirection = None
    StatusPositionerRunsInOPENDirection = None
    StatusPROFIenergyCommandStartPausePending = None
    StatusRemoteMode = None
    StatusStartActive = None
    StatusTestPosition = None
    StatusTorqueCLOSED = None
    StatusTorqueOPEN = None
    Timer1Output = None
    Timer2Output = None
    Timer3Output = None
    Timer4Output = None
    Timer5Output = None
    Timer6Output = None
    TruthTable10Output = None
    TruthTable11Output = None
    TruthTable1Output = None
    TruthTable2Output = None
    TruthTable3Output = None
    TruthTable4Output = None
    TruthTable5Output = None
    TruthTable6Output = None
    TruthTable7Output = None
    TruthTable8Output = None
    TruthTable9Output1 = None
    TruthTable9Output2 = None
    value__ = None
    WarningFeedbackCircuit = None
    WarningSimultaneity = None

class ControlFunctionOFF(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Possible values for property ControlFunctionOFF

    enum ControlFunctionOFF, values: AcyclicReceiveBit00 (40), AcyclicReceiveBit01 (41), AcyclicReceiveBit02 (42), AcyclicReceiveBit03 (43), AcyclicReceiveBit04 (44), AcyclicReceiveBit05 (45), AcyclicReceiveBit06 (46), AcyclicReceiveBit07 (47), AcyclicReceiveBit10 (48), AcyclicReceiveBit11 (49), AcyclicReceiveBit12 (50), AcyclicReceiveBit13 (51), AcyclicReceiveBit14 (52), AcyclicReceiveBit15 (53), AcyclicReceiveBit16 (54), AcyclicReceiveBit17 (55), BUInput1 (9), BUInput2 (10), BUInput3 (11), BUInput4 (12), BUTestResetButton (8), ContactorControl1QE1 (80), ContactorControl2QE2 (81), ContactorControl3QE3 (82), ContactorControl4QE4 (83), ContactorControl5QE5 (84), Counter1Output (236), Counter2Output (237), Counter3Output (238), Counter4Output (239), Counter5Output (228), Counter6Output (229), CyclicReceiveBit00 (56), CyclicReceiveBit01 (57), CyclicReceiveBit02 (58), CyclicReceiveBit03 (59), CyclicReceiveBit04 (60), CyclicReceiveBit05 (61), CyclicReceiveBit06 (62), CyclicReceiveBit07 (63), CyclicReceiveBit10 (64), CyclicReceiveBit11 (65), CyclicReceiveBit12 (66), CyclicReceiveBit13 (67), CyclicReceiveBit14 (68), CyclicReceiveBit15 (69), CyclicReceiveBit16 (70), CyclicReceiveBit17 (71), DisplayQLAOff (90), DisplayQLEForward (91), DisplayQLEForwardFast (92), DisplayQLEReverse (89), DisplayQLEReverseFast (88), DisplayQLSFault (93), DM1Input1 (16), DM1Input2 (17), DM1Input3 (18), DM1Input4 (19), DM1SensorChannel1 (24), DM1SensorChannel2 (25), DM2Input1 (20), DM2Input2 (21), DM2Input3 (22), DM2Input4 (23), EnabledControlCommandOff (74), EnabledControlCommandOnForward (75), EnabledControlCommandOnForwardFast (76), EnabledControlCommandOnReverse (73), EnabledControlCommandOnReverseFast (72), EventAM1OpenCircuit (180), EventAM1TripLevel0420mAGt (158), EventAM1TripLevel0420mALt (159), EventAM1WarningLevel0420mAGt (150), EventAM1WarningLevel0420mALt (151), EventAM2OpenCircuit (179), EventAM2TripLevel0420mAGt (6), EventAM2TripLevel0420mALt (7), EventAM2WarningLevel0420mAGt (4), EventAM2WarningLevel0420mALt (5), EventConfiguredOperatorPanelMissing (188), EventDMFLOCALOk (186), EventExternalFault1 (172), EventExternalFault2 (173), EventExternalFault3 (174), EventExternalFault4 (175), EventExternalFault5 (176), EventExternalFault6 (177), EventExternalGroundFault (133), EventExternalGroundFaultWarning (134), EventInternalGroundFault (132), EventJustOneStartPossible (165), EventLimitMonitor1 (168), EventLimitMonitor2 (169), EventLimitMonitor3 (170), EventLimitMonitor4 (171), EventLimitMonitor5 (38), EventLimitMonitor6 (39), EventMonitoringPeriodForMandatoryTestingTestRequirement (182), EventMotorOperatingHoursGt (166), EventNoStartPermitted (163), EventNumberOfStartsGt (164), EventOverload (130), EventOverloadAndPhaseFailure (131), EventPrewarningOverload (128), EventPROFIsafeActive (187), EventSafetyrelatedTripping (181), EventStalledRotor (160), EventStopTimeGt (167), EventThermistorOpenCircuit (137), EventThermistorShortCircuit (136), EventThermistorTripLevel (135), EventTimestampfctActiveAndOk (184), EventTM1OutOfRange (141), EventTM1SensorFault (140), EventTM1TripLevelTGt (139), EventTM1WarningLevelTGt (138), EventTM2OutOfRange (29), EventTM2SensorFault (28), EventTM2TripLevelTGt (31), EventTM2WarningLevelTGt (30), EventTripLevelCosPhiLt (156), EventTripLevelIGt (152), EventTripLevelILt (153), EventTripLevelPGt (154), EventTripLevelPLt (155), EventTripLevelULt (157), EventUnbalance (129), EventWarningLevelCosPhiLt (148), EventWarningLevelIGt (144), EventWarningLevelILt (145), EventWarningLevelPGt (146), EventWarningLevelPLt (147), EventWarningLevelULt (149), FaultAntivalence (208), FaultBus (197), FaultConfigurationError (195), FaultDouble0 (205), FaultDouble1 (206), FaultEndPosition (207), FaultExecutionOnCommand (200), FaultExecutionSTOPCommand (201), FaultFeedbackOff (203), FaultFeedbackOn (202), FaultHardwareFaultBasicUnit (192), FaultModuleFault (193), FaultOperationalProtectionOff (211), FaultParameterization (196), FaultPLCPCS (198), FaultPowerFailure (210), FaultStalledPositioner (204), FaultTemporaryComponents (194), FaultTestPositionFeedback (209), FixedLevel0 (1), FixedLevel1 (2), Flashing1Output (248), Flashing2Output (249), Flashing3Output (250), Flicker1Output (251), Flicker2Output (252), Flicker3Output (253), NonvolatileElement1Output (244), NonvolatileElement2Output (245), NonvolatileElement3Output (246), NonvolatileElement4Output (247), NotConnected (0), OPButton1 (33), OPButton2 (34), OPButton3 (35), OPButton4 (36), OPTestResetButton (32), PWMOutput (254), SignalConditioning1Output (240), SignalConditioning2Output (241), SignalConditioning3Output (242), SignalConditioning4Output (243), SignalConditioning5Output (214), SignalConditioning6Output (215), StatusBusOk (99), StatusChangeoverPauseActive (111), StatusCoolingDownPeriodActive (122), StatusCurrentFlowing (101), StatusDeviceOk (98), StatusDeviceTestActive (124), StatusEmergencyStartExecuted (121), StatusEnablingCircuitClosed (127), StatusFeedbackCLOSED (114), StatusFeedbackOPEN (115), StatusGroupFault (96), StatusGroupWarning (97), StatusInterlockingTimeActive (110), StatusOff (106), StatusOnForward (107), StatusOnForwardFast (108), StatusOnReverse (105), StatusOnReverseFast (104), StatusOperationalProtectionOff (119), StatusPauseTimeActive (123), StatusPhaseSequence123 (125), StatusPhaseSequence321 (126), StatusPLCPCSInRun (100), StatusPositionerRunsInCLOSEDDirection (113), StatusPositionerRunsInOPENDirection (112), StatusPROFIenergyCommandStartPausePending (102), StatusRemoteMode (120), StatusStartActive (109), StatusTestPosition (118), StatusTorqueCLOSED (116), StatusTorqueOPEN (117), Timer1Output (232), Timer2Output (233), Timer3Output (234), Timer4Output (235), Timer5Output (230), Timer6Output (231), TruthTable10Output (226), TruthTable11Output (227), TruthTable1Output (216), TruthTable2Output (217), TruthTable3Output (218), TruthTable4Output (219), TruthTable5Output (220), TruthTable6Output (221), TruthTable7Output (222), TruthTable8Output (223), TruthTable9Output1 (224), TruthTable9Output2 (225), WarningFeedbackCircuit (190), WarningSimultaneity (191)
    """

    AcyclicReceiveBit00 = None
    AcyclicReceiveBit01 = None
    AcyclicReceiveBit02 = None
    AcyclicReceiveBit03 = None
    AcyclicReceiveBit04 = None
    AcyclicReceiveBit05 = None
    AcyclicReceiveBit06 = None
    AcyclicReceiveBit07 = None
    AcyclicReceiveBit10 = None
    AcyclicReceiveBit11 = None
    AcyclicReceiveBit12 = None
    AcyclicReceiveBit13 = None
    AcyclicReceiveBit14 = None
    AcyclicReceiveBit15 = None
    AcyclicReceiveBit16 = None
    AcyclicReceiveBit17 = None
    BUInput1 = None
    BUInput2 = None
    BUInput3 = None
    BUInput4 = None
    BUTestResetButton = None
    ContactorControl1QE1 = None
    ContactorControl2QE2 = None
    ContactorControl3QE3 = None
    ContactorControl4QE4 = None
    ContactorControl5QE5 = None
    Counter1Output = None
    Counter2Output = None
    Counter3Output = None
    Counter4Output = None
    Counter5Output = None
    Counter6Output = None
    CyclicReceiveBit00 = None
    CyclicReceiveBit01 = None
    CyclicReceiveBit02 = None
    CyclicReceiveBit03 = None
    CyclicReceiveBit04 = None
    CyclicReceiveBit05 = None
    CyclicReceiveBit06 = None
    CyclicReceiveBit07 = None
    CyclicReceiveBit10 = None
    CyclicReceiveBit11 = None
    CyclicReceiveBit12 = None
    CyclicReceiveBit13 = None
    CyclicReceiveBit14 = None
    CyclicReceiveBit15 = None
    CyclicReceiveBit16 = None
    CyclicReceiveBit17 = None
    DisplayQLAOff = None
    DisplayQLEForward = None
    DisplayQLEForwardFast = None
    DisplayQLEReverse = None
    DisplayQLEReverseFast = None
    DisplayQLSFault = None
    DM1Input1 = None
    DM1Input2 = None
    DM1Input3 = None
    DM1Input4 = None
    DM1SensorChannel1 = None
    DM1SensorChannel2 = None
    DM2Input1 = None
    DM2Input2 = None
    DM2Input3 = None
    DM2Input4 = None
    EnabledControlCommandOff = None
    EnabledControlCommandOnForward = None
    EnabledControlCommandOnForwardFast = None
    EnabledControlCommandOnReverse = None
    EnabledControlCommandOnReverseFast = None
    EventAM1OpenCircuit = None
    EventAM1TripLevel0420mAGt = None
    EventAM1TripLevel0420mALt = None
    EventAM1WarningLevel0420mAGt = None
    EventAM1WarningLevel0420mALt = None
    EventAM2OpenCircuit = None
    EventAM2TripLevel0420mAGt = None
    EventAM2TripLevel0420mALt = None
    EventAM2WarningLevel0420mAGt = None
    EventAM2WarningLevel0420mALt = None
    EventConfiguredOperatorPanelMissing = None
    EventDMFLOCALOk = None
    EventExternalFault1 = None
    EventExternalFault2 = None
    EventExternalFault3 = None
    EventExternalFault4 = None
    EventExternalFault5 = None
    EventExternalFault6 = None
    EventExternalGroundFault = None
    EventExternalGroundFaultWarning = None
    EventInternalGroundFault = None
    EventJustOneStartPossible = None
    EventLimitMonitor1 = None
    EventLimitMonitor2 = None
    EventLimitMonitor3 = None
    EventLimitMonitor4 = None
    EventLimitMonitor5 = None
    EventLimitMonitor6 = None
    EventMonitoringPeriodForMandatoryTestingTestRequirement = None
    EventMotorOperatingHoursGt = None
    EventNoStartPermitted = None
    EventNumberOfStartsGt = None
    EventOverload = None
    EventOverloadAndPhaseFailure = None
    EventPrewarningOverload = None
    EventPROFIsafeActive = None
    EventSafetyrelatedTripping = None
    EventStalledRotor = None
    EventStopTimeGt = None
    EventThermistorOpenCircuit = None
    EventThermistorShortCircuit = None
    EventThermistorTripLevel = None
    EventTimestampfctActiveAndOk = None
    EventTM1OutOfRange = None
    EventTM1SensorFault = None
    EventTM1TripLevelTGt = None
    EventTM1WarningLevelTGt = None
    EventTM2OutOfRange = None
    EventTM2SensorFault = None
    EventTM2TripLevelTGt = None
    EventTM2WarningLevelTGt = None
    EventTripLevelCosPhiLt = None
    EventTripLevelIGt = None
    EventTripLevelILt = None
    EventTripLevelPGt = None
    EventTripLevelPLt = None
    EventTripLevelULt = None
    EventUnbalance = None
    EventWarningLevelCosPhiLt = None
    EventWarningLevelIGt = None
    EventWarningLevelILt = None
    EventWarningLevelPGt = None
    EventWarningLevelPLt = None
    EventWarningLevelULt = None
    FaultAntivalence = None
    FaultBus = None
    FaultConfigurationError = None
    FaultDouble0 = None
    FaultDouble1 = None
    FaultEndPosition = None
    FaultExecutionOnCommand = None
    FaultExecutionSTOPCommand = None
    FaultFeedbackOff = None
    FaultFeedbackOn = None
    FaultHardwareFaultBasicUnit = None
    FaultModuleFault = None
    FaultOperationalProtectionOff = None
    FaultParameterization = None
    FaultPLCPCS = None
    FaultPowerFailure = None
    FaultStalledPositioner = None
    FaultTemporaryComponents = None
    FaultTestPositionFeedback = None
    FixedLevel0 = None
    FixedLevel1 = None
    Flashing1Output = None
    Flashing2Output = None
    Flashing3Output = None
    Flicker1Output = None
    Flicker2Output = None
    Flicker3Output = None
    NonvolatileElement1Output = None
    NonvolatileElement2Output = None
    NonvolatileElement3Output = None
    NonvolatileElement4Output = None
    NotConnected = None
    OPButton1 = None
    OPButton2 = None
    OPButton3 = None
    OPButton4 = None
    OPTestResetButton = None
    PWMOutput = None
    SignalConditioning1Output = None
    SignalConditioning2Output = None
    SignalConditioning3Output = None
    SignalConditioning4Output = None
    SignalConditioning5Output = None
    SignalConditioning6Output = None
    StatusBusOk = None
    StatusChangeoverPauseActive = None
    StatusCoolingDownPeriodActive = None
    StatusCurrentFlowing = None
    StatusDeviceOk = None
    StatusDeviceTestActive = None
    StatusEmergencyStartExecuted = None
    StatusEnablingCircuitClosed = None
    StatusFeedbackCLOSED = None
    StatusFeedbackOPEN = None
    StatusGroupFault = None
    StatusGroupWarning = None
    StatusInterlockingTimeActive = None
    StatusOff = None
    StatusOnForward = None
    StatusOnForwardFast = None
    StatusOnReverse = None
    StatusOnReverseFast = None
    StatusOperationalProtectionOff = None
    StatusPauseTimeActive = None
    StatusPhaseSequence123 = None
    StatusPhaseSequence321 = None
    StatusPLCPCSInRun = None
    StatusPositionerRunsInCLOSEDDirection = None
    StatusPositionerRunsInOPENDirection = None
    StatusPROFIenergyCommandStartPausePending = None
    StatusRemoteMode = None
    StatusStartActive = None
    StatusTestPosition = None
    StatusTorqueCLOSED = None
    StatusTorqueOPEN = None
    Timer1Output = None
    Timer2Output = None
    Timer3Output = None
    Timer4Output = None
    Timer5Output = None
    Timer6Output = None
    TruthTable10Output = None
    TruthTable11Output = None
    TruthTable1Output = None
    TruthTable2Output = None
    TruthTable3Output = None
    TruthTable4Output = None
    TruthTable5Output = None
    TruthTable6Output = None
    TruthTable7Output = None
    TruthTable8Output = None
    TruthTable9Output1 = None
    TruthTable9Output2 = None
    value__ = None
    WarningFeedbackCircuit = None
    WarningSimultaneity = None

class ControlFunctionReverse(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Possible values for property ControlFunctionReverse

    enum ControlFunctionReverse, values: AcyclicReceiveBit00 (40), AcyclicReceiveBit01 (41), AcyclicReceiveBit02 (42), AcyclicReceiveBit03 (43), AcyclicReceiveBit04 (44), AcyclicReceiveBit05 (45), AcyclicReceiveBit06 (46), AcyclicReceiveBit07 (47), AcyclicReceiveBit10 (48), AcyclicReceiveBit11 (49), AcyclicReceiveBit12 (50), AcyclicReceiveBit13 (51), AcyclicReceiveBit14 (52), AcyclicReceiveBit15 (53), AcyclicReceiveBit16 (54), AcyclicReceiveBit17 (55), BUInput1 (9), BUInput2 (10), BUInput3 (11), BUInput4 (12), BUTestResetButton (8), ContactorControl1QE1 (80), ContactorControl2QE2 (81), ContactorControl3QE3 (82), ContactorControl4QE4 (83), ContactorControl5QE5 (84), Counter1Output (236), Counter2Output (237), Counter3Output (238), Counter4Output (239), Counter5Output (228), Counter6Output (229), CyclicReceiveBit00 (56), CyclicReceiveBit01 (57), CyclicReceiveBit02 (58), CyclicReceiveBit03 (59), CyclicReceiveBit04 (60), CyclicReceiveBit05 (61), CyclicReceiveBit06 (62), CyclicReceiveBit07 (63), CyclicReceiveBit10 (64), CyclicReceiveBit11 (65), CyclicReceiveBit12 (66), CyclicReceiveBit13 (67), CyclicReceiveBit14 (68), CyclicReceiveBit15 (69), CyclicReceiveBit16 (70), CyclicReceiveBit17 (71), DisplayQLAOff (90), DisplayQLEForward (91), DisplayQLEForwardFast (92), DisplayQLEReverse (89), DisplayQLEReverseFast (88), DisplayQLSFault (93), DM1Input1 (16), DM1Input2 (17), DM1Input3 (18), DM1Input4 (19), DM1SensorChannel1 (24), DM1SensorChannel2 (25), DM2Input1 (20), DM2Input2 (21), DM2Input3 (22), DM2Input4 (23), EnabledControlCommandOff (74), EnabledControlCommandOnForward (75), EnabledControlCommandOnForwardFast (76), EnabledControlCommandOnReverse (73), EnabledControlCommandOnReverseFast (72), EventAM1OpenCircuit (180), EventAM1TripLevel0420mAGt (158), EventAM1TripLevel0420mALt (159), EventAM1WarningLevel0420mAGt (150), EventAM1WarningLevel0420mALt (151), EventAM2OpenCircuit (179), EventAM2TripLevel0420mAGt (6), EventAM2TripLevel0420mALt (7), EventAM2WarningLevel0420mAGt (4), EventAM2WarningLevel0420mALt (5), EventConfiguredOperatorPanelMissing (188), EventDMFLOCALOk (186), EventExternalFault1 (172), EventExternalFault2 (173), EventExternalFault3 (174), EventExternalFault4 (175), EventExternalFault5 (176), EventExternalFault6 (177), EventExternalGroundFault (133), EventExternalGroundFaultWarning (134), EventInternalGroundFault (132), EventJustOneStartPossible (165), EventLimitMonitor1 (168), EventLimitMonitor2 (169), EventLimitMonitor3 (170), EventLimitMonitor4 (171), EventLimitMonitor5 (38), EventLimitMonitor6 (39), EventMonitoringPeriodForMandatoryTestingTestRequirement (182), EventMotorOperatingHoursGt (166), EventNoStartPermitted (163), EventNumberOfStartsGt (164), EventOverload (130), EventOverloadAndPhaseFailure (131), EventPrewarningOverload (128), EventPROFIsafeActive (187), EventSafetyrelatedTripping (181), EventStalledRotor (160), EventStopTimeGt (167), EventThermistorOpenCircuit (137), EventThermistorShortCircuit (136), EventThermistorTripLevel (135), EventTimestampfctActiveAndOk (184), EventTM1OutOfRange (141), EventTM1SensorFault (140), EventTM1TripLevelTGt (139), EventTM1WarningLevelTGt (138), EventTM2OutOfRange (29), EventTM2SensorFault (28), EventTM2TripLevelTGt (31), EventTM2WarningLevelTGt (30), EventTripLevelCosPhiLt (156), EventTripLevelIGt (152), EventTripLevelILt (153), EventTripLevelPGt (154), EventTripLevelPLt (155), EventTripLevelULt (157), EventUnbalance (129), EventWarningLevelCosPhiLt (148), EventWarningLevelIGt (144), EventWarningLevelILt (145), EventWarningLevelPGt (146), EventWarningLevelPLt (147), EventWarningLevelULt (149), FaultAntivalence (208), FaultBus (197), FaultConfigurationError (195), FaultDouble0 (205), FaultDouble1 (206), FaultEndPosition (207), FaultExecutionOnCommand (200), FaultExecutionSTOPCommand (201), FaultFeedbackOff (203), FaultFeedbackOn (202), FaultHardwareFaultBasicUnit (192), FaultModuleFault (193), FaultOperationalProtectionOff (211), FaultParameterization (196), FaultPLCPCS (198), FaultPowerFailure (210), FaultStalledPositioner (204), FaultTemporaryComponents (194), FaultTestPositionFeedback (209), FixedLevel0 (1), FixedLevel1 (2), Flashing1Output (248), Flashing2Output (249), Flashing3Output (250), Flicker1Output (251), Flicker2Output (252), Flicker3Output (253), NonvolatileElement1Output (244), NonvolatileElement2Output (245), NonvolatileElement3Output (246), NonvolatileElement4Output (247), NotConnected (0), OPButton1 (33), OPButton2 (34), OPButton3 (35), OPButton4 (36), OPTestResetButton (32), PWMOutput (254), SignalConditioning1Output (240), SignalConditioning2Output (241), SignalConditioning3Output (242), SignalConditioning4Output (243), SignalConditioning5Output (214), SignalConditioning6Output (215), StatusBusOk (99), StatusChangeoverPauseActive (111), StatusCoolingDownPeriodActive (122), StatusCurrentFlowing (101), StatusDeviceOk (98), StatusDeviceTestActive (124), StatusEmergencyStartExecuted (121), StatusEnablingCircuitClosed (127), StatusFeedbackCLOSED (114), StatusFeedbackOPEN (115), StatusGroupFault (96), StatusGroupWarning (97), StatusInterlockingTimeActive (110), StatusOff (106), StatusOnForward (107), StatusOnForwardFast (108), StatusOnReverse (105), StatusOnReverseFast (104), StatusOperationalProtectionOff (119), StatusPauseTimeActive (123), StatusPhaseSequence123 (125), StatusPhaseSequence321 (126), StatusPLCPCSInRun (100), StatusPositionerRunsInCLOSEDDirection (113), StatusPositionerRunsInOPENDirection (112), StatusPROFIenergyCommandStartPausePending (102), StatusRemoteMode (120), StatusStartActive (109), StatusTestPosition (118), StatusTorqueCLOSED (116), StatusTorqueOPEN (117), Timer1Output (232), Timer2Output (233), Timer3Output (234), Timer4Output (235), Timer5Output (230), Timer6Output (231), TruthTable10Output (226), TruthTable11Output (227), TruthTable1Output (216), TruthTable2Output (217), TruthTable3Output (218), TruthTable4Output (219), TruthTable5Output (220), TruthTable6Output (221), TruthTable7Output (222), TruthTable8Output (223), TruthTable9Output1 (224), TruthTable9Output2 (225), WarningFeedbackCircuit (190), WarningSimultaneity (191)
    """

    AcyclicReceiveBit00 = None
    AcyclicReceiveBit01 = None
    AcyclicReceiveBit02 = None
    AcyclicReceiveBit03 = None
    AcyclicReceiveBit04 = None
    AcyclicReceiveBit05 = None
    AcyclicReceiveBit06 = None
    AcyclicReceiveBit07 = None
    AcyclicReceiveBit10 = None
    AcyclicReceiveBit11 = None
    AcyclicReceiveBit12 = None
    AcyclicReceiveBit13 = None
    AcyclicReceiveBit14 = None
    AcyclicReceiveBit15 = None
    AcyclicReceiveBit16 = None
    AcyclicReceiveBit17 = None
    BUInput1 = None
    BUInput2 = None
    BUInput3 = None
    BUInput4 = None
    BUTestResetButton = None
    ContactorControl1QE1 = None
    ContactorControl2QE2 = None
    ContactorControl3QE3 = None
    ContactorControl4QE4 = None
    ContactorControl5QE5 = None
    Counter1Output = None
    Counter2Output = None
    Counter3Output = None
    Counter4Output = None
    Counter5Output = None
    Counter6Output = None
    CyclicReceiveBit00 = None
    CyclicReceiveBit01 = None
    CyclicReceiveBit02 = None
    CyclicReceiveBit03 = None
    CyclicReceiveBit04 = None
    CyclicReceiveBit05 = None
    CyclicReceiveBit06 = None
    CyclicReceiveBit07 = None
    CyclicReceiveBit10 = None
    CyclicReceiveBit11 = None
    CyclicReceiveBit12 = None
    CyclicReceiveBit13 = None
    CyclicReceiveBit14 = None
    CyclicReceiveBit15 = None
    CyclicReceiveBit16 = None
    CyclicReceiveBit17 = None
    DisplayQLAOff = None
    DisplayQLEForward = None
    DisplayQLEForwardFast = None
    DisplayQLEReverse = None
    DisplayQLEReverseFast = None
    DisplayQLSFault = None
    DM1Input1 = None
    DM1Input2 = None
    DM1Input3 = None
    DM1Input4 = None
    DM1SensorChannel1 = None
    DM1SensorChannel2 = None
    DM2Input1 = None
    DM2Input2 = None
    DM2Input3 = None
    DM2Input4 = None
    EnabledControlCommandOff = None
    EnabledControlCommandOnForward = None
    EnabledControlCommandOnForwardFast = None
    EnabledControlCommandOnReverse = None
    EnabledControlCommandOnReverseFast = None
    EventAM1OpenCircuit = None
    EventAM1TripLevel0420mAGt = None
    EventAM1TripLevel0420mALt = None
    EventAM1WarningLevel0420mAGt = None
    EventAM1WarningLevel0420mALt = None
    EventAM2OpenCircuit = None
    EventAM2TripLevel0420mAGt = None
    EventAM2TripLevel0420mALt = None
    EventAM2WarningLevel0420mAGt = None
    EventAM2WarningLevel0420mALt = None
    EventConfiguredOperatorPanelMissing = None
    EventDMFLOCALOk = None
    EventExternalFault1 = None
    EventExternalFault2 = None
    EventExternalFault3 = None
    EventExternalFault4 = None
    EventExternalFault5 = None
    EventExternalFault6 = None
    EventExternalGroundFault = None
    EventExternalGroundFaultWarning = None
    EventInternalGroundFault = None
    EventJustOneStartPossible = None
    EventLimitMonitor1 = None
    EventLimitMonitor2 = None
    EventLimitMonitor3 = None
    EventLimitMonitor4 = None
    EventLimitMonitor5 = None
    EventLimitMonitor6 = None
    EventMonitoringPeriodForMandatoryTestingTestRequirement = None
    EventMotorOperatingHoursGt = None
    EventNoStartPermitted = None
    EventNumberOfStartsGt = None
    EventOverload = None
    EventOverloadAndPhaseFailure = None
    EventPrewarningOverload = None
    EventPROFIsafeActive = None
    EventSafetyrelatedTripping = None
    EventStalledRotor = None
    EventStopTimeGt = None
    EventThermistorOpenCircuit = None
    EventThermistorShortCircuit = None
    EventThermistorTripLevel = None
    EventTimestampfctActiveAndOk = None
    EventTM1OutOfRange = None
    EventTM1SensorFault = None
    EventTM1TripLevelTGt = None
    EventTM1WarningLevelTGt = None
    EventTM2OutOfRange = None
    EventTM2SensorFault = None
    EventTM2TripLevelTGt = None
    EventTM2WarningLevelTGt = None
    EventTripLevelCosPhiLt = None
    EventTripLevelIGt = None
    EventTripLevelILt = None
    EventTripLevelPGt = None
    EventTripLevelPLt = None
    EventTripLevelULt = None
    EventUnbalance = None
    EventWarningLevelCosPhiLt = None
    EventWarningLevelIGt = None
    EventWarningLevelILt = None
    EventWarningLevelPGt = None
    EventWarningLevelPLt = None
    EventWarningLevelULt = None
    FaultAntivalence = None
    FaultBus = None
    FaultConfigurationError = None
    FaultDouble0 = None
    FaultDouble1 = None
    FaultEndPosition = None
    FaultExecutionOnCommand = None
    FaultExecutionSTOPCommand = None
    FaultFeedbackOff = None
    FaultFeedbackOn = None
    FaultHardwareFaultBasicUnit = None
    FaultModuleFault = None
    FaultOperationalProtectionOff = None
    FaultParameterization = None
    FaultPLCPCS = None
    FaultPowerFailure = None
    FaultStalledPositioner = None
    FaultTemporaryComponents = None
    FaultTestPositionFeedback = None
    FixedLevel0 = None
    FixedLevel1 = None
    Flashing1Output = None
    Flashing2Output = None
    Flashing3Output = None
    Flicker1Output = None
    Flicker2Output = None
    Flicker3Output = None
    NonvolatileElement1Output = None
    NonvolatileElement2Output = None
    NonvolatileElement3Output = None
    NonvolatileElement4Output = None
    NotConnected = None
    OPButton1 = None
    OPButton2 = None
    OPButton3 = None
    OPButton4 = None
    OPTestResetButton = None
    PWMOutput = None
    SignalConditioning1Output = None
    SignalConditioning2Output = None
    SignalConditioning3Output = None
    SignalConditioning4Output = None
    SignalConditioning5Output = None
    SignalConditioning6Output = None
    StatusBusOk = None
    StatusChangeoverPauseActive = None
    StatusCoolingDownPeriodActive = None
    StatusCurrentFlowing = None
    StatusDeviceOk = None
    StatusDeviceTestActive = None
    StatusEmergencyStartExecuted = None
    StatusEnablingCircuitClosed = None
    StatusFeedbackCLOSED = None
    StatusFeedbackOPEN = None
    StatusGroupFault = None
    StatusGroupWarning = None
    StatusInterlockingTimeActive = None
    StatusOff = None
    StatusOnForward = None
    StatusOnForwardFast = None
    StatusOnReverse = None
    StatusOnReverseFast = None
    StatusOperationalProtectionOff = None
    StatusPauseTimeActive = None
    StatusPhaseSequence123 = None
    StatusPhaseSequence321 = None
    StatusPLCPCSInRun = None
    StatusPositionerRunsInCLOSEDDirection = None
    StatusPositionerRunsInOPENDirection = None
    StatusPROFIenergyCommandStartPausePending = None
    StatusRemoteMode = None
    StatusStartActive = None
    StatusTestPosition = None
    StatusTorqueCLOSED = None
    StatusTorqueOPEN = None
    Timer1Output = None
    Timer2Output = None
    Timer3Output = None
    Timer4Output = None
    Timer5Output = None
    Timer6Output = None
    TruthTable10Output = None
    TruthTable11Output = None
    TruthTable1Output = None
    TruthTable2Output = None
    TruthTable3Output = None
    TruthTable4Output = None
    TruthTable5Output = None
    TruthTable6Output = None
    TruthTable7Output = None
    TruthTable8Output = None
    TruthTable9Output1 = None
    TruthTable9Output2 = None
    value__ = None
    WarningFeedbackCircuit = None
    WarningSimultaneity = None

class ControlFunctionReverseFast(
    Enum
):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Possible values for property ControlFunctionReverseFast

    enum ControlFunctionReverseFast, values: AcyclicReceiveBit00 (40), AcyclicReceiveBit01 (41), AcyclicReceiveBit02 (42), AcyclicReceiveBit03 (43), AcyclicReceiveBit04 (44), AcyclicReceiveBit05 (45), AcyclicReceiveBit06 (46), AcyclicReceiveBit07 (47), AcyclicReceiveBit10 (48), AcyclicReceiveBit11 (49), AcyclicReceiveBit12 (50), AcyclicReceiveBit13 (51), AcyclicReceiveBit14 (52), AcyclicReceiveBit15 (53), AcyclicReceiveBit16 (54), AcyclicReceiveBit17 (55), BUInput1 (9), BUInput2 (10), BUInput3 (11), BUInput4 (12), BUTestResetButton (8), ContactorControl1QE1 (80), ContactorControl2QE2 (81), ContactorControl3QE3 (82), ContactorControl4QE4 (83), ContactorControl5QE5 (84), Counter1Output (236), Counter2Output (237), Counter3Output (238), Counter4Output (239), Counter5Output (228), Counter6Output (229), CyclicReceiveBit00 (56), CyclicReceiveBit01 (57), CyclicReceiveBit02 (58), CyclicReceiveBit03 (59), CyclicReceiveBit04 (60), CyclicReceiveBit05 (61), CyclicReceiveBit06 (62), CyclicReceiveBit07 (63), CyclicReceiveBit10 (64), CyclicReceiveBit11 (65), CyclicReceiveBit12 (66), CyclicReceiveBit13 (67), CyclicReceiveBit14 (68), CyclicReceiveBit15 (69), CyclicReceiveBit16 (70), CyclicReceiveBit17 (71), DisplayQLAOff (90), DisplayQLEForward (91), DisplayQLEForwardFast (92), DisplayQLEReverse (89), DisplayQLEReverseFast (88), DisplayQLSFault (93), DM1Input1 (16), DM1Input2 (17), DM1Input3 (18), DM1Input4 (19), DM1SensorChannel1 (24), DM1SensorChannel2 (25), DM2Input1 (20), DM2Input2 (21), DM2Input3 (22), DM2Input4 (23), EnabledControlCommandOff (74), EnabledControlCommandOnForward (75), EnabledControlCommandOnForwardFast (76), EnabledControlCommandOnReverse (73), EnabledControlCommandOnReverseFast (72), EventAM1OpenCircuit (180), EventAM1TripLevel0420mAGt (158), EventAM1TripLevel0420mALt (159), EventAM1WarningLevel0420mAGt (150), EventAM1WarningLevel0420mALt (151), EventAM2OpenCircuit (179), EventAM2TripLevel0420mAGt (6), EventAM2TripLevel0420mALt (7), EventAM2WarningLevel0420mAGt (4), EventAM2WarningLevel0420mALt (5), EventConfiguredOperatorPanelMissing (188), EventDMFLOCALOk (186), EventExternalFault1 (172), EventExternalFault2 (173), EventExternalFault3 (174), EventExternalFault4 (175), EventExternalFault5 (176), EventExternalFault6 (177), EventExternalGroundFault (133), EventExternalGroundFaultWarning (134), EventInternalGroundFault (132), EventJustOneStartPossible (165), EventLimitMonitor1 (168), EventLimitMonitor2 (169), EventLimitMonitor3 (170), EventLimitMonitor4 (171), EventLimitMonitor5 (38), EventLimitMonitor6 (39), EventMonitoringPeriodForMandatoryTestingTestRequirement (182), EventMotorOperatingHoursGt (166), EventNoStartPermitted (163), EventNumberOfStartsGt (164), EventOverload (130), EventOverloadAndPhaseFailure (131), EventPrewarningOverload (128), EventPROFIsafeActive (187), EventSafetyrelatedTripping (181), EventStalledRotor (160), EventStopTimeGt (167), EventThermistorOpenCircuit (137), EventThermistorShortCircuit (136), EventThermistorTripLevel (135), EventTimestampfctActiveAndOk (184), EventTM1OutOfRange (141), EventTM1SensorFault (140), EventTM1TripLevelTGt (139), EventTM1WarningLevelTGt (138), EventTM2OutOfRange (29), EventTM2SensorFault (28), EventTM2TripLevelTGt (31), EventTM2WarningLevelTGt (30), EventTripLevelCosPhiLt (156), EventTripLevelIGt (152), EventTripLevelILt (153), EventTripLevelPGt (154), EventTripLevelPLt (155), EventTripLevelULt (157), EventUnbalance (129), EventWarningLevelCosPhiLt (148), EventWarningLevelIGt (144), EventWarningLevelILt (145), EventWarningLevelPGt (146), EventWarningLevelPLt (147), EventWarningLevelULt (149), FaultAntivalence (208), FaultBus (197), FaultConfigurationError (195), FaultDouble0 (205), FaultDouble1 (206), FaultEndPosition (207), FaultExecutionOnCommand (200), FaultExecutionSTOPCommand (201), FaultFeedbackOff (203), FaultFeedbackOn (202), FaultHardwareFaultBasicUnit (192), FaultModuleFault (193), FaultOperationalProtectionOff (211), FaultParameterization (196), FaultPLCPCS (198), FaultPowerFailure (210), FaultStalledPositioner (204), FaultTemporaryComponents (194), FaultTestPositionFeedback (209), FixedLevel0 (1), FixedLevel1 (2), Flashing1Output (248), Flashing2Output (249), Flashing3Output (250), Flicker1Output (251), Flicker2Output (252), Flicker3Output (253), NonvolatileElement1Output (244), NonvolatileElement2Output (245), NonvolatileElement3Output (246), NonvolatileElement4Output (247), NotConnected (0), OPButton1 (33), OPButton2 (34), OPButton3 (35), OPButton4 (36), OPTestResetButton (32), PWMOutput (254), SignalConditioning1Output (240), SignalConditioning2Output (241), SignalConditioning3Output (242), SignalConditioning4Output (243), SignalConditioning5Output (214), SignalConditioning6Output (215), StatusBusOk (99), StatusChangeoverPauseActive (111), StatusCoolingDownPeriodActive (122), StatusCurrentFlowing (101), StatusDeviceOk (98), StatusDeviceTestActive (124), StatusEmergencyStartExecuted (121), StatusEnablingCircuitClosed (127), StatusFeedbackCLOSED (114), StatusFeedbackOPEN (115), StatusGroupFault (96), StatusGroupWarning (97), StatusInterlockingTimeActive (110), StatusOff (106), StatusOnForward (107), StatusOnForwardFast (108), StatusOnReverse (105), StatusOnReverseFast (104), StatusOperationalProtectionOff (119), StatusPauseTimeActive (123), StatusPhaseSequence123 (125), StatusPhaseSequence321 (126), StatusPLCPCSInRun (100), StatusPositionerRunsInCLOSEDDirection (113), StatusPositionerRunsInOPENDirection (112), StatusPROFIenergyCommandStartPausePending (102), StatusRemoteMode (120), StatusStartActive (109), StatusTestPosition (118), StatusTorqueCLOSED (116), StatusTorqueOPEN (117), Timer1Output (232), Timer2Output (233), Timer3Output (234), Timer4Output (235), Timer5Output (230), Timer6Output (231), TruthTable10Output (226), TruthTable11Output (227), TruthTable1Output (216), TruthTable2Output (217), TruthTable3Output (218), TruthTable4Output (219), TruthTable5Output (220), TruthTable6Output (221), TruthTable7Output (222), TruthTable8Output (223), TruthTable9Output1 (224), TruthTable9Output2 (225), WarningFeedbackCircuit (190), WarningSimultaneity (191)
    """

    AcyclicReceiveBit00 = None
    AcyclicReceiveBit01 = None
    AcyclicReceiveBit02 = None
    AcyclicReceiveBit03 = None
    AcyclicReceiveBit04 = None
    AcyclicReceiveBit05 = None
    AcyclicReceiveBit06 = None
    AcyclicReceiveBit07 = None
    AcyclicReceiveBit10 = None
    AcyclicReceiveBit11 = None
    AcyclicReceiveBit12 = None
    AcyclicReceiveBit13 = None
    AcyclicReceiveBit14 = None
    AcyclicReceiveBit15 = None
    AcyclicReceiveBit16 = None
    AcyclicReceiveBit17 = None
    BUInput1 = None
    BUInput2 = None
    BUInput3 = None
    BUInput4 = None
    BUTestResetButton = None
    ContactorControl1QE1 = None
    ContactorControl2QE2 = None
    ContactorControl3QE3 = None
    ContactorControl4QE4 = None
    ContactorControl5QE5 = None
    Counter1Output = None
    Counter2Output = None
    Counter3Output = None
    Counter4Output = None
    Counter5Output = None
    Counter6Output = None
    CyclicReceiveBit00 = None
    CyclicReceiveBit01 = None
    CyclicReceiveBit02 = None
    CyclicReceiveBit03 = None
    CyclicReceiveBit04 = None
    CyclicReceiveBit05 = None
    CyclicReceiveBit06 = None
    CyclicReceiveBit07 = None
    CyclicReceiveBit10 = None
    CyclicReceiveBit11 = None
    CyclicReceiveBit12 = None
    CyclicReceiveBit13 = None
    CyclicReceiveBit14 = None
    CyclicReceiveBit15 = None
    CyclicReceiveBit16 = None
    CyclicReceiveBit17 = None
    DisplayQLAOff = None
    DisplayQLEForward = None
    DisplayQLEForwardFast = None
    DisplayQLEReverse = None
    DisplayQLEReverseFast = None
    DisplayQLSFault = None
    DM1Input1 = None
    DM1Input2 = None
    DM1Input3 = None
    DM1Input4 = None
    DM1SensorChannel1 = None
    DM1SensorChannel2 = None
    DM2Input1 = None
    DM2Input2 = None
    DM2Input3 = None
    DM2Input4 = None
    EnabledControlCommandOff = None
    EnabledControlCommandOnForward = None
    EnabledControlCommandOnForwardFast = None
    EnabledControlCommandOnReverse = None
    EnabledControlCommandOnReverseFast = None
    EventAM1OpenCircuit = None
    EventAM1TripLevel0420mAGt = None
    EventAM1TripLevel0420mALt = None
    EventAM1WarningLevel0420mAGt = None
    EventAM1WarningLevel0420mALt = None
    EventAM2OpenCircuit = None
    EventAM2TripLevel0420mAGt = None
    EventAM2TripLevel0420mALt = None
    EventAM2WarningLevel0420mAGt = None
    EventAM2WarningLevel0420mALt = None
    EventConfiguredOperatorPanelMissing = None
    EventDMFLOCALOk = None
    EventExternalFault1 = None
    EventExternalFault2 = None
    EventExternalFault3 = None
    EventExternalFault4 = None
    EventExternalFault5 = None
    EventExternalFault6 = None
    EventExternalGroundFault = None
    EventExternalGroundFaultWarning = None
    EventInternalGroundFault = None
    EventJustOneStartPossible = None
    EventLimitMonitor1 = None
    EventLimitMonitor2 = None
    EventLimitMonitor3 = None
    EventLimitMonitor4 = None
    EventLimitMonitor5 = None
    EventLimitMonitor6 = None
    EventMonitoringPeriodForMandatoryTestingTestRequirement = None
    EventMotorOperatingHoursGt = None
    EventNoStartPermitted = None
    EventNumberOfStartsGt = None
    EventOverload = None
    EventOverloadAndPhaseFailure = None
    EventPrewarningOverload = None
    EventPROFIsafeActive = None
    EventSafetyrelatedTripping = None
    EventStalledRotor = None
    EventStopTimeGt = None
    EventThermistorOpenCircuit = None
    EventThermistorShortCircuit = None
    EventThermistorTripLevel = None
    EventTimestampfctActiveAndOk = None
    EventTM1OutOfRange = None
    EventTM1SensorFault = None
    EventTM1TripLevelTGt = None
    EventTM1WarningLevelTGt = None
    EventTM2OutOfRange = None
    EventTM2SensorFault = None
    EventTM2TripLevelTGt = None
    EventTM2WarningLevelTGt = None
    EventTripLevelCosPhiLt = None
    EventTripLevelIGt = None
    EventTripLevelILt = None
    EventTripLevelPGt = None
    EventTripLevelPLt = None
    EventTripLevelULt = None
    EventUnbalance = None
    EventWarningLevelCosPhiLt = None
    EventWarningLevelIGt = None
    EventWarningLevelILt = None
    EventWarningLevelPGt = None
    EventWarningLevelPLt = None
    EventWarningLevelULt = None
    FaultAntivalence = None
    FaultBus = None
    FaultConfigurationError = None
    FaultDouble0 = None
    FaultDouble1 = None
    FaultEndPosition = None
    FaultExecutionOnCommand = None
    FaultExecutionSTOPCommand = None
    FaultFeedbackOff = None
    FaultFeedbackOn = None
    FaultHardwareFaultBasicUnit = None
    FaultModuleFault = None
    FaultOperationalProtectionOff = None
    FaultParameterization = None
    FaultPLCPCS = None
    FaultPowerFailure = None
    FaultStalledPositioner = None
    FaultTemporaryComponents = None
    FaultTestPositionFeedback = None
    FixedLevel0 = None
    FixedLevel1 = None
    Flashing1Output = None
    Flashing2Output = None
    Flashing3Output = None
    Flicker1Output = None
    Flicker2Output = None
    Flicker3Output = None
    NonvolatileElement1Output = None
    NonvolatileElement2Output = None
    NonvolatileElement3Output = None
    NonvolatileElement4Output = None
    NotConnected = None
    OPButton1 = None
    OPButton2 = None
    OPButton3 = None
    OPButton4 = None
    OPTestResetButton = None
    PWMOutput = None
    SignalConditioning1Output = None
    SignalConditioning2Output = None
    SignalConditioning3Output = None
    SignalConditioning4Output = None
    SignalConditioning5Output = None
    SignalConditioning6Output = None
    StatusBusOk = None
    StatusChangeoverPauseActive = None
    StatusCoolingDownPeriodActive = None
    StatusCurrentFlowing = None
    StatusDeviceOk = None
    StatusDeviceTestActive = None
    StatusEmergencyStartExecuted = None
    StatusEnablingCircuitClosed = None
    StatusFeedbackCLOSED = None
    StatusFeedbackOPEN = None
    StatusGroupFault = None
    StatusGroupWarning = None
    StatusInterlockingTimeActive = None
    StatusOff = None
    StatusOnForward = None
    StatusOnForwardFast = None
    StatusOnReverse = None
    StatusOnReverseFast = None
    StatusOperationalProtectionOff = None
    StatusPauseTimeActive = None
    StatusPhaseSequence123 = None
    StatusPhaseSequence321 = None
    StatusPLCPCSInRun = None
    StatusPositionerRunsInCLOSEDDirection = None
    StatusPositionerRunsInOPENDirection = None
    StatusPROFIenergyCommandStartPausePending = None
    StatusRemoteMode = None
    StatusStartActive = None
    StatusTestPosition = None
    StatusTorqueCLOSED = None
    StatusTorqueOPEN = None
    Timer1Output = None
    Timer2Output = None
    Timer3Output = None
    Timer4Output = None
    Timer5Output = None
    Timer6Output = None
    TruthTable10Output = None
    TruthTable11Output = None
    TruthTable1Output = None
    TruthTable2Output = None
    TruthTable3Output = None
    TruthTable4Output = None
    TruthTable5Output = None
    TruthTable6Output = None
    TruthTable7Output = None
    TruthTable8Output = None
    TruthTable9Output1 = None
    TruthTable9Output2 = None
    value__ = None
    WarningFeedbackCircuit = None
    WarningSimultaneity = None

class ControlFunctionTorqueCLOSEDTC(
    Enum
):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Possible values for property ControlFunctionTorqueCLOSEDTC

    enum ControlFunctionTorqueCLOSEDTC, values: AcyclicReceiveBit00 (40), AcyclicReceiveBit01 (41), AcyclicReceiveBit02 (42), AcyclicReceiveBit03 (43), AcyclicReceiveBit04 (44), AcyclicReceiveBit05 (45), AcyclicReceiveBit06 (46), AcyclicReceiveBit07 (47), AcyclicReceiveBit10 (48), AcyclicReceiveBit11 (49), AcyclicReceiveBit12 (50), AcyclicReceiveBit13 (51), AcyclicReceiveBit14 (52), AcyclicReceiveBit15 (53), AcyclicReceiveBit16 (54), AcyclicReceiveBit17 (55), BUInput1 (9), BUInput2 (10), BUInput3 (11), BUInput4 (12), BUTestResetButton (8), ContactorControl1QE1 (80), ContactorControl2QE2 (81), ContactorControl3QE3 (82), ContactorControl4QE4 (83), ContactorControl5QE5 (84), Counter1Output (236), Counter2Output (237), Counter3Output (238), Counter4Output (239), Counter5Output (228), Counter6Output (229), CyclicReceiveBit00 (56), CyclicReceiveBit01 (57), CyclicReceiveBit02 (58), CyclicReceiveBit03 (59), CyclicReceiveBit04 (60), CyclicReceiveBit05 (61), CyclicReceiveBit06 (62), CyclicReceiveBit07 (63), CyclicReceiveBit10 (64), CyclicReceiveBit11 (65), CyclicReceiveBit12 (66), CyclicReceiveBit13 (67), CyclicReceiveBit14 (68), CyclicReceiveBit15 (69), CyclicReceiveBit16 (70), CyclicReceiveBit17 (71), DisplayQLAOff (90), DisplayQLEForward (91), DisplayQLEForwardFast (92), DisplayQLEReverse (89), DisplayQLEReverseFast (88), DisplayQLSFault (93), DM1Input1 (16), DM1Input2 (17), DM1Input3 (18), DM1Input4 (19), DM1SensorChannel1 (24), DM1SensorChannel2 (25), DM2Input1 (20), DM2Input2 (21), DM2Input3 (22), DM2Input4 (23), EnabledControlCommandOff (74), EnabledControlCommandOnForward (75), EnabledControlCommandOnForwardFast (76), EnabledControlCommandOnReverse (73), EnabledControlCommandOnReverseFast (72), EventAM1OpenCircuit (180), EventAM1TripLevel0420mAGt (158), EventAM1TripLevel0420mALt (159), EventAM1WarningLevel0420mAGt (150), EventAM1WarningLevel0420mALt (151), EventAM2OpenCircuit (179), EventAM2TripLevel0420mAGt (6), EventAM2TripLevel0420mALt (7), EventAM2WarningLevel0420mAGt (4), EventAM2WarningLevel0420mALt (5), EventConfiguredOperatorPanelMissing (188), EventDMFLOCALOk (186), EventExternalFault1 (172), EventExternalFault2 (173), EventExternalFault3 (174), EventExternalFault4 (175), EventExternalFault5 (176), EventExternalFault6 (177), EventExternalGroundFault (133), EventExternalGroundFaultWarning (134), EventInternalGroundFault (132), EventJustOneStartPossible (165), EventLimitMonitor1 (168), EventLimitMonitor2 (169), EventLimitMonitor3 (170), EventLimitMonitor4 (171), EventLimitMonitor5 (38), EventLimitMonitor6 (39), EventMonitoringPeriodForMandatoryTestingTestRequirement (182), EventMotorOperatingHoursGt (166), EventNoStartPermitted (163), EventNumberOfStartsGt (164), EventOverload (130), EventOverloadAndPhaseFailure (131), EventPrewarningOverload (128), EventPROFIsafeActive (187), EventSafetyrelatedTripping (181), EventStalledRotor (160), EventStopTimeGt (167), EventThermistorOpenCircuit (137), EventThermistorShortCircuit (136), EventThermistorTripLevel (135), EventTimestampfctActiveAndOk (184), EventTM1OutOfRange (141), EventTM1SensorFault (140), EventTM1TripLevelTGt (139), EventTM1WarningLevelTGt (138), EventTM2OutOfRange (29), EventTM2SensorFault (28), EventTM2TripLevelTGt (31), EventTM2WarningLevelTGt (30), EventTripLevelCosPhiLt (156), EventTripLevelIGt (152), EventTripLevelILt (153), EventTripLevelPGt (154), EventTripLevelPLt (155), EventTripLevelULt (157), EventUnbalance (129), EventWarningLevelCosPhiLt (148), EventWarningLevelIGt (144), EventWarningLevelILt (145), EventWarningLevelPGt (146), EventWarningLevelPLt (147), EventWarningLevelULt (149), FaultAntivalence (208), FaultBus (197), FaultConfigurationError (195), FaultDouble0 (205), FaultDouble1 (206), FaultEndPosition (207), FaultExecutionOnCommand (200), FaultExecutionSTOPCommand (201), FaultFeedbackOff (203), FaultFeedbackOn (202), FaultHardwareFaultBasicUnit (192), FaultModuleFault (193), FaultOperationalProtectionOff (211), FaultParameterization (196), FaultPLCPCS (198), FaultPowerFailure (210), FaultStalledPositioner (204), FaultTemporaryComponents (194), FaultTestPositionFeedback (209), FixedLevel0 (1), FixedLevel1 (2), Flashing1Output (248), Flashing2Output (249), Flashing3Output (250), Flicker1Output (251), Flicker2Output (252), Flicker3Output (253), NonvolatileElement1Output (244), NonvolatileElement2Output (245), NonvolatileElement3Output (246), NonvolatileElement4Output (247), NotConnected (0), OPButton1 (33), OPButton2 (34), OPButton3 (35), OPButton4 (36), OPTestResetButton (32), PWMOutput (254), SignalConditioning1Output (240), SignalConditioning2Output (241), SignalConditioning3Output (242), SignalConditioning4Output (243), SignalConditioning5Output (214), SignalConditioning6Output (215), StatusBusOk (99), StatusChangeoverPauseActive (111), StatusCoolingDownPeriodActive (122), StatusCurrentFlowing (101), StatusDeviceOk (98), StatusDeviceTestActive (124), StatusEmergencyStartExecuted (121), StatusEnablingCircuitClosed (127), StatusFeedbackCLOSED (114), StatusFeedbackOPEN (115), StatusGroupFault (96), StatusGroupWarning (97), StatusInterlockingTimeActive (110), StatusOff (106), StatusOnForward (107), StatusOnForwardFast (108), StatusOnReverse (105), StatusOnReverseFast (104), StatusOperationalProtectionOff (119), StatusPauseTimeActive (123), StatusPhaseSequence123 (125), StatusPhaseSequence321 (126), StatusPLCPCSInRun (100), StatusPositionerRunsInCLOSEDDirection (113), StatusPositionerRunsInOPENDirection (112), StatusPROFIenergyCommandStartPausePending (102), StatusRemoteMode (120), StatusStartActive (109), StatusTestPosition (118), StatusTorqueCLOSED (116), StatusTorqueOPEN (117), Timer1Output (232), Timer2Output (233), Timer3Output (234), Timer4Output (235), Timer5Output (230), Timer6Output (231), TruthTable10Output (226), TruthTable11Output (227), TruthTable1Output (216), TruthTable2Output (217), TruthTable3Output (218), TruthTable4Output (219), TruthTable5Output (220), TruthTable6Output (221), TruthTable7Output (222), TruthTable8Output (223), TruthTable9Output1 (224), TruthTable9Output2 (225), WarningFeedbackCircuit (190), WarningSimultaneity (191)
    """

    AcyclicReceiveBit00 = None
    AcyclicReceiveBit01 = None
    AcyclicReceiveBit02 = None
    AcyclicReceiveBit03 = None
    AcyclicReceiveBit04 = None
    AcyclicReceiveBit05 = None
    AcyclicReceiveBit06 = None
    AcyclicReceiveBit07 = None
    AcyclicReceiveBit10 = None
    AcyclicReceiveBit11 = None
    AcyclicReceiveBit12 = None
    AcyclicReceiveBit13 = None
    AcyclicReceiveBit14 = None
    AcyclicReceiveBit15 = None
    AcyclicReceiveBit16 = None
    AcyclicReceiveBit17 = None
    BUInput1 = None
    BUInput2 = None
    BUInput3 = None
    BUInput4 = None
    BUTestResetButton = None
    ContactorControl1QE1 = None
    ContactorControl2QE2 = None
    ContactorControl3QE3 = None
    ContactorControl4QE4 = None
    ContactorControl5QE5 = None
    Counter1Output = None
    Counter2Output = None
    Counter3Output = None
    Counter4Output = None
    Counter5Output = None
    Counter6Output = None
    CyclicReceiveBit00 = None
    CyclicReceiveBit01 = None
    CyclicReceiveBit02 = None
    CyclicReceiveBit03 = None
    CyclicReceiveBit04 = None
    CyclicReceiveBit05 = None
    CyclicReceiveBit06 = None
    CyclicReceiveBit07 = None
    CyclicReceiveBit10 = None
    CyclicReceiveBit11 = None
    CyclicReceiveBit12 = None
    CyclicReceiveBit13 = None
    CyclicReceiveBit14 = None
    CyclicReceiveBit15 = None
    CyclicReceiveBit16 = None
    CyclicReceiveBit17 = None
    DisplayQLAOff = None
    DisplayQLEForward = None
    DisplayQLEForwardFast = None
    DisplayQLEReverse = None
    DisplayQLEReverseFast = None
    DisplayQLSFault = None
    DM1Input1 = None
    DM1Input2 = None
    DM1Input3 = None
    DM1Input4 = None
    DM1SensorChannel1 = None
    DM1SensorChannel2 = None
    DM2Input1 = None
    DM2Input2 = None
    DM2Input3 = None
    DM2Input4 = None
    EnabledControlCommandOff = None
    EnabledControlCommandOnForward = None
    EnabledControlCommandOnForwardFast = None
    EnabledControlCommandOnReverse = None
    EnabledControlCommandOnReverseFast = None
    EventAM1OpenCircuit = None
    EventAM1TripLevel0420mAGt = None
    EventAM1TripLevel0420mALt = None
    EventAM1WarningLevel0420mAGt = None
    EventAM1WarningLevel0420mALt = None
    EventAM2OpenCircuit = None
    EventAM2TripLevel0420mAGt = None
    EventAM2TripLevel0420mALt = None
    EventAM2WarningLevel0420mAGt = None
    EventAM2WarningLevel0420mALt = None
    EventConfiguredOperatorPanelMissing = None
    EventDMFLOCALOk = None
    EventExternalFault1 = None
    EventExternalFault2 = None
    EventExternalFault3 = None
    EventExternalFault4 = None
    EventExternalFault5 = None
    EventExternalFault6 = None
    EventExternalGroundFault = None
    EventExternalGroundFaultWarning = None
    EventInternalGroundFault = None
    EventJustOneStartPossible = None
    EventLimitMonitor1 = None
    EventLimitMonitor2 = None
    EventLimitMonitor3 = None
    EventLimitMonitor4 = None
    EventLimitMonitor5 = None
    EventLimitMonitor6 = None
    EventMonitoringPeriodForMandatoryTestingTestRequirement = None
    EventMotorOperatingHoursGt = None
    EventNoStartPermitted = None
    EventNumberOfStartsGt = None
    EventOverload = None
    EventOverloadAndPhaseFailure = None
    EventPrewarningOverload = None
    EventPROFIsafeActive = None
    EventSafetyrelatedTripping = None
    EventStalledRotor = None
    EventStopTimeGt = None
    EventThermistorOpenCircuit = None
    EventThermistorShortCircuit = None
    EventThermistorTripLevel = None
    EventTimestampfctActiveAndOk = None
    EventTM1OutOfRange = None
    EventTM1SensorFault = None
    EventTM1TripLevelTGt = None
    EventTM1WarningLevelTGt = None
    EventTM2OutOfRange = None
    EventTM2SensorFault = None
    EventTM2TripLevelTGt = None
    EventTM2WarningLevelTGt = None
    EventTripLevelCosPhiLt = None
    EventTripLevelIGt = None
    EventTripLevelILt = None
    EventTripLevelPGt = None
    EventTripLevelPLt = None
    EventTripLevelULt = None
    EventUnbalance = None
    EventWarningLevelCosPhiLt = None
    EventWarningLevelIGt = None
    EventWarningLevelILt = None
    EventWarningLevelPGt = None
    EventWarningLevelPLt = None
    EventWarningLevelULt = None
    FaultAntivalence = None
    FaultBus = None
    FaultConfigurationError = None
    FaultDouble0 = None
    FaultDouble1 = None
    FaultEndPosition = None
    FaultExecutionOnCommand = None
    FaultExecutionSTOPCommand = None
    FaultFeedbackOff = None
    FaultFeedbackOn = None
    FaultHardwareFaultBasicUnit = None
    FaultModuleFault = None
    FaultOperationalProtectionOff = None
    FaultParameterization = None
    FaultPLCPCS = None
    FaultPowerFailure = None
    FaultStalledPositioner = None
    FaultTemporaryComponents = None
    FaultTestPositionFeedback = None
    FixedLevel0 = None
    FixedLevel1 = None
    Flashing1Output = None
    Flashing2Output = None
    Flashing3Output = None
    Flicker1Output = None
    Flicker2Output = None
    Flicker3Output = None
    NonvolatileElement1Output = None
    NonvolatileElement2Output = None
    NonvolatileElement3Output = None
    NonvolatileElement4Output = None
    NotConnected = None
    OPButton1 = None
    OPButton2 = None
    OPButton3 = None
    OPButton4 = None
    OPTestResetButton = None
    PWMOutput = None
    SignalConditioning1Output = None
    SignalConditioning2Output = None
    SignalConditioning3Output = None
    SignalConditioning4Output = None
    SignalConditioning5Output = None
    SignalConditioning6Output = None
    StatusBusOk = None
    StatusChangeoverPauseActive = None
    StatusCoolingDownPeriodActive = None
    StatusCurrentFlowing = None
    StatusDeviceOk = None
    StatusDeviceTestActive = None
    StatusEmergencyStartExecuted = None
    StatusEnablingCircuitClosed = None
    StatusFeedbackCLOSED = None
    StatusFeedbackOPEN = None
    StatusGroupFault = None
    StatusGroupWarning = None
    StatusInterlockingTimeActive = None
    StatusOff = None
    StatusOnForward = None
    StatusOnForwardFast = None
    StatusOnReverse = None
    StatusOnReverseFast = None
    StatusOperationalProtectionOff = None
    StatusPauseTimeActive = None
    StatusPhaseSequence123 = None
    StatusPhaseSequence321 = None
    StatusPLCPCSInRun = None
    StatusPositionerRunsInCLOSEDDirection = None
    StatusPositionerRunsInOPENDirection = None
    StatusPROFIenergyCommandStartPausePending = None
    StatusRemoteMode = None
    StatusStartActive = None
    StatusTestPosition = None
    StatusTorqueCLOSED = None
    StatusTorqueOPEN = None
    Timer1Output = None
    Timer2Output = None
    Timer3Output = None
    Timer4Output = None
    Timer5Output = None
    Timer6Output = None
    TruthTable10Output = None
    TruthTable11Output = None
    TruthTable1Output = None
    TruthTable2Output = None
    TruthTable3Output = None
    TruthTable4Output = None
    TruthTable5Output = None
    TruthTable6Output = None
    TruthTable7Output = None
    TruthTable8Output = None
    TruthTable9Output1 = None
    TruthTable9Output2 = None
    value__ = None
    WarningFeedbackCircuit = None
    WarningSimultaneity = None

class ControlFunctionTorqueOPENTO(
    Enum
):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Possible values for property ControlFunctionTorqueOPENTO

    enum ControlFunctionTorqueOPENTO, values: AcyclicReceiveBit00 (40), AcyclicReceiveBit01 (41), AcyclicReceiveBit02 (42), AcyclicReceiveBit03 (43), AcyclicReceiveBit04 (44), AcyclicReceiveBit05 (45), AcyclicReceiveBit06 (46), AcyclicReceiveBit07 (47), AcyclicReceiveBit10 (48), AcyclicReceiveBit11 (49), AcyclicReceiveBit12 (50), AcyclicReceiveBit13 (51), AcyclicReceiveBit14 (52), AcyclicReceiveBit15 (53), AcyclicReceiveBit16 (54), AcyclicReceiveBit17 (55), BUInput1 (9), BUInput2 (10), BUInput3 (11), BUInput4 (12), BUTestResetButton (8), ContactorControl1QE1 (80), ContactorControl2QE2 (81), ContactorControl3QE3 (82), ContactorControl4QE4 (83), ContactorControl5QE5 (84), Counter1Output (236), Counter2Output (237), Counter3Output (238), Counter4Output (239), Counter5Output (228), Counter6Output (229), CyclicReceiveBit00 (56), CyclicReceiveBit01 (57), CyclicReceiveBit02 (58), CyclicReceiveBit03 (59), CyclicReceiveBit04 (60), CyclicReceiveBit05 (61), CyclicReceiveBit06 (62), CyclicReceiveBit07 (63), CyclicReceiveBit10 (64), CyclicReceiveBit11 (65), CyclicReceiveBit12 (66), CyclicReceiveBit13 (67), CyclicReceiveBit14 (68), CyclicReceiveBit15 (69), CyclicReceiveBit16 (70), CyclicReceiveBit17 (71), DisplayQLAOff (90), DisplayQLEForward (91), DisplayQLEForwardFast (92), DisplayQLEReverse (89), DisplayQLEReverseFast (88), DisplayQLSFault (93), DM1Input1 (16), DM1Input2 (17), DM1Input3 (18), DM1Input4 (19), DM1SensorChannel1 (24), DM1SensorChannel2 (25), DM2Input1 (20), DM2Input2 (21), DM2Input3 (22), DM2Input4 (23), EnabledControlCommandOff (74), EnabledControlCommandOnForward (75), EnabledControlCommandOnForwardFast (76), EnabledControlCommandOnReverse (73), EnabledControlCommandOnReverseFast (72), EventAM1OpenCircuit (180), EventAM1TripLevel0420mAGt (158), EventAM1TripLevel0420mALt (159), EventAM1WarningLevel0420mAGt (150), EventAM1WarningLevel0420mALt (151), EventAM2OpenCircuit (179), EventAM2TripLevel0420mAGt (6), EventAM2TripLevel0420mALt (7), EventAM2WarningLevel0420mAGt (4), EventAM2WarningLevel0420mALt (5), EventConfiguredOperatorPanelMissing (188), EventDMFLOCALOk (186), EventExternalFault1 (172), EventExternalFault2 (173), EventExternalFault3 (174), EventExternalFault4 (175), EventExternalFault5 (176), EventExternalFault6 (177), EventExternalGroundFault (133), EventExternalGroundFaultWarning (134), EventInternalGroundFault (132), EventJustOneStartPossible (165), EventLimitMonitor1 (168), EventLimitMonitor2 (169), EventLimitMonitor3 (170), EventLimitMonitor4 (171), EventLimitMonitor5 (38), EventLimitMonitor6 (39), EventMonitoringPeriodForMandatoryTestingTestRequirement (182), EventMotorOperatingHoursGt (166), EventNoStartPermitted (163), EventNumberOfStartsGt (164), EventOverload (130), EventOverloadAndPhaseFailure (131), EventPrewarningOverload (128), EventPROFIsafeActive (187), EventSafetyrelatedTripping (181), EventStalledRotor (160), EventStopTimeGt (167), EventThermistorOpenCircuit (137), EventThermistorShortCircuit (136), EventThermistorTripLevel (135), EventTimestampfctActiveAndOk (184), EventTM1OutOfRange (141), EventTM1SensorFault (140), EventTM1TripLevelTGt (139), EventTM1WarningLevelTGt (138), EventTM2OutOfRange (29), EventTM2SensorFault (28), EventTM2TripLevelTGt (31), EventTM2WarningLevelTGt (30), EventTripLevelCosPhiLt (156), EventTripLevelIGt (152), EventTripLevelILt (153), EventTripLevelPGt (154), EventTripLevelPLt (155), EventTripLevelULt (157), EventUnbalance (129), EventWarningLevelCosPhiLt (148), EventWarningLevelIGt (144), EventWarningLevelILt (145), EventWarningLevelPGt (146), EventWarningLevelPLt (147), EventWarningLevelULt (149), FaultAntivalence (208), FaultBus (197), FaultConfigurationError (195), FaultDouble0 (205), FaultDouble1 (206), FaultEndPosition (207), FaultExecutionOnCommand (200), FaultExecutionSTOPCommand (201), FaultFeedbackOff (203), FaultFeedbackOn (202), FaultHardwareFaultBasicUnit (192), FaultModuleFault (193), FaultOperationalProtectionOff (211), FaultParameterization (196), FaultPLCPCS (198), FaultPowerFailure (210), FaultStalledPositioner (204), FaultTemporaryComponents (194), FaultTestPositionFeedback (209), FixedLevel0 (1), FixedLevel1 (2), Flashing1Output (248), Flashing2Output (249), Flashing3Output (250), Flicker1Output (251), Flicker2Output (252), Flicker3Output (253), NonvolatileElement1Output (244), NonvolatileElement2Output (245), NonvolatileElement3Output (246), NonvolatileElement4Output (247), NotConnected (0), OPButton1 (33), OPButton2 (34), OPButton3 (35), OPButton4 (36), OPTestResetButton (32), PWMOutput (254), SignalConditioning1Output (240), SignalConditioning2Output (241), SignalConditioning3Output (242), SignalConditioning4Output (243), SignalConditioning5Output (214), SignalConditioning6Output (215), StatusBusOk (99), StatusChangeoverPauseActive (111), StatusCoolingDownPeriodActive (122), StatusCurrentFlowing (101), StatusDeviceOk (98), StatusDeviceTestActive (124), StatusEmergencyStartExecuted (121), StatusEnablingCircuitClosed (127), StatusFeedbackCLOSED (114), StatusFeedbackOPEN (115), StatusGroupFault (96), StatusGroupWarning (97), StatusInterlockingTimeActive (110), StatusOff (106), StatusOnForward (107), StatusOnForwardFast (108), StatusOnReverse (105), StatusOnReverseFast (104), StatusOperationalProtectionOff (119), StatusPauseTimeActive (123), StatusPhaseSequence123 (125), StatusPhaseSequence321 (126), StatusPLCPCSInRun (100), StatusPositionerRunsInCLOSEDDirection (113), StatusPositionerRunsInOPENDirection (112), StatusPROFIenergyCommandStartPausePending (102), StatusRemoteMode (120), StatusStartActive (109), StatusTestPosition (118), StatusTorqueCLOSED (116), StatusTorqueOPEN (117), Timer1Output (232), Timer2Output (233), Timer3Output (234), Timer4Output (235), Timer5Output (230), Timer6Output (231), TruthTable10Output (226), TruthTable11Output (227), TruthTable1Output (216), TruthTable2Output (217), TruthTable3Output (218), TruthTable4Output (219), TruthTable5Output (220), TruthTable6Output (221), TruthTable7Output (222), TruthTable8Output (223), TruthTable9Output1 (224), TruthTable9Output2 (225), WarningFeedbackCircuit (190), WarningSimultaneity (191)
    """

    AcyclicReceiveBit00 = None
    AcyclicReceiveBit01 = None
    AcyclicReceiveBit02 = None
    AcyclicReceiveBit03 = None
    AcyclicReceiveBit04 = None
    AcyclicReceiveBit05 = None
    AcyclicReceiveBit06 = None
    AcyclicReceiveBit07 = None
    AcyclicReceiveBit10 = None
    AcyclicReceiveBit11 = None
    AcyclicReceiveBit12 = None
    AcyclicReceiveBit13 = None
    AcyclicReceiveBit14 = None
    AcyclicReceiveBit15 = None
    AcyclicReceiveBit16 = None
    AcyclicReceiveBit17 = None
    BUInput1 = None
    BUInput2 = None
    BUInput3 = None
    BUInput4 = None
    BUTestResetButton = None
    ContactorControl1QE1 = None
    ContactorControl2QE2 = None
    ContactorControl3QE3 = None
    ContactorControl4QE4 = None
    ContactorControl5QE5 = None
    Counter1Output = None
    Counter2Output = None
    Counter3Output = None
    Counter4Output = None
    Counter5Output = None
    Counter6Output = None
    CyclicReceiveBit00 = None
    CyclicReceiveBit01 = None
    CyclicReceiveBit02 = None
    CyclicReceiveBit03 = None
    CyclicReceiveBit04 = None
    CyclicReceiveBit05 = None
    CyclicReceiveBit06 = None
    CyclicReceiveBit07 = None
    CyclicReceiveBit10 = None
    CyclicReceiveBit11 = None
    CyclicReceiveBit12 = None
    CyclicReceiveBit13 = None
    CyclicReceiveBit14 = None
    CyclicReceiveBit15 = None
    CyclicReceiveBit16 = None
    CyclicReceiveBit17 = None
    DisplayQLAOff = None
    DisplayQLEForward = None
    DisplayQLEForwardFast = None
    DisplayQLEReverse = None
    DisplayQLEReverseFast = None
    DisplayQLSFault = None
    DM1Input1 = None
    DM1Input2 = None
    DM1Input3 = None
    DM1Input4 = None
    DM1SensorChannel1 = None
    DM1SensorChannel2 = None
    DM2Input1 = None
    DM2Input2 = None
    DM2Input3 = None
    DM2Input4 = None
    EnabledControlCommandOff = None
    EnabledControlCommandOnForward = None
    EnabledControlCommandOnForwardFast = None
    EnabledControlCommandOnReverse = None
    EnabledControlCommandOnReverseFast = None
    EventAM1OpenCircuit = None
    EventAM1TripLevel0420mAGt = None
    EventAM1TripLevel0420mALt = None
    EventAM1WarningLevel0420mAGt = None
    EventAM1WarningLevel0420mALt = None
    EventAM2OpenCircuit = None
    EventAM2TripLevel0420mAGt = None
    EventAM2TripLevel0420mALt = None
    EventAM2WarningLevel0420mAGt = None
    EventAM2WarningLevel0420mALt = None
    EventConfiguredOperatorPanelMissing = None
    EventDMFLOCALOk = None
    EventExternalFault1 = None
    EventExternalFault2 = None
    EventExternalFault3 = None
    EventExternalFault4 = None
    EventExternalFault5 = None
    EventExternalFault6 = None
    EventExternalGroundFault = None
    EventExternalGroundFaultWarning = None
    EventInternalGroundFault = None
    EventJustOneStartPossible = None
    EventLimitMonitor1 = None
    EventLimitMonitor2 = None
    EventLimitMonitor3 = None
    EventLimitMonitor4 = None
    EventLimitMonitor5 = None
    EventLimitMonitor6 = None
    EventMonitoringPeriodForMandatoryTestingTestRequirement = None
    EventMotorOperatingHoursGt = None
    EventNoStartPermitted = None
    EventNumberOfStartsGt = None
    EventOverload = None
    EventOverloadAndPhaseFailure = None
    EventPrewarningOverload = None
    EventPROFIsafeActive = None
    EventSafetyrelatedTripping = None
    EventStalledRotor = None
    EventStopTimeGt = None
    EventThermistorOpenCircuit = None
    EventThermistorShortCircuit = None
    EventThermistorTripLevel = None
    EventTimestampfctActiveAndOk = None
    EventTM1OutOfRange = None
    EventTM1SensorFault = None
    EventTM1TripLevelTGt = None
    EventTM1WarningLevelTGt = None
    EventTM2OutOfRange = None
    EventTM2SensorFault = None
    EventTM2TripLevelTGt = None
    EventTM2WarningLevelTGt = None
    EventTripLevelCosPhiLt = None
    EventTripLevelIGt = None
    EventTripLevelILt = None
    EventTripLevelPGt = None
    EventTripLevelPLt = None
    EventTripLevelULt = None
    EventUnbalance = None
    EventWarningLevelCosPhiLt = None
    EventWarningLevelIGt = None
    EventWarningLevelILt = None
    EventWarningLevelPGt = None
    EventWarningLevelPLt = None
    EventWarningLevelULt = None
    FaultAntivalence = None
    FaultBus = None
    FaultConfigurationError = None
    FaultDouble0 = None
    FaultDouble1 = None
    FaultEndPosition = None
    FaultExecutionOnCommand = None
    FaultExecutionSTOPCommand = None
    FaultFeedbackOff = None
    FaultFeedbackOn = None
    FaultHardwareFaultBasicUnit = None
    FaultModuleFault = None
    FaultOperationalProtectionOff = None
    FaultParameterization = None
    FaultPLCPCS = None
    FaultPowerFailure = None
    FaultStalledPositioner = None
    FaultTemporaryComponents = None
    FaultTestPositionFeedback = None
    FixedLevel0 = None
    FixedLevel1 = None
    Flashing1Output = None
    Flashing2Output = None
    Flashing3Output = None
    Flicker1Output = None
    Flicker2Output = None
    Flicker3Output = None
    NonvolatileElement1Output = None
    NonvolatileElement2Output = None
    NonvolatileElement3Output = None
    NonvolatileElement4Output = None
    NotConnected = None
    OPButton1 = None
    OPButton2 = None
    OPButton3 = None
    OPButton4 = None
    OPTestResetButton = None
    PWMOutput = None
    SignalConditioning1Output = None
    SignalConditioning2Output = None
    SignalConditioning3Output = None
    SignalConditioning4Output = None
    SignalConditioning5Output = None
    SignalConditioning6Output = None
    StatusBusOk = None
    StatusChangeoverPauseActive = None
    StatusCoolingDownPeriodActive = None
    StatusCurrentFlowing = None
    StatusDeviceOk = None
    StatusDeviceTestActive = None
    StatusEmergencyStartExecuted = None
    StatusEnablingCircuitClosed = None
    StatusFeedbackCLOSED = None
    StatusFeedbackOPEN = None
    StatusGroupFault = None
    StatusGroupWarning = None
    StatusInterlockingTimeActive = None
    StatusOff = None
    StatusOnForward = None
    StatusOnForwardFast = None
    StatusOnReverse = None
    StatusOnReverseFast = None
    StatusOperationalProtectionOff = None
    StatusPauseTimeActive = None
    StatusPhaseSequence123 = None
    StatusPhaseSequence321 = None
    StatusPLCPCSInRun = None
    StatusPositionerRunsInCLOSEDDirection = None
    StatusPositionerRunsInOPENDirection = None
    StatusPROFIenergyCommandStartPausePending = None
    StatusRemoteMode = None
    StatusStartActive = None
    StatusTestPosition = None
    StatusTorqueCLOSED = None
    StatusTorqueOPEN = None
    Timer1Output = None
    Timer2Output = None
    Timer3Output = None
    Timer4Output = None
    Timer5Output = None
    Timer6Output = None
    TruthTable10Output = None
    TruthTable11Output = None
    TruthTable1Output = None
    TruthTable2Output = None
    TruthTable3Output = None
    TruthTable4Output = None
    TruthTable5Output = None
    TruthTable6Output = None
    TruthTable7Output = None
    TruthTable8Output = None
    TruthTable9Output1 = None
    TruthTable9Output2 = None
    value__ = None
    WarningFeedbackCircuit = None
    WarningSimultaneity = None

class ControlStationModeSelectorS1(
    Enum
):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Possible values for property ControlStationModeSelectorS1

    enum ControlStationModeSelectorS1, values: AcyclicReceiveBit00 (40), AcyclicReceiveBit01 (41), AcyclicReceiveBit02 (42), AcyclicReceiveBit03 (43), AcyclicReceiveBit04 (44), AcyclicReceiveBit05 (45), AcyclicReceiveBit06 (46), AcyclicReceiveBit07 (47), AcyclicReceiveBit10 (48), AcyclicReceiveBit11 (49), AcyclicReceiveBit12 (50), AcyclicReceiveBit13 (51), AcyclicReceiveBit14 (52), AcyclicReceiveBit15 (53), AcyclicReceiveBit16 (54), AcyclicReceiveBit17 (55), BUInput1 (9), BUInput2 (10), BUInput3 (11), BUInput4 (12), BUTestResetButton (8), ContactorControl1QE1 (80), ContactorControl2QE2 (81), ContactorControl3QE3 (82), ContactorControl4QE4 (83), ContactorControl5QE5 (84), Counter1Output (236), Counter2Output (237), Counter3Output (238), Counter4Output (239), Counter5Output (228), Counter6Output (229), CyclicReceiveBit00 (56), CyclicReceiveBit01 (57), CyclicReceiveBit02 (58), CyclicReceiveBit03 (59), CyclicReceiveBit04 (60), CyclicReceiveBit05 (61), CyclicReceiveBit06 (62), CyclicReceiveBit07 (63), CyclicReceiveBit10 (64), CyclicReceiveBit11 (65), CyclicReceiveBit12 (66), CyclicReceiveBit13 (67), CyclicReceiveBit14 (68), CyclicReceiveBit15 (69), CyclicReceiveBit16 (70), CyclicReceiveBit17 (71), DisplayQLAOff (90), DisplayQLEForward (91), DisplayQLEForwardFast (92), DisplayQLEReverse (89), DisplayQLEReverseFast (88), DisplayQLSFault (93), DM1Input1 (16), DM1Input2 (17), DM1Input3 (18), DM1Input4 (19), DM1SensorChannel1 (24), DM1SensorChannel2 (25), DM2Input1 (20), DM2Input2 (21), DM2Input3 (22), DM2Input4 (23), EnabledControlCommandOff (74), EnabledControlCommandOnForward (75), EnabledControlCommandOnForwardFast (76), EnabledControlCommandOnReverse (73), EnabledControlCommandOnReverseFast (72), EventAM1OpenCircuit (180), EventAM1TripLevel0420mAGt (158), EventAM1TripLevel0420mALt (159), EventAM1WarningLevel0420mAGt (150), EventAM1WarningLevel0420mALt (151), EventAM2OpenCircuit (179), EventAM2TripLevel0420mAGt (6), EventAM2TripLevel0420mALt (7), EventAM2WarningLevel0420mAGt (4), EventAM2WarningLevel0420mALt (5), EventConfiguredOperatorPanelMissing (188), EventDMFLOCALOk (186), EventExternalFault1 (172), EventExternalFault2 (173), EventExternalFault3 (174), EventExternalFault4 (175), EventExternalFault5 (176), EventExternalFault6 (177), EventExternalGroundFault (133), EventExternalGroundFaultWarning (134), EventInternalGroundFault (132), EventJustOneStartPossible (165), EventLimitMonitor1 (168), EventLimitMonitor2 (169), EventLimitMonitor3 (170), EventLimitMonitor4 (171), EventLimitMonitor5 (38), EventLimitMonitor6 (39), EventMonitoringPeriodForMandatoryTestingTestRequirement (182), EventMotorOperatingHoursGt (166), EventNoStartPermitted (163), EventNumberOfStartsGt (164), EventOverload (130), EventOverloadAndPhaseFailure (131), EventPrewarningOverload (128), EventPROFIsafeActive (187), EventSafetyrelatedTripping (181), EventStalledRotor (160), EventStopTimeGt (167), EventThermistorOpenCircuit (137), EventThermistorShortCircuit (136), EventThermistorTripLevel (135), EventTimestampfctActiveAndOk (184), EventTM1OutOfRange (141), EventTM1SensorFault (140), EventTM1TripLevelTGt (139), EventTM1WarningLevelTGt (138), EventTM2OutOfRange (29), EventTM2SensorFault (28), EventTM2TripLevelTGt (31), EventTM2WarningLevelTGt (30), EventTripLevelCosPhiLt (156), EventTripLevelIGt (152), EventTripLevelILt (153), EventTripLevelPGt (154), EventTripLevelPLt (155), EventTripLevelULt (157), EventUnbalance (129), EventWarningLevelCosPhiLt (148), EventWarningLevelIGt (144), EventWarningLevelILt (145), EventWarningLevelPGt (146), EventWarningLevelPLt (147), EventWarningLevelULt (149), FaultAntivalence (208), FaultBus (197), FaultConfigurationError (195), FaultDouble0 (205), FaultDouble1 (206), FaultEndPosition (207), FaultExecutionOnCommand (200), FaultExecutionSTOPCommand (201), FaultFeedbackOff (203), FaultFeedbackOn (202), FaultHardwareFaultBasicUnit (192), FaultModuleFault (193), FaultOperationalProtectionOff (211), FaultParameterization (196), FaultPLCPCS (198), FaultPowerFailure (210), FaultStalledPositioner (204), FaultTemporaryComponents (194), FaultTestPositionFeedback (209), FixedLevel0 (1), FixedLevel1 (2), Flashing1Output (248), Flashing2Output (249), Flashing3Output (250), Flicker1Output (251), Flicker2Output (252), Flicker3Output (253), NonvolatileElement1Output (244), NonvolatileElement2Output (245), NonvolatileElement3Output (246), NonvolatileElement4Output (247), NotConnected (0), OPButton1 (33), OPButton2 (34), OPButton3 (35), OPButton4 (36), OPTestResetButton (32), PWMOutput (254), SignalConditioning1Output (240), SignalConditioning2Output (241), SignalConditioning3Output (242), SignalConditioning4Output (243), SignalConditioning5Output (214), SignalConditioning6Output (215), StatusBusOk (99), StatusChangeoverPauseActive (111), StatusCoolingDownPeriodActive (122), StatusCurrentFlowing (101), StatusDeviceOk (98), StatusDeviceTestActive (124), StatusEmergencyStartExecuted (121), StatusEnablingCircuitClosed (127), StatusFeedbackCLOSED (114), StatusFeedbackOPEN (115), StatusGroupFault (96), StatusGroupWarning (97), StatusInterlockingTimeActive (110), StatusOff (106), StatusOnForward (107), StatusOnForwardFast (108), StatusOnReverse (105), StatusOnReverseFast (104), StatusOperationalProtectionOff (119), StatusPauseTimeActive (123), StatusPhaseSequence123 (125), StatusPhaseSequence321 (126), StatusPLCPCSInRun (100), StatusPositionerRunsInCLOSEDDirection (113), StatusPositionerRunsInOPENDirection (112), StatusPROFIenergyCommandStartPausePending (102), StatusRemoteMode (120), StatusStartActive (109), StatusTestPosition (118), StatusTorqueCLOSED (116), StatusTorqueOPEN (117), Timer1Output (232), Timer2Output (233), Timer3Output (234), Timer4Output (235), Timer5Output (230), Timer6Output (231), TruthTable10Output (226), TruthTable11Output (227), TruthTable1Output (216), TruthTable2Output (217), TruthTable3Output (218), TruthTable4Output (219), TruthTable5Output (220), TruthTable6Output (221), TruthTable7Output (222), TruthTable8Output (223), TruthTable9Output1 (224), TruthTable9Output2 (225), WarningFeedbackCircuit (190), WarningSimultaneity (191)
    """

    AcyclicReceiveBit00 = None
    AcyclicReceiveBit01 = None
    AcyclicReceiveBit02 = None
    AcyclicReceiveBit03 = None
    AcyclicReceiveBit04 = None
    AcyclicReceiveBit05 = None
    AcyclicReceiveBit06 = None
    AcyclicReceiveBit07 = None
    AcyclicReceiveBit10 = None
    AcyclicReceiveBit11 = None
    AcyclicReceiveBit12 = None
    AcyclicReceiveBit13 = None
    AcyclicReceiveBit14 = None
    AcyclicReceiveBit15 = None
    AcyclicReceiveBit16 = None
    AcyclicReceiveBit17 = None
    BUInput1 = None
    BUInput2 = None
    BUInput3 = None
    BUInput4 = None
    BUTestResetButton = None
    ContactorControl1QE1 = None
    ContactorControl2QE2 = None
    ContactorControl3QE3 = None
    ContactorControl4QE4 = None
    ContactorControl5QE5 = None
    Counter1Output = None
    Counter2Output = None
    Counter3Output = None
    Counter4Output = None
    Counter5Output = None
    Counter6Output = None
    CyclicReceiveBit00 = None
    CyclicReceiveBit01 = None
    CyclicReceiveBit02 = None
    CyclicReceiveBit03 = None
    CyclicReceiveBit04 = None
    CyclicReceiveBit05 = None
    CyclicReceiveBit06 = None
    CyclicReceiveBit07 = None
    CyclicReceiveBit10 = None
    CyclicReceiveBit11 = None
    CyclicReceiveBit12 = None
    CyclicReceiveBit13 = None
    CyclicReceiveBit14 = None
    CyclicReceiveBit15 = None
    CyclicReceiveBit16 = None
    CyclicReceiveBit17 = None
    DisplayQLAOff = None
    DisplayQLEForward = None
    DisplayQLEForwardFast = None
    DisplayQLEReverse = None
    DisplayQLEReverseFast = None
    DisplayQLSFault = None
    DM1Input1 = None
    DM1Input2 = None
    DM1Input3 = None
    DM1Input4 = None
    DM1SensorChannel1 = None
    DM1SensorChannel2 = None
    DM2Input1 = None
    DM2Input2 = None
    DM2Input3 = None
    DM2Input4 = None
    EnabledControlCommandOff = None
    EnabledControlCommandOnForward = None
    EnabledControlCommandOnForwardFast = None
    EnabledControlCommandOnReverse = None
    EnabledControlCommandOnReverseFast = None
    EventAM1OpenCircuit = None
    EventAM1TripLevel0420mAGt = None
    EventAM1TripLevel0420mALt = None
    EventAM1WarningLevel0420mAGt = None
    EventAM1WarningLevel0420mALt = None
    EventAM2OpenCircuit = None
    EventAM2TripLevel0420mAGt = None
    EventAM2TripLevel0420mALt = None
    EventAM2WarningLevel0420mAGt = None
    EventAM2WarningLevel0420mALt = None
    EventConfiguredOperatorPanelMissing = None
    EventDMFLOCALOk = None
    EventExternalFault1 = None
    EventExternalFault2 = None
    EventExternalFault3 = None
    EventExternalFault4 = None
    EventExternalFault5 = None
    EventExternalFault6 = None
    EventExternalGroundFault = None
    EventExternalGroundFaultWarning = None
    EventInternalGroundFault = None
    EventJustOneStartPossible = None
    EventLimitMonitor1 = None
    EventLimitMonitor2 = None
    EventLimitMonitor3 = None
    EventLimitMonitor4 = None
    EventLimitMonitor5 = None
    EventLimitMonitor6 = None
    EventMonitoringPeriodForMandatoryTestingTestRequirement = None
    EventMotorOperatingHoursGt = None
    EventNoStartPermitted = None
    EventNumberOfStartsGt = None
    EventOverload = None
    EventOverloadAndPhaseFailure = None
    EventPrewarningOverload = None
    EventPROFIsafeActive = None
    EventSafetyrelatedTripping = None
    EventStalledRotor = None
    EventStopTimeGt = None
    EventThermistorOpenCircuit = None
    EventThermistorShortCircuit = None
    EventThermistorTripLevel = None
    EventTimestampfctActiveAndOk = None
    EventTM1OutOfRange = None
    EventTM1SensorFault = None
    EventTM1TripLevelTGt = None
    EventTM1WarningLevelTGt = None
    EventTM2OutOfRange = None
    EventTM2SensorFault = None
    EventTM2TripLevelTGt = None
    EventTM2WarningLevelTGt = None
    EventTripLevelCosPhiLt = None
    EventTripLevelIGt = None
    EventTripLevelILt = None
    EventTripLevelPGt = None
    EventTripLevelPLt = None
    EventTripLevelULt = None
    EventUnbalance = None
    EventWarningLevelCosPhiLt = None
    EventWarningLevelIGt = None
    EventWarningLevelILt = None
    EventWarningLevelPGt = None
    EventWarningLevelPLt = None
    EventWarningLevelULt = None
    FaultAntivalence = None
    FaultBus = None
    FaultConfigurationError = None
    FaultDouble0 = None
    FaultDouble1 = None
    FaultEndPosition = None
    FaultExecutionOnCommand = None
    FaultExecutionSTOPCommand = None
    FaultFeedbackOff = None
    FaultFeedbackOn = None
    FaultHardwareFaultBasicUnit = None
    FaultModuleFault = None
    FaultOperationalProtectionOff = None
    FaultParameterization = None
    FaultPLCPCS = None
    FaultPowerFailure = None
    FaultStalledPositioner = None
    FaultTemporaryComponents = None
    FaultTestPositionFeedback = None
    FixedLevel0 = None
    FixedLevel1 = None
    Flashing1Output = None
    Flashing2Output = None
    Flashing3Output = None
    Flicker1Output = None
    Flicker2Output = None
    Flicker3Output = None
    NonvolatileElement1Output = None
    NonvolatileElement2Output = None
    NonvolatileElement3Output = None
    NonvolatileElement4Output = None
    NotConnected = None
    OPButton1 = None
    OPButton2 = None
    OPButton3 = None
    OPButton4 = None
    OPTestResetButton = None
    PWMOutput = None
    SignalConditioning1Output = None
    SignalConditioning2Output = None
    SignalConditioning3Output = None
    SignalConditioning4Output = None
    SignalConditioning5Output = None
    SignalConditioning6Output = None
    StatusBusOk = None
    StatusChangeoverPauseActive = None
    StatusCoolingDownPeriodActive = None
    StatusCurrentFlowing = None
    StatusDeviceOk = None
    StatusDeviceTestActive = None
    StatusEmergencyStartExecuted = None
    StatusEnablingCircuitClosed = None
    StatusFeedbackCLOSED = None
    StatusFeedbackOPEN = None
    StatusGroupFault = None
    StatusGroupWarning = None
    StatusInterlockingTimeActive = None
    StatusOff = None
    StatusOnForward = None
    StatusOnForwardFast = None
    StatusOnReverse = None
    StatusOnReverseFast = None
    StatusOperationalProtectionOff = None
    StatusPauseTimeActive = None
    StatusPhaseSequence123 = None
    StatusPhaseSequence321 = None
    StatusPLCPCSInRun = None
    StatusPositionerRunsInCLOSEDDirection = None
    StatusPositionerRunsInOPENDirection = None
    StatusPROFIenergyCommandStartPausePending = None
    StatusRemoteMode = None
    StatusStartActive = None
    StatusTestPosition = None
    StatusTorqueCLOSED = None
    StatusTorqueOPEN = None
    Timer1Output = None
    Timer2Output = None
    Timer3Output = None
    Timer4Output = None
    Timer5Output = None
    Timer6Output = None
    TruthTable10Output = None
    TruthTable11Output = None
    TruthTable1Output = None
    TruthTable2Output = None
    TruthTable3Output = None
    TruthTable4Output = None
    TruthTable5Output = None
    TruthTable6Output = None
    TruthTable7Output = None
    TruthTable8Output = None
    TruthTable9Output1 = None
    TruthTable9Output2 = None
    value__ = None
    WarningFeedbackCircuit = None
    WarningSimultaneity = None

class ControlStationModeSelectorS2(
    Enum
):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Possible values for property ControlStationModeSelectorS2

    enum ControlStationModeSelectorS2, values: AcyclicReceiveBit00 (40), AcyclicReceiveBit01 (41), AcyclicReceiveBit02 (42), AcyclicReceiveBit03 (43), AcyclicReceiveBit04 (44), AcyclicReceiveBit05 (45), AcyclicReceiveBit06 (46), AcyclicReceiveBit07 (47), AcyclicReceiveBit10 (48), AcyclicReceiveBit11 (49), AcyclicReceiveBit12 (50), AcyclicReceiveBit13 (51), AcyclicReceiveBit14 (52), AcyclicReceiveBit15 (53), AcyclicReceiveBit16 (54), AcyclicReceiveBit17 (55), BUInput1 (9), BUInput2 (10), BUInput3 (11), BUInput4 (12), BUTestResetButton (8), ContactorControl1QE1 (80), ContactorControl2QE2 (81), ContactorControl3QE3 (82), ContactorControl4QE4 (83), ContactorControl5QE5 (84), Counter1Output (236), Counter2Output (237), Counter3Output (238), Counter4Output (239), Counter5Output (228), Counter6Output (229), CyclicReceiveBit00 (56), CyclicReceiveBit01 (57), CyclicReceiveBit02 (58), CyclicReceiveBit03 (59), CyclicReceiveBit04 (60), CyclicReceiveBit05 (61), CyclicReceiveBit06 (62), CyclicReceiveBit07 (63), CyclicReceiveBit10 (64), CyclicReceiveBit11 (65), CyclicReceiveBit12 (66), CyclicReceiveBit13 (67), CyclicReceiveBit14 (68), CyclicReceiveBit15 (69), CyclicReceiveBit16 (70), CyclicReceiveBit17 (71), DisplayQLAOff (90), DisplayQLEForward (91), DisplayQLEForwardFast (92), DisplayQLEReverse (89), DisplayQLEReverseFast (88), DisplayQLSFault (93), DM1Input1 (16), DM1Input2 (17), DM1Input3 (18), DM1Input4 (19), DM1SensorChannel1 (24), DM1SensorChannel2 (25), DM2Input1 (20), DM2Input2 (21), DM2Input3 (22), DM2Input4 (23), EnabledControlCommandOff (74), EnabledControlCommandOnForward (75), EnabledControlCommandOnForwardFast (76), EnabledControlCommandOnReverse (73), EnabledControlCommandOnReverseFast (72), EventAM1OpenCircuit (180), EventAM1TripLevel0420mAGt (158), EventAM1TripLevel0420mALt (159), EventAM1WarningLevel0420mAGt (150), EventAM1WarningLevel0420mALt (151), EventAM2OpenCircuit (179), EventAM2TripLevel0420mAGt (6), EventAM2TripLevel0420mALt (7), EventAM2WarningLevel0420mAGt (4), EventAM2WarningLevel0420mALt (5), EventConfiguredOperatorPanelMissing (188), EventDMFLOCALOk (186), EventExternalFault1 (172), EventExternalFault2 (173), EventExternalFault3 (174), EventExternalFault4 (175), EventExternalFault5 (176), EventExternalFault6 (177), EventExternalGroundFault (133), EventExternalGroundFaultWarning (134), EventInternalGroundFault (132), EventJustOneStartPossible (165), EventLimitMonitor1 (168), EventLimitMonitor2 (169), EventLimitMonitor3 (170), EventLimitMonitor4 (171), EventLimitMonitor5 (38), EventLimitMonitor6 (39), EventMonitoringPeriodForMandatoryTestingTestRequirement (182), EventMotorOperatingHoursGt (166), EventNoStartPermitted (163), EventNumberOfStartsGt (164), EventOverload (130), EventOverloadAndPhaseFailure (131), EventPrewarningOverload (128), EventPROFIsafeActive (187), EventSafetyrelatedTripping (181), EventStalledRotor (160), EventStopTimeGt (167), EventThermistorOpenCircuit (137), EventThermistorShortCircuit (136), EventThermistorTripLevel (135), EventTimestampfctActiveAndOk (184), EventTM1OutOfRange (141), EventTM1SensorFault (140), EventTM1TripLevelTGt (139), EventTM1WarningLevelTGt (138), EventTM2OutOfRange (29), EventTM2SensorFault (28), EventTM2TripLevelTGt (31), EventTM2WarningLevelTGt (30), EventTripLevelCosPhiLt (156), EventTripLevelIGt (152), EventTripLevelILt (153), EventTripLevelPGt (154), EventTripLevelPLt (155), EventTripLevelULt (157), EventUnbalance (129), EventWarningLevelCosPhiLt (148), EventWarningLevelIGt (144), EventWarningLevelILt (145), EventWarningLevelPGt (146), EventWarningLevelPLt (147), EventWarningLevelULt (149), FaultAntivalence (208), FaultBus (197), FaultConfigurationError (195), FaultDouble0 (205), FaultDouble1 (206), FaultEndPosition (207), FaultExecutionOnCommand (200), FaultExecutionSTOPCommand (201), FaultFeedbackOff (203), FaultFeedbackOn (202), FaultHardwareFaultBasicUnit (192), FaultModuleFault (193), FaultOperationalProtectionOff (211), FaultParameterization (196), FaultPLCPCS (198), FaultPowerFailure (210), FaultStalledPositioner (204), FaultTemporaryComponents (194), FaultTestPositionFeedback (209), FixedLevel0 (1), FixedLevel1 (2), Flashing1Output (248), Flashing2Output (249), Flashing3Output (250), Flicker1Output (251), Flicker2Output (252), Flicker3Output (253), NonvolatileElement1Output (244), NonvolatileElement2Output (245), NonvolatileElement3Output (246), NonvolatileElement4Output (247), NotConnected (0), OPButton1 (33), OPButton2 (34), OPButton3 (35), OPButton4 (36), OPTestResetButton (32), PWMOutput (254), SignalConditioning1Output (240), SignalConditioning2Output (241), SignalConditioning3Output (242), SignalConditioning4Output (243), SignalConditioning5Output (214), SignalConditioning6Output (215), StatusBusOk (99), StatusChangeoverPauseActive (111), StatusCoolingDownPeriodActive (122), StatusCurrentFlowing (101), StatusDeviceOk (98), StatusDeviceTestActive (124), StatusEmergencyStartExecuted (121), StatusEnablingCircuitClosed (127), StatusFeedbackCLOSED (114), StatusFeedbackOPEN (115), StatusGroupFault (96), StatusGroupWarning (97), StatusInterlockingTimeActive (110), StatusOff (106), StatusOnForward (107), StatusOnForwardFast (108), StatusOnReverse (105), StatusOnReverseFast (104), StatusOperationalProtectionOff (119), StatusPauseTimeActive (123), StatusPhaseSequence123 (125), StatusPhaseSequence321 (126), StatusPLCPCSInRun (100), StatusPositionerRunsInCLOSEDDirection (113), StatusPositionerRunsInOPENDirection (112), StatusPROFIenergyCommandStartPausePending (102), StatusRemoteMode (120), StatusStartActive (109), StatusTestPosition (118), StatusTorqueCLOSED (116), StatusTorqueOPEN (117), Timer1Output (232), Timer2Output (233), Timer3Output (234), Timer4Output (235), Timer5Output (230), Timer6Output (231), TruthTable10Output (226), TruthTable11Output (227), TruthTable1Output (216), TruthTable2Output (217), TruthTable3Output (218), TruthTable4Output (219), TruthTable5Output (220), TruthTable6Output (221), TruthTable7Output (222), TruthTable8Output (223), TruthTable9Output1 (224), TruthTable9Output2 (225), WarningFeedbackCircuit (190), WarningSimultaneity (191)
    """

    AcyclicReceiveBit00 = None
    AcyclicReceiveBit01 = None
    AcyclicReceiveBit02 = None
    AcyclicReceiveBit03 = None
    AcyclicReceiveBit04 = None
    AcyclicReceiveBit05 = None
    AcyclicReceiveBit06 = None
    AcyclicReceiveBit07 = None
    AcyclicReceiveBit10 = None
    AcyclicReceiveBit11 = None
    AcyclicReceiveBit12 = None
    AcyclicReceiveBit13 = None
    AcyclicReceiveBit14 = None
    AcyclicReceiveBit15 = None
    AcyclicReceiveBit16 = None
    AcyclicReceiveBit17 = None
    BUInput1 = None
    BUInput2 = None
    BUInput3 = None
    BUInput4 = None
    BUTestResetButton = None
    ContactorControl1QE1 = None
    ContactorControl2QE2 = None
    ContactorControl3QE3 = None
    ContactorControl4QE4 = None
    ContactorControl5QE5 = None
    Counter1Output = None
    Counter2Output = None
    Counter3Output = None
    Counter4Output = None
    Counter5Output = None
    Counter6Output = None
    CyclicReceiveBit00 = None
    CyclicReceiveBit01 = None
    CyclicReceiveBit02 = None
    CyclicReceiveBit03 = None
    CyclicReceiveBit04 = None
    CyclicReceiveBit05 = None
    CyclicReceiveBit06 = None
    CyclicReceiveBit07 = None
    CyclicReceiveBit10 = None
    CyclicReceiveBit11 = None
    CyclicReceiveBit12 = None
    CyclicReceiveBit13 = None
    CyclicReceiveBit14 = None
    CyclicReceiveBit15 = None
    CyclicReceiveBit16 = None
    CyclicReceiveBit17 = None
    DisplayQLAOff = None
    DisplayQLEForward = None
    DisplayQLEForwardFast = None
    DisplayQLEReverse = None
    DisplayQLEReverseFast = None
    DisplayQLSFault = None
    DM1Input1 = None
    DM1Input2 = None
    DM1Input3 = None
    DM1Input4 = None
    DM1SensorChannel1 = None
    DM1SensorChannel2 = None
    DM2Input1 = None
    DM2Input2 = None
    DM2Input3 = None
    DM2Input4 = None
    EnabledControlCommandOff = None
    EnabledControlCommandOnForward = None
    EnabledControlCommandOnForwardFast = None
    EnabledControlCommandOnReverse = None
    EnabledControlCommandOnReverseFast = None
    EventAM1OpenCircuit = None
    EventAM1TripLevel0420mAGt = None
    EventAM1TripLevel0420mALt = None
    EventAM1WarningLevel0420mAGt = None
    EventAM1WarningLevel0420mALt = None
    EventAM2OpenCircuit = None
    EventAM2TripLevel0420mAGt = None
    EventAM2TripLevel0420mALt = None
    EventAM2WarningLevel0420mAGt = None
    EventAM2WarningLevel0420mALt = None
    EventConfiguredOperatorPanelMissing = None
    EventDMFLOCALOk = None
    EventExternalFault1 = None
    EventExternalFault2 = None
    EventExternalFault3 = None
    EventExternalFault4 = None
    EventExternalFault5 = None
    EventExternalFault6 = None
    EventExternalGroundFault = None
    EventExternalGroundFaultWarning = None
    EventInternalGroundFault = None
    EventJustOneStartPossible = None
    EventLimitMonitor1 = None
    EventLimitMonitor2 = None
    EventLimitMonitor3 = None
    EventLimitMonitor4 = None
    EventLimitMonitor5 = None
    EventLimitMonitor6 = None
    EventMonitoringPeriodForMandatoryTestingTestRequirement = None
    EventMotorOperatingHoursGt = None
    EventNoStartPermitted = None
    EventNumberOfStartsGt = None
    EventOverload = None
    EventOverloadAndPhaseFailure = None
    EventPrewarningOverload = None
    EventPROFIsafeActive = None
    EventSafetyrelatedTripping = None
    EventStalledRotor = None
    EventStopTimeGt = None
    EventThermistorOpenCircuit = None
    EventThermistorShortCircuit = None
    EventThermistorTripLevel = None
    EventTimestampfctActiveAndOk = None
    EventTM1OutOfRange = None
    EventTM1SensorFault = None
    EventTM1TripLevelTGt = None
    EventTM1WarningLevelTGt = None
    EventTM2OutOfRange = None
    EventTM2SensorFault = None
    EventTM2TripLevelTGt = None
    EventTM2WarningLevelTGt = None
    EventTripLevelCosPhiLt = None
    EventTripLevelIGt = None
    EventTripLevelILt = None
    EventTripLevelPGt = None
    EventTripLevelPLt = None
    EventTripLevelULt = None
    EventUnbalance = None
    EventWarningLevelCosPhiLt = None
    EventWarningLevelIGt = None
    EventWarningLevelILt = None
    EventWarningLevelPGt = None
    EventWarningLevelPLt = None
    EventWarningLevelULt = None
    FaultAntivalence = None
    FaultBus = None
    FaultConfigurationError = None
    FaultDouble0 = None
    FaultDouble1 = None
    FaultEndPosition = None
    FaultExecutionOnCommand = None
    FaultExecutionSTOPCommand = None
    FaultFeedbackOff = None
    FaultFeedbackOn = None
    FaultHardwareFaultBasicUnit = None
    FaultModuleFault = None
    FaultOperationalProtectionOff = None
    FaultParameterization = None
    FaultPLCPCS = None
    FaultPowerFailure = None
    FaultStalledPositioner = None
    FaultTemporaryComponents = None
    FaultTestPositionFeedback = None
    FixedLevel0 = None
    FixedLevel1 = None
    Flashing1Output = None
    Flashing2Output = None
    Flashing3Output = None
    Flicker1Output = None
    Flicker2Output = None
    Flicker3Output = None
    NonvolatileElement1Output = None
    NonvolatileElement2Output = None
    NonvolatileElement3Output = None
    NonvolatileElement4Output = None
    NotConnected = None
    OPButton1 = None
    OPButton2 = None
    OPButton3 = None
    OPButton4 = None
    OPTestResetButton = None
    PWMOutput = None
    SignalConditioning1Output = None
    SignalConditioning2Output = None
    SignalConditioning3Output = None
    SignalConditioning4Output = None
    SignalConditioning5Output = None
    SignalConditioning6Output = None
    StatusBusOk = None
    StatusChangeoverPauseActive = None
    StatusCoolingDownPeriodActive = None
    StatusCurrentFlowing = None
    StatusDeviceOk = None
    StatusDeviceTestActive = None
    StatusEmergencyStartExecuted = None
    StatusEnablingCircuitClosed = None
    StatusFeedbackCLOSED = None
    StatusFeedbackOPEN = None
    StatusGroupFault = None
    StatusGroupWarning = None
    StatusInterlockingTimeActive = None
    StatusOff = None
    StatusOnForward = None
    StatusOnForwardFast = None
    StatusOnReverse = None
    StatusOnReverseFast = None
    StatusOperationalProtectionOff = None
    StatusPauseTimeActive = None
    StatusPhaseSequence123 = None
    StatusPhaseSequence321 = None
    StatusPLCPCSInRun = None
    StatusPositionerRunsInCLOSEDDirection = None
    StatusPositionerRunsInOPENDirection = None
    StatusPROFIenergyCommandStartPausePending = None
    StatusRemoteMode = None
    StatusStartActive = None
    StatusTestPosition = None
    StatusTorqueCLOSED = None
    StatusTorqueOPEN = None
    Timer1Output = None
    Timer2Output = None
    Timer3Output = None
    Timer4Output = None
    Timer5Output = None
    Timer6Output = None
    TruthTable10Output = None
    TruthTable11Output = None
    TruthTable1Output = None
    TruthTable2Output = None
    TruthTable3Output = None
    TruthTable4Output = None
    TruthTable5Output = None
    TruthTable6Output = None
    TruthTable7Output = None
    TruthTable8Output = None
    TruthTable9Output1 = None
    TruthTable9Output2 = None
    value__ = None
    WarningFeedbackCircuit = None
    WarningSimultaneity = None

class CounterMode(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Possible values for property CounterMode

    enum CounterMode, values: CascadingFunction (2), ContinuouslyCountFunction (4), NormalCountFunction (1), OnceCountFunction (3), PeriodicCountFunction (0)
    """

    CascadingFunction = None
    ContinuouslyCountFunction = None
    NormalCountFunction = None
    OnceCountFunction = None
    PeriodicCountFunction = None
    value__ = None

class IHardwareCompareTarget:
    """Access to the device/device item in a HW compare scenario"""

    pass

class HardwareObject(
    IHardwareCompareTarget, IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """The base for hardware modules like devices or device items"""

    @property
    def DeviceItems(self) -> DeviceItemComposition:
        """
        Composition of device items

        Get: DeviceItems(self: HardwareObject) -> DeviceItemComposition
        """
        ...
    @property
    def HwIdentifiers(self):
        """
        Composition of HW identifiers

        Get: HwIdentifiers(self: HardwareObject) -> HwIdentifierComposition
        """
        ...
    @property
    def Items(self):
        """
        Associated device items for this device

        Get: Items(self: HardwareObject) -> DeviceItemAssociation
        """
        ...
    @property
    def Name(self) -> str:
        """Gets the name of the device"""
        ...
    @Name.setter
    def Name(self, value: str) -> None:
        """Sets the name of the device

        Parameters:
            value (str): The name of the device
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: HardwareObject) -> IEngineeringObject
        """
        ...
    @property
    def TypeIdentifier(self):
        """
        The type identifier of this device

        Get: TypeIdentifier(self: HardwareObject) -> str
        """
        ...
    def CanPlugCopy(self, deviceItem, positionNumber):
        """
        CanPlugCopy(self: HardwareObject, deviceItem: DeviceItem, positionNumber: int) -> bool

            Determines if plug can be copied

            deviceItem: Device for which the Plug will be moved

            positionNumber: The position number where to create the plug

            Returns: System.Boolean
        """
        ...
    def CanPlugMove(self, deviceItem, positionNumber):
        """
        CanPlugMove(self: HardwareObject, deviceItem: DeviceItem, positionNumber: int) -> bool

            Determines if plug can be moved

            deviceItem: Device for which the Plug will be moved

            positionNumber: The position number where to create the plug

            Returns: System.Boolean
        """
        ...
    def CanPlugNew(self, typeIdentifier, name, positionNumber):
        """
        CanPlugNew(self: HardwareObject, typeIdentifier: str, name: str, positionNumber: int) -> bool

            Determines if plug can be created

            typeIdentifier: The type identifier to use to create the plug

            name: The name of the plug to create

            positionNumber: The position number where to create the plug

            Returns: System.Boolean
        """
        ...
    def CompareTo(self, compareTarget):
        """
        CompareTo(self: HardwareObject, compareTarget: IHardwareCompareTarget) -> CompareResult

            Compare the hardware object vs the given target

            compareTarget: The target to compare to the hardware object

            Returns: Siemens.Engineering.Compare.CompareResult
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: HardwareObject) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def GetPlugLocations(self):
        """
        GetPlugLocations(self: HardwareObject) -> IList[PlugLocation]

            Determine some information about free slots.

            Returns: System.Collections.Generic.IList<Siemens.Engineering.HW.Extensions.PlugLocation>
        """
        ...
    def PlugCopy(self, deviceItem, positionNumber):
        """
        PlugCopy(self: HardwareObject, deviceItem: DeviceItem, positionNumber: int) -> DeviceItem

            Copies a plug to a given device

            deviceItem: Device for which the Plug will be moved

            positionNumber: The position number where to create the plug

            Returns: Siemens.Engineering.HW.DeviceItem
        """
        ...
    def PlugMove(self, deviceItem, positionNumber):
        """
        PlugMove(self: HardwareObject, deviceItem: DeviceItem, positionNumber: int) -> DeviceItem

            Moves a plug to a given device

            deviceItem: Device for which the Plug will be moved

            positionNumber: The position number where to create the plug

            Returns: Siemens.Engineering.HW.DeviceItem
        """
        ...
    def PlugNew(self, typeIdentifier, name, positionNumber):
        """
        PlugNew(self: HardwareObject, typeIdentifier: str, name: str, positionNumber: int) -> DeviceItem

            Creates and plugs a device item in a given hardware object.

            typeIdentifier: The type identifier of the device item to create.

            name: The name of the device item to create.

            positionNumber: The position number where to plug the created device item

            Returns: Siemens.Engineering.HW.DeviceItem
        """
        ...
    def ToString(self):
        """
        ToString(self: HardwareObject) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class Device(
    HardwareObject, IMasterCopySource, IMasterCopyTarget, IEngineeringServiceProvider
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IHardwareCompareTarget'>, <type 'IEngineeringObject'>, <type 'IInternalInstanceAccess'>, <type 'IServiceProvider'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """Device as an container for DeviceItems"""

    @property
    def IsGsd(self):
        """
        Indicates if this device is a Gsd device

        Get: IsGsd(self: Device) -> bool
        """
        ...
    @property
    def UnpluggedItems(self):
        """
        Associate unplugged items

        Get: UnpluggedItems(self: Device) -> DeviceItemAssociation
        """
        ...
    def Delete(self) -> None:
        """Deletes this instance."""
        ...
    def ShowInEditor(self, view):
        """
        ShowInEditor(self: Device, view: View)

            Show the indicated item in the HW editor

            view: Which view of the HW editor to show
        """
        ...
    def __next__(self) -> Device: ...

class DeviceComposition(
    IEngineeringComposition[Device], IInternalCompositionAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """Composition of Devices"""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: DeviceComposition) -> IEngineeringObject
        """
        ...
    def CreateFrom(self, masterCopy):
        """
        CreateFrom(self: DeviceComposition, masterCopy: MasterCopy) -> Device

            Create device from MasterCopy

            masterCopy: The source master copy

            Returns: Siemens.Engineering.HW.Device
        """
        ...
    def CreateWithItem(self, typeIdentifier: str, name: str, deviceName: Optional[str]) -> Device:
        """Create a device with subcomponents

        Parameters:
            typeIdentifier (str): Type identifier of the device to be created with sub items
            name (str): Name of the device to be created with sub items
            deviceName (str): The name of the device to create with subcomponents

        Returns:
            Device: The created device
        """
        ...
    def Find(self, name: str) -> Device:
        """Finds a given device

        Parameters:
            name (str): Name to find

        Returns:
            Device: The found device
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: DeviceComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: DeviceComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[Device](enumerable:  value: Device) -> bool"""
        ...
    def __ne__(self, *args): ...

class DeviceGroup(
    IEngineeringObject, IInternalObjectAccess, IEngineeringServiceProvider, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IServiceProvider'>, <type 'IInternalInstanceAccess'>
    """Group containing devices"""

    @property
    def Devices(self):
        """
        Composition of devices

        Get: Devices(self: DeviceGroup) -> DeviceComposition
        """
        ...
    @property
    def Name(self):
        """
        The name of the device group

        Get: Name(self: DeviceGroup) -> str
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: DeviceGroup) -> IEngineeringObject
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: DeviceGroup) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: DeviceGroup) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class DeviceItem(
    HardwareObject, IMasterCopySource, IEngineeringServiceProvider
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IHardwareCompareTarget'>, <type 'IEngineeringObject'>, <type 'IInternalInstanceAccess'>, <type 'IServiceProvider'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """DeviceItem object as representation of a hardware module"""

    @property
    def Addresses(self):
        """
        Composition of addresses

        Get: Addresses(self: DeviceItem) -> AddressComposition
        """
        ...
    @property
    def Channels(self):
        """
        Composition of channels

        Get: Channels(self: DeviceItem) -> ChannelComposition
        """
        ...
    @property
    def Classification(self):
        """
        The classifications a device item can belong to; Flags-enum

        Get: Classification(self: DeviceItem) -> DeviceItemClassifications
        """
        ...
    @property
    def Container(self):
        """
        This is the object where other DeviceItems are placed

        Get: Container(self: DeviceItem) -> HardwareObject
        """
        ...
    @property
    def IsBuiltIn(self):
        """
        Indicates if the device item is built into the device

        Get: IsBuiltIn(self: DeviceItem) -> bool
        """
        ...
    @property
    def IsPlugged(self):
        """
        Indicates if this device item is plugged into a device

        Get: IsPlugged(self: DeviceItem) -> bool
        """
        ...
    @property
    def PositionNumber(self):
        """
        Position number of this device item

        Get: PositionNumber(self: DeviceItem) -> int
        """
        ...
    def Delete(self):
        """
        Delete(self: DeviceItem)

            Deletes this instance.
        """
        ...
    def __next__(self) -> DeviceItem: ...

class DeviceItemAssociation(
    IEngineeringAssociation, IInternalAssociationAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalCollectionAccess'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>
    """Associated device items"""

    @property
    def Parent(self):
        """
        Gets the parent..

        Get: Parent(self: DeviceItemAssociation) -> IEngineeringObject
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: DeviceItemAssociation) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: DeviceItemAssociation) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[DeviceItem](enumerable:  value: DeviceItem) -> bool"""
        ...
    def __ne__(self, *args): ...

class DeviceItemClassifications(
    Enum
):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    The classifications a device item can belong to; Flags-enum.

    enum (flags) DeviceItemClassifications, values: CPU (1), HM (2), None (0)
    """

    CPU = None
    HM = None
    value__ = None

class DeviceItemComposition(
    IEngineeringComposition[DeviceItem], IInternalCompositionAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """Composition of DeviceItems"""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: DeviceItemComposition) -> IEngineeringObject
        """
        ...
    def Find(self, name: str) -> DeviceItem:
        """Find a device item by name

        Parameters:
            name (str): The name of the device item to find

        Returns:
            DeviceItem: The device item with the given name
        """
        ...
    def CreateFrom(self, masterCopy):
        """
        CreateFrom(self: DeviceItemComposition, masterCopy: MasterCopy) -> DeviceItem

            Create device item from MasterCopy

            masterCopy: The source MasterCopy

            Returns: Siemens.Engineering.HW.DeviceItem
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: DeviceItemComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: DeviceItemComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[DeviceItem](enumerable:  value: DeviceItem) -> bool"""
        ...
    def __ne__(self, *args): ...

class DeviceSystemGroup(
    DeviceGroup
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IServiceProvider'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringServiceProvider'>, <type 'IEquatable'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """Represents a device system group (e.g. ungrouped devices group)"""

    pass

class DeviceUserGroup(
    DeviceGroup, IMasterCopySource, IMasterCopyTarget
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IServiceProvider'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IEngineeringServiceProvider'>, <type 'IEquatable'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """Group containing the devices"""

    @property
    def Groups(self):
        """
        Composition of device user groups

        Get: Groups(self: DeviceUserGroup) -> DeviceUserGroupComposition
        """
        ...
    def Delete(self):
        """
        Delete(self: DeviceUserGroup)

            Deletes this instance.
        """
        ...

class DeviceUserGroupComposition(
    IEngineeringComposition, IInternalCompositionAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """Composition of DeviceUserGroups"""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: DeviceUserGroupComposition) -> IEngineeringObject
        """
        ...
    def CreateFrom(self, masterCopy):
        """
        CreateFrom(self: DeviceUserGroupComposition, masterCopy: MasterCopy) -> DeviceUserGroup

            Create device user group from MasterCopy

            masterCopy: The source MasterCopy

            Returns: Siemens.Engineering.HW.DeviceUserGroup
        """
        ...
    def Find(self, name):
        """
        Find(self: DeviceUserGroupComposition, name: str) -> DeviceUserGroup

            Finds a given device user group

            name: Name to find

            Returns: Siemens.Engineering.HW.DeviceUserGroup
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: DeviceUserGroupComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: DeviceUserGroupComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[DeviceUserGroup](enumerable:  value: DeviceUserGroup) -> bool"""
        ...
    def __ne__(self, *args): ...

class Failsafe_BehaviorAfterChannelFault(
    Enum
):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Possible values for property Failsafe_BehaviorAfterChannelFault

    enum Failsafe_BehaviorAfterChannelFault, values: PassivateChannel (1), PassivateTheEntireModule (0)
    """

    PassivateChannel = None
    PassivateTheEntireModule = None
    value__ = None

class Failsafe_ChannelFailureAcknowledge(
    Enum
):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Possible values for property Failsafe_ChannelFailureAcknowledge

    enum Failsafe_ChannelFailureAcknowledge, values: Automatic (1), Manual (0)
    """

    Automatic = None
    Manual = None
    value__ = None

class Failsafe_ControlOfOutput(
    Enum
):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Possible values for property Failsafe_ControlOfOutput

    enum Failsafe_ControlOfOutput, values: FCPU (0), FCPUAndOnboardFDI (1)
    """

    FCPU = None
    FCPUAndOnboardFDI = None
    value__ = None

class Failsafe_DiscrepancyBehavior(
    Enum
):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Possible values for property Failsafe_DiscrepancyBehavior

    enum Failsafe_DiscrepancyBehavior, values: SupplyLastValidValue (0), SupplyValue0 (1)
    """

    SupplyLastValidValue = None
    SupplyValue0 = None
    value__ = None

class Failsafe_DiscrepancyMonitoring(
    Enum
):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Possible values for property Failsafe_DiscrepancyMonitoring

    enum Failsafe_DiscrepancyMonitoring, values: Active (1), Deactivated (0)
    """

    Active = None
    Deactivated = None
    value__ = None

class Failsafe_FCheckiPar(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Possible values for property Failsafe_FCheckiPar

    enum Failsafe_FCheckiPar, values: Check (1), NoCheck (0)
    """

    Check = None
    NoCheck = None
    value__ = None

class Failsafe_FCheckSeqNr(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Possible values for property Failsafe_FCheckSeqNr

    enum Failsafe_FCheckSeqNr, values: Check (1), NoCheck (0)
    """

    Check = None
    NoCheck = None
    value__ = None

class Failsafe_FCRCSeed(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Possible values for property Failsafe_FCRCSeed

    enum Failsafe_FCRCSeed, values: CRCSeed16 (0), CRCSeed32 (1)
    """

    CRCSeed16 = None
    CRCSeed32 = None
    value__ = None

class Failsafe_FParVersion(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Possible values for property Failsafe_FParVersion

    enum Failsafe_FParVersion, values: V1mode (0), V2mode (1)
    """

    V1mode = None
    V2mode = None
    value__ = None

class Failsafe_FPassivation(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Possible values for property Failsafe_FPassivation

    enum Failsafe_FPassivation, values: Channel (1), DeviceModule (0)
    """

    Channel = None
    DeviceModule = None
    value__ = None

class Failsafe_FSIL(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Possible values for property Failsafe_FSIL

    enum Failsafe_FSIL, values: NoSIL (3), SIL1 (0), SIL2 (1), SIL3 (2)
    """

    NoSIL = None
    SIL1 = None
    SIL2 = None
    SIL3 = None
    value__ = None

class Failsafe_F_CRC_Length(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Possible values for property Failsafe_F_CRC_Length

    enum Failsafe_F_CRC_Length, values: FourByteCRC (2), ThreeByteCRC (0), TwoByteCRC (1)
    """

    FourByteCRC = None
    ThreeByteCRC = None
    TwoByteCRC = None
    value__ = None

class Failsafe_InputDelay(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Possible values for property Failsafe_InputDelay

    enum Failsafe_InputDelay, values: Value0dot4ms (1), Value0dot8ms (2), Value0ms (0), Value100ms (100), Value10ms (10), Value110ms (110), Value120ms (120), Value12dot8ms (12), Value130ms (130), Value140ms (140), Value150ms (150), Value1dot6ms (3), Value20ms (20), Value3dot2ms (4), Value50ms (50), Value60ms (60), Value6dot4ms (6), Value70ms (70), Value80ms (80), Value90ms (90)
    """

    Value0dot4ms = None
    Value0dot8ms = None
    Value0ms = None
    Value100ms = None
    Value10ms = None
    Value110ms = None
    Value120ms = None
    Value12dot8ms = None
    Value130ms = None
    Value140ms = None
    Value150ms = None
    Value1dot6ms = None
    Value20ms = None
    Value3dot2ms = None
    Value50ms = None
    Value60ms = None
    Value6dot4ms = None
    Value70ms = None
    Value80ms = None
    Value90ms = None
    value__ = None

class Failsafe_ManualAssignmentFIODBNumber(
    Enum
):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Possible values for property Failsafe_ManualAssignmentFIODBNumber

    enum Failsafe_ManualAssignmentFIODBNumber, values: Automatic (0), Manual (1)
    """

    Automatic = None
    Manual = None
    value__ = None

class Failsafe_MaximumTestPeriod(
    Enum
):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Possible values for property Failsafe_MaximumTestPeriod

    enum Failsafe_MaximumTestPeriod, values: Value1000sec (1), Value100sec (0)
    """

    Value1000sec = None
    Value100sec = None
    value__ = None

class Failsafe_MaxReadbackTimeLightTestAndDarkTest(
    Enum
):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Possible values for property Failsafe_MaxReadbackTimeLightTestAndDarkTest

    enum Failsafe_MaxReadbackTimeLightTestAndDarkTest, values: Value08Or10ms (0), Value30Or50ms (1)
    """

    Value08Or10ms = None
    Value30Or50ms = None
    value__ = None

class Failsafe_OutputType(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Possible values for property Failsafe_OutputType

    enum Failsafe_OutputType, values: PMSwitching (0), PPSwitching (1)
    """

    PMSwitching = None
    PPSwitching = None
    value__ = None

class Failsafe_ReintegrationAfterChannelFault(
    Enum
):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Possible values for property Failsafe_ReintegrationAfterChannelFault

    enum Failsafe_ReintegrationAfterChannelFault, values: Adjustable (0), AllChannelsAutomatically (1), AllChannelsManually (2)
    """

    Adjustable = None
    AllChannelsAutomatically = None
    AllChannelsManually = None
    value__ = None

class Failsafe_ReintegrationAfterDiscrepancyError(
    Enum
):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Possible values for property Failsafe_ReintegrationAfterDiscrepancyError

    enum Failsafe_ReintegrationAfterDiscrepancyError, values: Test0SignalNecessary (1), Test0SignalNotNecessary (0)
    """

    Test0SignalNecessary = None
    Test0SignalNotNecessary = None
    value__ = None

class Failsafe_SensorEvaluation(
    Enum
):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Possible values for property Failsafe_SensorEvaluation

    enum Failsafe_SensorEvaluation, values: Value1oo1Evaluation (0), Value1oo2EvaluationEquivalent (1), Value1oo2EvaluationNonEquivalent (2)
    """

    Value1oo1Evaluation = None
    Value1oo2EvaluationEquivalent = None
    Value1oo2EvaluationNonEquivalent = None
    value__ = None

class Failsafe_SensorSupply(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Possible values for property Failsafe_SensorSupply

    enum Failsafe_SensorSupply, values: ExternalSensorSupply (8), SensorSupply0 (0), SensorSupply1 (1), SensorSupply2 (2), SensorSupply3 (3), SensorSupply4 (4), SensorSupply5 (5), SensorSupply6 (6), SensorSupply7 (7)
    """

    ExternalSensorSupply = None
    SensorSupply0 = None
    SensorSupply1 = None
    SensorSupply2 = None
    SensorSupply3 = None
    SensorSupply4 = None
    SensorSupply5 = None
    SensorSupply6 = None
    SensorSupply7 = None
    value__ = None

class Failsafe_SequenceMonitoring(
    Enum
):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Possible values for property Failsafe_SequenceMonitoring

    enum Failsafe_SequenceMonitoring, values: Deactivated (0), SequenceMonitoringAscending (1), SequenceMonitoringDescending (2)
    """

    Deactivated = None
    SequenceMonitoringAscending = None
    SequenceMonitoringDescending = None
    value__ = None

class HardwareResource(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Hardware Resources that are assignable for interfaces

    enum HardwareResource, values: Undefined (0), X1 (1), X101 (101), X102 (102), X103 (103), X104 (104), X105 (105), X106 (106), X107 (107), X108 (108), X109 (109), X110 (110), X111 (111), X2 (2), X3 (3), X4 (4)
    """

    Undefined = None
    value__ = None
    X1 = None
    X101 = None
    X102 = None
    X103 = None
    X104 = None
    X105 = None
    X106 = None
    X107 = None
    X108 = None
    X109 = None
    X110 = None
    X111 = None
    X2 = None
    X3 = None
    X4 = None

class HwIdentifier(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Represents a HW identifier"""

    @property
    def HwIdentifierControllers(self):
        """
        Associated Hw identifier controllers

        Get: HwIdentifierControllers(self: HwIdentifier) -> HwIdentifierControllerAssociation
        """
        ...
    @property
    def Identifier(self):
        """
        Identifier for this HW identifier

        Get: Identifier(self: HwIdentifier) -> Int64
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: HwIdentifier) -> IEngineeringObject
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: HwIdentifier) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: HwIdentifier) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class HwIdentifierAssociation(
    IEngineeringAssociation, IInternalAssociationAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalCollectionAccess'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>
    """Associated Hw identifiers"""

    @property
    def Parent(self):
        """
        Gets the parent..

        Get: Parent(self: HwIdentifierAssociation) -> IEngineeringObject
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: HwIdentifierAssociation) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: HwIdentifierAssociation) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[HwIdentifier](enumerable:  value: HwIdentifier) -> bool"""
        ...
    def __ne__(self, *args): ...

class HwIdentifierComposition(
    IEngineeringComposition, IInternalCompositionAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """Composition of HwIdentifiers"""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: HwIdentifierComposition) -> IEngineeringObject
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: HwIdentifierComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: HwIdentifierComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[HwIdentifier](enumerable:  value: HwIdentifier) -> bool"""
        ...
    def __ne__(self, *args): ...

class InterfaceOperatingModes(
    Enum
):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Possible values for property InterfaceOperatingModes

    enum (flags) InterfaceOperatingModes, values: IoController (1), IoDevice (2), None (0)
    """

    IoController = None
    IoDevice = None
    value__ = None

class InterfaceType(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Possible values for property InterfaceType

    enum InterfaceType, values: Asi (4), Ethernet (3), Link (6), Mpi (2), PcInternal (7), Profibus (1), ProfibusIntegrated (8), Ptp (5), Unknown (0)
    """

    Asi = None
    Ethernet = None
    Link = None
    Mpi = None
    PcInternal = None
    Profibus = None
    ProfibusIntegrated = None
    Ptp = None
    Unknown = None
    value__ = None

class IoConnector(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Represents an IO connector"""

    @property
    def ConnectedToIoSystem(self):
        """
        The connected IO system

        Get: ConnectedToIoSystem(self: IoConnector) -> IoSystem
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: IoConnector) -> IEngineeringObject
        """
        ...
    def ConnectToIoSystem(self, ioSystem):
        """
        ConnectToIoSystem(self: IoConnector, ioSystem: IoSystem)

            Connects to the IO System

            ioSystem: The IO system to be connected
        """
        ...
    def DisconnectFromIoSystem(self):
        """
        DisconnectFromIoSystem(self: IoConnector)

            Disconnects a device from the given IO system
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: IoConnector) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def GetIoController(self):
        """
        GetIoController(self: IoConnector) -> IoController

            Returns the IO controller for this connector

            Returns: Siemens.Engineering.HW.IoController
        """
        ...
    def ToString(self):
        """
        ToString(self: IoConnector) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class IoConnectorAssociation(
    IEngineeringAssociation, IInternalAssociationAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalCollectionAccess'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>
    """Associated IO connectors"""

    @property
    def Parent(self):
        """
        Gets the parent..

        Get: Parent(self: IoConnectorAssociation) -> IEngineeringObject
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: IoConnectorAssociation) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: IoConnectorAssociation) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[IoConnector](enumerable:  value: IoConnector) -> bool"""
        ...
    def __ne__(self, *args): ...

class IoConnectorComposition(
    IEngineeringComposition, IInternalCompositionAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """Composition of IoConnectors"""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: IoConnectorComposition) -> IEngineeringObject
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: IoConnectorComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: IoConnectorComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[IoConnector](enumerable:  value: IoConnector) -> bool"""
        ...
    def __ne__(self, *args): ...

class IoController(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Represents an IO controller"""

    @property
    def Addresses(self):
        """
        Composition of addresses

        Get: Addresses(self: IoController) -> AddressComposition
        """
        ...
    @property
    def IoSystem(self):
        """
        Composition of IO system

        Get: IoSystem(self: IoController) -> IoSystem
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: IoController) -> IEngineeringObject
        """
        ...
    def CreateIoSystem(self, name):
        """
        CreateIoSystem(self: IoController, name: str) -> IoSystem

            Creates an IO system

            name: The name of the IO system to be created

            Returns: Siemens.Engineering.HW.IoSystem
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: IoController) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: IoController) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class IoControllerComposition(
    IEngineeringComposition, IInternalCompositionAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """Composition of IoControllers"""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: IoControllerComposition) -> IEngineeringObject
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: IoControllerComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: IoControllerComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[IoController](enumerable:  value: IoController) -> bool"""
        ...
    def __ne__(self, *args): ...

class IoSystem(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Represents an IO system"""

    @property
    def ConnectedIoDevices(self):
        """
        The connected IO devices

        Get: ConnectedIoDevices(self: IoSystem) -> IoConnectorAssociation
        """
        ...
    @property
    def HwIdentifiers(self):
        """
        Composition of HW identifiers

        Get: HwIdentifiers(self: IoSystem) -> HwIdentifierComposition
        """
        ...
    @property
    def Name(self):
        """
        The name of the IO system

        Get: Name(self: IoSystem) -> str

        Set: Name(self: IoSystem) = value
        """
        ...
    @property
    def Number(self):
        """
        The number of this IO system

        Get: Number(self: IoSystem) -> int

        Set: Number(self: IoSystem) = value
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: IoSystem) -> IEngineeringObject
        """
        ...
    @property
    def Subnet(self):
        """
        Associated Subnet

        Get: Subnet(self: IoSystem) -> Subnet
        """
        ...
    def Delete(self):
        """
        Delete(self: IoSystem)

            Deletes this instance.
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: IoSystem) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: IoSystem) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class IoSystemAssociation(
    IEngineeringAssociation, IInternalAssociationAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalCollectionAccess'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>
    """Associated IO systems"""

    @property
    def Parent(self):
        """
        Gets the parent..

        Get: Parent(self: IoSystemAssociation) -> IEngineeringObject
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: IoSystemAssociation) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: IoSystemAssociation) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[IoSystem](enumerable:  value: IoSystem) -> bool"""
        ...
    def __ne__(self, *args): ...

class IpProtocolSelection(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    IP protocol selection

    enum IpProtocolSelection, values: Dhcp (1), None (-1), OtherPath (3), Project (0), UserProgram (2), ViaIoController (4)
    """

    Dhcp = None
    OtherPath = None
    Project = None
    UserProgram = None
    value__ = None
    ViaIoController = None

class IsochronousTiToCalculationMode(
    Enum
):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Possible values for property IsochronousTiToCalculationMode

    enum IsochronousTiToCalculationMode, values: AutomaticMinimum (3), FromOB (1), FromSubnet (2), Manual (4), None (0)
    """

    AutomaticMinimum = None
    FromOB = None
    FromSubnet = None
    Manual = None
    value__ = None

class LengthOfIORange(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Possible values for property LengthOfIORange

    enum LengthOfIORange, values: None (0), Value128Byte (128), Value12Byte (12), Value160Byte (160), Value16Byte (16), Value192Byte (192), Value20Byte (20), Value224Byte (224), Value24Byte (24), Value256Byte (256), Value288Byte (288), Value28Byte (28), Value32Byte (32), Value4Byte (4), Value64Byte (64), Value8Byte (8), Value96Byte (96)
    """

    Value128Byte = None
    Value12Byte = None
    Value160Byte = None
    Value16Byte = None
    Value192Byte = None
    Value20Byte = None
    Value224Byte = None
    Value24Byte = None
    Value256Byte = None
    Value288Byte = None
    Value28Byte = None
    Value32Byte = None
    Value4Byte = None
    Value64Byte = None
    Value8Byte = None
    Value96Byte = None
    value__ = None

class MeasuringTemperatureCoefficient(
    Enum
):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Possible values for property MeasuringTemperatureCoefficient

    enum MeasuringTemperatureCoefficient, values: Cu0Dot00426 (17), Cu0Dot00427 (12), Cu0Dot00428 (13), Deactivated (0), LgNi0Dot005 (10), Ni0Dot005000 (16), Ni0Dot006170 (18), Ni0Dot006180 (7), Ni0Dot006720 (8), Pt0Dot003850 (9), Pt0Dot00385055 (6), Pt0Dot003850Its90 (5), Pt0Dot003851 (4), Pt0Dot003902 (2), Pt0Dot003910 (11), Pt0Dot003916 (1), Pt0Dot003920 (3)
    """

    Cu0Dot00426 = None
    Cu0Dot00427 = None
    Cu0Dot00428 = None
    Deactivated = None
    LgNi0Dot005 = None
    Ni0Dot005000 = None
    Ni0Dot006170 = None
    Ni0Dot006180 = None
    Ni0Dot006720 = None
    Pt0Dot003850 = None
    Pt0Dot00385055 = None
    Pt0Dot003850Its90 = None
    Pt0Dot003851 = None
    Pt0Dot003902 = None
    Pt0Dot003910 = None
    Pt0Dot003916 = None
    Pt0Dot003920 = None
    value__ = None

class MediaRedundancyRole(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Media Redundancy Role

    enum MediaRedundancyRole, values: Client (2), Manager (1), ManagerAuto (3), NotInRing (0)
    """

    Client = None
    Manager = None
    ManagerAuto = None
    NotInRing = None
    value__ = None

class MediumAttachmentType(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Possible values for property MediumAttachmentType

    enum MediumAttachmentType, values: Copper (1), FiberOptic (2), None (0)
    """

    Copper = None
    FiberOptic = None
    value__ = None

class MotorProtectionClass(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Possible values for property MotorProtectionClass

    enum MotorProtectionClass, values: None (0), Value10 (10), Value15 (15), Value20 (20), Value25 (25), Value30 (30), Value35 (35), Value40 (40), Value5 (5), Value7 (7)
    """

    Value10 = None
    Value15 = None
    Value20 = None
    Value25 = None
    Value30 = None
    Value35 = None
    Value40 = None
    Value5 = None
    Value7 = None
    value__ = None

class MotorProtectionReset(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Possible values for property MotorProtectionReset

    enum MotorProtectionReset, values: Auto (1), Manual (0)
    """

    Auto = None
    Manual = None
    value__ = None

class MotorProtectionResponseToPrewarning(
    Enum
):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Possible values for property MotorProtectionResponseToPrewarning

    enum MotorProtectionResponseToPrewarning, values: Deactivated (0), Signal (1), Trip (3), Warn (2)
    """

    Deactivated = None
    Signal = None
    Trip = None
    value__ = None
    Warn = None

class MotorProtectionResponseToTripLevel(
    Enum
):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Possible values for property MotorProtectionResponseToTripLevel

    enum MotorProtectionResponseToTripLevel, values: Deactivated (0), Signal (1), Trip (3), Warn (2)
    """

    Deactivated = None
    Signal = None
    Trip = None
    value__ = None
    Warn = None

class MotorProtectionStalledRotorResponse(
    Enum
):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Possible values for property MotorProtectionStalledRotorResponse

    enum MotorProtectionStalledRotorResponse, values: Deactivated (0), Signal (1), Trip (3), Warn (2)
    """

    Deactivated = None
    Signal = None
    Trip = None
    value__ = None
    Warn = None

class MotorProtectionTypeOfLoad(
    Enum
):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Possible values for property MotorProtectionTypeOfLoad

    enum MotorProtectionTypeOfLoad, values: OnePhase (1), TriPhase (0)
    """

    OnePhase = None
    TriPhase = None
    value__ = None

class MotorProtectionUnbalanceResponse(
    Enum
):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Possible values for property MotorProtectionUnbalanceResponse

    enum MotorProtectionUnbalanceResponse, values: Deactivated (0), Signal (1), Trip (3), Warn (2)
    """

    Deactivated = None
    Signal = None
    Trip = None
    value__ = None
    Warn = None

class NetType(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Network type

    enum NetType, values: Asi (4), Ethernet (3), Link (6), Mpi (2), PcInternal (7), Profibus (1), ProfibusIntegrated (8), Ptp (5), Unknown (0), Wan (9)
    """

    Asi = None
    Ethernet = None
    Link = None
    Mpi = None
    PcInternal = None
    Profibus = None
    ProfibusIntegrated = None
    Ptp = None
    Unknown = None
    value__ = None
    Wan = None

class Node(
    IEngineeringObject, IInternalObjectAccess, IEngineeringServiceProvider, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IServiceProvider'>, <type 'IInternalInstanceAccess'>
    """Node is an object which is used as an interface from DeviceItem to Subnet"""

    @property
    def ConnectedSubnet(self):
        """
        The connected subnet

        Get: ConnectedSubnet(self: Node) -> Subnet
        """
        ...
    @property
    def Name(self):
        """
        The name of the node

        Get: Name(self: Node) -> str
        """
        ...
    @property
    def NodeId(self):
        """
        The id of this node

        Get: NodeId(self: Node) -> str
        """
        ...
    @property
    def NodeType(self):
        """
        Particular type e.g. Industrial Ethernet or Wireless LAN

        Get: NodeType(self: Node) -> NetType

        Set: NodeType(self: Node) = value
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: Node) -> IEngineeringObject
        """
        ...
    def ConnectToSubnet(self, subnet):
        """
        ConnectToSubnet(self: Node, subnet: Subnet)

            Connects to the Subnet

            subnet: The subnet to be connected
        """
        ...
    def CreateAndConnectToSubnet(self, name):
        """
        CreateAndConnectToSubnet(self: Node, name: str) -> Subnet

            Create and connect to a subnet

            name: The name of the Subnet to create and connect

            Returns: Siemens.Engineering.HW.Subnet
        """
        ...
    def DisconnectFromSubnet(self):
        """
        DisconnectFromSubnet(self: Node)

            Disconnects a device from the given Subnet
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: Node) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: Node) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class NodeAssociation(
    IEngineeringAssociation, IInternalAssociationAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalCollectionAccess'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>
    """Associated nodes"""

    @property
    def Parent(self):
        """
        Gets the parent..

        Get: Parent(self: NodeAssociation) -> IEngineeringObject
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: NodeAssociation) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: NodeAssociation) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[Node](enumerable:  value: Node) -> bool"""
        ...
    def __ne__(self, *args): ...

class NodeComposition(
    IEngineeringComposition, IInternalCompositionAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """Composition of Nodes"""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: NodeComposition) -> IEngineeringObject
        """
        ...
    def Find(self, name):
        """
        Find(self: NodeComposition, name: str) -> Node

            Finds a given node

            name: The name of the Node instance to find

            Returns: Siemens.Engineering.HW.Node
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: NodeComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: NodeComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[Node](enumerable:  value: Node) -> bool"""
        ...
    def __ne__(self, *args): ...

class OpcUaSecurityPolicies(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Possible values for property OpcUaSecurityPolicies

    enum (flags) OpcUaSecurityPolicies, values: None (0), OpcUaSecurityPolicies128RSAS (2), OpcUaSecurityPolicies128RSASE (4), OpcUaSecurityPolicies256S (8), OpcUaSecurityPolicies256SE (16), OpcUaSecurityPolicies256SHAS (32), OpcUaSecurityPolicies256SHASE (64), OpcUaSecurityPoliciesNone (1)
    """

    OpcUaSecurityPolicies128RSAS = None
    OpcUaSecurityPolicies128RSASE = None
    OpcUaSecurityPolicies256S = None
    OpcUaSecurityPolicies256SE = None
    OpcUaSecurityPolicies256SHAS = None
    OpcUaSecurityPolicies256SHASE = None
    OpcUaSecurityPoliciesNone = None
    value__ = None

class OperatingHoursMonitoringResponse(
    Enum
):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Possible values for property OperatingHoursMonitoringResponse

    enum OperatingHoursMonitoringResponse, values: Deactivated (0), Signal (1), Warn (2)
    """

    Deactivated = None
    Signal = None
    value__ = None
    Warn = None

class OperatingMode(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Possible values for property OperatingMode

    enum OperatingMode, values: AnalogMode (67), Axis (270), ButtonHga (60), CascadingFunction (51), ConstantCurrent (255), Control (54), CountContinuously (2), Counting (23), CountOnce (3), CountPeriodically (4), D (256), Deactivated (281), DigitalInput (52), DigitalOutput (276), DiOversampling (24), DoOversampling (56), DosingMode (33), ElectronicShutdown (68), FastMode (1), FillLevel (62), FrequencyMeasurement (5), FrequencyOutput (266), FullDuplex4WireOperation (19), FullDuplex4WireOperationMultipointMaster (22), FullDuplex4WireOperationMultipointSlave (21), FullDuplex4WireOperationPtPConnection (25), HalfAndFullDuplex (55), HalfDuplex2WireOperation (20), I (257), Id (258), IncrementalEncoderABPhaseShifted (275), ManualOperation (278), Measuring (49), ModularCamControl (75), MotionControl (269), None (9), OnOffDelay (265), Oversampling (10), P (259), Pd (260), PeriodMeasurement (31), Pi (261), Pid (262), PositionFeedback (50), PositioningWithAnalogOutputs (18), PositioningWithDigitalOutputs (17), PulseOutput (264), PulseTrain (263), PulseTrainABphaseshifted (272), PulseTrainABphaseshiftedFourfold (271), PulseTrainAcountupBcountdown (273), PulseTrainApulseBdirection (274), PulseWidthModulation (7), PwmWithDcMotor (267), ReflectionBarrier (64), Reserved2 (61), Reserved6 (65), Reserved7 (66), RotationalSpeedMeasurement (32), Rs232c (268), SlowMode (0), StandardMode (57), TechnologyObject (277), TimerDI (34), TimerDQ (8), Toggle0Dot1Hz (26), Toggle0Dot5Hz (27), Toggle1Hz (6), Toggle2Hz (28), Trace (53), Value2Channels (38), Value4Channels (39), Value4ChannelsHardwareFilter (35), Value8ARo (40), Value8ARoS (48), Value8ChannelsHardwareFilter (36), Value8ChannelsSoftwareFilter (37), Window (63), WriteRead (30), WriteReadNeg (29)
    """

    AnalogMode = None
    Axis = None
    ButtonHga = None
    CascadingFunction = None
    ConstantCurrent = None
    Control = None
    CountContinuously = None
    Counting = None
    CountOnce = None
    CountPeriodically = None
    D = None
    Deactivated = None
    DigitalInput = None
    DigitalOutput = None
    DiOversampling = None
    DoOversampling = None
    DosingMode = None
    ElectronicShutdown = None
    FastMode = None
    FillLevel = None
    FrequencyMeasurement = None
    FrequencyOutput = None
    FullDuplex4WireOperation = None
    FullDuplex4WireOperationMultipointMaster = None
    FullDuplex4WireOperationMultipointSlave = None
    FullDuplex4WireOperationPtPConnection = None
    HalfAndFullDuplex = None
    HalfDuplex2WireOperation = None
    I = None
    Id = None
    IncrementalEncoderABPhaseShifted = None
    ManualOperation = None
    Measuring = None
    ModularCamControl = None
    MotionControl = None
    OnOffDelay = None
    Oversampling = None
    P = None
    Pd = None
    PeriodMeasurement = None
    Pi = None
    Pid = None
    PositionFeedback = None
    PositioningWithAnalogOutputs = None
    PositioningWithDigitalOutputs = None
    PulseOutput = None
    PulseTrain = None
    PulseTrainABphaseshifted = None
    PulseTrainABphaseshiftedFourfold = None
    PulseTrainAcountupBcountdown = None
    PulseTrainApulseBdirection = None
    PulseWidthModulation = None
    PwmWithDcMotor = None
    ReflectionBarrier = None
    Reserved2 = None
    Reserved6 = None
    Reserved7 = None
    RotationalSpeedMeasurement = None
    Rs232c = None
    SlowMode = None
    StandardMode = None
    TechnologyObject = None
    TimerDI = None
    TimerDQ = None
    Toggle0Dot1Hz = None
    Toggle0Dot5Hz = None
    Toggle1Hz = None
    Toggle2Hz = None
    Trace = None
    Value2Channels = None
    Value4Channels = None
    Value4ChannelsHardwareFilter = None
    Value8ARo = None
    Value8ARoS = None
    Value8ChannelsHardwareFilter = None
    Value8ChannelsSoftwareFilter = None
    value__ = None
    Window = None
    WriteRead = None
    WriteReadNeg = None

class OperatingRange(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Possible values for property OperatingRange

    enum OperatingRange, values: Cu100ClimaticRange (95), Cu100GostClimaticRange (78), Cu100GostStandardRange (79), Cu100StandardRange (96), Cu10ClimaticRange (74), Cu10GostClimaticRange (75), Cu10GostStandardRange (76), Cu10StandardRange (77), Cu50ClimaticRange (97), Cu50GostClimaticRange (80), Cu50GostStandardRange (81), Cu50StandardRange (98), Deactivated (0), Kty83slash110Silicon (70), Kty84slash130Silicon (71), LgNi1000ClimaticRange (60), LgNi1000StandardRange (61), Ni1000ClimaticRange (45), Ni1000StandardRange (51), Ni100ClimaticRange (44), Ni100GostClimaticRange (82), Ni100GostStandardRange (35), Ni100StandardRange (50), Ni10ClimaticRange (99), Ni10StandardRange (100), Ni120ClimaticRange (55), Ni120StandardRange (56), Ni200ClimaticRange (57), Ni200StandardRange (58), Ni500ClimaticRange (19), Ni500StandardRange (59), PlusMinus100mV (4), PlusMinus10mA (14), PlusMinus10V (11), PlusMinus1V (7), PlusMinus20mA (17), PlusMinus250mV (5), PlusMinus25mV (1), PlusMinus2dot5V (8), PlusMinus3dot2mA (12), PlusMinus500mV (6), PlusMinus50mV (2), PlusMinus5mA (13), PlusMinus5V (9), PlusMinus80mV (3), Pt1000ClimaticRange (43), Pt1000StandardRange (49), Pt100ClimaticRange (40), Pt100GostClimaticRange (85), Pt100GostStandardRange (86), Pt100StandardRange (46), Pt10ClimaticRange (101), Pt10GostClimaticRange (83), Pt10GostStandardRange (84), Pt10StandardRange (102), Pt200ClimaticRange (41), Pt200StandardRange (47), Pt500ClimaticRange (42), Pt500GostClimaticRange (89), Pt500GostStandardRange (90), Pt500StandardRange (48), Pt50ClimaticRange (103), Pt50GostClimaticRange (87), Pt50GostStandardRange (88), Pt50StandardRange (104), PTC (53), TypeB (20), TypeC (72), TypeE (22), TypeJ (25), TypeK (28), TypeL (26), TypeN (21), TypeR (23), TypeS (24), TypeT (27), TypeTxk (105), TypeTxkOrXkL (94), TypeTxKslashXKL (73), TypeU (29), Value0To10V (52), Value0To20mA (15), Value0To2V (92), Value1000Ohm (93), Value10KiloOhm (91), Value150Ohm (31), Value1To5mA (18), Value1To5V (10), Value300Ohm (32), Value3KiloOhm (54), Value48Ohm (30), Value4To20mA (16), Value600Ohm (33), Value6KiloOhm (34)
    """

    Cu100ClimaticRange = None
    Cu100GostClimaticRange = None
    Cu100GostStandardRange = None
    Cu100StandardRange = None
    Cu10ClimaticRange = None
    Cu10GostClimaticRange = None
    Cu10GostStandardRange = None
    Cu10StandardRange = None
    Cu50ClimaticRange = None
    Cu50GostClimaticRange = None
    Cu50GostStandardRange = None
    Cu50StandardRange = None
    Deactivated = None
    Kty83slash110Silicon = None
    Kty84slash130Silicon = None
    LgNi1000ClimaticRange = None
    LgNi1000StandardRange = None
    Ni1000ClimaticRange = None
    Ni1000StandardRange = None
    Ni100ClimaticRange = None
    Ni100GostClimaticRange = None
    Ni100GostStandardRange = None
    Ni100StandardRange = None
    Ni10ClimaticRange = None
    Ni10StandardRange = None
    Ni120ClimaticRange = None
    Ni120StandardRange = None
    Ni200ClimaticRange = None
    Ni200StandardRange = None
    Ni500ClimaticRange = None
    Ni500StandardRange = None
    PlusMinus100mV = None
    PlusMinus10mA = None
    PlusMinus10V = None
    PlusMinus1V = None
    PlusMinus20mA = None
    PlusMinus250mV = None
    PlusMinus25mV = None
    PlusMinus2dot5V = None
    PlusMinus3dot2mA = None
    PlusMinus500mV = None
    PlusMinus50mV = None
    PlusMinus5mA = None
    PlusMinus5V = None
    PlusMinus80mV = None
    Pt1000ClimaticRange = None
    Pt1000StandardRange = None
    Pt100ClimaticRange = None
    Pt100GostClimaticRange = None
    Pt100GostStandardRange = None
    Pt100StandardRange = None
    Pt10ClimaticRange = None
    Pt10GostClimaticRange = None
    Pt10GostStandardRange = None
    Pt10StandardRange = None
    Pt200ClimaticRange = None
    Pt200StandardRange = None
    Pt500ClimaticRange = None
    Pt500GostClimaticRange = None
    Pt500GostStandardRange = None
    Pt500StandardRange = None
    Pt50ClimaticRange = None
    Pt50GostClimaticRange = None
    Pt50GostStandardRange = None
    Pt50StandardRange = None
    PTC = None
    TypeB = None
    TypeC = None
    TypeE = None
    TypeJ = None
    TypeK = None
    TypeL = None
    TypeN = None
    TypeR = None
    TypeS = None
    TypeT = None
    TypeTxk = None
    TypeTxkOrXkL = None
    TypeTxKslashXKL = None
    TypeU = None
    Value0To10V = None
    Value0To20mA = None
    Value0To2V = None
    Value1000Ohm = None
    Value10KiloOhm = None
    Value150Ohm = None
    Value1To5mA = None
    Value1To5V = None
    Value300Ohm = None
    Value3KiloOhm = None
    Value48Ohm = None
    Value4To20mA = None
    Value600Ohm = None
    Value6KiloOhm = None
    value__ = None

class OperatingType(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Possible values for property OperatingType

    enum OperatingType, values: Current (2), Current2WireTransducer (4), Current4WireTransducer (3), Deactivated (0), Hart (24), Resistance (18), Resistor2Wire (7), Resistor3Wire (6), Resistor4Wire (5), RtdThermalResistorLinear (19), ThermalResistor2Wire (25), ThermalResistor3Wire (9), ThermalResistor4Wire (8), Thermocouple (10), Thermocouple0CCompLinear (22), Thermocouple50CCompLinear (23), ThermocoupleExtComp (11), ThermocoupleExtCompLinear (14), ThermocoupleIntComp (21), ThermocoupleIntCompLinear (13), Voltage (1)
    """

    Current = None
    Current2WireTransducer = None
    Current4WireTransducer = None
    Deactivated = None
    Hart = None
    Resistance = None
    Resistor2Wire = None
    Resistor3Wire = None
    Resistor4Wire = None
    RtdThermalResistorLinear = None
    ThermalResistor2Wire = None
    ThermalResistor3Wire = None
    ThermalResistor4Wire = None
    Thermocouple = None
    Thermocouple0CCompLinear = None
    Thermocouple50CCompLinear = None
    ThermocoupleExtComp = None
    ThermocoupleExtCompLinear = None
    ThermocoupleIntComp = None
    ThermocoupleIntCompLinear = None
    value__ = None
    Voltage = None

class OperatingTypeAndRange(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Possible values for property OperatingTypeAndRange

    enum OperatingTypeAndRange, values: Current0To20mA (2), Current2WireTransducer4To20mA (3), Current4To20mA (10), Current4WireTransducer4To20mA (20), Current4WireTransducerPlusMinus20mA (4), CurrentPlusMinus20mA (11), Deactivated (0), ThermocoupleTypeB (12), ThermocoupleTypeC (21), ThermocoupleTypeE (13), ThermocoupleTypeJ (14), ThermocoupleTypeK (8), ThermocoupleTypeL (15), ThermocoupleTypeN (16), ThermocoupleTypeR (17), ThermocoupleTypeS (18), ThermocoupleTypeT (19), Voltage1To5V (7), VoltagePlusMinus10V (9), VoltagePlusMinus2dot5V (5), VoltagePlusMinus5V (6), VoltagePlusMinus80mV (1)
    """

    Current0To20mA = None
    Current2WireTransducer4To20mA = None
    Current4To20mA = None
    Current4WireTransducer4To20mA = None
    Current4WireTransducerPlusMinus20mA = None
    CurrentPlusMinus20mA = None
    Deactivated = None
    ThermocoupleTypeB = None
    ThermocoupleTypeC = None
    ThermocoupleTypeE = None
    ThermocoupleTypeJ = None
    ThermocoupleTypeK = None
    ThermocoupleTypeL = None
    ThermocoupleTypeN = None
    ThermocoupleTypeR = None
    ThermocoupleTypeS = None
    ThermocoupleTypeT = None
    value__ = None
    Voltage1To5V = None
    VoltagePlusMinus10V = None
    VoltagePlusMinus2dot5V = None
    VoltagePlusMinus5V = None
    VoltagePlusMinus80mV = None

class PcInterfaceAssignmentMode(
    Enum
):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Interface assignment type for assignable interfaces

    enum PcInterfaceAssignmentMode, values: None (0), PcStation (1), SoftwarePlc (2)
    """

    PcStation = None
    SoftwarePlc = None
    value__ = None

class PcStationType(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Possible values for property PcStationType

    enum PcStationType, values: NotInstalled (0), PcStationV1Dot0 (1), PcStationV2Dot0 (2), PcStationV2Dot1 (3), PcStationV2Dot2 (4), PcStationV2Dot3 (5), PcStationV2Dot4 (6), PcStationV2Dot7 (7)
    """

    NotInstalled = None
    PcStationV1Dot0 = None
    PcStationV2Dot0 = None
    PcStationV2Dot1 = None
    PcStationV2Dot2 = None
    PcStationV2Dot3 = None
    PcStationV2Dot4 = None
    PcStationV2Dot7 = None
    value__ = None

class PlcProtectionAccessLevel(
    Enum
):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Access Level entries -enum

    enum (flags) PlcProtectionAccessLevel, values: FullAccess (1), FullAccessIncludingFailsafe (5), HMIAccess (3), NoAccess (4), None (0), ReadAccess (2)
    """

    FullAccess = None
    FullAccessIncludingFailsafe = None
    HMIAccess = None
    NoAccess = None
    ReadAccess = None
    value__ = None

class ResponseToOvershoot(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Possible values for property ResponseToOvershoot

    enum ResponseToOvershoot, values: Deactivated (0), Signal (1), Trip (3), Warn (2)
    """

    Deactivated = None
    Signal = None
    Trip = None
    value__ = None
    Warn = None

class ResponseToPrewarning(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Possible values for property ResponseToPrewarning

    enum ResponseToPrewarning, values: Deactivated (0), Signal (1), Warn (2)
    """

    Deactivated = None
    Signal = None
    value__ = None
    Warn = None

class RetentiveDataMemoryUsage(
    Enum
):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Possible values for property RetentiveDataMemoryUsage

    enum RetentiveDataMemoryUsage, values: NvramOfThePcSystem (1), PcMassStorage (0)
    """

    NvramOfThePcSystem = None
    PcMassStorage = None
    value__ = None

class RtClass(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Possible values for property RtClass

    enum RtClass, values: IRT (2), None (0), RT (1)
    """

    IRT = None
    RT = None
    value__ = None

class SignalDelaySelection(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Possible values for property SignalDelaySelection

    enum SignalDelaySelection, values: CableLength (1), None (0), SignalDelayTime (2)
    """

    CableLength = None
    SignalDelayTime = None
    value__ = None

class Software(
    IEngineeringObject, IInternalObjectAccess, IEquatable, IEngineeringServiceProvider  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Represents a base class of an object containing software components"""

    @property
    def Name(self):
        """
        The name of the software base

        Get: Name(self: Software) -> str
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: Software) -> IEngineeringObject
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: Software) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self) -> str:
        """Returns a System.String that represents the current System.Object.

        Returns:
            str: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class StopTimeOperatingHoursMonitoringResponse(
    Enum
):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Possible values for property StopTimeOperatingHoursMonitoringResponse

    enum StopTimeOperatingHoursMonitoringResponse, values: Deactivated (0), Signal (1), Warn (2)
    """

    Deactivated = None
    Signal = None
    value__ = None
    Warn = None

class Subnet(
    IEngineeringObject, IMasterCopySource, IInternalObjectAccess, IEngineeringServiceProvider, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IServiceProvider'>, <type 'IInternalInstanceAccess'>
    """Represents a Subnet, one of the following (SubnetMpi or SubnetIE) represents the net object"""

    @property
    def IoSystems(self):
        """
        Associated IO systems

        Get: IoSystems(self: Subnet) -> IoSystemAssociation
        """
        ...
    @property
    def Name(self):
        """
        The name of the Subnet

        Get: Name(self: Subnet) -> str

        Set: Name(self: Subnet) = value
        """
        ...
    @property
    def NetType(self):
        """
        Particular subnet net type

        Get: NetType(self: Subnet) -> NetType
        """
        ...
    @property
    def Nodes(self):
        """
        Associated nodes

        Get: Nodes(self: Subnet) -> NodeAssociation
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: Subnet) -> IEngineeringObject
        """
        ...
    @property
    def TypeIdentifier(self):
        """
        The type identifier of this Subnet

        Get: TypeIdentifier(self: Subnet) -> str
        """
        ...
    def Delete(self):
        """
        Delete(self: Subnet)

            Deletes this instance.
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: Subnet) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: Subnet) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class SubnetComposition(
    IEngineeringComposition, IInternalCompositionAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """Composition of Subnets"""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: SubnetComposition) -> IEngineeringObject
        """
        ...
    def CreateFrom(self, masterCopy):
        """
        CreateFrom(self: SubnetComposition, masterCopy: MasterCopy) -> Subnet

            Create subnet from MasterCopy

            masterCopy: The source MasterCopy

            Returns: Siemens.Engineering.HW.Subnet
        """
        ...
    def Find(self, name):
        """
        Find(self: SubnetComposition, name: str) -> Subnet

            Finds a given Subnet

            name: Name to find

            Returns: Siemens.Engineering.HW.Subnet
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: SubnetComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: SubnetComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[Subnet](enumerable:  value: Subnet) -> bool"""
        ...
    def __ne__(self, *args): ...

class SyncRole(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Possible values for property SyncRole

    enum SyncRole, values: NotSynchronized (0), RedundantSyncMaster (4), SyncMaster (1), SyncSlave (2)
    """

    NotSynchronized = None
    RedundantSyncMaster = None
    SyncMaster = None
    SyncSlave = None
    value__ = None

class TemperatureUnit(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Possible values for property TemperatureUnit

    enum TemperatureUnit, values: Deactivated (0), DegreesCelsius (1), DegreesFahrenheit (2), Kelvin (3)
    """

    Deactivated = None
    DegreesCelsius = None
    DegreesFahrenheit = None
    Kelvin = None
    value__ = None

class ThermistorResponseToSensorFault(
    Enum
):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Possible values for property ThermistorResponseToSensorFault

    enum ThermistorResponseToSensorFault, values: Deactivated (0), Signal (1), Trip (3), Warn (2)
    """

    Deactivated = None
    Signal = None
    Trip = None
    value__ = None
    Warn = None

class ThermistorResponseToTripLevel(
    Enum
):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Possible values for property ThermistorResponseToTripLevel

    enum ThermistorResponseToTripLevel, values: None (0), Signal (1), Trip (3), Warn (2)
    """

    Signal = None
    Trip = None
    value__ = None
    Warn = None

class TransferArea(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Addressmapping between local I-Slave / I-device and remote partner"""

    @property
    def Direction(self):
        """
        Direction of data communication between local and partner device

        Get: Direction(self: TransferArea) -> TransferAreaDirection

        Set: Direction(self: TransferArea) = value
        """
        ...
    @property
    def LocalAddresses(self):
        """
        Local addresses of a transfer area

        Get: LocalAddresses(self: TransferArea) -> AddressComposition
        """
        ...
    @property
    def LocalToPartnerLength(self):
        """
        Length of transferred data from local to partner device

        Get: LocalToPartnerLength(self: TransferArea) -> int

        Set: LocalToPartnerLength(self: TransferArea) = value
        """
        ...
    @property
    def Name(self):
        """
        Name of the transfer area

        Get: Name(self: TransferArea) -> str

        Set: Name(self: TransferArea) = value
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: TransferArea) -> IEngineeringObject
        """
        ...
    @property
    def PartnerAddresses(self):
        """
        Partner addresses of a transfer area

        Get: PartnerAddresses(self: TransferArea) -> AddressComposition
        """
        ...
    @property
    def PartnerToLocalLength(self):
        """
        Length of transferred data from partner to local device

        Get: PartnerToLocalLength(self: TransferArea) -> int

        Set: PartnerToLocalLength(self: TransferArea) = value
        """
        ...
    @property
    def PositionNumber(self):
        """
        Subslotnumber / Slotnumber of transfer area

        Get: PositionNumber(self: TransferArea) -> int
        """
        ...
    @property
    def TransferAreaMappingRules(self):
        """
        Mapping rules for transfer areas

        Get: TransferAreaMappingRules(self: TransferArea) -> TransferAreaMappingRuleComposition
        """
        ...
    @property
    def Type(self):
        """
        Transfer area type

        Get: Type(self: TransferArea) -> TransferAreaType

        Set: Type(self: TransferArea) = value
        """
        ...
    def Delete(self):
        """
        Delete(self: TransferArea)

            Deletes this instance.
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: TransferArea) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: TransferArea) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class TransferAreaComposition(
    IEngineeringComposition, IInternalCompositionAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """Composition of transfer areas"""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: TransferAreaComposition) -> IEngineeringObject
        """
        ...
    def Find(self, positionNumber):
        """
        Find(self: TransferAreaComposition, positionNumber: int) -> TransferArea

            Find a transfer area by position number

            positionNumber: Subslotnumber / Slotnumber of transfer area

            Returns: Siemens.Engineering.HW.TransferArea
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: TransferAreaComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: TransferAreaComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[TransferArea](enumerable:  value: TransferArea) -> bool"""
        ...
    def __ne__(self, *args): ...

class TransferAreaDirection(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Direction of data communication between local and partner device

    enum (flags) TransferAreaDirection, values: Bidirectional (3), LocalToPartner (1), None (0), PartnerToLocal (2)
    """

    Bidirectional = None
    LocalToPartner = None
    PartnerToLocal = None
    value__ = None

class TransferAreaMappingRule(
    IEngineeringObject, IInternalObjectAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalInstanceAccess'>
    """Mapping rule for transfer area"""

    @property
    def Begin(self):
        """
        Bit address of the begin of the mapped data

        Get: Begin(self: TransferAreaMappingRule) -> int

        Set: Begin(self: TransferAreaMappingRule) = value
        """
        ...
    @property
    def End(self):
        """
        Bit address of the end of the mapped data

        Get: End(self: TransferAreaMappingRule) -> int

        Set: End(self: TransferAreaMappingRule) = value
        """
        ...
    @property
    def IoType(self):
        """
        Type of data to be mapped (Input or Output)

        Get: IoType(self: TransferAreaMappingRule) -> AddressIoType

        Set: IoType(self: TransferAreaMappingRule) = value
        """
        ...
    @property
    def Offset(self):
        """
        Offset of the transfered data

        Get: Offset(self: TransferAreaMappingRule) -> int

        Set: Offset(self: TransferAreaMappingRule) = value
        """
        ...
    @property
    def Parent(self):
        """
        EOM parent of this object

        Get: Parent(self: TransferAreaMappingRule) -> IEngineeringObject
        """
        ...
    @property
    def PositionNumber(self):
        """
        Transfer area mapping rule number

        Get: PositionNumber(self: TransferAreaMappingRule) -> int
        """
        ...
    @property
    def Target(self):
        """
        I/O module or sub-module to be mapped

        Get: Target(self: TransferAreaMappingRule) -> DeviceItem

        Set: Target(self: TransferAreaMappingRule) = value
        """
        ...
    def Delete(self):
        """
        Delete(self: TransferAreaMappingRule)

            Deletes this instance.
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: TransferAreaMappingRule) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: TransferAreaMappingRule) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __ne__(self, *args): ...

class TransferAreaMappingRuleComposition(
    IEngineeringComposition, IInternalCompositionAccess, IEquatable  # type: ignore
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>
    """Mapping rules for transfer areas"""

    @property
    def Parent(self):
        """
        Gets the parent.

        Get: Parent(self: TransferAreaMappingRuleComposition) -> IEngineeringObject
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: TransferAreaMappingRuleComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...
    def ToString(self):
        """
        ToString(self: TransferAreaMappingRuleComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...
    def __contains__(self, *args):  # cannot find CLR method
        """__contains__[TransferAreaMappingRule](enumerable:  value: TransferAreaMappingRule) -> bool"""
        ...
    def __ne__(self, *args): ...

class TransferAreaType(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Type of transfer area

    enum TransferAreaType, values: CD (2), F_PS (3), MS (1), None (0), TM (4)
    """

    CD = None
    F_PS = None
    MS = None
    TM = None
    value__ = None

class TransmissionRateAndDuplex(
    Enum
):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Possible values for property TransmissionRateAndDuplex

    enum TransmissionRateAndDuplex, values: AsyncFiber10MbpsFullDuplex (13), AsyncFiber10MbpsHalfDuplex (12), AUI10Mbps (1), Automatic (8), FO10000MbpsFullDuplex (31), FO1000MbpsFullDuplex (26), FO1000MbpsFullDuplexLD (24), FO100MbpsFullDuplex (18), FO100MbpsFullDuplexLD (46), None (0), POFPCF100MbpsFullDuplex (54), TP1000MbpsFullDuplex (30), TP100MbpsFullDuplex (16), TP100MbpsHalfDuplex (15), TP10MbpsFullDuplex (11), TP10MbpsHalfDuplex (10), X1000MbpsFullDuplex (22)
    """

    AsyncFiber10MbpsFullDuplex = None
    AsyncFiber10MbpsHalfDuplex = None
    AUI10Mbps = None
    Automatic = None
    FO10000MbpsFullDuplex = None
    FO1000MbpsFullDuplex = None
    FO1000MbpsFullDuplexLD = None
    FO100MbpsFullDuplex = None
    FO100MbpsFullDuplexLD = None
    POFPCF100MbpsFullDuplex = None
    TP1000MbpsFullDuplex = None
    TP100MbpsFullDuplex = None
    TP100MbpsHalfDuplex = None
    TP10MbpsFullDuplex = None
    TP10MbpsHalfDuplex = None
    value__ = None
    X1000MbpsFullDuplex = None

class TypeOfConsumerLoad(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Possible values for property TypeOfConsumerLoad

    enum TypeOfConsumerLoad, values: Motor (0), ResistiveLoad (1)
    """

    Motor = None
    ResistiveLoad = None
    value__ = None

class View(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    The list of possible views in the HW editor

    enum View, values: Device (0), Network (1), Topology (2)
    """

    Device = None
    Network = None
    Topology = None
    value__ = None

# variables with complex values
