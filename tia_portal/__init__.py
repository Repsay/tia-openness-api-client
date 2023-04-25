"""This module contains the main classes of the TIA Portal Openness API."""  # pylint: disable=too-many-lines

from __future__ import annotations

import os
import re
import shutil
from typing import Any, Iterator, Optional, Union

import clr  # pylint: disable=import-error

import tia_portal.config as cfg
import tia_portal.exceptions as tia_e
from tia_portal.protocol.composition import Composition, CompositionItem
from tia_portal.protocol.objects import TiaObject
from tia_portal.version import TiaVersion

cfg.load()

from System.Diagnostics import Process  # type: ignore pylint: disable=import-error,wrong-import-position,wrong-import-order
from System.IO import DirectoryInfo, FileInfo  # type: ignore pylint: disable=import-error,wrong-import-position,wrong-import-order

dll_path = (
    f"C:\\Program Files\\Siemens\\Automation\\"
    f"Portal {cfg.VERSION.name}\\PublicAPI\\V{cfg.VERSION.value.replace('_', '.')}"
    "\\Siemens.Engineering.dll"
)

if not os.path.exists(dll_path):
    raise tia_e.LibraryDLLNotFound(f"Could not find {dll_path}")

try:
    clr.AddReference(dll_path)  # type: ignore pylint: disable=no-member
except Exception as e:
    raise tia_e.LibraryImportError(f"Could not load {dll_path}") from e

try:
    import Siemens.Engineering as tia  # type: ignore pylint: disable=import-error
except Exception as e:
    raise tia_e.LibraryImportError("Could not import Siemens.Engineering") from e

try:
    import Siemens.Engineering.Compiler as comp  # type: ignore pylint: disable=import-error
except Exception as e:
    raise tia_e.LibraryImportError(
        "Could not import Siemens.Engineering.Compiler"
    ) from e

try:
    import Siemens.Engineering.HW as hw  # type: ignore pylint: disable=import-error
except Exception as e:
    raise tia_e.LibraryImportError("Could not import Siemens.Engineering.HW") from e

try:
    import Siemens.Engineering.HW.Features as hwf  # type: ignore pylint: disable=import-error
except Exception as e:
    raise tia_e.LibraryImportError(
        "Could not import Siemens.Engineering.HW.Features"
    ) from e

try:
    import Siemens.Engineering.SW as sw  # type: ignore pylint: disable=import-error
except Exception as e:
    raise tia_e.LibraryImportError("Could not import Siemens.Engineering.SW") from e

try:
    import Siemens.Engineering.SW.Blocks as swb  # type: ignore pylint: disable=import-error
except Exception as e:
    raise tia_e.LibraryImportError(
        "Could not import Siemens.Engineering.SW.Blocks"
    ) from e

try:
    import Siemens.Engineering.Library as lib  # type: ignore pylint: disable=import-error
except Exception as e:
    raise tia_e.LibraryImportError(
        "Could not import Siemens.Engineering.Library"
    ) from e

try:
    import Siemens.Engineering.Library.MasterCopies as lib_mc  # type: ignore pylint: disable=import-error
except Exception as e:
    raise tia_e.LibraryImportError(
        "Could not import Siemens.Engineering.Library.MasterCopies"
    ) from e

try:
    import Siemens.Engineering.Library.Types as lib_type  # type: ignore pylint: disable=import-error
except Exception as e:
    raise tia_e.LibraryImportError(
        "Could not import Siemens.Engineering.Library.Types"
    ) from e


class Device(CompositionItem):
    """Represents a TIA Portal device. This device can be a PLC, HMI, etc. A device is part of a composition of devices.

    Attributes:
        parent (Devices): The parent composition of devices.
        name (str): The name of the device.
        value (Optional[hw.Device]): The value of the device and the connection to the C# library. So functions of the Openness API can be used on this variable.
    """

    def __init__(self, parent: Devices, name: str):
        """Initializes a device.

        Parameters:
            parent (Devices): The parent composition of devices.
            name (str): The name of the device.

        Raises:
            tia_e.InvalidDeviceComposition: If the parent value is None.
        """
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
        """Checks if the device exists by checking if the value is None.

        Returns:
            bool: True if the device exists, False otherwise.
        """
        return self.value is not None

    def remove(self) -> None:
        """Removes the device from the composition of devices.

        Raises:
            tia_e.InvalidDevice: If the value is None.
        """
        if self.value is None:
            raise tia_e.InvalidDevice("Value is None")

        self.value.Delete()
        self.value = None

    def delete(self) -> None:
        """Deletes the device from the composition of devices. This is an alias for remove."""
        self.remove()

    def get_items(self) -> DeviceItems:
        """Gets the items of the device.

        Returns:
            DeviceItems: The items of the device a composition of items.
        """
        return DeviceItems(self)


class Devices(Composition[Device]):
    """Represents a composition of devices. A device can be a PLC, HMI, etc.

    Attributes:
        parent (Project): The parent project.
        value (Optional[hw.DeviceComposition]): The value of the composition of devices
            and the connection to the C# library. So functions of the Openness API can be used on this variable.
    """

    def __init__(self, parent: Project) -> None:
        """Initializes a composition of devices.

        Parameters:
            parent (Project): The parent project.

        Raises:
            tia_e.InvalidProject: If the parent value is None.
        """
        self.parent = parent
        self.__value = None

        if self.parent.value is None:
            raise tia_e.InvalidProject("Project value is None")

        value = self.parent.value.Devices

        self.value = value

    @property
    def value(self) -> Optional[hw.DeviceComposition]:
        return self.__value

    @value.setter
    def value(self, value: Optional[hw.DeviceComposition]) -> None:
        self.__value = value

    def find(self, name: str) -> Device:
        """Finds a device by name.

        Parameters:
            name (str): The name of the device.

        Raises:
            tia_e.InvalidDeviceComposition: If the value is None.

        Returns:
            Device: The device with the given name.
        """
        if self.value is None:
            raise tia_e.InvalidDeviceComposition("Value is None")

        return Device(self, name)

    def __iter__(self) -> Iterator[Device]:
        """Iterates over all devices in the composition of devices.

        Raises:
            tia_e.InvalidDeviceComposition: If the value is None.

        Yields:
            Iterator[Device]: The next device in the composition of devices.
        """
        if self.value is None:
            raise tia_e.InvalidDeviceComposition("Value is None")

        device: hw.Device
        for device in self.value:
            yield Device(self, device.Name)

    def create(
        self,
        HwTypeIdentifier: str,
        name: str,
        device_name: Optional[str],  # pylint: disable=invalid-name
    ) -> Device:
        """Creates a device in the composition of devices.

        Parameters:
            HwTypeIdentifier (str): The hardware type identifier of the device.
                These can be found in the TIA Portal when creating a new device.
            name (str): The name of the device (This can be found in the network tab of the TIA Portal)
            device_name (Optional[str]): The device name of the device.
                This is the name of the device in the TIA Portal. This is optional in some cases.

        Raises:
            tia_e.InvalidDeviceComposition: If the value is None.
            tia_e.DeviceAlreadyExists: If the device already exists.

        Returns:
            Device: The created device.
        """
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

    def create_PLC(  # pylint: disable=invalid-name
        self, article_no: str, version: str, name: str, device_name: str
    ) -> Device:
        """Creates a PLC device in the composition of devices.

        Parameters:
            article_no (str): The article number of the PLC.
                This can be found in the TIA Portal when creating a new device.
            version (str): The version of the PLC. This can be found in the TIA Portal when creating a new device.
            name (str): The name of the device (This can be found in the network tab of the TIA Portal)
            device_name (str): The device name of the device. This is the name of the device in the TIA Portal.

        Returns:
            Device: The created device.
        """
        hw_id = f"OrderNumber:{article_no}/{version}"
        return self.create(hw_id, name, device_name)

    def create_HMI(
        self, article_no: str, version: str, name: str
    ) -> Device:  # pylint: disable=invalid-name
        """Creates a HMI device in the composition of devices.

        Parameters:
            article_no (str): The article number of the HMI.
                This can be found in the TIA Portal when creating a new device.
            version (str): The version of the HMI. This can be found in the TIA Portal when creating a new device.
            name (str): The name of the device (This can be found in the network tab of the TIA Portal)

        Returns:
            Device: The created device.
        """
        hw_id = f"OrderNumber:{article_no}/{version}"
        return self.create(hw_id, name, None)


