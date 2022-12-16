from __future__ import annotations

import configparser
import os
import shutil
from typing import List, Optional, Protocol, Union

import clr
import exceptions as tia_e
from System.Diagnostics import Process
from System.IO import DirectoryInfo, FileInfo
from version import TIAVersion

DATA_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "data"))
config = configparser.ConfigParser()
CONFIG_PATH = os.path.join(DATA_PATH, "config.ini")

if not os.path.exists(DATA_PATH):
    os.mkdir(DATA_PATH)

if not os.path.exists(CONFIG_PATH):
    config["DEFAULT"] = {"version": "V15_1"}
    config["USER"] = {}
    config.write(open(CONFIG_PATH, "w"))

config.read(CONFIG_PATH)
VERSION = (
    TIAVersion[config["DEFAULT"]["version"]]
    if config["USER"].get("version") is None
    else TIAVersion[config["USER"]["version"]]
)

DLL_PATH = f"C:\\Program Files\\Siemens\\Automation\\Portal {VERSION.name}\\PublicAPI\\V{VERSION.value.replace('_', '.')}\\Siemens.Engineering.dll"

if not os.path.exists(DLL_PATH):
    raise tia_e.TIALibraryNotFound(f"File {DLL_PATH} does not exist")

try:
    clr.AddReference(DLL_PATH)
except Exception as e:
    raise tia_e.TIALibraryNotFound(f"Could not load {DLL_PATH}") from e

try:
    import Siemens.Engineering as tia
    import Siemens.Engineering.Compiler as comp  # type: ignore
    import Siemens.Engineering.HmiUnified as hmiu  # type: ignore
    import Siemens.Engineering.HW as hw  # type: ignore
    import Siemens.Engineering.HW.Features as hwf  # type: ignore
    import Siemens.Engineering.SW as sw  # type: ignore
    import Siemens.Engineering.SW.Blocks as swb  # type: ignore
    import Siemens.Engineering.Library.Types as lbt  # type: ignore
except Exception as e:
    raise tia_e.TIALibraryNotFound(f"Could not load {DLL_PATH}") from e


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


class Project:
    def __init__(self, client: Client, path: str, name: str, version: Optional[TIAVersion] = None):
        self.client = client
        self.path = path
        self.name = name

        self.version = version if version is not None else VERSION
        self.value: Optional[tia.Project] = None

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

    def get_devices(self) -> List[Device]:
        if self.value is None:
            raise tia_e.TIAInvalidProject("Project is None")
        return [Device(self, device.Name) for device in self.value.Devices]

    def find_device(self, name: str):
        if self.value is None:
            raise tia_e.TIAInvalidProject("Project is None")

        devices = self.get_devices()

        for device in devices:
            if device.name == name:
                return device

        raise tia_e.TIADeviceNotFound(f"Device {name} not found")

    # ================================================================================================================
    # Device
    # ================================================================================================================

    def create_device(self, HwTypeIdentifier: str, deviceName: str) -> Device:
        if self.value is None:
            raise tia_e.TIAInvalidProject("Project is None")

        device = Device(self, deviceName)
        device.create(HwTypeIdentifier, deviceName)

        return device

    def create_PLC(self, article_no: str, version: str, deviceName: str, deviceItemName: str) -> Device:
        if self.value is None:
            raise tia_e.TIAInvalidProject("Project is None")

        device = Device(self, deviceName)
        device.create_PLC(article_no, version, deviceItemName)

        return device

    def create_HMI(self, article_no: str, version: str, deviceName: str) -> Device:
        if self.value is None:
            raise tia_e.TIAInvalidProject("Project is None")

        device = Device(self, deviceName)
        device.create_HMI(article_no, version)

        return device


class Device:
    def __init__(self, project: Project, name: str) -> None:
        self.project = project
        self.name = name

        if self.project.value is not None:
            device = self.project.value.Devices.Find(self.name)
            if isinstance(device, hw.Device):
                self.value = device
            else:
                self.value = None

    def create(self, HwTypeIdentifier: str, deviceName: str) -> None:
        if self.project.value is None:
            raise tia_e.TIAInvalidProject("Project is None")
        if self.value is not None:
            raise tia_e.TIADeviceAlreadyExists(f"Device {self.name} already exists")
        self.value = self.project.value.Devices.CreateWithItem(HwTypeIdentifier, deviceName, self.name)

    def create_PLC(self, article_no: str, version: str, deviceName: str) -> None:
        hwIdentifier = f"OrderNumber:{article_no}/{version}"
        self.create(hwIdentifier, deviceName)

    def create_HMI(self, article_no: str, version: str) -> None:
        hwIdentifier = f"OrderNumber:{article_no}/{version}"
        if self.project.value is None:
            raise tia_e.TIAInvalidProject("Project is None")
        if self.value is not None:
            raise tia_e.TIADeviceAlreadyExists(f"Device {self.name} already exists")
        self.value = self.project.value.Devices.CreateWithItem(hwIdentifier, self.name, None)

    def exists(self) -> bool:
        return self.value is not None

    def remove(self) -> None:
        if self.value is None:
            raise tia_e.TIADeviceNotFound(f"Device {self.name} not found")
        self.value.Delete()
        self.value = None

    def delete(self) -> None:
        self.remove()

    def get_device_items(self) -> List[DeviceItem]:
        if self.value is None:
            raise tia_e.TIADeviceNotFound(f"Device {self.name} not found")
        return [DeviceItem(self, item.Name) for item in self.value.DeviceItems]


