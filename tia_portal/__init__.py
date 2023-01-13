from __future__ import annotations

import clr
import os
import shutil
from typing import Any, Iterator, List, Optional, Union

import tia_portal.config as cfg
import tia_portal.exceptions as tia_e
from tia_portal.protocol.composition import Composition, CompositionItem
from tia_portal.protocol.objects import TiaObject
from tia_portal.version import TIAVersion

cfg.load()

from System.Diagnostics import Process
from System.IO import DirectoryInfo, FileInfo

dll_path = f"C:\\Program Files\\Siemens\\Automation\\Portal {cfg.VERSION.name}\\PublicAPI\\V{cfg.VERSION.value.replace('_', '.')}\\Siemens.Engineering.dll"

if not os.path.exists(dll_path):
    raise tia_e.LibraryDLLNotFound(f"Could not find {dll_path}")

try:
    clr.AddReference(dll_path)
except Exception as e:
    raise tia_e.LibraryImportError(f"Could not load {dll_path}") from e

try:
    import Siemens.Engineering as tia
except Exception as e:
    raise tia_e.LibraryImportError(f"Could not import Siemens.Engineering") from e

try:
    import Siemens.Engineering.Compiler as comp
except Exception as e:
    raise tia_e.LibraryImportError(f"Could not import Siemens.Engineering.Compiler") from e

try:
    import Siemens.Engineering.HW as hw
except Exception as e:
    raise tia_e.LibraryImportError(f"Could not import Siemens.Engineering.HW") from e

try:
    import Siemens.Engineering.HW.Features as hwf
except Exception as e:
    raise tia_e.LibraryImportError(f"Could not import Siemens.Engineering.HW.Features") from e

try:
    import Siemens.Engineering.SW as sw
except Exception as e:
    raise tia_e.LibraryImportError(f"Could not import Siemens.Engineering.SW") from e

try:
    import Siemens.Engineering.SW.Blocks as swb
except Exception as e:
    raise tia_e.LibraryImportError(f"Could not import Siemens.Engineering.SW.Blocks") from e

try:
    import Siemens.Engineering.Library as lib
except Exception as e:
    raise tia_e.LibraryImportError(f"Could not import Siemens.Engineering.Library") from e

try:
    import Siemens.Engineering.Library.MasterCopies as lib_mc
except Exception as e:
    raise tia_e.LibraryImportError(f"Could not import Siemens.Engineering.Library.MasterCopies") from e

try:
    import Siemens.Engineering.Library.Types as lib_type
except Exception as e:
    raise tia_e.LibraryImportError(f"Could not import Siemens.Engineering.Library.Types") from e


class Device(CompositionItem):
    def __init__(self, parent: Devices, name: str):
        self.parent = parent
        self.name = name
        self.__value = None

        if self.parent.value is None:
            raise tia_e.InvalidDeviceComposition("Parent value is None")

        value = self.parent.value.Find(name)

        if value is None:
            self.value = None
        else:
            self.value = value

    @property
    def value(self) -> Optional[hw.Device]:
        return self.__value

    @value.setter
    def value(self, value: Optional[hw.Device]) -> None:
        self.__value = value

    def exists(self) -> bool:
        return self.value is not None

    def remove(self) -> None:
        if self.value is None:
            raise tia_e.InvalidDevice("Value is None")

        self.value.Delete()
        self.value = None

    def delete(self) -> None:
        self.remove()

    def get_items(self) -> DeviceItems:
        return DeviceItems(self)


class Devices(Composition[Device]):
    def __init__(self, parent: Project) -> None:
        self.parent = parent
        self.__value = None

        if self.parent.value is None:
            raise tia_e.InvalidProject("Project value is None")

        value = self.parent.value.Devices

        if value is None:
            self.value = None
        else:
            self.value = value

    @property
    def value(self) -> Optional[hw.DeviceComposition]:
        return self.__value

    @value.setter
    def value(self, value: Optional[hw.DeviceComposition]) -> None:
        self.__value = value

    def find(self, name: str) -> Device:
        if self.value is None:
            raise tia_e.InvalidDeviceComposition("Value is None")

        return Device(self, name)

    def __iter__(self) -> Iterator[Device]:
        if self.value is None:
            raise tia_e.InvalidDeviceComposition("Value is None")

        for device in self.value:
            yield Device(self, device.Name)

    def create(self, HwTypeIdentifier: str, name: str, device_name: Optional[str]) -> Device:
        if self.value is None:
            raise tia_e.InvalidDeviceComposition("Value is None")

        device = Device(self, name)

        if device.value is not None:
            raise tia_e.DeviceAlreadyExists(f"Device '{name}' already exists")

        if device_name is None:
            self.value.CreateWithItem(HwTypeIdentifier, name, None)
        else:
            self.value.CreateWithItem(HwTypeIdentifier, device_name, name)

        return Device(self, name)

    def create_PLC(self, article_no: str, version: str, name: str, device_name: str) -> Device:
        hw_id = f"OrderNumber:{article_no}/{version}"
        return self.create(hw_id, name, device_name)

    def create_HMI(self, article_no: str, version: str, name: str) -> Device:
        hw_id = f"OrderNumber:{article_no}/{version}"
        return self.create(hw_id, name, None)


