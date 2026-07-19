from typing import TYPE_CHECKING
from code.Proxy import PyJinnProxy, PyJinnProxyMeta

PyJinnProxyMeta.bind_script("library.pyj")

if TYPE_CHECKING:
  from code.type_checking import ContainerHelper, GLFWHelper, WindowHelper, MappingsHelper, FishingHelper, UtilHelper, ClientHelper, ItemsHelper, BlocksHelper
else:
  class MappingsHelper(PyJinnProxy):
    pass

  def _resolve_slot_indexes(container):
    if container is None:
      return []
    
    return list(range(container.slots.size()))

  class ContainerHelper(PyJinnProxy):
    @staticmethod
    def get_container_layout():
      runtime_helper = PyJinnProxyMeta._pyj_class(ContainerHelper)
      container = runtime_helper._get_container()

      if container is None:
        return None

      container_name = runtime_helper.get_container_class_name()
      if container_name == "net.minecraft.world.inventory.InventoryMenu":
        return CraftingInventoryLayout(container_name, layouts={
          "crafting_grid": [1, 2, 3, 4],
          "result": [0],
          "inventory": list(range(9, 44+1)),
        })
      elif container_name == "net.minecraft.world.inventory.CrafterMenu":
        return CraftingInventoryLayout(container_name, layouts={
          "crafting_grid": list(range(0, 8+1)),
          "result": [45],
          "inventory": list(range(9, 44+1)),
        })
      elif container_name == "net.minecraft.world.inventory.CraftingMenu":
        return CraftingInventoryLayout(container_name, layouts={
          "crafting_grid": list(range(1, 9+1)),
          "result": [0],
          "inventory": list(range(10, 45+1)),
        })
      elif container_name == "net.minecraft.world.inventory.AnvilMenu":
        return AnvilLayout(container_name)
      elif container_name == "net.minecraft.world.inventory.EnchantmentMenu":
        return EnchantmentLayout(container_name)

      return DefaultContainerLayout(container_name, layouts={"slots": _resolve_slot_indexes(container)})

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
  def __init__(self, container_name, layouts=None):
    super().__init__(container_name, layouts)

  def get_inventory_slots(self):
    return self.get_group("inventory")

  def get_crafting_slots(self):
    return self.get_group("crafting_grid")

  def get_result_slot(self):
    return self.get_group("result")[0]

class AnvilLayout(CraftingInventoryLayout):
  def __init__(self, container_name):
    super().__init__(container_name, {
      "combine_grid": [0, 1],
      "result": [2],
      "inventory": list(range(3, 38+1)),
    })

class EnchantmentLayout(CraftingInventoryLayout):
  def __init__(self, container_name):
    super().__init__(container_name, {
      "enchantment_grid": [0],
      "lapis_grid": [1],
      "inventory": list(range(2, 37+1)),
    })