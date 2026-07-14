from typing import TYPE_CHECKING
from code.Proxy import PyJinnProxy, PyJinnProxyMeta

PyJinnProxyMeta.bind_script("library.pyj")

if TYPE_CHECKING:
  from code.type_checking import ContainerHelper, MappingsHelper, FishingHelper, ItemsHelper
else:
  class MappingsHelper(PyJinnProxy):
    pass

  class ContainerHelper(PyJinnProxy):
    pass

  class FishingHelper(PyJinnProxy):
    pass

  class ItemsHelper(PyJinnProxy):
    pass

  class ClientHelper(PyJinnProxy):
    pass