class DeviceItem(CompositionItem):
    def __init__(self, parent: DeviceItems, name: str):
        self.parent = parent
        self.name = name
        self.__value = None

        if self.parent.value is None:
            raise tia_e.InvalidDeviceItemComposition("Parent value is None")

        value = None

        for item in self.parent.value:
            if item.Name == name:
                value = item
                break

        if value is None:
            self.value = None
        else:
            self.value = value

    @property
    def value(self) -> Optional[hw.DeviceItem]:
        return self.__value

    @value.setter
    def value(self, value: Optional[hw.DeviceItem]) -> None:
        self.__value = value

    def get_software(self) -> Union[PLCSoftware, None]:
        if self.value is None:
            raise tia_e.InvalidDeviceItem("Value is None")

        software_container = self.value.GetService[hwf.SoftwareContainer]()  # type: ignore

        if software_container is None:
            return None

        if software_container.Software is None:
            return None

        software_type = software_container.Software.ToString()

        if software_type == "Siemens.Engineering.SW.PlcSoftware":
            return PLCSoftware(self)

        return None

    def get_items(self) -> Optional[DeviceItems]:
        if self.value is None:
            raise tia_e.InvalidDeviceItem("Value is None")

        if self.value.DeviceItems.Count > 0:
            return DeviceItems(self)

        return None


class DeviceItems(Composition[DeviceItem]):
    def __init__(self, parent: Union[Device, DeviceItem]) -> None:
        self.parent = parent
        self.__value = None

        if self.parent.value is None:
            raise tia_e.InvalidDevice("Device value is None")

        value = self.parent.value.DeviceItems

        if value is None:
            self.value = None
        else:
            self.value = value

    @property
    def value(self) -> Optional[hw.DeviceItemComposition]:
        return self.__value

    @value.setter
    def value(self, value: Optional[hw.DeviceItemComposition]) -> None:
        self.__value = value

    def find(self, name: str) -> DeviceItem:
        if self.value is None:
            raise tia_e.InvalidDeviceItemComposition("Value is None")

        return DeviceItem(self, name)

    def __iter__(self) -> Iterator[DeviceItem]:
        if self.value is None:
            raise tia_e.InvalidDeviceItemComposition("Value is None")

        for device_item in self.value:
            yield DeviceItem(self, device_item.Name)

    def get_device_items(self) -> list[DeviceItem]:
        device_items: list[DeviceItem] = []
        for device_item in self:
            device_items.append(device_item)

        return device_items


class PLCSoftware(TiaObject):
    def __init__(self, parent: DeviceItem) -> None:
        self.parent = parent
        self.__value = None

        if self.parent.value is None:
            raise tia_e.InvalidDeviceItem("Value is None")

        software_container = self.parent.value.GetService[hwf.SoftwareContainer]()  # type: ignore

        if software_container is None:
            raise tia_e.InvalidDeviceItem("Software container is None")

        if software_container.Software is None:
            raise tia_e.InvalidDeviceItem("Software is None")

        value = software_container.Software

        if not isinstance(value, sw.PlcSoftware):
            raise tia_e.InvalidSoftwareType("Software is not PLC software")

        self.value = value

    @property
    def value(self) -> Optional[sw.PlcSoftware]:
        return self.__value

    @value.setter
    def value(self, value: Optional[sw.PlcSoftware]) -> None:
        self.__value = value

    def get_system_block_groups(self) -> PLCSystemBlockGroups:
        if self.value is None:
            raise tia_e.InvalidSoftware("Value is None")

        return PLCSystemBlockGroups(self)

    def get_user_block_groups(self) -> PLCUserBlockGroups:
        if self.value is None:
            raise tia_e.InvalidSoftware("Value is None")

        return PLCUserBlockGroups(self)

    def get_blocks(self) -> PLCBlocks:
        if self.value is None:
            raise tia_e.InvalidSoftware("Value is None")

        return PLCBlocks(self)

    def get_all_blocks(self, recursive: bool = False) -> list[PLCBlock]:
        if not recursive:
            return [block for block in self.get_blocks()]
        else:
            blocks = [block for block in self.get_blocks()]
            for system_group in self.get_system_block_groups():
                blocks.extend(system_group.get_all_blocks(True))
            for user_group in self.get_user_block_groups():
                blocks.extend(user_group.get_all_blocks(True))

            return blocks


class PLCSystemBlockGroup(CompositionItem):
    def __init__(self, parent: PLCSystemBlockGroups, name: str) -> None:
        self.parent = parent
        self.name = name
        self.__value = None

        if self.parent.value is None:
            raise tia_e.InvalidSystemBlockGroupComposition("Parent value is None")

        value = self.parent.value.Find(name)

        if value is None:
            self.value = None
        else:
            self.value = value

    @property
    def value(self) -> Optional[swb.PlcSystemBlockGroup]:
        return self.__value

    @value.setter
    def value(self, value: Optional[swb.PlcSystemBlockGroup]) -> None:
        self.__value = value

    def get_groups(self) -> PLCSystemBlockGroups:
        if self.value is None:
            raise tia_e.InvalidSystemBlockGroup("Value is None")

        return PLCSystemBlockGroups(self)

    def get_blocks(self) -> PLCBlocks:
        if self.value is None:
            raise tia_e.InvalidSystemBlockGroup("Value is None")

        return PLCBlocks(self)

    def get_all_blocks(self, recursive: bool = False) -> list[PLCBlock]:
        if not recursive:
            return [block for block in self.get_blocks()]
        else:
            blocks = [block for block in self.get_blocks()]
            for group in self.get_groups():
                blocks.extend(group.get_all_blocks(True))

            return blocks


class PLCSystemBlockGroups(Composition[PLCSystemBlockGroup]):
    def __init__(self, parent: Union[PLCSoftware, PLCSystemBlockGroup]) -> None:
        self.parent = parent
        self.__value = None

        if self.parent.value is None:
            raise tia_e.InvalidSoftware("Software value is None")

        value = None

        if not isinstance(self.parent.value, sw.PlcSoftware):
            value = self.parent.value.Groups

        if not isinstance(self.parent.value, swb.PlcSystemBlockGroup):
            value = self.parent.value.BlockGroup.SystemBlockGroups

        if value is None:
            self.value = None
        else:
            self.value = value

    @property
    def value(self) -> Optional[swb.PlcSystemBlockGroupComposition]:
        return self.__value

    @value.setter
    def value(self, value: Optional[swb.PlcSystemBlockGroupComposition]) -> None:
        self.__value = value

    def find(self, name: str) -> PLCSystemBlockGroup:
        if self.value is None:
            raise tia_e.InvalidSystemBlockGroupComposition("Value is None")

        return PLCSystemBlockGroup(self, name)

    def __iter__(self) -> Iterator[PLCSystemBlockGroup]:
        if self.value is None:
            raise tia_e.InvalidSystemBlockGroupComposition("Value is None")

        for system_block_group in self.value:
            yield PLCSystemBlockGroup(self, system_block_group.Name)

    def create(self, name: str) -> PLCSystemBlockGroup:
        if self.value is None:
            raise tia_e.InvalidSystemBlockGroupComposition("Value is None")

        self.value.Create(name)

        return PLCSystemBlockGroup(self, name)


class PLCUserBlockGroup(CompositionItem):
    def __init__(self, parent: PLCUserBlockGroups, name: str) -> None:
        self.parent = parent
        self.name = name
        self.__value = None

        if self.parent.value is None:
            raise tia_e.InvalidUserBlockGroupComposition("Parent value is None")

        value = self.parent.value.Find(name)

        if value is None:
            self.value = None
        else:
            self.value = value

    @property
    def value(self) -> Optional[swb.PlcBlockUserGroup]:
        return self.__value

    @value.setter
    def value(self, value: Optional[swb.PlcBlockUserGroup]) -> None:
        self.__value = value

    def get_groups(self) -> PLCUserBlockGroups:
        if self.value is None:
            raise tia_e.InvalidUserBlockGroup("Value is None")

        return PLCUserBlockGroups(self)

    def get_blocks(self) -> PLCBlocks:
        if self.value is None:
            raise tia_e.InvalidUserBlockGroup("Value is None")

        return PLCBlocks(self)

    def get_all_blocks(self, recursive: bool = False) -> list[PLCBlock]:
        if not recursive:
            return [block for block in self.get_blocks()]
        else:
            blocks = [block for block in self.get_blocks()]
            for group in self.get_groups():
                blocks.extend(group.get_all_blocks(True))

            return blocks


class PLCUserBlockGroups(Composition[PLCUserBlockGroup]):
    def __init__(self, parent: Union[PLCSoftware, PLCUserBlockGroup]) -> None:
        self.parent = parent
        self.__value = None

        if self.parent.value is None:
            raise tia_e.InvalidSoftware("Software value is None")

        if not isinstance(self.parent.value, sw.PlcSoftware):
            value = self.parent.value.Groups

        if not isinstance(self.parent.value, swb.PlcBlockUserGroup):
            value = self.parent.value.BlockGroup.Groups

        if value is None:
            self.value = None
        else:
            self.value = value

    @property
    def value(self) -> Optional[swb.PlcBlockUserGroupComposition]:
        return self.__value

    @value.setter
    def value(self, value: Optional[swb.PlcBlockUserGroupComposition]) -> None:
        self.__value = value

    def find(self, name: str) -> PLCUserBlockGroup:
        if self.value is None:
            raise tia_e.InvalidUserBlockGroupComposition("Value is None")

        return PLCUserBlockGroup(self, name)

    def __iter__(self) -> Iterator[PLCUserBlockGroup]:
        if self.value is None:
            raise tia_e.InvalidUserBlockGroupComposition("Value is None")

        for user_block_group in self.value:
            yield PLCUserBlockGroup(self, user_block_group.Name)

    def create(self, name: str) -> PLCUserBlockGroup:
        if self.value is None:
            raise tia_e.InvalidUserBlockGroupComposition("Value is None")

        self.value.Create(name)

        return PLCUserBlockGroup(self, name)


