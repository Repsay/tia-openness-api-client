import configparser
import clr
from version import TIAVersion
from exceptions import LibraryDLLNotFound, LibraryImportError
import os

DATA_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "data"))
CONFIG_PATH = os.path.join(DATA_PATH, "config.ini")

def load():
    config = configparser.ConfigParser()

    if not os.path.exists(DATA_PATH):
        os.makedirs(DATA_PATH)

    if not os.path.exists(CONFIG_PATH):
        config["DEFAULT"] = {
            "version": "V15_1",
        }
        config["USER"] = {}
        config.write(open(CONFIG_PATH, "w"))

    config.read(CONFIG_PATH)
    global VERSION
    VERSION = TIAVersion[config["DEFAULT"]["version"]] if config["USER"].get("version") is None else TIAVersion[config["USER"]["version"]]

    dll_path = f"C:\\Program Files\\Siemens\\Automation\\Portal {VERSION.name}\\PublicAPI\\V{VERSION.value.replace('_', '.')}\\Siemens.Engineering.dll"
    if not os.path.exists(dll_path):
        raise LibraryDLLNotFound(f"Could not find {dll_path}")

    try:
        clr.AddReference(dll_path)
    except Exception as e:
        raise LibraryImportError(f"Could not load {dll_path}") from e

    global tia
    try:
        import Siemens.Engineering as tia
    except Exception as e:
        raise LibraryImportError(f"Could not import Siemens.Engineering") from e

    global comp
    try:
        import Siemens.Engineering.Compiler as comp
    except Exception as e:
        raise LibraryImportError(f"Could not import Siemens.Engineering.Compiler") from e

    global hw
    try:
        import Siemens.Engineering.HW as hw
    except Exception as e:
        raise LibraryImportError(f"Could not import Siemens.Engineering.HW") from e

    global hwf
    try:
        import Siemens.Engineering.HW.Features as hwf
    except Exception as e:
        raise LibraryImportError(f"Could not import Siemens.Engineering.HW.Features") from e

    global sw
    try:
        import Siemens.Engineering.SW as sw
    except Exception as e:
        raise LibraryImportError(f"Could not import Siemens.Engineering.SW") from e

    global swb
    try:
        import Siemens.Engineering.SW.Blocks as swb
    except Exception as e:
        raise LibraryImportError(f"Could not import Siemens.Engineering.SW.Blocks") from e

    global lib
    try:
        import Siemens.Engineering.Library as lib
    except Exception as e:
        raise LibraryImportError(f"Could not import Siemens.Engineering.Library") from e

    global lib_mc
    try:
        import Siemens.Engineering.Library.MasterCopies as lib_mc
    except Exception as e:
        raise LibraryImportError(f"Could not import Siemens.Engineering.Library.MasterCopies") from e