- [Usage](#usage)
  - [`FishingHelper`](#fishinghelper)
    - [is\_holding\_rod() -\> bool](#is_holding_rod---bool)
    - [is\_casted() -\> bool](#is_casted---bool)
    - [is\_biting() -\> bool](#is_biting---bool)
    - [is\_open\_water() -\> bool | None](#is_open_water---bool--none)
    - [get\_hooked\_entity() -\> Any](#get_hooked_entity---any)
    - [get\_time\_until\_lured() -\> int | None](#get_time_until_lured---int--none)
    - [get\_time\_until\_hooked() -\> int | None](#get_time_until_hooked---int--none)
    - [use\_rod() -\> bool](#use_rod---bool)
  - [`ItemsHelper`](#itemshelper)
    - [get\_item\_by\_item\_id(item\_id: str) -\> JavaObject](#get_item_by_item_iditem_id-str---javaobject)
    - [get\_item\_stack\_by\_item\_id(item\_id: str) -\> JavaObject](#get_item_stack_by_item_iditem_id-str---javaobject)
    - [get\_item\_numeric\_id(item: JavaObject) -\> int:](#get_item_numeric_iditem-javaobject---int)
    - [get\_item\_by\_numeric\_id(id: int) -\> JavaObject:](#get_item_by_numeric_idid-int---javaobject)
    - [get\_display\_name\_by\_item\_id(item\_id: str) -\> str | None:](#get_display_name_by_item_iditem_id-str---str--none)
    - [get\_display\_name\_by\_item(item: JavaObject, use\_custom\_name=False) -\> str | None:](#get_display_name_by_itemitem-javaobject-use_custom_namefalse---str--none)
    - [get\_display\_name\_by\_item\_stack(item: JavaObject, use\_custom\_name=False) -\> str | None:](#get_display_name_by_item_stackitem-javaobject-use_custom_namefalse---str--none)
  - [`MappingsHelper`](#mappingshelper)
    - [get\_runtime\_class\_name(pretty\_class\_name: str) -\> str](#get_runtime_class_namepretty_class_name-str---str)
    - [get\_pretty\_class\_name(runtime\_class\_name: str) -\> str](#get_pretty_class_nameruntime_class_name-str---str)
    - [get\_runtime\_field\_name(clazz: JavaClass, pretty\_field\_name: str) -\> str](#get_runtime_field_nameclazz-javaclass-pretty_field_name-str---str)
    - [get\_pretty\_field\_names(clazz: JavaClass) -\> JavaSet\[str\]](#get_pretty_field_namesclazz-javaclass---javasetstr)
    - [get\_runtime\_method\_names(clazz: JavaClass, pretty\_method\_name: str) -\> JavaSet\[str\]](#get_runtime_method_namesclazz-javaclass-pretty_method_name-str---javasetstr)
    - [get\_pretty\_method\_names(clazz: JavaClass) -\> JavaSet\[str\]](#get_pretty_method_namesclazz-javaclass---javasetstr)
  - [`CraftingLayout`](#craftinglayout)
    - [CraftingLayout(container\_name, grid\_slots, result\_slot)](#craftinglayoutcontainer_name-grid_slots-result_slot)
  - [`ContainerHelper`](#containerhelper)
    - [crafting\_get\_layout() -\> CraftingLayout](#crafting_get_layout---craftinglayout)
    - [crafting\_get\_grid\_size() -\> int](#crafting_get_grid_size---int)
    - [crafting\_place\_slot(slot, crafting\_slot, count = 1) -\> ItemStack](#crafting_place_slotslot-crafting_slot-count--1---itemstack)
    - [crafting\_shift\_click\_result() -\> ItemStack](#crafting_shift_click_result---itemstack)
    - [get\_container\_id() -\> int](#get_container_id---int)
    - [get\_container\_class\_name() -\> str](#get_container_class_name---str)
    - [get\_container\_slot(slot) -\> ItemStack](#get_container_slotslot---itemstack)
    - [get\_inventory\_slot(slot) -\> ItemStack](#get_inventory_slotslot---itemstack)
    - [container\_find\_item\_id(item\_id: str) -\> List\[ItemStack\]](#container_find_item_iditem_id-str---listitemstack)
    - [inventory\_find\_item\_id(item\_id: str) -\> List\[ItemStack\]](#inventory_find_item_iditem_id-str---listitemstack)
    - [get\_item\_stack\_by\_inventory\_slot(slot: int) -\> JavaObject](#get_item_stack_by_inventory_slotslot-int---javaobject)
    - [get\_item\_stack\_by\_container\_slot(slot: int) -\> JavaObject:](#get_item_stack_by_container_slotslot-int---javaobject)
    - [raw\_click(slot, button\_or\_slot = 0, click\_type = None) -\> bool](#raw_clickslot-button_or_slot--0-click_type--none---bool)
    - [click\_slot(slot, button = 0) -\> bool](#click_slotslot-button--0---bool)
    - [shift\_click\_slot(slot) -\> bool](#shift_click_slotslot---bool)
    - [click\_swap\_with\_hotbar(slot, hotbar\_slot) -\> bool](#click_swap_with_hotbarslot-hotbar_slot---bool)
    - [pickup\_swap\_container(slot\_a, slot\_b) -\> bool](#pickup_swap_containerslot_a-slot_b---bool)
  - [`ReflectionHelper`](#reflectionhelper)
    - [get\_private\_field(clazz: JavaClass, pretty\_field\_name: str) -\> Any](#get_private_fieldclazz-javaclass-pretty_field_name-str---any)

# Usage
See examples/

## `FishingHelper`

### is_holding_rod() -> bool
### is_casted() -> bool
### is_biting() -> bool
### is_open_water() -> bool | None
### get_hooked_entity() -> Any
### get_time_until_lured() -> int | None
### get_time_until_hooked() -> int | None
### use_rod() -> bool

---

## `ItemsHelper`

### get_item_by_item_id(item_id: str) -> JavaObject
  Example: `ItemsHelper.get_item_by_item_id("fishing_rod")`
### get_item_stack_by_item_id(item_id: str) -> JavaObject
  Example: `ItemsHelper.get_item_by_item_id("fishing_rod").getRarity()`

### get_item_numeric_id(item: JavaObject) -> int:
### get_item_by_numeric_id(id: int) -> JavaObject:

### get_display_name_by_item_id(item_id: str) -> str | None: 
  Example: `ItemsHelper.get_display_name_by_item_id("fishing_rod")` -> `[Fishing Rod]`

### get_display_name_by_item(item: JavaObject, use_custom_name=False) -> str | None:
  Args:
  - `item_id` (str): The item instance (of net.minecraft.world.item.Item)
  - `use_custom_name` (bool): If `True`, returns the hover name (custom name) instead of the default display name.
  
  Example:
  ```python
  item_instance = ...
  ItemsHelper.get_display_name_by_item(item_instance, True) # -> "cool item renamed at an anvil"
  ItemsHelper.get_display_name_by_item(item_instance, False) # -> "Iron Sword"
  ```

### get_display_name_by_item_stack(item: JavaObject, use_custom_name=False) -> str | None:
  Args:
  - `item_id` (str): The item instance (of net.minecraft.world.item.ItemStack)
  - `use_custom_name` (bool): If `True`, returns the hover name (custom name) instead of the default display name.
  
  Example:
  ```python
  item_stack_instance = ContainerHelper.get_item_stack_by_container_slot(27)
  ItemsHelper.get_display_name_by_item_stack(item_stack_instance, True) # -> "cool item renamed at an anvil"
  ```
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

## `CraftingLayout`
Object that stores crafting layout metadata for the current container.

### CraftingLayout(container_name, grid_slots, result_slot)
  Creates a layout object for crafting interactions.
  Stores:
  - `container_name`: Mapped runtime container class name.
  - `grid_slots`: List of valid crafting slot ids for the active menu.
  - `grid_size`: Precomputed length of `grid_slots`.
  - `result_slot`: Slot id containing crafting output.

  Example: `layout = ContainerHelper.crafting_get_layout()`

## `ContainerHelper`

### crafting_get_layout() -> CraftingLayout
  Returns the active crafting layout object for the current container.
  Returns: `CraftingLayout` with `container_name`, `grid_slots`, `grid_size`, and `result_slot`.

  Example: `layout = ContainerHelper.crafting_get_layout()`

### crafting_get_grid_size() -> int
  Gets crafting grid size for the current layout.
  Returns: `4`, `9`, or `0` when crafting is not supported by the open container.

  Example: `grid_size = ContainerHelper.crafting_get_grid_size()`


### crafting_place_slot(slot, crafting_slot, count = 1) -> ItemStack
  Places one item at a time from `slot` into `crafting_slot` repeatedly.
  `crafting_slot` must be in `crafting_get_layout().grid_slots`.
  Returns:
  - ItemStack object from `result_slot` after placement.
  - `False` when layout is unsupported, slot is invalid, count is not positive, or click fails.
  
  Example: `ContainerHelper.crafting_place_slot(15, 4, 2)`

### crafting_shift_click_result() -> ItemStack
  Shift-clicks the current crafting `result_slot`.
  Returns:
  - Result slot item object that was present before click.
  - `None` if result slot is empty.
  - `False` when layout is unsupported or click fails.

  Example: `crafted_item = ContainerHelper.crafting_shift_click_result()`


### get_container_id() -> int
  Gets current container id.
  Returns: Container id, or `-1` if unavailable.

  Example: `container_id = ContainerHelper.get_container_id()`

### get_container_class_name() -> str
  Gets mapped class name for the active container menu.
  Returns: Container class name, or empty string when unavailable.

  Example: `container_name = ContainerHelper.get_container_class_name()`

### get_container_slot(slot) -> ItemStack
  Looks up an item entry by slot from `container_get_items()`.
  Returns: ItemStack or `None` if not found.

  Example: `result_item = ContainerHelper.get_container_slot(0)`

### get_inventory_slot(slot) -> ItemStack
### container_find_item_id(item_id: str) -> List[ItemStack]
### inventory_find_item_id(item_id: str) -> List[ItemStack]
### get_item_stack_by_inventory_slot(slot: int) -> JavaObject
### get_item_stack_by_container_slot(slot: int) -> JavaObject:

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