class PLCBlock(CompositionItem):
    def __init__(self, parent: PLCBlocks, name: str) -> None:
        self.parent = parent
        self.name = name
        self.__value = None

        if self.parent.value is None:
            raise tia_e.InvalidBlockComposition("Parent value is None")

        value = self.parent.value.Find(name)

        if value is None:
            self.value = None
        else:
            self.value = value

    @property
    def value(self) -> Optional[swb.PlcBlock]:
        return self.__value

    @value.setter
    def value(self, value: Optional[swb.PlcBlock]) -> None:
        self.__value = value

    def export(self) -> str:
        if self.value is None:
            raise tia_e.InvalidBlock("Value is None")

        if not self.value.IsConsistent:
            raise tia_e.InvalidBlock("Block is inconsistent")

        new_file = os.path.join(cfg.DATA_PATH, "exported_blocks", f"{self.name}.xml")

        if not os.path.exists(os.path.dirname(new_file)):
            os.makedirs(os.path.dirname(new_file))

        file_info = FileInfo(new_file)

        self.value.Export(file_info, tia.ExportOptions(0))

        return new_file


class PLCBlocks(Composition[PLCBlock]):
    def __init__(self, parent: Union[PLCSoftware, PLCSystemBlockGroup, PLCUserBlockGroup]) -> None:
        self.parent = parent
        self.__value = None

        if isinstance(self.parent, PLCSoftware):
            if self.parent.value is None:
                raise tia_e.InvalidSoftware("Software value is None")

            self.value = self.parent.value.BlockGroup.Blocks
        elif isinstance(self.parent, PLCSystemBlockGroup):
            if self.parent.value is None:
                raise tia_e.InvalidSystemBlockGroup("Value is None")

            self.value = self.parent.value.Blocks
        else:
            if self.parent.value is None:
                raise tia_e.InvalidUserBlockGroup("Value is None")

            self.value = self.parent.value.Blocks

    @property
    def value(self) -> Optional[swb.PlcBlockComposition]:
        return self.__value

    @value.setter
    def value(self, value: Optional[swb.PlcBlockComposition]) -> None:
        self.__value = value

    def find(self, name: str) -> PLCBlock:
        if self.value is None:
            raise tia_e.InvalidBlockComposition("Value is None")

        return PLCBlock(self, name)

    def __iter__(self) -> Iterator[PLCBlock]:
        if self.value is None:
            raise tia_e.InvalidBlockComposition("Value is None")

        for block in self.value:
            yield PLCBlock(self, block.Name)

    def create(self, path: str, name: str) -> PLCBlock:
        if self.value is None:
            raise tia_e.InvalidBlockComposition("Value is None")

        if not os.path.isfile(path):
            raise tia_e.InvalidPath(f"Invalid path: {path}")

        new_file = os.path.join(cfg.DATA_PATH, "temp", os.path.basename(path))

        if not os.path.exists(os.path.dirname(new_file)):
            os.makedirs(os.path.dirname(new_file))

        shutil.copyfile(path, new_file)

        with open(new_file, "r") as f:
            data = f.read()

        data = data.replace("__NAME__", name)

        with open(new_file, "w") as f:
            f.write(data)

        file_info = FileInfo(new_file)

        self.value.Import(file_info, tia.ImportOptions.Override)

        os.remove(new_file)

        return PLCBlock(self, name)

    def create_instance_database(self, name: str, fb_name: str) -> PLCBlock:
        if self.value is None:
            raise tia_e.InvalidBlockComposition("Value is None")

        self.value.CreateInstanceDB(name, True, 1, fb_name)

        return PLCBlock(self, name)

    def create_prodiag_block(self, name: str):
        if self.value is None:
            raise tia_e.InvalidBlockComposition("Value is None")

        self.value.CreateFB(name, True, 1, swb.ProgrammingLanguage.ProDiag)

        idb_name = name.replace("FB", "IDB")

        if not self.parent.get_groups().find("IDB"):
            self.parent.get_groups().create("IDB")

        self.parent.get_groups().find("IDB").get_blocks().create_instance_database(idb_name, name)

        return PLCBlock(self, name)


