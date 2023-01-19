# encoding: utf-8
# module Siemens.Engineering.MC.Drives.Enums calls itself Enums
# from Siemens.Engineering, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

from System import Enum

class AbsoluteIncrementalFlag(
    Enum
):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    AbsoluteIncrementalFlag of encoder

    enum AbsoluteIncrementalFlag, values: Absolute (0), Incremental (1)
    """

    Absolute = None
    Incremental = None
    value__ = None

class DriveObjectActivationState(
    Enum
):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    The state of the activation

    enum DriveObjectActivationState, values: Activate (1), Deactivate (0), DeactivateAndNotPresent (2)
    """

    Activate = None
    Deactivate = None
    DeactivateAndNotPresent = None
    value__ = None

class EncoderInterface(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    EncoderInterface of encoder

    enum EncoderInterface, values: DriveCliQ (3), DSub (2), HTL (4), None (0), SSI (5), Terminal (1)
    """

    DriveCliQ = None
    DSub = None
    HTL = None
    SSI = None
    Terminal = None
    value__ = None

class EncoderType(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    EOMEncoderType of encoder

    enum EncoderType, values: DriveCliQ (9), EnDat (5), HTL (6), HTLTTL (2), NoEncoder (0), Resolver (1), SinCos (4), SSIProtocoll (3), SSIProtocollAndHTLTTL (7), SSIProtocollAndSinCos (8)
    """

    DriveCliQ = None
    EnDat = None
    HTL = None
    HTLTTL = None
    NoEncoder = None
    Resolver = None
    SinCos = None
    SSIProtocoll = None
    SSIProtocollAndHTLTTL = None
    SSIProtocollAndSinCos = None
    value__ = None

class MotorType(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Type of motor

    enum MotorType, values: InductionMotor (1), MotorSeriesNumber1LA81PQ8StandardInduction (7), NoCodeNumber1LA7InductionMotorNoCodeNumber (6), NoCodeNumber1LA9InductionMotor (8), NoCodeNumber1LE1InductionMotor (3), NoCodeNumber1LG6InductionMotor (4), NoCodeNumber1xx1SIMOTICSFDInductionMotor (5), NoMotor (0), SynchronousMotor (2)
    """

    InductionMotor = None
    MotorSeriesNumber1LA81PQ8StandardInduction = None
    NoCodeNumber1LA7InductionMotorNoCodeNumber = None
    NoCodeNumber1LA9InductionMotor = None
    NoCodeNumber1LE1InductionMotor = None
    NoCodeNumber1LG6InductionMotor = None
    NoCodeNumber1xx1SIMOTICSFDInductionMotor = None
    NoMotor = None
    SynchronousMotor = None
    value__ = None

class ResetMode(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Reset mode of factory reset

    enum ResetMode, values: ParameterReset (0), SafetyParameterReset (1)
    """

    ParameterReset = None
    SafetyParameterReset = None
    value__ = None

class RotaryLinearFlag(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    AbsoluteIncrementalFlag of encoder

    enum RotaryLinearFlag, values: Linear (1), Rotary (0)
    """

    Linear = None
    Rotary = None
    value__ = None

class TelegramType(Enum):  # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>
    """
    Type of telegram

    enum TelegramType, values: AdditionalTelegram (2), MainTelegram (0), SafetyTelegram (3), SupplementaryTelegram (1), TorqueTelegram (4)
    """

    AdditionalTelegram = None
    MainTelegram = None
    SafetyTelegram = None
    SupplementaryTelegram = None
    TorqueTelegram = None
    value__ = None
