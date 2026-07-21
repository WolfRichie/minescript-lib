from typing import TYPE_CHECKING
from code.Proxy import PyJinnProxy, PyJinnProxyMeta

PyJinnProxyMeta.bind_script("library.pyj")

if TYPE_CHECKING:
  from code.type_checking import BookScreenHelper, ContainerHelper, GLFWHelper, WindowHelper, MappingsHelper, FishingHelper, UtilHelper, ClientHelper, ItemsHelper, BlocksHelper, MerchantHelper
else:
  class BookScreenHelper(PyJinnProxy):
    pass
  
  class MappingsHelper(PyJinnProxy):
    pass
  class MerchantHelper(PyJinnProxy):
    pass

  class ContainerHelper(PyJinnProxy):
    @staticmethod
    def get_container_layout():
      runtime_helper = PyJinnProxyMeta._pyj_class(ContainerHelper)
      container = runtime_helper.get_container()

      if container is None:
        return None

      total_slots = container.slots.size()
      
      # todo move ContainerNames into class if not changing
      
      container_name = runtime_helper.get_container_class_name()
      if container_name == "net.minecraft.world.inventory.InventoryMenu":
        return CraftingInventoryLayout(
          container_name,
          crafting_grid=[1, 2, 3, 4],
          result=[0],
          inventory_grid=list(range(9, 44+1)),
        )
      elif container_name == "net.minecraft.world.inventory.CrafterMenu":
        return CraftingInventoryLayout(
          container_name,
          crafting_grid=list(range(0, 8+1)),
          result=[45],
          inventory_grid=list(range(9, 44+1)),
        )
      elif container_name == "net.minecraft.world.inventory.CraftingMenu":
        return CraftingInventoryLayout(
          container_name,
          crafting_grid=list(range(1, 9+1)),
          result=[0],
          inventory_grid=list(range(10, 45+1)),
        )
      elif container_name == "net.minecraft.world.inventory.ChestMenu":
        if total_slots >= 45 and (total_slots - 36) % 9 == 0:
            return ChestLayout(
                container_name,
                chest_slots=total_slots - 36
            )
      elif container_name == "net.minecraft.world.inventory.BrewingStandMenu":
        return BrewingStandLayout(container_name)
      elif container_name == "net.minecraft.world.inventory.AnvilMenu":
        return AnvilLayout(container_name)
      elif container_name == "net.minecraft.world.inventory.EnchantmentMenu":
        return EnchantmentLayout(container_name)
      elif container_name == "net.minecraft.world.inventory.MerchantMenu":
        return MerchantLayout(container_name)
      
      return DefaultContainerLayout(container_name, layouts={"slots":list(range(total_slots))})

  class FishingHelper(PyJinnProxy):
    pass

  class ClientHelper(PyJinnProxy):
    pass

  class UtilHelper(PyJinnProxy):
    pass

  class ItemsHelper(PyJinnProxy):
    pass

  class BlocksHelper(PyJinnProxy):
    pass

  class GLFWHelper(PyJinnProxy):
    pass

  class WindowHelper(PyJinnProxy):
    pass

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

class CraftingInventoryLayout(ContainerLayout):
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

class AnvilLayout(ContainerLayout):
  def __init__(self, container_name):
    super().__init__(container_name, {
      "combine_grid": [0, 1],
      "result": [2],
      "inventory_grid": list(range(3, 38+1)),
    })
    
    def get_combine_slots(self):
      return self.get_group("combine_grid")
    
    def get_result_slot(self):
      return self.get_group("result")[0]
    
    def get_inventory_slots(self):
      return self.get_group("inventory_grid")

class EnchantmentLayout(ContainerLayout):
  def __init__(self, container_name):
    super().__init__(container_name, {
      "enchantment_grid": [0],
      "lapis_grid": [1],
      "inventory_grid": list(range(2, 37+1)),
    })
    
  def get_lapis_slot(self):
    return self.get_group("lapis_grid")[0]

  def get_enchantment_slot(self):
    return self.get_group("enchantment_grid")[0]
  
  def get_inventory_slots(self):
    return self.get_group("inventory_grid")
  
  
class ChestLayout(ContainerLayout):
  def __init__(self, container_name, chest_slots):
      super().__init__(container_name, {
          "chest": list(range(chest_slots)),
          "inventory_grid": list(range(chest_slots, chest_slots + 36)),
      })
      
  def get_chest_slots(self):
      return self.get_group("chest")
    
  def get_inventory_slots(self):
      return self.get_group("inventory_grid")
      
class BrewingStandLayout(ContainerLayout):
  def __init__(self, container_name):
    super().__init__(container_name, {
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
  
  def get_inventory_slots(self):
    return self.get_group("inventory_grid")
  
class MerchantLayout(ContainerLayout):
  def __init__(self, container_name):
    super().__init__(container_name, {
      "cost_sell_grid": [0, 1],
      "result": [2],
      "inventory_grid": list(range(3, 38+1)),
    })
    
    def get_cost_sell_slots(self):
      return self.get_group("cost_sell_grid")
    
    def get_result_slot(self):
      return self.get_group("result")[0]
    
    def get_inventory_slots(self):
      return self.get_group("inventory_grid")