class GlobalLibrary(CompositionItem):
    def __init__(self, parent: GlobalLibraries, name: str):
        self.parent = parent
        self.name = name
        self.__value = None

        if self.parent.value is None:
            raise tia_e.InvalidGlobalLibraryComposition("Parent value is None")

        self.value = None

        for global_library in self.parent.value:
            if global_library.Name == name:
                self.value = global_library
                break

    @property
    def value(self) -> Optional[lib.GlobalLibrary]:
        return self.__value

    @value.setter
    def value(self, value: Optional[lib.GlobalLibrary]) -> None:
        self.__value = value

    @property
    def type_folder(self) -> LibraryTypeFolder:
        if self.value is None:
            raise tia_e.InvalidGlobalLibrary("Value is None")

        return LibraryTypeFolder(self)

    @type_folder.setter
    def type_folder(self, value: LibraryTypeFolder) -> None:
        raise NotImplementedError("Cannot set type folder")

    @property
    def master_copy_folder(self) -> MasterCopyFolder:
        if self.value is None:
            raise tia_e.InvalidGlobalLibrary("Value is None")

        return MasterCopyFolder(self)

    @master_copy_folder.setter
    def master_copy_folder(self, value: MasterCopyFolder) -> None:
        raise NotImplementedError("Cannot set master copy folder")


class GlobalLibraries(Composition[GlobalLibrary]):
    def __init__(self, parent: Client):
        self.parent = parent
        self.__value = None

        if self.parent.session is None:
            raise tia_e.TIAInvalidSession("Session is None")

        self.value = self.parent.session.GlobalLibraries

    @property
    def value(self) -> Optional[lib.GlobalLibraryComposition]:
        return self.__value

    @value.setter
    def value(self, value: Optional[lib.GlobalLibraryComposition]) -> None:
        self.__value = value

    def find(self, name: str) -> GlobalLibrary:
        if self.value is None:
            raise tia_e.InvalidGlobalLibraryComposition("Value is None")

        return GlobalLibrary(self, name)

    def __iter__(self) -> Iterator[GlobalLibrary]:
        if self.value is None:
            raise tia_e.InvalidGlobalLibraryComposition("Value is None")

        for global_library in self.value:
            yield GlobalLibrary(self, global_library.Name)


class LibraryTypeFolder(TiaObject):
    def __init__(self, parent: GlobalLibrary):
        self.parent = parent
        self.__value = None

        if self.parent.value is None:
            raise tia_e.InvalidGlobalLibrary("Value is None")

        self.value = self.parent.value.TypeFolder

    @property
    def value(self) -> Optional[lib_type.LibraryTypeFolder]:
        return self.__value

    @value.setter
    def value(self, value: Optional[lib_type.LibraryTypeFolder]) -> None:
        self.__value = value

    @property
    def folders(self) -> LibraryTypeUserFolders:
        if self.value is None:
            raise tia_e.InvalidTypeFolder("Value is None")

        return LibraryTypeUserFolders(self)

    @folders.setter
    def folders(self, value: LibraryTypeUserFolders) -> None:
        raise NotImplementedError("Cannot set type user folders")

    @property
    def types(self) -> LibraryTypes:
        if self.value is None:
            raise tia_e.InvalidTypeFolder("Value is None")

        return LibraryTypes(self)

    @types.setter
    def types(self, value: LibraryTypes) -> None:
        raise NotImplementedError("Cannot set types")


class LibraryTypeUserFolder(CompositionItem):
    def __init__(self, parent: LibraryTypeUserFolders, name: str):
        self.parent = parent
        self.name = name
        self.__value = None

        if self.parent.value is None:
            raise tia_e.InvalidTypeUserFolderComposition("Parent value is None")

        self.value = self.parent.value.Find(name)

    @property
    def value(self) -> Optional[lib_type.LibraryTypeUserFolder]:
        return self.__value

    @value.setter
    def value(self, value: Optional[lib_type.LibraryTypeUserFolder]) -> None:
        self.__value = value

    @property
    def folders(self) -> LibraryTypeUserFolders:
        if self.value is None:
            raise tia_e.InvalidTypeFolder("Value is None")

        return LibraryTypeUserFolders(self)

    @folders.setter
    def folders(self, value: LibraryTypeUserFolders) -> None:
        raise NotImplementedError("Cannot set type user folders")

    @property
    def types(self) -> LibraryTypes:
        if self.value is None:
            raise tia_e.InvalidTypeFolder("Value is None")

        return LibraryTypes(self)

    @types.setter
    def types(self, value: LibraryTypes) -> None:
        raise NotImplementedError("Cannot set types")