class DeviceItem(CompositionItem):
    """Represents a device item. A device item can be a PLC object or a HMI object.
         This class contains more specific functions for PLC and HMI objects.

    Attributes:
        parent (DeviceItems): The parent device items. This is the composition of device items.
        name (str): The name of the device item.
        value (Optional[hw.DeviceItem]): The value of the device item
            and the connection to the C# library. So functions of the Openness
            API can be used on this variable.
    """

    def __init__(self, parent: DeviceItems, name: str):
        """Initializes the device item.

        Parameters:
            parent (DeviceItems): The parent device items. This is the composition of device items.
            name (str): The name of the device item.

        Raises:
            tia_e.InvalidDeviceItemComposition: If the parent value is None.
        """
        self.parent = parent
        self.name = name
        self.__value = None

        if self.parent.value is None:
            raise tia_e.InvalidDeviceItemComposition("Parent value is None")

        value = None

        item: hw.DeviceItem
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
        # TODO: Implement more different software types
        """Gets the software of the device item.

        Raises:
            tia_e.InvalidDeviceItem: If the value is None.

        Returns:
            Union[PLCSoftware, None]: The software of the device item.
        """
        if self.value is None:
            raise tia_e.InvalidDeviceItem("Value is None")

        software_container: Optional[hwf.SoftwareContainer]
        software_container = self.value.GetService[hwf.SoftwareContainer]()  # type: ignore

        if software_container is None:
            return None

        software_type = software_container.Software.ToString()

        if software_type == "Siemens.Engineering.SW.PlcSoftware":
            return PLCSoftware(self)

        return None

    def get_items(self) -> Optional[DeviceItems]:
        """Gets the device items of the device item.

        Raises:
            tia_e.InvalidDeviceItem: If the value is None.

        Returns:
            Optional[DeviceItems]: The device items of the device item.
        """
        if self.value is None:
            raise tia_e.InvalidDeviceItem("Value is None")

        if self.value.DeviceItems.Count > 0:
            return DeviceItems(self)

        return None

    def set_name(self, name: str) -> None:
        if self.value is None:
            raise tia_e.InvalidDeviceItem("Value is None")

        self.value.Name = name
        self.name = name

        return None


class DeviceItems(Composition[DeviceItem]):
    """Represents the device items of a device. This class contains more specific
        functions for PLC and HMI objects. This class is a composition of device items.

    Attributes:
        parent (Union[Device, DeviceItem]): The parent device or device item.
            This is a single device or a device item that contains device items.
        value (Optional[hw.DeviceItemComposition]): The value of the device items
            and the connection to the C# library. So functions of the Openness
            API can be used on this variable.
    """

    def __init__(self, parent: Union[Device, DeviceItem]) -> None:
        """Initializes the device items.

        Parameters:
            parent (Union[Device, DeviceItem]): The parent device or device item.
                This is a single device or a device item that contains device items.

        Raises:
            tia_e.InvalidDevice: If the parent value is None.
        """
        self.parent = parent
        self.__value = None

        if self.parent.value is None:
            raise tia_e.InvalidDevice("Device value is None")

        value = self.parent.value.DeviceItems

        self.value = value

    @property
    def value(self) -> Optional[hw.DeviceItemComposition]:
        return self.__value

    @value.setter
    def value(self, value: Optional[hw.DeviceItemComposition]) -> None:
        self.__value = value

    def find(self, name: str) -> DeviceItem:
        """Finds a device item by name.

        Parameters:
            name (str): The name of the device item.

        Raises:
            tia_e.InvalidDeviceItemComposition: If the value is None.

        Returns:
            DeviceItem: The device item.
        """
        if self.value is None:
            raise tia_e.InvalidDeviceItemComposition("Value is None")

        return DeviceItem(self, name)

    def __iter__(self) -> Iterator[DeviceItem]:
        """Iterates over the device items.

        Raises:
            tia_e.InvalidDeviceItemComposition: If the value is None.

        Yields:
            Iterator[DeviceItem]: The device item.
        """
        if self.value is None:
            raise tia_e.InvalidDeviceItemComposition("Value is None")

        device_item: hw.DeviceItem
        for device_item in self.value:
            yield DeviceItem(self, device_item.Name)

    def get_device_items(self) -> list[DeviceItem]:
        """Gets a list of the device items.

        Returns:
            list[DeviceItem]: The device items.
        """
        device_items: list[DeviceItem] = []
        for device_item in self:
            device_items.append(device_item)

        return device_items


