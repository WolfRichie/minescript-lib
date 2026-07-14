from typing import Any
import java
from minescript import ItemStack

from code.Proxy import PyJinnProxy

class MappingsHelper(PyJinnProxy):
  @staticmethod
  def get_runtime_class_name(pretty_class_name: str) -> str: ...
  @staticmethod
  def get_pretty_class_name(runtime_class_name: str) -> str: ...
  @staticmethod
  def get_runtime_field_name(clazz: java.JavaObject, pretty_field_name: str) -> str: ...
  @staticmethod
  def get_pretty_field_names(clazz: java.JavaObject) -> java.JavaObject: ...
  @staticmethod
  def get_runtime_method_names(clazz: java.JavaObject, pretty_method_name: str) -> java.JavaObject: ...
  @staticmethod
  def get_pretty_method_names(clazz: java.JavaObject) -> java.JavaObject: ...

class ReflectionHelper(PyJinnProxy):
  @staticmethod
  def get_private_field(instance: java.JavaObject, pretty_field_name: str) -> Any:
    """Read a private field value via mappings and reflection.

    Args:
      instance: Java object instance containing the field.
      pretty_field_name: Mapped field name to read.

    Returns:
      The reflected field value.
    """
    ...

class CraftingLayout(PyJinnProxy):
  container_name: str
  grid_slots: list[int]
  grid_size: int
  result_slot: int

class ContainerHelper(PyJinnProxy):
  @staticmethod
  def get_container_class_name() -> str:
    """Return the mapped class name for the currently open container menu."""
    ...
  @staticmethod
  def get_container_id() -> int:
    """Return the active container id.

    Returns:
      The menu/container id when available.
      `-1` if no container is currently available.
    """
    ...
  @staticmethod
  def container_get_slot(slot: int) -> Any:
    """Return the item entry for `slot` from `container_get_items()`.

    Returns:
      The slot item object when found, otherwise `None`.
    """
    ...
  @staticmethod
  def crafting_get_grid_size() -> int:
    """Return the crafting grid size for the currently-open container.

    Returns:
      9 for a 3x3 crafting grid, 4 for a 2x2 player crafting grid, or 0 if
      the open container is not a crafting UI.
    """
    ...
  @staticmethod
  def crafting_get_layout() -> CraftingLayout:
    """Return menu-specific crafting slot layout.

    Returns:
      CraftingLayout object with:
      - `container_name`: mapped runtime container class name.
      - `grid_slots`: list of valid crafting menu slot ids.
      - `grid_size`: precomputed length of `grid_slots`.
      - `result_slot`: menu slot id for the crafting result.
    """
    ...
  @staticmethod
  def crafting_place_slot(slot: int, crafting_slot: int, count: int = 1) -> ItemStack | bool | None:
    """Place item(s) from a container slot into a crafting grid slot.

    Args:
      slot (int): Source container slot index to take item(s) from.
      crafting_slot (int): Target crafting menu slot id. Must be present in
        `get_crafting_layout().grid_slots`.
      count (int): Number of right-click placements to perform.

    Returns:
      ItemStack: The current crafting result item from the active result slot
        (slot 0 for crafting/inventory menus, slot 45 for crafter).
      None: If the active result slot has no result item after placement.
      bool: `False` when the open container is not a supported crafting UI or
        when an interaction click fails.

    Raises:
      IndexError: If `crafting_slot` is outside the supported range.
    """
    ...
  @staticmethod
  def crafting_shift_click_result() -> ItemStack | bool | None:
    """Shift-clicks the result slot and return the item that was present.

    Returns:
      ItemStack: The item that was present in the active result slot before
        shift-click (slot 0 or slot 45 for crafter).
      bool: `False` when the open container is unsupported or the click fails.
      None: If the result slot has no item.
    """
    ...
  @staticmethod
  def raw_click(slot: int, button_or_slot: int = 0, click_type: str | None = ...) -> bool:
    """Click a slot in the open container.

    Args:
      slot (int): Slot index to click.
      button_or_slot (int): Mouse button or hotbar slot index, depending on click type.
      click_type (str | None): Click type enum name as expected by runtime.
        If `None`, defaults to PICKUP.

    Returns:
      bool: `True` when the click call was issued, otherwise `False`.
    """
    ...

  @staticmethod
  def click_slot(slot: int, button: int = 0) -> bool: ...
  @staticmethod
  def shift_click_slot(slot: int) -> bool: ...
  @staticmethod
  def click_swap_with_hotbar(slot: int, hotbar_slot: int) -> bool: ...
  @staticmethod
  def pickup_swap_container(slot_a: int, slot_b: int) -> bool: ...
