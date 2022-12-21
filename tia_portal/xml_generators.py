from datetime import datetime
import os
from typing import Optional, Protocol
import xml.etree.ElementTree as ET

from config import DATA_PATH
from version import TIAVersion

class Block(Protocol):
    def get_id(self) -> str:
        ...

class MultilingualText:
    def __init__(self, id: str, composition_name: str):
        self.element = ET.Element("MultilingualText", {"ID": id, "CompositionName": composition_name})

        self.object_list = ET.Element("ObjectList")
        self.element.append(self.object_list)

    def add_text(self, id: str, culture: str, text: str):
        text_item = ET.Element("MultilingualTextItem", {"ID": id, "CompositionName": "Items"})
        self.object_list.append(text_item)

        text_item_attribute_list = ET.Element("AttributeList")
        text_item.append(text_item_attribute_list)

        text_item_culture = ET.Element("Culture")
        text_item_culture.text = culture
        text_item_attribute_list.append(text_item_culture)

        text_item_text = ET.Element("Text")
        text_item_text.text = text
        text_item_attribute_list.append(text_item_text)

    @staticmethod
    def generate_oneline_text(culture: str, text: str):
        element = ET.Element("MultiLanguageText", {"Lang": culture})
        element.text = text
        return element

class FunctionBlockInterface:
    def __init__(self):
        self.element = ET.Element("Interface")
        self.sections = ET.Element("Sections", {"xmlns": "http://www.siemens.com/automation/Openness/SW/Interface/v3"})

        self.element.append(self.sections)

        self.input = ET.Element("Section", {"Name": "Input"})
        self.output = ET.Element("Section", {"Name": "Output"})
        self.inout = ET.Element("Section", {"Name": "InOut"})
        self.static = ET.Element("Section", {"Name": "Static"})
        self.temp = ET.Element("Section", {"Name": "Temp"})
        self.constant = ET.Element("Section", {"Name": "Constant"})

        self.sections.extend([self.input, self.output, self.inout, self.static, self.temp, self.constant])

    def add_variable(self, section: ET.Element, name: str, type: str, comment: str):
        member = ET.Element("Member", {"Name": name, "Datatype": type})
        section.append(member)

        if comment:
            comment_element = ET.Element("Comment")
            comment_element.append(MultilingualText.generate_oneline_text("en-US", comment))
            member.append(comment_element)

    def add_input(self, name: str, type: str, comment: str = ""):
        self.add_variable(self.input, name, type, comment)

    def add_output(self, name: str, type: str, comment: str = ""):
        self.add_variable(self.output, name, type, comment)

    def add_inout(self, name: str, type: str, comment: str = ""):
        self.add_variable(self.inout, name, type, comment)

    def add_static(self, name: str, type: str, comment: str = ""):
        self.add_variable(self.static, name, type, comment)

    def add_temp(self, name: str, type: str, comment: str = ""):
        self.add_variable(self.temp, name, type, comment)

    def add_constant(self, name: str, type: str, comment: str = ""):
        self.add_variable(self.constant, name, type, comment)

class Network:
    def __init__(self, block: Block, title: str, comment: str = ""):
        self.id = 21
        self.element = ET.Element("SW.Blocks.CompileUnit", {"ID": block.get_id(), "CompositionName": "CompileUnits"})
        attribute_list = ET.Element("AttributeList")
        self.element.append(attribute_list)

        self.network_source = ET.Element("NetworkSource")
        attribute_list.append(self.network_source)

        programming_language = ET.Element("ProgrammingLanguage")
        programming_language.text = "FBD"
        attribute_list.append(programming_language)

        self.flg_net_appended = False
        self.flg_net = ET.Element("FlgNet", {"xmlns": "http://www.siemens.com/automation/Openness/SW/NetworkSource/FlgNet/v3"})

        self.labels_appended = False
        self.labels = ET.Element("Labels")

        self.parts_appended = False
        self.parts = ET.Element("Parts")

        self.wires_appended = False
        self.wires = ET.Element("Wires")

        object_list = ET.Element("ObjectList")
        self.element.append(object_list)

        title_element = MultilingualText(block.get_id(), "Title")
        title_element.add_text(block.get_id(), "en-US", title)
        object_list.append(title_element.element)

        if comment:
            comment_element = MultilingualText(block.get_id(), "Comment")
            comment_element.add_text(block.get_id(), "en-US", comment)
            object_list.append(comment_element.element)

    def get_id(self):
        value = self.id
        self.id += 1
        return str(value)

    def add_label(self):
        raise NotImplementedError("Not implemented yet")

    def add_access(self, scope: str, uid: str, type: str, value: str):
        if not self.flg_net_appended:
            self.network_source.append(self.flg_net)
            self.flg_net_appended = True
        if not self.parts_appended:
            self.flg_net.append(self.parts)
            self.parts_appended = True

        access = ET.Element("Access", {"Scope": scope, "UId": uid})
        constant = ET.Element("Constant")
        constanttype = ET.Element("ConstantType")
        constanttype.text = type
        constantvalue = ET.Element("ConstantValue")
        constantvalue.text = value
        constant.append(constanttype)
        constant.append(constantvalue)
        access.append(constant)
        self.parts.append(access)

    def add_part(self, name: str, parent: Optional[str] = None):
        if not self.flg_net_appended:
            self.network_source.append(self.flg_net)
            self.flg_net_appended = True
        if not self.parts_appended:
            self.flg_net.append(self.parts)
            self.parts_appended = True

        if name == "GetBlockName":
            version = "1.1"
            inputs = {"en": {}, "size": {"scope": "LiteralConstant", "UId": self.get_id(), "type": "DInt", "value": "0"}}
            outputs = {"Ret_Val": {"scope": "LocalVariable", "UId": self.get_id(), ""}}
        else:
            raise NotImplementedError("Not implemented yet")

        part_uid = self.get_id()
        part = ET.Element("Part", {"Name": name, "Version": version, "UId": part_uid})
        self.parts.append(part)

        for input in inputs.keys():
            if input == "en" and parent is None:
                self.add_wire(part_uid, "en", True)
            else:
                self.add_access(inputs[input]["scope"], inputs[input]["UId"], inputs[input]["type"], inputs[input]["value"])
                self.add_wire(part_uid, input)

        for output in outputs:
            self.add_access()
            self.add_wire(part_uid, output)

    def add_wire(self, source: str, target: Optional[str] = None, powerrail: bool = False):
        if not self.flg_net_appended:
            self.network_source.append(self.flg_net)
            self.flg_net_appended = True
        if not self.wires_appended:
            self.flg_net.append(self.wires)
            self.wires_appended = True

        wire = ET.Element("Wire", {"UId": self.get_id()})
        self.wires.append(wire)

        if powerrail:
            powerrail_elem = ET.Element("Powerrail")
            wire.append(powerrail_elem)

        if target is not None:
            name_con = ET.Element("NameCon", {"UId": source, "Name": target})
            wire.append(name_con)

