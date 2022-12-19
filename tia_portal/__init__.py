from __future__ import annotations

import os
import shutil
from typing import Any, Iterator, List, Optional, Union

import config as cfg
import exceptions as tia_e
from protocol.composition import Composition, CompositionItem
from protocol.objects import TiaObject
from version import TIAVersion

cfg.load()

from System.Diagnostics import Process
from System.IO import DirectoryInfo, FileInfo

tia = cfg.tia
comp = cfg.comp
hw = cfg.hw
hwf = cfg.hwf
sw = cfg.sw
swb = cfg.swb
lib = cfg.lib
lib_mc = cfg.lib_mc

class Device(CompositionItem[hw.Device]):
    def __init__(self, parent: Devices, name: str):
        self.parent = parent
        self.name = name

        if self.parent.value is None:
            raise tia_e.InvalidDeviceComposition("Parent value is None")

        value = self.parent.value.Find(name)

        if value is None:
            self.value = None
        else:
            self.value = value

    @staticmethod
    def find(object: Devices, name: str) -> Device:
        return object.find(name)

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

class Devices(Composition[Device, hw.DeviceComposition]):
    def __init__(self, parent: Project) -> None:
        self.parent = parent

        if self.parent.value is None:
            raise tia_e.InvalidProject("Project value is None")

        value = self.parent.value.Devices

        if value is None:
            self.value = None
        else:
            self.value = value

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

class DeviceItem(CompositionItem[hw.DeviceItem]):
    def __init__(self, parent: DeviceItems, name: str):
        self.parent = parent
        self.name = name

        if self.parent.value is None:
            raise tia_e.InvalidDeviceItemComposition("Parent value is None")

        value = self.parent.value.Find(name)

        if value is None:
            self.value = None
        else:
            self.value = value

    @staticmethod
    def find(object: DeviceItems, name: str) -> DeviceItem:
        return object.find(name)

    def get_software(self):
        if self.value is None:
            raise tia_e.InvalidDeviceItem("Value is None")

        software_container = self.value.GetService[hwf.SoftwareContainer]()

        if software_container is None:
            return None

        if software_container.Software is None:
            return None

        software_type = software_container.Software.ToString()

        if software_type == "Siemens.Engineering.SW.PlcSoftware":
            return PLCSoftware(self)

    def get_items(self) -> Optional[DeviceItems]:
        if self.value is None:
            raise tia_e.InvalidDeviceItem("Value is None")

        if self.value.DeviceItems.Count > 0:
            return DeviceItems(self)

class DeviceItems(Composition[DeviceItem, hw.DeviceItemComposition]):
    def __init__(self, parent: Union[Device, DeviceItem]) -> None:
        self.parent = parent

        if self.parent.value is None:
            raise tia_e.InvalidDevice("Device value is None")

        value = self.parent.value.DeviceItems

        if value is None:
            self.value = None
        else:
            self.value = value

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

class PLCSoftware(TiaObject[sw.PlcSoftware]):
    def __init__(self, parent: DeviceItem) -> None:
        self.parent = parent

        if self.parent.value is None:
            raise tia_e.InvalidDeviceItem("Value is None")

        software_container = self.parent.value.GetService[hwf.SoftwareContainer]()

        if software_container is None:
            raise tia_e.InvalidDeviceItem("Software container is None")

        if software_container.Software is None:
            raise tia_e.InvalidDeviceItem("Software is None")

        value = software_container.Software

        if not isinstance(value, sw.PlcSoftware):
            raise tia_e.InvalidSoftwareType("Software is not PLC software")

        self.value = value

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
            for group in self.get_system_block_groups():
                blocks.extend(group.get_all_blocks(True))
            for group in self.get_user_block_groups():
                blocks.extend(group.get_all_blocks(True))

            return blocks

class PLCSystemBlockGroup(CompositionItem[swb.PlcSystemBlockGroup]):
    def __init__(self, parent: PLCSystemBlockGroups, name: str) -> None:
        self.parent = parent
        self.name = name

        if self.parent.value is None:
            raise tia_e.InvalidSystemBlockGroupComposition("Parent value is None")

        value = self.parent.value.Find(name)

        if value is None:
            self.value = None
        else:
            self.value = value

    @staticmethod
    def find(object: PLCSystemBlockGroups, name: str) -> PLCSystemBlockGroup:
        return object.find(name)

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

class PLCSystemBlockGroups(Composition[PLCSystemBlockGroup, swb.PlcSystemBlockGroupComposition]):
    def __init__(self, parent: Union[PLCSoftware, PLCSystemBlockGroup]) -> None:
        self.parent = parent

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

class PLCUserBlockGroup(CompositionItem[swb.PlcBlockUserGroup]):
    def __init__(self, parent: PLCUserBlockGroups, name: str) -> None:
        self.parent = parent
        self.name = name

        if self.parent.value is None:
            raise tia_e.InvalidUserBlockGroupComposition("Parent value is None")

        value = self.parent.value.Find(name)

        if value is None:
            self.value = None
        else:
            self.value = value

    @staticmethod
    def find(object: PLCUserBlockGroups, name: str) -> PLCUserBlockGroup:
        return object.find(name)

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