class PLCSoftware(TiaObject):
    """Represents the PLC software of a device item. This class contains
        more specific functions for PLC objects and its software.

    Attributes:
        parent (DeviceItem): The parent device item. This is a single device item that contains PLC software.
        value (Optional[sw.PlcSoftware]): The value of the PLC software
            and the connection to the C# library. So functions of the Openness API can be used on this variable.
    """

    def __init__(self, parent: DeviceItem) -> None:
        """Initializes the PLC software.

        Parameters:
            parent (DeviceItem): The parent device item.
                This is a single device item that contains PLC software.

        Raises:
            tia_e.InvalidDeviceItem: If the parent value is None or the software container
                is None or the software is None.
            tia_e.InvalidSoftwareType: If the software is not PLC software.
        """
        self.parent = parent
        self.__value = None

        if self.parent.value is None:
            raise tia_e.InvalidDeviceItem("Value is None")

        software_container: Optional[hwf.SoftwareContainer]
        software_container = self.parent.value.GetService[hwf.SoftwareContainer]()  # type: ignore

        if software_container is None:
            raise tia_e.InvalidDeviceItem("Software container is None")

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
        """Gets the system block groups of the PLC software.

        Raises:
            tia_e.InvalidSoftware: If the value is None.

        Returns:
            PLCSystemBlockGroups: The system block groups this is a composition of system block groups.
        """
        if self.value is None:
            raise tia_e.InvalidSoftware("Value is None")

        return PLCSystemBlockGroups(self)

    def get_user_block_groups(self) -> PLCUserBlockGroups:
        """Gets the user block groups of the PLC software. This is a composition of user block groups.
             To this group new user block groups can be added.

        Raises:
            tia_e.InvalidSoftware: If the value is None.

        Returns:
            PLCUserBlockGroups: The user block groups. This is a composition of user block groups.
        """
        if self.value is None:
            raise tia_e.InvalidSoftware("Value is None")

        return PLCUserBlockGroups(self)

    def get_blocks(self) -> PLCBlocks:
        """Gets the blocks of the PLC software. This is a composition of blocks. This is of the main block group.

        Raises:
            tia_e.InvalidSoftware: If the value is None.

        Returns:
            PLCBlocks: The blocks of the PLC software. This is a composition of blocks.
        """
        if self.value is None:
            raise tia_e.InvalidSoftware("Value is None")

        return PLCBlocks(self)

    def get_all_blocks(self, recursive: bool = False) -> list[PLCBlock]:
        """Gets all blocks of the PLC software. This includes all blocks of the main block group
            and all blocks of the system block groups and user block groups.

        Parameters:
            recursive (bool, optional): If True, all blocks of the system block groups
                and user block groups will be included. Defaults to False.

        Returns:
            list[PLCBlock]: The blocks of the PLC software.
        """
        if not recursive:
            return list(self.get_blocks())

        blocks = list(self.get_blocks())
        for system_group in self.get_system_block_groups():
            blocks.extend(system_group.get_all_blocks(True))
        for user_group in self.get_user_block_groups():
            blocks.extend(user_group.get_all_blocks(True))

        return blocks


class PLCSystemBlockGroup(CompositionItem):
    """Represents a system block group of a PLC software. This is a composition of system block groups.

    Attributes:
        parent (PLCSystemBlockGroups): The parent system block groups. This is a composition of system block groups.
        name (str): The name of the system block group.
        value (Optional[swb.PlcSystemBlockGroup]): The value of the system block group
            and the connection to the C# library. So functions of the Openness API can be used on this variable.
    """

    def __init__(self, parent: PLCSystemBlockGroups, name: str) -> None:
        """Initializes the system block group.

        Parameters:
            parent (PLCSystemBlockGroups): The parent system block groups. This is a composition of system block groups.
            name (str): The name of the system block group.

        Raises:
            tia_e.InvalidSystemBlockGroupComposition: If the parent value is None.
        """
        self.parent = parent
        self.name = name
        self.__value = None

        if self.parent.value is None:
            raise tia_e.InvalidSystemBlockGroupComposition("Parent value is None")

        value = self.parent.value.Find(name)

        self.value = value

    @property
    def value(self) -> Optional[swb.PlcSystemBlockGroup]:
        return self.__value

    @value.setter
    def value(self, value: Optional[swb.PlcSystemBlockGroup]) -> None:
        self.__value = value

    def get_groups(self) -> PLCSystemBlockGroups:
        """Gets the system block groups of the system block group. This is a composition of system block groups.

        Raises:
            tia_e.InvalidSystemBlockGroup: If the value is None.

        Returns:
            PLCSystemBlockGroups: The system block groups of the system block group.
                This is a composition of system block groups.
        """
        if self.value is None:
            raise tia_e.InvalidSystemBlockGroup("Value is None")

        return PLCSystemBlockGroups(self)

    def get_blocks(self) -> PLCBlocks:
        """Gets the blocks of the system block group. This is a composition of blocks.

        Raises:
            tia_e.InvalidSystemBlockGroup: If the value is None.

        Returns:
            PLCBlocks: The blocks of the system block group. This is a composition of blocks.
        """
        if self.value is None:
            raise tia_e.InvalidSystemBlockGroup("Value is None")

        return PLCBlocks(self)

    def get_all_blocks(self, recursive: bool = False) -> list[PLCBlock]:
        """Gets all blocks of the system block group. This includes all blocks of the
            system block group and all blocks of the system block groups.

        Parameters:
            recursive (bool, optional): If True, all blocks of the system block
                groups will be included. Defaults to False.

        Returns:
            list[PLCBlock]: The blocks of the system block group.
        """
        if not recursive:
            return list(self.get_blocks())

        blocks = list(self.get_blocks())
        for group in self.get_groups():
            blocks.extend(group.get_all_blocks(True))

        return blocks


class PLCSystemBlockGroups(Composition[PLCSystemBlockGroup]):
    """Represents a composition of system block groups. This is a composition of system block groups.

    Attributes:
        parent (Union[PLCSoftware, PLCSystemBlockGroup]): The parent of the system block groups.
            This can be a PLC software or a system block group.
        value (Optional[swb.PlcSystemBlockGroupComposition]): The value of the system
            block groups and the connection to the C# library. So functions of the Openness
            API can be used on this variable.
    """

    def __init__(self, parent: Union[PLCSoftware, PLCSystemBlockGroup]) -> None:
        """Initializes the system block groups.

        Parameters:
            parent (Union[PLCSoftware, PLCSystemBlockGroup]): The parent of the system block groups.
                 This can be a PLC software or a system block group.

        Raises:
            tia_e.InvalidSoftware: If the parent value is None.
        """
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
        """Finds a system block group by name.

        Parameters:
            name (str): The name of the system block group.

        Raises:
            tia_e.InvalidSystemBlockGroupComposition: If the value is None.

        Returns:
            PLCSystemBlockGroup: The system block group with the given name.
        """
        if self.value is None:
            raise tia_e.InvalidSystemBlockGroupComposition("Value is None")

        return PLCSystemBlockGroup(self, name)

    def __iter__(self) -> Iterator[PLCSystemBlockGroup]:
        """Iterates over the system block groups.

        Raises:
            tia_e.InvalidSystemBlockGroupComposition: If the value is None.

        Yields:
            Iterator[PLCSystemBlockGroup]: The system block groups.
        """
        if self.value is None:
            raise tia_e.InvalidSystemBlockGroupComposition("Value is None")

        system_block_group: swb.PlcSystemBlockGroup
        for system_block_group in self.value:
            yield PLCSystemBlockGroup(self, system_block_group.Name)

    def create(self, name: str) -> PLCSystemBlockGroup:
        """Creates a system block group.

        Parameters:
            name (str): The name of the system block group.

        Raises:
            tia_e.InvalidSystemBlockGroupComposition: If the value is None.

        Returns:
            PLCSystemBlockGroup: The created system block group.
        """
        if self.value is None:
            raise tia_e.InvalidSystemBlockGroupComposition("Value is None")

        self.value.Create(name)

        return PLCSystemBlockGroup(self, name)


