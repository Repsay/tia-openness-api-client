# encoding: utf-8
# module Siemens.Engineering.AddIn.Menu calls itself Menu
# from Siemens.Engineering.AddIn, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

from System import Enum

class ActionItem:
    """ """

    @property
    def DefaultLabelText(self):
        """Get: DefaultLabelText(self: ActionItem) -> str"""
        ...

class ActionItemStyle:  # skipped bases: <type 'object'>
    """ """

    pass

class CheckBoxActionItemStyle(ActionItemStyle):
    """ """

    @property
    def State(self):
        """
        Get: State(self: CheckBoxActionItemStyle) -> CheckBoxState

        Set: State(self: CheckBoxActionItemStyle) = value
        """
        ...

class CheckBoxState(Enum):  # skipped bases: <type 'IComparable'>, <type 'IFormattable'>, <type 'IConvertible'>
    """enum CheckBoxState, values: Checked (1), Unchecked (0)"""

    Checked = None
    Unchecked = None
    value__ = None

class ChildItemFactory(
    IMenuItemFactoryPrivate  # type: ignore
):  # skipped bases: <type 'ISubmenuFactoryPrivate'>, <type 'IActionItemFactoryPrivate'>
    """ """

    def AddActionItem(self, defaultLabelText, clickDelegate, updateStatusDelegate=...):
        """
        AddActionItem[TSelectedObject](self: ChildItemFactory, defaultLabelText: str, clickDelegate: OnClickDelegate) -> ActionItem[TSelectedObject]

        AddActionItem[TSelectedObject](self: ChildItemFactory, defaultLabelText: str, clickDelegate: OnClickDelegate, updateStatusDelegate: OnUpdateStatusDelegate) -> ActionItem[TSelectedObject]

        AddActionItem[(TSelectedObject1, TSelectedObject2)](self: ChildItemFactory, defaultLabelText: str, clickDelegate: OnClickDelegate) -> ActionItem[TSelectedObject1, TSelectedObject2]

        AddActionItem[(TSelectedObject1, TSelectedObject2)](self: ChildItemFactory, defaultLabelText: str, clickDelegate: OnClickDelegate, updateStatusDelegate: OnUpdateStatusDelegate) -> ActionItem[TSelectedObject1, TSelectedObject2]

        AddActionItem[(TSelectedObject1, TSelectedObject2, TSelectedObject3)](self: ChildItemFactory, defaultLabelText: str, clickDelegate: OnClickDelegate) -> ActionItem[TSelectedObject1, TSelectedObject2, TSelectedObject3]

        AddActionItem[(TSelectedObject1, TSelectedObject2, TSelectedObject3)](self: ChildItemFactory, defaultLabelText: str, clickDelegate: OnClickDelegate, updateStatusDelegate: OnUpdateStatusDelegate) -> ActionItem[TSelectedObject1, TSelectedObject2, TSelectedObject3]
        """
        ...
    def AddActionItemWithCheckBox(self, defaultLabelText, clickDelegate, updateStatusDelegate):
        """
        AddActionItemWithCheckBox[TSelectedObject](self: ChildItemFactory, defaultLabelText: str, clickDelegate: OnClickDelegate, updateStatusDelegate: OnUpdateStatusDelegate[TSelectedObject, CheckBoxActionItemStyle]) -> ActionItem[TSelectedObject]

        AddActionItemWithCheckBox[(TSelectedObject1, TSelectedObject2)](self: ChildItemFactory, defaultLabelText: str, clickDelegate: OnClickDelegate, updateStatusDelegate: OnUpdateStatusDelegate[TSelectedObject1, TSelectedObject2, CheckBoxActionItemStyle]) -> ActionItem[TSelectedObject1, TSelectedObject2]

        AddActionItemWithCheckBox[(TSelectedObject1, TSelectedObject2, TSelectedObject3)](self: ChildItemFactory, defaultLabelText: str, clickDelegate: OnClickDelegate, updateStatusDelegate: OnUpdateStatusDelegate[TSelectedObject1, TSelectedObject2, TSelectedObject3, CheckBoxActionItemStyle]) -> ActionItem[TSelectedObject1, TSelectedObject2, TSelectedObject3]
        """
        ...
    def AddActionItemWithRadioButton(self, defaultLabelText, clickDelegate, updateStatusDelegate):
        """
        AddActionItemWithRadioButton[TSelectedObject](self: ChildItemFactory, defaultLabelText: str, clickDelegate: OnClickDelegate, updateStatusDelegate: OnUpdateStatusDelegate[TSelectedObject, RadioButtonActionItemStyle]) -> ActionItem[TSelectedObject]

        AddActionItemWithRadioButton[(TSelectedObject1, TSelectedObject2)](self: ChildItemFactory, defaultLabelText: str, clickDelegate: OnClickDelegate, updateStatusDelegate: OnUpdateStatusDelegate[TSelectedObject1, TSelectedObject2, RadioButtonActionItemStyle]) -> ActionItem[TSelectedObject1, TSelectedObject2]

        AddActionItemWithRadioButton[(TSelectedObject1, TSelectedObject2, TSelectedObject3)](self: ChildItemFactory, defaultLabelText: str, clickDelegate: OnClickDelegate, updateStatusDelegate: OnUpdateStatusDelegate[TSelectedObject1, TSelectedObject2, TSelectedObject3, RadioButtonActionItemStyle]) -> ActionItem[TSelectedObject1, TSelectedObject2, TSelectedObject3]
        """
        ...
    def AddSubmenu(self, defaultLabelText):
        """AddSubmenu(self: ChildItemFactory, defaultLabelText: str) -> Submenu"""
        ...

class ContextMenuAddIn:  # skipped bases: <type 'object'>
    """ """

    def BuildContextMenuItems(self, *args):  # cannot find CLR method
        """BuildContextMenuItems(self: ContextMenuAddIn, addInRootSubmenu: Submenu)"""
        ...

class MenuItem:  # skipped bases: <type 'object'>
    """ """

    pass

class MenuSelectionProvider:
    """ """

    def GetSelection(self):
        """
        GetSelection(self: MenuSelectionProvider) -> IEnumerable[object]

        GetSelection[TRequestedType](self: MenuSelectionProvider) -> IEnumerable[TRequestedType]
        """
        ...

# Error generating skeleton for function __repr__: 'type' object has no attribute '__bases__'

class MenuStatus(Enum):  # skipped bases: <type 'IComparable'>, <type 'IFormattable'>, <type 'IConvertible'>
    """enum MenuStatus, values: Disabled (1), Enabled (0), Hidden (2)"""

    Disabled = None
    Enabled = None
    Hidden = None
    value__ = None

class RadioButtonActionItemStyle(ActionItemStyle):
    """ """

    @property
    def State(self):
        """
        Get: State(self: RadioButtonActionItemStyle) -> RadioButtonState

        Set: State(self: RadioButtonActionItemStyle) = value
        """
        ...

class RadioButtonState(Enum):  # skipped bases: <type 'IComparable'>, <type 'IFormattable'>, <type 'IConvertible'>
    """enum RadioButtonState, values: Selected (1), Unselected (0)"""

    Selected = None
    Unselected = None
    value__ = None

class Submenu(MenuItem, IMenuItemContainerPrivate):  # type: ignore
    """ """

    @property
    def DefaultLabelText(self):
        """Get: DefaultLabelText(self: Submenu) -> str"""
        ...
    @property
    def Items(self):
        """Get: Items(self: Submenu) -> ChildItemFactory"""
        ...
