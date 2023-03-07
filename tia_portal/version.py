""" TIA Portal version. This module only has the Enum class TIAVersion. The Enum class is used to store the TIA Portal version. The TIA Portal version is used to determine the correct TIA Portal API to use. The TIA Portal version is stored in the config.ini file in the user's home directory. The config.ini file is created if it does not exist. The default version is V17. The user can change the version by calling the set_version function.
"""
from __future__ import annotations
from enum import Enum


class TiaVersion(Enum):
    """TIA Portal version. The TIA Portal version is used to determine the correct TIA Portal API to use. The TIA Portal version is stored in the config.ini file in the user's home directory. The config.ini file is created if it does not exist. The default version is V17. The user can change the version by calling the set_version function.

    Attributes:
        V15 (str): TIA Portal V15.
        V15_1 (str): TIA Portal V15.1.
        V16 (str): TIA Portal V16.
        V17 (str): TIA Portal V17.
    """

    V15 = "15"
    V15_1 = "15_1"
    V16 = "16"
    V17 = "17"