class LibraryTypeUserFolders(Composition[LibraryTypeUserFolder]):
    def __init__(self, parent: Union[LibraryTypeFolder, LibraryTypeUserFolder]):
        self.parent = parent
        self.__value = None

        if self.parent.value is None:
            raise tia_e.InvalidTypeFolder("Value is None")

        self.value = self.parent.value.Folders

    @property
    def value(self) -> Optional[lib_type.LibraryTypeUserFolderComposition]:
        return self.__value

    @value.setter
    def value(self, value: Optional[lib_type.LibraryTypeUserFolderComposition]) -> None:
        self.__value = value

    def find(self, name: str) -> LibraryTypeUserFolder:
        if self.value is None:
            raise tia_e.InvalidTypeUserFolderComposition("Value is None")

        return LibraryTypeUserFolder(self, name)

    def __iter__(self) -> Iterator[LibraryTypeUserFolder]:
        if self.value is None:
            raise tia_e.InvalidTypeUserFolderComposition("Value is None")

        for folder in self.value:
            yield LibraryTypeUserFolder(self, folder.Name)


class LibraryType(CompositionItem):
    def __init__(self, parent: LibraryTypes, name: str):
        self.parent = parent
        self.name = name
        self.__value = None

        if self.parent.value is None:
            raise tia_e.InvalidTypeComposition("Parent value is None")

        self.value = self.parent.value.Find(name)

    @property
    def value(self) -> Optional[lib_type.LibraryType]:
        return self.__value

    @value.setter
    def value(self, value: Optional[lib_type.LibraryType]) -> None:
        self.__value = value


class LibraryTypes(Composition[LibraryType]):
    def __init__(self, parent: Union[LibraryTypeFolder, LibraryTypeUserFolder]):
        self.parent = parent
        self.__value = None

        if self.parent.value is None:
            raise tia_e.InvalidTypeFolder("Value is None")

        self.value = self.parent.value.Types

    @property
    def value(self) -> Optional[lib_type.LibraryTypeComposition]:
        return self.__value

    @value.setter
    def value(self, value: Optional[lib_type.LibraryTypeComposition]) -> None:
        self.__value = value

    def find(self, name: str) -> LibraryType:
        if self.value is None:
            raise tia_e.InvalidTypeComposition("Value is None")

        return LibraryType(self, name)

    def __iter__(self) -> Iterator[LibraryType]:
        if self.value is None:
            raise tia_e.InvalidTypeComposition("Value is None")

        for type in self.value:
            yield LibraryType(self, type.Name)


class MasterCopyFolder(TiaObject):
    def __init__(self, parent: GlobalLibrary):
        self.parent = parent
        self.__value = None

        if self.parent.value is None:
            raise tia_e.InvalidGlobalLibrary("Value is None")

        self.value = self.parent.value.MasterCopyFolder

    @property
    def value(self) -> Optional[lib_mc.MasterCopyFolder]:
        return self.__value

    @value.setter
    def value(self, value: Optional[lib_mc.MasterCopyFolder]) -> None:
        self.__value = value

    @property
    def folders(self) -> MasterCopyUserFolders:
        if self.value is None:
            raise tia_e.InvalidTypeFolder("Value is None")

        return MasterCopyUserFolders(self)

    @folders.setter
    def folders(self, value: MasterCopyUserFolders) -> None:
        raise NotImplementedError("Cannot set type user folders")

    @property
    def master_copies(self) -> MasterCopies:
        if self.value is None:
            raise tia_e.InvalidMasterCopyFolder("Value is None")

        return MasterCopies(self)

    @master_copies.setter
    def master_copies(self, value: MasterCopies) -> None:
        raise NotImplementedError("Cannot set master copies")


class MasterCopyUserFolder(CompositionItem):
    def __init__(self, parent: MasterCopyUserFolders, name: str):
        self.parent = parent
        self.name = name
        self.__value = None

        if self.parent.value is None:
            raise tia_e.InvalidMasterCopyUserFolderComposition("Parent value is None")

        self.value = self.parent.value.Find(name)

    @property
    def value(self) -> Optional[lib_mc.MasterCopyUserFolder]:
        return self.__value

    @value.setter
    def value(self, value: Optional[lib_mc.MasterCopyUserFolder]) -> None:
        self.__value = value

    @property
    def folders(self) -> MasterCopyUserFolders:
        if self.value is None:
            raise tia_e.InvalidTypeFolder("Value is None")

        return MasterCopyUserFolders(self)

    @folders.setter
    def folders(self, value: MasterCopyUserFolders) -> None:
        raise NotImplementedError("Cannot set type user folders")

    @property
    def master_copies(self) -> MasterCopies:
        if self.value is None:
            raise tia_e.InvalidMasterCopyFolder("Value is None")

        return MasterCopies(self)

    @master_copies.setter
    def master_copies(self, value: MasterCopies) -> None:
        raise NotImplementedError("Cannot set master copies")


