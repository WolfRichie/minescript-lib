# Minescript Library

Developed in `Minecraft 1.21.11` using `minescript 5.0b11` with `Fabric API 0.141.4`

---

## Table of Contents

- [ItemsHelper](#itemshelper)
- [ContainerHelper](#containerhelper)
- [FishingHelper](#fishinghelper)
- [ClientHelper](#clienthelper)
- [MappingsHelper](#mappingshelper)
- [ReflectionHelper](#reflectionhelper)
- [UtilHelper](#utilhelper)

---

## ItemsHelper

Static helper class for working with items and item stacks. All methods accept item references in multiple formats:
- `JavaObject`: Direct Item or ItemStack objects
- `str`: Item ID (e.g., `"minecraft:diamond_sword"`, `"fishing_rod"`)
- `int`: Numeric registry ID (e.g., `69`)
NOTE YOU CANT PASS minescript.ItemStack instances, these ARE DATA OBJECTS

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
Get the stack count. Returns `1` for single items, actual count for item stacks.

```python
ItemsHelper.get_count("diamond_sword")  # -> 1
stack = ContainerHelper.get_item_stack_by_inventory_slot(0)
print(ItemsHelper.get_count(stack))  # -> actual stack size
```

### get_max_stack_size(item) -> int
Get the maximum stack size for an item.

```python
ItemsHelper.get_max_stack_size("dirt")  # -> 64
ItemsHelper.get_max_stack_size("diamond_sword")  # -> 1
```

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
Get only the `components` field from an item stack as a JSON string. Use this to access enchantments, custom names, and other component data without the full item stack wrapper.

```python
item = ContainerHelper.get_item_stack_by_inventory_slot(0)
if item:
    components_str = ItemsHelper.get_components(item) # -> '{"minecraft:enchantments":{"minecraft:unbreaking":3,"minecraft:mending":1,"minecraft:sharpness":5},"minecraft:custom_name":"test"}'
    components_json = json.loads(components_str)
        enchantments = components_json.get("minecraft:enchantments", {})
    print(enchantments)  # -> {"minecraft:enchantments":{"minecraft:unbreaking":3,"minecraft:mending":1,"minecraft:sharpness":5},"minecraft:custom_name":"test"}
```

---

## ContainerHelper

Static helper class for container/inventory operations.

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
- `button_or_slot` (int): Mouse button (0=left, 1=right) or drag slot
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

```python
ContainerHelper.shift_click_slot(15)  # Quick move slot 15
```

### click_swap_with_hotbar(slot, hotbar_slot) -> bool
Swap item in slot with item in hotbar (number key press).

```python
# Swap slot 15 with hotbar slot 0 (key 1)
ContainerHelper.click_swap_with_hotbar(15, 0)
```

### pickup_swap_container(slot_a, slot_b) -> bool
Swap items between two slots using pickup/place operations.

```python
ContainerHelper.pickup_swap_container(15, 16)
```

---

## FishingHelper

Static helper class for fishing operations.

### is_holding_rod() -> bool
Check if player is holding a fishing rod.

```python
if FishingHelper.is_holding_rod():
    print("Fishing rod equipped")
```

### is_casted() -> bool
Check if fishing line is cast (hook in water).

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
Check if hook is in open water. Returns `None` if no hook in water.

```python
if FishingHelper.is_open_water():
    print("In open water")
```

### get_hooked_entity() -> JavaObject | None
Get the entity (fish or player) hooked by the fishing line, if any.

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
Use the fishing rod (cast or reel in).

```python
if FishingHelper.use_rod():
    print("Rod action successful")
```

---

## ClientHelper

Static helper class for client screen and connection operations.

### get_current_screen() -> JavaObject | None
Get the current open screen. Returns `None` if no screen open.

```python
screen = ClientHelper.get_current_screen()
if screen:
    print(f"Screen open: {ClientHelper.get_current_screen_class_name()}")
```

### get_current_screen_class_name() -> str
Get the mapped class name of the current screen.

```python
class_name = ClientHelper.get_current_screen_class_name()
if "Inventory" in class_name:
    print("Inventory screen open")
```

### set_current_screen(screen) -> None
Open a screen.

```python
screen = JavaClass("net.minecraft.client.gui.screens.PauseScreen").constructor(False)(False)
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
Open the pause menu.

```python
ClientHelper.open_pause_screen()
```

### open_inventory_screen() -> None
Open the inventory screen.

```python
ClientHelper.open_inventory_screen()
```

### disconnect(reason="Disconnected by Minescript") -> None
Disconnect from server.

```python
ClientHelper.disconnect("Leaving")
```

### get_fps() -> int
Get current FPS.

```python
fps = ClientHelper.get_fps()
print(f"FPS: {fps}")
```

### get_camera_position() -> JavaObject
Get the camera position as a `Vector3f` JavaObject.

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
Get current level/world data. Returns `ClientLevelData` object or `None` if no level loaded.

```python
level = ClientHelper.get_level_data()
if level:
    print(f"Difficulty: {level.difficulty}")
    print(f"Day time: {level.daytime}")
```

#### ClientLevelData
Object containing level metadata:
- `difficulty` (int): Difficulty level (0-3)
- `daytime` (int): Current day time (0-24000)
- `game_time` (int): Total game time in ticks

---

## MappingsHelper

Static helper class for working with Minecraft's name mappings (deobfuscation).

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
Resolve a mapped field name to the runtime field name for a class.

```python
runtime_field = MappingsHelper.get_runtime_field_name(
    minecraft.player.getClass(), 
    "containerMenu"
)
```

### get_pretty_field_names(clazz) -> JavaSet[str]
Get all mapped field names for a class.

```python
fields = MappingsHelper.get_pretty_field_names(minecraft.player.getClass())
for field in fields:
    print(field)
```

### get_runtime_method_names(clazz, pretty_method_name) -> JavaSet[str]
Resolve a mapped method name to runtime method names for a class.

```python
methods = MappingsHelper.get_runtime_method_names(
    minecraft.player.getClass(), 
    "getInventory"
)
```

### get_pretty_method_names(clazz) -> JavaSet[str]
Get all mapped method names for a class.

```python
methods = MappingsHelper.get_pretty_method_names(minecraft.player.getClass())
```

---

## ReflectionHelper

Static helper class for Java reflection operations.

### get_private_field(clazz, pretty_field_name) -> Any
Get a private field value from a class instance using reflection.

```python
container_menu = ReflectionHelper.get_private_field(
    minecraft.player,
    "containerMenu"
)
```

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

---

## Example Usage

```python
from library.pyj import *

def on_item_taken(event):
    """Event handler when item is taken from container."""
    # Get the item that was taken
    item = ContainerHelper.get_item_stack_by_inventory_slot(27)
    
    if item:
        # Get basic item info
        item_id = ItemsHelper.get_item_id(item)
        count = ItemsHelper.get_count(item)
        display_name = ItemsHelper.get_display_name(item)
        
        print(f"Took {count}x {display_name} ({item_id})")
        
        # Get components (enchantments, custom name, etc.)
        components_str = ItemsHelper.get_components(item)
        components = json.loads(components_str)
        
        # Check for enchantments
        enchantments = components.get("minecraft:enchantments", {})
        for ench_id, ench_level in enchantments.items():
            print(f"  - {ench_id}: {ench_level}")
        
        # Check for custom name
        custom_name = components.get("minecraft:custom_name")
        if custom_name:
            print(f"  Custom name: {custom_name}")
```

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
    - [get\_inventory\_selected\_hotbar\_slot() -\> int](#get_inventory_selected_hotbar_slot---int)
    - [get\_inventory\_free\_slot() -\> int | None](#get_inventory_free_slot---int--none)
  - [`ReflectionHelper`](#reflectionhelper)
    - [get\_private\_field(clazz: JavaClass, pretty\_field\_name: str) -\> Any](#get_private_fieldclazz-javaclass-pretty_field_name-str---any)
  - [`ClientHelper`](#clienthelper)
    - [set\_current\_screen(screen: JavaObject) -\> None:](#set_current_screenscreen-javaobject---none)
    - [get\_current\_screen() -\> JavaObject | None](#get_current_screen---javaobject--none)
    - [get\_current\_screen\_class\_name() -\> str](#get_current_screen_class_name---str)
    - [close\_current\_screen(with\_close\_container\_packet: bool = True) -\> None](#close_current_screenwith_close_container_packet-bool--true---none)
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

Developed in `Minecraft 1.12.11` `minescript 5.0b11` using `Fabric API 0.141.4`