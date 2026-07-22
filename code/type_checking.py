from java import *
from code.Proxy import PyJinnProxy
from main import ContainerLayout

from minescript import ItemStack, Vector3f

class Stat:
    def __init__(self, stat_id: str, value: int, display_name: str): ...
    stat_id: str
    value: int
    display_name: str

class StatGroup:
    def __init__(self, group_id: str, display_name: str): ...
    group_id: str
    display_name: str
    stats: List[Stat]

class StatisticsHelper(PyJinnProxy):
    @staticmethod
    def get_stats() -> List[StatGroup]: ...
    @staticmethod
    def get_stat_value(stat: JavaObject) -> int:
      """
      Returns the value of the stat
      Args:
      - `stat` (JavaObject): Accepts an `net.minecraft.stats.Stat` JavaObject
      """
      ...
    
class Waypoint:
    def __init__(self, name: str, initials: str, x: int, y: int, z: int, index: int = 0, set_name: str = ""): ...
    name: str
    initials: str
    x: int
    y: int
    z: int
    index: int
    set_name: str

class GuiWidget:
    def __init__(self, x: int, y: int, width: int, height: int, message: str, active: bool, visible: bool, focused: bool, java_object: JavaObject): ...
    x: int
    y: int
    width: int
    height: int
    message: str
    active: bool
    visible: bool
    focused: bool
    java_object: JavaObject

class FoodInfo:
    food_level: int
    saturation_level: float
    exhaustion_level: float
    def __init__(self, food_level: int, saturation_level: float, exhaustion_level: float): ...
        
class XaeroHelper(PyJinnProxy):
    @staticmethod
    def is_mod_loaded() -> bool: ...
    @staticmethod
    def get_current_minimap_session() -> JavaObject | None: ...
    @staticmethod
    def get_current_world_manager() -> JavaObject | None: ...
    @staticmethod
    def get_current_world() -> JavaObject | None: ...
    @staticmethod
    def get_current_waypoint_set() -> JavaObject | None: ...
    @staticmethod
    def get_current_waypoint_set_name() -> str | None: ...
    @staticmethod
    def get_current_set_waypoints() -> List[Waypoint] | None:  ...
    @staticmethod
    def add_waypoint_to_current_set(name: str, x: float|int, y: float|int, z: float|int, initials: str) -> bool | None: ...
    @staticmethod
    def remove_waypoint_from_current_set(waypoint: Waypoint | int) -> bool: ...
    @staticmethod
    def get_waypoint_from_current_set(waypoint: Waypoint | int) -> Waypoint | None: ...
    @staticmethod
    def get_current_waypoint_set_count() -> int | None: ...
    
class BookScreenHelper(PyJinnProxy):

    @staticmethod
    def is_edit_book_screen() -> bool: ...
    @staticmethod
    def is_view_book_screen() -> bool: ...
    @staticmethod
    def is_sign_book_screen() -> bool: ...
    @staticmethod
    def is_book_screen() -> bool:
      """
      Wrapper for is_edit_book_screen() || is_view_book_screen() || is_sign_book_screen()
      """
      ...
    @staticmethod
    def get_book_content() -> List[str] | None: ...
    @staticmethod
    def get_page_content(page_index: int) -> str | None: ...
    @staticmethod
    def set_page_content_list(pages_content: List[str]) -> bool: ...
    @staticmethod
    def set_page_content(page_index: int, content: str) -> bool:
      """
      If the page index doesn't exist it will keep adding empty pages until it does.
      """
      ...
    @staticmethod
    def get_page_count() -> int | None: ...
    @staticmethod
    def get_current_page_index() -> int | None:
      """
      to get the current page "number" as shown on screen get_current_page_index + 1
      """
      ...
    @staticmethod
    def is_last_page() -> bool | None: ...
    @staticmethod
    def page_forward() -> None: ...
    @staticmethod
    def page_back() -> None: ...
    @staticmethod
    def sign_editable_book(title: str) -> bool: ...
    @staticmethod
    def save_editable_book() -> bool:
      """
      Saves the current edits to the book & quill and closes the screen (equivalent to clicking "Done").
      """
      ...
  
