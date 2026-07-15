- [Usage](#usage)
  - [`FishingHelper`](#fishinghelper)
    - [is\_holding\_rod() -\> bool](#is_holding_rod---bool)
    - [is\_casted() -\> bool](#is_casted---bool)
    - [is\_biting() -\> bool | None](#is_biting---bool--none)
    - [is\_open\_water() -\> bool | None](#is_open_water---bool--none)
    - [get\_hooked\_entity() -\> Any](#get_hooked_entity---any)
    - [get\_time\_until\_lured() -\> int | None](#get_time_until_lured---int--none)
    - [get\_time\_until\_hooked() -\> int | None](#get_time_until_hooked---int--none)
    - [use\_rod() -\> bool](#use_rod---bool)
  - [`ItemStackInstance`](#itemstackinstance)
    - [get\_display\_name(use\_custom\_name=False) -\> str | None](#get_display_nameuse_custom_namefalse---str--none)
    - [get\_item\_id() -\> str | None](#get_item_id---str--none)
    - [get\_item() -\> ItemInstance](#get_item---iteminstance)
    - [get\_count() -\> int](#get_count---int)
    - [get\_max\_stack\_size() -\> int](#get_max_stack_size---int)
    - [get\_item\_java\_object() -\> JavaObject](#get_item_java_object---javaobject)
    - [get\_java\_object() -\> JavaObject](#get_java_object---javaobject)
  - [`ItemInstance`](#iteminstance)
    - [get\_item\_id() -\> str | None](#get_item_id---str--none-1)
    - [get\_numeric\_id() -\> int](#get_numeric_id---int)
    - [by\_numeric\_id(id: int) -\> ItemInstance](#by_numeric_idid-int---iteminstance)
    - [get\_display\_name(use\_custom\_name=False) -\> str | None](#get_display_nameuse_custom_namefalse---str--none-1)
    - [get\_count() -\> int](#get_count---int-1)
    - [get\_max\_stack\_size() -\> int](#get_max_stack_size---int-1)
    - [get\_item\_stack() -\> ItemStackInstance](#get_item_stack---itemstackinstance)
    - [get\_item\_stack\_java\_object() -\> JavaObject:](#get_item_stack_java_object---javaobject)
    - [get\_java\_object() -\> JavaObject](#get_java_object---javaobject-1)
  - [`MappingsHelper`](#mappingshelper)
    - [get\_runtime\_class\_name(pretty\_class\_name: str) -\> str](#get_runtime_class_namepretty_class_name-str---str)
    - [get\_pretty\_class\_name(runtime\_class\_name: str) -\> str](#get_pretty_class_nameruntime_class_name-str---str)
    - [get\_runtime\_field\_name(clazz: JavaClass, pretty\_field\_name: str) -\> str](#get_runtime_field_nameclazz-javaclass-pretty_field_name-str---str)
    - [get\_pretty\_field\_names(clazz: JavaClass) -\> JavaSet\[str\]](#get_pretty_field_namesclazz-javaclass---javasetstr)
    - [get\_runtime\_method\_names(clazz: JavaClass, pretty\_method\_name: str) -\> JavaSet\[str\]](#get_runtime_method_namesclazz-javaclass-pretty_method_name-str---javasetstr)
    - [get\_pretty\_method\_names(clazz: JavaClass) -\> JavaSet\[str\]](#get_pretty_method_namesclazz-javaclass---javasetstr)
  - [`ContainerHelper`](#containerhelper)
    - [crafting\_get\_layout() -\> CraftingLayout](#crafting_get_layout---craftinglayout)
      - [`CraftingLayout`](#craftinglayout)
    - [crafting\_get\_grid\_size() -\> int](#crafting_get_grid_size---int)
    - [crafting\_place\_slot(slot, crafting\_slot, count = 1) -\> ItemStackInstance | bool | None](#crafting_place_slotslot-crafting_slot-count--1---itemstackinstance--bool--none)
    - [crafting\_shift\_click\_result() -\> ItemStackInstance | bool | None](#crafting_shift_click_result---itemstackinstance--bool--none)
    - [get\_container\_id() -\> int](#get_container_id---int)
    - [get\_container\_class\_name() -\> str](#get_container_class_name---str)
    - [get\_container\_slot(slot) -\> ItemStackInstance | None](#get_container_slotslot---itemstackinstance--none)
    - [get\_inventory\_slot(slot) -\> ItemStackInstance | None](#get_inventory_slotslot---itemstackinstance--none)
    - [container\_find\_item\_id(item\_id: str) -\> list\[ItemStackInstance\]](#container_find_item_iditem_id-str---listitemstackinstance)
    - [inventory\_find\_item\_id(item\_id: str) -\> list\[ItemStackInstance\]](#inventory_find_item_iditem_id-str---listitemstackinstance)
    - [get\_item\_stack\_by\_inventory\_slot(slot: int) -\> ItemStackInstance | None](#get_item_stack_by_inventory_slotslot-int---itemstackinstance--none)
    - [get\_item\_stack\_by\_container\_slot(slot: int) -\> ItemStackInstance | None:](#get_item_stack_by_container_slotslot-int---itemstackinstance--none)
    - [raw\_click(slot, button\_or\_slot = 0, click\_type = None) -\> bool](#raw_clickslot-button_or_slot--0-click_type--none---bool)
    - [click\_slot(slot, button = 0) -\> bool](#click_slotslot-button--0---bool)
    - [shift\_click\_slot(slot) -\> bool](#shift_click_slotslot---bool)
    - [click\_swap\_with\_hotbar(slot, hotbar\_slot) -\> bool](#click_swap_with_hotbarslot-hotbar_slot---bool)
    - [pickup\_swap\_container(slot\_a, slot\_b) -\> bool](#pickup_swap_containerslot_a-slot_b---bool)
  - [`ReflectionHelper`](#reflectionhelper)
    - [get\_private\_field(clazz: JavaClass, pretty\_field\_name: str) -\> Any](#get_private_fieldclazz-javaclass-pretty_field_name-str---any)
  - [`ClientHelper`](#clienthelper)
    - [set\_current\_screen(screen: JavaObject) -\> None:](#set_current_screenscreen-javaobject---none)
    - [get\_current\_screen() -\> JavaObject | None](#get_current_screen---javaobject--none)
    - [get\_current\_screen\_class\_name() -\> str](#get_current_screen_class_name---str)
    - [close\_current\_screen() -\> None](#close_current_screen---none)
    - [open\_pause\_screen() -\> None](#open_pause_screen---none)
    - [open\_inventory\_screen() -\> None](#open_inventory_screen---none)
    - [disconnect(str = "Disconnected by Minescript") -\> None](#disconnectstr--disconnected-by-minescript---none)
    - [get\_level\_data() -\> ClientLevelData](#get_level_data---clientleveldata)
      - [`ClientLevelData`](#clientleveldata)
    - [get\_fps() -\> int](#get_fps---int)
    - [get\_camera\_position() -\> Vector3f](#get_camera_position---vector3f)
    - [get\_camera\_type() -\> str:](#get_camera_type---str)
  - [FIRST\_PERSON or THIRD\_PERSON\_BACK or THIRD\_PERSON\_FRONT](#first_person-or-third_person_back-or-third_person_front)
  - [`UtilHelper`](#utilhelper)
    - [get\_class\_name(obj: JavaObject) -\> str:](#get_class_nameobj-javaobject---str)
    - [get\_clipboard() -\> str:](#get_clipboard---str)
    - [set\_clipboard(text: str) -\> None:](#set_clipboardtext-str---none)

# Usage
See examples/

## `FishingHelper`

### is_holding_rod() -> bool
### is_casted() -> bool
### is_biting() -> bool | None
### is_open_water() -> bool | None
### get_hooked_entity() -> Any
### get_time_until_lured() -> int | None
### get_time_until_hooked() -> int | None
### use_rod() -> bool

---

## `ItemStackInstance`

Wrapper class for JavaObject item stack objects. Returned by all `ContainerHelper` and `ItemInstance` methods that retrieve ItemstackInstance's NOT Itemstack dataclass's

You can construct it directly from either a  ``net.minecraft.world.item.ItemStack` JavaObject instance or an item id string:

```python
item = ItemStackInstance("fishing_rod")
```

### get_display_name(use_custom_name=False) -> str | None
  Gets the display name of the item stack.
  Args:
  - `use_custom_name` (bool): If `True`, returns the hover name (custom name) instead of the default display name.
  
  Returns:
  - Display name as string, or `None` if unavailable.
  
  Example:
  ```python
  item = ContainerHelper.get_item_stack_by_container_slot(27)
  if item:
      print(item.get_display_name())  # -> "Iron Sword"
      print(item.get_display_name(use_custom_name=True))  # -> "cool sword renamed at an anvil"
  ```

### get_item_id() -> str | None
  Returns the wrapped item id path, such as `fishing_rod`.

  Example:
  ```python
  print(ItemStackInstance("fishing_rod").get_item_id())  # -> "fishing_rod"
  ```

### get_item() -> ItemInstance
  Returns the wrapped `net.minecraft.world.item.Item` for the stack as an `ItemInstance`.

  Example:
  ```python
  item = ContainerHelper.get_item_stack_by_container_slot(27)
  if item:
      print(item.get_item().get_numeric_id())  # -> 69
  ```

### get_count() -> int
  Returns the current item count in the stack.

### get_max_stack_size() -> int
  Returns the maximum stack size for the wrapped item.

### get_item_java_object() -> JavaObject
  Returns the underlying `net.minecraft.world.item.Item` JavaObject for the stack.

### get_java_object() -> JavaObject
  Returns the underlying wrapped `net.minecraft.world.item.ItemStack` JavaObject.

---

## `ItemInstance`

Wrapper class for JavaObject `net.minecraft.world.item.Item` instances (as opposed to `ItemStackInstance`, which wraps `ItemStack`).

You can construct it directly from either a `net.minecraft.world.item.Item` JavaObject instance or an item id string:

```python
item = ItemInstance("fishing_rod")
```

### get_item_id() -> str | None
  Returns the wrapped item id path, such as `fishing_rod`.

  Example: `ItemInstance("fishing_rod").get_item_id()` -> `"fishing_rod"`

### get_numeric_id() -> int
  Returns the numeric registry id of the wrapped item.

### by_numeric_id(id: int) -> ItemInstance
  Static method. Constructs an `ItemInstance` from a numeric registry id.
  e.g `ItemInstance.by(69)`

### get_display_name(use_custom_name=False) -> str | None
  Args:
  - `use_custom_name` (bool): If `True`, returns the hover name (custom name) instead of the default display name.

  Example:
  ```python
  item = ItemInstance("fishing_rod")
  item.get_display_name() # -> "Fishing Rod"
  ```

### get_count() -> int
  Returns the count of the default item stack (normally `1`).

### get_max_stack_size() -> int
  Returns the maximum stack size for the wrapped item.

### get_item_stack() -> ItemStackInstance
  Returns a default `ItemStackInstance` (count 1, no NBT) for the wrapped item.

### get_item_stack_java_object() -> JavaObject:
  Returns the underlying wrapped `net.minecraft.world.item.ItemStack` JavaObject.

### get_java_object() -> JavaObject
  Returns the underlying wrapped `net.minecraft.world.item.Item` JavaObject.

---

## `MappingsHelper`

### get_runtime_class_name(pretty_class_name: str) -> str
  Resolves a mapped class name to its runtime class name.
  Returns: Runtime class name string.

  Example: `MappingsHelper.get_runtime_class_name("net.minecraft.client.Minecraft")`

### get_pretty_class_name(runtime_class_name: str) -> str
  Resolves a runtime class name to its mapped class name.
  Returns: Pretty class name string.

  Example: `MappingsHelper.get_pretty_class_name("net.minecraft.class_310")`

### get_runtime_field_name(clazz: JavaClass, pretty_field_name: str) -> str
  Resolves a mapped field name to the runtime field name for a class.
  Returns: Runtime field name string.

  Example: `MappingsHelper.get_runtime_field_name(minecraft.player.getClass(), "containerMenu")`

### get_pretty_field_names(clazz: JavaClass) -> JavaSet[str]
  Gets all mapped field names available for a class.
  Returns: Java set of pretty field names.

  Example: `MappingsHelper.get_pretty_field_names(minecraft.player.getClass())`

### get_runtime_method_names(clazz: JavaClass, pretty_method_name: str) -> JavaSet[str]
  Resolves a mapped method name to runtime method names for a class.
  Returns: Java set of runtime method names.

  Example: `MappingsHelper.get_runtime_method_names(minecraft.player.getClass(), "getInventory")`

### get_pretty_method_names(clazz: JavaClass) -> JavaSet[str]
  Gets all mapped method names available for a class.
  Returns: Java set of pretty method names.

  Example: `MappingsHelper.get_pretty_method_names(minecraft.player.getClass())`

  Example: `layout = ContainerHelper.crafting_get_layout()`

## `ContainerHelper`

### crafting_get_layout() -> CraftingLayout
  Returns the active crafting layout object for the current container.
  Returns: `CraftingLayout` with `container_name`, `grid_slots`, `grid_size`, and `result_slot`.

  Example: `layout = ContainerHelper.crafting_get_layout()`

#### `CraftingLayout`
Object that stores crafting layout metadata for the current container.
Stores:
  - `container_name` str: Mapped runtime container class name.
  - `grid_slots` List[int]: List of valid crafting slot ids for the active menu.
  - `grid_size` int: Precomputed length of `grid_slots`.
  - `result_slot` int: Slot id containing crafting output.


### crafting_get_grid_size() -> int
  Gets crafting grid size for the current layout.
  Returns: `4`, `9`, or `0` when crafting is not supported by the open container.

  Example: `grid_size = ContainerHelper.crafting_get_grid_size()`

### crafting_place_slot(slot, crafting_slot, count = 1) -> ItemStackInstance | bool | None
  Places one item at a time from `slot` into `crafting_slot` repeatedly.
  `crafting_slot` must be in `crafting_get_layout().grid_slots`.
  Returns:
  - `ItemStackInstance` object from `result_slot` after placement.
  - `False` when layout is unsupported, slot is invalid, count is not positive, or click fails.
  - `None` if result slot is empty after placement.
  
  Example: 
  ```python
  result = ContainerHelper.crafting_place_slot(15, 4, 2)
  if result and result is not False:
      print(result.get_display_name())
  ```

### crafting_shift_click_result() -> ItemStackInstance | bool | None
  Shift-clicks the current crafting `result_slot`.
  Returns:
  - `ItemStackInstance` object that was present in the result slot before click.
  - `None` if result slot is empty.
  - `False` when layout is unsupported or click fails.

  Example: 
  ```python
  crafted_item = ContainerHelper.crafting_shift_click_result()
  if crafted_item and crafted_item is not False:
      print(crafted_item.get_display_name())
  ```


### get_container_id() -> int
  Gets current container id.
  Returns: Container id, or `-1` if unavailable.

  Example: `container_id = ContainerHelper.get_container_id()`

### get_container_class_name() -> str
  Gets mapped class name for the active container menu.
  Returns: Container class name, or empty string when unavailable.

  Example: `container_name = ContainerHelper.get_container_class_name()`

### get_container_slot(slot) -> ItemStackInstance | None
  Looks up an item entry by slot from `container_get_items()`.
  Returns: `ItemStackInstance` or `None` if not found.

  Example: 
  ```python
  item = ContainerHelper.get_container_slot(0)
  if item:
      print(item.get_display_name())
  ```

### get_inventory_slot(slot) -> ItemStackInstance | None

### container_find_item_id(item_id: str) -> list[ItemStackInstance]
  Finds all items in the container matching the given item ID.
  Returns: List of `ItemStackInstance` objects.
  
  Example:
  ```python
  items = ContainerHelper.container_find_item_id("diamond_sword")
  for item in items:
      print(item.get_display_name())
  ```

### inventory_find_item_id(item_id: str) -> list[ItemStackInstance]
  Finds all items in the player inventory matching the given item ID.
  Returns: List of `ItemStackInstance` objects.

### get_item_stack_by_inventory_slot(slot: int) -> ItemStackInstance | None
  Returns the item at the given inventory slot wrapped in `ItemStackInstance`, or `None` if empty.
  
  Example:
  ```python
  item = ContainerHelper.get_item_stack_by_inventory_slot(0)
  if item:
      print(item.get_display_name(use_custom_name=True))
  ```

### get_item_stack_by_container_slot(slot: int) -> ItemStackInstance | None:
  Returns the item at the given container slot wrapped in `ItemStackInstance`, or `None` if empty.

### raw_click(slot, button_or_slot = 0, click_type = None) -> bool
  Sends a low-level inventory click to Minecraft.
  Returns: `True` when click is sent, `False` when no valid container id is available.

  Example: `ContainerHelper.raw_click(0, 0, "PICKUP")`

### click_slot(slot, button = 0) -> bool
  Performs a PICKUP click on a slot.
  Returns: `True`/`False` from `raw_click`.
  Example: `ContainerHelper.click_slot(13)`

### shift_click_slot(slot) -> bool
  Performs a QUICK_MOVE (shift-click) on a slot.
  Returns: `True`/`False` from `raw_click`.

  Example: `ContainerHelper.shift_click_slot(13)`

### click_swap_with_hotbar(slot, hotbar_slot) -> bool
  Swaps a slot with a hotbar slot via SWAP click.
  Returns: `True`/`False` from `raw_click`.

  Example: `ContainerHelper.click_swap_with_hotbar(13, 0)`

### pickup_swap_container(slot_a, slot_b) -> bool
  Swaps two slots using pickup sequence (A -> B -> A).
  Returns: `True` if all clicks succeed, `False` otherwise.

  Example: `ContainerHelper.pickup_swap_container(10, 11)`

---

## `ReflectionHelper`
Methods for accessing to internal/private Java fields.

### get_private_field(clazz: JavaClass, pretty_field_name: str) -> Any
  Reads a private field value from the given Java Class instance using mappings.
  Returns: Reflected field value.

  Example: `ReflectionHelper.get_private_field(hook, "biting")`

---

## `ClientHelper`

### set_current_screen(screen: JavaObject) -> None:
### get_current_screen() -> JavaObject | None
### get_current_screen_class_name() -> str
### close_current_screen() -> None
### open_pause_screen() -> None
### open_inventory_screen() -> None
### disconnect(str = "Disconnected by Minescript") -> None

### get_level_data() -> ClientLevelData

#### `ClientLevelData`
  Stores:
  - `hardcore` bool:
  - `is_flat` bool:
  - `game_time` int:
  - `day_time` int:
  - `raining` bool:
  - `difficulty` str:
  - `difficulty_locked` bool:

###  get_fps() -> int
###  get_camera_position() -> [Vector3f](https://minescript.net/docs#vector3f)

###  get_camera_type() -> str:

Returns:
  FIRST_PERSON or THIRD_PERSON_BACK or THIRD_PERSON_FRONT
---

## `UtilHelper`

### get_class_name(obj: JavaObject) -> str:
### get_clipboard() -> str:
### set_clipboard(text: str) -> None: