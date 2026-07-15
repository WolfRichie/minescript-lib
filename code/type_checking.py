from __future__ import annotations

from typing import Any

import java

from code.Proxy import PyJinnProxy

Vector3f = tuple[float, float, float]


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
  def get_container_slot(slot: int) -> ItemStackInstance | None:
    """Return the item entry for `slot` from `get_container_items()`.

    Returns:
      The ItemStackInstance object when found, otherwise `None`.
    """
    ...

  @staticmethod
  def get_inventory_slot(slot: int) -> ItemStackInstance | None: ...

  @staticmethod
  def get_item_stack_by_inventory_slot(slot: int) -> ItemStackInstance | None: ...

  @staticmethod
  def get_item_stack_by_container_slot(slot: int) -> ItemStackInstance | None: ...

  @staticmethod
  def container_find_item_id(item_id: str) -> list[ItemStackInstance]: ...

  @staticmethod
  def inventory_find_item_id(item_id: str) -> list[ItemStackInstance]: ...

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
  def crafting_place_slot(slot: int, crafting_slot: int, count: int = 1) -> ItemStackInstance | bool | None:
    """Place item(s) from a container slot into a crafting grid slot.

    Args:
      slot (int): Source container slot index to take item(s) from.
      crafting_slot (int): Target crafting menu slot id. Must be present in
        `get_crafting_layout().grid_slots`.
      count (int): Number of right-click placements to perform.

    Returns:
      ItemStackInstance: The current crafting result item from the active result slot
        (slot 0 for crafting/inventory menus, slot 45 for crafter).
      None: If the active result slot has no result item after placement.
      bool: `False` when the open container is not a supported crafting UI or
        when an interaction click fails.

    Raises:
      IndexError: If `crafting_slot` is outside the supported range.
    """
    ...

  @staticmethod
  def crafting_shift_click_result() -> ItemStackInstance | bool | None:
    """Shift-clicks the result slot and return the item that was present.

    Returns:
      ItemStackInstance: The item that was present in the active result slot before
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

  @staticmethod
  def get_inventory_selected_hotbar_slot() -> int: ...


class FishingHelper(PyJinnProxy):
  @staticmethod
  def is_holding_rod() -> bool: ...

  @staticmethod
  def is_casted() -> bool: ...

  @staticmethod
  def is_biting() -> bool | None: ...

  @staticmethod
  def is_open_water() -> bool | None: ...

  @staticmethod
  def get_hooked_entity() -> Any: ...

  @staticmethod
  def get_time_until_lured() -> int | None: ...

  @staticmethod
  def get_time_until_hooked() -> int | None: ...

  @staticmethod
  def use_rod() -> bool: ...


class ClientHelper(PyJinnProxy):
  @staticmethod
  def set_current_screen(screen: java.JavaObject) -> None: ...

  @staticmethod
  def get_current_screen() -> java.JavaObject | None: ...

  @staticmethod
  def get_current_screen_class_name() -> str: ...

  @staticmethod
  def close_current_screen() -> None: ...

  @staticmethod
  def open_pause_screen() -> None: ...

  @staticmethod
  def open_inventory_screen() -> None: ...

  @staticmethod
  def disconnect(str: str = "Disconnected by Minescript") -> None: ...

  @staticmethod
  def get_level_data() -> ClientLevelData: ...

  @staticmethod
  def get_fps() -> int: ...

  @staticmethod
  def get_camera_position() -> Vector3f: ...

  @staticmethod
  def get_camera_type() -> str:
    """
    FIRST_PERSON, THIRD_PERSON_BACK, THIRD_PERSON_FRONT
    """
    ...


class ClientLevelData(PyJinnProxy):
  hardcore: bool
  is_flat: bool
  game_time: int
  day_time: int
  raining: bool
  difficulty: str
  difficulty_locked: bool

  def __init__(self, hardcore: bool, is_flat: bool, game_time: int, day_time: int, raining: bool, difficulty: str, difficulty_locked: bool) -> None: ...


class UtilHelper(PyJinnProxy):
  @staticmethod
  def get_class_name(obj: java.JavaObject) -> str:
    """Return the mapped class name for a Java object instance."""
    ...

  @staticmethod
  def get_clipboard() -> str: ...

  @staticmethod
  def set_clipboard(text: str) -> None: ...


class ItemStackInstance(PyJinnProxy):
  def __init__(self, item_stack: java.JavaObject | str) -> None: ...

  def get_display_name(self: ItemStackInstance, use_custom_name: bool = False) -> str | None: ...

  def get_item_id(self: ItemStackInstance) -> str | None: ...

  def get_item(self: ItemStackInstance) -> ItemInstance: ...

  def get_item_java_object(self: ItemStackInstance) -> java.JavaObject: ...

  def get_count(self: ItemStackInstance) -> int: ...

  def get_max_stack_size(self: ItemStackInstance) -> int: ...

  def get_java_object(self: ItemStackInstance) -> java.JavaObject: ...


class ItemInstance(PyJinnProxy):
  def __init__(self, item: java.JavaObject | str) -> None: ...

  def get_item_id(self: ItemInstance) -> str | None: ...

  def get_numeric_id(self: ItemInstance) -> int: ...

  @staticmethod
  def by_numeric_id(id: int) -> ItemInstance: ...

  def get_display_name(self: ItemInstance, use_custom_name: bool = False) -> str | None: ...

  def get_item_stack(self: ItemInstance) -> ItemStackInstance: ...

  def get_item_stack_java_object(self: ItemInstance) -> java.JavaObject: ...

  def get_count(self: ItemInstance) -> int: ...

  def get_max_stack_size(self: ItemInstance) -> int: ...

  def get_java_object(self: ItemInstance) -> java.JavaObject: ...