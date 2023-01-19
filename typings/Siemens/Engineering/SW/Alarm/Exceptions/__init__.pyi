# encoding: utf-8
# module Siemens.Engineering.SW.Alarm.Exceptions calls itself Exceptions
# from Siemens.Engineering, Version=17.0.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class TextListNotFoundException(
    EngineeringTargetInvocationException
):  # skipped bases: <type '_Exception'>, <type 'ISerializable'>
    """
    If the given controller target does not contain any textlist this exception will be thrown.

    TextListNotFoundException()

    TextListNotFoundException(text: str)

    TextListNotFoundException(text: str, exception: Exception)

    TextListNotFoundException(text: str, *detailTexts: Array[str])
    """

    SerializeObjectState = None