class MasterCopyUserFolders(Composition[MasterCopyUserFolder]):
    def __init__(self, parent: Union[MasterCopyFolder, MasterCopyUserFolder]):
        self.parent = parent
        self.__value = None

        if self.parent.value is None:
            raise tia_e.InvalidMasterCopyFolder("Value is None")

        self.value = self.parent.value.Folders

    @property
    def value(self) -> Optional[lib_mc.MasterCopyUserFolderComposition]:
        return self.__value

    @value.setter
    def value(self, value: Optional[lib_mc.MasterCopyUserFolderComposition]) -> None:
        self.__value = value

    def find(self, name: str) -> MasterCopyUserFolder:
        if self.value is None:
            raise tia_e.InvalidMasterCopyUserFolderComposition("Value is None")

        return MasterCopyUserFolder(self, name)

    def __iter__(self) -> Iterator[MasterCopyUserFolder]:
        if self.value is None:
            raise tia_e.InvalidMasterCopyUserFolderComposition("Value is None")

        for folder in self.value:
            yield MasterCopyUserFolder(self, folder.Name)


class MasterCopy(CompositionItem):
    def __init__(self, parent: MasterCopies, name: str):
        self.parent = parent
        self.name = name
        self.__value = None

        if self.parent.value is None:
            raise tia_e.InvalidMasterCopyComposition("Parent value is None")

        self.value = self.parent.value.Find(name)

    @property
    def value(self) -> Optional[lib_mc.MasterCopy]:
        return self.__value

    @value.setter
    def value(self, value: Optional[lib_mc.MasterCopy]) -> None:
        self.__value = value


class MasterCopies(Composition[MasterCopy]):
    def __init__(self, parent: Union[MasterCopyFolder, MasterCopyUserFolder]):
        self.parent = parent
        self.__value = None

        if self.parent.value is None:
            raise tia_e.InvalidMasterCopyFolder("Value is None")

        self.value = self.parent.value.MasterCopies

    @property
    def value(self) -> Optional[lib_mc.MasterCopyComposition]:
        return self.__value

    @value.setter
    def value(self, value: Optional[lib_mc.MasterCopyComposition]) -> None:
        self.__value = value

    def find(self, name: str) -> MasterCopy:
        if self.value is None:
            raise tia_e.InvalidMasterCopyComposition("Value is None")

        return MasterCopy(self, name)

    def __iter__(self) -> Iterator[MasterCopy]:
        if self.value is None:
            raise tia_e.InvalidMasterCopyComposition("Value is None")

        for master_copy in self.value:
            yield MasterCopy(self, master_copy.Name)


class Client:
    def __init__(self) -> None:
        self.session: Optional[tia.TiaPortal] = tia.TiaPortal(tia.TiaPortalMode.WithoutUserInterface)
        self.project: Optional[Project] = None

    # ==================================================================================================================
    # GUI actions
    # ==================================================================================================================
    def open_gui(self) -> None:
        if self.session is None:
            raise tia_e.TIAInvalidSession("Session is None")

        process = self.session.GetCurrentProcess()
        project_open = False

        if not process.Mode == tia.TiaPortalMode.WithUserInterface:
            if self.project and self.project.is_open():
                project_open = True
                self.project.close()
            self.session.Dispose()
            Process.GetProcessById(process.Id).Kill()
            self.session = tia.TiaPortal(tia.TiaPortalMode.WithUserInterface)

            if project_open and self.project:
                self.project.open()

    def close_gui(self) -> None:
        if self.session is None:
            raise tia_e.TIAInvalidSession("Session is None")
        process = self.session.GetCurrentProcess()
        project_open = False

        if process.Mode == tia.TiaPortalMode.WithUserInterface:
            if self.project and self.project.is_open():
                project_open = True
                self.project.close()

            self.session.Dispose()
            Process.GetProcessById(process.Id).Kill()
            self.session = tia.TiaPortal(tia.TiaPortalMode.WithoutUserInterface)

            if project_open and self.project:
                self.project.open()

    # ==================================================================================================================
    # QUITING AND CLOSING
    # ==================================================================================================================
    def close(self) -> None:
        if self.session is None:
            return

        if self.project and self.project.is_open():
            self.project.close()

        process = self.session.GetCurrentProcess()
        self.session.Dispose()
        self.session = None
        Process.GetProcessById(process.Id).Kill()

    def quit(self) -> None:
        self.close()

    def __del__(self) -> None:
        if self.session is None:
            return

        if self.project and self.project.is_open():
            self.project.force_close()

        process = self.session.GetCurrentProcess()
        self.session.Dispose()
        self.session = None
        Process.GetProcessById(process.Id).Kill()

    # ==================================================================================================================
    # PROJECTS
    # ==================================================================================================================

    def open_project(self, path: str, name: str, version: Optional[TIAVersion] = None) -> Project:
        if self.session is None:
            raise tia_e.TIAInvalidSession("Session is None")

        if self.project is not None and self.project.is_open():
            self.project.close()

        self.project = Project(self, path, name, version)
        self.project.open()

        return self.project

    def create_project(self, path: str, name: str, version: Optional[TIAVersion] = None) -> Project:
        if self.session is None:
            raise tia_e.TIAInvalidSession("Session is None")

        if self.project is not None and self.project.is_open():
            self.project.close()

        self.project = Project(self, path, name, version)
        self.project.create(True)

        return self.project

    def create_projects(self, path: str, names: List[str], version: Optional[TIAVersion] = None) -> List[Project]:
        if self.session is None:
            raise tia_e.TIAInvalidSession("Session is None")

        if self.project is not None:
            self.project.close()

        projects: List[Project] = []
        for name in names:
            project = Project(self, path, name, version)
            try:
                project.create(False)
            except tia_e.TIAProjectAlreadyExists:
                projects.append(project)
                continue
            projects.append(project)

        return projects


