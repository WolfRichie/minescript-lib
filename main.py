from typing import TYPE_CHECKING
from code.Proxy import PyJinnProxy
from minescript import container_get_items

PyJinnProxy.bind_script("library.pyj")

if TYPE_CHECKING:
  from code.type_checking import StatisticsHelper, ScoreboardHelper, XaeroHelper, WidgetScreenHelper, ScreenHelper, BookScreenHelper, ContainerHelper, GLFWHelper, WindowHelper, MappingsHelper, FishingHelper, UtilHelper, ClientHelper, ItemsHelper, BlocksHelper, MerchantHelper, PlayerHelper, RegistryHelper
else:
  XaeroHelper = PyJinnProxy("XaeroHelper")
  RegistryHelper = PyJinnProxy("RegistryHelper")
  BookScreenHelper = PyJinnProxy("BookScreenHelper")
  PlayerHelper = PyJinnProxy("PlayerHelper")
  MappingsHelper = PyJinnProxy("MappingsHelper")
  MerchantHelper = PyJinnProxy("MerchantHelper")
  ScoreboardHelper = PyJinnProxy("ScoreboardHelper")
  ContainerHelper = PyJinnProxy("ContainerHelper")
  
  # To avoid overwriting proxy dynamically at runtime we can just inject a method
  def get_container_layout():
    runtime_helper = ContainerHelper._pyj_class()
    container = runtime_helper.get_container()
    if container is None:
      return None

    total_slots = container.slots.size()

    container_name = runtime_helper.get_container_class_name()
    if container_name == CraftingInventoryLayout.INVENTORY_MENU_NAME:
      return CraftingInventoryLayout(
        container_name,
        crafting_grid=[1, 2, 3, 4],
        result=[0],
        inventory_grid=list(range(9, 44+1)),
      )
    elif container_name == CraftingInventoryLayout.CRAFTER_MENU_NAME:
      return CraftingInventoryLayout(
        container_name,
        crafting_grid=list(range(0, 8+1)),
        result=[45],
        inventory_grid=list(range(9, 44+1)),
      )
    elif container_name == CraftingInventoryLayout.CRAFTING_MENU_NAME:
      return CraftingInventoryLayout(
        container_name,
        crafting_grid=list(range(1, 9+1)),
        result=[0],
        inventory_grid=list(range(10, 45+1)),
      )
    elif (container_name == ChestLayout.CHEST_MENU_NAME or 
          container_name == ChestLayout.SHULKER_BOX_MENU_NAME):
      if total_slots >= 45 and (total_slots - 36) % 9 == 0:
          return ChestLayout(
              container_name,
              chest_slots=total_slots - 36
          )
    elif container_name == BrewingStandLayout.BREWING_STAND_MENU_NAME:
      return BrewingStandLayout()
    elif container_name == AnvilLayout.ANVIL_MENU_NAME:
      return AnvilLayout()
    elif container_name == EnchantmentLayout.ENCHANTMENT_MENU_NAME:
      return EnchantmentLayout()
    elif container_name == MerchantLayout.MERCHANT_MENU_NAME:
      return MerchantLayout()
    elif container_name == GrindstoneLayout.GRINDSTONE_MENU_NAME:
      return GrindstoneLayout()
    elif container_name == BeaconLayout.BEACON_MENU_NAME:
      return BeaconLayout()
    return DefaultContainerLayout(container_name, layouts={"slots":list(range(total_slots))})
  
  ContainerHelper.get_container_layout = get_container_layout

  def container_get_items_excluding_inventory():
    container_layout = ContainerHelper.get_container_layout()
    if container_layout is None:
        return []
    
    if isinstance(container_layout, InventoryLayout):
        inventory_grid = container_layout.get_inventory_slots()
        items = container_get_items()
        return [item for item in items if item.slot not in inventory_grid]
    return container_get_items()
  
  ContainerHelper.container_get_items_excluding_inventory = container_get_items_excluding_inventory

  FishingHelper = PyJinnProxy("FishingHelper")
  ScreenHelper = PyJinnProxy("ScreenHelper")
  WidgetScreenHelper = PyJinnProxy("WidgetScreenHelper")
  ClientHelper = PyJinnProxy("ClientHelper")
  UtilHelper = PyJinnProxy("UtilHelper")
  ItemsHelper = PyJinnProxy("ItemsHelper")
  BlocksHelper = PyJinnProxy("BlocksHelper")
  GLFWHelper = PyJinnProxy("GLFWHelper")
  WindowHelper = PyJinnProxy("WindowHelper")
  StatisticsHelper = PyJinnProxy("StatisticsHelper")

class ContainerLayout:
  def __init__(self, container_name, layouts=None):
    self.container_name = container_name
    self.layouts = layouts if layouts is not None else {}

  @property
  def groups(self):
    return self.layouts

  @property
  def size(self):
    return sum(len(group_slots) for group_slots in self.layouts.values())

  @property
  def is_unknown(self) -> bool:
    return False

  def get_group(self, group_name):
    return self.layouts.get(group_name, [])

  def get_layouts(self):
    return self.layouts