class PLCUserBlockGroup(CompositionItem):
    """Represents a user block group. This is a composition item of user block groups.

    Attributes:
        parent (PLCUserBlockGroups): The parent of the user block group. This is a composition of user block groups.
        name (str): The name of the user block group.
        value (Optional[swb.PlcBlockUserGroup]): The value of the user block group
            and the connection to the C# library. So functions of the Openness
            API can be used on this variable.
    """

    def __init__(self, parent: PLCUserBlockGroups, name: str) -> None:
        """Initializes the user block group.

        Parameters:
            parent (PLCUserBlockGroups): The parent of the user block group. This is a composition of user block groups.
            name (str): The name of the user block group.

        Raises:
            tia_e.InvalidUserBlockGroupComposition: If the parent value is None.
        """
        self.parent = parent
        self.name = name
        self.__value = None

        if self.parent.value is None:
            raise tia_e.InvalidUserBlockGroupComposition("Parent value is None")

        value = self.parent.value.Find(name)

        self.value = value

    @property
    def value(self) -> Optional[swb.PlcBlockUserGroup]:
        return self.__value

    @value.setter
    def value(self, value: Optional[swb.PlcBlockUserGroup]) -> None:
        self.__value = value

    def get_groups(self) -> PLCUserBlockGroups:
        """Gets the user block groups of the user block group.

        Raises:
            tia_e.InvalidUserBlockGroup: If the value is None.

        Returns:
            PLCUserBlockGroups: The user block groups of the user block group.
        """
        if self.value is None:
            raise tia_e.InvalidUserBlockGroup("Value is None")

        return PLCUserBlockGroups(self)

    def get_blocks(self) -> PLCBlocks:
        """Gets the blocks of the user block group.

        Raises:
            tia_e.InvalidUserBlockGroup: If the value is None.

        Returns:
            PLCBlocks: The blocks of the user block group.
        """
        if self.value is None:
            raise tia_e.InvalidUserBlockGroup("Value is None")

        return PLCBlocks(self)

    def get_all_blocks(self, recursive: bool = False) -> list[PLCBlock]:
        """Gets all blocks of the user block group.

        Parameters:
            recursive (bool, optional): If the blocks of the subgroups should be included. Defaults to False.

        Returns:
            list[PLCBlock]: The blocks of the user block group.
        """
        if not recursive:
            return list(self.get_blocks())

        blocks = list(self.get_blocks())
        for group in self.get_groups():
            blocks.extend(group.get_all_blocks(True))

        return blocks


class PLCUserBlockGroups(Composition[PLCUserBlockGroup]):
    """Represents a composition of user block groups. This is a composition of user block groups.

    Attributes:
        parent (Union[PLCSoftware, PLCUserBlockGroup]): The parent of the user block groups.
            This is a software or a user block group.
        value (Optional[swb.PlcBlockUserGroupComposition]): The value of the user block groups
            and the connection to the C# library. So functions of the Openness
            API can be used on this variable.
    """

    def __init__(self, parent: Union[PLCSoftware, PLCUserBlockGroup]) -> None:
        """Initializes the user block groups.

        Parameters:
            parent (Union[PLCSoftware, PLCUserBlockGroup]): The parent of the user block groups.
                This is a software or a user block group.

        Raises:
            tia_e.InvalidSoftware: If the parent value is None.
        """
        self.parent = parent
        self.__value: Optional[swb.PlcBlockUserGroupComposition] = None

        value = None

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
        """Finds a user block group by name.

        Parameters:
            name (str): The name of the user block group.

        Raises:
            tia_e.InvalidUserBlockGroupComposition: If the value is None.

        Returns:
            PLCUserBlockGroup: The user block group.
        """
        if self.value is None:
            raise tia_e.InvalidUserBlockGroupComposition("Value is None")

        return PLCUserBlockGroup(self, name)

    def __iter__(self) -> Iterator[PLCUserBlockGroup]:
        """Iterates over the user block groups.

        Raises:
            tia_e.InvalidUserBlockGroupComposition: If the value is None.

        Yields:
            Iterator[PLCUserBlockGroup]: The user block groups.
        """
        if self.value is None:
            raise tia_e.InvalidUserBlockGroupComposition("Value is None")

        user_block_group: swb.PlcBlockUserGroup
        for user_block_group in self.value:
            yield PLCUserBlockGroup(self, user_block_group.Name)

    def create(self, name: str) -> PLCUserBlockGroup:
        """Creates a user block group.

        Parameters:
            name (str): The name of the user block group.

        Raises:
            tia_e.InvalidUserBlockGroupComposition: If the value is None.

        Returns:
            PLCUserBlockGroup: The user block group.
        """
        if self.value is None:
            raise tia_e.InvalidUserBlockGroupComposition("Value is None")

        self.value.Create(name)

        return PLCUserBlockGroup(self, name)


class PLCBlock(CompositionItem):
    """Represents a block. This is a composition item of blocks.

    Attributes:
        parent (PLCBlocks): The parent of the block. This is a blocks.
        name (str): The name of the block.
        value (Optional[swb.PlcBlock]): The value of the block and the connection
            to the C# library. So functions of the Openness API can be used on this variable.
    """

    def __init__(self, parent: PLCBlocks, name: str) -> None:
        """Initializes the block.

        Parameters:
            parent (PLCBlocks): The parent of the block. This is a blocks.
            name (str): The name of the block.

        Raises:
            tia_e.InvalidBlockComposition: If the parent value is None.
        """
        self.parent = parent
        self.name = name
        self.__value = None

        if self.parent.value is None:
            raise tia_e.InvalidBlockComposition("Parent value is None")

        value = self.parent.value.Find(name)

        self.value = value

    @property
    def value(self) -> Optional[swb.PlcBlock]:
        return self.__value

    @value.setter
    def value(self, value: Optional[swb.PlcBlock]) -> None:
        self.__value = value

    def export(self) -> str:
        """This function exports the block to a file. The file is stored in
            the exported_blocks folder in the data folder.

        Raises:
            tia_e.InvalidBlock: If the value is None or when the block is inconsistent.
                This means that the block is not compiled and therefore not exportable.

        Returns:
            str: The path to the exported file.
        """
        if self.value is None:
            raise tia_e.InvalidBlock("Value is None")

        if not self.value.IsConsistent:
            raise tia_e.InvalidBlock("Block is inconsistent")

        new_file = os.path.join(cfg.DATA_PATH, "exported_blocks", f"{self.name}.xml")

        if not os.path.exists(os.path.dirname(new_file)):
            os.makedirs(os.path.dirname(new_file))

        file_info = FileInfo(new_file)

        self.value.Export(file_info, tia.ExportOptions(0))  # type: ignore

        return new_file

    def update_software(self) -> None:
        """This function updates the software with the block.

        Raises:
            tia_e.InvalidBlock: If the value is None.
        """
        if self.value is None:
            raise tia_e.InvalidBlock("Value is None")

        self.value.GetService[comp.ICompilable]().Compile()  # type: ignore

    def get_type(self) -> str:
        """This function returns the type of the block.

        Raises:
            tia_e.InvalidBlock: If the value is None.

        Returns:
            str: The type of the block.
        """
        if self.value is None:
            raise tia_e.InvalidBlock("Value is None")

        temp = self.value.GetType().Name

        return temp.split(".")[-1]

    def assign_prodiag(self, prodiag: str):
        """This function assigns a prodiag to the block.

        Parameters:
            prodiag (str): The prodiag to assign.

        Raises:
            tia_e.InvalidBlock: If the value is None.
        """
        if self.value is None:
            raise tia_e.InvalidBlock("Value is None")

        self.value.SetAttribute("AssignedProDiagFB", prodiag)