class DeviceItem:
    def __init__(self, parent: Union[Device, DeviceItem], name: str) -> None:
        self.parent = parent
        temp_parent = parent

        while not isinstance(temp_parent, Device) and isinstance(temp_parent, DeviceItem):
            temp_parent = temp_parent.parent

        if not isinstance(temp_parent, Device):
            raise tia_e.TIADeviceNotFound(f"Device not found")

        self.device: Device = temp_parent

        self.name = name

        if self.parent.value is not None:
            device_items = self.parent.value.DeviceItems
            for item in device_items:
                if item.Name == self.name:
                    self.value = item
                    break

    def get_software(self):
        if self.value is None:
            raise tia_e.TIADeviceItemNotFound(f"DeviceItem {self.name} not found")

        software_container = self.value.GetService[hwf.SoftwareContainer]()  # type: ignore
        if software_container is None:
            raise tia_e.TIADeviceItemNotFound(f"DeviceItem {self.name} not found")

        software_container: hwf.SoftwareContainer

        if software_container.Software is None:
            raise tia_e.TIADeviceItemNotFound(f"DeviceItem {self.name} not found")

        software_type = software_container.Software.ToString()

        if software_type == "Siemens.Engineering.SW.PlcSoftware":
            return PLCSoftware(self)

    def get_device_items(self) -> List[DeviceItem]:
        if self.value is None:
            raise tia_e.TIADeviceItemNotFound(f"DeviceItem {self.name} not found")
        return [DeviceItem(self, item.Name) for item in self.value.DeviceItems]


class PLCSoftware:
    def __init__(self, device_item: DeviceItem) -> None:
        self.device_item = device_item

        software_container = self.device_item.value.GetService[hwf.SoftwareContainer]()  # type: ignore
        if software_container is None:
            raise tia_e.TIADeviceItemNotFound(f"DeviceItem {self.device_item.name} not found")
        self.value: sw.PlcSoftware = software_container.Software

        if self.value is None:
            raise tia_e.TIADeviceItemNotFound(f"DeviceItem {self.device_item.name} not found")

        if not isinstance(self.value, sw.PlcSoftware):
            raise tia_e.TIADeviceItemNotFound(f"DeviceItem {self.device_item.name} not found")

    def get_system_block_groups(self) -> List[PLCSystemBlockGroup]:
        if self.value is None:
            raise tia_e.TIADeviceItemNotFound(f"DeviceItem {self.device_item.name} not found")
        return [PLCSystemBlockGroup(self, None, group.Name) for group in self.value.BlockGroup.SystemBlockGroups]

    def get_block_groups(self) -> List[PLCBlockUserGroup]:
        if self.value is None:
            raise tia_e.TIADeviceItemNotFound(f"DeviceItem {self.device_item.name} not found")
        return [PLCBlockUserGroup(self, None, group.Name) for group in self.value.BlockGroup.Groups]

    def get_blocks(self) -> List[PLCBlock]:
        if self.value is None:
            raise tia_e.TIADeviceItemNotFound(f"DeviceItem {self.device_item.name} not found")
        return [PLCBlock(self, block.Name) for block in self.value.BlockGroup.Blocks]


class PLCBlockGroup(Protocol):
    value: Optional[Union[swb.PlcSystemBlockGroup, swb.PlcBlockUserGroup]]
    plc_software: PLCSoftware
    group: Optional[Union[PLCSystemBlockGroup, PLCBlockUserGroup]]
    name: str

    def get_groups(self):
        ...

    def get_blocks(self) -> List[PLCBlock]:
        ...

    def create(self) -> None:
        ...