class GLFWHelper(PyJinnProxy):
    @staticmethod
    def get_cursor_gui_position() -> Vec2:
      """
      Vec2 has x,y fields
      """
      ...
    @staticmethod
    def get_cursor_position() -> Vec2:
      """
      Vec2 has x,y fields
      """
      ...
    @staticmethod
    def set_cursor_position(x: float, y: float): ...
    @staticmethod
    def show_cursor(): ...
    @staticmethod
    def hide_cursor(): ...
    @staticmethod
    def disable_cursor(): ...
    @staticmethod
    def is_cursor_hidden_or_disabled() -> bool: ...
    @staticmethod
    def is_mouse_button_pressed(button: int) -> bool: ...
    @staticmethod
    def send_mouse_button(button: int, press: bool):
      """
      Click the current position on the screen, (or release if press is set to false)
      """
      ...
  
class WindowHelper(PyJinnProxy):
    @staticmethod
    def get_window_handle() -> JavaObject:
      """
      Returns a `java.lang.Long` JavaObject
      """
      ...
    @staticmethod
    def is_window_fullscreen() -> bool: ...
    @staticmethod
    def is_window_minimized() -> bool: ...
    @staticmethod
    def get_position() -> Vec2:
      """
      Vec2 has x,y fields
      """
      ...
    @staticmethod
    def get_size() -> WindowSize:
      """
      WindowSize has width,height fields
      """
      ...
    @staticmethod
    def get_screen_size() -> WindowSize: ...
    @staticmethod
    def get_gui_size() -> WindowSize: ...
    @staticmethod
    def get_aspect_ratio() -> float: ...
    @staticmethod
    def get_gui_scale() -> float: ...
    @staticmethod
    def get_coordinate_scale(window_to_gui: bool = False) -> Vec2: ...
    @staticmethod
    def get_screen_position(gui_x: float, gui_y: float) -> Vec2:
      """
      Vec2 has x,y fields

      Convert Minecraft GUI-scaled coordinates into absolute window coordinates
      This function is used by `get_slot_screen_position` to calculate the position of a slot in a container
      """
      ...
    @staticmethod
    def get_gui_position(window_x: float, window_y: float) -> Vec2:
      """
      Vec2 has x,y fields. 
      Inverse of `get_screen_position`
      """
      ...

class EnchantmentInfo:
    id: int
    name: str
    level: int
    costs: int

class BlocksHelper(PyJinnProxy):
  @staticmethod
  def get_block_pos(x: int|float, y: int|float|None = None, z: int|float|None = None) -> JavaObject:
    """
    Create a Minecraft `net.minecraft.core.BlockPos` Java object from a position or coordinates.

    Accepted formats:

    - `x, y, z`: Individual numeric coordinates (float or int)

    All float values are automatically converted to integers, they are simply allowed for compatability purposes
    """
    ...
  @staticmethod
  def get_block_state(x: int|float|JavaObject, y: int|float|None = None, z: int|float|None = None) -> JavaObject:
    """
    Returnws the minecraft `net.minecraft.world.level.block.state.BlockState` Java object from a position or coordinates.

    Accepted formats:
    - `x, y, z`: Individual numeric coordinates (float or int)
    - `JavaObject` of `net.minecraft.core.BlockPos` passed into x and y/z are left to None
    """
    ...
  @staticmethod
  def get_block_state_block(block_state: JavaObject) -> JavaObject:
    """
    Returnws the minecraft `net.minecraft.world.level.block.Block` from a blockstate

    Accepted formats:
    - `JavaObject` of ``net.minecraft.world.level.block.state.BlockState`
    """
    ...
  @staticmethod
  def get_block_id(block: JavaObject) -> str | None:
    """
    Accepted formats:
    - `block`: `net.minecraft.world.level.block.Block` JavaObject
    """
    ...
  @staticmethod
  def get_block_state_id(block_state: JavaObject) -> str | None:
    """
    Accepted formats:
    - `block_state`: `net.minecraft.world.level.block.state.BlockState` JavaObject
    """
    ...
  @staticmethod
  def get_block_state_json(block_state: JavaObject) -> str:
    """
    Accepted formats:
    - `JavaObject` of `net.minecraft.world.level.block.state.BlockState`
    """
    ...
  @staticmethod
  def get_block_entity(x: int|float|JavaObject, y: int|float|None = None, z: int|float|None = None) -> JavaObject:
    """
    Returnws the minecraft `net.minecraft.world.level.block.entity.BlockEntity` Java object from a position or coordinates.

    Accepted formats:
    - `x, y, z`: Individual numeric coordinates (float or int)
    - `JavaObject` of `net.minecraft.core.BlockPos` passed into x and y/z are left to None
    """
    ...
  @staticmethod
  def is_command_block_entity(block_entity: JavaObject) -> bool: ...
  @staticmethod
  def set_command_block_entity_command(command_block_entity: JavaObject, command: str) -> bool: ...
  @staticmethod
  def get_command_block_entity_command(command_block_entity: JavaObject) -> str | None: ...
  @staticmethod
  def get_command_block_entity_last_output(command_block_entity: JavaObject) -> str | None: ...
  @staticmethod
  def get_command_block_entity_mode(command_block_entity: JavaObject) -> str | None:
    """
    Returns SEQUENCE or AUTO or REDSTONE
    (Sequence being the CHAIN Command Block)
    """
    ...
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
  @staticmethod
  def set_private_field(instance, pretty_field_name, value) -> bool: ...
  @staticmethod
  def get_declared_method_accessible(instance, pretty_method_name): ...
  @staticmethod
  def invoke_private_method(instance, pretty_method_name, *args): ...
  @staticmethod
  def is_instance_of(instance: JavaObject, class_name: str) -> bool: ...