class PLCBlocks(Composition[PLCBlock]):
    """Represents a blocks. This is a composition of blocks.

    Attributes:
        parent (Union[PLCSoftware, PLCSystemBlockGroup, PLCUserBlockGroup]): The parent of the blocks.
            This is a software, a system block group or a user block group.
        value (Optional[swb.PlcBlockComposition]): The value of the blocks
            and the connection to the C# library. So functions of the Openness
                API can be used on this variable.
    """

    def __init__(
        self, parent: Union[PLCSoftware, PLCSystemBlockGroup, PLCUserBlockGroup]
    ) -> None:
        """Initializes the blocks.

        Parameters:
            parent (Union[PLCSoftware, PLCSystemBlockGroup, PLCUserBlockGroup]): The parent of the blocks.
                This is a software, a system block group or a user block group.

        Raises:
            tia_e.InvalidSoftware: The software value is None.
            tia_e.InvalidSystemBlockGroup: The system block group value is None.
            tia_e.InvalidUserBlockGroup: The user block group value is None.
        """
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
        """Finds a block by name.

        Parameters:
            name (str): The name of the block.

        Raises:
            tia_e.InvalidBlockComposition: If the value is None.

        Returns:
            PLCBlock: The block.
        """
        if self.value is None:
            raise tia_e.InvalidBlockComposition("Value is None")

        return PLCBlock(self, name)

    def __iter__(self) -> Iterator[PLCBlock]:
        """Iterates over all blocks.

        Raises:
            tia_e.InvalidBlockComposition: If the value is None.

        Yields:
            Iterator[PLCBlock]: The block.
        """
        if self.value is None:
            raise tia_e.InvalidBlockComposition("Value is None")

        block: swb.PlcBlock
        for block in self.value:
            yield PLCBlock(self, block.Name)

    def create(
        self, path: str, name: str, labels: Optional[dict[str, str]] = None
    ) -> PLCBlock:
        """Creates a block from a file.

        Parameters:
            path (str): The path to the file. The file must be an valid XML file.
            name (str): The name of the block.

        Raises:
            tia_e.InvalidBlockComposition: If the value is None.
            tia_e.InvalidPath: If the path is invalid.

        Returns:
            PLCBlock: The block.
        """
        if labels is None:
            labels = {}

        if self.value is None:
            raise tia_e.InvalidBlockComposition("Value is None")

        if not os.path.isfile(path):
            raise tia_e.InvalidPath(f"Invalid path: {path}")

        new_file = os.path.join(cfg.DATA_PATH, "temp", os.path.basename(path))

        if not os.path.exists(os.path.dirname(new_file)):
            os.makedirs(os.path.dirname(new_file))

        shutil.copyfile(path, new_file)

        with open(new_file, "r", encoding="utf-8") as file:
            data = file.read()

        for key, value in labels.items():
            data = data.replace(key, value)

        data = data.replace("__NAME__", name)

        match = re.match(r"__\w+__", data)

        if match:
            for group in match.groups():
                print(f"Warning: {group} is not replaced in {new_file}!")

        with open(new_file, "w", encoding="utf-8") as file:
            file.write(data)

        file_info = FileInfo(new_file)

        self.value.Import(file_info, tia.ImportOptions.Override)

        os.remove(new_file)

        return PLCBlock(self, name)

    def create_instance_database(self, name: str, fb_name: str) -> PLCBlock:
        """Creates an instance database.

        Parameters:
            name (str): The name of the instance database.
            fb_name (str): The name of the function block which is used to link to the instance database.

        Raises:
            tia_e.InvalidBlockComposition: If the value is None.

        Returns:
            PLCBlock: The block.
        """
        if self.value is None:
            raise tia_e.InvalidBlockComposition("Value is None")

        self.value.CreateInstanceDB(name, True, 1, fb_name)

        return PLCBlock(self, name)

    def create_prodiag_block(self, name: str) -> PLCBlock:
        """Creates a ProDiag block. This is a function block with an instance database.
            The instance database is created automatically. The instance database is created
            in the IDB group which is created automatically if it does not exist. This group
            is placed in the same group as the function block.

        Parameters:
            name (str): The name of the function block.

        Raises:
            tia_e.InvalidBlockComposition: If the value is None.

        Returns:
            PLCBlock: The block.
        """
        if self.value is None:
            raise tia_e.InvalidBlockComposition("Value is None")

        self.value.CreateFB(name, True, 1, swb.ProgrammingLanguage.ProDiag)

        idb_name = name.replace("FB", "IDB")

        if isinstance(self.parent, PLCSoftware):
            groups = self.parent.get_user_block_groups()
        else:
            groups = self.parent.get_groups()

        if not groups.find("IDB").value:
            groups.create("IDB")

        groups.find("IDB").get_blocks().create_instance_database(idb_name, name)

        return PLCBlock(self, name)


class GlobalLibrary(CompositionItem):
    """Represents a global library.

    Attributes:
        parent (GlobalLibraries): The parent.
        name (str): The name of the global library.
        value (Optional[lib.GlobalLibrary]): The global library.
    """

    def __init__(self, parent: GlobalLibraries, name: str):
        """Initializes the global library.

        Args:
            parent (GlobalLibraries): The parent.
            name (str): The name of the global library.

        Raises:
            tia_e.InvalidGlobalLibraryComposition: If the parent value is None.
        """
        self.parent = parent
        self.name = name
        self.__value = None

        if self.parent.value is None:
            raise tia_e.InvalidGlobalLibraryComposition("Parent value is None")

        self.value = None

        global_library: lib.GlobalLibrary
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
        """Returns the type folder.

        Raises:
            tia_e.InvalidGlobalLibrary: If the value is None.

        Returns:
            LibraryTypeFolder: The type folder.
        """
        if self.value is None:
            raise tia_e.InvalidGlobalLibrary("Value is None")

        return LibraryTypeFolder(self)

    @type_folder.setter
    def type_folder(self, value: LibraryTypeFolder) -> None:
        raise NotImplementedError("Cannot set type folder")

    @property
    def master_copy_folder(self) -> MasterCopyFolder:
        """Returns the master copy folder.

        Raises:
            tia_e.InvalidGlobalLibrary: If the value is None.

        Returns:
            MasterCopyFolder: The master copy folder.
        """
        if self.value is None:
            raise tia_e.InvalidGlobalLibrary("Value is None")

        return MasterCopyFolder(self)

    @master_copy_folder.setter
    def master_copy_folder(self, value: MasterCopyFolder) -> None:
        raise NotImplementedError("Cannot set master copy folder")