class PLCUserBlockGroups(Composition[PLCUserBlockGroup, swb.PlcBlockUserGroupComposition]):
    def __init__(self, parent: Union[PLCSoftware, PLCUserBlockGroup]) -> None:
        self.parent = parent

        if self.parent.value is None:
            raise tia_e.InvalidSoftware("Software value is None")

        value = None

        if not isinstance(self.parent.value, sw.PlcSoftware):
            value = self.parent.value.Groups

        if not isinstance(self.parent.value, swb.PlcBlockUserGroup):
            value = self.parent.value.BlockGroup.SystemBlockGroups

        if value is None:
            self.value = None
        else:
            self.value = value

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

class PLCBlock(CompositionItem[swb.PlcBlock]):
    def __init__(self, parent: PLCBlocks, name: str) -> None:
        self.parent = parent
        self.name = name

        if self.parent.value is None:
            raise tia_e.InvalidBlockComposition("Parent value is None")

        value = self.parent.value.Find(name)

        if value is None:
            self.value = None
        else:
            self.value = value

    @staticmethod
    def find(object: PLCBlocks, name: str) -> PLCBlock:
        return object.find(name)

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

class PLCBlocks(Composition[PLCBlock, swb.PlcBlockComposition]):
    def __init__(self, parent: Union[PLCSoftware, PLCSystemBlockGroup, PLCUserBlockGroup]) -> None:
        self.parent = parent

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

    def find(self, name: str) -> PLCBlock:
        if self.value is None:
            raise tia_e.InvalidBlockComposition("Value is None")

        return PLCBlock(self, name)

    def __iter__(self) -> Iterator[PLCBlock]:
        if self.value is None:
            raise tia_e.InvalidBlockComposition("Value is None")

        for block in self.value:
            yield PLCBlock(self, block.Name)

    def create(self, type: str, name: str) -> PLCBlock:
        if self.value is None:
            raise tia_e.InvalidBlockComposition("Value is None")

        file = os.path.join(cfg.DATA_PATH, "empty_blocks", f"{type}.xml")
        new_file = os.path.join(cfg.DATA_PATH, "temp", f"{name}.xml")

        if not os.path.isfile(file):
            raise tia_e.InvalidBlockType(f"Invalid block type: {type}")

        shutil.copyfile(file, new_file)

        with open(new_file, "r") as f:
            data = f.read()

        data = data.replace("__NAME__", name)

        with open(new_file, "w") as f:
            f.write(data)

        file_info = FileInfo(new_file)

        self.value.Import(file_info, tia.ImportOptions.Override)

        os.remove(new_file)

        return PLCBlock(self, name)

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

class Project(TiaObject[tia.Project]):
    def __init__(self, client: Client, path: str, name: str, version: Optional[TIAVersion] = None):
        self.client = client
        self.path = path
        self.name = name

        self.version = version if version is not None else cfg.VERSION
        self.value = None

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
            session = tia.TiaPortal(tia.TiaPortalMode.WithoutUserInterface)
        else:
            session = self.client.session

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

    def is_modified(self):
        if self.value is None:
            raise tia_e.TIAInvalidProject("Project is None")
        return self.value.IsModified

    def compile(self) -> None:
        if self.value is None:
            raise tia_e.TIAInvalidProject("Project is None")

        devices = self.value.Devices

        devices = [item for device in self.value.Devices for item in device.DeviceItems]
        software_containers = [item.GetService[hwf.SoftwareContainer]() for item in devices]
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

    @property
    def devices(self) -> Devices:
        ...

    @devices.getter
    def devices(self) -> Devices:
        if self.value is None:
            raise tia_e.TIAInvalidProject("Project is None")
        return Devices(self)

    @devices.setter
    def devices(self, value: Any) -> None:
        raise NotImplementedError("Devices can only be accessed through the devices property")

# class GlobalLibrary:
#     def __init__(self, client: Client, name: str):
#         self.client = client
#         self.value: Optional[lib.GlobalLibrary] = None
#         self.name = name

#         if not self.client.session:
#             raise tia_e.TIAInvalidSession("Session is None")

#         info =  self.client.session.GlobalLibraries.GetGlobalLibraryInfos()

#         for lib_info in info:
#             if lib_info.Name == self.name:
#                 self.value = self.client.session.GlobalLibraries.Open(lib_info)
#                 return

# class MasterCopy(Protocol):
#     def __init__(self, global_library: GlobalLibrary, name: str):
#         ...

# class MasterCopyGlobalLibrary(MasterCopy):
#     def __init__(self, global_library: GlobalLibrary, name: str):
#         self.global_library = global_library
#         self.value: Optional[lib_mc.MasterCopySystemFolder] = None

#         if not self.global_library.value:
#             raise tia_e.TIAGlobalLibraryNotFound("Global Library is None")

#         copy = self.global_library.value.MasterCopyFolder.MasterCopies.Find(name)

#         if isinstance(copy, lib_mc.MasterCopy):
#             self.value = copy
#         else:
#             self.value = None