class ItemsHelper(PyJinnProxy):  
  @staticmethod
  def get_item_id(item: JavaObject | str | int) -> str | None:
    """
    Get the item ID (namespace identifier) for an item.
    """
    ...

  @staticmethod
  def get_numeric_id(item: JavaObject | str | int) -> int:
    """
    Get the numeric registry ID for an item.
    """
    ...

  @staticmethod
  def get_display_name(item: JavaObject | str | int, use_custom_name: bool = False) -> str | None:
    """
    Get the display name of an item or item stack.

    Args:
    - `use_custom_name` (bool): If `True`, returns the custom hover name (e.g, from an anvil). If `False`, returns the default display name.
    """
    ...

  @staticmethod
  def get_count(item: JavaObject | str | int) -> int: ...

  @staticmethod
  def get_max_stack_size(item: JavaObject | str | int) -> int: ...

  @staticmethod
  def get_item_stack_java_object(item: JavaObject | str | int) -> JavaObject:
    """
    Get the underlying ItemStack JavaObject (`net.minecraft.world.item.ItemStack`).
    """
    ...

  @staticmethod
  def get_item_java_object(item: JavaObject | str | int) -> JavaObject:
    """
    Get the underlying Item JavaObject (`net.minecraft.world.item.Item`).
    """
    ...

  @staticmethod
  def get_json(item: JavaObject | str | int) -> str:
    """
    Get the full serialized item stack as a JSON string
    """
    ...

  @staticmethod
  def get_components(item: JavaObject | str | int) -> str:
    """
    Get only the `components` field from an item stack as a JSON string.
    """
    ...


