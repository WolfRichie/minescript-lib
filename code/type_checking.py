from java import *
from code.Proxy import PyJinnProxy
from minescript import Vector3f, BlockPos

class ContainerLayout:
    container_name: str
    layouts: dict[str, list[int]]
    size: int
    is_unknown: bool

    def __init__(
        self,
        container_name: str,
        layouts: dict[str, list[int]],
        is_unknown: bool = False,
    ) -> None: ...

class EnchantmentInfo:
    id: int
    name: str
    level: int
    costs: int

class CraftingLayout:
    container_name: str
    layouts: dict[str, list[int]]
    result_slot: int
    is_unknown: bool
    size: int

    def __init__(
        self,
        container_name: str,
        crafting_grid: list[int],
        result_slot: int,
        inventory: list[int],
        is_unknown: bool = False,
    ) -> None: ...

    @property
    def grid_slots(self) -> list[int]: ...

    @property
    def grid_size(self) -> int: ...
  
class BlocksHelper(PyJinnProxy):
  @staticmethod
  def get_block_pos(x: int|float|BlockPos|Vector3f, y: int|float|None = None, z: int|float|None = None) -> JavaObject: ...
  @staticmethod
  def get_block_entity(x: int|float|JavaObject|BlockPos|Vector3f, y: int|float|None = None, z: int|float|None = None) -> JavaObject: ...
  @staticmethod
  def set_command_block_entity_command(command_block_entity: JavaObject, command: str) -> bool: ...
  @staticmethod
  def get_command_block_entity_command(command_block_entity: JavaObject) -> str | None: ...
  @staticmethod
  def get_command_block_entity_last_output(command_block_entity: JavaObject) -> str | None: ...
  @staticmethod
  def get_command_block_entity_mode(command_block_entity: JavaObject) -> str | None: ...
  @staticmethod
  def is_command_block_entity_conditions_met(command_block_entity: JavaObject) -> bool | None: ...
  @staticmethod
  def is_command_block_entity_powered(command_block_entity: JavaObject) -> bool | None: ...
  @staticmethod
  def is_command_block_entity_automatic(command_block_entity: JavaObject) -> bool | None: ...
  @staticmethod
  def get_jukebox_block_entity_item(jukebox_block_entity: JavaObject) -> JavaObject | None: ...
  @staticmethod
  def get_jukebox_block_entity_ticks_since_song_started(jukebox_block_entity: JavaObject) -> int | None: ...
  @staticmethod
  def is_jukebox_block_entity_song_playing(jukebox_block_entity: JavaObject) -> bool | None: ...
  
class MappingsHelper(PyJinnProxy):
  @staticmethod
  def get_runtime_class_name(pretty_class_name: str) -> str: ...

  @staticmethod
  def get_pretty_class_name(runtime_class_name: str) -> str: ...

  @staticmethod
  def get_runtime_field_name(clazz: JavaObject, pretty_field_name: str) -> str: ...

  @staticmethod
  def get_pretty_field_names(clazz: JavaObject) -> JavaObject: ...

  @staticmethod
  def get_runtime_method_names(clazz: JavaObject, pretty_method_name: str) -> JavaObject: ...

  @staticmethod
  def get_pretty_method_names(clazz: JavaObject) -> JavaObject: ...


class ReflectionHelper(PyJinnProxy):
  @staticmethod
  def get_private_field(instance: JavaObject, pretty_field_name: str) -> Any: ...


class ItemsHelper(PyJinnProxy):  
  @staticmethod
  def get_item_id(item: JavaObject | str | int) -> str | None: ...

  @staticmethod
  def get_numeric_id(item: JavaObject | str | int) -> int: ...

  @staticmethod
  def get_display_name(item: JavaObject | str | int, use_custom_name: bool = False) -> str | None:  ...

  @staticmethod
  def get_count(item: JavaObject | str | int) -> int: ...

  @staticmethod
  def get_max_stack_size(item: JavaObject | str | int) -> int: ...

  @staticmethod
  def get_item_stack_java_object(item: JavaObject | str | int) -> JavaObject: ...

  @staticmethod
  def get_item_java_object(item: JavaObject | str | int) -> JavaObject: ...

  @staticmethod
  def get_json(item: JavaObject | str | int) -> str: ...

  @staticmethod
  def get_components(item: JavaObject | str | int) -> str: ...


class ContainerHelper(PyJinnProxy): 
  @staticmethod
  def enchantment_table_get_enchant_info(enchantment_apply_type) -> EnchantmentInfo|None: ...
  @staticmethod
  def enchantment_table_apply_enchant(enchantment_apply_type) -> bool: ...

  @staticmethod
  def get_container_layout() -> ContainerLayout|CraftingLayout|None: ...
  @staticmethod
  def get_container_class_name() -> str: ...

  @staticmethod
  def get_container_id() -> int: ...

  @staticmethod
  def get_container_slot(slot: int) -> JavaObject | None: ...

  @staticmethod
  def get_inventory_slot(slot: int) -> JavaObject | None:...

  @staticmethod
  def get_item_stack_by_inventory_slot(slot: int) -> JavaObject | None: ...

  @staticmethod
  def get_item_stack_by_container_slot(slot: int) -> JavaObject | None: ...

  @staticmethod
  def container_find_item_id(item_id: str) -> list[JavaObject]: ...

  @staticmethod
  def inventory_find_item_id(item_id: str) -> list[JavaObject]: ...

  @staticmethod
  def crafting_get_grid_size() -> int:...

  @staticmethod
  def crafting_get_layout() -> CraftingLayout:...

  @staticmethod
  def crafting_place_slot(slot: int, crafting_slot: int, count: int = 1) -> ItemStack | bool | None: ...

  @staticmethod
  def crafting_shift_click_result() -> ItemStack | bool | None: ...

  @staticmethod
  def raw_click(slot: int, button_or_slot: int = 0, click_type: str | None = ...) -> bool: ...

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

  @staticmethod
  def get_inventory_free_slot() -> int | None: ...
  # @staticmethod
  # def test(): ...

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
  def set_current_screen(screen: JavaObject) -> None: ...

  @staticmethod
  def get_current_screen() -> JavaObject | None: ...

  @staticmethod
  def get_current_screen_class_name() -> str: ...

  @staticmethod
  def close_current_screen(with_close_container_packet: bool = True) -> None: ...

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
  def get_class_name(obj: JavaObject) -> str: ...
  @staticmethod
  def get_clipboard() -> str: ...
  @staticmethod
  def set_clipboard(text: str) -> None: ...

class RegistryHelper(PyJinnProxy):
  @staticmethod
  def get_by_id(registry: JavaObject, identifier: str) -> JavaObject: ...
  @staticmethod
  def get_registry_path(registry_name: str) -> JavaObject: ...