class Project(TiaObject):
    def __init__(self, client: Client, path: str, name: str, version: Optional[TIAVersion] = None):
        self.client = client
        self.path = path
        self.name = name
        self.__value = None

        self.version = version if version is not None else cfg.VERSION
        self.value = None

    @property
    def value(self) -> Optional[tia.Project]:
        return self.__value

    @value.setter
    def value(self, value: Optional[tia.Project]) -> None:
        self.__value = value

    def open(self) -> None:
        if self.client.session is None:
            raise tia_e.TIAInvalidSession("Session is None")

        if self.value is not None:
            print(f"There is already a Project open, closing {self.value.Name} before opening {self.name}")
            self.close()

        if isinstance(self.path, FileInfo):
            file_info = self.path
            self.name = file_info.Name.split(".")[0]
        else:
            if self.name is None:
                raise tia_e.TIAProjectNotFound("Name is None but path is a string")

            file_name = (
                self.name if self.name.endswith(f".ap{self.version.value}") else f"{self.name}.ap{self.version.value}"
            )
            file_path = os.path.join(self.path, self.name, file_name)
            self.name = self.name

            if not os.path.exists(file_path):
                raise tia_e.TIAProjectNotFound(f"File {file_path} does not exist")

            file_info = FileInfo(file_path)

        self.value = self.client.session.Projects.Open(file_info)

        self.client.project = self

    def close(self) -> None:
        if self.value is None:
            return
        self.save()
        self.value.Close()
        self.value = None

    def force_close(self) -> None:
        if self.value is None:
            return
        self.value.Close()
        self.value = None

    def create(self, open: bool = False) -> None:
        if not open:
            new_session = tia.TiaPortal(tia.TiaPortalMode.WithoutUserInterface)
            old_session = None
        else:
            new_session = None
            old_session = self.client.session

            if old_session is None:
                raise tia_e.TIAInvalidSession("Old session is None")

        session = new_session if not new_session is None else old_session

        if session is None:
            raise tia_e.TIAInvalidSession("Session is None")

        file_name = (
            self.name if self.name.endswith(f".ap{self.version.value}") else f"{self.name}.ap{self.version.value}"
        )
        file_path = os.path.join(self.path, self.name, file_name)

        if os.path.exists(file_path):
            raise tia_e.TIAProjectAlreadyExists(f"File {file_path} already exists")

        self.value = session.Projects.Create(DirectoryInfo(self.path), self.name)

        self.client.project = self

    def save(self) -> None:
        if self.value is None:
            raise tia_e.TIAInvalidProject("Project is None")
        if self.is_modified():
            self.value.Save()

    def is_modified(self) -> bool:
        if self.value is None:
            raise tia_e.TIAInvalidProject("Project is None")
        return self.value.IsModified

    def compile(self) -> None:
        if self.value is None:
            raise tia_e.TIAInvalidProject("Project is None")

        devices = [item for device in self.value.Devices for item in device.DeviceItems]
        software_containers = [item.GetService[hwf.SoftwareContainer]() for item in devices]  # type: ignore
        software_containers = [item for item in software_containers if item is not None]

        for software_container in software_containers:
            software = software_container.Software
            if software is None:
                continue
            software_compile_service: comp.ICompilable = software.GetService[comp.ICompilable]()  # type: ignore
            if software_compile_service is not None:
                software_compile_service.Compile()

    def get_file_info(self) -> FileInfo:
        if self.value is None:
            raise tia_e.TIAInvalidProject("Project is None")
        return self.value.Path

    def is_open(self) -> bool:
        return self.value is not None

    def get_device_item(self, name: str) -> Optional[DeviceItem]:
        if self.value is None:
            raise tia_e.TIAInvalidProject("Project is None")

        for device in self.devices:
            for item in device.get_items():
                if item.name == name:
                    return item

        return None

    def get_plcs(self) -> list[DeviceItem]:
        if self.value is None:
            raise tia_e.TIAInvalidProject("Project is None")

        plcs = []

        for device in self.devices:
            for item in device.get_items():
                if isinstance(item.get_software(), PLCSoftware):
                    plcs.append(item)

        return plcs

    @property
    def devices(self) -> Devices:
        if self.value is None:
            raise tia_e.TIAInvalidProject("Project is None")
        return Devices(self)

    @devices.setter
    def devices(self, value: Any) -> None:
        raise NotImplementedError("Devices can only be accessed through the devices property")