class GlobalLibraries(Composition[GlobalLibrary]):
    """A composition of global libraries.

    Attributes:
        parent (Client): The parent.
        value (Optional[lib.GlobalLibraryComposition]): The global library composition.
    """

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
        """Iterates over the global libraries.

        Raises:
            tia_e.InvalidGlobalLibraryComposition: If the value is None.

        Yields:
            Iterator[GlobalLibrary]: The global library.
        """
        if self.value is None:
            raise tia_e.InvalidGlobalLibraryComposition("Value is None")

        global_library: lib.GlobalLibrary
        for global_library in self.value:
            yield GlobalLibrary(self, global_library.Name)


class LibraryTypeFolder(TiaObject):
    """Represents a library type folder.

    Attributes:
        parent (GlobalLibrary): The parent.
        value (Optional[lib_type.LibraryTypeFolder]): The library type folder.
        folders (LibraryTypeUserFolders): The library type user folders.
        types (LibraryTypes): The library types.
    """

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
        """Returns the library type user folders.

        Raises:
            tia_e.InvalidTypeFolder: If the value is None.

        Returns:
            LibraryTypeUserFolders: The library type user folders.
        """
        if self.value is None:
            raise tia_e.InvalidTypeFolder("Value is None")

        return LibraryTypeUserFolders(self)

    @folders.setter
    def folders(self, value: LibraryTypeUserFolders) -> None:
        raise NotImplementedError("Cannot set type user folders")

    @property
    def types(self) -> LibraryTypes:
        """Returns the library types.

        Raises:
            tia_e.InvalidTypeFolder: If the value is None.

        Returns:
            LibraryTypes: The library types.
        """
        if self.value is None:
            raise tia_e.InvalidTypeFolder("Value is None")

        return LibraryTypes(self)

    @types.setter
    def types(self, value: LibraryTypes) -> None:
        raise NotImplementedError("Cannot set types")


class LibraryTypeUserFolder(CompositionItem):
    """Represents a library type user folder.

    Attributes:
        parent (LibraryTypeUserFolders): The parent.
        name (str): The name of the library type user folder.
        value (Optional[lib_type.LibraryTypeUserFolder]): The library type user folder.
        folders (LibraryTypeUserFolders): The library type user folders.
        types (LibraryTypes): The library types.

    """

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
        """Returns the library type user folders.

        Raises:
            tia_e.InvalidTypeFolder: If the value is None.

        Returns:
            LibraryTypeUserFolders: The library type user folders.
        """
        if self.value is None:
            raise tia_e.InvalidTypeFolder("Value is None")

        return LibraryTypeUserFolders(self)

    @folders.setter
    def folders(self, value: LibraryTypeUserFolders) -> None:
        raise NotImplementedError("Cannot set type user folders")

    @property
    def types(self) -> LibraryTypes:
        """Returns the library types.

        Raises:
            tia_e.InvalidTypeFolder: If the value is None.

        Returns:
            LibraryTypes: The library types.
        """
        if self.value is None:
            raise tia_e.InvalidTypeFolder("Value is None")

        return LibraryTypes(self)

    @types.setter
    def types(self, value: LibraryTypes) -> None:
        raise NotImplementedError("Cannot set types")


class LibraryTypeUserFolders(Composition[LibraryTypeUserFolder]):
    """A composition of library type user folders.

    Attributes:
        parent (Union[LibraryTypeFolder, LibraryTypeUserFolder]): The parent.
        value (Optional[lib_type.LibraryTypeUserFolderComposition]): The library type user folder composition.
    """

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

        folder: lib_type.LibraryTypeUserFolder
        for folder in self.value:
            yield LibraryTypeUserFolder(self, folder.Name)


class LibraryType(CompositionItem):  # pylint: disable=too-few-public-methods
    """Represents a library type.

    Attributes:
        parent (LibraryTypes): The parent.
        name (str): The name of the library type.
        value (Optional[lib_type.LibraryType]): The library type.
    """

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
    """A composition of library types.

    Attributes:
        parent (Union[LibraryTypeFolder, LibraryTypeUserFolder]): The parent.
        value (Optional[lib_type.LibraryTypeComposition]): The library type composition.
    """

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

        library_type: lib_type.LibraryType
        for library_type in self.value:
            yield LibraryType(self, library_type.Name)


class MasterCopyFolder(TiaObject):
    """Represents a master copy folder.

    Attributes:
        parent (Union[MasterCopyUserFolder, MasterCopyUserFolders]): The parent.
        name (str): The name of the master copy folder.
        value (Optional[lib_mc.MasterCopyFolder]): The master copy folder.
    """

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
        """Returns the master copy user folders.

        Raises:
            tia_e.InvalidTypeFolder: If the value is None.

        Returns:
            MasterCopyUserFolders: The master copy user folders.
        """
        if self.value is None:
            raise tia_e.InvalidTypeFolder("Value is None")

        return MasterCopyUserFolders(self)

    @folders.setter
    def folders(self, value: MasterCopyUserFolders) -> None:
        raise NotImplementedError("Cannot set type user folders")

    @property
    def master_copies(self) -> MasterCopies:
        """Returns the master copies.

        Raises:
            tia_e.InvalidMasterCopyFolder: If the value is None.

        Returns:
            MasterCopies: The master copies.
        """
        if self.value is None:
            raise tia_e.InvalidMasterCopyFolder("Value is None")

        return MasterCopies(self)

    @master_copies.setter
    def master_copies(self, value: MasterCopies) -> None:
        raise NotImplementedError("Cannot set master copies")