class DefaultContainerLayout(ContainerLayout):
  def __init__(self, container_name, layouts):
    super().__init__(container_name, layouts)

  @property
  def is_unknown(self) -> bool:
    return True


class InventoryLayout(ContainerLayout):
  def get_inventory_slots(self):
    return self.get_group("inventory_grid")
  
class GrindstoneLayout(InventoryLayout):
  GRINDSTONE_MENU_NAME = "net.minecraft.world.inventory.GrindstoneMenu"
  def __init__(self):
    super().__init__(GrindstoneLayout.GRINDSTONE_MENU_NAME, {
      "repair_slots": [0, 1],
      "result": [2],
      "inventory_grid": list(range(3, 38+1)),
    })
    
  def get_repair_slots(self):
    return self.get_group("repair_slots")

  def get_result_slot(self):
    return self.get_group("result")[0]

class CraftingInventoryLayout(InventoryLayout):
    INVENTORY_MENU_NAME = "net.minecraft.world.inventory.InventoryMenu"
    CRAFTER_MENU_NAME = "net.minecraft.world.inventory.CrafterMenu"
    CRAFTING_MENU_NAME = "net.minecraft.world.inventory.CraftingMenu"

    def __init__(
        self,
        container_name,
        crafting_grid,
        result,
        inventory_grid,
    ):
        super().__init__(container_name, {
            "crafting_grid": crafting_grid,
            "result": result,
            "inventory_grid": inventory_grid,
        })

    def get_inventory_slots(self):
        return self.get_group("inventory_grid")

    def get_crafting_slots(self):
        return self.get_group("crafting_grid")

    def get_result_slot(self):
        return self.get_group("result")[0]

class AnvilLayout(InventoryLayout):
  ANVIL_MENU_NAME = "net.minecraft.world.inventory.AnvilMenu"
  def __init__(self):
    super().__init__(AnvilLayout.ANVIL_MENU_NAME, {
      "combine_grid": [0, 1],
      "result": [2],
      "inventory_grid": list(range(3, 38+1)),
    })
    
  def get_combine_slots(self):
    return self.get_group("combine_grid")
  
  def get_result_slot(self):
    return self.get_group("result")[0]

class EnchantmentLayout(InventoryLayout):
  ENCHANTMENT_MENU_NAME = "net.minecraft.world.inventory.EnchantmentMenu"
  def __init__(self):
    super().__init__(EnchantmentLayout.ENCHANTMENT_MENU_NAME, {
      "enchantment_grid": [0],
      "lapis_grid": [1],
      "inventory_grid": list(range(2, 37+1)),
    })
    
  def get_lapis_slot(self):
    return self.get_group("lapis_grid")[0]

  def get_enchantment_slot(self):
    return self.get_group("enchantment_grid")[0]
  
  
class ChestLayout(InventoryLayout):
  CHEST_MENU_NAME = "net.minecraft.world.inventory.ChestMenu"
  SHULKER_BOX_MENU_NAME = "net.minecraft.world.inventory.ShulkerBoxMenu"
  def __init__(self, container_name, chest_slots):
      super().__init__(container_name, {
          "chest": list(range(chest_slots)),
          "inventory_grid": list(range(chest_slots, chest_slots + 36)),
      })
      
  def get_chest_slots(self):
      return self.get_group("chest")
  
  
class BeaconLayout(InventoryLayout):
  BEACON_MENU_NAME = "net.minecraft.world.inventory.BeaconMenu"
  def __init__(self):
    super().__init__(BeaconLayout.BEACON_MENU_NAME, {
      "payment_slot": [0],
      "inventory_grid": list(range(1, 35+1)),
    })
  
  def get_payment_slot(self):
    return self.get_group("payment_slot")[0]
  
class BrewingStandLayout(InventoryLayout):
  BREWING_STAND_MENU_NAME = "net.minecraft.world.inventory.BrewingStandMenu"
  def __init__(self):
    super().__init__(BrewingStandLayout.BREWING_STAND_MENU_NAME, {
      "potions_grid": [0, 1, 2],
      "ingredient": [3],
      "blaze_powder": [4],
      "inventory_grid": list(range(5, 40+1)),
    })
    
  def get_potion_slots(self):
    return self.get_group("potions_grid")
  
  def get_ingredient_slot(self):
    return self.get_group("ingredient")[0]
  
  def get_blaze_powder_slot(self):
    return self.get_group("blaze_powder")[0]
  
class MerchantLayout(InventoryLayout):
  MERCHANT_MENU_NAME = "net.minecraft.world.inventory.MerchantMenu"
  def __init__(self):
    super().__init__(MerchantLayout.MERCHANT_MENU_NAME, {
      "cost_sell_grid": [0, 1],
      "result": [2],
      "inventory_grid": list(range(3, 38+1)),
    })
    
  def get_cost_sell_slots(self):
    return self.get_group("cost_sell_grid")

  def get_result_slot(self):
    return self.get_group("result")[0]
