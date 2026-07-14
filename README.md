# Library API
# Usage
```python
from main import ContainerHelper, MappingsHelper, ReflectionHelper
```

## `MappingsHelper`
- **get_runtime_class_name(pretty_class_name: str) -> str**
  Resolves a mapped class name to its runtime class name.
  *Returns:* Runtime class name string.
  *Example:* `MappingsHelper.get_runtime_class_name("net.minecraft.client.Minecraft")`

- **get_pretty_class_name(runtime_class_name: str) -> str**
  Resolves a runtime class name to its mapped class name.
  *Returns:* Pretty class name string.
  *Example:* `MappingsHelper.get_pretty_class_name("minecraft_class_1707")`

- **get_runtime_field_name(clazz: JavaClass, pretty_field_name: str) -> str**
  Resolves a mapped field name to the runtime field name for a class.
  *Returns:* Runtime field name string.
  *Example:* `MappingsHelper.get_runtime_field_name(minecraft.player.getClass(), "containerMenu")`

- **get_pretty_field_names(clazz: JavaClass) -> JavaSet[str]**
  Gets all mapped field names available for a class.
  *Returns:* Java set of pretty field names.
  *Example:* `MappingsHelper.get_pretty_field_names(minecraft.player.getClass())`

- **get_runtime_method_names(clazz: JavaClass, pretty_method_name: str) -> JavaSet[str]**
  Resolves a mapped method name to runtime method names for a class.
  *Returns:* Java set of runtime method names.
  *Example:* `MappingsHelper.get_runtime_method_names(minecraft.player.getClass(), "getInventory")`

- **get_pretty_method_names(clazz: JavaClass) -> JavaSet[str]**
  Gets all mapped method names available for a class.
  *Returns:* Java set of pretty method names.
  *Example:* `MappingsHelper.get_pretty_method_names(minecraft.player.getClass())`

## `ReflectionHelper`
Methods for reflective access to internal/private Java fields.

- **get_private_field(instance, pretty_field_name: str, super_class: bool = False)**
  Reads a private field value from the given Java object instance using mappings.
  *Returns:* Reflected field value.
  *Example:* `N/A`

## `CraftingLayout`
Object that stores crafting layout metadata for the current container.

- **CraftingLayout(container_name, grid_slots, result_slot)**
  Creates a layout object for crafting interactions.
  *Stores:*
  - `container_name`: Mapped runtime container class name.
  - `grid_slots`: List of valid crafting slot ids for the active menu.
  - `grid_size`: Precomputed length of `grid_slots`.
  - `result_slot`: Slot id containing crafting output.
  *Example:* `layout = ContainerHelper.crafting_get_layout()`

## `ContainerHelper`
Methods for container interactions, slot clicks, and crafting operations.

- **crafting_get_layout() -> CraftingLayout**
  Returns the active crafting layout object for the current container.
  *Returns:* `CraftingLayout` with `container_name`, `grid_slots`, `grid_size`, and `result_slot`.
  *Example:* `layout = ContainerHelper.crafting_get_layout()`

- **crafting_get_grid_size() -> int**
  Gets crafting grid size for the current layout.
  *Returns:* `4`, `9`, or `0` when crafting is not supported by the open container.
  *Example:* `grid_size = ContainerHelper.crafting_get_grid_size()`

- **get_container_id() -> int**
  Gets current container id.
  *Returns:* Container id, or `-1` if unavailable.
  *Example:* `container_id = ContainerHelper.get_container_id()`

- **get_container_class_name() -> str**
  Gets mapped class name for the active container menu.
  *Returns:* Container class name, or empty string when unavailable.
  *Example:* `container_name = ContainerHelper.get_container_class_name()`

- **container_get_slot(slot)**
  Looks up an item entry by slot from `container_get_items()`.
  *Returns:* Slot item object, or `None` if not found.
  *Example:* `result_item = ContainerHelper.container_get_slot(0)`

- **raw_click(slot, button_or_slot = 0, click_type = None) -> bool**
  Sends a low-level inventory click to Minecraft.
  *Returns:* `True` when click is sent, `False` when no valid container id is available.
  *Example:* `ContainerHelper.raw_click(0, 0, "PICKUP")`

- **click_slot(slot, button = 0) -> bool**
  Performs a PICKUP click on a slot.
  *Returns:* `True`/`False` from `raw_click`.
  *Example:* `ContainerHelper.click_slot(13)`

- **shift_click_slot(slot) -> bool**
  Performs a QUICK_MOVE (shift-click) on a slot.
  *Returns:* `True`/`False` from `raw_click`.
  *Example:* `ContainerHelper.shift_click_slot(13)`

- **click_swap_with_hotbar(slot, hotbar_slot) -> bool**
  Swaps a slot with a hotbar slot via SWAP click.
  *Returns:* `True`/`False` from `raw_click`.
  *Example:* `ContainerHelper.click_swap_with_hotbar(13, 0)`

- **pickup_swap_container(slot_a, slot_b) -> bool**
  Swaps two slots using pickup sequence (A -> B -> A).
  *Returns:* `True` if all clicks succeed, `False` otherwise.
  *Example:* `ContainerHelper.pickup_swap_container(10, 11)`

- **crafting_place_slot(slot, crafting_slot, count = 1)**
  Places one item at a time from `slot` into `crafting_slot` repeatedly.
  `crafting_slot` must be in `crafting_get_layout().grid_slots`.
  *Returns:*
  - Slot item object from `result_slot` after placement.
  - `False` when layout is unsupported, slot is invalid, count is not positive, or click fails.
  *Example:* `ContainerHelper.crafting_place_slot(15, 4, 2)`

- **crafting_shift_click_result()**
  Shift-clicks the current crafting `result_slot`.
  *Returns:*
  - Result slot item object that was present before click.
  - `None` if result slot is empty.
  - `False` when layout is unsupported or click fails.
  *Example:* `crafted_item = ContainerHelper.crafting_shift_click_result()`
  Gets active player container menu object.
  *Example:* `menu = ContainerHelper._get_container()`

- **_resolve_click_type(click_type)**
  Resolves string click type names to enum values.
  *Example:* `click_type_enum = ContainerHelper._resolve_click_type("PICKUP")`

- **_validate_crafting_slot(crafting_slot) -> bool**
  Checks whether a crafting slot id exists in current layout `grid_slots`.
  *Example:* `is_valid_slot = ContainerHelper._validate_crafting_slot(4)`
