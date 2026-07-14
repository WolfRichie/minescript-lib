
- [`FishingHelper`](#fishinghelper)
  - [is\_holding\_rod() -\> bool](#is_holding_rod---bool)
  - [is\_casted() -\> bool](#is_casted---bool)
  - [is\_biting() -\> bool](#is_biting---bool)
  - [is\_open\_water() -\> bool](#is_open_water---bool)
  - [get\_hooked\_entity() -\> Any](#get_hooked_entity---any)
  - [get\_time\_until\_lured() -\> int](#get_time_until_lured---int)
  - [get\_time\_until\_hooked() -\> int](#get_time_until_hooked---int)
  - [use\_rod() -\> bool](#use_rod---bool)
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
  - [get\_container\_id() -\> int](#get_container_id---int)
  - [get\_container\_class\_name() -\> str](#get_container_class_name---str)
  - [container\_get\_slot(slot) -\> ItemStack](#container_get_slotslot---itemstack)
  - [raw\_click(slot, button\_or\_slot = 0, click\_type = None) -\> bool](#raw_clickslot-button_or_slot--0-click_type--none---bool)
  - [click\_slot(slot, button = 0) -\> bool](#click_slotslot-button--0---bool)
  - [shift\_click\_slot(slot) -\> bool](#shift_click_slotslot---bool)
  - [click\_swap\_with\_hotbar(slot, hotbar\_slot) -\> bool](#click_swap_with_hotbarslot-hotbar_slot---bool)
  - [pickup\_swap\_container(slot\_a, slot\_b) -\> bool](#pickup_swap_containerslot_a-slot_b---bool)
  - [crafting\_place\_slot(slot, crafting\_slot, count = 1) -\> ItemStack](#crafting_place_slotslot-crafting_slot-count--1---itemstack)
  - [crafting\_shift\_click\_result() -\> ItemStack](#crafting_shift_click_result---itemstack)
- [`ReflectionHelper`](#reflectionhelper)
  - [get\_private\_field(clazz: JavaClass, pretty\_field\_name: str) -\> Any](#get_private_fieldclazz-javaclass-pretty_field_name-str---any)

## `FishingHelper`

### is_holding_rod() -> bool
### is_casted() -> bool
### is_biting() -> bool
### is_open_water() -> bool
### get_hooked_entity() -> Any
### get_time_until_lured() -> int
### get_time_until_hooked() -> int
### use_rod() -> bool

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

### get_container_id() -> int
  Gets current container id.
  Returns: Container id, or `-1` if unavailable.
  Example: `container_id = ContainerHelper.get_container_id()`

### get_container_class_name() -> str
  Gets mapped class name for the active container menu.
  Returns: Container class name, or empty string when unavailable.
  Example: `container_name = ContainerHelper.get_container_class_name()`

### container_get_slot(slot) -> ItemStack
  Looks up an item entry by slot from `container_get_items()`.
  Returns: StackItem or `None` if not found.
  Example: `result_item = ContainerHelper.container_get_slot(0)`

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

---

## `ReflectionHelper`
Methods for accessing to internal/private Java fields.

### get_private_field(clazz: JavaClass, pretty_field_name: str) -> Any
  Reads a private field value from the given Java Class instance using mappings.
  Returns: Reflected field value.
  Example: `ReflectionHelper.get_private_field(hook, "biting")`
