# Minescript Library

Developed in `Minecraft 1.21.11` using `minescript 5.0b11` with `Fabric API 0.141.4`

---
- [Minescript Library](#minescript-library)
  - [BlocksHelper](#blockshelper)
    - [get\_block\_pos(x, y=None, z=None) -\> JavaObject](#get_block_posx-ynone-znone---javaobject)
    - [get\_block\_entity(x:, y: int|float|None = None, z: int|float|None = None) -\> JavaObject:](#get_block_entityx-y-intfloatnone--none-z-intfloatnone--none---javaobject)
    - [set\_command\_block\_entity\_command(command\_block\_entity: JavaObject, command: str) -\> bool](#set_command_block_entity_commandcommand_block_entity-javaobject-command-str---bool)
    - [get\_command\_block\_entity\_command(command\_block\_entity: JavaObject) -\> str | None](#get_command_block_entity_commandcommand_block_entity-javaobject---str--none)
    - [get\_command\_block\_entity\_last\_output(command\_block\_entity: JavaObject) -\> str | None](#get_command_block_entity_last_outputcommand_block_entity-javaobject---str--none)
    - [get\_command\_block\_entity\_mode(command\_block\_entity: JavaObject) -\> str | None](#get_command_block_entity_modecommand_block_entity-javaobject---str--none)
    - [is\_command\_block\_entity\_conditions\_met(command\_block\_entity: JavaObject) -\> bool | Non](#is_command_block_entity_conditions_metcommand_block_entity-javaobject---bool--non)
    - [is\_command\_block\_entity\_powered(command\_block\_entity: JavaObject) -\> bool | None](#is_command_block_entity_poweredcommand_block_entity-javaobject---bool--none)
    - [is\_command\_block\_entity\_automatic(command\_block\_entity: JavaObject) -\> bool | None](#is_command_block_entity_automaticcommand_block_entity-javaobject---bool--none)
    - [get\_spawner\_block\_entity\_display\_entity\_id(jukebox\_block\_entity: spawner\_block\_entity) -\> str | None](#get_spawner_block_entity_display_entity_idjukebox_block_entity-spawner_block_entity---str--none)
  - [ItemsHelper](#itemshelper)
    - [get\_json(item) -\> str](#get_jsonitem---str)
    - [get\_components(item) -\> str](#get_componentsitem---str)
    - [get\_item\_id(item) -\> str | None](#get_item_iditem---str--none)
    - [get\_numeric\_id(item) -\> int](#get_numeric_iditem---int)
    - [get\_display\_name(item, use\_custom\_name=False) -\> str | None](#get_display_nameitem-use_custom_namefalse---str--none)
    - [get\_count(item) -\> int](#get_countitem---int)
    - [get\_max\_stack\_size(item) -\> int](#get_max_stack_sizeitem---int)
    - [get\_item\_stack\_java\_object(item) -\> JavaObject](#get_item_stack_java_objectitem---javaobject)
    - [get\_item\_java\_object(item) -\> JavaObject](#get_item_java_objectitem---javaobject)
  - [ContainerHelper](#containerhelper)
    - [crafting\_get\_layout() -\> CraftingLayout](#crafting_get_layout---craftinglayout)
    - [crafting\_get\_grid\_size() -\> int](#crafting_get_grid_size---int)
    - [crafting\_place\_slot(slot, crafting\_slot, count=1) -\> ItemStack | bool | None](#crafting_place_slotslot-crafting_slot-count1---itemstack--bool--none)
    - [crafting\_shift\_click\_result() -\> ItemStack | bool | None](#crafting_shift_click_result---itemstack--bool--none)
    - [get\_container\_id() -\> int](#get_container_id---int)
    - [get\_container\_class\_name() -\> str](#get_container_class_name---str)
    - [get\_container\_slot(slot) -\> ItemStack | None](#get_container_slotslot---itemstack--none)
    - [get\_inventory\_slot(slot) -\> ItemStack | None](#get_inventory_slotslot---itemstack--none)
    - [get\_item\_stack\_by\_inventory\_slot(slot) -\> JavaObject | None](#get_item_stack_by_inventory_slotslot---javaobject--none)
    - [get\_item\_stack\_by\_container\_slot(slot) -\> JavaObject | None](#get_item_stack_by_container_slotslot---javaobject--none)
    - [container\_find\_item\_id(item\_id) -\> list\[JavaObject\]](#container_find_item_iditem_id---listjavaobject)
    - [inventory\_find\_item\_id(item\_id) -\> list\[ItemStack\]](#inventory_find_item_iditem_id---listitemstack)
    - [get\_inventory\_free\_slot() -\> int | None](#get_inventory_free_slot---int--none)
    - [get\_inventory\_selected\_hotbar\_slot() -\> int](#get_inventory_selected_hotbar_slot---int)
    - [raw\_click(slot, button\_or\_slot=0, click\_type=None) -\> bool](#raw_clickslot-button_or_slot0-click_typenone---bool)
    - [click\_slot(slot, button=0) -\> bool](#click_slotslot-button0---bool)
    - [shift\_click\_slot(slot) -\> bool](#shift_click_slotslot---bool)
    - [click\_swap\_with\_hotbar(slot, hotbar\_slot) -\> bool](#click_swap_with_hotbarslot-hotbar_slot---bool)
    - [pickup\_swap\_container(slot\_a, slot\_b) -\> bool](#pickup_swap_containerslot_a-slot_b---bool)
  - [FishingHelper](#fishinghelper)
    - [is\_holding\_rod() -\> bool](#is_holding_rod---bool)
    - [is\_casted() -\> bool](#is_casted---bool)
    - [is\_biting() -\> bool | None](#is_biting---bool--none)
    - [is\_open\_water() -\> bool | None](#is_open_water---bool--none)
    - [get\_hooked\_entity() -\> JavaObject | None](#get_hooked_entity---javaobject--none)
    - [get\_time\_until\_lured() -\> int | None](#get_time_until_lured---int--none)
    - [get\_time\_until\_hooked() -\> int | None](#get_time_until_hooked---int--none)
    - [use\_rod() -\> bool](#use_rod---bool)
  - [ClientHelper](#clienthelper)
    - [get\_current\_screen() -\> JavaObject | None](#get_current_screen---javaobject--none)
    - [get\_current\_screen\_class\_name() -\> str](#get_current_screen_class_name---str)
    - [set\_current\_screen(screen) -\> None](#set_current_screenscreen---none)
    - [close\_current\_screen(with\_close\_container\_packet=True) -\> None](#close_current_screenwith_close_container_packettrue---none)
    - [open\_pause\_screen() -\> None](#open_pause_screen---none)
    - [open\_inventory\_screen() -\> None](#open_inventory_screen---none)
    - [disconnect(reason="Disconnected by Minescript") -\> None](#disconnectreasondisconnected-by-minescript---none)
    - [get\_fps() -\> int](#get_fps---int)
    - [get\_camera\_position() -\> Vector3f](#get_camera_position---vector3f)
    - [get\_camera\_type() -\> str](#get_camera_type---str)
    - [get\_level\_data() -\> ClientLevelData](#get_level_data---clientleveldata)
      - [ClientLevelData](#clientleveldata)
  - [MappingsHelper](#mappingshelper)
    - [get\_runtime\_class\_name(pretty\_class\_name) -\> str](#get_runtime_class_namepretty_class_name---str)
    - [get\_pretty\_class\_name(runtime\_class\_name) -\> str](#get_pretty_class_nameruntime_class_name---str)
    - [get\_runtime\_field\_name(clazz, pretty\_field\_name) -\> str](#get_runtime_field_nameclazz-pretty_field_name---str)
    - [get\_pretty\_field\_names(clazz) -\> JavaSet\[str\]](#get_pretty_field_namesclazz---javasetstr)
    - [get\_runtime\_method\_names(clazz, pretty\_method\_name) -\> JavaSet\[str\]](#get_runtime_method_namesclazz-pretty_method_name---javasetstr)
    - [get\_pretty\_method\_names(clazz) -\> JavaSet\[str\]](#get_pretty_method_namesclazz---javasetstr)
  - [ReflectionHelper](#reflectionhelper)
    - [get\_private\_field(clazz, pretty\_field\_name) -\> Any](#get_private_fieldclazz-pretty_field_name---any)
  - [UtilHelper](#utilhelper)
    - [get\_class\_name(obj) -\> str](#get_class_nameobj---str)
    - [get\_clipboard() -\> str](#get_clipboard---str)
    - [set\_clipboard(text) -\> None](#set_clipboardtext---none)
  - [RegistryHelper](#registryhelper)
    - [get\_by\_id(registry: JavaObject, identifier: str) -\> JavaObject](#get_by_idregistry-javaobject-identifier-str---javaobject)
    - [get\_by\_id(registry: JavaObject, identifier: str) -\> JavaObject](#get_by_idregistry-javaobject-identifier-str---javaobject-1)

---

## BlocksHelper

### get_block_pos(x, y=None, z=None) -> JavaObject

Create a Minecraft `net.minecraft.core.BlockPos` Java object from a position or coordinates.

Accepted formats:

- `x, y, z`: Individual numeric coordinates (float or int)

All float values are automatically converted to integers, they are simply allowed for compatability purposes

```
targeted_block_pos = minescript.player_get_targeted_block()
if targeted_block_pos is not None:
    x, y, z = targeted_block_pos.position
    block_pos = BlocksHelper.get_block_pos(x, y, z)
```


### get_block_entity(x:, y: int|float|None = None, z: int|float|None = None) -> JavaObject:

Create a Minecraft `net.minecraft.core.BlockPos` Java object from a position or coordinates.

Accepted formats:
- `x, y, z`: Individual numeric coordinates (float or int)
- `Vector3f`/`BlockPos`  `tuple` or `list`: e.g. `[x, y, z]` or `(x, y, z)` passed into x and y/z are left to None
- `JavaObject` of `net.minecraft.core.BlockPos` passed into x and y/z are left to None

All float values are automatically converted to integers, they are simply allowed for compatability purposes


```
targeted_block_pos = player_get_targeted_block()
if targeted_block_pos is not None:
    x, y, z = targeted_block_pos.position
    
    block_pos = BlocksHelper.get_block_pos(x, y, z)
    block_entity = BlocksHelper.get_block_entity(block_pos)

    # Or simply
    block_entity = BlocksHelper.get_block_entity(x, y, z)

    if block_entity is not null:
        print(UtilHelper.get_class_name(block_entity)) -> net.minecraft.world.level.block.entity.CommandBlockEntity      
```

### set_command_block_entity_command(command_block_entity: JavaObject, command: str) -> bool
### get_command_block_entity_command(command_block_entity: JavaObject) -> str | None

```
block_entity = ... # See previous example
if UtilHelper.get_class_name(command_block_entity) == "net.minecraft.world.level.block.entity.
    print(BlocksHelper.get_command_block_entity_command(block_entity)) # -> setblock ~ ~10 ~ minecraft:redstone_block
    print(BlocksHelper.get_command_block_entity_command(block_entity)) # -> [@: Changed the block at 163, 94, 125]
```

### get_command_block_entity_last_output(command_block_entity: JavaObject) -> str | None
### get_command_block_entity_mode(command_block_entity: JavaObject) -> str | None

Returns SEQUENCE or AUTO or REDSTONE
(Sequence being the CHAIN Command Block)

### is_command_block_entity_conditions_met(command_block_entity: JavaObject) -> bool | Non
### is_command_block_entity_powered(command_block_entity: JavaObject) -> bool | None
### is_command_block_entity_automatic(command_block_entity: JavaObject) -> bool | None
### get_spawner_block_entity_display_entity_id(jukebox_block_entity: spawner_block_entity) -> str | None

## ItemsHelper

> [!NOTE] 
> NOTE YOU CANT PASS minescript.ItemStack instances, these ARE DATA OBJECTS

Static helper class for working with items and item stacks. All methods accept item references in multiple formats:
- `JavaObject`: Direct Item or ItemStack objects
- `str`: Item ID (e.g., `"minecraft:diamond_sword"`, `"fishing_rod"`)
- `int`: Numeric registry ID (e.g., `69`)

### get_json(item) -> str
Get the full serialized item stack as a JSON string

```python
item = ContainerHelper.get_item_stack_by_inventory_slot(0)
if item:
    json_str = ItemsHelper.get_json(item)
    print(json_str)
    # -> '{"id":"minecraft:iron_sword","count":1,"components":{"minecraft:enchantments":{"minecraft:unbreaking":3,"minecraft:mending":1,"minecraft:sharpness":5},"minecraft:custom_name":"test"}}'
```

### get_components(item) -> str
Get only the `components` field from an item stack as a JSON string.

```python
item = ContainerHelper.get_item_stack_by_inventory_slot(0)
if item:
    components_str = ItemsHelper.get_components(item) # -> '{"minecraft:enchantments":{"minecraft:unbreaking":3,"minecraft:mending":1,"minecraft:sharpness":5},"minecraft:custom_name":"test"}'
    components_json = json.loads(components_str)
        enchantments = components_json.get("minecraft:enchantments", {})
    print(enchantments)  # -> {"minecraft:enchantments":{"minecraft:unbreaking":3,"minecraft:mending":1,"minecraft:sharpness":5},"minecraft:custom_name":"test"}
```

### get_item_id(item) -> str | None
Get the item ID (namespace identifier) for an item.

```python
ItemsHelper.get_item_id("diamond_sword")  # -> "minecraft:diamond_sword"
ItemsHelper.get_item_id(69)  # -> "minecraft:item_id_69"
```

### get_numeric_id(item) -> int
Get the numeric registry ID for an item.

```python
ItemsHelper.get_numeric_id("diamond_sword")  # -> 69
```

### get_display_name(item, use_custom_name=False) -> str | None
Get the display name of an item or item stack.

Args:
- `use_custom_name` (bool): If `True`, returns the custom hover name (e.g., from an anvil). If `False`, returns the default display name.

```python
item = ContainerHelper.get_item_stack_by_inventory_slot(0)
if item:
    print(ItemsHelper.get_display_name(item))  # -> "Diamond Sword"
    print(ItemsHelper.get_display_name(item, use_custom_name=True))  # -> "Blade of Destiny" (if renamed)
```

### get_count(item) -> int
### get_max_stack_size(item) -> int

### get_item_stack_java_object(item) -> JavaObject
Get the underlying ItemStack JavaObject (`net.minecraft.world.item.ItemStack`).

```python
java_stack = ItemsHelper.get_item_stack_java_object("diamond_sword")
# Now you can call Java methods directly on it
count = java_stack.getCount()
```

### get_item_java_object(item) -> JavaObject
Get the underlying Item JavaObject (`net.minecraft.world.item.Item`).

```python
java_item = ItemsHelper.get_item_java_object("diamond_sword")
```

---

## ContainerHelper

### crafting_get_layout() -> CraftingLayout
Returns the active crafting layout object for the current container.

Returns: `CraftingLayout` object with:
- `container_name` (str): Mapped runtime container class name
- `grid_slots` (list[int]): List of valid crafting slot IDs
- `grid_size` (int): Length of `grid_slots`
- `result_slot` (int): Slot ID containing crafting output

```python
layout = ContainerHelper.crafting_get_layout()
print(layout.grid_size)  # -> 4, 9, or 0 if crafting unsupported
print(layout.result_slot)  # -> slot ID for result
```

### crafting_get_grid_size() -> int
Get crafting grid size for the current layout.

Returns: `4` (2x2 inventory crafting), `9` (3x3 crafting table), or `0` if crafting unsupported.

```python
grid_size = ContainerHelper.crafting_get_grid_size()
if grid_size > 0:
    print(f"Crafting grid: {grid_size} slots")
```

### crafting_place_slot(slot, crafting_slot, count=1) -> ItemStack | bool | None
Place items from inventory `slot` into `crafting_slot`. Repeats for specified `count`.

Args:
- `slot` (int): Inventory/container slot to take from
- `crafting_slot` (int): Crafting grid slot to place into
- `count` (int): Number of items to place (default 1)

Returns:
- `ItemStack`: ItemStack
- `False`: Layout unsupported, invalid slot, invalid count, or click failed
- `None`: Result slot is empty after placement

```python
result = ContainerHelper.crafting_place_slot(15, 4, 2)
if result and result is not False:
    print(f"Crafted: {result.name}")
elif result is False:
    print("Crafting failed")
else:
    print("No result")
```

### crafting_shift_click_result() -> ItemStack | bool | None
Shift-click the current crafting result slot.

Returns:
- `ItemStack`: ItemStack from result slot before click
- `None`: Result slot was empty
- `False`: Layout unsupported or click failed

### get_container_id() -> int
Get the current container ID. Returns `-1` if no container open.

```python
container_id = ContainerHelper.get_container_id()
```

### get_container_class_name() -> str
Get the runtime mapped class name of the current container.

```python
class_name = ContainerHelper.get_container_class_name()
if class_name == "net.minecraft.world.inventory.CraftingMenu":
    print("Crafting table open")
```

### get_container_slot(slot) -> ItemStack | None
Get the item stack at a container slot.

```python
item = ContainerHelper.get_container_slot(0)
print(item.item)
```

### get_inventory_slot(slot) -> ItemStack | None
Get the item stack at an inventory slot

```python
hotbar_item = ContainerHelper.get_inventory_slot(27)
```

### get_item_stack_by_inventory_slot(slot) -> JavaObject | None
Alias for `get_inventory_slot()`.

```python
item = ContainerHelper.get_item_stack_by_inventory_slot(0)
if item:
    print(ItemsHelper.get_count(item))
```

### get_item_stack_by_container_slot(slot) -> JavaObject | None
Alias for `get_container_slot()`.

### container_find_item_id(item_id) -> list[JavaObject]
Find all item stacks in container matching the given item ID.

```python
diamonds = ContainerHelper.container_find_item_id("minecraft:diamond")
for stack in diamonds:
    print(ItemsHelper.get_count(stack))
```

### inventory_find_item_id(item_id) -> list[ItemStack]
Find all item stacks in inventory matching the given item ID.

```python
swords = ContainerHelper.inventory_find_item_id("diamond_sword")
```

### get_inventory_free_slot() -> int | None
Get the first empty slot in inventory. Returns `None` if inventory full.

```python
free_slot = ContainerHelper.get_inventory_free_slot()
if free_slot is not None:
    print(f"Free slot: {free_slot}")
```

### get_inventory_selected_hotbar_slot() -> int
Get the currently selected hotbar slot (0-8).

```python
selected = ContainerHelper.get_inventory_selected_hotbar_slot()
print(f"Selected hotbar slot: {selected}")
```

### raw_click(slot, button_or_slot=0, click_type=None) -> bool
Raw click operation on a slot. For advanced container manipulation.

Args:
- `slot` (int): Slot to click
- `button_or_slot` (int): Mouse button (0=left, 1=right) or drag slot / slot_b
- `click_type` (str|JavaObject): Click type (PICKUP, QUICK_MOVE, SWAP, CLONE, THROW, QUICK_CRAFT, PICKUP_ALL)

Returns: `True` if click succeeded, `False` otherwise

### click_slot(slot, button=0) -> bool
Click a slot with left (0) or right (1) mouse button.

```python
if ContainerHelper.click_slot(15, button=0):
    print("Clicked slot 15")
```

### shift_click_slot(slot) -> bool
Shift-click a slot (quick move).


### click_swap_with_hotbar(slot, hotbar_slot) -> bool
### pickup_swap_container(slot_a, slot_b) -> bool

---

## FishingHelper

### is_holding_rod() -> bool
Check if player is holding a fishing rod.

```python
if FishingHelper.is_holding_rod():
    print("Fishing rod equipped")
```

### is_casted() -> bool
```python
if FishingHelper.is_casted():
    print("Line is cast")
```

### is_biting() -> bool | None
Check if a fish is biting. Returns `None` if no hook in water.

```python
biting = FishingHelper.is_biting()
if biting:
    print("Fish biting!")
elif biting is None:
    print("No hook in water")
```

### is_open_water() -> bool | None
### get_hooked_entity() -> JavaObject | None
```python
entity = FishingHelper.get_hooked_entity()
if entity:
    print(f"Hooked: {type(entity)}")
```

### get_time_until_lured() -> int | None
Get ticks until a fish is lured. Returns `None` if no hook in water.

```python
ticks = FishingHelper.get_time_until_lured()
if ticks:
    print(f"Fish lured in {ticks} ticks")
```

### get_time_until_hooked() -> int | None
Get ticks until a fish is hooked (after being lured). Returns `None` if no hook in water.

```python
ticks = FishingHelper.get_time_until_hooked()
```

### use_rod() -> bool

---

## ClientHelper

### get_current_screen() -> JavaObject | None

### get_current_screen_class_name() -> str
### set_current_screen(screen) -> None
Open a screen.

```python
screen = JavaClass("net.minecraft.client.gui.screens.PauseScreen")()
ClientHelper.set_current_screen(screen)
```

### close_current_screen(with_close_container_packet=True) -> None
Close the current screen.

Args:
- `with_close_container_packet` (bool): If `True`, sends close container packet to server (default)

```python
ClientHelper.close_current_screen()
```

### open_pause_screen() -> None
### open_inventory_screen() -> None
### disconnect(reason="Disconnected by Minescript") -> None
### get_fps() -> int

### get_camera_position() -> Vector3f

```python
pos = ClientHelper.get_camera_position()
x = pos.x()
y = pos.y()
z = pos.z()
```

### get_camera_type() -> str
Get the current camera type: `"FIRST_PERSON"`, `"THIRD_PERSON_BACK"`, or `"THIRD_PERSON_FRONT"`.

```python
camera_type = ClientHelper.get_camera_type()
```

### get_level_data() -> ClientLevelData

#### ClientLevelData
Object containing level metadata:
- `difficulty` (int): Difficulty level (0-3)
- `daytime` (int): Current day time (0-24000)
- `game_time` (int): Total game time in ticks

---

## MappingsHelper


### get_runtime_class_name(pretty_class_name) -> str
Resolve a mapped (readable) class name to the actual runtime class name.

```python
runtime_name = MappingsHelper.get_runtime_class_name("net.minecraft.client.Minecraft")
```

### get_pretty_class_name(runtime_class_name) -> str
Resolve a runtime class name to the mapped (readable) class name.

```python
pretty_name = MappingsHelper.get_pretty_class_name("net.minecraft.class_310")
```

### get_runtime_field_name(clazz, pretty_field_name) -> str
### get_pretty_field_names(clazz) -> JavaSet[str]
### get_runtime_method_names(clazz, pretty_method_name) -> JavaSet[str]
### get_pretty_method_names(clazz) -> JavaSet[str]

---

## ReflectionHelper

### get_private_field(clazz, pretty_field_name) -> Any

---

## UtilHelper

Static utility helper class for miscellaneous operations.

### get_class_name(obj) -> str
Get the mapped (readable) class name of a Java object.

```python
item = ContainerHelper.get_inventory_slot(0)
if item:
    class_name = UtilHelper.get_class_name(item)
    # -> "net.minecraft.world.item.ItemStack"
```

### get_clipboard() -> str
Get the current clipboard contents.

```python
text = UtilHelper.get_clipboard()
```

### set_clipboard(text) -> None
Set the clipboard contents.

```python
UtilHelper.set_clipboard("Hello, World!")
```

## RegistryHelper

### get_by_id(registry: JavaObject, identifier: str) -> JavaObject
```
RegistryHelper.get_by_id(RegistryHelper.BuiltInRegistries.ITEM, "diamond") # -> net.minecraft.world.item.Item
```

### get_by_id(registry: JavaObject, identifier: str) -> JavaObject
```
item_instance = ...
RegistryHelper.get_registry_path(RegistryHelper.BuiltInRegistries.ITEM, item_instance) # -> diamond_sword
```