class FunctionBlock(Block):
    def __init__(self, name: str, version: TIAVersion, description: str = ""):
        self.name = name
        self.path = os.path.join(DATA_PATH, f"{name}.xml")
        self.version = version
        self.description = description
        self.__id = 0

        # if os.path.exists(self.path):
        #     raise FileExistsError(f"File {self.path} already exists")

        self.document = ET.Element("Document")
        self.document_info = ET.Element("DocumentInfo")
        self.block = ET.Element("SW.Blocks.FB", {"ID": self.get_id()})

        self.basic_load()

        version_name = version.name.replace("_", ".")

        self.engnieering = ET.Element("Engineering", {"version": version_name})


    def get_id(self) -> str:
        if self.__id == 0:
            self.__id += 1
            return "0"
        value = hex(self.__id).lstrip("0x").rstrip("L")
        self.__id += 1
        return value

    def basic_load(self):
        self.load_document_info()
        self.load_default_block()
        self.load_block_header()

    def load_document_info(self):
        current_time = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ")

        created = ET.Element("Created")
        created.text = current_time
        self.document_info.append(created)

        export_settings = ET.Element("ExportSettings")
        export_settings.text = "None"
        self.document_info.append(export_settings)

        # It might be necessary to add the InstalledProducts to the DocumentInfo

    def load_default_block(self):
        self.block_attribute_list = ET.Element("AttributeList")
        self.block.append(self.block_attribute_list)

        self.auto_number = ET.Element("AutoNumber")
        self.auto_number.text = "true"
        self.block_attribute_list.append(self.auto_number)

        self.interface = FunctionBlockInterface()
        self.block_attribute_list.append(self.interface.element)

        self.memory_layout = ET.Element("MemoryLayout")
        self.memory_layout.text = "Optimized"
        self.block_attribute_list.append(self.memory_layout)

        self.memory_reserve = ET.Element("MemoryReserve")
        self.memory_reserve.text = "100"
        self.block_attribute_list.append(self.memory_reserve)

        self.name_xml = ET.Element("Name")
        self.name_xml.text = self.name
        self.block_attribute_list.append(self.name_xml)

        self.programming_languague = ET.Element("ProgrammingLanguage")
        self.programming_languague.text = "FBD"
        self.block_attribute_list.append(self.programming_languague)

        self.block_object_list = ET.Element("ObjectList")
        self.block.append(self.block_object_list)

    def load_block_header(self):
        self.block_title = MultilingualText(self.get_id(), "Title")
        self.block_title.add_text(self.get_id(), "en-US", self.name)

        self.block_object_list.append(self.block_title.element)

        self.block_comment = MultilingualText(self.get_id(), "Comment")
        self.block_comment.add_text(self.get_id(), "en-US", self.description)

        self.block_object_list.append(self.block_comment.element)

    def build(self):
        self.document.append(self.engnieering)
        self.document.append(self.document_info)
        self.document.append(self.block)

    def save(self):
        self.build()
        ET.ElementTree(self.document).write(self.path, encoding="utf-8", xml_declaration=True)

    def add_input_variable(self, name: str, type: str, comment: str = ""):
        self.interface.add_input(name, type, comment)

    def add_output_variable(self, name: str, type: str, comment: str = ""):
        self.interface.add_output(name, type, comment)

    def add_inout_variable(self, name: str, type: str, comment: str = ""):
        self.interface.add_inout(name, type, comment)

    def add_static_variable(self, name: str, type: str, comment: str = ""):
        self.interface.add_static(name, type, comment)

    def add_temp_variable(self, name: str, type: str, comment: str = ""):
        self.interface.add_temp(name, type, comment)

    def add_constant_variable(self, name: str, type: str, comment: str = ""):
        self.interface.add_constant(name, type, comment)

    def add_network(self, network: Network):
        self.block_object_list.append(network.element)

if __name__ == "__main__":
    fb = FunctionBlock("test", TIAVersion.V15_1, "test description")

    fb.add_static_variable("Mode", '"Mode_PLC_FB"', "Mode")

    network = Network(fb, "test_network", "test_network_description")
    network.add_part("GetBlockName")

    fb.add_network(network)

    fb.save()