class ContainerHelper(PyJinnProxy): 
  @staticmethod
  def enchantment_table_get_enchant_info(enchantment_apply_type) -> EnchantmentInfo|None:
    """
    Returns info about the enchant buttons in the opened enchantment table container

    Args:
        - `enchantment_apply_type` (`str`): top, middle, bottom
    """
    ...
  @staticmethod
  def enchantment_table_apply_enchant(enchantment_apply_type) -> bool:
    """
    Clicks the enchantment button in the opened enchantment table container

    Args:
        - `enchantment_apply_type` (`str`): top, middle, bottom
    """
    ...

  @staticmethod
  def get_container() -> JavaObject | None: ...
  @staticmethod
  def get_container_class_name() -> str:
    """
    Get the runtime mapped class name of the current container.
    """
    ...

  @staticmethod
  def get_container_id() -> int:
    """
    Get the current container ID. Returns `-1` if no container open.
    """
    ...

  @staticmethod
  def get_container_slot(slot: int) -> ItemStack | None:
    """
    Get the item stack at a container slot.
    """
    ...

  @staticmethod
  def get_inventory_slot(slot: int) -> ItemStack | None:
    """
    Get the item stack at an inventory slot
    """
    ...

  @staticmethod
  def get_item_stack_by_inventory_slot(slot: int) -> JavaObject | None:
    """
    Alias for `get_inventory_slot()`.
    """
    ...

  @staticmethod
  def get_item_stack_by_container_slot(slot: int) -> JavaObject | None:
    """
    Alias for `get_container_slot()`.
    """
    ...

  @staticmethod
  def container_find_item_id(item_id: str) -> list[JavaObject]:
    """
    Find all item stacks in container matching the given item ID.
    """
    ...

  @staticmethod
  def inventory_find_item_id(item_id: str) -> list[JavaObject]:
    """
    Find all item stacks in inventory matching the given item ID.
    """
    ...

  @staticmethod
  def raw_click(slot: int, button_or_slot: int = 0, click_type: str | None = ...) -> bool:
    """
    Raw click operation on a slot. For advanced container manipulation.

    Args:
    - `slot` (int): Slot to click
    - `button_or_slot` (int): Mouse button (0=left, 1=right) or drag slot / slot_b
    - `click_type` (str|JavaObject): Click type (PICKUP, QUICK_MOVE, SWAP, CLONE, THROW, QUICK_CRAFT, PICKUP_ALL)

    Returns: `True` if click succeeded, `False` otherwise
    """
    ...

  @staticmethod
  def click_slot(slot: int, button: int = 0) -> bool:
    """
    Click a slot with left (0) or right (1) mouse button.
    """
    ...

  @staticmethod
  def shift_click_slot(slot: int) -> bool:
    """
    Shift-click a slot (quick move).
    """
    ...

  @staticmethod
  def click_swap_with_hotbar(slot: int, hotbar_slot: int) -> bool: ...

  @staticmethod
  def pickup_swap_container(slot_a: int, slot_b: int) -> bool: ...

  @staticmethod
  def get_inventory_selected_hotbar_slot() -> int:
    """
    Get the currently selected hotbar slot (0-8).
    """
    ...

  @staticmethod
  def get_inventory_free_slot() -> int | None:
    """
    Get the first empty slot in inventory. Returns `None` if inventory full.
    """
    ...
  @staticmethod
  def get_slot_screen_position(slot: int) -> Vec2 | None:
    """
    Get the screen-space position for a container slot so you can move the cursor manually.
    """
    ...
  @staticmethod
  def get_container_layout() -> ContainerLayout | None:
    """
    Return a python layout object for the currently open container.
    """
    ...

class FishingHelper(PyJinnProxy):
  @staticmethod
  def is_holding_rod() -> bool:
    """
    Check if player is holding a fishing rod.
    """
    ...

  @staticmethod
  def is_casted() -> bool: ...

  @staticmethod
  def is_biting() -> bool | None:
    """
    Check if a fish is biting. Returns `None` if no hook in water.
    """
    ...

  @staticmethod
  def is_open_water() -> bool | None: ...

  @staticmethod
  def get_hooked_entity() -> Any: ...

  @staticmethod
  def get_time_until_lured() -> int | None:
    """
    Get ticks until a fish is lured. Returns `None` if no hook in water.
    """
    ...

  @staticmethod
  def get_time_until_hooked() -> int | None:
    """
    Get ticks until a fish is hooked (after being lured). Returns `None` if no hook in water.
    """
    ...

  @staticmethod
  def use_rod() -> bool: ...


class ContainerBounds:
  left: int
  top: int
  width: int
  height: int

class ScreenHelper(PyJinnProxy):
  @staticmethod
  def set_current_screen(screen: JavaObject) -> None:
    """
    Open a screen.
    """
    ...

  @staticmethod
  def get_anvil_cost_required() -> int: ...

  @staticmethod
  def get_current_screen() -> JavaObject | None: ...

  @staticmethod
  def get_current_screen_class_name() -> str: ...
  
  @staticmethod
  def get_container_bounds() -> ContainerBounds | None:
    """
    Returns the bounds (`left`, `top`, `width`, `height`) of the container background if the current screen is a container screen.
    """
    ...

  @staticmethod
  def close_current_screen(with_close_container_packet: bool = True) -> None:
    """
    Close the current screen.

    Args:
    - `with_close_container_packet` (bool): If `True`, sends close container packet to server (default)
    """
    ...

  @staticmethod
  def open_pause_screen() -> None: ...

  @staticmethod
  def open_inventory_screen() -> None: ...

  @staticmethod
  def open_alert_screen(title_text: str, message_text: str, ok_button_text: str = "OK"):
    """
    Shows an alert screen
    """
    ...

  @staticmethod
  def show_toast(title: str, desc: str, display_time: float = 5000.0): ...
  
  @staticmethod
  def set_anvil_screen_text(text: str) -> bool: ...

  @staticmethod
  def is_any_toast_showing() -> bool: ...