class PLCSystemBlockGroup(PLCBlockGroup):
    def __init__(self, plc_software: PLCSoftware, group: Optional[PLCSystemBlockGroup], name: str) -> None:
        self.plc_software = plc_software
        self.name = name
        self.group: Optional[PLCSystemBlockGroup] = group

        if self.plc_software.value is not None:
            self.value: Optional[swb.PlcSystemBlockGroup] = self.plc_software.value.BlockGroup.SystemBlockGroups.Find(
                self.name
            )
        else:
            self.value = None

    def get_groups(self) -> List[PLCSystemBlockGroup]:
        if self.value is None:
            raise tia_e.TIAGroupNotFound(f"Group {self.name} not found")
        return [PLCSystemBlockGroup(self.plc_software, self, item.Name) for item in self.value.Groups]

    def get_blocks(self) -> List[PLCBlock]:
        if self.value is None:
            raise tia_e.TIAGroupNotFound(f"Group {self.name} not found")
        return [PLCBlock(self, item.Name) for item in self.value.Blocks]

    def create(self) -> None:
        if self.group is None:
            if self.plc_software.value is None:
                raise tia_e.TIAInvalidProperty(f"PLCSoftware not found")
            else:
                self.plc_software.value.BlockGroup.SystemBlockGroups.Create(self.name)
                return
        if self.group.value is None:
            raise tia_e.TIAGroupNotFound(f"Group {self.group.name} not found")
        self.group.value.Groups.Create(self.name)


class PLCBlockUserGroup:
    def __init__(self, plc_software: PLCSoftware, group: Optional[PLCBlockUserGroup], name: str) -> None:
        self.plc_software = plc_software
        self.name = name
        self.group: Optional[PLCBlockUserGroup] = group

        if self.plc_software.value is not None:
            self.value: Optional[swb.PlcBlockUserGroup] = self.plc_software.value.BlockGroup.Groups.Find(self.name)
        else:
            self.value = None

    def get_groups(self) -> List[PLCBlockUserGroup]:
        if self.value is None:
            raise tia_e.TIAGroupNotFound(f"Group {self.name} not found")
        return [PLCBlockUserGroup(self.plc_software, self, item.Name) for item in self.value.Groups]

    def get_blocks(self) -> List[PLCBlock]:
        if self.value is None:
            raise tia_e.TIAGroupNotFound(f"Group {self.name} not found")
        return [PLCBlock(self, item.Name) for item in self.value.Blocks]

    def create(self) -> None:
        if self.group is None:
            if self.plc_software.value is None:
                raise tia_e.TIAInvalidProperty(f"PLCSoftware not found")
            else:
                self.plc_software.value.BlockGroup.Groups.Create(self.name)
                return
        if self.group.value is None:
            raise tia_e.TIAGroupNotFound(f"Group {self.group.name} not found")
        self.group.value.Groups.Create(self.name)


class PLCBlock:
    def __init__(self, parent: Union[PLCSoftware, PLCSystemBlockGroup, PLCBlockUserGroup], name: str) -> None:
        self.parent = parent
        self.name = name
        self.value = None

        self.parent_blocks = None

        if isinstance(self.parent, PLCSoftware):
            if self.parent.value is not None:
                self.parent_blocks = self.parent.value.BlockGroup.Blocks
        else:
            if self.parent.value is not None:
                self.parent_blocks = self.parent.value.Blocks

        if self.parent_blocks is not None:
            self.value = self.parent_blocks.Find(self.name)
        else:
            self.value = None

    def create(self):
        if self.parent_blocks is None:
            raise tia_e.TIAInvalidProperty(f"Parent blocks not found")

        file = os.path.join(DATA_PATH, "empty_block.xml")

        shutil.copyfile(file, f"{os.path.join(DATA_PATH, self.name)}.xml")

        with open(f"{os.path.join(DATA_PATH, self.name)}.xml", "r") as f:
            filedata = f.read()

        filedata = filedata.replace("__EMPTY_BLOCK__", self.name)

        with open(f"{os.path.join(DATA_PATH, self.name)}.xml", "w") as f:
            f.write(filedata)

        file_info = FileInfo(f"{os.path.join(DATA_PATH, self.name)}.xml")

        self.parent_blocks.Import(file_info, tia.ImportOptions.Override)

        os.remove(f"{os.path.join(DATA_PATH, self.name)}.xml")



        self.parent_blocks.CreateFrom(swb.CodeBlockLibraryTypeVersion)

    def export(self):
        if self.value is None:
            raise tia_e.TIABlockNotFound(f"Block {self.name} not found")

        if not self.value.IsConsistent:
            raise tia_e.TIAInconsistentBlock(
                f"Block {self.name} is inconsistent and needs to be compiled before exporting"
            )

        file_name = f"{self.name}.xml"

        file_info = rf"{os.path.join(DATA_PATH, file_name)}"

        file_info = FileInfo(file_info)

        return self.value.Export(file_info, tia.ExportOptions(0))
