import configparser
from tia_portal.version import TIAVersion
import os

DATA_PATH = os.path.join(os.path.expanduser("~"), ".tia_portal")
CONFIG_PATH = os.path.join(DATA_PATH, "config.ini")
VERSION = TIAVersion.V15_1


def load() -> None:
    config = configparser.ConfigParser()

    if not os.path.exists(DATA_PATH):
        os.makedirs(DATA_PATH)

    if not os.path.exists(CONFIG_PATH):
        config["DEFAULT"] = {
            "version": "V17",
        }
        config["USER"] = {}
        config.write(open(CONFIG_PATH, "w", encoding="utf-8"))

    config.read(CONFIG_PATH)
    global VERSION
    VERSION = (
        TIAVersion[config["DEFAULT"]["version"]]
        if config["USER"].get("version") is None
        else TIAVersion[config["USER"]["version"]]
    )


def set_version(version: TIAVersion) -> None:
    config = configparser.ConfigParser()
    config.read(CONFIG_PATH)

    config["USER"]["version"] = version.name
    with open(CONFIG_PATH, "w", encoding="utf-8") as configfile:
        config.write(configfile)
