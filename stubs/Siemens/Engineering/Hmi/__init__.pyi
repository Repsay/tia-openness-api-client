# encoding: utf-8
# module Siemens.Engineering.Hmi calls itself Hmi
# from Siemens.Engineering, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

from Siemens.Engineering import IEngineeringServiceProvider
from Siemens.Engineering.HW import Software
from Siemens.Engineering.Library.Types import IInstanceSearchScope, IUpdateProjectScope

class HmiTarget(
    Software, IInstanceSearchScope, IUpdateProjectScope, IEngineeringServiceProvider
):  # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringObject'>, <type 'IServiceProvider'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalObjectAccess'>
    """Represents the target device"""

    @property
    def Author(self):
        """
        Author of the device

        Get: Author(self: HmiTarget) -> str
        """
        ...
    @property
    def Connections(self):
        """
        Composition of connections

        Get: Connections(self: HmiTarget) -> ConnectionComposition
        """
        ...
    @property
    def Cycles(self):
        """
        Composition of cycles

        Get: Cycles(self: HmiTarget) -> CycleComposition
        """
        ...
    @property
    def GraphicLists(self):
        """
        Composition of graphic lists

        Get: GraphicLists(self: HmiTarget) -> GraphicListComposition
        """
        ...
    @property
    def ScreenFolder(self):
        """
        Gets the Hmi screen system folder

        Get: ScreenFolder(self: HmiTarget) -> ScreenSystemFolder
        """
        ...
    @property
    def ScreenGlobalElements(self):
        """
        Gets the Hmi screen global elements

        Get: ScreenGlobalElements(self: HmiTarget) -> ScreenGlobalElements
        """
        ...
    @property
    def ScreenOverview(self):
        """
        Gets the Hmi screen overview

        Get: ScreenOverview(self: HmiTarget) -> ScreenOverview
        """
        ...
    @property
    def ScreenPopupFolder(self):
        """
        System folder for the HMI pop-up screens

        Get: ScreenPopupFolder(self: HmiTarget) -> ScreenPopupSystemFolder
        """
        ...
    @property
    def ScreenSlideinFolder(self):
        """
        System folder for the HMI slide-in screens

        Get: ScreenSlideinFolder(self: HmiTarget) -> ScreenSlideinSystemFolder
        """
        ...
    @property
    def ScreenTemplateFolder(self):
        """
        Composition of screen template folders

        Get: ScreenTemplateFolder(self: HmiTarget) -> ScreenTemplateSystemFolder
        """
        ...
    @property
    def TagFolder(self):
        """
        Gets the Hmi tag system folder

        Get: TagFolder(self: HmiTarget) -> TagSystemFolder
        """
        ...
    @property
    def TextLists(self):
        """
        Composition of text lists

        Get: TextLists(self: HmiTarget) -> TextListComposition
        """
        ...
    @property
    def VBScriptFolder(self):
        """
        Gets the VBScript system folder

        Get: VBScriptFolder(self: HmiTarget) -> VBScriptSystemFolder
        """
        ...
    def GetAttribute(self, name):
        """
        GetAttribute(self: HmiTarget, name: str) -> object

            Gets an attribute with the given name.

            name: The name of the attribute to get.

            Returns: The attribute with the given name; otherwise, null.
        """
        ...
    def GetAttributeInfos(self):
        """
        GetAttributeInfos(self: HmiTarget) -> IList[EngineeringAttributeInfo]

            Returns a collection of EngineeringAttributeInfo objects describing the different attributes on this object.

            Returns: A collection of EngineeringAttributeInfo objects describing the different attributes on this object.
        """
        ...
    def ImportScreenGlobalElements(self, path, importOptions):
        """
        ImportScreenGlobalElements(self: HmiTarget, path: FileInfo, importOptions: ImportOptions)

            Simatic ML import of screen global elements

            path: Path to the Simatic ML file

            importOptions: Options to use for Import
        """
        ...
    def ImportScreenOverview(self, path, importOptions):
        """
        ImportScreenOverview(self: HmiTarget, path: FileInfo, importOptions: ImportOptions)

            Simatic ML import of a screen overview

            path: Path to the Simatic ML file

            importOptions: Options to use for Import
        """
        ...
    def SetAttribute(self, name, value):
        """
        SetAttribute(self: HmiTarget, name: str, value: object)

            Sets value of the attribute.

            name: The name of the attribute to set.

            value: The value of the attribute to set.
        """
        ...

# variables with complex values