class MasterCopyUserFolder(CompositionItem):
    """Represents a master copy user folder.

    Attributes:
        parent (MasterCopyUserFolders): The parent.
        name (str): The name of the master copy user folder.
        value (Optional[lib_mc.MasterCopyUserFolder]): The master copy user folder.
    """

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
        """Returns the master copy user folders.

        Raises:
            tia_e.InvalidTypeFolder: If the value is None.

        Returns:
            MasterCopyUserFolders: The master copy user folders.
        """
        if self.value is None:
            raise tia_e.InvalidTypeFolder("Value is None")

        return MasterCopyUserFolders(self)

    @folders.setter
    def folders(self, value: MasterCopyUserFolders) -> None:
        raise NotImplementedError("Cannot set type user folders")

    @property
    def master_copies(self) -> MasterCopies:
        """Returns the master copies.

        Raises:
            tia_e.InvalidMasterCopyFolder: If the value is None.

        Returns:
            MasterCopies: The master copies.
        """
        if self.value is None:
            raise tia_e.InvalidMasterCopyFolder("Value is None")

        return MasterCopies(self)

    @master_copies.setter
    def master_copies(self, value: MasterCopies) -> None:
        raise NotImplementedError("Cannot set master copies")


class MasterCopyUserFolders(Composition[MasterCopyUserFolder]):
    """Represents a master copy user folder composition.

    Attributes:
        parent (Union[MasterCopyFolder, MasterCopyUserFolder]): The parent.
        value (Optional[lib_mc.MasterCopyUserFolderComposition]): The master copy user folder composition.
    """

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

        folder: lib_mc.MasterCopyUserFolder
        for folder in self.value:
            yield MasterCopyUserFolder(self, folder.Name)


class MasterCopy(CompositionItem):  # pylint: disable=too-few-public-methods
    """Represents a master copy.

    Attributes:
        parent (MasterCopies): The parent.
        name (str): The name of the master copy.
    """

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
    """Represents a master copy composition.

    Attributes:
        parent (Union[MasterCopyFolder, MasterCopyUserFolder]): The parent.
        value (Optional[lib_mc.MasterCopyComposition]): The master copy composition.
    """

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

        master_copy: lib_mc.MasterCopy
        for master_copy in self.value:
            yield MasterCopy(self, master_copy.Name)