class WidgetScreenHelper(PyJinnProxy):
  @staticmethod
  def get_widgets() -> List[GuiWidget] | None:
    """
    Returns the list of widgets on the current screen wrapped in `GuiWidget` objects.
    """
    ...
  @staticmethod
  def click_widget(widget: GuiWidget | JavaObject) -> bool:
    """
    Simulates a mouse click at the center of the specified widget.
    """
    ...
  @staticmethod
  def click_at(x: float, y: float, button: int = 0) -> bool:
    """
    Simulates a mouse click at the specified GUI coordinates on the current screen.
    """
    ...
  @staticmethod
  def get_renderables() -> List[GuiWidget | JavaObject] | None:
    """
    Returns the list of raw renderable elements on the current screen.
    """
    ...
  @staticmethod
  def get_widget_by_message(text: str, match_case: bool = False) -> GuiWidget | None:
    """
    Finds a widget whose message contains the specified text.
    """
    ...

class ClientHelper(PyJinnProxy):
  @staticmethod
  def disconnect(str: str = "Disconnected by Minescript") -> None: ...

  @staticmethod
  def get_level_data() -> ClientLevelData: ...

  @staticmethod
  def get_fps() -> int: ...

  @staticmethod
  def get_camera_position() -> Vector3f: ...
  @staticmethod
  def get_camera_block_position() -> Vector3f: ...

  @staticmethod
  def get_camera_type() -> str:
    """
    FIRST_PERSON, THIRD_PERSON_BACK, THIRD_PERSON_FRONT
    """
    ...
    
  @staticmethod
  def narrate_text(text: str): ...


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
  @staticmethod
  def random_uuid() -> str: ...

class PlayerHelper(PyJinnProxy):
  @staticmethod
  def get_food_info() -> FoodInfo | None:
    """
    Returns the player's food, saturation, and exhaustion levels.
    """
    ...

  @staticmethod
  def get_gamemode() -> str:
    """
    `adventure`, `survival`, `creative`, or `spectator`
    """
    ...

  @staticmethod
  def get_experience() -> int: ...

  @staticmethod
  def get_level() -> int: ...

class RegistryHelper(PyJinnProxy):
  BuiltInRegistries: JavaObject
  Registries: JavaObject

  @staticmethod
  def get_by_id(registry: JavaObject, identifier: str) -> JavaObject | None:
    """
    Gets an object from the specified registry by its identifier string (e.g, `minecraft:diamond`)
    """
    ...
  @staticmethod
  def get_id(registry: JavaObject, value: JavaObject) -> str | None:
    """
    Gets the full identifier string (e.g, `minecraft:stone`) for a value in a registry
    """
    ...
  @staticmethod
  def get_registry_path(registry: JavaObject, value: JavaObject) -> str | None:
    """
    Gets only the path part of the identifier (e.g, `stone`) for a value in a registry
    """
    ...
  @staticmethod
  def get_all_ids(registry: JavaObject) -> List[str]:
    """
    Returns a list of all identifier strings in the given registry
    """
    ...
  @staticmethod
  def get_registry(registry_key: JavaObject) -> JavaObject:
    """
    Returns the registry object for the given registry key. e.g, `RegistryHelper.Registries.BLOCK`
    """
    ...
  @staticmethod
  def get_holder_by_numeric_id(registry_key: JavaObject, numeric_id: int) -> JavaObject | None: ...

class Vec3:
  x: float
  y: float
  z: float

class Vec2:
  def __init__(self, x: float, y: float) -> None: ...
  x: float
  y: float
  
class WindowSize:
  width: float
  height: float
  
class MerchantHelper(PyJinnProxy):
  @staticmethod
  def is_container_merchant() -> bool: ...
  @staticmethod
  def get_offers_json() -> str | None:
    """
    Example return
    # [{"buy":{"id":"minecraft:wheat","count":20},"sell":{"id":"minecraft:emerald","count":1},"maxUses":16,"priceMultiplier":0.05,"xp":2},{"buy":{"id":"minecraft:beetroot","count":15},"sell":{"id":"minecraft:emerald","count":1},"maxUses":16,"priceMultiplier":0.05,"xp":2}]
    """
    ...
  @staticmethod
  def set_selected_trade_index(index: int) -> bool | None:
    """
    Automatically puts in the correct items from your inventory into the slots if possible
    """
    ...
  @staticmethod
  def get_xp() -> int | None: ...
  @staticmethod
  def get_total_xp_needed_for_level_up() -> int | None: ...
  @staticmethod
  def get_level() -> int | None: ...