class Client:
    """Client for TIA Portal. This is the main class for the TIA Portal API.
        This class can create a new connection via Openness API to
        connect to a TIA Portal instance.

    Attributes:
        session (Optional[tia.TiaPortal]): The TIA Portal session.
        project (Optional[Project]): The currently opened project.
    """

    def __init__(self) -> None:
        """Constructor for the Client class. This class can create a new connection
        via Openness API to connect to a TIA Portal instance."""
        self.session: Optional[tia.TiaPortal] = tia.TiaPortal(tia.TiaPortalMode.WithoutUserInterface)  # type: ignore
        self.project: Optional[Project] = None

    # ==================================================================================================================
    # GUI actions
    # ==================================================================================================================
    def open_gui(self) -> None:
        """Opens the TIA Portal GUI. If a project is opened, it will be opened in the GUI as well.

        Raises:
            tia_e.TIAInvalidSession: If the session is None.
        """
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
            self.session = tia.TiaPortal(tia.TiaPortalMode.WithUserInterface)  # type: ignore

            if project_open and self.project:
                self.project.open()

    def close_gui(self) -> None:
        """Closes the TIA Portal GUI. If a project is opened, it will be closed as well and reopened in the background.

        Raises:
            tia_e.TIAInvalidSession: If the session is None.
        """
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
            self.session = tia.TiaPortal(tia.TiaPortalMode.WithoutUserInterface)  # type: ignore

            if project_open and self.project:
                self.project.open()

    # ==================================================================================================================
    # QUITTING AND CLOSING
    # ==================================================================================================================
    def close(self) -> None:
        """Closes the TIA Portal session and kills the process. If a project is opened, it will be closed as well."""
        if self.session is None:
            return

        if self.project and self.project.is_open():
            self.project.close()

        process = self.session.GetCurrentProcess()
        self.session.Dispose()
        self.session = None
        Process.GetProcessById(process.Id).Kill()

    def quit(self) -> None:
        """This is an alias for the close method."""
        self.close()

    def __del__(self) -> None:
        """Destructor for the Client class. This method will close the TIA Portal
        session and kill the process. If a project is opened, it will be closed as well."""
        if self.session is None:
            return

        try:
            if self.project and self.project.is_open():
                self.project.force_close()

            process = self.session.GetCurrentProcess()
            self.session.Dispose()
            self.session = None
            Process.GetProcessById(process.Id).Kill()
        except Exception:  # pylint: disable=broad-except
            pass

    # ==================================================================================================================
    # PROJECTS
    # ==================================================================================================================

    def open_project(
        self, path: str, name: str, version: Optional[TiaVersion] = None
    ) -> Project:
        """Opens a project in the TIA Portal.

        Parameters:
            path (str): The path to the Automation folder where all subfolders are located.
            name (str): The name of the project.
            version (Optional[TIAVersion], optional): The version of the project. Defaults to None.
                If None, the version of the session will be used.

        Raises:
            tia_e.TIAInvalidSession: If the session is None.

        Returns:
            Project: The opened project.
        """
        if self.session is None:
            raise tia_e.TIAInvalidSession("Session is None")

        if self.project is not None and self.project.is_open():
            self.project.close()

        self.project = Project(self, path, name, version)
        self.project.open()

        return self.project

    def create_project(
        self, path: str, name: str, version: Optional[TiaVersion] = None
    ) -> Project:
        """Creates a new project in the TIA Portal.

        Parameters:
            path (str): The path to the Automation folder where all subfolders are located.
            name (str): The name of the project.
            version (Optional[TIAVersion], optional): The version of the project. Defaults to None.`
                If None, the version of the session will be used.

        Raises:
            tia_e.TIAInvalidSession: If the session is None.

        Returns:
            Project: The created project.
        """
        if self.session is None:
            raise tia_e.TIAInvalidSession("Session is None")

        if self.project is not None and self.project.is_open():
            self.project.close()

        self.project = Project(self, path, name, version)
        self.project.create(True)

        return self.project

    def create_projects(
        self, path: str, names: list[str], version: Optional[TiaVersion] = None
    ) -> list[Project]:
        """Creates multiple projects in the TIA Portal.

        Parameters:
            path (str): The path to the Automation folder where all subfolders are located.
            names (list[str]): A list of project names.
            version (Optional[TIAVersion], optional): The version of the project. Defaults to None.
                If None, the version of the session will be used.

        Raises:
            tia_e.TIAInvalidSession: If the session is None.

        Returns:
            list[Project]: A list of created projects.
        """
        if self.session is None:
            raise tia_e.TIAInvalidSession("Session is None")

        if self.project is not None:
            self.project.close()

        projects: list[Project] = []
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
    """A class for handling projects in the TIA Portal. This class is not intended
    to be used directly. Use the Client class instead.

    Attributes:
        client (Client): The client object.
        path (str): The path to the Automation folder where all subfolders are located.
        name (str): The name of the project.
        version (Optional[TIAVersion]): The version of the project. Defaults to None.
            If None, the version of the session will be used.
        value (Optional[tia.Project]): The project object.
        devices (Devices): A composition of Devices that are part of the project.
    """

    def __init__(
        self, client: Client, path: str, name: str, version: Optional[TiaVersion] = None
    ):
        """Constructor for the Project class.

        Parameters:
            client (Client): The client object that created this project. This is used to access the session object.
            path (str): The path to the Automation folder where all subfolders are located.
            name (str): The name of the project.
            version (Optional[TIAVersion], optional): The version of the project. Defaults to None.
                If None, the version of the session will be used.
        """
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
        """Opens the project in the TIA Portal.

        Raises:
            tia_e.TIAInvalidSession: If the session is None.
            tia_e.TIAProjectNotFound: If the project is not found or the path is not a file and the name is None.
        """
        if self.client.session is None:
            raise tia_e.TIAInvalidSession("Session is None")

        if self.value is not None:
            print(
                f"There is already a Project open, closing {self.value.Name} before opening {self.name}"
            )
            self.close()

        if isinstance(self.path, FileInfo):
            file_info = self.path
            self.name = file_info.Name.split(".")[0]
        else:
            file_name = (
                self.name
                if self.name.endswith(f".ap{self.version.value}")
                else f"{self.name}.ap{self.version.value}"
            )
            file_path = os.path.join(self.path, self.name, file_name)
            self.name = self.name

            if not os.path.exists(file_path):
                raise tia_e.TIAProjectNotFound(f"File {file_path} does not exist")

            file_info = FileInfo(file_path)

        self.value = self.client.session.Projects.Open(file_info)

        self.client.project = self

    def close(self) -> None:
        """Closes the project in the TIA Portal."""
        if self.value is None:
            return
        self.save()
        self.value.Close()
        self.value = None

    def force_close(self) -> None:
        """Forces the project to close without saving in the TIA Portal.
        This is useful if the project is not responding."""
        if self.value is None:
            return
        self.value.Close()
        self.value = None

    def create(self, open_existing: bool = False) -> None:
        """Creates a new project in the TIA Portal.

        Parameters:
            open_existing (bool, optional): If True, the project will be opened if it already exists. Defaults to False.

        Raises:
            tia_e.TIAInvalidSession: If the session is None or the old session is None.
            tia_e.TIAProjectAlreadyExists: If the project already exists and open_existing is False.
        """
        if not open_existing:
            new_session = tia.TiaPortal(tia.TiaPortalMode.WithoutUserInterface)  # type: ignore
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
            self.name
            if self.name.endswith(f".ap{self.version.value}")
            else f"{self.name}.ap{self.version.value}"
        )
        file_path = os.path.join(self.path, self.name, file_name)

        if os.path.exists(file_path):
            raise tia_e.TIAProjectAlreadyExists(f"File {file_path} already exists")

        self.value = session.Projects.Create(DirectoryInfo(self.path), self.name)

        self.client.project = self

    def save(self) -> None:
        """Saves the project in the TIA Portal.

        Raises:
            tia_e.TIAInvalidProject: If the value is None.
        """
        if self.value is None:
            raise tia_e.TIAInvalidProject("Project is None")
        if self.is_modified():
            self.value.Save()

    def save_as(self, name: str, path: Optional[str] = None) -> None:
        """Saves the project in the TIA Portal.

        Parameters:
            name (str): The name of the project.

        Raises:
            tia_e.TIAInvalidProject: If the value is None.
        """
        if self.value is None:
            raise tia_e.TIAInvalidProject("Project is None")

        if path is None:
            dir_info = DirectoryInfo(os.path.join(self.path, name))
        else:
            dir_info = DirectoryInfo(os.path.join(path, name))

        self.value.SaveAs(dir_info)

        self.close()

        if path is None:
            project = Project(self.client, self.path, name, self.version)
        else:
            project = Project(self.client, path, name, self.version)
        project.open()

    def is_modified(self) -> bool:
        """Checks if the project is modified.

        Raises:
            tia_e.TIAInvalidProject: If the value is None.

        Returns:
            bool: True if the project is modified, False otherwise.
        """
        if self.value is None:
            raise tia_e.TIAInvalidProject("Project is None")
        return self.value.IsModified

    def compile(self) -> None:
        """Compiles the project in the TIA Portal. This will compile all the software in the project.
        This will be needed to be able to export parts of the project.

        Raises:
            tia_e.TIAInvalidProject: If the value is None.
        """
        if self.value is None:
            raise tia_e.TIAInvalidProject("Project is None")

        devices: list[hw.DeviceItem]
        devices = [item for device in self.value.Devices for item in device.DeviceItems]  # type: ignore
        software_containers: list[Optional[hwf.SoftwareContainer]]
        software_containers = [item.GetService[hwf.SoftwareContainer]() for item in devices]  # type: ignore
        software_containers_filtered = [
            item for item in software_containers if item is not None
        ]

        for software_container in software_containers_filtered:
            software = software_container.Software

            software_compile_service: Optional[comp.ICompilable]
            software_compile_service = software.GetService[comp.ICompilable]()  # type: ignore
            if software_compile_service is not None:
                software_compile_service.Compile()

    def get_file_info(self) -> FileInfo:
        """Gets the file info of the project.

        Raises:
            tia_e.TIAInvalidProject: If the value is None.

        Returns:
            FileInfo: The file info of the project.
        """
        if self.value is None:
            raise tia_e.TIAInvalidProject("Project is None")
        return self.value.Path

    def is_open(self) -> bool:
        """Checks if the project is open. Basically checks if the value is None.

        Returns:
            bool: True if the project is open, False otherwise.
        """
        return self.value is not None

    def get_device_item(self, name: str) -> Optional[DeviceItem]:
        """Gets a device item by name.

        Parameters:
            name (str): The name of the device item.

        Raises:
            tia_e.TIAInvalidProject: If the value is None.

        Returns:
            Optional[DeviceItem]: The device item if it exists, None otherwise.
        """
        if self.value is None:
            raise tia_e.TIAInvalidProject("Project is None")

        for device in self.devices:
            for item in device.get_items():
                if item.name == name:
                    return item

        return None

    def get_plcs(self) -> list[DeviceItem]:
        """Gets all the PLCs in the project.

        Raises:
            tia_e.TIAInvalidProject: If the value is None.

        Returns:
            list[DeviceItem]: A list of all the PLCs in the project.
        """
        if self.value is None:
            raise tia_e.TIAInvalidProject("Project is None")

        plcs: list[DeviceItem] = []

        for device in self.devices:
            for item in device.get_items():
                if isinstance(item.get_software(), PLCSoftware):
                    plcs.append(item)

        return plcs

    @property
    def devices(self) -> Devices:
        """Gets the devices in the project.

        Raises:
            tia_e.TIAInvalidProject: If the value is None.

        Returns:
            Devices: The devices in the project.
        """
        if self.value is None:
            raise tia_e.TIAInvalidProject("Project is None")
        return Devices(self)

    @devices.setter
    def devices(self, value: Any) -> None:
        raise NotImplementedError(
            "Devices can only be accessed through the devices property"
        )
